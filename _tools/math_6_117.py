# -*- coding: utf-8 -*-
"""6. klase, 117. stunda: «Kā pieraksta punkta koordinātas?»

Jauns mikrotemats. Koordinātu pieraksts ir vienošanās: pirmais skaitlis
vienmēr ir horizontālais. Tieši secība ir tā, kas jāiemācās - (3; −2) un
(−2; 3) ir divi pavisam dažādi punkti.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, plakne)

TEMA = "Kā pieraksta punkta koordinātas?"

MERKIS = ("Iemācīsimies nolasīt un pierakstīt koordinātu plaknē atlikto "
          "punktu koordinātas.")

SATURS = [
    Sakums("Pirmais skaitlis - pa labi vai pa kreisi",
           zimejums=plakne(punkti=[(3, -2, "A"), (-2, 3, "B")],
                           no_x=-4, lidz_x=4, no_y=-4, lidz_y=4, solis=1),
           paraksts="A ir (3; −2), B ir (−2; 3). Tie paši skaitļi, bet cita "
                    "secība - un pavisam cita vieta.",
           fakti=["Pirmā koordināta rāda kustību pa horizontālo asi.",
                  "Otrā - pa vertikālo.",
                  "Punktu pieraksta iekavās, atdalot ar semikolu."]),

    Doma("Vispirms pa labi, tad uz augšu",
         "Punkta koordinātas pieraksta pārī: pirmā ir attālums pa "
         "horizontālo asi, otrā - pa vertikālo; abas var būt negatīvas.",
         soli=[
             "No sākumpunkta ej pa horizontālo asi līdz punkta vietai.",
             "Nolasi šo skaitli ar zīmi - tā ir pirmā koordināta.",
             "No turienes ej pa vertikāli līdz punktam.",
             "Nolasi otro skaitli ar zīmi.",
             "Pieraksti abus iekavās, atdalot ar semikolu.",
         ],
         pieze="Ja punkts atrodas uz horizontālās ass, otrā koordināta ir "
               "nulle; ja uz vertikālās - pirmā. Sākumpunkts ir (0; 0), "
               "vienīgais punkts ar abām koordinātām nulle."),

    Paraugs("Nolasi koordinātas",
            uzd="Punkts A atrodas trīs soļus pa labi un divus uz leju no "
                "sākumpunkta. Kādas ir tā koordinātas?",
            soli=[
                ("Pa labi ir pozitīvs virziens",
                 "Pirmā koordināta ir 3."),
                ("Uz leju ir negatīvs virziens",
                 "Otrā koordināta ir −2."),
                ("A(3; −2)",
                 "Pieraksts ar semikolu."),
                ("Salīdzinājumam: B(−2; 3) ir pavisam citur",
                 "Secība maina vietu."),
            ],
            atbilde="A(3; −2)"),

    Ievadi("Nolasi un pieraksti", [
        {"jaut": "Punkts ir 3 pa labi un 2 uz leju. Kāda ir pirmā "
                 "koordināta?",
         "atb": ["3"], "padoms": "Pa labi - pozitīvs."},
        {"jaut": "Kāda ir otrā koordināta?",
         "atb": ["-2", "−2"], "padoms": "Uz leju - negatīvs."},
        {"jaut": "Punkts C(−4; 0). Uz kuras ass tas atrodas? Raksti «x» vai "
                 "«y».",
         "atb": ["x"], "padoms": "Otrā koordināta ir nulle."},
        {"jaut": "Punkts D(0; 5). Kāda ir tā pirmā koordināta?",
         "atb": ["0"], "padoms": "Uz vertikālās ass."},
        {"jaut": "Kādas koordinātas ir sākumpunktam? Ieraksti otro "
                 "koordinātu.",
         "atb": ["0"], "padoms": "(0; 0)."},
        {"jaut": "Punkts ir 5 pa kreisi un 1 uz augšu. Kāda ir pirmā "
                 "koordināta?",
         "atb": ["-5", "−5"], "padoms": "Pa kreisi - negatīvs."},
    ], pamats=4),

    Varianti("Kur atrodas punkts?", [
        {"jaut": "Punkts (3; −2) atrodas...",
         "opcijas": ["pa labi un uz leju", "pa kreisi un uz augšu",
                     "pa labi un uz augšu", "uz ass"],
         "pareizi": 0,
         "padoms": "Pirmā koordināta pozitīva, otrā negatīva."},
        {"jaut": "Vai (3; −2) un (−2; 3) ir viens un tas pats punkts?",
         "opcijas": ["Nē, secība maina vietu", "Jā, skaitļi tie paši",
                     "Jā, ja abi ir plaknē", "Nevar zināt"],
         "pareizi": 0,
         "padoms": "Pirmā koordināta vienmēr ir horizontālā."},
        {"jaut": "Punkts ar koordinātām (−5; 0) atrodas...",
         "opcijas": ["uz horizontālās ass", "uz vertikālās ass",
                     "sākumpunktā", "otrajā kvadrantā"],
         "pareizi": 0,
         "padoms": "Otrā koordināta ir nulle."},
        {"jaut": "Punkti ar abām negatīvām koordinātām atrodas...",
         "opcijas": ["pa kreisi un zem ass", "pa labi un zem ass",
                     "pa kreisi un virs ass", "uz asīm"],
         "pareizi": 0,
         "padoms": "Abas koordinātas negatīvas."},
    ], pamats=4),

    Pasaule("Kur atrodas objekts kartē?",
            Ievadi("", [
                {"jaut": "Kuģis ir 4 vienības uz austrumiem un 3 uz "
                         "dienvidiem no ostas. Kāda ir pirmā koordināta, ja "
                         "austrumi ir pozitīvi?",
                 "atb": ["4"], "padoms": "Austrumi - pa labi.",
                 "zim": plakne(punkti=[(4, -3, "kuģis")], no_x=-5, lidz_x=5,
                               no_y=-5, lidz_y=5, solis=1)},
                {"jaut": "Kāda ir otrā koordināta, ja ziemeļi ir pozitīvi?",
                 "atb": ["-3", "−3"], "padoms": "Dienvidi - uz leju."},
                {"jaut": "Otrs kuģis ir punktā (−2; −4). Cik vienības uz "
                         "rietumiem no ostas tas ir?",
                 "atb": ["2"], "padoms": "Modulis."},
                {"jaut": "Cik vienības uz dienvidiem tas ir?",
                 "atb": ["4"], "padoms": "Modulis otrajai koordinātai."},
            ]),
            pavediens="celojums",
            konteksts="Jūras kartē katram objektam ir divas koordinātas - un "
                      "secība tajās ir stingri noteikta.",
            kapec="Sajaukta secība nozīmē pavisam citu vietu."),

    Zimejums("Četri punkti četros kvadrantos",
             plakne(punkti=[(3, 2, "A"), (-3, 2, "B"), (-3, -2, "C"),
                            (3, -2, "D")],
                    no_x=-4, lidz_x=4, no_y=-4, lidz_y=4, solis=1),
             paskaidro="A(3; 2), B(−3; 2), C(−3; −2), D(3; −2). Zīmes pasaka, "
                       "kurā kvadrantā punkts atrodas.",
             ievads="Pa vienam punktam katrā plaknes daļā."),

    Kopsavilkums([
        "Nolasu punkta koordinātas no koordinātu plaknes.",
        "Pierakstu tās iekavās, atdalot ar semikolu.",
        "Zinu, ka pirmā koordināta ir horizontālā.",
        "Nosaku, kurā kvadrantā punkts atrodas pēc zīmēm.",
    ]),

    Majas([
        "Uzzīmē plakni un atzīmē punktus (2; 3), (−2; 3) un (−2; −3).",
        "Pieraksti, kurā kvadrantā katrs atrodas.",
        "Atrodi divus punktus, kuri atrodas uz asīm.",
    ]),
]
