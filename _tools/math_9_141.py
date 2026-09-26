# -*- coding: utf-8 -*-
"""9. klase, 141. stunda: «Kā to risinātu eksāmenā?»

Virknes un progresija eksāmenā: 1. daļas 5. uzdevums (d un a_4 no
teksta), formulas no formulu lapas un 2. daļas figūru virkne ar summu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, restis)

TEMA = "Kā to risinātu eksāmenā?"

MERKIS = ("Risināsim eksāmena formāta uzdevumus par virknēm un progresiju.")

SATURS = [
    Sakums("Trīs formulas no formulu lapas",
           zimejums=restis([["ko meklē", "formula"],
                            ["n-to locekli", "a₁ + (n − 1)d"],
                            ["summu", "(a₁ + aₙ)n : 2"],
                            ["vidējo", "(aₖ₋₁ + aₖ₊₁) : 2"]]),
           paraksts="Formulas ir dotas - jāprot izvēlēties.",
           fakti=["Nosaki a_1 un d no teksta vai figūrām.",
                  "Loceklis vai summa? - izlasi jautājumu.",
                  "Pārbaudi ar pirmajiem locekļiem."]),

    Doma("Eksāmena algoritms",
         "Teksts → a_1 un d → formula → aprēķins → pārbaude ar pirmajiem "
         "locekļiem.",
         soli=[
             "Izraksti 3-4 pirmos locekļus (arī no zīmējuma).",
             "Pārliecinies, ka starpības vienādas.",
             "Pieraksti formulu ar skaitļiem.",
             "Atbildi uz jautājumu ar vārdiem.",
         ]),

    Paraugs("Eksāmens 2025, 5. uzdevums",
            uzd="Aritmētiskās progresijas a_1 = 3, katrs nākamais par 2 "
                "lielāks. Nosaki d un a_4.",
            soli=[
                ("d = 2", "«Par 2 lielāks»."),
                ("a_4 = 3 + 3 · 2 = 9", "a_1 + (4 − 1)d."),
            ],
            atbilde="d = 2; a_4 = 9"),

    Ievadi("1. daļa", [
        {"jaut": "a_1 = −5, d = 4. a_6 = ?", "atb": ["15"],
         "padoms": "−5 + 20."},
        {"jaut": "12, 9, 6, ... d = ?", "atb": ["−3", "-3"],
         "padoms": "9 − 12."},
        {"jaut": "a_1 = 2, a_{10} = 29. S_{10} = ?", "atb": ["155"],
         "padoms": "{31 · 10|2}."},
        {"jaut": "a_3 = 8, a_5 = 14. a_4 = ?", "atb": ["11"],
         "padoms": "Vidējais."},
    ]),

    Varianti("Atbilžu izvēle", [
        {"jaut": "Kura virkne ir aritmētiskā progresija?",
         "opcijas": ["−3; 1; 5; 9", "1; 2; 4; 8", "1; 4; 9; 16",
                     "2; 3; 5; 8"],
         "pareizi": 0, "padoms": "Starpība 4."},
        {"jaut": "a_n = 5n − 3. a_{10} = ?",
         "opcijas": ["47", "50", "53", "44"],
         "pareizi": 0, "padoms": "50 − 3."},
    ]),

    Pasaule("2. daļa: figūru virkne",
            Ievadi("", [
                {"jaut": "No kvadrātiņiem veido «L» figūras: 3, 5, 7, ... "
                         "kvadrātiņi. Cik kvadrātiņu 20. figūrā?",
                 "atb": ["41"], "padoms": "3 + 19 · 2."},
                {"jaut": "Cik kvadrātiņu vajag visām 20 figūrām kopā?",
                 "atb": ["440"], "padoms": "{(3 + 41) · 20|2}."},
                {"jaut": "Kura figūra ir pirmā ar vairāk nekā 100 "
                         "kvadrātiņiem? n = ?", "atb": ["50"],
                 "padoms": "2n + 1 > 100 ⇒ n ≥ 50."},
            ]),
            pavediens="speles",
            konteksts="Eksāmena 2. daļā bieži ir zīmēta figūru virkne - "
                      "jāsaskata progresija.",
            kapec="Pierakstot pirmos locekļus, uzdevums kļūst par formulu."),

    Kopsavilkums([
        "Izvēlos pareizo progresijas formulu.",
        "Nolasu a_1 un d no teksta vai zīmējuma.",
        "Noformēju atbildi eksāmena stilā.",
    ]),

    Majas([
        "Atkārto 9.7. tematu - nākamajā stundā pārbaudes darbs.",
        "a_2 = 7, a_6 = 27. Atrodi S_{10}.",
        "Uzzīmē savu figūru virkni un uzraksti formulu.",
    ]),
]
