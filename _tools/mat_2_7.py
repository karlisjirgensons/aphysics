# -*- coding: utf-8 -*-
"""Matemātika, 2. klase. 2.7. Ko nozīmē reizināt un dalīt ar 2?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 2. klase, 2.7. temats): reizināšana ar 2
kā vienādu daudzumu ņemšana, dalīšana ar 2 kā sadalīšana divās vienādās
daļās, saistība starp reizināšanu un dalīšanu, pāra un nepāra skaitļi,
jēdzieni «2 reizes vairāk/mazāk» un «puse».

Daļas raksta ar {skaitītājs|saucējs}, piemēram «{1|2}», tāpēc ekrānā un Word
failā tās ir vertikālas (rules_pd.txt).
"""

PRIEKSMETS = "Matemātika  |  2. klase"
TEMATS = "2.7."
NOSAUKUMS = "Ko nozīmē reizināt un dalīt ar 2?"

ATGADNE = [
    "Reizināt ar 2 nozīmē ņemt 2 tādus daudzumus:  2 · 5 = 5 + 5 = 10",
    "Dalīt ar 2 nozīmē sadalīt divās vienādās daļās:  10 : 2 = 5   ·   "
    "puse ir {1|2} no veselā",
    "Pāra skaitli var izdalīt ar 2:  2, 4, 6, 8, 10, …   ·   nepāra: "
    "1, 3, 5, 7, 9, …",
]

