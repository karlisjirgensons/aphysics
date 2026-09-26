# -*- coding: utf-8 -*-
"""4. klase, 135. stunda: «Kāds uzdevums sanāk tev?»

Radošā stunda: skolēns pats sastāda uzdevumu par daļas vērtību, apmainās
ar klasesbiedru un risina. Laba uzdevuma pazīmes - skaidrs veselais,
dalāmi skaitļi un jautājums, uz kuru var atbildēt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, restis)

TEMA = "Kāds uzdevums sanāk tev?"

MERKIS = ("Sastādīsim savu uzdevumu par daļas vērtību, apmainīsimies ar "
          "klasesbiedru un risināsim.")

SATURS = [
    Sakums("Kā izdomāt labu uzdevumu?",
           zimejums=restis([["veselais", "daļa", "jautājums"],
                            ["36 konfektes", "2/3", "cik apēda?"],
                            ["800 m", "1/4", "cik atlika?"]],
                           "trīs sastāvdaļas"),
           fakti=["Labam uzdevumam ir veselais, daļa un jautājums.",
                  "Skaitļiem jādalās bez atlikuma."]),

    Doma("Veselais + daļa + jautājums",
         "Uzdevumu sastāda, izvēloties veselo, kas dalās ar saucēju, daļu un "
         "skaidru jautājumu.",
         soli=[
             "Izvēlies situāciju: konfektes, ceļš, nauda.",
             "Izvēlies veselo, kas dalās ar saucēju: 36 dalās ar 3.",
             "Izvēlies daļu: {2|3}.",
             "Uzdod jautājumu: cik? cik atlika? cik bija?",
         ],
         pieze="Pirms dod citam, atrisini pats - tā pārbaudīsi, vai uzdevums "
               "ir atrisināms."),

    Varianti("Vai uzdevums ir labs?", [
        {"jaut": "«{1|3} no 20 konfektēm apēda. Cik?»",
         "opcijas": ["slikts - 20 nedalās ar 3", "labs",
                     "trūkst jautājuma"], "pareizi": 0,
         "padoms": "20 : 3 nav vesels."},
        {"jaut": "«{3|4} no 40 lappusēm izlasīja.»",
         "opcijas": ["trūkst jautājuma", "labs",
                     "skaitļi nedalās"], "pareizi": 0,
         "padoms": "Ko jāatrod?"},
        {"jaut": "«{2|5} no 50 € iztērēja. Cik € palika?»",
         "opcijas": ["labs", "slikts", "trūkst veselā"], "pareizi": 0,
         "padoms": "50 : 5 = 10, palika 30 €."},
        {"jaut": "«Apēda {1|4}. Cik apēda?»",
         "opcijas": ["trūkst veselā", "labs", "trūkst daļas"],
         "pareizi": 0, "padoms": "No kā ceturtdaļa?"},
    ], pamats=4),

    Ievadi("Atrisini klasesbiedru uzdevumus", [
        {"jaut": "Annas uzdevums: 36 konfektes, apēda {2|3}. Cik apēda?",
         "atb": ["24"], "padoms": "36 : 3 · 2."},
        {"jaut": "Jura uzdevums: 800 m ceļš, noieta {3|4}. Cik atlika?",
         "atb": ["200"], "padoms": "{1|4} no 800."},
        {"jaut": "Ievas uzdevums: {2|5} klases ir 12. Cik klasē?",
         "atb": ["30"], "padoms": "12 : 2 · 5."},
        {"jaut": "Kārļa uzdevums: 50 €, iztērēja {2|5}. Cik palika?",
         "atb": ["30"], "padoms": "{3|5} no 50."},
    ]),

    Petijums("Uzdevumu apmaiņa",
             soli=[
                 "Uzraksti savu uzdevumu uz lapiņas.",
                 "Atrisini to pats otrā pusē.",
                 "Apmainies ar klasesbiedru un atrisini viņa uzdevumu.",
                 "Salīdziniet atbildes un pārrunājiet.",
             ],
             vajag="lapiņas, zīmulis",
             secinajums="Ja atbildes sakrīt, uzdevums ir labs un "
                        "atrisināts pareizi."),

    Pasaule("Uzdevums par tavu pilsētu",
            Ievadi("", [
                {"jaut": "Parkā 120 koku, {3|8} ir ozoli. Cik ozolu?",
                 "atb": ["45"], "padoms": "120 : 8 · 3."},
                {"jaut": "Ielā 60 māju, {1|5} ir jaunas. Cik jaunu?",
                 "atb": ["12"], "padoms": "60 : 5."},
                {"jaut": "Bibliotēkā {1|10} grāmatu ir komiksi - 350. Cik "
                         "grāmatu?",
                 "atb": ["3500"], "padoms": "350 · 10."},
                {"jaut": "Tirgū 48 stendi, {5|6} tirgo dārzeņus. Cik "
                         "stendu?",
                 "atb": ["40"], "padoms": "48 : 6 · 5."},
            ]),
            pavediens="skola",
            konteksts="Labākie uzdevumi ir par vietu, kuru pazīsti - savu "
                      "pilsētu vai ciemu.",
            kapec="Kas sastāda uzdevumu, tas saprot daļas no iekšpuses."),

    Kopsavilkums([
        "Sastādu uzdevumu par daļas vērtību.",
        "Pārbaudu, vai uzdevums ir atrisināms.",
        "Risinu klasesbiedru uzdevumus.",
    ]),

    Majas([
        "Sastādi 2 uzdevumus par daļām savā ģimenē.",
        "Palūdz mājiniekiem tos atrisināt.",
        "Uzraksti vienu «sliktu» uzdevumu un paskaidro, kas tajā nav labi.",
    ]),
]
