# -*- coding: utf-8 -*-
"""Desmit dizaina varianti izvēlei - visi ar īsto saturu.

Katrs variants lieto vienu un to pašu HTML struktūru (SRP: šis modulis
atbild tikai par izskata izmēģināšanu) - atšķiras tikai stils. Tāpēc, kad
variants izvēlēts, pietiek pārnest tā CSS uz site_index.py, un visa vietne
izskatās tāpat.

Datus lasa site_index.scan_course - mapes tiek apstaigātas vienu reizi un
tikai vienā vietā visā projektā (DRY).

Lietošana:
    python design_previews.py       # uzbūvē C:/aphysics/aphizika
"""

import os
import shutil
import sys

from courses import LESSONS_LEAD, SITE_LEAD, SITE_ROOT, SITE_TITLE, ordered
from site_index import (course_stats, esc, plural, scan_course, split_number)

OUT = os.path.join(SITE_ROOT, "aphizika")


# ------------------------------------------------------- kopīgais skelets
# Izkārtojums, atstarpes un responsivitāte visiem variantiem ir vienādi;
# variants maina tikai mainīgos un dažas savas rindas.
COMMON = """
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);
     font-family:var(--font);line-height:1.45}
a{color:inherit;text-decoration:none}
.wrap{max-width:60rem;margin:0 auto;padding:0 1rem 3.5rem}

header{padding:1.6rem 0 1rem}
h1{margin:0;font-family:var(--font-h);font-weight:var(--h-weight);
   font-size:clamp(1.35rem,5vw,2.1rem);letter-spacing:var(--h-space)}
.lead{margin:.45rem 0 0;color:var(--dim);max-width:44rem;
      font-size:clamp(.85rem,3.4vw,1rem)}

.bar{display:flex;align-items:center;gap:.75rem;flex-wrap:wrap;
     padding:.8rem 0;position:sticky;top:0;z-index:10;
     background:var(--bg);border-bottom:1px solid var(--line)}
.back{color:var(--dim);padding:.3rem 0;font-size:clamp(.85rem,3.4vw,.95rem)}
.back:hover{color:var(--acc)}
.spacer{flex:1}
.toggle{background:var(--card);color:var(--fg);border:1px solid var(--line);
        border-radius:var(--r);padding:.45rem .8rem;cursor:pointer;
        font:inherit;font-size:clamp(.8rem,3.2vw,.9rem)}
.toggle:hover{background:var(--card2);border-color:var(--rule)}

.cards{display:grid;gap:.9rem;margin:1.6rem 0;
       grid-template-columns:repeat(auto-fit,minmax(18rem,1fr))}
.card{display:block;background:var(--card);border:1px solid var(--line);
      border-radius:var(--r);padding:1.3rem 1.2rem;
      transition:background .15s,border-color .15s,transform .15s}
.card:hover{background:var(--card2);border-color:var(--rule)}
.card-t{display:block;color:var(--acc);font-family:var(--font-h);
        font-weight:var(--h-weight);font-size:clamp(1.1rem,4.5vw,1.45rem)}
.card-s{display:block;margin-top:.3rem;color:var(--dim);
        font-size:clamp(.82rem,3.3vw,.95rem)}
.card-m{display:block;margin-top:.9rem;color:var(--dim);opacity:.8;
        font-size:clamp(.75rem,3vw,.85rem)}

.theme{border-bottom:1px solid var(--line)}
.theme summary{display:flex;align-items:baseline;gap:.6rem;cursor:pointer;
               padding:.85rem .2rem;list-style:none;
               font-family:var(--font-h);font-weight:var(--h-weight);
               font-size:clamp(.95rem,3.8vw,1.15rem)}
.theme summary::-webkit-details-marker{display:none}
.theme summary:hover{color:var(--acc)}
.theme summary .n{flex:none;min-width:2.2rem;color:var(--acc);
                  font-family:var(--font-n)}
.theme summary .t{flex:1}
.theme summary .c{flex:none;color:var(--dim);font-size:.8em}
.theme summary::after{content:"";flex:none;width:.5rem;height:.5rem;
    margin-left:.2rem;transform:rotate(45deg);transition:transform .15s;
    border-right:2px solid var(--dim);border-bottom:2px solid var(--dim)}
.theme[open] summary{color:var(--acc)}
.theme[open] summary::after{transform:rotate(225deg)}

ul{list-style:none;margin:0;padding:0 0 1rem;display:grid;gap:.5rem;
   grid-template-columns:repeat(auto-fill,minmax(15rem,1fr))}
li a{display:flex;gap:.5rem;padding:.7rem .8rem;background:var(--card);
     border:1px solid var(--line);border-radius:var(--r);
     transition:background .15s,border-color .15s;
     font-size:clamp(.85rem,3.5vw,1rem)}
li a:hover{background:var(--card2);border-color:var(--rule)}
li a .n{flex:none;color:var(--acc);font-family:var(--font-n)}

.foot{margin-top:2.5rem;padding-top:1rem;border-top:1px solid var(--line);
      color:var(--dim);font-size:.85rem}
.foot a{color:var(--acc)}

@media (max-width:768px){ul{grid-template-columns:1fr}}
"""

