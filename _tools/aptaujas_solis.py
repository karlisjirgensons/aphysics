# -*- coding: utf-8 -*-
"""Viens aptaujas solis: «2. jautājums no 5», progresa josla, jautājums un
atbilžu pogas vienā kolonnā, pēc vajadzības «Atpakaļ».

To pašu soli lieto vecāku aptauja (parent/) un «Cik labi zini bērna
matemātiku» (smart/) - jautājumi un rezultāts katrai ir savi, bet solis
viens (DRY). Šis modulis zina tikai, kā solis izskatās un ko tas paziņo
(SRP) un tā divus teikumus. Kartītes, pogas un josla ir play_stils.
"""

import json

import valoda

TEKSTI = {
    "en": {"jautajums": "Question {n} of {k}", "atpakal": "Back"},
    "lv": {"jautajums": "{n}. jautājums no {k}", "atpakal": "Atpakaļ"},
}

CSS = """
.ap-rez{display:grid;gap:1rem}
.ap-jt{margin:.2rem 0 1rem;color:var(--fg);font-family:var(--font-h);
  font-weight:600;line-height:1.35;font-size:clamp(1.15rem,5vw,1.4rem)}
.pl-opt.ap-opt{grid-template-columns:1fr}
.pl-opt.ap-opt button{min-height:3.2rem;padding:.6rem 1rem;text-align:left;
  font-size:clamp(1rem,4.4vw,1.1rem)}
.pl-opt.ap-opt button.on{border-color:var(--violet);background:var(--surface2)}
"""

JS = r"""
var AS={T:/*TEKSTI*/,
  /* o: {n: jautājuma nr (no 0), k: cik pavisam, jaut: HTML,
         opcijas: [HTML], izveleta: indekss vai undefined,
         izvele: function(ix), uzAtpakal: function()}
     «Atpakaļ» ir no 2. jautājuma. */
  solis:function(vieta,o){
    vieta.innerHTML=
      '<div class="pl-augsa"><span></span></div>'+
      '<div class="pl-josla"><i></i></div>'+
      '<p class="ap-jt"></p><div class="pl-opt ap-opt"></div>'+
      (o.n?'<button type="button" class="pl-izlaist"></button>':'');
    vieta.querySelector(".pl-augsa span").textContent=
      PT.f(AS.T.jautajums,{n:o.n+1,k:o.k});
    vieta.querySelector(".pl-josla i").style.width=(o.n/o.k*100)+"%";
    vieta.querySelector(".ap-jt").innerHTML=o.jaut;
    var opt=vieta.querySelector(".ap-opt");
    o.opcijas.forEach(function(h,ix){
      var b=document.createElement("button");
      b.type="button";b.innerHTML=h;
      if(o.izveleta===ix){b.className="on";}
      b.onclick=function(){o.izvele(ix);};
      opt.appendChild(b);
    });
    var atp=vieta.querySelector(".pl-izlaist");
    if(atp){atp.textContent=AS.T.atpakal;atp.onclick=o.uzAtpakal;}
  }
};
"""


def css():
    return CSS


def js():
    """AS ar tagadējās valodas teikumiem; vajag PT (play_teksti) - PT.f."""
    return JS.replace("/*TEKSTI*/", json.dumps(TEKSTI[valoda.tagad()],
                                                ensure_ascii=False))
