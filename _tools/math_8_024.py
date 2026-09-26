# -*- coding: utf-8 -*-
"""8. klase, 24. stunda: «Ko nozīmē negatīvs kāpinātājs?»

Virkni no iepriekšējās stundas turpina pāri nullei: 2^0 = 1, 2^{−1} = {1|2},
2^{−2} = {1|4}. Negatīvs kāpinātājs nozīmē apgriezto skaitli, nevis
negatīvu vērtību - tā ir biežākā kļūda.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, restis)

TEMA = "Ko nozīmē negatīvs kāpinātājs?"

MERKIS = ("Sapratīsim pakāpi ar negatīvu kāpinātāju kā apgriezto skaitli.")

SATURS = [
    Sakums("Turpini virkni pāri nullei",
           zimejums=restis([["2²", "2¹", "2⁰", "2⁻¹", "2⁻²"],
                            ["4", "2", "1", "1/2", "1/4"]]),
           paraksts="Katrs solis pa labi - joprojām dala ar 2.",
           fakti=["1 : 2 = {1|2}, tātad 2⁻¹ = {1|2}.",
                  "{1|2} : 2 = {1|4}, tātad 2⁻² = {1|4}.",
                  "Negatīvs kāpinātājs - vērtība joprojām pozitīva."]),

    Slidnis("Tālāk par nulli", [
        {"v": "2^0 = 1", "teksts": "Tur apstājāmies"},
        {"v": "2^−1 = {1|2}", "teksts": "1 : 2"},
        {"v": "2^−2 = {1|4} = {1|2^2}", "teksts": "{1|2} : 2"},
        {"v": "2^−3 = {1|8} = {1|2^3}", "teksts": "{1|4} : 2"},
        {"v": "a^−n = {1|a^n}", "teksts": "Apgrieztais skaitlis pakāpei a^n"},
    ]),

    Doma("Negatīvs kāpinātājs - apgrieztais skaitlis",
         "Ja a ≠ 0 un n ir naturāls skaitlis, tad a^−n = {1|a^n}. Mīnuss "
         "kāpinātājā nozīmē «viens dalīts ar», nevis «negatīvs».",
         soli=[
             "Pārraksti kā daļu: 1 skaitītājā, a^n saucējā.",
             "Aprēķini a^n.",
             "Rezultāts ir pozitīvs, ja a > 0.",
             "Tas saskan ar dalīšanu: {a^2|a^5} = a^{2 − 5} = a^−3.",
         ],
         pieze="10^−3 = {1|1000} = 0,001 - tā ir «mili-»: 1 mm = 10^−3 m."),

    Paraugs("Aprēķini",
            uzd="Aprēķini 5^−2, 10^−4 un (−2)^−3.",
            soli=[
                ("5^−2 = {1|5^2} = {1|25} = 0,04", "Apgrieztais."),
                ("10^−4 = {1|10 000} = 0,0001", "4 cipari aiz komata."),
                ("(−2)^−3 = {1|(−2)^3} = −{1|8}", "Nepāra - mīnuss."),
            ],
            atbilde="0,04; 0,0001; −{1|8}"),

    Ievadi("Aprēķini", [
        {"jaut": "3^−2 - atbildi raksti kā a/b",
         "atb": ["{1|9}", "1/9"], "padoms": "{1|3^2}."},
        {"jaut": "10^−2 - decimāldaļā",
         "atb": ["0,01", "0.01"], "padoms": "{1|100}."},
        {"jaut": "4^−1 - decimāldaļā",
         "atb": ["0,25", "0.25"], "padoms": "{1|4}."},
        {"jaut": "2^−5 - atbildi raksti kā a/b",
         "atb": ["{1|32}", "1/32"], "padoms": "2^5 = 32."},
        {"jaut": "9^−2 - atbildi raksti kā a/b",
         "atb": ["{1|81}", "1/81"], "padoms": "Eksāmena uzdevums."},
        {"jaut": "(−5)^−1 - decimāldaļā",
         "atb": ["−0,2", "-0,2", "-0.2"], "padoms": "{1|−5}."},
    ], pamats=4),

    Varianti("Kas ir 2^−3?", [
        {"jaut": "2^−3 =",
         "opcijas": ["{1|8}", "−8", "−6", "8"],
         "pareizi": 0, "padoms": "Apgrieztais, ne negatīvais."},
        {"jaut": "Kurš skaitlis ir lielāks: 10^−2 vai 10^−3?",
         "opcijas": ["10^−2", "10^−3", "Vienādi", "Nevar salīdzināt"],
         "pareizi": 0, "padoms": "0,01 > 0,001."},
        {"jaut": "x^−1 =",
         "opcijas": ["{1|x}", "−x", "x − 1", "−{1|x}"],
         "pareizi": 0, "padoms": "Apgrieztais x."},
    ]),

    Pasaule("Mazie izmēri",
            Ievadi("", [
                {"jaut": "Mikrometrs ir 10^−6 m. Cik tas ir milimetros? "
                         "(1 mm = 10^−3 m)",
                 "atb": ["0,001", "0.001"], "padoms": "10^−6 : 10^−3 = 10^−3."},
                {"jaut": "Mata biezums ir ap 70 mikrometriem. Cik mm?",
                 "atb": ["0,07", "0.07"], "padoms": "70 · 0,001."},
                {"jaut": "Baktērija ir 2 · 10^−6 m gara. Cik baktēriju "
                         "ietilpst 1 mm rindā?",
                 "atb": ["500"], "padoms": "10^−3 : (2 · 10^−6)."},
            ]),
            pavediens="daba",
            konteksts="Mikroskopā redzamo pasauli mēra ar negatīvām desmit "
                      "pakāpēm: mili- (10^−3), mikro- (10^−6), nano- (10^−9).",
            kapec="Negatīvs kāpinātājs ir īss pieraksts ļoti mazam skaitlim."),

    Kopsavilkums([
        "Zinu, ka a^−n = {1|a^n}.",
        "Aprēķinu pakāpi ar negatīvu kāpinātāju.",
        "Nejaucu negatīvu kāpinātāju ar negatīvu vērtību.",
    ]),

    Majas([
        "Uzraksti virkni 10^3, 10^2, ..., 10^−3 ar vērtībām.",
        "Aprēķini 2^−4, 5^−3, (−3)^−2.",
        "Atrodi, ko nozīmē priedēklis «nano-» un pieraksti to kā 10 pakāpi.",
    ]),
]
