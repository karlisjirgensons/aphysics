# -*- coding: utf-8 -*-
"""7. klase, 160. stunda: «Kas ir divkārša nevienādība?»

Divkārša nevienādība a < x < b nozīmē divas nevienādības vienlaikus:
x > a UN x < b. To var atrisināt, darot vienu un to pašu visām trim daļām.
Atrisinājums ir intervāls starp diviem galiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kas ir divkārša nevienādība?"

MERKIS = ("Pierakstīsim divkāršu nevienādību kā nevienādību sistēmu un "
          "atrisināsim to.")

SATURS = [
    Sakums("Bagāža: no 5 līdz 23 kg",
           zimejums=taisne(0, 30, 5, intervali=[(5, 23, False, True)]),
           paraksts="5 < m ≤ 23: abas prasības vienlaikus.",
           fakti=["Divkārša nevienādība = divas prasības.",
                  "m > 5 UN m ≤ 23.",
                  "Atrisinājums - intervāls (5; 23]."]),

    Doma("Visām trim daļām",
         "Divkāršā nevienādība a < x < b ir sistēma {x > a; x < b}. To "
         "atrisina, visām trim daļām pieskaitot, atņemot, reizinot vai dalot "
         "ar vienu un to pašu skaitli (ar negatīvu - abas zīmes mainās).",
         soli=[
             "Pieraksti trīs daļas: kreisā < vidējā < labā.",
             "Vidū atstāj tikai x: darbības visām daļām.",
             "Ja dala ar negatīvu - abas zīmes mainās, pārraksti no mazākā.",
             "Pieraksti intervālu.",
         ]),

    Paraugs("Atrisini",
            uzd="Atrisini −1 < 2x + 3 ≤ 9.",
            soli=[
                ("−4 < 2x ≤ 6", "(− 3 visām daļām)"),
                ("−2 < x ≤ 3", "(: 2 visām daļām)"),
                ("x ∈ (−2; 3]", "Intervāls."),
            ],
            atbilde="x ∈ (−2; 3]"),

    Zimejums("−2 < x ≤ 3",
             taisne(-4, 5, 1, intervali=[(-2, 3, False, True)]),
             paskaidro="Veseli atrisinājumi: −1; 0; 1; 2; 3."),

    Ievadi("Atrisini", [
        {"jaut": "3 < x + 2 < 8. Mazākā vesela x vērtība?",
         "atb": ["2"], "padoms": "1 < x < 6."},
        {"jaut": "Tai pašai - lielākā vesela x vērtība?",
         "atb": ["5"], "padoms": "x < 6."},
        {"jaut": "−6 ≤ 3x ≤ 12. Cik veselu x?",
         "atb": ["7"], "padoms": "−2 ≤ x ≤ 4."},
        {"jaut": "1 < 5 − x < 4. Mazākā vesela x vērtība?",
         "atb": ["2"], "padoms": "−4 < −x < −1 ⇒ 1 < x < 4."},
    ]),

    Varianti("Pieraksts", [
        {"jaut": "x ≥ −3 un x < 2 - viena nevienādība?",
         "opcijas": ["−3 ≤ x < 2", "−3 < x ≤ 2", "2 < x ≤ −3",
                     "−3 ≥ x > 2"],
         "pareizi": 0, "padoms": "Mazākais pa kreisi."},
        {"jaut": "Vai 5 < x < 2 ir atrisinājumi?",
         "opcijas": ["Nav - neviens skaitlis", "Ir - 3; 4",
                     "Ir - visi", "Ir - 5 un 2"],
         "pareizi": 0, "padoms": "Lielāks par 5 un mazāks par 2."},
    ]),

    Pasaule("Veselīgs pulss",
            Ievadi("", [
                {"jaut": "Treniņā pulsam jābūt 60-80 % no maksimālā (200). "
                         "Apakšējā robeža (sitieni/min)?",
                 "atb": ["120"], "padoms": "0,6 · 200."},
                {"jaut": "Augšējā robeža?",
                 "atb": ["160"], "padoms": "0,8 · 200."},
                {"jaut": "Pulss 155 - vai zonā? Raksti «jā» vai «nē».",
                 "atb": ["jā", "ja"], "padoms": "120 ≤ 155 ≤ 160."},
            ]),
            pavediens="sports",
            konteksts="Sporta pulksteņi rāda pulsa zonas - tās ir divkāršas "
                      "nevienādības.",
            kapec="Zona = intervāls starp divām robežām."),

    Kopsavilkums([
        "Zinu, ka divkārša nevienādība ir divas prasības vienlaikus.",
        "Atrisinu, darot vienu darbību visām trim daļām.",
        "Pierakstu atbildi kā intervālu.",
        "Saskaitu veselos atrisinājumus.",
    ]),

    Majas([
        "Atrisini: −3 ≤ 2x − 1 < 5.",
        "Aprēķini savu pulsa zonu (maksimālais ≈ 220 − vecums).",
        "Atrodi dzīvē divkāršu nevienādību.",
    ]),
]
