# -*- coding: utf-8 -*-
"""Formatīvā darba ģeneratora veidotājs - no satura uz vienu HTML lapu.

Formatīvais darbs ir īss tests stundas sākumā vai beigās: 12 jautājumi ar
četrām atbildēm, viena lapa, ~15 minūtes. Paraugs ir ĀT1 darba lapa, un
ģenerētais Word fails izskatās tieši tāpat (sk. fd_paper.py).

Atšķirībā no at_common.py, kas uzbūvē vienu gatavu .docx, šis modulis
uzbūvē lapu, kas darbu izloze pati - vietnē, bez servera. Tāpēc saturs te
nav viens jautājumu saraksts, bet jautājumu grupas:

    FD = {
        "nr": 1, "nosaukums": ..., "prieksmets": ..., "kicker": ...,
        "sakne": "Fizika_1", "mape": ..., "fails": "Formatīvais darbs_tt",
        "laiks": 15, "apraksts": ..., "atgadne": [...],
        "grupas": [
            {"sr": "sasniedzamais rezultāts", "stunda": "1.5.",
             "jautajumi": [(teksts, [4 atbildes], pareizās indekss), ...]},
            ...
        ],
    }

Viena grupa = viens sasniedzamais rezultāts, un tajā ir vairāki līdzvērtīgi
jautājumi. Darba uzbūve tāpēc nemainās - mainās tikai konkrētie jautājumi.
Jaunu variantu pievieno, ierakstot grupā vēl vienu jautājumu; jaunu tematu -
uzrakstot vēl vienu fd_*.py failu (DRY: dzinējs paliek šis).

Šī moduļa atbildība ir tikai pārbaudīt saturu un uzrakstīt failu (SRP);
lapas izskats ir fd_page.py, lapas saturs - fd_paper.py, Word fails -
fd_docx.py ziņā.
"""

import os
import re

import at_common
import courses
import fd_page
import fd_stils
import pd_common as C

VIRSRAKSTS = "Formatīvais darbs"
IEVADS = ("Katram jautājumam ir viena pareizā atbilde. Par pareizu — "
          "1 punkts, par nepareizu neatņem. Atļauts kalkulators.")
MIN_VARIANTI = 2        # cik jautājumu vismaz jābūt vienā grupā

# Daļas marķējums saturā: {skaitītājs|saucējs}. Mērīšanai daļa aizņem tik,
# cik tās platākā rinda.
DALA = re.compile(r"\{([^{}|]*)\|([^{}|]*)\}")


def vienkarsi(teksts):
    """Teksts bez daļu marķējuma - platuma un augstuma mērīšanai."""
    return DALA.sub(lambda m: max(m.group(1), m.group(2), key=len), teksts)


# ----------------------------------------------------------------- pārbaude
def jautajumi(fd):
    """Visi grupu jautājumi vienā sarakstā."""
    return [j for g in fd["grupas"] for j in g["jautajumi"]]


def kombinacijas(fd):
    """Cik dažādus darbus var izlozēt (neskaitot atbilžu pārkārtošanu)."""
    n = 1
    for g in fd["grupas"]:
        n *= len(g["jautajumi"])
    return n


def garakais(grupa):
    """Grupas jautājums, kas uz lapas aizņem visvairāk vietas."""
    def h(j):
        teksts, varianti, _ = j
        return at_common.h_jautajumi(
            [(vienkarsi(teksts), [vienkarsi(v) for v in varianti], 0)])
    return max(grupa["jautajumi"], key=h)


def augstums(fd, jautajumi):
    """Darba lapas augstums centimetros - tā, kā to mēra ĀT lapām.

    Jautājumu un atbilžu tabulas mērs nāk no at_common.py (DRY); atšķiras
    tikai ievads un ATGĀDNE, jo tie te ir citā garumā.
    """
    return (at_common.H_GALVENE
            + C.h_para(vienkarsi(fd.get("ievads", IEVADS)), 9.5, after=4)
            + 1.45                                      # veidlapa
            + 0.55 + len(fd["atgadne"]) * 0.42 + 0.45   # ATGĀDNE kaste
            + at_common.h_jautajumi(jautajumi)
            + at_common.h_atbilzu_tabula(len(jautajumi))
            + at_common.H_PUNKTI)


def sliktakais(fd):
    """Vissmagākais iespējamais darbs - no katras grupas garākais jautājums.

    Ja tas ietilpst vienā lapā, tad ietilpst jebkurš izlozētais darbs, tāpēc
    lapu pietiek pārbaudīt vienreiz - būvējot, nevis stundā pie datora.
    """
    return [(vienkarsi(t), [vienkarsi(v) for v in vv], p)
            for t, vv, p in map(garakais, fd["grupas"])]


