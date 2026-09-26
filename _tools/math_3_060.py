# -*- coding: utf-8 -*-
"""3. klase, 60. stunda: «Kādas prasmes mums vēl trūkst?»

Praktiskā darba plānošana. Skolēni jau zina, kas ir plāns; tagad viņi
saskaita, ko prot un ko ne - lielus skaitļus, mērīšanu, dalīšanu ar 10 un
100. Tieši no šī saraksta aug nākamo stundu kārtība.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kādas prasmes mums vēl trūkst?"

MERKIS = ("Veidosim darbības plānu klases attēlošanai un noteiksim, kādas "
          "prasmes vēl vajadzīgas.")

SATURS = [
    Sakums("Ko vajag zināt, lai uzzīmētu klases plānu?",
           zimejums=restis([["1.", "izmērīt telpu"],
                            ["2.", "izteikt metrus centimetros"],
                            ["3.", "dalīt ar 10 un 100"],
                            ["4.", "uzzīmēt mērogā"]],
                           "četras prasmes"),
           paraksts="Divas no tām mēs vēl neprotam - tāpēc tās mācīsimies.",
           fakti=["Praktisks darbs sākas ar sarakstu, kas jāprot.",
                  "Trūkstošās prasmes apgūst pirms darba, ne tā laikā."]),

    Doma("Vispirms saraksts, tad darbs",
         "Uzraksti visus soļus un pretī katram - vai to jau proti.",
         soli=[
             "Pieraksti visus darba soļus pēc kārtas.",
             "Pretī katram atzīmē: «protu» vai «vēl ne».",
             "Atzīmētās prasmes sakārto tādā secībā, kādā tās vajadzēs.",
             "Nosaki, cik stundu vajadzēs katrai.",
         ],
         pieze="Ja kāda prasme pietrūkst darba vidū, viss darbs apstājas - "
               "tāpēc saraksts ir svarīgāks par sākumu."),

    Paraugs("Cik stundu vajadzēs darbam?",
            uzd="Darbā ir 4 soļi. Diviem vajag pa 1 stundai, diviem pa 2. "
                "Cik stundu vajadzēs kopā?",
            soli=[
                ("2 · 1 = 2",
                 "Divi īsie soļi."),
                ("2 · 2 = 4",
                 "Divi garie soļi."),
                ("2 + 4 = 6",
                 "Kopā sešas stundas."),
            ],
            atbilde="6 stundas"),

    Petijums("Uztaisi klases darba plānu",
             vajag="lapa un zīmulis",
             soli=[
                 "Pieraksti, ko vajag izdarīt, lai taptu klases plāns.",
                 "Atzīmē, kuras prasmes jau ir un kuras vēl nav.",
                 "Sadali soļus pa stundām.",
                 "Vienojieties klasē par kopīgu sarakstu.",
             ],
             secinajums="Plāns ir gatavs tad, kad katram solim ir gan "
                        "izpildītājs, gan laiks."),

    Ievadi("Saplāno darbu", [
        {"jaut": "Darbā 6 soļi, katram 2 stundas. Cik stundu kopā?",
         "atb": ["12"], "padoms": "6 · 2."},
        {"jaut": "Ir 8 stundas, katram solim 2. Cik soļu var paspēt?",
         "atb": ["4"], "padoms": "8 : 2."},
        {"jaut": "Klasē 24 skolēni, 4 grupas. Cik skolēnu vienā grupā?",
         "atb": ["6"], "padoms": "24 : 4."},
        {"jaut": "Katrai grupai jāizmēra 3 sienas. Cik sienu izmēra 4 grupas?",
         "atb": ["12"], "padoms": "4 · 3."},
        {"jaut": "Vienas sienas mērīšana aizņem 5 minūtes. Cik minūšu "
                 "aizņems 3 sienas?",
         "atb": ["15"], "padoms": "3 · 5."},
        {"jaut": "Stundā ir 40 minūtes. Cik minūšu paliks pāri?",
         "atb": ["25"], "padoms": "40 − 15."},
    ], pamats=4),

    Zimejums("Prasmju saraksts",
             restis([["prasme", "protu?"],
                     ["mērīt ar mērlenti", "jā"],
                     ["lasīt skaitļus līdz 1000", "vēl ne"],
                     ["dalīt ar 10 un 100", "vēl ne"],
                     ["zīmēt taisnstūri", "jā"]],
                    "ko mācāmies tālāk"),
             paskaidro="Divas atzīmētās prasmes ir tieši nākamo stundu "
                       "temats.",
             ievads="Tā izskatās aizpildīts saraksts."),

    Varianti("Kā plānot darbu?", [
        {"jaut": "Ko dara vispirms?",
         "opcijas": ["Pieraksta visus soļus", "Sāk mērīt",
                     "Zīmē plānu", "Izvēlas krāsas"],
         "pareizi": 0, "padoms": "Vispirms saraksts."},
        {"jaut": "Ko nozīmē atzīme «vēl ne» pie prasmes?",
         "opcijas": ["To vajag apgūt pirms darba", "To var izlaist",
                     "To izdarīs skolotājs", "Tā nav svarīga"],
         "pareizi": 0, "padoms": "Bez tās darbs apstāsies."},
        {"jaut": "Kas plānā jāpieraksta katram solim?",
         "opcijas": ["Izpildītājs un laiks", "Tikai nosaukums",
                     "Tikai laiks", "Nekas"],
         "pareizi": 0, "padoms": "Citādi solis paliks neizdarīts."},
        {"jaut": "Darbā 5 soļi pa 2 stundām. Cik stundu vajag?",
         "opcijas": ["10", "7", "3", "25"],
         "pareizi": 0, "padoms": "5 · 2."},
    ], pamats=4),

    Pasaule("Kā sadalīt skolas plāna zīmēšanu?",
            Ievadi("", [
                {"jaut": "Skolā ir 12 telpas, klasē 4 grupas. Cik telpu "
                         "vienai grupai?",
                 "atb": ["3"], "padoms": "12 : 4."},
                {"jaut": "Vienas telpas mērīšana aizņem 10 minūtes. Cik "
                         "minūšu vajag vienai grupai?",
                 "atb": ["30"], "padoms": "3 · 10."},
                {"jaut": "Cik minūšu kopā strādās visas četras grupas?",
                 "atb": ["120"], "padoms": "4 · 30."},
                {"jaut": "Cik stundu tas ir, ja stundā ir 60 minūtes?",
                 "atb": ["2"], "padoms": "120 : 60."},
            ]),
            pavediens="skola",
            konteksts="Kad darbu sadala grupās, katra strādā reizē - tāpēc "
                      "kopējais laiks ir īsāks.",
            kapec="Plāns pasaka, vai darbs vispār ietilps stundās, kas ir."),

    Kopsavilkums([
        "Veidoju darba plānu ar soļiem un laiku.",
        "Atzīmēju, kuras prasmes jau ir un kuras vēl jāapgūst.",
        "Izrēķinu, cik laika prasīs viss darbs.",
        "Sadalu darbu grupās.",
    ]),

    Majas([
        "Uzraksti plānu kādam mājas darbam ar trim soļiem.",
        "Pieraksti pie katra soļa, cik minūšu tas prasīs.",
        "Izrēķini kopējo laiku un pārbaudi, vai tas sakrita.",
    ]),
]
