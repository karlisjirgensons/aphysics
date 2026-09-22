# -*- coding: utf-8 -*-
"""6. klase, 106. stunda: «Kādi skaitļi ir starp?»

Uzdevums ar vairākām pareizām atbildēm. Starp diviem skaitļiem veselo ir
ierobežots skaits, bet daļu - bezgalīgi daudz, un tieši šī atšķirība ir
stundas galvenā doma.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kādi skaitļi ir starp?"

MERKIS = ("Iemācīsimies nosaukt vairākus skaitļus starp diviem dotajiem "
          "negatīviem skaitļiem.")

SATURS = [
    Sakums("Starp diviem skaitļiem vienmēr ir vēl kāds",
           zimejums=taisne(-6, -1, 1, [(-4, "−4"), (-3, "−3"), (-2, "−2")]),
           paraksts="Starp −5 un −1 veseli skaitļi ir trīs. Daļu turpat ir "
                    "bezgalīgi daudz.",
           fakti=["Veselo skaitļu starp diviem dotajiem ir ierobežots "
                  "skaits.",
                  "Daļskaitļu starp tiem ir bezgalīgi daudz.",
                  "Robežskaitļi paši parasti netiek ieskaitīti."]),

    Doma("Vispirms veselie, tad daļas",
         "Starp diviem skaitļiem atrodami visi skaitļi, kas uz taisnes ir pa "
         "labi no mazākā un pa kreisi no lielākā.",
         soli=[
             "Nosaki, kurš no dotajiem skaitļiem ir mazāks.",
             "Uzskaiti veselos skaitļus pēc kārtas.",
             "Pārbaudi, vai katrs tiešām ir starp abiem.",
             "Pievieno daļas vai decimāldaļas, ja uzdevums to atļauj.",
             "Pieraksti atbildi augošā secībā.",
         ],
         pieze="Ja robežas ir tuvu - piemēram, starp −1 un 0 -, veselu "
               "skaitļu nav vispār, bet daļu joprojām ir bezgalīgi daudz: "
               "−0,1; −0,5; −{3|4} un citas."),

    Paraugs("Uzskaiti skaitļus starp",
            uzd="Kuri veseli skaitļi atrodas starp −5 un −1?",
            soli=[
                ("Mazākais ir −5, lielākais −1",
                 "Robežas."),
                ("Pa labi no −5: −4; −3; −2",
                 "Uzskaita pēc kārtas."),
                ("−1 pati nav ieskaitīta",
                 "Robeža nav «starp»."),
                ("Atbilde: −4; −3; −2",
                 "Trīs veseli skaitļi."),
            ],
            atbilde="−4; −3; −2"),

    Ievadi("Cik un kuri?", [
        {"jaut": "Cik veselu skaitļu ir starp −5 un −1?",
         "atb": ["3"], "padoms": "−4, −3, −2."},
        {"jaut": "Cik veselu skaitļu ir starp −3 un 2?",
         "atb": ["4"], "padoms": "−2, −1, 0, 1."},
        {"jaut": "Cik veselu skaitļu ir starp −1 un 0?",
         "atb": ["0"], "padoms": "Neviena."},
        {"jaut": "Kurš vesels skaitlis ir tieši pa labi no −4?",
         "atb": ["-3", "−3"], "padoms": "Viens solis pa labi."},
        {"jaut": "Cik veselu skaitļu ir starp −10 un −6?",
         "atb": ["3"], "padoms": "−9, −8, −7."},
        {"jaut": "Ieraksti vienu daļskaitli, kas atrodas starp −1 un 0.",
         "atb": ["-0,5", "−0,5", "-0.5"], "padoms": "Piemēram, puse ar "
                                                    "mīnusu."},
    ], pamats=4),

    Varianti("Kas ir starp?", [
        {"jaut": "Cik veselu skaitļu ir starp −2 un −1?",
         "opcijas": ["Neviena", "Viens", "Divi", "Bezgalīgi daudz"],
         "pareizi": 0,
         "padoms": "Tie ir blakus."},
        {"jaut": "Cik daļskaitļu ir starp −2 un −1?",
         "opcijas": ["Bezgalīgi daudz", "Neviena", "Viens", "Desmit"],
         "pareizi": 0,
         "padoms": "Vienmēr var atrast vidu."},
        {"jaut": "Kurš skaitlis *nav* starp −4 un 1?",
         "opcijas": ["−5", "−3", "0", "−0,5"],
         "pareizi": 0,
         "padoms": "Tas ir pa kreisi no −4."},
        {"jaut": "Vai robežskaitļus ieskaita?",
         "opcijas": ["Parasti nē", "Vienmēr jā",
                     "Tikai negatīvos", "Tikai pozitīvos"],
         "pareizi": 0,
         "padoms": "«Starp» nozīmē starp, ne ieskaitot."},
    ], pamats=4),

    Pasaule("Kuras temperatūras ir iespējamas?",
            Ievadi("", [
                {"jaut": "Prognoze: no −6 °C līdz −2 °C. Cik veselu grādu "
                         "vērtību ir starp tām?",
                 "atb": ["3"], "padoms": "−5, −4, −3."},
                {"jaut": "Cik veselu grādu vērtību ir diapazonā no −6 līdz "
                         "−2, ieskaitot galus?",
                 "atb": ["5"], "padoms": "−6, −5, −4, −3, −2."},
                {"jaut": "Prognoze no −1 °C līdz 3 °C. Cik veselu vērtību ir "
                         "starp tām?",
                 "atb": ["3"], "padoms": "0, 1, 2."},
                {"jaut": "Cik no tām ir zem nulles?",
                 "atb": ["0"], "padoms": "Starp −1 un 3 negatīvu veselo nav."},
            ]),
            pavediens="planeta",
            konteksts="Laika prognozē min diapazonu, un tajā ietilpst gan "
                      "gali, gan viss starp tiem.",
            kapec="«Starp» un «ieskaitot» ir divas dažādas atbildes."),

    Zimejums("Starp −5 un −1",
             taisne(-6, 0, 1, [(-5, "robeža"), (-1, "robeža")]),
             paskaidro="Iekšpusē paliek −4; −3 un −2. Robežskaitļi paši "
                       "netiek ieskaitīti.",
             ievads="Robežas un iekšpuse ir divas dažādas lietas."),

    Kopsavilkums([
        "Nosaucu veselos skaitļus starp diviem dotajiem.",
        "Zinu, ka daļskaitļu starp tiem ir bezgalīgi daudz.",
        "Atšķiru «starp» no «ieskaitot galus».",
        "Pierakstu atbildi augošā secībā.",
    ]),

    Majas([
        "Uzskaiti visus veselos skaitļus starp −8 un −3.",
        "Atrodi trīs daļskaitļus starp −1 un 0.",
        "Pieraksti, cik veselu skaitļu ir starp −100 un −95.",
    ]),
]
