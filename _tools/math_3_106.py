# -*- coding: utf-8 -*-
"""3. klase, 106. stunda: «Kas taisnstūrim ir īpašs?»

Ģeometrijas temata sākums. Taisnstūri skolēns pazīst pēc izskata; te viņš
iemācās to raksturot ar *pazīmēm* - četras malas, pretējās vienādas, visi
leņķi taisni. Kvadrāts ir īpašs taisnstūra gadījums, nevis cita figūra.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, figura)

TEMA = "Kas taisnstūrim ir īpašs?"

MERKIS = ("Raksturosim taisnstūri un kvadrātu, nosaucot kopīgās un "
          "atšķirīgās īpašības.")

SATURS = [
    Sakums("Kāpēc telefona ekrāns ir taisnstūris?",
           zimejums=figura([(0, 0), (8, 0), (8, 5), (0, 5)],
                           [(4, -0.7, "a"), (8.8, 2.5, "b")],
                           "taisnstūris"),
           paraksts="Četras malas, pretējās vienādas, visi leņķi taisni.",
           fakti=["Taisnstūrim ir četras malas un četri taisni leņķi.",
                  "Pretējās malas ir vienāda garuma.",
                  "Kvadrāts ir taisnstūris, kuram visas malas vienādas."]),

    Doma("Taisnstūri nosaka trīs pazīmes",
         "Četras malas, pretējās malas vienādas un visi četri leņķi taisni.",
         soli=[
             "Saskaiti malas - tām jābūt četrām.",
             "Pārbaudi, vai pretējās malas ir vienāda garuma.",
             "Pārbaudi ar uzstūri, vai visi leņķi ir taisni.",
             "Ja visas malas vienādas, tas ir kvadrāts.",
         ],
         pieze="Katrs kvadrāts ir taisnstūris, bet ne katrs taisnstūris ir "
               "kvadrāts - tāpat kā katrs ābols ir auglis, bet ne otrādi."),

    Paraugs("Vai šī figūra ir taisnstūris?",
            uzd="Figūrai ir 4 malas: 5 cm, 3 cm, 5 cm, 3 cm, un visi leņķi "
                "taisni. Vai tas ir taisnstūris?",
            soli=[
                ("Četras malas",
                 "Pirmā pazīme izpildās."),
                ("5 = 5 un 3 = 3",
                 "Pretējās malas ir vienādas."),
                ("Visi leņķi taisni",
                 "Trešā pazīme izpildās - tas ir taisnstūris, bet ne "
                 "kvadrāts."),
            ],
            atbilde="taisnstūris"),

    Ievadi("Taisnstūra īpašības", [
        {"jaut": "Cik malu ir taisnstūrim?", "atb": ["4"],
         "padoms": "Četrstūris."},
        {"jaut": "Cik taisnu leņķu ir taisnstūrim?", "atb": ["4"],
         "padoms": "Visi četri."},
        {"jaut": "Taisnstūra malas ir 7 cm un 4 cm. Cik ir perimetrs?",
         "atb": ["22"], "padoms": "2 · 11."},
        {"jaut": "Kvadrāta mala ir 6 cm. Cik ir perimetrs?", "atb": ["24"],
         "padoms": "4 · 6."},
        {"jaut": "Cik virsotņu ir taisnstūrim?", "atb": ["4"],
         "padoms": "Tik, cik malu."},
        {"jaut": "Taisnstūra viena mala 9 cm, perimetrs 30 cm. Cik ir otra "
                 "mala?",
         "atb": ["6"], "padoms": "30 : 2 = 15; 15 − 9."},
    ], pamats=4),

    Zimejums("Kvadrāts",
             figura([(0, 0), (5, 0), (5, 5), (0, 5)],
                    [(2.5, -0.7, "a"), (5.8, 2.5, "a")],
                    "kvadrāts - visas malas vienādas"),
             paskaidro="Kvadrātam visas četras malas ir vienāda garuma, tāpēc "
                       "tam pietiek ar vienu burtu.",
             ievads="Tas ir taisnstūris ar vienādām malām."),

    Varianti("Kura figūra tā ir?", [
        {"jaut": "Vai katrs kvadrāts ir taisnstūris?",
         "opcijas": ["Jā", "Nē", "Tikai mazi", "To nevar pateikt"],
         "pareizi": 0, "padoms": "Kvadrātam izpildās visas trīs pazīmes."},
        {"jaut": "Vai katrs taisnstūris ir kvadrāts?",
         "opcijas": ["Nē", "Jā", "Tikai lieli", "Vienmēr"],
         "pareizi": 0, "padoms": "Malas var būt dažādas."},
        {"jaut": "Kura pazīme taisnstūrim *nav* obligāta?",
         "opcijas": ["Visas malas vienādas", "Četras malas",
                     "Taisni leņķi", "Pretējās malas vienādas"],
         "pareizi": 0, "padoms": "Tā ir kvadrāta pazīme."},
        {"jaut": "Kvadrāta perimetrs ir 28 cm. Cik gara ir viena mala?",
         "opcijas": ["7 cm", "4 cm", "14 cm", "28 cm"],
         "pareizi": 0, "padoms": "28 : 4."},
    ], pamats=4),

    Pasaule("Kāpēc detaļas ir taisnstūrveida?",
            Ievadi("", [
                {"jaut": "Ekrāns ir 16 cm un 9 cm. Cik ir perimetrs?",
                 "atb": ["50"], "padoms": "2 · 25."},
                {"jaut": "Otrs ekrāns ir kvadrāts ar malu 12 cm. Cik ir "
                         "perimetrs?",
                 "atb": ["48"], "padoms": "4 · 12."},
                {"jaut": "Kuram perimetrs ir lielāks? Ieraksti lielāko "
                         "skaitli.",
                 "atb": ["50"], "padoms": "50 > 48."},
                {"jaut": "Cik centimetru ir abu perimetru summa?",
                 "atb": ["98"], "padoms": "50 + 48."},
            ]),
            pavediens="tehnika",
            konteksts="Ekrānus, plates un kastes ražo taisnstūrveida - tās "
                      "ērti salikt blakus bez tukšumiem.",
            kapec="Taisni leņķi ļauj detaļām saskarties precīzi."),

    Kopsavilkums([
        "Raksturoju taisnstūri ar trim pazīmēm.",
        "Zinu, ka kvadrāts ir taisnstūris ar vienādām malām.",
        "Aprēķinu taisnstūra un kvadrāta perimetru.",
        "Atrodu trūkstošo malu, ja zināms perimetrs.",
    ]),

    Majas([
        "Atrodi mājās piecus taisnstūrveida priekšmetus.",
        "Izmēri vienu no tiem un izrēķini perimetru.",
        "Atrodi vienu kvadrātveida priekšmetu.",
    ]),
]
