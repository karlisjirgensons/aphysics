# -*- coding: utf-8 -*-
"""4. klase, 55. stunda: «Kā apzīmē leņķi?»

Leņķi apzīmē ar trim burtiem, virsotni rakstot vidū: ∠ABC, vai ar vienu -
∠B, ja pārpratumu nav. Tas ir pirmais ģeometrijas pieraksts, ko skolēns
lietos līdz 9. klasei, tāpēc stunda trenē tieši to - kur liek virsotni.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, figura, lenkis)

TEMA = "Kā apzīmē leņķi?"

MERKIS = ("Nosauksim un pierakstīsim leņķus ar pieņemtajiem apzīmējumiem un "
          "noteiksim leņķa virsotni un malas.")

SATURS = [
    Sakums("Kā pateikt, kuru leņķi domā?",
           zimejums=lenkis([(0, "B"), (50, "A")], loki=[(0, 50, "")]),
           paraksts="Virsotne C ir punkts, kur malas satiekas: ∠ACB.",
           fakti=["Leņķa zīme ir ∠.",
                  "Trīs burti: punkts uz malas, virsotne, punkts uz malas.",
                  "Virsotnes burts vienmēr ir vidū."]),

    Doma("Virsotne vidū",
         "Leņķi apzīmē ∠ABC: A un C ir punkti uz malām, B - virsotne; to "
         "pašu leņķi var saukt arī ∠CBA vai īsi ∠B.",
         soli=[
             "Atrodi virsotni - tur satiekas malas.",
             "Izvēlies pa punktam uz katras malas.",
             "Raksti: punkts - virsotne - punkts.",
             "Ja virsotnē ir tikai viens leņķis, pietiek ar ∠B.",
         ],
         pieze="∠ABC un ∠BAC ir dažādi leņķi - pirmajā virsotne B, otrajā - "
               "A."),

    Zimejums("Trijstūra leņķi",
             figura([(1, 1), (10, 1), (4, 6)],
                    uzraksti=[(0.4, 0.5, "A"), (10.6, 0.5, "B"),
                              (4, 6.7, "C")],
                    platums=11, augstums=7),
             paskaidro="∠A = ∠BAC, ∠B = ∠ABC, ∠C = ∠ACB.",
             ievads="Trijstūrī ABC ir trīs leņķi - katrs savā virsotnē."),

    Paraugs("Nosauc leņķi pie C",
            uzd="Trijstūrī ABC nosauc leņķi ar virsotni C trijos veidos.",
            soli=[
                ("∠ACB", "Virsotne C vidū."),
                ("∠BCA", "Tas pats leņķis, no otras malas."),
                ("∠C", "Īsi - C virsotnē ir tikai viens leņķis."),
            ],
            atbilde="∠ACB = ∠BCA = ∠C"),

    Varianti("Kura ir virsotne?", [
        {"jaut": "Kura ir virsotne leņķim ∠KLM?",
         "opcijas": ["L", "K", "M", "KM"], "pareizi": 0,
         "padoms": "Vidējais burts."},
        {"jaut": "Kurš pieraksts ir tas pats, kas ∠PQR?",
         "opcijas": ["∠RQP", "∠QPR", "∠PRQ", "∠QRP"], "pareizi": 0,
         "padoms": "Q jāpaliek vidū."},
        {"jaut": "∠DEF malas ir...",
         "opcijas": ["ED un EF", "DE un DF", "FD un FE", "DF un EF"],
         "pareizi": 0, "padoms": "Malas iet no virsotnes E."},
        {"jaut": "Trijstūrī ABC leņķis pie virsotnes A ir...",
         "opcijas": ["∠BAC", "∠ABC", "∠ACB", "∠CBA"], "pareizi": 0,
         "padoms": "A vidū."},
    ], pamats=4),

    Ievadi("Burti un leņķi", [
        {"jaut": "Kvadrātam ABCD - cik leņķu var nosaukt ar vienu burtu?",
         "atb": ["4"], "padoms": "Katrā virsotnē viens."},
        {"jaut": "Ieraksti virsotnes burtu leņķim ∠XYZ.",
         "atb": ["Y", "y"], "tastatura": "text", "padoms": "Vidējais."},
        {"jaut": "Ieraksti virsotni leņķim ∠MNK.", "atb": ["N", "n"],
         "tastatura": "text", "padoms": "Vidējais."},
        {"jaut": "Cik dažādos veidos ar trim burtiem var nosaukt vienu "
                 "leņķi?", "atb": ["2"], "padoms": "∠ABC un ∠CBA."},
    ]),

    Pasaule("Jumta leņķis",
            Varianti("", [
                {"jaut": "Mājas jumta virsotne ir punkts K, jumta malas iet uz "
                         "L un M. Kā apzīmē jumta leņķi?",
                 "opcijas": ["∠LKM", "∠KLM", "∠LMK"], "pareizi": 0,
                 "padoms": "Virsotne K vidū."},
                {"jaut": "Stāvākam jumtam leņķis ∠LKM ir...",
                 "opcijas": ["mazāks", "lielāks", "tāds pats"],
                 "pareizi": 0, "padoms": "Malas ir tuvāk viena otrai."},
                {"jaut": "Skandināvijā jumti stāvi - lai sniegs...",
                 "opcijas": ["noslīd", "paliek", "izkūst ātrāk"],
                 "pareizi": 0, "padoms": "Stāvā jumtā sniegs neturas."},
            ]),
            pavediens="maja",
            konteksts="Arhitekti rasējumos leņķus apzīmē ar burtiem - tā visi "
                      "celtnieki saprot vienādi.",
            kapec="Precīzs apzīmējums novērš pārpratumus būvē."),

    Kopsavilkums([
        "Apzīmēju leņķi ar trim burtiem, virsotni rakstot vidū.",
        "Lietoju īso apzīmējumu ∠B, ja nav pārpratumu.",
        "Nosaucu leņķa malas.",
    ]),

    Majas([
        "Uzzīmē četrstūri KLMN un pieraksti visus tā leņķus.",
        "Uzzīmē jumta leņķi un apzīmē to ar burtiem.",
        "Paskaidro kādam, kāpēc virsotnes burts ir vidū.",
    ]),
]
