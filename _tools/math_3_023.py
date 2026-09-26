# -*- coding: utf-8 -*-
"""3. klase, 23. stunda: «Kāds uzdevums der šai darbībai?»

Apgrieztais virziens: nevis no teksta uz rēķinu, bet no rēķina uz tekstu. Kas
prot izdomāt uzdevumu, tas ir sapratis darbības jēgu - un tieši to šī stunda
prasa, nevis vēl vienu aprēķinu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kāds uzdevums der šai darbībai?"

MERKIS = ("Izdomāsim situāciju, kas atbilst dotai reizināšanas vai dalīšanas "
          "darbībai, un izvērtēsim citu izdomāto.")

SATURS = [
    Sakums("Kāds stāsts slēpjas aiz rēķina 6 · 8?",
           zimejums=restis([["6 · 8 = 48"],
                            ["6 kastes pa 8 olām"],
                            ["6 rindas pa 8 rūtiņām"],
                            ["6 dienas pa 8 lapām"]],
                           "viens rēķins - daudz stāstu"),
           paraksts="Viens un tas pats rēķins der ļoti dažādām situācijām.",
           fakti=["Rēķins pasaka darbību, bet ne to, par ko ir stāsts.",
                  "Labs uzdevums nosauc, kas ir grupa un kas - grupas "
                  "lielums."]),

    Doma("Labā uzdevumā ir trīs lietas",
         "Kas tiek skaitīts, cik ir grupu un kas tiek jautāts - bez kādas no "
         "tām uzdevuma nav.",
         soli=[
             "Izvēlies, par ko būs stāsts: par naudu, ēdienu vai ceļu.",
             "Pasaki, cik ir grupu un cik liela ir viena grupa.",
             "Uzdod jautājumu, uz kuru atbild tieši šis rēķins.",
             "Pārbaudi, vai atbilde sanāk tāda, kāda bija iecerēta.",
         ],
         pieze="Ja uz uzdevumu var atbildēt ar citu darbību, tas vēl nav "
               "slikti - bet tad pārraksti to tā, lai derētu tikai viena."),

    Paraugs("Izdomā uzdevumu darbībai 42 : 7",
            uzd="Uzraksti situāciju, kurā jāizrēķina 42 : 7.",
            soli=[
                ("42 ir kopskaits, 7 - daļu skaits",
                 "Vispirms izlemj, ko nozīmēs abi skaitļi."),
                ("«Klasē ir 42 burtnīcas un 7 plaukti.»",
                 "Situācija, kurā abi skaitļi ir dabiski."),
                ("«Cik burtnīcu būs vienā plauktā, ja tās saliek pa vienādi?»",
                 "Jautājums, uz kuru atbild tieši dalīšana."),
            ],
            atbilde="42 : 7 = 6 burtnīcas plauktā"),

    Ievadi("Atrodi rēķinu uzdevumam", [
        {"jaut": "«8 grozi, katrā 7 āboli. Cik ābolu kopā?» Cik ir atbilde?",
         "atb": ["56"], "padoms": "8 · 7."},
        {"jaut": "«56 āboli, 8 grozi. Cik ābolu vienā grozā?» Cik ir "
                 "atbilde?",
         "atb": ["7"], "padoms": "56 : 8."},
        {"jaut": "«54 lapas, pa 9 katram. Cik bērnu?» Cik ir atbilde?",
         "atb": ["6"], "padoms": "54 : 9."},
        {"jaut": "«6 somas, katrā 9 grāmatas. Cik grāmatu?» Cik ir atbilde?",
         "atb": ["54"], "padoms": "6 · 9."},
        {"jaut": "«36 konfektes, 4 bērni. Cik katram?» Cik ir atbilde?",
         "atb": ["9"], "padoms": "36 : 4."},
        {"jaut": "«4 maisiņi pa 9 konfektēm. Cik kopā?» Cik ir atbilde?",
         "atb": ["36"], "padoms": "4 · 9."},
    ], pamats=4),

    Petijums("Uzraksti uzdevumu un iedod to draugam",
             vajag="lapa un zīmulis",
             soli=[
                 "Izvēlies vienu rēķinu: 7 · 6, 48 : 8 vai 9 · 5.",
                 "Uzraksti situāciju, kurā šis rēķins ir vajadzīgs.",
                 "Iedod uzdevumu klasesbiedram, nerādot rēķinu.",
                 "Pārbaudi, vai viņš izmantoja tieši to darbību, ko tu "
                 "domāji.",
             ],
             secinajums="Ja klasesbiedrs izvēlējās citu darbību, uzdevuma "
                        "tekstā kaut kas nebija pateikts skaidri."),

    Zimejums("Kas uzdevumā ir jāpasaka",
             restis([["kas", "cik grupu", "cik katrā", "jautājums"],
                     ["āboli", "8 grozi", "7 grozā", "cik kopā?"]],
                    "uzdevuma četras daļas"),
             paskaidro="Ja kāda aile ir tukša, uzdevumu atrisināt nevar.",
             ievads="Pārbaudi savu uzdevumu pēc šīs tabulas."),

    Varianti("Vai uzdevums ir labs?", [
        {"jaut": "«Veikalā ir 7 kastes. Cik olu ir kopā?» Kas pietrūkst?",
         "opcijas": ["Cik olu ir vienā kastē", "Cik maksā ola",
                     "Kāda ir veikala adrese", "Nekas nepietrūkst"],
         "pareizi": 0, "padoms": "Nav zināms grupas lielums."},
        {"jaut": "Kurš uzdevums atbilst rēķinam 45 : 9?",
         "opcijas": ["45 lapas sadala 9 bērniem",
                     "9 bērniem pa 45 lapām",
                     "45 lapas un vēl 9 lapas",
                     "45 reizes pa 9 lapām"],
         "pareizi": 0, "padoms": "Kopskaitu dala ar bērnu skaitu."},
        {"jaut": "Kurš uzdevums atbilst rēķinam 6 · 9?",
         "opcijas": ["6 kastes pa 9 zīmuļiem",
                     "6 zīmuļi no 9", "9 zīmuļi mazāk nekā 6",
                     "9 zīmuļi sadalīti 6 bērniem"],
         "pareizi": 0, "padoms": "Grupu skaits reiz grupas lielums."},
        {"jaut": "Ko vienmēr jāpasaka uzdevuma beigās?",
         "opcijas": ["Jautājumu", "Atbildi", "Rēķinu", "Pārbaudi"],
         "pareizi": 0, "padoms": "Bez jautājuma uzdevuma nav."},
    ], pamats=4),

    Pasaule("Uzraksti uzdevumu par veikalu",
            Ievadi("", [
                {"jaut": "«7 paciņas pa 8 cepumiem. Cik cepumu kopā?»",
                 "atb": ["56"], "padoms": "7 · 8."},
                {"jaut": "«56 cepumi, 7 paciņas. Cik cepumu vienā paciņā?»",
                 "atb": ["8"], "padoms": "56 : 7."},
                {"jaut": "«63 cepumi, pa 9 katrā paciņā. Cik paciņu?»",
                 "atb": ["7"], "padoms": "63 : 9."},
                {"jaut": "«9 paciņas pa 7 cepumiem. Cik cepumu kopā?»",
                 "atb": ["63"], "padoms": "9 · 7."},
            ]),
            pavediens="veikals",
            konteksts="Visi četri uzdevumi ir par vienu un to pašu preci - "
                      "atšķiras tikai tas, kas ir zināms.",
            kapec="Kad proti uzrakstīt uzdevumu, proti arī to atrisināt."),

    Kopsavilkums([
        "Izdomāju situāciju, kas atbilst dotai darbībai.",
        "Uzdevumā nosaucu, kas tiek skaitīts, cik ir grupu un kas tiek "
        "jautāts.",
        "Izvērtēju klasesbiedra uzdevumu un pasaku, kā to uzlabot.",
        "Atpazīstu, kura darbība slēpjas aiz teksta.",
    ]),

    Majas([
        "Uzraksti divus uzdevumus: vienu ar reizināšanu, otru ar dalīšanu.",
        "Iedod tos kādam mājās un pārbaudi, vai atbilde sakrita.",
        "Pārraksti uzdevumu, ja atbilde nesakrita.",
    ]),
]
