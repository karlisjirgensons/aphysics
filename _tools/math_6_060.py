# -*- coding: utf-8 -*-
"""6. klase, 60. stunda: «Cik dažādus ķermeņus var izveidot?»

Jauns temats sākas ar rokām. No pieciem vienādiem kubiem var salikt daudz
dažādu ķermeņu - un tiem visiem ir viens un tas pats tilpums, bet dažāda
virsma. Tas ir visa temata galvenais jautājums, uzdots jau pirmajā stundā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         kermenis)

TEMA = "Cik dažādus ķermeņus var izveidot?"

MERKIS = ("No dotā kubu skaita veidosim dažādus ķermeņus un raksturosim "
          "tos.")

SATURS = [
    Sakums("Četri kubi - astoņas figūras",
           zimejums=kermenis("kubs"),
           paraksts="Viens kubs. No četriem tādiem var salikt astoņas "
                    "dažādas figūras - un visām tilpums ir vienāds.",
           fakti=["Vienāds kubu skaits nenozīmē vienādu formu.",
                  "Tilpums ir kubu skaits - tas nemainās.",
                  "Virsma turpretī mainās: jo vairāk saskarēs, jo mazāka."]),

    Doma("Tilpums ir kubu skaits, virsma - atklātās rūtiņas",
         "No viena un tā paša kubu skaita var izveidot dažādus ķermeņus: "
         "tilpums tiem ir vienāds, bet virsmas laukums - ne.",
         soli=[
             "Saskaiti kubus - tas ir tilpums vienības kubos.",
             "Saliec kubus citā formā un pārbaudi, vai skaits nav mainījies.",
             "Saskaiti, cik kvadrātu ir redzami no ārpuses.",
             "Salīdzini divas figūras: kurai virsma ir mazāka?",
             "Pieraksti, kas mainījās un kas palika.",
         ],
         pieze="Katra saskare starp diviem kubiem paslēpj divas rūtiņas. "
               "Tāpēc kompakta figūra ir ar mazāko virsmu - un tieši tāpēc "
               "iepakojumi ir kastes, ne garas rindas."),

    Paraugs("Divas figūras no četriem kubiem",
            uzd="Cik liela ir virsma rindai no 4 kubiem un kvadrātam 2 x 2?",
            soli=[
                ("Vienam kubam ir 6 rūtiņas",
                 "Četriem kopā būtu 24."),
                ("Rindā ir 3 saskares, katra paslēpj 2 rūtiņas",
                 "24 − 6 = 18."),
                ("Kvadrātā 2 x 2 ir 4 saskares",
                 "24 − 8 = 16."),
                ("Tilpums abiem ir 4 kubi",
                 "Mainījās tikai virsma."),
            ],
            atbilde="rindai 18, kvadrātam 16 rūtiņas"),

    Ievadi("Saskaiti kubus un rūtiņas", [
        {"jaut": "Cik rūtiņu ir vienam kubam?",
         "atb": ["6"], "padoms": "Seši kvadrāti."},
        {"jaut": "Cik rūtiņu ir divu kubu figūrai?",
         "atb": ["10"], "padoms": "12 − 2."},
        {"jaut": "Cik vienības kubu ir figūrā 2 x 2 x 2?",
         "atb": ["8"], "padoms": "2 · 2 · 2."},
        {"jaut": "Cik rūtiņu ir figūrai 2 x 2 x 2?",
         "atb": ["24"], "padoms": "6 skaldnes pa 4 rūtiņām."},
        {"jaut": "Cik vienības kubu ir figūrā 3 x 2 x 1?",
         "atb": ["6"], "padoms": "3 · 2 · 1."},
        {"jaut": "Rindā no 5 kubiem ir cik saskares?",
         "atb": ["4"], "padoms": "Par vienu mazāk nekā kubu."},
    ], pamats=4),

    Petijums("Saliec figūras no kubiem",
             vajag="5 vienādi kubiņi vai cukurgraudi",
             soli=[
                 "Saliec no 4 kubiem tik dažādu figūru, cik vari.",
                 "Uzzīmē katru figūru un pieraksti tās tilpumu.",
                 "Saskaiti katrai redzamās rūtiņas.",
                 "Atrodi figūru ar vismazāko virsmu.",
             ],
             secinajums="Vismazākā virsma ir viskompaktākajai figūrai - tā, "
                        "kurā kubiem ir visvairāk saskaru."),

    Varianti("Kas mainās, kas ne?", [
        {"jaut": "Pārliekot kubus citā formā, kas paliek nemainīgs?",
         "opcijas": ["Tilpums", "Virsmas laukums", "Augstums", "Nekas"],
         "pareizi": 0,
         "padoms": "Kubu skaits nemainās."},
        {"jaut": "Kurai figūrai no 8 kubiem ir vismazākā virsma?",
         "opcijas": ["Kubam 2 x 2 x 2", "Rindai no 8 kubiem",
                     "Figūrai 4 x 2 x 1", "Visām vienāda"],
         "pareizi": 0,
         "padoms": "Jo kompaktāka, jo mazāka virsma."},
        {"jaut": "Cik rūtiņu paslēpj viena saskare?",
         "opcijas": ["2", "1", "4", "6"],
         "pareizi": 0,
         "padoms": "Katram kubam pa vienai."},
        {"jaut": "Kāpēc iepakojumi ir kastes, nevis garas rindas?",
         "opcijas": ["Jo kastei vajag mazāk materiāla",
                     "Jo kaste ir skaistāka",
                     "Jo kastei ir lielāks tilpums",
                     "Tas ir vienalga"],
         "pareizi": 0,
         "padoms": "Mazāka virsma - mazāk kartona."},
    ], pamats=4),

    Pasaule("Kā salikt kravu konteinerā?",
            Ievadi("", [
                {"jaut": "Konteinerā ir 4 x 3 x 2 kastes. Cik kastu ir kopā?",
                 "atb": ["24"], "padoms": "4 · 3 · 2."},
                {"jaut": "Tās pašas kastes sakrauj 6 x 2 x 2. Cik kastu ir "
                         "kopā?",
                 "atb": ["24"], "padoms": "Skaits nemainās."},
                {"jaut": "Cik kastu ir slānī 4 x 3?",
                 "atb": ["12"], "padoms": "4 · 3."},
                {"jaut": "Cik slāņu ir konteinerā ar 24 kastēm, ja slānī ir "
                         "12?",
                 "atb": ["2"], "padoms": "24 : 12."},
            ]),
            pavediens="tehnika",
            konteksts="Kravas kārtojumu var mainīt, bet kastu skaits paliek "
                      "tas pats - mainās tikai konteinera forma.",
            kapec="Tilpums ir skaits; forma nosaka tikai virsmu."),

    Zimejums("Kubs un kvadrs",
             kermenis("kvadrs"),
             paskaidro="Kvadrs ir izstiepts kubs: skaldņu skaits tas pats, "
                       "bet malas - dažādas.",
             ievads="Abi ir daudzskaldņi ar sešām skaldnēm."),

    Kopsavilkums([
        "Veidoju dažādus ķermeņus no viena kubu skaita.",
        "Zinu, ka tilpums ir kubu skaits un tas nemainās.",
        "Saskaitu redzamās rūtiņas un salīdzinu virsmas.",
        "Paskaidroju, kāpēc kompaktai figūrai ir mazāka virsma.",
    ]),

    Majas([
        "Saliec no 6 kubiņiem trīs dažādas figūras un uzzīmē tās.",
        "Atrodi to, kurai virsma ir vismazākā.",
        "Pieraksti, kurus mājas priekšmetus var uzskatīt par kvadriem.",
    ]),
]
