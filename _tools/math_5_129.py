# -*- coding: utf-8 -*-
"""5. klase, 129. stunda: «Kā uzzīmēt figūru ar dotu laukumu?»

Temata pēdējā stunda pirms pārbaudes darba, un uzdevums ir apgriezts: dots
laukums, jāatrod figūra. Atbilžu ir daudz, un tieši tas padara uzdevumu
interesantu - divi skolēni uzzīmē pavisam dažādas figūras, un abas ir
pareizas, ja rūtiņu skaits sakrīt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         figura)

TEMA = "Kā uzzīmēt figūru ar dotu laukumu?"

MERKIS = ("Mācīsimies rūtiņu lapā zīmēt daudzstūri ar dotu laukumu un dotām "
          "malu īpašībām.")

SATURS = [
    Sakums("Laukums 12 - cik figūru?",
           zimejums=figura([(0, 0), (6, 0), (6, 2), (0, 2)],
                           virsraksts="Taisnstūris 6 x 2"),
           paraksts="Laukums 12 rūtiņas - bet tāds pats ir arī 4 x 3 un "
                    "12 x 1.",
           fakti=["Dots laukums, nevis figūra.",
                  "Pareizu atbilžu ir daudz.",
                  "Svarīgi ir tikai tas, lai rūtiņu skaits sakristu."]),

    Doma("No laukuma uz malām",
         "Lai uzzīmētu taisnstūri ar dotu laukumu, meklē divus skaitļus, "
         "kuru reizinājums ir šis laukums; kombinētai figūrai gabalu laukumu "
         "summai jābūt dotajam skaitlim.",
         soli=[
             "Pieraksti doto laukumu.",
             "Atrodi divus reizinātājus, kas dod šo skaitli.",
             "Uzzīmē taisnstūri ar šādām malām.",
             "Ja doti papildu nosacījumi, pārbaudi arī tos.",
             "Saskaiti rūtiņas un pārbaudi laukumu.",
         ],
         pieze="Šis ir 30. un 31. stundas uzdevums no cita gala: tur meklēja "
               "visus veidus, kā skaitli uzrakstīt kā reizinājumu, te katrs "
               "no tiem ir gatava figūra."),

    Petijums("Uzzīmē trīs figūras ar laukumu 12",
             soli=["Uzzīmē rūtiņu lapā taisnstūri ar laukumu 12 rūtiņas.",
                   "Uzzīmē otru taisnstūri ar to pašu laukumu, bet citām "
                   "malām.",
                   "Uzzīmē kombinētu figūru ar laukumu 12.",
                   "Saskaiti rūtiņas katrā figūrā.",
                   "Salīdzini savas figūras ar solabiedra figūrām."],
             vajag="rūtiņu lapa, lineāls, zīmulis",
             secinajums="Vienam laukumam atbilst daudz dažādu figūru."),

    Paraugs("Taisnstūris ar laukumu 12",
            uzd="Uzzīmē taisnstūri ar laukumu 12 rūtiņas, kura viena mala ir "
                "garāka par otru.",
            soli=[
                ("12 = 6 · 2",
                 "Pirmais reizinātāju pāris."),
                ("12 = 4 · 3",
                 "Otrais pāris."),
                ("12 = 12 · 1",
                 "Trešais pāris."),
                ("Visi trīs der nosacījumam",
                 "Katrā viena mala ir garāka."),
                ("Nederētu tikai kvadrāts",
                 "Bet 12 nav kvadrāta laukums ar veselu malu."),
            ],
            atbilde="Der 6 x 2, 4 x 3 vai 12 x 1"),

    Ievadi("Atrodi malas", [
        {"jaut": "Taisnstūra laukums ir 12, viena mala 6. Cik ir otra?",
         "atb": ["2"], "padoms": "12 : 6."},
        {"jaut": "Laukums 12, viena mala 4. Cik ir otra?",
         "atb": ["3"], "padoms": "12 : 4."},
        {"jaut": "Laukums 20, viena mala 5. Cik ir otra?",
         "atb": ["4"], "padoms": "20 : 5."},
        {"jaut": "Laukums 36, abas malas vienādas. Cik ir katra?",
         "atb": ["6"], "padoms": "6 · 6."},
        {"jaut": "Laukums 24, viena mala 8. Cik ir otra?",
         "atb": ["3"], "padoms": "24 : 8."},
        {"jaut": "Kvadrāta laukums ir 49. Cik ir mala?",
         "atb": ["7"], "padoms": "7 · 7."},
        {"jaut": "Laukums 18, viena mala 3. Cik ir otra?",
         "atb": ["6"], "padoms": "18 : 3."},
        {"jaut": "Cik dažādu taisnstūru ar veselām malām ir laukumam 12? "
                 "Ieraksti skaitli.",
         "atb": ["3"], "padoms": "6x2, 4x3 un 12x1."},
    ], pamats=4,
        ievads="Meklē divus skaitļus, kuru reizinājums ir dotais laukums."),

    Zimejums("Tas pats laukums, cita forma",
             figura([(0, 0), (4, 0), (4, 3), (0, 3)],
                    virsraksts="Taisnstūris 4 x 3"),
             paskaidro="Arī šeit laukums ir 12 rūtiņas, bet figūra izskatās "
                       "pavisam citāda nekā 6 x 2.",
             ievads="Otra pareizā atbilde tam pašam uzdevumam."),

    Varianti("Kura figūra der?", [
        {"jaut": "Laukums 12, viena mala 3. Kāda ir otra?",
         "opcijas": ["4", "9", "6", "36"],
         "pareizi": 0,
         "padoms": "12 : 3."},
        {"jaut": "Cik taisnstūru ar veselām malām ir laukumam 12?",
         "opcijas": ["3", "1", "2", "12"],
         "pareizi": 0,
         "padoms": "Skaitļa 12 reizinātāju pāri."},
        {"jaut": "Vai kvadrāts ar veselu malu var būt ar laukumu 12?",
         "opcijas": ["Nevar", "Var", "Var, ja mala ir 3",
                     "To nevar zināt"],
         "pareizi": 0,
         "padoms": "12 nav vesela skaitļa kvadrāts."},
        {"jaut": "Kāds ir kvadrāta laukums ar malu 5?",
         "opcijas": ["25", "10", "20", "55"],
         "pareizi": 0,
         "padoms": "5 · 5."},
        {"jaut": "Kā pārbauda uzzīmēto figūru?",
         "opcijas": ["Saskaita rūtiņas", "Izmēra perimetru",
                     "Salīdzina ar kaimiņa", "Pārbaudīt nevar"],
         "pareizi": 0,
         "padoms": "Laukums ir rūtiņu skaits."},
        {"jaut": "Cik dažādu figūru ar laukumu 12 var uzzīmēt?",
         "opcijas": ["Ļoti daudz", "Tikai trīs", "Vienu", "Nevienu"],
         "pareizi": 0,
         "padoms": "Arī kombinētas figūras der."},
    ], pamats=4),

    Pasaule("Kādu dobi ierīkot?",
            Ievadi("", [
                {"jaut": "Dobei jābūt 24 m² lielai, viena mala 6 m. Cik metru "
                         "ir otra?",
                 "atb": ["4"], "padoms": "24 : 6."},
                {"jaut": "Cita dobe: 24 m², viena mala 8 m. Cik metru ir "
                         "otra?",
                 "atb": ["3"], "padoms": "24 : 8."},
                {"jaut": "Cik metru žoga vajag dobei 6 m x 4 m?",
                 "atb": ["20"], "padoms": "(6 + 4) · 2."},
                {"jaut": "Cik metru žoga vajag dobei 8 m x 3 m?",
                 "atb": ["22"], "padoms": "(8 + 3) · 2."},
            ]),
            pavediens="maja",
            konteksts="Dārzā laukums ir noteikts, bet formu izvēlas pats - "
                      "un no formas atkarīgs žoga garums.",
            kapec="Vienādam laukumam žoga garums var būt dažāds."),

    Kopsavilkums([
        "Zīmēju taisnstūri ar dotu laukumu.",
        "Atrodu visus veselo malu pārus dotajam laukumam.",
        "Zīmēju kombinētu figūru ar dotu laukumu.",
        "Pārbaudu figūru, saskaitot rūtiņas.",
    ]),

    Majas([
        "Uzzīmē visus taisnstūrus ar veselām malām un laukumu 18.",
        "Uzzīmē kombinētu figūru ar laukumu 18.",
        "Sagatavojies pārbaudes darbam: pārskati 108.-128. stundas "
        "kopsavilkumus.",
    ]),
]
