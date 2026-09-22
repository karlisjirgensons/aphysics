# -*- coding: utf-8 -*-
"""5. klase, 30. stunda: «Cik dažādi var sadalīt šokolādi?»

Mikrotemata sākums, un reizinātāji te vēl nav skaitļu teorija - tie ir
taisnstūri. Šokolādes tāfelīte, sadalīta rindās un kolonnās, ir tas modelis,
uz kura vēlāk balstās gan dalītāji, gan pirmskaitļi: skaitlis ir pirmskaitlis
tieši tad, ja no tā nevar salikt nevienu citu taisnstūri kā vienu rindu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Cik dažādi var sadalīt šokolādi?"

MERKIS = ("Mācīsimies sadalīt objektu vienādās daļās un pierakstīt šo "
          "sadalījumu ar reizinājumu.")

SATURS = [
    Sakums("Viena tāfelīte, vairāki sadalījumi",
           zimejums=restis([[""] * 6 for _ in range(4)]),
           paraksts="4 rindas pa 6 rūtiņām - kopā 24. Pieraksta to kā 4 · 6.",
           fakti=["Rūtiņu skaits nemainās, lai kā tāfelīti lauztu.",
                  "Mainās tikai tas, cik rindu un cik kolonnu."]),

    Doma("Rindas reiz kolonnas - tas ir reizinājums",
         "Katrs veids, kā skaitli salikt taisnstūrī, ir viens tā pieraksts "
         "ar reizinājumu.",
         soli=[
             "Saskaiti, cik rūtiņu ir pavisam.",
             "Izvēlies, cik rindu būs.",
             "Pārbaudi, vai rūtiņas sadalās pa rindām vienādi.",
             "Ja sadalās - pieraksti to kā rindas · kolonnas.",
             "Ja nesadalās - tāds sadalījums neder.",
         ],
         pieze="24 rūtiņas var salikt pa 1, 2, 3, 4, 6, 8, 12 vai 24 rindām, "
               "bet ne pa 5: 24 rūtiņas piecās vienādās rindās nesadalās."),

    Zimejums("Tā pati tāfelīte citādi",
             restis([[""] * 8 for _ in range(3)]),
             paskaidro="3 rindas pa 8 rūtiņām - atkal 24, tikai cits "
                       "taisnstūris: 3 · 8.",
             ievads="Rūtiņu skaits tas pats, forma cita."),

    Paraugs("Visi 24 rūtiņu taisnstūri",
            uzd="Cik dažādos taisnstūros var salikt 24 rūtiņas?",
            soli=[
                ("1 · 24 - viena gara rinda",
                 "Der vienmēr, jebkuram skaitlim."),
                ("2 · 12 un 3 · 8",
                 "24 sadalās gan uz pusēm, gan trīs daļās."),
                ("4 · 6",
                 "Vēl viens veids."),
                ("Pa 5 rindām nesadalās",
                 "24 : 5 nav vesels skaitlis."),
            ],
            atbilde="1 · 24, 2 · 12, 3 · 8 un 4 · 6"),

    Ievadi("Cik rindu un cik kolonnu?", [
        {"jaut": "24 rūtiņas, 6 kolonnas. Cik rindu?", "atb": ["4"],
         "padoms": "24 : 6."},
        {"jaut": "24 rūtiņas, 3 rindas. Cik kolonnu?", "atb": ["8"],
         "padoms": "24 : 3."},
        {"jaut": "36 rūtiņas, 4 rindas. Cik kolonnu?", "atb": ["9"],
         "padoms": "36 : 4."},
        {"jaut": "36 rūtiņas, 6 kolonnas. Cik rindu?", "atb": ["6"],
         "padoms": "36 : 6."},
        {"jaut": "Cik rūtiņu ir tāfelītē 5 · 7?", "atb": ["35"],
         "padoms": "5 · 7."},
        {"jaut": "12 rūtiņas. Cik dažādos taisnstūros tās var salikt? "
                 "(1 · 12 un 12 · 1 skaitās viens)",
         "atb": ["3"], "padoms": "1 · 12, 2 · 6, 3 · 4."},
        {"jaut": "16 rūtiņas. Cik dažādos taisnstūros?", "atb": ["3"],
         "padoms": "1 · 16, 2 · 8, 4 · 4."},
        {"jaut": "7 rūtiņas. Cik dažādos taisnstūros?", "atb": ["1"],
         "padoms": "Tikai 1 · 7 - citādi nesadalās."},
    ], pamats=4,
        ievads="Rindas reiz kolonnas dod rūtiņu skaitu."),

    Varianti("Kurš sadalījums ir iespējams?", [
        {"jaut": "Vai 24 rūtiņas var salikt 5 vienādās rindās?",
         "opcijas": ["Nē, 24 nedalās ar 5", "Jā, pa 5 rūtiņām",
                     "Jā, pa 4 rūtiņām", "Jā, ja vienu rūtiņu izmet"],
         "pareizi": 0,
         "padoms": "24 : 5 nav vesels skaitlis."},
        {"jaut": "Ko nozīmē, ka tāfelīti var salikt tikai vienā rindā?",
         "opcijas": ["Skaitlis dalās tikai ar 1 un sevi",
                     "Skaitlis ir pāra",
                     "Tāfelīte ir maza",
                     "Skaitlis ir apaļš"],
         "pareizi": 0,
         "padoms": "Padomā par 7 rūtiņām."},
        {"jaut": "Tāfelīte 4 · 6. Cik rūtiņu tajā ir?",
         "opcijas": ["24", "10", "46", "12"],
         "pareizi": 0,
         "padoms": "Rindas reiz kolonnas."},
        {"jaut": "Kurš skaitlis dod visvairāk dažādu taisnstūru?",
         "opcijas": ["24", "23", "25", "Visiem vienādi"],
         "pareizi": 0,
         "padoms": "23 ir pirmskaitlis; 25 sadalās maz."},
    ], pamats=4),

    Pasaule("Kā izlikt flīzes?",
            Ievadi("", [
                {"jaut": "48 flīzes, 6 rindas. Cik flīžu rindā?",
                 "atb": ["8"], "padoms": "48 : 6."},
                {"jaut": "48 flīzes, 8 kolonnas. Cik rindu?",
                 "atb": ["6"], "padoms": "48 : 8."},
                {"jaut": "Grīda 5 flīzes plata un 9 garumā. Cik flīžu vajag?",
                 "atb": ["45"], "padoms": "5 · 9."},
                {"jaut": "Ir 30 flīzes. Vai tās var izlikt 4 vienādās rindās? "
                         "Raksti, cik paliktu pāri.",
                 "atb": ["2"], "padoms": "30 : 4 = 7, atlikums 2."},
            ]),
            pavediens="maja",
            konteksts="Flīzes, dēļus un dobes liek taisnstūros, tāpēc "
                      "vienmēr jāzina, kā skaitlis sadalās.",
            kapec="Ja skaitlis nedalās, rindā paliek tukša vieta."),

    Kopsavilkums([
        "Sadalu objektu vienādās daļās un pierakstu to ar reizinājumu.",
        "Atrodu visus veidus, kā skaitli salikt taisnstūrī.",
        "Pamanu, kad sadalījums nav iespējams.",
        "Zinu, ka rindas reiz kolonnas vienmēr dod to pašu skaitli.",
    ]),

    Majas([
        "Uzzīmē visus taisnstūrus, kādos var salikt 18 rūtiņas.",
        "Atrodi skaitli līdz 30, kuram ir visvairāk dažādu taisnstūru.",
        "Atrodi trīs skaitļus, kuriem ir tikai viens taisnstūris.",
    ]),
]
