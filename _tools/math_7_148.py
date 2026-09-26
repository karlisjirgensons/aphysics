# -*- coding: utf-8 -*-
"""7. klase, 148. stunda: «Kā vienādojums apraksta figūru?»

Ģeometrijā vienādojums rodas no figūras īpašības: perimetrs, leņķu summa,
vienādas malas. Stunda apvieno ģeometriju un algebru - tā ir biežākā
kombinācija eksāmenā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, geometrija)

TEMA = "Kā vienādojums apraksta figūru?"

MERKIS = ("Aprakstīsim ar lineāru vienādojumu sakarības starp figūras "
          "lielumiem un atrisināsim to.")

SATURS = [
    Sakums("Leņķi x, 2x un 3x",
           zimejums=geometrija([("A", 0, 0), ("B", 6, 0), ("C", 1.5, 2.6)],
                               nogriezni=["AB", "BC", "CA"],
                               lenki=[("BAC", "2x"), ("CBA", "x"),
                                      ("ACB", "3x")]),
           paraksts="x + 2x + 3x = 180°.",
           fakti=["Īpašība (leņķu summa) dod vienādojumu.",
                  "6x = 180°, x = 30°.",
                  "Leņķi: 30°, 60°, 90°."]),

    Doma("Īpašība → vienādojums",
         "Ģeometriskā uzdevumā vienādojumu iegūst no figūras īpašības: "
         "perimetrs (malu summa), leņķu summa (180°, blakusleņķi 180°), "
         "vienādsānu trijstūra vienādas malas vai leņķi.",
         soli=[
             "Izsaki figūras elementus ar x.",
             "Atrodi īpašību, kas tos saista.",
             "Uzraksti vienādojumu un atrisini.",
             "Aprēķini visus elementus un pārbaudi.",
         ]),

    Paraugs("Vienādsānu trijstūris",
            uzd="Vienādsānu trijstūra sānu mala par 3 cm garāka nekā pamats, "
                "perimetrs 30 cm. Atrodi malas.",
            soli=[
                ("Pamats x, sāni x + 3", "Izsaka."),
                ("x + 2(x + 3) = 30", "(perimetrs)"),
                ("3x + 6 = 30, x = 8", "Atrisina."),
                ("8, 11, 11 cm; 11 + 8 > 11 ✓", "Pārbaude."),
            ],
            atbilde="Pamats 8 cm, sāni 11 cm."),

    Ievadi("Atrisini", [
        {"jaut": "Blakusleņķi x un x + 40°. x (°)?",
         "atb": ["70"], "padoms": "2x + 40 = 180."},
        {"jaut": "Taisnstūra garums 3 reizes lielāks par platumu, P = 48 cm. "
                 "Platums (cm)?",
         "atb": ["6"], "padoms": "2(x + 3x) = 48."},
        {"jaut": "Trijstūra leņķi x, x + 10°, x + 20°. Lielākais (°)?",
         "atb": ["70"], "padoms": "3x + 30 = 180, x = 50."},
        {"jaut": "Kvadrāta mala x + 2, perimetrs 36. x = ?",
         "atb": ["7"], "padoms": "4(x + 2) = 36."},
    ]),

    Varianti("Kura īpašība dod vienādojumu?", [
        {"jaut": "Krustleņķi 3x − 10 un 2x + 20.",
         "opcijas": ["Krustleņķi vienādi: 3x − 10 = 2x + 20",
                     "Summa 180°", "Summa 90°", "Nevar"],
         "pareizi": 0, "padoms": "x = 30."},
        {"jaut": "Vienpusleņķi pie paralēlām: x un 2x.",
         "opcijas": ["x + 2x = 180°", "x = 2x", "x + 2x = 90°",
                     "x + 2x = 360°"],
         "pareizi": 0, "padoms": "Summa 180°."},
    ]),

    Pasaule("Žoga plāns",
            Ievadi("", [
                {"jaut": "Taisnstūra dārza garums par 6 m lielāks nekā platums, "
                         "žogs 60 m. Platums (m)?",
                 "atb": ["12"], "padoms": "2(2x + 6) = 60."},
                {"jaut": "Garums (m)?",
                 "atb": ["18"], "padoms": "12 + 6."},
                {"jaut": "Laukums (m²)?",
                 "atb": ["216"], "padoms": "12 · 18."},
            ]),
            pavediens="maja",
            konteksts="Pērkot žogu, zina kopgarumu - vienādojums dod dārza "
                      "izmērus.",
            kapec="Perimetrs → vienādojums → malas."),

    Kopsavilkums([
        "Izsaku figūras elementus ar x.",
        "Izmantoju īpašību, lai uzrakstītu vienādojumu.",
        "Atrisinu un aprēķinu visus elementus.",
        "Pārbaudu ar trijstūra nevienādību vai leņķu summu.",
    ]),

    Majas([
        "Trijstūra leņķi attiecas 2 : 3 : 7 - atrisini ar vienādojumu.",
        "Izdomā perimetra uzdevumu ar x.",
        "Atrisini: krustleņķi 5x − 20 un 3x + 30.",
    ]),
]
