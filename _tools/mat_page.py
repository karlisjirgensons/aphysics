# -*- coding: utf-8 -*-
"""Matemātikas darbu ģeneratora lapas čaula: CSS, vadība un lapas veidne.

Lapa rāda vienu darba variantu; poga «Ģenerēt» izlozē nākamo. Variantam nav
kārtas numura - to apzīmē piecu zīmju kods (piemēram, T32MC), tāpēc pēc koda
nevar noprast, kurš darbs kuram skolēnam dots. Ar to pašu kodu vienmēr sanāk
tā pati lapa, tāpēc skolotājs var izdrukāt tieši to, ko redzēja ekrānā.

Šis modulis atbild tikai par lapu ap darbiem (SRP): joslu ar pogām, izskatu
ekrānā un uz printera, un to JavaScript daļu, kas savieno izlozi ar
attēlotāju. Izloze ir izloze.py, darba lapas saturs - fd_paper.py (formatīvā
darba lapa) un mat_paper.py (pārbaudes darba divas lapas), Word fails -
fd_docx.py. Stils nāk no fd_page.py un palette.py, tāpēc ģenerētās lapas
izskatās tāpat kā fizikas darbi (DRY).
"""

import html
import json

import fd_docx
import fd_math
import fd_page
import fd_paper
import fd_stils
import izloze
import mat_paper
import palette

# Ģenerētas lapas izskats ir tas pats, kas formatīvajam darbam; klāt nāk
# tikai tas, kā tur nav - uzdevumi ar darba vietu un vairākas lapas.
CSS = fd_page.CSS + """
/* ---------- vairākas lapas vienā skatā ---------- */
.sheet+.sheet{margin-top:1.4rem}
.sheet.atbl{display:none;border-top:4px solid var(--amber)}
.sheet.atbl.key{display:block}

/* ---------- pārbaudes darba uzdevumi ---------- */
.sheet .puzd{margin:1.1rem 0 .3rem;font-weight:600;color:var(--primary);
     font-size:1rem}
.sheet .puzd .pp{color:var(--amber-ink);font-weight:500;font-size:.85rem}
.sheet .ptext{margin:.2rem 0 .4rem;font-size:.95rem}

.rindas{margin:.3rem 0 .6rem;border:1px solid #A6A6A6;border-radius:.4rem;
     overflow:hidden}
.rindas p{margin:0;padding:.45rem .6rem;font-size:1rem;
     border-top:1px solid #A6A6A6}
.rindas p:first-child{border-top:0}

.jaut{margin:.2rem 0 .4rem;padding-left:.9rem}
.jaut p{margin:.1rem 0;font-size:.92rem}

/* Darba vieta ir rūtiņas - pirmklasnieks tajās zīmē figūras ar lineālu. */
.vieta{position:relative;margin:.3rem 0 .7rem;border:1px solid #A6A6A6;
     border-radius:.4rem;background-color:#fff;
     background-image:linear-gradient(#EEF2F8 1px,transparent 1px),
                      linear-gradient(90deg,#EEF2F8 1px,transparent 1px);
     background-size:.5cm .5cm;background-position:-1px -1px}
.vieta .vh{position:absolute;top:.2rem;left:.5rem;font-size:.72rem;
     color:var(--dim)}
table.grid td.vertr,table.grid tr.vertr td{height:1.6rem;letter-spacing:0}

.atbsar{margin:.1rem 0 .3rem;padding-left:.9rem}
.atbsar p{margin:.1rem 0;font-size:.9rem}

@media (max-width:768px){
  .sheet .puzd{font-size:.95rem}
  .rindas p{font-size:.95rem;padding:.4rem .5rem}
}

@media print{
  /* Katrs variants un katra lapa sākas ar jaunu A4 lapu. */
  .sheet+.sheet{break-before:page;margin-top:0}
  .sheet .puzd{font-size:11pt;margin:6pt 0 2pt}
  .sheet .ptext{font-size:10.5pt;margin:0 0 3pt}
  .rindas{margin:2pt 0 4pt;border-radius:0}
  .rindas p{font-size:11pt;padding:3pt 4pt}
  .jaut p{font-size:10pt;margin:0}
  .vieta{margin:2pt 0 4pt;border-radius:0}
  .vieta .vh{font-size:8pt}
  .atbsar p{font-size:10pt;margin:0}
  .rindas,.vieta,.jaut{break-inside:avoid}
}
"""

