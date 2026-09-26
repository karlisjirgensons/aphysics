# -*- coding: utf-8 -*-
"""2. klase, 145. stunda: «Kur dabā ir pa 4?»

Pa 4: kaķa, suņa un zirga kājas, četrlapu āboliņš, mašīnas riteņi,
gadalaiki. Zinot vienību skaitu, kopskaitu aprēķina ar reizināšanu ar 4.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, bildes)

TEMA = "Kur dabā ir pa 4?"

MERKIS = ("Šodien atradīsim objektus ar 4 vienādiem elementiem un "
          "aprēķināsim to kopskaitu.")

SATURS = [
    Sakums("Cik riteņu ir 5 mašīnām stāvvietā?",
           zimejums=bildes([[("masina", 5)]]),
           paraksts="Katrai mašīnai 4 riteņi: 5 · 4 = 20.",
           fakti=["Pa 4: mašīnas riteņi, suņa kājas, gadalaiki.",
                  "Laimīgais āboliņš - 4 lapiņas.",
                  "Kopskaits - reizinājums ar 4."]),

    Doma("Pa 4",
         "Ja katram ir 4, kopskaits = skaits · 4.",
         soli=[
             "Saskaiti, cik ir priekšmetu.",
             "Katram - 4 daļas.",
             "Reizini ar 4 (divreiz dubulto).",
             "Pieraksti ar mērvienību vai nosaukumu.",
         ]),

    Ievadi("Cik kopā?", [
        {"jaut": "Cik kāju 6 suņiem?", "atb": ["24"], "padoms": "6 · 4."},
        {"jaut": "Cik riteņu 5 mašīnām?", "zim": bildes([[("masina", 5)]]),
         "atb": ["20"], "padoms": "5 · 4."},
        {"jaut": "Cik gadalaiku 3 gados?", "atb": ["12"], "padoms": "3 · 4."},
        {"jaut": "Cik kāju 9 krēsliem?", "atb": ["36"], "padoms": "9 · 4."},
        {"jaut": "Cik lapiņu 7 laimīgajiem āboliņiem?", "atb": ["28"],
         "padoms": "7 · 4."},
        {"jaut": "Cik stūru 8 kvadrātiem?", "atb": ["32"], "padoms": "8 · 4."},
    ], pamats=4),

    Varianti("Pa 4 vai nē?", [
        {"jaut": "Kam ir 4?", "opcijas": ["zirga kājas", "putna kājas",
                                          "zirnekļa kājas"],
         "pareizi": 0, "padoms": "Putnam 2, zirneklim 8."},
        {"jaut": "Kopā kājas 20 - cik kaķu?", "opcijas": ["5", "4", "10"],
         "pareizi": 0, "padoms": "? · 4 = 20."},
    ]),

    Pasaule("Lauku sētā",
            Ievadi("", [
                {"jaut": "Sētā 4 govis un 3 vistas. Cik kāju kopā? "
                         "(4 · 4 + 3 · 2)", "atb": ["22"],
                 "padoms": "16 + 6."},
                {"jaut": "Cik astu?", "atb": ["7"],
                 "padoms": "Katram dzīvniekam viena."},
            ]),
            pavediens="daba",
            konteksts="Vecvecāku lauku sētā ir govis un vistas.",
            kapec="Reizinājumi palīdz saskaitīt ātri."),

    Kopsavilkums([
        "Atrodu dabā un apkārtnē lietas pa 4.",
        "Aprēķinu kopskaitu ar reizināšanu ar 4.",
        "Apvienoju ar citiem reizinājumiem.",
    ]),

    Majas([
        "Atrodi mājās 5 lietas ar 4 kājām vai stūriem.",
        "Saskaiti, cik kāju/stūru kopā.",
        "Pieraksti ar reizināšanu.",
    ]),
]
