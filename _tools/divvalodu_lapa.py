# -*- coding: utf-8 -*-
"""Divvalodu lapa mapē, kur angļu valoda ir pašā mapē un latviskā - lv/.

    play/index.html      angliski          parent/index.html
    play/lv/index.html   latviski          parent/lv/index.html

Dienas izaicinājums (play_vietne) un vecāku aptauja (vecaki_vietne) ir
uzbūvēti vienādi: lapas ceļš valodā, LV | EN pārslēgs uz to pašu lapu,
vietnes karkass ar savu stilu un skriptu. Šis modulis zina tikai to (SRP),
lai abas lapu kopas to neraksta katra savā vietā (DRY).
"""

import os

import site_index
import valoda
from courses import SITE_ROOT

# Valoda -> apakšmape (angļu valoda ir pašā mapē).
APAKSMAPE = {"en": "", "lv": "lv"}


def cels(mape, lapa, kura=None):
    """Lapas fails mapē «mape» valodā «kura» (pēc noklusējuma - tagadējā)."""
    v = kura or valoda.tagad()
    return os.path.join(SITE_ROOT, mape, APAKSMAPE[v], lapa)


def valodu_saites(mape, lapa):
    """LV | EN pārslēgs uz to pašu lapu otrā valodā."""
    sheit = os.path.dirname(cels(mape, lapa))
    return site_index.render_valodas(
        {v: os.path.relpath(cels(mape, lapa, v), sheit).replace(os.sep, "/")
         for v in valoda.VALODAS}, valoda.tagad())


def lapa(virsraksts, mape, kas, saturs, skripts, css, head=""):
    """Vietnes karkass: galva ar pārslēgu, <main class="pl"> ar «saturu»,
    «skripts» (gatavs <script>) un lapas «css»."""
    return site_index.page(virsraksts, "\n".join([
        site_index.render_header(virsraksts, valodu_saites(mape, kas)),
        '<main class="pl">\n%s\n</main>' % saturs,
        skripts]),
        head="<style>%s</style>\n%s" % (css, head))


def raksti(cels_, text):
    os.makedirs(os.path.dirname(cels_), exist_ok=True)
    return site_index.write(cels_, text)
