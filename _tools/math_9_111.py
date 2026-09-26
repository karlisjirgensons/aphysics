# -*- coding: utf-8 -*-
"""9. klase, 111. stunda: «Cik precīzs ir grafiskais atrisinājums?»

Ja krustpunkts nav rūtiņas stūrī (piem., (1,4; 2,6)), no zīmējuma to
nolasa tikai aptuveni. Tāpēc grafiski novērtē, bet precīzi aprēķina - un
pārbauda, vai abi rezultāti saskan.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, plakne)

TEMA = "Cik precīzs ir grafiskais atrisinājums?"

MERKIS = ("Izvērtēsim grafiskā atrisinājuma precizitāti un pārbaudīsim to "
          "analītiski.")

SATURS = [
    Sakums("Krustpunkts starp rūtiņām",
           zimejums=plakne(grafiki=[(1, 1.2, "y = x + 1,2"),
                                    (-1.5, 4.7, "y = −1,5x + 4,7")],
                           punkti=[(1.4, 2.6, "?")],
                           no_x=-1, lidz_x=4, no_y=-1, lidz_y=5),
           paraksts="Aptuveni (1,5; 2,5)? Precīzi - (1,4; 2,6).",
           fakti=["Grafiks dod tuvinājumu.",
                  "Precīzu vērtību dod aprēķins.",
                  "Zīmējums der kā pārbaude."]),

    Doma("Grafiks un aprēķins kopā",
         "Grafiski atrod aptuveno krustpunktu; analītiski - precīzo; ja tie "
         "ir tuvu, aprēķins ir ticams.",
         soli=[
             "Nolasi krustpunktu līdz pusrūtiņai.",
             "Aprēķini precīzi (pielīdzini y izteiksmes).",
             "Salīdzini: atšķirība < pusrūtiņa - labi.",
             "Ja atšķirība liela - meklē kļūdu.",
         ]),

    Paraugs("Precīzais krustpunkts",
            uzd="Atrodi y = x + 1,2 un y = −1,5x + 4,7 krustpunktu precīzi.",
            soli=[
                ("x + 1,2 = −1,5x + 4,7", "y vienādi."),
                ("2,5x = 3,5 ⇒ x = 1,4", "Atrisina."),
                ("y = 1,4 + 1,2 = 2,6", "Ievieto."),
            ],
            atbilde="(1,4; 2,6)"),

    Ievadi("Aprēķini precīzi", [
        {"jaut": "y = 2x un y = −x + 5: x = ? (līdz simtdaļām)",
         "atb": ["1,67"], "padoms": "3x = 5."},
        {"jaut": "Tai pašai y = ? (līdz simtdaļām)", "atb": ["3,33"],
         "padoms": "2 · 1,667."},
        {"jaut": "y = 0,5x + 1 un y = −x + 4: x = ?", "atb": ["2"],
         "padoms": "1,5x = 3."},
        {"jaut": "Tai pašai y = ?", "atb": ["2"], "padoms": "1 + 1."},
    ]),

    Varianti("Vai ticams?", [
        {"jaut": "Grafiski (2; 3), aprēķinā (2,1; 2,9).",
         "opcijas": ["Ticami - atšķirība maza", "Kļūda aprēķinā",
                     "Kļūda grafikā", "Nevar zināt"],
         "pareizi": 0, "padoms": "Mazāk par pusrūtiņu."},
        {"jaut": "Grafiski (2; 3), aprēķinā (5; −1).",
         "opcijas": ["Kāds no tiem kļūdains", "Ticami", "Abi pareizi",
                     "Tā mēdz būt"],
         "pareizi": 0, "padoms": "Pārāk tālu."},
    ]),

    Pasaule("Divi riteņbraucēji",
            Ievadi("", [
                {"jaut": "Anna brauc 18 km/h no starta, Jānis - 24 km/h, izbrauc "
                         "pusstundu vēlāk: 18t = 24(t − 0,5). Pēc cik h (no "
                         "Annas starta) Jānis panāk?", "atb": ["2"],
                 "padoms": "6t = 12."},
                {"jaut": "Cik km no starta?", "atb": ["36"],
                 "padoms": "18 · 2."},
            ]),
            pavediens="sports",
            konteksts="Kustības grafiki (ceļš - laiks) ir taisnes; panākšana ir "
                      "krustpunkts.",
            kapec="Grafiks rāda «ap 2 h», aprēķins - precīzi.",
            zimejums=plakne(grafiki=[(18, 0, "Anna"), (24, -12, "Jānis")],
                            punkti=[(2, 36, "(2; 36)")],
                            no_x=0, lidz_x=3, no_y=0, lidz_y=50, solis=1,
                            solis_y=10, x_nos="t, h", y_nos="s, km")),

    Kopsavilkums([
        "Nolasu krustpunktu aptuveni.",
        "Aprēķinu to precīzi.",
        "Salīdzinu un izvērtēju ticamību.",
    ]),

    Majas([
        "Atrisini grafiski un analītiski: y = 3x − 1, y = −2x + 3.",
        "Cik liela ir atšķirība starp abiem rezultātiem?",
        "Kāpēc grafiskā metode der aptuvenai atbildei?",
    ]),
]
