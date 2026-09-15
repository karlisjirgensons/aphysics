# -*- coding: utf-8 -*-
"""Summatīvā pārbaudes darba lapa (divas lapas) - JavaScript teksts.

Formatīvais darbs ir viena lapa ar jautājumiem A-D, un to jau prot fd_paper.py.
Pārbaudes darbam klāt nāk uzdevumi ar darba vietu, un tas ir garāks par vienu
lapu, tāpēc te ir tikai tas, kā fd_paper.py vēl nav (SRP):

    PAPER_PD.blocks(dati, darbs, atslega) - saturs -> lapas modelis
    PAPER_PD.html(blocks)  /  PAPER_PD.docx(blocks)

Jaunie bloku tipi: «uzd» (uzdevuma virsraksts ar punktiem), «para» (uzdevuma
teksts), «rindas» (ierakstāmās rindas ar rāmi), «jaut» (apakšjautājumi),
«vieta» (tukša darba vieta zīmējumam un risinājumam), «vert» (vērtējuma aile)
un «saraksts» (atbilžu vai kritēriju saraksts skolotājam). Visu pārējo -
galveni, ATGĀDNI, testa jautājumus, atbilžu tabulu, skalu - zīmē fd_paper.py
attēlotāji, kurus te tikai papildina (DRY).

Lapu dala bloks {t:"pb"}: Word failā tas ir lappuses pārtraukums, ekrānā -
jauna balta lapa (sk. mat_page.py).
"""

