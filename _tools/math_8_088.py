# -*- coding: utf-8 -*-
"""8. klase, 88. stunda: «Kas ir attālums starp paralēlām taisnēm?»

Attālums starp paralēlām taisnēm ir perpendikula garums; no jebkura
punkta tas ir vienāds. Slīps nogrieznis vienmēr ir garāks. Šis attālums
kļūs par paralelograma un trapeces augstumu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, geometrija)

TEMA = "Kas ir attālums starp paralēlām taisnēm?"

MERKIS = "Definēsim attālumu starp paralēlām taisnēm un mērīsim to."

SATURS = [
    Sakums("Cik tālu ir taisne b no taisnes a?",
           zimejums=geometrija(
               [("_1", -1, 0), ("_2", 8, 0), ("_3", -1, 3), ("_4", 8, 3),
                ("A", 1, 0, 270), ("B", 1, 3, 90), ("C", 5, 0, 270),
                ("D", 5, 3, 90), ("E", 3, 3, 90)],
               taisnes=[("_1", "_2"), ("_3", "_4")],
               nogriezni=["AB", "CD"], izcelti=["AE"],
               taisni=["BAC", "DCA"], malas=[("AB", "d"), ("CD", "d")],
               uzraksti=[(8.3, -0.6, "a"), (8.3, 3.4, "b")]),
           paraksts="Perpendikuli AB un CD ir vienādi; slīpais AE ir garāks.",
           fakti=["Attālums starp paralēlām taisnēm ir perpendikula garums.",
                  "No jebkura punkta tas ir vienāds.",
                  "Slīps nogrieznis vienmēr ir garāks par perpendikulu."]),

    Doma("Kā mēra attālumu",
         "Attālumu mēra pa perpendikulu - tas ir īsākais ceļš.",
         soli=[
             "Izvēlies jebkuru punktu uz vienas taisnes.",
             "Ar stūreni novelc perpendikulu pret otru taisni.",
             "Izmēri perpendikula garumu.",
             "Paralelogramā un trapecē šis attālums ir augstums.",
         ]),

    Varianti("Spried", [
        {"jaut": "Kurš nogrieznis ir attālums starp a un b?",
         "opcijas": ["Perpendikuls starp taisnēm", "Jebkurš slīps nogrieznis",
                     "Garākais nogrieznis", "Taisnes garums"],
         "pareizi": 0, "padoms": "AB vai CD zīmējumā."},
        {"jaut": "Vai attālums mainās, ja mēra citā vietā?",
         "opcijas": ["Nē", "Jā", "Palielinās pa labi",
                     "Atkarīgs no leņķa"],
         "pareizi": 0, "padoms": "AB = CD."},
        {"jaut": "Slīps nogrieznis starp taisnēm ir 5 cm. Attālums var būt...",
         "opcijas": ["4 cm", "5 cm", "6 cm", "7 cm"],
         "pareizi": 0, "padoms": "Perpendikuls ir īsāks par slīpo."},
    ]),

    Ievadi("Aprēķini", [
        {"jaut": "a ∥ b, attālums 4 cm. Trijstūrim viena mala 6 cm uz a, "
                 "virsotne uz b. Laukums (cm²)?", "atb": ["12"],
         "padoms": "Augstums = 4."},
        {"jaut": "Paralelograma mala 10 cm uz a, pretējā uz b, attālums "
                 "3 cm. Laukums (cm²)?", "atb": ["30"],
         "padoms": "10 · 3."},
        {"jaut": "a ∥ b ∥ c; a-b ir 5 cm, b-c ir 3 cm, b atrodas starp tām. "
                 "Attālums a-c (cm)?", "atb": ["8"], "padoms": "5 + 3."},
        {"jaut": "c ir starp a un b; a-c ir 2 cm, a-b ir 7 cm. Attālums c-b "
                 "(cm)?", "atb": ["5"], "padoms": "7 − 2."},
    ]),

    Pasaule("Futbola laukums",
            Ievadi("", [
                {"jaut": "Sānu līnijas ir paralēlas, attālums 68 m. Cik m "
                         "noskrien, skrienot perpendikulāri no vienas līdz "
                         "otrai?",
                 "atb": ["68"], "padoms": "Perpendikuls = attālums."},
                {"jaut": "Skrienot slīpi, ceļš ir... (1 - garāks, 2 - īsāks)",
                 "atb": ["1"], "padoms": "Slīpais garāks."},
                {"jaut": "Laukuma garums 105 m. Laukums (m²)?",
                 "atb": ["7140"], "padoms": "105 · 68."},
            ]),
            pavediens="sports",
            konteksts="Laukuma platums ir attālums starp sānu līnijām - to "
                      "mēra perpendikulāri.",
            kapec="Perpendikuls ir īsākais ceļš starp paralēlām taisnēm."),

    Kopsavilkums([
        "Definēju attālumu starp paralēlām taisnēm.",
        "Izmēru to ar stūreni un lineālu.",
        "Saistu attālumu ar augstumu laukuma formulās.",
    ]),

    Majas([
        "Izmēri attālumu starp burtnīcas līnijām trīs vietās.",
        "Izmēri attālumu starp galda malām un pārbaudi, vai tās paralēlas.",
        "Uzzīmē trīs paralēlas taisnes ar attālumiem 2 cm un 3 cm.",
    ]),
]
