# -*- coding: utf-8 -*-
"""Vecāku aptauja: 5 jautājumi «cik bieži», rezultāts pret tipisku vecāku.

Visiem jautājumiem ir viena skala (BIEZUMS): «gandrīz katru dienu» = 3
punkti ... «reti» = 0. Tipiskā atbilde katram jautājumam ir vidējā
(mediānas) atbilde lielos ģimeņu pētījumos (OECD PISA vecāku aptauja,
Scholastic Kids & Family Reading Report) - aptuvena, apzināti pieticīga.
Ja nāk labāki dati, maina tikai JAUTAJUMI otro skaitli.

Atbildes nekur netiek sūtītas un glabātas - tabulā nonāk tikai e-pasts
un valoda, ja vecāks to atstāj (play_forma, avots «parent»).

Šis modulis zina tikai jautājumus, punktus un rezultāta karti (SRP);
solis - aptaujas_solis, teikumi - vecaki_teksti, forma - play_forma,
lapa - vecaki_vietne.
"""

import json

# (jautājuma atslēga vecaki_teksti «q_..»/«i_..», tipiskās atbildes indekss
# BIEZUMS: 0 = gandrīz katru dienu, 1 = dažas reizes nedēļā, ...).
JAUTAJUMI = [("lasit", 1), ("spelet", 1), ("macities", 1), ("runat", 0),
             ("est", 1)]

# Atbildes indekss -> punkti; teksti ir vecaki_teksti «b0»..«b3».
BIEZUMS = [3, 2, 1, 0]

# Cik punktu virs/zem tipiskā jau ir «virs» / «zem», nevis «līdzīgi».
SLIEKSNIS = 2

JS = r"""
var VA=(function(){
  var T=VT, J=%(jautajumi)s, B=%(biezums)s, SL=%(slieksnis)d;
  var MAX=J.length*B[0], atb=[], i=0;

  function $(s){return document.querySelector(s);}
  function punkti(ix){return B[ix];}
  function summa(ixi){return ixi.reduce(function(s,x){return s+punkti(x);},0);}
  var TIP=summa(J.map(function(j){return j[1];}));

  function sak(){
    $("#vk-sakums").hidden=true;$("#vk-jaut").hidden=false;
    atb=[];i=0;rad();
    if(window.gtag){gtag("event","parent_quiz_start");}
  }

  function rad(){
    AS.solis($("#vk-jaut"),{
      n:i,k:J.length,
      jaut:T["q_"+J[i][0]],opcijas:B.map(function(_,ix){return T["b"+ix];}),
      izveleta:atb[i],
      izvele:function(ix){atb[i]=ix;i++;i<J.length?rad():beigas();},
      uzAtpakal:function(){i--;rad();}});
  }

  /* Kopsumma pret tipisko -> «virs» | «lidz» | «zem». */
  function limenis(s){
    return s-TIP>=SL?"virs":TIP-s>=SL?"zem":"lidz";
  }

  function josla(vards,s,kl){
    return '<div class="vk-rinda'+kl+'"><span>'+vards+'</span>'+
      '<div class="vk-j"><i style="width:'+(s/MAX*100)+'%%"></i></div>'+
      '<b>'+s+'/'+MAX+'</b></div>';
  }

  function beigas(){
    var s=summa(atb),l=limenis(s),
        ikona={virs:"💛",lidz:"🌱",zem:"🤍"}[l];
    var h='<div class="pl-slava'+(l==="virs"?' labs':'')+'">'+
      '<span class="pl-ikona">'+ikona+'</span>'+
      '<b>'+T[l+"_v"]+'</b>'+
      '<span class="pl-motiv">'+T[l]+'</span></div>'+
      '<div class="vk-salid">'+josla(T.tu,s,"")+josla(T.tipisks,TIP," tip")+
      '</div><ul class="vk-ier">';
    J.forEach(function(j,n){
      var labi=punkti(atb[n])>=punkti(j[1]);
      h+='<li class="'+(labi?'vk-labi':'')+'"><span class="vk-z">'+
        (labi?'✓':'•')+'</span><span class="vk-it">'+
        '<b>'+T["i_"+j[0]]+'</b>'+
        '<span>'+T.tu+': '+T["b"+atb[n]]+'</span>'+
        '<span class="vk-dim">'+PT.f(T.vairums,{a:T["b"+j[1]]})+'</span>'+
        '</span></li>';
    });
    $(".vk-karte").innerHTML=h+'</ul>';
    $("#vk-jaut").hidden=true;$("#vk-rez").hidden=false;
    window.scrollTo(0,0);
    if(window.gtag){gtag("event","parent_quiz_finish",{score:s,level:l});}
  }

  return {sak:sak};
})();
"""


def js():
    return JS % {"jautajumi": json.dumps(JAUTAJUMI),
                 "biezums": json.dumps(BIEZUMS),
                 "slieksnis": SLIEKSNIS}
