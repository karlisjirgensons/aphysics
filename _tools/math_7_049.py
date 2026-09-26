# -*- coding: utf-8 -*-
"""7. klase, 49. stunda: «Ko stāsta grafika tuvošanās asīm?»

Apgrieztās proporcionalitātes grafiks tuvojas asīm, bet tās nekad
nesasniedz: taisnstūris ar laukumu 24 nevar būt ar malu 0, un ar ļoti mazu
malu otrai jābūt ļoti garai. Stunda nolasa grafiku un skaidro, kādas
vērtības lielumi var pieņemt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, plakne)

TEMA = "Ko stāsta grafika tuvošanās asīm?"

MERKIS = ("Nolasīsim informāciju no apgrieztās proporcionalitātes grafika "
          "un paskaidrosim lielumu iespējamās vērtības.")

_LIKNE = [(x / 10.0, 12 / (x / 10.0)) for x in range(10, 121)]

SATURS = [
    Sakums("Cik ilgi brauksi 120 km?",
           zimejums=plakne(grafiki=[([(v, 120.0 / v) for v in
                                      range(10, 121, 2)], "")],
                           no_x=0, lidz_x=120, no_y=0, lidz_y=12,
                           solis=20, solis_y=2, x_nos="v", y_nos="t"),
           paraksts="t = 120 : v. Jo ātrāk, jo īsāks laiks.",
           fakti=["Ar 10 km/h - 12 stundas.",
                  "Ar 120 km/h - 1 stunda.",
                  "Ar 0 km/h nekad neaizbrauks - tāpēc līkne nesasniedz "
                  "asi."]),

    Doma("Līkne tuvojas asīm, bet tās nesasniedz",
         "Grafikam y = {k|x} (k > 0) neviena no koordinātām nevar būt nulle: "
         "ja x būtu 0, reizinājums būtu 0, nevis k. Tāpēc grafiks tuvojas "
         "asīm, bet tās nekrusto.",
         soli=[
             "Nolasi vērtības pie maza x - y ir liels.",
             "Nolasi vērtības pie liela x - y ir mazs.",
             "Pārbaudi: x · y = k katrā punktā.",
             "Secini: x ≠ 0 un y ≠ 0.",
         ],
         pieze="Situācijā vēl ir savas robežas: ātrums nevar būt 1000 km/h "
               "uz ceļa, un laiks nevar būt 0."),

    Zimejums("y = 12 : x",
             plakne(grafiki=[(_LIKNE, "")],
                    punkti=[(1, 12), (2, 6), (3, 4), (4, 3), (6, 2),
                            (12, 1)],
                    no_x=0, lidz_x=12, no_y=0, lidz_y=12, solis=1),
             paskaidro="Līkne ir simetriska: punkti (2; 6) un (6; 2)."),

    Paraugs("Nolasi un pamato",
            uzd="No grafika y = 12 : x nolasi y, ja x = 4. Vai grafikā ir "
                "punkts ar x = 0?",
            soli=[
                ("x = 4: y = 3", "12 : 4 = 3."),
                ("Pārbaude: 4 · 3 = 12", "Reizinājums k."),
                ("x = 0: 0 · y = 0 ≠ 12", "Neviens y neder."),
                ("Punkta ar x = 0 nav", "Grafiks nekrusto y asi."),
            ],
            atbilde="y = 3; punkta ar x = 0 nav."),

    Varianti("Ko rāda grafiks?", [
        {"jaut": "Kas notiek ar y, kad x kļūst ļoti liels?",
         "opcijas": ["y tuvojas 0, bet nav 0", "y kļūst 0",
                     "y kļūst negatīvs", "y aug"],
         "pareizi": 0,
         "padoms": "12 : 1000 = 0,012."},
        {"jaut": "Kas notiek ar y, kad x tuvojas 0?",
         "opcijas": ["y kļūst ļoti liels", "y kļūst 0", "y ir 12",
                     "y kļūst negatīvs"],
         "pareizi": 0,
         "padoms": "12 : 0,1 = 120."},
        {"jaut": "Vai punkts (5; 2,4) ir uz grafika y = 12 : x?",
         "opcijas": ["Jā", "Nē"],
         "pareizi": 0, "jaukt": False,
         "padoms": "5 · 2,4 = 12."},
    ]),

    Ievadi("Nolasi un aprēķini", [
        {"jaut": "t = 120 : v. Cik h ar 40 km/h?",
         "atb": ["3"], "padoms": "120 : 40."},
        {"jaut": "Ar kādu ātrumu (km/h) jābrauc, lai 120 km veiktu 1,5 h?",
         "atb": ["80"], "padoms": "120 : 1,5."},
        {"jaut": "y = 12 : x. Kāds ir x, ja y = 0,5?",
         "atb": ["24"], "padoms": "12 : 0,5."},
        {"jaut": "y = 12 : x. Kāds ir y, ja x = 0,1?",
         "atb": ["120"], "padoms": "12 : 0,1."},
    ]),

    Pasaule("Uzlādes jauda un laiks",
            Ievadi("", [
                {"jaut": "Elektroauto akumulatoram vajag 60 kWh. Ar 11 kW "
                         "lādētāju - cik stundās (noapaļo līdz veseliem)?",
                 "atb": ["5"], "padoms": "60 : 11 ≈ 5,45."},
                {"jaut": "Ar 150 kW ātrlādētāju - cik minūtēs?",
                 "atb": ["24"], "padoms": "60 : 150 = 0,4 h."},
                {"jaut": "Vai ar bezgalīgi lielu jaudu laiks būtu 0? Raksti "
                         "«jā» vai «nē».",
                 "atb": ["nē", "ne"],
                 "padoms": "Laiks tuvojas 0, bet grafiks asi nesasniedz."},
            ]),
            pavediens="tehnika",
            konteksts="Uzlādes laiks ir apgriezti proporcionāls jaudai - "
                      "tāpēc ātrlādētāji ir tik vērtīgi.",
            kapec="Grafiks parāda, ka ieguvums ar katru kW kļūst mazāks."),

    Kopsavilkums([
        "Nolasu vērtības no līknes y = {k|x}.",
        "Pamatoju, kāpēc grafiks nekrusto asis.",
        "Pārbaudu punktu ar reizinājumu.",
        "Skaidroju lielumu iespējamās vērtības situācijā.",
    ]),

    Majas([
        "Uzzīmē grafiku t = 60 : v ātrumiem no 5 līdz 60 km/h.",
        "Nolasi, cik ilgi 60 km iet kājām (5 km/h).",
        "Paskaidro, kāpēc grafiks nekad nesasniedz asi.",
    ]),
]
