# -*- coding: utf-8 -*-
"""2. klase, 52. stunda: «Kā samaksāt ar monētām?»

Vienu summu var salikt no monētām dažādos veidos: 50 c = 20 + 20 + 10 =
20 + 10 + 10 + 5 + 5. Jautājums «ar vismazāk monētām» liek sākt ar
lielākajām - tas pats, ko dara kasieris.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, monetas)

TEMA = "Kā samaksāt ar monētām?"

MERKIS = ("Šodien saliksim doto summu no monētām vairākos veidos un "
          "atradīsim veidu ar vismazāk monētām.")

SATURS = [
    Sakums("Kā samaksāt 50 c, ja nav 50 centu monētas?",
           zimejums=monetas(["20 c", "20 c", "10 c"]),
           paraksts="20 + 20 + 10 = 50.",
           fakti=["Eiro monētas: 1, 2, 5, 10, 20, 50 c, 1 €, 2 €.",
                  "Vienu summu var salikt daudzos veidos.",
                  "Ar vismazāk monētām - sāc ar lielāko."]),

    Doma("Saliec summu",
         "Ņem lielāko monētu, kas vēl der, un turpini ar atlikumu.",
         soli=[
             "Summa 75 c: lielākā derīgā - 50 c. Paliek 25 c.",
             "20 c - paliek 5 c.",
             "5 c - paliek 0.",
             "75 = 50 + 20 + 5 - tikai 3 monētas.",
         ]),

    Ievadi("Cik kopā?", [
        {"jaut": "Cik centu?", "zim": monetas(["50 c", "20 c", "5 c",
                                               "2 c"]),
         "atb": ["77"], "mers": "c", "padoms": "50 + 20 + 5 + 2."},
        {"jaut": "Cik centu?", "zim": monetas(["20 c", "20 c", "20 c",
                                               "10 c", "1 c"]),
         "atb": ["71"], "mers": "c", "padoms": "60 + 10 + 1."},
        {"jaut": "Cik centu?", "zim": monetas(["10 c", "10 c", "5 c",
                                               "5 c", "2 c", "2 c"]),
         "atb": ["34"], "mers": "c", "padoms": "20 + 10 + 4."},
        {"jaut": "Cik eiro?", "zim": monetas(["2 €", "2 €", "1 €",
                                              "5 €"]),
         "atb": ["10"], "mers": "€", "padoms": "5 + 2 + 2 + 1."},
    ]),

    Ievadi("Ar vismazāk monētām", [
        {"jaut": "Cik monētu vajag 30 c?", "atb": ["2"],
         "padoms": "20 + 10."},
        {"jaut": "Cik monētu vajag 85 c?", "atb": ["4"],
         "padoms": "50 + 20 + 10 + 5."},
        {"jaut": "Cik monētu vajag 99 c?", "atb": ["6"],
         "padoms": "50 + 20 + 20 + 5 + 2 + 2."},
        {"jaut": "Cik monētu vajag 40 c?", "atb": ["2"],
         "padoms": "20 + 20."},
    ]),

    Varianti("Vai summa pareiza?", [
        {"jaut": "Kurš komplekts dod 60 c?",
         "opcijas": ["50 c + 10 c", "20 c + 20 c + 10 c",
                     "50 c + 5 c + 2 c"], "pareizi": 0,
         "padoms": "Saskaiti katru."},
        {"jaut": "Kurš komplekts nav 25 c?",
         "opcijas": ["10 c + 10 c + 2 c", "20 c + 5 c",
                     "10 c + 10 c + 5 c"], "pareizi": 0,
         "padoms": "10 + 10 + 2 = 22."},
    ]),

    Petijums("Cik veidos?", [
        "Paņem monētu modeļus: 20 c, 10 c, 5 c.",
        "Saliec 30 c visos veidos, kā vari.",
        "Pieraksti katru veidu ar summu.",
        "Cik veidu atradi? Kurā vismazāk monētu?",
    ], vajag="monētu modeļi vai īstas monētas",
             secinajums="30 c var salikt vairākos veidos, bet ar vismazāk "
                        "monētām - 20 c + 10 c."),

    Pasaule("Automāts neizdod atlikumu",
            Varianti("", [
                {"jaut": "Ūdens pudele automātā maksā 85 c. Kurš komplekts "
                         "der precīzi?",
                 "opcijas": ["50 c + 20 c + 10 c + 5 c", "50 c + 50 c",
                             "20 c + 20 c + 20 c + 20 c"], "pareizi": 0,
                 "padoms": "Jāsanāk tieši 85."},
                {"jaut": "Tev ir 20 c, 20 c, 20 c, 10 c, 10 c, 5 c. Vai vari "
                         "samaksāt 85 c precīzi?",
                 "opcijas": ["Jā", "Nē"], "jaukt": False, "pareizi": 0,
                 "padoms": "20 + 20 + 20 + 10 + 10 + 5 = 85."},
            ]),
            pavediens="veikals",
            konteksts="Stacijas dzērienu automāts atlikumu neizdod.",
            kapec="Jāsaliek tieši vajadzīgā summa."),

    Kopsavilkums([
        "Saskaitu monētu summu.",
        "Saliku summu no monētām dažādos veidos.",
        "Atrodu veidu ar vismazāk monētām.",
    ]),

    Majas([
        "Saskaiti monētas savā krājkasītē.",
        "Saliec 1 € no monētām divos veidos.",
        "Kurā veidā bija mazāk monētu?",
    ]),
]