JS = r"""
window.PAPER_PD=(function(){
"use strict";
var P=window.PAPER,S=window.FD_STILS,K=S.krasas,Z=S.izmeri,B=S.burti;
var esc=P.esc,mt=P.mt,gabali=P.gabali;

var TEKSTI={
  uzdevums:"uzdevums",
  tests:"Tests",
  testaNorade:"Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "+
              "atbildes burtu!",
  turpinajums:"2. lapa",
  vertejums:"Vērtējums",
  vertejumaGalva:["Kopā","Balle"],
  maks:"Maksimālais punktu skaits par uzdevumu:  ",
  darbaVieta:"Risinājums un zīmējums",
  skolotajam:"Atbildes un vērtēšana — SKOLOTĀJAM",
  pareizas:"1. uzdevums. Tests — pareizās atbildes",
  parbauda:"Ko darbs pārbauda",
  skala:"Vērtēšanas skala (kopā %d punkti)",
  parbaudaGalva:["Uzd.","Pārbaudāmais sasniedzamais rezultāts","P."],
  punktuZime:" p."
};
var INDEKSI="abcdefgh";

function pk(n){return "("+n+TEKSTI.punktuZime+")";}

/* ------------------------------------------------------------- modelis */
function galvene(dati,darbs,apaks){
  return [{t:"meta",text:P.metaRinda(dati)},
          {t:"h1",text:dati.virsraksts+" Nr. "+dati.nr+".  "+dati.nosaukums},
          {t:"h2",text:apaks}];
}

/* Viena uzdevuma saturs. Uzbūve ir tā pati, ko lieto Word darba lapas
   (pd_common.py), tāpēc uzdevumu apraksts satura failā ir vienāds. */
function uzdevums(out,nr,u,punkti){
  out.push({t:"uzd",nr:nr,virs:u.virs,punkti:punkti});
  if(u.tips==="parveide"){
    if(u.note)out.push({t:"note",text:u.note});
    out.push({t:"rindas",items:u.rindas.map(function(r,i){
      return INDEKSI[i]+")   "+r[0];})});
  }else if(u.tips==="aprekins"){
    out.push({t:"para",text:u.teksts});
    out.push({t:"vieta",augstums:u.vieta,hint:u.hint||TEKSTI.darbaVieta});
  }else{
    out.push({t:"para",text:u.ievads});
    out.push({t:"jaut",items:u.jaut.map(function(j,i){
      return (i+1)+") "+j[0]+"  "+pk(j[1]);})});
    out.push({t:"vieta",augstums:u.vieta,hint:u.hint||TEKSTI.darbaVieta});
  }
}

function lapa(out,dati,darbs,nr){
  darbs.uzdevumi.forEach(function(x){
    if(x.lapa===nr)uzdevums(out,x.nr,x.u,x.punkti);
  });
}

function blocks(dati,darbs,atslega){
  var out=[],n=darbs.tests.length;
  if(atslega)return atbildes(dati,darbs);
  out=out.concat(galvene(dati,darbs,
    dati.kopa+" punkti  ·  "+dati.laiks+" minūtes  ·  variants "+
    darbs.kods));
  out.push({t:"note",text:dati.ievads});
  out.push({t:"form"});
  out.push({t:"box",title:P.TEKSTI.atgadne,lines:dati.atgadne});
  out.push({t:"uzd",nr:1,virs:TEKSTI.tests,punkti:n});
  out.push({t:"note",text:TEKSTI.testaNorade});
  darbs.tests.forEach(function(x,i){
    out.push({t:"q",nr:i+1,text:x.teksts,options:x.varianti,
              correct:x.pareizais});});
  lapa(out,dati,darbs,1);
  out.push({t:"pb"});
  out=out.concat(galvene(dati,darbs,
    TEKSTI.turpinajums+"  ·  variants "+darbs.kods));
  lapa(out,dati,darbs,2);
  out.push({t:"vert",punkti:[n].concat(darbs.uzdevumi.map(function(x){
    return x.punkti;}))});
  return out;
}

function atbildes(dati,darbs){
  var out=galvene(dati,darbs,TEKSTI.skolotajam),n=darbs.tests.length;
  out.push({t:"note",text:dati.apraksts+"  Variants "+darbs.kods+
    ".  Izpildes laiks — "+dati.laiks+" minūtes, kopā "+dati.kopa+
    " punkti."});
  out.push({t:"sec",text:TEKSTI.pareizas});
  out.push({t:"key",items:darbs.tests.map(function(x,i){
    return {nr:i+1,letter:darbs.burti[i],text:x.varianti[x.pareizais]};})});
  darbs.uzdevumi.forEach(function(x){
    out.push({t:"sec",text:x.nr+". "+TEKSTI.uzdevums+". "+x.u.virs+"  "+
      pk(x.punkti)});
    out.push({t:"saraksts",items:atbilzuRindas(x.u)});
  });
  out.push({t:"sec",text:TEKSTI.parbauda});
  out.push({t:"tbl",widths:S.platumi.struktura,head:TEKSTI.parbaudaGalva,
    rows:[["1.",darbs.tests.map(function(x){return x.sr;}).join("; "),
           String(n)]].concat(darbs.uzdevumi.map(function(x){
      return [x.nr+".",x.sr,String(x.punkti)];}))});
  out.push({t:"sec",text:TEKSTI.skala.replace("%d",dati.kopa)});
  out.push({t:"skala",skala:dati.skala});
  return out;
}

function atbilzuRindas(u){
  /* Pārveides uzdevumam atbilde ir katrai rindai, pārējiem - saraksts. */
  if(u.tips==="parveide")
    return u.rindas.map(function(r,i){
      return INDEKSI[i]+")  "+r[0]+"   →   "+r[1];});
  return u.atbildes||u.kriteriji||[];
}

/* ---------------------------------------------------------------- HTML */
function kopija(avots){
  var out={},k;
  for(k in avots)if(Object.prototype.hasOwnProperty.call(avots,k))
    out[k]=avots[k];
  return out;
}

var HTML=kopija(P.HTML);

HTML.uzd=function(b){
  return '<p class="puzd"><b>'+b.nr+'. '+esc(TEKSTI.uzdevums)+'.</b> '+
    mt(b.virs)+' <span class="pp">'+esc(pk(b.punkti))+'</span></p>';};
HTML.para=function(b){return '<p class="ptext">'+mt(b.text)+'</p>';};
HTML.rindas=function(b){
  return '<div class="rindas">'+b.items.map(function(x){
    return '<p>'+mt(x)+'</p>';}).join("")+'</div>';};
HTML.jaut=function(b){
  return '<div class="jaut">'+b.items.map(function(x){
    return '<p>'+mt(x)+'</p>';}).join("")+'</div>';};
HTML.vieta=function(b){
  return '<div class="vieta" style="min-height:'+b.augstums+'cm">'+
    '<span class="vh">'+esc(b.hint)+'</span></div>';};
HTML.vert=function(b){
  var galva="",rinda="",i;
  for(i=0;i<b.punkti.length;i++){
    galva+='<th>'+(i+1)+'. uzd.</th>';rinda+='<td></td>';}
  TEKSTI.vertejumaGalva.forEach(function(g){
    galva+='<th>'+esc(g)+'</th>';rinda+='<td></td>';});
  return '<p class="psec">'+esc(TEKSTI.vertejums)+'</p>'+
    '<div class="tw"><table class="grid"><tr class="nr">'+galva+
    '</tr><tr class="ab vertr">'+rinda+'</tr></table></div>'+
    '<p class="pnote">'+esc(TEKSTI.maks)+b.punkti.map(function(p,i){
      return (i+1)+". uzd. — "+p+TEKSTI.punktuZime;}).join("  ·  ")+'</p>';};
HTML.saraksts=function(b){
  return '<div class="atbsar">'+b.items.map(function(x){
    return '<p>'+mt(x)+'</p>';}).join("")+'</div>';};
HTML.pb=function(){return "";};

function html(blocks){
  return blocks.map(function(b){
    return HTML[b.t]?HTML[b.t](b):"";}).join("\n");
}

/* ---------------------------------------------------------------- DOCX */
var DOCXR=kopija(P.DOCXR);

DOCXR.uzd=function(b){
  return [{size:Z.sec,bold:true,color:K.navy,before:8,after:2,
           parts:[{text:b.nr+". "+TEKSTI.uzdevums+". "+b.virs+"   "+
                        pk(b.punkti)}]}];};
DOCXR.para=function(b){
  return [{parts:gabali(b.text),size:11,after:3}];};
DOCXR.rindas=function(b){
  return [{t:"tbl",widths:[S.platums],rows:b.items.map(function(x){
    return {height:0.85,cells:[{parts:gabali(x),size:11}]};})}];};
DOCXR.jaut=function(b){
  return b.items.map(function(x,i){
    return {parts:gabali(x),size:Z.jaut,left:0.4,
            after:i===b.items.length-1?3:1};});};
DOCXR.vieta=function(b){
  return [{t:"tbl",widths:[S.platums],rows:[{height:b.augstums,
    cells:[{text:b.hint,size:Z.mazs,color:K.grey}]}]}];};
DOCXR.vert=function(b){
  var galva=[],rinda=[],i,n=b.punkti.length+TEKSTI.vertejumaGalva.length;
  var w=S.platums/n;
  for(i=0;i<b.punkti.length;i++){
    galva.push({text:(i+1)+". uzd.",size:Z.mazs,bold:true,color:K.white,
                fill:K.navy,align:"center"});
    rinda.push({text:"",size:11});}
  TEKSTI.vertejumaGalva.forEach(function(g){
    galva.push({text:g,size:Z.mazs,bold:true,color:K.white,fill:K.navy,
                align:"center"});
    rinda.push({text:"",size:11});});
  return [{t:"tbl",widths:Array(n).fill(w),
           rows:[{cells:galva},{cells:rinda,height:1.0}]},
          {text:TEKSTI.maks+b.punkti.map(function(p,i){
             return (i+1)+". uzd. — "+p+TEKSTI.punktuZime;}).join("  ·  "),
           size:Z.mazs,color:K.grey,before:2,after:0}];};
DOCXR.saraksts=function(b){
  return b.items.map(function(x){
    return {parts:gabali(x),size:Z.jaut,left:0.4,after:1};});};
DOCXR.pb=function(){return [{t:"pb"}];};

function docx(blocks){
  var out=[],i;
  for(i=0;i<blocks.length;i++){
    var f=DOCXR[blocks[i].t];
    if(f)out=out.concat(f(blocks[i]));
  }
  return out;
}

return {blocks:blocks,html:html,docx:docx};
})();
"""
