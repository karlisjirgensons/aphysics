# -*- coding: utf-8 -*-
"""3. klase, 74. stunda: «Kā sadalīt sloksnīti trīs daļās?»

Trešdaļu ar locīšanu uz pusēm nedabū - tāpēc šī stunda ir grūtāka par
iepriekšējo un arī vērtīgāka: skolēns pats atrod veidu, kā sadalīt trīs daļās,
un tad pārbauda, vai daļas tiešām ir vienādas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         dala)

TEMA = "Kā sadalīt sloksnīti trīs daļās?"

MERKIS = ("Salocīsim sloksnīti 3 un 6 vienādās daļās un pārbaudīsim, vai "
          "daļas ir vienādas.")

SATURS = [
    Sakums("Kāpēc trīs daļas ir grūtāk nekā četras?",
           zimejums=dala(3, 1, "1/3", "sloksnīte trijās daļās"),
           paraksts="Trešdaļu ar vienu locījumu uz pusēm nedabū.",
           fakti=["Locot uz pusēm, sanāk 2, 4, 8 daļas - nekad 3.",
                  "Trešdaļu meklē, sloksnīti saritinot un pielāgojot."]),

    Doma("Vienādību pārbauda, uzliekot vienu daļu uz otras",
         "Ja trīs daļas sakrīt, tās ir vienādas; ja ne - sloksnīti pielāgo "
         "un mēģina vēlreiz.",
         soli=[
             "Saritini sloksnīti trīs kārtās, vēl nesalocot.",
             "Pabīdi galus, līdz visas trīs kārtas sakrīt.",
             "Tikai tad saspied locījumus.",
             "Atloc un pārbaudi, uzliekot daļas vienu uz otras.",
         ],
         pieze="Ja katru trešdaļu vēl saloc uz pusēm, sanāk sešas daļas - "
               "tāpēc sestdaļa ir puse no trešdaļas."),

    Petijums("Saloc sloksnīti trijās daļās",
             vajag="papīra sloksnīte, lineāls un zīmulis",
             soli=[
                 "Saritini sloksnīti trīs kārtās un pielāgo galus.",
                 "Saspied locījumus un atloc.",
                 "Izmēri katru daļu ar lineālu.",
                 "Saloc katru trešdaļu uz pusēm un saskaiti daļas.",
             ],
             secinajums="Ja visas trīs daļas ir vienāda garuma, sadalījums "
                        "izdevās; seši locījumi dod sestdaļas."),

    Paraugs("Cik gara ir viena trešdaļa?",
            uzd="Sloksnīte ir 24 cm gara. Cik gara ir viena trešdaļa?",
            soli=[
                ("24 : 3 = 8",
                 "Visu garumu dala ar daļu skaitu."),
                ("8 cm",
                 "Tik gara ir viena trešdaļa."),
                ("3 · 8 = 24",
                 "Pārbaude: trīs trešdaļas dod visu sloksnīti."),
            ],
            atbilde="8 cm"),

    Ievadi("Cik gara ir viena daļa?", [
        {"jaut": "Sloksnīte 24 cm. Cik centimetru ir {1|3}?",
         "atb": ["8"], "padoms": "24 : 3."},
        {"jaut": "Sloksnīte 24 cm. Cik centimetru ir {1|6}?",
         "atb": ["4"], "padoms": "24 : 6."},
        {"jaut": "Sloksnīte 30 cm. Cik centimetru ir {1|3}?",
         "atb": ["10"], "padoms": "30 : 3."},
        {"jaut": "Sloksnīte 18 cm. Cik centimetru ir {1|6}?",
         "atb": ["3"], "padoms": "18 : 6."},
        {"jaut": "Sloksnīte 36 cm. Cik centimetru ir {2|3}?",
         "atb": ["24"], "padoms": "36 : 3 = 12; 2 · 12."},
        {"jaut": "Viena trešdaļa ir 7 cm. Cik gara ir visa sloksnīte?",
         "atb": ["21"], "padoms": "3 · 7."},
    ], pamats=4),

    Zimejums("Sestdaļas",
             dala(6, 1, "1/6", "tā pati sloksnīte sešās daļās"),
             paskaidro="Katra trešdaļa, salocīta uz pusēm, dod divas "
                       "sestdaļas.",
             ievads="Salīdzini ar stundas sākuma zīmējumu."),

    Varianti("Kā iegūt trešdaļu?", [
        {"jaut": "Vai trešdaļu var iegūt, locot uz pusēm?",
         "opcijas": ["Nē, tā sanāk 2, 4, 8 daļas", "Jā, ar vienu locījumu",
                     "Jā, ar diviem locījumiem", "Jā, vienmēr"],
         "pareizi": 0, "padoms": "Locot uz pusēm, daļu skaits divkāršojas."},
        {"jaut": "Cik sestdaļu ir vienā trešdaļā?",
         "opcijas": ["2", "3", "6", "1"],
         "pareizi": 0, "padoms": "Trešdaļu saloc uz pusēm."},
        {"jaut": "Kura daļa ir lielāka?",
         "opcijas": ["{1|3}", "{1|6}", "Abas vienādas", "To nevar pateikt"],
         "pareizi": 0, "padoms": "Jo vairāk daļu, jo mazāka katra."},
        {"jaut": "Sloksnīte 12 cm. Cik centimetru ir {1|3}?",
         "opcijas": ["4 cm", "3 cm", "6 cm", "9 cm"],
         "pareizi": 0, "padoms": "12 : 3."},
    ], pamats=4),

    Pasaule("Kā sadalīt mīklu?",
            Ievadi("", [
                {"jaut": "Mīklas gabals 300 g. Cik gramu ir {1|3}?",
                 "atb": ["100"], "padoms": "300 : 3."},
                {"jaut": "Cik gramu ir {2|3}?",
                 "atb": ["200"], "padoms": "2 · 100."},
                {"jaut": "Mīklu sadala 6 vienādos klaipiņos. Cik gramu ir "
                         "viens?",
                 "atb": ["50"], "padoms": "300 : 6."},
                {"jaut": "Cik klaipiņu ir {1|3} no mīklas?",
                 "atb": ["2"], "padoms": "6 : 3."},
            ]),
            pavediens="virtuve",
            konteksts="Receptē bieži raksta «trešdaļu mīklas» - un to vienmēr "
                       "var izmērīt ar svariem.",
            kapec="Kad zini veselo, jebkuru daļu var izrēķināt ar dalīšanu."),

    Kopsavilkums([
        "Salocu sloksnīti 3 un 6 vienādās daļās.",
        "Pārbaudu daļu vienādību ar mērījumu.",
        "Izrēķinu vienas daļas garumu, dalot veselo ar daļu skaitu.",
        "Zinu, ka sestdaļa ir puse no trešdaļas.",
    ]),

    Majas([
        "Saloc papīra sloksnīti trijās vienādās daļās un izmēri tās.",
        "Sadali auklu trijās vienādās daļās un pārbaudi ar lineālu.",
        "Atrodi receptē daļu un pasaki, cik tā ir gramos.",
    ]),
]
