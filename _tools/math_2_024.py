# -*- coding: utf-8 -*-
"""2. klase, 24. stunda: «Kā uzbūvēt modeli pēc reāliem izmēriem?»

Tēmas noslēgums: grupa izgatavo mēbeles vai mājas modeli pēc dotiem
izmēriem. Tajā sanāk viss tēmā apgūtais - mērīšana cm un mm, zīmēšana,
saskaitīšana un pārbaude.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, restis)

TEMA = "Kā uzbūvēt modeli pēc reāliem izmēriem?"

MERKIS = ("Šodien grupā izgatavosim objekta modeli pēc dotiem izmēriem un "
          "pārbaudīsim, vai izmēri sakrīt.")

_PLANS = restis([["daļa", "garums", "platums"],
                 ["galda virsma", "12 cm", "8 cm"],
                 ["kāja", "6 cm", "1 cm"],
                 ["plaukts", "12 cm", "4 cm"]])

SATURS = [
    Sakums("Kā arhitekts parāda māju, kas vēl nav uzbūvēta?",
           zimejums=_PLANS,
           paraksts="Rasējumā katrai daļai ir izmēri.",
           fakti=["Pirms būvēt, arhitekts izgatavo mazu modeli.",
                  "Modeli taisa pēc precīziem izmēriem.",
                  "Ja izmērs neder, kļūdu pamana modelī, nevis mājā."]),

    Doma("Modelis pēc plāna",
         "Katru daļu atmēri, izgriez un pārbaudi, pirms salīmē.",
         soli=[
             "Nolasi izmērus no plāna.",
             "Uzzīmē daļas uz kartona ar lineālu.",
             "Izgriez un izmēri vēlreiz.",
             "Salīmē un pārbaudi kopējos izmērus.",
         ]),

    Petijums("Galda modelis", [
        "Pēc plāna uzzīmējiet galda virsmu 12 cm garu un 8 cm platu.",
        "Uzzīmējiet 4 kājas pa 6 cm.",
        "Izgrieziet un salīmējiet.",
        "Izmēriet gatavā galda augstumu. Vai sanāca 6 cm?",
    ], vajag="kartons, lineāls, zīmulis, šķēres, līme",
             secinajums="Ja katra daļa atmērīta precīzi, viss modelis "
                        "sakrīt ar plānu."),

    Ievadi("Rēķini pēc plāna", [
        {"jaut": "Cik cm kartona sloksnes vajag 4 galda kājām pa 6 cm?",
         "zim": _PLANS, "atb": ["24"], "mers": "cm", "padoms": "6 + 6 + 6 + 6."},
        {"jaut": "Par cik cm galda virsma ir garāka nekā platāka?",
         "zim": _PLANS, "atb": ["4"], "mers": "cm", "padoms": "12 − 8."},
        {"jaut": "Plaukts ir 12 cm garš. Kartona sloksne - 20 cm. Cik cm "
                 "paliks pāri?", "zim": _PLANS, "atb": ["8"], "mers": "cm",
         "padoms": "20 − 12."},
        {"jaut": "Cik mm ir galda kājas platums 1 cm?", "zim": _PLANS,
         "atb": ["10"], "mers": "mm", "padoms": "1 cm = 10 mm."},
    ]),

    Varianti("Pārbaudi modeli", [
        {"jaut": "Viena kāja iznāca 5 cm 5 mm. Kas notiks?",
         "opcijas": ["Galds šķobīsies", "Nekas", "Galds būs augstāks"],
         "pareizi": 0, "padoms": "Viena kāja īsāka."},
        {"jaut": "Kā labot?",
         "opcijas": ["Izgriezt jaunu kāju 6 cm", "Nogriezt virsmu",
                     "Pielīmēt vēl vienu kāju"], "pareizi": 0,
         "padoms": "Visām kājām jābūt vienādām."},
    ]),

    Pasaule("Vai gulta ietilps istabas modelī?",
            Ievadi("", [
                {"jaut": "Istabas modelis ir 30 cm garš. Gulta 20 cm, skapis "
                         "8 cm. Cik cm paliek, ja tos noliek gar vienu sienu?",
                 "atb": ["2"], "mers": "cm", "padoms": "30 − 20 − 8."},
                {"jaut": "Vai 5 cm plats galds vēl ietilps gar to pašu sienu? "
                         "Raksti, cik cm pietrūkst.", "atb": ["3"],
                 "mers": "cm", "padoms": "Vajag 5, ir 2."},
            ]),
            pavediens="maja",
            konteksts="Pirms pārkārtot istabu, var pārbaudīt modelī.",
            kapec="Modelī mēbeles pārvietot ir vieglāk nekā īstenībā."),

    Kopsavilkums([
        "Nolasu izmērus no plāna.",
        "Atmēru un izgriežu daļas pēc izmēriem.",
        "Pārbaudu, vai modelis sakrīt ar plānu.",
    ]),

    Majas([
        "Izmēri savu gultu un galdu.",
        "Uzzīmē savas istabas plānu ar izmēriem.",
        "Vai ir vieta vēl vienam plauktam?",
    ]),
]
