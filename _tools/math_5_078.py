# -*- coding: utf-8 -*-
"""5. klase, 78. stunda: «Ko stāsta produkta sastāvs?»

Jauns mikrotemats un apgriezts jautājums: līdz šim daļa bija dota, tagad tā
jāizveido pašam no diviem skaitļiem. Uz iepakojuma abi skaitļi jau ir
uzdrukāti - kopējā masa un viena sastāvdaļa -, tāpēc stunda sākas nevis ar
formulu, bet ar etiķetes lasīšanu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala)

TEMA = "Ko stāsta produkta sastāvs?"

MERKIS = ("Mācīsimies lasīt tekstu ar masas datiem un izteikt vienu "
          "sastāvdaļu kā daļu no visa produkta.")

SATURS = [
    Sakums("Uz iepakojuma ir divi skaitļi",
           zimejums=dala(5, 1, "1/5 cukura"),
           paraksts="500 g jogurta, no tiem 100 g cukura - tā ir {1|5} no "
                    "visas masas.",
           fakti=["Uz etiķetes ir kopējā masa un katras sastāvdaļas masa.",
                  "No diviem skaitļiem var izveidot daļu.",
                  "Skaitītājā - sastāvdaļa, saucējā - viss produkts."]),

    Doma("Daļu veido no diviem skaitļiem",
         "Lai pateiktu, kāda daļa no produkta ir viena sastāvdaļa, tās masu "
         "raksta skaitītājā, bet visa produkta masu - saucējā.",
         soli=[
             "Atrodi tekstā visa produkta masu - tas ir veselais.",
             "Atrodi sastāvdaļas masu - tas ir gabals.",
             "Uzraksti daļu: gabals pār veselo.",
             "Saīsini daļu līdz nesaīsināmai.",
             "Pieraksti secinājumu vārdiem.",
         ],
         pieze="Abām masām jābūt vienās mērvienībās. Ja produkts ir 1 kg, "
               "bet cukurs 200 g, vispirms kilogramu pārraksta kā 1000 g - "
               "citādi daļa iznāk pavisam cita."),

    Paraugs("Cik liela daļa ir cukurs?",
            uzd="Jogurta paciņā ir 500 g, no tiem 100 g cukura. Kāda daļa no "
                "produkta ir cukurs?",
            soli=[
                ("Veselais ir 500 g",
                 "Visa paciņas masa."),
                ("Gabals ir 100 g",
                 "Cukura masa."),
                ("{100|500}",
                 "Gabals pār veselo."),
                ("{100 : 100|500 : 100} = {1|5}",
                 "Saīsina abus locekļus."),
                ("Cukurs ir {1|5} no produkta",
                 "Secinājums vārdiem."),
            ],
            atbilde="Cukurs ir {1|5} jogurta masas"),

    Ievadi("Izsaki sastāvdaļu kā daļu", [
        {"jaut": "500 g produkta, 100 g cukura. Kāda daļa ir cukurs? Atbildi "
                 "raksti kā a/b.",
         "atb": ["1/5"], "padoms": "{100|500}, abus dala ar 100."},
        {"jaut": "400 g produkta, 100 g tauku. Kāda daļa ir tauki? Atbildi "
                 "raksti kā a/b.",
         "atb": ["1/4"], "padoms": "{100|400}."},
        {"jaut": "250 g produkta, 50 g olbaltumvielu. Kāda daļa? Atbildi "
                 "raksti kā a/b.",
         "atb": ["1/5"], "padoms": "{50|250}, abus dala ar 50."},
        {"jaut": "600 g produkta, 150 g ogu. Kāda daļa ir ogas? Atbildi "
                 "raksti kā a/b.",
         "atb": ["1/4"], "padoms": "{150|600}, abus dala ar 150."},
        {"jaut": "1 kg produkta, 200 g cukura. Kāda daļa ir cukurs? Atbildi "
                 "raksti kā a/b.",
         "atb": ["1/5"], "padoms": "1 kg = 1000 g; {200|1000}."},
        {"jaut": "800 g produkta, 300 g ūdens. Kāda daļa ir ūdens? Atbildi "
                 "raksti kā a/b.",
         "atb": ["3/8"], "padoms": "{300|800}, abus dala ar 100."},
        {"jaut": "900 g produkta, 600 g miltu. Kāda daļa ir milti? Atbildi "
                 "raksti kā a/b.",
         "atb": ["2/3"], "padoms": "{600|900}, abus dala ar 300."},
        {"jaut": "200 g produkta, 25 g sāls. Kāda daļa ir sāls? Atbildi "
                 "raksti kā a/b.",
         "atb": ["1/8"], "padoms": "{25|200}, abus dala ar 25."},
    ], pamats=4,
        ievads="Skaitītājā - sastāvdaļa, saucējā - viss produkts, tad "
               "saīsina."),

    Zimejums("Viena piektdaļa no paciņas",
             dala(5, 1, "1/5"),
             paskaidro="Visa josla ir 500 g. Viens gabals ir 100 g - tieši "
                       "tik daudz paciņā ir cukura.",
             ievads="Sastāvdaļu daļu var uzzīmēt tāpat kā jebkuru citu."),

    Varianti("Ko var uzzināt no etiķetes?", [
        {"jaut": "Kurš skaitlis ir saucējā?",
         "opcijas": ["Visa produkta masa", "Sastāvdaļas masa",
                     "Lielākais skaitlis tekstā", "Cena"],
         "pareizi": 0,
         "padoms": "Saucējs ir veselais."},
        {"jaut": "Produkts ir 1 kg, cukurs 250 g. Ko dara vispirms?",
         "opcijas": ["Pārraksta kilogramu gramos", "Saīsina daļu",
                     "Saskaita abus skaitļus", "Dala ar 4"],
         "pareizi": 0,
         "padoms": "Vienas mērvienības."},
        {"jaut": "{200|800} saīsinātā veidā ir...",
         "opcijas": ["{1|4}", "{2|8}", "{1|2}", "{4|1}"],
         "pareizi": 0,
         "padoms": "Abus dala ar 200."},
        {"jaut": "Vai sastāvdaļas daļa var būt lielāka par 1?",
         "opcijas": ["Nē, tā ir daļa no produkta", "Jā, ja ir daudz cukura",
                     "Jā, vienmēr", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Gabals nav lielāks par veselo."},
        {"jaut": "Ko nozīmē, ka ūdens ir {3|4} produkta?",
         "opcijas": ["Trīs ceturtdaļas masas ir ūdens",
                     "Produktā ir 3 g ūdens",
                     "Ūdens ir 4 reizes vairāk",
                     "Produkts sver 4 g"],
         "pareizi": 0,
         "padoms": "Daļa no visas masas."},
        {"jaut": "Divi produkti: pirmajā cukurs ir {1|5}, otrajā {1|4}. Kurā "
                 "cukura ir vairāk pēc daļas?",
         "opcijas": ["Otrajā", "Pirmajā", "Vienādi", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "{1|4} > {1|5}."},
    ], pamats=4),

    Pasaule("Ko nopirkt veikalā?",
            Ievadi("", [
                {"jaut": "Paciņā 400 g, cukura 50 g. Kāda daļa ir cukurs? "
                         "Atbildi raksti kā a/b.",
                 "atb": ["1/8"], "padoms": "{50|400}."},
                {"jaut": "Citā paciņā 400 g, cukura 100 g. Kāda daļa? "
                         "Atbildi raksti kā a/b.",
                 "atb": ["1/4"], "padoms": "{100|400}."},
                {"jaut": "Kurā paciņā cukura ir mazāk? Ieraksti daļu kā a/b.",
                 "atb": ["1/8"], "padoms": "{1|8} < {1|4}."},
                {"jaut": "Trešajā paciņā 300 g, cukura 60 g. Kāda daļa? "
                         "Atbildi raksti kā a/b.",
                 "atb": ["1/5"], "padoms": "{60|300}."},
            ]),
            pavediens="veikals",
            konteksts="Uz plaukta blakus stāv paciņas ar dažādu masu, tāpēc "
                       "gramus vien salīdzināt ir maldinoši.",
            kapec="Daļa pasaka, cik cukura ir katrā paciņas gramā."),

    Kopsavilkums([
        "Atrodu tekstā veselo un sastāvdaļas masu.",
        "Uzrakstu sastāvdaļu kā daļu no visa produkta.",
        "Pārrakstu masas vienās mērvienībās, pirms veidoju daļu.",
        "Saīsinu iegūto daļu un pierakstu secinājumu vārdiem.",
    ]),

    Majas([
        "Atrodi mājās produktu un izsaki vienu sastāvdaļu kā daļu no masas.",
        "Salīdzini divu produktu cukura daļas.",
        "Uzraksti, kāpēc masām jābūt vienās mērvienībās.",
    ]),
]
