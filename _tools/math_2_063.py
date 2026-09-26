# -*- coding: utf-8 -*-
"""2. klase, 63. stunda: «Vai paspēsi uz autobusu?»

Kustības saraksts ir tabula ar laikiem. No tās nolasa, kurš autobuss der, un
aprēķina, cik laika atliek - atņemot laiku, kas ir tagad, no atiešanas
laika.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, laiks, pulkstenis, restis)

TEMA = "Vai paspēsi uz autobusu?"

MERKIS = ("Šodien lasīsim kustības sarakstu un aprēķināsim, cik laika "
          "atliek līdz atiešanai.")

_SARAKSTS = restis([["pietura", "1. reiss", "2. reiss", "3. reiss"],
                    ["Skola", "7:40", "13:25", "15:10"],
                    ["Parks", "7:48", "13:33", "15:18"],
                    ["Stacija", "8:02", "13:47", "15:32"]])

SATURS = [
    Sakums("Pulkstenis rāda šo laiku. Autobuss no skolas atiet 13:25. Vai "
           "paspēsi?",
           zimejums=pulkstenis(1, 12),
           paraksts="Ir 13:12 - līdz atiešanai 13 minūtes.",
           fakti=["Kustības saraksts ir tabula ar laikiem.",
                  "Rindā - pietura, kolonnā - reiss.",
                  "Autobuss negaida - jābūt pieturā laikus."]),

    Doma("Lasi sarakstu",
         "Atrodi pieturu rindā, reisu kolonnā - krustpunktā ir laiks.",
         soli=[
             "Atrodi savu pieturu.",
             "Atrodi pirmo reisu, kas ir pēc tagadējā laika.",
             "Aprēķini: atiešanas laiks − tagadējais laiks.",
             "Salīdzini ar laiku, kas vajadzīgs ceļam līdz pieturai.",
         ]),

    Ievadi("Nolasi sarakstu", [
        {"jaut": "Cikos 2. reiss atiet no Parka?", "zim": _SARAKSTS,
         "atb": laiks(13, 33), "padoms": "Rinda «Parks», kolonna «2. reiss»."},
        {"jaut": "Cik minūšu brauc no Skolas līdz Stacijai 1. reisā?",
         "zim": _SARAKSTS, "atb": ["22"], "mers": "min",
         "padoms": "No 7:40 līdz 8:02: 20 + 2."},
        {"jaut": "Cik minūšu brauc no Skolas līdz Parkam?",
         "zim": _SARAKSTS, "atb": ["8"], "mers": "min",
         "padoms": "7:48 − 7:40."},
        {"jaut": "Ir 15:02. Cik minūšu līdz 3. reisam no Skolas?",
         "zim": _SARAKSTS, "atb": ["8"], "mers": "min",
         "padoms": "15:10 − 15:02."},
    ]),

    Varianti("Kurš reiss der?", [
        {"jaut": "Ir 13:30, tu esi pie Skolas. Kurš ir nākamais reiss?",
         "zim": _SARAKSTS, "opcijas": ["3. reiss", "2. reiss", "1. reiss"],
         "pareizi": 0, "padoms": "13:25 jau aizbrauca."},
        {"jaut": "Stacijā jābūt līdz 14:00. Kurš reiss no Skolas der?",
         "zim": _SARAKSTS, "opcijas": ["2. reiss", "3. reiss",
                                       "neviens"], "pareizi": 0,
         "padoms": "13:47 ir pirms 14:00."},
    ]),

    Pasaule("Ceļš līdz pieturai",
            Varianti("", [
                {"jaut": "Ir 13:15. Līdz pieturai jāiet 7 minūtes. Vai "
                         "paspēsi uz 13:25?",
                 "opcijas": ["Jā, būšu 13:22", "Nē"], "jaukt": False,
                 "pareizi": 0, "padoms": "13:15 + 7 min."},
                {"jaut": "Ir 13:20, jāiet 7 minūtes. Vai paspēsi?",
                 "opcijas": ["Nē, būšu 13:27", "Jā"], "jaukt": False,
                 "pareizi": 0, "padoms": "13:20 + 7 min."},
            ]),
            pavediens="celojums",
            konteksts="No skolas līdz pieturai ir 7 minūšu gājiens.",
            kapec="Divu minūšu kļūda nozīmē stundu gaidīšanas."),

    Kopsavilkums([
        "Lasu kustības sarakstu.",
        "Atrodu piemērotu reisu.",
        "Aprēķinu, cik laika atliek līdz atiešanai.",
    ]),

    Majas([
        "Atrodi internetā sava tuvākā autobusa vai vilciena sarakstu.",
        "Pieraksti 3 atiešanas laikus.",
        "Cik minūšu starp tiem?",
    ]),
]
