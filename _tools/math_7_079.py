# -*- coding: utf-8 -*-
"""7. klase, 79. stunda: «Kāda ir pazīme mmm?»

Trīs malas trijstūri nosaka pilnībā: ar cirkuli no divu galu punktiem
novelkot lokus, trešā virsotne var būt tikai krustpunktā. Tāpēc trijstūri
ar vienādām visām trim malām ir vienādi - pazīme mmm.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Petijums, Sakums, Varianti, Zimejums, geometrija)

TEMA = "Kāda ir pazīme mmm?"

MERKIS = ("Ar cirkuli un lineālu konstruēsim trijstūri pēc trim malām un "
          "formulēsim pazīmi mmm.")

SATURS = [
    Sakums("Kāpēc tilti ir no trijstūriem?",
           zimejums=geometrija([("A", 0, 0), ("B", 6, 0), ("C", 3, 4),
                                ("D", 9, 4), ("E", 12, 0)],
                               nogriezni=["AB", "BC", "CA", "CD", "DB", "BE",
                                          "ED"]),
           paraksts="Kopne no trijstūriem - tā nesaliecas.",
           fakti=["Četrstūris no četriem stieņiem var saplakt.",
                  "Trijstūris no trim stieņiem - nevar.",
                  "Trīs malas nosaka trijstūri pilnībā."]),

    Doma("Pazīme mmm",
         "Ja viena trijstūra trīs malas ir attiecīgi vienādas ar otra "
         "trijstūra trim malām, tad šie trijstūri ir vienādi.",
         soli=[
             "Konstrukcija: uzzīmē nogriezni AB = c.",
             "No A ar cirkuli novelc loku ar rādiusu b.",
             "No B novelc loku ar rādiusu a.",
             "Krustpunkts ir C - trijstūris ABC.",
             "Otrs krustpunkts zem AB dod vienādu, spoguļotu trijstūri.",
         ],
         pieze="Tieši tāpēc konstruējot vienādu leņķi mēs pārnesām trīs "
               "malas - tā strādā pazīme mmm."),

    Petijums("Konstruē pēc trim malām",
             ["Uzzīmē AB = 6 cm.",
              "No A ar cirkuli novelc loku ar rādiusu 5 cm.",
              "No B novelc loku ar rādiusu 4 cm.",
              "Krustpunkts - C. Savieno.",
              "Salīdzini ar klasesbiedru trijstūriem - uzliec vienu otram."],
             vajag="cirkulis, lineāls, papīrs, šķēres",
             secinajums="Visiem klasē trijstūri sakrīt - trīs malas nosaka "
                         "trijstūri."),

    Paraugs("Pierādi ar mmm",
            uzd="Četrstūrī ABCD AB = CD un BC = DA. Pierādi, ka "
                "△ABC = △CDA.",
            soli=[
                ("AB = CD", "(dots)"),
                ("BC = DA", "(dots)"),
                ("AC = CA", "(kopīga mala)"),
                ("△ABC = △CDA", "(mmm)"),
            ],
            atbilde="Pierādīts pēc pazīmes mmm."),

    Zimejums("Kopīgā mala",
             geometrija([("A", 0, 0), ("B", 5, 0), ("C", 7, 3),
                         ("D", 2, 3)],
                        nogriezni=["AB", "BC", "CD", "DA"], izcelti=["AC"],
                        svitras=[("AB", 1), ("CD", 1), ("BC", 2),
                                 ("DA", 2)]),
             paskaidro="Diagonāle AC pieder abiem trijstūriem."),

    Varianti("Pazīme mmm", [
        {"jaut": "△ABC: 3, 4, 5 cm; △KLM: 5, 3, 4 cm. Vai vienādi?",
         "opcijas": ["Jā - malas tās pašas, tikai citā secībā", "Nē"],
         "pareizi": 0, "jaukt": False,
         "padoms": "Atbilstību atrod pēc garumiem."},
        {"jaut": "Kurš elements pierādījumos bieži ir «bez maksas»?",
         "opcijas": ["Kopīga mala", "Taisns leņķis", "Viduspunkts",
                     "Paralēla taisne"],
         "pareizi": 0, "padoms": "Tā ir abiem trijstūriem."},
        {"jaut": "Cik trijstūru var konstruēt pēc malām 6, 5, 4 cm virs "
                 "dotā AB = 6 cm?",
         "opcijas": ["Vienu (un spoguļattēlu zem AB)", "Bezgalīgi daudz",
                     "Nevienu", "Trīs"],
         "pareizi": 0, "padoms": "Loki krustojas 2 punktos."},
    ]),

    Pasaule("Plauktu stiprinājums",
            Varianti("", [
                {"jaut": "Plaukts ļodzās. Ko pieskrūvēt, lai tas vairs "
                         "nekustētos?",
                 "opcijas": ["Diagonālu stieni - veidojas trijstūri",
                             "Vēl vienu plauktu", "Lielākas skrūves",
                             "Neko"],
                 "pareizi": 0,
                 "padoms": "Trijstūris ir ciets."},
                {"jaut": "Kāpēc trijstūris ir ciets?",
                 "opcijas": ["Trīs malas nosaka leņķus - pazīme mmm",
                             "Tam ir 3 stūri", "Tas ir mazs",
                             "Tas ir smags"],
                 "pareizi": 0,
                 "padoms": "Malas nevar mainīt leņķus."},
                {"jaut": "Kurš no šiem ir ciets bez papildu stieņa?",
                 "opcijas": ["Trijstūra rāmis", "Kvadrāta rāmis",
                             "Piecstūra rāmis", "Neviens"],
                 "pareizi": 0,
                 "padoms": "Kvadrāts saplok rombā."},
            ]),
            pavediens="maja",
            konteksts="IKEA plauktu aizmugurē ir plāns dēlis - tas veido "
                      "trijstūrus un neļauj plauktam saplakt.",
            kapec="mmm: trīs malas - viens trijstūris."),

    Kopsavilkums([
        "Konstruēju trijstūri pēc trim malām.",
        "Formulēju pazīmi mmm.",
        "Izmantoju kopīgu malu pierādījumā.",
        "Skaidroju, kāpēc trijstūra konstrukcija ir cieta.",
    ]),

    Majas([
        "Konstruē trijstūri ar malām 7, 5 un 4 cm.",
        "Pierādi, ka rombs sadalās divos vienādos trijstūros.",
        "Uzbūvē no salmiņiem trijstūri un četrstūri un salīdzini.",
    ]),
]
