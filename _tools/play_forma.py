# -*- coding: utf-8 -*-
"""«Saņem agrāko piekļuvi» - vecāka e-pasta forma.

E-pasts aiziet uz Google Sheet caur Google Apps Script tīmekļa lietotni
(leads/apps_script.gs). Cilvēks Google nekad neredz: forma nosūta datus
fonā (fetch, mode "no-cors" - Apps Script atbildi lasīt nevar, bet rinda
tabulā parādās), un tajā pašā vietā parādās «Paldies!». Bez maksas; Apps
Script dienas limiti ir tūkstošos, mums vajag ~100.

ADRESE ir Apps Script lietotnes adrese (.../exec). Kamēr tā ir tukša, forma
saka «Neizdevās nosūtīt» un konsolē paskaidro, kāpēc.

Šis modulis zina tikai formu (SRP); to pašu formu lieto spēles lapa un
rezultāta lapa (DRY) - atšķiras tikai «avots», kas aiziet līdzi uz tabulu.
"""

import html

from play_teksti import teksts

# Google Apps Script tīmekļa lietotnes adrese (Deploy -> Web app -> URL).
ADRESE = ("https://script.google.com/macros/s/AKfycbzvB7sitENtYXHtWkIeWUJtB3hR4r1m_hChhWsbVROPrMsJ6-38dS2iyyrgdnEBeXHTKw/exec")

HTML = """<form class="pl-forma" data-avots="%(avots)s" novalidate>
<label class="pl-sl" for="pl-ep-%(avots)s">%(epasts)s</label>
<div class="pl-ievade">
<input id="pl-ep-%(avots)s" type="email" name="epasts" required
 autocomplete="email" inputmode="email" placeholder="%(epasts)s">
<button type="submit" class="pl-poga pl-galvena">%(poga)s</button>
</div>
<input class="pl-sl" type="text" name="web" tabindex="-1" autocomplete="off"
 aria-hidden="true">
<p class="pl-piekr">%(piekrisana)s</p>
<p class="pl-zina" role="status" aria-live="polite"></p>
</form>"""


def render(avots):
    """Forma; «avots» (play | rezultats) aiziet uz tabulu līdzi e-pastam."""
    e = lambda k: html.escape(teksts(k))                       # noqa: E731
    return HTML % {"avots": avots, "epasts": e("epasts"),
                   "poga": e("pieteikties"), "piekrisana": e("piekrisana")}


JS = r"""
var PF=(function(){
  var T=PT.T, ADRESE=%(adrese)s, ATSLEGA="calcubo-agri";
  var RE=/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

  function paldies(f){
    f.querySelector(".pl-ievade").hidden=true;
    f.querySelector(".pl-piekr").hidden=true;
    var z=f.querySelector(".pl-zina");
    z.textContent=T.paldies;z.className="pl-zina ok";
  }

  /* Visas formas lapā; «r» - rezultāta kods, ja lapa to zina. */
  function sak(r){
    var formas=document.querySelectorAll(".pl-forma");
    var bija=false;
    try{bija=localStorage.getItem(ATSLEGA)==="1";}catch(e){}
    Array.prototype.forEach.call(formas,function(f){
      if(bija){paldies(f);return;}
      f.addEventListener("submit",function(ev){
        ev.preventDefault();
        var ep=f.epasts.value.trim(),z=f.querySelector(".pl-zina"),
            poga=f.querySelector("button");
        if(f.web.value){paldies(f);return;}
        if(!RE.test(ep)){z.textContent=T.slikts_epasts;z.className="pl-zina kluda";
          f.epasts.focus();return;}
        if(!ADRESE){console.warn("play_forma.ADRESE nav iestatīta");
          z.textContent=T.nesanaca;z.className="pl-zina kluda";return;}
        poga.disabled=true;z.textContent="";
        fetch(ADRESE,{method:"POST",mode:"no-cors",
          body:new URLSearchParams({epasts:ep,avots:f.getAttribute("data-avots"),
            valoda:document.documentElement.lang,
            r:f.getAttribute("data-r")||r||""})})
        .then(function(){
          try{localStorage.setItem(ATSLEGA,"1");}catch(e){}
          if(window.gtag){gtag("event","lead_submit",
            {source:f.getAttribute("data-avots")});}
          Array.prototype.forEach.call(formas,paldies);
        },function(){
          poga.disabled=false;
          z.textContent=T.nesanaca;z.className="pl-zina kluda";
        });
      });
    });
  }

  return {sak:sak};
})();
"""


def js():
    return JS % {"adrese": '"%s"' % ADRESE}
