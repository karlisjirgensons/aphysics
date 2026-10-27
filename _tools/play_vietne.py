# -*- coding: utf-8 -*-
"""Dienas izaicinājuma lapas (calcubo.lv/play):

    play/index.html      angliski - spēle un «I'm a parent» forma
    play/r.html          angliski - rezultāts, ko bērns nosūta vecākiem
    play/lv/index.html   tas pats latviski
    play/lv/r.html

Angļu valoda ir galvenā, tāpēc tā ir pašā play/ (saite, ko dod visiem), un
latviskā ir apakšmapē. Abas valodas būvē viens kods ar valoda.ar (DRY).

Lapas karkass, galva un valodu pārslēgs ir tie paši, kas visā vietnē
(site_index.page / render_header / render_valodas). Šis modulis tikai
saliek lapas no gatavām daļām (SRP): teikumi - play_teksti, uzdevumi -
play_uzdevumi, rezultāts - play_rezultats, spēle - play_spele, dalīšanās -
play_dalisana, e-pasta forma - play_forma, stils - play_stils.
"""

import html
import os

import play_dalisana
import play_forma
import play_rezultats
import play_slava
import play_spele
import play_stils
import play_teksti
import play_uzdevumi
import site_index
import valoda
from courses import SITE_ROOT
from play_teksti import teksts

MAPE = "play"
# Valoda -> apakšmape zem play/ (angļu valoda ir pašā play/).
APAKSMAPE = {"en": "", "lv": "lv"}
SPELE, REZULTATS = "index.html", "r.html"


def cels(lapa, kura=None):
    """Lapas fails valodā «kura» (pēc noklusējuma - tagadējā)."""
    v = kura or valoda.tagad()
    return os.path.join(SITE_ROOT, MAPE, APAKSMAPE[v], lapa)


def valodu_saites(lapa):
    """LV | EN pārslēgs uz to pašu lapu otrā valodā."""
    sheit = os.path.dirname(cels(lapa))
    return site_index.render_valodas(
        {v: os.path.relpath(cels(lapa, v), sheit).replace(os.sep, "/")
         for v in valoda.VALODAS}, valoda.tagad())


def e(atslega):
    return html.escape(teksts(atslega))


def skripts(starts):
    """Visi spēles moduļi vienā <script> un lapas palaišana «starts»."""
    return "<script>%s</script>" % "\n".join([
        play_teksti.js(), play_uzdevumi.js(), play_slava.js(),
        play_rezultats.js(),
        play_dalisana.js(), play_forma.js(), play_spele.js(), starts])


def lapa(virsraksts, kas, saturs, starts, head=""):
    return site_index.page(virsraksts, "\n".join([
        site_index.render_header(virsraksts, valodu_saites(kas)),
        '<main class="pl">\n%s\n</main>' % saturs,
        skripts(starts)]),
        head="<style>%s</style>\n%s" % (play_stils.css(), head))


# ------------------------------------------------------------------ spēle
SPELES_SATURS = """<section id="pl-sakums">
<div class="pl-kartite pl-start">
<button type="button" class="pl-poga pl-galvena pl-liela" id="pl-sakt">%(sakt)s</button>
<p class="pl-meta">%(meta)s</p>
</div>
<details class="pl-vecaks">
<summary><span>%(vecaks)s</span></summary>
<div class="pl-iekss">
<h2>%(agri)s</h2>
<p>%(kapec)s</p>
%(forma)s
</div>
</details>
</section>
<section id="pl-spele" class="pl-kartite" hidden></section>
<section id="pl-rezultats" hidden>
<div class="pl-kartite"><div class="pl-karte"></div><div class="pl-dalities"></div></div>
<div class="pl-kartite" id="pl-pieaug" hidden>
<h2>%(agri)s</h2>
<p>%(kapec)s</p>
%(forma18)s
</div>
</section>"""

SPELES_STARTS = """
document.getElementById("pl-sakt").onclick=PS.sak;
PF.sak("");
"""


def render_spele():
    return lapa(teksts("virsraksts"), SPELE, SPELES_SATURS % {
        "sakt": e("sakt"), "meta": e("sakt_meta"), "vecaks": e("vecaks"),
        "agri": e("agri"), "kapec": e("agri_kapec"),
        "forma": play_forma.render("play"),
        "forma18": play_forma.render("play-18")}, SPELES_STARTS)


# -------------------------------------------------------------- rezultāts
REZ_SATURS = """<section class="pl-kartite"><div class="pl-karte"></div></section>
<section class="pl-kartite">
<h2>%(agri)s</h2>
<p>%(kapec)s</p>
%(forma)s
</section>
<p class="pl-centrs"><a class="pl-poga pl-galvena" href="index.html">%(izmeginat)s</a></p>"""

# Rezultāts ir saitē (?r=...); valodu pārslēgam tas jānes līdzi.
REZ_STARTS = """
(function(){
  var k=new URLSearchParams(location.search).get("r")||"",x=PR.lasi(k),
      el=document.querySelector(".pl-karte");
  if(x){PR.karte(el,x);}
  else{el.innerHTML='<p class="pl-zina kluda">'+PT.T.slikta_saite+'</p>';}
  Array.prototype.forEach.call(document.querySelectorAll(".valodas a"),
    function(a){a.href+=location.search;});
  PF.sak(x?k:"");
})();
"""

REZ_HEAD = """<meta name="robots" content="noindex">
<meta property="og:title" content="%(t)s">
<meta property="og:description" content="%(d)s">
"""


def render_rezultats():
    return lapa(teksts("rez_virsraksts"), REZULTATS, REZ_SATURS % {
        "agri": e("agri_vecakiem"), "kapec": e("agri_kapec"),
        "forma": play_forma.render("rezultats"),
        "izmeginat": e("izmeginat")}, REZ_STARTS,
        REZ_HEAD % {"t": e("zina_virsraksts"), "d": e("sakt_meta")})


# --------------------------------------------------------------- būvēšana
def _raksti(cels_, text):
    os.makedirs(os.path.dirname(cels_), exist_ok=True)
    return site_index.write(cels_, text)


def build():
    out = []
    for v in valoda.VALODAS:
        with valoda.ar(v):
            out.append(_raksti(cels(SPELE), render_spele()))
            out.append(_raksti(cels(REZULTATS), render_rezultats()))
    return out
