# -*- coding: utf-8 -*-
"""5. klase, 60. stunda: «Kā salīdzināt daļas ar dažādiem saucējiem?»

Jauns mikrotemats, bet neviena jauna darbība: salīdzināšana te ir tikai
paplašināšana plus veselu skaitļu salīdzināšana. Tieši tāpēc stunda sākas ar
atgādinājumu, ka lielāks saucējs nenozīmē lielāku daļu - šī ir biežākā kļūda,
un ar modeli to var novērst uzreiz.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala, taisne)

TEMA = "Kā salīdzināt daļas ar dažādiem saucējiem?"

MERKIS = ("Iemācīsimies salīdzināt divas daļas, vienādojot to saucējus, un "
          "skaidrot katru darbību.")

SATURS = [
    Sakums("Kurš sitis precīzāk?",
           zimejums=dala(5, 3, "3/5"),
           paraksts="Trīs precīzi metieni no pieciem.",
           fakti=["Viens spēlētājs trāpīja 3 no 5, otrs 5 no 8.",
                  "Metienu skaits atšķiras, tāpēc skaitļus salīdzināt nevar.",
                  "Vispirms abiem jādod viens saucējs."]),

    Doma("Vienāds saucējs - salīdzina skaitītājus",
         "Lai salīdzinātu daļas ar dažādiem saucējiem, tās paplašina līdz "
         "kopīgam saucējam un tad salīdzina tikai skaitītājus.",
         soli=[
             "Atrodi skaitli, kas dalās ar abiem saucējiem.",
             "Paplašini katru daļu līdz šim saucējam.",
             "Salīdzini skaitītājus kā parastus skaitļus.",
             "Uzraksti atbildi ar sākotnējām daļām.",
         ],
         pieze="Lielāks saucējs nenozīmē lielāku daļu - tieši otrādi: jo "
               "lielāks saucējs, jo sīkāki gabali. Tāpēc {1|8} ir mazāka "
               "nekā {1|3}, kaut 8 ir lielāks par 3."),

    Paraugs("{3|5} vai {5|8}?",
            uzd="Viens spēlētājs trāpīja 3 no 5 metieniem, otrs 5 no 8. "
                "Kurš sitis precīzāk?",
            soli=[
                ("Kopīgais saucējs ir 40",
                 "40 dalās ar 5 un ar 8."),
                ("{3|5} = {24|40}",
                 "Abus locekļus reizina ar 8."),
                ("{5|8} = {25|40}",
                 "Abus locekļus reizina ar 5."),
                ("24 < 25",
                 "Salīdzina tikai skaitītājus."),
                ("{3|5} < {5|8}",
                 "Atbildi raksta ar sākotnējām daļām."),
            ],
            atbilde="Precīzāk sitis otrais spēlētājs"),

    Ievadi("Kura daļa ir lielāka?", [
        {"jaut": "{1|2} vai {1|3}? Ieraksti lielāko kā a/b.",
         "atb": ["1/2"], "padoms": "Puse ir lielāka par trešdaļu."},
        {"jaut": "{2|3} vai {3|4}? Ieraksti lielāko kā a/b.",
         "atb": ["3/4"], "padoms": "Ar saucēju 12: {8|12} un {9|12}."},
        {"jaut": "{3|5} vai {2|4}? Ieraksti lielāko kā a/b.",
         "atb": ["3/5"], "padoms": "Ar saucēju 20: {12|20} un {10|20}."},
        {"jaut": "{5|6} vai {7|9}? Ieraksti lielāko kā a/b.",
         "atb": ["5/6"], "padoms": "Ar saucēju 18: {15|18} un {14|18}."},
        {"jaut": "{4|7} vai {3|5}? Ieraksti lielāko kā a/b.",
         "atb": ["3/5"], "padoms": "Ar saucēju 35: {20|35} un {21|35}."},
        {"jaut": "{2|5} vai {3|10}? Ieraksti lielāko kā a/b.",
         "atb": ["2/5"], "padoms": "Ar saucēju 10: {4|10} un {3|10}."},
        {"jaut": "{5|8} vai {7|12}? Ieraksti lielāko kā a/b.",
         "atb": ["5/8"], "padoms": "Ar saucēju 24: {15|24} un {14|24}."},
        {"jaut": "{3|4} vai {7|10}? Ieraksti lielāko kā a/b.",
         "atb": ["3/4"], "padoms": "Ar saucēju 20: {15|20} un {14|20}."},
    ], pamats=4,
        ievads="Vispirms viens saucējs, tikai tad salīdzināšana."),

    Zimejums("Abas daļas uz vienas taisnes",
             taisne(0, 1, 1, [(3 / 5.0, "3/5"), (5 / 8.0, "5/8")],
                    virsraksts="Tikai nedaudz, bet viena ir tālāk"),
             paskaidro="Atšķirība ir viena četrdesmitdaļa - ar aci to gandrīz "
                       "neredz, bet ar kopīgo saucēju redz skaidri.",
             ievads="Kad daļas ir tuvu, rēķins ir drošāks par acumēru."),

    Varianti("Kā salīdzina daļas?", [
        {"jaut": "Ko dara vispirms, salīdzinot daļas ar dažādiem saucējiem?",
         "opcijas": ["Atrod kopīgu saucēju", "Salīdzina skaitītājus",
                     "Salīdzina saucējus", "Saīsina abas daļas"],
         "pareizi": 0,
         "padoms": "Salīdzināt var tikai vienādus gabalus."},
        {"jaut": "Vai lielāks saucējs nozīmē lielāku daļu?",
         "opcijas": ["Nē, gabali kļūst sīkāki", "Jā, vienmēr",
                     "Jā, ja skaitītājs ir 1", "Tikai ar pāra skaitļiem"],
         "pareizi": 0,
         "padoms": "{1|8} un {1|3}."},
        {"jaut": "Divām daļām ir vienāds skaitītājs. Kura ir lielāka?",
         "opcijas": ["Tā, kurai mazāks saucējs", "Tā, kurai lielāks saucējs",
                     "Tās ir vienādas", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Lielāki gabali - lielāka daļa."},
        {"jaut": "{3|7} un {3|5} - kura ir lielāka?",
         "opcijas": ["{3|5}", "{3|7}", "Tās ir vienādas", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Piektdaļas ir lielākas par septītdaļām."},
        {"jaut": "Kāds ir ērtākais kopīgais saucējs daļām {1|4} un {1|6}?",
         "opcijas": ["12", "24", "10", "6"],
         "pareizi": 0,
         "padoms": "Mazākais skaitlis, kas dalās ar 4 un 6."},
        {"jaut": "Ar ko beidzas salīdzināšanas pieraksts?",
         "opcijas": ["Ar atbildi par sākotnējām daļām",
                     "Ar kopīgo saucēju",
                     "Ar saīsinātām daļām",
                     "Ar zīmējumu"],
         "pareizi": 0,
         "padoms": "Jautājums bija par dotajām daļām."},
    ], pamats=4),

    Pasaule("Kurš sportists ir precīzāks?",
            Ievadi("", [
                {"jaut": "Anna trāpīja 3 no 4 metieniem, Roberts 5 no 8. Cik "
                         "astotdaļu ir Annas rezultāts?",
                 "atb": ["6"], "padoms": "{3|4} = {6|8}."},
                {"jaut": "Kurš rezultāts ir labāks? Ieraksti vārdu: Anna vai "
                         "Roberts.",
                 "atb": ["Anna", "anna"], "padoms": "6 no 8 pret 5 no 8."},
                {"jaut": "Marks trāpīja 7 no 10, Elza 2 no 3. Cik "
                         "trīsdesmitdaļu ir Marka rezultāts?",
                 "atb": ["21"], "padoms": "{7|10} = {21|30}."},
                {"jaut": "Cik trīsdesmitdaļu ir Elzas rezultāts?",
                 "atb": ["20"], "padoms": "{2|3} = {20|30}."},
            ]),
            pavediens="sports",
            konteksts="Statistikā metienu skaits nekad nav vienāds, tāpēc "
                      "procentus un daļas rēķina ar vienu saucēju.",
            kapec="Bez kopīga saucēja skaitļi ir salīdzināmi tikai no "
                  "izskata."),

    Kopsavilkums([
        "Atrodu divām daļām kopīgu saucēju.",
        "Paplašinu abas daļas līdz šim saucējam.",
        "Salīdzinu daļas, salīdzinot to skaitītājus.",
        "Zinu, ka lielāks saucējs nozīmē sīkākus gabalus.",
    ]),

    Majas([
        "Salīdzini {4|9} un {1|2}, pierakstot visus soļus.",
        "Atrodi sporta statistikā divus rezultātus ar dažādiem saucējiem un "
        "salīdzini tos.",
        "Uzraksti divas daļas, kuras salīdzināt var bez kopīga saucēja, un "
        "paskaidro, kāpēc.",
    ]),
]
