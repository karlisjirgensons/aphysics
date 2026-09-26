# -*- coding: utf-8 -*-
"""4. klase, 96. stunda: «Kad daļa ir vienāda ar vienu?»

Ja skaitītājs un saucējs vienādi, ir paņemtas visas daļas - veselais.
{4|4} = {8|8} = {100|100} = 1. Šī vienkāršā doma ir pamats īstām un
neīstām daļām un papildinājumam līdz veselam.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Sakums, Slidnis, Varianti, dala)

TEMA = "Kad daļa ir vienāda ar vienu?"

MERKIS = ("Paskaidrosim, ka daļa, kurai skaitītājs un saucējs vienādi, ir "
          "viens, un minēsim piemērus.")

SATURS = [
    Sakums("Visa pica apēsta - cik tas ir?",
           zimejums=dala(8, 8, "8/8 = 1", "visi 8 gabali"),
           paraksts="Astoņas astotdaļas ir viena vesela pica.",
           fakti=["Ja paņemtas visas daļas, ir viss veselais.",
                  "Tāpēc {8|8} = 1."]),

    Doma("Visas daļas kopā ir viens",
         "Daļa ar vienādu skaitītāju un saucēju ir vienāda ar 1: "
         "{n|n} = 1.",
         soli=[
             "Saucējs pasaka, cik daļu ir veselajā.",
             "Ja skaitītājs tikpat liels, paņemtas visas.",
             "Visas daļas kopā ir veselais - 1.",
             "Uz taisnes šāda daļa ir tieši pie 1.",
         ],
         pieze="{2|2} = {3|3} = {10|10} = 1 - daudz pierakstu, viens "
               "skaitlis."),

    Slidnis("Josla pildās",
            soli=[
                {"v": "{1|5}", "zim": dala(5, 1), "teksts": "Viena daļa."},
                {"v": "{3|5}", "zim": dala(5, 3), "teksts": "Trīs daļas."},
                {"v": "{5|5} = 1", "zim": dala(5, 5),
                 "teksts": "Visas daļas - veselais!"},
            ],
            ievads="Kad skaitītājs panāk saucēju, josla ir pilna."),

    Ievadi("Cik trūkst līdz 1?", [
        {"jaut": "{5|5} = ?", "atb": ["1"], "padoms": "Visas daļas."},
        {"jaut": "{?|7} = 1. Kāds skaitītājs?", "atb": ["7"],
         "padoms": "Vienāds ar saucēju."},
        {"jaut": "{12|?} = 1. Kāds saucējs?", "atb": ["12"],
         "padoms": "Vienāds ar skaitītāju."},
        {"jaut": "Kūka 6 gabalos, visi apēsti. Kāda daļa apēsta? Raksti "
                 "daļu.", "atb": ["6/6", "1"], "vieta": "piem., 1/2",
         "padoms": "{6|6} = 1."},
    ]),

    Varianti("Viens vai nē?", [
        {"jaut": "Kura daļa ir vienāda ar 1?",
         "opcijas": ["{9|9}", "{1|9}", "{9|1}", "{8|9}"], "pareizi": 0,
         "padoms": "Vienādi skaitītājs un saucējs."},
        {"jaut": "Vai {100|100} = 1?",
         "opcijas": ["jā", "nē"], "pareizi": 0,
         "padoms": "Visas 100 daļas."},
        {"jaut": "Kura daļa *nav* 1?",
         "opcijas": ["{3|4}", "{4|4}", "{2|2}", "{7|7}"], "pareizi": 0,
         "padoms": "Trūkst vienas ceturtdaļas."},
        {"jaut": "Kur uz taisnes ir {6|6}?",
         "opcijas": ["pie 1", "pie 0", "pie 6", "pusē"], "pareizi": 0,
         "padoms": "{6|6} = 1."},
    ], pamats=4),

    Pasaule("Tortes svētkos",
            Ievadi("", [
                {"jaut": "Torte sagriezta 12 gabalos. Viesi apēda 12. Kāda "
                         "daļa apēsta? (raksti daļu)",
                 "atb": ["12/12", "1"], "vieta": "piem., 1/2",
                 "padoms": "Visa torte."},
                {"jaut": "Otra torte 10 gabalos, apēsti 7. Cik gabalu līdz "
                         "veselai tortei?",
                 "atb": ["3"], "padoms": "10 − 7."},
                {"jaut": "Kāda daļa no otrās tortes palika?",
                 "atb": ["3/10"], "vieta": "piem., 1/2", "padoms": "3 no 10."},
                {"jaut": "Cik veselu tortu ir 24 gabalos, ja tortē 12 gabali?",
                 "atb": ["2"], "padoms": "24 : 12."},
            ]),
            pavediens="virtuve",
            konteksts="Svētkos tortes griež vienādos gabalos - un tad skaita, "
                      "cik daļu vēl palicis.",
            kapec="Kas zina, ka {12|12} = 1, tas zina, kad torte beigusies."),

    Kopsavilkums([
        "Zinu, ka daļa ar vienādu skaitītāju un saucēju ir 1.",
        "Minu piemērus: {2|2}, {5|5}, {100|100}.",
        "Atrodu, cik daļu trūkst līdz veselajam.",
    ]),

    Majas([
        "Sagriez ābolu 4 daļās un pierakstiet ar ģimeni: {4|4} = 1.",
        "Atrodi mājās 3 lietas, kas sadalītas vienādās daļās.",
        "Uzraksti 5 dažādas daļas, kas visas ir 1.",
    ]),
]
