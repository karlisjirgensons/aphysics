# -*- coding: utf-8 -*-
"""4. klase, 65. stunda: «Kā pagriezt taisnstūri par 90°?»

No stara uz figūru: pagriežot taisnstūri ap virsotni par 90°, katra mala
pagriežas par 90° - horizontālā kļūst vertikāla. Rūtiņu lapā to var
izdarīt bez transportiera, jo taisns leņķis ir rūtiņās jau iekšā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Slidnis, Varianti,
                         figura)

TEMA = "Kā pagriezt taisnstūri par 90°?"

MERKIS = ("Pagriezīsim taisnstūri rūtiņu lapā ap virsotni un attēlosim abas "
          "figūras.")

SATURS = [
    Sakums("Kā tetris pagriež klucīti?",
           zimejums=figura([(6, 4), (12, 4), (12, 6), (6, 6), (6, 4), (6, 10),
                            (4, 10), (4, 4)],
                           uzraksti=[(6.5, 3.4, "O")],
                           platums=12, augstums=10, aizpildi=False),
           paraksts="Guļus taisnstūris 6 × 2 un tas pats, pagriezts ap O.",
           fakti=["Tetrī klucītis griežas par 90° vienā spiedienā.",
                  "Figūra nemaina izmēru - tikai virzienu."]),

    Doma("Katra mala pagriežas par 90°",
         "Pagriežot ap virsotni O par 90°, horizontālā mala kļūst vertikāla, "
         "vertikālā - horizontāla, garumi nemainās.",
         soli=[
             "Izvēlies centru O - taisnstūra virsotni.",
             "Mala, kas iet no O pa labi 6 rūtiņas, tagad iet uz augšu 6.",
             "Mala, kas iet no O uz augšu 2, tagad iet pa kreisi 2.",
             "Pabeidz taisnstūri pēc jaunajām malām.",
         ],
         pieze="Pagriežot pretēji pulksteņa rādītājam: pa labi → uz augšu, "
               "uz augšu → pa kreisi."),

    Slidnis("Pagrieziens soli pa solim",
            soli=[
                {"v": "sākums", "teksts": "Taisnstūris 6 × 2, virsotne O.",
                 "zim": figura([(6, 4), (12, 4), (12, 6), (6, 6)],
                               uzraksti=[(6.5, 3.4, "O")],
                               platums=12, augstums=10)},
                {"v": "pagriezts par 90°", "teksts": "Tagad 2 × 6 - stāvus.",
                 "zim": figura([(6, 4), (6, 10), (4, 10), (4, 4)],
                               uzraksti=[(6.5, 3.4, "O")],
                               platums=12, augstums=10)},
                {"v": "vēl par 90°", "teksts": "180° - atkal guļus, bet otrā "
                 "pusē.",
                 "zim": figura([(6, 4), (0, 4), (0, 2), (6, 2)],
                               uzraksti=[(6.5, 4.6, "O")],
                               platums=12, augstums=10)},
            ],
            ievads="Pagriežam pretēji pulksteņa rādītājam ap O."),

    Paraugs("Kur būs virsotnes?",
            uzd="Taisnstūris ar malām 4 (pa labi) un 3 (uz augšu) no O. Kādas "
                "būs malas pēc pagrieziena par 90°?",
            soli=[
                ("4 pa labi → 4 uz augšu", None),
                ("3 uz augšu → 3 pa kreisi", None),
            ],
            atbilde="taisnstūris 3 × 4, stāvus"),

    Varianti("Kas notiek pēc pagrieziena?", [
        {"jaut": "Taisnstūris 5 × 2 pagriezts par 90°. Tā izmēri...",
         "opcijas": ["2 × 5", "5 × 2 guļus", "10 × 1", "4 × 4"],
         "pareizi": 0, "padoms": "Malas samainās vietām."},
        {"jaut": "Vai laukums pēc pagrieziena mainās?",
         "opcijas": ["nē", "jā, palielinās", "jā, samazinās"], "pareizi": 0,
         "padoms": "Tā pati figūra."},
        {"jaut": "Kvadrāts pagriezts par 90° ap centru izskatās...",
         "opcijas": ["tieši tāpat", "citādi", "kā taisnstūris"],
         "pareizi": 0, "padoms": "Visas malas vienādas."},
        {"jaut": "Cik pagriezienu par 90° vajag, lai figūra atgrieztos "
                 "sākumā?",
         "opcijas": ["4", "2", "3", "1"], "pareizi": 0,
         "padoms": "4 · 90 = 360."},
    ], pamats=4),

    Ievadi("Rēķini pēc pagrieziena", [
        {"jaut": "Taisnstūris 6 × 2. Laukums (rūtiņās) pēc pagrieziena?",
         "atb": ["12"], "padoms": "Nemainās: 6 · 2."},
        {"jaut": "Tā perimetrs (rūtiņu malās)?", "atb": ["16"],
         "padoms": "6 + 2 + 6 + 2."},
        {"jaut": "Par cik grādiem pagrieztas visas malas kopā ar figūru?",
         "atb": ["90"], "padoms": "Visas vienādi."},
        {"jaut": "Cik grādu ir trīs pagriezieni par 90°?", "atb": ["270"],
         "padoms": "3 · 90."},
    ]),

    Pasaule("Tetris un spēļu programmēšana",
            Varianti("", [
                {"jaut": "Klucītis «I» (4 × 1) guļus. Pēc 90° pagrieziena tas "
                         "ir...",
                 "opcijas": ["stāvus 1 × 4", "guļus 4 × 1", "kvadrāts"],
                 "pareizi": 0, "padoms": "Garā mala kļūst vertikāla."},
                {"jaut": "Cik spiedienu vajag, lai klucītis pagrieztos par "
                         "180°?",
                 "opcijas": ["2", "1", "4"], "pareizi": 0,
                 "padoms": "180 : 90."},
                {"jaut": "Kvadrātveida klucītis «O» pēc pagrieziena...",
                 "opcijas": ["izskatās tāpat", "kļūst garāks",
                             "kļūst šaurāks"], "pareizi": 0,
                 "padoms": "Kvadrāts."},
            ]),
            pavediens="dati",
            konteksts="Datorspēlē katrs pagrieziens par 90° ir programmas "
                      "komanda - figūras rūtiņas tiek pārrēķinātas.",
            kapec="Spēļu programmētāji ik dienu lieto pagriezienus."),

    Petijums("Papīra taisnstūris",
             soli=[
                 "Izgriez taisnstūri 6 × 2 rūtiņas.",
                 "Noliec to uz rūtiņu lapas un apvelc.",
                 "Iedur zīmuli virsotnē O un pagriez taisnstūri par 90°.",
                 "Apvelc vēlreiz un salīdzini ar zīmējumu.",
             ],
             vajag="rūtiņu lapa, šķēres, zīmulis",
             secinajums="Pagrieztā figūra ir tāda pati, tikai vērsta citādi."),

    Kopsavilkums([
        "Pagriežu taisnstūri ap virsotni par 90° rūtiņu lapā.",
        "Zinu, ka figūras izmēri un laukums nemainās.",
        "Zinu, ka 4 pagriezieni par 90° dod pilnu apli.",
    ]),

    Majas([
        "Uzzīmē rūtiņās taisnstūri 5 × 3 un pagriez to ap virsotni.",
        "Paspēlē tetri un skaiti, cik reizes pagriez klucīti.",
        "Pagriez burtu «L» par 90° un uzzīmē visus 4 stāvokļus.",
    ]),
]
