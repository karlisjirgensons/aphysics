# -*- coding: utf-8 -*-
"""9. klase, 37. stunda: «Kā aprēķināt tilpumu?»

Prizmas tilpums V = S_{pam} · H der jebkuram pamatam. Trapeces prizmai tas
nozīmē divus soļus: trapeces laukums, tad reizināt ar garumu. Grāvja,
dambja un baseina tilpums ir tieši šāds.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, trapeces_prizma)

TEMA = "Kā aprēķināt tilpumu?"

MERKIS = "Aprēķināsim prizmas tilpumu ar trapeces pamatu."

SATURS = [
    Sakums("Cik ūdens ietilpst baseinā ar slīpu dibenu?",
           zimejums=trapeces_prizma(10, 6, 3, 7, nobide=0),
           paraksts="Baseina sānskats - taisnleņķa trapece.",
           fakti=["Tilpums = pamata laukums · garums.",
                  "Pamats te ir sānskata trapece.",
                  "1 m³ = 1000 litru."]),

    Slidnis("Slāņi pa vienam", [
        {"v": "1 slānis", "teksts": "Trapece 1 cm biezumā: V = S · 1",
         "zim": trapeces_prizma(10, 6, 3, 1.2, nobide=0)},
        {"v": "3 slāņi", "teksts": "V = S · 3",
         "zim": trapeces_prizma(10, 6, 3, 3.6, nobide=0)},
        {"v": "H slāņi", "teksts": "V = S_{pam} · H",
         "zim": trapeces_prizma(10, 6, 3, 7, nobide=0)},
    ], ievads="Prizma ir vienādu trapeču kaudze."),

    Doma("Prizmas tilpums",
         "V = S_{pam} · H, kur S_{pam} = {a + b|2} · h.",
         soli=[
             "Nosaki, kura skaldne ir pamats (trapece).",
             "Aprēķini trapeces laukumu.",
             "Reizini ar prizmas augstumu (garumu).",
             "Pārvērš mērvienības: 1 m³ = 1000 l, 1 dm³ = 1 l.",
         ]),

    Paraugs("Grāvis",
            uzd="Grāvja šķērsgriezums - trapece: augšā 2 m, apakšā 0,8 m, "
                "dziļums 1 m. Grāvis 50 m garš. Cik m³ zemes izraka?",
            soli=[
                ("S = {2 + 0,8|2} · 1 = 1,4 (m²)", "Šķērsgriezums."),
                ("V = 1,4 · 50 = 70 (m³)", "Tilpums."),
            ],
            atbilde="70 m³"),

    Ievadi("Aprēķini tilpumu", [
        {"jaut": "S_{pam} = 12 cm², H = 5 cm. V = ? cm³", "atb": ["60"],
         "padoms": "12 · 5."},
        {"jaut": "Trapece 8, 4, h = 3; H = 10. V = ?", "atb": ["180"],
         "padoms": "18 · 10."},
        {"jaut": "V = 240, S_{pam} = 20. H = ?", "atb": ["12"],
         "padoms": "240 : 20."},
        {"jaut": "Trapece 1,2 m, 0,8 m, h = 0,5 m; H = 3 m. V = ? m³",
         "atb": ["1,5"], "padoms": "0,5 · 3."},
        {"jaut": "Tas pats tilpums litros?", "atb": ["1500"],
         "padoms": "· 1000."},
    ], pamats=3),

    Pasaule("Baseina piepildīšana",
            Kustiba("", [
                {"jaut": "Baseins 25 m garš, 10 m plats; seklajā galā 1 m, "
                         "dziļajā 2 m dziļš. Tilpums = {1 + 2|2} · 25 · 10 = "
                         "? m³",
                 "atb": 375, "beigas": 500, "iedala": 50, "mers": "m³",
                 "merkis": "pilns", "objekts": "Ūdens",
                 "padoms": "1,5 · 250."},
                {"jaut": "Sūknis dod 25 m³ stundā. Cik stundās piepildīs?",
                 "atb": 15, "beigas": 24, "iedala": 2, "mers": "h",
                 "merkis": "gatavs", "objekts": "Sūknis",
                 "padoms": "375 : 25."},
            ]),
            pavediens="planeta",
            konteksts="Peldbaseina dibens slīpi padziļinās, tāpēc tā "
                      "sānskats ir trapece.",
            kapec="Ūdens daudzums nosaka sūkņa darba laiku un rēķinu."),

    Varianti("Izvēlies", [
        {"jaut": "Ja prizmas garumu dubulto, tilpums...",
         "opcijas": ["dubultojas", "četrkāršojas", "nemainās",
                     "palielinās par 2"],
         "pareizi": 0, "padoms": "V ~ H."},
        {"jaut": "Ja visus izmērus dubulto, tilpums...",
         "opcijas": ["pieaug 8 reizes", "pieaug 2 reizes",
                     "pieaug 4 reizes", "pieaug 6 reizes"],
         "pareizi": 0, "padoms": "k^3 - līdzīgi ķermeņi."},
    ]),

    Kopsavilkums([
        "Aprēķinu prizmas tilpumu V = S_{pam} · H.",
        "Saskatu trapeci kā pamatu arī «guļošai» prizmai.",
        "Pārvēršu m³ litros.",
    ]),

    Majas([
        "Izmēri kādu trapeces formas trauku un aprēķini tilpumu.",
        "Grāvis: augšā 1,5 m, apakšā 0,5 m, dziļums 0,8 m, garums 30 m. "
        "Cik m³?",
        "Cik litru ietilpst baseinā 12 m × 5 m ar dziļumu 1 m un 1,8 m?",
    ]),
]
