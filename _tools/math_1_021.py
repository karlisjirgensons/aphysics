# -*- coding: utf-8 -*-
"""1. klase, 21. stunda: «Ko nozīmē 0?»

0 nozīmē «necik» - tukša roka, tukša bļoda. Mājiņā tas dod divus jaunus
stāvus: 0 un 5, 5 un 0. Pieskaitot vai atņemot 0, skaitlis nemainās.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, bildes, majina)

TEMA = "Ko nozīmē 0?"

MERKIS = ("Šodien iemācīsimies, ko nozīmē 0, un pierakstīsim sadalījumu, "
          "kurā viena daļa ir tukša.")

SATURS = [
    Sakums("Visas 5 ripiņas izbira violetas - cik oranžu?",
           zimejums=bildes([[("ripina", 5)]]),
           paraksts="5 violetas un 0 oranžu.",
           fakti=["0 nozīmē - necik, nav neviena.",
                  "Arī tukša roka ir daļa.",
                  "5 un 0 ir 5."]),

    Doma("Nulle mājiņā",
         "Ar nulli mājiņai rodas divi jauni stāvi: 0 un skaitlis, skaitlis "
         "un 0.",
         soli=[
             "Visi vienā rokā, otra tukša: 5 un 0.",
             "Otrādi: 0 un 5.",
             "Tagad skaitlim 5 ir 6 stāvi.",
         ],
         pieze="Ja pieskaita vai atņem 0, skaitlis nemainās."),

    Ievadi("Nulle", [
        {"jaut": "Kurš skaitlis trūkst?",
         "zim": majina(5, [(0, None), (1, 4), (2, 3)]), "atb": ["5"],
         "padoms": "0 un vēl cik ir 5?"},
        {"jaut": "Kurš skaitlis trūkst?", "zim": majina(4, [(None, 4)]),
         "atb": ["0"], "padoms": "Visi jau labajā pusē."},
        {"jaut": "Cik ābolu ir tukšā bļodā?", "atb": ["0"],
         "padoms": "Nav neviena."},
        {"jaut": "Cik stāvu ir skaitļa 5 mājiņai ar 0?", "atb": ["6"],
         "padoms": "4 stāvi un vēl 2."},
    ]),

    Varianti("Patiess?", [
        {"jaut": "7 un 0 ir 7.", "opcijas": ["Patiess", "Aplams"],
         "jaukt": False, "pareizi": 0, "padoms": "Nekas netika pielikts."},
        {"jaut": "0 un 3 ir 0.", "opcijas": ["Patiess", "Aplams"],
         "jaukt": False, "pareizi": 1, "padoms": "Nekas un 3 ir 3."},
        {"jaut": "Tukšā penālī ir 0 zīmuļu.", "opcijas": ["Patiess",
                                                          "Aplams"],
         "jaukt": False, "pareizi": 0, "padoms": "Nav neviena."},
    ]),

    Pasaule("Punkti spēlē",
            Ievadi("", [
                {"jaut": "Pirmajā kārtā Liene ieguva 0 punktu, otrajā - 4. "
                         "Cik kopā?", "atb": ["4"], "padoms": "0 un 4."},
                {"jaut": "Mārtiņš ieguva 6 un 0. Cik kopā?", "atb": ["6"],
                 "padoms": "6 un nekas."},
            ]),
            pavediens="speles",
            konteksts="Spēlē par katru kārtu var dabūt arī 0 punktu.",
            kapec="0 ir skaitlis - tas nozīmē «neko neieguva»."),

    Kopsavilkums([
        "Zinu, ka 0 nozīmē necik.",
        "Pierakstu sadalījumus ar 0 mājiņā.",
        "Zinu, ka pieskaitot 0, skaitlis nemainās.",
    ]),

    Majas([
        "Atrodi mājās kaut ko, kā ir 0 (piem., sniega vasarā).",
        "Uzzīmē skaitļa 6 mājiņu ar 0.",
        "Paslēp visas 5 pogas vienā rokā - cik otrā?",
    ]),
]
