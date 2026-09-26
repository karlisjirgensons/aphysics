# -*- coding: utf-8 -*-
"""4. klase, 11. stunda: «Precīzi vai aptuveni?»

Mikrotemata noslēgums. Ne katram skaitlim jābūt precīzam: pilsētas
iedzīvotāju skaitu mainās katru dienu, bet cenai čekā jābūt līdz centam.
Stunda māca argumentēt izvēli un noapaļot līdz desmitiem, simtiem un
tūkstošiem - tas vajadzīgs aptuvenai vērtībai visā turpmākajā gadā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, kolonnas,
                         taisne)

TEMA = "Precīzi vai aptuveni?"

MERKIS = ("Pamatosim, kad lielumu raksturo precīzi un kad aptuveni, un "
          "noapaļosim skaitļus līdz desmitiem, simtiem un tūkstošiem.")

SATURS = [
    Sakums("Cik skatītāju bija stadionā?",
           zimejums=kolonnas([("precīzi", 8764), ("aptuveni", 9000)]),
           paraksts="Ziņās saka «ap 9000», biļešu kasē zina 8764.",
           fakti=["Kasē vajag precīzu skaitu - tur ir nauda.",
                  "Ziņās pietiek ar aptuveno - tā vieglāk iegaumēt."]),

    Doma("Noapaļo pēc cipara aiz vajadzīgās šķiras",
         "Ja nākamais cipars ir 0-4, noapaļo uz leju; ja 5-9 - uz augšu.",
         soli=[
             "Atrodi šķiru, līdz kurai apaļo.",
             "Paskaties uz ciparu tūlīt pa labi no tās.",
             "0, 1, 2, 3, 4 - šķira nemainās; 5, 6, 7, 8, 9 - palielinās "
             "par 1.",
             "Visus ciparus pa labi aizstāj ar nullēm; raksta ≈.",
         ],
         pieze="8764 ≈ 9000 (līdz tūkstošiem), 8764 ≈ 8800 (līdz simtiem), "
               "8764 ≈ 8760 (līdz desmitiem)."),

    Paraugs("Noapaļo 4350 līdz tūkstošiem",
            uzd="Noapaļo 4350 līdz tūkstošiem.",
            soli=[
                ("tūkstoši: 4", None),
                ("nākamais cipars: 3", "3 ir mazāks par 5."),
                ("4350 ≈ 4000", "Apaļo uz leju."),
            ],
            atbilde="4350 ≈ 4000"),

    Zimejums("Kuram tūkstotim tuvāk?",
             taisne(4000, 5000, 100, [(4350, "4350")]),
             paskaidro="4350 ir pa kreisi no vidus (4500), tāpēc tuvāk 4000.",
             ievads="Noapaļošana ir jautājums: kurai iedaļai tuvāk?"),

    Ievadi("Noapaļo", [
        {"jaut": "6280 līdz tūkstošiem ≈ ?", "atb": ["6000"],
         "padoms": "Simtos 2 - uz leju."},
        {"jaut": "6280 līdz simtiem ≈ ?", "atb": ["6300"],
         "padoms": "Desmitos 8 - uz augšu."},
        {"jaut": "3547 līdz desmitiem ≈ ?", "atb": ["3550"],
         "padoms": "Vienos 7 - uz augšu."},
        {"jaut": "9501 līdz tūkstošiem ≈ ?", "atb": ["10000", "10 000"],
         "padoms": "Simtos 5 - uz augšu; 9 + 1 = 10."},
        {"jaut": "1449 līdz simtiem ≈ ?", "atb": ["1400"],
         "padoms": "Desmitos 4 - uz leju."},
        {"jaut": "7050 līdz simtiem ≈ ?", "atb": ["7100"],
         "padoms": "Desmitos 5 - uz augšu."},
    ], pamats=4),

    Varianti("Precīzi vai aptuveni?", [
        {"jaut": "Maizes cena čekā", "opcijas": ["precīzi", "aptuveni"],
         "pareizi": 0, "padoms": "Maksā līdz centam."},
        {"jaut": "Cik cilvēku dzīvo Rīgā",
         "opcijas": ["aptuveni", "precīzi"], "pareizi": 0,
         "padoms": "Skaits mainās katru dienu."},
        {"jaut": "Tava tālruņa numurs", "opcijas": ["precīzi", "aptuveni"],
         "pareizi": 0, "padoms": "Ar aptuvenu numuru nevar piezvanīt."},
        {"jaut": "Attālums līdz Mēnesim",
         "opcijas": ["aptuveni", "precīzi"], "pareizi": 0,
         "padoms": "Tas mainās visu laiku."},
        {"jaut": "Tavs dzimšanas gads", "opcijas": ["precīzi", "aptuveni"],
         "pareizi": 0, "padoms": "Tas nemainās."},
        {"jaut": "Cik matu ir uz galvas",
         "opcijas": ["aptuveni", "precīzi"], "pareizi": 0,
         "padoms": "Neviens tos nesaskaita."},
    ], pamats=4),

    Pasaule("Cik skatītāju šovakar?",
            Ievadi("", [
                {"jaut": "Arēnā Rīga pārdotas 8764 biļetes. Cik tas ir "
                         "aptuveni tūkstošos?",
                 "atb": ["9000"], "padoms": "Simtos 7 - uz augšu."},
                {"jaut": "Koncertā bija 5432 cilvēki. Noapaļo līdz simtiem.",
                 "atb": ["5400"], "padoms": "Desmitos 3."},
                {"jaut": "Hallē ir 10 000 vietu, pārdotas 8764. Cik vietu "
                         "tukšas?",
                 "atb": ["1236"], "padoms": "10 000 − 8764."},
                {"jaut": "Noapaļo tukšo vietu skaitu līdz simtiem.",
                 "atb": ["1200"], "padoms": "Desmitos 3."},
            ]),
            pavediens="sports",
            konteksts="Hokeja spēles ziņās skatītāju skaitu noapaļo, bet "
                      "kasē skaita katru biļeti.",
            kapec="Jāizvēlas, kuram vajadzīgs precīzais un kuram - "
                  "aptuvenais."),

    Kopsavilkums([
        "Pamatoju, kad lielumu raksturo precīzi un kad aptuveni.",
        "Noapaļoju līdz desmitiem, simtiem un tūkstošiem.",
        "Aptuveno vērtību rakstu ar zīmi ≈.",
    ]),

    Majas([
        "Atrodi ziņās vai internetā trīs noapaļotus skaitļus. Kāpēc tie "
        "noapaļoti?",
        "Noapaļo sava soļu skaita vakardienas rezultātu līdz simtiem.",
        "Noapaļo savas skolas skolēnu skaitu līdz desmitiem.",
    ]),
]
