# -*- coding: utf-8 -*-
"""9. klase, 140. stunda: «Kur vēl sastopamas virknes?»

Virknes ap mums: aritmētiskās (kāpnes, grafiki, sēdvietas), ģeometriskās
(baktērijas, procenti, papīra locīšana), Fibonači (augi). Skolēns
klasificē virknes un salīdzina, cik ātri tās aug.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, plakne, restis)

TEMA = "Kur vēl sastopamas virknes?"

MERKIS = ("Minēsim piemērus par virknēm dabā un tehnikā un raksturosim "
          "tās.")

SATURS = [
    Sakums("Papīru pārloka 42 reizes - līdz Mēnesim?",
           zimejums=restis([["locījumi", "0", "1", "2", "10", "42"],
                            ["biezums", "0,1 mm", "0,2 mm", "0,4 mm",
                             "~10 cm", "~440 000 km"]]),
           paraksts="Katrs locījums dubulto biezumu: 0,1 · 2ⁿ mm.",
           fakti=["Tā ir ģeometriskā progresija - katrs reiz 2.",
                  "Aritmētiskā progresija aug daudz lēnāk.",
                  "Mēness ir ~384 000 km attālumā."]),

    Doma("Virkņu veidi",
         "Aritmētiskā - pieskaita d; ģeometriskā - reizina ar q; ir arī "
         "citas (Fibonači, kvadrāti).",
         soli=[
             "Starpības vienādas → aritmētiskā.",
             "Attiecības vienādas → ģeometriskā (pēc izvēles, 10. klase).",
             "Katrs - iepriekšējo divu summa → Fibonači.",
             "Salīdzini augšanas ātrumu ar grafiku.",
         ]),

    Slidnis("Kurš aug ātrāk?", [
        {"v": "+10", "teksts": "Aritmētiskā: 10, 20, 30, 40, 50, 60",
         "zim": plakne(punkti=[(n, 10 * n, "") for n in range(1, 7)],
                       no_x=0, lidz_x=7, no_y=0, lidz_y=70, solis_y=10)},
        {"v": "· 2", "teksts": "Ģeometriskā: 2, 4, 8, 16, 32, 64",
         "zim": plakne(punkti=[(n, 2 ** n, "") for n in range(1, 7)],
                       no_x=0, lidz_x=7, no_y=0, lidz_y=70, solis_y=10)},
    ]),

    Varianti("Kāda virkne?", [
        {"jaut": "Kāpņu pakāpienu augstumi no zemes: 18, 36, 54, 72 cm",
         "opcijas": ["Aritmētiskā", "Ģeometriskā", "Fibonači",
                     "Neviena"],
         "pareizi": 0, "padoms": "+18."},
        {"jaut": "Baktērijas: 100, 200, 400, 800",
         "opcijas": ["Ģeometriskā", "Aritmētiskā", "Fibonači", "Neviena"],
         "pareizi": 0, "padoms": "· 2."},
        {"jaut": "Zaru skaits kokā: 1, 1, 2, 3, 5, 8",
         "opcijas": ["Fibonači", "Aritmētiskā", "Ģeometriskā", "Neviena"],
         "pareizi": 0, "padoms": "Divu iepriekšējo summa."},
        {"jaut": "Olimpiskās spēles: 2024, 2028, 2032",
         "opcijas": ["Aritmētiskā", "Ģeometriskā", "Fibonači", "Neviena"],
         "pareizi": 0, "padoms": "+4."},
    ]),

    Petijums("Virknes ap mani", [
        "Atrodi 3 virknes skolā vai mājās (sēdvietas, kalendārs, cenas).",
        "Pieraksti pirmos 5 locekļus.",
        "Nosaki veidu un, ja var, formulu.",
        "Aprēķini 20. locekli.",
    ], vajag="burtnīca, novērojumi"),

    Ievadi("Aprēķini", [
        {"jaut": "Olimpiskās spēles 2024, 2028, ... Kura gada spēles būs "
                 "10. šajā virknē?", "atb": ["2060"], "padoms": "2024 + 36."},
        {"jaut": "Papīra biezums pēc 10 locījumiem: 0,1 · 1024 mm = ? mm",
         "atb": ["102,4"], "padoms": "2^10 = 1024."},
    ]),

    Pasaule("Saules aptumsumi un komētas",
            Ievadi("", [
                {"jaut": "Haleja komēta tuvojas Saulei aptuveni ik 76 gadus; "
                         "1986. gadā tā bija redzama. Kurā gadā nākamreiz?",
                 "atb": ["2062"], "padoms": "1986 + 76."},
                {"jaut": "Kurā gadā tā bija redzama divas reizes pirms 1986.?",
                 "atb": ["1834"], "padoms": "1986 − 152."},
            ]),
            pavediens="kosmoss",
            konteksts="Periodiskas komētas atgriežas pēc vienāda laika - "
                      "atgriešanās gadi veido aritmētisku progresiju.",
            kapec="Aptuveni - periods nedaudz mainās, bet modelis strādā."),

    Kopsavilkums([
        "Atrodu virknes dabā, tehnikā un ikdienā.",
        "Atšķiru aritmētisko, ģeometrisko un Fibonači virkni.",
        "Salīdzinu, cik ātri virknes aug.",
    ]),

    Majas([
        "Aizpildi pētījumu ar 3 virknēm.",
        "Aprēķini, cik reižu jāpārloka papīrs, lai biezums pārsniegtu 1 m.",
        "Atrodi informāciju par kādu citu periodisku notikumu.",
    ]),
]
