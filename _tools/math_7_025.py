# -*- coding: utf-8 -*-
"""7. klase, 25. stunda: «Kad divas figūras ir vienādas?»

Divas figūras ir vienādas, ja vienu var uzlikt otrai tā, ka tās sakrīt.
Pārvietot drīkst ar bīdīšanu, pagriešanu un apgriešanu otrādi - bet ne
stiepjot. Vienādām figūrām atbilstošie elementi ir vienādi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, figura,
                         geometrija)

TEMA = "Kad divas figūras ir vienādas?"

MERKIS = ("Uzzināsim, kad figūras ir vienādas, un atradīsim to "
          "atbilstošos elementus.")

SATURS = [
    Sakums("Puzles gabaliņi no rūpnīcas",
           fakti=["Rūpnīca izgriež tūkstošiem vienādu detaļu.",
                  "Detaļas ir vienādas, ja vienu var uzlikt otrai un tās "
                  "sakrīt.",
                  "Pagriezt vai apgriezt otrādi drīkst - stiept nedrīkst."]),

    Doma("Vienādas figūras sakrīt, tās uzliekot",
         "Divas figūras sauc par vienādām, ja tās var novietot tā, ka tās "
         "sakrīt. Vienādām figūrām atbilstošās malas un atbilstošie leņķi "
         "ir vienādi.",
         soli=[
             "Iedomājies, ka vienu figūru pārvieto (bīda, pagriež, "
             "apgriež).",
             "Ja tā pilnībā sakrīt ar otru - figūras ir vienādas.",
             "Virsotnes, kas sakrīt, sauc par atbilstošajām.",
             "Pierakstā atbilstošās virsotnes raksta vienādā secībā: "
             "△ABC = △KLM nozīmē A→K, B→L, C→M.",
         ],
         pieze="Vienādām figūrām ir vienāds laukums, bet figūras ar vienādu "
               "laukumu var nebūt vienādas: 2 × 8 un 4 × 4."),

    Zimejums("Vienādi trijstūri, viens pagriezts",
             geometrija([("A", 0, 0), ("B", 4, 0), ("C", 1, 3),
                         ("K", 9, 3), ("L", 5, 3), ("M", 8, 0)],
                        nogriezni=["AB", "BC", "CA", "KL", "LM", "MK"],
                        svitras=[("AB", 1), ("KL", 1), ("BC", 2), ("LM", 2),
                                 ("CA", 3), ("MK", 3)]),
             paskaidro="△ABC = △KLM: vienādas malas atzīmētas ar vienādu "
                       "svītriņu skaitu."),

    Paraugs("Atbilstošie elementi",
            uzd="△ABC = △KLM. AB = 5 cm, BC = 7 cm, ∠C = 40°. Kuras "
                "△KLM malas un leņķi ir zināmi?",
            soli=[
                ("A → K, B → L, C → M", "Secība pierakstā."),
                ("KL = AB = 5 cm", "Pirmie divi burti."),
                ("LM = BC = 7 cm", "Otrais un trešais burts."),
                ("∠M = ∠C = 40°", "Trešā virsotne."),
            ],
            atbilde="KL = 5 cm, LM = 7 cm, ∠M = 40°"),

    Varianti("Vienādas vai nē?", [
        {"jaut": "Divi kvadrāti ar malu 3 cm",
         "opcijas": ["Vienādi", "Nav vienādi", "Nevar zināt"],
         "pareizi": 0, "jaukt": False,
         "padoms": "Kvadrātu nosaka mala."},
        {"jaut": "Divi taisnstūri ar laukumu 12 cm²",
         "opcijas": ["Vienādi", "Nav vienādi", "Nevar zināt"],
         "pareizi": 2, "jaukt": False,
         "padoms": "3 × 4 un 2 × 6 - abiem 12 cm²."},
        {"jaut": "Divas riņķa līnijas ar rādiusu 5 cm",
         "opcijas": ["Vienādas", "Nav vienādas", "Nevar zināt"],
         "pareizi": 0, "jaukt": False,
         "padoms": "Uzliek centru uz centra."},
        {"jaut": "Figūra un tās spoguļattēls",
         "opcijas": ["Vienādas", "Nav vienādas", "Nevar zināt"],
         "pareizi": 0, "jaukt": False,
         "padoms": "Apgriezt otrādi drīkst."},
    ], pamats=4),

    Ievadi("Nosaki pēc vienādības", [
        {"jaut": "△PQR = △DEF, PQ = 6 cm. Cik cm ir DE?",
         "atb": ["6"], "padoms": "P → D, Q → E."},
        {"jaut": "△PQR = △DEF, ∠R = 55°. Cik grādu ir ∠F?",
         "atb": ["55"], "padoms": "R → F."},
        {"jaut": "△PQR = △DEF, QR = 4 cm, EF = ? cm",
         "atb": ["4"], "padoms": "QR → EF."},
        {"jaut": "Vienādu trijstūru perimetri: viena perimetrs 18 cm. "
                 "Otra perimetrs (cm)?",
         "atb": ["18"], "padoms": "Visas malas vienādas."},
    ]),

    Zimejums("Vienāds laukums - nav vienādas figūras",
             figura([(0, 0), (8, 0), (8, 2), (0, 2)], platums=9, augstums=3),
             paskaidro="2 × 8 = 16 un 4 × 4 = 16, bet taisnstūri nesakrīt."),

    Pasaule("Rezerves daļa",
            Varianti("", [
                {"jaut": "Velosipēda zobratam jābūt vienādam ar veco. Ko "
                         "pietiek pārbaudīt?",
                 "opcijas": ["Vai to var uzlikt vecajam un tie sakrīt",
                             "Vai tam ir tāda pati masa",
                             "Vai tam ir tāda pati krāsa",
                             "Vai tas ir no tā paša veikala"],
                 "pareizi": 0,
                 "padoms": "Definīcija."},
                {"jaut": "Veikalā ir zobrats ar tādu pašu laukumu, bet "
                         "citu formu. Vai tas derēs?",
                 "opcijas": ["Nē - vienāds laukums nenozīmē vienādas "
                             "figūras",
                             "Jā - laukums ir svarīgākais",
                             "Jā, ja masa vienāda",
                             "Nevar zināt"],
                 "pareizi": 0,
                 "padoms": "Skat. taisnstūrus 2 × 8 un 4 × 4."},
                {"jaut": "Rūpnīca izgatavo 1000 vienādu zobratu. Ja viena "
                         "zoba platums ir 4 mm, cik mm tas ir citiem?",
                 "opcijas": ["4 mm", "Katram savs", "40 mm", "Nevar zināt"],
                 "pareizi": 0,
                 "padoms": "Atbilstošie elementi vienādi."},
            ]),
            pavediens="tehnika",
            konteksts="Rezerves daļām jābūt tieši tādām pašām - tas ir "
                      "vienādu figūru uzdevums.",
            kapec="Vienādība nozīmē visu elementu vienādību."),

    Kopsavilkums([
        "Zinu, ka vienādas figūras var novietot tā, ka tās sakrīt.",
        "Atrodu atbilstošās virsotnes pēc pieraksta secības.",
        "Zinu, ka vienādām figūrām atbilstošie elementi ir vienādi.",
        "Zinu, ka vienāds laukums vēl nenozīmē vienādas figūras.",
    ]),

    Majas([
        "Atrodi mājās 3 vienādu priekšmetu pārus.",
        "Uzzīmē divus taisnstūrus ar laukumu 24 cm², kas nav vienādi.",
        "△ABC = △XYZ. Uzraksti visus atbilstošo elementu pārus.",
    ]),
]
