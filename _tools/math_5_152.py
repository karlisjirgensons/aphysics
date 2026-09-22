# -*- coding: utf-8 -*-
"""5. klase, 152. stunda: «Kā uzzīmēt sektoru diagrammu?»

Praktiskā stunda: aprēķinātie leņķi tiek likti uz papīra. Transportieris te
ir obligāts, bet tikpat svarīgs ir pēdējais solis - pārbaudīt, vai pēdējais
sektors aizpilda riņķi tieši. Ja nē, kaut kur ir kļūda leņķu aprēķinā, un
zīmējums to parāda uzreiz.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         rinkis)

TEMA = "Kā uzzīmēt sektoru diagrammu?"

MERKIS = ("Iemācīsimies zīmēt sektoru diagrammu ar transportieri un ar "
          "digitāliem rīkiem.")

SATURS = [
    Sakums("No skaitļiem uz riņķi",
           zimejums=rinkis(sektors=180, virsraksts="Pirmais sektors: 50 %"),
           paraksts="Pirmo leņķi atliek no rādiusa, nākamo - no iepriekšējā.",
           fakti=["Vispirms aprēķina visu sektoru leņķus.",
                  "Tad novelk rādiusu un atliek pirmo leņķi.",
                  "Katru nākamo mēra no iepriekšējā sektora malas."]),

    Doma("Mēri no iepriekšējās malas",
       "Sektoru diagrammu zīmē, pēc kārtas atliekot aprēķinātos leņķus: "
       "katru nākamo mēra no iepriekšējā sektora malas.",
         soli=[
             "Aprēķini visu sektoru leņķus un pārbaudi summu.",
             "Uzzīmē riņķa līniju un novelc vienu rādiusu.",
             "Pieliec transportieri un atliec pirmo leņķi.",
             "Novelc jaunu rādiusu un atliec nākamo leņķi no tā.",
             "Pēdējam sektoram jāaizpilda atlikušais riņķis tieši.",
         ],
         pieze="Ja pēdējais sektors neaizpilda riņķi, kļūda ir vai nu "
               "leņķu aprēķinā, vai mērīšanā. Tieši tāpēc pēdējo leņķi "
               "nerēķina - to izmanto kā pārbaudi."),

    Petijums("Uzzīmē savu diagrammu",
             soli=["Aptaujā klasi: futbols, basketbols vai volejbols.",
                   "Izsaki katru rezultātu procentos.",
                   "Aprēķini katra sektora leņķi.",
                   "Uzzīmē riņķi un atliec leņķus ar transportieri.",
                   "Pārbaudi, vai pēdējais sektors aizpilda riņķi."],
             vajag="cirkulis, transportieris, krāsainie zīmuļi",
             secinajums="Ja visi leņķi aprēķināti pareizi, pēdējais sektors "
                        "iekļaujas tieši."),

    Paraugs("Trīs sektori: 50 %, 25 % un 25 %",
            uzd="Kā uzzīmēt šo diagrammu?",
            soli=[
                ("Leņķi: 180°, 90° un 90°",
                 "Aprēķināti iepriekš."),
                ("180 + 90 + 90 = 360",
                 "Summa pareiza."),
                ("Atliec pirmo leņķi 180°",
                 "No sākuma rādiusa."),
                ("No jaunās malas atliec 90°",
                 "Otrais sektors."),
                ("Pēdējais sektors iznāk pats",
                 "Tam jābūt tieši 90°."),
            ],
            atbilde="Trīs sektori: 180°, 90° un 90°"),

    Ievadi("Sagatavo diagrammu", [
        {"jaut": "50 % sektoram - cik grādu?",
         "atb": ["180"], "padoms": "360 : 2."},
        {"jaut": "25 % sektoram - cik grādu?",
         "atb": ["90"], "padoms": "360 : 4."},
        {"jaut": "Cik grādu ir visiem trim sektoriem kopā?",
         "atb": ["360"], "padoms": "180 + 90 + 90."},
        {"jaut": "Divi sektori ir 180° un 120°. Cik grādu ir trešais?",
         "atb": ["60"], "padoms": "360 - 300."},
        {"jaut": "Divi sektori ir 90° un 90°. Cik grādu ir trešais?",
         "atb": ["180"], "padoms": "360 - 180."},
        {"jaut": "40 % sektoram - cik grādu?",
         "atb": ["144"], "padoms": "3,6 · 40."},
        {"jaut": "Sektori ir 40 % un 35 %. Cik procentu ir trešais?",
         "atb": ["25"], "padoms": "100 - 75."},
        {"jaut": "30 % sektoram - cik grādu?",
         "atb": ["108"], "padoms": "3,6 · 30."},
    ], pamats=4,
        ievads="Vispirms visi leņķi, tikai tad transportieris."),

    Zimejums("Trīs ceturtdaļas aizņemti",
             rinkis(sektors=270, virsraksts="Pēc diviem sektoriem"),
             paskaidro="Kad atlikti 180° un 90°, riņķī palicis tieši viens "
                       "90° sektors. Ja tas neiznāk, kaut kur ir kļūda.",
             ievads="Pēdējais sektors ir pārbaude."),

    Varianti("Kā zīmē diagrammu?", [
        {"jaut": "No kurienes mēra otro leņķi?",
         "opcijas": ["No pirmā sektora malas", "No sākuma rādiusa",
                     "No centra", "No riņķa līnijas"],
         "pareizi": 0,
         "padoms": "Sektori iet cits aiz cita."},
        {"jaut": "Ko dara vispirms?",
         "opcijas": ["Aprēķina visus leņķus", "Zīmē riņķi",
                     "Ņem transportieri", "Iekrāso"],
         "pareizi": 0,
         "padoms": "Bez leņķiem nav ko atlikt."},
        {"jaut": "Kāpēc pēdējo leņķi nerēķina?",
         "opcijas": ["To izmanto kā pārbaudi", "Tas nav vajadzīgs",
                     "Tas vienmēr ir 90°", "To nevar aprēķināt"],
         "pareizi": 0,
         "padoms": "Riņķim jāaizpildās tieši."},
        {"jaut": "Divi sektori ir 180° un 120°. Cik ir trešais?",
         "opcijas": ["60°", "80°", "40°", "120°"],
         "pareizi": 0,
         "padoms": "360 - 300."},
        {"jaut": "Ar ko mēra leņķus?",
         "opcijas": ["Ar transportieri", "Ar cirkuli", "Ar lineālu",
                     "Ar aci"],
         "pareizi": 0,
         "padoms": "Leņķu mērierīce."},
        {"jaut": "Pēdējais sektors neaizpilda riņķi. Ko tas nozīmē?",
         "opcijas": ["Kaut kur ir kļūda", "Viss kārtībā",
                     "Vajag citu riņķi", "Diagramma ir gatava"],
         "pareizi": 0,
         "padoms": "Summai jābūt 360°."},
    ], pamats=4),

    Pasaule("Klases aptaujas diagramma",
            Ievadi("", [
                {"jaut": "Klasē 20 skolēni, 10 izvēlējās futbolu. Cik "
                         "procentu tas ir?",
                 "atb": ["50"], "padoms": "{10|20}."},
                {"jaut": "Cik grādu ir šis sektors?",
                 "atb": ["180"], "padoms": "360 : 2."},
                {"jaut": "5 skolēni izvēlējās basketbolu. Cik grādu ir šis "
                         "sektors?",
                 "atb": ["90"], "padoms": "{5|20} = 25 %."},
                {"jaut": "Cik grādu paliek pēdējam sektoram?",
                 "atb": ["90"], "padoms": "360 - 270."},
            ]),
            pavediens="skola",
            konteksts="Klases aptauju rezultātus pie sienas liek tieši kā "
                      "sektoru diagrammu.",
            kapec="Riņķī uzreiz redz, kura grupa ir lielākā."),

    Kopsavilkums([
        "Aprēķinu visu sektoru leņķus, pirms sāku zīmēt.",
        "Atlieku leņķus ar transportieri, katru no iepriekšējās malas.",
        "Izmantoju pēdējo sektoru kā pārbaudi.",
        "Iekrāsoju un apzīmēju katru sektoru.",
    ]),

    Majas([
        "Uzzīmē diagrammu sektoriem 40 %, 35 % un 25 %.",
        "Pārbaudi, vai pēdējais sektors iekļaujas tieši.",
        "Pamēģini to pašu uzzīmēt ar datora rīku.",
    ]),
]
