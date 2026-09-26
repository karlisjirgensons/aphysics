# -*- coding: utf-8 -*-
"""1. klase, 112. stunda: «Palielināt vai pamazināt?»

Palielināt par n - pieskaitīt; pamazināt par n - atņemt. Vārdi situācijā
(uzauga, atlaide, vecāks, atdeva) pasaka, kuru darbību izvēlēties.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti)

TEMA = "Palielināt vai pamazināt?"

MERKIS = ("Šodien izvēlēsimies pareizo darbību situācijā, kurā lielumu "
          "palielina vai pamazina.")

SATURS = [
    Sakums("Cena bija 15 €, atlaide 4 €. Palielināt vai pamazināt?",
           fakti=["Atlaide - cena kļūst mazāka: 15 − 4.",
                  "Uzauga, pielika, atnāca - palielina: «+».",
                  "Atdeva, nogrieza, apēda - pamazina: «−»."]),

    Doma("Vārdi, kas palīdz",
         "Izlasi, kas notiek ar lielumu - tas kļūst lielāks vai mazāks?",
         soli=[
             "Lielāks: palielināja, pieauga, pielika, vecāks.",
             "Mazāks: pamazināja, atlaide, nogrieza, jaunāks.",
             "Izvēlies «+» vai «−» un aprēķini.",
         ]),

    Varianti("Palielināt vai pamazināt?", [
        {"jaut": "Temperatūra bija 8 grādi, pieauga par 5.",
         "opcijas": ["8 + 5", "8 − 5"], "jaukt": False, "pareizi": 0,
         "padoms": "Pieauga - lielāks."},
        {"jaut": "Aukla 16 cm, nogrieza 7 cm.",
         "opcijas": ["16 − 7", "16 + 7"], "jaukt": False, "pareizi": 0,
         "padoms": "Nogrieza - mazāks."},
        {"jaut": "Kucēns svēra 9 kg, pieņēmās svarā par 3 kg.",
         "opcijas": ["9 + 3", "9 − 3"], "jaukt": False, "pareizi": 0,
         "padoms": "Pieņēmās - lielāks."},
        {"jaut": "Grāmata 18 €, atlaide 6 €.",
         "opcijas": ["18 − 6", "18 + 6"], "jaukt": False, "pareizi": 0,
         "padoms": "Atlaide - mazāks."},
    ]),

    Ievadi("Aprēķini", [
        {"jaut": "8 grādi, pieauga par 5. Cik tagad?", "atb": ["13"],
         "padoms": "8 + 5."},
        {"jaut": "16 cm aukla, nogrieza 7 cm. Cik palika?", "atb": ["9"],
         "padoms": "16 − 7."},
        {"jaut": "Grāmata 18 €, atlaide 6 €. Jaunā cena?", "atb": ["12"],
         "padoms": "18 − 6."},
    ]),

    Pasaule("Istabas augs",
            Ievadi("", [
                {"jaut": "Puķe bija 11 cm, nedēļā izauga par 4 cm. Cik "
                         "augsta?", "atb": ["15"], "padoms": "11 + 4."},
                {"jaut": "Nogrieza 3 cm sausās lapas. Cik tagad?",
                 "atb": ["12"], "padoms": "15 − 3."},
            ]),
            pavediens="daba",
            konteksts="Klasē aug puķe, un to mēra katru nedēļu.",
            kapec="Vārdi «izauga» un «nogrieza» pasaka darbību."),

    Kopsavilkums([
        "Atpazīstu palielināšanu un pamazināšanu.",
        "Izvēlos «+» vai «−».",
        "Aprēķinu jauno lielumu.",
    ]),

    Majas([
        "Atrodi reklāmā atlaidi un aprēķini jauno cenu.",
        "Izmēri augu mājās un pēc nedēļas vēlreiz.",
        "Par cik tas palielinājās?",
    ]),
]
