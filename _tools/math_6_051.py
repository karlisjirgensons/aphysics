# -*- coding: utf-8 -*-
"""6. klase, 51. stunda: «Kā dalīt ar decimāldaļu?»

Galvenā dalīšanas stunda. Viss paņēmiens ir viens solis: dalītāju padarīt
par veselu skaitli. Pamatojums nāk no daļas pamatīpašības, kas skolēniem jau
ir pazīstama no parastajām daļām, tāpēc te nav jauna likuma - ir jauns
pielietojums.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā dalīt ar decimāldaļu?"

MERKIS = ("Iemācīsimies dalīt ar decimāldaļu, palielinot dalāmo un dalītāju "
          "vienādu skaitu reižu, un pamatot to ar daļas pamatīpašību.")

SATURS = [
    Sakums("Dalītājam jākļūst veselam",
           fakti=["7,2 : 0,8 = 72 : 8 - abus palielina 10 reižu.",
                  "Dalījums nemainās, jo tā ir daļas pamatīpašība.",
                  "Ar veselu dalītāju dalīšana ir jau zināma."]),

    Doma("Pārceļ komatu abos skaitļos vienādi",
         "Dalot ar decimāldaļu, dalāmo un dalītāju reizina ar 10, 100 vai "
         "1000 tā, lai dalītājs kļūtu par veselu skaitli.",
         soli=[
             "Saskaiti ciparus aiz komata dalītājā.",
             "Pārcel komatu pa labi par tik vietām *abos* skaitļos.",
             "Ja dalāmajā ciparu nepietiek, beigās pieraksti nulles.",
             "Dali ar veselu skaitli, kā iemācījies iepriekš.",
             "Pārbaudi ar reizināšanu.",
         ],
         pieze="Pamatojums: {7,2|0,8} = {7,2 · 10|0,8 · 10} = {72|8}. Abus "
               "daļas locekļus reizinot ar vienu skaitli, vērtība nemainās - "
               "tieši to darījām ar parastajām daļām."),

    Paraugs("Padari dalītāju par veselu",
            uzd="Cik ir 4,5 : 0,15?",
            soli=[
                ("0,15 - divi cipari aiz komata",
                 "Abus skaitļus reizina ar 100."),
                ("4,5 · 100 = 450; 0,15 · 100 = 15",
                 "Dalāmajam pieraksta nulli."),
                ("450 : 15 = 30",
                 "Tagad dalīšana ir ar veselu skaitli."),
                ("Pārbaude: 30 · 0,15 = 4,5",
                 "Atgriežas dalāmais."),
            ],
            atbilde="30"),

    Ievadi("Dali ar decimāldaļu", [
        {"jaut": "Cik ir 7,2 : 0,8?",
         "atb": ["9"], "padoms": "72 : 8."},
        {"jaut": "Cik ir 3,6 : 0,4?",
         "atb": ["9"], "padoms": "36 : 4."},
        {"jaut": "Cik ir 1,2 : 0,03?",
         "atb": ["40"], "padoms": "120 : 3."},
        {"jaut": "Cik ir 6 : 0,25?",
         "atb": ["24"], "padoms": "600 : 25."},
        {"jaut": "Cik ir 0,9 : 0,15?",
         "atb": ["6"], "padoms": "90 : 15."},
        {"jaut": "Cik ir 2,55 : 0,5?",
         "atb": ["5,1", "5.1"], "padoms": "25,5 : 5."},
    ], pamats=4,
        ievads="Vispirms dalītājs kļūst vesels - abiem skaitļiem vienādi."),

    Pasaule("Cik pilnas kārbas sanāks?",
            Kustiba("", [
                {"jaut": "Ir 4,8 kg produkta, vienā kārbā 0,4 kg. Cik "
                         "kārbu?",
                 "atb": 12, "beigas": 40, "iedala": 10, "mers": "kārbas",
                 "merkis": "kārbu skaits", "objekts": "Iepakotājs",
                 "padoms": "48 : 4."},
                {"jaut": "Ir 7,5 l, vienā pudelē 0,25 l. Cik pudeļu?",
                 "atb": 30, "beigas": 40, "iedala": 10, "mers": "pudeles",
                 "merkis": "pudeļu skaits", "objekts": "Iepakotājs",
                 "padoms": "750 : 25."},
                {"jaut": "Ir 2,4 kg, vienā maisiņā 0,15 kg. Cik maisiņu?",
                 "atb": 16, "beigas": 40, "iedala": 10, "mers": "maisiņi",
                 "merkis": "maisiņu skaits", "objekts": "Iepakotājs",
                 "padoms": "240 : 15."},
                {"jaut": "Ir 9 m auduma, vienam gabalam 0,45 m. Cik gabalu?",
                 "atb": 20, "beigas": 40, "iedala": 10, "mers": "gabali",
                 "merkis": "gabalu skaits", "objekts": "Iepakotājs",
                 "padoms": "900 : 45."},
            ]),
            pavediens="virtuve",
            konteksts="Fasēšanas līnija apstājas tieši tad, kad produkts "
                      "beidzas - kārbu skaitu var aprēķināt iepriekš.",
            kapec="Dalīšana ar decimāldaļu atbild uz «cik reižu pietiks»."),

    Varianti("Ko dara ar komatu?", [
        {"jaut": "Dalot ar 0,04, abus skaitļus reizina ar...",
         "opcijas": ["100", "10", "1000", "4"],
         "pareizi": 0,
         "padoms": "Divi cipari aiz komata."},
        {"jaut": "Kāpēc dalījums nemainās?",
         "opcijas": ["Jo abus locekļus reizina ar vienu skaitli",
                     "Jo dalītājs kļūst vesels",
                     "Jo komats pazūd", "Tas mainās"],
         "pareizi": 0,
         "padoms": "Daļas pamatīpašība."},
        {"jaut": "Skolēns rēķina 6 : 0,2, pārceļot komatu tikai dalītājā. "
                 "Kas notiks?",
         "opcijas": ["Atbilde būs 10 reižu par mazu",
                     "Atbilde būs pareiza",
                     "Atbilde būs 10 reižu par lielu",
                     "Dalīt nevarēs"],
         "pareizi": 0,
         "padoms": "Jāpārceļ abos skaitļos."},
        {"jaut": "6 : 0,2 ir vienāds ar...",
         "opcijas": ["30", "3", "12", "0,3"],
         "pareizi": 0,
         "padoms": "60 : 2."},
    ], pamats=4),

    Kopsavilkums([
        "Dalu ar decimāldaļu, padarot dalītāju par veselu skaitli.",
        "Pārceļu komatu vienādi abos skaitļos.",
        "Pamatoju paņēmienu ar daļas pamatīpašību.",
        "Pārbaudu rezultātu ar reizināšanu.",
    ]),

    Majas([
        "Izrēķini 8,4 : 0,6 un 1,44 : 0,12 ar pārbaudi.",
        "Atrodi dalījumu, kurā dalāmajam jāpieraksta nulles.",
        "Paskaidro, kāpēc 5 : 0,5 ir 10, nevis 2,5.",
    ]),
]
