# -*- coding: utf-8 -*-
"""2. klase, 133. stunda: «Par 2 lielāks vai 2 reizes lielāks?»

Divas līdzīgas frāzes, divas dažādas darbības: «par 2 lielāks» ir + 2,
«2 reizes lielāks» ir · 2. Sloksņu zīmējumā atšķirība redzama uzreiz: vienā
- pieliek 2 rūtiņas, otrā - vēl vienu tikpat garu sloksni.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, sloksnes)

TEMA = "Par 2 lielāks vai 2 reizes lielāks?"

MERKIS = ("Šodien nošķirsim «par 2 lielāks» no «2 reizes lielāks» "
          "shematiskā zīmējumā.")

_DARB = ["+ 2", "· 2"]

SATURS = [
    Sakums("Annai 6 konfektes. Kam vairāk - «par 2 vairāk» vai «2 reizes "
           "vairāk»?",
           zimejums=sloksnes([("Anna", 6, "6"), ("par 2", 8, "8"),
                              ("2 reizes", 12, "12")]),
           paraksts="6 + 2 = 8, bet 6 · 2 = 12.",
           fakti=["«Par 2» - pieskaita 2.",
                  "«2 reizes» - reizina ar 2.",
                  "Vārdi līdzīgi, rezultāti dažādi!"]),

    Doma("Par cik vai cik reizes",
         "«Par» - saskaitīšana vai atņemšana; «reizes» - reizināšana vai "
         "dalīšana.",
         soli=[
             "Par 2 lielāks: + 2.",
             "Par 2 mazāks: − 2.",
             "2 reizes lielāks: · 2.",
             "2 reizes mazāks: : 2.",
         ]),

    Slidnis("Salīdzinām no 5", [
        {"v": "5", "teksts": "Dotā sloksne.",
         "zim": sloksnes([("dotā", 5, "5")])},
        {"v": "5 + 2 = 7", "teksts": "Par 2 lielāka - pieliek 2 rūtiņas.",
         "zim": sloksnes([("dotā", 5, "5"), ("par 2", 7, "7")])},
        {"v": "5 · 2 = 10", "teksts": "2 reizes lielāka - vēl tikpat.",
         "zim": sloksnes([("dotā", 5, "5"), ("2 reizes", 10, "10")])},
    ]),

    Varianti("Kura darbība?", [
        {"jaut": "Par 2 lielāks nekā 9", "opcijas": _DARB, "jaukt": False,
         "pareizi": 0, "padoms": "«Par»."},
        {"jaut": "2 reizes lielāks nekā 9", "opcijas": _DARB,
         "jaukt": False, "pareizi": 1, "padoms": "«Reizes»."},
        {"jaut": "Brālim par 2 gadiem vairāk nekā man", "opcijas": _DARB,
         "jaukt": False, "pareizi": 0, "padoms": "«Par»."},
        {"jaut": "Tēvs 2 reizes smagāks nekā es", "opcijas": _DARB,
         "jaukt": False, "pareizi": 1, "padoms": "«Reizes»."},
    ]),

    Ievadi("Aprēķini", [
        {"jaut": "Par 2 lielāks nekā 9?", "atb": ["11"], "padoms": "9 + 2."},
        {"jaut": "2 reizes lielāks nekā 9?", "atb": ["18"],
         "padoms": "9 · 2."},
        {"jaut": "Par 2 mazāks nekā 16?", "atb": ["14"], "padoms": "16 − 2."},
        {"jaut": "2 reizes mazāks nekā 16?", "atb": ["8"],
         "padoms": "16 : 2."},
        {"jaut": "2 reizes lielāks nekā 30?", "atb": ["60"],
         "padoms": "30 + 30."},
        {"jaut": "Par 2 lielāks nekā 30?", "atb": ["32"], "padoms": "30 + 2."},
    ], pamats=4),

    Pasaule("Kabatas nauda",
            Ievadi("", [
                {"jaut": "Tev nedēļā 5 €. Māsai par 2 € vairāk. Cik māsai?",
                 "atb": ["7"], "mers": "€", "padoms": "5 + 2."},
                {"jaut": "Brālim 2 reizes vairāk nekā tev. Cik brālim?",
                 "atb": ["10"], "mers": "€", "padoms": "5 · 2."},
            ]),
            pavediens="veikals",
            konteksts="Ģimenē katram bērnam ir sava kabatas nauda.",
            kapec="Viens vārds - «par» vai «reizes» - maina rezultātu."),

    Kopsavilkums([
        "Atšķiru «par 2» no «2 reizes».",
        "Attēloju abus ar sloksnēm.",
        "Izvēlos pareizo darbību.",
    ]),

    Majas([
        "Izdomā 2 teikumus ar «par 2 vairāk» un 2 ar «2 reizes vairāk».",
        "Lai mājinieks pasaka darbību.",
        "Uzzīmē vienam sloksnes.",
    ]),
]
