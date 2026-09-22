# -*- coding: utf-8 -*-
"""5. klase, 81. stunda: «Cik precīzi metieni?»

Sporta statistika ir vieta, kur daļas lieto katru dienu, bet nekad nesauc
vārdā. Te skolēns to izdara pats: no diviem skaitļiem izveido daļu, saīsina
to un izdara secinājumu. Svarīgākā stundas daļa ir pēdējais solis - ar skaitli
vien nepietiek, jāpasaka arī, ko tas nozīmē.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala, kolonnas)

TEMA = "Cik precīzi metieni?"

MERKIS = ("Mācīsimies izteikt vienu lielumu kā otra daļu sporta datos un "
          "formulēt secinājumu.")

SATURS = [
    Sakums("Metienu tabula pēc spēles",
           zimejums=kolonnas([("Anna", 9), ("Roberts", 12), ("Elza", 8)]),
           paraksts="Stabiņi rāda trāpījumu skaitu, nevis precizitāti.",
           fakti=["Anna trāpīja 9 no 12 metieniem.",
                  "Roberts trāpīja 12 no 20 metieniem.",
                  "Vairāk metienu nenozīmē precīzāku spēlētāju."]),

    Doma("Precizitāte ir daļa, nevis skaits",
         "Precizitāti izsaka kā daļu: trāpīto metienu skaits pār visu "
         "metienu skaitu.",
         soli=[
             "Atrodi, cik metienu bija pavisam - tas ir veselais.",
             "Atrodi, cik no tiem trāpīja - tas ir gabals.",
             "Uzraksti daļu un saīsini to.",
             "Salīdzini daļas ar kopsaucēju.",
             "Formulē secinājumu vārdiem: kurš bija precīzāks un cik.",
         ],
         pieze="Daļa nesaka, kurš guva vairāk punktu - tikai to, cik droši "
               "viņš met. Abi skaitļi ir vajadzīgi: precīzs spēlētājs ar "
               "diviem metieniem komandai palīdz mazāk nekā ar divdesmit."),

    Paraugs("Kurš metis precīzāk?",
            uzd="Anna trāpīja 9 no 12 metieniem, Roberts 12 no 20. Kurš bija "
                "precīzāks?",
            soli=[
                ("Anna: {9|12}",
                 "Trāpītie pār visiem."),
                ("{9|12} = {3|4}",
                 "Abus locekļus dala ar 3."),
                ("Roberts: {12|20} = {3|5}",
                 "Abus locekļus dala ar 4."),
                ("{3|4} = {15|20}, {3|5} = {12|20}",
                 "Ar kopsaucēju 20."),
                ("15 > 12",
                 "Anna ir precīzāka."),
            ],
            atbilde="Precīzāka bija Anna: {3|4} pret {3|5}"),

    Ievadi("Izsaki precizitāti kā daļu", [
        {"jaut": "9 trāpījumi no 12 metieniem. Kāda daļa? Atbildi raksti kā "
                 "a/b.",
         "atb": ["3/4", "9/12"], "padoms": "Abus dala ar 3."},
        {"jaut": "12 trāpījumi no 20 metieniem. Kāda daļa? Atbildi raksti kā "
                 "a/b.",
         "atb": ["3/5", "12/20"], "padoms": "Abus dala ar 4."},
        {"jaut": "6 trāpījumi no 8 metieniem. Kāda daļa? Atbildi raksti kā "
                 "a/b.",
         "atb": ["3/4", "6/8"], "padoms": "Abus dala ar 2."},
        {"jaut": "14 trāpījumi no 21 metiena. Kāda daļa? Atbildi raksti kā "
                 "a/b.",
         "atb": ["2/3", "14/21"], "padoms": "Abus dala ar 7."},
        {"jaut": "15 trāpījumi no 25 metieniem. Kāda daļa? Atbildi raksti kā "
                 "a/b.",
         "atb": ["3/5", "15/25"], "padoms": "Abus dala ar 5."},
        {"jaut": "Komanda uzvarēja 8 no 24 spēlēm. Kāda daļa? Atbildi raksti "
                 "kā a/b.",
         "atb": ["1/3", "8/24"], "padoms": "Abus dala ar 8."},
        {"jaut": "Komanda uzvarēja 18 no 30 spēlēm. Kāda daļa? Atbildi "
                 "raksti kā a/b.",
         "atb": ["3/5", "18/30"], "padoms": "Abus dala ar 6."},
        {"jaut": "Kura daļa ir lielāka - {3|4} vai {3|5}? Ieraksti kā a/b.",
         "atb": ["3/4"], "padoms": "Ceturtdaļas ir lielākas par "
                                   "piektdaļām."},
    ], pamats=4,
        ievads="Trāpītie skaitītājā, visi metieni saucējā - un tad saīsini."),

    Zimejums("Trīs no četriem metieniem",
             dala(4, 3, "3/4"),
             paskaidro="Tā izskatās Annas precizitāte: no katriem četriem "
                       "metieniem trīs ir trāpīti.",
             ievads="Saīsināta daļa pasaka to pašu ar mazākiem skaitļiem."),

    Varianti("Ko rāda skaitlis un ko - daļa?", [
        {"jaut": "Kurš skaitlis ir saucējā?",
         "opcijas": ["Visu metienu skaits", "Trāpīto metienu skaits",
                     "Punktu skaits", "Spēļu skaits"],
         "pareizi": 0,
         "padoms": "Saucējs ir veselais."},
        {"jaut": "Anna trāpīja 9 no 12, Elza 8 no 8. Kura ir precīzāka?",
         "opcijas": ["Elza", "Anna", "Vienādi", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "{8|8} = 1."},
        {"jaut": "Vai vairāk trāpījumu vienmēr nozīmē lielāku precizitāti?",
         "opcijas": ["Nē, svarīgs ir arī metienu skaits", "Jā",
                     "Tikai basketbolā", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "12 no 20 ir mazāk precīzi nekā 9 no 12."},
        {"jaut": "{8|24} saīsinātā veidā ir...",
         "opcijas": ["{1|3}", "{2|6}", "{4|12}", "{3|1}"],
         "pareizi": 0,
         "padoms": "Abus dala ar 8."},
        {"jaut": "Ko nozīmē precizitāte {1|2}?",
         "opcijas": ["Trāpīta puse metienu", "Trāpīts viens metiens",
                     "Bija divi metieni", "Trāpīts divreiz"],
         "pareizi": 0,
         "padoms": "Daļa no visiem metieniem."},
        {"jaut": "Ar ko beidzas secinājums?",
         "opcijas": ["Ar teikumu, kurš bija precīzāks",
                     "Ar daļu",
                     "Ar kopsaucēju",
                     "Ar stabiņu diagrammu"],
         "pareizi": 0,
         "padoms": "Skaitlis pats neko nepasaka."},
    ], pamats=4),

    Pasaule("Kuru izvēlēties komandā?",
            Ievadi("", [
                {"jaut": "Marks trāpīja 10 no 16 metieniem. Kāda daļa? "
                         "Atbildi raksti kā a/b.",
                 "atb": ["5/8", "10/16"], "padoms": "Abus dala ar 2."},
                {"jaut": "Elza trāpīja 9 no 15. Kāda daļa? Atbildi raksti kā "
                         "a/b.",
                 "atb": ["3/5", "9/15"], "padoms": "Abus dala ar 3."},
                {"jaut": "Ar kopsaucēju 40: cik ir Marka skaitītājs?",
                 "atb": ["25"], "padoms": "{5|8} = {25|40}."},
                {"jaut": "Ar kopsaucēju 40: cik ir Elzas skaitītājs?",
                 "atb": ["24"], "padoms": "{3|5} = {24|40}."},
            ]),
            pavediens="sports",
            konteksts="Treneris izvēlas spēlētāju pēc precizitātes, nevis "
                      "pēc metienu skaita.",
            kapec="Daļa salīdzina spēlētājus, kuriem metienu skaits atšķiras."),

    Kopsavilkums([
        "Izsaku trāpījumus kā daļu no visiem metieniem.",
        "Saīsinu iegūto daļu.",
        "Salīdzinu divu spēlētāju precizitāti ar kopsaucēju.",
        "Formulēju secinājumu vārdiem, nevis tikai ar skaitli.",
    ]),

    Majas([
        "Atrodi sporta ziņās divus rezultātus un salīdzini precizitāti.",
        "Izsaki savu rezultātu kādā spēlē kā daļu.",
        "Uzraksti, kāpēc precizitāte {1|1} ar vienu metienu neko nepierāda.",
    ]),
]
