# -*- coding: utf-8 -*-
"""«Cik labi zini bērna matemātiku» gaita: klase -> 5 uzdevumi -> rezultāts.

Atbildes un rezultāts nekur netiek sūtīti; ja vecāks atstāj e-pastu, līdzi
aiziet tikai izvēlētā klase (formas data-klase, play_forma) un valoda.

Šis modulis zina tikai gaitu un rezultāta karti (SRP); uzdevumi -
smart_uzdevumi (SU), solis - aptaujas_solis (AS), teikumi - smart_teksti
(ST), forma - play_forma (PF). Rezultāta saraksts lieto dienas izaicinājuma
stilu (.pl-uzd, play_stils).
"""

import json

# Pareizo skaits -> līmenis; ikona līmenim.
AUGSTS, VIDEJS = 5, 3
IKONAS = {"augsts": "\U0001F3C6", "videjs": "\U0001F4A1",
          "zems": "\U0001F90D"}

JS = r"""
var SM=(function(){
  var T=ST, IK=%(ikonas)s, AUGSTS=%(augsts)d, VIDEJS=%(videjs)d;
  var klase, uzd, atb, i;

  function $(s){return document.querySelector(s);}

  /* Atbildes jaukti; «ok» - pareizās vieta pēc sajaukšanas. */
  function sajauc(u){
    var o=u.o.map(function(h,ix){return {h:h,ok:!ix};});
    for(var j=o.length-1;j>0;j--){
      var r=Math.floor(Math.random()*(j+1)),t=o[j];o[j]=o[r];o[r]=t;}
    return {q:u.q,o:o.map(function(x){return x.h;}),
      ok:o.map(function(x){return x.ok;}).indexOf(true)};
  }

  function sak(k){
    klase=k;uzd=SU[k].map(sajauc);atb=[];i=0;
    $("#sm-sakums").hidden=true;$("#sm-rez").hidden=true;
    $("#sm-jaut").hidden=false;rad();
    if(window.gtag){gtag("event","smart_start",{grade:k});}
  }

  function rad(){
    AS.solis($("#sm-jaut"),{n:i,k:uzd.length,jaut:uzd[i].q,
      opcijas:uzd[i].o,izveleta:atb[i],
      izvele:function(ix){atb[i]=ix;i++;i<uzd.length?rad():beigas();},
      uzAtpakal:function(){i--;rad();}});
  }

  function limenis(c){return c>=AUGSTS?"augsts":c>=VIDEJS?"videjs":"zems";}

  function beigas(){
    var c=uzd.filter(function(u,n){return atb[n]===u.ok;}).length,
        l=limenis(c),v={n:klase,c:c};
    var h='<div class="pl-slava'+(l==="augsts"?' labs':'')+'">'+
      '<span class="pl-ikona">'+IK[l]+'</span>'+
      '<span class="sm-skaits">'+c+'/'+uzd.length+'</span>'+
      '<b>'+T[l+"_v"]+'</b>'+
      '<span class="pl-motiv">'+PT.f(T[l],v)+'</span></div>'+
      '<p class="pl-sk">'+PT.f(T.klase,v)+' · '+PT.f(T.pareizi_no,v)+'</p>'+
      '<ul class="pl-uzd">';
    uzd.forEach(function(u,n){
      var labi=atb[n]===u.ok;
      h+='<li class="'+(labi?'pl-c':'pl-w')+'"><span class="pl-z">'+
        (labi?'✓':'✗')+'</span><span class="pl-ut">'+
        '<span class="pl-ue">'+u.q+'</span>'+
        (labi?'':'<span class="pl-ua">'+PT.f(T.tava,{a:u.o[atb[n]]})+'</span>')+
        '<span class="pl-ua">'+PT.f(T.atbilde,{a:u.o[u.ok]})+'</span>'+
        '</span></li>';
    });
    $(".sm-karte").innerHTML=h+'</ul>';
    $("#sm-cta").textContent=PT.f(T.cta,v);
    Array.prototype.forEach.call(document.querySelectorAll(".pl-forma"),
      function(f){f.setAttribute("data-klase",klase);});
    $("#sm-jaut").hidden=true;$("#sm-rez").hidden=false;
    window.scrollTo(0,0);
    if(window.gtag){gtag("event","smart_finish",{grade:klase,score:c});}
  }

  /* Klašu pogas un «Izmēģināt citu klasi». */
  function sakt(){
    Array.prototype.forEach.call(document.querySelectorAll(".sm-klase"),
      function(b){b.onclick=function(){sak(+b.getAttribute("data-k"));};});
    $("#sm-cita").onclick=function(){
      $("#sm-rez").hidden=true;$("#sm-sakums").hidden=false;
      window.scrollTo(0,0);};
  }

  return {sakt:sakt};
})();
"""


def js():
    return JS % {"ikonas": json.dumps(IKONAS), "augsts": AUGSTS,
                 "videjs": VIDEJS}
