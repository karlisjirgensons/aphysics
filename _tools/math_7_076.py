# -*- coding: utf-8 -*-
"""7. klase, 76. stunda: «Kā ar locīšanu iegūt vienādus trijstūrus?»

Salokot papīra lapu, divi tās gabali sakrīt - tātad tie ir vienādi. Ja
locījuma līnija iet caur trijstūra virsotni un pretējās malas viduspunktu
vienādsānu trijstūrī, iegūst divus vienādus trijstūrus. Stunda to dara ar
rokām un pamato.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Petijums, Sakums, Varianti, Zimejums, geometrija)

TEMA = "Kā ar locīšanu iegūt vienādus trijstūrus?"

MERKIS = ("Ar locīšanu iegūsim vienādus trijstūrus un pamatosim to "
          "vienādību.")

_TAISNSTURIS = geometrija([("A", 0, 0), ("B", 6, 0), ("C", 6, 4),
                           ("D", 0, 4)],
                          nogriezni=["AB", "BC", "CD", "DA"],
                          izcelti=["AC"],
                          iekrasot=[("ABC", 0), ("ACD", 1)])

SATURS = [
    Sakums("Salvete, pārlocīta pa diagonāli",
           zimejums=_TAISNSTURIS,
           paraksts="Pārgriežot pa diagonāli AC, iegūst divus trijstūrus.",
           fakti=["Kvadrātveida salveti pārloka pa diagonāli - puses "
                  "sakrīt.",
                  "Taisnstūrim pa diagonāli pārlocīt nesanāk - bet pagriežot "
                  "sakrīt.",
                  "Sakrītoši trijstūri ir vienādi."]),

    Doma("Sakrīt - tātad vienādi",
         "Ja, pārlokot vai pagriežot, viens trijstūris pilnībā sakrīt ar "
         "otru, tie ir vienādi. Tad vienādas ir visas atbilstošās malas un "
         "visi atbilstošie leņķi.",
         soli=[
             "Saloki vai pagriez tā, lai viena figūra nonāk uz otras.",
             "Pieraksti, kura virsotne nonāca kurā.",
             "Uzraksti vienādību ar atbilstošo virsotņu secību.",
             "Uzraksti vienādās malas un leņķus.",
         ],
         pieze="Locīšana ir spoguļattēls pret locījuma līniju - tā saglabā "
               "garumus un leņķus."),

    Petijums("Loki un griez",
             ["Izgriez no papīra vienādsānu trijstūri ABC (AC = BC).",
              "Saloki to tā, lai A nonāk uz B.",
              "Locījuma līnija iet caur C - atzīmē, kur tā krusto AB (punkts "
              "M).",
              "Salīdzini: AM un MB, ∠ACM un ∠BCM, ∠AMC un ∠BMC."],
             vajag="papīrs, šķēres, lineāls, transportieris",
             secinajums="△AMC = △BMC: AM = MB, ∠ACM = ∠BCM, un "
                         "∠AMC = ∠BMC = 90°."),

    Zimejums("Vienādsānu trijstūris, pārlocīts",
             geometrija([("A", 0, 0), ("B", 6, 0), ("C", 3, 4),
                         ("M", 3, 0, -90)],
                        nogriezni=["AB", "BC", "CA"], izcelti=["CM"],
                        svitras=[("AC", 1), ("BC", 1), ("AM", 2),
                                 ("MB", 2)],
                        taisni=["CMB"]),
             paskaidro="Locījuma līnija CM sadala trijstūri divos vienādos."),

    Paraugs("Pamato vienādību",
            uzd="Taisnstūri ABCD sagriež pa diagonāli AC. Pamato, ka "
                "△ABC = △CDA.",
            soli=[
                ("Pagriežam △ABC par 180° ap AC viduspunktu",
                 "A nonāk C, C nonāk A."),
                ("B nonāk D", "Taisnstūra simetrija."),
                ("△ABC sakrīt ar △CDA", "Visi punkti sakrīt."),
                ("AB = CD, BC = DA, ∠B = ∠D", "Atbilstošie elementi."),
            ],
            atbilde="△ABC = △CDA"),

    Varianti("Kas ir vienāds?", [
        {"jaut": "△KLM = △PQR. Kura mala ir vienāda ar LM?",
         "opcijas": ["QR", "PQ", "PR", "Nevar zināt"],
         "pareizi": 0, "padoms": "2. un 3. burts."},
        {"jaut": "Pēc locīšanas A nonāca B, C - pats sevī. Kā pierakstīt?",
         "opcijas": ["△AMC = △BMC", "△AMC = △CMB", "△ACM = △BMA",
                     "△ABC = △CBA"],
         "pareizi": 0, "padoms": "A ↔ B, M un C paliek."},
        {"jaut": "Vai divi trijstūri ar vienādu laukumu vienmēr sakrīt?",
         "opcijas": ["Nē", "Jā", "Tikai taisnleņķa"],
         "pareizi": 0, "jaukt": False,
         "padoms": "Forma var atšķirties."},
    ]),

    Pasaule("Origami lidmašīna",
            Varianti("", [
                {"jaut": "Lidmašīnas spārnus loka simetriski. Kāpēc tas "
                         "svarīgi?",
                 "opcijas": ["Vienādi spārni - lidmašīna nesagriežas",
                             "Tā ir skaistāk", "Papīrs ir smagāks",
                             "Tā ātrāk krīt"],
                 "pareizi": 0, "padoms": "Vienāda cēlējspēka dēļ."},
                {"jaut": "Kā pārbaudīt, ka spārni vienādi?",
                 "opcijas": ["Salocīt lidmašīnu pa vidu - spārniem jāsakrīt",
                             "Nosvērt", "Nomērīt tikai garumu",
                             "Nopūst"],
                 "pareizi": 0, "padoms": "Locīšanas pārbaude."},
                {"jaut": "Ja viens spārns par 5 mm platāks, kas notiks?",
                 "opcijas": ["Lidmašīna sagriezīsies uz sāniem",
                             "Nekas", "Lidos taisnāk",
                             "Nelidos vispār"],
                 "pareizi": 0, "padoms": "Nav vienādi."},
            ]),
            pavediens="tehnika",
            konteksts="Origami un aviācijā simetrija ir lidošanas noteikums.",
            kapec="Locīšana ir vienkāršākais vienādības tests."),

    Kopsavilkums([
        "Iegūstu vienādus trijstūrus ar locīšanu un griešanu.",
        "Pierakstu atbilstošās virsotnes pareizā secībā.",
        "Uzskaitu vienādās malas un leņķus.",
        "Zinu, ka locīšana saglabā garumus un leņķus.",
    ]),

    Majas([
        "Salokot papīru, iegūsti 4 vienādus trijstūrus.",
        "Uzraksti visus vienādos elementus.",
        "Izveido origami lidmašīnu un pārbaudi simetriju.",
    ]),
]
