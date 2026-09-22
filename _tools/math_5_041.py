# -*- coding: utf-8 -*-
"""5. klase, 41. stunda: «Kā sagrupēt skaitļus Venna diagrammā?»

Mikrotemata pēdējā stunda saliek kopā divas prasmes: dalāmības pazīmes un
Venna diagrammu, kas pazīstama no 4. stundas. Pārklājums te vairs nav
zīmējuma detaļa - tieši tajā atrodas skaitļi, kas dalās ar abiem, un tas ir
tas pats kopīgais dalāmais, tikai attēlots.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, venna)

TEMA = "Kā sagrupēt skaitļus Venna diagrammā?"

MERKIS = ("Mācīsimies grupēt skaitļus pēc dalāmības pazīmēm un attēlot tos "
          "Venna diagrammā.")

SATURS = [
    Sakums("Kur liek skaitli, kas dalās ar abiem?",
           zimejums=venna([2, 4, 8, 10], [3, 9, 15, 21], [6, 12, 18],
                          ("dalās ar 2", "dalās ar 3")),
           paraksts="Pārklājumā - skaitļi, kas dalās gan ar 2, gan ar 3.",
           fakti=["Katrs aplis ir viena pazīme.",
                  "Pārklājums nozīmē «abas pazīmes reizē»."]),

    Doma("Pārklājums nozīmē «un», ne «vai»",
         "Skaitlis nonāk pārklājumā tikai tad, ja tam piemīt abas pazīmes "
         "vienlaikus.",
         soli=[
             "Nosauc abas pazīmes - katrai savs aplis.",
             "Paņem skaitli un pārbaudi pirmo pazīmi.",
             "Pārbaudi otro pazīmi.",
             "Ja abas izpildās - raksti pārklājumā.",
             "Ja neviena neizpildās - raksti ārpus abiem apļiem.",
         ],
         pieze="Skaitļi, kas dalās gan ar 2, gan ar 3, dalās arī ar 6 - "
               "tāpēc pārklājumā vienmēr nonāk tieši abu skaitļu kopīgie "
               "dalāmie."),

    Zimejums("Citas divas pazīmes",
             venna([3, 9, 21], [5, 10, 20], [15, 30],
                   ("dalās ar 3", "dalās ar 5")),
             paskaidro="Pārklājumā ir 15 un 30 - tie dalās ar 15, kas ir 3 un "
                       "5 mazākais kopīgais dalāmais.",
             ievads="Tas pats ar citām pazīmēm."),

    Paraugs("Sagrupē skaitļus no 1 līdz 20",
            uzd="Sagrupē skaitļus 6, 9, 10 un 7 pēc pazīmēm «dalās ar 2» un "
                "«dalās ar 3».",
            soli=[
                ("6 dalās ar 2 un ar 3 - pārklājumā",
                 "Abas pazīmes reizē."),
                ("9 dalās tikai ar 3 - labajā aplī",
                 "Ar 2 nedalās, jo ir nepāra."),
                ("10 dalās tikai ar 2 - kreisajā aplī",
                 "1 + 0 = 1, ar 3 nedalās."),
                ("7 nedalās ne ar vienu - ārpus abiem",
                 "Ne visi skaitļi nonāk aplī."),
            ],
            atbilde="6 - pārklājumā, 9 - pa labi, 10 - pa kreisi, 7 - ārpusē"),

    Ievadi("Kur liksi skaitli?", [
        {"jaut": "Pazīmes «dalās ar 2» un «dalās ar 3». Cik ir mazākais "
                 "skaitlis pārklājumā?",
         "atb": ["6"], "padoms": "2 un 3 mazākais kopīgais dalāmais."},
        {"jaut": "Cik skaitļu no 1 līdz 20 ir pārklājumā?", "atb": ["3"],
         "padoms": "6, 12, 18."},
        {"jaut": "Pazīmes «dalās ar 3» un «dalās ar 5». Kāds skaitlis ir "
                 "pārklājumā pirmais?",
         "atb": ["15"], "padoms": "3 · 5."},
        {"jaut": "Ar ko dalās visi skaitļi pārklājumā, ja pazīmes ir "
                 "«dalās ar 2» un «dalās ar 3»?",
         "atb": ["6"], "padoms": "Abas pazīmes reizē."},
        {"jaut": "Cik skaitļu no 1 līdz 20 dalās ar 2, bet ne ar 3?",
         "atb": ["7"], "padoms": "Desmit pāra skaitļu mīnus 6, 12 un 18."},
        {"jaut": "Cik skaitļu no 1 līdz 20 nedalās ne ar 2, ne ar 3?",
         "atb": ["7"], "padoms": "1, 5, 7, 11, 13, 17, 19."},
        {"jaut": "Pazīmes «dalās ar 4» un «dalās ar 6». Kāds skaitlis ir "
                 "pārklājumā pirmais?",
         "atb": ["12"], "padoms": "4 un 6 mazākais kopīgais dalāmais."},
        {"jaut": "Cik skaitļu no 1 līdz 20 dalās ar 3, bet ne ar 2?",
         "atb": ["3"], "padoms": "3, 9, 15."},
    ], pamats=4,
        ievads="Pārklājumā nonāk tikai tie, kam piemīt abas pazīmes."),

    Varianti("Ko diagramma parāda?", [
        {"jaut": "Ko nozīmē skaitlis pārklājumā?",
         "opcijas": ["Tam piemīt abas pazīmes",
                     "Tam piemīt viena pazīme",
                     "Tam nepiemīt neviena",
                     "Tas ir pirmskaitlis"],
         "pareizi": 0,
         "padoms": "Pārklājums ir «un»."},
        {"jaut": "Kur liek skaitli 7, ja pazīmes ir «dalās ar 2» un «dalās "
                 "ar 3»?",
         "opcijas": ["Ārpus abiem apļiem", "Pārklājumā", "Kreisajā aplī",
                     "Labajā aplī"],
         "pareizi": 0,
         "padoms": "7 nedalās ne ar 2, ne ar 3."},
        {"jaut": "Ar ko dalās visi pārklājuma skaitļi, ja pazīmes ir «dalās "
                 "ar 4» un «dalās ar 6»?",
         "opcijas": ["Ar 12", "Ar 24", "Ar 10", "Ar 2"],
         "pareizi": 0,
         "padoms": "4 un 6 mazākais kopīgais dalāmais."},
        {"jaut": "Kāpēc pārklājumā nekad nav skaitļu, ja pazīmes ir «dalās "
                 "ar 2» un «nedalās ar 2»?",
         "opcijas": ["Abas pazīmes reizē nav iespējamas",
                     "Jo skaitļu ir par maz",
                     "Jo pazīmes ir vienādas",
                     "Tur ir visi skaitļi"],
         "pareizi": 0,
         "padoms": "Viens skaitlis nevar būt gan pāra, gan nepāra."},
    ], pamats=4),

    Pasaule("Kuras dienas der abiem?",
            Ievadi("", [
                {"jaut": "Viens ceļotājs brauc ik pēc 2 dienām, otrs ik pēc "
                         "3. Kurā dienā abi brauks kopā pirmoreiz?",
                 "atb": ["6"], "padoms": "Pārklājuma pirmais skaitlis."},
                {"jaut": "Cik reižu 30 dienās abi brauks vienā dienā?",
                 "atb": ["5"], "padoms": "6, 12, 18, 24, 30."},
                {"jaut": "Cik dienās no 30 brauks tikai pirmais?",
                 "atb": ["10"], "padoms": "15 pāra dienas mīnus 5 kopīgās."},
                {"jaut": "Cik dienās no 30 nebrauks neviens?",
                 "atb": ["10"], "padoms": "Kāds brauc 20 dienās: "
                                          "15 + 10 − 5."},
            ]),
            pavediens="celojums",
            konteksts="Plānojot kopīgu braucienu, vispirms saliek blakus abu "
                      "brīvās dienas un skatās, kuras sakrīt.",
            kapec="Pārklājums ir tieši tās dienas, kas der abiem."),

    Kopsavilkums([
        "Grupēju skaitļus pēc dalāmības pazīmēm.",
        "Attēloju grupas Venna diagrammā.",
        "Zinu, ka pārklājums nozīmē abas pazīmes reizē.",
        "Pamanu, ka pārklājumā ir abu skaitļu kopīgie dalāmie.",
    ]),

    Majas([
        "Uzzīmē Venna diagrammu skaitļiem no 1 līdz 30 ar pazīmēm «dalās ar "
        "3» un «dalās ar 4».",
        "Saskaiti, cik skaitļu nonāca ārpus abiem apļiem.",
        "Izdomā divas pazīmes, kurām pārklājums ir tukšs.",
    ]),
]
