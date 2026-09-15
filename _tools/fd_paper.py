# -*- coding: utf-8 -*-
"""Formatīvā darba lapa: viens modelis, divi attēlotāji - JavaScript teksts.

Lapa (blocks) ir tikai saraksts ar to, kas uz tās stāv: galvene, ATGĀDNE,
jautājumi, atbilžu tabula, kājene. Pats saraksts nezina, vai to zīmēs ekrānā
vai Word failā - to dara divi atsevišķi attēlotāji (SRP):

    PAPER.blocks(dati, tests, atslega) - saturs -> lapas modelis
    PAPER.html(blocks)                 - modelis -> HTML ekrānam
    PAPER.docx(blocks)                 - modelis -> DOCX bloki (fd_docx.py)

Tāpēc jautājuma izskats jāapraksta vienreiz: abi attēlotāji lasa vienu un to
pašu modeli, un Word fails nevar "aizmirst" to, ko rāda ekrāns (DRY).

Daļas satura tekstā raksta ar {skaitītājs|saucējs}, piemēram «v = {s|t}».
Ekrānā tā top par vertikālu daļu (CSS), Word failā - par īstu formulu
(OMML), tāpēc rules_lessons.txt prasība par vertikālām daļām ir izpildīta
abās vidēs. Mērvienības (km/h, m/s) paliek nepārveidotas, jo daļa tiek
atzīmēta ar roku - nekas netiek uzminēts.

Ekrāna lapā pareizās atbildes ir klāt vienmēr, tikai apslēptas ar CSS -
poga «Rādīt atbildes» tikai pieliek lapai klasi, tāpēc pārzīmēt nevajag un
izlozētais variants nemainās.
"""

