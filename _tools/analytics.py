# -*- coding: utf-8 -*-
"""Google Analytics skaitītājs - viena vieta, kur zināms mērījuma ID (SRP).

Lapas aug no pieciem veidņiem (site_index.py, deck_page.py, math_lapa.py,
mat_page.py, fd_page.py). Katrs savu <head> raksta pats, bet skaitītāju
ieliek ar %(analytics)s, tāpēc ID un skripts nedzīvo vairākās vietās (DRY).

Divas lietas skripts izlemj pats, lai tās nebūtu jāraksta katrā lapā:

  sadaļa  - adreses pirmā mape (Dabaszinibas, Fizika_1, Math, PD_generate).
            Mapes nosaukums jau ir sadaļas nosaukums, tāpēc būvētājam tas
            nav jāatkārto. GA4 to saņem kā "content_group", un atskaitē
            katra sadaļa ir viena rinda - tieši tas, ko vajag, lai redzētu,
            cik cilvēku iet uz kuru priekšmetu.

  vai skaitīt - tikai īstajā vietnē. Lapas atver arī lokāli (check_stunda.py
            vienā piegājienā izspēlē simtiem stundu no file://), un tie nav
            apmeklētāji; ja tos skaitītu, atskaite melotu. Kamēr adrese nav
            īstā, skripts pat nelejupielādējas.
"""

import os

import courses

# Mērījuma ID no Google Analytics (Analytics/analytics_google.txt).
MERIJUMS = "G-D08NE6MVZ7"

# Sākumlapai adresē nav mapes - tai vajag vārdu, citādi sadaļa būtu tukša.
SAKUMS = "Sākums"


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
  var DOM=%(domens)s, ID=%(id)s;
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
  /* Sadaļa ir adreses pirmā mape; sākumlapai mapes nav. */
  var d=location.pathname.split("/")[1]||"";
  gtag("js",new Date());
  gtag("config",ID,{content_group:(d&&d.indexOf(".")<0)?d:%(sakums)s});
})();
</script>
"""


def head():
    """Skaitītāja HTML - veidnes to ieliek <head> beigās."""
    return HEAD % {"id": '"%s"' % MERIJUMS,
                   "domens": '"%s"' % domens(),
                   "sakums": '"%s"' % SAKUMS}
