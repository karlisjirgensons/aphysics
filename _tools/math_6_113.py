# -*- coding: utf-8 -*-
"""6. klase, 113. stunda: «Kā attēlot temperatūras izmaiņas?»

No tabulas uz grafiku. Šī ir pirmā stunda, kurā skolēns pats pārnes datus uz
plakni - un uzreiz ar negatīvām vērtībām, tāpēc punkti nonāk zem ass. Pēc
zīmēšanas grafiks jāizstāsta vārdiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         plakne, restis)

TEMA = "Kā attēlot temperatūras izmaiņas?"

MERKIS = ("Attēlosim tabulā dotos temperatūras datus koordinātu plaknē un "
          "skaidrosim grafiku.")

SATURS = [
    Sakums("Tabula un grafiks stāsta vienu stāstu",
           zimejums=restis([["h", "0", "3", "6", "9", "12"],
                            ["°C", "−5", "−3", "0", "3", "4"]]),
           paraksts="Pieci mērījumi. Katra kolonna kļūs par vienu punktu "
                    "koordinātu plaknē.",
           fakti=["Katra tabulas kolonna ir viens punkts.",
                  "Pirmā rinda nonāk uz horizontālās ass.",
                  "Punktus savieno ar līniju tikai tad, ja starp tiem "
                  "lielums mainās vienmērīgi."]),

    Doma("Kolonna kļūst par punktu",
         "Tabulā dotos datus attēlo plaknē, katru kolonnu pārvēršot par "
         "punktu: pirmā rinda dod x, otrā - y.",
         soli=[
             "Atrodi datu diapazonu un izvēlies vienības.",
             "Iekārto plakni ar abām asīm.",
             "Katrai kolonnai atzīmē punktu.",
             "Savieno punktus, ja starp mērījumiem lielums mainās "
             "pakāpeniski.",
             "Izstāsti grafiku vārdiem.",
         ],
         pieze="Temperatūra starp mērījumiem mainās pakāpeniski, tāpēc "
               "punktus savieno. Skolēnu skaitu klasēs nesavieno - starp "
               "divām klasēm nav «pusklases»."),

    Paraugs("No tabulas uz grafiku",
            uzd="Attēlo grafikā: 0 h → −5 °C; 3 h → −3 °C; 6 h → 0 °C; "
                "9 h → 3 °C; 12 h → 4 °C.",
            soli=[
                ("Diapazons: no −5 līdz 4",
                 "Vertikālajā asī vajag arī negatīvo daļu."),
                ("Punkti: (0; −5), (3; −3), (6; 0)",
                 "Pirmie trīs."),
                ("Punkti: (9; 3), (12; 4)",
                 "Pēdējie divi."),
                ("Savieno punktus ar līniju",
                 "Temperatūra mainās pakāpeniski."),
                ("Grafiks šķērso asi pie 6 h",
                 "Tur temperatūra kļūst pozitīva."),
            ],
            atbilde="līnija no (0; −5) uz (12; 4)"),

    Ievadi("Nolasi no grafika", [
        {"jaut": "Cik grādu ir pie 0 h?",
         "atb": ["-5", "−5"], "padoms": "Punkts (0; −5).",
         "zim": plakne(lauzta=[(0, -5), (3, -3), (6, 0), (9, 3), (12, 4)],
                       no_x=0, lidz_x=12, no_y=-6, lidz_y=6, solis=3,
                       x_nos="h", y_nos="°C")},
        {"jaut": "Pie kuras stundas temperatūra ir 0 °C?",
         "atb": ["6"], "padoms": "Tur grafiks šķērso asi."},
        {"jaut": "Cik grādu ir pie 9 h?",
         "atb": ["3"], "padoms": "Punkts (9; 3)."},
        {"jaut": "Par cik grādiem temperatūra pieauga no 0 h līdz 6 h?",
         "atb": ["5"], "padoms": "No −5 līdz 0."},
        {"jaut": "Par cik grādiem tā pieauga no 0 h līdz 12 h?",
         "atb": ["9"], "padoms": "No −5 līdz 4."},
        {"jaut": "Cik stundas temperatūra bija zem nulles?",
         "atb": ["6"], "padoms": "No 0 h līdz 6 h."},
    ], pamats=4),

    Petijums("Uzzīmē savu temperatūras grafiku",
             vajag="rūtiņu lapa, termometrs vai laika ziņas",
             soli=[
                 "Pieraksti tabulā temperatūru četros dienas brīžos.",
                 "Izvēlies vienības tā, lai ietilptu arī negatīvās vērtības.",
                 "Iekārto plakni un atliec punktus.",
                 "Savieno tos ar līniju.",
                 "Pieraksti trīs teikumus par to, ko grafiks rāda.",
             ],
             secinajums="Grafiks parāda ne tikai vērtības, bet arī to, kurā "
                        "brīdī izmaiņa bija visstraujākā."),

    Varianti("Kad punktus savieno?", [
        {"jaut": "Temperatūras mērījumus savieno ar līniju, jo...",
         "opcijas": ["starp mērījumiem temperatūra mainās pakāpeniski",
                     "tā ir skaistāk", "tā prasa likums",
                     "punktu ir maz"],
         "pareizi": 0,
         "padoms": "Starp mērījumiem ir īstas vērtības."},
        {"jaut": "Kurus datus *nesavieno* ar līniju?",
         "opcijas": ["Skolēnu skaitu klasēs", "Temperatūru",
                     "Ceļu un laiku", "Auguma garumu pa gadiem"],
         "pareizi": 0,
         "padoms": "Starp divām klasēm nav starpvērtību."},
        {"jaut": "Tabulas kolonna (3; −3) plaknē ir...",
         "opcijas": ["punkts trīs pa labi un trīs uz leju",
                     "punkts trīs uz augšu",
                     "divi punkti", "līnija"],
         "pareizi": 0,
         "padoms": "Pirmais skaitlis - horizontāli."},
        {"jaut": "Kur grafiks šķērso horizontālo asi?",
         "opcijas": ["Tur, kur vērtība ir nulle", "Grafika sākumā",
                     "Grafika beigās", "Nekur"],
         "pareizi": 0,
         "padoms": "y = 0."},
    ], pamats=4),

    Pasaule("Kāda bija nedēļa?",
            Ievadi("", [
                {"jaut": "Pirmdien −6 °C, otrdien −2 °C. Par cik grādiem "
                         "kļuva siltāks?",
                 "atb": ["4"], "padoms": "No −6 līdz −2."},
                {"jaut": "Trešdien 1 °C. Par cik grādiem siltāks nekā "
                         "otrdien?",
                 "atb": ["3"], "padoms": "No −2 līdz 1."},
                {"jaut": "Ceturtdien −4 °C. Par cik grādiem aukstāks nekā "
                         "trešdien?",
                 "atb": ["5"], "padoms": "No 1 līdz −4."},
                {"jaut": "Kāda ir starpība starp siltāko un aukstāko dienu?",
                 "atb": ["7"], "padoms": "No −6 līdz 1."},
            ]),
            pavediens="planeta",
            konteksts="Nedēļas grafiks rāda ne tikai temperatūru, bet arī "
                      "to, cik strauji tā mainījās.",
            kapec="Straujākā izmaiņa grafikā ir stāvākā līnijas daļa."),

    Zimejums("Tabula kļuvusi par grafiku",
             plakne(lauzta=[(0, -5), (3, -3), (6, 0), (9, 3), (12, 4)],
                    no_x=0, lidz_x=12, no_y=-6, lidz_y=6, solis=3,
                    x_nos="h", y_nos="°C"),
             paskaidro="Tie paši pieci mērījumi, kas stundas sākuma tabulā - "
                       "tikai tagad redzams, kā temperatūra mainījās.",
             ievads="Salīdzini šo attēlu ar stundas sākuma tabulu."),

    Kopsavilkums([
        "Pārnesu tabulas datus uz koordinātu plakni.",
        "Izvēlos vienības tā, lai ietilptu negatīvās vērtības.",
        "Savienoju punktus tad, kad lielums mainās pakāpeniski.",
        "Izstāstu grafiku vārdiem.",
    ]),

    Majas([
        "Pieraksti tabulā četras šīs dienas temperatūras.",
        "Uzzīmē tās koordinātu plaknē.",
        "Pieraksti, kurā brīdī izmaiņa bija visstraujākā.",
    ]),
]
