# -*- coding: utf-8 -*-
"""9. klase, 8. stunda: «Kas ir līdzības koeficients?»

Līdzības koeficients k ir viens skaitlis, kas pasaka visu par izmēra maiņu:
k > 1 - palielinājums, k < 1 - samazinājums. Kartes mērogs ir tas pats k.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, lidzigi)

TEMA = "Kas ir līdzības koeficients?"

MERKIS = ("Noteiksim līdzības koeficientu un skaidrosim, ko tas parāda.")

_ABC = [(0, 0), (6, 0), (2.25, 3.31)]

SATURS = [
    Sakums("Kas kopīgs kartei un fotokopijai?",
           zimejums=lidzigi(_ABC, 0.5, malas=[(0, 1, "6"), (1, 2, "5")],
                            malas2=[(0, 1, "3"), (1, 2, "2,5")],
                            lenki=[(0, "", 1)]),
           paraksts="Visas malas samazinātas 2 reizes: k = 0,5.",
           fakti=["Līdzības koeficients k = {A_1B_1|AB}.",
                  "k > 1 - palielinājums, k < 1 - samazinājums.",
                  "Kartes mērogs 1 : 50 000 ir k = {1|50 000}."]),

    Doma("Līdzības koeficients",
         "Ja △ABC ∼ △A_1B_1C_1, tad k = {A_1B_1|AB} = {B_1C_1|BC} = "
         "{A_1C_1|AC}.",
         soli=[
             "Izvēlies vienu atbilstošo malu pāri ar zināmiem garumiem.",
             "Dali jaunā trijstūra malu ar sākotnējā malu.",
             "Pārējās malas: A_1B_1 = k · AB.",
             "Ja maina secību, iegūst {1|k}.",
         ]),

    Paraugs("Atrodi k un malu",
            uzd="△ABC ∼ △A_1B_1C_1. AB = 8 cm, A_1B_1 = 6 cm, BC = 10 cm. "
                "Atrodi k un B_1C_1.",
            soli=[
                ("k = {A_1B_1|AB} = {6|8} = 0,75", "Otrais ir mazāks."),
                ("B_1C_1 = k · BC = 0,75 · 10 = 7,5", "Visas malas reizina "
                                                      "ar k."),
            ],
            atbilde="k = 0,75; B_1C_1 = 7,5 cm"),

    Ievadi("Aprēķini", [
        {"jaut": "AB = 5, A_1B_1 = 15. k = ?", "atb": ["3"],
         "padoms": "15 : 5."},
        {"jaut": "AB = 12, A_1B_1 = 4. k = ?",
         "atb": ["{1|3}", "1/3"], "padoms": "4 : 12."},
        {"jaut": "k = 2,5, AC = 4. A_1C_1 = ?", "atb": ["10"],
         "padoms": "2,5 · 4."},
        {"jaut": "k = 0,4, B_1C_1 = 6. BC = ?", "atb": ["15"],
         "padoms": "6 : 0,4."},
        {"jaut": "Karte 1 : 25 000. 4 cm kartē = ? m dabā",
         "atb": ["1000"], "padoms": "4 · 25 000 cm."},
        {"jaut": "Karte 1 : 50 000. 3 km dabā = ? cm kartē", "atb": ["6"],
         "padoms": "300 000 cm : 50 000."},
    ], pamats=4),

    Varianti("Ko rāda k?", [
        {"jaut": "k = 1. Trijstūri ir...",
         "opcijas": ["vienādi", "otrais divreiz lielāks",
                     "nelīdzīgi", "otrais mazāks"],
         "pareizi": 0, "padoms": "Malas nemainās."},
        {"jaut": "k = 0,2. Otrais trijstūris ir...",
         "opcijas": ["5 reizes mazāks", "5 reizes lielāks",
                     "0,2 reizes lielāks", "2 reizes mazāks"],
         "pareizi": 0, "padoms": "1 : 0,2 = 5."},
        {"jaut": "Vai k var būt negatīvs?",
         "opcijas": ["Nē, garumi ir pozitīvi", "Jā", "Tikai platleņķa "
                     "trijstūrim", "Tikai samazinot"],
         "pareizi": 0, "padoms": "Garumu attiecība."},
    ]),

    Pasaule("Projektors klasē",
            Kustiba("", [
                {"jaut": "Slaidā trijstūra mala ir 4 cm, projektors palielina "
                         "ar k = 25. Cik cm tā ir uz ekrāna?",
                 "atb": 100, "beigas": 150, "iedala": 25, "mers": "cm",
                 "merkis": "ekrāna mala", "objekts": "Stars",
                 "padoms": "4 · 25."},
                {"jaut": "Ekrānā attēls ir 120 cm plats, slaidā - 4,8 cm. "
                         "Kāds ir k?",
                 "atb": 25, "beigas": 50, "iedala": 5, "mers": "",
                 "merkis": "k", "objekts": "k",
                 "padoms": "120 : 4,8."},
            ]),
            pavediens="tehnika",
            konteksts="Projektors katru slaida garumu palielina vienādi, "
                      "tāpēc attēls uz ekrāna ir līdzīgs slaidam.",
            kapec="Viens skaitlis k apraksta visu palielinājumu."),

    Kopsavilkums([
        "Aprēķinu līdzības koeficientu.",
        "Ar k atrodu nezināmās malas.",
        "Kartes mērogu saprotu kā līdzības koeficientu.",
    ]),

    Majas([
        "Izmēri telefona ekrānu un tā ekrānuzņēmumu datorā. Aprēķini k.",
        "Kartē 1 : 10 000 izmēri ceļu līdz skolai. Cik m tas ir?",
        "Uzzīmē trijstūri un tam līdzīgu ar k = 1,5.",
    ]),
]
