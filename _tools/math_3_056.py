# -*- coding: utf-8 -*-
"""3. klase, 56. stunda: «Kāds perimetrs rodas, figūras savietojot?»

Temata pēdējā mācību stunda. Saliekot divus taisnstūrus kopā, perimetrs nav
abu perimetru summa - saskares mala pazūd no apmales. Tas ir pirmais
gadījums, kad «kopā» nenozīmē «saskaitīt», un to var redzēt tikai zīmējumā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         figura)

TEMA = "Kāds perimetrs rodas, figūras savietojot?"

MERKIS = ("Kombinēsim figūras un pierakstīsim izteiksmi jaunās figūras "
          "perimetram.")

SATURS = [
    Sakums("Kāpēc divu kvadrātu perimetrs nav divi perimetri?",
           zimejums=figura([(0, 0), (8, 0), (8, 4), (0, 4)],
                           [(4, -0.6, "8"), (8.8, 2, "4")],
                           "divi kvadrāti 4 x 4 blakus"),
           paraksts="Saskares mala vairs nav apmalē - tā ir iekšā.",
           fakti=["Viena kvadrāta 4 x 4 perimetrs ir 16.",
                  "Divi kopā dod 24, nevis 32 - divas malas pazuda."]),

    Doma("Saskares malas perimetrā neieiet",
         "Savienojot figūras, no kopējās apmales pazūd tieši divas saskares "
         "malas.",
         soli=[
             "Saskaiti abu figūru perimetrus atsevišķi.",
             "Atrodi, cik gara ir saskares mala.",
             "Atņem to divreiz - reizi no katras figūras.",
             "Pārbaudi, saskaitot jaunās figūras malas pa apmali.",
         ],
         pieze="Tāpēc divas istabas kopā prasa mazāk grīdlīstes nekā abas "
               "atsevišķi: kopējā siena grīdlīsti neprasa."),

    Paraugs("Kāds perimetrs ir diviem kvadrātiem blakus?",
            uzd="Divus kvadrātus ar malu 4 cm noliek blakus. Kāds ir "
                "iegūtās figūras perimetrs?",
            soli=[
                ("4 · 4 = 16; 16 + 16 = 32",
                 "Abu kvadrātu perimetri atsevišķi."),
                ("Saskares mala ir 4 cm",
                 "Tieši tā pazūd no apmales - divas reizes."),
                ("32 − 2 · 4 = 24",
                 "Jaunās figūras perimetrs."),
                ("2 · (8 + 4) = 24",
                 "Pārbaude: sanāca taisnstūris 8 x 4."),
            ],
            atbilde="24 cm"),

    Petijums("Saliec figūras un izmēri apmali",
             vajag="rūtiņu lapa, šķēres un zīmulis",
             soli=[
                 "Izgriez divus kvadrātus ar malu 3 rūtiņas.",
                 "Noliec tos blakus un saskaiti apmales rūtiņas.",
                 "Noliec tos vienu virs otra un saskaiti vēlreiz.",
                 "Noliec tos tā, lai saskartos tikai stūri, un saskaiti.",
             ],
             secinajums="Jo garāka saskares mala, jo mazāks kopējais "
                        "perimetrs."),

    Ievadi("Aprēķini jauno perimetru", [
        {"jaut": "Divi kvadrāti ar malu 3 cm blakus. Cik ir perimetrs?",
         "atb": ["18"], "padoms": "Sanāk taisnstūris 6 x 3."},
        {"jaut": "Divi kvadrāti ar malu 5 cm blakus. Cik ir perimetrs?",
         "atb": ["30"], "padoms": "Taisnstūris 10 x 5."},
        {"jaut": "Trīs kvadrāti ar malu 2 cm rindā. Cik ir perimetrs?",
         "atb": ["16"], "padoms": "Taisnstūris 6 x 2."},
        {"jaut": "Divi taisnstūri 4 x 2 cm, salikti pa garo malu. Cik ir "
                 "perimetrs?",
         "atb": ["16"], "padoms": "Sanāk kvadrāts 4 x 4."},
        {"jaut": "Četri kvadrāti ar malu 3 cm rindā. Cik ir perimetrs?",
         "atb": ["30"], "padoms": "Taisnstūris 12 x 3."},
        {"jaut": "Četri kvadrāti ar malu 3 cm kvadrātā 2 x 2. Cik ir "
                 "perimetrs?",
         "atb": ["24"], "padoms": "Sanāk kvadrāts 6 x 6."},
    ], pamats=4),

    Zimejums("Viena figūra, divi salikumi",
             figura([(0, 0), (4, 0), (4, 2), (2, 2), (2, 4), (0, 4)],
                    [(2, -0.6, "4"), (4.8, 1, "2")],
                    "«L» burta figūra"),
             paskaidro="Arī šeit perimetru saskaita pa apmali - iekšējās "
                       "malas tajā neieiet.",
             ievads="No diviem taisnstūriem var salikt arī šādu figūru."),

    Varianti("Kā mainās perimetrs?", [
        {"jaut": "Divus kvadrātus noliek blakus. Kas notiek ar kopējo "
                 "perimetru?",
         "opcijas": ["Tas kļūst mazāks par abu summu",
                     "Tas ir tieši abu summa", "Tas kļūst lielāks",
                     "Tas nemainās"],
         "pareizi": 0, "padoms": "Divas malas pazūd no apmales."},
        {"jaut": "Cik gara mala pazūd, saliekot divus kvadrātus ar malu 6?",
         "opcijas": ["2 malas pa 6", "1 mala pa 6", "4 malas pa 6",
                     "Neviena"],
         "pareizi": 0, "padoms": "Pa vienai no katras figūras."},
        {"jaut": "Kad kopējais perimetrs ir vismazākais?",
         "opcijas": ["Kad saskares mala ir visgarākā",
                     "Kad figūras saskaras stūrī",
                     "Kad figūras ir tālu viena no otras",
                     "Tas vienmēr ir vienāds"],
         "pareizi": 0, "padoms": "Jo vairāk pazūd, jo mazāks perimetrs."},
        {"jaut": "Divi taisnstūri 5 x 2 salikti pa garo malu. Kāds ir "
                 "perimetrs?",
         "opcijas": ["18 cm", "28 cm", "14 cm", "20 cm"],
         "pareizi": 0, "padoms": "Sanāk taisnstūris 5 x 4."},
    ], pamats=4),

    Pasaule("Cik grīdlīstes vajag divām istabām?",
            Ievadi("", [
                {"jaut": "Istaba 5 m x 4 m. Cik metru ir perimetrs?",
                 "atb": ["18"], "padoms": "2 · 9."},
                {"jaut": "Otra istaba 5 m x 3 m. Cik metru ir perimetrs?",
                 "atb": ["16"], "padoms": "2 · 8."},
                {"jaut": "Cik metru ir abu perimetru summa?",
                 "atb": ["34"], "padoms": "18 + 16."},
                {"jaut": "Istabām ir kopēja 5 m siena, kur grīdlīste nav "
                         "vajadzīga abās pusēs. Cik metru tad vajag?",
                 "atb": ["29"], "padoms": "34 − 5."},
            ]),
            pavediens="maja",
            konteksts="Remontā kopējā siena parādās abos rēķinos - tāpēc "
                      "materiāla vajag mazāk, nekā rāda summa.",
            kapec="Bez šīs pārbaudes remontam pērk par daudz."),

    Kopsavilkums([
        "Aprēķinu jaunas figūras perimetru, savienojot divas figūras.",
        "Zinu, ka saskares malas perimetrā neieiet.",
        "Pierakstu perimetru kā izteiksmi.",
        "Pārbaudu rezultātu, saskaitot malas pa apmali.",
    ]),

    Majas([
        "Saliec divus vienādus taisnstūrus divos dažādos veidos un salīdzini "
        "perimetrus.",
        "Uzzīmē «L» formas figūru un aprēķini tās perimetru.",
        "Pārlasi tematu un atzīmē, kas vēl jāatkārto pirms pārbaudes darba.",
    ], ievads="Šī ir pēdējā stunda pirms pārbaudes darba."),
]
