# -*- coding: utf-8 -*-
"""1. klase, 28. stunda: «Kā pastāstīt citam, ko izdarīji?»

Stāsta pēc savas tabulas: ko darīja, kā pierakstīja un kā zina, ka atrasti
visi veidi. Labs stāsts ir pēc kārtas - «vispirms, tad, beigās».
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Pasaule, Petijums,
                         Sakums, Varianti, restis)

TEMA = "Kā pastāstīt citam, ko izdarīji?"

MERKIS = ("Šodien pastāstīsim pēc savas tabulas, kā atradām visus veidus.")

_TABULA = restis([["V", "O"], [0, 4], [1, 3], [2, 2], [3, 1], [4, 0]])

SATURS = [
    Sakums("Kā pastāstīt, ka esi atradis visus veidus?",
           zimejums=_TABULA,
           paraksts="Visi skaitļa 4 sadalījumi - pēc kārtas.",
           fakti=["Stāsti pēc kārtas: vispirms, tad, beigās.",
                  "Rādi tabulā, par ko runā.",
                  "Pastāsti, kā zini, ka nekā netrūkst."]),

    Doma("Stāsts pēc tabulas",
         "Labs stāsts pasaka, ko darīji, kā pierakstīji un kāpēc tas ir "
         "viss.",
         soli=[
             "Vispirms: ko darīju (izbēru ripiņas, dalīju klucīšus).",
             "Tad: kā pierakstīju (tabula ar divām ailēm).",
             "Beigās: kāpēc visi veidi atrasti (kreisā aile 0, 1, 2, 3, 4).",
         ]),

    Varianti("Kurš stāsts labāks?", [
        {"jaut": "Kurš stāsts labāk izskaidro tabulu?", "zim": _TABULA,
         "opcijas": ["Sāku ar 0 kreisajā ailē un liku par 1 vairāk, līdz 4",
                     "Es kaut ko sarakstīju",
                     "Tur ir skaitļi"],
         "pareizi": 0, "padoms": "Kurš pastāsta, kā?"},
        {"jaut": "Kā zināt, ka visi 4 sadalījumi atrasti?",
         "opcijas": ["kreisajā ailē ir 0, 1, 2, 3, 4 - bez cauruma",
                     "tabula ir gara", "tā teica draugs"],
         "pareizi": 0, "padoms": "Pēc kārtas un bez cauruma."},
        {"jaut": "Kurš vārds palīdz stāstīt pēc kārtas?",
         "opcijas": ["vispirms", "varbūt", "skaisti"], "pareizi": 0,
         "padoms": "Vispirms, tad, beigās."},
    ]),

    Petijums("Pastāsti pārim", [
        "Paņem savu tabulu no iepriekšējām stundām.",
        "Pastāsti pārim: vispirms, tad, beigās.",
        "Pāris jautā vienu jautājumu par tabulu.",
        "Mainieties lomām.",
    ], vajag="tava tabula"),

    Pasaule("Ziņojums skolotājai",
            Varianti("", [
                {"jaut": "Tu skaitīji, cik bērnu nāk kājām un cik ar "
                         "autobusu. Ko pateikt vispirms?",
                 "opcijas": ["ko es skaitīju", "cik bija kopā",
                             "kas bija grūti"],
                 "pareizi": 0, "padoms": "Sāc ar to, ko darīji."},
            ]),
            pavediens="skola",
            konteksts="Skolotāja lūdz pastāstīt klasei par tavu pētījumu.",
            kapec="Kas stāsta pēc kārtas, to saprot visi."),

    Kopsavilkums([
        "Stāstu pēc tabulas: vispirms, tad, beigās.",
        "Paskaidroju, kā zinu, ka visi veidi atrasti.",
        "Uzklausu pāri un uzdodu jautājumu.",
    ]),

    Majas([
        "Pastāsti mājiniekiem, kā sadalīji 5 ripiņas.",
        "Parādi viņiem savu tabulu.",
        "Pajautā: vai viņi saprata?",
    ]),
]
