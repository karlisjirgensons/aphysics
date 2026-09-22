# -*- coding: utf-8 -*-
"""6. klase, 67. stunda: «Cik liela ir kubu figūras virsma?»

Atgriešanās pie kubiem no temata pirmās stundas, tikai tagad ar skaitļiem.
Virsmu te nevar izrēķināt pēc formulas - to jāsaskaita, un tieši tas parāda,
kāpēc forma maina virsmu, bet ne tilpumu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Cik liela ir kubu figūras virsma?"

MERKIS = ("Iemācīsimies aprēķināt virsmas laukumu ķermenim, kas sastāv no "
          "vienādiem kubiem.")

SATURS = [
    Sakums("Formulas nav - ir skaitīšana",
           zimejums=restis([["priekša", "aizmugure"],
                            ["kreisais", "labais"],
                            ["augša", "apakša"]]),
           paraksts="Katram no sešiem virzieniem saskaita redzamos "
                    "kvadrātus un summē.",
           fakti=["Vienam kubam ir 6 kvadrāti.",
                  "Katra saskare paslēpj divus kvadrātus.",
                  "Tāpēc virsmu var rēķināt divos veidos - abi dod vienu."]),

    Doma("Skaiti pa virzieniem vai atņem saskares",
         "Kubu figūras virsmu var iegūt divos ceļos: saskaitot redzamos "
         "kvadrātus no visām sešām pusēm vai no kopējā skaita atņemot "
         "saskares.",
         soli=[
             "Saskaiti kubus figūrā.",
             "Reizini ar 6 - tik kvadrātu būtu bez saskarēm.",
             "Saskaiti saskares starp blakus esošiem kubiem.",
             "Atņem divas reizes saskaru skaitu.",
             "Pārbaudi otrā ceļā: saskaiti redzamo no visām sešām pusēm.",
         ],
         pieze="Otrais ceļš ir drošāks, kad figūra ir sarežģīta: no katras "
               "puses fotografē un saskaita kvadrātus. Bet saskaru "
               "atņemšana ir ātrāka."),

    Paraugs("Virsma rindai no 3 kubiem",
            uzd="Trīs vienības kubi salikti rindā. Cik liela ir figūras "
                "virsma?",
            soli=[
                ("3 · 6 = 18 kvadrāti",
                 "Bez saskarēm."),
                ("Saskares ir 2",
                 "Starp 1. un 2. un starp 2. un 3. kubu."),
                ("2 · 2 = 4 paslēptie kvadrāti",
                 "Katra saskare paslēpj divus."),
                ("18 − 4 = 14 kvadrāti",
                 "Tā ir figūras virsma."),
            ],
            atbilde="14 vienības kvadrāti"),

    Ievadi("Saskaiti virsmu", [
        {"jaut": "Cik kvadrātu ir diviem kubiem rindā?",
         "atb": ["10"], "padoms": "12 − 2."},
        {"jaut": "Cik kvadrātu ir trim kubiem rindā?",
         "atb": ["14"], "padoms": "18 − 4."},
        {"jaut": "Cik kvadrātu ir četriem kubiem rindā?",
         "atb": ["18"], "padoms": "24 − 6."},
        {"jaut": "Cik kvadrātu ir kubam 2 x 2 x 2?",
         "atb": ["24"], "padoms": "6 skaldnes pa 4."},
        {"jaut": "Cik saskaru ir kubā 2 x 2 x 2?",
         "atb": ["12"], "padoms": "48 − 24 = 24; 24 : 2."},
        {"jaut": "Cik kvadrātu ir figūrai 3 x 2 x 1?",
         "atb": ["22"], "padoms": "2 · (6 + 3 + 2)."},
    ], pamats=4),

    Petijums("Saliec un saskaiti",
             vajag="6 vienādi kubiņi",
             soli=[
                 "Saliec no 6 kubiem rindu un saskaiti tās virsmu.",
                 "Saliec no tiem pašiem kubiem figūru 3 x 2 x 1.",
                 "Saskaiti arī tās virsmu.",
                 "Saliec vēl vienu formu un salīdzini visas trīs.",
             ],
             secinajums="Tilpums visām figūrām ir 6 kubi, bet virsma "
                        "atšķiras - vismazākā tā ir viskompaktākajai."),

    Varianti("Kā mainās virsma?", [
        {"jaut": "Kas paslēpj kvadrātus?",
         "opcijas": ["Katra saskare starp diviem kubiem",
                     "Katrs jauns kubs", "Figūras augstums", "Nekas"],
         "pareizi": 0,
         "padoms": "Divi kvadrāti uz vienu saskari."},
        {"jaut": "Kurai figūrai no 8 kubiem ir vislielākā virsma?",
         "opcijas": ["Rindai no 8 kubiem", "Kubam 2 x 2 x 2",
                     "Figūrai 4 x 2 x 1", "Visām vienāda"],
         "pareizi": 0,
         "padoms": "Vismazāk saskaru - vislielākā virsma."},
        {"jaut": "Tilpums figūrai no 8 kubiem ir...",
         "opcijas": ["8 vienības kubi", "24 vienības kubi",
                     "atkarīgs no formas", "48 vienības kubi"],
         "pareizi": 0,
         "padoms": "Tilpums ir kubu skaits."},
        {"jaut": "Ja pieliek vienu kubu pie figūras malas, virsma...",
         "opcijas": ["palielinās par 4 kvadrātiem",
                     "palielinās par 6 kvadrātiem",
                     "samazinās", "nemainās"],
         "pareizi": 0,
         "padoms": "6 jauni, 2 paslēpjas."},
    ], pamats=4),

    Pasaule("Cik plēves vajag kravai?",
            Ievadi("", [
                {"jaut": "Krava ir 4 x 3 x 2 kastes. Cik kastu ir kopā?",
                 "atb": ["24"], "padoms": "4 · 3 · 2."},
                {"jaut": "Cik kastu malu ir redzamas no augšas?",
                 "atb": ["12"], "padoms": "4 · 3."},
                {"jaut": "Cik kastu malu ir redzamas no priekšas?",
                 "atb": ["8"], "padoms": "4 · 2."},
                {"jaut": "Cik kastu malu ir redzamas no sāna?",
                 "atb": ["6"], "padoms": "3 · 2."},
            ]),
            pavediens="tehnika",
            konteksts="Kravu aptin ar plēvi pa ārpusi, tāpēc svarīgs ir "
                      "virsmas, nevis tilpuma lielums.",
            kapec="Kompaktāka krava prasa mazāk plēves."),

    Zimejums("Virsmas skaitīšana pa virzieniem",
             restis([["4 · 3", "4 · 2", "3 · 2"],
                     ["12", "8", "6"]],
                    "augša / priekša / sāns"),
             paskaidro="Katrs skaitlis jāņem divreiz: 2 · (12 + 8 + 6) = "
                       "52 kvadrāti.",
             ievads="Ja figūra ir kvadrs, skaitīšana kļūst par formulu."),

    Kopsavilkums([
        "Aprēķinu virsmas laukumu figūrai no vienādiem kubiem.",
        "Lietoju abus ceļus: saskares un skaitīšanu pa virzieniem.",
        "Zinu, ka viena saskare paslēpj divus kvadrātus.",
        "Paskaidroju, kāpēc forma maina virsmu, bet ne tilpumu.",
    ]),

    Majas([
        "Saliec no 5 kubiem divas figūras un saskaiti to virsmas.",
        "Atrodi, kurai no tām virsma ir lielāka.",
        "Pieraksti, cik saskaru bija katrā figūrā.",
    ]),
]
