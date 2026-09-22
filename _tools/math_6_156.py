# -*- coding: utf-8 -*-
"""6. klase, 156. stunda: «Kā sagrupēt skaitļus?»

Šķirošanas uzdevums. Skaitļus sadala pa kopām, un tas prasa zināt gan katras
kopas definīciju, gan to, ka kopas pārklājas. Venna diagramma te ir īstajā
vietā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         venna)

TEMA = "Kā sagrupēt skaitļus?"

MERKIS = ("Sagrupēsim skaitļus pēc to veida un pamatosim katra vietu.")

SATURS = [
    Sakums("Viens skaitlis var būt vairākās kopās",
           zimejums=venna([-5, -1], [], [1, 2, 3],
                          ("veselie", "naturālie")),
           paraksts="Naturālie skaitļi pilnībā ietilpst veselajos - tāpēc "
                    "viena kopa ir otras iekšpusē.",
           fakti=["Naturālie ietilpst veselajos.",
                  "Veselie ietilpst racionālajos.",
                  "Daļa, kas nav vesela, paliek tikai racionālajos."]),

    Doma("Sāc ar šaurāko kopu",
         "Skaitļus grupē, sākot ar šaurāko kopu: vispirms naturālie, tad "
         "veselie, tad pārējie racionālie.",
         soli=[
             "Pārbaudi, vai skaitlis ir naturāls.",
             "Ja nav, pārbaudi, vai tas ir vesels.",
             "Ja nav, pārbaudi, vai to var uzrakstīt kā daļu.",
             "Pieraksti skaitli visās kopās, kurām tas pieder.",
             "Pārbaudi, vai neviens skaitlis nav palicis bez kopas.",
         ],
         pieze="Nulle ir vesels skaitlis, bet nav naturāls - to bieži "
               "aizmirst. Un negatīvs vesels skaitlis, piemēram −5, ir gan "
               "vesels, gan racionāls."),

    Paraugs("Sagrupē sešus skaitļus",
            uzd="Sagrupē: 3; −5; 0; {2|3}; −0,5; 12.",
            soli=[
                ("Naturālie: 3 un 12",
                 "Pozitīvi veseli."),
                ("Veselie: 3; −5; 0; 12",
                 "Arī naturālie un nulle."),
                ("Tikai racionālie: {2|3} un −0,5",
                 "Nav veseli."),
                ("Visi seši ir racionāli",
                 "Katru var uzrakstīt kā daļu."),
            ],
            atbilde="2 naturāli, 4 veseli, visi 6 racionāli"),

    Ievadi("Saskaiti pa kopām", [
        {"jaut": "Skaitļi 3; −5; 0; {2|3}; −0,5; 12. Cik ir naturālo?",
         "atb": ["2"], "padoms": "3 un 12."},
        {"jaut": "Cik no tiem ir veseli?",
         "atb": ["4"], "padoms": "3; −5; 0; 12."},
        {"jaut": "Cik no tiem ir racionāli?",
         "atb": ["6"], "padoms": "Visi."},
        {"jaut": "Cik no tiem nav veseli?",
         "atb": ["2"], "padoms": "{2|3} un −0,5."},
        {"jaut": "Vai 0 ir naturāls skaitlis? Raksti «jā» vai «nē».",
         "atb": ["nē", "ne"], "padoms": "Naturālie sākas ar 1."},
        {"jaut": "Vai −5 ir racionāls skaitlis?",
         "atb": ["jā", "ja"], "padoms": "{−5|1}."},
    ], pamats=4),

    Petijums("Sašķiro savus skaitļus",
             vajag="burtnīca",
             soli=[
                 "Pieraksti astoņus dažādus skaitļus.",
                 "Uzzīmē divus pārklājošos apļus: veselie un naturālie.",
                 "Ieraksti katru skaitli tā vietā.",
                 "Skaitļus, kas nav veseli, raksti ārpus abiem apļiem.",
                 "Pārbaudi, vai neviens skaitlis nav palicis bez vietas.",
             ],
             secinajums="Naturālo apļis pilnībā atrodas veselo apļa "
                        "iekšpusē - tāpēc tie nekad nepārklājas daļēji."),

    Varianti("Kurai kopai pieder?", [
        {"jaut": "Skaitlis −7 ir...",
         "opcijas": ["vesels un racionāls", "naturāls",
                     "tikai racionāls", "neviens no tiem"],
         "pareizi": 0,
         "padoms": "Negatīvs vesels."},
        {"jaut": "Skaitlis {3|5} ir...",
         "opcijas": ["tikai racionāls", "vesels",
                     "naturāls", "neviens no tiem"],
         "pareizi": 0,
         "padoms": "Nav vesels."},
        {"jaut": "Skaitlis 0 ir...",
         "opcijas": ["vesels, bet ne naturāls", "naturāls",
                     "tikai racionāls", "neviens no tiem"],
         "pareizi": 0,
         "padoms": "Naturālie sākas ar 1."},
        {"jaut": "Kura kopa ir visplašākā?",
         "opcijas": ["racionālie", "veselie", "naturālie", "visas vienādas"],
         "pareizi": 0,
         "padoms": "Tā ietver pārējās."},
    ], pamats=4),

    Pasaule("Kādi skaitļi ir datos?",
            Ievadi("", [
                {"jaut": "Dati: 25 skolēni; −3 °C; 1,75 m; 0 punkti. Cik no "
                         "tiem ir naturāli?",
                 "atb": ["1"], "padoms": "Tikai 25."},
                {"jaut": "Cik no tiem ir veseli?",
                 "atb": ["3"], "padoms": "25; −3; 0."},
                {"jaut": "Cik no tiem ir racionāli?",
                 "atb": ["4"], "padoms": "Visi."},
                {"jaut": "Cik no tiem nav veseli?",
                 "atb": ["1"], "padoms": "1,75."},
            ]),
            pavediens="skola",
            konteksts="Vienā datu tabulā parasti ir visu veidu skaitļi - un "
                      "katram lielumam savs veids.",
            kapec="Skaitļa veids pasaka, kādas vērtības vispār iespējamas."),

    Zimejums("Trīs kopas, viena otrā",
             venna([-5, 0], [], [1, 2],
                   ("veselie", "naturālie")),
             paskaidro="Naturālie ir veselo iekšpusē. Ārpus abiem apļiem "
                       "paliek daļas un decimāldaļas.",
             ievads="Kopas neatrodas blakus - tās ir viena otrā."),

    Kopsavilkums([
        "Sagrupēju skaitļus pēc to veida.",
        "Sāku ar šaurāko kopu un eju uz plašāko.",
        "Zinu, ka viens skaitlis var piederēt vairākām kopām.",
        "Pamatoju katra skaitļa vietu.",
    ]),

    Majas([
        "Sagrupē skaitļus 8; −2; 0; 0,5; {1|3}; 100.",
        "Uzzīmē divus pārklājošos apļus un ieraksti tos.",
        "Pieraksti, cik skaitļu palika ārpus abiem apļiem.",
    ]),
]
