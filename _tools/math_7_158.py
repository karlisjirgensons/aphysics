# -*- coding: utf-8 -*-
"""7. klase, 158. stunda: «Kā atrisinājumu attēlot uz taisnes?»

Viens un tas pats atrisinājums ir četros pierakstos: nevienādība, intervāls,
skaitļu taisne un vārdi. Stunda trenē pāreju starp visiem četriem - to
prasa eksāmena uzdevumos ar izvēli.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, taisne)

TEMA = "Kā atrisinājumu attēlot uz taisnes?"

MERKIS = ("Pārveidosim intervāla attēlojumu no viena veida citā.")

SATURS = [
    Sakums("Četri veidi - viena kopa",
           zimejums=taisne(-3, 6, 1, intervali=[(-1, 4, False, True)]),
           paraksts="−1 < x ≤ 4 ⇔ (−1; 4] ⇔ «lielāks par −1, ne lielāks "
                    "par 4».",
           fakti=["Taisne - ātrs pārskats.",
                  "Intervāls - īss pieraksts.",
                  "Nevienādība - aprēķiniem."]),

    Doma("Tulko starp pierakstiem",
         "Uz skaitļu taisnes: galapunkts pilns - pieder (≤, ≥, [ ]); tukšs - "
         "nepieder (<, >, ( )); svītrojums rāda visus kopas skaitļus.",
         soli=[
             "No taisnes: nolasi galus un punktu veidu.",
             "Uzraksti nevienādību (mazākais pa kreisi).",
             "Pārraksti iekavās.",
             "Pārbaudi ar vienu skaitli no svītrojuma.",
         ]),

    Slidnis("Dažādi intervāli", [
        {"v": "x > 1", "teksts": "(1; +∞)",
         "zim": taisne(-3, 6, 1, intervali=[(1, None, False, False)])},
        {"v": "x ≤ 2", "teksts": "(−∞; 2]",
         "zim": taisne(-3, 6, 1, intervali=[(None, 2, False, True)])},
        {"v": "−2 ≤ x < 3", "teksts": "[−2; 3)",
         "zim": taisne(-3, 6, 1, intervali=[(-2, 3, True, False)])},
        {"v": "0 < x < 5", "teksts": "(0; 5)",
         "zim": taisne(-3, 6, 1, intervali=[(0, 5, False, False)])},
    ]),

    Paraugs("No taisnes uz pierakstu",
            uzd="Uz taisnes: tukšs punkts pie −2, svītrojums pa labi. "
                "Pieraksti.",
            soli=[
                ("Tukšs punkts - −2 nepieder", "Apaļā iekava."),
                ("Pa labi - lielāki", "x > −2."),
                ("x ∈ (−2; +∞)", "Intervāls."),
            ],
            atbilde="x > −2; (−2; +∞)"),

    Varianti("Kurš pieraksts atbilst?", [
        {"jaut": "Pilns punkts pie 3, svītrots pa kreisi.",
         "opcijas": ["x ≤ 3", "x < 3", "x ≥ 3", "x > 3"],
         "pareizi": 0, "padoms": "Pilns - ietilpst."},
        {"jaut": "(−4; 1]",
         "opcijas": ["−4 < x ≤ 1", "−4 ≤ x < 1", "−4 ≤ x ≤ 1",
                     "−4 < x < 1"],
         "pareizi": 0, "padoms": "Apaļā - stingri."},
        {"jaut": "«Ne mazāk par 0 un mazāk par 10»",
         "opcijas": ["[0; 10)", "(0; 10]", "[0; 10]", "(0; 10)"],
         "pareizi": 0, "padoms": "0 der, 10 - nē."},
        {"jaut": "x ≥ 7",
         "opcijas": ["[7; +∞)", "(7; +∞)", "(−∞; 7]", "[7; +∞]"],
         "pareizi": 0, "padoms": "Pie ∞ vienmēr apaļā."},
    ], pamats=4),

    Pasaule("Mūzikas skaļums",
            Varianti("", [
                {"jaut": "Austiņām droši līdz 85 dB (ieskaitot). Kurš "
                         "pieraksts?",
                 "opcijas": ["x ≤ 85", "x < 85", "x ≥ 85", "x > 85"],
                 "pareizi": 0, "padoms": "Līdz ieskaitot."},
                {"jaut": "Kaitīgi - virs 85 dB. Intervāls?",
                 "opcijas": ["(85; +∞)", "[85; +∞)", "(−∞; 85)",
                             "(0; 85]"],
                 "pareizi": 0, "padoms": "85 nav kaitīgs."},
            ]),
            pavediens="tehnika",
            konteksts="Telefoni brīdina, ja skaļums ilgstoši pārsniedz drošo "
                      "intervālu.",
            kapec="Intervāls robežo drošo no kaitīgā."),

    Kopsavilkums([
        "Pārveidoju nevienādību intervālā un taisnē.",
        "Nolasu intervālu no taisnes.",
        "Atšķiru pilnu un tukšu punktu.",
        "Pie bezgalības lietoju apaļo iekavu.",
    ]),

    Majas([
        "Uzzīmē uz taisnes: [−1; 4), (−∞; 0], (2; +∞).",
        "Pieraksti ar vārdiem un nevienādībām.",
        "Atrodi drošo intervālu sadzīves tehnikai.",
    ]),
]
