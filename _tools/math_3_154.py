# -*- coding: utf-8 -*-
"""3. klase, 154. stunda: «Ko stāsta diagramma?»

Stabiņu diagramma ar iedaļas vērtību, kas nav 1. Tieši tā ir galvenā prasme:
viens stabiņa solis var nozīmēt 10 vai 100 objektus, un bez skalas nolasīšanas
diagramma melo.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, kolonnas)

TEMA = "Ko stāsta diagramma?"

MERKIS = ("Lasīsim stabiņu un joslu diagrammu, kurā viena iedaļa atbilst 10 "
          "vai 100 objektiem.")

SATURS = [
    Sakums("Ko nozīmē viena iedaļa diagrammā?",
           zimejums=kolonnas([("1. kl.", 60), ("2. kl.", 80),
                              ("3. kl.", 50), ("4. kl.", 90)]),
           paraksts="Katrs stabiņš rāda skolēnu skaitu klasē.",
           fakti=["Diagrammā stabiņa augstums rāda skaitu.",
                  "Vienmēr vispirms noskaidro, ko nozīmē viena iedaļa."]),

    Doma("Vispirms iedaļa, tad stabiņš",
         "Ja viena iedaļa ir 10 objekti, tad piecu iedaļu stabiņš rāda 50.",
         soli=[
             "Atrodi diagrammas skalu un tās iedaļas vērtību.",
             "Saskaiti, cik iedaļu ir stabiņā.",
             "Reizini iedaļu skaitu ar iedaļas vērtību.",
             "Salīdzini stabiņus savā starpā.",
         ],
         pieze="Diagramma parāda arī to, ko tabula neparāda uzreiz: kurš "
               "stabiņš ir garākais, redzams ar aci, skaitļus nelasot."),

    Paraugs("Cik skolēnu ir otrajā klasē?",
            uzd="Viena iedaļa ir 10 skolēni. Otrās klases stabiņā ir 8 "
                "iedaļas. Cik skolēnu tur ir?",
            soli=[
                ("Viena iedaļa = 10 skolēni",
                 "Skalas vērtība."),
                ("8 iedaļas",
                 "Tik augsts ir stabiņš."),
                ("8 · 10 = 80",
                 "Otrajā klasē ir 80 skolēnu."),
            ],
            atbilde="80 skolēnu"),

    Ievadi("Nolasi diagrammu", [
        {"jaut": "Viena iedaļa ir 10. Stabiņā 8 iedaļas. Cik tas ir?",
         "atb": ["80"], "padoms": "8 · 10."},
        {"jaut": "Viena iedaļa ir 100. Stabiņā 6 iedaļas. Cik tas ir?",
         "atb": ["600"], "padoms": "6 · 100."},
        {"jaut": "Klasēs 60, 80, 50 un 90 skolēnu. Cik kopā?",
         "atb": ["280"], "padoms": "140 + 140."},
        {"jaut": "Par cik lielākā klase ir lielāka par mazāko?",
         "atb": ["40"], "padoms": "90 − 50."},
        {"jaut": "Cik skolēnu vidēji ir vienā klasē no šīm četrām?",
         "atb": ["70"], "padoms": "280 : 4."},
        {"jaut": "Stabiņš rāda 70, viena iedaļa ir 10. Cik iedaļu tajā ir?",
         "atb": ["7"], "padoms": "70 : 10."},
    ], pamats=4),

    Zimejums("Diagramma ar lielu iedaļu",
             kolonnas([("pirmd.", 300), ("otrd.", 500), ("trešd.", 400)],
                      " pusdienas"),
             paskaidro="Šeit viena iedaļa ir 100 pusdienu - tāpēc stabiņi "
                       "nav augstāki, kaut skaitļi ir lielāki.",
             ievads="Ēdnīcas dati trijās dienās."),

    Varianti("Ko rāda diagramma?", [
        {"jaut": "Kurš stabiņš ir visaugstākais?",
         "opcijas": ["4. klase ar 90", "2. klase ar 80", "1. klase ar 60",
                     "3. klase ar 50"],
         "pareizi": 0, "padoms": "Lielākais skaitlis."},
        {"jaut": "Viena iedaļa ir 100. Ko rāda 5 iedaļu stabiņš?",
         "opcijas": ["500", "50", "5", "5000"],
         "pareizi": 0, "padoms": "5 · 100."},
        {"jaut": "Ko noskaidro vispirms, lasot diagrammu?",
         "opcijas": ["Iedaļas vērtību", "Stabiņu skaitu",
                     "Krāsas", "Virsrakstu"],
         "pareizi": 0, "padoms": "Bez tās skaitļus nolasīt nevar."},
        {"jaut": "Kāpēc diagramma ir ērtāka par tabulu?",
         "opcijas": ["Lielāko redz ar aci", "Tajā ir vairāk skaitļu",
                     "Tā ir precīzāka", "Tā ir īsāka"],
         "pareizi": 0, "padoms": "Salīdzināt var, skaitļus nelasot."},
    ], pamats=4),

    Pasaule("Cik pusdienu izsniedz ēdnīca?",
            Ievadi("", [
                {"jaut": "Pirmdien 300, otrdien 500, trešdien 400 pusdienu. "
                         "Cik kopā?",
                 "atb": ["1200"], "padoms": "800 + 400."},
                {"jaut": "Par cik otrdien izsniedza vairāk nekā pirmdien?",
                 "atb": ["200"], "padoms": "500 − 300."},
                {"jaut": "Cik pusdienu vidēji dienā?", "atb": ["400"],
                 "padoms": "1200 : 3."},
                {"jaut": "Viena pusdiena maksā 2 eiro. Cik eiro ieņēma trīs "
                         "dienās?",
                 "atb": ["2400"], "padoms": "1200 · 2."},
            ]),
            pavediens="skola",
            konteksts="Ēdnīca skaita pusdienas katru dienu un rāda tās "
                      "diagrammā - tā uzreiz redz, kura diena ir noslogotākā.",
            kapec="Pēc diagrammas plāno, cik ēdiena gatavot rīt."),

    Kopsavilkums([
        "Nolasu stabiņu diagrammu.",
        "Nosaku iedaļas vērtību.",
        "Salīdzinu stabiņus savā starpā.",
        "Aprēķinu kopsummu un vidējo vērtību.",
    ]),

    Majas([
        "Saskaiti, cik stundu nedēļā tev ir katrā mācību priekšmetā.",
        "Uzzīmē stabiņu diagrammu ar iedaļu 1 stunda.",
        "Pasaki, kurš priekšmets ir ar visaugstāko stabiņu.",
    ]),
]
