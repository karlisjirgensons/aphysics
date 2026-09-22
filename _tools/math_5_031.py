# -*- coding: utf-8 -*-
"""5. klase, 31. stunda: «Cik veidos skaitli var uzrakstīt kā reizinājumu?»

No taisnstūra uz pierakstu. Divu reizinātāju sadalījums jau zināms (30.
stunda); te reizinātāju kļūst trīs un vairāk, un parādās doma, ka sadalīt var
tālāk, līdz vairs nevar - tas ir tiešs ceļš uz pirmreizinātājiem 34. stundā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Cik veidos skaitli var uzrakstīt kā reizinājumu?"

MERKIS = ("Iemācīsimies izteikt doto skaitli kā divu, trīs vai vairāku "
          "skaitļu reizinājumu.")

SATURS = [
    Sakums("Cik reizinājumu slēpjas skaitlī 36?",
           fakti=["36 = 4 · 9 un 36 = 6 · 6.",
                  "Bet arī 36 = 2 · 2 · 9 un 36 = 2 · 2 · 3 · 3.",
                  "Katru reizinātāju, ja var, sadala tālāk."]),

    Doma("Sadali reizinātāju, un reizinājums kļūst garāks",
         "Ja kādu reizinātāju aizstāj ar tā reizinājumu, kopējais rezultāts "
         "nemainās.",
         soli=[
             "Uzraksti skaitli kā divu reizinātāju reizinājumu.",
             "Paskaties, vai kādu no tiem var sadalīt tālāk.",
             "Aizstāj to ar tā reizinātājiem.",
             "Turpini, kamēr neviens vairs nesadalās.",
             "Pārbaudi: sareizini visu un salīdzini ar sākuma skaitli.",
         ],
         pieze="Reizinātāju 1 pierakstā neraksta: 1 · 36 gan ir pareizi, bet "
               "no 1 nekā jauna neuzzina - to var pierakstīt bezgalīgi daudz "
               "reižu."),

    Paraugs("Sadali 36 pēc iespējas tālāk",
            uzd="Uzraksti 36 kā divu, trīs un četru skaitļu reizinājumu.",
            soli=[
                ("Divi: 36 = 4 · 9",
                 "Vienkāršākais sadalījums."),
                ("Trīs: 4 = 2 · 2, tātad 36 = 2 · 2 · 9",
                 "Sadalām pirmo reizinātāju."),
                ("Četri: 9 = 3 · 3, tātad 36 = 2 · 2 · 3 · 3",
                 "Sadalām arī otro."),
                ("Tālāk nevar: 2 un 3 nesadalās",
                 "Esam nonākuši līdz galam."),
            ],
            atbilde="36 = 4 · 9 = 2 · 2 · 9 = 2 · 2 · 3 · 3"),

    Ievadi("Atrodi trūkstošo reizinātāju", [
        {"jaut": "36 = 4 · ? Cik ir trūkstošais?", "atb": ["9"],
         "padoms": "36 : 4."},
        {"jaut": "36 = 2 · 2 · ? Cik ir trūkstošais?", "atb": ["9"],
         "padoms": "36 : 4."},
        {"jaut": "60 = 6 · ? Cik ir trūkstošais?", "atb": ["10"],
         "padoms": "60 : 6."},
        {"jaut": "60 = 2 · 3 · ? Cik ir trūkstošais?", "atb": ["10"],
         "padoms": "60 : 6."},
        {"jaut": "48 = 2 · 2 · 2 · ? Cik ir trūkstošais?", "atb": ["6"],
         "padoms": "48 : 8."},
        {"jaut": "Cik reizinātāju ir pierakstā 2 · 2 · 3 · 3?", "atb": ["4"],
         "padoms": "Saskaiti tos."},
        {"jaut": "100 = 4 · ? Cik ir trūkstošais?", "atb": ["25"],
         "padoms": "100 : 4."},
        {"jaut": "100 = 2 · 2 · 5 · ? Cik ir trūkstošais?", "atb": ["5"],
         "padoms": "100 : 20."},
    ], pamats=4,
        ievads="Trūkstošo reizinātāju atrod ar dalīšanu."),

    Varianti("Kurš pieraksts ir pareizs?", [
        {"jaut": "Kurš reizinājums dod 36?",
         "opcijas": ["2 · 2 · 3 · 3", "2 · 3 · 3 · 3", "2 · 2 · 2 · 3",
                     "3 · 3 · 3"],
         "pareizi": 0,
         "padoms": "4 · 9 = 36."},
        {"jaut": "Kāpēc reizinātāju 1 pierakstā neraksta?",
         "opcijas": ["No tā neuzzina neko jaunu",
                     "Jo 1 nav skaitlis",
                     "Jo ar 1 nedrīkst reizināt",
                     "Jo tad reizinājums mainās"],
         "pareizi": 0,
         "padoms": "1 · 1 · 1 · 36 arī ir 36."},
        {"jaut": "Kad reizinājumu vairs nevar pagarināt?",
         "opcijas": ["Kad neviens reizinātājs vairs nesadalās",
                     "Kad reizinātāju ir četri",
                     "Kad skaitlis ir pāra",
                     "Kad atbilde ir apaļa"],
         "pareizi": 0,
         "padoms": "2 un 3 tālāk nesadalās."},
        {"jaut": "Kurš skaitlis nav 60 reizinātājs?",
         "opcijas": ["8", "6", "10", "5"],
         "pareizi": 0,
         "padoms": "60 : 8 nav vesels skaitlis."},
    ], pamats=4),

    Pasaule("Kā salikt dēļus kaudzē?",
            Ievadi("", [
                {"jaut": "36 dēļus liek 4 kaudzēs. Cik dēļu kaudzē?",
                 "atb": ["9"], "padoms": "36 : 4."},
                {"jaut": "60 flīzes 6 kastēs. Cik flīžu kastē?",
                 "atb": ["10"], "padoms": "60 : 6."},
                {"jaut": "48 skrūves paciņās pa 2, paciņas kastēs pa 4, "
                         "kastes plauktos pa 2. Cik plauktu vajag?",
                 "atb": ["3"], "padoms": "48 : 2 : 4 : 2."},
                {"jaut": "100 podiņus liek 4 rindās pa 5 plauktos. Cik "
                         "podiņu vienā vietā?",
                 "atb": ["5"], "padoms": "100 : 4 : 5."},
            ]),
            pavediens="maja",
            konteksts="Materiālu pako pa paciņām, kastēm un paletēm - tas ir "
                      "viens skaitlis, sadalīts vairākos reizinātājos.",
            kapec="Katrs iepakojuma līmenis ir viens reizinātājs."),

    Kopsavilkums([
        "Uzrakstu skaitli kā divu, trīs vai vairāku skaitļu reizinājumu.",
        "Sadalu reizinātāju tālāk, kamēr vairs nevar.",
        "Zinu, kāpēc reizinātāju 1 pierakstā neraksta.",
        "Pārbaudu sadalījumu, sareizinot visus reizinātājus.",
    ]),

    Majas([
        "Uzraksti 48 kā divu, trīs un četru skaitļu reizinājumu.",
        "Atrodi skaitli, kuru var uzrakstīt kā piecu skaitļu reizinājumu.",
        "Pārbaudi katru savu sadalījumu ar reizināšanu.",
    ]),
]