G1 = "1. kārta"
G2 = "2. kārta - itāļu elegance, violets, violets+zils"

SANS = 'Calibri,"Segoe UI",system-ui,sans-serif'
SERIF = 'Cambria,Georgia,"Times New Roman",serif'
MONO = '"Cascadia Mono",Consolas,"Courier New",monospace'

# Tīmekļa fonti - ja interneta nav, paliek vietējā rezerve aiz komata.
INTER = '"Inter",' + SANS
POPPINS = '"Poppins","Inter",' + SANS
CORMORANT = '"Cormorant Garamond",' + SERIF
JOST = '"Jost","Century Gothic",' + SANS


def gfont(spec):
    """Google Fonts saite - lapa strādā arī bez tās, tikai ar rezerves fontu."""
    return ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
            '<link rel="preconnect" href="https://fonts.gstatic.com" '
            'crossorigin>\n<link rel="stylesheet" '
            'href="https://fonts.googleapis.com/css2?%s&amp;display=swap">\n'
            % spec)


def tokens(**kw):
    """Noklusētie mainīgie + varianta izmaiņas - lai neatkārtotu visu sarakstu."""
    t = {"font": SANS, "font-h": SANS, "font-n": SANS,
         "h-weight": "700", "h-space": "0", "r": ".45rem"}
    t.update({k.replace("_", "-"): v for k, v in kw.items()})
    return ":root{%s}" % ";".join("--%s:%s" % kv for kv in t.items())


