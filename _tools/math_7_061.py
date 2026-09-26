# -*- coding: utf-8 -*-
"""7. klase, 61. stunda: «Kā izvēlēties vienības uz asīm?»

Funkcijai y = 50x + 200 ar vienu rūtiņu uz vienību grafiks neietilptu
burtnīcā. Tāpēc katrai asij izvēlas savu vienības nogriezni: uz x ass
1 rūtiņa = 1, uz y ass 1 rūtiņa = 100. Stunda iemāca to izvēlēties.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, plakne)

TEMA = "Kā izvēlēties vienības uz asīm?"

MERKIS = ("Noteiksim piemērotus vienību nogriežņus, lai attēlotu funkciju "
          "ar lieliem koeficientiem.")

SATURS = [
    Sakums("Lidmašīnas augstums: 0 līdz 10 000 m",
           zimejums=plakne(grafiki=[([(0, 0), (10, 10000)], "")],
                           no_x=0, lidz_x=12, no_y=0, lidz_y=12000,
                           solis=2, solis_y=2000, x_nos="min", y_nos="m"),
           paraksts="1 rūtiņa uz x - 2 min, uz y - 2000 m.",
           fakti=["Pacelšanās 10 minūtēs līdz 10 km.",
                  "Ar 1 rūtiņu = 1 m grafiks būtu 10 km augsts.",
                  "Tāpēc katrai asij savs mērogs."]),

    Doma("Katrai asij - savs vienības nogrieznis",
         "Vienības nogriezni uz katras ass izvēlas tā, lai visas vajadzīgās "
         "vērtības ietilptu grafikā un grafiks būtu lasāms.",
         soli=[
             "Nosaki lielāko un mazāko x un y, kas jāattēlo.",
             "Izdali y diapazonu ar rūtiņu skaitu, kas ir pieejams.",
             "Noapaļo uz ērtu skaitli: 1, 2, 5, 10, 20, 50, 100...",
             "Pieraksti pie ass iedaļas un mērvienību.",
         ],
         pieze="Asīm var būt dažādi mērogi - bet uz vienas ass iedaļas "
               "vienmēr ir vienādas."),

    Slidnis("Tas pats grafiks, cits mērogs", [
        {"v": "1 rūtiņa = 1", "teksts": "Taisne nemaz neparādās - tā ir augstāk par zīmējumu.",
         "zim": plakne(grafiki=[(50, 200, "")], no_x=0, lidz_x=6, no_y=0,
                       lidz_y=6, solis=1)},
        {"v": "1 rūtiņa = 100", "teksts": "Uz y ass viss ietilpst.",
         "zim": plakne(grafiki=[(50, 200, "")], no_x=0, lidz_x=6, no_y=0,
                       lidz_y=600, solis=1, solis_y=100)},
        {"v": "1 rūtiņa = 50", "teksts": "Precīzāk, bet augstāks.",
         "zim": plakne(grafiki=[(50, 200, "")], no_x=0, lidz_x=6, no_y=0,
                       lidz_y=500, solis=1, solis_y=50)},
    ], ievads="y = 50x + 200, x no 0 līdz 6."),

    Paraugs("Izvēlies mērogu",
            uzd="Jāattēlo y = 30x + 60, kad 0 ≤ x ≤ 10. Burtnīcā ir 12 "
                "rūtiņu augstumā. Kādu vienību izvēlēties uz y ass?",
            soli=[
                ("Mazākā y: 60; lielākā: 30 · 10 + 60 = 360", "Diapazons."),
                ("360 : 12 = 30 uz rūtiņu", "Minimāli vajadzīgs."),
                ("Ērts skaitlis ≥ 30: 50", "Noapaļo uz augšu."),
                ("Ar 50: 360 : 50 ≈ 7,2 rūtiņas - ietilpst", "Pārbaude."),
            ],
            atbilde="1 rūtiņa = 50 uz y ass"),

    Varianti("Kurš mērogs der?", [
        {"jaut": "y no 0 līdz 800, pieejamas 10 rūtiņas.",
         "opcijas": ["1 rūtiņa = 100", "1 rūtiņa = 10",
                     "1 rūtiņa = 1", "1 rūtiņa = 1000"],
         "pareizi": 0,
         "padoms": "800 : 10 = 80 → 100."},
        {"jaut": "x no 0 līdz 60 min, 12 rūtiņas.",
         "opcijas": ["1 rūtiņa = 5 min", "1 rūtiņa = 1 min",
                     "1 rūtiņa = 60 min", "1 rūtiņa = 0,5 min"],
         "pareizi": 0,
         "padoms": "60 : 12."},
        {"jaut": "Kāpēc nav labi izvēlēties 1 rūtiņa = 1000, ja y līdz 800?",
         "opcijas": ["Grafiks būs mazāks par 1 rūtiņu - nesalasāms",
                     "Tas ir aizliegts", "Tas ir pareizi",
                     "Ass kļūs negatīva"],
         "pareizi": 0,
         "padoms": "Par sīku."},
    ]),

    Ievadi("Nolasi ar mērogu", [
        {"jaut": "Uz y ass 1 rūtiņa = 50. Punkts ir 7 rūtiņas augstumā. "
                 "Kāds y?",
         "atb": ["350"], "padoms": "7 · 50."},
        {"jaut": "Uz x ass 1 rūtiņa = 5 min. Punkts 9 rūtiņas pa labi. "
                 "Kāds x (min)?",
         "atb": ["45"], "padoms": "9 · 5."},
        {"jaut": "y = 50x + 200. Cik ir y, ja x = 4?",
         "atb": ["400"], "padoms": "200 + 200."},
        {"jaut": "Cik rūtiņas augstumā ir y = 400, ja 1 rūtiņa = 100?",
         "atb": ["4"], "padoms": "400 : 100."},
    ]),

    Pasaule("Raķetes starts",
            Ievadi("", [
                {"jaut": "Raķete pirmajās 60 s sasniedz 12 000 m. Ja uz y "
                         "ass ir 12 rūtiņas, cik metru uz rūtiņu?",
                 "atb": ["1000"], "padoms": "12 000 : 12."},
                {"jaut": "Uz x ass 6 rūtiņas līdz 60 s. Cik sekunžu uz "
                         "rūtiņu?",
                 "atb": ["10"], "padoms": "60 : 6."},
                {"jaut": "Vidējais ātrums pirmajās 60 s (m/s)?",
                 "atb": ["200"], "padoms": "12 000 : 60."},
            ]),
            pavediens="kosmoss",
            konteksts="Raķešu telemetrija rāda augstumu kilometros un laiku "
                      "sekundēs - asīm pilnīgi dažādi mērogi.",
            kapec="Bez mēroga izvēles grafiks nav iespējams."),

    Kopsavilkums([
        "Nosaku vajadzīgo diapazonu katrai asij.",
        "Izvēlos ērtu vienības nogriezni: 1, 2, 5, 10, 50, 100...",
        "Zinu, ka asīm var būt dažādi mērogi.",
        "Nolasu vērtības, ņemot vērā mērogu.",
    ]),

    Majas([
        "Uzzīmē y = 200x + 1000, 0 ≤ x ≤ 5.",
        "Izvēlies mērogus sava telefona lādiņa grafikam (0-100 %, 0-3 h).",
        "Atrodi ziņās grafiku un pieraksti tā mērogus.",
    ]),
]
