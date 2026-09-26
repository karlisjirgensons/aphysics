# -*- coding: utf-8 -*-
"""7. klase, 29. stunda: «Kā lasīt zīmējumu?»

Ģeometrijas uzdevumā zīmējumā ir vairāk figūru, nekā no pirmā acu
uzmetiena šķiet. Stunda iemāca sistemātiski meklēt nogriežņus un
trijstūrus - ar to pašu pilno pārlasi, ko mācījāmies kopās.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, geometrija)

TEMA = "Kā lasīt zīmējumu?"

MERKIS = ("Iemācīsimies atrast un pierakstīt visas figūras dotajā "
          "zīmējumā.")

_TRIJST = geometrija([("A", 0, 0), ("B", 3, 0), ("C", 6, 0), ("D", 3, 4)],
                     nogriezni=["AC", "AD", "BD", "CD"])

SATURS = [
    Sakums("Cik trijstūru ir šajā zīmējumā?",
           zimejums=_TRIJST,
           paraksts="Vairums cilvēku saka «divi». Pareizi - trīs.",
           fakti=["ABD un BCD redz uzreiz.",
                  "Bet arī ACD ir trijstūris - lielais.",
                  "Sistēma palīdz neizlaist nevienu."]),

    Doma("Meklē sistemātiski",
         "Lai atrastu visas figūras zīmējumā, tās uzskaita pēc noteikuma: "
         "piemēram, trijstūrus - pēc virsotnēm, nogriežņus - pēc katras "
         "līnijas punktiem.",
         soli=[
             "Nosauc visus punktus ar burtiem.",
             "Katrā līnijā saskaiti punktus: n punkti dod n · (n − 1) : 2 "
             "nogriežņus.",
             "Trijstūrus meklē, ņemot trīs punktus, kas pa pāriem savienoti "
             "un nav uz vienas līnijas.",
             "Pieraksti katru figūru ar burtiem - tā redz, ka nav "
             "atkārtojumu.",
         ],
         pieze="Trijstūrim ABD un DBA ir viena un tā pati figūra - to "
               "skaita vienu reizi."),

    Paraugs("Nogriežņi zīmējumā",
            uzd="Sākuma zīmējumā saskaiti visus nogriežņus.",
            soli=[
                ("Uz līnijas AC ir A, B, C: 3 nogriežņi",
                 "AB, BC, AC."),
                ("AD, BD, CD - pa vienam", "Trīs līnijas no D."),
                ("3 + 3 = 6", "Kopā."),
            ],
            atbilde="6 nogriežņi: AB, BC, AC, AD, BD, CD"),

    Zimejums("Divas diagonāles",
             geometrija([("A", 0, 0), ("B", 6, 0), ("C", 6, 4), ("D", 0, 4),
                         ("O", 3, 2, 90)],
                        nogriezni=["AB", "BC", "CD", "DA", "AC", "BD"]),
             ievads="Taisnstūris ar diagonālēm.",
             paskaidro="Trijstūri: 4 mazie (AOB, BOC, COD, DOA) un 4 lielie "
                       "(ABC, BCD, CDA, DAB) - kopā 8."),

    Ievadi("Saskaiti figūras", [
        {"jaut": "Taisnstūrī ar abām diagonālēm - cik trijstūru?",
         "atb": ["8"], "padoms": "4 mazie un 4 lielie."},
        {"jaut": "Tajā pašā zīmējumā - cik nogriežņu (visus, arī daļas)?",
         "atb": ["10"], "padoms": "4 malas + katrā diagonālē 3."},
        {"jaut": "Trijstūrī no virsotnes uz pretējo malu novilkti 2 "
                 "nogriežņi. Cik trijstūru?",
         "atb": ["6"], "padoms": "Uz pamata 4 punkti: 4 · 3 : 2."},
        {"jaut": "No viena punkta iziet 4 stari. Cik leņķu (mazāku par "
                 "180°) veido stari?",
         "atb": ["6"], "padoms": "Katrs pāris staru: 4 · 3 : 2."},
    ]),

    Varianti("Pieraksti pareizi", [
        {"jaut": "Kurš pieraksts apzīmē to pašu trijstūri kā ABD?",
         "opcijas": ["DBA", "ABC", "ABB", "AD"],
         "pareizi": 0,
         "padoms": "Tie paši trīs burti."},
        {"jaut": "Punkti A, B, C ir uz vienas taisnes. Vai ABC ir "
                 "trijstūris?",
         "opcijas": ["Nē", "Jā", "Tikai, ja B ir vidū", "Nevar zināt"],
         "pareizi": 0,
         "padoms": "Tas ir nogrieznis AC."},
    ]),

    Pasaule("Tilta kopne",
            Ievadi("", [
                {"jaut": "Tilta kopnē apakšā 5 punkti vienā līnijā, visi "
                         "savienoti ar vienu augšējo punktu. Cik trijstūru?",
                 "atb": ["10"], "padoms": "Divi apakšējie punkti + "
                                         "augšējais: 5 · 4 : 2."},
                {"jaut": "Cik tēraudsiju ir kopnē (apakšējā josla "
                         "sadalīta 4 daļās, plus 5 slīpās)?",
                 "atb": ["9"], "padoms": "4 + 5."},
                {"jaut": "Kāpēc tiltus būvē no trijstūriem, nevis "
                         "kvadrātiem? Kurš ir cietāks - «trijstūris» vai "
                         "«četrstūris»?",
                 "atb": ["trijstūris", "trijsturis"],
                 "padoms": "Trijstūri nevar saspiest, nemainot malas.",
                 "tastatura": "text"},
            ]),
            pavediens="tehnika",
            konteksts="Tiltu kopnes un torņu konstrukcijas ir tīkls no "
                      "trijstūriem.",
            kapec="Inženieris saskaita katru trijstūri, jo katrs nes slodzi."),

    Kopsavilkums([
        "Nosaucu visus punktus un skaitu sistemātiski.",
        "Uz līnijas ar n punktiem atrodu n · (n − 1) : 2 nogriežņus.",
        "Atrodu arī lielos, «saliktos» trijstūrus.",
        "Pierakstu katru figūru ar burtiem.",
    ]),

    Majas([
        "Uzzīmē trijstūri ar 3 nogriežņiem no virsotnes un saskaiti "
        "trijstūrus.",
        "Atrodi zīmējumu ar figūrām (logs, karogs) un saskaiti trijstūrus.",
        "Izdomā zīmējumu, kurā ir tieši 5 trijstūri.",
    ]),
]