# ------------------------------------------------------------- 10 varianti
THEMES = [
 {"slug": "01-nakts", "name": "Nakts",
  "note": "Tumši zils ar zeltu - tāds pats tonis kā stundu prezentācijām.",
  "css": tokens(bg="#0E1A2F", fg="#E7EEF7", dim="#9DC3E6", acc="#FFD966",
                card="#17294a", card2="#20355e", line="#24406e",
                rule="#2E75B6", r=".45rem") + """
.card{border-left:4px solid var(--rule)}
.card:hover{border-left-color:var(--acc)}
"""},

 {"slug": "02-tinte", "name": "Tinte",
  "note": "Gandrīz melns, tikai matu līnijas - nekādu aizpildījumu, daudz gaisa.",
  "css": tokens(bg="#0B0F14", fg="#E6EDF3", dim="#7D8A97", acc="#58C4DD",
                card="transparent", card2="#11161D", line="#1E262F",
                rule="#58C4DD", r="0", h_weight="600") + """
.wrap{max-width:56rem}
.card{border:0;border-top:2px solid var(--line);border-radius:0;
      padding:1.5rem .2rem}
.card:hover{border-top-color:var(--acc);background:transparent}
li a{border:0;border-bottom:1px solid var(--line);border-radius:0;
     padding:.65rem .2rem}
li a:hover{background:transparent;border-bottom-color:var(--acc);
           color:var(--acc)}
ul{gap:0}
.theme summary{padding:1rem .2rem}
"""},

 {"slug": "03-papirs", "name": "Papīrs",
  "note": "Gaišs, silts fons, serifa virsraksti - kā izdrukāts materiāls.",
  "css": tokens(bg="#F6F3EC", fg="#1F2A37", dim="#6B7280", acc="#8A5A2B",
                card="#FFFFFF", card2="#FFFDF8", line="#E2DDD2",
                rule="#C8A97E", r=".5rem", font_h=SERIF) + """
.card{box-shadow:0 1px 2px rgba(31,42,55,.06)}
.card:hover{box-shadow:0 4px 14px rgba(31,42,55,.10);transform:translateY(-1px)}
li a{box-shadow:0 1px 1px rgba(31,42,55,.04)}
h1{letter-spacing:-.01em}
"""},

 {"slug": "04-kontrasts", "name": "Kontrasts",
  "note": "Melns un balts, lieli numuri kā grafiskais elements, viens sarkans akcents.",
  "css": tokens(bg="#000000", fg="#FFFFFF", dim="#8A8A8A", acc="#FF3B30",
                card="#0A0A0A", card2="#141414", line="#2A2A2A",
                rule="#FF3B30", r="0", h_weight="800",
                h_space="-.02em") + """
.theme summary .n{font-size:1.6em;min-width:3.4rem;line-height:1;
                  color:var(--fg);opacity:.35}
.theme[open] summary .n,.theme summary:hover .n{color:var(--acc);opacity:1}
li a .n{opacity:.5;color:var(--fg)}
li a:hover .n{color:var(--acc);opacity:1}
.card{border-left:6px solid var(--acc)}
"""},

 {"slug": "05-grafits", "name": "Grafīts",
  "note": "Neitrāli pelēks, monospace numuri, blīvas rindas - daudz redzams uzreiz.",
  "css": tokens(bg="#16181D", fg="#E4E6EB", dim="#8B919C", acc="#7FB3FF",
                card="#1D2027", card2="#262A33", line="#2E323B",
                rule="#4A76B8", r=".3rem", font_n=MONO) + """
ul{grid-template-columns:1fr;gap:.2rem;padding-bottom:.8rem}
li a{padding:.45rem .6rem;border:0;border-left:2px solid transparent;
     border-radius:0;background:transparent}
li a:hover{background:var(--card);border-left-color:var(--acc)}
li a .n{min-width:3.2rem;font-size:.9em}
.theme summary{padding:.7rem .2rem}
.theme summary .n{font-size:.95em}
"""},

 {"slug": "06-krits", "name": "Krīts",
  "note": "Tāfeles zaļš ar krīta baltu - mīksts, silts, mazāk spilgts par nakti.",
  "css": tokens(bg="#1B2B26", fg="#EFEAE0", dim="#9BB3A6", acc="#F2D07B",
                card="#233630", card2="#2C443C", line="#334C43",
                rule="#6FA98F", r=".75rem") + """
.card{border-radius:1rem}
li a{border-radius:.75rem}
.theme{border-bottom-style:dashed}
.theme summary::after{border-width:2px}
"""},

 {"slug": "07-linija", "name": "Līnija",
  "note": "Gaišs, zilas malas pie katras rindas - kā burtnīcas līnijas.",
  "css": tokens(bg="#FFFFFF", fg="#16243B", dim="#5B7089", acc="#1D5FBF",
                card="#F7F9FC", card2="#EDF3FB", line="#DCE5F0",
                rule="#1D5FBF", r=".25rem") + """
.card{border-left:5px solid var(--acc)}
li a{border:0;border-left:3px solid var(--line);border-radius:0;
     background:transparent;padding:.55rem .7rem}
li a:hover{background:var(--card2);border-left-color:var(--acc)}
ul{gap:.25rem}
.theme{border-bottom-color:var(--line)}
.theme summary .n{font-variant-numeric:tabular-nums}
"""},

 {"slug": "08-flizes", "name": "Flīzes",
  "note": "Tumšs, bet stundas ir kvadrātiskas flīzes ar lielu numuru virsū.",
  "css": tokens(bg="#101826", fg="#E8EEF6", dim="#8FA3BC", acc="#5EEAD4",
                card="#18233A", card2="#1F2E4C", line="#243451",
                rule="#5EEAD4", r=".6rem") + """
ul{grid-template-columns:repeat(auto-fill,minmax(11rem,1fr));gap:.6rem}
li a{flex-direction:column;gap:.35rem;padding:.9rem .8rem;min-height:5.5rem}
li a .n{font-size:1.35rem;line-height:1}
li a:hover{transform:translateY(-2px)}
.card{border-radius:.9rem}
@media (max-width:768px){ul{grid-template-columns:repeat(2,1fr)}
  li a{min-height:4.5rem;font-size:.8rem}}
"""},

 {"slug": "09-klusums", "name": "Klusums",
  "note": "Gaišs un pilnīgi bez rāmjiem - tikai burti, atstarpes un pasvītrojums.",
  "css": tokens(bg="#FAFAF9", fg="#22262B", dim="#8A9099", acc="#166534",
                card="transparent", card2="transparent", line="#EBEAE7",
                rule="#166534", r="0", h_weight="600") + """
.wrap{max-width:52rem}
.card{border:0;border-radius:0;padding:1.2rem 0;
      border-bottom:1px solid var(--line)}
.card:hover{background:transparent;transform:none}
.card:hover .card-t{text-decoration:underline;text-underline-offset:.25em}
li a{border:0;border-radius:0;background:transparent;padding:.5rem 0}
li a:hover{background:transparent;color:var(--acc);
           text-decoration:underline;text-underline-offset:.2em}
ul{gap:.15rem;padding-bottom:1.2rem}
.theme{border-bottom-color:var(--line)}
.theme summary{padding:1rem .1rem}
"""},

 {"slug": "10-indigo", "name": "Indigo",
  "note": "Dziļš indigo ar gradienta joslu un apaļām pogām - mūsdienīgākais.",
  "css": tokens(bg="#0F1024", fg="#EAE8FF", dim="#9C97C8", acc="#C4B5FD",
                card="#1A1B3A", card2="#242557", line="#2C2D5C",
                rule="#7C6BF0", r="999px") + """
header{background:linear-gradient(135deg,#241C5E 0%,#0F1024 70%);
       margin:0 -1rem;padding:2rem 1rem 1.4rem}
.card{border-radius:1rem;
      background:linear-gradient(160deg,var(--card),#141530)}
.card:hover{border-color:var(--rule)}
li a{padding:.6rem 1rem}
.toggle{border-radius:999px}
.theme summary::after{border-color:var(--acc)}
"""},

 # ---- otrā kārta: itāļu elegance, violets, violets+zils (matematika) ----
 {"slug": "11-calcubo", "name": "Calcubo", "group": G2,
  "note": "Violets un zils tieši kā matematika projektā - indigo, violets, "
          "ciāns, dzintara akcents.",
  "fonts": gfont("family=Inter:wght@400;500&family=Poppins:wght@500;600"),
  "css": tokens(bg="#F7F8FC", fg="#374151", dim="#6B7280", acc="#4F46E5",
                card="#FFFFFF", card2="#F5F3FF", line="#E5E7EB",
                rule="#7C3AED", r="1rem", font=INTER, font_h=POPPINS,
                h_weight="600") + """
header{background:linear-gradient(135deg,#4F46E5 0%,#7C3AED 50%,#06B6D4 100%);
       margin:0 -1rem;padding:2.2rem 1rem 1.8rem;color:#fff;border-radius:0 0 1.5rem 1.5rem}
h1{color:#fff}
.lead{color:rgba(255,255,255,.85)}
.card{box-shadow:0 1px 3px rgba(0,0,0,.1),0 1px 2px rgba(0,0,0,.06);
      border-color:transparent}
.card:hover{transform:translateY(-3px);
            box-shadow:0 10px 15px -3px rgba(79,70,229,.18)}
.card-m{color:#F59E0B;opacity:1;font-weight:500}
li a{border-radius:.75rem;box-shadow:0 1px 2px rgba(0,0,0,.05)}
li a:hover{background:var(--card2);border-color:var(--rule);
           transform:translateY(-1px)}
.toggle{border-radius:50rem;background:var(--acc);color:#fff;border:0}
.toggle:hover{background:var(--rule)}
.theme summary .c{color:#06B6D4}
"""},

 {"slug": "12-calcubo-nakts", "name": "Calcubo nakts", "group": G2,
  "note": "Tā pati matematika projekta palete, bet uz tumša fona - der pie "
          "tagadējām prezentācijām.",
  "fonts": gfont("family=Inter:wght@400;500&family=Poppins:wght@500;600"),
  "css": tokens(bg="#0D0B21", fg="#E8E6F5", dim="#9B96C4", acc="#A78BFA",
                card="#171436", card2="#211D48",
                line="#2A2555", rule="#06B6D4", r="1rem",
                font=INTER, font_h=POPPINS, h_weight="600") + """
header{background:linear-gradient(135deg,#4F46E5 0%,#7C3AED 55%,#06B6D4 130%);
       margin:0 -1rem;padding:2.2rem 1rem 1.8rem;
       border-radius:0 0 1.5rem 1.5rem}
h1{color:#fff}
.lead{color:rgba(255,255,255,.85)}
.card:hover{transform:translateY(-3px);border-color:var(--acc)}
.card-m{color:#F59E0B;opacity:1}
li a{border-radius:.75rem}
.toggle{border-radius:50rem}
.theme summary .c{color:#06B6D4}
"""},

 {"slug": "13-violets", "name": "Violets", "group": G2,
  "note": "Tikai violets - dziļš purpurs ar gaiši lillā akcentiem, bez zila.",
  "css": tokens(bg="#150E24", fg="#EDE7F6", dim="#A99BC4", acc="#C4A2FF",
                card="#1F1636", card2="#2B1F4A",
                line="#332748", rule="#8B5CF6", r=".6rem") + """
.card{border-left:4px solid var(--rule)}
.card:hover{border-left-color:var(--acc)}
.theme summary .n{color:var(--rule)}
.theme[open] summary .n{color:var(--acc)}
li a:hover{box-shadow:0 0 0 1px var(--rule)}
"""},

 {"slug": "14-ametists", "name": "Ametists", "group": G2,
  "note": "Gaišs violets - balts fons, lillā tonis, viegls un tīrs.",
  "css": tokens(bg="#FCFAFF", fg="#2E1A47", dim="#7E6B96", acc="#6D28D9",
                card="#F6F1FE", card2="#EDE4FD", line="#E4DAF5",
                rule="#8B5CF6", r=".6rem") + """
.card{border-left:4px solid var(--rule)}
.card:hover{transform:translateY(-2px);
            box-shadow:0 8px 20px rgba(109,40,217,.10)}
li a{background:var(--card)}
.theme summary .c{color:var(--rule)}
"""},

 {"slug": "15-milana", "name": "Milāna", "group": G2,
  "note": "Itāļu zīmola elegance - ziloņkaula fons, plāns serifs, zelta "
          "matiņlīnija, daudz gaisa.",
  "fonts": gfont("family=Cormorant+Garamond:wght@300;400;500"
                 "&family=Jost:wght@300;400"),
  "css": tokens(bg="#F4F1EA", fg="#14110E", dim="#8A8175", acc="#A98B54",
                card="transparent", card2="#EFEBE1", line="#DDD6C7",
                rule="#A98B54", r="0", font=JOST, font_h=CORMORANT,
                h_weight="400", h_space=".01em") + """
.wrap{max-width:50rem;padding-bottom:5rem}
header{padding:3.5rem 0 2rem;text-align:center}
h1{font-size:clamp(1.9rem,7vw,3.2rem)}
.lead{margin:1rem auto 0;text-align:center;font-size:.9rem;
      letter-spacing:.04em}
.cards{gap:0;margin:2.5rem 0;grid-template-columns:1fr}
.card{border:0;border-top:1px solid var(--line);padding:2.2rem .2rem;
      text-align:center}
.card:last-child{border-bottom:1px solid var(--line)}
.card:hover{background:transparent}
.card-t{font-size:clamp(1.5rem,5.5vw,2.1rem);color:var(--fg)}
.card:hover .card-t{color:var(--acc)}
.card-s,.card-m{text-transform:uppercase;letter-spacing:.18em;
                font-size:.66rem;font-family:var(--font)}
.card-m{margin-top:.7rem;color:var(--acc);opacity:1}
.theme summary{padding:1.3rem .2rem;font-size:clamp(1.05rem,4vw,1.35rem)}
.theme summary .c{text-transform:uppercase;letter-spacing:.16em;
                  font-size:.6rem;font-family:var(--font)}
.theme summary::after{border-width:1px}
li a{border:0;border-radius:0;padding:.55rem 0;background:transparent;
     letter-spacing:.02em}
li a:hover{background:transparent;color:var(--acc)}
ul{gap:.1rem;padding-bottom:1.6rem}
.bar{border-bottom:1px solid var(--line)}
.back,.toggle{text-transform:uppercase;letter-spacing:.16em;font-size:.66rem}
.toggle{border:1px solid var(--line);background:transparent;padding:.6rem 1.1rem}
"""},

 {"slug": "16-firenze", "name": "Firenze", "group": G2,
  "note": "Tā pati itāļu elegance tumšā izpildījumā - espresso fons, zelts, "
          "serifs.",
  "fonts": gfont("family=Cormorant+Garamond:wght@300;400;500"
                 "&family=Jost:wght@300;400"),
  "css": tokens(bg="#17140F", fg="#EDE6D8", dim="#9A8F7C", acc="#C9A76A",
                card="transparent", card2="#1F1B15", line="#332D24",
                rule="#C9A76A", r="0", font=JOST, font_h=CORMORANT,
                h_weight="400") + """
.wrap{max-width:50rem;padding-bottom:5rem}
header{padding:3.5rem 0 2rem;text-align:center}
h1{font-size:clamp(1.9rem,7vw,3.2rem);color:var(--acc)}
.lead{margin:1rem auto 0;text-align:center;font-size:.9rem;
      letter-spacing:.04em}
.cards{gap:0;margin:2.5rem 0;grid-template-columns:1fr}
.card{border:0;border-top:1px solid var(--line);padding:2.2rem .2rem;
      text-align:center}
.card:last-child{border-bottom:1px solid var(--line)}
.card:hover{background:var(--card2)}
.card-t{font-size:clamp(1.5rem,5.5vw,2.1rem)}
.card-s,.card-m{text-transform:uppercase;letter-spacing:.18em;
                font-size:.66rem;font-family:var(--font)}
.theme summary{padding:1.3rem .2rem;font-size:clamp(1.05rem,4vw,1.35rem)}
.theme summary .c{text-transform:uppercase;letter-spacing:.16em;
                  font-size:.6rem;font-family:var(--font)}
li a{border:0;border-radius:0;padding:.55rem 0;background:transparent}
li a:hover{background:transparent;color:var(--acc)}
ul{gap:.1rem;padding-bottom:1.6rem}
.back,.toggle{text-transform:uppercase;letter-spacing:.16em;font-size:.66rem}
.toggle{border:1px solid var(--line);background:transparent;padding:.6rem 1.1rem}
"""},

 {"slug": "17-terrakota", "name": "Terrakota", "group": G2,
  "note": "Itāļu, bet siltāks - smilšu fons, terakotas akcents, mierīgs serifs.",
  "fonts": gfont("family=Cormorant+Garamond:wght@400;500&family=Jost:wght@400"),
  "css": tokens(bg="#FAF6F0", fg="#2A211B", dim="#8B7A6B", acc="#B4552D",
                card="#FFFFFF", card2="#FBEFE7", line="#E8DCD0",
                rule="#B4552D", r=".35rem", font=JOST, font_h=CORMORANT,
                h_weight="500") + """
h1{font-size:clamp(1.7rem,6vw,2.6rem)}
.card{border-top:3px solid var(--acc)}
.card:hover{transform:translateY(-2px);
            box-shadow:0 8px 18px rgba(180,85,45,.12)}
.card-s{text-transform:uppercase;letter-spacing:.14em;font-size:.68rem;
        font-family:var(--font)}
.theme summary .n{color:var(--acc)}
li a{background:var(--card)}
li a:hover{background:var(--card2)}
"""},

 {"slug": "18-safirs", "name": "Safīrs", "group": G2,
  "note": "Zils pamatā ar violetu akcentu - otrādi nekā Calcubo.",
  "css": tokens(bg="#0A1428", fg="#E3ECF9", dim="#8AA3C4", acc="#A78BFA",
                card="#12203C", card2="#1A2C4F",
                line="#213556", rule="#3B82F6", r=".5rem") + """
.card{border-left:4px solid var(--rule)}
.card:hover{border-left-color:var(--acc)}
.theme summary .n{color:var(--rule)}
.theme[open] summary .n{color:var(--acc)}
.theme summary .c{color:var(--acc)}
"""},

 {"slug": "19-aurora", "name": "Aurora", "group": G2,
  "note": "Tumšs ar violeta-zila gradienta svītrām un mīkstu mirdzumu.",
  "css": tokens(bg="#0B0A1A", fg="#E9E8F7", dim="#8F8CB8", acc="#B197FC",
                card="#141330", card2="#1C1B42", line="#242252",
                rule="#6366F1", r=".7rem") + """
header{position:relative}
header::after{content:"";display:block;height:3px;margin-top:1.2rem;
  background:linear-gradient(90deg,#6366F1,#A855F7,#06B6D4);border-radius:2px}
.card{position:relative;overflow:hidden}
.card::before{content:"";position:absolute;left:0;top:0;bottom:0;width:3px;
  background:linear-gradient(180deg,#6366F1,#A855F7,#06B6D4)}
.card:hover{box-shadow:0 0 24px rgba(99,102,241,.25);
            transform:translateY(-2px)}
li a:hover{box-shadow:0 0 14px rgba(177,151,252,.18)}
.theme summary .n{background:linear-gradient(90deg,#A855F7,#06B6D4);
  -webkit-background-clip:text;background-clip:text;color:transparent}
"""},

 {"slug": "20-marmors", "name": "Marmors", "group": G2,
  "note": "Itāļu marmors - gandrīz balts, melns serifs, zelta matiņlīnija.",
  "fonts": gfont("family=Cormorant+Garamond:wght@300;400;500"
                 "&family=Jost:wght@300;400"),
  "css": tokens(bg="#FBFBFA", fg="#1A1A18", dim="#8C8C86", acc="#8C7853",
                card="#FFFFFF", card2="#F4F3F0", line="#E6E5E0",
                rule="#8C7853", r="0", font=JOST, font_h=CORMORANT,
                h_weight="300", h_space=".02em") + """
body{background:linear-gradient(160deg,#FBFBFA 0%,#F2F1ED 55%,#FBFBFA 100%);
     background-attachment:fixed}
.wrap{max-width:54rem;padding-bottom:5rem}
header{padding:3rem 0 1.6rem}
h1{font-size:clamp(1.8rem,6.5vw,3rem)}
.lead{font-size:.9rem;letter-spacing:.03em}
.card{border:1px solid var(--line);padding:1.8rem 1.5rem}
.card:hover{border-color:var(--acc);background:var(--card)}
.card-t{color:var(--fg)}
.card:hover .card-t{color:var(--acc)}
.card-s,.card-m{text-transform:uppercase;letter-spacing:.16em;
                font-size:.66rem;font-family:var(--font)}
.theme summary{padding:1.15rem .2rem;font-size:clamp(1rem,4vw,1.3rem)}
.theme summary .c{text-transform:uppercase;letter-spacing:.14em;
                  font-size:.6rem;font-family:var(--font)}
li a{border:0;border-bottom:1px solid var(--line);border-radius:0;
     background:transparent;padding:.6rem .2rem}
li a:hover{background:var(--card2);color:var(--acc)}
ul{gap:0;padding-bottom:1.5rem}
.back,.toggle{text-transform:uppercase;letter-spacing:.14em;font-size:.66rem}
"""},
]


