# -*- coding: utf-8 -*-
"""5. klase, 74. stunda: «Kā pierakstīt aprēķinu?»

Rēķins ir tas pats, kas iepriekšējā stundā, bet te to raksta divējādi: pa
darbībām un ar vienu izteiksmi. Otrais pieraksts ir arī pirmā tikšanās ar
darbību secību reālā uzdevumā - dalīšana un reizināšana ir vienāda ranga,
tāpēc izteiksmi 240 : 4 · 3 rēķina no kreisās uz labo.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala, restis)

TEMA = "Kā pierakstīt aprēķinu?"

MERKIS = ("Mācīsimies aprēķināt daļas skaitlisko vērtību, pierakstot to pa "
          "darbībām un ar vienu izteiksmi.")

SATURS = [
    Sakums("Divi pieraksti, viena atbilde",
           zimejums=dala(4, 3, "3/4 no 240 km"),
           paraksts="Pa darbībām: 240 : 4 = 60, tad 60 · 3 = 180. Ar "
                    "izteiksmi: 240 : 4 · 3 = 180.",
           fakti=["Pa darbībām - katrs solis savā rindā.",
                  "Ar izteiksmi - viss vienā rindā.",
                  "Atbilde abos gadījumos ir viena."]),

    Doma("Viens rēķins, divi pieraksti",
         "Daļas vērtību pieraksta vai nu pa darbībām, numurējot soļus, vai "
         "ar vienu izteiksmi, kurā darbības izpilda pēc kārtas.",
         soli=[
             "Pa darbībām: 1) veselo dala ar saucēju; 2) reizina ar "
             "skaitītāju.",
             "Katram solim pieraksti, ko tas nozīmē.",
             "Ar izteiksmi: veselais : saucējs · skaitītājs.",
             "Dalīšanu un reizināšanu izpilda no kreisās uz labo.",
             "Atbildi raksti ar mērvienību.",
         ],
         pieze="Izteiksmē iekavas nav vajadzīgas: dalīšana un reizināšana ir "
               "vienāda ranga darbības, tāpēc 240 : 4 · 3 nozīmē tieši to "
               "pašu, ko divi soļi pēc kārtas."),

    Paraugs("Cik ir {3|4} no 240 km?",
            uzd="Pieraksti aprēķinu abos veidos.",
            soli=[
                ("1) 240 : 4 = 60 (km)",
                 "Viena ceturtdaļa ceļa."),
                ("2) 60 · 3 = 180 (km)",
                 "Trīs ceturtdaļas."),
                ("Ar izteiksmi: 240 : 4 · 3 = 180",
                 "Tie paši soļi vienā rindā."),
                ("Atbilde: 180 km",
                 "Vērtība vienmēr ar mērvienību."),
            ],
            atbilde="180 km"),

    Ievadi("Aprēķini pēc izteiksmes", [
        {"jaut": "Cik ir 240 : 4 · 3?",
         "atb": ["180"], "padoms": "Vispirms dalīšana."},
        {"jaut": "Cik ir 120 : 3 · 2?",
         "atb": ["80"], "padoms": "120 : 3 = 40."},
        {"jaut": "Cik ir 350 : 5 · 4?",
         "atb": ["280"], "padoms": "350 : 5 = 70."},
        {"jaut": "Cik ir {2|3} no 90 km? Atbildi kilometros.",
         "atb": ["60"], "padoms": "90 : 3 · 2."},
        {"jaut": "Cik ir {3|5} no 200 km? Atbildi kilometros.",
         "atb": ["120"], "padoms": "200 : 5 · 3."},
        {"jaut": "Cik ir {5|6} no 180 km? Atbildi kilometros.",
         "atb": ["150"], "padoms": "180 : 6 · 5."},
        {"jaut": "Cik ir {3|8} no 400 kg? Atbildi kilogramos.",
         "atb": ["150"], "padoms": "400 : 8 · 3."},
        {"jaut": "Cik ir {4|9} no 270 minūtēm? Atbildi minūtēs.",
         "atb": ["120"], "padoms": "270 : 9 · 4."},
    ], pamats=4,
        ievads="Izteiksmē darbības izpilda no kreisās uz labo."),

    Zimejums("Trīs skaitļi, kas parādās aprēķinā",
             restis([["240", "60", "180"]],
                    virsraksts="Veselais, viena daļa, trīs daļas"),
             paskaidro="Pirmais skaitlis ir dotais, otrais rodas dalot, "
                       "trešais - reizinot. Abos pieraksta veidos tie ir "
                       "tie paši un tajā pašā secībā.",
             ievads="Pieraksta veidu izvēlas pats, atbilde ir viena."),

    Varianti("Kurš pieraksts ir pareizs?", [
        {"jaut": "Kura izteiksme atbilst uzdevumam «{3|4} no 240»?",
         "opcijas": ["240 : 4 · 3", "240 · 4 : 3", "240 : 3 · 4",
                     "240 · 3 · 4"],
         "pareizi": 0,
         "padoms": "Vispirms dala ar saucēju."},
        {"jaut": "Kādā secībā izpilda 120 : 3 · 2?",
         "opcijas": ["No kreisās uz labo", "Vispirms reizināšanu",
                     "Vispirms lielāko skaitli", "Secība nav svarīga"],
         "pareizi": 0,
         "padoms": "Vienāda ranga darbības."},
        {"jaut": "Vai izteiksmē 240 : 4 · 3 vajadzīgas iekavas?",
         "opcijas": ["Nav, darbības ir vienāda ranga",
                     "Vajadzīgas ap 4 · 3",
                     "Vajadzīgas ap 240 : 4",
                     "Vienmēr vajadzīgas"],
         "pareizi": 0,
         "padoms": "Secība jau ir noteikta."},
        {"jaut": "Cik ir 240 : (4 · 3)?",
         "opcijas": ["20", "180", "60", "720"],
         "pareizi": 0,
         "padoms": "Iekavas maina rezultātu: 240 : 12."},
        {"jaut": "Kas jāpieraksta pie katra soļa?",
         "opcijas": ["Ko tas nozīmē un mērvienība",
                     "Tikai skaitlis",
                     "Tikai darbība",
                     "Neko nevajag"],
         "pareizi": 0,
         "padoms": "Citādi solis neko neizskaidro."},
        {"jaut": "Kura izteiksme dod {2|5} no 300?",
         "opcijas": ["300 : 5 · 2", "300 · 5 : 2", "300 : 2 · 5",
                     "300 - 5 · 2"],
         "pareizi": 0,
         "padoms": "Saucējs ir 5."},
    ], pamats=4),

    Pasaule("Cik degvielas paliks?",
            Ievadi("", [
                {"jaut": "Tvertnē ir 60 l degvielas, izlietotas {2|3}. Cik "
                         "litru izlietots?",
                 "atb": ["40"], "padoms": "60 : 3 · 2."},
                {"jaut": "Cik litru degvielas palicis?",
                 "atb": ["20"], "padoms": "60 - 40."},
                {"jaut": "Ceļš ir 450 km, nobraukta {3|5}. Cik kilometru "
                         "nobraukts?",
                 "atb": ["270"], "padoms": "450 : 5 · 3."},
                {"jaut": "Cik kilometru vēl jābrauc?",
                 "atb": ["180"], "padoms": "450 - 270."},
            ]),
            pavediens="celojums",
            konteksts="Ceļā vienmēr ir divi skaitļi: cik jau izlietots un "
                      "cik palicis.",
            kapec="Pierakstītu aprēķinu var pārbaudīt arī tas, kas sēž "
                  "blakus."),

    Kopsavilkums([
        "Pierakstu daļas vērtības aprēķinu pa darbībām.",
        "Pierakstu to pašu aprēķinu ar vienu izteiksmi.",
        "Zinu, ka dalīšanu un reizināšanu izpilda no kreisās uz labo.",
        "Pie katra soļa pierakstu, ko tas nozīmē.",
    ]),

    Majas([
        "Aprēķini {5|8} no 320 abos pieraksta veidos.",
        "Uzraksti izteiksmi uzdevumam «{2|7} no 350 kg».",
        "Padomā, kad iekavas izteiksmē tomēr ir vajadzīgas.",
    ]),
]