JS = r"""
(function(){
"use strict";
var D=window.MAT_DATI,S=window.FD_STILS,I=window.IZLOZE;
var MOD=D.veids==="pd"?window.PAPER_PD:window.PAPER;
var KODA_GARUMS=5;

/* ------------------------------------------------------------- izloze */
function darbs(kod){
  /* Viens darbs: no katras jautājumu grupas viens jautājums un katram
     uzdevumam viens tā variants. Ar to pašu kodu vienmēr sanāk tas pats. */
  var rnd=I.lozes(I.seja(kod)),grupas=D.veids==="pd"?D.tests:D.grupas;
  var m=I.merki(grupas.length,rnd);
  var q=grupas.map(function(g,i){
    var izvele=g.jautajumi[Math.floor(rnd()*g.jautajumi.length)];
    var x=I.sagatavo(izvele,m[i],rnd);
    x.sr=g.sr;x.stunda=g.stunda;
    return x;});
  var d={kods:kod,burti:q.map(function(x){return S.burti[x.pareizais];})};
  if(D.veids==="pd"){
    d.tests=q;
    d.uzdevumi=D.uzdevumi.map(function(u,i){
      return {nr:i+2,sr:u.sr,punkti:u.punkti,lapa:u.lapa,
              u:u.varianti[Math.floor(rnd()*u.varianti.length)]};});
  }else{
    d.jautajumi=q;
  }
  return d;
}

/* --------------------------------------------------------- attēlošana */
var laukums=document.getElementById("darbs"),
    kodsEl=document.getElementById("kods"),
    poga=document.getElementById("atb"),
    tagad=null;

function lapas(bloki){
  /* Bloku saraksts -> lapas; {t:"pb"} sāk jaunu lapu. */
  var out=[[]],i;
  for(i=0;i<bloki.length;i++){
    if(bloki[i].t==="pb")out.push([]);
    else out[out.length-1].push(bloki[i]);
  }
  return out;
}
function lapa(bloki,klase){
  return '<div class="sheet'+(klase?" "+klase:"")+'">'+MOD.html(bloki)+
         '</div>';
}
function zime(d){
  tagad=d;
  var teksts="";
  lapas(MOD.blocks(D,d,false)).forEach(function(l){teksts+=lapa(l);});
  /* Atbildes ir klāt vienmēr, tikai apslēptas - poga tās tikai parāda. */
  lapas(MOD.blocks(D,d,true)).forEach(function(l){teksts+=lapa(l,"atbl");});
  laukums.innerHTML=teksts;
  atslega(false);
  kodsEl.innerHTML="Variants <b>"+d.kods+"</b>";
  if(location.hash.slice(1)!==d.kods)
    history.replaceState(null,"","#"+d.kods);
}
function atslega(on){
  var lapas=laukums.getElementsByClassName("sheet"),i;
  for(i=0;i<lapas.length;i++)
    lapas[i].classList[on?"add":"remove"]("key");
  poga.setAttribute("aria-pressed",on?"true":"false");
}
function lejup(atsl){
  var bloki=MOD.docx(MOD.blocks(D,tagad,atsl));
  window.DOCX.save(window.DOCX.build(bloki),
    D.fails+" ("+(atsl?"atbildes, ":"")+"variants "+tagad.kods+").docx");
}

document.getElementById("jauns").addEventListener("click",function(){
  zime(darbs(I.kods(KODA_GARUMS)));
  window.scrollTo({top:0,behavior:"smooth"});
});
poga.addEventListener("click",function(){
  atslega(poga.getAttribute("aria-pressed")!=="true");});
document.getElementById("word").addEventListener("click",function(){
  lejup(false);});
document.getElementById("wordatb").addEventListener("click",function(){
  lejup(true);});
document.getElementById("druka").addEventListener("click",function(){
  window.print();});

var sakums=location.hash.slice(1).toUpperCase();
zime(darbs(/^[A-Z0-9]{5}$/.test(sakums)?sakums:I.kods(KODA_GARUMS)));
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
  <a class="back" href="../index.html">&#8592; Uz tematiem</a>
  <b>%(title)s</b>
  <span class="sub">%(kicker)s</span>
</div>
<div class="tools">
  <button id="jauns" class="main" type="button">&#9851; &#288;ener&#275;t</button>
  <button id="atb" type="button" aria-pressed="false">R&#257;d&#299;t atbildes</button>
  <button id="word" type="button">Darba lapa (Word)</button>
  <button id="wordatb" type="button">Atbildes (Word)</button>
  <button id="druka" type="button">Drukāt</button>
  <span class="kods" id="kods"></span>
</div>
<div id="darbs"></div>
<script>%(stils)s</script>
<script>%(dati)s</script>
<script>%(math)s</script>
<script>%(izloze)s</script>
<script>%(docx)s</script>
<script>%(paper)s</script>
<script>%(paperpd)s</script>
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
        "izloze": izloze.JS,
        "math": fd_math.js(indeksi=False),
        "docx": fd_docx.JS, "paper": fd_paper.JS,
        "paperpd": mat_paper.JS,
        "dati": "window.MAT_DATI=%s;" % json.dumps(dati, ensure_ascii=False),
        "root": palette.root_css(), "fonts": palette.FONT_LINK,
    }
