# -*- coding: utf-8 -*-
"""4. klase, 140. stunda: «Cik dažādi var sadalīt figūru?»

Sadalīt figūru vienlielās daļās var daudzos veidos - taisnstūri 4 × 2
uz pusēm var griezt gareniski, šķērsām vai pa diagonāli. Skolēns meklē
dažādus risinājumus un salīdzina tos - atvērts uzdevums ģeometrijā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Sakums, Varianti, figura)

TEMA = "Cik dažādi var sadalīt figūru?"

MERKIS = ("Dalīsim figūru vienlielās daļās vairākos veidos un salīdzināsim "
          "risinājumus.")

SATURS = [
    Sakums("Kā sadalīt šokolādi divām māsām?",
           zimejums=figura([(0, 0), (4, 0), (4, 2), (0, 2), (0, 0), (4, 2)],
                           platums=5, augstums=3, aizpildi=False),
           paraksts="Pa diagonāli - divi vienādi trijstūri pa 4 rūtiņām.",
           fakti=["Šokolāde 4 × 2 - 8 rūtiņas, katrai 4.",
                  "Griezt var gareniski, šķērsām vai pa diagonāli."]),

    Doma("Vienlielas daļas - dažādi griezumi",
         "Figūru vienlielās daļās var sadalīt vairākos veidos; katrā daļā "
         "jābūt vienādam rūtiņu skaitam.",
         soli=[
             "Saskaiti visas rūtiņas: 8.",
             "Izdali ar daļu skaitu: 8 : 2 = 4.",
             "Meklē dažādus griezumus, kur katrā daļā 4 rūtiņas.",
             "Pārbaudi katru risinājumu.",
         ],
         pieze="Daļām nav jābūt vienādas formas - tikai vienāda laukuma."),

    Ievadi("Cik rūtiņu katrā daļā?", [
        {"jaut": "Taisnstūris 6 × 4 jāsadala 3 vienlielās daļās. Cik rūtiņu "
                 "katrā?", "atb": ["8"], "padoms": "24 : 3."},
        {"jaut": "Kvadrāts 6 × 6 jāsadala 4 daļās. Cik rūtiņu katrā?",
         "atb": ["9"], "padoms": "36 : 4."},
        {"jaut": "Taisnstūris 5 × 4 - 5 daļās. Cik rūtiņu katrā?",
         "atb": ["4"], "padoms": "20 : 5."},
        {"jaut": "Vai taisnstūri 3 × 3 var sadalīt 2 vienlielās daļās pa "
                 "veselām rūtiņām? Raksti «jā» vai «nē».",
         "atb": ["nē", "ne"], "tastatura": "text",
         "padoms": "9 nedalās ar 2 - tikai ar pusrūtiņām."},
    ]),

    Varianti("Vai daļas vienlielas?", [
        {"jaut": "Taisnstūri 4 × 2 sagrieza 3 + 5 rūtiņās.",
         "opcijas": ["nē", "jā"], "pareizi": 0, "padoms": "3 ≠ 5."},
        {"jaut": "Kvadrāts 2 × 2 sagriezts pa diagonāli.",
         "opcijas": ["jā", "nē"], "pareizi": 0,
         "padoms": "Divi vienādi trijstūri."},
        {"jaut": "Vai daļām jābūt vienādas formas?",
         "opcijas": ["nē, tikai vienāda laukuma", "jā"], "pareizi": 0,
         "padoms": "Vienlielas - vienāds laukums."},
        {"jaut": "Kādā skaitā vienlielu daļu var sadalīt 12 rūtiņas?",
         "opcijas": ["2, 3, 4, 6", "tikai 2", "5 un 7", "tikai 12"],
         "pareizi": 0, "padoms": "12 dalītāji."},
    ], pamats=4),

    Pasaule("Dārza sadalīšana kaimiņiem",
            Ievadi("", [
                {"jaut": "Dārzs 12 m × 8 m. Cik m²?", "atb": ["96"],
                 "padoms": "12 · 8."},
                {"jaut": "Sadala 4 kaimiņiem vienādi. Cik m² katram?",
                 "atb": ["24"], "padoms": "96 : 4."},
                {"jaut": "Ja katrs gabals ir 6 m plats, cik garš?",
                 "atb": ["4"], "padoms": "24 : 6."},
                {"jaut": "Ja sadala 6 kaimiņiem - cik m² katram?",
                 "atb": ["16"], "padoms": "96 : 6."},
            ]),
            pavediens="maja",
            konteksts="Kopienas dārzos zemi dala vienādos gabalos - bet "
                      "gabalu formas var būt dažādas.",
            kapec="Godīgi - tas nozīmē vienādu laukumu."),

    Kopsavilkums([
        "Sadalu figūru vienlielās daļās vairākos veidos.",
        "Pārbaudu, vai daļās ir vienāds rūtiņu skaits.",
        "Salīdzinu risinājumus.",
    ]),

    Majas([
        "Sadali 4 × 4 kvadrātu 4 vienlielās daļās trijos veidos.",
        "Sadali šokolādi ģimenei godīgi un pārbaudi ar rūtiņām.",
        "Atrodi, kādās daļās var sadalīt 18 rūtiņas.",
    ]),
]
