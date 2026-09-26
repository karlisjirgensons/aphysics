# -*- coding: utf-8 -*-
"""IQ sadaļas lapas: Math/IQ/index.html un katra testa lapa.

IQ dzīvo mapē Math/IQ un tiek atvērts no vietnes sākumlapas (sava poga
blakus priekšmetiem), bet uzbūvēts tas ir kā vēl viena klase - tie paši moduļi, kas
klases (DRY): tematu sarakstu - math_vietne.render_klase, failu ceļus un
saites uz kaimiņiem - math_stundas, lapas čaulu - math_lapa. Šis modulis
tikai pasaka, kas IQ lapā ir savādāk (SRP): nav ievada un teorijas, nav
datuma, un vienīgais bloks ir IQ tests (iq_bloks.py).

    python gen_iq.py        # tikai IQ lapas un klašu saraksts
"""

import os
import types

import iq_bloks
import iq_testi
import math_lapa
import math_stundas
import math_vietne
import site_index
from site_index import href, plural, write

LEAD = ("Mīklas bez stundas: skaitļu virknes, figūru matricas, telpiskā "
        "domāšana, loģika un atmiņa. Katrā kategorijā ir trīs pakāpes - no "
        "1., 4. un 7. klases. Par pareizu atbildi ar pirmo mēģinājumu - "
        "zvaigzne!")
KAIMINI = ("Iepriekšējais tests", "Nākamais tests")
KARTE = "IQ testi"
KARTE_APRAKSTS = "mīklas un loģika · 1.-9. klase"
KARTE_ZIME = "★ spēle"


def saturs(tests):
    """Testa lapas saturs tādā pašā formā, kādu gaida math_lapa."""
    kartas = tests.kartas()
    s = types.SimpleNamespace(
        TEMA=tests.tema,
        MERKIS="%s · %s" % (plural(len(kartas), "mīkla", "mīklas", "mīklu"),
                            tests.sr),
        SATURS=[iq_bloks.IQTests(kartas, "iq-%d" % tests.nr)])
    iq_bloks.parbaudi(s)
    return s


def build_tests(kurss, tests, visi):
    cels = os.path.join(math_stundas.mape(kurss),
                        math_stundas.cels(kurss, tests))
    if not os.path.isdir(os.path.dirname(cels)):
        os.makedirs(os.path.dirname(cels))
    lapa = math_lapa.render(
        tests, saturs(tests), atpakal="../index.html",
        klases_nosaukums=kurss.nosaukums, datums=None,
        saites=math_stundas.blakus(kurss, tests, visi, KAIMINI),
        kods="%s · %d. tests" % (kurss.kods, tests.nr), skats="spele")
    return write(cels, lapa)


def build_saraksts(kurss):
    mape = math_vietne.klases_mape(kurss)
    if not os.path.isdir(mape):
        os.makedirs(mape)
    return write(os.path.join(mape, "index.html"),
                 math_vietne.render_klase(kurss, LEAD,
                                          ("../../index.html", "Sākums")))


def build():
    """Visi IQ testi un to saraksts; testi pirms saraksta - poga kļūst
    aktīva tikai tad, kad lapa ir vietā."""
    kurss = iq_testi.kurss()
    visi = {t.nr: t for t in kurss.visas}
    return ([build_tests(kurss, t, visi) for t in kurss.visas]
            + [build_saraksts(kurss)])


def _skaiti():
    kurss = iq_testi.kurss()
    return "%s · %s" % (plural(len(kurss.temati), "kategorija",
                               "kategorijas", "kategoriju"),
                        plural(kurss.stundu_skaits, "tests", "testi",
                               "testu"))


def render_card():
    """IQ poga vietnes sākumlapā - tāda pati kā priekšmetiem."""
    return site_index.render_karte(
        href(math_vietne.MAPE, iq_testi.NOSAUKUMS, "index.html"), KARTE,
        KARTE_APRAKSTS, _skaiti(), KARTE_ZIME)
