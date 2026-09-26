# -*- coding: utf-8 -*-
"""3. klase, 44. stunda: «Cik izteiksmes var izveidot no trim skaitļiem?»

Atvērts uzdevums: no trim skaitļiem, četrām zīmēm un iekavām veido pēc
iespējas vairāk izteiksmju. Te nav vienas atbildes, bet ir sistēma - un tieši
sistēmu skolēns mācās, jo bez tās daži varianti vienmēr paliek neatrasti.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Cik izteiksmes var izveidot no trim skaitļiem?"

MERKIS = ("Veidosim pēc iespējas vairāk dažādu izteiksmju no dotiem "
          "skaitļiem, zīmēm un iekavām.")

SATURS = [
    Sakums("Cik dažādus rēķinus var salikt no 2, 3 un 4?",
           zimejums=restis([["2 + 3 · 4", "= 14"],
                            ["(2 + 3) · 4", "= 20"],
                            ["2 · 3 + 4", "= 10"],
                            ["2 · (3 + 4)", "= 14"]],
                           "četras no daudzām"),
           paraksts="Tie paši trīs skaitļi - un pavisam dažādas vērtības.",
           fakti=["Zīmes var izvēlēties četras, un iekavas - vairākās vietās.",
                  "Tāpēc izteiksmju ir daudz vairāk, nekā liekas."]),

    Doma("Meklē pēc sistēmas, ne pēc nejaušības",
         "Vispirms visas izteiksmes bez iekavām, tad visas ar iekavām - tā "
         "neviena nepaliek neatrasta.",
         soli=[
             "Pieraksti skaitļus vienā secībā: 2, 3, 4.",
             "Izmēģini visas zīmju kombinācijas bez iekavām.",
             "Tad ieliec iekavas ap pirmajiem diviem skaitļiem.",
             "Tad ap pēdējiem diviem.",
             "Aprēķini katras izteiksmes vērtību.",
         ],
         pieze="Dažas izteiksmes dod vienu un to pašu vērtību: 2 + 3 · 4 un "
               "2 · (3 + 4) abas ir 14. Izteiksmes ir dažādas, vērtība - "
               "viena."),

    Paraugs("Cik izteiksmju bez iekavām ar zīmēm + un ·?",
            uzd="No skaitļiem 2, 3 un 4 (šajā secībā) veido izteiksmes ar "
                "zīmēm + un ·, neliekot iekavas.",
            soli=[
                ("2 + 3 + 4 = 9",
                 "Abas zīmes ir saskaitīšana."),
                ("2 + 3 · 4 = 14",
                 "Otrā zīme ir reizināšana."),
                ("2 · 3 + 4 = 10",
                 "Pirmā zīme ir reizināšana."),
                ("2 · 3 · 4 = 24",
                 "Abas zīmes ir reizināšana."),
            ],
            atbilde="četras izteiksmes: 9, 14, 10 un 24"),

    Petijums("Atrodi visas izteiksmes",
             vajag="lapa un zīmulis",
             soli=[
                 "Uzraksti skaitļus 3, 4 un 5 vienā secībā.",
                 "Pieraksti visas izteiksmes ar + un · bez iekavām.",
                 "Pieraksti tās pašas ar iekavām ap pirmajiem diviem.",
                 "Aprēķini katras vērtību un sakārto tās augošā secībā.",
             ],
             secinajums="Ja strādā pēc sistēmas, neviena izteiksme nepaliek "
                        "aizmirsta - un beigās var pateikt, cik to ir."),

    Ievadi("Aprēķini izteiksmes", [
        {"jaut": "2 + 3 + 4 = ?", "atb": ["9"], "padoms": "Pa kārtai."},
        {"jaut": "2 + 3 · 4 = ?", "atb": ["14"], "padoms": "Vispirms 3 · 4."},
        {"jaut": "(2 + 3) · 4 = ?", "atb": ["20"], "padoms": "5 · 4."},
        {"jaut": "2 · (3 + 4) = ?", "atb": ["14"], "padoms": "2 · 7."},
        {"jaut": "2 · 3 · 4 = ?", "atb": ["24"], "padoms": "6 · 4."},
        {"jaut": "(2 · 3) + 4 = ?", "atb": ["10"], "padoms": "6 + 4."},
    ], pamats=4),

    Zimejums("Sistēma, pēc kuras meklēt",
             restis([["bez iekavām", "a + b + c", "a + b · c", "a · b + c",
                      "a · b · c"],
                     ["ar iekavām", "(a + b) · c", "a · (b + c)", "", ""]],
                    "meklēšanas kārtība"),
             paskaidro="Vispirms visa pirmā rinda, tad otrā - tā nekas "
                       "neaizmirstas.",
             ievads="Tā izskatās sistēmiska meklēšana."),

    Varianti("Kura izteiksme dod lielāko vērtību?", [
        {"jaut": "Kura no šīm ir lielākā?",
         "opcijas": ["2 · 3 · 4", "(2 + 3) · 4", "2 + 3 · 4", "2 + 3 + 4"],
         "pareizi": 0, "padoms": "24, 20, 14 un 9."},
        {"jaut": "Kuras divas izteiksmes dod vienu un to pašu vērtību?",
         "opcijas": ["2 + 3 · 4 un 2 · (3 + 4)", "2 + 3 + 4 un 2 · 3 + 4",
                     "(2 + 3) · 4 un 2 · 3 · 4", "Nevienas"],
         "pareizi": 0, "padoms": "Abas dod 14."},
        {"jaut": "Cik izteiksmju bez iekavām var izveidot no trim skaitļiem "
                 "ar zīmēm + un ·?",
         "opcijas": ["4", "2", "6", "8"],
         "pareizi": 0, "padoms": "Divas zīmes, katrai divas izvēles."},
        {"jaut": "Kāpēc jāstrādā pēc sistēmas?",
         "opcijas": ["Lai neviens variants nepaliktu neatrasts",
                     "Lai būtu ātrāk", "Tā prasa skolotājs",
                     "Lai atbilde būtu skaistāka"],
         "pareizi": 0, "padoms": "Nejauši meklējot, kaut kas vienmēr paliek."},
    ], pamats=4),

    Pasaule("Cik dažādu paroļu var izveidot?",
            Ievadi("", [
                {"jaut": "Parolei jāizvēlas viens no 3 burtiem un viens no 4 "
                         "cipariem. Cik variantu?",
                 "atb": ["12"], "padoms": "3 · 4."},
                {"jaut": "Ja burtu ir 5, cik variantu?",
                 "atb": ["20"], "padoms": "5 · 4."},
                {"jaut": "Ja pievieno vēl vienu izvēli no 2 zīmēm, cik "
                         "variantu ir 5 burtiem un 4 cipariem?",
                 "atb": ["40"], "padoms": "20 · 2."},
                {"jaut": "Cik variantu ir 2 burtiem, 3 cipariem un 2 zīmēm?",
                 "atb": ["12"], "padoms": "2 · 3 · 2."},
            ]),
            pavediens="dati",
            konteksts="Paroļu skaitu rēķina tieši tāpat kā izteiksmju "
                      "skaitu: reizina izvēļu skaitu katrā vietā.",
            kapec="Tāpēc gara parole ir daudz drošāka nekā īsa."),

    Kopsavilkums([
        "Veidoju dažādas izteiksmes no dotiem skaitļiem un zīmēm.",
        "Strādāju pēc sistēmas: vispirms bez iekavām, tad ar tām.",
        "Aprēķinu katras izteiksmes vērtību.",
        "Zinu, ka dažādas izteiksmes var dot vienu un to pašu vērtību.",
    ]),

    Majas([
        "Izveido visas izteiksmes no skaitļiem 1, 5 un 6.",
        "Atrodi, kura no tām dod vislielāko vērtību.",
        "Pameklē divas izteiksmes ar vienādu vērtību.",
    ]),
]
