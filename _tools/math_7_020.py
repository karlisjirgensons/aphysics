# -*- coding: utf-8 -*-
"""7. klase, 20. stunda: «Kāpēc punktu nevar definēt?»

Katru jēdzienu definē ar citiem, jau zināmiem jēdzieniem. Ja tā iet
atpakaļ, kaut kur jāapstājas - pie pamatjēdzieniem, ko nedefinē: punkts,
taisne, plakne. Tos raksturo ar modeļiem un pamatīpašībām (aksiomām).
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, Zimejums, geometrija, restis)

TEMA = "Kāpēc punktu nevar definēt?"

MERKIS = ("Sapratīsim, kāpēc punktu, taisni un plakni nedefinē, un "
          "raksturosim tos ar modeļiem un īpašībām.")

SATURS = [
    Sakums("Vārdnīca, kas iet pa apli",
           fakti=["«Punkts ir vieta.» - «Vieta ir punkts.»",
                  "Ja katru vārdu skaidro ar citu, kaut kur jāapstājas.",
                  "Ģeometrija apstājas pie punkta, taisnes un plaknes."]),

    Doma("Pamatjēdzienus nedefinē - tos raksturo",
         "Punkts, taisne un plakne ir pamatjēdzieni: tos nedefinē, bet "
         "raksturo ar modeļiem un pamatīpašībām. Visus citus jēdzienus "
         "definē ar tiem.",
         soli=[
             "Punkta modelis - zīmuļa pieskāriens, zvaigzne debesīs.",
             "Taisnes modelis - nostiepts diegs, gaismas stars.",
             "Plaknes modelis - galda virsma, mierīga ūdens virsma.",
             "Pamatīpašība: caur diviem punktiem var novilkt tieši vienu "
             "taisni.",
         ],
         pieze="Modelis nav pats objekts: punktam nav izmēra, taisnei nav "
               "platuma un gala. Modelis tikai palīdz iztēloties."),

    Zimejums("Caur diviem punktiem - viena taisne",
             geometrija([("A", 0, 0), ("B", 6, 2)], taisnes=["AB"]),
             paskaidro="Tāpēc taisni var nosaukt ar diviem tās punktiem: "
                       "taisne AB."),

    Zimejums("No kā definē kuru jēdzienu",
             restis([["pamatjēdzieni", "punkts, taisne, plakne"],
                     ["definē ar tiem", "nogrieznis, stars"],
                     ["tālāk", "leņķis, trijstūris"]]),
             paskaidro="Katrs nākamais jēdziens lieto tikai iepriekšējos."),

    Paraugs("Raksturo ar īpašībām",
            uzd="Kādas ir punkta un taisnes pamatīpašības? Uzraksti divas.",
            soli=[
                ("Caur diviem punktiem iet tieši viena taisne",
                 "Tāpēc lineāls ļauj novilkt tikai vienu līniju."),
                ("Uz katras taisnes ir bezgalīgi daudz punktu",
                 "Starp jebkuriem diviem - vēl viens."),
                ("Ir punkti, kas nepieder taisnei",
                 "Plakne nav tikai viena taisne."),
            ],
            atbilde="Piemēram: caur 2 punktiem - viena taisne; uz taisnes "
                    "bezgalīgi daudz punktu."),

    Varianti("Modelis vai definīcija?", [
        {"jaut": "«Taisne ir kā nostiepts diegs, kas turpinās bezgalīgi.» "
                 "Kas tas ir?",
         "opcijas": ["Modelis, kas palīdz iztēloties",
                     "Taisnes definīcija", "Aksioma", "Teorēma"],
         "pareizi": 0,
         "padoms": "Diegs nav bezgalīgs - tas ir tikai modelis."},
        {"jaut": "Kuru jēdzienu definē, nevis tikai raksturo?",
         "opcijas": ["Nogrieznis", "Punkts", "Taisne", "Plakne"],
         "pareizi": 0,
         "padoms": "Nogriezni definē ar punktiem un taisni."},
        {"jaut": "Cik taisņu var novilkt caur 2 dažādiem punktiem?",
         "opcijas": ["Tieši vienu", "Divas", "Bezgalīgi daudz", "Nevienu"],
         "pareizi": 0,
         "padoms": "Pamatīpašība."},
        {"jaut": "Cik taisņu var novilkt caur vienu punktu?",
         "opcijas": ["Bezgalīgi daudz", "Vienu", "Divas", "Nevienu"],
         "pareizi": 0,
         "padoms": "Pagriez lineālu ap vienu punktu."},
    ], pamats=4),

    Pasaule("Kāpēc galds ar trim kājām nešūpojas?",
            Varianti("", [
                {"jaut": "Trīs kāju gali vienmēr atrodas...",
                 "opcijas": ["vienā plaknē", "uz vienas taisnes",
                             "dažādās plaknēs", "vienā punktā"],
                 "pareizi": 0,
                 "padoms": "Caur trim punktiem (ne uz vienas taisnes) iet "
                           "tieši viena plakne."},
                {"jaut": "Kāpēc četrkājainais galds var šūpoties?",
                 "opcijas": ["Ceturtais kājas gals var nebūt tajā pašā "
                             "plaknē",
                             "Četras kājas ir par smagu",
                             "Četri punkti vienmēr ir uz taisnes",
                             "Grīda ir taisne"],
                 "pareizi": 0,
                 "padoms": "Plakni nosaka jau trīs punkti."},
                {"jaut": "Kāpēc fotogrāfa statīvam ir trīs kājas?",
                 "opcijas": ["Tas stāv stabili uz jebkuras virsmas",
                             "Tas ir lētāk",
                             "Trīs ir skaists skaitlis",
                             "Tā ir tradīcija"],
                 "pareizi": 0,
                 "padoms": "Trīs punkti vienmēr ir vienā plaknē."},
            ]),
            pavediens="maja",
            konteksts="Pamatīpašība: caur trim punktiem, kas nav uz vienas "
                      "taisnes, iet tieši viena plakne.",
            kapec="Aksiomas nav tikai teorija - tās skaidro sadzīvi."),

    Kopsavilkums([
        "Zinu, ka punkts, taisne un plakne ir pamatjēdzieni.",
        "Raksturoju tos ar modeļiem un pamatīpašībām.",
        "Atšķiru modeli no definīcijas.",
        "Zinu: caur 2 punktiem iet tieši viena taisne.",
    ]),

    Majas([
        "Atrodi mājās 3 punkta, taisnes un plaknes modeļus.",
        "Pamēģini novilkt divas dažādas taisnes caur diviem punktiem.",
        "Paskaidro kādam, kāpēc taburete ar 3 kājām nešūpojas.",
    ]),
]
