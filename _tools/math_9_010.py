# -*- coding: utf-8 -*-
"""9. klase, 10. stunda: «Kādas ir pārējās pazīmes?»

Otrā pazīme - divas malas proporcionālas un leņķis starp tām vienāds;
trešā - visas trīs malas proporcionālas. Tās atgādina trijstūru vienādības
pazīmes, tikai «vienāds» nomainīts ar «proporcionāls».
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, lidzigi, restis)

TEMA = "Kādas ir pārējās pazīmes?"

MERKIS = ("Formulēsim un lietosim līdzības pazīmes pēc malām un leņķa.")

_ABC = [(0, 0), (6, 0), (2.25, 3.31)]

SATURS = [
    Sakums("Vai leņķi var nemērīt?",
           zimejums=lidzigi(_ABC, 1.5,
                            malas=[(0, 1, "6"), (0, 2, "4"), (1, 2, "5")],
                            malas2=[(0, 1, "9"), (0, 2, "6"),
                                    (1, 2, "7,5")]),
           paraksts="{9|6} = {6|4} = {7,5|5} = 1,5",
           fakti=["Ja visas malas proporcionālas, leņķi ir vienādi paši.",
                  "Pietiek arī ar divām malām un leņķi starp tām.",
                  "Pazīmes atgādina vienādības pazīmes."]),

    Doma("Vēl divas pazīmes",
         "Trijstūri ir līdzīgi, ja divas malas ir proporcionālas un leņķi "
         "starp tām vienādi, vai ja visas trīs malas ir proporcionālas.",
         soli=[
             "Sakārto katra trijstūra malas no mazākās līdz lielākajai.",
             "Dali atbilstošās malas: mazākā ar mazāko, lielākā ar lielāko.",
             "Visas attiecības vienādas - līdzīgi pēc trim malām.",
             "Divām malām pārbaudi, vai vienādais leņķis ir STARP tām.",
         ]),

    Slidnis("Trīs pazīmes vienā skatā", [
        {"v": "2 leņķi", "teksts": "Divi leņķi vienādi",
         "zim": lidzigi(_ABC, 1.5, lenki=[(0, "", 1), (1, "", 2)])},
        {"v": "2 malas, leņķis", "teksts": "Divas malas proporcionālas, leņķis starp "
                                   "tām vienāds",
         "zim": lidzigi(_ABC, 1.5, malas=[(0, 1, "6"), (0, 2, "4")],
                        malas2=[(0, 1, "9"), (0, 2, "6")],
                        lenki=[(0, "", 1)])},
        {"v": "3 malas", "teksts": "Visas trīs malas proporcionālas",
         "zim": lidzigi(_ABC, 1.5,
                        malas=[(0, 1, "6"), (0, 2, "4"), (1, 2, "5")],
                        malas2=[(0, 1, "9"), (0, 2, "6"), (1, 2, "7,5")])},
    ]),

    Paraugs("Trīs malas",
            uzd="Vai trijstūri ar malām 4, 6, 8 un 6, 9, 12 ir līdzīgi?",
            soli=[
                ("{6|4} = 1,5; {9|6} = 1,5; {12|8} = 1,5",
                 "Sakārtotas malas, atbilstošās attiecības."),
                ("Visas attiecības vienādas", "Trešā pazīme."),
            ],
            atbilde="jā, līdzīgi ar k = 1,5"),

    Varianti("Līdzīgi vai nē?", [
        {"jaut": "Malas 3, 4, 5 un 6, 8, 10",
         "opcijas": ["Līdzīgi, k = 2", "Nelīdzīgi", "Vienādi",
                     "Līdzīgi, k = 3"],
         "pareizi": 0, "padoms": "Visas divkāršotas."},
        {"jaut": "Malas 2, 3, 4 un 4, 6, 7",
         "opcijas": ["Nelīdzīgi", "Līdzīgi, k = 2", "Līdzīgi, k = 1,5",
                     "Vienādi"],
         "pareizi": 0, "padoms": "{7|4} ≠ 2."},
        {"jaut": "AB = 3, AC = 5, ∠A = 40°; KL = 6, KM = 10, ∠K = 40°",
         "opcijas": ["Līdzīgi pēc 2. pazīmes", "Nelīdzīgi",
                     "Līdzīgi pēc 3. pazīmes", "Nevar zināt"],
         "pareizi": 0, "padoms": "{6|3} = {10|5}, leņķis starp tām."},
        {"jaut": "AB = 3, AC = 5, ∠B = 40°; KL = 6, KM = 10, ∠L = 40°",
         "opcijas": ["Ar šiem datiem nevar apgalvot", "Līdzīgi pēc 2. pazīmes",
                     "Nelīdzīgi noteikti", "Vienādi"],
         "pareizi": 0, "padoms": "Leņķis nav starp dotajām malām."},
    ]),

    Ievadi("Atrodi k vai malu", [
        {"jaut": "Malas 5, 7, 9 un 15, 21, x ir līdzīgas. x = ?",
         "atb": ["27"], "padoms": "k = 3."},
        {"jaut": "Malas 8, 10, 12 un 6, 7,5, x. x = ?", "atb": ["9"],
         "padoms": "k = 0,75."},
        {"jaut": "AB = 4, AC = 6, ∠A = 70°; A_1B_1 = 10, ∠A_1 = 70°. Kāds "
                 "jābūt A_1C_1, lai būtu līdzīgi?", "atb": ["15"],
         "padoms": "k = 2,5."},
        {"jaut": "Malas 6, 8, 10. Līdzīga trijstūra perimetrs 36. Tā "
                 "lielākā mala?", "atb": ["15"],
         "padoms": "P = 24, k = 1,5."},
    ]),

    Pasaule("Jumta kopnes no rūpnīcas",
            Ievadi("", [
                {"jaut": "Kopne ar sijām 3 m, 4 m, 5 m. Mazākai kopnei sijas "
                         "2,4 m, 3,2 m, 4 m. Kāds ir k?", "atb": ["0,8"],
                 "padoms": "2,4 : 3."},
                {"jaut": "Lielās kopnes jumta slīpums ir 37°. Mazās kopnes "
                         "slīpums (grādos)?", "atb": ["37"],
                 "padoms": "Līdzīgiem trijstūriem leņķi vienādi."},
            ]),
            pavediens="maja",
            konteksts="Rūpnīca kopnes ražo dažādos izmēros; ja sijas ir "
                      "proporcionālas, jumts būs vienādi slīps.",
            kapec="Proporcionālas malas nozīmē vienādus leņķus.",
            zimejums=restis([["kopne", "sijas, m"], ["liela", "3; 4; 5"],
                             ["maza", "2,4; 3,2; 4"]])),

    Kopsavilkums([
        "Formulēju līdzības pazīmi pēc divām malām un leņķa.",
        "Formulēju līdzības pazīmi pēc trim malām.",
        "Pārbaudu, vai leņķis ir starp dotajām malām.",
    ]),

    Majas([
        "Pārbaudi, vai trijstūri 5, 12, 13 un 7,5, 18, 19,5 ir līdzīgi.",
        "Uzraksti tabulu: vienādības pazīmes un līdzības pazīmes blakus.",
        "Izdomā piemēru, kur divas malas proporcionālas, bet trijstūri nav "
        "līdzīgi.",
    ]),
]