# ------------------------------------------------------------- attēlošana
PAGE = """<!DOCTYPE html>
<html lang="lv">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%(title)s</title>
%(fonts)s<style>%(common)s%(css)s</style>
</head>
<body>
<div class="wrap">
%(body)s
</div>
<script>%(js)s</script>
</body>
</html>
"""

JS = """
(function(){
  var b=document.getElementById("all");
  if(!b){return;}
  b.addEventListener("click",function(){
    var d=document.getElementsByTagName("details"),
        open=b.getAttribute("data-open")!=="1",i;
    for(i=0;i<d.length;i++){d[i].open=open;}
    b.setAttribute("data-open",open?"1":"0");
    b.textContent=open?"Sakļaut visu":"Izvērst visu";
  });
})();
"""


def page(theme, title, body):
    return PAGE % {"title": esc(title), "common": COMMON,
                   "css": theme["css"], "js": JS, "body": body,
                   "fonts": theme.get("fonts", "")}


def num_span(text):
    return '<span class="n">%s</span>' % esc(text) if text else ""


def head(title, lead):
    return ('<header>\n<h1>%s</h1>\n<p class="lead">%s</p>\n</header>'
            % (esc(title), esc(lead)))


def foot(theme, home):
    return ('<p class="foot">Dizains <b>%s</b> &#183; %s<br>'
            '<a href="%s">&#8592; Visi dizaina varianti</a></p>'
            % (esc(theme["name"]), esc(theme["note"]), home))


