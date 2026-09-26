# -*- coding: utf-8 -*-
"""4. klase, 118. stunda: «Kas šajā situācijā ir veselais?»

4.6. temata sākums. Daļa vienmēr ir daļa *no kaut kā*. {1|2} klases un
{1|2} skolas ir dažādi skaitļi, jo veselais ir cits. Pirms rēķina skolēns
nosauc veselo un raksturo to skaitliski - tas ir svarīgākais solis visos
daļu uzdevumos.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, kolonnas)

TEMA = "Kas šajā situācijā ir veselais?"

MERKIS = ("Paskaidrosim, kas dotajā situācijā ir veselais, un raksturosim "
          "to skaitliski.")

SATURS = [
    Sakums("Kura puse ir lielāka?",
           zimejums=kolonnas([("1/2 klases", 13), ("1/2 skolas", 250)]),
           paraksts="Abas ir «puse», bet veselie atšķiras: 26 un 500.",
           fakti=["Daļa bez veselā neko nepasaka.",
                  "Vispirms jājautā: puse no kā?"]),

    Doma("Daļa vienmēr ir daļa no kaut kā",
         "Veselais ir tas, ko dala; tā skaitliskā vērtība nosaka, cik ir "
         "daļa.",
         soli=[
             "Izlasi teikumu un atrodi vārdu «no»: {1|3} *no klases*.",
             "Tas, kas aiz «no», ir veselais.",
             "Nosaki veselā lielumu skaitliski: klasē 24 skolēni.",
             "Tikai tad rēķini daļu: {1|3} no 24 ir 8.",
         ],
         pieze="Ja veselais nav zināms skaitliski, no daļas vien nevar "
               "pateikt, cik tas ir."),

    Paraugs("Kas ir veselais?",
            uzd="«{1|4} no 20 € kabatasnaudas iztērēju saldējumam.» Kas ir "
                "veselais un cik tas ir?",
            soli=[
                ("veselais - kabatasnauda", "Aiz vārda «no»."),
                ("skaitliski - 20 €", None),
                ("{1|4} no 20 € = 5 €", "Tagad var rēķināt."),
            ],
            atbilde="veselais - 20 € kabatasnauda"),

    Varianti("Kas ir veselais?", [
        {"jaut": "«{2|3} klases skolēnu mīl futbolu.»",
         "opcijas": ["visi klases skolēni", "futbols", "{2|3}",
                     "futbola bumba"], "pareizi": 0,
         "padoms": "No kā ņemta daļa?"},
        {"jaut": "«Pusi picas apēda Anna.»",
         "opcijas": ["visa pica", "Anna", "puse", "gabals"], "pareizi": 0,
         "padoms": "Puse no picas."},
        {"jaut": "«{1|10} no algas iekrāj.»",
         "opcijas": ["visa alga", "krājums", "10 €", "banka"], "pareizi": 0,
         "padoms": "Daļa no algas."},
        {"jaut": "«{3|4} ceļa jau nobraukts.»",
         "opcijas": ["viss ceļš", "nobrauktais", "{3|4}", "auto"],
         "pareizi": 0, "padoms": "Daļa no ceļa."},
    ], pamats=4),

    Ievadi("Cik ir veselais?", [
        {"jaut": "Klasē 26 skolēni. Cik ir {1|2} klases?", "atb": ["13"],
         "padoms": "26 : 2."},
        {"jaut": "Skolā 500 skolēni. Cik ir {1|2} skolas?", "atb": ["250"],
         "padoms": "500 : 2."},
        {"jaut": "Diennaktī 24 h. Cik stundu ir {1|3} diennakts?",
         "atb": ["8"], "padoms": "24 : 3."},
        {"jaut": "Gadā 12 mēneši. Cik mēnešu ir {1|4} gada?", "atb": ["3"],
         "padoms": "12 : 4."},
    ]),

    Pasaule("Latvijas daba skaitļos",
            Ievadi("", [
                {"jaut": "Novadā ir 40 ezeru, {1|4} no tiem ir lieli. Cik "
                         "lielu ezeru?",
                 "atb": ["10"], "padoms": "40 : 4."},
                {"jaut": "Mežā 900 koku, {1|3} ir priedes. Cik priežu?",
                 "atb": ["300"], "padoms": "900 : 3."},
                {"jaut": "Upe ir 60 km gara, {1|2} tās tek caur mežu. Cik km?",
                 "atb": ["30"], "padoms": "60 : 2."},
                {"jaut": "Kas pirmajā uzdevumā bija veselais? Ieraksti skaitli.",
                 "atb": ["40"], "padoms": "Visi novada ezeri."},
            ]),
            pavediens="daba",
            konteksts="Apmēram puse Latvijas teritorijas ir meži - bet «puse» "
                      "ir liela tikai tāpēc, ka veselais ir visa valsts.",
            kapec="Kas zina veselo, tas zina, cik liela ir daļa."),

    Kopsavilkums([
        "Nosaucu, kas situācijā ir veselais.",
        "Raksturoju veselo skaitliski.",
        "Zinu, ka viena daļa no dažādiem veselajiem ir dažāda.",
    ]),

    Majas([
        "Atrodi 3 teikumus ar daļām (ziņās, grāmatā) un nosauc veselo.",
        "Salīdzini: {1|2} no tavas klases un {1|2} no tavas ģimenes.",
        "Paskaidro kādam, kāpēc «puse» var būt gan 2, gan 250.",
    ]),
]
