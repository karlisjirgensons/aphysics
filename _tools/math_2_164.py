# -*- coding: utf-8 -*-
"""2. klase, 164. stunda: «Ko stāsta diagramma?»

Stabiņu diagramma par lielumiem, kas atšķiras vairākas reizes: nolasa
vērtības un salīdzina ne tikai «par cik», bet arī «cik reižu». Pēc tam zīmē
savu diagrammu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, kolonnas)

TEMA = "Ko stāsta diagramma?"

MERKIS = ("Šodien lasīsim un zīmēsim stabiņu diagrammu par lielumiem, kas "
          "atšķiras vairākas reizes.")

_LASA = kolonnas([("Anna", 5), ("Toms", 10), ("Līva", 20),
                  ("Markuss", 40)])

SATURS = [
    Sakums("Cik reižu vairāk lappušu izlasīja Markuss nekā Anna?",
           zimejums=_LASA,
           paraksts="Izlasītās lappuses lasīšanas maratona dienā.",
           fakti=["Katrs nākamais stabiņš divreiz augstāks.",
                  "Markuss 40, Anna 5.",
                  "40 : 5 = 8 - astoņas reizes!"]),

    Doma("Par cik un cik reižu",
         "«Par cik» - atņem; «cik reižu» - dala lielāko ar mazāko.",
         soli=[
             "Nolasi abas vērtības.",
             "Par cik: 20 − 10 = 10.",
             "Cik reižu: 20 : 10 = 2.",
             "Diagrammā: augstākais stabiņš ir 2 reizes augstāks.",
         ]),

    Ievadi("Lasi diagrammu", [
        {"jaut": "Cik reižu Toms izlasīja vairāk nekā Anna?", "zim": _LASA,
         "atb": ["2"], "padoms": "10 : 5."},
        {"jaut": "Par cik lappusēm Līva izlasīja vairāk nekā Toms?", "zim": _LASA,
         "atb": ["10"], "padoms": "20 − 10."},
        {"jaut": "Cik reižu Līva izlasīja vairāk nekā Anna?", "zim": _LASA,
         "atb": ["4"], "padoms": "20 : 5."},
        {"jaut": "Cik reižu Markuss izlasīja vairāk nekā Toms?", "zim": _LASA,
         "atb": ["4"], "padoms": "40 : 10."},
    ]),

    Varianti("Kas patiess?", [
        {"jaut": "Kurš apgalvojums patiess?", "zim": _LASA,
         "opcijas": ["Markuss izlasīja 2 reizes vairāk nekā Līva",
                     "Toms izlasīja 3 reizes vairāk nekā Anna",
                     "Līva izlasīja par 5 lappusēm vairāk nekā Toms"],
         "pareizi": 0, "padoms": "40 : 20 = 2."},
    ]),

    Petijums("Mūsu diagramma", [
        "Pierakstiet, cik minūtes katrs lasa dienā: 5, 10, 15 vai 20.",
        "Saskaitiet, cik bērnu katrā grupā.",
        "Uzzīmējiet stabiņu diagrammu.",
        "Atrodiet divas grupas, kur viena 2 reizes lielāka.",
    ], vajag="rūtiņu lapa, krāsainie zīmuļi"),

    Pasaule("Ūdens patēriņš",
            Ievadi("", [
                {"jaut": "Dušā 5 minūtēs iztek 40 l ūdens, vannā - 80 l. "
                         "Cik reižu vanna patērē vairāk?", "atb": ["2"],
                 "padoms": "80 : 40."},
                {"jaut": "Par cik litriem vairāk?", "atb": ["40"], "mers": "l",
                 "padoms": "80 − 40."},
            ]),
            zimejums=kolonnas([("duša", 40), ("vanna", 80)], " l"),
            pavediens="planeta",
            konteksts="Ūdens taupīšana ir svarīga visai planētai.",
            kapec="Diagramma parāda, kur var ietaupīt."),

    Kopsavilkums([
        "Nolasu stabiņu diagrammu.",
        "Salīdzinu par cik un cik reižu.",
        "Zīmēju savu diagrammu.",
    ]),

    Majas([
        "Pieraksti, cik glāzes ūdens katrs mājinieks izdzer dienā.",
        "Uzzīmē diagrammu.",
        "Vai kāds izdzer 2 reizes vairāk nekā cits?",
    ]),
]
