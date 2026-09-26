# -*- coding: utf-8 -*-
"""1. klase, 14. stunda: «Kā pateikt, kur kas atrodas?»

Novietojuma vārdi: pa labi, pa kreisi, virs, zem, starp, blakus. Vispirms
vienojas, no kura skatās - «pa labi» ir no skatītāja puses.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Pasaule, Petijums,
                         Sakums, Varianti, bildes)

TEMA = "Kā pateikt, kur kas atrodas?"

MERKIS = ("Šodien stāstīsim, kur kas atrodas: pa labi, pa kreisi, virs, "
          "zem un starp.")

_RINDA = bildes([["abols", "bumba", "gramata", "puke"]])
_PLAUKTS = bildes([["", "putns", ""], ["zivs", "abols", "masina"],
                   ["", "soma", ""]])

SATURS = [
    Sakums("Kas ir starp bumbu un puķi?",
           zimejums=_RINDA,
           paraksts="Ābols, bumba, grāmata, puķe - no kreisās uz labo.",
           fakti=["Pa kreisi un pa labi - no tevis skatoties.",
                  "Virs - augstāk, zem - zemāk.",
                  "Starp - vidū starp diviem."]),

    Doma("Vārdi vietai",
         "Lai otrs atrod lietu, pasaki, kas ir tai blakus.",
         soli=[
             "Pa kreisi - uz to pusi, kur kreisā roka.",
             "Pa labi - uz labās rokas pusi.",
             "Virs, zem - augšā, apakšā.",
             "Starp - vidū starp divām lietām.",
         ]),

    Varianti("Kur tas ir? (rindā)", [
        {"jaut": "Kas ir starp bumbu un puķi?", "zim": _RINDA,
         "opcijas": ["grāmata", "ābols", "bumba"], "pareizi": 0,
         "padoms": "Paskaties vidū."},
        {"jaut": "Kas ir pa kreisi no bumbas?", "zim": _RINDA,
         "opcijas": ["ābols", "grāmata", "puķe"], "pareizi": 0,
         "padoms": "Kreisās rokas pusē."},
        {"jaut": "Kas ir pa labi no grāmatas?", "zim": _RINDA,
         "opcijas": ["puķe", "bumba", "ābols"], "pareizi": 0,
         "padoms": "Labās rokas pusē."},
    ]),

    Varianti("Kur tas ir? (plauktā)", [
        {"jaut": "Kas ir virs ābola?", "zim": _PLAUKTS,
         "opcijas": ["putns", "soma", "zivs"], "pareizi": 0,
         "padoms": "Augšā."},
        {"jaut": "Kas ir zem ābola?", "zim": _PLAUKTS,
         "opcijas": ["soma", "putns", "mašīna"], "pareizi": 0,
         "padoms": "Apakšā."},
        {"jaut": "Kas ir starp zivi un mašīnu?", "zim": _PLAUKTS,
         "opcijas": ["ābols", "putns", "soma"], "pareizi": 0,
         "padoms": "Vidū."},
        {"jaut": "Kur ir mašīna no ābola?", "zim": _PLAUKTS,
         "opcijas": ["pa labi", "pa kreisi", "virs"], "pareizi": 0,
         "padoms": "Labās rokas pusē."},
    ]),

    Petijums("Sakārto galdu", [
        "Noliec penāli sev priekšā.",
        "Pa labi no penāļa - burtnīcu.",
        "Pa kreisi - lineālu.",
        "Virs burtnīcas - zīmuli.",
        "Pajautā blakus sēdētājam, vai viss ir pareizi.",
    ], vajag="penālis, burtnīca, lineāls, zīmulis"),

    Pasaule("Kur ir manas kurpes?",
            Varianti("", [
                {"jaut": "Plauktā: augšā cepure, vidū kurpes, apakšā zābaki. "
                         "Kas ir starp cepuri un zābakiem?",
                 "opcijas": ["kurpes", "cepure", "zābaki"], "pareizi": 0,
                 "padoms": "Vidū."},
                {"jaut": "Kas ir zem kurpēm?",
                 "opcijas": ["zābaki", "cepure", "nekas"], "pareizi": 0,
                 "padoms": "Apakšā."},
            ]),
            pavediens="maja",
            konteksts="Priekšnamā ir plaukts ar trim stāviem.",
            kapec="Vietas vārdi palīdz ātri atrast lietas."),

    Kopsavilkums([
        "Lietoju vārdus pa labi, pa kreisi, virs, zem, starp.",
        "Aprakstu, kur kas atrodas.",
        "Sakārtoju galdu pēc norādēm.",
    ]),

    Majas([
        "Pastāsti, kas ir pa labi un pa kreisi no tavas gultas.",
        "Paslēp rotaļlietu un pastāsti, kur tā ir, - lai kāds atrod.",
        "Kas ir virs un zem virtuves galda?",
    ]),
]