FD = {
    "veids": "fd",
    "klase": 2,
    "temats": TEMATS,
    "nr": 7,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "7. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 2.7. temata beigās. Pārbauda "
                "reizināšanas un dalīšanas ar 2 jēgu, reizinājumu un "
                "dalījumu, saistību starp abām darbībām, pāra un nepāra "
                "skaitļus, jēdzienus «2 reizes vairāk/mazāk» un «puse».",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Skaidro, ko nozīmē reizināt ar 2",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko nozīmē reizināt ar 2?",
              ["ņemt 2 tādus daudzumus", "sadalīt uz pusēm",
               "pieskaitīt 2", "atņemt 2"], 0),
             ("Kā citādi pieraksta 4 + 4?",
              ["2 · 4", "4 · 4", "4 : 2", "4 − 2"], 0),
             ("Kā citādi pieraksta 2 · 7?",
              ["7 + 7", "7 + 2", "7 − 2", "7 : 2"], 0),
         ]},
        {"sr": "Reizina viencipara skaitļus ar 2",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 2 · 6?", ["8", "10", "12", "14"], 2),
             ("Cik ir 2 · 9?", ["11", "16", "18", "20"], 2),
             ("Cik ir 2 · 8?", ["10", "14", "16", "18"], 2),
         ]},
        {"sr": "Skaidro, ko nozīmē dalīt ar 2",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko nozīmē dalīt ar 2?",
              ["sadalīt divās vienādās daļās", "ņemt 2 tādus daudzumus",
               "atņemt 2", "pieskaitīt 2"], 0),
             ("Ar kuru zīmi pieraksta dalīšanu?", [":", "·", "+", "−"], 0),
             ("12 konfektes sadala uz pusēm. Cik ir katrā daļā?",
              ["4", "5", "6", "10"], 2),
         ]},
        {"sr": "Dala pāra skaitļus līdz 20 ar 2",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 14 : 2?", ["6", "7", "8", "12"], 1),
             ("Cik ir 18 : 2?", ["7", "8", "9", "16"], 2),
             ("Cik ir 20 : 2?", ["2", "5", "10", "18"], 2),
         ]},
        {"sr": "Lieto saistību starp reizināšanu un dalīšanu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Zināms, ka 2 · 5 = 10. Cik ir 10 : 2?",
              ["2", "5", "10", "20"], 1),
             ("Zināms, ka 16 : 2 = 8. Cik ir 2 · 8?",
              ["8", "10", "16", "18"], 2),
             ("Kā pārbaudīt, vai 18 : 2 = 9?",
              ["aprēķinot 2 · 9", "aprēķinot 18 + 9", "aprēķinot 18 − 9",
               "aprēķinot 9 : 2"], 0),
         ]},
        {"sr": "Atšķir pāra un nepāra skaitļus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurš skaitlis ir pāra skaitlis?", ["7", "9", "14", "15"], 2),
             ("Kurš skaitlis ir nepāra skaitlis?", ["8", "12", "13", "20"],
              2),
             ("Kuru skaitli var izdalīt ar 2 bez atlikuma?",
              ["11", "15", "16", "19"], 2),
         ]},
        {"sr": "Zina pāra un nepāra skaitļu secību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāds skaitlis seko pāra skaitlim?",
              ["nepāra", "pāra", "vienmēr 10", "vienmēr 0"], 0),
             ("Virkne:  2, 4, 6, 8, …  Kurš skaitlis ir nākamais?",
              ["9", "10", "11", "12"], 1),
             ("Virkne:  1, 3, 5, 7, …  Kurš skaitlis ir nākamais?",
              ["8", "9", "10", "11"], 1),
         ]},
        {"sr": "Lieto jēdzienu «2 reizes vairāk»",
         "stunda": TEMATS,
         "jautajumi": [
             ("Annai ir 6 uzlīmes, Ilzei 2 reizes vairāk. Cik ir Ilzei?",
              ["3", "8", "12", "16"], 2),
             ("Kurš skaitlis ir 2 reizes lielāks nekā 7?",
              ["9", "12", "14", "72"], 2),
             ("Ar kuru darbību aprēķina «2 reizes vairāk»?",
              ["reizina ar 2", "dala ar 2", "pieskaita 2", "atņem 2"], 0),
         ]},
        {"sr": "Lieto jēdzienu «2 reizes mazāk»",
         "stunda": TEMATS,
         "jautajumi": [
             ("Jānim ir 16 klucīši, Pēterim 2 reizes mazāk. Cik ir Pēterim?",
              ["6", "8", "14", "32"], 1),
             ("Kurš skaitlis ir 2 reizes mazāks nekā 18?",
              ["8", "9", "16", "36"], 1),
             ("Ar kuru darbību aprēķina «2 reizes mazāk»?",
              ["dala ar 2", "reizina ar 2", "atņem 2", "pieskaita 2"], 0),
         ]},
        {"sr": "Lieto jēdzienu «puse»",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā pieraksta pusi?", ["{1|2}", "{2|1}", "{1|4}", "{2|2}"], 0),
             ("Cik ir puse no 10?", ["2", "5", "8", "20"], 1),
             ("Lente ir 12 cm. Cik gara ir tās puse?",
              ["4 cm", "6 cm", "10 cm", "24 cm"], 1),
         ]},
        {"sr": "Risina situāciju uzdevumu ar reizināšanu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Vienā kastē 8 olas. Cik olu ir 2 kastēs?",
              ["4", "10", "16", "18"], 2),
             ("Biļete maksā 5 €. Cik maksā 2 biļetes?",
              ["5 €", "7 €", "10 €", "25 €"], 2),
             ("Viens loks ir 9 m. Cik metru ir 2 tādi loki?",
              ["11 m", "18 m", "19 m", "92 m"], 1),
         ]},
        {"sr": "Risina situāciju uzdevumu ar dalīšanu",
         "stunda": TEMATS,
         "jautajumi": [
             ("14 ābolus sadala 2 vienādās daļās. Cik ir katrā?",
              ["6", "7", "8", "12"], 1),
             ("20 grāmatas sadala uz pusēm. Cik ir katrā daļā?",
              ["2", "5", "10", "18"], 2),
             ("Virve ir 16 m gara. To pārgriež uz pusēm. Cik garš ir viens "
              "gabals?",
              ["4 m", "8 m", "14 m", "32 m"], 1),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 2,
    "temats": TEMATS,
    "nr": 7,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "7. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 2.7. temata noslēgumā. "
                "Pārbauda reizināšanu un dalīšanu ar 2, saistību starp abām "
                "darbībām, pāra un nepāra skaitļus, jēdzienus «2 reizes "
                "vairāk/mazāk» un «puse», kā arī situāciju uzdevumu "
                "risināšanu.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 punktus. "
              "Risinājumu raksti un zīmē tam atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Skaidro reizināšanas un dalīšanas jēgu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko nozīmē reizināt ar 2?",
              ["ņemt 2 tādus daudzumus", "sadalīt uz pusēm", "pieskaitīt 2",
               "atņemt 2"], 0),
             ("Ko nozīmē dalīt ar 2?",
              ["sadalīt divās vienādās daļās", "ņemt 2 tādus daudzumus",
               "pieskaitīt 2", "atņemt 2"], 0),
             ("Kā citādi pieraksta 6 + 6?",
              ["2 · 6", "6 · 6", "6 : 2", "6 − 2"], 0),
         ]},
        {"sr": "Reizina ar 2",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 2 · 7?", ["9", "12", "14", "16"], 2),
             ("Cik ir 2 · 9?", ["11", "16", "18", "20"], 2),
             ("Cik ir 2 · 5?", ["7", "10", "12", "25"], 1),
         ]},
        {"sr": "Dala ar 2",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 12 : 2?", ["4", "6", "8", "10"], 1),
             ("Cik ir 16 : 2?", ["6", "8", "14", "32"], 1),
             ("Cik ir 20 : 2?", ["2", "5", "10", "18"], 2),
         ]},
        {"sr": "Atšķir pāra un nepāra skaitļus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurš skaitlis ir pāra?", ["9", "11", "18", "13"], 2),
             ("Kurš skaitlis ir nepāra?", ["10", "14", "15", "20"], 2),
             ("Kuru skaitli nevar izdalīt ar 2 bez atlikuma?",
              ["12", "14", "17", "18"], 2),
         ]},
        {"sr": "Lieto «2 reizes vairāk» un «2 reizes mazāk»",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurš skaitlis ir 2 reizes lielāks nekā 8?",
              ["4", "10", "16", "82"], 2),
             ("Kurš skaitlis ir 2 reizes mazāks nekā 14?",
              ["7", "12", "16", "28"], 0),
             ("Ar kuru darbību aprēķina «2 reizes mazāk»?",
              ["dala ar 2", "reizina ar 2", "atņem 2", "pieskaita 2"], 0),
         ]},
        {"sr": "Lieto jēdzienu «puse»",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā pieraksta pusi?", ["{1|2}", "{2|1}", "{1|3}", "{1|4}"], 0),
             ("Cik ir puse no 18?", ["6", "9", "12", "36"], 1),
             ("Lente ir 20 cm. Cik gara ir tās puse?",
              ["5 cm", "10 cm", "15 cm", "40 cm"], 1),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Reizina un dala ar 2",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("2 · 6 = ……", "12"), ("14 : 2 = ……", "7"),
                         ("2 · 9 = ……", "18"), ("20 : 2 = ……", "10")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("2 · 8 = ……", "16"), ("12 : 2 = ……", "6"),
                         ("2 · 7 = ……", "14"), ("18 : 2 = ……", "9")]},
             {"tips": "parveide", "virs": "Aprēķini",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("2 · 5 = ……", "10"), ("16 : 2 = ……", "8"),
                         ("2 · 10 = ……", "20"), ("10 : 2 = ……", "5")]},
         ]},
        {"sr": "Lieto «2 reizes vairāk», «2 reizes mazāk» un «puse»",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Ieraksti skaitli",
              "note": "Ieraksti pareizo skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("2 reizes vairāk nekā 7 ir ……", "14"),
                         ("2 reizes mazāk nekā 16 ir ……", "8"),
                         ("Puse no 12 ir ……", "6")]},
             {"tips": "parveide", "virs": "Ieraksti skaitli",
              "note": "Ieraksti pareizo skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("2 reizes vairāk nekā 9 ir ……", "18"),
                         ("2 reizes mazāk nekā 20 ir ……", "10"),
                         ("Puse no 14 ir ……", "7")]},
             {"tips": "parveide", "virs": "Ieraksti skaitli",
              "note": "Ieraksti pareizo skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("2 reizes vairāk nekā 6 ir ……", "12"),
                         ("2 reizes mazāk nekā 18 ir ……", "9"),
                         ("Puse no 16 ir ……", "8")]},
         ]},
        {"sr": "Modelē reizināšanu un dalīšanu ar zīmējumu",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Zīmē un pieraksti", "vieta": 6.5,
              "ievads": "Zīmē ripas rūtiņās!",
              "jaut": [("Uzzīmē 2 grupas pa 6 ripām!", 1),
                       ("Pieraksti to kā reizinājumu un aprēķini!", 1),
                       ("Uzzīmē, kā 12 ripas sadalīt divās vienādās daļās!",
                        1),
                       ("Pieraksti to kā dalījumu un aprēķini!", 1)],
              "atbildes": ["1) Uzzīmētas 2 grupas pa 6 ripām.   (1 p.)",
                           "2) 2 · 6 = 12   (1 p.)",
                           "3) Uzzīmētas divas grupas pa 6 ripām.   (1 p.)",
                           "4) 12 : 2 = 6   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Zīmē un pieraksti", "vieta": 6.5,
              "ievads": "Zīmē ripas rūtiņās!",
              "jaut": [("Uzzīmē 2 grupas pa 7 ripām!", 1),
                       ("Pieraksti to kā reizinājumu un aprēķini!", 1),
                       ("Uzzīmē, kā 14 ripas sadalīt divās vienādās daļās!",
                        1),
                       ("Pieraksti to kā dalījumu un aprēķini!", 1)],
              "atbildes": ["1) Uzzīmētas 2 grupas pa 7 ripām.   (1 p.)",
                           "2) 2 · 7 = 14   (1 p.)",
                           "3) Uzzīmētas divas grupas pa 7 ripām.   (1 p.)",
                           "4) 14 : 2 = 7   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Zīmē un pieraksti", "vieta": 6.5,
              "ievads": "Zīmē ripas rūtiņās!",
              "jaut": [("Uzzīmē 2 grupas pa 8 ripām!", 1),
                       ("Pieraksti to kā reizinājumu un aprēķini!", 1),
                       ("Uzzīmē, kā 16 ripas sadalīt divās vienādās daļās!",
                        1),
                       ("Pieraksti to kā dalījumu un aprēķini!", 1)],
              "atbildes": ["1) Uzzīmētas 2 grupas pa 8 ripām.   (1 p.)",
                           "2) 2 · 8 = 16   (1 p.)",
                           "3) Uzzīmētas divas grupas pa 8 ripām.   (1 p.)",
                           "4) 16 : 2 = 8   (1 p.)"]},
         ]},
        {"sr": "Risina situāciju uzdevumu ar reizināšanu vai dalīšanu",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Uzdevums par konfektēm",
              "vieta": 5.5,
              "ievads": "Vienā paciņā ir 9 konfektes. Nopirka 2 paciņas un "
                        "visas konfektes sadalīja uz pusēm diviem bērniem.",
              "jaut": [("Aprēķini, cik konfekšu nopirka!", 1),
                       ("Aprēķini, cik konfekšu tika katram bērnam!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) 2 · 9 = 18   (1 p.)", "2) 18 : 2 = 9   (1 p.)",
                           "3) Atbilde: nopirka 18; katram tika "
                           "9 konfektes.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Uzdevums par ābolīšiem",
              "vieta": 5.5,
              "ievads": "Vienā grozā ir 8 āboli. Atnesa 2 grozus un visus "
                        "ābolus sadalīja uz pusēm divām klasēm.",
              "jaut": [("Aprēķini, cik ābolu atnesa!", 1),
                       ("Aprēķini, cik ābolu tika katrai klasei!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) 2 · 8 = 16   (1 p.)", "2) 16 : 2 = 8   (1 p.)",
                           "3) Atbilde: atnesa 16; katrai klasei tika "
                           "8 āboli.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Uzdevums par lenti", "vieta": 5.5,
              "ievads": "Viena lente ir 10 cm gara. Nopirka 2 tādas lentes "
                        "un kopējo garumu pārgrieza uz pusēm.",
              "jaut": [("Aprēķini abu lenšu kopgarumu!", 1),
                       ("Aprēķini, cik garš ir viens gabals pēc "
                        "pārgriešanas!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) 2 · 10 cm = 20 cm   (1 p.)",
                           "2) 20 cm : 2 = 10 cm   (1 p.)",
                           "3) Atbilde: kopā 20 cm; viens gabals 10 cm.   "
                           "(1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
