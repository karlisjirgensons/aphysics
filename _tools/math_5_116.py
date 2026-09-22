# -*- coding: utf-8 -*-
"""5. klase, 116. stunda: «Cik reižu rādiuss ietilpst riņķa līnijā?»

Iepriekšējās stundas tabula te pārvēršas sakarībā. Visiem mērījumiem
attiecība C : d iznāk apmēram viena un tā pati - tas ir atklājums, ko
skolēns izdara pats no saviem datiem. Skaitli pi 5. klasē vēl nemāca
precīzi; pietiek ar «apmēram trīs» un ar to, ka tas nav atkarīgs no lieluma.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         restis, rinkis)

TEMA = "Cik reižu rādiuss ietilpst riņķa līnijā?"

MERKIS = ("Mācīsimies formulēt sakarību starp rādiusu, diametru un riņķa "
          "līnijas garumu.")

SATURS = [
    Sakums("Visiem iznāk viens skaitlis",
           zimejums=restis([["25:8", "31:10", "16:5"]],
                           virsraksts="Trīs dažādas lietas"),
           paraksts="Visas trīs attiecības ir apmēram 3 - neatkarīgi no "
                    "lieluma.",
           fakti=["Lielai bundžai un mazai monētai attiecība ir viena.",
                  "Riņķa līnijas garums ir apmēram 3 diametri.",
                  "Tātad tas ir apmēram 6 rādiusi."]),

    Doma("Garums ir apmēram trīs diametri",
         "Riņķa līnijas garums ir apmēram trīs reizes lielāks par diametru "
         "un apmēram sešas reizes lielāks par rādiusu; šī attiecība ir viena "
         "un tā pati visām riņķa līnijām.",
         soli=[
             "Izmēri vai uzzini diametru.",
             "Reizini to ar 3 - iegūsi aptuveno garumu.",
             "Ja zināms rādiuss, reizini to ar 6.",
             "Ja zināms garums, dali to ar 3 - iegūsi diametru.",
             "Atceries: atbilde ir aptuvena.",
         ],
         pieze="Precīzāk attiecība ir 3,14, un to apzīmē ar burtu π. To "
               "5. klasē vēl nelieto rēķinos, bet skaitlis ir tas pats "
               "visām riņķa līnijām pasaulē - lielām un mazām."),

    Slidnis("Riņķa līnija aug, attiecība nemainās",
            [{"v": "d = 5 cm", "teksts": "garums apmēram 15 cm", "josla": 20,
              "zim": rinkis(diametrs="5 cm")},
             {"v": "d = 10 cm", "teksts": "garums apmēram 30 cm",
              "josla": 40, "zim": rinkis(diametrs="10 cm")},
             {"v": "d = 20 cm", "teksts": "garums apmēram 60 cm",
              "josla": 70, "zim": rinkis(diametrs="20 cm")},
             {"v": "d = 30 cm", "teksts": "garums apmēram 90 cm",
              "josla": 100, "zim": rinkis(diametrs="30 cm")}],
            ievads="Spied soli pa solim: diametrs aug, garums aug tikpat "
                   "reižu, bet attiecība paliek 3."),

    Paraugs("Cik gara ir riņķa līnija ar rādiusu 5 cm?",
            uzd="Aprēķini aptuveno riņķa līnijas garumu.",
            soli=[
                ("d = 2 · 5 = 10 (cm)",
                 "Vispirms diametrs."),
                ("C apmēram 3 · d",
                 "Sakarība."),
                ("3 · 10 = 30 (cm)",
                 "Aptuvenais garums."),
                ("Vai arī uzreiz: 6 · 5 = 30 (cm)",
                 "Seši rādiusi - tas pats."),
            ],
            atbilde="Apmēram 30 cm"),

    Ievadi("Aprēķini aptuveno garumu", [
        {"jaut": "Diametrs 10 cm. Cik apmēram centimetru ir garums?",
         "atb": ["30"], "padoms": "3 · 10."},
        {"jaut": "Diametrs 7 cm. Cik apmēram centimetru ir garums?",
         "atb": ["21"], "padoms": "3 · 7."},
        {"jaut": "Rādiuss 5 cm. Cik apmēram centimetru ir garums?",
         "atb": ["30"], "padoms": "6 · 5."},
        {"jaut": "Rādiuss 10 cm. Cik apmēram centimetru ir garums?",
         "atb": ["60"], "padoms": "6 · 10."},
        {"jaut": "Garums apmēram 60 cm. Cik apmēram centimetru ir diametrs?",
         "atb": ["20"], "padoms": "60 : 3."},
        {"jaut": "Garums apmēram 90 cm. Cik apmēram centimetru ir rādiuss?",
         "atb": ["15"], "padoms": "90 : 6."},
        {"jaut": "Cik reižu rādiuss ietilpst riņķa līnijā? Ieraksti aptuvenu "
                 "veselu skaitli.",
         "atb": ["6"], "padoms": "Divreiz vairāk nekā diametru."},
        {"jaut": "Cik reižu diametrs ietilpst riņķa līnijā? Ieraksti "
                 "aptuvenu veselu skaitli.",
         "atb": ["3"], "padoms": "No mērījumiem."},
    ], pamats=4,
        ievads="Diametru reizini ar 3, rādiusu - ar 6."),

    Zimejums("Seši rādiusi ap līniju",
             rinkis(radiuss="r", virsraksts="Garums ir apmēram 6 rādiusi"),
             paskaidro="Ja rādiusu atliktu pa riņķa līniju, tas ietilptu "
                       "tajā nedaudz vairāk nekā sešas reizes.",
             ievads="Tā pati sakarība, tikai izteikta ar rādiusu."),

    Varianti("Kāda ir sakarība?", [
        {"jaut": "Riņķa līnijas garums ir apmēram...",
         "opcijas": ["3 diametri", "2 diametri", "4 diametri",
                     "10 diametri"],
         "pareizi": 0,
         "padoms": "No mērījumu tabulas."},
        {"jaut": "Riņķa līnijas garums ir apmēram...",
         "opcijas": ["6 rādiusi", "3 rādiusi", "2 rādiusi", "12 rādiusi"],
         "pareizi": 0,
         "padoms": "Divreiz vairāk nekā diametru."},
        {"jaut": "Vai attiecība mainās, ja riņķa līnija ir lielāka?",
         "opcijas": ["Nemainās", "Kļūst lielāka", "Kļūst mazāka",
                     "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Visiem mērījumiem iznāca tas pats."},
        {"jaut": "Ar kādu burtu apzīmē šo attiecību?",
         "opcijas": ["π", "r", "d", "C"],
         "pareizi": 0,
         "padoms": "Grieķu burts."},
        {"jaut": "Diametrs 12 cm. Cik apmēram ir garums?",
         "opcijas": ["36 cm", "24 cm", "48 cm", "120 cm"],
         "pareizi": 0,
         "padoms": "3 · 12."},
        {"jaut": "Garums 120 cm. Cik apmēram ir diametrs?",
         "opcijas": ["40 cm", "60 cm", "20 cm", "360 cm"],
         "pareizi": 0,
         "padoms": "120 : 3."},
    ], pamats=4),

    Pasaule("Cik tālu aizbrauc ritenis?",
            Ievadi("", [
                {"jaut": "Riteņa diametrs ir 60 cm. Cik apmēram centimetru "
                         "tas nobrauc vienā apgriezienā?",
                 "atb": ["180"], "padoms": "3 · 60."},
                {"jaut": "Cik apmēram centimetru tas nobrauc divos "
                         "apgriezienos?",
                 "atb": ["360"], "padoms": "180 · 2."},
                {"jaut": "Mazāka riteņa rādiuss ir 20 cm. Cik apmēram "
                         "centimetru tas nobrauc vienā apgriezienā?",
                 "atb": ["120"], "padoms": "6 · 20."},
                {"jaut": "Ritenis nobrauca 90 cm vienā apgriezienā. Cik "
                         "apmēram centimetru ir tā diametrs?",
                 "atb": ["30"], "padoms": "90 : 3."},
            ]),
            pavediens="maja",
            konteksts="Katrs riteņa apgrieziens nobrauc tieši tik, cik gara "
                      "ir tā riņķa līnija.",
            kapec="Tāpēc lielāks ritenis ar vienu apgriezienu tiek tālāk."),

    Kopsavilkums([
        "Formulēju, ka riņķa līnijas garums ir apmēram trīs diametri.",
        "Zinu, ka tas ir apmēram seši rādiusi.",
        "Aprēķinu aptuveno garumu no rādiusa vai diametra.",
        "Zinu, ka šī attiecība ir viena visām riņķa līnijām.",
    ]),

    Majas([
        "Aprēķini aptuveno garumu riņķa līnijām ar rādiusiem 3 cm un 8 cm.",
        "Izmēri riteņa diametru un aprēķini, cik tas nobrauc apgriezienā.",
        "Uzraksti, kāpēc attiecība nav atkarīga no riņķa lieluma.",
    ]),
]
