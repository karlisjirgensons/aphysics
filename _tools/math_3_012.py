# -*- coding: utf-8 -*-
"""3. klase, 12. stunda: «Kā izskatās pabeigta reizināšanas tabula?»

Visas rindas ir apgūtas - tagad tās saliek vienā tabulā un skatās uz to kā
uz veselu. Galvenais atklājums nav atbildes, bet tabulas simetrija: tā ir
spogulis pa diagonāli, un tieši tāpēc iegaumējamā puse ir tikai puse.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kā izskatās pabeigta reizināšanas tabula?"

MERKIS = ("Pabeigsim un pārskatīsim visu reizināšanas tabulu un atradīsim "
          "tajā atkārtojumus.")

SATURS = [
    Sakums("Kur tabulā ir spogulis?",
           zimejums=restis([["·", 6, 7, 8, 9],
                            [6, 36, 42, 48, 54],
                            [7, 42, 49, 56, 63],
                            [8, 48, 56, 64, 72],
                            [9, 54, 63, 72, 81]],
                           "tabulas grūtākais stūris"),
           paraksts="Pa diagonāli tabula ir spogulis: 42 ir divreiz, 56 arī.",
           fakti=["Visa tabula ir 100 reizinājumu, bet dažādu atbilžu - 42.",
                  "Pa diagonāli stāv kvadrāti: 36, 49, 64, 81."]),

    Doma("Tabula ir simetriska pa diagonāli",
         "Kas ir pa kreisi no diagonāles, tas ir arī pa labi - tikai "
         "apgriezts.",
         soli=[
             "Atrodi tabulā diagonāli: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100.",
             "Izvēlies jebkuru rūtiņu vienā pusē.",
             "Atrodi tās spoguļattēlu otrā pusē - skaitlis ir tas pats.",
             "Tāpēc iegaumēt vajag tikai vienu tabulas pusi.",
         ],
         pieze="Uz diagonāles stāv reizinājumi, kuros abi skaitļi ir vienādi. "
               "Tos sauc par *kvadrātiem*, un tiem spoguļattēla nav."),

    Paraugs("Kā tabulā atrast 8 · 7?",
            uzd="Atrodi tabulā reizinājumu 8 · 7 un pasaki, kur ir tā "
                "spoguļattēls.",
            soli=[
                ("Rinda 8, kolonna 7",
                 "Ej pa astotnieku rindu līdz septītajai kolonnai."),
                ("8 · 7 = 56",
                 "Rūtiņā ir atbilde."),
                ("Rinda 7, kolonna 8 - arī 56",
                 "Spoguļattēls otrā diagonāles pusē dod to pašu skaitli."),
            ],
            atbilde="56; abās vietās tas pats"),

    Ievadi("Visa tabula kopā", [
        {"jaut": "8 · 6 = ?", "atb": ["48"], "padoms": "Dubulto 4 · 6."},
        {"jaut": "9 · 7 = ?", "atb": ["63"], "padoms": "70 − 7."},
        {"jaut": "7 · 7 = ?", "atb": ["49"], "padoms": "Kvadrāts uz "
                                                       "diagonāles."},
        {"jaut": "9 · 9 = ?", "atb": ["81"], "padoms": "90 − 9."},
        {"jaut": "8 · 8 = ?", "atb": ["64"], "padoms": "32 + 32."},
        {"jaut": "6 · 6 = ?", "atb": ["36"], "padoms": "30 + 6."},
    ], pamats=4),

    Petijums("Iekrāso tabulas spoguli",
             vajag="reizināšanas tabula uz lapas un divi krāsaini zīmuļi",
             soli=[
                 "Uzzīmē 10 x 10 tabulu un ieraksti visus reizinājumus.",
                 "Iekrāso diagonāli - rūtiņas, kur abi skaitļi ir vienādi.",
                 "Ar otru krāsu iekrāso visu, kas ir zem diagonāles.",
                 "Pārbaudi dažas rūtiņas: vai virs un zem ir tie paši "
                 "skaitļi?",
             ],
             secinajums="Iekrāsotā daļa ir tieši tā puse, kas jāiegaumē - "
                        "pārējo var nolasīt kā spogulī."),

    Zimejums("Kvadrāti uz diagonāles",
             restis([[1, 4, 9, 16, 25],
                     [36, 49, 64, 81, 100]],
                    "1 · 1, 2 · 2, 3 · 3, ..."),
             paskaidro="Šie desmit skaitļi ir vienīgie, kuriem tabulā nav "
                       "spoguļattēla.",
             ievads="Tie ir tabulas mugurkauls."),

    Varianti("Ko rāda tabula?", [
        {"jaut": "Cik reizinājumu ir visā 10 x 10 tabulā?",
         "opcijas": ["100", "50", "81", "10"],
         "pareizi": 0, "padoms": "10 rindas pa 10."},
        {"jaut": "Kuram reizinājumam tabulā *nav* spoguļattēla?",
         "opcijas": ["9 · 9", "9 · 8", "7 · 6", "4 · 5"],
         "pareizi": 0, "padoms": "Abi skaitļi ir vienādi."},
        {"jaut": "Kurš skaitlis tabulā parādās visbiežāk?",
         "opcijas": ["12", "49", "81", "100"],
         "pareizi": 0, "padoms": "12 ir 2 · 6, 6 · 2, 3 · 4 un 4 · 3."},
        {"jaut": "Kur tabulā atrodas 72?",
         "opcijas": ["Rindā 8, kolonnā 9", "Rindā 7, kolonnā 2",
                     "Rindā 6, kolonnā 6", "Rindā 9, kolonnā 9"],
         "pareizi": 0, "padoms": "8 · 9 = 72."},
    ], pamats=4),

    Pasaule("Cik detaļu ir konstruktora kastē?",
            Ievadi("", [
                {"jaut": "Kastē detaļas saliktas 8 rindās pa 9. Cik detaļu "
                         "ir kopā?",
                 "atb": ["72"], "padoms": "8 · 9."},
                {"jaut": "Tās pašas detaļas saliek 9 rindās. Cik to ir "
                         "vienā rindā?",
                 "atb": ["8"], "padoms": "72 : 9."},
                {"jaut": "Otrā kastē ir 7 rindas pa 7 detaļām. Cik detaļu?",
                 "atb": ["49"], "padoms": "7 · 7."},
                {"jaut": "Cik detaļu ir abās kastēs kopā?",
                 "atb": ["121"], "padoms": "72 + 49."},
            ]),
            pavediens="tehnika",
            konteksts="Konstruktoru detaļas rūpnīcā skaita pa rindām - tāpat "
                      "kā reizināšanas tabulā.",
            kapec="Tabula ļauj pārbaudīt iepakojumu, neizberot to uz galda."),

    Kopsavilkums([
        "Pārzinu visu reizināšanas tabulu no 1 līdz 10.",
        "Zinu, ka tabula ir simetriska pa diagonāli.",
        "Atrodu tabulā reizinājumu un tā spoguļattēlu.",
        "Zinu kvadrātus: 36, 49, 64 un 81.",
    ]),

    Majas([
        "Uzzīmē savu reizināšanas tabulu un pakar to virs rakstāmgalda.",
        "Atrodi tabulā visus skaitļus, kas ir lielāki par 50.",
        "Pajautā mājiniekiem trīs reizinājumus un pārbaudi tos tabulā.",
    ]),
]
