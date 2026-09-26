# -*- coding: utf-8 -*-
"""4. klase, 97. stunda: «Kas ir īsta un kas - neīsta daļa?»

Īsta daļa - skaitītājs mazāks par saucēju, un tā ir starp 0 un 1. Neīsta -
skaitītājs vienāds vai lielāks, tā ir 1 vai vairāk. Uz skaitļu taisnes
neīstās daļas «pārlec» pāri 1 - tas ir galvenais attēls.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala, taisne)

TEMA = "Kas ir īsta un kas - neīsta daļa?"

MERKIS = ("Nošķirsim īstu un neīstu daļu un parādīsim tās uz skaitļu "
          "taisnes.")

SATURS = [
    Sakums("Vai var apēst {5|4} picas?",
           zimejums=taisne(0, 2, 1, [(0.75, "3/4"), (1.25, "5/4")], sikas=4),
           paraksts="{5|4} - viena vesela pica un vēl ceturtdaļa.",
           fakti=["Ja ir divas picas, {5|4} apēst var.",
                  "Šāda daļa ir lielāka par 1 - to sauc par neīstu."]),

    Doma("Īsta < 1, neīsta ≥ 1",
         "Daļa ir īsta, ja skaitītājs mazāks par saucēju; neīsta, ja "
         "skaitītājs vienāds ar saucēju vai lielāks.",
         soli=[
             "Salīdzini skaitītāju ar saucēju.",
             "Skaitītājs < saucējs → īsta daļa, tā ir starp 0 un 1.",
             "Skaitītājs = saucējs → daļa ir 1 (neīsta).",
             "Skaitītājs > saucējs → neīsta daļa, lielāka par 1.",
         ],
         pieze="{7|3} - septiņas trešdaļas - ir vairāk nekā 2 veseli."),

    Zimejums("Divas joslas: {5|4}",
             dala(4, 4, "4/4 = 1", "pirmā pica - visa")
             + dala(4, 1, "1/4", "otrā pica - ceturtdaļa"),
             paskaidro="{5|4} = {4|4} + {1|4} = 1 un vēl {1|4}.",
             ievads="Neīstai daļai vajag vairāk nekā vienu veselo."),

    Paraugs("{7|3} uz taisnes",
            uzd="Kur uz taisnes ir {7|3}?",
            soli=[
                ("{3|3} = 1, {6|3} = 2", "Katras 3 trešdaļas - viens "
                 "vesels."),
                ("{7|3} = 2 un vēl {1|3}", None),
            ],
            atbilde="aiz 2, pirmajā trešdaļā"),

    Varianti("Īsta vai neīsta?", [
        {"jaut": "{3|8}", "opcijas": ["īsta", "neīsta"], "pareizi": 0,
         "padoms": "3 < 8."},
        {"jaut": "{9|4}", "opcijas": ["neīsta", "īsta"], "pareizi": 0,
         "padoms": "9 > 4."},
        {"jaut": "{6|6}", "opcijas": ["neīsta", "īsta"], "pareizi": 0,
         "padoms": "Vienāda ar 1 - neīsta."},
        {"jaut": "{1|100}", "opcijas": ["īsta", "neīsta"], "pareizi": 0,
         "padoms": "1 < 100."},
        {"jaut": "Kura daļa ir lielāka par 1?",
         "opcijas": ["{11|10}", "{10|11}", "{9|10}", "{10|10}"],
         "pareizi": 0, "padoms": "Skaitītājs > saucējs."},
        {"jaut": "Starp kuriem veseliem ir {5|2}?",
         "opcijas": ["2 un 3", "0 un 1", "1 un 2", "5 un 6"], "pareizi": 0,
         "padoms": "{4|2} = 2, {6|2} = 3."},
    ], pamats=4),

    Ievadi("Rēķini ar daļām", [
        {"jaut": "Cik ceturtdaļu ir 2 veselos?", "atb": ["8"],
         "padoms": "2 · 4."},
        {"jaut": "{12|4} = ?", "atb": ["3"], "padoms": "12 : 4."},
        {"jaut": "Mazākais skaitītājs, lai daļa ar saucēju 5 būtu neīsta?",
         "atb": ["5"], "padoms": "Vienāds ar saucēju."},
        {"jaut": "Lielākais skaitītājs, lai daļa ar saucēju 5 būtu īsta?",
         "atb": ["4"], "padoms": "Mazāks par 5."},
    ]),

    Pasaule("Picērijas pasūtījums",
            Ievadi("", [
                {"jaut": "Katrā picā 8 gabali. Klase apēda 19 gabalus. Raksti "
                         "to kā daļu no picas.",
                 "atb": ["19/8"], "vieta": "piem., 1/2",
                 "padoms": "19 astotdaļas."},
                {"jaut": "Cik veselu picu apēsts?", "atb": ["2"],
                 "padoms": "16 gabali = 2 picas."},
                {"jaut": "Cik gabalu no trešās picas?", "atb": ["3"],
                 "padoms": "19 − 16."},
                {"jaut": "Cik gabalu palika no 3 picām?", "atb": ["5"],
                 "padoms": "24 − 19."},
            ]),
            pavediens="virtuve",
            konteksts="Ja ēd vairāk nekā vienu picu, daļa kļūst neīsta - "
                      "un tas ir pilnīgi normāli.",
            kapec="Neīsta daļa vienkārši nozīmē: vairāk nekā viens "
                  "veselais."),

    Kopsavilkums([
        "Nošķiru īstu un neīstu daļu.",
        "Zinu, ka īsta daļa ir starp 0 un 1.",
        "Atlieku neīstu daļu uz taisnes aiz 1.",
    ]),

    Majas([
        "Uzraksti 3 īstas un 3 neīstas daļas ar saucēju 6.",
        "Atliec tās uz taisnes no 0 līdz 2.",
        "Paskaidro kādam, kāpēc {6|6} ir neīsta daļa.",
    ]),
]
