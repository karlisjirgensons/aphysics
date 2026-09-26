# -*- coding: utf-8 -*-
"""9. klase, 28. stunda: «Kā aprēķināt pamatu?»

Formula m = {a + b|2} ir vienādojums ar trim lielumiem: no jebkuriem diviem
iegūst trešo. Uzdevumos arī attiecības (a : b = 3 : 2) un perimetrs.
"""

from math_saturs import (TRAPECES_MALAS, Doma, Ievadi, Kopsavilkums, Kustiba,
                         Majas, Paraugs, Pasaule, Sakums, Varianti,
                         geometrija, trapece)

TEMA = "Kā aprēķināt pamatu?"

MERKIS = ("Aprēķināsim trapeces pamatu vai viduslīniju, ja pārējie lielumi "
          "zināmi.")

SATURS = [
    Sakums("Viduslīnija 9, augšā 5. Cik apakšā?",
           zimejums=geometrija(trapece(10, 5, 4, nobide=2, viduspunkti=True),
                               nogriezni=TRAPECES_MALAS, izcelti=["MN"],
                               malas=[("DC", "5"), ("MN", "9"),
                                      ("AB", "?")]),
           paraksts="{a + 5|2} = 9 - vienādojums.",
           fakti=["No m = {a + b|2} izriet a = 2m − b.",
                  "Viduslīnija ir tikpat tālu no abiem pamatiem.",
                  "Pārbaude: m jābūt starp a un b."]),

    Doma("Trīs lielumi, viena formula",
         "m = {a + b|2} ⇔ a + b = 2m ⇔ a = 2m − b.",
         soli=[
             "Pieraksti formulu.",
             "Ievieto zināmos.",
             "Atrisini vienādojumu.",
             "Pārbaudi: vai b < m < a?",
         ]),

    Paraugs("Pamati attiecībā",
            uzd="Trapeces viduslīnija ir 15 cm, pamati attiecas kā 2 : 3. "
                "Atrodi pamatus.",
            soli=[
                ("a + b = 2 · 15 = 30", "Pamatu summa."),
                ("b = 2x, a = 3x; 5x = 30; x = 6", "Attiecība."),
                ("b = 12, a = 18", "Pārbaude: (18 + 12) : 2 = 15."),
            ],
            atbilde="12 cm un 18 cm"),

    Kustiba("Aizbrauc līdz pamatam", [
        {"jaut": "m = 8, b = 5. Apakšējais pamats a = ?",
         "atb": 11, "beigas": 20, "iedala": 2, "mers": "cm",
         "merkis": "a", "objekts": "Lineāls",
         "padoms": "2 · 8 − 5."},
        {"jaut": "m = 12, a = 17. Augšējais pamats b = ?",
         "atb": 7, "beigas": 20, "iedala": 2, "mers": "cm",
         "merkis": "b", "objekts": "Lineāls",
         "padoms": "24 − 17."},
    ]),

    Ievadi("Aprēķini", [
        {"jaut": "a = 13, b = 7. m = ?", "atb": ["10"],
         "padoms": "20 : 2."},
        {"jaut": "m = 6,5, a = 9. b = ?", "atb": ["4"],
         "padoms": "13 − 9."},
        {"jaut": "m = 10, a − b = 6. a = ?", "atb": ["13"],
         "padoms": "a + b = 20."},
        {"jaut": "Vienādsānu: m = 9, sānu mala 5. Perimetrs?", "atb": ["28"],
         "padoms": "a + b = 18."},
        {"jaut": "Perimetrs 40, sānu malas 7 un 9. m = ?", "atb": ["12"],
         "padoms": "a + b = 24."},
        {"jaut": "a = 3b, m = 16. b = ?", "atb": ["8"],
         "padoms": "4b = 32."},
    ], pamats=4),

    Varianti("Vai tā var būt?", [
        {"jaut": "a = 10, b = 4, m = 8.",
         "opcijas": ["Nē, m = 7", "Jā", "Jā, ja trapece vienādsānu",
                     "Nevar zināt"],
         "pareizi": 0, "padoms": "(10 + 4) : 2."},
        {"jaut": "m = 5, a = 12. b = ?",
         "opcijas": ["Negatīvs - tādas trapeces nav", "2", "7", "17"],
         "pareizi": 0, "padoms": "10 − 12 = −2."},
    ]),

    Pasaule("Dārza terases",
            Ievadi("", [
                {"jaut": "Nogāzes terase - trapece; apakšējā mala 14 m, vidējā "
                         "(viduslīnija) 11 m. Augšējā mala (m)?",
                 "atb": ["8"], "padoms": "22 − 14."},
                {"jaut": "Apmales akmeņi gar vidējo līniju ik pēc 0,5 m. Cik "
                         "akmeņu (ieskaitot galus)?", "atb": ["23"],
                 "padoms": "11 : 0,5 = 22 posmi."},
            ]),
            pavediens="maja",
            konteksts="Terasētā dārzā dobes sašaurinās uz augšu - katra ir "
                      "trapece.",
            kapec="Pietiek izmērīt divas līnijas, trešo aprēķina."),

    Kopsavilkums([
        "No m = {a + b|2} izsaku jebkuru lielumu.",
        "Risinu uzdevumus ar pamatu attiecību vai starpību.",
        "Pārbaudu, vai rezultāts ir iespējams.",
    ]),

    Majas([
        "m = 14, pamatu starpība 8. Atrodi pamatus.",
        "Viduslīnija 12, pamati attiecas kā 1 : 5. Atrodi pamatus.",
        "Izdomā uzdevumu, kurā pamats iznāk negatīvs, un paskaidro, kāpēc.",
    ]),
]
