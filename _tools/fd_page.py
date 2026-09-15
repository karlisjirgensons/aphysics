# -*- coding: utf-8 -*-
"""Formatīvā darba ģeneratora lapas čaula: CSS, vadība un lapas veidne.

Šis modulis atbild tikai par lapu ap darbu (SRP): joslu ar pogām, lapas
izskatu ekrānā un uz printera, un to JavaScript daļu, kas izlozē variantu.
Kas uz lapas stāv, zina fd_paper.py; kā top Word fails - fd_docx.py.

Izloze strādā tā, ka temats ir sadalīts jautājumu grupās (viena grupa = viens
sasniedzamais rezultāts), un katrā grupā ir vairāki līdzvērtīgi jautājumi. No
katras grupas paņem vienu - tā darba uzbūve nemainās, bet lapas atšķiras.
Variants ir četru zīmju kods; ar to pašu kodu vienmēr sanāk tā pati lapa,
tāpēc skolotājs var izdrukāt to, ko redzēja ekrānā, vai pateikt kodu kolēģim.

Pati izloze (kods, sēkla, atbilžu pārkārtošana) ir izloze.py, jo to lieto
arī matemātikas ģeneratora lapas (DRY).

Krāsas nāk no palette.py, lapas noformējums - no fd_stils.py (DRY).
"""

import html
import json

import fd_docx
import fd_math
import fd_paper
import izloze
import fd_stils
import palette

