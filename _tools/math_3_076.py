# -*- coding: utf-8 -*-
"""3. klase, 76. stunda: «Cik liela ir viena daļa?»

Nogrieznis, sadalīts vienādās daļās, ir modelis, kurā abi daļas skaitļi ir
redzami reizē: cik daļu ir pavisam un cik liela ir viena. Šī stunda vēl
nemāca pierakstu - tā māca *skatīties*, un pieraksts nāk 81. stundā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         dala, taisne)

TEMA = "Cik liela ir viena daļa?"

MERKIS = ("Vērojot vienādās daļās sadalītu nogriezni, noteiksim daļu skaitu "
          "un vienas daļas lielumu.")

SATURS = [
    Sakums("Cik gara ir viena daļa, ja visa sloksne ir 20 cm?",
           zimejums=taisne(0, 20, 5, [(5, "5"), (10, "10"), (15, "15")]),
           paraksts="Nogrieznis sadalīts četrās vienādās daļās.",
           fakti=["Daļu skaitu redz pēc atzīmēm: 3 atzīmes dod 4 daļas.",
                  "Vienas daļas lielums ir veselais, dalīts ar daļu skaitu."]),

    Doma("Vienas daļas lielums = veselais : daļu skaits",
         "Vispirms saskaiti, cik daļu ir pavisam, tikai tad dali.",
         soli=[
             "Saskaiti daļas - nevis atzīmes, bet posmus starp tām.",
             "Izdali veselā lielumu ar daļu skaitu.",
             "Iegūtais skaitlis ir vienas daļas lielums.",
             "Pārbaudi: daļu skaits reiz vienas daļas lielums dod veselo.",
         ],
         pieze="Atzīmju vienmēr ir par vienu mazāk nekā daļu: trīs atzīmes "
               "sadala nogriezni četrās daļās."),

    Slidnis("Jo vairāk daļu, jo mazāka katra",
            soli=[
                {"v": "2 daļas pa 10 cm", "teksts": "Nogrieznis 20 cm.",
                 "josla": 100},
                {"v": "4 daļas pa 5 cm", "teksts": "Daļu divreiz vairāk.",
                 "josla": 50},
                {"v": "5 daļas pa 4 cm", "teksts": "Vēl vairāk daļu.",
                 "josla": 40},
                {"v": "10 daļas pa 2 cm", "teksts": "Katra daļa jau ļoti maza.",
                 "josla": 20},
            ],
            ievads="Nogrieznis paliek tas pats, mainās tikai daļu skaits."),

    Paraugs("Cik gara ir viena daļa?",
            uzd="Nogrieznis ir 20 cm garš un sadalīts 4 vienādās daļās. Cik "
                "gara ir viena daļa?",
            soli=[
                ("4 daļas",
                 "Trīs atzīmes sadala nogriezni četros posmos."),
                ("20 : 4 = 5",
                 "Veselo dala ar daļu skaitu."),
                ("4 · 5 = 20",
                 "Pārbaude: četras daļas pa 5 cm dod visu nogriezni."),
            ],
            atbilde="5 cm"),

    Ievadi("Cik liela ir viena daļa?", [
        {"jaut": "Nogrieznis 20 cm, 4 daļas. Cik centimetru ir viena daļa?",
         "atb": ["5"], "padoms": "20 : 4."},
        {"jaut": "Nogrieznis 36 cm, 6 daļas. Cik centimetru ir viena daļa?",
         "atb": ["6"], "padoms": "36 : 6."},
        {"jaut": "Nogrieznis 24 cm, 8 daļas. Cik centimetru ir viena daļa?",
         "atb": ["3"], "padoms": "24 : 8."},
        {"jaut": "Viena daļa ir 7 cm, daļu ir 5. Cik garš ir nogrieznis?",
         "atb": ["35"], "padoms": "5 · 7."},
        {"jaut": "Nogrieznis 45 cm, viena daļa 9 cm. Cik daļu ir?",
         "atb": ["5"], "padoms": "45 : 9."},
        {"jaut": "Nogrieznī ir 5 atzīmes. Cik daļu tas ir?",
         "atb": ["6"], "padoms": "Par vienu vairāk nekā atzīmju."},
    ], pamats=4),

    Zimejums("Divas daļas no piecām",
             dala(5, 2, "2/5", "nogrieznis piecās daļās"),
             paskaidro="Iekrāsotas ir divas no piecām vienādām daļām.",
             ievads="Tā izskatās divas piektdaļas."),

    Varianti("Ko rāda modelis?", [
        {"jaut": "Nogrieznī ir 4 atzīmes. Cik daļu tas ir?",
         "opcijas": ["5", "4", "3", "8"],
         "pareizi": 0, "padoms": "Atzīmju ir par vienu mazāk nekā daļu."},
        {"jaut": "Nogrieznis 30 cm, 5 daļas. Cik gara ir viena?",
         "opcijas": ["6 cm", "5 cm", "25 cm", "35 cm"],
         "pareizi": 0, "padoms": "30 : 5."},
        {"jaut": "Kas notiek ar daļas lielumu, ja daļu skaits aug?",
         "opcijas": ["Daļa kļūst mazāka", "Daļa kļūst lielāka",
                     "Nemainās", "To nevar pateikt"],
         "pareizi": 0, "padoms": "Veselais taču paliek tas pats."},
        {"jaut": "Viena daļa ir 4 cm, nogrieznis 32 cm. Cik daļu ir?",
         "opcijas": ["8", "4", "6", "28"],
         "pareizi": 0, "padoms": "32 : 4."},
    ], pamats=4),

    Pasaule("Cik gabalu sanāks no klaipa?",
            Ievadi("", [
                {"jaut": "Maizes klaips ir 40 cm garš, sagriež 8 vienādos "
                         "gabalos. Cik centimetru ir viens?",
                 "atb": ["5"], "padoms": "40 : 8."},
                {"jaut": "Cik gabalu sanāks, ja katrs ir 4 cm?",
                 "atb": ["10"], "padoms": "40 : 4."},
                {"jaut": "Cik centimetru ir 3 gabali pa 5 cm?",
                 "atb": ["15"], "padoms": "3 · 5."},
                {"jaut": "Cik centimetru klaipa palika, ja apēda 3 gabalus "
                         "pa 5 cm?",
                 "atb": ["25"], "padoms": "40 − 15."},
            ]),
            pavediens="virtuve",
            konteksts="Maizi griež vienādos gabalos - un gabala biezums ir "
                      "tieši klaips, dalīts ar gabalu skaitu.",
            kapec="Zinot vienu, otru vienmēr var izrēķināt."),

    Kopsavilkums([
        "Nosaku daļu skaitu, skaitot posmus, ne atzīmes.",
        "Aprēķinu vienas daļas lielumu, dalot veselo ar daļu skaitu.",
        "Atrodu veselo, ja zināma viena daļa un daļu skaits.",
        "Zinu, ka jo vairāk daļu, jo mazāka katra.",
    ]),

    Majas([
        "Uzzīmē 24 cm garu nogriezni un sadali to 6 vienādās daļās.",
        "Izmēri vienu daļu un pārbaudi aprēķinu.",
        "Atrodi mājās kaut ko, kas sadalīts vienādās daļās, un izmēri vienu.",
    ]),
]
