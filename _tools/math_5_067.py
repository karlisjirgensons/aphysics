# -*- coding: utf-8 -*-
"""5. klase, 67. stunda: «Kā atņemt daļas?»

Atņemšana ir tā pati saskaitīšana ar vienu zīmi citādu, tāpēc šai stundai
nav jauna paņēmiena. Jauna ir tikai viena lieta: rezultāts biežāk iznāk
saīsināms, un tieši tur skolēns apstājas par agru. Tāpēc katrā uzdevumā te
ir pēdējais solis - pārbaudīt, vai atbildi var uzrakstīt īsāk.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala)

TEMA = "Kā atņemt daļas?"

MERKIS = ("Iemācīsimies atņemt daļas ar dažādiem saucējiem un saīsināt "
          "rezultātu.")

SATURS = [
    Sakums("Cik palika pāri?",
           zimejums=dala(6, 1, "1/6"),
           paraksts="{1|2} - {1|3} = {1|6} - paliek viens sestdaļas gabals.",
           fakti=["No puses atņem trešdaļu - cik paliek?",
                  "Atbildi ar aci nepateiksi.",
                  "Bet ar kopsaucēju tā ir vienkārša atņemšana."]),

    Doma("Atņem tāpat kā saskaita",
         "Daļas ar dažādiem saucējiem atņem, pārrakstot tās ar kopsaucēju un "
         "atņemot skaitītājus; saucējs paliek tas pats.",
         soli=[
             "Atrodi abu daļu kopsaucēju.",
             "Paplašini abas daļas līdz šim saucējam.",
             "Atņem skaitītājus, saucēju atstāj neskartu.",
             "Pārbaudi, vai rezultāts ir saīsināms.",
             "Ja ir - saīsini un raksti atbildi.",
         ],
         pieze="Starpība vienmēr ir mazāka par pirmo daļu. Ja iznāk lielāka, "
               "kaut kur samainītas vietām daļas vai skaitītāji."),

    Paraugs("{3|4} - {1|6}",
            uzd="Izrēķini {3|4} - {1|6} un saīsini rezultātu, ja vajag.",
            soli=[
                ("Kopsaucējs ir 12",
                 "12 dalās ar 4 un 6."),
                ("{3|4} = {9|12}",
                 "Abus locekļus reizina ar 3."),
                ("{1|6} = {2|12}",
                 "Abus locekļus reizina ar 2."),
                ("{9|12} - {2|12} = {7|12}",
                 "Atņem skaitītājus."),
                ("7 un 12 kopīga dalītāja nav",
                 "{7|12} jau ir nesaīsināma."),
            ],
            atbilde="{3|4} - {1|6} = {7|12}"),

    Ievadi("Atņem un saīsini", [
        {"jaut": "Cik ir {1|2} - {1|3}? Atbildi raksti kā a/b.",
         "atb": ["1/6"], "padoms": "{3|6} - {2|6}."},
        {"jaut": "Cik ir {3|4} - {1|2}? Atbildi raksti kā a/b.",
         "atb": ["1/4"], "padoms": "{3|4} - {2|4}."},
        {"jaut": "Cik ir {5|6} - {1|3}? Atbildi raksti kā a/b.",
         "atb": ["1/2", "3/6"], "padoms": "{5|6} - {2|6} = {3|6}."},
        {"jaut": "Cik ir {7|8} - {1|4}? Atbildi raksti kā a/b.",
         "atb": ["5/8"], "padoms": "{7|8} - {2|8}."},
        {"jaut": "Cik ir {2|3} - {1|6}? Atbildi raksti kā a/b.",
         "atb": ["1/2", "3/6"], "padoms": "{4|6} - {1|6} = {3|6}."},
        {"jaut": "Cik ir {4|5} - {3|10}? Atbildi raksti kā a/b.",
         "atb": ["1/2", "5/10"], "padoms": "{8|10} - {3|10} = {5|10}."},
        {"jaut": "Cik ir {5|8} - {1|2}? Atbildi raksti kā a/b.",
         "atb": ["1/8"], "padoms": "{5|8} - {4|8}."},
        {"jaut": "Cik ir {3|4} - {2|3}? Atbildi raksti kā a/b.",
         "atb": ["1/12"], "padoms": "{9|12} - {8|12}."},
    ], pamats=4,
        ievads="Beidz ar pārbaudi: vai atbildi var uzrakstīt īsāk."),

    Zimejums("Kas paliek no puses",
             dala(6, 1, "1/6"),
             paskaidro="No {3|6} atņemot {2|6}, paliek viens gabals no "
                       "sešiem - tāpēc starpība ir {1|6}.",
             ievads="Atņemšana uz joslas ir gabalu noņemšana."),

    Varianti("Pārbaudi atņemšanu", [
        {"jaut": "Kas notiek ar saucēju, atņemot daļas ar kopsaucēju?",
         "opcijas": ["Tas paliek nemainīgs", "Tas atņemas",
                     "Tas dalās", "Tas divkāršojas"],
         "pareizi": 0,
         "padoms": "Gabalu lielums nemainās."},
        {"jaut": "Skolēns rēķina {3|4} - {1|2} = {2|2}. Kas nav labi?",
         "opcijas": ["Atņemti arī saucēji", "Nav saīsināts",
                     "Kopsaucējs par mazu", "Viss ir labi"],
         "pareizi": 0,
         "padoms": "Saucēju neatņem."},
        {"jaut": "Starpība iznāca {4|8}. Kā to raksta atbildē?",
         "opcijas": ["{1|2}", "{4|8}", "{2|4}", "{8|4}"],
         "pareizi": 0,
         "padoms": "Saīsina līdz galam."},
        {"jaut": "Kā pārbaudīt atņemšanas rezultātu?",
         "opcijas": ["Pieskaitīt starpību atņēmējam",
                     "Saskaitīt abas dotās daļas",
                     "Saīsināt vēlreiz",
                     "Pārbaudīt nevar"],
         "pareizi": 0,
         "padoms": "Atņemšanu pārbauda ar saskaitīšanu."},
        {"jaut": "Vai starpība var būt lielāka par mazināmo?",
         "opcijas": ["Nē", "Jā, ja saucēji atšķiras",
                     "Jā, vienmēr", "Tikai ar neīstām daļām"],
         "pareizi": 0,
         "padoms": "Atņemot paliek mazāk."},
        {"jaut": "Cik ir {5|6} - {5|6}?",
         "opcijas": ["0", "1", "{5|6}", "{1|6}"],
         "pareizi": 0,
         "padoms": "Noņem visu, kas bija."},
    ], pamats=4),

    Pasaule("Cik brīvā laika paliek?",
            Ievadi("", [
                {"jaut": "No skolas dienas {3|4} aizņem stundas, {1|2} no "
                         "dienas ir mājās. Cik ir {3|4} - {1|2}? Atbildi "
                         "raksti kā a/b.",
                 "atb": ["1/4"], "padoms": "{3|4} - {2|4}."},
                {"jaut": "Mājasdarbiem atvēlētas {2|3} stundas, pabeigtas "
                         "{1|6}. Cik palicis? Atbildi raksti kā a/b.",
                 "atb": ["1/2", "3/6"], "padoms": "{4|6} - {1|6} = {3|6}."},
                {"jaut": "Projektam doti {5|6} no nedēļas, pagājušas {1|3}. "
                         "Cik palicis? Atbildi raksti kā a/b.",
                 "atb": ["1/2", "3/6"], "padoms": "{5|6} - {2|6}."},
                {"jaut": "No {7|8} stundas pagājušas {1|4}. Cik palicis? "
                         "Atbildi raksti kā a/b.",
                 "atb": ["5/8"], "padoms": "{7|8} - {2|8}."},
            ]),
            pavediens="skola",
            konteksts="Skolas dienā viss ir daļas no dienas, un brīvais "
                      "laiks ir tieši tas, kas paliek pāri.",
            kapec="Atņemšana ar kopsaucēju pasaka, cik daudz tas ir."),

    Kopsavilkums([
        "Atņemu daļas ar dažādiem saucējiem, lietojot kopsaucēju.",
        "Atņemu skaitītājus, saucēju atstājot nemainīgu.",
        "Saīsinu rezultātu, ja tas ir saīsināms.",
        "Pārbaudu atņemšanu ar saskaitīšanu.",
    ]),

    Majas([
        "Izrēķini {5|6} - {3|4} un pieraksti visus soļus.",
        "Atrodi divas daļas, kuru starpība ir tieši {1|4}.",
        "Pārbaudi vienu savu atbildi, pieskaitot starpību atņēmējam.",
    ]),
]
