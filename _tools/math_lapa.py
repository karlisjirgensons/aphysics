# -*- coding: utf-8 -*-
"""Matemātikas stundas lapas čaula: augšējā josla, galva un bloku vieta.

Stunda ir viena patstāvīga HTML lapa, kas pirmām kārtām domāta telefonam:
pamatizkārtojums ir viena sleja ar lielu tekstu un lielām pogām, un platākam
ekrānam pieliek tikai vairāk vietas malās (rules_matematika.txt). Lapa nezina
neko par konkrētu stundu - saturu tā saņem kā bloku sarakstu (SRP), bet CSS un
JS gabalus paņem no pašiem blokiem, katru pa vienai reizei (DRY).

Platā ekrānā to pašu stundu var rādīt kā prezentāciju - to pieliek
math_pilnekrans.py, lapas veidnē par to nav nevienas rindas.

Čaulas CSS selektori nosauc savu elementu (header.galva, nav.talak): bloku
klases dzīvo tajā pašā lapā, un vaļēja klase citādi krīt virsū blokam, kam
gadījies tāds pats vārds.

Krāsas un fonti nāk no palette.py, tāpēc stunda izskatās tāpat kā pārējā
vietne; kur lapa nonāk failu kokā, zina math_stundas.py.
"""

import math_bloki
import math_ikonas
import math_pilnekrans
import palette
from site_index import esc

