# -*- coding: utf-8 -*-
"""3. klase, 65. stunda: «Cik tas ir centimetros?»

Garuma mērvienības ir pirmā vieta, kur reizināšana ar 10 un 100 tiešām
vajadzīga. Skolēns iemācās, kurā virzienā reizina un kurā dala: uz mazāku
vienību - reizina, uz lielāku - dala. Tas pats noteikums der visam kursam.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         restis)

TEMA = "Cik tas ir centimetros?"

MERKIS = ("Izteiksim metrus centimetros un centimetrus milimetros.")

SATURS = [
    Sakums("Cik milimetru ir vienā metrā?",
           zimejums=restis([["1 m", "=", "100 cm"],
                            ["1 cm", "=", "10 mm"],
                            ["1 m", "=", "1000 mm"]],
                           "garuma mērvienības"),
           paraksts="No metra līdz milimetram ir trīs nulles.",
           fakti=["1 m = 100 cm, 1 cm = 10 mm.",
                  "Tātad 1 m = 1000 mm - tieši tikpat, cik gramu kilogramā."]),

    Doma("Uz mazāku vienību - reizina, uz lielāku - dala",
         "Mazāku vienību vajag vairāk, tāpēc skaitlis kļūst lielāks.",
         soli=[
             "Nosaki, vai jaunā vienība ir lielāka vai mazāka.",
             "Ja mazāka - reizini ar 10, 100 vai 1000.",
             "Ja lielāka - dali ar to pašu skaitli.",
             "Pārbaudi: vai atbilde ir loģiska?",
         ],
         pieze="Pārbaudei der vesels teikums: «3 metri ir 300 centimetri» - "
               "centimetru skaitlim jābūt lielākam, jo centimetrs ir mazāks."),

    Slidnis("No metra līdz milimetram",
            soli=[
                {"v": "3 m", "teksts": "Sākums - trīs metri.", "josla": 25},
                {"v": "30 dm", "teksts": "Decimetru ir 10 reizes vairāk.",
                 "josla": 50},
                {"v": "300 cm", "teksts": "Centimetru - vēl 10 reizes vairāk.",
                 "josla": 75},
                {"v": "3000 mm", "teksts": "Milimetru - vēl 10 reizes vairāk.",
                 "josla": 100},
            ],
            ievads="Katrā solī vienība kļūst mazāka, bet skaitlis - lielāks."),

    Paraugs("Cik centimetru ir 4 m 25 cm?",
            uzd="Izsaki 4 m 25 cm centimetros.",
            soli=[
                ("4 · 100 = 400",
                 "Metrus pārvērš centimetros."),
                ("400 + 25 = 425",
                 "Pieskaita atlikušos centimetrus."),
                ("4 m 25 cm = 425 cm",
                 "Atbilde vienā mērvienībā."),
            ],
            atbilde="425 cm"),

    Ievadi("Pārvērt mērvienības", [
        {"jaut": "Cik centimetru ir 3 m?", "atb": ["300"],
         "padoms": "3 · 100."},
        {"jaut": "Cik milimetru ir 7 cm?", "atb": ["70"],
         "padoms": "7 · 10."},
        {"jaut": "Cik centimetru ir 2 m 40 cm?", "atb": ["240"],
         "padoms": "200 + 40."},
        {"jaut": "Cik metru ir 500 cm?", "atb": ["5"],
         "padoms": "500 : 100."},
        {"jaut": "Cik centimetru ir 120 mm?", "atb": ["12"],
         "padoms": "120 : 10."},
        {"jaut": "Cik milimetru ir 1 m?", "atb": ["1000"],
         "padoms": "100 cm pa 10 mm."},
    ], pamats=4),

    Zimejums("Mērvienību kāpnes",
             restis([["mm", "cm", "dm", "m"],
                     ["· 10 →", "· 10 →", "· 10 →", ""]],
                    "uz lielāku - dala, uz mazāku - reizina"),
             paskaidro="Katrs pakāpiens ir 10 reizes: no milimetra līdz "
                       "metram ir trīs pakāpieni.",
             ievads="Šīs kāpnes vērts atcerēties."),

    Varianti("Reizināt vai dalīt?", [
        {"jaut": "Metrus pārvēršot centimetros, ko dara?",
         "opcijas": ["Reizina ar 100", "Dala ar 100", "Reizina ar 10",
                     "Dala ar 10"],
         "pareizi": 0, "padoms": "Centimetrs ir mazāks, tāpēc to ir vairāk."},
        {"jaut": "Cik centimetru ir 6 m 5 cm?",
         "opcijas": ["605 cm", "65 cm", "650 cm", "6005 cm"],
         "pareizi": 0, "padoms": "600 + 5."},
        {"jaut": "Cik milimetru ir 25 cm?",
         "opcijas": ["250 mm", "25 mm", "2500 mm", "2,5 mm"],
         "pareizi": 0, "padoms": "25 · 10."},
        {"jaut": "Kurš garums ir vislielākais?",
         "opcijas": ["1 m", "90 cm", "500 mm", "9 dm"],
         "pareizi": 0, "padoms": "Pārvērt visus centimetros."},
    ], pamats=4),

    Pasaule("Cik gara ir ceļasoma?",
            Ievadi("", [
                {"jaut": "Soma ir 55 cm gara. Cik milimetru tas ir?",
                 "atb": ["550"], "padoms": "55 · 10."},
                {"jaut": "Lidmašīnā drīkst somu līdz 1 m. Cik centimetru "
                         "tas ir?",
                 "atb": ["100"], "padoms": "1 · 100."},
                {"jaut": "Par cik centimetriem soma ir īsāka par atļauto?",
                 "atb": ["45"], "padoms": "100 − 55."},
                {"jaut": "Otra soma ir 1 m 20 cm. Cik centimetru tas ir?",
                 "atb": ["120"], "padoms": "100 + 20."},
            ]),
            pavediens="celojums",
            konteksts="Lidostā bagāžas izmērus mēra centimetros, bet "
                      "noteikumos tos raksta metros.",
            kapec="Bez pārrēķina nevar pateikt, vai soma vispār ietilps."),

    Kopsavilkums([
        "Izsaku metrus centimetros un centimetrus milimetros.",
        "Zinu, ka uz mazāku vienību reizina, uz lielāku - dala.",
        "Pārvēršu jauktu pierakstu (2 m 40 cm) vienā mērvienībā.",
        "Salīdzinu garumus, izteiktus dažādās mērvienībās.",
    ]),

    Majas([
        "Izmēri savu augumu centimetros un pieraksti to arī milimetros.",
        "Izmēri galda garumu un izsaki to metros un centimetros.",
        "Atrodi mājās priekšmetu, kas ir apmēram 1 dm garš.",
    ]),
]
