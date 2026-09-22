# -*- coding: utf-8 -*-
"""6. klase, 19. stunda: «Kā daļu sadalīt vienādās daļās?»

Otrā darbība - dalīšana ar veselu skaitli. To var saprast divējādi: vai nu
katru daļu sasmalcina, vai skaitītāju izdala. Stunda sāk ar sasmalcināšanu,
jo tā ir redzama, un tikai tad nonāk pie īsā pieraksta.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, dala)

TEMA = "Kā daļu sadalīt vienādās daļās?"

MERKIS = ("Iemācīsimies dalīt daļu ar veselu skaitli, spriežot un lietojot "
          "daļas pamatīpašību.")

SATURS = [
    Sakums("Vienu zāļu devu sadala trīs reizēm",
           zimejums=dala(12, 4, "4/12"),
           paraksts="{4|12} ir tas pats, kas {1|3}. Ja to izdzer trijās "
                    "reizēs, katrā reizē ir {1|9}.",
           fakti=["Aptiekā deva reti sakrīt ar visu iepakojumu.",
                  "Dalot daļu, gabali kļūst mazāki - saucējs aug."]),

    Doma("Dalot daļu, aug saucējs",
         "Daļu dalot ar veselu skaitli, ar to reizina saucēju: gabalu skaits "
         "paliek, bet katrs gabals kļūst attiecīgi mazāks.",
         soli=[
             "Pieraksti daļu un veselo skaitli, ar kuru dala.",
             "Ja skaitītājs dalās ar to skaitli, izdali skaitītāju.",
             "Ja nedalās, reizini saucēju ar to skaitli.",
             "Saīsini rezultātu, ja var.",
             "Pārbaudi ar reizināšanu: rezultāts reiz dalītājs dod sākotnējo "
             "daļu.",
         ],
         pieze="{2|3} : 2 var izrēķināt abos veidos: {2 : 2|3} = {1|3} vai "
               "{2|3 · 2} = {2|6} = {1|3}. Rezultāts ir viens, tikai pirmais "
               "ceļš ir īsāks."),

    Slidnis("Jo vairāk daļu, jo mazāks gabals",
            [{"v": "{1|2} : 1", "teksts": "paliek {1|2}",
              "josla": 50, "zim": dala(2, 1)},
             {"v": "{1|2} : 2", "teksts": "sanāk {1|4}",
              "josla": 25, "zim": dala(4, 1)},
             {"v": "{1|2} : 3", "teksts": "sanāk {1|6}",
              "josla": 17, "zim": dala(6, 1)},
             {"v": "{1|2} : 4", "teksts": "sanāk {1|8}",
              "josla": 12, "zim": dala(8, 1)}],
            ievads="Spied soli pa solim: puse, sadalīta arvien sīkāk. "
                   "Iekrāsotā daļa sarūk tieši tikpat reižu, cik liels ir "
                   "dalītājs."),

    Paraugs("Sadali {3|4} trijās daļās",
            uzd="Trīs ceturtdaļas litra jāsadala trīs vienādās glāzēs. Cik "
                "ir katrā glāzē?",
            soli=[
                ("{3|4} : 3",
                 "Dalīšana ar veselu skaitli."),
                ("Skaitītājs 3 dalās ar 3",
                 "Tāpēc īsākais ceļš ir dalīt skaitītāju."),
                ("{3 : 3|4} = {1|4}",
                 "Saucējs paliek nemainīgs."),
                ("Pārbaude: {1|4} · 3 = {3|4}",
                 "Reizināšana atgriež sākotnējo daļu."),
            ],
            atbilde="{1|4} l katrā glāzē"),

    Ievadi("Izdali daļu", [
        {"jaut": "Cik ir {4|5} : 2? Atbildi raksti kā a/b.",
         "atb": ["2/5"], "padoms": "Skaitītājs dalās: 4 : 2."},
        {"jaut": "Cik ir {1|3} : 2? Atbildi raksti kā a/b.",
         "atb": ["1/6"], "padoms": "Skaitītājs nedalās - reizini saucēju."},
        {"jaut": "Cik ir {6|7} : 3? Atbildi raksti kā a/b.",
         "atb": ["2/7"], "padoms": "6 : 3 = 2."},
        {"jaut": "Cik ir {2|3} : 4? Atbildi raksti kā a/b.",
         "atb": ["1/6", "2/12"], "padoms": "{2|12} un tad saīsina."},
        {"jaut": "Cik ir {5|8} : 5? Atbildi raksti kā a/b.",
         "atb": ["1/8"], "padoms": "5 : 5 = 1."},
        {"jaut": "Cik ir {3|4} : 6? Atbildi raksti kā a/b.",
         "atb": ["1/8", "3/24"], "padoms": "{3|24} saīsināts ar 3."},
    ], pamats=4,
        ievads="Vispirms paskaties, vai skaitītājs dalās - tas ir īsākais "
               "ceļš."),

    Varianti("Kurš ceļš ir īsāks?", [
        {"jaut": "{6|7} : 2. Kā rēķināt ātrāk?",
         "opcijas": ["Dalīt skaitītāju", "Reizināt saucēju",
                     "Dalīt abus", "Reizināt abus"],
         "pareizi": 0,
         "padoms": "6 dalās ar 2 bez atlikuma."},
        {"jaut": "{5|6} : 4. Kā rēķināt?",
         "opcijas": ["Reizināt saucēju: {5|24}", "Dalīt skaitītāju",
                     "Atņemt 4", "{5|2}"],
         "pareizi": 0,
         "padoms": "5 ar 4 nedalās."},
        {"jaut": "Kas notiek ar daļas vērtību, dalot to ar 3?",
         "opcijas": ["Tā kļūst trīs reizes mazāka",
                     "Tā kļūst trīs reizes lielāka",
                     "Tā nemainās", "Tā kļūst par veselu skaitli"],
         "pareizi": 0,
         "padoms": "Dalīšana vienmēr samazina pozitīvu skaitli."},
        {"jaut": "{2|3} : 2 = {1|3}. Kā to pārbaudīt?",
         "opcijas": ["{1|3} · 2 = {2|3}", "{1|3} : 2",
                     "{2|3} + {1|3}", "Pārbaudīt nevar"],
         "pareizi": 0,
         "padoms": "Dalījumu pārbauda ar reizināšanu."},
    ], pamats=4),

    Pasaule("Cik saņem katrs?",
            Ievadi("", [
                {"jaut": "{3|4} l sulas sadala 3 glāzēs. Cik litru ir vienā? "
                         "Atbildi raksti kā a/b.",
                 "atb": ["1/4"], "padoms": "3 : 3 = 1."},
                {"jaut": "{1|2} kg riekstu sadala 4 maisiņos. Cik kg ir "
                         "vienā? Atbildi raksti kā a/b.",
                 "atb": ["1/8"], "padoms": "Saucēju reizina ar 4."},
                {"jaut": "{4|5} tortes sadala 8 gabalos. Cik tortes ir vienā "
                         "gabalā? Atbildi raksti kā a/b.",
                 "atb": ["1/10", "4/40"], "padoms": "{4|40} saīsināts."},
                {"jaut": "{6|7} m lentes sadala 3 daļās. Cik metru ir vienā? "
                         "Atbildi raksti kā a/b.",
                 "atb": ["2/7"], "padoms": "6 : 3 = 2."},
            ]),
            pavediens="virtuve",
            konteksts="Sadalīt vienādi nozīmē dalīt arī to, kas pats jau ir "
                      "daļa.",
            kapec="Dalot daļu, gabali kļūst mazāki, tāpēc saucējs aug."),

    Kopsavilkums([
        "Dalu daļu ar veselu skaitli abos veidos.",
        "Izvēlos īsāko ceļu: skatos, vai skaitītājs dalās.",
        "Saīsinu rezultātu, ja tas ir iespējams.",
        "Pārbaudu dalījumu ar reizināšanu.",
    ]),

    Majas([
        "Sadali {4|5} litra trīs vienādās glāzēs un pieraksti rezultātu.",
        "Atrodi divus dalījumus, kuru rezultāts ir {1|6}.",
        "Paskaidro kādam mājās, kāpēc, dalot daļu, saucējs kļūst lielāks.",
    ]),
]
