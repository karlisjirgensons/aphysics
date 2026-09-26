# -*- coding: utf-8 -*-
"""3. klase, 61. stunda: «Kā sadalīt darbu grupā?»

Grupu darbs te ir arī rēķins: cik cilvēku, cik uzdevumu katram, cik laika
kopā. Sadalīšana vienādās daļās - tas ir tas pats, ko mācījāmies 3.1. tematā,
tikai tagad dala darbu, nevis ābolus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kā sadalīt darbu grupā?"

MERKIS = ("Vienosimies grupā par pienākumiem un darba gaitu un izrēķināsim, "
          "cik darba tiek katram.")

SATURS = [
    Sakums("Kāpēc četri cilvēki nepaveic visu četras reizes ātrāk?",
           zimejums=restis([["pienākums", "kam"],
                            ["mēra sienas", "2 skolēni"],
                            ["pieraksta", "1 skolēns"],
                            ["zīmē", "1 skolēns"]],
                           "grupas pienākumi"),
           paraksts="Katram savs darbs - un neviens negaida savu kārtu.",
           fakti=["Darbu sadala pēc pienākumiem, ne tikai pēc skaita.",
                  "Daži darbi jādara pēc kārtas, citus var darīt reizē."]),

    Doma("Sadali darbu tā, lai visi strādā reizē",
         "Ja darbi ir neatkarīgi, tos var darīt vienlaikus - un kopējais "
         "laiks kļūst īsāks.",
         soli=[
             "Pieraksti visus darbus.",
             "Atzīmē, kurus var darīt reizē un kuriem jāgaida.",
             "Sadali reizē darāmos starp grupas dalībniekiem.",
             "Izrēķini, cik ilgi strādās katrs.",
         ],
         pieze="Zīmēšana nevar sākties, pirms nav mērījumu - tāpēc daži darbi "
               "vienmēr jādara pēc kārtas, lai cik liela būtu grupa."),

    Paraugs("Cik ilgi strādās grupa?",
            uzd="Jāizmēra 12 sienas. Grupā 4 skolēni, vienas sienas mērīšana "
                "aizņem 5 minūtes. Cik ilgi strādās grupa?",
            soli=[
                ("12 : 4 = 3",
                 "Katram jāizmēra trīs sienas."),
                ("3 · 5 = 15",
                 "Katrs strādās 15 minūtes."),
                ("Visi strādā reizē",
                 "Tāpēc grupa būs gatava pēc 15 minūtēm, nevis 60."),
            ],
            atbilde="15 minūtes"),

    Petijums("Vienojieties par pienākumiem",
             vajag="grupas plāna lapa",
             soli=[
                 "Sadaliet grupā četrus pienākumus: mērīt, pierakstīt, "
                 "rēķināt, zīmēt.",
                 "Pierakstiet, kurš ko dara.",
                 "Vienojieties, kurš darbs sākas pirmais.",
                 "Izrēķiniet, cik ilgi strādās katrs.",
             ],
             secinajums="Grupa ir gatava darbam tad, kad katrs zina ne tikai "
                        "savu daļu, bet arī to, kas notiek pirms un "
                        "pēc."),

    Ievadi("Sadali darbu", [
        {"jaut": "16 uzdevumi, 4 skolēni. Cik katram?", "atb": ["4"],
         "padoms": "16 : 4."},
        {"jaut": "24 mērījumi, 6 skolēni. Cik katram?", "atb": ["4"],
         "padoms": "24 : 6."},
        {"jaut": "Katrs mērījums 3 minūtes. Cik minūšu strādās viens?",
         "atb": ["12"], "padoms": "4 · 3."},
        {"jaut": "18 telpas, 3 grupas. Cik telpu vienai grupai?",
         "atb": ["6"], "padoms": "18 : 3."},
        {"jaut": "Grupā 5 skolēni, katram 7 uzdevumi. Cik uzdevumu kopā?",
         "atb": ["35"], "padoms": "5 · 7."},
        {"jaut": "20 uzdevumi, 6 skolēni. Cik uzdevumu paliks pāri, ja "
                 "katrs paņem 3?",
         "atb": ["2"], "padoms": "6 · 3 = 18; 20 − 18."},
    ], pamats=4),

    Zimejums("Pēc kārtas vai reizē",
             restis([["darbs", "kad"],
                     ["mērīt", "vispirms"],
                     ["pierakstīt", "reizē ar mērīšanu"],
                     ["rēķināt", "pēc mērīšanas"],
                     ["zīmēt", "pēdējais"]],
                    "darba gaita"),
             paskaidro="Divus darbus var darīt reizē, divi jādara pēc kārtas - "
                       "tāpēc grupa nevar būt gatava uzreiz.",
             ievads="Tā izskatās darba gaita."),

    Varianti("Kā sadalīt gudri?", [
        {"jaut": "Kurus darbus var darīt reizē?",
         "opcijas": ["Mērīt un pierakstīt", "Mērīt un zīmēt",
                     "Zīmēt un rēķināt", "Visus"],
         "pareizi": 0, "padoms": "Zīmēšanai vajag jau gatavus skaitļus."},
        {"jaut": "20 uzdevumi, 5 skolēni. Cik katram?",
         "opcijas": ["4", "5", "25", "15"],
         "pareizi": 0, "padoms": "20 : 5."},
        {"jaut": "Kāpēc kopējais laiks nav skolēnu laiku summa?",
         "opcijas": ["Jo visi strādā reizē", "Jo daži nestrādā",
                     "Jo darbs ir viegls", "Jo laiks ir īss"],
         "pareizi": 0, "padoms": "Vienlaicīgs darbs laiku nesaskaita."},
        {"jaut": "Ko dara, ja uzdevumi nedalās vienādi?",
         "opcijas": ["Atlikušos sadala pa vienam", "Atmet lieko",
                     "Visu dara viens", "Neko"],
         "pareizi": 0, "padoms": "Atlikums arī jāizdara."},
    ], pamats=4),

    Pasaule("Kā strādā skolas dežuranti?",
            Ievadi("", [
                {"jaut": "Skolā 15 gaiteņi, dežurē 5 klases. Cik gaiteņu "
                         "vienai klasei?",
                 "atb": ["3"], "padoms": "15 : 5."},
                {"jaut": "Vienā klasē 24 skolēni, dežurē 6 reizē. Cik "
                         "grupas sanāk?",
                 "atb": ["4"], "padoms": "24 : 6."},
                {"jaut": "Katra grupa dežurē vienu nedēļu. Cik nedēļu "
                         "pietiks visām grupām?",
                 "atb": ["4"], "padoms": "Viena nedēļa katrai."},
                {"jaut": "Cik dienu tas ir, ja nedēļā dežurē 5 dienas?",
                 "atb": ["20"], "padoms": "4 · 5."},
            ]),
            pavediens="skola",
            konteksts="Dežūru grafiks ir tas pats dalīšanas uzdevums - tikai "
                      "dala laiku un cilvēkus.",
            kapec="Taisnīgs grafiks ir tāds, kurā visiem iznāk vienāds "
                  "skaits."),

    Kopsavilkums([
        "Vienojos grupā par pienākumiem un darba gaitu.",
        "Izrēķinu, cik darba tiek katram.",
        "Atšķiru darbus, ko var darīt reizē, no tiem, kas jādara pēc kārtas.",
        "Zinu, ka kopējais laiks nav visu dalībnieku laiku summa.",
    ]),

    Majas([
        "Sadali mājas darbus starp ģimenes locekļiem un pieraksti grafiku.",
        "Izrēķini, cik minūšu strādās katrs.",
        "Pastāsti, kuri darbi jādara pēc kārtas.",
    ]),
]