def render_theme(title, lessons, prefix):
    num, name = split_number(title)
    items = "\n".join(
        '  <li><a href="%s%s">%s<span>%s</span></a></li>'
        % (prefix, link, num_span(split_number(label)[0]),
           esc(split_number(label)[1]))
        for link, label in lessons)
    return ('<details class="theme">\n<summary>%s<span class="t">%s</span>'
            '<span class="c">%d</span></summary>\n<ul>\n%s\n</ul>\n</details>'
            % (num_span(num), esc(name), len(lessons), items))


def render_subject(theme, course):
    """Viena kursa lapa - stundu saites rāda uz īstajām prezentācijām."""
    prefix = "../../%s/" % os.path.basename(course["root"])
    bar = ('<div class="bar">\n<a class="back" href="index.html">'
           '&#8592; Sākums</a>\n<span class="spacer"></span>\n'
           '<button class="toggle" id="all" data-open="0" type="button">'
           'Izvērst visu</button>\n</div>')
    body = "\n".join(
        [head(course["title"], LESSONS_LEAD), bar]
        + [render_theme(t, ls, prefix)
           for t, ls in scan_course(course["root"])]
        + [foot(theme, "../index.html")])
    return page(theme, "%s · %s" % (course["title"], theme["name"]), body)


def render_home(theme, cards):
    body = "\n".join([head(SITE_TITLE, SITE_LEAD),
                      '<div class="cards">\n%s\n</div>' % "\n".join(cards),
                      foot(theme, "../index.html")])
    return page(theme, "%s · %s" % (SITE_TITLE, theme["name"]), body)


