# -*- coding: utf-8 -*-
"""6. klase, 121. stunda: «Kā uzzīmēt simetrisku figūru pret asi?»

Otrā transformācija. Simetrija pret asi koordinātās izskatās vēl vienkāršāk
nekā pārvietošana: mainās tikai vienas koordinātas zīme. To skolēni atklāj
paši, salīdzinot virsotņu pārus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         plakne)

TEMA = "Kā uzzīmēt simetrisku figūru pret asi?"

MERKIS = ("Zīmēsim dotai figūrai simetrisku figūru pret koordinātu asi.")

SATURS = [
    Sakums("Spogulis maina vienu zīmi",
           zimejums=plakne(lauzta=[(1, 1), (4, 1), (4, 3)], aizpildi=True,
                           no_x=-5, lidz_x=5, no_y=-4, lidz_y=4, solis=1),
           paraksts="Ja šo trīsstūri atspoguļo pret vertikālo asi, pirmajām "
                    "koordinātām mainās zīme: (1; 1) → (−1; 1).",
           fakti=["Simetrija pret vertikālo asi maina pirmās koordinātas "
                  "zīmi.",
                  "Simetrija pret horizontālo asi maina otrās koordinātas "
                  "zīmi.",
                  "Figūras izmēri nemainās - mainās tikai puse."]),

    Doma("Viena ass - viena zīme",
         "Atspoguļojot figūru pret koordinātu asi, mainās tikai tās "
         "koordinātas zīme, kura mēra attālumu līdz šai asij.",
         soli=[
             "Nosaki, pret kuru asi jāatspoguļo.",
             "Pret vertikālo asi - maini pirmās koordinātas zīmi.",
             "Pret horizontālo asi - maini otrās koordinātas zīmi.",
             "Atliec jaunās virsotnes un savieno tās.",
             "Pārbaudi: abas figūras ir vienādā attālumā no ass.",
         ],
         pieze="Punkti, kas atrodas uz pašas ass, nemainās - to attālums "
               "līdz asij ir nulle. Tāpēc figūra, kas skar asi, pēc "
               "atspoguļošanas ar to sakrīt tieši šajos punktos."),

    Paraugs("Atspoguļo pret vertikālo asi",
            uzd="Trīsstūris (1; 1), (4; 1), (4; 3) jāatspoguļo pret "
                "vertikālo asi.",
            soli=[
                ("Pret vertikālo asi mainās pirmā koordināta",
                 "Otrā paliek tā pati."),
                ("(1; 1) → (−1; 1)",
                 "Pirmā virsotne."),
                ("(4; 1) → (−4; 1); (4; 3) → (−4; 3)",
                 "Pārējās divas."),
                ("Malu garumi nemainījās",
                 "3 un 2 vienības."),
            ],
            atbilde="(−1; 1), (−4; 1), (−4; 3)"),

    Ievadi("Atspoguļo punktu", [
        {"jaut": "Punktu (1; 1) atspoguļo pret vertikālo asi. Kāda ir jaunā "
                 "pirmā koordināta?",
         "atb": ["-1", "−1"], "padoms": "Maina zīmi."},
        {"jaut": "Kāda ir jaunā otrā koordināta?",
         "atb": ["1"], "padoms": "Nemainās."},
        {"jaut": "Punktu (3; −2) atspoguļo pret horizontālo asi. Kāda ir "
                 "jaunā otrā koordināta?",
         "atb": ["2"], "padoms": "Maina zīmi."},
        {"jaut": "Punktu (−4; 5) atspoguļo pret vertikālo asi. Kāda ir jaunā "
                 "pirmā koordināta?",
         "atb": ["4"], "padoms": "Mīnuss kļūst par plusu."},
        {"jaut": "Punkts (0; 3) atspoguļots pret vertikālo asi. Kāda ir "
                 "jaunā pirmā koordināta?",
         "atb": ["0"], "padoms": "Punkts ir uz ass."},
        {"jaut": "Punktu (2; 6) atspoguļo pret horizontālo asi. Kāda ir "
                 "jaunā otrā koordināta?",
         "atb": ["-6", "−6"], "padoms": "Maina zīmi."},
    ], pamats=4),

    Petijums("Atspoguļo savu figūru",
             vajag="rūtiņu lapa, spogulis vai caurspīdīgs papīrs",
             soli=[
                 "Uzzīmē plaknē kādu četrstūri pirmajā kvadrantā.",
                 "Pieraksti tā virsotņu koordinātas.",
                 "Atspoguļo to pret vertikālo asi un pieraksti jaunās "
                 "koordinātas.",
                 "Pārbaudi ar spoguli vai pārlokot lapu pa asi.",
                 "Pieraksti, kura koordināta mainījās.",
             ],
             secinajums="Pārlokot lapu pa asi, abas figūras sakrīt - tā ir "
                        "simetrijas pārbaude bez rēķina."),

    Varianti("Kura koordināta mainās?", [
        {"jaut": "Atspoguļojot pret vertikālo asi, mainās...",
         "opcijas": ["pirmā koordināta", "otrā koordināta",
                     "abas", "neviena"],
         "pareizi": 0,
         "padoms": "Attālums līdz vertikālajai asij."},
        {"jaut": "Atspoguļojot pret horizontālo asi, mainās...",
         "opcijas": ["otrā koordināta", "pirmā koordināta",
                     "abas", "neviena"],
         "pareizi": 0,
         "padoms": "Attālums līdz horizontālajai asij."},
        {"jaut": "Kuri punkti atspoguļojot nemainās?",
         "opcijas": ["Tie, kas atrodas uz pašas ass",
                     "Tie, kas ir sākumpunktā",
                     "Visi", "Neviens"],
         "pareizi": 0,
         "padoms": "Attālums līdz asij ir nulle."},
        {"jaut": "Punkts (−3; 4) pēc atspoguļošanas pret horizontālo asi "
                 "ir...",
         "opcijas": ["(−3; −4)", "(3; 4)", "(3; −4)", "(−4; 3)"],
         "pareizi": 0,
         "padoms": "Maina otro zīmi."},
    ], pamats=4),

    Pasaule("Kā uzzīmēt simetrisku rakstu?",
            Ievadi("", [
                {"jaut": "Raksta puse ir punktos (1; 2), (3; 2), (3; 4). "
                         "Atspoguļojot pret vertikālo asi, kāda ir pirmā "
                         "punkta pirmā koordināta?",
                 "atb": ["-1", "−1"], "padoms": "Maina zīmi."},
                {"jaut": "Cik virsotņu būs visam rakstam kopā?",
                 "atb": ["6"], "padoms": "3 + 3."},
                {"jaut": "Cik vienības plats ir viss raksts no −3 līdz 3?",
                 "atb": ["6"], "padoms": "3 + 3."},
                {"jaut": "Ja viena vienība ir 5 cm, cik centimetru plats ir "
                         "raksts?",
                 "atb": ["30"], "padoms": "6 · 5."},
            ]),
            pavediens="maja",
            konteksts="Tautiskos rakstos viena puse ir otras spoguļattēls - "
                      "tāpēc pietiek uzzīmēt pusi.",
            kapec="Simetrija samazina darbu uz pusi."),

    Zimejums("Abas puses kopā",
             plakne(lauzta=[(-4, 1), (-1, 1), (-4, 3)], aizpildi=True,
                    no_x=-5, lidz_x=5, no_y=-4, lidz_y=4, solis=1),
             paskaidro="Spoguļattēls stundas sākuma trīsstūrim. Abas figūras "
                       "ir vienādā attālumā no vertikālās ass.",
             ievads="Otrā puse, kas iegūta ar atspoguļošanu."),

    Kopsavilkums([
        "Zīmēju figūrai simetrisku figūru pret koordinātu asi.",
        "Zinu, kura koordināta maina zīmi katrā gadījumā.",
        "Pārbaudu simetriju, pārlokot lapu pa asi.",
        "Zinu, ka punkti uz ass nemainās.",
    ]),

    Majas([
        "Uzzīmē figūru un tās spoguļattēlu pret vertikālo asi.",
        "Uzzīmē to pašu figūru un spoguļattēlu pret horizontālo asi.",
        "Pieraksti, ar ko abi rezultāti atšķiras.",
    ]),
]
