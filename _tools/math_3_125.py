# -*- coding: utf-8 -*-
"""3. klase, 125. stunda: «Kas kopīgs diviem ķermeņiem?»

Salīdzināšana pēc vairākām pazīmēm reizē: tilpums, forma, virsmu skaits. Divi
ķermeņi var būt vienāda tilpuma, bet pavisam citas formas - tieši tāpat kā
figūras ar vienādu laukumu 118. stundā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         kermenis)

TEMA = "Kas kopīgs diviem ķermeņiem?"

MERKIS = ("Salīdzināsim ķermeņus pēc tilpuma un formas; raksturosim kopīgo "
          "un atšķirīgo.")

SATURS = [
    Sakums("Vai divas kastes ar vienādu tilpumu ir vienādas?",
           zimejums=kermenis("kvadrs", virsraksts="kaste 8 x 3 x 1"),
           paraksts="Tilpums ir 24 kubi - tikpat, cik kastei 4 x 3 x 2.",
           fakti=["Vienāds tilpums nenozīmē vienādu formu.",
                  "Ķermeņus salīdzina pēc vairākām pazīmēm."]),

    Doma("Salīdzini pēc vairākām pazīmēm",
         "Divi ķermeņi var sakrist pēc tilpuma un atšķirties pēc formas - un "
         "otrādi.",
         soli=[
             "Izrēķini abu tilpumu.",
             "Salīdzini formu: vai abi ir kvadri, kubi vai cilindri?",
             "Saskaiti skaldnes, šķautnes un virsotnes.",
             "Pieraksti, kas ir kopīgs un kas atšķirīgs.",
         ],
         pieze="Kubs ir kvadrs ar vienādām malām - tāpat kā kvadrāts ir "
               "taisnstūris ar vienādām malām."),

    Petijums("Salīdzini divas kastes",
             vajag="divas dažādas kastītes un kubiņi",
             soli=[
                 "Izmēri abu kastīšu malas kubiņos.",
                 "Izrēķini abu tilpumu.",
                 "Saskaiti abām skaldnes, šķautnes un virsotnes.",
                 "Uzraksti divus teikumus: kas kopīgs, kas atšķirīgs.",
             ],
             secinajums="Abām kastēm skaldņu, šķautņu un virsotņu skaits "
                        "sakrīt - atšķiras tikai izmēri."),

    Paraugs("Kas kopīgs un kas atšķirīgs?",
            uzd="Kaste A ir 4 x 3 x 2, kaste B ir 8 x 3 x 1. Salīdzini tās.",
            soli=[
                ("A: 4 · 3 · 2 = 24",
                 "Pirmās tilpums."),
                ("B: 8 · 3 · 1 = 24",
                 "Otrās tilpums - tas pats."),
                ("Formas atšķiras",
                 "B ir plakanāka un garāka, bet tilpums vienāds."),
            ],
            atbilde="tilpums vienāds, forma atšķirīga"),

    Ievadi("Salīdzini ķermeņus", [
        {"jaut": "Kaste 4 x 3 x 2. Cik ir tilpums kubos?", "atb": ["24"],
         "padoms": "12 · 2."},
        {"jaut": "Kaste 8 x 3 x 1. Cik ir tilpums?", "atb": ["24"],
         "padoms": "24 · 1."},
        {"jaut": "Cik skaldņu ir kvadram?", "atb": ["6"],
         "padoms": "Augša, apakša un četri sāni."},
        {"jaut": "Cik šķautņu ir kvadram?", "atb": ["12"],
         "padoms": "Trīs grupas pa četrām."},
        {"jaut": "Cik virsotņu ir kvadram?", "atb": ["8"],
         "padoms": "Četras augšā, četras apakšā."},
        {"jaut": "Kubs ar malu 3. Cik ir tilpums?", "atb": ["27"],
         "padoms": "9 · 3."},
    ], pamats=4),

    Zimejums("Kubs un cilindrs",
             kermenis("cilindrs", virsraksts="cilindrs"),
             paskaidro="Cilindram nav ne šķautņu, ne virsotņu - tas ir "
                       "galvenais, ar ko tas atšķiras no kvadra.",
             ievads="Cits ķermeņa veids."),

    Varianti("Kas tiem kopīgs?", [
        {"jaut": "Kas kopīgs kubam un kvadram?",
         "opcijas": ["6 skaldnes, 12 šķautnes, 8 virsotnes",
                     "Vienāds tilpums", "Vienādas malas",
                     "Nekas"],
         "pareizi": 0, "padoms": "Kubs ir kvadra īpašs gadījums."},
        {"jaut": "Ar ko cilindrs atšķiras no kvadra?",
         "opcijas": ["Tam nav šķautņu un virsotņu", "Tas ir lielāks",
                     "Tam ir vairāk skaldņu", "Nekā"],
         "pareizi": 0, "padoms": "Cilindram malas ir apaļas."},
        {"jaut": "Vai vienāds tilpums nozīmē vienādu formu?",
         "opcijas": ["Nē", "Jā", "Tikai kubiem", "Vienmēr"],
         "pareizi": 0, "padoms": "4 x 3 x 2 un 8 x 3 x 1."},
        {"jaut": "Kaste 6 x 2 x 2. Cik ir tilpums?",
         "opcijas": ["24", "10", "12", "20"],
         "pareizi": 0, "padoms": "12 · 2."},
    ], pamats=4),

    Pasaule("Kāda forma ir tvertnei?",
            Ievadi("", [
                {"jaut": "Tvertne 5 x 4 x 2 m. Cik kubikmetru ir tilpums?",
                 "atb": ["40"], "padoms": "20 · 2."},
                {"jaut": "Otra tvertne 10 x 2 x 2 m. Cik kubikmetru?",
                 "atb": ["40"], "padoms": "20 · 2."},
                {"jaut": "Vai abiem tilpums ir vienāds? Raksti «jā» vai "
                         "«nē».",
                 "atb": ["jā", "ja"], "padoms": "40 un 40.",
                 "tastatura": "text"},
                {"jaut": "Vienā kubikmetrā ir 1000 litru. Cik litru ietilpst "
                         "tvertnē?",
                 "atb": ["40000", "40 000"], "padoms": "40 · 1000."},
            ]),
            pavediens="planeta",
            konteksts="Ūdens tvertnes ražo dažādās formās, bet tilpumu vienmēr "
                      "saka kubikmetros vai litros.",
            kapec="Forma izlemj, kur tvertne ietilps; tilpums - cik tā tur."),

    Kopsavilkums([
        "Salīdzinu ķermeņus pēc tilpuma un formas.",
        "Saskaitu skaldnes, šķautnes un virsotnes.",
        "Zinu, ka vienāds tilpums nenozīmē vienādu formu.",
        "Raksturoju kopīgo un atšķirīgo.",
    ]),

    Majas([
        "Atrodi mājās divas kastes ar apmēram vienādu tilpumu.",
        "Saskaiti abām skaldnes, šķautnes un virsotnes.",
        "Uzraksti, kas tām kopīgs un kas atšķirīgs.",
    ]),
]
