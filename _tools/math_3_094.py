# -*- coding: utf-8 -*-
"""3. klase, 94. stunda: «Vai vienu skaitli var pierakstīt dažādi?»

Vienādas daļas ar dažādiem pierakstiem. Ar modeli tas ir redzams uzreiz -
puse un divas ceturtdaļas aizņem vienu un to pašu vietu -, un no šī
atklājuma vēlāk aug daļu paplašināšana un saīsināšana.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         dala)

TEMA = "Vai vienu skaitli var pierakstīt dažādi?"

MERKIS = ("Ar modeli parādīsim, ka puse ir tas pats, kas divas ceturtdaļas.")

SATURS = [
    Sakums("Vai {1|2} un {2|4} ir viens un tas pats?",
           zimejums=dala(4, 2, "2/4 = 1/2", "četras vienādas daļas"),
           paraksts="Abas aizņem tieši pusi joslas.",
           fakti=["Vienu un to pašu daļu var pierakstīt vairākos veidos.",
                  "{1|2} = {2|4} = {4|8} - visas ir puse."]),

    Doma("Vienu daļu var pierakstīt dažādi",
         "Ja daļas sadala sīkāk, gabalu skaits aug, bet aizņemtā vieta paliek "
         "tā pati.",
         soli=[
             "Uzzīmē joslu un iekrāso pusi.",
             "Sadali katru pusi uz pusēm - sanāk četras daļas.",
             "Iekrāsotā daļa tagad ir divas no četrām.",
             "Vieta nemainījās, tāpēc {1|2} = {2|4}.",
         ],
         pieze="Skaitītājs un saucējs abi kļuva divreiz lielāki. Tā vienmēr "
               "notiek: {1|2} = {2|4} = {3|6} = {4|8}."),

    Petijums("Atrodi vienādas daļas",
             vajag="trīs vienāda garuma sloksnes un krāsainie zīmuļi",
             soli=[
                 "Pirmo sloksni sadali 2 daļās un iekrāso vienu.",
                 "Otro sadali 4 daļās un iekrāso tik, lai sakristu.",
                 "Trešo sadali 8 daļās un dari to pašu.",
                 "Pieraksti visas trīs daļas.",
             ],
             secinajums="Visas trīs iekrāsotās daļas ir vienāda garuma - "
                        "tātad {1|2} = {2|4} = {4|8}."),

    Paraugs("Cik ceturtdaļu ir pusē?",
            uzd="Cik ceturtdaļu ir vienā pusē?",
            soli=[
                ("Veselais sadalīts 4 daļās",
                 "Saucējs ir 4."),
                ("Puse ir 4 : 2 = 2 daļas",
                 "Puse no četrām ceturtdaļām."),
                ("{1|2} = {2|4}",
                 "Abi pieraksti nozīmē vienu un to pašu."),
            ],
            atbilde="2 ceturtdaļas"),

    Ievadi("Atrodi vienādo daļu", [
        {"jaut": "{1|2} = {?|4}. Ieraksti skaitītāju.", "atb": ["2"],
         "padoms": "4 : 2."},
        {"jaut": "{1|2} = {?|8}. Ieraksti skaitītāju.", "atb": ["4"],
         "padoms": "8 : 2."},
        {"jaut": "{1|2} = {?|10}. Ieraksti skaitītāju.", "atb": ["5"],
         "padoms": "10 : 2."},
        {"jaut": "{1|3} = {?|6}. Ieraksti skaitītāju.", "atb": ["2"],
         "padoms": "6 : 3."},
        {"jaut": "{1|4} = {?|8}. Ieraksti skaitītāju.", "atb": ["2"],
         "padoms": "8 : 4."},
        {"jaut": "{3|4} = {?|8}. Ieraksti skaitītāju.", "atb": ["6"],
         "padoms": "3 · 2."},
    ], pamats=4),

    Zimejums("Astotdaļas un puse",
             dala(8, 4, "4/8 = 1/2", "astoņas vienādas daļas"),
             paskaidro="Četras astotdaļas aizņem tieši tikpat, cik viena "
                       "puse.",
             ievads="Tā pati puse, cits pieraksts."),

    Varianti("Kuras daļas ir vienādas?", [
        {"jaut": "Kura daļa ir vienāda ar {1|2}?",
         "opcijas": ["{5|10}", "{2|10}", "{10|5}", "{1|10}"],
         "pareizi": 0, "padoms": "10 : 2 = 5."},
        {"jaut": "Kura daļa ir vienāda ar {1|4}?",
         "opcijas": ["{2|8}", "{4|8}", "{1|8}", "{8|2}"],
         "pareizi": 0, "padoms": "8 : 4 = 2."},
        {"jaut": "Kas notiek ar abiem skaitļiem, sadalot daļas sīkāk?",
         "opcijas": ["Abi kļūst vienādu reižu lielāki",
                     "Tikai saucējs kļūst lielāks",
                     "Tikai skaitītājs kļūst lielāks",
                     "Abi kļūst mazāki"],
         "pareizi": 0, "padoms": "{1|2} = {2|4} = {3|6}."},
        {"jaut": "Kura daļa *nav* vienāda ar {1|2}?",
         "opcijas": ["{3|4}", "{2|4}", "{4|8}", "{6|12}"],
         "pareizi": 0, "padoms": "Trīs ceturtdaļas ir vairāk par pusi."},
    ], pamats=4),

    Pasaule("Cik daļu no meža ir priedes?",
            Ievadi("", [
                {"jaut": "Mežā 20 koki, 10 no tiem priedes. Cik ir puse no "
                         "20?",
                 "atb": ["10"], "padoms": "20 : 2."},
                {"jaut": "Cik desmitdaļu no meža ir priedes? Ieraksti "
                         "skaitītāju.",
                 "atb": ["5"], "padoms": "{1|2} = {5|10}."},
                {"jaut": "Mežā 40 koki, {1|4} ir bērzi. Cik ir bērzu?",
                 "atb": ["10"], "padoms": "40 : 4."},
                {"jaut": "Cik astotdaļu no meža ir bērzi? Ieraksti "
                         "skaitītāju.",
                 "atb": ["2"], "padoms": "{1|4} = {2|8}."},
            ]),
            pavediens="daba",
            konteksts="Mežsargs koku daļu var pierakstīt gan ceturtdaļās, "
                      "gan astotdaļās - skaits no tā nemainās.",
            kapec="Viena un tā pati daļa dažādos pierakstos ir viens un tas "
                  "pats daudzums."),

    Kopsavilkums([
        "Zinu, ka vienu daļu var pierakstīt dažādos veidos.",
        "Parādu ar modeli, ka {1|2} = {2|4} = {4|8}.",
        "Atrodu vienādu daļu ar citu saucēju.",
        "Zinu, ka abi daļas skaitļi mainās vienādu reižu skaitu.",
    ]),

    Majas([
        "Uzzīmē divas vienāda garuma joslas un parādi, ka {1|2} = {3|6}.",
        "Atrodi trīs pierakstus daļai {1|4}.",
        "Pastāsti mājiniekiem, kāpēc {2|4} un {1|2} ir viens un tas pats.",
    ]),
]
