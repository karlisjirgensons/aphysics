# -*- coding: utf-8 -*-
"""4. klase, 147. stunda: «Cik liels ir šis galds?»

Mikrotemata noslēgums. Aptuvens novērtējums: galds apmēram 120 cm × 60 cm,
tātad ap 7200 cm² jeb ap 72 dm². Skolēns novērtē, tad izmēra un salīdzina
- tā viņš iegūst «laukuma izjūtu» dažādās vienībās.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, restis)

TEMA = "Cik liels ir šis galds?"

MERKIS = ("Aptuveni novērtēsim taisnstūrveida virsmas laukumu un "
          "pārbaudīsim aprēķinu.")

SATURS = [
    Sakums("Novērtē, tad izmēri!",
           zimejums=restis([["virsma", "novērtējums", "mērījums"],
                            ["galds", "ap 70 dm²", "120 × 60 = 72 dm²"],
                            ["grāmata", "ap 5 dm²", "20 × 25 = 5 dm²"],
                            ["logs", "ap 2 m²", "150 × 120 = 1,8 m²"]],
                           "novērtējums un mērījums"),
           fakti=["Labs novērtējums ir tuvu mērījumam.",
                  "Svarīgākais - pareiza vienība."]),

    Doma("Noapaļo malas, sareizini, pārbaudi",
         "Laukumu novērtē, noapaļojot malas līdz ērtiem skaitļiem un "
         "sareizinot tos galvā.",
         soli=[
             "Izvēlies vienību: mazam - cm², vidējam - dm², lielam - m².",
             "Noapaļo malas: 118 cm ≈ 120 cm, 59 cm ≈ 60 cm.",
             "Sareizini: 12 dm · 6 dm = 72 dm².",
             "Izmēri precīzi un salīdzini.",
         ],
         pieze="Galdam ērtāk rēķināt decimetros: 12 · 6 = 72, nevis "
               "120 · 60 = 7200."),

    Petijums("Klases virsmas",
             soli=[
                 "Izvēlies 3 virsmas: galds, grāmata, logs.",
                 "Katrai novērtē laukumu un pieraksti.",
                 "Izmēri malas un aprēķini precīzi.",
                 "Aprēķini, par cik novērtējums atšķīrās.",
             ],
             vajag="mērlente vai lineāls",
             secinajums="Jo vairāk novērtē, jo precīzāka kļūst acs."),

    Ievadi("Novērtē un aprēķini", [
        {"jaut": "Galds 12 dm × 6 dm. Laukums dm²?", "atb": ["72"],
         "padoms": "12 · 6."},
        {"jaut": "Grāmata 2 dm × 3 dm. Laukums dm²?", "atb": ["6"],
         "padoms": "2 · 3."},
        {"jaut": "Paklājs 3 m × 2 m. Laukums m²?", "atb": ["6"],
         "padoms": "3 · 2."},
        {"jaut": "Planšete 25 cm × 16 cm. Laukums cm²?", "atb": ["400"],
         "padoms": "25 · 16."},
    ]),

    Varianti("Kura vienība der?", [
        {"jaut": "Pastmarka",
         "opcijas": ["cm²", "m²", "ha"], "pareizi": 0,
         "padoms": "Maza virsma."},
        {"jaut": "Grāmatas vāks",
         "opcijas": ["dm² vai cm²", "ha", "km²"], "pareizi": 0,
         "padoms": "Vidēja virsma."},
        {"jaut": "Basketbola laukums",
         "opcijas": ["m²", "cm²", "mm²"], "pareizi": 0,
         "padoms": "Liela virsma."},
    ]),

    Pasaule("Jauna rakstāmgalda izvēle",
            Ievadi("", [
                {"jaut": "Galds A: 10 dm × 6 dm. Laukums dm²?", "atb": ["60"],
                 "padoms": "10 · 6."},
                {"jaut": "Galds B: 12 dm × 5 dm. Laukums dm²?", "atb": ["60"],
                 "padoms": "12 · 5."},
                {"jaut": "Galds C: 14 dm × 5 dm. Laukums dm²?", "atb": ["70"],
                 "padoms": "14 · 5."},
                {"jaut": "Istabā vieta galdam 13 dm garumā. Kura galda "
                         "laukums lielākais no derīgajiem (A vai B)? Ieraksti "
                         "laukumu.",
                 "atb": ["60"], "padoms": "C ir 14 dm - neder; A un B pa 60."},
            ]),
            pavediens="maja",
            konteksts="Pērkot mēbeles, jāņem vērā gan laukums, gan tas, vai "
                      "tā ietilps istabā.",
            kapec="Laukums pasaka, cik vietas darbam; garums - vai ietilps."),

    Kopsavilkums([
        "Novērtēju virsmas laukumu aptuveni.",
        "Izvēlos piemērotu vienību.",
        "Pārbaudu novērtējumu ar mērījumu.",
    ]),

    Majas([
        "Novērtē un izmēri 3 virsmas mājās.",
        "Atrodi virsmu ar laukumu ap 1 m².",
        "Salīdzini savu novērtējumu ar mājinieka novērtējumu.",
    ]),
]
