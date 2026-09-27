# -*- coding: utf-8 -*-
"""IQ sadaļas lapas: Math/IQ/index.html un katra testa lapa - un tās pašas
angliski (en/IQ/...) ar savu sākumlapu en/index.html.

IQ dzīvo mapē Math/IQ un tiek atvērts no vietnes sākumlapas (sava poga
blakus priekšmetiem), bet uzbūvēts tas ir kā vēl viena klase - tie paši moduļi, kas
klases (DRY): tematu sarakstu - math_vietne.render_klase, failu ceļus un
saites uz kaimiņiem - math_stundas, lapas čaulu - math_lapa. Šis modulis
tikai pasaka, kas IQ lapā ir savādāk (SRP): nav ievada un teorijas, nav
datuma, un vienīgais bloks ir IQ tests (iq_bloks.py).

Angliskā vietne ir tikai IQ testi, lai tos var dot arī ārzemēs: sākumlapā
en/index.html ir viena poga «IQ tests». Tulkojumi dzīvo turpat, kur
latviskie teikumi (valoda.t), tāpēc angļu testu uzbūvē tas pats kods -
build("en") (valoda.py).

    python gen_iq.py        # IQ lapas abās valodās un abas sākumlapas
"""

import os
import types

import iq_bloks
import iq_testi
import math_lapa
import math_plani
import math_stundas
import math_vietne
import site_index
import valoda
from site_index import href, write
from valoda import t

# Angļu vietnes mape - viss angliskais dzīvo zem tās.
EN_MAPE = "en"


def kaimini():
    return (t("Iepriekšējais tests", "Previous test"),
            t("Nākamais tests", "Next test"))


def karte():
    return t("IQ testi", "IQ tests")


def karte_apraksts():
    return t("mīklas un loģika · 1.-9. klase", "puzzles and logic · age 7+")


def karte_zime():
    return t("★ spēle", "★ game")


# -------------------------------------------------------------------- ceļi
def mape():
    """IQ mape tagadējā valodā: Math/IQ vai en/IQ."""
    if valoda.en():
        return os.path.join(sakne(), iq_testi.NOSAUKUMS)
    return os.path.join(math_vietne.sakne(), iq_testi.NOSAUKUMS)


def kurss_():
    """IQ kurss tagadējā valodā, kas zina savu mapi - pēc tās testu
    sarakstā (math_vietne.render_klase) redz, kuri testi jau ir uzbūvēti."""
    k = iq_testi.kurss()
    k.mape = mape()
    return k


def sakne():
    """Vietnes sakne tagadējā valodā: latviskā vai en/."""
    if valoda.en():
        return os.path.join(math_plani.SAKNE, EN_MAPE)
    return math_plani.SAKNE


def testa_cels(kurss, tests):
    """Testa HTML fails tagadējā valodā."""
    return os.path.join(mape(), math_stundas.cels(kurss, tests))


# Lapas, kas ir abās valodās: sākumlapa, testu saraksts un katrs tests (pēc
# numura - tas abās valodās ir viens un tas pats).
SAKUMS, SARAKSTS = "sakums", "saraksts"


def lapas_cels(kas, kura=None):
    """Lapas fails valodā «kura» (pēc noklusējuma - tagadējā); «kas» -
    SAKUMS, SARAKSTS vai testa numurs. Te vienīgajā vietā zināms, kur katra
    lapa stāv katrā valodā - pēc tā būvē lapas un valodu pārslēgu."""
    with valoda.ar(kura or valoda.tagad()):
        if kas == SAKUMS:
            return os.path.join(sakne(), "index.html")
        if kas == SARAKSTS:
            return os.path.join(mape(), "index.html")
        kurss = kurss_()
        return testa_cels(kurss, kurss.visas[kas - 1])


def saite(no_lapas, uz_lapu):
    """Relatīva saite no vienas lapas faila uz citu."""
    rel = os.path.relpath(uz_lapu, os.path.dirname(no_lapas))
    return href(*rel.split(os.sep))


