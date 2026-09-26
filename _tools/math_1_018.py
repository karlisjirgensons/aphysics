# -*- coding: utf-8 -*-
"""1. klase, 18. stunda: «Cik dažādi var izbirt piecas ripiņas?»

Divpusējas ripiņas (violeta/oranža puse) izber un saskaita, cik katrā
krāsā. Kopā vienmēr 5, bet daļas mainās - tas ir skaitļa sastāvs. Iznākumus
pieraksta divu aiļu tabulā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, bildes, restis)

TEMA = "Cik dažādi var izbirt piecas ripiņas?"

MERKIS = ("Šodien izbērsim ripiņas un pierakstīsim tabulā, kā 5 sadalās "
          "divās daļās.")


def _izbira(v, o):
    return bildes([["ripina"] * v + ["ripina*"] * o])


SATURS = [
    Sakums("5 ripiņas - cik violetu, cik oranžu?",
           zimejums=_izbira(3, 2),
           paraksts="3 violetas un 2 oranžas - kopā 5.",
           fakti=["Ripiņai ir divas puses: violeta un oranža.",
                  "Kopā vienmēr ir 5.",
                  "Mainās tikai, cik ir katrā krāsā."]),

    Slidnis("Kā var izbirt", [
        {"v": "4 un 1", "teksts": "4 violetas, 1 oranža",
         "zim": _izbira(4, 1)},
        {"v": "3 un 2", "teksts": "3 violetas, 2 oranžas",
         "zim": _izbira(3, 2)},
        {"v": "2 un 3", "teksts": "2 violetas, 3 oranžas",
         "zim": _izbira(2, 3)},
        {"v": "1 un 4", "teksts": "1 violeta, 4 oranžas",
         "zim": _izbira(1, 4)},
    ]),

    Doma("Skaitļa sastāvs",
         "5 var sadalīt divās daļās dažādi, bet kopā vienmēr ir 5.",
         soli=[
             "Izber ripiņas.",
             "Saskaiti violetās un oranžās.",
             "Ieraksti tabulā: vienā ailē violetās, otrā - oranžās.",
         ]),

    Ievadi("Cik oranžu?", [
        {"jaut": "Kopā 5. Violetas 4. Cik oranžu?", "zim": _izbira(4, 1),
         "atb": ["1"], "padoms": "Saskaiti oranžās."},
        {"jaut": "Kopā 5. Violetas 2. Cik oranžu?", "zim": _izbira(2, 3),
         "atb": ["3"], "padoms": "Saskaiti oranžās."},
        {"jaut": "Kopā 5. Violetas 3. Cik oranžu?", "atb": ["2"],
         "padoms": "3 un vēl cik ir 5?"},
        {"jaut": "Kopā 5. Violetas 1. Cik oranžu?", "atb": ["4"],
         "padoms": "1 un vēl cik ir 5?"},
    ]),

    Ievadi("Tabula", [
        {"jaut": "Kurš skaitlis trūkst tabulā?",
         "zim": restis([["V", "O"], [4, 1], [3, 2], [2, None], [1, 4]]),
         "atb": ["3"], "padoms": "2 un vēl cik ir 5?"},
        {"jaut": "Kurš skaitlis trūkst tabulā?",
         "zim": restis([["V", "O"], [4, 1], [None, 2], [2, 3]]),
         "atb": ["3"], "padoms": "Cik un vēl 2 ir 5?"},
    ]),

    Petijums("Izber pats", [
        "Paņem 5 divpusējas ripiņas.",
        "Izber tās uz galda 10 reizes.",
        "Katru reizi ieraksti tabulā: V - violetās, O - oranžās.",
        "Kurš iznākums bija visbiežāk?",
    ], vajag="5 divpusējas ripiņas, lapa ar tabulu"),

    Pasaule("Āboli divās bļodās",
            Ievadi("", [
                {"jaut": "Mamma saliek 5 ābolus divās bļodās. Vienā ir 2. "
                         "Cik otrā?", "zim": bildes([[("abols", 2), "",
                                                      ("abols*", 3)]]),
                 "atb": ["3"], "padoms": "Saskaiti oranžos."},
                {"jaut": "Tagad vienā bļodā ir 4 āboli. Cik otrā?",
                 "atb": ["1"], "padoms": "4 un vēl cik ir 5?"},
            ]),
            pavediens="virtuve",
            konteksts="Āboli vienmēr ir 5 - mainās tikai, kā tos sadala.",
            kapec="Skaitļa sastāvs palīdz dalīt lietas."),

    Kopsavilkums([
        "Sadalu 5 divās daļās dažādos veidos.",
        "Pierakstu iznākumus divu aiļu tabulā.",
        "Zinu, ka kopā vienmēr ir 5.",
    ]),

    Majas([
        "Sadali 5 karotes divās kaudzītēs visos veidos.",
        "Uzmet 5 monētas: cik ciparu, cik ģerboņu?",
        "Ieraksti iznākumus tabulā.",
    ]),
]
