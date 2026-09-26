# -*- coding: utf-8 -*-
"""4. klase, 24. stunda: «Kā modelēt 23 · 3?»

4.2. temata sākums. Pirms pieraksta - modelis: 23 · 3 ir trīs reizes pa
2 desmitiem un 3 vieniem. Rūtiņu taisnstūrī tas sadalās divās daļās -
20 · 3 un 3 · 3 -, un no šī attēla vēlāk aug sadalīšanas īpašība un
reizināšana stabiņā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         figura, restis)

TEMA = "Kā modelēt 23 · 3?"

MERKIS = ("Modelēsim divciparu skaitļa reizinājumu ar viencipara skaitli ar "
          "monētām un rūtiņām taisnstūrī.")

SATURS = [
    Sakums("Cik maksā 3 kino biļetes pa 23 €?",
           zimejums=restis([["10 €", "10 €", "1 €", "1 €", "1 €"],
                            ["10 €", "10 €", "1 €", "1 €", "1 €"],
                            ["10 €", "10 €", "1 €", "1 €", "1 €"]],
                           "3 reizes pa 23 €"),
           paraksts="Seši desmitnieki un deviņi viennieki.",
           fakti=["Desmitniekus saskaita atsevišķi: 3 · 20 = 60.",
                  "Vienniekus atsevišķi: 3 · 3 = 9.",
                  "Kopā 60 + 9 = 69."]),

    Doma("Reizini desmitus un vienus atsevišķi",
         "Divciparu skaitli sadala desmitos un vienos, katru daļu reizina, un "
         "rezultātus saskaita.",
         soli=[
             "Sadali: 23 = 20 + 3.",
             "Reizini desmitus: 20 · 3 = 60.",
             "Reizini vienus: 3 · 3 = 9.",
             "Saskaiti: 60 + 9 = 69.",
         ],
         pieze="Rūtiņās: taisnstūris 23 × 3 sadalās 20 × 3 un 3 × 3."),

    Zimejums("Rūtiņu taisnstūris 23 × 3",
             figura([(0, 0), (23, 0), (23, 3), (20, 3), (20, 0), (20, 3),
                     (0, 3)],
                    uzraksti=[(10, 1.5, "20 · 3 = 60"),
                              (21.5, 1.5, "9")],
                    platums=24, augstums=4),
             paskaidro="Garākā daļa - 20 kolonnas pa 3; īsā - 3 kolonnas pa 3.",
             ievads="Katra rūtiņa ir viens. Pavisam 69 rūtiņas."),

    Paraugs("Modelē 42 · 2",
            uzd="Cik ir 42 · 2? Izmanto monētas: 4 desmitnieki un 2 viennieki, "
                "divreiz.",
            soli=[
                ("42 = 40 + 2", None),
                ("40 · 2 = 80", "Astoņi desmitnieki."),
                ("2 · 2 = 4", "Četri viennieki."),
                ("80 + 4 = 84", None),
            ],
            atbilde="84"),

    Ievadi("Modelē un izrēķini", [
        {"jaut": "31 · 3 = ?", "atb": ["93"], "padoms": "90 + 3."},
        {"jaut": "24 · 2 = ?", "atb": ["48"], "padoms": "40 + 8."},
        {"jaut": "12 · 4 = ?", "atb": ["48"], "padoms": "40 + 8."},
        {"jaut": "21 · 4 = ?", "atb": ["84"], "padoms": "80 + 4."},
        {"jaut": "33 · 3 = ?", "atb": ["99"], "padoms": "90 + 9."},
        {"jaut": "11 · 7 = ?", "atb": ["77"], "padoms": "70 + 7."},
    ], pamats=4),

    Varianti("Kurš modelis atbilst?", [
        {"jaut": "Kurš modelis ir 32 · 3?",
         "opcijas": ["3 rindas pa 3 desmitniekiem un 2 vienniekiem",
                     "3 desmitnieki un 2 viennieki",
                     "32 rindas pa 3 desmitniekiem",
                     "2 rindas pa 3 desmitniekiem"], "pareizi": 0,
         "padoms": "Trīs reizes skaitlis 32."},
        {"jaut": "Taisnstūris 14 × 2 sadalās:",
         "opcijas": ["10 × 2 un 4 × 2", "14 × 1 un 1 × 2",
                     "10 × 4 un 2 × 2", "1 × 4 un 2 × 2"], "pareizi": 0,
         "padoms": "14 = 10 + 4."},
        {"jaut": "Cik desmitnieku vajag, lai modelētu 23 · 3?",
         "opcijas": ["6", "2", "3", "9"], "pareizi": 0,
         "padoms": "Katrā 23 ir 2 desmitnieki, un to ir trīs."},
    ]),

    Pasaule("Konstruktora komplekti",
            Ievadi("", [
                {"jaut": "Vienā kastē ir 21 riepa. Cik riepu ir 4 kastēs?",
                 "atb": ["84"], "padoms": "20 · 4 + 1 · 4."},
                {"jaut": "Vienā komplektā 32 skrūves. Cik skrūvju 3 "
                         "komplektos?",
                 "atb": ["96"], "padoms": "90 + 6."},
                {"jaut": "Robota rokai 13 detaļas. Cik detaļu 3 rokām?",
                 "atb": ["39"], "padoms": "30 + 9."},
                {"jaut": "Vienā maisiņā 44 klucīši. Cik klucīšu 2 maisiņos?",
                 "atb": ["88"], "padoms": "80 + 8."},
            ]),
            pavediens="tehnika",
            konteksts="Detaļas pako vienādos komplektos - tāpēc kopējo skaitu "
                      "var atrast ar reizināšanu.",
            kapec="Modelis parāda, kāpēc desmitus un vienus drīkst reizināt "
                  "atsevišķi."),

    Petijums("Monētu modelis",
             soli=[
                 "Paņem 10 centu un 1 centa monētas (vai papīra kartītes).",
                 "Saliec 23 ct trīs reizes.",
                 "Saskaiti atsevišķi desmitnieku un viennieku summas.",
                 "Pieraksti: 23 · 3 = 60 + 9 = 69.",
             ],
             vajag="monētas vai papīra kartītes ar 10 un 1",
             secinajums="Reizinot desmitus un vienus atsevišķi, iegūst to "
                        "pašu, ko skaitot visu kopā."),

    Kopsavilkums([
        "Modelēju divciparu skaitļa reizinājumu ar monētām.",
        "Sadalu rūtiņu taisnstūri divās daļās.",
        "Reizinu desmitus un vienus atsevišķi un saskaitu.",
    ]),

    Majas([
        "Ar monētām modelē 34 · 2 un pastāsti mājiniekiem, ko dari.",
        "Uzzīmē rūtiņās taisnstūri 12 × 3 un sadali to divās daļās.",
        "Atrodi mājās kaut ko, kas sapakots pa 10 vai 20.",
    ]),
]
