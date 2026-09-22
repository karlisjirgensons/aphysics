# -*- coding: utf-8 -*-
"""5. klase, 65. stunda: «Kas ir kopsaucējs?»

Kopīgais saucējs skolēnam jau ir pazīstams - to lietoja, salīdzinot un
kārtojot. Te tam tiek dots vārds un viens jauns uzdevums: izvēlēties. Der
jebkurš kopīgais dalāmais, bet saucēju reizinājums reizēm ir divreiz par
lielu, tāpēc stunda māca izvēli pamatot, nevis tikai atrast.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kas ir kopsaucējs?"

MERKIS = ("Iemācīsimies noteikt divu daļu kopsaucēju un pamatot, kāpēc "
          "izvēlēts tieši tas.")

SATURS = [
    Sakums("Divi saucēji, viens rēķins",
           zimejums=restis([["1/4", "1/6", "?"],
                            ["3/12", "2/12", "12"]],
                           virsraksts="Apakšā abas daļas runā vienā valodā"),
           paraksts="Kopsaucējs 12 der abām daļām: 12 dalās ar 4 un ar 6.",
           fakti=["Saskaitīt var tikai vienādus gabalus.",
                  "Ceturtdaļu un sestdaļu saskaitīt nevar.",
                  "Tāpēc abām vispirms atrod vienu saucēju."]),

    Doma("Kopsaucējs dalās ar abiem saucējiem",
         "Kopsaucējs ir skaitlis, kas dalās ar abu daļu saucējiem; ērtākais "
         "ir mazākais tāds skaitlis.",
         soli=[
             "Izraksti abus saucējus.",
             "Pārbaudi, vai lielākais dalās ar mazāko - tad tas arī der.",
             "Ja nedalās, meklē mazāko kopīgo dalāmo.",
             "Galējā gadījumā der abu saucēju reizinājums.",
             "Pieraksti, kāpēc izvēlējies tieši šo skaitli.",
         ],
         pieze="Daļām {1|4} un {1|6} reizinājums dod 24, bet mazākais "
               "kopīgais dalāmais ir 12 - divreiz mazāki skaitļi un tikpat "
               "pareiza atbilde."),

    Paraugs("Kāds kopsaucējs daļām {1|4} un {1|6}?",
            uzd="Nosaki daļu {1|4} un {1|6} kopsaucēju un pamato izvēli.",
            soli=[
                ("Saucēji ir 4 un 6",
                 "6 ar 4 nedalās - lielākais neder."),
                ("4 = 2 · 2 un 6 = 2 · 3",
                 "Sadala pirmreizinātājos."),
                ("Mazākais kopīgais dalāmais ir 12",
                 "2 · 2 · 3."),
                ("{1|4} = {3|12} un {1|6} = {2|12}",
                 "Abas daļas ar vienu saucēju."),
            ],
            atbilde="Kopsaucējs ir 12"),

    Ievadi("Atrodi kopsaucēju", [
        {"jaut": "Kāds ir mazākais kopsaucējs daļām {1|2} un {1|3}?",
         "atb": ["6"], "padoms": "6 dalās ar 2 un 3."},
        {"jaut": "Kāds ir mazākais kopsaucējs daļām {1|3} un {1|6}?",
         "atb": ["6"], "padoms": "6 jau dalās ar 3."},
        {"jaut": "Kāds ir mazākais kopsaucējs daļām {2|5} un {1|2}?",
         "atb": ["10"], "padoms": "5 · 2."},
        {"jaut": "Kāds ir mazākais kopsaucējs daļām {3|4} un {5|6}?",
         "atb": ["12"], "padoms": "12 dalās ar 4 un 6."},
        {"jaut": "Kāds ir mazākais kopsaucējs daļām {1|8} un {3|4}?",
         "atb": ["8"], "padoms": "8 jau dalās ar 4."},
        {"jaut": "Kāds ir mazākais kopsaucējs daļām {2|9} un {1|6}?",
         "atb": ["18"], "padoms": "18 dalās ar 9 un 6."},
        {"jaut": "Kāds ir mazākais kopsaucējs daļām {1|7} un {1|3}?",
         "atb": ["21"], "padoms": "7 · 3."},
        {"jaut": "Kāds ir mazākais kopsaucējs daļām {5|12} un {1|8}?",
         "atb": ["24"], "padoms": "24 dalās ar 12 un 8."},
    ], pamats=4,
        ievads="Vispirms pārbaudi, vai lielākais saucējs jau neder."),

    Zimejums("Viens saucējs abām daļām",
             restis([["1/4", "1/6"],
                     ["3/12", "2/12"]],
                    virsraksts="Augšā dotās, apakšā - ar kopsaucēju"),
             paskaidro="Gabali abās daļās tagad ir vienādi: divpadsmitdaļas. "
                       "Tikai tādus gabalus drīkst likt kopā.",
             ievads="Kopsaucējs nemaina daļas, tikai to pierakstu."),

    Varianti("Kurš skaitlis der par kopsaucēju?", [
        {"jaut": "Kāds skaitlis var būt kopsaucējs?",
         "opcijas": ["Tāds, kas dalās ar abiem saucējiem",
                     "Tāds, kas dalās ar abiem skaitītājiem",
                     "Abu saucēju summa",
                     "Lielākais no skaitītājiem"],
         "pareizi": 0,
         "padoms": "Abām daļām jāietilpst vienā iedaļā."},
        {"jaut": "Daļām {1|3} un {1|9} der kopsaucējs 9. Kāpēc?",
         "opcijas": ["9 dalās ar 3", "9 ir lielāks", "9 ir nepāra",
                     "3 · 9 = 27"],
         "pareizi": 0,
         "padoms": "Lielākais saucējs reizēm jau ir kopsaucējs."},
        {"jaut": "Vai daļām {1|4} un {1|6} der kopsaucējs 24?",
         "opcijas": ["Der, bet 12 ir ērtāk", "Neder",
                     "Der, un mazāk nevar", "Der tikai pirmajai"],
         "pareizi": 0,
         "padoms": "Jebkurš kopīgais dalāmais der."},
        {"jaut": "Kad kopsaucējs ir saucēju reizinājums?",
         "opcijas": ["Kad saucējiem nav kopīga dalītāja",
                     "Vienmēr",
                     "Kad abi ir pāra skaitļi",
                     "Nekad"],
         "pareizi": 0,
         "padoms": "{1|7} un {1|3}."},
        {"jaut": "Kāpēc mazāks kopsaucējs ir ērtāks?",
         "opcijas": ["Skaitļi ir mazāki un mazāk jāsaīsina",
                     "Atbilde iznāk citāda",
                     "Tas ir vienīgais pareizais",
                     "Tas nav ērtāks"],
         "pareizi": 0,
         "padoms": "Mazāki skaitļi - mazāk kļūdu."},
        {"jaut": "Kas notiek ar daļas vērtību, pārrakstot to ar kopsaucēju?",
         "opcijas": ["Nekas", "Tā kļūst lielāka", "Tā kļūst mazāka",
                     "Tā kļūst vesela"],
         "pareizi": 0,
         "padoms": "Tā ir paplašināšana."},
    ], pamats=4),

    Pasaule("Divas klases, viena tabula",
            Ievadi("", [
                {"jaut": "Vienā klasē {1|4} skolēnu brauc ar autobusu, otrā "
                         "{1|6}. Kāds ir mazākais kopsaucējs?",
                 "atb": ["12"], "padoms": "12 dalās ar 4 un 6."},
                {"jaut": "Cik divpadsmitdaļu ir pirmās klases daļa?",
                 "atb": ["3"], "padoms": "{1|4} = {3|12}."},
                {"jaut": "Cik divpadsmitdaļu ir otrās klases daļa?",
                 "atb": ["2"], "padoms": "{1|6} = {2|12}."},
                {"jaut": "Trešajā klasē ar autobusu brauc {1|3}. Cik "
                         "divpadsmitdaļu tas ir?",
                 "atb": ["4"], "padoms": "{1|3} = {4|12}."},
            ]),
            pavediens="skola",
            konteksts="Klases ir dažāda lieluma, tāpēc daļas ar dažādiem "
                      "saucējiem nevienā tabulā nesalīdzinās.",
            kapec="Kopsaucējs ir tabulas kopīgā valoda."),

    Kopsavilkums([
        "Zinu, ka kopsaucējs dalās ar abu daļu saucējiem.",
        "Atrodu divu daļu mazāko kopsaucēju.",
        "Pamatoju, kāpēc izvēlējos tieši šo skaitli.",
        "Pārrakstu abas daļas ar kopsaucēju.",
    ]),

    Majas([
        "Atrodi kopsaucēju daļām {2|3} un {3|8} un pieraksti abas ar to.",
        "Uzraksti divas daļas, kurām kopsaucējs ir lielākais no saucējiem.",
        "Uzraksti divas daļas, kurām kopsaucējs ir saucēju reizinājums.",
    ]),
]
