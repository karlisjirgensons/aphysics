# -*- coding: utf-8 -*-
"""1. klase, 117. stunda: «Cik kopā un cik katram?»

Daļa-daļa-viss: ja zina abas daļas - saskaita; ja zina visu un vienu daļu
- atņem. Skaitļa mājiņa rāda, kas ir viss un kas daļas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, majina)

TEMA = "Cik kopā un cik katram?"

MERKIS = ("Šodien risināsim uzdevumus par «cik kopā», «cik vienam», «cik "
          "otram».")

SATURS = [
    Sakums("Kopā 15 ābolu, Annai 9. Cik Jānim?",
           zimejums=majina(15, [(9, None)]),
           paraksts="Viss 15, viena daļa 9 - otra: 15 − 9 = 6.",
           fakti=["Abas daļas zināmas - saskaiti.",
                  "Viss un viena daļa - atņem.",
                  "Mājiņa parāda, kas ir kas."]),

    Doma("Viss un daļas",
         "Viss ir jumtā, daļas - stāvā.",
         soli=[
             "Atrodi, kas ir «kopā» - tas ir viss.",
             "Atrodi daļas - katram.",
             "Trūkst visa? - Saskaiti. Trūkst daļas? - Atņem.",
         ]),

    Ievadi("Atrisini", [
        {"jaut": "Annai 9, Jānim 6. Cik kopā?",
         "zim": majina(None, [(9, 6)]), "atb": ["15"], "padoms": "9 + 6."},
        {"jaut": "Kopā 15, Annai 9. Cik Jānim?",
         "zim": majina(15, [(9, None)]), "atb": ["6"], "padoms": "15 − 9."},
        {"jaut": "Kopā 17, Jānim 8. Cik Annai?",
         "zim": majina(17, [(None, 8)]), "atb": ["9"], "padoms": "17 − 8."},
        {"jaut": "Zēni 7, meitenes 8. Cik bērnu kopā?", "atb": ["15"],
         "padoms": "7 + 8."},
    ]),

    Varianti("Saskaitīt vai atņemt?", [
        {"jaut": "Klasē 18 bērnu, 10 zēnu. Cik meiteņu?",
         "opcijas": ["18 − 10", "18 + 10"], "jaukt": False, "pareizi": 0,
         "padoms": "Viss un daļa."},
        {"jaut": "Grozā 6 ābolu un 7 bumbieru. Cik augļu?",
         "opcijas": ["6 + 7", "7 − 6"], "jaukt": False, "pareizi": 0,
         "padoms": "Abas daļas."},
    ]),

    Pasaule("Galda spēle divatā",
            Ievadi("", [
                {"jaut": "Abi kopā savāca 16 kārtis. Tev 7. Cik draugam?",
                 "atb": ["9"], "padoms": "16 − 7."},
            ]),
            pavediens="speles",
            konteksts="Pēc spēles skaita kārtis.",
            kapec="Mājiņa palīdz saprast, ko meklēt."),

    Kopsavilkums([
        "Atšķiru visu un daļas.",
        "Saskaitu, ja zināmas daļas.",
        "Atņemu, ja zināms viss un viena daļa.",
    ]),

    Majas([
        "Cik ģimenē ir sieviešu un vīriešu? Cik kopā?",
        "Izdomā uzdevumu par «cik katram».",
        "Uzzīmē tam mājiņu.",
    ]),
]
