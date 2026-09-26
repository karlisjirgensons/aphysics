# -*- coding: utf-8 -*-
"""1. klase, 170. stunda: «Cik veikli rēķinu 20 apjomā?»

Formatīva pārbaude: saskaitīšana un atņemšana 20 apjomā, ar un bez
pāriešanas. Skolēns pats atzīmē, kas vēl jātrenē.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, ramis)

TEMA = "Cik veikli rēķinu 20 apjomā?"

MERKIS = ("Šodien pārbaudīsim savu veiklību 20 apjomā un atzīmēsim, kas vēl "
          "jātrenē.")

SATURS = [
    Sakums("Cik piemēru atrisināsi pareizi?",
           zimejums=ramis(20, 2, otra=10),
           paraksts="20 - divi pilni desmiti.",
           fakti=["Risini pats.",
                  "Pārbaudi ar pretējo darbību.",
                  "Pieraksti, kas bija grūti."]),

    Doma("Pašpārbaude",
         "Svarīgi nav tikai ātri, bet pareizi - un zināt, ko trenēt.",
         soli=[
             "Risini visus piemērus.",
             "Pārbaudi katru.",
             "Atzīmē, kuri bija grūti.",
         ]),

    Ievadi("Bez pāriešanas", [
        {"jaut": "12 + 5", "atb": ["17"], "padoms": "2 + 5."},
        {"jaut": "18 − 6", "atb": ["12"], "padoms": "8 − 6."},
        {"jaut": "14 + 4", "atb": ["18"], "padoms": "4 + 4."},
        {"jaut": "19 − 9", "atb": ["10"], "padoms": "9 − 9."},
    ]),

    Ievadi("Ar pāriešanu", [
        {"jaut": "8 + 5", "atb": ["13"], "padoms": "8 + 2 + 3."},
        {"jaut": "7 + 9", "atb": ["16"], "padoms": "9 + 1 + 6."},
        {"jaut": "14 − 6", "atb": ["8"], "padoms": "14 − 4 − 2."},
        {"jaut": "12 − 9", "atb": ["3"], "padoms": "9 + 3 = 12."},
        {"jaut": "6 + 6", "atb": ["12"], "padoms": "Dubultais."},
        {"jaut": "15 − 7", "atb": ["8"], "padoms": "7 + 8 = 15."},
    ], pamats=4),

    Ievadi("Nezināmais", [
        {"jaut": "9 + ? = 14", "atb": ["5"], "padoms": "14 − 9."},
        {"jaut": "? − 8 = 7", "atb": ["15"], "padoms": "7 + 8."},
    ]),

    Petijums("Mana trenēšanas lapa", [
        "Pieraksti piemērus, kuros kļūdījies.",
        "Pie katra - kāds paņēmiens palīdzētu.",
        "Izdomā vēl 3 līdzīgus un atrisini.",
    ], vajag="lapa, zīmulis"),

    Pasaule("Sporta punkti",
            Ievadi("", [
                {"jaut": "Tava komanda: 9 un 8 punkti. Cik kopā?",
                 "atb": ["17"], "padoms": "9 + 1 + 7."},
            ]),
            pavediens="sports",
            konteksts="Sporta dienā skaita punktus ātri.",
            kapec="Veikls rēķins - ātrs rezultāts."),

    Kopsavilkums([
        "Pārbaudīju savu veiklību 20 apjomā.",
        "Zinu, kas vēl jātrenē.",
        "Pārbaudu savas atbildes.",
    ]),

    Majas([
        "Vasarā reizi nedēļā atrisini 10 piemērus.",
        "Spēlē kauliņu spēles.",
        "Trenē piemērus no savas lapas.",
    ]),
]