def render_card(course, page_name, n_themes, n_lessons):
    return ('<a class="card" href="%s">\n<span class="card-t">%s</span>\n'
            '<span class="card-s">%s</span>\n'
            '<span class="card-m">%s · %s</span>\n</a>'
            % (page_name, esc(course["label"]), esc(course["kicker"]),
               plural(n_themes, "temats", "temati", "tematu"),
               plural(n_lessons, "stunda", "stundas", "stundu")))


# -------------------------------------------------------------- rakstīšana
def write(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def page_name(slug):
    return "%s.html" % slug


def build_variant(theme, courses):
    """Viena varianta mape: sākumlapa + katra kursa saraksts."""
    folder = os.path.join(OUT, theme["slug"])
    os.makedirs(folder, exist_ok=True)
    cards = []
    for slug, course in courses:
        write(os.path.join(folder, page_name(slug)),
              render_subject(theme, course))
        cards.append(render_card(course, page_name(slug),
                                 *course_stats(course["root"])))
    return write(os.path.join(folder, "index.html"),
                 render_home(theme, cards))


GALLERY_CSS = THEMES[0]["css"] + """
.cards{grid-template-columns:repeat(auto-fit,minmax(15rem,1fr))}
.card-n{display:block;color:var(--dim);font-size:.8rem;letter-spacing:.08em}
.grp{margin:2.2rem 0 0;color:var(--dim);font-size:.8rem;font-weight:400;
     text-transform:uppercase;letter-spacing:.14em}
"""


def build_gallery():
    """Saraksts ar visiem variantiem - no šejienes tos salīdzina."""
    body = []
    group = None
    for i, t in enumerate(THEMES, 1):
        if t.get("group", G1) != group:
            if group is not None:
                body.append("</div>")
            group = t.get("group", G1)
            body.append('<h2 class="grp">%s</h2>' % esc(group))
            body.append('<div class="cards">')
        body.append(
            '<a class="card" href="%s/index.html">\n'
            '<span class="card-n">%02d</span>\n'
            '<span class="card-t">%s</span>\n'
            '<span class="card-s">%s</span>\n</a>'
            % (t["slug"], i, esc(t["name"]), esc(t["note"])))
    body.append("</div>")
    lead = ("Viens un tas pats saturs %d izskatos. Atver, paskaties telefonā "
            "un datorā, un pasaki numuru - to pārnesīšu uz visu vietni."
            % len(THEMES))
    body = ([head("Dizaina varianti", lead)] + body
            + ['<p class="foot">Stundu saites variantos ved uz īstajām '
               'prezentācijām.</p>'])
    gallery = {"name": "Galerija", "note": "", "css": GALLERY_CSS}
    return write(os.path.join(OUT, "index.html"),
                 page(gallery, "Dizaina varianti", "\n".join(body)))


def build_all():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    courses = ordered()
    for t in THEMES:
        build_variant(t, courses)
    return build_gallery()


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    print("Galerija:  %s" % build_all())
    print("Varianti:  %d" % len(THEMES))
