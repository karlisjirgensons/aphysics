# -*- coding: utf-8 -*-
"""8. klase, 78. stunda: «Kāds ķermenis tas ir?»

Ķermeni nosaka pēc skatiem: priekšskats, virsskats, sānskats. Viens skats
parasti neatklāj ķermeni (riņķis der cilindram, konusam un lodei), divi
vai trīs skati kopā - atklāj. Slīdnis min ķermeni soli pa solim.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, geometrija, kermenis, rinkis)

TEMA = "Kāds ķermenis tas ir?"

MERKIS = "Noteiksim iespējamo telpisko ķermeni pēc dažiem tā skatiem."

_TAISNSTURIS = geometrija([("_a", 0, 0), ("_b", 4, 0), ("_c", 4, 5),
                           ("_d", 0, 5)],
                          nogriezni=[("_a", "_b"), ("_b", "_c"),
                                     ("_c", "_d"), ("_d", "_a")],
                          iekrasot=[(["_a", "_b", "_c", "_d"], 0)])
_TRIJSTURIS = geometrija([("_a", 0, 0), ("_b", 4, 0), ("_c", 2, 5)],
                         nogriezni=[("_a", "_b"), ("_b", "_c"),
                                    ("_c", "_a")],
                         iekrasot=[(["_a", "_b", "_c"], 0)])

SATURS = [
    Sakums("No augšas redzams riņķis. Kas tas ir?",
           zimejums=rinkis(),
           paraksts="Virsskats - riņķis. Tas var būt cilindrs, konuss vai "
                    "lode.",
           fakti=["Priekšskats, virsskats un sānskats rāda ķermeni no trim "
                  "pusēm.",
                  "Viens skats bieži neatklāj ķermeni.",
                  "Divi vai trīs skati kopā ķermeni nosaka."]),

    Doma("Kā lasīt skatus",
         "Katrs skats izslēdz daļu ķermeņu; paliek tas, kam der visi skati.",
         soli=[
             "Salīdzini skatu formas: taisnstūris, trijstūris, riņķis.",
             "Riņķis kādā skatā nozīmē apaļu ķermeni.",
             "Trijstūris priekšā un taisnstūris augšā - guļus trijstūra "
             "prizma.",
             "Pārbaudi, vai izvēlētajam ķermenim der visi skati.",
         ]),

    Slidnis("Atmini ķermeni", [
        {"v": "Priekšskats", "teksts": "Taisnstūris: kvadrs, cilindrs vai "
                                       "prizma?",
         "zim": _TAISNSTURIS},
        {"v": "Virsskats", "teksts": "Riņķis - tātad apaļš",
         "zim": rinkis()},
        {"v": "Cilindrs", "teksts": "Abiem skatiem der tikai cilindrs",
         "zim": kermenis("cilindrs")},
        {"v": "Cits priekšskats", "teksts": "Trijstūris, virsskats - riņķis",
         "zim": _TRIJSTURIS},
        {"v": "Konuss", "teksts": "Trijstūris un riņķis - konuss",
         "zim": kermenis("konuss")},
    ]),

    Varianti("Kurš ķermenis?", [
        {"jaut": "Priekšskats - taisnstūris, virsskats - riņķis.",
         "opcijas": ["Cilindrs", "Konuss", "Kvadrs", "Lode"],
         "pareizi": 0, "padoms": "Skaties slīdni."},
        {"jaut": "Priekšskats - trijstūris, virsskats un sānskats - "
                 "taisnstūri.",
         "opcijas": ["Trijstūra prizma", "Piramīda", "Konuss", "Kubs"],
         "pareizi": 0, "padoms": "Guļus prizma."},
        {"jaut": "Visi trīs skati - vienādi kvadrāti.",
         "opcijas": ["Kubs", "Kvadrs", "Cilindrs", "Lode"],
         "pareizi": 0, "padoms": "Visas šķautnes vienādas."},
        {"jaut": "Visi trīs skati - vienādi riņķi.",
         "opcijas": ["Lode", "Cilindrs", "Konuss", "Kubs"],
         "pareizi": 0, "padoms": "No jebkuras puses apaļa."},
        {"jaut": "Priekšskats - trijstūris, virsskats - kvadrāts ar "
                 "diagonālēm.",
         "opcijas": ["Četrstūra piramīda", "Konuss", "Prizma", "Kubs"],
         "pareizi": 0, "padoms": "Diagonāles ir sānu šķautnes."},
    ]),

    Ievadi("Nolasi izmērus", [
        {"jaut": "Cilindra priekšskats: platums 6 cm, augstums 10 cm. "
                 "Pamata rādiuss (cm)?", "atb": ["3"],
         "padoms": "Platums = diametrs."},
        {"jaut": "Tā paša cilindra augstums (cm)?", "atb": ["10"],
         "padoms": "Priekšskata augstums."},
        {"jaut": "Kuba virsskata laukums ir 16 cm². Šķautne (cm)?",
         "atb": ["4"], "padoms": "√16."},
        {"jaut": "Kvadrs: priekšskats 5 × 3, virsskats 5 × 2. Tilpums?",
         "atb": ["30"], "padoms": "5 · 3 · 2."},
    ]),

    Pasaule("Detaļas rasējums",
            Ievadi("", [
                {"jaut": "Priekšskats - taisnstūris 20 cm × 30 cm (platums × "
                         "augstums), virsskats - riņķis ar d = 20 cm. Kāds "
                         "ķermenis?",
                 "atb": ["cilindrs"], "tastatura": "text",
                 "padoms": "Taisnstūris un riņķis."},
                {"jaut": "Detaļas augstums (cm)?", "atb": ["30"],
                 "padoms": "Priekšskata augstums."},
                {"jaut": "Pamata rādiuss (cm)?", "atb": ["10"],
                 "padoms": "{20|2}."},
            ]),
            pavediens="tehnika",
            konteksts="Inženieri detaļas rasē skatos - no priekšas, no augšas "
                      "un no sāna.",
            kapec="Divi skati kopā nosaka formu, ko viens skats nevar."),

    Kopsavilkums([
        "Nosaku ķermeni pēc diviem vai trim skatiem.",
        "Zinu, ka viens skats var derēt vairākiem ķermeņiem.",
        "Nolasu izmērus no skatiem.",
    ]),

    Majas([
        "Uzzīmē krūzes priekšskatu, virsskatu un sānskatu.",
        "Kurš ķermenis no augšas izskatās kā riņķis, bet no priekšas - kā "
        "kvadrāts?",
        "Uzzīmē skatus ķermenim no LEGO klucīšiem.",
    ]),
]
