# -*- coding: utf-8 -*-
"""Fizikas formulu lapa - viens saraksta īpašnieks (SRP).

Saraksts pats dzīvo Fizika_1/Fizika_1_formulas.txt (to labo skolotājs);
šis modulis to tikai nolasa un atbild uz vienu jautājumu:

    vai uzdevuma "Formulas:" sadaļa ir pierakstīta formulu lapas formā?

Noteikums (rules_fizika.txt un Fizika_1_formulas.txt ievads): ja uzdevumā
lieto no formulu lapas izteiktu formu ("T = λ/v"), tad pirms tās - tieši
pirms, nevis kaut kur sarakstā - jābūt arī pašai formulu lapas formai
("λ = v · T"). Formulas, kuru formulu lapā nav, netiek skartas.

Lieto tā:

    import fiz_formulas as FF

    FF.parbaudit(["T = λ/v"])   -> [(izteiktā, lapas forma, veids)]

kur veids ir "trūkst" (lapas formas sarakstā nav vispār) vai "secība"
(tā ir, bet tikai aiz izteiktās formas).
"""

import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SARAKSTS = os.path.join(ROOT, "Fizika_1", "Fizika_1_formulas.txt")

# Kas pierakstā nemaina formulas nozīmi: atstarpes, reizināšanas zīme,
# dažādi domuzīmju un apostrofu varianti.
_REIZ = "·*×"
_MINUS = "−–—"
_DZEST = re.compile(r"\s+")


def normalize(f):
    """Formulas pieraksta "pirkstu nospiedums" - salīdzināšanai.

    "v = λ · f", "v = λ*f" un "v=λf" ir viena un tā pati formula, tāpēc
    atstarpes un reizināšanas zīmes izmet.
    """
    f = _DZEST.sub("", f)
    for ch in _REIZ:
        f = f.replace(ch, "")
    for ch in _MINUS:
        f = f.replace(ch, "-")
    return f


def _lasit(celš=SARAKSTS):
    """(sadaļa, [lapas formas], [izteiktās formas]) no formulu saraksta."""
    sadala = ""
    for rinda in open(celš, encoding="utf-8"):
        rinda = rinda.strip()
        if not rinda:
            continue
        if rinda.startswith("##"):
            sadala = rinda[2:].strip()
            continue
        if rinda.startswith("#"):
            continue
        lapa, _, atv = rinda.partition("|")
        yield (sadala,
               [x.strip() for x in lapa.split(";") if x.strip()],
               [x.strip() for x in atv.split(";") if x.strip()])


def _uzbuvet():
    """Divas kartes: visas pazīstamās formas un tikai lapas formas.

    Vērtība abās ir (pamatforma, sadaļa) - pamatforma ir pirmā rindā
    uzrakstītā lapas forma, un tieši to piedāvā, ja uzdevumā tās trūkst.
    """
    formas, lapas = {}, {}
    for sadala, lapas_formas, izteiktas in _lasit():
        ieraksts = (lapas_formas[0], sadala, tuple(lapas_formas))
        for f in lapas_formas:
            lapas.setdefault(normalize(f), ieraksts)
        for f in lapas_formas + izteiktas:
            formas.setdefault(normalize(f), ieraksts)
    return formas, lapas


FORMAS, LAPAS = _uzbuvet()

_SIMBOLS = re.compile(r"[A-Za-zΑ-Ωα-ω][₀-₉ₓ]*")


def _simboli(f):
    return set(_SIMBOLS.findall(f.split("=")[-1] + f.split("=")[0]))


def ieteikt(formula):
    """Kuru no vienas rindas lapas pierakstiem likt blakus šai formulai.

    Vienai sakarībai lapā mēdz būt vairāki pieraksti (s = v₀t + at²/2 un
    h = gt²/2). Piedāvā to, kam visvairāk kopīgu apzīmējumu ar uzdevumā
    lietoto formu - tad blakus nonāk tas pats gadījums, nevis vispārīgais.
    """
    tr = FORMAS.get(normalize(formula))
    if not tr:
        return None
    _, _, varianti = tr
    sim = _simboli(formula)
    return max(varianti,
               key=lambda v: (len(sim & _simboli(v)), -varianti.index(v)))


def kanoniska(formula):
    """Formulas rindas pamatforma vai None, ja formulu lapā tādas nav."""
    tr = FORMAS.get(normalize(formula))
    return tr[0] if tr else None


def ir_lapas_forma(formula):
    """Vai formula jau ir pierakstīta tā, kā tā ir formulu lapā?"""
    return normalize(formula) in LAPAS


def parbaudit(formulas):
    """Kuras izteiktās formas lietotas bez formulu lapas formas priekšā.

    Saraksts ir secīgs, tāpēc pietiek iet no sākuma uz beigām un skatīties,
    kas jau ir bijis: lapas forma, kas parādās tikai vēlāk, uzdevumā
    neder - skolēns to izteikto formu redz pirmo.

    Atgriež [(izteiktā, kanoniskā, veids), ...]. Tukšs saraksts - viss
    kārtībā.
    """
    visas = {LAPAS[normalize(f)][0] for f in formulas if ir_lapas_forma(f)}
    redzetas, trukst, zinami = set(), [], set()
    for f in formulas:
        if ir_lapas_forma(f):
            redzetas.add(LAPAS[normalize(f)][0])
            continue
        pamats = kanoniska(f)
        if pamats is None or pamats in redzetas or pamats in zinami:
            continue
        zinami.add(pamats)
        trukst.append((f, ieteikt(f),
                       "secība" if pamats in visas else "trūkst"))
    return trukst