CSS = """
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font-family:var(--font);
     line-height:1.55}
a{color:inherit;text-decoration:none}

.augsa{position:sticky;top:0;z-index:20;display:flex;align-items:center;
    gap:.6rem;padding:.55rem .8rem;background:var(--grad);color:#fff;
    box-shadow:var(--sh-md)}
.augsa .atpakal{flex:none;padding:.35rem .8rem;border-radius:var(--r-pill);
    background:rgba(255,255,255,.16);font-size:.85rem;font-weight:500;
    transition:background .15s}
.augsa .atpakal:hover{background:rgba(255,255,255,.3)}
.augsa .kods{flex:1;text-align:right;font-size:.78rem;
    color:rgba(255,255,255,.85)}

.lapa{max-width:46rem;margin:0 auto;padding:0 .8rem 3rem}

header.galva{margin:0 -.8rem 1.1rem;padding:1.4rem 1.1rem 1.5rem;
    background:var(--grad);color:#fff;border-radius:0 0 1.5rem 1.5rem}
header.galva .mikro{margin:0;font-size:.82rem;color:rgba(255,255,255,.85);
    text-transform:uppercase;letter-spacing:.06em}
header.galva h1{margin:.3rem 0 0;font-family:var(--font-h);font-weight:600;
    line-height:1.2;font-size:clamp(1.45rem,6.4vw,2.1rem)}
header.galva .merkis{margin:.6rem 0 0;font-size:clamp(.95rem,4vw,1.08rem);
    color:rgba(255,255,255,.9)}

.skolotajam{margin:.4rem 0 1rem;border:1px dashed var(--line);
    border-radius:var(--r);background:var(--surface)}
.skolotajam summary{padding:.6rem .9rem;cursor:pointer;color:var(--dim);
    font-size:.85rem;font-weight:500;list-style:none}
.skolotajam summary::-webkit-details-marker{display:none}
.skolotajam summary::before{content:"\\25B8  "}
.skolotajam[open] summary::before{content:"\\25BE  "}
.skolotajam div{padding:0 .9rem .8rem}
.skolotajam p{margin:.2rem 0;font-size:.85rem;color:var(--dim)}
.skolotajam b{color:var(--fg);font-weight:600}

nav.talak{display:flex;gap:.6rem;flex-wrap:wrap;margin:1.2rem 0 0}
nav.talak a{flex:1 1 12rem;padding:.85rem 1rem;border-radius:var(--r);
    background:var(--surface);border:1px solid var(--line);
    box-shadow:var(--sh);font-size:.95rem;transition:border-color .15s}
nav.talak a:hover{border-color:var(--violet)}
nav.talak a span{display:block;color:var(--dim);font-size:.78rem}
nav.talak a b{color:var(--primary);font-weight:600}

/* Vertikāla daļa un kvadrātsakne - tas pats pieraksts, ko lieto
   prezentācijas (deck_page.py) un darba lapas (fd_page.py); HTML tam nāk no
   mathhtml.py, tāpēc forma ir vienā vietā (DRY). */
.f{display:inline-flex;flex-direction:column;align-items:stretch;
   text-align:center;vertical-align:middle;margin:0 .28em;line-height:1.14}
.f .n{display:block;padding:0 .2em}
.f .d{display:block;padding:0 .2em;border-top:.075em solid currentColor}
.rt{position:relative;display:inline-block;white-space:nowrap;
    --rw:.66em;padding-left:var(--rw);margin:0 .06em}
.rt .rk{position:absolute;left:0;top:0;bottom:0;width:var(--rw);height:auto;
        fill:currentColor}
.rt .rv{display:inline-block;border-top:.075em solid currentColor;
        padding:.16em .2em 0 .06em}
.izcel{color:var(--violet);font-weight:700}

/* Zīmējumi (math_zimejumi.py). Izskats ir lapas, nevis bloka ziņā, jo
   zīmējums var stāvēt gan savā blokā, gan stundas sākumā - un abās vietās
   tam jāizskatās vienādi (DRY). */
svg.zim{display:block;width:100%;height:auto;max-height:52vh;
    overflow:visible}
.zim text{font-family:var(--font);fill:var(--fg)}
.zim .z-ass{stroke:var(--fg);stroke-width:.5;fill:var(--fg)}
.zim .z-iedala{stroke:var(--dim);stroke-width:.4}
.zim .z-punkts{fill:var(--violet)}
.zim .z-stabs{fill:var(--violet);opacity:.85}
.zim .z-kopa{fill:rgba(124,58,237,.10);stroke:var(--violet);stroke-width:.5}
.zim .z-bits{fill:var(--surface);stroke:var(--violet);stroke-width:.5}
.zim .z-bits.on{fill:var(--violet)}
.zim .z-ruts{fill:var(--surface);stroke:var(--violet);stroke-width:.5}
.zim .z-ruts.tuksa{fill:var(--bg);stroke-dasharray:1.8 1.2}
.zim .z-resti{stroke:var(--line);stroke-width:.35}
.zim .z-rame{fill:none;stroke:var(--violet);stroke-width:.7}
.zim .z-lauks{fill:rgba(124,58,237,.28)}
.zim .z-figura{fill:rgba(124,58,237,.16);stroke:var(--violet);
    stroke-width:.7}
.zim .z-lin{fill:none;stroke:var(--violet);stroke-width:.8;
    stroke-linejoin:round}
.zim .z-kerm{fill:none;stroke:var(--primary);stroke-width:.7;
    stroke-linejoin:round}
.zim .z-kerm.slepts{stroke:var(--dim);stroke-dasharray:1.6 1.2}
.zim .z-bulta{fill:none;stroke:var(--amber-ink);stroke-width:.7}
.zim .z-bultgals{fill:var(--amber-ink)}
.zim .z-mazs{font-size:3px;fill:var(--dim)}
.zim .z-dsvitra{stroke:currentColor;stroke-width:.3;stroke:var(--violet)}
.zim .z-nr{font-size:3.4px}
.zim .z-atzime{font-size:3.6px;font-weight:600;fill:var(--violet)}
.zim .z-virs{font-size:3.8px;font-weight:600;fill:var(--primary)}
.zim .z-bits-c{font-size:4.4px;font-weight:700;fill:var(--violet)}
.zim .z-bits-c.on{fill:#fff}
.zim .z-ruts-c{font-size:5px;font-weight:700;fill:var(--violet)}
.zim .z-ruts-c.tuksa{fill:var(--dim);font-weight:600}
.vv{position:relative;white-space:nowrap}
.vv::after{content:"";position:absolute;left:-.04em;right:-.04em;top:-.52em;
    height:.42em;border-top:.075em solid currentColor;
    border-right:.075em solid currentColor;
    transform:skewX(58deg) scaleY(.5);transform-origin:right top}

.ik{display:inline-block;width:1em;height:1em;vertical-align:-.13em;
    line-height:0}
.ik svg{width:100%;height:100%;display:block;overflow:visible}
.ik .l{fill:none;stroke:currentColor;stroke-width:3.4;stroke-linecap:round;
    stroke-linejoin:round}
.ik .p{fill:currentColor;stroke:none}

@media (min-width:768px){
  .lapa{padding:0 1.4rem 4rem}
  header.galva{margin:0 -1.4rem 1.4rem;padding:2rem 1.6rem 2.1rem}
  .bl{padding:1.4rem 1.4rem 1.5rem}
}
"""

PAGE = """<!DOCTYPE html>
<html lang="lv">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%(title)s</title>
%(fonts)s<style>%(root)s%(css)s</style>
</head>
<body>
<div class="augsa">
<a class="atpakal" href="%(atpakal)s">&#8592; %(klase)s</a>
<span class="kods">%(kods)s</span>
</div>
<div class="lapa">
%(body)s
</div>
<script>%(js)s</script>
</body>
</html>
"""


