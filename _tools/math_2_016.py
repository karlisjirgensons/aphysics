# -*- coding: utf-8 -*-
"""2. klase, 16. stunda: «Cik tas ir centimetros un cik milimetros?»

Vienu garumu pieraksta divos veidos: 4 cm 5 mm un 45 mm. Pāreja ir tā pati,
ko skolēns zina no desmitiem un vieniem - centimetrs ir «desmits»
milimetru.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, lineals)

TEMA = "Cik tas ir centimetros un cik milimetros?"

MERKIS = ("Šodien mērīsim vienu garumu divās mērvienībās un pierakstīsim "
          "abus rezultātus.")

SATURS = [
    Sakums("Kāpēc skrūvei uz kastītes raksta 45 mm, nevis 4 cm 5 mm?",
           zimejums=lineals(6, [(0, 4.5, "skrūve")], mm=True),
           paraksts="4 cm 5 mm = 45 mm.",
           fakti=["Veikalā sīkas lietas mēra tikai milimetros.",
                  "Tas pats garums - divi pieraksti."]),

    Doma("Centimetrs ir desmit milimetri",
         "Katrs centimetrs ir 10 mm, tāpēc 4 cm 5 mm = 40 mm + 5 mm = 45 mm.",
         soli=[
             "Veselos centimetrus pārvērt milimetros: 4 cm = 40 mm.",
             "Pieskaiti atlikušos milimetrus: 40 + 5 = 45.",
             "Atpakaļ: 45 mm - 4 pilni desmiti un 5.",
             "Tātad 45 mm = 4 cm 5 mm.",
         ],
         pieze="Tieši tāpat kā skaitlis 45 ir 4 desmiti un 5 vieni."),

    Paraugs("Cik mm ir 6 cm 3 mm?",
            uzd="Pārvērt 6 cm 3 mm milimetros.",
            soli=[("6 cm = 60 mm", "Katrs centimetrs - 10 mm."),
                  ("60 mm + 3 mm = 63 mm", "Pieskaita atlikušos mm.")],
            atbilde="63 mm"),

    Ievadi("Pārvērt milimetros", [
        {"jaut": "2 cm 7 mm = ? mm", "atb": ["27"], "padoms": "20 + 7."},
        {"jaut": "5 cm = ? mm", "atb": ["50"], "padoms": "5 desmiti."},
        {"jaut": "8 cm 1 mm = ? mm", "atb": ["81"], "padoms": "80 + 1."},
        {"jaut": "Cik mm garš ir nogrieznis?",
         "zim": lineals(8, [(0, 3.6, "")], mm=True), "atb": ["36"],
         "padoms": "3 cm 6 mm."},
        {"jaut": "9 cm 9 mm = ? mm", "atb": ["99"], "padoms": "90 + 9."},
        {"jaut": "Cik mm garš ir nogrieznis?",
         "zim": lineals(8, [(0, 7.2, "")], mm=True), "atb": ["72"],
         "padoms": "7 cm 2 mm."},
    ], pamats=4),

    Ievadi("Pārvērt centimetros un milimetros", [
        {"jaut": "34 mm = 3 cm un cik mm?", "atb": ["4"],
         "padoms": "34 = 30 + 4."},
        {"jaut": "58 mm = cik veselu cm un 8 mm?", "atb": ["5"],
         "padoms": "5 desmiti."},
        {"jaut": "90 mm = cik cm?", "atb": ["9"], "padoms": "9 desmiti."},
        {"jaut": "16 mm = 1 cm un cik mm?", "atb": ["6"],
         "padoms": "16 = 10 + 6."},
    ]),

    Varianti("Salīdzini", [
        {"jaut": "Kurš garums ir lielāks?",
         "opcijas": ["5 cm 2 mm", "48 mm"], "jaukt": False, "pareizi": 0,
         "padoms": "5 cm 2 mm = 52 mm."},
        {"jaut": "Kurš garums ir lielāks?",
         "opcijas": ["3 cm 9 mm", "41 mm"], "jaukt": False, "pareizi": 1,
         "padoms": "3 cm 9 mm = 39 mm."},
    ]),

    Pasaule("Vai skrūve der?",
            Varianti("", [
                {"jaut": "Dēlis ir 3 cm biezs. Skrūve 25 mm. Vai tā izurbsies "
                         "cauri?",
                 "opcijas": ["Nē, 25 mm ir mazāk nekā 30 mm",
                             "Jā, 25 ir vairāk nekā 3"],
                 "jaukt": False, "pareizi": 0,
                 "padoms": "Vispirms pārvērt vienādās vienībās."},
                {"jaut": "Kura skrūve savienos divus dēļus pa 2 cm?",
                 "opcijas": ["45 mm", "30 mm", "15 mm"], "pareizi": 0,
                 "padoms": "Kopā 4 cm = 40 mm; skrūvei jābūt garākai."},
            ]),
            pavediens="maja",
            konteksts="Galdnieks pērk skrūves, kuru garums rakstīts "
                      "milimetros.",
            kapec="Kļūda pārvēršanā - un plaukts nokritīs."),

    Kopsavilkums([
        "Pārvēršu cm un mm milimetros: 4 cm 5 mm = 45 mm.",
        "Pārvēršu milimetrus atpakaļ cm un mm.",
        "Salīdzinu garumus vienā mērvienībā.",
    ]),

    Majas([
        "Izmēri 3 lietas un pieraksti katru divos veidos.",
        "Piemēram: 6 cm 2 mm = 62 mm.",
        "Atrodi mājās iepakojumu, kur garums rakstīts mm.",
    ]),
]
