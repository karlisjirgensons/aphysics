# -*- coding: utf-8 -*-
"""5. klase, 103. stunda: «Kā saskaitīt, ja saucēji atšķiras?»

Iepriekšējās stundas plāns te tiek izpildīts. Jauna paņēmiena nav - ir tikai
divas jau zināmas lietas vienā rēķinā: kopsaucējs no 65. stundas un jaukto
skaitļu saskaitīšana no 97. Tāpēc stundas svars ir uz pierakstu: kur beidzas
viens solis un sākas nākamais.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā saskaitīt, ja saucēji atšķiras?"

MERKIS = ("Iemācīsimies saskaitīt jauktus skaitļus ar dažādiem saucējiem, "
          "veidojot skaidru pierakstu.")

SATURS = [
    Sakums("Divas distances, divi saucēji",
           zimejums=restis([["2 1/2", "1 1/3", "3 5/6"]],
                           virsraksts="Summa ar kopsaucēju 6"),
           paraksts="2{1|2} km + 1{1|3} km = 3{5|6} km.",
           fakti=["Saucēji ir 2 un 3 - saskaitīt tieši nevar.",
                  "Kopsaucējs ir 6.",
                  "Tikai pēc tam saskaita veselos un daļas."]),

    Doma("Kopsaucējs, tad saskaitīšana",
         "Jauktus skaitļus ar dažādiem saucējiem saskaita, vispirms daļas "
         "pārrakstot ar kopsaucēju un tikai pēc tam saskaitot veselos un "
         "daļas.",
         soli=[
             "Atrodi daļu kopsaucēju.",
             "Pārraksti abas daļas ar to, pierakstot reizinātāju.",
             "Saskaiti veselās daļas.",
             "Saskaiti daļas, saucēju atstājot to pašu.",
             "Atdali veselo un saīsini, ja vajag.",
         ],
         pieze="Pierakstā katrs solis ir savā rindā. Tas nav skaistuma dēļ: "
               "ja atbilde iznāk greiza, pa rindām var atrast, kurā solī "
               "kļūda radās."),

    Paraugs("2{1|2} + 1{1|3}",
            uzd="Saskaiti jauktus skaitļus ar dažādiem saucējiem.",
            soli=[
                ("Kopsaucējs ir 6",
                 "6 dalās ar 2 un 3."),
                ("{1|2} = {1 · 3|2 · 3} = {3|6}",
                 "Pirmā daļa."),
                ("{1|3} = {1 · 2|3 · 2} = {2|6}",
                 "Otrā daļa."),
                ("2 + 1 = 3",
                 "Veselās daļas."),
                ("{3|6} + {2|6} = {5|6}",
                 "Daļas; iznāk 3{5|6}."),
            ],
            atbilde="2{1|2} + 1{1|3} = 3{5|6}"),

    Ievadi("Saskaiti ar kopsaucēju", [
        {"jaut": "2{1|2} + 1{1|3} = ? Atbildi raksti kā a b/c.",
         "atb": ["3 5/6"], "padoms": "{3|6} + {2|6}."},
        {"jaut": "1{1|4} + 2{1|2} = ? Atbildi raksti kā a b/c.",
         "atb": ["3 3/4"], "padoms": "{1|4} + {2|4}."},
        {"jaut": "3{1|3} + 1{1|6} = ? Atbildi raksti kā a b/c.",
         "atb": ["4 1/2", "4 3/6"], "padoms": "{2|6} + {1|6} = {3|6}."},
        {"jaut": "2{2|5} + 1{3|10} = ? Atbildi raksti kā a b/c.",
         "atb": ["3 7/10"], "padoms": "{4|10} + {3|10}."},
        {"jaut": "1{3|4} + 2{1|3} = ? Atbildi raksti kā a b/c.",
         "atb": ["4 1/12"], "padoms": "{9|12} + {4|12} = {13|12}."},
        {"jaut": "2{5|6} + 1{1|2} = ? Atbildi raksti kā a b/c.",
         "atb": ["4 1/3", "4 2/6"], "padoms": "{5|6} + {3|6} = {8|6}."},
        {"jaut": "3{1|8} + 1{1|4} = ? Atbildi raksti kā a b/c.",
         "atb": ["4 3/8"], "padoms": "{1|8} + {2|8}."},
        {"jaut": "1{2|3} + 1{1|3} = ? Ieraksti skaitli.",
         "atb": ["3"], "padoms": "{3|3} = 1."},
    ], pamats=4,
        ievads="Kopsaucējs vienmēr ir pirmais solis."),

    Zimejums("Divas daļas, viens saucējs",
             restis([["1/2", "3/6"],
                     ["1/3", "2/6"],
                     ["kopā", "5/6"]],
                    virsraksts="Tikai pēdējā rindā saskaita"),
             paskaidro="Pirmās divas rindas ir pārrakstīšana, trešā - "
                       "saskaitīšana. Veselos saskaita atsevišķi.",
             ievads="Pieraksts iet pa rindām, viens solis katrā."),

    Varianti("Kur pieraksts sabruka?", [
        {"jaut": "Kas ir pirmais solis?",
         "opcijas": ["Kopsaucēja atrašana", "Veselo saskaitīšana",
                     "Daļu saskaitīšana", "Saīsināšana"],
         "pareizi": 0,
         "padoms": "Vienādi gabali vispirms."},
        {"jaut": "Skolēns raksta 2{1|2} + 1{1|3} = 3{2|5}. Kas nav labi?",
         "opcijas": ["Saskaitīti arī saucēji", "Nav saīsināts",
                     "Veselie nav saskaitīti", "Kļūdas nav"],
         "pareizi": 0,
         "padoms": "Saucēju nesaskaita."},
        {"jaut": "Cik ir 1{3|4} + 2{1|3}?",
         "opcijas": ["4{1|12}", "3{13|12}", "3{4|7}", "4{13|12}"],
         "pareizi": 0,
         "padoms": "{13|12} = 1{1|12}."},
        {"jaut": "Daļu summa iznāca {8|6}. Ko dara tālāk?",
         "opcijas": ["Atdala veselo: 1{2|6}", "Atstāj kā ir",
                     "Saīsina saucēju", "Atņem vienu"],
         "pareizi": 0,
         "padoms": "Neīsta daļa jāsakārto."},
        {"jaut": "Kāds kopsaucējs ir daļām {1|4} un {1|3}?",
         "opcijas": ["12", "7", "6", "4"],
         "pareizi": 0,
         "padoms": "4 · 3."},
        {"jaut": "Kāpēc katru soli raksta savā rindā?",
         "opcijas": ["Lai kļūdu varētu atrast", "Lai aizņemtu vietu",
                     "Lai būtu skaisti", "Tas nav vajadzīgs"],
         "pareizi": 0,
         "padoms": "Pieraksts ir pierādījums."},
    ], pamats=4),

    Pasaule("Cik noskrien nedēļā?",
            Ievadi("", [
                {"jaut": "Pirmdien 2{1|2} km, otrdien 1{1|3} km. Cik kopā? "
                         "Atbildi raksti kā a b/c.",
                 "atb": ["3 5/6"], "padoms": "{3|6} + {2|6}."},
                {"jaut": "Trešdien 1{3|4} km, ceturtdien 2{1|3} km. Cik kopā? "
                         "Atbildi raksti kā a b/c.",
                 "atb": ["4 1/12"], "padoms": "{9|12} + {4|12}."},
                {"jaut": "Piektdien 2{5|6} km, sestdien 1{1|2} km. Cik kopā? "
                         "Atbildi raksti kā a b/c.",
                 "atb": ["4 1/3", "4 2/6"], "padoms": "{5|6} + {3|6}."},
                {"jaut": "Svētdien 1{2|3} km un vēl 1{1|3} km. Cik kopā? "
                         "Ieraksti skaitli.",
                 "atb": ["3"], "padoms": "{3|3} = 1."},
            ]),
            pavediens="sports",
            konteksts="Treniņu dienasgrāmatā katra diena ir jaukts skaitlis, "
                      "un saucēji tur nekad nav vienādi.",
            kapec="Nedēļas kopsummu var izrēķināt tikai ar kopsaucēju."),

    Kopsavilkums([
        "Atrodu jauktu skaitļu daļām kopsaucēju.",
        "Pārrakstu abas daļas ar kopsaucēju, pierakstot reizinātāju.",
        "Saskaitu veselos un daļas atsevišķi.",
        "Atdalu veselo un saīsinu rezultātu.",
    ]),

    Majas([
        "Izrēķini 3{2|5} + 1{1|2} un pieraksti katru soli savā rindā.",
        "Atrodi divus jauktus skaitļus ar dažādiem saucējiem, kuru summa ir "
        "vesels skaitlis.",
        "Saskaiti savas nedēļas gājienu attālumus.",
    ]),
]
