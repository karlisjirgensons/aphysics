# -*- coding: utf-8 -*-
"""Vecāku aptaujas lapas (calcubo.lv/parent):

    parent/index.html      angliski
    parent/lv/index.html   latviski

Īsa, sirsnīga aptauja pieaugušajiem (cik bieži lasāt, spēlējaties,
mācāties kopā ...), rezultāts pret tipisku vecāku un beigās «Saņem agrāko
piekļuvi» e-pasta forma - tā pati, kas calcubo.lv/play (play_forma), tikai
ar avotu «parent», tāpēc e-pasti nonāk tajā pašā tabulā.

Šis modulis tikai saliek lapu (SRP): karkass - divvalodu_lapa, teikumi -
vecaki_teksti, jautājumi un rezultāts - vecaki_aptauja, solis -
aptaujas_solis, stils - vecaki_stils, forma - play_forma.
"""

import html

import aptaujas_solis
import divvalodu_lapa
import play_forma
import play_teksti
import valoda
import vecaki_aptauja
import vecaki_stils
import vecaki_teksti
from vecaki_teksti import teksts

MAPE = "parent"
LAPA = "index.html"
AVOTS = "parent"

SATURS = """<section id="vk-sakums" class="pl-kartite pl-start">
<h2>%(ievads_v)s</h2>
<p>%(ievads)s</p>
<button type="button" class="pl-poga pl-galvena pl-liela" id="vk-sakt">%(sakt)s</button>
<p class="pl-meta">%(meta)s</p>
</section>
<section id="vk-jaut" class="pl-kartite" hidden></section>
<section id="vk-rez" class="ap-rez" hidden>
<div class="pl-kartite vk-karte"></div>
<div class="pl-kartite">
<h2>%(cta_v)s</h2>
<p>%(cta)s</p>
%(forma)s
</div>
<p class="vk-avoti">%(avoti)s</p>
</section>"""

STARTS = """
document.getElementById("vk-sakt").onclick=VA.sak;
PF.sak("");
"""


def e(atslega):
    return html.escape(teksts(atslega))


def skripts():
    """PT (formas teikumi) + VT + solis + aptauja + forma vienā <script>."""
    return "<script>%s</script>" % "\n".join([
        play_teksti.js(), vecaki_teksti.js(), aptaujas_solis.js(),
        vecaki_aptauja.js(),
        play_forma.js(), STARTS])


def render():
    return divvalodu_lapa.lapa(
        teksts("virsraksts"), MAPE, LAPA,
        SATURS % dict({k: e(k) for k in (
            "ievads_v", "ievads", "sakt", "cta_v", "cta", "avoti")},
            meta=e("sakt_meta"), forma=play_forma.render(AVOTS, play_forma.POGA_VECAKIEM)),
        skripts(), vecaki_stils.css())


def build():
    out = []
    for v in valoda.VALODAS:
        with valoda.ar(v):
            out.append(divvalodu_lapa.raksti(
                divvalodu_lapa.cels(MAPE, LAPA), render()))
    return out