def parbaudi(fd):
    """Pārbauda grupu un atbilžu uzbūvi - to, ko lapa vairs nepārbauda."""
    grupas = fd["grupas"]
    assert grupas, "%s: nav neviena jautājumu grupas" % fd["fails"]
    assert len(grupas) % fd_stils.AILES == 0, \
        "%s: grupu skaits (%d) nedalās ar %d — atbilžu tabula būs nepilna" \
        % (fd["fails"], len(grupas), fd_stils.AILES)
    assert re.sub(r"_tt$", "", fd["fails"]) in courses.RIKI, \
        "%s: šāda nosaukuma nav courses.RIKI — tematu sarakstā lapa " \
        "parādītos kā stunda" % fd["fails"]
    redzeti = set()
    for g in grupas:
        assert g.get("sr") and g.get("stunda"), \
            "%s: grupai trūkst «sr» vai «stunda»" % fd["fails"]
        assert len(g["jautajumi"]) >= MIN_VARIANTI, \
            "%s: grupā «%s» ir tikai %d jautājums — vajag vismaz %d" \
            % (fd["fails"], g["sr"][:40], len(g["jautajumi"]), MIN_VARIANTI)
        for teksts, varianti, pareizais in g["jautajumi"]:
            assert len(varianti) == 4, \
                "%s: %s — vajag 4 atbilžu variantus" % (fd["fails"],
                                                        teksts[:40])
            assert len(set(varianti)) == 4, \
                "%s: %s — atkārtojas atbilžu varianti" % (fd["fails"],
                                                          teksts[:40])
            assert 0 <= pareizais < 4, \
                "%s: %s — nederīgs pareizās atbildes numurs" % (fd["fails"],
                                                                teksts[:40])
            assert teksts not in redzeti, \
                "%s: jautājums atkārtojas — %s" % (fd["fails"], teksts[:40])
            redzeti.add(teksts)
    h = augstums(fd, sliktakais(fd))
    assert h <= C.LAPAS_BUDZETS, \
        "%s: garākie jautājumi vienā lapā neietilpst — %.1f cm no %.1f cm" \
        % (fd["fails"], h, C.LAPAS_BUDZETS)
    return h


# ------------------------------------------------------------------ saturs
def dati(fd):
    """Saturs tādā veidā, kā to lasa lapa: ar noklusējumiem un skalu."""
    n = len(fd["grupas"])
    out = {
        "virsraksts": fd.get("virsraksts", VIRSRAKSTS),
        "nr": fd["nr"],
        "nosaukums": fd["nosaukums"],
        "prieksmets": fd.get("prieksmets", C.PRIEKSMETS),
        "kicker": fd["kicker"],
        "laiks": fd["laiks"],
        "apraksts": fd["apraksts"],
        "ievads": fd.get("ievads", IEVADS),
        "atgadne": fd["atgadne"],
        "fails": fd.get("lejupielade", "%s %d. %s"
                        % (fd.get("virsraksts", VIRSRAKSTS), fd["nr"],
                           fd["nosaukums"])),
        "skala": [list(r) for r in C.skala(n)],
        "grupas": [{"sr": g["sr"], "stunda": g["stunda"],
                    "jautajumi": [[t, list(v), p]
                                  for t, v, p in g["jautajumi"]]}
                   for g in fd["grupas"]],
    }
    return out


def mape(fd):
    sakne = (os.path.join(C.SAKNE, fd["sakne"]) if fd.get("sakne")
             else C.SAKNES_MAPE)
    return os.path.join(sakne, fd["mape"])


def build(fd):
    """Uzbūvē ģeneratora lapu temata mapē un atgriež ceļu."""
    h = parbaudi(fd)
    galamerkis = mape(fd)
    if not os.path.isdir(galamerkis):
        raise SystemExit("Nav atrasta mape: %s" % galamerkis)
    path = os.path.join(galamerkis, "%s.html" % fd["fails"])
    with open(path, "w", encoding="utf-8") as f:
        f.write(fd_page.page(dati(fd)))
    print("Izveidots: %s\n           %d grupas, %d jautājumi, %s dažādi "
          "darbi; smagākā lapa %.1f cm no %.1f cm"
          % (os.path.relpath(path, C.SAKNE), len(fd["grupas"]),
             len(jautajumi(fd)),
             "{:,}".format(kombinacijas(fd)).replace(",", " "),
             h, C.LAPAS_BUDZETS))
    return path
