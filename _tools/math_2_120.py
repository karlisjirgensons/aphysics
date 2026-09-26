# -*- coding: utf-8 -*-
"""2. klase, 120. stunda: «Kā sadalīt uz pusēm?»

Dalīšanai ir divas nozīmes: sadalīt 2 vienādās daļās (cik katrā?) un
sadalīt pa 2 (cik daļu?). 12 konfektes: uz pusēm - pa 6 katram; pa 2 - 6
cilvēkiem. Skaitļi sakrīt, bet jautājums atšķiras.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, bildes)

TEMA = "Kā sadalīt uz pusēm?"

MERKIS = ("Šodien dalīsim doto daudzumu divās vienādās daļās un pa 2 un "
          "pastāstīsim atšķirību.")

SATURS = [
    Sakums("12 konfektes - kā sadalīt?",
           zimejums=bildes([[("ripina", 6)], [("ripina", 6)]]),
           paraksts="Uz pusēm: 2 bērniem pa 6.",
           fakti=["Uz pusēm - 2 vienādas daļas.",
                  "Pa 2 - katram 2, un saskaita, cik bērnu.",
                  "12 pa 2 - pietiek 6 bērniem."]),

    Doma("Divas dalīšanas",
         "«Uz pusēm» - cik katrā daļā; «pa 2» - cik daļu.",
         soli=[
             "Uz pusēm: liek pa vienam pārmaiņus divās kaudzītēs.",
             "Tad skaita vienu kaudzīti.",
             "Pa 2: ņem pa divi un liek katru pāri atsevišķi.",
             "Tad skaita pārus.",
         ]),

    Slidnis("12 dala divos veidos", [
        {"v": "uz pusēm", "teksts": "2 daļas pa 6.",
         "zim": bildes([[("ripina", 6)], [("ripina", 6)]])},
        {"v": "pa 2", "teksts": "6 daļas pa 2.",
         "zim": bildes([["ripina", "ripina", "", "ripina", "ripina", "",
                         "ripina", "ripina"],
                        ["ripina", "ripina", "", "ripina", "ripina", "",
                         "ripina", "ripina"]])},
    ]),

    Ievadi("Uz pusēm", [
        {"jaut": "Puse no 10?", "atb": ["5"], "padoms": "5 + 5 = 10."},
        {"jaut": "Puse no 16?", "atb": ["8"], "padoms": "8 + 8."},
        {"jaut": "Puse no 20?", "atb": ["10"], "padoms": "10 + 10."},
        {"jaut": "Puse no 14?", "atb": ["7"], "padoms": "7 + 7."},
    ]),

    Ievadi("Pa 2", [
        {"jaut": "10 āboli pa 2 katram. Cik bērniem pietiks?", "atb": ["5"],
         "padoms": "2, 4, 6, 8, 10 - piecas reizes."},
        {"jaut": "18 zīmuļi pa 2. Cik bērniem?", "atb": ["9"],
         "padoms": "Skaiti pa 2 līdz 18."},
        {"jaut": "8 pīrāgi pa 2. Cik šķīvju?", "atb": ["4"],
         "padoms": "2 + 2 + 2 + 2."},
        {"jaut": "20 cimdi. Cik pāru?", "atb": ["10"],
         "padoms": "Pa 2."},
    ]),

    Varianti("Kura dalīšana?", [
        {"jaut": "«14 cepumus sadala 2 draugiem vienādi.» Ko jautā?",
         "opcijas": ["cik katram - uz pusēm", "cik draugiem - pa 2"],
         "jaukt": False, "pareizi": 0, "padoms": "Draugu skaits zināms."},
        {"jaut": "«14 cepumus liek pa 2 maisiņos.» Ko jautā?",
         "opcijas": ["cik katrā - uz pusēm", "cik maisiņu - pa 2"],
         "jaukt": False, "pareizi": 1, "padoms": "Maisiņu skaits nezināms."},
    ]),

    Pasaule("Kūka diviem",
            Ievadi("", [
                {"jaut": "Brāļi dala 16 zemenes uz pusēm. Cik katram?",
                 "atb": ["8"], "padoms": "8 + 8."},
                {"jaut": "Mamma liek pa 2 zemenēm uz katras kūciņas. Cik "
                         "kūciņām pietiek 16 zemeņu?", "atb": ["8"],
                 "padoms": "Pa 2."},
            ]),
            pavediens="virtuve",
            konteksts="Svētdienā cep zemeņu kūciņas.",
            kapec="Vienādi skaitļi - bet dažādi jautājumi."),

    Kopsavilkums([
        "Dalu daudzumu uz pusēm.",
        "Dalu daudzumu pa 2.",
        "Pastāstu, ar ko abas dalīšanas atšķiras.",
    ]),

    Majas([
        "Sadali 10 karotes uz pusēm - cik katrā kaudzītē?",
        "Sadali tās pašas pa 2 - cik kaudzīšu?",
        "Pastāsti mājiniekam atšķirību.",
    ]),
]
