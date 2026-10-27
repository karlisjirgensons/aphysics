# -*- coding: utf-8 -*-
"""Dienas izaicinājuma spēle: 3 uzdevumi, minūte katram, poga «Izlaist».

Laiks beidzas -> uzdevums skaitās «t» un spēle iet tālāk. Pēc atbildes
uz brīdi parāda, vai pareizi (un pareizo atbildi), tad nākamais uzdevums.
Beigās rezultāta karte (PR.karte) un pogas nosūtīšanai (PD.pogas).

Šis modulis zina tikai spēles gaitu (SRP); uzdevumi, rezultāts un dalīšanās
ir savos moduļos.
"""

from play_rezultats import LIMITS_SEK

JS = r"""
var PS=(function(){
  var T=PT.T, LIMITS=%(limits)d, PAUZE=1100;

  function $(s){return document.querySelector(s);}

  function sak(){
    var d=PU.sodiena(),uzd=PU.dienas(d),o="",sek=0,i=0,
        vieta=$("#pl-spele"),sakums,taimeris,slegts;
    $("#pl-sakums").hidden=true;
    vieta.hidden=false;
    if(window.gtag){gtag("event","play_start",{day:d});}
    vieta.innerHTML=
      '<div class="pl-augsa"><span class="pl-nr"></span>'+
        '<span class="pl-laiks"></span></div>'+
      '<div class="pl-josla"><i></i></div>'+
      '<p class="pl-q"></p><div class="pl-e"></div>'+
      '<div class="pl-opt"></div>'+
      '<p class="pl-fb" aria-live="polite"></p>'+
      '<button type="button" class="pl-izlaist">'+T.izlaist+'</button>';
    var nr=vieta.querySelector(".pl-nr"),laiks=vieta.querySelector(".pl-laiks"),
        josla=vieta.querySelector(".pl-josla i"),opt=vieta.querySelector(".pl-opt"),
        fb=vieta.querySelector(".pl-fb"),izl=vieta.querySelector(".pl-izlaist");

    function rad(){
      var u=uzd[i];slegts=false;
      nr.textContent=PT.f(T.uzdevums,{n:i+1});
      vieta.querySelector(".pl-q").innerHTML=u.q;
      vieta.querySelector(".pl-e").innerHTML=u.e;
      fb.textContent="";fb.className="pl-fb";
      opt.innerHTML=u.opts.map(function(v,j){
        return '<button type="button" data-j="'+j+'">'+v+'</button>';}).join("");
      izl.disabled=false;
      sakums=Date.now();tiksk();
      taimeris=setInterval(tiksk,200);
    }

    function tiksk(){
      var atl=Math.max(0,LIMITS-(Date.now()-sakums)/1000);
      laiks.textContent=Math.ceil(atl)+" s";
      josla.style.width=(atl/LIMITS*100)+"%%";
      laiks.classList.toggle("maz",atl<=5);
      if(atl<=0){beigt("t",-1);}
    }

    /* Uzdevuma beigas: «k» - c/w/s/t, «j» - izvēlētā poga vai -1. */
    function beigt(k,j){
      if(slegts){return;}
      slegts=true;clearInterval(taimeris);
      sek+=Math.min(LIMITS,Math.round((Date.now()-sakums)/1000));
      o+=k;izl.disabled=true;
      var u=uzd[i],pogas=opt.querySelectorAll("button");
      Array.prototype.forEach.call(pogas,function(b){b.disabled=true;});
      if(k!=="s"){
        pogas[u.ok].classList.add("ok");
        if(k==="w"){pogas[j].classList.add("kluda");}
        fb.textContent=k==="c"?T.pareizi:k==="w"?T.nepareizi:T.laiks_beidzas;
        fb.className="pl-fb "+(k==="c"?"ok":"kluda");
      }
      setTimeout(nakamais,k==="s"?0:PAUZE);
    }

    function nakamais(){
      i++;
      if(i<uzd.length){rad();}else{gals({d:d,o:o,s:sek});}
    }

    opt.addEventListener("click",function(e){
      var b=e.target.closest("button");
      if(!b||slegts){return;}
      var j=+b.getAttribute("data-j");
      beigt(j===uzd[i].ok?"c":"w",j);
    });
    izl.onclick=function(){beigt("s",-1);};
    rad();
  }

  function gals(x){
    $("#pl-spele").hidden=true;
    var r=$("#pl-rezultats");r.hidden=false;
    var m=PR.karte(r.querySelector(".pl-karte"),x);
    var forma=$("#pl-pieaug");
    forma.querySelector("form").setAttribute("data-r",PR.kods(x));
    PD.pogas(r.querySelector(".pl-dalities"),x,forma);
    if(window.gtag){gtag("event","play_finish",
      {day:x.d,correct:m.c,seconds:x.s});}
    window.scrollTo(0,0);
  }

  return {sak:sak};
})();
"""


def js():
    return JS % {"limits": LIMITS_SEK}
