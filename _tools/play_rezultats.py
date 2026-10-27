# -*- coding: utf-8 -*-
"""Dienas izaicinājuma rezultāts: saites kods, rādītāji un rezultāta karte.

Rezultātu nekur neglabā - tas ir pašā saitē (r.html?r=...), jo vietne ir
statiska. Kods ir

    1-20261027-cws-41-k7
    │ │        │   │  └ pārbaudes zīmes (lai saiti nevar viegli «uzlabot»)
    │ │        │   └ kopējais laiks sekundēs
    │ │        └ katrs uzdevums: c pareizi, w nepareizi, s izlaists,
    │ │          t laiks beidzās
    │ └ izaicinājuma diena (pēc tās PU.dienas uzbūvē tos pašus uzdevumus)
    └ VERSIJA

Pārbaudes zīmes nav drošība - tikai šķērslis, lai, mainot vienu ciparu,
saite nesāktu rādīt 100 %.

Šis modulis zina tikai rezultātu (SRP); karti zīmē viena funkcija PR.karte,
ko lieto gan bērna lapa pēc spēles, gan vecāku saņemtā lapa (DRY).
"""

# Ja maina uzdevumus (play_uzdevumi.py), palielini - vecās saites tad
# atzīst par bojātām, nevis rāda citus uzdevumus.
VERSIJA = "1"

# Labākā spēlētāja laiks vienam uzdevumam sekundēs - pret to mēra ātrumu.
# Tas ir mērķis, ne īsts vidējais (kā IQ testu MERKA_LAIKS).
TOP_SEK = 5

UZDEVUMI = 3
LIMITS_SEK = 20

JS = r"""
var PR=(function(){
  var T=PT.T, V=%(versija)s, TOP=%(top)d, N=%(n)d, MAX=%(max)d;

  function zimes(s){
    var h=7;
    for(var i=0;i<s.length;i++){h=(h*31+s.charCodeAt(i)+17)%%1679616;}
    return ("00"+(h%%1296).toString(36)).slice(-2);
  }

  /* {d:"20261027", o:"cws", s:41} -> kods saitei */
  function kods(x){
    var b=[V,x.d,x.o,x.s].join("-");
    return b+"-"+zimes(b);
  }

  /* kods -> {d,o,s} vai null, ja saite bojāta */
  function lasi(k){
    var p=String(k||"").split("-");
    if(p.length!==5||p[0]!==V||zimes(p.slice(0,4).join("-"))!==p[4]){
      return null;}
    if(!/^\d{8}$/.test(p[1])||!new RegExp("^[cwst]{"+N+"}$").test(p[2])||
       !/^\d{1,3}$/.test(p[3])||+p[3]>N*MAX){return null;}
    return {d:p[1],o:p[2],s:+p[3]};
  }

  function viens(x){return Math.round(x*10)/10;}
  function skaits(o,ch){return o.split("").filter(function(c){
    return ch.indexOf(c)>=0;}).length;}

  /* Rādītāji: precizitāte - pareizo daļa no visiem uzdevumiem, ātrums -
     labākā spēlētāja laiks pret tavu laiku vienai pareizai atbildei
     (100 %% - tikpat ātri vai ātrāk). */
  function raditaji(x){
    var c=skaits(x.o,"c"),uz=c?x.s/c:0;
    return {c:c,precizitate:viens(c/N*100),
      atrums:c?Math.min(100,Math.round(TOP/Math.max(uz,1)*100)):null,
      uzPareizo:viens(uz)};
  }

  function proc(x){return x===null?"—":String(x).replace(".",
    document.documentElement.lang==="lv"?",":".")+"%%";}

  var ZIME={c:"✓",w:"✗",s:"↷",t:"⏱"},
      KAS={c:T.pareizi,w:T.nepareizi,s:T.izlaists,t:T.laiks_beidzas};

  function rutina(nos,vert,sik,klase){
    return '<div class="pl-r '+klase+'"><span class="pl-rn">'+nos+
      '</span><b>'+vert+'</b><span class="pl-rs">'+sik+'</span></div>';
  }

  /* Rezultāta karte elementā «el»: rādītāji un uzdevumi ar atbildēm. */
  function karte(el,x){
    var m=raditaji(x),uzd=PU.dienas(x.d);
    var h='<div class="pl-rr">'+
      rutina(T.precizitate,proc(m.precizitate),PT.f(T.no_3,{c:m.c}),"r1")+
      rutina(T.atrums,proc(m.atrums),T.pret_labako,"r3")+
      '</div><p class="pl-sk">'+
      (m.c?PT.f(T.atruma_skaidrojums,{top:TOP,tavs:m.uzPareizo}):"")+
      ' '+PT.f(T.kopa_laiks,{s:x.s})+'</p><ol class="pl-uzd">';
    uzd.forEach(function(u,i){
      var o=x.o.charAt(i);
      h+='<li class="pl-'+o+'"><span class="pl-z" title="'+KAS[o]+'">'+
        ZIME[o]+'</span><span class="pl-ut"><span class="pl-uq">'+u.q+
        '</span><span class="pl-ue">'+u.e+'</span><span class="pl-ua">'+
        PT.f(T.pareiza_atbilde,{a:u.opts[u.ok]})+'</span></span></li>';
    });
    el.innerHTML=h+'</ol>';
    return m;
  }

  return {kods:kods,lasi:lasi,raditaji:raditaji,karte:karte};
})();
"""


def js():
    return JS % {"versija": '"%s"' % VERSIJA, "top": TOP_SEK,
                 "n": UZDEVUMI, "max": LIMITS_SEK}
