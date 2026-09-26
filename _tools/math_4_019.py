# -*- coding: utf-8 -*-
"""4. klase, 19. stunda: «Kā attēlot savus datus?»

Pēc lasīšanas - zīmēšana. Grūtākais ir mērogs: ja dati ir 1200 un 3500,
katra rūtiņa nevar būt 1. Skolēns izvēlas mērogu un pamato to - tā pati
doma, kas skaitļu taisnes solim 3. un 10. stundā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Slidnis, Varianti,
                         kolonnas, restis)

TEMA = "Kā attēlot savus datus?"

MERKIS = ("Attēlosim skaitliskus datus stabiņu diagrammā un pamatosim "
          "izvēlēto mērogu.")

SATURS = [
    Sakums("Kā uz vienas lapas uzzīmēt 3500 grāmatu?",
           zimejums=kolonnas([("pasakas", 1200), ("enciklopēdijas", 800),
                              ("romāni", 3500)]),
           paraksts="Skolas bibliotēka: grāmatu skaits pa veidiem.",
           fakti=["Ja 1 rūtiņa = 1 grāmata, stabiņš būtu 3500 rūtiņu augsts.",
                  "Ar mērogu 1 rūtiņa = 500 grāmatu tas ir 7 rūtiņas."]),

    Doma("Mērogs pasaka, cik daudz ir vienā rūtiņā",
         "Izvēlies mērogu tā, lai lielākais stabiņš ietilpst lapā un visus "
         "stabiņus ir viegli nolasīt.",
         soli=[
             "Atrodi lielāko vērtību.",
             "Izvēlies apaļu mērogu: 1, 10, 100, 500 vai 1000 vienā rūtiņā.",
             "Izrēķini katra stabiņa augstumu: vērtība : mērogs.",
             "Uzraksti virsrakstu, nosaukumus un mērogu.",
         ],
         pieze="Mērogs 500: 1200 : 500 nav vesels - stabiņš beidzas starp "
               "iedaļām (2 un vēl mazliet)."),

    Slidnis("Tie paši dati, trīs mērogi",
            soli=[
                {"v": "1 rūtiņa = 100", "teksts": "Romāni - 35 rūtiņas. Par "
                 "augstu lapai."},
                {"v": "1 rūtiņa = 500", "teksts": "Romāni - 7 rūtiņas. "
                 "Ietilpst un labi redzams."},
                {"v": "1 rūtiņa = 5000", "teksts": "Romāni - mazāk par 1 "
                 "rūtiņu. Neko nevar salīdzināt."},
            ],
            ievads="Mērogu izvēlas tā, lai diagramma ir ne par lielu, ne par "
                   "mazu."),

    Paraugs("Cik rūtiņu augsts stabiņš?",
            uzd="Mērogs: 1 rūtiņa = 200 skolēnu. Skolā ir 1400 skolēnu. "
                "Cik rūtiņu augsts būs stabiņš?",
            soli=[
                ("1400 : 200", "Cik reižu 200 ietilpst 1400?"),
                ("1400 : 200 = 7", None),
            ],
            atbilde="7 rūtiņas"),

    Ievadi("Rēķini stabiņus", [
        {"jaut": "Mērogs 1 rūtiņa = 100. Vērtība 600. Cik rūtiņu?",
         "atb": ["6"], "padoms": "600 : 100."},
        {"jaut": "Mērogs 1 rūtiņa = 1000. Vērtība 8000. Cik rūtiņu?",
         "atb": ["8"], "padoms": "8000 : 1000."},
        {"jaut": "Mērogs 1 rūtiņa = 50. Stabiņš 9 rūtiņas. Kāda vērtība?",
         "atb": ["450"], "padoms": "9 · 50."},
        {"jaut": "Mērogs 1 rūtiņa = 500. Stabiņš 4 rūtiņas. Kāda vērtība?",
         "atb": ["2000"], "padoms": "4 · 500."},
    ]),

    Varianti("Kurš mērogs der?", [
        {"jaut": "Dati: 20, 35, 50. Lapā ir 10 rūtiņu augstumā.",
         "opcijas": ["1 rūtiņa = 5", "1 rūtiņa = 1", "1 rūtiņa = 100"],
         "pareizi": 0, "padoms": "50 : 5 = 10 - tieši ietilpst."},
        {"jaut": "Dati: 2000, 4500, 6000. Lapā 12 rūtiņu.",
         "opcijas": ["1 rūtiņa = 500", "1 rūtiņa = 10", "1 rūtiņa = 5000"],
         "pareizi": 0, "padoms": "6000 : 500 = 12."},
        {"jaut": "Dati: 3, 7, 9. Lapā 10 rūtiņu.",
         "opcijas": ["1 rūtiņa = 1", "1 rūtiņa = 10", "1 rūtiņa = 100"],
         "pareizi": 0, "padoms": "Mazi skaitļi - mazs mērogs."},
        {"jaut": "Ko nedrīkst aizmirst uzrakstīt diagrammā?",
         "opcijas": ["mērogu", "zīmētāja vārdu", "datumu", "krāsu"],
         "pareizi": 0, "padoms": "Bez mēroga stabiņus nevar nolasīt."},
    ], pamats=4),

    Pasaule("Klases lasītāju diagramma",
            Ievadi("", [
                {"jaut": "Klase izlasīja: septembrī 1200 lpp., oktobrī "
                         "1800 lpp., novembrī 2400 lpp. Kāds mērogs ļauj "
                         "novembrim 8 rūtiņas? 1 rūtiņa = ?",
                 "atb": ["300"], "padoms": "2400 : 8."},
                {"jaut": "Cik rūtiņu būs septembra stabiņš?",
                 "atb": ["4"], "padoms": "1200 : 300."},
                {"jaut": "Cik rūtiņu - oktobra stabiņš?",
                 "atb": ["6"], "padoms": "1800 : 300."},
                {"jaut": "Cik lappušu klase izlasīja trijos mēnešos?",
                 "atb": ["5400"], "padoms": "1200 + 1800 + 2400."},
            ]),
            pavediens="skola",
            zimejums=restis([["mēnesis", "lpp.", "rūtiņas"],
                             ["sept.", 1200, None],
                             ["okt.", 1800, None],
                             ["nov.", 2400, 8]]),
            konteksts="Lasīšanas sacensībā klase zīmē diagrammu uz sienas.",
            kapec="Labs mērogs padara progresu redzamu no klases otra gala."),

    Petijums("Mūsu klases diagramma",
             soli=[
                 "Katrs pasaka, cik minūšu vakar lasīja (vai spēlēja āra "
                 "spēles).",
                 "Sagrupējiet: 0-10, 11-20, 21-30, vairāk nekā 30 minūtes.",
                 "Saskaitiet, cik skolēnu katrā grupā.",
                 "Izvēlieties mērogu un uzzīmējiet stabiņu diagrammu.",
             ],
             vajag="rūtiņu lapa, lineāls, krāsainie zīmuļi",
             secinajums="Pamato, kāpēc izvēlējies tieši šo mērogu."),

    Kopsavilkums([
        "Izvēlos diagrammai piemērotu mērogu.",
        "Izrēķinu stabiņa augstumu ar dalīšanu.",
        "Nolasu vērtību ar reizināšanu.",
        "Pamatoju sava mēroga izvēli.",
    ]),

    Majas([
        "Nedēļu pieraksti, cik minūšu katru dienu pavadi pie ekrāna, un "
        "uzzīmē diagrammu.",
        "Izvēlies mērogu un paskaidro mājiniekiem, kāpēc tieši tāds.",
        "Salīdzini savu diagrammu ar klasesbiedra: kas līdzīgs?",
    ]),
]
