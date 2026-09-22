# -*- coding: utf-8 -*-
"""5. klase, 56. stunda: «Ko nozīmē saīsināt daļu?»

Paplašināšanas pretstats. Rēķins te ir tas pats, tikai uz otru pusi, bet
jautājums ir jauns: kad apstāties. Tāpēc stundas centrā nav dalīšana, bet
pārbaude - vai palikušajiem skaitļiem vēl ir kopīgs dalītājs.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums, dala)

TEMA = "Ko nozīmē saīsināt daļu?"

MERKIS = ("Iemācīsimies saīsināt daļu un pārbaudīt, vai iegūta nesaīsināma "
          "daļa.")

SATURS = [
    Sakums("Astoņas divpadsmitdaļas - vai citādi nevar?",
           zimejums=dala(12, 8, "8/12"),
           paraksts="Tie paši divi trešdaļu gabali, tikai smalkāk sagriezti.",
           fakti=["Lielos skaitļos daļas vērtību ir grūti saskatīt.",
                  "Ja gabalus saliek atpakaļ, skaitļi kļūst mazāki.",
                  "Daudzums no tā nemainās."]),

    Doma("Saīsināt nozīmē dalīt abus locekļus",
         "Daļu saīsina, dalot skaitītāju un saucēju ar vienu un to pašu "
         "skaitli; daļas vērtība nemainās, tikai skaitļi kļūst mazāki.",
         soli=[
             "Atrodi skaitītāja un saucēja kopīgo dalītāju.",
             "Izdali ar to abus locekļus.",
             "Pārbaudi, vai jaunajiem skaitļiem vēl ir kopīgs dalītājs.",
             "Ja ir - saīsini vēlreiz.",
             "Ja nav - daļa ir nesaīsināma, un darbs ir galā.",
         ],
         pieze="Nesaīsināma daļa ir tāda, kuras skaitītājam un saucējam "
               "vienīgais kopīgais dalītājs ir 1. Tāda ir {2|3}, bet nav "
               "{4|6} - to vēl var saīsināt ar 2."),

    Paraugs("Saīsini {8|12}",
            uzd="Saīsini daļu {8|12} līdz nesaīsināmai.",
            soli=[
                ("8 un 12 abi dalās ar 4",
                 "Meklē kopīgo dalītāju."),
                ("8 : 4 = 2 un 12 : 4 = 3",
                 "Dala abus locekļus ar vienu skaitli."),
                ("{8|12} = {2|3}",
                 "Jaunais pieraksts."),
                ("2 un 3 kopīgu dalītāju nav",
                 "Tātad {2|3} ir nesaīsināma - tālāk nevar."),
            ],
            atbilde="{8|12} = {2|3}"),

    Slidnis("Ceļš atpakaļ pie mazākajiem skaitļiem",
            [{"v": "{12|18}", "teksts": "sākuma daļa", "josla": 67,
              "zim": dala(18, 12)},
             {"v": "{6|9}", "teksts": "abus dala ar 2", "josla": 67,
              "zim": dala(9, 6)},
             {"v": "{4|6}", "teksts": "cits ceļš: sākuma daļu dala ar 3",
              "josla": 67, "zim": dala(6, 4)},
             {"v": "{2|3}", "teksts": "nesaīsināma daļa", "josla": 67,
              "zim": dala(3, 2)}],
            ievads="Spied soli pa solim: skaitļi sarūk, josla paliek tā "
                   "pati."),

    Ievadi("Saīsini līdz galam", [
        {"jaut": "Saīsini {4|8}. Atbildi raksti kā a/b.",
         "atb": ["1/2"], "padoms": "Abus dala ar 4."},
        {"jaut": "Saīsini {6|9}. Atbildi raksti kā a/b.",
         "atb": ["2/3"], "padoms": "Abus dala ar 3."},
        {"jaut": "Saīsini {10|15}. Atbildi raksti kā a/b.",
         "atb": ["2/3"], "padoms": "Abus dala ar 5."},
        {"jaut": "Saīsini {9|12}. Atbildi raksti kā a/b.",
         "atb": ["3/4"], "padoms": "Abus dala ar 3."},
        {"jaut": "Saīsini {14|21}. Atbildi raksti kā a/b.",
         "atb": ["2/3"], "padoms": "Abus dala ar 7."},
        {"jaut": "Saīsini {16|24}. Atbildi raksti kā a/b.",
         "atb": ["2/3"], "padoms": "Abus dala ar 8."},
        {"jaut": "Saīsini {15|25}. Atbildi raksti kā a/b.",
         "atb": ["3/5"], "padoms": "Abus dala ar 5."},
        {"jaut": "Saīsini {18|24}. Atbildi raksti kā a/b.",
         "atb": ["3/4"], "padoms": "Abus dala ar 6."},
    ], pamats=4,
        ievads="Saīsini tik ilgi, kamēr kopīga dalītāja vairs nav."),

    Zimejums("Divas trešdaļas",
             dala(3, 2, "2/3"),
             paskaidro="Tas pats daudzums, kas {8|12}, bet tagad to var "
                       "pateikt ar diviem maziem skaitļiem.",
             ievads="Saīsinātā daļa ir tā pati daļa, tikai īsāk pierakstīta."),

    Varianti("Vai daļa ir nesaīsināma?", [
        {"jaut": "Kura daļa ir nesaīsināma?",
         "opcijas": ["{5|7}", "{5|10}", "{6|8}", "{9|12}"],
         "pareizi": 0,
         "padoms": "Meklē kopīgu dalītāju."},
        {"jaut": "Kad daļa ir nesaīsināma?",
         "opcijas": ["Kad vienīgais kopīgais dalītājs ir 1",
                     "Kad skaitītājs ir 1",
                     "Kad saucējs ir pirmskaitlis",
                     "Kad skaitļi ir mazi"],
         "pareizi": 0,
         "padoms": "Kopīga dalītāja vairs nav."},
        {"jaut": "{12|18} saīsināja kā {6|9}. Vai darbs ir galā?",
         "opcijas": ["Nav, 6 un 9 vēl dalās ar 3", "Ir, skaitļi kļuva mazāki",
                     "Nav, jāsaīsina ar 6", "Ir, 6 un 9 ir pirmskaitļi"],
         "pareizi": 0,
         "padoms": "Vienmēr pārbauda, vai var vēl."},
        {"jaut": "Kas notiek ar daļas vērtību, to saīsinot?",
         "opcijas": ["Nekas", "Tā kļūst mazāka", "Tā kļūst lielāka",
                     "Tā kļūst par veselu skaitli"],
         "pareizi": 0,
         "padoms": "Tas ir tas pats daudzums."},
        {"jaut": "Ar kuru skaitli {24|36} var saīsināt uzreiz līdz galam?",
         "opcijas": ["Ar 12", "Ar 2", "Ar 3", "Ar 6"],
         "pareizi": 0,
         "padoms": "Lielākais kopīgais dalītājs."},
        {"jaut": "Kāda daļa iznāk, saīsinot {7|7}?",
         "opcijas": ["1", "{1|7}", "{7|1}", "0"],
         "pareizi": 0,
         "padoms": "Septiņas septītdaļas ir vesels."},
    ], pamats=4),

    Pasaule("Cik vienkārši var pateikt atlaidi?",
            Ievadi("", [
                {"jaut": "Prece maksāja 100 €, atlaide 25 €. Kāda daļa tā "
                         "ir? Atbildi raksti kā a/b.",
                 "atb": ["1/4"], "padoms": "{25|100}, abus dala ar 25."},
                {"jaut": "Prece maksāja 100 €, atlaide 50 €. Kāda daļa tā "
                         "ir? Atbildi raksti kā a/b.",
                 "atb": ["1/2"], "padoms": "{50|100}, abus dala ar 50."},
                {"jaut": "Prece maksāja 60 €, atlaide 15 €. Kāda daļa tā ir? "
                         "Atbildi raksti kā a/b.",
                 "atb": ["1/4"], "padoms": "{15|60}, abus dala ar 15."},
                {"jaut": "Prece maksāja 80 €, atlaide 20 €. Kāda daļa tā ir? "
                         "Atbildi raksti kā a/b.",
                 "atb": ["1/4"], "padoms": "{20|80}, abus dala ar 20."},
            ]),
            pavediens="veikals",
            konteksts="Čekā stāv eiro, bet prātā vieglāk turēt ceturtdaļu "
                      "nekā pierakstu {15|60}.",
            kapec="Saīsināta daļa uzreiz pasaka, cik liela atlaide ir."),

    Kopsavilkums([
        "Zinu, ka saīsināt nozīmē dalīt abus daļas locekļus.",
        "Atrodu skaitītāja un saucēja kopīgo dalītāju.",
        "Saīsinu daļu līdz nesaīsināmai.",
        "Pārbaudu, vai kopīgs dalītājs tiešām vairs nav atrodams.",
    ]),

    Majas([
        "Saīsini līdz galam {20|30}, {18|27} un {21|28}.",
        "Uzraksti trīs nesaīsināmas daļas ar saucēju, lielāku par 10.",
        "Atrodi čekā divus skaitļus un pieraksti to daļu saīsinātā veidā.",
    ]),
]
