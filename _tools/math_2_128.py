# -*- coding: utf-8 -*-
"""2. klase, 128. stunda: «Kur dzīvē reizina ar 2?»

Mikrotemata noslēgums: dzīves piemēri, kur jāreizina vai jādala ar 2 -
apavi, divvietīgas istabas, abpusējas lapas, dubultas porcijas. Skolēni
izdomā savus piemērus un pieraksta tos ar «·» un «:».
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti)

TEMA = "Kur dzīvē reizina ar 2?"

MERKIS = ("Šodien izdomāsim piemērus no dzīves, kur jāreizina vai jādala "
          "ar 2.")

SATURS = [
    Sakums("Cik lappušu ir grāmatā ar 50 lapām?",
           fakti=["Katrai lapai ir 2 puses - 2 lappuses.",
                  "50 · 2 = 100 lappušu.",
                  "Reizināšana ar 2 ir visur ap mums."]),

    Doma("Kur meklēt «pa 2»",
         "Ja katrā ir pa 2 - reizina; ja kopskaitu dala pāros - dala.",
         soli=[
             "Pāri: apavi, cimdi, zeķes.",
             "Katram 2: acis, rokas, velosipēda riteņi.",
             "Dubultas lietas: divvietīga istaba, divas puses.",
             "Pieraksti ar «·» vai «:».",
         ]),

    Ievadi("Rēķini", [
        {"jaut": "Viesnīcā 9 divvietīgas istabas. Cik viesu var "
                 "apmesties?", "atb": ["18"], "padoms": "9 · 2."},
        {"jaut": "Laivā 2 airi. Cik airu 6 laivām?", "atb": ["12"],
         "padoms": "6 · 2."},
        {"jaut": "20 skolēni sēž solos pa 2. Cik solu?", "atb": ["10"],
         "padoms": "20 : 2."},
        {"jaut": "Ģimenē 4 cilvēki, katrs uzvilka zābakus. Cik zābaku "
                 "kopā?",
         "atb": ["8"], "padoms": "4 · 2."},
    ]),

    Varianti("Reizināt vai dalīt?", [
        {"jaut": "«Cik riteņu 5 motocikliem?»",
         "opcijas": ["5 · 2", "5 : 2"], "jaukt": False, "pareizi": 0,
         "padoms": "Katram 2."},
        {"jaut": "«16 bērni pāros - cik pāru?»",
         "opcijas": ["16 · 2", "16 : 2"], "jaukt": False, "pareizi": 1,
         "padoms": "Sadala pa 2."},
        {"jaut": "«Grāmata 30 lapas. Cik lappušu?»",
         "opcijas": ["30 · 2", "30 : 2"], "jaukt": False, "pareizi": 0,
         "padoms": "Katrai lapai 2 lappuses."},
        {"jaut": "«18 € sadala 2 brāļiem vienādi.»",
         "opcijas": ["18 · 2", "18 : 2"], "jaukt": False, "pareizi": 1,
         "padoms": "Uz pusēm."},
    ]),

    Pasaule("Ekskursija ar vilcienu",
            Ievadi("", [
                {"jaut": "Vilciena vagonā sēdekļi pa 2. Klasē 24 bērni. "
                         "Cik sēdekļu pāru vajag?", "atb": ["12"],
                 "padoms": "24 : 2."},
                {"jaut": "Biļete 2 €. Cik maksā 10 biļetes?", "atb": ["20"],
                 "mers": "€", "padoms": "10 · 2."},
            ]),
            pavediens="celojums",
            konteksts="Klase brauc ar vilcienu uz Jūrmalu.",
            kapec="Ar reizināšanu plāno ātrāk."),

    Kopsavilkums([
        "Atrodu dzīvē situācijas ar «pa 2».",
        "Izvēlos: reizināt vai dalīt.",
        "Pierakstu ar «·» un «:».",
    ]),

    Majas([
        "Atrodi mājās 3 situācijas, kur jāreizina ar 2.",
        "Atrodi 1 situāciju, kur jādala ar 2.",
        "Pieraksti tās ar zīmēm.",
    ]),
]
