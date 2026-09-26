# -*- coding: utf-8 -*-
"""2. klase, 104. stunda: «Kādas figūras rodas, tās savietojot?»

No divām vai vairākām figūrām, tās noliekot malu pie malas, rodas jauna:
divi vienādi trijstūri - kvadrāts vai lielāks trijstūris, divi kvadrāti -
taisnstūris. Tangrama spēle ir šī ideja.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Pasaule, Petijums,
                         Sakums, Slidnis, Varianti, figura, geometrija)

TEMA = "Kādas figūras rodas, tās savietojot?"

MERKIS = ("Šodien veidosim jaunas figūras no dotajām, tās savietojot, un "
          "nosauksim rezultātu.")

_KVADRATS_NO_TRIJSTURIEM = geometrija(
    [("_A", 0, 0), ("_B", 4, 0), ("_C", 4, 4), ("_D", 0, 4)],
    nogriezni=[("_A", "_B"), ("_B", "_C"), ("_C", "_D"), ("_D", "_A"),
               ("_A", "_C")],
    iekrasot=[(["_A", "_B", "_C"], 0)])

SATURS = [
    Sakums("Kas sanāk, ja divas trijstūra sviestmaizes noliek kopā?",
           zimejums=_KVADRATS_NO_TRIJSTURIEM,
           paraksts="Divi trijstūri - viens kvadrāts.",
           fakti=["No figūrām var salikt jaunas figūras.",
                  "Ķīniešu spēlē tangramā no 7 gabaliem saliek simtiem "
                  "attēlu.",
                  "Kopā saliekot, malas pieskaras visā garumā."]),

    Doma("Savietošana",
         "Figūras noliek tā, lai malas pieskartos visā garumā.",
         soli=[
             "Izvēlies, kuras malas savietot - tām jābūt vienāda garuma.",
             "Noliec figūras blakus, malu pie malas.",
             "Apskati jaunās figūras robežu.",
             "Saskaiti stūrus un nosauc to.",
         ]),

    Slidnis("Divi kvadrāti", [
        {"v": "1 kvadrāts", "teksts": "4 stūri.",
         "zim": figura([(0, 0), (3, 0), (3, 3), (0, 3)], platums=7)},
        {"v": "+ vēl viens", "teksts": "Malu pie malas - taisnstūris.",
         "zim": figura([(0, 0), (6, 0), (6, 3), (0, 3)], platums=7)},
        {"v": "nobīdīts", "teksts": "Ar nobīdi - sešstūris.",
         "zim": figura([(0, 0), (3, 0), (3, 1), (6, 1), (6, 4), (3, 4),
                        (3, 3), (0, 3)], platums=7)},
    ]),

    Varianti("Kas sanāks?", [
        {"jaut": "Divi vienādi kvadrāti blakus, visu malu kopā.",
         "opcijas": ["taisnstūris", "trijstūris", "aplis"], "pareizi": 0,
         "padoms": "Garš un šaurs."},
        {"jaut": "Divi vienādi taisnleņķa trijstūri ar garāko malu kopā.",
         "opcijas": ["kvadrāts vai taisnstūris", "aplis", "piecstūris"],
         "pareizi": 0, "padoms": "Kā sviestmaize pa diagonāli."},
        {"jaut": "Kvadrāts un trijstūris virs tā.",
         "opcijas": ["piecstūris (mājiņa)", "četrstūris", "trijstūris"],
         "pareizi": 0, "padoms": "Saskaiti stūrus mājiņai."},
        {"jaut": "Četri vienādi kvadrāti 2 rindās pa 2.",
         "opcijas": ["lielāks kvadrāts", "trijstūris", "sešstūris"],
         "pareizi": 0, "padoms": "Visas malas vienādas."},
    ]),

    Petijums("Tangrams", [
        "Izgriez no kvadrāta 7 tangrama gabalus pēc parauga.",
        "Saliec no diviem mazajiem trijstūriem kvadrātu.",
        "Saliec no visiem 7 gabaliem kaķi vai laivu.",
        "Kādas figūras sanāca, savietojot gabalus?",
    ], vajag="papīra kvadrāts, šķēres, tangrama paraugs"),

    Pasaule("Parketa raksts",
            Varianti("", [
                {"jaut": "Parketu liek no taisnstūra dēlīšiem. Kas sanāk no "
                         "diviem blakus noliktiem?",
                 "opcijas": ["lielāks taisnstūris vai kvadrāts", "aplis",
                             "trijstūris"], "pareizi": 0,
                 "padoms": "Malu pie malas."},
            ]),
            pavediens="maja",
            konteksts="Grīdas raksts rodas, savietojot vienādas figūras.",
            kapec="No vienkāršām figūrām rodas skaisti raksti."),

    Kopsavilkums([
        "Savietoju figūras malu pie malas.",
        "Nosaucu jauno figūru.",
        "Zinu, ka no vienām figūrām var iegūt dažādas.",
    ]),

    Majas([
        "Izgriez 4 vienādus trijstūrus.",
        "Saliec no tiem kvadrātu un lielāku trijstūri.",
        "Kādas vēl figūras izdevās?",
    ]),
]
