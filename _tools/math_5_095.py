# -*- coding: utf-8 -*-
"""5. klase, 95. stunda: «Kurš jauktais skaitlis lielāks?»

Salīdzināšana ar jauktiem skaitļiem ir vieglāka nekā ar daļām: gandrīz
vienmēr pietiek ar veselo daļu, un daļas jāsalīdzina tikai tad, kad veselās
sakrīt. Tieši tāpēc šī stunda māca pārbaudīt secībā - vispirms lielais
skaitlis, tikai pēc tam mazais.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kurš jauktais skaitlis lielāks?"

MERKIS = ("Iemācīsimies salīdzināt jauktus skaitļus un pamatot "
          "salīdzinājumu.")

SATURS = [
    Sakums("Divas dēļu garumu zīmes",
           zimejums=taisne(0, 4, 1, [(2.25, "2 1/4"), (3.5, "3 1/2")],
                           virsraksts="Kurš dēlis ir garāks"),
           paraksts="3{1|2} ir pa labi no 2{1|4}, tātad lielāks.",
           fakti=["Viens dēlis ir 2{1|4} m, otrs 3{1|2} m.",
                  "Veselās daļas ir 2 un 3 - ar to jau pietiek.",
                  "Daļas šoreiz nav jāsalīdzina nemaz."]),

    Doma("Vispirms veselās daļas",
         "Jauktus skaitļus salīdzina pēc veselajām daļām; ja tās ir vienādas, "
         "salīdzina daļas.",
         soli=[
             "Salīdzini veselās daļas.",
             "Lielāka veselā daļa - lielāks skaitlis.",
             "Ja veselās daļas vienādas, salīdzini daļas.",
             "Daļas ar dažādiem saucējiem pārraksta ar kopsaucēju.",
             "Pieraksti salīdzinājumu ar zīmi < vai >.",
         ],
         pieze="Ja viens skaitlis ir neīsta daļa, to vispirms pārveido par "
               "jauktu: {11|4} un 2{1|2} salīdzināt ir grūti, bet 2{3|4} un "
               "2{1|2} - viegli."),

    Paraugs("Kurš lielāks: 2{3|4} vai 2{2|3}?",
            uzd="Salīdzini divus jauktus skaitļus un pamato atbildi.",
            soli=[
                ("Veselās daļas abiem ir 2",
                 "Ar tām neizšķiras."),
                ("Salīdzina {3|4} un {2|3}",
                 "Pāriet uz daļām."),
                ("Kopsaucējs ir 12",
                 "12 dalās ar 4 un 3."),
                ("{3|4} = {9|12}, {2|3} = {8|12}",
                 "Abas daļas ar vienu saucēju."),
                ("2{3|4} > 2{2|3}",
                 "9 > 8."),
            ],
            atbilde="Lielāks ir 2{3|4}"),

    Ievadi("Kurš skaitlis ir lielāks?", [
        {"jaut": "2{1|4} vai 3{1|2}? Ieraksti lielāko kā a b/c.",
         "atb": ["3 1/2"], "padoms": "Veselās daļas 2 un 3."},
        {"jaut": "4{1|8} vai 4{3|8}? Ieraksti lielāko kā a b/c.",
         "atb": ["4 3/8"], "padoms": "Veselās vienādas, saucēji vienādi."},
        {"jaut": "2{3|4} vai 2{2|3}? Ieraksti lielāko kā a b/c.",
         "atb": ["2 3/4"], "padoms": "{9|12} pret {8|12}."},
        {"jaut": "5{1|3} vai 5{1|4}? Ieraksti lielāko kā a b/c.",
         "atb": ["5 1/3"], "padoms": "Trešdaļa ir lielāka par ceturtdaļu."},
        {"jaut": "1{5|6} vai 2{1|6}? Ieraksti lielāko kā a b/c.",
         "atb": ["2 1/6"], "padoms": "Veselās daļas 1 un 2."},
        {"jaut": "{11|4} vai 2{1|2}? Ieraksti lielāko kā a b/c.",
         "atb": ["2 3/4"], "padoms": "{11|4} = 2{3|4}."},
        {"jaut": "3{2|5} vai 3{1|2}? Ieraksti lielāko kā a b/c.",
         "atb": ["3 1/2"], "padoms": "{4|10} pret {5|10}."},
        {"jaut": "{13|2} kā jaukts skaitlis. Atbildi raksti kā a b/c.",
         "atb": ["6 1/2"], "padoms": "13 : 2 = 6, atl. 1."},
    ], pamats=4,
        ievads="Vispirms veselās daļas; daļas - tikai tad, ja vajag."),

    Zimejums("Kur katrs stāv uz taisnes",
             taisne(0, 4, 1, [(2.25, "2 1/4"), (2.75, "2 3/4"),
                              (3.5, "3 1/2")],
                    virsraksts="Pa labi - lielāks"),
             paskaidro="Divi punkti ir starp 2 un 3, viens - starp 3 un 4. "
                       "Trešais ir lielākais jau pēc veselās daļas.",
             ievads="Uz taisnes salīdzinājums ir redzams bez rēķina."),

    Varianti("Ar ko sāk salīdzināšanu?", [
        {"jaut": "Ko salīdzina vispirms?",
         "opcijas": ["Veselās daļas", "Daļu skaitītājus", "Daļu saucējus",
                     "Skaitļu garumu"],
         "pareizi": 0,
         "padoms": "Lielais skaitlis izšķir biežāk."},
        {"jaut": "Kad jāsalīdzina arī daļas?",
         "opcijas": ["Kad veselās daļas ir vienādas", "Vienmēr", "Nekad",
                     "Kad saucēji ir vienādi"],
         "pareizi": 0,
         "padoms": "Citādi ar veselo pietiek."},
        {"jaut": "Kurš skaitlis ir lielākais?",
         "opcijas": ["3{1|8}", "2{7|8}", "2{1|2}", "1{9|10}"],
         "pareizi": 0,
         "padoms": "Veselā daļa ir 3."},
        {"jaut": "5{1|3} un 5{1|4} - kurš lielāks?",
         "opcijas": ["5{1|3}", "5{1|4}", "Vienādi", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "{4|12} pret {3|12}."},
        {"jaut": "Ko dara ar neīstu daļu, pirms salīdzina?",
         "opcijas": ["Pārveido par jauktu skaitli", "Saīsina",
                     "Paplašina", "Neko"],
         "pareizi": 0,
         "padoms": "Tad veselās daļas ir redzamas."},
        {"jaut": "Vai 2{9|8} ir pareizi uzrakstīts jaukts skaitlis?",
         "opcijas": ["Nav, daļa nav īsta", "Ir", "Ir, ja saucējs ir 8",
                     "To nevar zināt"],
         "pareizi": 0,
         "padoms": "{9|8} ir lielāka par 1."},
    ], pamats=4),

    Pasaule("Kurš dēlis der?",
            Ievadi("", [
                {"jaut": "Dēļi ir 2{1|4} m un 2{1|2} m gari. Kurš ir garāks? "
                         "Ieraksti kā a b/c.",
                 "atb": ["2 1/2"], "padoms": "{1|2} > {1|4}."},
                {"jaut": "Vajag dēli, garāku par 2{3|4} m. Vai der 2{1|2} m "
                         "dēlis? Raksti «jā» vai «nē».",
                 "atb": ["nē", "ne"], "padoms": "2{1|2} < 2{3|4}."},
                {"jaut": "Vai der 3{1|8} m dēlis? Raksti «jā» vai «nē».",
                 "atb": ["jā", "ja"], "padoms": "Veselā daļa ir 3."},
                {"jaut": "Dēlis ir {11|4} m garš. Cik tas ir kā jaukts "
                         "skaitlis? Atbildi raksti kā a b/c.",
                 "atb": ["2 3/4"], "padoms": "11 : 4."},
            ]),
            pavediens="maja",
            konteksts="Būvmateriālu garumus raksta ar jauktiem skaitļiem, un "
                      "izvēle jāizdara veikalā, nevis mājās.",
            kapec="Salīdzināt pēc veselās daļas var uzreiz, ar aci."),

    Kopsavilkums([
        "Salīdzinu jauktus skaitļus pēc veselajām daļām.",
        "Salīdzinu daļas, ja veselās daļas ir vienādas.",
        "Pārveidoju neīstu daļu par jauktu skaitli, pirms salīdzinu.",
        "Pamatoju salīdzinājumu ar skaitļiem, ne ar izskatu.",
    ]),

    Majas([
        "Sakārto augošā secībā 2{1|2}, {11|4} un 2{1|3}.",
        "Uzraksti divus jauktus skaitļus, kurus nevar salīdzināt pēc "
        "veselās daļas.",
        "Paskaidro, kāpēc {13|2} un 6{1|2} ir viens un tas pats skaitlis.",
    ]),
]