def valodu_saites(kas):
    """Pārslēgs LV | EN lapai «kas»: katra valoda ved uz to pašu lapu
    tulkojumā (testā - uz to pašu testu)."""
    sheit = lapas_cels(kas)
    return site_index.render_valodas(
        {v: saite(sheit, lapas_cels(kas, v)) for v in valoda.VALODAS},
        valoda.tagad())


# ------------------------------------------------------------------- lapas
def saturs(tests):
    """Testa lapas saturs tādā pašā formā, kādu gaida math_lapa."""
    kartas = tests.kartas()
    s = types.SimpleNamespace(
        TEMA=tests.tema,
        MERKIS="%s · %s" % (valoda.skaits(len(kartas),
                                          ("mīkla", "mīklas", "mīklu"),
                                          ("puzzle", "puzzles")),
                            tests.sr),
        SATURS=[iq_bloks.IQTests(kartas, "iq-%d" % tests.nr)])
    iq_bloks.parbaudi(s)
    return s


def _raksti(cels, html):
    if not os.path.isdir(os.path.dirname(cels)):
        os.makedirs(os.path.dirname(cels))
    return write(cels, html)


def build_tests(kurss, tests, visi):
    lapa = math_lapa.render(
        tests, saturs(tests), atpakal="../index.html",
        klases_nosaukums=t(kurss.nosaukums, "IQ tests"), datums=None,
        saites=math_stundas.blakus(kurss, tests, visi, kaimini()),
        kods=t("%s · %d. tests", "%s · test %d") % (kurss.kods, tests.nr),
        skats="spele", valodas=valodu_saites(tests.nr))
    return _raksti(testa_cels(kurss, tests), lapa)


def build_saraksts(kurss):
    cels = lapas_cels(SARAKSTS)
    html = math_vietne.render_klase(
        kurss, (saite(cels, lapas_cels(SAKUMS)), t("Sākums", "Home")),
        virsraksts=t(None, "IQ tests · brain puzzles"),
        galva=t(None, "IQ tests"), valodas=valodu_saites(SARAKSTS))
    return _raksti(cels, html)


def build(kuras=valoda.VALODAS):
    """Visi IQ testi un to saraksts katrā valodā; testi pirms saraksta -
    poga kļūst aktīva tikai tad, kad lapa ir vietā. Angliski vēl arī
    angļu sākumlapa."""
    out = []
    for v in kuras:
        with valoda.ar(v):
            kurss = kurss_()
            visi = {x.nr: x for x in kurss.visas}
            out += [build_tests(kurss, x, visi) for x in kurss.visas]
            out.append(build_saraksts(kurss))
            if valoda.en():
                out.append(build_home_en())
    return out


def _skaiti():
    kurss = kurss_()
    return "%s · %s" % (valoda.skaits(len(kurss.temati),
                                      ("kategorija", "kategorijas",
                                       "kategoriju"),
                                      ("category", "categories")),
                        valoda.skaits(kurss.stundu_skaits,
                                      ("tests", "testi", "testu"),
                                      ("test", "tests")))


def render_card():
    """IQ poga sākumlapā - tāda pati kā priekšmetiem. Latviskajā sākumlapā
    tā ved uz Math/IQ, angliskajā (en/index.html) - uz blakus mapi IQ."""
    return site_index.render_karte(
        saite(lapas_cels(SAKUMS), lapas_cels(SARAKSTS)), karte(),
        karte_apraksts(), _skaiti(), karte_zime())


# --------------------------------------------------------- angļu sākumlapa
EN_TITLE = "IQ tests"


def build_home_en():
    """en/index.html - angliskā sākumlapa: tikai IQ testi."""
    with valoda.ar("en"):
        html = site_index.page(EN_TITLE, "\n".join([
            site_index.render_header(EN_TITLE, valodu_saites(SAKUMS)),
            '<div class="cards">\n%s\n</div>' % render_card()]))
        return _raksti(lapas_cels(SAKUMS), html)
