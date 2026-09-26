# -*- coding: utf-8 -*-
"""2. klase, 72. stunda: «Kāpēc vajadzīgas iekavas?»

Ja no skaitļa jāatņem divu skaitļu summa, to raksta ar iekavām:
50 − (12 + 8). Iekavas saka: «šo izrēķini vispirms». Bez iekavām 50 − 12 + 8
nozīmētu ko citu - un iznāktu cits skaitlis.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kāpēc vajadzīgas iekavas?"

MERKIS = ("Šodien lietosim iekavas, ja no skaitļa jāatņem divu skaitļu "
          "summa.")

SATURS = [
    Sakums("Tev ir 50 €. Tu pērc grāmatu par 12 € un pildspalvu par 8 €. "
           "Kā uzrakstīt, cik paliks?",
           fakti=["Kopā iztērē 12 + 8 = 20 €.",
                  "No 50 atņem visu summu: 50 − (12 + 8) = 30.",
                  "Iekavas saka: vispirms izrēķini šo."]),

    Doma("Iekavas - vispirms",
         "Darbību iekavās izpilda pirms visām pārējām.",
         soli=[
             "Atrodi iekavas.",
             "Izrēķini, kas iekavās: 12 + 8 = 20.",
             "Tad veic pārējās darbības: 50 − 20 = 30.",
             "Bez iekavām rēķina no kreisās uz labo.",
         ],
         pieze="50 − (12 + 8) = 30, bet 50 − 12 + 8 = 46. Iekavas maina "
               "rezultātu!"),

    Paraugs("Cik ir 70 − (25 + 15)?",
            uzd="Aprēķini ar iekavām.",
            soli=[("25 + 15 = 40", "Vispirms iekavās."),
                  ("70 − 40 = 30", "Tad atņem.")],
            atbilde="30"),

    Ievadi("Rēķini ar iekavām", [
        {"jaut": "60 − (20 + 10) = ?", "atb": ["30"], "padoms": "60 − 30."},
        {"jaut": "45 − (15 + 5) = ?", "atb": ["25"], "padoms": "45 − 20."},
        {"jaut": "90 − (34 + 16) = ?", "atb": ["40"], "padoms": "90 − 50."},
        {"jaut": "80 − (27 + 13) = ?", "atb": ["40"], "padoms": "80 − 40."},
        {"jaut": "100 − (45 + 25) = ?", "atb": ["30"], "padoms": "100 − 70."},
        {"jaut": "56 − (18 + 12) = ?", "atb": ["26"], "padoms": "56 − 30."},
    ], pamats=4),

    Varianti("Kura izteiksme der?", [
        {"jaut": "Kastē 40 konfektes. Anna paņēma 6, Toms 9. Cik palika? "
                 "(ar iekavām)",
         "opcijas": ["40 − (6 + 9)", "40 − 6 + 9", "(40 − 6) + 9"],
         "pareizi": 0, "padoms": "No 40 atņem abu kopā paņemto."},
        {"jaut": "Kurš pieraksts dod 30?",
         "opcijas": ["50 − (12 + 8)", "50 − 12 + 8", "50 + 12 − 8"],
         "pareizi": 0, "padoms": "50 − 20."},
    ]),

    Pasaule("Kabatas nauda",
            Ievadi("", [
                {"jaut": "Mēnesim 30 €. Kino 12 €, saldējums 5 €. Cik palika? "
                         "30 − (12 + 5) = ?", "atb": ["13"], "mers": "€",
                 "padoms": "30 − 17."},
                {"jaut": "Vēl nopirka grāmatu par 9 €. Cik tagad?",
                 "atb": ["4"], "mers": "€", "padoms": "13 − 9."},
            ]),
            pavediens="veikals",
            konteksts="Kabatas naudu tērē vairākiem pirkumiem.",
            kapec="Iekavās - visi tēriņi kopā."),

    Kopsavilkums([
        "Lietoju iekavas, ja jāatņem summa.",
        "Vispirms rēķinu iekavās.",
        "Zinu, ka iekavas var mainīt rezultātu.",
    ]),

    Majas([
        "Izdomā uzdevumu: no naudas atņem divus pirkumus.",
        "Pieraksti to ar iekavām un aprēķini.",
        "Aprēķini to pašu bez iekavām - vai sanāk cits skaitlis?",
    ]),
]
