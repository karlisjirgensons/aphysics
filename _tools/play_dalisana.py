# -*- coding: utf-8 -*-
"""Rezultāta pogas: nosūtīšana vecākiem WhatsApp un «Man ir 18+ gadu».

  * «Nosūtīt vecākiem» - https://wa.me/?text=... : WhatsApp atveras ar
    gatavu ziņu un saiti, bērns tikai izvēlas, kam sūtīt. Bez maksas,
    nekāds WhatsApp API nav vajadzīgs.
  * «Man ir 18+ gadu» - ja spēlēja pieaugušais, atver tepat agrās piekļuves
    formu (elements «forma»).
  * «Kopēt saiti».

Saite ved uz r.html blakus spēles lapai (tā pati valoda), un rezultāts ir
saitē (play_rezultats.py). Šis modulis zina tikai šīs pogas (SRP).
"""

JS = r"""
var PD=(function(){
  var T=PT.T;
  function notikums(veids){
    if(window.gtag){gtag("event","play_share",{method:veids});}
  }

  /* Pogas elementā «el» rezultātam «x» ({d,o,s}); «forma» - paslēpts
     agrās piekļuves bloks, ko atver «Man ir 18+ gadu». */
  function pogas(el,x,forma){
    var saite=new URL("r.html?r="+PR.kods(x),location.href).href,
        zina=PT.f(T.zina,{c:PR.raditaji(x).c}),
        wa="https://wa.me/?text="+encodeURIComponent(zina+" "+saite);
    el.innerHTML=
      '<a class="pl-poga pl-galvena pl-wa" href="'+wa+'" target="_blank"'+
        ' rel="noopener" data-k="dalities">'+T.dalities+'</a>'+
      '<div class="pl-otras">'+
      '<button type="button" class="pl-poga" data-k="pieaug">'+
        T.pieaugusais+'</button>'+
      '<button type="button" class="pl-poga" data-k="kopet">'+
        T.kopet+'</button></div>';
    el.querySelector('[data-k="dalities"]').onclick=function(){
      notikums("whatsapp");};
    el.querySelector('[data-k="pieaug"]').onclick=function(){
      forma.hidden=false;
      forma.scrollIntoView({behavior:"smooth",block:"start"});
      if(window.gtag){gtag("event","play_adult");}
    };
    var kop=el.querySelector('[data-k="kopet"]');
    kop.onclick=function(){
      var gatavs=function(){kop.textContent=T.nokopets;notikums("copy");};
      if(navigator.clipboard){
        navigator.clipboard.writeText(saite).then(gatavs,function(){
          prompt("",saite);});
      }else{prompt("",saite);}
    };
  }

  return {pogas:pogas};
})();
"""


def js():
    return JS
