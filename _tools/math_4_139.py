# -*- coding: utf-8 -*-
"""4. klase, 139. stunda: «Kā izveidot citu figūru ar to pašu laukumu?»

Sagriez un saliec citādi: taisnstūri sagriež divās daļās un saliek par
«L», trepēm vai garāku taisnstūri. Laukums nemainās, jo nekas netiek
pazaudēts vai pielikts - tā ir laukuma saglabāšanās ideja.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, figura)

TEMA = "Kā izveidot citu figūru ar to pašu laukumu?"

MERKIS = ("Sadalīsim figūru daļās un savietosim citādi, iegūstot vienlielu "
          "figūru.")

SATURS = [
    Sakums("Sagriez un saliec!",
           zimejums=figura([(0, 0), (4, 0), (4, 4), (0, 4)], platums=9,
                           augstums=5),
           paraksts="Kvadrātu 4 × 4 sagriež uz pusēm un saliek garumā.",
           fakti=["Kvadrāts 4 × 4 - 16 rūtiņas.",
                  "Divas pusītes 4 × 2 blakus - taisnstūris 8 × 2, arī 16."]),

    Doma("Griežot un saliekot, laukums saglabājas",
         "Ja figūru sagriež daļās un saliek citādi, jaunās figūras laukums "
         "ir tāds pats.",
         soli=[
             "Sagriez figūru pa rūtiņu līnijām.",
             "Pārvieto vai pagriez daļas.",
             "Saliec bez spraugām un pārklāšanās.",
             "Pārbaudi, saskaitot rūtiņas.",
         ],
         pieze="Tā strādā tangrams - septiņas daļas, simtiem figūru, viens "
               "laukums."),

    Slidnis("No kvadrāta uz taisnstūri",
            soli=[
                {"v": "kvadrāts 4 × 4 = 16",
                 "zim": figura([(0, 0), (4, 0), (4, 4), (0, 4)], platums=9,
                               augstums=5), "teksts": "Sākums."},
                {"v": "sagriež pusēs", "teksts": "Divas daļas 4 × 2.",
                 "zim": figura([(0, 0), (4, 0), (4, 2), (0, 2), (0, 4),
                                (4, 4), (4, 2), (0, 2)], platums=9,
                               augstums=5, aizpildi=False)},
                {"v": "taisnstūris 8 × 2 = 16", "teksts": "Saliek garumā.",
                 "zim": figura([(0, 0), (8, 0), (8, 2), (0, 2)], platums=9,
                               augstums=5)},
            ]),

    Varianti("Vai laukums mainījās?", [
        {"jaut": "Taisnstūri 6 × 2 sagrieza un salika «L» formā.",
         "opcijas": ["nemainījās - 12", "palielinājās", "samazinājās"],
         "pareizi": 0, "padoms": "Nekas nepazuda."},
        {"jaut": "No 16 rūtiņu kvadrāta nogrieza 4 rūtiņas un izmeta.",
         "opcijas": ["samazinājās - 12", "nemainījās", "palielinājās"],
         "pareizi": 0, "padoms": "Daļa pazuda."},
        {"jaut": "Kurš taisnstūris vienliels ar 3 × 8?",
         "opcijas": ["4 × 6", "3 × 9", "5 × 5", "2 × 11"], "pareizi": 0,
         "padoms": "24."},
    ]),

    Ievadi("Jaunā figūra", [
        {"jaut": "Kvadrāts 6 × 6 pārveidots taisnstūrī ar platumu 4. "
                 "Garums?", "atb": ["9"], "padoms": "36 : 4."},
        {"jaut": "Taisnstūris 10 × 3 → kvadrāts nav iespējams? Laukums?",
         "atb": ["30"], "padoms": "10 · 3."},
        {"jaut": "Taisnstūris 2 × 18 → taisnstūris ar platumu 6. Garums?",
         "atb": ["6"], "padoms": "36 : 6 - kvadrāts!"},
        {"jaut": "Tangrama kvadrāts ir 64 rūtiņas. Cik rūtiņu ir tangrama "
                 "kaķim?", "atb": ["64"], "padoms": "Tās pašas daļas."},
    ]),

    Pasaule("Tangrams - ķīniešu mīkla",
            Varianti("", [
                {"jaut": "Tangramā 7 daļas saliek kvadrātā. Ja saliek laivā, "
                         "laukums...",
                 "opcijas": ["tas pats", "lielāks", "mazāks"], "pareizi": 0,
                 "padoms": "Tās pašas daļas."},
                {"jaut": "Tangramu izdomāja...",
                 "opcijas": ["Ķīnā", "Latvijā", "Ēģiptē"], "pareizi": 0,
                 "padoms": "Vairāk nekā pirms 200 gadiem Ķīnā."},
                {"jaut": "Ja viena tangrama daļa pazūd, laukums...",
                 "opcijas": ["samazinās", "nemainās", "palielinās"],
                 "pareizi": 0, "padoms": "Trūkst gabala."},
            ]),
            pavediens="tehnika",
            konteksts="Tangramā no 7 daļām var salikt vairāk nekā tūkstoti "
                      "figūru - visām viens laukums.",
            kapec="Sagriežot un saliekot, laukums nekur nepazūd."),

    Petijums("Mans tangrams",
             soli=[
                 "Izgriez kvadrātu 8 × 8 rūtiņas.",
                 "Sagriez to 4 daļās pa rūtiņu līnijām.",
                 "Saliec no tām 2 jaunas figūras.",
                 "Saskaiti rūtiņas katrā - vai 64?",
             ],
             vajag="rūtiņu papīrs, šķēres",
             secinajums="Visas figūras ir vienlielas - 64 rūtiņas."),

    Kopsavilkums([
        "Sagriežu un saliku figūru citādi.",
        "Zinu, ka laukums saglabājas.",
        "Pārbaudu, skaitot rūtiņas.",
    ]),

    Majas([
        "Izgriez un saliec 3 figūras no viena 6 × 4 taisnstūra.",
        "Uzspēlē tangramu (arī tiešsaistē).",
        "Paskaidro kādam, kāpēc laukums nemainās.",
    ]),
]
