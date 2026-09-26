# -*- coding: utf-8 -*-
"""2. klase, 158. stunda: «Kā samaksāt ar vienādām monētām?»

Kuras summas var samaksāt ar 3, 4 vai 5 vienādām monētām? 3 monētas pa
20 c - 60 c; 5 monētas pa 10 c - 50 c. Otrādi: 40 c ar 4 vienādām - pa 10 c.
Reizināšana un dalīšana ar naudu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, monetas)

TEMA = "Kā samaksāt ar vienādām monētām?"

MERKIS = ("Šodien pierakstīsim, kādas summas var samaksāt ar 3, 4 vai 5 "
          "vienādām monētām.")

SATURS = [
    Sakums("Kā samaksāt 60 c ar 3 vienādām monētām?",
           zimejums=monetas(["20 c", "20 c", "20 c"]),
           paraksts="3 · 20 c = 60 c.",
           fakti=["60 c : 3 = 20 c - katra monēta.",
                  "20 c monēta ir - der!",
                  "Ne katru summu var samaksāt vienādi."]),

    Doma("Vienādas monētas",
         "Summa : monētu skaits = vienas monētas vērtība.",
         soli=[
             "Izdali summu ar monētu skaitu.",
             "Pārbaudi, vai tāda monēta eksistē: 1, 2, 5, 10, 20, 50 c.",
             "Ja eksistē - var samaksāt.",
             "Pārbaude ar reizināšanu.",
         ]),

    Ievadi("Cik kopā?", [
        {"jaut": "4 monētas pa 5 c?", "atb": ["20"], "mers": "c",
         "padoms": "4 · 5."},
        {"jaut": "5 monētas pa 10 c?", "atb": ["50"], "mers": "c",
         "padoms": "5 · 10."},
        {"jaut": "3 monētas pa 2 €?", "atb": ["6"], "mers": "€",
         "padoms": "3 · 2."},
        {"jaut": "4 monētas pa 20 c?", "zim": monetas(["20 c"] * 4),
         "atb": ["80"], "mers": "c", "padoms": "4 · 20."},
    ]),

    Ievadi("Kāda monēta?", [
        {"jaut": "40 c ar 4 vienādām monētām. Vienas vērtība?", "atb": ["10"],
         "mers": "c", "padoms": "40 : 4."},
        {"jaut": "15 c ar 3 vienādām. Vienas vērtība?", "atb": ["5"],
         "mers": "c", "padoms": "15 : 3."},
        {"jaut": "10 € ar 5 vienādām. Vienas vērtība?", "atb": ["2"],
         "mers": "€", "padoms": "10 : 5."},
        {"jaut": "8 c ar 4 vienādām. Vienas vērtība?", "atb": ["2"],
         "mers": "c", "padoms": "8 : 4."},
    ]),

    Varianti("Var vai nevar?", [
        {"jaut": "30 c ar 3 vienādām monētām",
         "opcijas": ["var - pa 10 c", "nevar"], "jaukt": False,
         "pareizi": 0, "padoms": "30 : 3 = 10."},
        {"jaut": "12 c ar 4 vienādām monētām",
         "opcijas": ["var", "nevar - 3 c monētas nav"], "jaukt": False,
         "pareizi": 1, "padoms": "12 : 4 = 3."},
        {"jaut": "25 c ar 5 vienādām monētām",
         "opcijas": ["var - pa 5 c", "nevar"], "jaukt": False,
         "pareizi": 0, "padoms": "25 : 5 = 5."},
        {"jaut": "45 c ar 3 vienādām monētām",
         "opcijas": ["var", "nevar - 15 c monētas nav"], "jaukt": False,
         "pareizi": 1, "padoms": "45 : 3 = 15."},
    ]),

    Pasaule("Parkošanās automāts",
            Ievadi("", [
                {"jaut": "Parkošana maksā 1 € (100 c). Tev ir tikai 20 c "
                         "monētas. Cik vajag?", "atb": ["5"],
                 "padoms": "5 · 20 = 100."},
                {"jaut": "Ja būtu tikai 50 c monētas?", "atb": ["2"],
                 "padoms": "2 · 50 = 100."},
            ]),
            pavediens="celojums",
            konteksts="Automāts pieņem tikai monētas.",
            kapec="Dalot uzzina, cik monētu sagatavot."),

    Kopsavilkums([
        "Aprēķinu vienādu monētu summu.",
        "Atrodu monētas vērtību ar dalīšanu.",
        "Pārbaudu, vai tāda monēta eksistē.",
    ]),

    Majas([
        "Paņem vienādas monētas un saskaiti summu ar reizināšanu.",
        "Izdomā summu, ko nevar samaksāt ar 3 vienādām monētām.",
        "Paskaidro, kāpēc.",
    ]),
]
