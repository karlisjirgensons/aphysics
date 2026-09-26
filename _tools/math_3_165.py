# -*- coding: utf-8 -*-
"""3. klase, 165. stunda: «Kā ķermenis izskatās no augšas?»

Skati no trim pusēm ir tas pats, ko dara rasējumi un 3D programmas: telpisku
lietu apraksta ar plakaniem attēliem. No augšas skatoties, augstums pazūd -
tieši tāpēc vajag vairākus skatus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kā ķermenis izskatās no augšas?"

MERKIS = ("Zīmēsim telpiskas figūras skatus no dažādām pusēm.")

SATURS = [
    Sakums("Ko redz, skatoties uz kasti no augšas?",
           zimejums=restis([["skats", "ko redz"],
                            ["no augšas", "garums un platums"],
                            ["no priekšas", "garums un augstums"],
                            ["no sāniem", "platums un augstums"]],
                           "trīs skati"),
           paraksts="Katrā skatā viens izmērs pazūd.",
           fakti=["No augšas redz garumu un platumu, bet ne augstumu.",
                  "Tāpēc ķermeni apraksta ar trim skatiem."]),

    Doma("Katrā skatā viens izmērs pazūd",
         "Viens skats ķermeni neapraksta; vajag vismaz trīs - no augšas, no "
         "priekšas un no sāniem.",
         soli=[
             "Noliec ķermeni uz galda.",
             "Paskaties uz to tieši no augšas un uzzīmē, ko redzi.",
             "Tad no priekšas, tad no sāniem.",
             "Pieraksti pie katra zīmējuma, no kuras puses tas ir.",
         ],
         pieze="Skatā zīmē tikai kontūru - to, ko redz, nevis to, ko zini. "
               "Slēptās malas skatā neparādās."),

    Petijums("Uzzīmē trīs skatus",
             vajag="kastīte, lapa un zīmulis",
             soli=[
                 "Noliec kastīti uz galda un izmēri tās trīs izmērus.",
                 "Uzzīmē skatu no augšas ar īstajiem izmēriem.",
                 "Uzzīmē skatu no priekšas un no sāniem.",
                 "Pieraksti pie katra zīmējuma tā nosaukumu.",
             ],
             secinajums="Trīs skati kopā pastāsta visu par kastīti - pēc "
                        "tiem to var izgatavot, pašu kastīti neredzot."),

    Paraugs("Kādi ir kastes skati?",
            uzd="Kaste ir 5 cm gara, 3 cm plata un 2 cm augsta. Kādi "
                "taisnstūri ir trijos skatos?",
            soli=[
                ("No augšas: 5 x 3",
                 "Garums un platums."),
                ("No priekšas: 5 x 2",
                 "Garums un augstums."),
                ("No sāniem: 3 x 2",
                 "Platums un augstums."),
            ],
            atbilde="5 x 3, 5 x 2 un 3 x 2"),

    Ievadi("Skatu laukumi", [
        {"jaut": "Kaste 5 x 3 x 2. Cik kvadrātcentimetru ir skats no augšas?",
         "atb": ["15"], "padoms": "5 · 3."},
        {"jaut": "Cik kvadrātcentimetru ir skats no priekšas?", "atb": ["10"],
         "padoms": "5 · 2."},
        {"jaut": "Cik kvadrātcentimetru ir skats no sāniem?", "atb": ["6"],
         "padoms": "3 · 2."},
        {"jaut": "Cik kvadrātcentimetru ir visu trīs skatu summa?",
         "atb": ["31"], "padoms": "15 + 10 + 6."},
        {"jaut": "Cik kvadrātcentimetru ir visa kastes virsma?",
         "atb": ["62"], "padoms": "2 · 31."},
        {"jaut": "Kubs ar malu 4 cm. Cik kvadrātcentimetru ir viens skats?",
         "atb": ["16"], "padoms": "4 · 4."},
    ], pamats=4),

    Zimejums("Kuba skati",
             restis([["skats", "forma"],
                     ["no augšas", "kvadrāts"],
                     ["no priekšas", "kvadrāts"],
                     ["no sāniem", "kvadrāts"]],
                    "kubam visi skati vienādi"),
             paskaidro="Kubam visi trīs skati ir vienādi kvadrāti - tāpēc pēc "
                       "viena skata to var atpazīt.",
             ievads="Īpašais gadījums."),

    Varianti("Ko redz skatā?", [
        {"jaut": "Kas pazūd, skatoties no augšas?",
         "opcijas": ["Augstums", "Garums", "Platums", "Nekas"],
         "pareizi": 0, "padoms": "Skatās tieši uz leju."},
        {"jaut": "Cik skatu vajag, lai aprakstītu kasti?",
         "opcijas": ["3", "1", "2", "6"],
         "pareizi": 0, "padoms": "Trīs izmēri, trīs skati."},
        {"jaut": "Kāda forma ir kuba skatam no jebkuras puses?",
         "opcijas": ["Kvadrāts", "Taisnstūris", "Riņķis", "Trīsstūris"],
         "pareizi": 0, "padoms": "Visas skaldnes vienādas."},
        {"jaut": "Kaste 6 x 4 x 3. Cik kvadrātvienību ir skats no priekšas?",
         "opcijas": ["18", "24", "12", "6"],
         "pareizi": 0, "padoms": "6 · 3."},
    ], pamats=4),

    Pasaule("Kā dators rāda telpisku modeli?",
            Ievadi("", [
                {"jaut": "Modelis 8 x 5 x 4. Cik kvadrātvienību ir skats no "
                         "augšas?",
                 "atb": ["40"], "padoms": "8 · 5."},
                {"jaut": "Cik kvadrātvienību ir skats no priekšas?",
                 "atb": ["32"], "padoms": "8 · 4."},
                {"jaut": "Cik kvadrātvienību ir skats no sāniem?",
                 "atb": ["20"], "padoms": "5 · 4."},
                {"jaut": "Cik kubikvienību ir modeļa tilpums?",
                 "atb": ["160"], "padoms": "8 · 5 · 4."},
            ]),
            pavediens="dati",
            konteksts="Datorprogrammā telpisku modeli rāda no vairākām "
                      "pusēm - tieši tāpat kā rasējumā.",
            kapec="Viens attēls telpisku lietu nekad neapraksta pilnībā."),

    Kopsavilkums([
        "Zīmēju ķermeņa skatus no augšas, priekšas un sāniem.",
        "Zinu, ka katrā skatā viens izmērs pazūd.",
        "Aprēķinu katra skata laukumu.",
        "Zinu, ka kubam visi skati ir vienādi.",
    ]),

    Majas([
        "Uzzīmē trīs skatus savai skolas somai.",
        "Uzzīmē trīs skatus krūzei.",
        "Parādi zīmējumus mājiniekiem un lūdz uzminēt priekšmetu.",
    ]),
]