JS = r"""
window.PAPER=(function(){
"use strict";
var S=window.FD_STILS,K=S.krasas,Z=S.izmeri,B=S.burti;

var TEKSTI={
  tabula:"ATBILŽU TABULA",
  atslega:"ATBILŽU ATSLĒGA",
  pamaciba:"Katram jautājumam apvelc vienu burtu! Labojums der tikai tad, "+
           "ja nepareizā atbilde ir skaidri nosvītrota.",
  atgadne:"ATGĀDNE",
  veidlapa:["Vārds","Uzvārds","Klase","Datums"],
  pareizas:"Pareizās atbildes",
  parbauda:"Ko darbs pārbauda",
  skala:"Vērtēšanas skala (kopā %d punkti)",
  skalasParaksts:"Augšējā rindā — balle, apakšējā — iegūto punktu skaits.",
  strukturasGalva:["Jaut.","Pārbaudāmais sasniedzamais rezultāts","Stunda"],
  skolotajam:"Atbildes un vērtēšanas skala — SKOLOTĀJAM"
};
var ATSTARPE="      ";          /* starp atbilžu variantiem vienā rindā */

function punkti(n){return "Punkti:  ............ / "+n+"          Balle:  "+
  "............          Skolotāja paraksts:  .......................";}

/* ------------------------------------------------------- daļas un saknes */
/* Marķējumu ({a|b}, √(a+b)) izjauc FD_MATH; te tas tikai top par HTML. */
var gabali=window.FD_MATH.atomi,vienkarsi=window.FD_MATH.vienkarsi;
var indeksi=window.FD_MATH.indeksi;

/* ------------------------------------------------------------- modelis */
function bloki(n){
  var out=[],i;
  for(i=0;i<n;i+=S.ailes)out.push({no:i,lidz:Math.min(i+S.ailes,n)});
  return out;
}

function metaRinda(dati){
  /* Galvenes augšrinda. Skolas nosaukumu var noņemt, satura datos ierakstot
     tukšu «skola» (matemātikas darbi to nelieto). */
  return [dati.prieksmets,dati.skola==null?S.skola:dati.skola,S.gads]
    .filter(function(x){return x;}).join("  |  ");
}

function variants(tests){
  /* Ja darbs top vairākos variantos (mat_page.py), tiem ir arī numurs. */
  return tests.nr?tests.nr+". variants  ·  kods "+tests.kods
                 :"variants "+tests.kods;
}

function blocks(dati,tests,atslega){
  var q=tests.jautajumi,n=q.length,out=[];
  out.push({t:"meta",text:metaRinda(dati)});
  out.push({t:"h1",text:dati.virsraksts+" Nr. "+dati.nr+".  "+dati.nosaukums});
  if(atslega){
    out.push({t:"h2",text:TEKSTI.skolotajam});
    out.push({t:"note",text:dati.apraksts+"  "+variants(tests)+
      ".  Izpildes laiks — "+dati.laiks+" minūtes, kopā "+n+
      " punkti (1 p. par katru pareizu atbildi)."});
    out.push({t:"grid",n:n,letters:tests.burti,atslega:true});
    out.push({t:"sec",text:TEKSTI.pareizas});
    out.push({t:"key",items:q.map(function(x,i){
      return {nr:i+1,letter:tests.burti[i],text:x.varianti[x.pareizais]};})});
    out.push({t:"sec",text:TEKSTI.parbauda});
    out.push({t:"tbl",widths:S.platumi.struktura,
      head:dati.aile||TEKSTI.strukturasGalva,
      rows:q.map(function(x,i){return [(i+1)+".",x.sr,x.stunda];})});
    out.push({t:"sec",text:TEKSTI.skala.replace("%d",n)});
    out.push({t:"skala",skala:dati.skala});
    return out;
  }
  out.push({t:"h2",text:n+" jautājumi  ·  "+dati.laiks+" minūtes  ·  "+n+
    " punkti  ·  "+variants(tests)});
  out.push({t:"note",text:dati.ievads});
  out.push({t:"form"});
  out.push({t:"box",title:TEKSTI.atgadne,lines:dati.atgadne});
  q.forEach(function(x,i){
    out.push({t:"q",nr:i+1,text:x.teksts,options:x.varianti,
              correct:x.pareizais});});
  out.push({t:"grid",n:n,letters:tests.burti,atslega:false});
  out.push({t:"foot",text:punkti(n)});
  return out;
}

/* ---------------------------------------------------------------- HTML */
function esc(s){return String(s==null?"":s)
  .replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");}
function teksts(s){
  /* Teksts ar indeksiem: "s(kopā)" -> "s<sub>kopā</sub>". */
  return indeksi(s).map(function(r){
    return r.sub!=null?"<sub>"+esc(r.sub)+"</sub>":esc(r.text);}).join("");
}
function sakne(izteiksme){
  /* Zīme ir zīmēta (FD_STILS.sakne), tāpēc vinkuls turpinās no tās stūra
     un pāri paliek VISA izteiksme, ne tikai iekava. */
  var r=S.sakne;
  return '<span class="rt" style="--rw:'+r.w.toFixed(3)+'em">'+r.svg+
         '<span class="rv">'+teksts(izteiksme)+'</span></span>';
}
function atomi(list){
  return list.map(function(g){
    if(g.frac)return '<span class="f"><span class="n">'+atomi(g.frac[0])+
      '</span><span class="d">'+atomi(g.frac[1])+'</span></span>';
    if(g.root!=null)return sakne(g.root);
    return teksts(g.text);
  }).join("");
}
function mt(s){
  /* Teksts ekrānam: marķētās daļas un saknes top par īstām formulām. */
  return atomi(gabali(s));
}

var HTML={
  meta:function(b){return '<p class="meta">'+mt(b.text)+'</p>';},
  h1:function(b){return '<h2 class="ph1">'+mt(b.text)+'</h2>';},
  h2:function(b){return '<p class="ph2">'+mt(b.text)+'</p>';},
  note:function(b){return '<p class="pnote">'+mt(b.text)+'</p>';},
  sec:function(b){return '<p class="psec">'+mt(b.text)+'</p>';},
  foot:function(b){return '<p class="pfoot">'+mt(b.text)+'</p>';},
  form:function(){
    return '<div class="form">'+TEKSTI.veidlapa.map(function(x){
      return '<div><span class="line"></span><span class="lbl">'+esc(x)+
             '</span></div>';}).join("")+'</div>';},
  box:function(b){
    return '<div class="box"><p class="boxt">'+esc(b.title)+'</p>'+
      b.lines.map(function(x){return '<p>'+mt(x)+'</p>';}).join("")+'</div>';},
  q:function(b){
    return '<div class="q"><p class="qt"><b>'+b.nr+'.</b> '+mt(b.text)+
      '</p><div class="opts">'+b.options.map(function(o,i){
        return '<span class="opt'+(i===b.correct?" ok":"")+'"><b>'+B[i]+
               ')</b> '+mt(o)+'</span>';}).join("")+'</div></div>';},
  grid:function(b){
    var out='<p class="psec">'+esc(TEKSTI.tabula)+'</p>'+
            '<p class="pnote">'+esc(TEKSTI.pamaciba)+'</p>';
    bloki(b.n).forEach(function(g){
      var nr="",ab="",i;
      for(i=g.no;i<g.lidz;i++){
        nr+='<th>'+(i+1)+'.</th>';
        ab+='<td><span class="abcd">'+B.split("").join(" ")+
            '</span><span class="ans">'+b.letters[i]+'</span></td>';
      }
      for(i=g.lidz-g.no;i<S.ailes;i++){nr+='<th class="tuksa"></th>';
                                       ab+='<td></td>';}
      /* Tabulai ir sava rāmja josla: uz šaura telefona tā drīkst ritināties
         sāniski, bet lapa pati - ne. */
      out+='<div class="tw"><table class="grid"><tr class="nr">'+nr+
           '</tr><tr class="ab">'+ab+'</tr></table></div>';
    });
    return out;},
  key:function(b){
    return '<div class="keys">'+b.items.map(function(x){
      return '<p><b>'+x.nr+'. — '+x.letter+')</b> <span>'+mt(x.text)+
             '</span></p>';}).join("")+'</div>';},
  tbl:function(b){
    return '<table class="tbl"><tr>'+b.head.map(function(h){
      return '<th>'+esc(h)+'</th>';}).join("")+'</tr>'+
      b.rows.map(function(r){return '<tr>'+r.map(function(c){
        return '<td>'+mt(c)+'</td>';}).join("")+'</tr>';}).join("")+
      '</table>';},
  skala:function(b){
    var galva="",rinda="";
    b.skala.forEach(function(x){
      galva+='<th>'+x[0]+'</th>';
      rinda+='<td>'+(x[1]===x[2]?x[1]:x[1]+"–"+x[2])+'</td>';});
    return '<table class="grid"><tr class="nr">'+galva+'</tr><tr class="ab">'+
      rinda+'</tr></table><p class="pnote">'+esc(TEKSTI.skalasParaksts)+
      '</p>';}
};

function html(blocks){
  return blocks.map(function(b){
    return HTML[b.t]?HTML[b.t](b):"";}).join("\n");
}

/* ---------------------------------------------------------------- DOCX */
function punktoti(n){var s="",i;for(i=0;i<n;i++)s+=".";return s;}

/* Atbilžu varianti vienā rindā, ja ietilpst; citādi divās (kā at_common.py) */
function rindas(varianti){
  var apz=varianti.map(function(o,i){return B[i]+") "+o;});
  var visi=apz.join(ATSTARPE);
  return ietilpst(vienkarsi(visi),Z.jaut,S.platums-0.6)
    ? [visi] : [apz.slice(0,2).join(ATSTARPE),apz.slice(2).join(ATSTARPE)];
}
function ietilpst(teksts,izmers,platums){
  return teksts.length*izmers*0.47/28.35<=platums;
}

var DOCXR={
  meta:function(b){return [{parts:gabali(b.text),size:Z.meta,color:K.grey,
                            after:1}];},
  h1:function(b){return [{parts:gabali(b.text),size:Z.h1,bold:true,
                          color:K.navy,after:1}];},
  h2:function(b){return [{parts:gabali(b.text),size:Z.h2,bold:true,
                          color:K.navy,after:4}];},
  note:function(b){return [{parts:gabali(b.text),size:Z.note,italic:true,
                            color:K.grey,after:4}];},
  sec:function(b){return [{parts:gabali(b.text),size:Z.sec,bold:true,
                           color:K.navy,before:8,after:2}];},
  foot:function(b){return [{text:b.text,size:Z.jaut,before:4,after:0}];},
  form:function(){
    return [{t:"tbl",plain:true,widths:S.platumi.veidlapa,rows:[
      {cells:TEKSTI.veidlapa.map(function(){
        return {text:punktoti(32),size:11};})},
      {cells:TEKSTI.veidlapa.map(function(x){
        return {text:x,size:Z.mazs,color:K.grey};})}]},
      {text:"",size:2,after:2}];},
  box:function(b){
    return [{t:"tbl",widths:[S.platums],rows:[{cells:[{fill:K.box,
      paras:[{text:b.title,size:Z.mazs,bold:true,color:K.navy}].concat(
        b.lines.map(function(x){
          return {parts:gabali(x),size:Z.mazs};}))}]}]}];},
  q:function(b){
    var out=[{parts:gabali(b.nr+". "+b.text),size:Z.jaut,after:1}];
    var r=rindas(b.options);
    r.forEach(function(rinda,i){
      out.push({parts:gabali(rinda),size:Z.jaut,left:0.6,
                after:i===r.length-1?3:0});});
    return out;},
  grid:function(b){
    var out=[{text:b.atslega?TEKSTI.atslega:TEKSTI.tabula,size:Z.jaut,
              bold:true,color:K.navy,before:4,after:2}];
    if(!b.atslega)out.push({text:TEKSTI.pamaciba,size:Z.mazs,italic:true,
                            color:K.grey,after:3});
    var w=S.platums/S.ailes;
    bloki(b.n).forEach(function(g){
      var nr=[],ab=[],i;
      for(i=g.no;i<g.lidz;i++){
        nr.push({text:(i+1)+".",size:Z.jaut,bold:true,color:K.white,
                 fill:K.navy,align:"center"});
        ab.push({text:b.atslega?b.letters[i]:B.split("").join("     "),
                 size:12,bold:b.atslega,align:"center"});
      }
      out.push({t:"tbl",widths:Array(S.ailes).fill(w),
                rows:[{cells:nr},{cells:ab,height:0.70}]});
    });
    return out;},
  key:function(b){
    return b.items.map(function(x){
      return {left:0.4,after:0,parts:[
        {text:x.nr+". — "+x.letter+") ",size:Z.vid,bold:true}].concat(
        gabali(x.text).map(function(g){g.size=Z.jaut;g.color=K.grey;
                                       return g;}))};});},
  tbl:function(b){
    return [{t:"tbl",widths:b.widths,rows:[{cells:b.head.map(function(h){
      return {text:h,size:Z.note,bold:true,color:K.white,fill:K.navy};})}]
      .concat(b.rows.map(function(r){
        return {cells:r.map(function(c,i){
          return {parts:gabali(c),size:Z.jaut,bold:i===0,
                  color:i===0?K.navy:(i===2?K.grey:null)};})};}))}];},
  skala:function(b){
    var w=S.platums/b.skala.length;
    return [{t:"tbl",widths:Array(b.skala.length).fill(w),rows:[
      {cells:b.skala.map(function(x){
        return {text:String(x[0]),size:Z.jaut,bold:true,color:K.white,
                fill:K.navy,align:"center"};})},
      {cells:b.skala.map(function(x){
        return {text:x[1]===x[2]?String(x[1]):x[1]+"–"+x[2],size:Z.jaut,
                align:"center"};})}]},
      {text:TEKSTI.skalasParaksts,size:Z.mazs,italic:true,color:K.grey,
       before:2,after:0}];}
};

function docx(blocks){
  var out=[],i;
  for(i=0;i<blocks.length;i++){
    var f=DOCXR[blocks[i].t];
    if(f)out=out.concat(f(blocks[i]));
  }
  return out;
}

/* Bloku tipu tabulas un palīgi ir ārā, lai citi darbu veidi (piemēram,
   divu lapu pārbaudes darbs mat_paper.py) varētu likt klāt savus blokus,
   nepārrakstot jau uzrakstītos (DRY). */
return {blocks:blocks,html:html,docx:docx,gabali:gabali,
        vienkarsi:vienkarsi,HTML:HTML,DOCXR:DOCXR,TEKSTI:TEKSTI,
        bloki:bloki,esc:esc,mt:mt,punkti:punkti,rindas:rindas,
        metaRinda:metaRinda};
})();
"""