CSS = """
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font-family:var(--font);
     line-height:1.55;-webkit-text-size-adjust:100%}
a{color:inherit;text-decoration:none}

.top{position:sticky;top:0;z-index:20;display:flex;gap:.6rem;
     align-items:center;flex-wrap:wrap;padding:.6rem .9rem;
     background:var(--grad);color:#fff;box-shadow:var(--sh-md)}
.top b{font-size:1rem;font-weight:600;font-family:var(--font-h)}
.top .sub{font-size:.78rem;color:rgba(255,255,255,.82);flex:1 1 10rem}
sub{font-size:.62em;vertical-align:-.22em;line-height:0}
.top .back{font-size:.82rem;padding:.35rem .75rem;border-radius:var(--r-pill);
     background:rgba(255,255,255,.14);transition:background .15s}
.top .back:hover{background:rgba(255,255,255,.28)}

.tools{display:flex;gap:.5rem;align-items:center;flex-wrap:wrap;
     max-width:52rem;margin:1rem auto 0;padding:0 1rem}
.tools button{font:inherit;font-size:.88rem;font-weight:500;border:0;
     cursor:pointer;border-radius:var(--r-pill);padding:.55rem 1.1rem;
     background:var(--surface);color:var(--primary);box-shadow:var(--sh);
     transition:transform .15s,box-shadow .15s,background .15s}
.tools button:hover{transform:translateY(-1px);box-shadow:var(--sh-lg)}
.tools button.main{background:var(--primary);color:#fff}
.tools button.main:hover{background:var(--violet)}
.tools button[aria-pressed="true"]{background:var(--amber-ink);color:#fff}
.tools .kods{margin-left:auto;font-size:.8rem;color:var(--dim);
     font-variant-numeric:tabular-nums}
.tools .kods b{color:var(--primary);font-size:.95rem;letter-spacing:.08em}

/* ---------- lapa ---------- */
.sheet{max-width:52rem;margin:1rem auto 3rem;background:var(--surface);
     border-radius:var(--r);box-shadow:var(--sh-md);padding:2rem 2.2rem 2.4rem;
     color:#1A1A1A}
/* Gara punktu virkne ("......") ir viens vārds - bez šī tā izstieptu lapu. */
.sheet p{overflow-wrap:break-word}
.sheet .meta{margin:0 0 .1rem;font-size:.78rem;color:var(--dim)}
.sheet .ph1{margin:0 0 .1rem;font-family:var(--font-h);font-weight:600;
     color:var(--primary);font-size:clamp(1.15rem,4.4vw,1.5rem)}
.sheet .ph2{margin:0 0 .5rem;font-weight:600;color:var(--primary);
     font-size:clamp(.92rem,3.6vw,1.05rem)}
.sheet .pnote{margin:.2rem 0 .6rem;font-size:.82rem;font-style:italic;
     color:var(--dim)}
.sheet .psec{margin:1.1rem 0 .3rem;font-weight:600;color:var(--primary);
     font-size:.95rem}
.sheet .pfoot{margin:.9rem 0 0;font-size:.85rem;color:var(--dim)}

.form{display:flex;gap:.8rem;flex-wrap:wrap;margin:.6rem 0 .9rem}
.form>div{flex:1 1 8rem}
.form .line{display:block;border-bottom:1px dotted #9CA3AF;height:1.25rem}
.form .lbl{font-size:.72rem;color:var(--dim)}

.box{border:1px solid var(--line);border-left:4px solid var(--violet);
     border-radius:.6rem;background:var(--surface2);padding:.6rem .8rem;
     margin:.7rem 0 1rem}
/* ATGĀDNE nāk no tā paša teksta, ko Word fails, tāpēc platās atstarpes
   starp formulām jāpatur - citādi tās saplūst vienā rindā. */
.box p{margin:0;font-size:.85rem;white-space:pre-wrap}
.box .boxt{font-weight:600;color:var(--primary);font-size:.75rem;
     letter-spacing:.06em}

/* Vertikāla daļa (a/b) - tā pati, ko lieto prezentācijas (deck_page.py). */
.f{display:inline-flex;flex-direction:column;align-items:stretch;
   text-align:center;vertical-align:middle;margin:0 .28em;line-height:1.14}
.f .n{display:block;padding:0 .2em}
.f .d{display:block;padding:0 .2em;border-top:.075em solid currentColor}

/* Kvadrātsakne: vinkuls pāri VISAI izteiksmei (rules_pd.txt). Zīme ir
   zīmēta (SVG), nevis ņemta no fonta, tāpēc vinkuls turpinās tieši no tās
   augšējā stūra - tāpat kā prezentācijās (deck_page.py). */
.rt{position:relative;display:inline-block;white-space:nowrap;
    --rw:.66em;padding-left:var(--rw);margin:0 .06em}
.rt .rk{position:absolute;left:0;top:0;bottom:0;width:var(--rw);height:auto;
        fill:currentColor}
.rt .rv{display:inline-block;border-top:.075em solid currentColor;
        padding:.16em .2em 0 .06em}

.q{margin:.7rem 0 .9rem}
.q .qt{margin:0 0 .25rem;font-size:.95rem}
.q .opts{display:grid;gap:.25rem .9rem;grid-template-columns:1fr 1fr;
     padding-left:.9rem}
.q .opt{font-size:.9rem;padding:.1rem .35rem;border-radius:.4rem}
.q .opt b{color:var(--dim);font-weight:600}
.sheet.key .opt.ok{background:#DCFCE7;color:#065F46;font-weight:500}
.sheet.key .opt.ok b{color:#047857}

.tw{overflow-x:auto;margin:.4rem 0 .2rem}
table.grid,table.tbl{border-collapse:collapse;width:100%;table-layout:fixed}
table.tbl{margin:.4rem 0 .2rem}
table.grid th,table.tbl th,table.grid td,table.tbl td{
     border:1px solid #A6A6A6;padding:.3rem .4rem;font-size:.85rem;
     text-align:left;vertical-align:middle}
table.grid th,table.tbl th{background:#1F3864;color:#fff;font-weight:600;
     text-align:center;font-size:.8rem}
table.tbl th{text-align:left}
table.grid td{height:1.8rem;text-align:center;letter-spacing:.28em}
table.grid th.tuksa{background:transparent;border:0}
table.grid .ans{display:none;font-weight:700;letter-spacing:0;
     color:#047857}
.sheet.key table.grid .abcd{display:none}
.sheet.key table.grid .ans{display:inline}

.keys{display:none;margin:.2rem 0}
.keys p{margin:0;font-size:.88rem}
.keys span{color:var(--dim)}
.sheet.key .keys{display:block}

/* ---------- telefons ---------- */
@media (max-width:768px){
  .sheet{margin:.7rem .6rem 2rem;padding:1.1rem 1rem 1.4rem;
         border-radius:.9rem}
  .tools{padding:0 .6rem}
  .tools button{flex:1 1 auto;font-size:.82rem;padding:.55rem .8rem}
  .tools .kods{flex:1 1 100%;margin-left:0;text-align:right}
  .q .opts{grid-template-columns:1fr;padding-left:.5rem}
  .top b{flex:1 1 100%;order:2;font-size:.92rem}
  .top .back{order:1}
  .top .sub{order:3}
  table.grid{min-width:19rem}
  table.grid th,table.grid td{padding:.25rem .2rem;font-size:.78rem}
  table.grid td{letter-spacing:.12em}
}

/* ---------- printeris ----------
   Uz papīra lapa ir tā pati, kas Word failā: A4, Calibri izmēri punktos un
   viss vienā lapā. Tāpēc drukāt var arī tieši no pārlūka. */
@page{size:A4;margin:12mm 15mm}
@media print{
  .top,.tools{display:none}
  body{background:#fff;font-family:Calibri,var(--font);line-height:1.22}
  .sheet{margin:0;padding:0;max-width:none;box-shadow:none;border-radius:0}
  .sheet .meta{font-size:9pt;margin:0}
  .sheet .ph1{font-family:inherit;font-size:16pt;margin:0}
  .sheet .ph2{font-size:13pt;margin:0 0 3pt}
  .sheet .pnote{font-size:9.5pt;margin:0 0 4pt}
  .sheet .psec{font-size:10pt;margin:5pt 0 2pt}
  .sheet .pfoot{font-size:10pt;margin:4pt 0 0;color:#000}
  .form{margin:2pt 0 4pt;gap:.5rem}
  .form .line{height:14pt}
  .form .lbl{font-size:8pt}
  .box{margin:3pt 0 4pt;padding:4pt 6pt;border-radius:0}
  .box p{font-size:9pt}
  .box .boxt{font-size:8pt}
  .q{margin:0 0 2pt}
  .q .qt{font-size:10pt;margin:0}
  .q .opts{grid-template-columns:1fr 1fr;gap:0 .6rem;padding-left:.6rem}
  .q .opt{font-size:10pt;padding:0}
  .tw{overflow:visible;margin:2pt 0}
  table.grid th,table.grid td{font-size:10pt;padding:1pt 2pt}
  table.grid td{height:15pt;letter-spacing:.3em}
  .q,.box,.tw{break-inside:avoid}
}
"""

