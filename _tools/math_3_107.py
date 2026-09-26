# -*- coding: utf-8 -*-
"""3. klase, 107. stunda: «Kāpēc figūra ar vienādām malām var izskatīties
citādi?»

Malu garumi figūru nenosaka. Ja taisnstūri «pastumj» sānis, malas paliek tās
pašas, bet leņķi vairs nav taisni - un figūra ir cita. Tieši no šī
novērojuma rodas vajadzība pēc leņķa jēdziena, kas nāk nākamajā stundā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         figura)

TEMA = "Kāpēc figūra ar vienādām malām var izskatīties citādi?"

MERKIS = ("Salīdzināsim taisnstūri ar figūru, kurai tādas pašas malas, bet "
          "leņķi nav taisni.")

SATURS = [
    Sakums("Vai malu garumi nosaka figūru?",
           zimejums=figura([(0, 0), (6, 0), (8, 3), (2, 3)],
                           [(3, -0.7, "6"), (7.5, 1.5, "slīpa mala")],
                           "malas tās pašas, leņķi citi"),
           paraksts="Šai figūrai malas ir tādas pašas kā taisnstūrim.",
           fakti=["Vienādas malas vēl nenozīmē vienādu figūru.",
                  "Figūru nosaka gan malas, gan leņķi."]),

    Doma("Figūru nosaka malas *un* leņķi",
         "Ja taisnstūri pastumj sānis, malas paliek tās pašas, bet leņķi "
         "vairs nav taisni - un figūra ir cita.",
         soli=[
             "Izmēri visas malas - tās var sakrist.",
             "Pārbaudi leņķus ar uzstūri.",
             "Ja kaut viens leņķis nav taisns, tas nav taisnstūris.",
             "Salīdzini abu figūru augstumu.",
         ],
         pieze="Perimetrs abām figūrām ir vienāds, bet laukums - nē: "
               "pastumjot figūra kļūst zemāka un tajā ietilpst mazāk."),

    Petijums("Pastum taisnstūri",
             vajag="četri kociņi vai salmiņi un plastilīna bumbiņas",
             soli=[
                 "Saliec taisnstūri no četriem kociņiem.",
                 "Savieno stūrus ar plastilīnu, lai tie varētu griezties.",
                 "Pastum vienu malu sānis.",
                 "Pārbaudi, vai malu garumi mainījās.",
             ],
             secinajums="Malas paliek tās pašas, bet figūra kļūst zemāka - "
                        "tātad figūru nosaka arī leņķi."),

    Paraugs("Vai perimetrs mainījās?",
            uzd="Taisnstūra malas ir 6 cm un 3 cm. To pastumj sānis. Kāds "
                "ir jaunās figūras perimetrs?",
            soli=[
                ("2 · (6 + 3) = 18",
                 "Taisnstūra perimetrs."),
                ("Malas nemainījās",
                 "Pastumjot garumi paliek tie paši."),
                ("Perimetrs arī ir 18 cm",
                 "Bet figūra vairs nav taisnstūris."),
            ],
            atbilde="18 cm"),

    Ievadi("Malas un perimetrs", [
        {"jaut": "Figūras malas 6, 3, 6 un 3 cm. Cik ir perimetrs?",
         "atb": ["18"], "padoms": "6 + 3 + 6 + 3."},
        {"jaut": "Taisnstūra malas 6 un 3 cm. Cik ir perimetrs?",
         "atb": ["18"], "padoms": "2 · 9."},
        {"jaut": "Vai abiem perimetrs ir vienāds? Raksti «jā» vai «nē».",
         "atb": ["jā", "ja"], "padoms": "Malas taču tās pašas.",
         "tastatura": "text"},
        {"jaut": "Cik taisnu leņķu ir taisnstūrim?", "atb": ["4"],
         "padoms": "Visi četri."},
        {"jaut": "Cik taisnu leņķu ir pastumtajai figūrai?", "atb": ["0"],
         "padoms": "Neviens vairs nav taisns."},
        {"jaut": "Figūras malas 5, 5, 5 un 5 cm. Cik ir perimetrs?",
         "atb": ["20"], "padoms": "4 · 5."},
    ], pamats=4),

    Zimejums("Kvadrāts un pastumts kvadrāts",
             figura([(0, 0), (5, 0), (7, 4), (2, 4)],
                    [(2.5, -0.7, "5"), (6.5, 2, "5")],
                    "visas malas 5, bet nav kvadrāts"),
             paskaidro="Visas četras malas ir vienādas, bet leņķi nav taisni - "
                       "tāpēc tas nav kvadrāts.",
             ievads="Šo figūru sauc par rombu."),

    Varianti("Kas nosaka figūru?", [
        {"jaut": "Vai figūra ar malām 4, 4, 4, 4 vienmēr ir kvadrāts?",
         "opcijas": ["Nē, leņķiem jābūt taisniem", "Jā, vienmēr",
                     "Jā, ja tā ir liela", "To nevar pateikt"],
         "pareizi": 0, "padoms": "Var būt arī rombs."},
        {"jaut": "Kas mainās, pastumjot taisnstūri?",
         "opcijas": ["Leņķi un augstums", "Malu garumi",
                     "Perimetrs", "Malu skaits"],
         "pareizi": 0, "padoms": "Malas paliek tās pašas."},
        {"jaut": "Vai perimetrs mainās, pastumjot figūru?",
         "opcijas": ["Nē", "Jā, kļūst lielāks", "Jā, kļūst mazāks",
                     "To nevar pateikt"],
         "pareizi": 0, "padoms": "Malu garumi nemainās."},
        {"jaut": "Ar ko pārbauda, vai leņķis ir taisns?",
         "opcijas": ["Ar uzstūri", "Ar lineālu", "Ar cirkuli", "Ar aci"],
         "pareizi": 0, "padoms": "Uzstūrim ir taisns leņķis."},
    ], pamats=4),

    Pasaule("Kāpēc būvēs liek slīpās balstus?",
            Ievadi("", [
                {"jaut": "Rāmim malas ir 8, 5, 8 un 5 cm. Cik ir perimetrs?",
                 "atb": ["26"], "padoms": "2 · 13."},
                {"jaut": "Cik taisnu leņķu ir taisnstūrveida rāmim?",
                 "atb": ["4"], "padoms": "Visi četri."},
                {"jaut": "Cik kociņu vajag rāmim ar četrām malām un vienu "
                         "slīpo balstu?",
                 "atb": ["5"], "padoms": "4 + 1."},
                {"jaut": "Cik kociņu vajag pieciem tādiem rāmjiem?",
                 "atb": ["25"], "padoms": "5 · 5."},
            ]),
            pavediens="tehnika",
            konteksts="Četrstūrveida rāmis viegli pastumjas, tāpēc būvēs tam "
                      "pieliek slīpu balstu - un rāmis vairs nekustas.",
            kapec="Trīsstūri pastumt nevar - tieši tāpēc tas ir stiprākais."),

    Kopsavilkums([
        "Zinu, ka figūru nosaka gan malas, gan leņķi.",
        "Salīdzinu taisnstūri ar figūru, kurai leņķi nav taisni.",
        "Zinu, ka pastumjot perimetrs nemainās.",
        "Pārbaudu leņķus ar uzstūri.",
    ]),

    Majas([
        "Saliec no četriem zīmuļiem taisnstūri un pastum to sānis.",
        "Pārbaudi, vai malu garumi mainījās.",
        "Atrodi mājās figūru, kurai malas vienādas, bet leņķi nav taisni.",
    ]),
]
