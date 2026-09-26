# -*- coding: utf-8 -*-
"""2. klase, 56. stunda: «Kas ir 13 dienā un kas - 1 naktī?»

Diennaktī ir 24 stundas. Pulkstenis ar rādītājiem apiet divreiz, bet
sarakstos un telefonā stundas skaita tālāk: 13:00 ir 1 dienā, 20:00 - 8
vakarā. Pēcpusdienas laiku atrod, pieskaitot 12.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, laiks, pulkstenis, taisne)

TEMA = "Kas ir 13 dienā un kas - 1 naktī?"

MERKIS = ("Šodien nolasīsim laiku 24 stundu diennaktī un saistīsim to ar "
          "dienas gaitu.")

SATURS = [
    Sakums("Kāpēc telefonā ir 13:00, bet sienas pulkstenī - 1?",
           zimejums=taisne(0, 24, 3, atzimes=[(1, "nakts"), (13, "diena")]),
           paraksts="Diennaktī ir 24 stundas.",
           fakti=["Sienas pulkstenis diennaktī apiet divreiz.",
                  "Telefons turpina skaitīt: 13, 14 ... 23.",
                  "13:00 = 1 dienā, 1:00 = 1 naktī."]),

    Doma("24 stundas",
         "Pēc 12 dienā skaita tālāk: 13, 14, 15 ... 24.",
         soli=[
             "0:00 - pusnakts, 12:00 - pusdienlaiks.",
             "Pēcpusdienas stundai pieskaiti 12: 3 dienā = 15:00.",
             "No 24 stundu laika atņem 12: 20:00 = 8 vakarā.",
             "Rīta stundas paliek tādas pašas: 7:00.",
         ]),

    Ievadi("Telefona laiks", [
        {"jaut": "Cik ir 3 pēcpusdienā telefona laikā? Raksti kā 15:00.",
         "atb": laiks(15, 0), "padoms": "3 + 12."},
        {"jaut": "Cik ir 7 vakarā telefona laikā?", "atb": laiks(19, 0),
         "padoms": "7 + 12."},
        {"jaut": "Cik ir 11 vakarā telefona laikā?", "atb": laiks(23, 0),
         "padoms": "11 + 12."},
        {"jaut": "Cik ir 9 no rīta telefona laikā?", "atb": laiks(9, 0),
         "padoms": "Rīts paliek tāds pats."},
    ]),

    Ievadi("Sienas pulksteņa laiks", [
        {"jaut": "14:00 - cik sienas pulkstenī?", "atb": ["2"],
         "padoms": "14 − 12."},
        {"jaut": "18:00 - cik sienas pulkstenī?", "atb": ["6"],
         "padoms": "18 − 12."},
        {"jaut": "21:00 - cik sienas pulkstenī?", "atb": ["9"],
         "padoms": "21 − 12."},
        {"jaut": "16:30 - cik stundas sienas pulkstenī?", "atb": ["4"],
         "padoms": "16 − 12, un vēl pusstunda."},
    ]),

    Varianti("Diena vai nakts?", [
        {"jaut": "Pulkstenis rāda šo. Skolā ir stunda. Kāds ir telefona "
                 "laiks?", "zim": pulkstenis(10, 0),
         "opcijas": ["10:00", "22:00"], "jaukt": False, "pareizi": 0,
         "padoms": "Stundas notiek dienā."},
        {"jaut": "Pulkstenis rāda šo, un ārā ir tumšs, tu guli. Telefona "
                 "laiks?", "zim": pulkstenis(10, 0),
         "opcijas": ["10:00", "22:00"], "jaukt": False, "pareizi": 1,
         "padoms": "Naktī - pēc 12 skaita tālāk."},
        {"jaut": "Pusdienas ēd...", "opcijas": ["13:00", "1:00",
                                                 "20:00"],
         "pareizi": 0, "padoms": "Pusdienas ir dienā."},
        {"jaut": "Multfilma sākas 19:30. Tas ir...",
         "opcijas": ["pusastoņos vakarā", "pusastoņos no rīta",
                     "deviņos"], "pareizi": 0, "padoms": "19 − 12 = 7."},
    ]),

    Pasaule("Kinoteātra seansi",
            Varianti("", [
                {"jaut": "Seansi: 11:00, 15:30, 20:45. Kurš ir pēcpusdienā?",
                 "opcijas": ["15:30", "11:00", "20:45"], "pareizi": 0,
                 "padoms": "15:30 = pusčetros dienā."},
                {"jaut": "Tev jābūt mājās līdz 8 vakarā. Kurus seansus vari "
                         "noskatīties, ja filma ilgst 2 stundas?",
                 "opcijas": ["11:00 un 15:30", "tikai 20:45",
                             "visus"], "pareizi": 0,
                 "padoms": "8 vakarā ir 20:00."},
            ]),
            pavediens="celojums",
            konteksts="Kino sarakstā laikus raksta 24 stundu formā.",
            kapec="Sajaucot 8:45 un 20:45, var nokavēt filmu."),

    Kopsavilkums([
        "Zinu, ka diennaktī ir 24 stundas.",
        "Pārvēršu pēcpusdienas laiku 24 stundu formā.",
        "Saistu laiku ar dienas gaitu.",
    ]),

    Majas([
        "Pieraksti 24 stundu formā, kad tu mosties, ēd pusdienas un "
        "ej gulēt.",
        "Pārbaudi telefonā.",
        "Kura stunda ir lielākā?",
    ]),
]
