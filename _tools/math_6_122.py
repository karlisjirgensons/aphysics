# -*- coding: utf-8 -*-
"""6. klase, 122. stunda: «Kā pagriezt figūru par 180°?»

Temata pēdējā mācību stunda. Pagrieziens par 180° ap sākumpunktu ir
simetrija pret punktu, un koordinātās tā ir visvienkāršākā no visām
transformācijām: abām koordinātām mainās zīme.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         plakne)

TEMA = "Kā pagriezt figūru par 180°?"

MERKIS = ("Zīmēsim figūru, kas simetriska dotajai pret punktu, un "
          "skaidrosim savu rīcību.")

SATURS = [
    Sakums("Abas zīmes mainās reizē",
           zimejums=plakne(lauzta=[(1, 1), (4, 1), (4, 3)], aizpildi=True,
                           no_x=-5, lidz_x=5, no_y=-4, lidz_y=4, solis=1),
           paraksts="Pagriežot šo trīsstūri par 180° ap sākumpunktu, "
                    "(1; 1) → (−1; −1): abām koordinātām mainās zīme.",
           fakti=["Pagrieziens par 180° ir simetrija pret punktu.",
                  "Abām koordinātām mainās zīme.",
                  "Sākumpunkts paliek savā vietā."]),

    Doma("Maini abas zīmes",
         "Pagriežot figūru par 180° ap sākumpunktu, katras virsotnes abām "
         "koordinātām maina zīmi uz pretējo.",
         soli=[
             "Pieraksti visu virsotņu koordinātas.",
             "Katrai virsotnei maini abu koordinātu zīmes.",
             "Atliec jaunās virsotnes.",
             "Savieno tās tādā pašā secībā kā sākotnējā figūrā.",
             "Pārbaudi: sākumpunkts ir tieši vidū starp atbilstošajām "
             "virsotnēm.",
         ],
         pieze="Tas ir tas pats, kas atspoguļot divreiz: vispirms pret vienu "
               "asi, tad pret otru. Tāpēc arī mainās abas zīmes."),

    Paraugs("Pagriez trīsstūri",
            uzd="Trīsstūris (1; 1), (4; 1), (4; 3) jāpagriež par 180° ap "
                "sākumpunktu.",
            soli=[
                ("(1; 1) → (−1; −1)",
                 "Abas zīmes mainās."),
                ("(4; 1) → (−4; −1)",
                 "Otrā virsotne."),
                ("(4; 3) → (−4; −3)",
                 "Trešā virsotne."),
                ("Pārbaude: starp (1; 1) un (−1; −1) vidū ir (0; 0)",
                 "Sākumpunkts ir simetrijas centrs."),
            ],
            atbilde="(−1; −1), (−4; −1), (−4; −3)"),

    Ievadi("Pagriez punktu", [
        {"jaut": "Punktu (1; 1) pagriež par 180°. Kāda ir jaunā pirmā "
                 "koordināta?",
         "atb": ["-1", "−1"], "padoms": "Maina zīmi."},
        {"jaut": "Kāda ir jaunā otrā koordināta?",
         "atb": ["-1", "−1"], "padoms": "Arī maina zīmi."},
        {"jaut": "Punktu (−3; 2) pagriež par 180°. Kāda ir jaunā pirmā "
                 "koordināta?",
         "atb": ["3"], "padoms": "Mīnuss kļūst par plusu."},
        {"jaut": "Kāda ir tā jaunā otrā koordināta?",
         "atb": ["-2", "−2"], "padoms": "Pluss kļūst par mīnusu."},
        {"jaut": "Punkts (0; 0) pēc pagrieziena. Kāda ir tā pirmā "
                 "koordināta?",
         "atb": ["0"], "padoms": "Centrs nemainās."},
        {"jaut": "Punkts (5; −4) pagriezts par 180°. Kāda ir jaunā otrā "
                 "koordināta?",
         "atb": ["4"], "padoms": "−4 kļūst par 4."},
    ], pamats=4),

    Varianti("Kura transformācija tā ir?", [
        {"jaut": "Ja abām koordinātām mainās zīme, tas ir...",
         "opcijas": ["pagrieziens par 180°",
                     "atspoguļojums pret vertikālo asi",
                     "pārvietojums", "nekas nemainās"],
         "pareizi": 0,
         "padoms": "Simetrija pret punktu."},
        {"jaut": "Ja mainās tikai otrā koordināta, tas ir...",
         "opcijas": ["atspoguļojums pret horizontālo asi",
                     "pagrieziens par 180°",
                     "pārvietojums pa labi", "nekas"],
         "pareizi": 0,
         "padoms": "Viena ass - viena zīme."},
        {"jaut": "Ja abām koordinātām pieskaita skaitli, tas ir...",
         "opcijas": ["pārvietojums", "pagrieziens",
                     "atspoguļojums", "palielinājums"],
         "pareizi": 0,
         "padoms": "Saskaitīšana, ne zīmes maiņa."},
        {"jaut": "Punkts (2; −5) pēc pagrieziena par 180° ir...",
         "opcijas": ["(−2; 5)", "(−2; −5)", "(2; 5)", "(5; −2)"],
         "pareizi": 0,
         "padoms": "Abas zīmes."},
    ], pamats=4),

    Petijums("Trīs transformācijas vienai figūrai",
             vajag="rūtiņu lapa",
             soli=[
                 "Uzzīmē trīsstūri pirmajā kvadrantā un pieraksti "
                 "koordinātas.",
                 "Pārvieto to par 3 pa kreisi un pieraksti jaunās.",
                 "Atspoguļo sākotnējo pret vertikālo asi.",
                 "Pagriez sākotnējo par 180° ap sākumpunktu.",
                 "Salīdzini visas trīs jaunās figūras.",
             ],
             secinajums="Visās trijās figūra ir tikpat liela, mainās tikai "
                        "tās vieta un orientācija - un katrai ir savs "
                        "koordinātu likums."),

    Pasaule("Kā pagriezt detaļu rasējumā?",
            Ievadi("", [
                {"jaut": "Detaļas stūris ir (3; 2). Pagriežot par 180°, kāda "
                         "ir jaunā pirmā koordināta?",
                 "atb": ["-3", "−3"], "padoms": "Maina zīmi."},
                {"jaut": "Otrs stūris ir (3; −2). Kāda ir tā jaunā otrā "
                         "koordināta?",
                 "atb": ["2"], "padoms": "−2 kļūst par 2."},
                {"jaut": "Cik vienības gara ir mala starp (3; 2) un (3; −2)?",
                 "atb": ["4"], "padoms": "2 + 2."},
                {"jaut": "Cik vienības gara tā ir pēc pagrieziena?",
                 "atb": ["4"], "padoms": "Izmēri nemainās."},
            ]),
            pavediens="tehnika",
            konteksts="Rasējumā detaļu bieži jāparāda apgrieztu - un tad "
                      "visām koordinātām maina zīmi.",
            kapec="Pagrieziens nemaina detaļas izmērus, tikai orientāciju."),

    Zimejums("Figūra pēc pagrieziena",
             plakne(lauzta=[(-1, -1), (-4, -1), (-4, -3)], aizpildi=True,
                    no_x=-5, lidz_x=5, no_y=-4, lidz_y=4, solis=1),
             paskaidro="Tas pats trīsstūris pēc pagrieziena par 180°. "
                       "Sākumpunkts ir tieši starp abām figūrām.",
             ievads="Salīdzini ar stundas sākuma zīmējumu."),

    Kopsavilkums([
        "Zīmēju figūru, kas simetriska dotajai pret punktu.",
        "Mainu abu koordinātu zīmes.",
        "Pārbaudu, vai sākumpunkts ir vidū starp virsotnēm.",
        "Atšķiru pārvietojumu, atspoguļojumu un pagriezienu.",
    ]),

    Majas([
        "Uzzīmē četrstūri un pagriez to par 180° ap sākumpunktu.",
        "Pieraksti abu figūru koordinātas.",
        "Pieraksti, ar ko pagrieziens atšķiras no atspoguļojuma.",
    ]),
]
