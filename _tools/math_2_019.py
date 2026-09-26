# -*- coding: utf-8 -*-
"""2. klase, 19. stunda: «Kā pierakstīt visus mērījumus?»

Kad mēra vairāki cilvēki vai vairākas lietas, rezultātus liek tabulā: katrai
lietai rinda, katram lielumam kolonna. Tabulā uzreiz redz lielāko, mazāko
un starpību.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, restis)

TEMA = "Kā pierakstīt visus mērījumus?"

MERKIS = ("Šodien izveidosim tabulu mērījumiem, ierakstīsim tajā grupas "
          "datus un lasīsim no tās.")

_TABULA = restis([["priekšmets", "garums"],
                  ["zīmulis", "17 cm"],
                  ["burtnīca", "21 cm"],
                  ["penālis", "20 cm"],
                  ["dzēšgumija", "4 cm"]])

_AUGUMI = restis([["vārds", "augums"],
                  ["Anna", "1 m 24 cm"],
                  ["Mārtiņš", "1 m 31 cm"],
                  ["Līva", "1 m 27 cm"]])

SATURS = [
    Sakums("Kā atcerēties 20 mērījumus un nesajaukt?",
           zimejums=_TABULA,
           paraksts="Tabulā katram priekšmetam ir sava rinda.",
           fakti=["Tabulas pirmajā rindā raksta, kas ir kolonnās.",
                  "Pie skaitļa vienmēr raksta mērvienību."]),

    Doma("Mērījumu tabula",
         "Tabulā katram mērījumam ir sava vieta - to nevar pazaudēt.",
         soli=[
             "Pirmajā rindā uzraksti kolonnu nosaukumus.",
             "Katrai lietai ieraksti savu rindu.",
             "Pie skaitļa pieraksti mērvienību.",
             "Pēc tam salīdzini: kas garākais, kas īsākais?",
         ]),

    Ievadi("Lasi tabulu", [
        {"jaut": "Cik gara ir burtnīca?", "zim": _TABULA, "atb": ["21"],
         "mers": "cm", "padoms": "Atrodi rindu «burtnīca»."},
        {"jaut": "Par cik cm penālis ir garāks nekā zīmulis?",
         "zim": _TABULA, "atb": ["3"], "mers": "cm", "padoms": "20 − 17."},
        {"jaut": "Par cik cm burtnīca ir garāka nekā dzēšgumija?",
         "zim": _TABULA, "atb": ["17"], "mers": "cm", "padoms": "21 − 4."},
        {"jaut": "Cik cm ir zīmulis un dzēšgumija kopā, noliktas vienā "
                 "rindā?", "zim": _TABULA, "atb": ["21"], "mers": "cm",
         "padoms": "17 + 4."},
    ]),

    Varianti("Kurš?", [
        {"jaut": "Kurš priekšmets ir visgarākais?", "zim": _TABULA,
         "opcijas": ["burtnīca", "penālis", "zīmulis"], "pareizi": 0,
         "padoms": "Lielākais skaitlis."},
        {"jaut": "Kurš bērns ir visgarākais?", "zim": _AUGUMI,
         "opcijas": ["Mārtiņš", "Līva", "Anna"], "pareizi": 0,
         "padoms": "Lielākais skaitlis."},
        {"jaut": "Kura rinda pareizi pieraksta mērījumu?",
         "opcijas": ["galds - 75 cm", "galds - 75", "75 cm - "],
         "pareizi": 0, "padoms": "Vajag gan lietu, gan mērvienību."},
        {"jaut": "Kurš bērns ir par 3 cm garāks nekā Anna?",
         "zim": _AUGUMI, "opcijas": ["Līva", "Mārtiņš", "neviens"],
         "pareizi": 0, "padoms": "24 + 3."},
    ]),

    Petijums("Mūsu grupas tabula", [
        "Grupā izvēlieties 4 priekšmetus uz galda.",
        "Uzzīmējiet tabulu: «priekšmets» un «garums».",
        "Katrs izmēra vienu priekšmetu un ieraksta rezultātu.",
        "Sakārtojiet no garākā līdz īsākajam.",
    ], vajag="lineāls, lapa, zīmulis"),

    Pasaule("Kurš izaudzis visvairāk?",
            Ievadi("", [
                {"jaut": "Septembrī Anna bija 1 m 24 cm, maijā - 1 m 28 cm. Par "
                         "cik viņa izauga?", "atb": ["4"], "mers": "cm",
                 "padoms": "28 − 24."},
                {"jaut": "Mārtiņš bija 1 m 31 cm un izauga par 5 cm. Cik "
                         "cm virs 1 m viņš ir tagad?", "atb": ["36"],
                 "mers": "cm", "padoms": "31 + 5."},
            ]),
            pavediens="skola",
            konteksts="Skolas māsa katru gadu ieraksta augumu tabulā.",
            kapec="Tabula ļauj salīdzināt mērījumus pēc vairākiem "
                  "mēnešiem."),

    Kopsavilkums([
        "Izveidoju tabulu mērījumiem.",
        "Ierakstu mērījumus ar mērvienību.",
        "Nolasu no tabulas garāko, īsāko un starpību.",
    ]),

    Majas([
        "Izmēri 4 mājinieku plaukstas garumu.",
        "Ieraksti rezultātus tabulā.",
        "Kuram plauksta garākā? Par cik garāka nekā tavējā?",
    ]),
]
