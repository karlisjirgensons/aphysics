# -*- coding: utf-8 -*-
"""Matemātikas stundu lapas: kuras stundas ir uzrakstītas un kur tās liek.

Katras stundas saturs ir viens fails - math_<klase>_<numurs>.py ar trim
lietām: TEMA (tā pati, kas plānā), MERKIS (ko skolēns šodien iemācīsies) un
SATURS (bloku saraksts no math_bloki.py). Šis modulis tos atrod, pārbauda, vai
tie sakrīt ar plānu, un ieraksta lapas mapē Math/<klase>/<temats>/ (SRP).

Kur stundai jādzīvo un kā sauc failu, jau zina math_plani.py, tāpēc ceļus te
neraksta otrreiz (DRY); kā lapa izskatās - math_lapa.py.

Lietošana:
    import math_stundas
    math_stundas.build_visas()          # visas uzrakstītās stundas
"""

import importlib
import os

import math_lapa
import math_plani
from math_plani import d
from site_index import href, write


def modulis(klases_nr, stundas_nr):
    """Stundas satura modulis vai None, ja tā stunda vēl nav uzrakstīta."""
    vards = "math_%d_%03d" % (klases_nr, stundas_nr)
    try:
        return importlib.import_module(vards)
    except ImportError:
        return None


def saturs(klases_nr, stunda):
    """Stundas saturs vai None, ja tā vēl nav uzrakstīta.

    Pārbaudes darbam lapu nebūvē: PD paliek plānā un vērtēšanas kalendārā kā
    mācību diena, bet tematā vietnē rāda tikai mācību stundas - skolēnam tur
    nav ko darīt, un pats darbs notiek klasē. (Lapu no plāna prot salikt
    math_pd.py, ja tāda kādreiz atkal vajag.)
    """
    if stunda.pd:
        return None
    return modulis(klases_nr, stunda.nr)


def cels(klase, stunda):
    """Stundas fails attiecībā pret klases mapi."""
    return os.path.join(math_plani.stundas_mape(stunda),
                        math_plani.stundas_fails(stunda))


def mape(klase):
    return os.path.join(math_plani.MAPE, klase.nosaukums)


def saite(no_stundas, uz_stundu, klase):
    """Saite no vienas stundas lapas uz citu - arī pāri tematu mapēm."""
    rel = os.path.relpath(cels(klase, uz_stundu),
                          math_plani.stundas_mape(no_stundas))
    return href(*rel.split(os.sep))


def blakus(klase, stunda, gatavas,
           vardi=("Iepriekšējā stunda", "Nākamā stunda")):
    """Pogas «iepriekšējā» un «nākamā» - tikai uz jau uzrakstītām stundām."""
    out = []
    for nobide, uzraksts in zip((-1, 1), vardi):
        kaimins = gatavas.get(stunda.nr + nobide)
        if kaimins:
            out.append((uzraksts, "%d. %s" % (kaimins.nr, kaimins.tema),
                        saite(stunda, kaimins, klase)))
    return out


def saturi(klase):
    """{stundas numurs: stunda} - tikai tās, kurām saturs jau ir."""
    out = {}
    for s in klase.visas:
        if saturs(klase.nr, s) is not None:
            out[s.nr] = s
    return out


def build_stunda(klase, stunda, saturs, gatavas):
    galamerkis = os.path.join(mape(klase), cels(klase, stunda))
    if not os.path.isdir(os.path.dirname(galamerkis)):
        os.makedirs(os.path.dirname(galamerkis))
    lapa = math_lapa.render(stunda, saturs,
                            atpakal="../index.html",
                            klases_nosaukums=klase.nosaukums,
                            datums=d(stunda.datums),
                            saites=blakus(klase, stunda, gatavas))
    return write(galamerkis, lapa)


def parbaudi(klase, stunda, saturs):
    """Saturs un plāns ir viens un tas pats - numuri nedrīkst aizšķobīties."""
    math_lapa.parbaudi(saturs)
    if saturs.TEMA != stunda.tema:
        raise AssertionError(
            "%d. klases %d. stunda: saturā «%s», plānā «%s»"
            % (klase.nr, stunda.nr, saturs.TEMA, stunda.tema))


def build_klase(klase):
    """Visas uzrakstītās vienas klases stundas; atgriež ceļu sarakstu."""
    gatavas = saturi(klase)
    out = []
    for nr in sorted(gatavas):
        stunda = gatavas[nr]
        lapas_saturs = saturs(klase.nr, stunda)
        parbaudi(klase, stunda, lapas_saturs)
        out.append(build_stunda(klase, stunda, lapas_saturs, gatavas))
    return out


def build_visas(numuri=None):
    """Visu klašu stundu lapas - pirms tam, kad būvē stundu sarakstus."""
    klases = ([math_plani.klase(n) for n in numuri] if numuri
              else math_plani.klases())
    out = []
    for k in klases:
        out.extend(build_klase(k))
    return out
