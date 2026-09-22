# -*- coding: utf-8 -*-
"""5. klase, 120. stunda: «Kāds daudzstūris atbilst nosacījumiem?»

Jauns mikrotemats, un uzdevums ir apgriezts ierastajam: nevis apraksti doto
figūru, bet uzzīmē tādu, kas atbilst nosacījumiem. Atbilžu parasti ir
vairākas, un tieši tas ir stundas atklājums - divi skolēni var uzzīmēt
dažādas figūras, un abas būs pareizas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         figura)

TEMA = "Kāds daudzstūris atbilst nosacījumiem?"

MERKIS = ("Mācīsimies zīmēt daudzstūri pēc diviem vai trim nosacījumiem par "
          "malām un leņķiem.")

SATURS = [
    Sakums("Divas dažādas pareizās atbildes",
           zimejums=figura([(0, 0), (5, 0), (5, 3), (0, 3)],
                           virsraksts="Četrstūris ar taisniem leņķiem"),
           paraksts="Šis der nosacījumiem, bet der arī kvadrāts 4 x 4.",
           fakti=["Nosacījumi reti nosaka vienu vienīgu figūru.",
                  "Parasti der vairākas dažādas figūras.",
                  "Svarīgi ir pārbaudīt katru nosacījumu atsevišķi."]),

    Doma("Pārbaudi katru nosacījumu",
         "Zīmējot figūru pēc nosacījumiem, tos pieraksta sarakstā un pēc "
         "zīmēšanas pārbauda pa vienam.",
         soli=[
             "Izraksti visus nosacījumus atsevišķās rindās.",
             "Sāc ar to, kas nosaka visvairāk - parasti leņķus.",
             "Uzzīmē figūru rūtiņu lapā.",
             "Pārbaudi katru nosacījumu pēc kārtas.",
             "Ja kāds neizpildās, labo zīmējumu, nevis nosacījumu.",
         ],
         pieze="Reizēm nosacījumi ir pretrunīgi, un figūra nav uzzīmējama: "
               "četrstūris ar četriem taisniem leņķiem un trim vienādām "
               "malām neeksistē. Arī tā ir pareiza atbilde."),

    Paraugs("Četrstūris ar taisniem leņķiem",
            uzd="Uzzīmē četrstūri, kuram visi leņķi ir taisni un divas malas "
                "ir 5 rūtiņas garas.",
            soli=[
                ("Visi leņķi taisni - tas ir taisnstūris",
                 "Pirmais nosacījums."),
                ("Divas malas pa 5 rūtiņām",
                 "Otrais nosacījums."),
                ("Zīmē 5 x 3 taisnstūri",
                 "Pretējās malas ir vienādas."),
                ("Pārbaude: 4 taisni leņķi, divas malas pa 5",
                 "Abi nosacījumi izpildīti."),
            ],
            atbilde="Der taisnstūris 5 x 3, bet arī 5 x 2 vai 5 x 5"),

    Petijums("Uzzīmē trīs dažādas figūras",
             soli=["Uzraksti nosacījumus: piecstūris ar vismaz vienu taisnu "
                   "leņķi.",
                   "Uzzīmē rūtiņu lapā vienu tādu figūru.",
                   "Uzzīmē otru, kas izskatās pavisam citādi.",
                   "Uzzīmē trešo, kurai taisnu leņķu ir divi.",
                   "Pārbaudi, vai visas trīs atbilst nosacījumiem."],
             vajag="rūtiņu lapa, lineāls, zīmulis",
             secinajums="Nosacījumiem atbilst daudz dažādu figūru, nevis "
                        "viena."),

    Ievadi("Cik malu un leņķu?", [
        {"jaut": "Cik malu ir piecstūrim?",
         "atb": ["5"], "padoms": "Nosaukums to pasaka."},
        {"jaut": "Cik virsotņu ir sešstūrim?",
         "atb": ["6"], "padoms": "Tikpat, cik malu."},
        {"jaut": "Cik taisnu leņķu ir taisnstūrim?",
         "atb": ["4"], "padoms": "Visi leņķi taisni."},
        {"jaut": "Taisnstūra malas ir 5 un 3 rūtiņas. Cik rūtiņu ir "
                 "perimetrs?",
         "atb": ["16"], "padoms": "(5 + 3) · 2."},
        {"jaut": "Kvadrāta mala ir 4 rūtiņas. Cik rūtiņu ir perimetrs?",
         "atb": ["16"], "padoms": "4 · 4."},
        {"jaut": "Cik malu ir trijstūrim?",
         "atb": ["3"], "padoms": "Trīs stūri."},
        {"jaut": "Taisnstūra malas ir 6 un 2. Cik rūtiņu ir laukums?",
         "atb": ["12"], "padoms": "6 · 2."},
        {"jaut": "Kvadrāta mala ir 5 rūtiņas. Cik rūtiņu ir laukums?",
         "atb": ["25"], "padoms": "5 · 5."},
    ], pamats=4,
        ievads="Nosaukums pasaka malu skaitu, zīmējums - pārējo."),

    Zimejums("Viens nosacījums, divas figūras",
             figura([(0, 0), (4, 0), (4, 4), (0, 4)],
                    virsraksts="Kvadrāts 4 x 4 - arī der"),
             paskaidro="Arī šī figūra atbilst nosacījumiem «visi leņķi "
                       "taisni» un «ir mala 4 rūtiņas». Pareizas atbildes ir "
                       "vairākas.",
             ievads="Otra figūra tiem pašiem nosacījumiem."),

    Varianti("Vai figūra der?", [
        {"jaut": "Cik figūru parasti atbilst diviem nosacījumiem?",
         "opcijas": ["Vairākas", "Tikai viena", "Neviena", "Tieši divas"],
         "pareizi": 0,
         "padoms": "Nosacījumi neatstāj vienu vienīgu iespēju."},
        {"jaut": "Ko dara, ja kāds nosacījums neizpildās?",
         "opcijas": ["Labo zīmējumu", "Maina nosacījumu",
                     "Atstāj kā ir", "Zīmē citu figūru veidu"],
         "pareizi": 0,
         "padoms": "Nosacījumi ir uzdevums."},
        {"jaut": "Četrstūris ar četriem taisniem leņķiem ir...",
         "opcijas": ["Taisnstūris", "Trijstūris", "Piecstūris",
                     "Ieliekts četrstūris"],
         "pareizi": 0,
         "padoms": "Arī kvadrāts ir taisnstūris."},
        {"jaut": "Vai eksistē četrstūris ar pieciem leņķiem?",
         "opcijas": ["Nē, leņķu ir tikpat, cik malu", "Jā",
                     "Jā, ja tas ir ieliekts", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Četrstūrim ir četri leņķi."},
        {"jaut": "Cik malu ir daudzstūrim ar 7 virsotnēm?",
         "opcijas": ["7", "6", "8", "14"],
         "pareizi": 0,
         "padoms": "Tikpat, cik virsotņu."},
        {"jaut": "Ko izraksta vispirms?",
         "opcijas": ["Visus nosacījumus", "Figūras nosaukumu",
                     "Laukumu", "Perimetru"],
         "pareizi": 0,
         "padoms": "Tikai tad var pārbaudīt."},
    ], pamats=4),

    Pasaule("Kāda būs skolas puķu dobe?",
            Ievadi("", [
                {"jaut": "Dobe ir taisnstūris ar malām 6 m un 4 m. Cik metru "
                         "ir tās perimetrs?",
                 "atb": ["20"], "padoms": "(6 + 4) · 2."},
                {"jaut": "Cik kvadrātmetru ir šīs dobes laukums?",
                 "atb": ["24"], "padoms": "6 · 4."},
                {"jaut": "Cita dobe ir kvadrāts ar malu 5 m. Cik metru ir "
                         "perimetrs?",
                 "atb": ["20"], "padoms": "4 · 5."},
                {"jaut": "Cik kvadrātmetru ir kvadrātveida dobes laukums?",
                 "atb": ["25"], "padoms": "5 · 5."},
            ]),
            pavediens="skola",
            konteksts="Skolas pagalmā dobei uzdod nosacījumus - cik gara "
                      "mala un cik apmales -, nevis gatavu formu.",
            kapec="No nosacījumiem figūru var uzzīmēt vairākos veidos."),

    Kopsavilkums([
        "Izrakstu visus nosacījumus atsevišķās rindās.",
        "Zīmēju daudzstūri, kas atbilst diviem vai trim nosacījumiem.",
        "Pārbaudu katru nosacījumu pēc kārtas.",
        "Zinu, ka pareizu atbilžu var būt vairākas.",
    ]),

    Majas([
        "Uzzīmē divas dažādas figūras ar nosacījumiem: četrstūris, viena "
        "mala 6 rūtiņas, vismaz divi taisni leņķi.",
        "Pārbaudi abas figūras pēc nosacījumiem.",
        "Izdomā nosacījumus, kuriem neatbilst neviena figūra.",
    ]),
]
