# -*- coding: utf-8 -*-
"""9. klase, 165. stunda: «Kas ir eksāmenā?»

Centralizētā eksāmena uzbūve (Math/mat_ex.pdf, 2025): 1. daļa - 26
uzdevumi, 57 + 3 punkti, 105 min, bez kalkulatora; starpbrīdis; 2. daļa -
5 kompleksi uzdevumi, 20 punkti, 75 min, ar zinātnisko kalkulatoru. Visu
laiku atļauta formulu lapa, lineāls un cirkulis; raksta tikai ar pildspalvu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, sektori)

TEMA = "Kas ir eksāmenā?"

MERKIS = ("Iepazīsim eksāmena uzbūvi, laiku, vērtēšanu un atļautos "
          "palīglīdzekļus.")

_PUNKTI = sektori([("1. daļa", 60),
                   ("2. daļa", 20)], procenti=False)

SATURS = [
    Sakums("80 punkti, divas daļas, trīs stundas",
           zimejums=_PUNKTI,
           paraksts="1. daļā 57 + 3 punkti, 2. daļā 20 punkti.",
           fakti=["1. daļa: 26 uzdevumi, 105 min, bez kalkulatora.",
                  "2. daļa: 5 uzdevumi, 75 min, ar kalkulatoru.",
                  "Visu laiku: formulu lapa, lineāls, cirkulis."]),

    Doma("Eksāmena uzbūve",
         "1. daļa pārbauda zināšanas un prasmes algebrā un ģeometrijā, "
         "2. daļa - kompleksu problēmu risināšanu.",
         soli=[
             "1. daļā ir izvēles, īsās atbildes un izvērstie uzdevumi.",
             "Izvērstajos uzdevumos (2 un vairāk punkti) raksta pilnu "
             "risinājumu.",
             "3 punktus dod par matemātikas valodu un risinājuma "
             "skaidrību.",
             "Ar zīmuli rakstīto nevērtē - arī zīmējumus velk ar "
             "pildspalvu.",
         ],
         pieze="Starp daļām ir starpbrīdis; kalkulatoru drīkst lietot tikai "
               "2. daļā."),

    Ievadi("Rēķini ar eksāmenu", [
        {"jaut": "Cik punktu var iegūt kopā?", "atb": ["80"],
         "padoms": "57 + 3 + 20."},
        {"jaut": "Cik minūšu ilgst abas daļas kopā (bez starpbrīža)?",
         "atb": ["180"], "padoms": "105 + 75."},
        {"jaut": "Cik minūšu vidēji uz vienu 2. daļas uzdevumu?",
         "atb": ["15"], "padoms": "75 : 5."},
        {"jaut": "Cik procentu no visiem punktiem ir 2. daļā?",
         "atb": ["25"], "padoms": "20 : 80."},
    ]),

    Varianti("Kas atļauts?", [
        {"jaut": "Kalkulators 1. daļā", "opcijas": ["Atļauts", "Aizliegts"],
         "jaukt": False, "pareizi": 1, "padoms": "Tikai 2. daļā."},
        {"jaut": "Formulu lapa 1. daļā", "opcijas": ["Atļauts", "Aizliegts"],
         "jaukt": False, "pareizi": 0, "padoms": "Visa eksāmena laikā."},
        {"jaut": "Cirkulis un lineāls", "opcijas": ["Atļauts", "Aizliegts"],
         "jaukt": False, "pareizi": 0, "padoms": "Visa eksāmena laikā."},
        {"jaut": "Viedpulkstenis", "opcijas": ["Atļauts", "Aizliegts"],
         "jaukt": False, "pareizi": 1,
         "padoms": "Nekādas viedierīces telpā."},
        {"jaut": "Zīmējums ar zīmuli tiek vērtēts", "opcijas": ["Jā", "Nē"],
         "jaukt": False, "pareizi": 1, "padoms": "Tikai pildspalva."},
    ]),

    Pasaule("Mans rezultāts procentos",
            Ievadi("", [
                {"jaut": "1. daļā ieguvi 42 punktus, 2. daļā 12. Cik procentu "
                         "no 80?", "atb": ["67,5"], "padoms": "54 : 80 · 100."},
                {"jaut": "Cik punktu vajag 75 %?", "atb": ["60"],
                 "padoms": "0,75 · 80."},
                {"jaut": "Ja 1. daļā ir 45 punkti, cik vēl vajag 2. daļā "
                         "75 %?", "atb": ["15"], "padoms": "60 − 45."},
            ]),
            pavediens="skola",
            konteksts="Eksāmena rezultātu sertifikātā raksta procentos no "
                      "80 punktiem.",
            kapec="Zinot, kur ir punkti, var plānot, cik daudz no katras "
                  "daļas mērķēt."),

    Kopsavilkums([
        "Zinu eksāmena daļas, uzdevumu skaitu un laiku.",
        "Zinu, ko drīkst lietot un kad.",
        "Aprēķinu savu rezultātu procentos.",
    ]),

    Majas([
        "Izdrukā vai atver eksāmena formulu lapu un izlasi to visu.",
        "Atrisini viena iepriekšējā gada eksāmena 1. daļas pirmos 5 "
        "uzdevumus.",
        "Uzraksti, cik punktu tu gribi iegūt katrā daļā.",
    ]),
]
