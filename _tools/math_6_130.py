# -*- coding: utf-8 -*-
"""6. klase, 130. stunda: «Vai no mazāka var atņemt lielāku?»

Jauns mikrotemats. Līdz šim atbilde bija «nē» - tagad tā kļūst par «jā», un
rezultāts ir negatīvs. Modelis ir tas pats: soļi pa skaitļu taisni, tikai
tagad tie aiziet pāri nullei.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Vai no mazāka var atņemt lielāku?"

MERKIS = ("Modelēsim uz skaitļu taisnes atņemšanu, kur mazinātājs ir lielāks "
          "nekā mazināmais.")

SATURS = [
    Sakums("Tagad atbilde ir «jā»",
           zimejums=taisne(-6, 6, 2, [(3, "sākums"), (-2, "rezultāts")],
                           bultas=[(3, -2, "−5")]),
           paraksts="No 3 atņem 5: pieci soļi pa kreisi noved pie −2.",
           fakti=["Atņemšana ir soļi pa kreisi.",
                  "Ja soļu ir vairāk nekā līdz nullei, rezultāts ir "
                  "negatīvs.",
                  "Sākumskolā tādu uzdevumu vienkārši nebija."]),

    Doma("Ej pa kreisi, arī pāri nullei",
         "Atņemot lielāku skaitli no mazāka, soļi pa kreisi aiziet pāri "
         "nullei, un rezultāts ir negatīvs.",
         soli=[
             "Atzīmē mazināmo uz skaitļu taisnes.",
             "Ej pa kreisi tik soļu, cik pasaka mazinātājs.",
             "Ja nonāc pāri nullei, turpini skaitīt negatīvos skaitļus.",
             "Nolasi rezultātu.",
             "Pārbaudi: rezultāts plus mazinātājs dod mazināmo.",
         ],
         pieze="Rezultāta modulis ir starpība starp abiem moduļiem: "
               "3 − 5 = −2, jo 5 − 3 = 2 un zīme ir mīnuss. Tāpēc atbildi "
               "var pateikt uzreiz."),

    Paraugs("No mazāka atņem lielāku",
            uzd="Cik ir 3 − 5?",
            soli=[
                ("Sākums: 3",
                 "Mazināmais."),
                ("Pieci soļi pa kreisi",
                 "3 → 2 → 1 → 0 → −1 → −2."),
                ("Rezultāts: −2",
                 "Trīs soļi līdz nullei un vēl divi."),
                ("Pārbaude: −2 + 5 = 3",
                 "Atgriežas mazināmais."),
            ],
            atbilde="−2"),

    Ievadi("Atņem lielāku no mazāka", [
        {"jaut": "Cik ir 3 − 5?",
         "atb": ["-2", "−2"], "padoms": "Divi soļi pāri nullei."},
        {"jaut": "Cik ir 4 − 9?",
         "atb": ["-5", "−5"], "padoms": "9 − 4, zīme mīnus."},
        {"jaut": "Cik ir 0 − 7?",
         "atb": ["-7", "−7"], "padoms": "Septiņi soļi no nulles."},
        {"jaut": "Cik ir 12 − 20?",
         "atb": ["-8", "−8"], "padoms": "20 − 12."},
        {"jaut": "Cik ir 6 − 6?",
         "atb": ["0"], "padoms": "Vienādi skaitļi."},
        {"jaut": "Cik ir 2 − 11?",
         "atb": ["-9", "−9"], "padoms": "11 − 2."},
    ], pamats=4),

    Pasaule("Cik dziļi nolaidīsies zonde?",
            Kustiba("", [
                {"jaut": "Zonde ir 3 m virs ūdens un nolaižas par 5 m. Kurā "
                         "atzīmē tā ir?",
                 "atb": -2, "sakums": -10, "beigas": 10, "iedala": 5,
                 "mers": "metri", "merkis": "jaunā vieta",
                 "objekts": "Zonde", "padoms": "3 − 5."},
                {"jaut": "No −2 m tā nolaižas vēl par 6 m. Kur tā ir?",
                 "atb": -8, "sakums": -10, "beigas": 10, "iedala": 5,
                 "mers": "metri", "merkis": "jaunā vieta",
                 "objekts": "Zonde", "padoms": "−2 − 6."},
                {"jaut": "No −8 m tā paceļas par 10 m. Kur tā ir?",
                 "atb": 2, "sakums": -10, "beigas": 10, "iedala": 5,
                 "mers": "metri", "merkis": "jaunā vieta",
                 "objekts": "Zonde", "padoms": "−8 + 10."},
                {"jaut": "No 2 m tā nolaižas par 9 m. Kur tā ir?",
                 "atb": -7, "sakums": -10, "beigas": 10, "iedala": 5,
                 "mers": "metri", "merkis": "jaunā vieta",
                 "objekts": "Zonde", "padoms": "2 − 9."},
            ]),
            pavediens="planeta",
            konteksts="Zonde var nolaisties dziļāk, nekā tā bija pacēlusies - "
                      "tad rezultāts ir zem nulles.",
            kapec="Atņemt lielāku no mazāka nozīmē pāriet uz otru pusi."),

    Varianti("Kāds būs rezultāts?", [
        {"jaut": "Ja mazinātājs ir lielāks par mazināmo, rezultāts ir...",
         "opcijas": ["negatīvs", "pozitīvs", "nulle", "nevar zināt"],
         "pareizi": 0,
         "padoms": "Soļi aiziet pāri nullei."},
        {"jaut": "Cik ir 5 − 8?",
         "opcijas": ["−3", "3", "13", "−13"],
         "pareizi": 0,
         "padoms": "8 − 5, zīme mīnus."},
        {"jaut": "Kāds ir 0 − 4?",
         "opcijas": ["−4", "4", "0", "−8"],
         "pareizi": 0,
         "padoms": "Četri soļi no nulles pa kreisi."},
        {"jaut": "Kā pārbaudīt, vai 3 − 5 = −2?",
         "opcijas": ["−2 + 5 = 3", "3 + 5", "−2 − 5", "5 − 3"],
         "pareizi": 0,
         "padoms": "Rezultāts plus mazinātājs."},
    ], pamats=4),

    Zimejums("Soļi pāri nullei",
             taisne(-8, 4, 2, [(2, "sākums"), (-6, "rezultāts")],
                    bultas=[(2, -6, "−8")]),
             paskaidro="2 − 8 = −6. Divi soļi līdz nullei un vēl seši pāri "
                       "tai.",
             ievads="Vēl viens piemērs ar garāku bultiņu."),

    Kopsavilkums([
        "Atņemu lielāku skaitli no mazāka.",
        "Modelēju to ar soļiem pa kreisi uz skaitļu taisnes.",
        "Zinu, ka rezultāts tad ir negatīvs.",
        "Pārbaudu rezultātu ar saskaitīšanu.",
    ]),

    Majas([
        "Izrēķini 4 − 11; 0 − 6 un 7 − 15.",
        "Uzzīmē skaitļu taisni vienam no tiem.",
        "Pieraksti, cik soļu bija līdz nullei un cik pāri tai.",
    ]),
]
