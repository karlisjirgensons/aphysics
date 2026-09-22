# -*- coding: utf-8 -*-
"""5. klase, 17. stunda: «Kā saskatīt sakarību summā?»

Jauna mikrotemata sākums: saskaitīšana un atņemšana nav jauna darbība, bet
jauns skatiens. Vairāku saskaitāmo summu te rēķina nevis no kreisās uz labo,
bet meklējot pārus, kas dod apaļu skaitli - tā pati pārkārtošana vēlāk noder
daļām un decimāldaļām.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā saskatīt sakarību summā?"

MERKIS = ("Iemācīsimies pārkārtot un grupēt saskaitāmos tā, lai vairāku "
          "skaitļu summu var izrēķināt galvā.")

SATURS = [
    Sakums("Kurš izrēķinās ātrāk?",
           fakti=["37 + 48 + 63 + 52 - četri skaitļi, neviens nav apaļš.",
                  "Viens skolēns rēķina pēc kārtas un raksta trīs soļus.",
                  "Otrs saliek pa pāriem un pasaka atbildi uzreiz."]),

    Doma("Saskaitāmos drīkst pārkārtot un salikt pa pāriem",
         "Summa nemainās, ja saskaitāmos samaina vietām vai apvieno grupās.",
         soli=[
             "Pārskati visus saskaitāmos, pirms sāc rēķināt.",
             "Meklē pārus, kuru summa ir apaļa: 10, 100 vai 1 000.",
             "Saskaiti katru pāri atsevišķi.",
             "Saskaiti apaļos rezultātus - to var izdarīt galvā.",
         ],
         pieze="Pārkārtot drīkst tikai saskaitāmos. Ja izteiksmē ir "
               "atņemšana, zīme ceļo kopā ar skaitli: 50 − 17 + 30 nav "
               "tas pats, kas "
               "50 − (17 + 30)."),

    Paraugs("Saliec pa pāriem",
            uzd="Aprēķini 37 + 48 + 63 + 52 racionāli.",
            soli=[
                ("37 + 63 = 100",
                 "Vienu ciparu summa ir 10, desmitu - 9 desmiti + 1."),
                ("48 + 52 = 100",
                 "Otrs pāris arī dod apaļu simtu."),
                ("100 + 100 = 200",
                 "Atlikušo saskaitīšanu var izdarīt galvā."),
            ],
            atbilde="37 + 48 + 63 + 52 = 200"),

    Ievadi("Atrodi pāri un izrēķini", [
        {"jaut": "25 + 37 + 75 = ?", "atb": ["137"],
         "padoms": "25 + 75 = 100."},
        {"jaut": "48 + 19 + 52 + 81 = ?", "atb": ["200"],
         "padoms": "48 + 52 un 19 + 81."},
        {"jaut": "128 + 96 + 72 = ?", "atb": ["296"],
         "padoms": "128 + 72 = 200."},
        {"jaut": "17 + 45 + 83 + 55 = ?", "atb": ["200"],
         "padoms": "17 + 83 un 45 + 55."},
        {"jaut": "1 250 + 380 + 750 = ?", "atb": ["2380"],
         "padoms": "1 250 + 750 = 2 000."},
        {"jaut": "64 + 29 + 36 + 71 = ?", "atb": ["200"],
         "padoms": "64 + 36 un 29 + 71."},
        {"jaut": "199 + 246 + 1 = ?", "atb": ["446"],
         "padoms": "199 + 1 = 200."},
        {"jaut": "97 + 58 + 3 + 42 = ?", "atb": ["200"],
         "padoms": "97 + 3 un 58 + 42."},
    ], pamats=4,
        ievads="Vispirms paskaties uz visiem saskaitāmajiem, tikai tad "
               "rēķini."),

    Varianti("Kur slēpjas sakarība?", [
        {"jaut": "Kurš pāris izteiksmē 28 + 45 + 72 + 51 jāsaliek kopā?",
         "opcijas": ["28 un 72", "28 un 45", "45 un 72", "28 un 51"],
         "pareizi": 0,
         "padoms": "Meklē to pāri, kas dod apaļu simtu."},
        {"jaut": "Kāpēc saskaitāmos drīkst samainīt vietām?",
         "opcijas": ["Summa no secības nemainās",
                     "Jo tā ir ātrāk rakstīt",
                     "Jo skaitļi ir mazi",
                     "Tā drīkst tikai ar apaļiem skaitļiem"],
         "pareizi": 0,
         "padoms": "Pārbaudi ar 3 + 5 un 5 + 3."},
        {"jaut": "Izteiksmē 80 − 25 + 15 skolēns saskaitīja 25 + 15 un "
                 "atņēma. Kas notika?",
         "opcijas": ["Sanāca cita izteiksme un cita atbilde",
                     "Nekas, atbilde ir tā pati",
                     "Atbilde kļuva lielāka par 80",
                     "Izteiksme kļuva vienkāršāka"],
         "pareizi": 0,
         "padoms": "80 − 25 + 15 = 70, bet 80 − (25 + 15) = 40."},
        {"jaut": "Ko izdevīgāk meklēt garā summā?",
         "opcijas": ["Pārus, kas dod apaļu skaitli",
                     "Vislielāko skaitli",
                     "Vismazāko skaitli",
                     "Pāra skaitļus"],
         "pareizi": 0,
         "padoms": "Apaļus skaitļus saskaita galvā."},
    ], pamats=4),

    Pasaule("Cik skolēnu piedalījās?",
            Ievadi("", [
                {"jaut": "Klasēs ir 23, 27, 18 un 22 skolēni. Cik pavisam?",
                 "atb": ["90"], "padoms": "23 + 27 = 50 un 18 + 22 = 40."},
                {"jaut": "Ēdnīcā izsniedza 145, 155 un 130 porcijas. Cik "
                         "pavisam?",
                 "atb": ["430"], "padoms": "145 + 155 = 300."},
                {"jaut": "Bibliotēkā atdeva 68, 32 un 45 grāmatas. Cik "
                         "pavisam?",
                 "atb": ["145"], "padoms": "68 + 32 = 100."},
                {"jaut": "Sporta dienā skrēja 115, 85 un 60 skolēni. Cik "
                         "pavisam?",
                 "atb": ["260"], "padoms": "115 + 85 = 200."},
            ]),
            pavediens="skola",
            konteksts="Skolā skaitļus saskaita katru dienu - pa klasēm, pa "
                      "porcijām, pa grāmatām - un vienmēr pa vairākiem.",
            kapec="Pāris, kas dod apaļu skaitli, atbildi pietuvina par vienu "
                  "soli."),

    Kopsavilkums([
        "Pirms rēķināšanas pārskatu visus saskaitāmos.",
        "Pārkārtoju un grupēju saskaitāmos, lai sanāk apaļi skaitļi.",
        "Zinu, ka atņemšanā zīme ceļo kopā ar skaitli.",
    ]),

    Majas([
        "Izdomā četrus skaitļus, kuru summa ir tieši 200, un iedod tos "
        "draugam izrēķināt.",
        "Saskaiti čeka summas, meklējot pārus, kas dod apaļus eiro.",
        "Uzraksti izteiksmi, kurā pārkārtošana nepalīdz, un paskaidro kāpēc.",
    ]),
]
