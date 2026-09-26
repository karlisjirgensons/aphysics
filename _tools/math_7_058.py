# -*- coding: utf-8 -*-
"""7. klase, 58. stunda: «Kāpēc grafiks ir taisne?»

Funkcijai y = kx + b katrs argumenta pieaugums par 1 dod vienu un to pašu
vērtības pieaugumu k. Vienādi soļi pa labi un vienādi soļi uz augšu - tā
izskatās taisne. Tāpēc šādas funkcijas sauc par lineārām.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         plakne, restis)

TEMA = "Kāpēc grafiks ir taisne?"

MERKIS = ("Formulēsim vispārinājumu: ja argumentu reizina ar skaitli un "
          "pieskaita skaitli, grafiks ir taisne.")


def _kapnes(n):
    """Taisne y = 2x + 1 un n pakāpieni pa 1 pa labi un 2 uz augšu."""
    celi = [(0, 1)]
    for i in range(n):
        celi += [(i + 1, 2 * i + 1), (i + 1, 2 * i + 3)]
    return plakne(grafiki=[(2, 1, "y = 2x + 1"), (celi, "")],
                  no_x=-1, lidz_x=4, no_y=-1, lidz_y=9, solis=1, solis_y=2)


SATURS = [
    Sakums("Kāpnes un rampa",
           zimejums=_kapnes(3),
           paraksts="Katrs pakāpiens: 1 pa labi, 2 uz augšu.",
           fakti=["Vienādi pakāpieni - stūri ir uz vienas taisnes.",
                  "Tāpat ir ar y = 2x + 1: katrs +1 pie x dod +2 pie y."]),

    Doma("Lineāra funkcija: y = kx + b",
         "Funkciju y = kx + b, kur k un b ir skaitļi, sauc par lineāru "
         "funkciju. Tās grafiks ir taisne, jo, argumentam pieaugot par 1, "
         "vērtība vienmēr mainās par to pašu skaitli k.",
         soli=[
             "Izveido tabulu ar argumentiem pēc kārtas: 0; 1; 2; 3.",
             "Aprēķini pieaugumus starp blakus vērtībām.",
             "Ja visi pieaugumi vienādi (k) - punkti ir uz taisnes.",
             "b ir vērtība, kad x = 0 - kur taisne krusto y asi.",
         ],
         pieze="Tieša proporcionalitāte y = kx ir lineāra funkcija ar b = 0: "
               "tās taisne iet caur (0; 0)."),

    Slidnis("Pakāpiens pēc pakāpiena", [
        {"v": "x = 0", "teksts": "y = 1", "zim": _kapnes(0)},
        {"v": "x = 1", "teksts": "y = 1 + 2 = 3", "zim": _kapnes(1)},
        {"v": "x = 2", "teksts": "y = 3 + 2 = 5", "zim": _kapnes(2)},
        {"v": "x = 3", "teksts": "y = 5 + 2 = 7", "zim": _kapnes(3)},
    ]),

    Paraugs("Pārbaudi linearitāti",
            uzd="Tabula: x = 0; 1; 2; 3, y = 4; 1; −2; −5. Vai funkcija ir "
                "lineāra? Uzraksti formulu.",
            soli=[
                ("Pieaugumi: −3; −3; −3", "Visi vienādi."),
                ("k = −3", "Pieaugums, x pieaugot par 1."),
                ("b = 4", "Vērtība, kad x = 0."),
                ("y = −3x + 4", "Formula."),
            ],
            atbilde="Lineāra, y = −3x + 4"),

    Zimejums("Nav lineāra",
             restis([["x", "0", "1", "2", "3"],
                     ["y = x²", "0", "1", "4", "9"],
                     ["pieaugums", "", "+1", "+3", "+5"]]),
             paskaidro="Pieaugumi atšķiras - punkti nav uz taisnes."),

    Varianti("Lineāra vai nē?", [
        {"jaut": "y = 5x − 2",
         "opcijas": ["Lineāra", "Nav lineāra"],
         "pareizi": 0, "jaukt": False, "padoms": "k = 5, b = −2."},
        {"jaut": "y = {6|x}",
         "opcijas": ["Lineāra", "Nav lineāra"],
         "pareizi": 1, "jaukt": False, "padoms": "Apgrieztā proporcionalitāte."},
        {"jaut": "y = 7",
         "opcijas": ["Lineāra", "Nav lineāra"],
         "pareizi": 0, "jaukt": False, "padoms": "k = 0, b = 7."},
        {"jaut": "y = x · x",
         "opcijas": ["Lineāra", "Nav lineāra"],
         "pareizi": 1, "jaukt": False, "padoms": "Tas ir x²."},
    ], pamats=4),

    Ievadi("Nosaki k un b", [
        {"jaut": "y = −2x + 9. Cik ir k?",
         "atb": ["−2", "-2"], "padoms": "Reizinātājs pie x."},
        {"jaut": "y = −2x + 9. Cik ir b?",
         "atb": ["9"], "padoms": "Brīvais loceklis."},
        {"jaut": "y = 4 + 0,5x. Cik ir k?",
         "atb": ["0,5"], "padoms": "Secība nav svarīga."},
        {"jaut": "y = 3x. Cik ir b?",
         "atb": ["0"], "padoms": "Nekā nepieskaita."},
    ]),

    Pasaule("Taksometra tarifs",
            Ievadi("", [
                {"jaut": "Taksometrs: 2,50 € + 0,90 € par km. Formula "
                         "S = kx + b. Cik ir k?",
                 "atb": ["0,9"], "padoms": "Maksa par vienu km."},
                {"jaut": "Cik ir b?",
                 "atb": ["2,5"], "padoms": "Iekāpšanas maksa."},
                {"jaut": "Par cik € pieaug summa ar katriem 10 km?",
                 "atb": ["9"], "padoms": "10 · 0,9."},
            ]),
            pavediens="celojums",
            konteksts="Taksometru tarifi ir lineāras funkcijas: sākuma maksa "
                      "plus vienāda maksa par katru km.",
            kapec="Vienāds pieaugums par katru km - taisne."),

    Kopsavilkums([
        "Zinu, ka y = kx + b ir lineāra funkcija.",
        "Pamatoju, kāpēc grafiks ir taisne - vienādi pieaugumi.",
        "Atrodu k un b no formulas un tabulas.",
        "Atšķiru lineāru funkciju no nelineāras.",
    ]),

    Majas([
        "Izveido tabulu y = −x + 3 un pārbaudi pieaugumus.",
        "Atrodi dzīvē tarifu, kas ir lineāra funkcija, un uzraksti formulu.",
        "Uzraksti tabulu, kas nav lineāra.",
    ]),
]
