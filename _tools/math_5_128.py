# -*- coding: utf-8 -*-
"""5. klase, 128. stunda: «Cik liels ir figūras laukums?»

Te trīs iepriekšējās stundas saplūst vienā uzdevumā: pārveidot vienības,
atrast trūkstošās malas, sadalīt figūru un saskaitīt laukumus. Tāpēc stundas
galvenā prasība nav atbilde, bet plāns - pateikt iepriekš, kādā secībā tas
viss tiks darīts.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, figura)

TEMA = "Cik liels ir figūras laukums?"

MERKIS = ("Iemācīsimies aprēķināt kombinētas figūras laukumu un skaidrot "
          "savu plānu.")

SATURS = [
    Sakums("Četri soļi līdz laukumam",
           zimejums=figura([(0, 0), (6, 0), (6, 2), (3, 2), (3, 5), (0, 5)],
                           uzraksti=[(3, -0.4, "6 m"), (6.8, 1, "2 m"),
                                     (-0.8, 2.5, "5 m")],
                           virsraksts="Kombinēta grīda"),
           paraksts="Laukums ir 21 m², bet līdz tam ir četri soļi.",
           fakti=["Vispirms - vienas mērvienības.",
                  "Tad trūkstošās malas.",
                  "Tad sadalījums un laukumu summa."]),

    Doma("Vispirms plāns, tad rēķins",
         "Kombinētas figūras laukumu aprēķina pa soļiem: vienādo mērvienības, "
         "atrod trūkstošās malas, sadala figūru un saskaita gabalu laukumus.",
         soli=[
             "Pārbaudi, vai visi izmēri ir vienās vienībās.",
             "Aprēķini trūkstošās malas.",
             "Sadali figūru taisnstūros un apzīmē tos.",
             "Aprēķini katra gabala laukumu.",
             "Saskaiti laukumus un pieraksti atbildi ar kvadrātvienību.",
         ],
         pieze="Plānu var pateikt vārdiem, pirms uzrakstīts kaut viens "
               "skaitlis: «sadalīšu divos taisnstūros, izrēķināšu abus un "
               "saskaitīšu». Tieši tas atšķir risinājumu no minēšanas."),

    Paraugs("L formas grīdas laukums",
            uzd="Grīdas malas ir 6 m, 2 m un 5 m; pārējās jāaprēķina. Cik "
                "kvadrātmetru ir laukums?",
            soli=[
                ("Visi izmēri ir metros",
                 "Pirmais solis izpildīts."),
                ("Trūkstošās malas: 5 - 2 = 3 un 6 - 3 = 3",
                 "Otrais solis."),
                ("Sadalījums: 6 x 2 un 3 x 3",
                 "Trešais solis."),
                ("12 + 9 = 21",
                 "Ceturtais solis."),
                ("S = 21 m²",
                 "Atbilde ar kvadrātvienību."),
            ],
            atbilde="S = 21 m²"),

    Ievadi("Aprēķini laukumu pa soļiem", [
        {"jaut": "Gabals 6 m x 2 m. Cik kvadrātmetru?",
         "atb": ["12"], "padoms": "6 · 2."},
        {"jaut": "Gabals 3 m x 3 m. Cik kvadrātmetru?",
         "atb": ["9"], "padoms": "3 · 3."},
        {"jaut": "Cik kvadrātmetru ir abi gabali kopā?",
         "atb": ["21"], "padoms": "12 + 9."},
        {"jaut": "Liels taisnstūris 8 m x 5 m. Cik kvadrātmetru?",
         "atb": ["40"], "padoms": "8 · 5."},
        {"jaut": "No tā izgriež 2 m x 3 m gabalu. Cik kvadrātmetru paliek?",
         "atb": ["34"], "padoms": "40 - 6."},
        {"jaut": "Gabali 4 m x 3 m un 2 m x 2 m. Cik kvadrātmetru kopā?",
         "atb": ["16"], "padoms": "12 + 4."},
        {"jaut": "Gabali 5 m x 4 m un 5 m x 2 m. Cik kvadrātmetru kopā?",
         "atb": ["30"], "padoms": "20 + 10."},
        {"jaut": "Liels taisnstūris 10 m x 6 m, izgriezts 4 m x 3 m. Cik "
                 "kvadrātmetru paliek?",
         "atb": ["48"], "padoms": "60 - 12."},
    ], pamats=4,
        ievads="Katru gabalu rēķini atsevišķi, tikai tad saskaiti."),

    Zimejums("Tā pati figūra ar visiem izmēriem",
             figura([(0, 0), (6, 0), (6, 2), (3, 2), (3, 5), (0, 5)],
                    uzraksti=[(3, -0.4, "6 m"), (6.8, 1, "2 m"),
                              (4.5, 1.7, "3 m"), (3.7, 3.5, "3 m"),
                              (1.5, 5.4, "3 m"), (-0.8, 2.5, "5 m")],
                    virsraksts="Visi seši izmēri"),
             paskaidro="Kad visi izmēri ir atzīmēti, sadalījumu var izvēlēties "
                       "un laukumu izrēķināt bez jauniem mērījumiem.",
             ievads="Pilns rasējums ir puse darba."),

    Varianti("Kāds ir plāns?", [
        {"jaut": "Kas ir pirmais solis?",
         "opcijas": ["Pārbaudīt mērvienības", "Sadalīt figūru",
                     "Saskaitīt laukumus", "Uzrakstīt atbildi"],
         "pareizi": 0,
         "padoms": "Reizināt drīkst tikai vienādas vienības."},
        {"jaut": "Kas ir pēdējais solis?",
         "opcijas": ["Atbilde ar kvadrātvienību", "Sadalīšana",
                     "Trūkstošo malu meklēšana", "Mērvienību pārbaude"],
         "pareizi": 0,
         "padoms": "Laukumam ir sava vienība."},
        {"jaut": "Figūra 6 x 2 un 3 x 3. Cik ir laukums?",
         "opcijas": ["21", "18", "30", "11"],
         "pareizi": 0,
         "padoms": "12 + 9."},
        {"jaut": "Kad lieto atņemšanu?",
         "opcijas": ["Kad figūru papildina līdz taisnstūrim",
                     "Vienmēr",
                     "Nekad",
                     "Kad malas ir garas"],
         "pareizi": 0,
         "padoms": "No lielā atņem iztrūkstošo."},
        {"jaut": "Kāpēc plānu pasaka pirms rēķina?",
         "opcijas": ["Lai neizlaistu nevienu soli", "Lai būtu ātrāk",
                     "Lai atbilde būtu skaistāka", "Tas nav vajadzīgs"],
         "pareizi": 0,
         "padoms": "Izlaists solis ir biežākā kļūda."},
        {"jaut": "Kādā vienībā pieraksta laukumu?",
         "opcijas": ["Kvadrātvienībā", "Metros", "Centimetros", "Grādos"],
         "pareizi": 0,
         "padoms": "m² vai cm²."},
    ], pamats=4),

    Pasaule("Cik laminata vajag?",
            Ievadi("", [
                {"jaut": "Istaba ir L formas: gabali 6 m x 2 m un 3 m x 3 m. "
                         "Cik kvadrātmetru ir grīda?",
                 "atb": ["21"], "padoms": "12 + 9."},
                {"jaut": "Laminātu pārdod pa 2 m² paciņā. Cik paciņu vajag "
                         "vismaz?",
                 "atb": ["11"], "padoms": "21 : 2 - un noapaļo uz augšu."},
                {"jaut": "Cita istaba: 8 m x 5 m, izgriezta niša 2 m x 3 m. "
                         "Cik kvadrātmetru ir grīda?",
                 "atb": ["34"], "padoms": "40 - 6."},
                {"jaut": "Cik paciņu pa 2 m² vajag šai istabai?",
                 "atb": ["17"], "padoms": "34 : 2."},
            ]),
            pavediens="maja",
            konteksts="Veikalā jāzina viens skaitlis - kvadrātmetru skaits -, "
                      "bet istaba nav taisnstūris.",
            kapec="Plāns pa soļiem noved no rasējuma līdz paciņu skaitam."),

    Kopsavilkums([
        "Aprēķinu kombinētas figūras laukumu pa soļiem.",
        "Pasaku plānu, pirms sāku rēķināt.",
        "Sadalu figūru vai papildinu to līdz taisnstūrim.",
        "Pierakstu atbildi ar kvadrātvienību.",
    ]),

    Majas([
        "Aprēķini laukumu figūrai ar gabaliem 7 m x 3 m un 2 m x 2 m.",
        "Uzzīmē savas istabas plānu un aprēķini grīdas laukumu.",
        "Pieraksti savu plānu četros teikumos.",
    ]),
]
