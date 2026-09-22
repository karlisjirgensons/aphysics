# -*- coding: utf-8 -*-
"""6. klase, 127. stunda: «Kāpēc pretējo skaitļu summa ir nulle?»

Viena sakarība, kas atvieglo visu turpmāko rēķināšanu. Ja garā summā pamana
pretēju skaitļu pāri, to var izsvītrot - un bieži no garas izteiksmes paliek
divi skaitļi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kāpēc pretējo skaitļu summa ir nulle?"

MERKIS = ("Formulēsim secinājumu par pretējo skaitļu summu un lietosim to "
          "aprēķinos.")

SATURS = [
    Sakums("Divas vienāda garuma bultiņas pretējos virzienos",
           zimejums=taisne(-6, 6, 2, [(0, "sākums un gals")],
                           bultas=[(0, 4, "+4"), (4, 0, "−4")]),
           paraksts="Četri soļi pa labi un četri pa kreisi atgriež turpat, "
                    "kur sākām: 4 + (−4) = 0.",
           fakti=["Skaitļa un tā pretējā skaitļa summa vienmēr ir nulle.",
                  "Garā summā tādus pārus var izsvītrot.",
                  "Tas strādā arī ar daļām un decimāldaļām."]),

    Doma("Meklē pārus, pirms rēķini",
         "Pretējo skaitļu summa ir nulle, tāpēc garā izteiksmē vispirms "
         "atrod un izsvītro tādus pārus.",
         soli=[
             "Izlasi visu izteiksmi un pieraksti saskaitāmos ar zīmēm.",
             "Meklē pārus, kuros skaitļi ir vienādi pēc moduļa, bet ar "
             "pretējām zīmēm.",
             "Izsvītro katru tādu pāri.",
             "Saskaiti to, kas palicis.",
             "Pārbaudi, vai neviens saskaitāmais nav izlaists.",
         ],
         pieze="Pāri var būt ne tikai blakus: izteiksmē 5 + (−3) + (−5) + 3 "
               "ir divi pāri, un atbilde ir nulle. Tāpēc vispirms pārraksta "
               "visus saskaitāmos."),

    Paraugs("Izsvītro pārus",
            uzd="Cik ir 7 + (−4) + (−7) + 9 + 4?",
            soli=[
                ("Saskaitāmie: 7; −4; −7; 9; 4",
                 "Visi ar zīmēm."),
                ("7 un −7 ir pretēji - izsvītro",
                 "Pirmais pāris."),
                ("−4 un 4 arī - izsvītro",
                 "Otrais pāris."),
                ("Paliek 9",
                 "Vienīgais bez pāra."),
                ("Atbilde: 9",
                 "Bez neviena rēķina."),
            ],
            atbilde="9"),

    Ievadi("Atrodi pārus un saskaiti", [
        {"jaut": "Cik ir 4 + (−4)?",
         "atb": ["0"], "padoms": "Pretēji skaitļi."},
        {"jaut": "Cik ir 7 + (−4) + (−7) + 9 + 4?",
         "atb": ["9"], "padoms": "Divi pāri izsvītrojas."},
        {"jaut": "Cik ir −5 + 8 + 5?",
         "atb": ["8"], "padoms": "−5 un 5."},
        {"jaut": "Cik ir 12 + (−3) + (−12) + 3?",
         "atb": ["0"], "padoms": "Divi pāri."},
        {"jaut": "Cik ir −6 + 6 + (−2)?",
         "atb": ["-2", "−2"], "padoms": "Pirmais pāris izsvītrojas."},
        {"jaut": "Kāds skaitlis jāpieskaita skaitlim −11, lai iegūtu nulli?",
         "atb": ["11"], "padoms": "Pretējais skaitlis."},
    ], pamats=4,
        ievads="Vispirms meklē pārus - tikai tad saskaiti."),

    Varianti("Kur ir pāris?", [
        {"jaut": "Kurš skaitlis veido pāri ar −8?",
         "opcijas": ["8", "−8", "0", "16"],
         "pareizi": 0,
         "padoms": "Pretējais skaitlis."},
        {"jaut": "Izteiksmē 3 + (−5) + 5 + (−3) summa ir...",
         "opcijas": ["0", "6", "−6", "16"],
         "pareizi": 0,
         "padoms": "Divi pāri."},
        {"jaut": "Vai pāri var būt ne blakus?",
         "opcijas": ["Jā, saskaitāmos drīkst mainīt vietām",
                     "Nē, tikai blakus", "Nē, nekad",
                     "Tikai pozitīviem"],
         "pareizi": 0,
         "padoms": "Saskaitīšanā secība nav svarīga."},
        {"jaut": "Skaitļa un tā pretējā skaitļa summa ir...",
         "opcijas": ["vienmēr nulle", "vienmēr pozitīva",
                     "atkarīga no skaitļa", "vienmēr negatīva"],
         "pareizi": 0,
         "padoms": "Bultiņas izlīdzinās."},
    ], pamats=4),

    Pasaule("Kas paliek pēc visām izmaiņām?",
            Ievadi("", [
                {"jaut": "Kontā: +50; −30; −50; +30; +20. Cik eiro ir "
                         "kontā?",
                 "atb": ["20"], "padoms": "Divi pāri izsvītrojas."},
                {"jaut": "Temperatūra mainījās: +7; −4; −7; +2. Par cik "
                         "grādiem kopā?",
                 "atb": ["-2", "−2"], "padoms": "+7 un −7 izsvītrojas."},
                {"jaut": "Lifts: +5; −3; −5; +1. Par cik stāviem kopā?",
                 "atb": ["-2", "−2"], "padoms": "+5 un −5."},
                {"jaut": "Kontā: −40; +40. Cik eiro ir kontā?",
                 "atb": ["0"], "padoms": "Viens pāris."},
            ]),
            pavediens="veikals",
            konteksts="Bankas izrakstā ieņēmumi un izdevumi bieži veido "
                      "pārus - atcelts maksājums un pats maksājums.",
            kapec="Pretēju skaitļu pāris atlikumu nemaina."),

    Zimejums("Četri saskaitāmie, divi pāri",
             taisne(-8, 8, 4, [(0, "sākums un gals")],
                    bultas=[(0, 5, "+5"), (5, 0, "−5")]),
             paskaidro="Pirmais pāris jau atgriež pie nulles. Otrs pāris "
                       "darīs to pašu.",
             ievads="Katrs pāris ir turp un atpakaļ."),

    Kopsavilkums([
        "Zinu, ka pretējo skaitļu summa ir nulle.",
        "Meklēju pretēju skaitļu pārus garā izteiksmē.",
        "Izsvītroju tos un saskaitu atlikušos.",
        "Paskaidroju to ar bultiņām uz skaitļu taisnes.",
    ]),

    Majas([
        "Izrēķini 9 + (−6) + (−9) + 6 + 4.",
        "Izdomā izteiksmi ar pieciem saskaitāmajiem, kuras summa ir nulle.",
        "Atrodi bankas izrakstā vai pierakstos divus skaitļus, kas veido "
        "pāri.",
    ]),
]