def _fragmenti(bloki):
    """Bloku CSS un JS gabali - katrs vienu reizi, tādā secībā, kā vajadzīgs.

    Dzinēja gabals (Spele) sanāk pirms tā veidiem, jo mantojuma ķēdi ejam no
    pamata uz leju.
    """
    redzeti, css, js = set(), [], []
    for b in bloki:
        for atslega, c, j in b.fragmenti():
            if atslega in redzeti:
                continue
            redzeti.add(atslega)
            css.append(c)
            js.append(j)
    return "".join(css), "".join(js)


def render_galva(stunda, merkis):
    return ('<header class="galva">\n<p class="mikro">%s</p>\n<h1>%s</h1>\n'
            '<p class="merkis">%s</p>\n</header>'
            % (esc(stunda.bloks.nosaukums), esc(stunda.tema), esc(merkis)))


def render_skolotajam(stunda, datums):
    """Plāna rinda par šo stundu - skolēnam to nevajag, skolotājam gan."""
    temats = stunda.temats
    rindas = ["<p><b>Sasniedzamais rezultāts.</b> %s</p>" % esc(stunda.sr)]
    if temats:
        rindas.append("<p><b>Temats.</b> %s %s</p>"
                      % (esc(temats.kods), esc(temats.nosaukums)))
    rindas.append("<p><b>Mikrotemats.</b> %s</p>"
                  % esc(stunda.bloks.nosaukums))
    rindas.append("<p><b>Provizoriskais datums.</b> %s</p>" % esc(datums))
    return ('<details class="skolotajam">\n<summary>Skolotājam</summary>\n'
            '<div>\n%s\n</div>\n</details>' % "\n".join(rindas))


def render_talak(saites):
    """Pogas uz iepriekšējo un nākamo stundu; ja tādu vēl nav - nav pogu."""
    if not saites:
        return ""
    pogas = ['<a href="%s"><span>%s</span><b>%s</b></a>' % (c, esc(v), esc(t))
             for v, t, c in saites]
    return '<nav class="talak">\n%s\n</nav>' % "\n".join(pogas)


def render(stunda, saturs, atpakal, klases_nosaukums, datums, saites=()):
    """Vienas stundas lapa: galva, bloki, skolotāja rinda un ceļš tālāk."""
    bloki = list(saturs.SATURS)
    css, js = _fragmenti(bloki)
    kods = "%s %s · %d. stunda" % (
        stunda.temats.kods if stunda.temats else "",
        klases_nosaukums, stunda.nr)
    body = "\n".join([render_galva(stunda, saturs.MERKIS),
                      render_skolotajam(stunda, datums),
                      '<main class="saturs">',
                      "\n".join(b.html() for b in bloki),
                      "</main>",
                      render_talak(saites)])
    return PAGE % {"title": esc("%d. %s" % (stunda.nr, stunda.tema)),
                   "fonts": palette.FONT_LINK, "root": palette.root_css(),
                   "css": CSS + css + math_pilnekrans.CSS,
                   "js": math_ikonas.js() + js + math_pilnekrans.JS,
                   "atpakal": atpakal, "klase": esc(klases_nosaukums),
                   "kods": esc(kods.strip()), "body": body}


def parbaudi(saturs):
    """Vai stundas saturs ir uzrakstīts tā, kā lapa to gaida.

    Divas prasības ir par pašu stundas uzbūvi, un tās pārbauda šeit, nevis
    atstāj katra autora ziņā (tāpēc tās der visām klasēm un tematiem):

        * stunda sākas ar Sakums - īss jautājums, attēls un daži fakti,
          nevis rindkopas, ko neviens nelasa;
        * stundā ir vismaz viens Pasaule uzdevums - tas pats rēķins par
          īstu lietu, piesiets pavedienam.
    """
    import math_uzdevumi                             # noqa: E402 - aplis
    for vards in ("TEMA", "MERKIS", "SATURS"):
        if not getattr(saturs, vards, None):
            raise AssertionError("stundas saturā trūkst %s" % vards)
    bloki = list(saturs.SATURS)
    for b in bloki:
        if not isinstance(b, math_bloki.Bloks):
            raise AssertionError("«%s» nav stundas bloks" % (b,))
    if not isinstance(bloki[0], math_bloki.Sakums):
        raise AssertionError(
            "«%s»: stundai jāsākas ar Sakums, nevis ar %s"
            % (saturs.TEMA, bloki[0].__class__.__name__))
    if getattr(saturs, "PARBAUDES_DARBS", False):
        return                       # pārbaudes darbā uzdevumu nav
    if not any(isinstance(b, math_uzdevumi.Pasaule) for b in bloki):
        raise AssertionError(
            "«%s»: stundā vajag vismaz vienu Pasaule uzdevumu" % saturs.TEMA)
