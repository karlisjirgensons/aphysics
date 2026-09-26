# -*- coding: utf-8 -*-
"""1. klase, 100. stunda: «Kāda summa uzkrīt biežāk?»

Divus kauliņus met daudzkārt un pieraksta summas. 7 iznāk visbiežāk, jo to
var dabūt visvairāk veidos (1+6, 2+5, 3+4, 4+3, 5+2, 6+1), bet 2 un 12 -
tikai vienā. Simulācija dod daudz metienu ātri.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Simulacija, Varianti, kaulini)

TEMA = "Kāda summa uzkrīt biežāk?"

MERKIS = ("Šodien metīsim kauliņus, pierakstīsim summas un noteiksim, "
          "kuras iznāk biežāk.")

SATURS = [
    Sakums("Kura summa ar 2 kauliņiem iznāk visbiežāk?",
           zimejums=kaulini([3, 4]),
           paraksts="3 + 4 = 7. Vai 7 ir biežāk nekā 12?",
           fakti=["Mazākā summa - 2, lielākā - 12.",
                  "Dažas summas var dabūt daudzos veidos.",
                  "Pārbaudīsim ar metieniem."]),

    Doma("Cik veidos?",
         "Jo vairāk veidu dabūt summu, jo biežāk tā iznāk.",
         soli=[
             "12 = 6 + 6 - viens veids.",
             "7 = 1+6, 2+5, 3+4, 4+3, 5+2, 6+1 - seši veidi.",
             "Tāpēc 7 iznāk visbiežāk.",
         ]),

    Simulacija("Met 100 reizes",
               ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
               [5], "summa ir 7",
               svari=[1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1],
               ievads="Spied «10 reizes» un vēro, kura josla aug "
                      "visātrāk."),

    Ievadi("Summas", [
        {"jaut": "Cik kopā?", "zim": kaulini([6, 5]), "atb": ["11"],
         "padoms": "6 + 5."},
        {"jaut": "Cik kopā?", "zim": kaulini([4, 4]), "atb": ["8"],
         "padoms": "Dubultais."},
        {"jaut": "Cik veidos var dabūt 3? (1+2 un ...)", "atb": ["2"],
         "padoms": "1 + 2 un 2 + 1."},
        {"jaut": "Lielākā iespējamā summa ar 2 kauliņiem?", "atb": ["12"],
         "padoms": "6 + 6."},
    ]),

    Varianti("Kura biežāk?", [
        {"jaut": "Kura summa iznāks biežāk: 7 vai 12?",
         "opcijas": ["7", "12", "vienādi"], "pareizi": 0,
         "padoms": "7 - seši veidi."},
        {"jaut": "Vai summa 1 var iznākt?",
         "opcijas": ["Nē - mazākā ir 2", "Jā"], "jaukt": False,
         "pareizi": 0, "padoms": "Katrs kauliņš vismaz 1."},
    ]),

    Petijums("Metienu tabula", [
        "Met divus kauliņus 20 reizes.",
        "Katru summu atzīmē tabulā ar svītriņu.",
        "Saskaiti svītriņas pie katras summas.",
        "Kura summa iznāca visbiežāk? Salīdzini ar klasesbiedriem.",
    ], vajag="2 kauliņi, tabula ar summām 2-12"),

    Pasaule("Galda spēle",
            Varianti("", [
                {"jaut": "Spēlē tev jāuzmet summa, lai trāpītu uz lauciņa. "
                         "Kuru lauciņu izvēlēties?",
                 "opcijas": ["7 soļu attālumā", "12 soļu attālumā",
                             "2 soļu attālumā"], "pareizi": 0,
                 "padoms": "7 iznāk visbiežāk."},
            ]),
            pavediens="speles",
            konteksts="Galda spēlēs ar diviem kauliņiem daži lauciņi ir "
                      "«laimīgāki».",
            kapec="Matemātika palīdz spēlēt gudri."),

    Kopsavilkums([
        "Metu kauliņus un pierakstu summas.",
        "Nosaku, kura summa iznāk biežāk.",
        "Skaidroju ar veidu skaitu.",
    ]),

    Majas([
        "Met kauliņus mājās 30 reizes un pieraksti summas.",
        "Vai 7 bija visbiežāk?",
        "Kura summa neiznāca ne reizi?",
    ]),
]
