# -*- coding: utf-8 -*-
"""«Cik labi zini bērna matemātiku» lapas (calcubo.lv/smart):

    smart/index.html      angliski
    smart/lv/index.html   latviski

Vecāks izvēlas bērna klasi (1-9), atrisina 5 tās klases uzdevumus, redz
rezultātu ar sirsnīgu vārdu un «Saņem agrāko piekļuvi» formu - to pašu,
kas calcubo.lv/play (play_forma) ar avotu «smart»; līdzi aiziet klase.

Šis modulis tikai saliek lapu (SRP): karkass - divvalodu_lapa, teikumi -
smart_teksti, uzdevumi - smart_uzdevumi, gaita - smart_aptauja, solis -
aptaujas_solis, stils - smart_stils, forma - play_forma.
"""

import html

import aptaujas_solis
import divvalodu_lapa
import play_forma
import play_teksti
import smart_aptauja
import smart_stils
import smart_teksti
import smart_uzdevumi
import valoda
from smart_teksti import teksts

MAPE = "smart"
LAPA = "index.html"
AVOTS = "smart"

SATURS = """<section id="sm-sakums" class="pl-kartite pl-start">
<h2>%(ievads_v)s</h2>
<p>%(ievads)s</p>
<p class="sm-klases-v">%(klase_v)s</p>
<div class="sm-klases">
%(klases)s
</div>
<p class="pl-meta">%(meta)s</p>
</section>
<section id="sm-jaut" class="pl-kartite" hidden></section>
<section id="sm-rez" class="ap-rez" hidden>
<div class="pl-kartite sm-karte"></div>
<div class="pl-kartite">
<h2>%(cta_v)s</h2>
<p id="sm-cta"></p>
%(forma)s
</div>
<p class="pl-centrs"><button type="button" class="pl-poga" id="sm-cita">%(cita_klase)s</button></p>
</section>"""

STARTS = """
SM.sakt();
PF.sak("");
"""


def e(atslega, **vietas):
    return html.escape(teksts(atslega, **vietas))


def klasu_pogas():
    return "\n".join(
        '<button type="button" class="pl-poga sm-klase" data-k="%d">%s'
        '</button>' % (k, e("klase", n=k)) for k in smart_uzdevumi.KLASES)


def skripts():
    return "<script>%s</script>" % "\n".join([
        play_teksti.js(), smart_teksti.js(), smart_uzdevumi.js(),
        aptaujas_solis.js(), smart_aptauja.js(), play_forma.js(), STARTS])


def render():
    saturs = SATURS % dict(
        {k: e(k) for k in ("ievads_v", "ievads", "klase_v", "meta", "cta_v",
                           "cita_klase")},
        klases=klasu_pogas(),
        forma=play_forma.render(AVOTS, play_forma.POGA_VECAKIEM))
    return divvalodu_lapa.lapa(teksts("virsraksts"), MAPE, LAPA, saturs,
                               skripts(), smart_stils.css())


def build():
    out = []
    for v in valoda.VALODAS:
        with valoda.ar(v):
            out.append(divvalodu_lapa.raksti(
                divvalodu_lapa.cels(MAPE, LAPA), render()))
    return out
