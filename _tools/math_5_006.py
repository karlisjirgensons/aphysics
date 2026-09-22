# -*- coding: utf-8 -*-
"""5. klase, 6. stunda: «Kā izskatās laika ass?»

Mikrotemata noslēgums. Laika ass ir tā pati skaitļu taisne, tikai vienība ir
gads - tāpēc te nav jauna pieraksta, bet ir jauna prasme: nolasīt no ass, cik
ilgi kaut kas noticis, un saprast, ka «pirms» nozīmē pa kreisi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, laika_ass)

TEMA = "Kā izskatās laika ass?"

MERKIS = ("Iemācīsimies atlikt gadskaitļus uz laika ass un aprēķināt, cik "
          "gadu pagājis starp diviem notikumiem.")

SATURS = [
    Sakums("Cik ilgi no pirmā satelīta līdz cilvēkam uz Mēness?",
           zimejums=laika_ass([(1957, "satelīts"), (1961, "cilvēks"),
                               (1969, "Mēness"), (1998, "stacija")],
                              sakums=1950, beigas=2000, solis=10),
           paraksts="No 1957. līdz 1969. gadam pagāja tikai 12 gadi.",
           fakti=["Jo tālāk pa labi, jo vēlāk.",
                  "Attālums starp punktiem parāda, cik gadu pagājis."]),

    Doma("Laika ass ir skaitļu taisne, kur vienība ir gads",
         "Starpība starp diviem gadskaitļiem parāda, cik gadu pagājis.",
         soli=[
             "Atrodi senāko un jaunāko gadu - tie noteiks ass galus.",
             "Izvēlies iedaļu: 10, 25 vai 50 gadi, lai viss ietilptu.",
             "Atzīmē notikumus un pieraksti gadu.",
             "Lai uzzinātu, cik ilgi, atņem: vēlākais mīnus agrākais.",
         ],
         pieze="Starp 1918. un 2018. gadu ir 100 gadu, nevis 101 - skaita "
               "attālumu, nevis atzīmes."),

    Zimejums("Latvijas valsts gadi",
             laika_ass([(1918, "1918"), (1940, "1940"), (1991, "1991"),
                        (2004, "2004")], sakums=1900, beigas=2025, solis=25),
             paskaidro="Viena iedaļa ir 25 gadi. Redzams, ka no 1940. līdz "
                       "1991. gadam pagāja vairāk nekā puse gadsimta.",
             ievads="Četri gadskaitļi uz vienas ass."),

    Paraugs("Cik gadu pagājis?",
            uzd="Skola celta 1963. gadā, pēdējoreiz remontēta 2011. gadā. Cik "
                "gadu pagāja starp abiem notikumiem?",
            soli=[
                ("2011 − 1963",
                 "Cik ilgi - tas ir atņemšana: vēlākais mīnus agrākais."),
                ("2011 − 1963 = 48",
                 "Var rēķināt pa daļām: no 1963 līdz 2000 ir 37, no 2000 līdz "
                 "2011 ir 11; kopā 48."),
            ],
            atbilde="pagāja 48 gadi"),

    Ievadi("Cik gadu starp notikumiem?", [
        {"jaut": "No 1918. gada līdz 2018. gadam - cik gadu?",
         "atb": ["100"], "padoms": "2018 − 1918."},
        {"jaut": "No 1991. gada līdz šodienai (2026. gads) - cik gadu?",
         "atb": ["35"], "padoms": "2026 − 1991."},
        {"jaut": "Cilvēks dzimis 1985. gadā. Cik viņam gadu 2026. gadā?",
         "atb": ["41"], "padoms": "2026 − 1985."},
        {"jaut": "Ēka celta 1878. gadā. Kurā gadā tai apritēja 100 gadu?",
         "atb": ["1978"], "padoms": "1878 + 100."},
        {"jaut": "Starp diviem notikumiem ir 250 gadu, vēlākais bija 1900. "
                 "gadā. Kurā gadā bija agrākais?",
         "atb": ["1650"], "padoms": "1900 − 250."},
        {"jaut": "Cik gadu ir vienā gadsimtā?",
         "atb": ["100"], "padoms": "Gadsimts nozīmē simts gadu."},
    ], pamats=4),

    Varianti("Kā lasīt laika asi?", [
        {"jaut": "Uz laika ass notikums A ir pa kreisi no notikuma B. Ko tas "
                 "nozīmē?",
         "opcijas": ["A notika agrāk", "A notika vēlāk",
                     "Abi notika vienlaikus", "A ilga ilgāk"],
         "pareizi": 0,
         "padoms": "Jo tālāk pa labi, jo vēlāk."},
        {"jaut": "Kurā gadsimtā ir 1945. gads?",
         "opcijas": ["20. gadsimtā", "19. gadsimtā", "21. gadsimtā",
                     "18. gadsimtā"],
         "pareizi": 0,
         "padoms": "Gadi no 1901 līdz 2000 ir 20. gadsimts."},
        {"jaut": "Ass iedaļa ir 50 gadu. Cik iedaļu aizņem 200 gadi?",
         "opcijas": ["4", "2", "200", "50"],
         "pareizi": 0,
         "padoms": "200 : 50."},
        {"jaut": "Kurš gads ir tuvāk 2026. gadam?",
         "opcijas": ["1999", "1950", "1918", "1880"],
         "pareizi": 0,
         "padoms": "Salīdzini starpības."},
    ], pamats=4),

    Pasaule("Cik gadu kosmosā?",
            Ievadi("", [
                {"jaut": "No 1957. līdz 1969. gadam - cik gadu?",
                 "atb": ["12"], "padoms": "1969 − 1957."},
                {"jaut": "Kosmosa stacija strādā kopš 1998. gada. Cik tai "
                         "gadu 2026. gadā?",
                 "atb": ["28"], "padoms": "2026 − 1998."},
                {"jaut": "No 1961. gada pagājuši 65 gadi. Kurš tagad ir gads?",
                 "atb": ["2026"], "padoms": "1961 + 65."},
                {"jaut": "Cik gadu ir pusgadsimtā?",
                 "atb": ["50"], "padoms": "Puse no simta."},
            ]),
            pavediens="kosmoss",
            konteksts="Pirmais satelīts lidoja 1957. gadā, pirmais cilvēks "
                      "kosmosā - 1961. gadā.",
            kapec="Laika ass parāda, cik strauji viss notika: divpadsmit "
                  "gados no satelīta līdz Mēnesim."),

    Kopsavilkums([
        "Atlieku gadskaitļus uz laika ass un izvēlos tai piemērotu iedaļu.",
        "Aprēķinu, cik gadu pagājis starp diviem notikumiem.",
        "Zinu, ka uz ass pa kreisi ir agrāk, pa labi - vēlāk.",
    ]),

    Majas([
        "Uzzīmē savas dzīves laika asi: dzimšana, skolas sākums, šodiena.",
        "Atrodi, cik gadu vecs ir tavs mājoklis.",
        "Uzzini, kurā gadā celta jūsu skola, un aprēķini, cik gadu tai ir.",
    ]),
]