JS = r"""
(function(){
"use strict";
var D=window.FD_DATI,S=window.FD_STILS,I=window.IZLOZE;

/* --- viens darbs: no katras grupas viens jautājums --- */
function darbs(kod){
  var rnd=I.lozes(I.seja(kod)),grupas=D.grupas,n=grupas.length;
  var m=I.merki(n,rnd),jautajumi=grupas.map(function(g,i){
    var izvele=g.jautajumi[Math.floor(rnd()*g.jautajumi.length)];
    var q=I.sagatavo(izvele,m[i],rnd);
    q.sr=g.sr;q.stunda=g.stunda;
    return q;
  });
  return {kods:kod,jautajumi:jautajumi,
          burti:jautajumi.map(function(q){return S.burti[q.pareizais];})};
}

/* --- attēlošana --- */
var lapa=document.getElementById("sheet"),
    kodsEl=document.getElementById("kods"),
    poga=document.getElementById("atb"),
    tagad=null;

function zime(t){
  tagad=t;
  lapa.innerHTML=window.PAPER.html(window.PAPER.blocks(D,t,false));
  kodsEl.innerHTML="Variants <b>"+t.kods+"</b>";
  if(location.hash.slice(1)!==t.kods)
    history.replaceState(null,"","#"+t.kods);
}
function lejup(atslega){
  var bloki=window.PAPER.blocks(D,tagad,atslega);
  var vards=D.fails+" ("+(atslega?"atbildes, ":"")+"variants "+tagad.kods+
            ").docx";
  window.DOCX.save(window.DOCX.build(window.PAPER.docx(bloki)),vards);
}

document.getElementById("jauns").addEventListener("click",function(){
  zime(darbs(I.kods()));
  lapa.classList.remove("key");
  poga.setAttribute("aria-pressed","false");
  window.scrollTo({top:0,behavior:"smooth"});
});
poga.addEventListener("click",function(){
  var on=lapa.classList.toggle("key");
  poga.setAttribute("aria-pressed",on?"true":"false");
});
document.getElementById("word").addEventListener("click",function(){
  lejup(false);});
document.getElementById("wordatb").addEventListener("click",function(){
  lejup(true);});
document.getElementById("druka").addEventListener("click",function(){
  window.print();});

var sakums=location.hash.slice(1).toUpperCase();
zime(darbs(/^[A-Z0-9]{4}$/.test(sakums)?sakums:I.kods()));
})();
"""

PAGE = """<!DOCTYPE html>
<html lang="lv">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>%(title)s</title>
%(fonts)s<style>%(root)s%(css)s</style>
</head>
<body>
<div class="top">
  <a class="back" href="../index.html">&#8592; Uz t&#275;m&#257;m</a>
  <b>%(title)s</b>
  <span class="sub">%(kicker)s</span>
</div>
<div class="tools">
  <button id="jauns" class="main" type="button">&#9851; &#288;ener&#275;t jaunu variantu</button>
  <button id="atb" type="button" aria-pressed="false">R&#257;d&#299;t atbildes</button>
  <button id="word" type="button">Darba lapa (Word)</button>
  <button id="wordatb" type="button">Atbildes (Word)</button>
  <button id="druka" type="button">Drukāt</button>
  <span class="kods" id="kods"></span>
</div>
<div class="sheet" id="sheet"></div>
<script>%(stils)s</script>
<script>%(dati)s</script>
<script>%(math)s</script>
<script>%(izloze)s</script>
<script>%(docx)s</script>
<script>%(paper)s</script>
<script>%(js)s</script>
</body>
</html>
"""


def page(dati):
    """Gatava ģeneratora lapa no satura vārdnīcas."""
    title = "%s Nr. %d. %s" % (dati["virsraksts"], dati["nr"],
                               dati["nosaukums"])
    return PAGE % {
        "title": html.escape(title),
        "kicker": html.escape(dati["kicker"]),
        "css": CSS, "js": JS,
        "stils": fd_stils.js(),
        "math": fd_math.js(indeksi=True),
        "docx": fd_docx.JS, "paper": fd_paper.JS,
        "izloze": izloze.JS,
        "dati": "window.FD_DATI=%s;" % json.dumps(dati, ensure_ascii=False),
        "root": palette.root_css(), "fonts": palette.FONT_LINK,
    }
