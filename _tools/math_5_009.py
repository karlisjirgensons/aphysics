# -*- coding: utf-8 -*-
"""5. klase, 9. stunda: «Kad ciparus saskaita un kad atņem?»

Turpina 8. stundu. Atņemšanas likums ir vienīgā vieta romiešu pierakstā, kur
zīmes secība maina rezultātu, tāpēc to māca atsevišķi un uzreiz liek pašam
pārbaudīt savu pierakstu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, kolonnas)

TEMA = "Kad ciparus saskaita un kad atņem?"

MERKIS = ("Iemācīsimies romiešu pieraksta atņemšanas likumu un pārbaudīsim, "
          "vai pieraksts ir pareizs.")

SATURS = [
    Sakums("Kāpēc IX, nevis VIIII?",
           zimejums=kolonnas([("VIIII", 5), ("IX", 2), ("XXXX", 4),
                              ("XL", 2)]),
           paraksts="Zīmju skaits. Atņemšanas likums saīsina pierakstu uz "
                    "pusi un vairāk.",
           fakti=["Ja mazāka zīme stāv pirms lielākas, to atņem."]),

    Doma("Mazāka zīme priekšā nozīmē atņemšanu",
         "Ja zīme ir mazāka par nākamo, to atņem; citādi to pieskaita.",
         soli=[
             "Skaties uz katru zīmi un tās kaimiņu pa labi.",
             "Ja zīme ir mazāka par kaimiņu - atņem to.",
             "Citādi - pieskaiti.",
             "Atņem tikai I, X un C; atņem tikai no divām nākamajām zīmēm.",
         ],
         pieze="Der IV, IX, XL, XC, CD un CM. Neder IL vai IC - no I drīkst "
               "atņemt tikai V un X."),

    Paraugs("Ko nozīmē XCIV?",
            uzd="Izlasi romiešu skaitli XCIV.",
            soli=[
                ("XC: X ir mazāks par C, tātad 100 − 10 = 90",
                 "Pirmais pāris ir atņemšana."),
                ("IV: I ir mazāks par V, tātad 5 − 1 = 4",
                 "Otrais pāris arī ir atņemšana."),
                ("90 + 4 = 94",
                 "Abus gabalus saskaita."),
            ],
            atbilde="XCIV ir 94"),

    Ievadi("Izlasi skaitli", [
        {"jaut": "IV", "atb": ["4"], "padoms": "5 − 1."},
        {"jaut": "IX", "atb": ["9"], "padoms": "10 − 1."},
        {"jaut": "XIV", "atb": ["14"], "padoms": "10 + (5 − 1)."},
        {"jaut": "XL", "atb": ["40"], "padoms": "50 − 10."},
        {"jaut": "XLIX", "atb": ["49"], "padoms": "(50 − 10) + (10 − 1)."},
        {"jaut": "CMXC", "atb": ["990"],
         "padoms": "(1000 − 100) + (100 − 10)."},
    ], pamats=4,
        ievads="Uzmanies: dažviet zīmes atņem, dažviet saskaita."),

    Ievadi("Uzraksti ar romiešu cipariem", [
        {"jaut": "9", "atb": ["ix"], "padoms": "10 − 1.", "tastatura": "text",
         "vieta": "IX"},
        {"jaut": "40", "atb": ["xl"], "padoms": "50 − 10.",
         "tastatura": "text"},
        {"jaut": "19", "atb": ["xix"], "padoms": "10 + (10 − 1).",
         "tastatura": "text"},
        {"jaut": "400", "atb": ["cd"], "padoms": "500 − 100.",
         "tastatura": "text"},
    ]),

    Varianti("Vai pieraksts ir pareizs?", [
        {"jaut": "Kurš pieraksts skaitlim 99 ir pareizs?",
         "opcijas": ["XCIX", "IC", "LXXXXVIIII", "XCVIIII"],
         "pareizi": 0,
         "padoms": "No I drīkst atņemt tikai V un X."},
        {"jaut": "Ko nozīmē VI?",
         "opcijas": ["6", "4", "5", "11"],
         "pareizi": 0,
         "padoms": "I stāv aiz V, tāpēc to pieskaita."},
        {"jaut": "Kurš skaitlis ir MCMXCI?",
         "opcijas": ["1991", "1891", "2091", "1911"],
         "pareizi": 0,
         "padoms": "M + CM + XC + I."},
        {"jaut": "Kāpēc VX nav pareizs pieraksts?",
         "opcijas": ["No V neko neatņem", "V ir par lielu",
                     "Trūkst I", "Jāraksta XV vietā"],
         "pareizi": 0,
         "padoms": "Atņem tikai I, X un C."},
    ], pamats=4),

    Pasaule("Ko raksta uz pulksteņa?",
            Ievadi("", [
                {"jaut": "Uz pulksteņa cipars IX - kura tā stunda?",
                 "atb": ["9"], "padoms": "10 − 1."},
                {"jaut": "Cik zīmju vajag skaitlim 40 ar atņemšanas likumu?",
                 "atb": ["2"], "padoms": "XL."},
                {"jaut": "Cik zīmju vajadzētu skaitlim 40 bez tā likuma?",
                 "atb": ["4"], "padoms": "XXXX."},
                {"jaut": "Uz pieminekļa MCMXVIII. Kurš gads?",
                 "atb": ["1918"], "padoms": "1000 + 900 + 10 + 8."},
            ]),
            pavediens="dati",
            konteksts="Pulksteņu ciparnīcās un uz pieminekļiem šis likums "
                      "sastopams gandrīz vienmēr.",
            kapec="Īsāks pieraksts nozīmē mazāk vietas un mazāk kļūdu."),

    Kopsavilkums([
        "Zinu, ka mazāka zīme pirms lielākas nozīmē atņemšanu.",
        "Izlasu un uzrakstu skaitļus ar IV, IX, XL, XC, CD un CM.",
        "Pārbaudu savu pierakstu: vai atņemta tikai I, X vai C.",
    ]),

    Majas([
        "Uzraksti ar romiešu cipariem šo gadu un savu dzimšanas gadu.",
        "Pārbaudi uz kāda pulksteņa, kā tur uzrakstīts četri.",
        "Padomā, kurš pieraksts ir īsāks: 1999 mūsu vai romiešu cipariem.",
    ]),
]
