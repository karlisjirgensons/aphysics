# -*- coding: utf-8 -*-
"""4. klase, 141. stunda: «Kā uzzīmēt trijstūri ar tādu pašu laukumu?»

Trijstūris, kas «izgriezts» pa taisnstūra diagonāli, ir puse no tā. Tāpēc
trijstūrim ar tādu pašu laukumu kā taisnstūris 4 × 3 vajag divreiz
lielāku «kasti»: 8 × 3 vai 4 × 6. Formulu 4. klasē neraksta - to redz.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, figura)

TEMA = "Kā uzzīmēt trijstūri ar tādu pašu laukumu?"

MERKIS = ("Zīmēsim trijstūri, kura laukums vienāds ar dotā taisnstūra "
          "laukumu, un paskaidrosim rīcību.")

SATURS = [
    Sakums("Trijstūris ir puse no kastes",
           zimejums=figura([(0, 0), (4, 0), (4, 3), (0, 3), (0, 0), (4, 3)],
                           platums=5, augstums=4, aizpildi=False),
           paraksts="Diagonāle sadala taisnstūri 4 × 3 divos trijstūros pa 6.",
           fakti=["Taisnleņķa trijstūris ir puse no taisnstūra.",
                  "Lai trijstūrim būtu 12, vajag taisnstūri ar 24."]),

    Doma("Divreiz lielāks taisnstūris - tad puse",
         "Lai trijstūra laukums būtu tāds pats kā taisnstūrim, zīmē "
         "taisnstūri ar divreiz lielāku laukumu un sadali to pa diagonāli.",
         soli=[
             "Taisnstūra laukums: 4 · 3 = 12.",
             "Vajag «kasti» ar 24: piemēram, 8 × 3.",
             "Novelc diagonāli - trijstūris ar 12 rūtiņām.",
             "Pārbaudi: pusrūtiņas saliec pa divām.",
         ],
         pieze="Der arī 4 × 6 vai 12 × 2 - visām kastēm laukums 24."),

    Zimejums("Trijstūris 8 × 3 kastē",
             figura([(0, 0), (8, 0), (8, 3)], platums=9, augstums=4),
             paskaidro="Puse no 8 · 3 = 24 ir 12 - tāpat kā taisnstūrim "
                       "4 × 3.",
             ievads="Iekrāsotais trijstūris."),

    Paraugs("Trijstūris kā taisnstūris 5 × 2",
            uzd="Uzzīmē taisnleņķa trijstūri ar laukumu kā taisnstūrim 5 × 2.",
            soli=[
                ("5 · 2 = 10", "Taisnstūra laukums."),
                ("kaste 10 × 2 vai 5 × 4 - laukums 20", None),
                ("puse no 20 = 10", "Trijstūris pa diagonāli."),
            ],
            atbilde="trijstūris ar malām 5 un 4 (vai 10 un 2)"),

    Ievadi("Trijstūru laukumi", [
        {"jaut": "Taisnleņķa trijstūris, malas pie taisnā leņķa 6 un 4. "
                 "Laukums?", "atb": ["12"], "padoms": "6 · 4 : 2."},
        {"jaut": "Malas 10 un 3. Laukums?", "atb": ["15"],
         "padoms": "30 : 2."},
        {"jaut": "Trijstūrim jābūt 8 rūtiņām, viena mala 4. Otra mala?",
         "atb": ["4"], "padoms": "Kaste 16 = 4 · 4."},
        {"jaut": "Trijstūrim jābūt 9, viena mala 6. Otra mala?",
         "atb": ["3"], "padoms": "Kaste 18 = 6 · 3."},
    ]),

    Varianti("Kurš trijstūris der?", [
        {"jaut": "Taisnstūris 3 × 4 (12). Kurš taisnleņķa trijstūris "
                 "vienliels?",
         "opcijas": ["malas 6 un 4", "malas 3 un 4", "malas 2 un 4"],
         "pareizi": 0, "padoms": "6 · 4 : 2 = 12."},
        {"jaut": "Trijstūris ar malām 3 un 4 ir ... no 3 × 4 taisnstūra.",
         "opcijas": ["puse", "tikpat", "divreiz vairāk"], "pareizi": 0,
         "padoms": "Diagonāle."},
        {"jaut": "Trijstūris ar malām 8 un 2. Laukums?",
         "opcijas": ["8", "16", "10", "4"], "pareizi": 0,
         "padoms": "16 : 2."},
    ]),

    Pasaule("Buru laivas bura",
            Ievadi("", [
                {"jaut": "Trijstūra bura: malas pie taisnā leņķa 4 m un 3 m. "
                         "Cik m² auduma?",
                 "atb": ["6"], "padoms": "4 · 3 : 2."},
                {"jaut": "Lielākai laivai malas 6 m un 4 m. Cik m²?",
                 "atb": ["12"], "padoms": "24 : 2."},
                {"jaut": "Audums maksā 15 € par m². Cik maksā lielā bura?",
                 "atb": ["180"], "padoms": "12 · 15."},
                {"jaut": "Cik reižu lielā bura lielāka par mazo?",
                 "atb": ["2"], "padoms": "12 : 6."},
            ]),
            pavediens="tehnika",
            konteksts="Buras bieži ir trijstūri - un audumu pērk "
                      "kvadrātmetros.",
            kapec="Trijstūris ir puse no taisnstūra - to zina buru šuvēji."),

    Kopsavilkums([
        "Zinu, ka taisnleņķa trijstūris ir puse no taisnstūra.",
        "Zīmēju trijstūri ar dotu laukumu.",
        "Paskaidroju, kāpēc vajag divreiz lielāku «kasti».",
    ]),

    Majas([
        "Uzzīmē 3 dažādus trijstūrus ar laukumu 6 rūtiņas.",
        "Sagriez papīra taisnstūri pa diagonāli un pārbaudi, ka puses "
        "vienādas.",
        "Aprēķini trijstūrveida karodziņa laukumu.",
    ]),
]
