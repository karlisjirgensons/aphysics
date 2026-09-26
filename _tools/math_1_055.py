# -*- coding: utf-8 -*-
"""1. klase, 55. stunda: «Kāpēc 10 ir īpašs skaitlis?»

Desmit vieni kopā ir viens desmits - to pašu skaitu var paņemt vienā
sloksnītē. Pēc 9 cipari beidzas, tāpēc 10 raksta ar diviem cipariem:
1 desmits un 0 vienu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, desmiti, ramis)

TEMA = "Kāpēc 10 ir īpašs skaitlis?"

MERKIS = ("Šodien iemācīsimies, ka viens desmits ir desmit vieni, un "
          "modelēsim desmitu.")

SATURS = [
    Sakums("Kāpēc 10 raksta ar diviem cipariem?",
           zimejums=desmiti(1, 0),
           paraksts="1 desmits un 0 vienu - 10.",
           fakti=["Ciparu ir tikai 10: no 0 līdz 9.",
                  "Pēc 9 vienus saliek desmitā.",
                  "10 vieni = 1 desmits."]),

    Doma("Desmit vieni - viens desmits",
         "Kad vienu ir desmit, tos saliek vienā desmitā.",
         soli=[
             "Pilns desmitnieka rāmis - viens desmits.",
             "Klucīšu sloksnīte ar 10 klucīšiem - viens desmits.",
             "10: pirmais cipars - desmiti, otrais - vieni.",
         ]),

    Ievadi("Desmits", [
        {"jaut": "Cik vienu ir vienā desmitā?", "atb": ["10"],
         "padoms": "Pilns rāmis."},
        {"jaut": "Cik trūkst līdz desmitam?", "zim": ramis(7), "atb": ["3"],
         "padoms": "Tukšās rūtiņas."},
        {"jaut": "9 + 1 = ?", "atb": ["10"], "padoms": "Rāmis pilns."},
        {"jaut": "Cik desmitu ir 20?", "zim": desmiti(2, 0), "atb": ["2"],
         "padoms": "Divi stieņi."},
    ]),

    Varianti("Kas ir desmits?", [
        {"jaut": "Kurš ir viens desmits?",
         "opcijas": ["10 vieni", "1 viens", "100 vienu"], "pareizi": 0,
         "padoms": "Desmit kopā."},
        {"jaut": "Ko nozīmē 0 skaitlī 10?",
         "opcijas": ["vienu nav", "desmitu nav", "nekas nav"],
         "pareizi": 0, "padoms": "Otrais cipars - vieni."},
        {"jaut": "Kas notiek, ja pie 9 pieliek vēl 1?",
         "opcijas": ["sanāk pilns desmits", "sanāk 91", "nekas"],
         "pareizi": 0, "padoms": "9 + 1."},
    ]),

    Pasaule("Pirksti klasē",
            Ievadi("", [
                {"jaut": "Katram bērnam ir 10 pirkstu. Cik pirkstu ir 3 "
                         "bērniem?", "atb": ["30"], "padoms": "10, 20, 30."},
                {"jaut": "Cik desmitu pirkstu ir 5 bērniem?", "atb": ["5"],
                 "padoms": "Katram bērnam viens desmits."},
            ]),
            pavediens="skola",
            konteksts="Mūsu rokas ir dabisks desmits.",
            kapec="Tāpēc cilvēki skaita tieši pa 10."),

    Kopsavilkums([
        "Zinu, ka 10 vieni ir 1 desmits.",
        "Modelēju desmitu ar rāmi un sloksnīti.",
        "Zinu, kāpēc 10 raksta ar diviem cipariem.",
    ]),

    Majas([
        "Izveido desmitu no 10 pogām un saliec tās vienā rindā.",
        "Atrodi mājās lietas, ko pārdod pa 10.",
        "Saskaiti mājinieku pirkstus pa 10.",
    ]),
]
