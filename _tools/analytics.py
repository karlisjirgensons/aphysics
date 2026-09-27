# -*- coding: utf-8 -*-
"""Google Analytics skaitītājs - viena vieta, kur zināms mērījuma ID (SRP).

Lapas aug no pieciem veidņiem (site_index.py, deck_page.py, math_lapa.py,
mat_page.py, fd_page.py). Katrs savu <head> raksta pats, bet skaitītāju
ieliek ar %(analytics)s, tāpēc ID un skripts nedzīvo vairākās vietās (DRY).

Divas lietas skripts izlemj pats, lai tās nebūtu jāraksta katrā lapā:

  sadaļa  - no adreses. Pēc noklusējuma tā ir pirmā mape (Dabaszinibas,
            Fizika_1, PD_generate) - mapes nosaukums jau ir sadaļas
            nosaukums, tāpēc būvētājam tas nav jāatkārto. Dažām mapēm ir
            savs vārds (SADALAS): IQ testi ir sava sadaļa, lai gan dzīvo
            zem Math, angļu vietne (en/...) ir atsevišķi, un matemātikā
            katra klase ir sava rinda («Matemātika · 5. klase»). GA4 to
            saņem kā "content_group", un atskaitē katra sadaļa ir viena
            rinda - tieši tas, ko vajag, lai redzētu, cik cilvēku iet uz
            kuru priekšmetu.

  vai skaitīt - tikai īstajā vietnē. Lapas atver arī lokāli (check_stunda.py
            vienā piegājienā izspēlē simtiem stundu no file://), un tie nav
            apmeklētāji; ja tos skaitītu, atskaite melotu. Kamēr adrese nav
            īstā, skripts pat nelejupielādējas.

IQ testi vēl sūta notikumus «iq_start» un «iq_finish» (iq_bloks.py) ar
rezultātu - tos GA rāda sadaļā Events.
"""

import json
import os

import courses

# Mērījuma ID no Google Analytics (Analytics/analytics_google.txt).
MERIJUMS = "G-D08NE6MVZ7"

# Sākumlapai adresē nav mapes - tai vajag vārdu, citādi sadaļa būtu tukša.
SAKUMS = "Sākums"

# Adreses sākums (mapes, atdalītas ar «/») -> sadaļas vārds. Uzvar garākais
# sakritušais sākums. «*» nozīmē: vārdam piekabina nākamo mapi, ja tā ir
# (Math/5. klase/... -> «Matemātika · 5. klase»).
SADALAS = {
    "en": "EN · Home",
    "en/IQ": "EN · IQ tests",
    "Math": "Matemātika*",
    "Math/IQ": "IQ testi",
}


def domens():
    """Vietnes adrese - to zina CNAME, tāpēc te to neraksta vēlreiz (DRY).

    Ja CNAME nav (vietne stāv tikai uz github.io), atgriež tukšu virkni:
    tad skaitītājs strādā jebkurā tīmekļa adresē, bet joprojām ne file://.
    """
    try:
        with open(os.path.join(courses.SITE_ROOT, "CNAME"),
                  encoding="utf-8") as f:
            return f.read().strip()
    except OSError:
        return ""


HEAD = """<script>
(function(){
  var DOM=%(domens)s, ID=%(id)s, SAD=%(sadalas)s;
  /* Lokāli atvērta lapa nav apmeklējums. */
  if(location.protocol.indexOf("http")!==0){return;}
  if(DOM&&location.hostname!==DOM&&location.hostname!=="www."+DOM){return;}
  var dl=window.dataLayer=window.dataLayer||[];
  function gtag(){dl.push(arguments);}
  window.gtag=gtag;
  var s=document.createElement("script");
  s.async=true;
  s.src="https://www.googletagmanager.com/gtag/js?id="+ID;
  document.head.appendChild(s);
  /* Sadaļa: garākais SAD sākums vai pirmā mape; sākumlapai mapes nav. */
  var m=location.pathname.split("/").slice(1,-1).map(function(x){
    try{return decodeURIComponent(x);}catch(e){return x;}});
  var grupa=m.length?m[0]:%(sakums)s;
  for(var n=m.length;n>0;n--){
    var v=SAD[m.slice(0,n).join("/")];
    if(v){grupa=v.slice(-1)==="*"?v.slice(0,-1)+(m[n]?" · "+m[n]:""):v;
      break;}
  }
  gtag("js",new Date());
  gtag("config",ID,{content_group:grupa});
})();
</script>
"""


def head():
    """Skaitītāja HTML - veidnes to ieliek <head> beigās."""
    return HEAD % {"id": '"%s"' % MERIJUMS,
                   "domens": '"%s"' % domens(),
                   "sakums": '"%s"' % SAKUMS,
                   "sadalas": json.dumps(SADALAS, ensure_ascii=False)}
