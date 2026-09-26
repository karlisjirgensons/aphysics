# -*- coding: utf-8 -*-
"""3. klase, 122. stunda: «Kurā traukā ietilpst vairāk?»

Tilpumu var salīdzināt arī tad, kad kubus izmantot nevar: ar pārliešanu vai
ar beramu produktu. Tas ir pirmais mērījums, kurā mērs nav lineāls, bet
cits trauks - un tieši no tā aug mērtrauka ideja.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         kolonnas)

TEMA = "Kurā traukā ietilpst vairāk?"

MERKIS = ("Salīdzināsim trauku tilpumus, izmantojot beramus produktus vai "
          "ūdeni.")

SATURS = [
    Sakums("Kurā pudelē ir vairāk - garajā vai platajā?",
           zimejums=kolonnas([("garā", 5), ("platā", 7)], " glāzes"),
           paraksts="Augstums nepasaka tilpumu - platā pudele tur vairāk.",
           fakti=["Augstāks trauks ne vienmēr ir lielāks.",
                  "Tilpumu salīdzina, pārlejot vienā un tajā pašā mērā."]),

    Doma("Mēri abus ar vienu un to pašu mēru",
         "Ja abus traukus piepilda ar vienādām glāzēm, tilpumu var salīdzināt "
         "pēc glāžu skaita.",
         soli=[
             "Izvēlies vienu mēru - glāzi vai karoti.",
             "Piepildi pirmo trauku, skaitot mērus.",
             "To pašu izdari ar otro.",
             "Salīdzini mēru skaitu.",
         ],
         pieze="Mēram jābūt vienam un tam pašam. Ja vienu mēra ar glāzi, "
               "otru ar krūzi, skaitļus salīdzināt nedrīkst."),

    Petijums("Salīdzini divus traukus",
             vajag="divi dažādas formas trauki, glāze un ūdens vai rīsi",
             soli=[
                 "Piepildi pirmo trauku, skaitot glāzes.",
                 "Pieraksti glāžu skaitu.",
                 "To pašu izdari ar otro trauku.",
                 "Salīdzini skaitļus un pasaki, kurā ietilpst vairāk.",
             ],
             secinajums="Tilpumu nosaka mēru skaits, nevis trauka augstums "
                        "vai forma."),

    Paraugs("Kurā traukā ir vairāk?",
            uzd="Pirmajā traukā ietilpa 5 glāzes, otrajā 7. Kurā ir vairāk?",
            soli=[
                ("Abus mērīja ar vienu glāzi",
                 "Mērs ir viens un tas pats."),
                ("5 < 7",
                 "Salīdzina glāžu skaitu."),
                ("Otrajā ir vairāk",
                 "Par divām glāzēm."),
            ],
            atbilde="otrajā, par 2 glāzēm vairāk"),

    Ievadi("Salīdzini tilpumus", [
        {"jaut": "Pirmajā 5 glāzes, otrajā 7. Par cik vairāk ir otrajā?",
         "atb": ["2"], "padoms": "7 − 5."},
        {"jaut": "Traukā ietilpst 8 glāzes. Cik glāžu ietilpst divos tādos?",
         "atb": ["16"], "padoms": "2 · 8."},
        {"jaut": "Traukā ietilpst 12 glāzes. Cik glāžu ir puse trauka?",
         "atb": ["6"], "padoms": "12 : 2."},
        {"jaut": "Lielajā traukā ietilpst 3 mazie. Cik mazo ietilpst divos "
                 "lielajos?",
         "atb": ["6"], "padoms": "2 · 3."},
        {"jaut": "Traukā 20 glāzes, izlēja 8. Cik palika?", "atb": ["12"],
         "padoms": "20 − 8."},
        {"jaut": "Cik glāžu ir {1|4} no 20 glāžu trauka?", "atb": ["5"],
         "padoms": "20 : 4."},
    ], pamats=4),

    Zimejums("Trīs trauki, viens mērs",
             kolonnas([("A", 4), ("B", 6), ("C", 9)], " glāzes"),
             paskaidro="Visus trīs mērīja ar vienu glāzi, tāpēc skaitļus var "
                       "salīdzināt.",
             ievads="Tā izskatās mērījumu rezultāts."),

    Varianti("Kā salīdzināt traukus?", [
        {"jaut": "Vai augstāks trauks vienmēr tur vairāk?",
         "opcijas": ["Nē", "Jā", "Tikai ja tas ir plats", "Vienmēr"],
         "pareizi": 0, "padoms": "Svarīgs ir arī platums."},
        {"jaut": "Ko vajag, lai salīdzinātu divus traukus?",
         "opcijas": ["Vienu un to pašu mēru", "Lineālu",
                     "Svarus", "Divus dažādus mērus"],
         "pareizi": 0, "padoms": "Skaitļus var salīdzināt tikai vienā mērā."},
        {"jaut": "Traukā ietilpst 6 glāzes. Cik glāžu ir trijos tādos?",
         "opcijas": ["18", "9", "12", "6"],
         "pareizi": 0, "padoms": "3 · 6."},
        {"jaut": "Kas nemainās, pārlejot ūdeni citā traukā?",
         "opcijas": ["Ūdens daudzums", "Ūdens forma",
                     "Ūdens augstums", "Nekas"],
         "pareizi": 0, "padoms": "Mainās tikai forma."},
    ], pamats=4),

    Pasaule("Cik ūdens ir ezerā?",
            Ievadi("", [
                {"jaut": "Spainī ietilpst 10 litru. Cik litru ir 6 spaiņos?",
                 "atb": ["60"], "padoms": "6 · 10."},
                {"jaut": "Mucā ietilpst 200 litru. Cik spaiņu pa 10 l tas "
                         "ir?",
                 "atb": ["20"], "padoms": "200 : 10."},
                {"jaut": "Cik litru ir {1|4} no mucas?", "atb": ["50"],
                 "padoms": "200 : 4."},
                {"jaut": "Cik spaiņu tas ir?", "atb": ["5"],
                 "padoms": "50 : 10."},
            ]),
            pavediens="planeta",
            konteksts="Ūdens krājumus mēra litros un kubikmetros - vienmēr "
                      "ar vienu un to pašu mēru.",
            kapec="Tikai tad var salīdzināt, cik ūdens ir dažādās vietās."),

    Kopsavilkums([
        "Salīdzinu trauku tilpumus ar vienu mēru.",
        "Zinu, ka augstums vien tilpumu nenosaka.",
        "Pierakstu mērījumu rezultātus un salīdzinu skaitļus.",
        "Zinu, ka pārlejot ūdens daudzums nemainās.",
    ]),

    Majas([
        "Salīdzini divu mājas trauku tilpumus ar vienu glāzi.",
        "Pieraksti abus skaitļus.",
        "Atrodi trauku, kurā ietilpst tieši 5 glāzes.",
    ]),
]
