# -*- coding: utf-8 -*-
"""6. klase, 158. stunda: «Kā izplānot garu aprēķinu?»

Jauns mikrotemats par darba organizāciju. Gara izteiksme ar visu veidu
skaitļiem nav grūtāka par īsu - tā tikai prasa plānu. Plānu te pieraksta
pirms rēķina, tieši tāpat kā 143. stundā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti)

TEMA = "Kā izplānot garu aprēķinu?"

MERKIS = ("Plānosim garu aprēķinu ar visu veidu skaitļiem un pierakstīsim "
          "to pa soļiem.")

SATURS = [
    Sakums("Gara izteiksme ir vairāki īsi soļi",
           fakti=["Vispirms izlasa visu izteiksmi, tikai tad rēķina.",
                  "Katru soli raksta jaunā rindā.",
                  "Iekavas un reizināšana ir pirms saskaitīšanas."]),

    Doma("Viens solis - viena rinda",
         "Garu aprēķinu plāno pa soļiem: nosaka darbību secību, izvēlas "
         "vienotu pierakstu un katru soli raksta atsevišķā rindā.",
         soli=[
             "Izlasi visu izteiksmi un atrodi iekavas.",
             "Nosaki darbību secību.",
             "Izvēlies, vai rēķināsi daļās vai decimāldaļās.",
             "Veic pa vienam solim, katru jaunā rindā.",
             "Pārbaudi rezultātu ar novērtējumu.",
         ],
         pieze="Ja vienā rindā izdara divus soļus, kļūdu vairs nevar atrast - "
               "jāpārrēķina viss. Tāpēc viena rinda ir viens solis."),

    Paraugs("Plāns un izpilde",
            uzd="Izrēķini (−3 + 7) · (−2) + 5.",
            soli=[
                ("Plāns: vispirms iekavas, tad reizināšana, tad saskaitīšana",
                 "Trīs soļi."),
                ("(−3 + 7) = 4",
                 "Pirmais solis."),
                ("4 · (−2) = −8",
                 "Otrais solis."),
                ("−8 + 5 = −3",
                 "Trešais solis."),
            ],
            atbilde="−3"),

    Ievadi("Izrēķini pa soļiem", [
        {"jaut": "Cik ir (−3 + 7) · (−2) + 5?",
         "atb": ["-3", "−3"], "padoms": "4 · (−2) + 5."},
        {"jaut": "Cik ir (−8) : 4 + 6?",
         "atb": ["4"], "padoms": "−2 + 6."},
        {"jaut": "Cik ir 2 · (−5) − (−4)?",
         "atb": ["-6", "−6"], "padoms": "−10 + 4."},
        {"jaut": "Cik ir (−12) : (−3) · 2?",
         "atb": ["8"], "padoms": "4 · 2."},
        {"jaut": "Cik ir (4 − 9) · (−2)?",
         "atb": ["10"], "padoms": "(−5) · (−2)."},
        {"jaut": "Cik ir −6 + 3 · (−2)?",
         "atb": ["-12", "−12"], "padoms": "Vispirms reizināšana."},
    ], pamats=4,
        ievads="Pirms rēķini, pasaki, kurā secībā darīsi."),

    Petijums("Pieraksti savu plānu",
             vajag="burtnīca un trīs garas izteiksmes",
             soli=[
                 "Izvēlies trīs izteiksmes ar iekavām un vairākām darbībām.",
                 "Katrai pieraksti plānu: darbību secību ar vārdiem.",
                 "Tikai tad izrēķini, katru soli jaunā rindā.",
                 "Pārbaudi katru rezultātu ar novērtējumu.",
                 "Atzīmē, kurā solī bija visvieglāk kļūdīties.",
             ],
             secinajums="Kļūdas gandrīz vienmēr rodas tur, kur divi soļi "
                        "izdarīti vienā rindā."),

    Varianti("Kura darbība ir pirmā?", [
        {"jaut": "Izteiksmē (−3 + 7) · (−2) pirmā ir...",
         "opcijas": ["iekava", "reizināšana", "saskaitīšana", "dalīšana"],
         "pareizi": 0,
         "padoms": "Iekavas vienmēr pirmās."},
        {"jaut": "Izteiksmē −6 + 3 · (−2) pirmā ir...",
         "opcijas": ["reizināšana", "saskaitīšana", "atņemšana", "dalīšana"],
         "pareizi": 0,
         "padoms": "Reizināšana pirms saskaitīšanas."},
        {"jaut": "Cik soļu jāraksta vienā rindā?",
         "opcijas": ["Viens", "Divi", "Visi", "Cik sanāk"],
         "pareizi": 0,
         "padoms": "Lai kļūdu varētu atrast."},
        {"jaut": "Izteiksmē (−12) : (−3) · 2 darbības veic...",
         "opcijas": ["no kreisās uz labo", "vispirms reizināšanu",
                     "vispirms dalīšanu vienmēr", "jebkurā secībā"],
         "pareizi": 0,
         "padoms": "Vienādas prioritātes darbības."},
    ], pamats=4),

    Pasaule("Kā aprēķināt gala summu?",
            Ievadi("", [
                {"jaut": "3 preces pa 12 € un atlaide 10 €. Cik eiro jāmaksā?",
                 "atb": ["26"], "padoms": "36 − 10."},
                {"jaut": "Piegāde 5 € un atlaide vēl 8 €. Cik eiro jāmaksā "
                         "kopā?",
                 "atb": ["23"], "padoms": "26 + 5 − 8."},
                {"jaut": "Ja preču būtu 5, nevis 3, cik eiro būtu pirmais "
                         "solis?",
                 "atb": ["60"], "padoms": "5 · 12."},
                {"jaut": "Cik eiro tad būtu gala summa ar to pašu atlaidi un "
                         "piegādi?",
                 "atb": ["47"], "padoms": "60 − 10 + 5 − 8."},
            ]),
            pavediens="veikals",
            konteksts="Pirkuma summa ir gara izteiksme, kurā katrs solis ir "
                      "viena čeka rinda.",
            kapec="Plāns pasaka, kurā secībā rindas jāsaskaita."),

    Kopsavilkums([
        "Plānoju garu aprēķinu pirms rēķināšanas.",
        "Nosaku darbību secību un izvēlos vienotu pierakstu.",
        "Rakstu vienu soli vienā rindā.",
        "Pārbaudu rezultātu ar novērtējumu.",
    ]),

    Majas([
        "Izrēķini (−5 + 2) · 4 − (−6).",
        "Pieraksti katru soli jaunā rindā.",
        "Pieraksti plānu vārdiem pirms rēķina.",
    ]),
]
