# -*- coding: utf-8 -*-
"""3. klase, 113. stunda: «Cik rūtiņu ietilpst figūrā?»

Laukuma sākums. Laukums te vēl nav formula, bet skaits: cik vienādu rūtiņu
figūra aizņem. Tieši šis skatiens vēlāk padara formulu saprotamu, nevis
iekalamu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Cik rūtiņu ietilpst figūrā?"

MERKIS = ("Noteiksim figūras laukumu, skaitot vienādas rūtiņas.")

SATURS = [
    Sakums("Cik flīžu vajag virtuves grīdai?",
           zimejums=restis([["", "", "", "", ""],
                            ["", "", "", "", ""],
                            ["", "", "", "", ""]],
                           "15 rūtiņas"),
           paraksts="Laukums ir tas, cik vienādu rūtiņu figūra aizņem.",
           fakti=["Laukumu mēra ar vienādām rūtiņām.",
                  "Perimetrs ir apmale, laukums - tas, kas iekšā."]),

    Doma("Laukums ir rūtiņu skaits",
         "Lai uzzinātu laukumu, saskaiti, cik vienādu rūtiņu figūra aizņem.",
         soli=[
             "Noklāj figūru ar vienādām rūtiņām bez spraugām.",
             "Saskaiti rūtiņas.",
             "Ja kāda rūtiņa ir pusē, saliec divas puses kopā.",
             "Pieraksti laukumu kopā ar vienību - «rūtiņas».",
         ],
         pieze="Perimetrs un laukums ir dažādi lielumi: perimetru mēra "
               "centimetros, laukumu - kvadrātiņos."),

    Paraugs("Cik rūtiņu ir figūrā?",
            uzd="Taisnstūris ir 5 rūtiņas plats un 3 augsts. Cik rūtiņu tajā "
                "ir?",
            soli=[
                ("Pirmajā rindā 5 rūtiņas",
                 "Skaita vienu rindu."),
                ("Rindu ir 3",
                 "Katra tāda pati."),
                ("5 + 5 + 5 = 15",
                 "Kopā 15 rūtiņas."),
            ],
            atbilde="15 rūtiņas"),

    Ievadi("Saskaiti rūtiņas", [
        {"jaut": "Taisnstūris 5 rūtiņas plats, 3 augsts. Cik rūtiņu?",
         "atb": ["15"], "padoms": "Trīs rindas pa 5."},
        {"jaut": "Taisnstūris 4 rūtiņas plats, 6 augsts. Cik rūtiņu?",
         "atb": ["24"], "padoms": "Sešas rindas pa 4."},
        {"jaut": "Kvadrāts 5 x 5 rūtiņas. Cik rūtiņu?", "atb": ["25"],
         "padoms": "Piecas rindas pa 5."},
        {"jaut": "Taisnstūris 7 rūtiņas plats, 2 augsts. Cik rūtiņu?",
         "atb": ["14"], "padoms": "Divas rindas pa 7."},
        {"jaut": "Figūrā 20 rūtiņas, platums 4. Cik rindu ir?",
         "atb": ["5"], "padoms": "20 : 4."},
        {"jaut": "Figūrā 18 rūtiņas, rindu 3. Cik rūtiņu ir rindā?",
         "atb": ["6"], "padoms": "18 : 3."},
    ], pamats=4),

    Zimejums("Divas figūras, viens laukums",
             restis([["", "", "", "", "", ""],
                     ["", "", "", "", "", ""]],
                    "arī 12 rūtiņas"),
             paskaidro="Šeit ir divas rindas pa 6 - tikpat rūtiņu, cik "
                       "trijās rindās pa 4.",
             ievads="Forma cita, rūtiņu skaits var sakrist."),

    Varianti("Kas ir laukums?", [
        {"jaut": "Kas ir figūras laukums?",
         "opcijas": ["Rūtiņu skaits figūrā", "Malu garumu summa",
                     "Lielākā mala", "Virsotņu skaits"],
         "pareizi": 0, "padoms": "Perimetrs ir apmale."},
        {"jaut": "Taisnstūris 6 x 3 rūtiņas. Cik ir laukums?",
         "opcijas": ["18", "9", "12", "36"],
         "pareizi": 0, "padoms": "Trīs rindas pa 6."},
        {"jaut": "Kurš lielums mēra apmali?",
         "opcijas": ["Perimetrs", "Laukums", "Tilpums", "Rādiuss"],
         "pareizi": 0, "padoms": "Apkārt figūrai."},
        {"jaut": "Figūrā 30 rūtiņas, platums 5. Cik rindu?",
         "opcijas": ["6", "5", "25", "35"],
         "pareizi": 0, "padoms": "30 : 5."},
    ], pamats=4),

    Pasaule("Cik flīžu vajag grīdai?",
            Ievadi("", [
                {"jaut": "Grīda ir 5 flīzes plata un 4 garas. Cik flīžu "
                         "vajag?",
                 "atb": ["20"], "padoms": "4 rindas pa 5."},
                {"jaut": "Cik flīžu vajag grīdai 6 x 5?", "atb": ["30"],
                 "padoms": "5 rindas pa 6."},
                {"jaut": "Nopirka 40 flīzes. Cik paliks pāri no grīdas 6 x 5?",
                 "atb": ["10"], "padoms": "40 − 30."},
                {"jaut": "Cik flīžu ir rindā, ja grīdā to ir 48 un rindu ir "
                         "6?",
                 "atb": ["8"], "padoms": "48 : 6."},
            ]),
            pavediens="maja",
            konteksts="Flīzes klāj rindās bez spraugām - tieši tāpat, kā "
                      "rūtiņas noklāj figūru.",
            kapec="Flīžu skaits ir grīdas laukums, izteikts flīzēs."),

    Kopsavilkums([
        "Zinu, ka laukums ir vienādu rūtiņu skaits figūrā.",
        "Saskaitu rūtiņas pa rindām.",
        "Atšķiru laukumu no perimetra.",
        "Atrodu rindu skaitu, ja zināms laukums un platums.",
    ]),

    Majas([
        "Uzzīmē rūtiņu lapā taisnstūri 6 x 4 un saskaiti rūtiņas.",
        "Saskaiti, cik flīžu ir jūsu virtuves grīdā.",
        "Atrodi divas figūras ar vienādu rūtiņu skaitu.",
    ]),
]
