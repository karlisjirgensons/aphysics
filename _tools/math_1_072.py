# -*- coding: utf-8 -*-
"""1. klase, 72. stunda: «Vai virkni var turpināt citādi?»

Ja doti tikai daži skaitļi, likumu var izdomāt dažādi: 1; 2; 4 var
turpināt ar 7 (+1, +2, +3) vai ar 8 (katru reizi divreiz). Abi ir pareizi,
ja likumu pamato.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, restis)

TEMA = "Vai virkni var turpināt citādi?"

MERKIS = ("Šodien atradīsim vairākus veidus, kā turpināt vienu virkni, un "
          "pamatosim katru.")

SATURS = [
    Sakums("1; 2; 4; ... - 7 vai 8?",
           zimejums=restis([[1, 2, 4, None]]),
           paraksts="Abi var būt pareizi - atkarībā no likuma.",
           fakti=["Likums A: +1, +2, +3 - nākamais 7.",
                  "Likums B: divreiz vairāk - nākamais 8.",
                  "Svarīgi pateikt, kādu likumu izvēlējies."]),

    Doma("Vairāki likumi",
         "Ja skaitļu maz, der vairāki likumi - pamato savējo.",
         soli=[
             "Izdomā likumu, kas der visiem dotajiem.",
             "Turpini pēc tā.",
             "Pamēģini atrast vēl vienu likumu.",
         ]),

    Ievadi("Divi likumi: 1; 2; 4", [
        {"jaut": "Likums: pieskaita 1, tad 2, tad 3... Nākamais?",
         "atb": ["7"], "padoms": "4 + 3."},
        {"jaut": "Likums: katru reizi divreiz vairāk. Nākamais?",
         "atb": ["8"], "padoms": "4 + 4."},
    ]),

    Ievadi("Divi likumi: 2; 4", [
        {"jaut": "Likums +2. Nākamais?", "atb": ["6"], "padoms": "4 + 2."},
        {"jaut": "Likums: 2, 4, 2, 4 - atkārtojas. Nākamais?",
         "atb": ["2"], "padoms": "Grupa 2, 4."},
    ]),

    Varianti("Vai pamatojums der?", [
        {"jaut": "Virkne 5; 10; ... Jānis turpina ar 15: «+5». Vai der?",
         "opcijas": ["Jā", "Nē"], "jaukt": False, "pareizi": 0,
         "padoms": "10 + 5."},
        {"jaut": "Tai pašai virknei Ieva raksta 20: «divreiz vairāk». Vai "
                 "der?", "opcijas": ["Jā", "Nē"], "jaukt": False,
         "pareizi": 0, "padoms": "10 + 10 = 20 arī der."},
        {"jaut": "Kas vajadzīgs, lai būtu tikai viens pareizs turpinājums?",
         "opcijas": ["vairāk doto skaitļu", "lielāki skaitļi",
                     "mazāk skaitļu"], "pareizi": 0,
         "padoms": "Vairāk skaitļu - mazāk iespēju."},
    ]),

    Pasaule("Kāpnes",
            Varianti("", [
                {"jaut": "Pakāpieni: 1. stāvā 10, 2. stāvā 20. Cik 3. stāvā?",
                 "opcijas": ["30, ja katrā stāvā ir 10 pakāpienu", "5",
                             "100"],
                 "pareizi": 0, "padoms": "Likums +10."},
            ]),
            pavediens="maja",
            konteksts="Daudzstāvu mājā skaita pakāpienus līdz katram stāvam.",
            kapec="Likums ir pieņēmums - to pārbauda, ejot."),

    Kopsavilkums([
        "Zinu, ka virkni var turpināt dažādi.",
        "Pamatoju savu likumu.",
        "Salīdzinu dažādus likumus.",
    ]),

    Majas([
        "Izdomā divus turpinājumus virknei 3; 6.",
        "Palūdz mājiniekam atrast vēl vienu.",
        "Kurš likums tev šķiet interesantākais?",
    ]),
]
