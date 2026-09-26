# -*- coding: utf-8 -*-
"""8. klase, 54. stunda: «Kad kvadrātsakne neeksistē?»

Neviena reāla skaitļa kvadrāts nav negatīvs, tāpēc √(−4) reālo skaitļu
kopā nav. Stunda to pārvērš praktiskā prasmē: noteikt, kurām mainīgā
vērtībām izteiksmei √(x − 3) ir jēga.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, restis, taisne)

TEMA = "Kad kvadrātsakne neeksistē?"

MERKIS = ("Sapratīsim, kāpēc negatīvam skaitlim aritmētiskās kvadrātsaknes "
          "nav.")

SATURS = [
    Sakums("Kurš skaitlis kvadrātā ir −4?",
           zimejums=restis([["x", "−2", "−1", "0", "1", "2"],
                            ["x²", "4", "1", "0", "1", "4"]]),
           paraksts="Kvadrāti ir 0 vai pozitīvi - nekad negatīvi.",
           fakti=["Pluss reiz pluss - pluss.",
                  "Mīnuss reiz mīnuss - arī pluss.",
                  "Tāpēc √(−4) reālo skaitļu kopā nav."]),

    Doma("Kad sakne ir definēta",
         "Izteiksmei √a ir jēga tikai tad, ja a ≥ 0. Ja zemsaknes izteiksmē "
         "ir mainīgais, tā pieļaujamās vērtības atrod ar nevienādību.",
         soli=[
             "Pieraksti nosacījumu: zemsaknes izteiksme ≥ 0.",
             "Atrisini nevienādību.",
             "Atbilde - intervāls, kurā izteiksmei ir jēga.",
             "√0 = 0 - nulle ir atļauta.",
         ],
         pieze="Kalkulators uz √(−4) rāda «Error» vai «Math ERROR» - tas "
               "nav bojāts, tā ir matemātika."),

    Varianti("Vai ir jēga?", [
        {"jaut": "√(−9)",
         "opcijas": ["Nav", "Ir: −3", "Ir: 3", "Ir: ±3"],
         "pareizi": 0, "padoms": "Negatīvs zem saknes."},
        {"jaut": "−√9",
         "opcijas": ["Ir: −3", "Nav", "Ir: 3", "Ir: 9"],
         "pareizi": 0, "padoms": "Mīnuss ir ārpus saknes."},
        {"jaut": "√((−3)^2)",
         "opcijas": ["Ir: 3", "Nav", "Ir: −3", "Ir: 9"],
         "pareizi": 0, "padoms": "(−3)^2 = 9."},
        {"jaut": "√(5 − 8)",
         "opcijas": ["Nav", "Ir: √3", "Ir: −√3", "Ir: 3"],
         "pareizi": 0, "padoms": "5 − 8 = −3."},
    ]),

    Ievadi("Pieļaujamās vērtības", [
        {"jaut": "√(x − 3) ir jēga, ja x ≥ ?",
         "atb": ["3"], "padoms": "x − 3 ≥ 0."},
        {"jaut": "√(2x + 8) ir jēga, ja x ≥ ?",
         "atb": ["−4", "-4"], "padoms": "2x ≥ −8."},
        {"jaut": "√(6 − x) ir jēga, ja x ≤ ?",
         "atb": ["6"], "padoms": "−x ≥ −6."},
        {"jaut": "Mazākā x vērtība, kurai √(x + 5) ir jēga?",
         "atb": ["−5", "-5"], "padoms": "√0 = 0."},
    ]),

    Pasaule("Kvadrāts ar dotu laukumu",
            Ievadi("", [
                {"jaut": "Dārza laukums S = 60 − 4x (m²). Kad vēl var būt "
                         "kvadrāts? x ≤ ?",
                 "atb": ["15"], "padoms": "60 − 4x ≥ 0."},
                {"jaut": "Ja x = 6, kāda ir kvadrāta mala (m)?",
                 "atb": ["6"], "padoms": "√36."},
                {"jaut": "Ja x = 11, kāda ir mala (m)?",
                 "atb": ["4"], "padoms": "√16."},
            ]),
            pavediens="maja",
            konteksts="Formula var dot jebkuru skaitli, bet mala eksistē "
                      "tikai tad, ja laukums nav negatīvs.",
            kapec="Nosacījums pasaka, kuras vērtības ir reālas.",
            zimejums=taisne(10, 20, 1, [(15, "15")],
                            intervali=[(None, 15, False, True)])),

    Kopsavilkums([
        "Zinu, ka negatīvam skaitlim kvadrātsaknes nav.",
        "Atšķiru √(−9) no −√9.",
        "Atrodu mainīgā vērtības, kurām sakne ir definēta.",
    ]),

    Majas([
        "Nosaki, kurām ir jēga: √(−16), −√16, √((−4)^2), √(1 − 10).",
        "Atrodi pieļaujamās vērtības: √(x + 7), √(12 − 3x).",
        "Pamēģini kalkulatorā √(−1) un pieraksti, ko tas rāda.",
    ]),
]
