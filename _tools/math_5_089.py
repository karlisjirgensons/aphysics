# -*- coding: utf-8 -*-
"""5. klase, 89. stunda: «Kur vēl noder daļu rēķini?»

Temata pēdējā stunda pirms pārbaudes darba. Te nav neviena jauna paņēmiena -
ir tikai viens jautājums: kuros dzīves gadījumos rēķina tieši tāpat. Skolēns
pats atlasa piemērus un pats izdomā jaunus, un tieši tas parāda, vai
prasme ir saprasta vai tikai iemācīta.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kur vēl noder daļu rēķini?"

MERKIS = ("Mācīsimies atlasīt un veidot sadzīves piemērus, kuros daļu "
          "rēķinus lieto vienādi.")

SATURS = [
    Sakums("Trīs uzdevumi, viens rēķins",
           zimejums=restis([["1/4", "1/4", "1/4"]],
                           virsraksts="Atlaide, sastāvs, iespējamība"),
           paraksts="Trīs pavisam dažādas situācijas, bet rēķins ir viens un "
                    "tas pats.",
           fakti=["Atlaide 100 € no 400 € cenas ir {1|4}.",
                  "Cukurs 100 g no 400 g ir {1|4}.",
                  "Viena bumbiņa no četrām ir {1|4}."]),

    Doma("Vienādi uzdevumi izskatās dažādi",
         "Daļu rēķins ir viens un tas pats visur, kur ir veselais un gabals; "
         "mainās tikai vārdi ap skaitļiem.",
         soli=[
             "Atrodi situācijā veselo.",
             "Atrodi gabalu.",
             "Uzraksti daļu un saīsini to.",
             "Pārbaudi, vai uzdevums nav no zināmā tipa.",
             "Pieraksti atbildi tās situācijas vārdiem.",
         ],
         pieze="Trīs tipi aptver gandrīz visu: atrodi daļu no veselā, atrodi "
               "veselo pēc daļas, izsaki vienu skaitli kā otra daļu. Ja "
               "uzdevums neizskatās pēc neviena, parasti tas ir otrais."),

    Paraugs("Viens rēķins trijās situācijās",
            uzd="Kas kopīgs uzdevumiem par atlaidi 100 € no 400 €, cukuru "
                "100 g no 400 g un vienu bumbiņu no četrām?",
            soli=[
                ("Visur ir veselais un gabals",
                 "400 €, 400 g un 4 bumbiņas."),
                ("{100|400} = {1|4}",
                 "Atlaides daļa."),
                ("{100|400} = {1|4}",
                 "Cukura daļa - tas pats rēķins."),
                ("{1|4}",
                 "Arī iespējamība izvilkt vienu bumbiņu no četrām."),
                ("Visos trijos atbilde ir {1|4}",
                 "Atšķiras tikai vārdi."),
            ],
            atbilde="Visos trijos uzdevumos daļa ir {1|4}"),

    Ievadi("Kurš rēķins te vajadzīgs?", [
        {"jaut": "Prece maksā 400 €, atlaide 100 €. Kāda daļa? Atbildi "
                 "raksti kā a/b.",
         "atb": ["1/4", "100/400"], "padoms": "{100|400}."},
        {"jaut": "Klasē 24 skolēni, {1|4} brauc ekskursijā. Cik skolēnu?",
         "atb": ["6"], "padoms": "24 : 4."},
        {"jaut": "{1|4} skolēnu ir 6. Cik skolēnu ir klasē?",
         "atb": ["24"], "padoms": "6 · 4."},
        {"jaut": "Maisā 20 bumbiņas, 5 sarkanas. Kāda iespējamība izvilkt "
                 "sarkanu? Atbildi raksti kā a/b.",
         "atb": ["1/4", "5/20"], "padoms": "{5|20}."},
        {"jaut": "Ceļš 60 km, nobraukta {2|3}. Cik kilometru?",
         "atb": ["40"], "padoms": "60 : 3 · 2."},
        {"jaut": "Nobraukti 40 km, tas ir {2|3} ceļa. Cik garš ir ceļš?",
         "atb": ["60"], "padoms": "40 : 2 · 3."},
        {"jaut": "Produktā 900 g, ūdens 600 g. Kāda daļa ir ūdens? Atbildi "
                 "raksti kā a/b.",
         "atb": ["2/3", "600/900"], "padoms": "Abus dala ar 300."},
        {"jaut": "Pulciņā 18 bērni, {1|3} ir meitenes. Cik meiteņu?",
         "atb": ["6"], "padoms": "18 : 3."},
    ], pamats=4,
        ievads="Vispirms nosaki uzdevuma tipu, tikai tad rēķini."),

    Zimejums("Trīs tipi, kas aptver visu",
             restis([["1/4", "6", "24"]],
                    virsraksts="Daļa, tās vērtība, veselais"),
             paskaidro="Ja zināmi divi no trim skaitļiem, trešo vienmēr var "
                       "atrast. Tieši tā ir visos trijos uzdevumu tipos.",
             ievads="Uzdevums ir tikai jautājums par to, kurš skaitlis "
                    "trūkst."),

    Varianti("Kāds uzdevums tas ir?", [
        {"jaut": "«Klasē 24 skolēni, {1|4} brauc ekskursijā. Cik brauc?» "
                 "Kāds tips?",
         "opcijas": ["Daļa no veselā", "Veselais pēc daļas",
                     "Skaitlis kā daļa", "Nav neviens"],
         "pareizi": 0,
         "padoms": "Zināms veselais, meklē gabalu."},
        {"jaut": "«6 skolēni ir {1|4} klases. Cik skolēnu klasē?» Kāds tips?",
         "opcijas": ["Veselais pēc daļas", "Daļa no veselā",
                     "Skaitlis kā daļa", "Nav neviens"],
         "pareizi": 0,
         "padoms": "Zināma daļas vērtība."},
        {"jaut": "«No 24 skolēniem 6 brauc. Kāda daļa brauc?» Kāds tips?",
         "opcijas": ["Skaitlis kā daļa", "Daļa no veselā",
                     "Veselais pēc daļas", "Nav neviens"],
         "pareizi": 0,
         "padoms": "Meklē pašu daļu."},
        {"jaut": "Kas kopīgs atlaidei, produkta sastāvam un iespējamībai?",
         "opcijas": ["Visur ir veselais un gabals",
                     "Visur ir nauda",
                     "Visur ir procenti",
                     "Nekas nav kopīgs"],
         "pareizi": 0,
         "padoms": "Divi skaitļi, viena daļa."},
        {"jaut": "Cik skaitļu jāzina, lai atrastu trešo?",
         "opcijas": ["Divi", "Viens", "Trīs", "Neviens"],
         "pareizi": 0,
         "padoms": "Daļa, vērtība, veselais."},
        {"jaut": "Ja uzdevumā prasa pašu daļu, ko dara?",
         "opcijas": ["Gabalu dala ar veselo", "Veselo dala ar gabalu",
                     "Saskaita abus", "Reizina abus"],
         "pareizi": 0,
         "padoms": "Gabals skaitītājā."},
    ], pamats=4),

    Pasaule("Viena diena, pieci daļu rēķini",
            Ievadi("", [
                {"jaut": "Skolā 6 stundas, {1|3} no tām ir matemātika un "
                         "latviešu valoda. Cik stundu?",
                 "atb": ["2"], "padoms": "6 : 3."},
                {"jaut": "Pusdienās 20 skolēni, 15 ēd zupu. Kāda daļa? "
                         "Atbildi raksti kā a/b.",
                 "atb": ["3/4", "15/20"], "padoms": "{15|20}."},
                {"jaut": "Mājasdarbos pagāja 45 minūtes, tas ir {3|4} no "
                         "plānotā laika. Cik minūtes bija plānotas?",
                 "atb": ["60"], "padoms": "45 : 3 · 4."},
                {"jaut": "Klasē 25 skolēni, 5 spēlē futbolu. Kāda "
                         "iespējamība, ka nejauši izvēlēts skolēns spēlē "
                         "futbolu? Atbildi raksti kā a/b.",
                 "atb": ["1/5", "5/25"], "padoms": "{5|25}."},
            ]),
            pavediens="skola",
            konteksts="Viena skolas diena satur visus trīs daļu uzdevumu "
                      "tipus, tikai neviens tos tā nesauc.",
            kapec="Kas pamanīs tipu, tam uzdevums jau ir atrisināts."),

    Kopsavilkums([
        "Atpazīstu daļu uzdevuma tipu pēc tā, kurš skaitlis trūkst.",
        "Atlasu sadzīves piemērus, kuros rēķina vienādi.",
        "Izveidoju savu uzdevumu katram no trim tipiem.",
        "Pierakstu atbildi tās situācijas vārdiem.",
    ]),

    Majas([
        "Atrodi trīs sadzīves situācijas ar daļām un nosaki katras tipu.",
        "Izdomā pa vienam uzdevumam katram tipam un atrisini tos.",
        "Sagatavojies pārbaudes darbam: pārskati 72.-88. stundas "
        "kopsavilkumus.",
    ]),
]
