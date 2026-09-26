# -*- coding: utf-8 -*-
"""2. klase, 96. stunda: «Cik soļu vajag mērķim?»

Divus algoritmus, kas nonāk pie tā paša mērķa, salīdzina pēc soļu skaita.
Īsākais ceļš rūtiņās ir tas, kurā nav lieku soļu atpakaļ; skaitļu mašīnā
«+ 30 − 10» ir īsāk rakstīt kā «+ 20». Tēmas noslēgums.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, celjs)

TEMA = "Cik soļu vajag mērķim?"

MERKIS = ("Šodien salīdzināsim divus algoritmus pēc soļu skaita un "
          "izvēlēsimies īsāko.")

SATURS = [
    Sakums("Divi roboti nonāca pie ābola. Kurš bija gudrāks?",
           zimejums=celjs(6, 4, (0, 3), (3, 1), "↑↑↑→→→↓"),
           paraksts="Šim robotam vajadzēja 7 soļus.",
           fakti=["Otrajam pietika ar 5: →→→↑↑.",
                  "Abi nonāca pie mērķa.",
                  "Īsāks algoritms - ātrāk un lētāk."]),

    Doma("Īsākais algoritms",
         "No diviem pareiziem algoritmiem labāks ir tas, kurā mazāk soļu.",
         soli=[
             "Pārbaudi, vai abi nonāk pie mērķa.",
             "Saskaiti soļus katrā.",
             "Meklē liekos soļus: uz augšu un tad uz leju.",
             "Izvēlies īsāko.",
         ]),

    Ievadi("Saskaiti soļus", [
        {"jaut": "Cik soļu šajā ceļā?",
         "zim": celjs(6, 4, (0, 3), (3, 1), "↑↑↑→→→↓"), "atb": ["7"],
         "padoms": "Saskaiti bultiņas."},
        {"jaut": "Cik soļu šajā ceļā?",
         "zim": celjs(6, 4, (0, 3), (3, 1), "→→→↑↑"), "atb": ["5"],
         "padoms": "3 + 2."},
        {"jaut": "Par cik soļiem otrais ceļš īsāks?", "atb": ["2"],
         "padoms": "7 − 5."},
        {"jaut": "Kāds ir mazākais soļu skaits no (0; 0) līdz 4 pa labi un "
                 "3 uz augšu?", "atb": ["7"], "padoms": "4 + 3."},
    ]),

    Varianti("Kurš īsāks?", [
        {"jaut": "Skaitļu mašīna A: + 30, − 10. Mašīna B: + 20. Vai tās "
                 "dara to pašu?", "opcijas": ["Jā, B ir īsāka", "Nē"],
         "jaukt": False, "pareizi": 0, "padoms": "+ 30 − 10 = + 20."},
        {"jaut": "Mašīna A: + 5, + 5, + 5, + 5. Mašīna B: + 20. Kura "
                 "īsāka?", "opcijas": ["B", "A", "vienādas"], "pareizi": 0,
         "padoms": "Viens solis pret četriem."},
        {"jaut": "Mašīna A: − 10, + 4. Kura viena darbība dara to pašu?",
         "opcijas": ["− 6", "+ 6", "− 14"], "pareizi": 0,
         "padoms": "Pamēģini ar skaitli 20."},
    ]),

    Pasaule("Kurjera maršruts",
            Varianti("", [
                {"jaut": "Kurjers var braukt: veikals → skola → māja (3 km + "
                         "4 km) vai veikals → māja → skola (5 km + 4 km). "
                         "Kurš īsāks?",
                 "opcijas": ["pirmais - 7 km", "otrais - 9 km",
                             "vienādi"], "pareizi": 0,
                 "padoms": "3 + 4 un 5 + 4."},
                {"jaut": "Par cik km?", "opcijas": ["2 km", "4 km", "1 km"],
                 "pareizi": 0, "padoms": "9 − 7."},
            ]),
            pavediens="celojums",
            konteksts="Kurjers izvēlas maršrutu ar mazāk kilometriem.",
            kapec="Īsāks maršruts - ātrāka piegāde un mazāk degvielas."),

    Kopsavilkums([
        "Salīdzinu algoritmus pēc soļu skaita.",
        "Atrodu liekos soļus.",
        "Izvēlos īsāko algoritmu.",
    ]),

    Majas([
        "Uzzīmē savu ceļu no istabas līdz virtuvei soļos.",
        "Vai ir īsāks ceļš?",
        "Saskaiti soļus abos.",
    ]),
]
