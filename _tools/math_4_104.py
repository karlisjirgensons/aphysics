# -*- coding: utf-8 -*-
"""4. klase, 104. stunda: «Kāda daļa ir starp šīm divām?»

Mikrotemata noslēgums. Starp {1|4} un {2|4} ir citas daļas - piemēram,
{3|8}. Sadalot gabalus sīkāk, starp jebkurām divām daļām atrodas vēl
kāda. Tas ir pirmais solis uz izpratni, ka daļu ir bezgalīgi daudz.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, taisne)

TEMA = "Kāda daļa ir starp šīm divām?"

MERKIS = ("Uzrakstīsim un atliksim uz skaitļu taisnes daļas, kas lielākas "
          "vai mazākas nekā dotā.")

SATURS = [
    Sakums("Kas ir starp {1|4} un {2|4}?",
           zimejums=taisne(0, 1, 1, [(0.25, "1/4"), (3 / 8.0, "3/8"),
                                     (0.5, "2/4")], sikas=8),
           paraksts="{1|4} = {2|8}, {2|4} = {4|8} - starp tām ir {3|8}.",
           fakti=["Sadalot gabalus uz pusēm, parādās jaunas daļas.",
                  "Starp jebkurām divām daļām ir vēl kāda."]),

    Doma("Sadali sīkāk - un vieta atradīsies",
         "Ja starp divām daļām ar vienādu saucēju nav citas, sadali katru "
         "gabalu uz pusēm (divkāršo saucēju un skaitītāju) un meklē vēlreiz.",
         soli=[
             "{1|4} un {2|4} - starpā nav ceturtdaļu.",
             "Pārvērt astotdaļās: {2|8} un {4|8}.",
             "Starpā ir {3|8}.",
             "Vēl sīkāk: sešpadsmitdaļās starpā ir {5|16}, {6|16}, {7|16}.",
         ],
         pieze="Lielāka nekā {3|5} ar to pašu saucēju: {4|5}, {5|5}; mazāka: "
               "{2|5}, {1|5}."),

    Slidnis("Tuvinām taisni",
            soli=[
                {"v": "ceturtdaļas", "zim": taisne(0, 1, 1, [(0.25, "1/4"),
                 (0.5, "2/4")], sikas=4), "teksts": "Starpā nekā nav."},
                {"v": "astotdaļas", "zim": taisne(0, 1, 1, [(0.25, "2/8"),
                 (3 / 8.0, "3/8"), (0.5, "4/8")], sikas=8),
                 "teksts": "Parādās {3|8}."},
                {"v": "sešpadsmitdaļas", "zim": taisne(0, 1, 1, [
                    (5 / 16.0, ""), (6 / 16.0, ""), (7 / 16.0, "")],
                    sikas=16),
                 "teksts": "Vēl trīs daļas starpā."},
            ],
            ievads="Katrā solī iedaļas divreiz sīkākas."),

    Paraugs("Starp {2|3} un 1",
            uzd="Uzraksti daļu, kas ir starp {2|3} un 1.",
            soli=[
                ("{2|3} = {4|6}, 1 = {6|6}", "Sestdaļās."),
                ("{5|6}", "Starpā."),
            ],
            atbilde="{5|6}"),

    Ievadi("Atrodi daļu starpā", [
        {"jaut": "Daļa ar saucēju 8 starp {1|4} un {1|2}. Skaitītājs?",
         "atb": ["3"], "padoms": "{2|8} un {4|8}."},
        {"jaut": "Daļa ar saucēju 10 starp {1|5} un {2|5}. Skaitītājs?",
         "atb": ["3"], "padoms": "{2|10} un {4|10}."},
        {"jaut": "Daļa ar saucēju 6 starp {1|3} un {2|3}. Skaitītājs?",
         "atb": ["3"], "padoms": "{2|6} un {4|6}."},
        {"jaut": "Cik daļu ar saucēju 12 ir starp {1|4} un {1|2}?",
         "atb": ["2"], "padoms": "{3|12} un {6|12}: starpā 4 un 5."},
    ]),

    Varianti("Kura ir starpā?", [
        {"jaut": "Kura daļa ir starp {1|2} un 1?",
         "opcijas": ["{3|4}", "{1|4}", "{1|3}", "{5|4}"], "pareizi": 0,
         "padoms": "{2|4} < {3|4} < {4|4}."},
        {"jaut": "Kura daļa ir starp 0 un {1|5}?",
         "opcijas": ["{1|10}", "{1|4}", "{2|5}", "{1|2}"], "pareizi": 0,
         "padoms": "{1|5} = {2|10}."},
        {"jaut": "Vai starp {1|8} un {2|8} ir kāda daļa?",
         "opcijas": ["jā, piemēram {3|16}", "nē, nav", "tikai {1|8}"],
         "pareizi": 0, "padoms": "{2|16} < {3|16} < {4|16}."},
    ]),

    Pasaule("Tvertnes līmenis",
            Ievadi("", [
                {"jaut": "Ūdens tvertne pildīta starp {1|2} un {3|4}. Ar "
                         "saucēju 8 - kāds skaitītājs starpā?",
                 "atb": ["5"], "padoms": "{4|8} un {6|8}."},
                {"jaut": "Tvertnē 80 l. Cik litru ir {5|8} tvertnes?",
                 "atb": ["50"], "padoms": "80 : 8 · 5."},
                {"jaut": "Cik litru ir {1|2} tvertnes?", "atb": ["40"],
                 "padoms": "80 : 2."},
                {"jaut": "Cik litru ir {3|4} tvertnes?", "atb": ["60"],
                 "padoms": "80 : 4 · 3."},
            ]),
            pavediens="planeta",
            konteksts="Lietus ūdens tvertnes mērogs rāda daļas - un "
                      "dārznieks zina, cik vēl var laistīt.",
            kapec="Starp divām atzīmēm vienmēr ir vēl kāda vērtība."),

    Kopsavilkums([
        "Atrodu daļu starp divām dotām daļām.",
        "Sadalu gabalus sīkāk, ja starpā nekā nav.",
        "Uzrakstu daļas, kas lielākas vai mazākas nekā dotā.",
    ]),

    Majas([
        "Uzraksti 3 daļas starp {1|3} un {1|2}.",
        "Salokot papīra sloksni 2, 4 un 8 daļās, atzīmē {3|8}.",
        "Paskaidro kādam, kāpēc daļu ir bezgalīgi daudz.",
    ]),
]
