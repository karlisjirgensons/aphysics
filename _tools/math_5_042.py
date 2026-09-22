# -*- coding: utf-8 -*-
"""5. klase, 42. stunda: «Kā saīsināt vienādu reizinātāju reizinājumu?»

Pakāpe ienāk kā saīsinājums, ne kā jauna darbība: 2 · 2 · 2 · 2 · 2 ir gari
rakstāms, un tieši tāpēc kāds izdomāja rakstīt mazu ciparu augšā. Pirmajā
stundā vēl nav ne bāzes, ne kāpinātāja - tikai pieraksts un lasīšana.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, kolonnas)

TEMA = "Kā saīsināt vienādu reizinātāju reizinājumu?"

MERKIS = ("Iemācīsimies pierakstīt vienādu reizinātāju reizinājumu kā pakāpi "
          "un izlasīt to.")

SATURS = [
    Sakums("Cik reižu te uzrakstīts divnieks?",
           fakti=["2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 - desmit reižu.",
                  "To pašu raksta īsi: 2¹⁰.",
                  "Mazais cipars augšā pasaka, cik reižu reizina."]),

    Doma("Pakāpe ir saīsināts pieraksts",
         "Vienādu reizinātāju reizinājumu raksta kā pakāpi: reizinātājs "
         "lielajā ciparā, reizinātāju skaits - mazajā augšā.",
         soli=[
             "Pārbaudi, vai visi reizinātāji ir vienādi.",
             "Uzraksti reizinātāju lielajā ciparā.",
             "Saskaiti, cik reižu tas atkārtojas.",
             "Uzraksti šo skaitu mazajā ciparā augšā.",
             "Izlasi: «divi trešajā pakāpē».",
         ],
         pieze="Pakāpe nav jauna darbība - tas ir tas pats reizinājums, tikai "
               "īsāk uzrakstīts. 2³ nav 2 · 3, bet 2 · 2 · 2, tātad 8."),

    Zimejums("Cik ātri aug pakāpe",
             kolonnas([("2²", 4), ("2³", 8), ("2⁴", 16), ("2⁵", 32),
                       ("2⁶", 64)]),
             paskaidro="Katrs nākamais stabiņš ir divreiz augstāks nekā "
                       "iepriekšējais.",
             ievads="Pieraksts kļūst par vienu ciparu garāks, skaitlis - "
                    "divreiz lielāks."),

    Paraugs("No reizinājuma uz pakāpi",
            uzd="Uzraksti 3 · 3 · 3 · 3 kā pakāpi un izrēķini.",
            soli=[
                ("Visi reizinātāji ir 3",
                 "Pakāpi drīkst rakstīt tikai tad."),
                ("Trijnieks atkārtojas 4 reizes",
                 "Saskaitām reizinātājus."),
                ("3⁴",
                 "Lasa: «trīs ceturtajā pakāpē»."),
                ("3 · 3 = 9, 9 · 3 = 27, 27 · 3 = 81",
                 "Rēķina pa vienam reizinātājam."),
            ],
            atbilde="3 · 3 · 3 · 3 = 3⁴ = 81"),

    Ievadi("Izrēķini pakāpi", [
        {"jaut": "Cik ir 2³?", "atb": ["8"], "padoms": "2 · 2 · 2."},
        {"jaut": "Cik ir 3⁴?", "atb": ["81"], "padoms": "3 · 3 · 3 · 3."},
        {"jaut": "Cik ir 5²?", "atb": ["25"], "padoms": "5 · 5."},
        {"jaut": "Cik ir 10³?", "atb": ["1000"], "padoms": "10 · 10 · 10."},
        {"jaut": "Cik reižu 2 atkārtojas pierakstā 2⁵?", "atb": ["5"],
         "padoms": "Mazais cipars augšā."},
        {"jaut": "Cik ir 2⁵?", "atb": ["32"], "padoms": "2 · 2 · 2 · 2 · 2."},
        {"jaut": "Cik ir 4³?", "atb": ["64"], "padoms": "4 · 4 · 4."},
        {"jaut": "Cik ir 1⁷?", "atb": ["1"], "padoms": "Vieninieks jebkurā "
                                                       "pakāpē."},
    ], pamats=4,
        ievads="Pakāpe ir reizinājums - rēķini pa vienam reizinātājam."),

    Varianti("Vai pieraksts ir pareizs?", [
        {"jaut": "Ko nozīmē 2³?",
         "opcijas": ["2 · 2 · 2", "2 · 3", "3 · 3", "2 + 2 + 2"],
         "pareizi": 0,
         "padoms": "Mazais cipars rāda reizinātāju skaitu."},
        {"jaut": "Kuru reizinājumu var uzrakstīt kā pakāpi?",
         "opcijas": ["5 · 5 · 5", "5 · 4 · 3", "5 + 5 + 5", "5 · 4"],
         "pareizi": 0,
         "padoms": "Visiem reizinātājiem jābūt vienādiem."},
        {"jaut": "Kurš apgalvojums ir pareizs?",
         "opcijas": ["2³ = 8", "2³ = 6", "2³ = 9", "2³ = 5"],
         "pareizi": 0,
         "padoms": "2 · 2 · 2."},
        {"jaut": "Kāpēc pakāpi vispār izdomāja?",
         "opcijas": ["Lai garu reizinājumu uzrakstītu īsi",
                     "Lai rēķināt būtu grūtāk",
                     "Lai aizstātu saskaitīšanu",
                     "Lai skaitļi kļūtu mazāki"],
         "pareizi": 0,
         "padoms": "Salīdzini 2¹⁰ ar desmit divniekiem."},
    ], pamats=4),

    Pasaule("Cik vietas aizņem fails?",
            Ievadi("", [
                {"jaut": "Datorā atmiņu skaita ar divnieka pakāpēm. Cik ir "
                         "2⁴?",
                 "atb": ["16"], "padoms": "2 · 2 · 2 · 2."},
                {"jaut": "Cik ir 2⁸?", "atb": ["256"],
                 "padoms": "2⁴ · 2⁴ = 16 · 16."},
                {"jaut": "Cik ir 2¹⁰?", "atb": ["1024"],
                 "padoms": "256 · 4."},
                {"jaut": "Cik baitu ir vienā kilobaitā? (tas ir 2¹⁰)",
                 "atb": ["1024"], "padoms": "Tāpēc kilobaits nav tieši "
                                            "1 000."},
            ]),
            pavediens="dati",
            konteksts="Datora atmiņu mēra divnieka pakāpēs, tāpēc "
                      "kilobaits ir 1 024, nevis 1 000 baiti.",
            kapec="Pakāpe apraksta to, kas katrā solī dubultojas."),

    Kopsavilkums([
        "Pierakstu vienādu reizinātāju reizinājumu kā pakāpi.",
        "Izlasu pakāpi: «divi trešajā pakāpē».",
        "Izrēķinu pakāpes vērtību, reizinot pa vienam.",
        "Zinu, ka 2³ nav 2 · 3.",
    ]),

    Majas([
        "Uzraksti kā pakāpes: 7 · 7, 10 · 10 · 10 · 10, 6 · 6 · 6.",
        "Izrēķini 2¹, 2², 2³ ... 2¹⁰ un paskaties, cik ātri tie aug.",
        "Atrodi, kurā pakāpē divnieks pirmoreiz pārsniedz 1 000.",
    ]),
]
