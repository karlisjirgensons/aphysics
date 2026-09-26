# -*- coding: utf-8 -*-
"""1. klase, 129. stunda: «Kā samaksāt tieši?»

Vienu summu var salikt ar dažādām monētām: 30 c = 20 c + 10 c = 10 c +
10 c + 10 c = 20 c + 5 c + 5 c. Meklē vairākus veidus un to, kurā vismazāk
monētu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, monetas)

TEMA = "Kā samaksāt tieši?"

MERKIS = ("Šodien saliksim doto summu ar naudas modeļiem vairākos veidos.")

SATURS = [
    Sakums("Kā samaksāt tieši 30 c?",
           zimejums=monetas(["20 c", "10 c"]),
           paraksts="20 c + 10 c. Bet ir arī citi veidi!",
           fakti=["Vienu summu var salikt dažādi.",
                  "Mazāk monētu - ātrāk samaksāt.",
                  "Tieši - lai nav jāizdod atlikums."]),

    Doma("Saliec summu",
         "Sāc ar lielāko monētu, kas nav par lielu, un papildini.",
         soli=[
             "Paņem lielāko monētu, kas nepārsniedz summu.",
             "Cik vēl trūkst?",
             "Papildini ar mazākām.",
         ]),

    Varianti("Vai tieši?", [
        {"jaut": "Vajag 30 c.", "zim": monetas(["10 c", "10 c", "10 c"]),
         "opcijas": ["tieši", "par maz", "par daudz"], "jaukt": False,
         "pareizi": 0, "padoms": "10 + 10 + 10."},
        {"jaut": "Vajag 50 c.", "zim": monetas(["20 c", "20 c", "5 c"]),
         "opcijas": ["tieši", "par maz", "par daudz"], "jaukt": False,
         "pareizi": 1, "padoms": "45 c."},
        {"jaut": "Vajag 7 €.", "zim": monetas(["5 €", "2 €", "1 €"]),
         "opcijas": ["tieši", "par maz", "par daudz"], "jaukt": False,
         "pareizi": 2, "padoms": "8 €."},
    ]),

    Ievadi("Cik monētu?", [
        {"jaut": "Vismazāk monētu, lai samaksātu 30 c?", "atb": ["2"],
         "padoms": "20 c + 10 c."},
        {"jaut": "Vismazāk monētu 70 c?", "atb": ["2"],
         "padoms": "50 c + 20 c."},
        {"jaut": "Cik 10 c monētu vajag 50 c?", "atb": ["5"],
         "padoms": "10, 20, 30, 40, 50."},
        {"jaut": "Cik 2 € monētu vajag 10 €?", "atb": ["5"],
         "padoms": "2, 4, 6, 8, 10."},
    ]),

    Petijums("Rotaļu veikals", [
        "Paņemiet rotaļu naudu.",
        "Viens saka cenu, otrs saliek summu.",
        "Atrodiet vēl vienu veidu tai pašai summai.",
        "Kurā veidā vismazāk monētu?",
    ], vajag="rotaļu nauda vai izgrieztas monētas"),

    Pasaule("Autobusa biļete",
            Ievadi("", [
                {"jaut": "Biļete 1 € 50 c. Tev 1 € un 50 c monētas. Cik "
                         "monētu atdosi?", "atb": ["2"], "padoms": "1 € + 50 c."},
            ]),
            pavediens="celojums",
            konteksts="Šoferis lūdz samaksāt tieši.",
            kapec="Tieša samaksa ir ātra."),

    Kopsavilkums([
        "Saliku summu ar monētām.",
        "Atrodu vairākus veidus.",
        "Atrodu veidu ar vismazāk monētām.",
    ]),

    Majas([
        "Saliec 40 c no mājas monētām trīs veidos.",
        "Kurā veidā vismazāk monētu?",
        "Samaksā veikalā tieši (ar pieaugušo).",
    ]),
]
