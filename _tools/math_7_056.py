# -*- coding: utf-8 -*-
"""7. klase, 56. stunda: «Kādas vērtības funkcija pieņem?»

Definīcijas kopa D(f) ir visi argumenti, kuriem funkcija ir definēta;
vērtību kopa E(f) - visas vērtības, ko funkcija pieņem. No grafika tās
nolasa kā grafika «ēnu» uz x un y asīm.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, plakne)

TEMA = "Kādas vērtības funkcija pieņem?"

MERKIS = ("Noteiksim funkcijas definīcijas kopu un vērtību kopu vienkāršos "
          "gadījumos.")

_NOGR = plakne(grafiki=[([(-2, -1), (4, 2)], "")],
               punkti=[(-2, -1), (4, 2)],
               no_x=-3, lidz_x=5, no_y=-2, lidz_y=3, solis=1)

SATURS = [
    Sakums("Grafika ēna uz asīm",
           zimejums=_NOGR,
           paraksts="x no −2 līdz 4, y no −1 līdz 2.",
           fakti=["Nospīdi gaismu no augšas - ēna uz x ass ir D(f).",
                  "Nospīdi no sāniem - ēna uz y ass ir E(f)."]),

    Doma("D(f) - argumenti, E(f) - vērtības",
         "Funkcijas definīcijas kopa D(f) ir visu to argumentu kopa, kuriem "
         "funkcija ir definēta. Vērtību kopa E(f) ir visu funkcijas vērtību "
         "kopa.",
         soli=[
             "No grafika: skaties, no kura līdz kuram x grafiks iet - D(f).",
             "Skaties, no kura līdz kuram y - E(f).",
             "No formulas: vai kādu x nedrīkst ievietot (dalīt ar 0)?",
             "No situācijas: kādi argumenti ir jēgpilni?",
         ],
         pieze="Pieraksts ar nevienādību: D(f): −2 ≤ x ≤ 4. Ja funkcija "
               "definēta visiem skaitļiem - D(f) ir visi skaitļi."),

    Paraugs("Nolasi no grafika",
            uzd="Sākuma grafikā nosaki D(f) un E(f).",
            soli=[
                ("Kreisais gals (−2; −1), labais (4; 2)", "Nolasa galus."),
                ("D(f): −2 ≤ x ≤ 4", "Argumenti."),
                ("E(f): −1 ≤ y ≤ 2", "Vērtības."),
            ],
            atbilde="D(f): −2 ≤ x ≤ 4; E(f): −1 ≤ y ≤ 2"),

    Varianti("Nosaki kopas", [
        {"jaut": "f(x) = {12|x}. Kurš skaitlis nepieder D(f)?",
         "opcijas": ["0", "1", "−12", "12"],
         "pareizi": 0,
         "padoms": "Ar 0 dalīt nevar."},
        {"jaut": "f(x) = 2x + 3 visiem x. Kāda ir D(f)?",
         "opcijas": ["Visi skaitļi", "Tikai pozitīvi", "Tikai veseli",
                     "x ≥ 3"],
         "pareizi": 0,
         "padoms": "Jebkuru skaitli var reizināt un saskaitīt."},
        {"jaut": "f(x) = 5 visiem x. Kāda ir E(f)?",
         "opcijas": ["{5}", "Visi skaitļi", "x ≥ 5", "∅"],
         "pareizi": 0,
         "padoms": "Vienīgā vērtība ir 5."},
        {"jaut": "Biļešu cena S(n) = 6n skolēnu grupai līdz 30. Kāda "
                 "ir D(S)?",
         "opcijas": ["{1; 2; ...; 30}", "Visi skaitļi", "0 ≤ n ≤ 180",
                     "Tikai 30"],
         "pareizi": 0,
         "padoms": "Skolēnu skaits - naturāls, līdz 30."},
    ], pamats=4),

    Ievadi("Aprēķini robežas", [
        {"jaut": "f(x) = 2x, D(f): 0 ≤ x ≤ 5. Lielākā vērtība?",
         "atb": ["10"], "padoms": "f(5)."},
        {"jaut": "f(x) = 10 − x, D(f): 1 ≤ x ≤ 4. Mazākā vērtība?",
         "atb": ["6"], "padoms": "f(4) - jo lielāks x, jo mazāks f."},
        {"jaut": "f(x) = 10 − x, D(f): 1 ≤ x ≤ 4. Lielākā vērtība?",
         "atb": ["9"], "padoms": "f(1)."},
        {"jaut": "Grafiks - nogrieznis no (−3; 4) līdz (5; 0). Mazākā "
                 "E(f) vērtība?",
         "atb": ["0"], "padoms": "y no 0 līdz 4."},
    ]),

    Pasaule("Termometrs ar diapazonu",
            Ievadi("", [
                {"jaut": "Āra termometrs mēra no −40 °C līdz 50 °C. Cik "
                         "grādu plats ir tā diapazons?",
                 "atb": ["90"], "padoms": "50 − (−40)."},
                {"jaut": "Temperatūra naktī T(t) = −2t, 0 ≤ t ≤ 6 (h pēc "
                         "pusnakts). Kāda ir mazākā vērtība (°C)?",
                 "atb": ["−12", "-12"], "padoms": "T(6)."},
                {"jaut": "Vai termometrs var parādīt −55 °C? Raksti «jā» "
                         "vai «nē».",
                 "atb": ["nē", "ne"], "padoms": "Ārpus E."},
            ]),
            pavediens="planeta",
            konteksts="Katrai mērierīcei ir diapazons - tā ir tās "
                      "vērtību kopa.",
            kapec="D(f) un E(f) pasaka, ko ierīce var un ko nevar."),

    Kopsavilkums([
        "Nosaku D(f) un E(f) no grafika.",
        "Zinu, ka ar 0 dalīt nevar - šis x nepieder D(f).",
        "Nosaku D(f) no situācijas.",
        "Pierakstu kopas ar nevienādību.",
    ]),

    Majas([
        "Uzzīmē funkcijas grafiku ar D(f): 0 ≤ x ≤ 6 un E(f): 1 ≤ y ≤ 4.",
        "Kādai funkcijai D(f) ir visi skaitļi, izņemot 2?",
        "Atrodi mājās ierīci ar diapazonu un pieraksti to.",
    ]),
]
