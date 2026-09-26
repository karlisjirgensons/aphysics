# -*- coding: utf-8 -*-
"""3. klase, 53. stunda: «Kā pateikt formulu ar vārdiem?»

Pirms burtiem - vārdi. Skolēns formulē perimetra aprēķinu tā, lai to varētu
izpildīt jebkurš taisnstūris, nevis tikai tas, kas uzzīmēts uz tāfeles. Tieši
šī vispārināšana ir formulas jēga, un burti to tikai saīsina.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kā pateikt formulu ar vārdiem?"

MERKIS = ("Formulēsim taisnstūra perimetra aprēķināšanu vārdiski tā, lai tā "
          "derētu jebkuram taisnstūrim.")

SATURS = [
    Sakums("Kā pateikt vienu noteikumu visiem taisnstūriem?",
           zimejums=restis([["6 x 4", "→", "20"],
                            ["7 x 3", "→", "20"],
                            ["9 x 2", "→", "22"]],
                           "dažādi taisnstūri, viens noteikums"),
           paraksts="Katram sava atbilde, bet rēķins ir viens un tas pats.",
           fakti=["Formula ir noteikums, kas der visiem gadījumiem.",
                  "Vispirms to pasaka vārdiem, tad pieraksta ar burtiem."]),

    Doma("Formula ir noteikums, ne viens rēķins",
         "«Saskaita garumu un platumu un summu reizina ar divi» - šis "
         "teikums der jebkuram taisnstūrim.",
         soli=[
             "Pasaki, kurus lielumus ņem: garumu un platumu.",
             "Pasaki, ko ar tiem dara: saskaita.",
             "Pasaki, ko dara tālāk: summu reizina ar 2.",
             "Pārbaudi teikumu uz diviem dažādiem taisnstūriem.",
         ],
         pieze="Ja teikumā parādās kāds konkrēts skaitlis, piemēram «reizina "
               "sešus ar diviem», tā vēl nav formula - tas ir viens rēķins."),

    Paraugs("Vai teikums der visiem?",
            uzd="Pārbaudi teikumu «perimetrs ir garuma un platuma summa, "
                "reizināta ar 2» uz taisnstūriem 6 x 4 un 9 x 2.",
            soli=[
                ("6 + 4 = 10; 2 · 10 = 20",
                 "Pirmais taisnstūris."),
                ("9 + 2 = 11; 2 · 11 = 22",
                 "Otrais taisnstūris."),
                ("Abi reizi teikums derēja",
                 "Tātad tā ir formula, nevis viens rēķins."),
            ],
            atbilde="20 cm un 22 cm; teikums der abiem"),

    Petijums("Pārbaudi savu formulējumu",
             vajag="lapa, lineāls un zīmulis",
             soli=[
                 "Uzraksti savu teikumu par perimetra aprēķināšanu.",
                 "Uzzīmē trīs dažādus taisnstūrus.",
                 "Izrēķini katram perimetru pēc sava teikuma.",
                 "Pārbaudi, saskaitot visas četras malas.",
             ],
             secinajums="Ja visas trīs reizes sakrita, teikums ir formula - "
                        "un to var lietot arī turpmāk."),

    Ievadi("Lieto formulu", [
        {"jaut": "Garums 8 cm, platums 5 cm. Cik ir perimetrs?",
         "atb": ["26"], "padoms": "2 · 13."},
        {"jaut": "Garums 11 cm, platums 4 cm. Cik ir perimetrs?",
         "atb": ["30"], "padoms": "2 · 15."},
        {"jaut": "Garums 9 cm, platums 9 cm. Cik ir perimetrs?",
         "atb": ["36"], "padoms": "2 · 18 jeb 4 · 9."},
        {"jaut": "Perimetrs 24 cm, garums 8 cm. Cik ir platums?",
         "atb": ["4"], "padoms": "24 : 2 = 12; 12 − 8."},
        {"jaut": "Garums 15 cm, platums 5 cm. Cik ir perimetrs?",
         "atb": ["40"], "padoms": "2 · 20."},
        {"jaut": "Perimetrs 30 cm, platums 6 cm. Cik ir garums?",
         "atb": ["9"], "padoms": "30 : 2 = 15; 15 − 6."},
    ], pamats=4),

    Zimejums("Formula un viens rēķins",
             restis([["formula", "viens rēķins"],
                     ["garums + platums, reiz 2", "6 + 4, reiz 2"],
                     ["der visiem", "der vienam"]],
                    "kāda ir atšķirība"),
             paskaidro="Formulā skaitļu nav - ir tikai lielumu nosaukumi.",
             ievads="Salīdzini abas kolonnas."),

    Varianti("Kurš teikums ir formula?", [
        {"jaut": "Kurš teikums ir formula?",
         "opcijas": ["Garuma un platuma summu reizina ar 2",
                     "Sešus un četrus saskaita un reizina ar 2",
                     "Perimetrs ir 20", "Malas ir 6 un 4"],
         "pareizi": 0, "padoms": "Formulā konkrētu skaitļu nav."},
        {"jaut": "Kurš teikums der kvadrātam?",
         "opcijas": ["Malas garumu reizina ar 4", "Malas garumu reizina ar 2",
                     "Malas garumu saskaita ar 4", "Malas garumu dala ar 4"],
         "pareizi": 0, "padoms": "Kvadrātam visas četras malas vienādas."},
        {"jaut": "Garums 10 cm, platums 3 cm. Cik ir perimetrs?",
         "opcijas": ["26 cm", "30 cm", "13 cm", "20 cm"],
         "pareizi": 0, "padoms": "2 · 13."},
        {"jaut": "Kā pārbaudīt, vai teikums ir formula?",
         "opcijas": ["Izmēģināt to uz vairākiem taisnstūriem",
                     "Izlasīt to skaļi", "Pajautāt draugam",
                     "Pārrakstīt skaistāk"],
         "pareizi": 0, "padoms": "Formulai jāder visiem gadījumiem."},
    ], pamats=4),

    Pasaule("Cik tapetes līstes vajag katrai istabai?",
            Ievadi("", [
                {"jaut": "Istaba 6 m un 4 m. Cik metru ir perimetrs?",
                 "atb": ["20"], "padoms": "2 · 10."},
                {"jaut": "Istaba 5 m un 5 m. Cik metru ir perimetrs?",
                 "atb": ["20"], "padoms": "4 · 5."},
                {"jaut": "Istaba 8 m un 3 m. Cik metru ir perimetrs?",
                 "atb": ["22"], "padoms": "2 · 11."},
                {"jaut": "Cik metru līstes vajag visām trim istabām?",
                 "atb": ["62"], "padoms": "20 + 20 + 22."},
            ]),
            pavediens="maja",
            konteksts="Remonta tāmē katrai istabai rēķina pēc viena un tā "
                      "paša noteikuma - tikai skaitļi ir citi.",
            kapec="Tieši tāpēc formulu ir vērts iemācīties vienu reizi."),

    Kopsavilkums([
        "Formulēju taisnstūra perimetra aprēķinu vārdiski.",
        "Zinu, ka formulā nedrīkst būt konkrētu skaitļu.",
        "Pārbaudu savu formulējumu uz vairākiem taisnstūriem.",
        "Atrodu trūkstošo malu, ja zināms perimetrs.",
    ]),

    Majas([
        "Uzraksti savu formulējumu perimetram un pārbaudi to trīs reizes.",
        "Uzraksti formulējumu arī kvadrātam.",
        "Izmēri kādu mājas priekšmetu un izrēķini tā perimetru.",
    ]),
]
