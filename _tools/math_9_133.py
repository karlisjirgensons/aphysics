# -*- coding: utf-8 -*-
"""9. klase, 133. stunda: «Kāda ir vidējā locekļa īpašība?»

Katrs loceklis (izņemot pirmo) ir kaimiņu vidējais aritmētiskais:
a_k = {a_{k−1} + a_{k+1}|2} (formulu lapā). No tā - progresijas pazīme un
ātrs veids atrast «trūkstošo» locekli.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, taisne)

TEMA = "Kāda ir vidējā locekļa īpašība?"

MERKIS = ("Lietosim īpašību, ka katrs loceklis ir kaimiņu vidējais "
          "aritmētiskais.")

SATURS = [
    Sakums("Kas ir pa vidu starp 8 un 20?",
           zimejums=taisne(6, 22, 2, atzimes=[(8, "a₁"), (14, "a₂ = ?"),
                                               (20, "a₃")],
                           bultas=[(8, 14, "d"), (14, 20, "d")]),
           paraksts="Vienādi soļi - vidējais ir tieši pa vidu: 14.",
           fakti=["a_2 = {8 + 20|2} = 14.",
                  "Katrs loceklis - kaimiņu vidējais.",
                  "Tā ir arī progresijas pazīme."]),

    Doma("Vidējā locekļa īpašība",
         "Aritmētiskajā progresijā aₖ = {aₖ₋₁ + aₖ₊₁|2}; un otrādi - "
         "ja tā ir katram loceklim, virkne ir aritmētiskā progresija.",
         soli=[
             "Kaimiņus saskaita un dala ar 2.",
             "Der arī simetriskiem: aₖ = {aₖ₋ₘ + aₖ₊ₘ|2}.",
             "Pārbaudei: 2a_2 = a_1 + a_3.",
         ]),

    Paraugs("Atrodi x",
            uzd="Skaitļi 2x − 1, x + 5 un 3x + 1 ir progresijas secīgi "
                "locekļi. Atrodi x.",
            soli=[
                ("2(x + 5) = (2x − 1) + (3x + 1)", "Vidējā locekļa īpašība."),
                ("2x + 10 = 5x ⇒ x = {10|3}", "Atrisina."),
            ],
            atbilde="x = {10|3}"),

    Ievadi("Aprēķini", [
        {"jaut": "a_4 = 13, a_6 = 21. a_5 = ?", "atb": ["17"],
         "padoms": "{13 + 21|2}."},
        {"jaut": "a_2 = −4, a_4 = 10. a_3 = ?", "atb": ["3"],
         "padoms": "{6|2}."},
        {"jaut": "a_3 = 7, a_9 = 25. a_6 = ?", "atb": ["16"],
         "padoms": "Simetriski: {7 + 25|2}."},
        {"jaut": "x, 10, 16 - progresija. x = ?", "atb": ["4"],
         "padoms": "20 = x + 16."},
    ]),

    Varianti("Vai progresija?", [
        {"jaut": "3, 7, 11: vai 7 = {3 + 11|2}?",
         "opcijas": ["Jā - progresija", "Nē"], "jaukt": False,
         "pareizi": 0, "padoms": "14 : 2 = 7."},
        {"jaut": "4, 9, 16: vai 9 = {4 + 16|2}?",
         "opcijas": ["Jā - progresija", "Nē"], "jaukt": False,
         "pareizi": 1, "padoms": "10 ≠ 9."},
    ]),

    Pasaule("Tilta balsti",
            Ievadi("", [
                {"jaut": "Tilta vanšu garumi aug vienmērīgi. 3. vants 18 m, "
                         "5. vants 26 m. Cik garš 4. vants (m)?",
                 "atb": ["22"], "padoms": "{18 + 26|2}."},
                {"jaut": "Cik garš 6. vants?", "atb": ["30"], "padoms": "d = 4."},
            ]),
            pavediens="tehnika",
            konteksts="Vanšu tiltos troses no pilona iet uz tilta klāju "
                      "vienmērīgi garākas.",
            kapec="Vidējais aritmētiskais dod trūkstošo garumu."),

    Kopsavilkums([
        "Lietoju a_k = (kaimiņu summa) : 2.",
        "Atrodu trūkstošo locekli.",
        "Pārbaudu, vai trīs skaitļi veido progresiju.",
    ]),

    Majas([
        "Atrodi x: x + 2, 3x, 4x + 1 - progresijas locekļi.",
        "Vai 5, 12, 19 ir progresija? Pamato ar vidējo.",
        "Izdomā trīs skaitļus, kas veido progresiju ar d = −7.",
    ]),
]
