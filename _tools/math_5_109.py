# -*- coding: utf-8 -*-
"""5. klase, 109. stunda: «Kā sadalīt izstieptu leņķi?»

Pirmais leņķu aprēķins, un tas balstās uz vienu faktu: izstiepts leņķis ir
180°. Ja to sadala ar staru, abi iegūtie leņķi kopā joprojām ir 180°, tāpēc
otru var atrast ar atņemšanu. Tas ir tas pats «papildini līdz veselam», kas
bija 68. stundā, tikai veselais te ir 180.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, lenkis)

TEMA = "Kā sadalīt izstieptu leņķi?"

MERKIS = ("Iemācīsimies ar staru sadalīt izstieptu leņķi un aprēķināt otra "
          "leņķa lielumu.")

SATURS = [
    Sakums("Viens stars, divi leņķi",
           zimejums=lenkis([(0, "A"), (60, "C"), (180, "B")],
                           loki=[(0, 60, "60°"), (60, 180, "?")],
                           virsraksts="Izstiepts leņķis, sadalīts ar staru"),
           paraksts="Abi leņķi kopā ir 180°, tāpēc otrs ir 120°.",
           fakti=["Izstiepts leņķis ir 180°.",
                  "Stars to sadala divos leņķos.",
                  "Abu leņķu summa paliek 180°."]),

    Doma("Abu daļu summa ir 180°",
         "Ja izstieptu leņķi sadala ar staru, abu iegūto leņķu summa ir "
         "180°, tāpēc otru atrod, no 180° atņemot pirmo.",
         soli=[
             "Pārliecinies, ka abi malējie stari veido taisni.",
             "Pieraksti zināmā leņķa lielumu.",
             "Atņem to no 180°.",
             "Pieraksti atbildi ar grādu zīmi.",
             "Pārbaudi: abu leņķu summai jābūt 180°.",
         ],
         pieze="Divus leņķus, kuru summa ir 180°, sauc par blakusleņķiem. "
               "Tieši tāpēc, zinot vienu, otru vienmēr var izrēķināt bez "
               "mērīšanas."),

    Paraugs("Viens leņķis ir 60°",
            uzd="Izstieptu leņķi sadala ar staru tā, ka viens leņķis ir 60°. "
                "Cik liels ir otrs?",
            soli=[
                ("Izstiepts leņķis ir 180°",
                 "Veselais, ko dala."),
                ("180° - 60° = 120°",
                 "Atņem zināmo leņķi."),
                ("Otrs leņķis ir 120°",
                 "Tas ir plats leņķis."),
                ("Pārbaude: 60° + 120° = 180°",
                 "Summa sakrīt."),
            ],
            atbilde="Otrs leņķis ir 120°"),

    Ievadi("Aprēķini otru leņķi", [
        {"jaut": "Viens leņķis ir 60°. Cik grādu ir otrs?",
         "atb": ["120"], "padoms": "180 - 60."},
        {"jaut": "Viens leņķis ir 90°. Cik grādu ir otrs?",
         "atb": ["90"], "padoms": "180 - 90."},
        {"jaut": "Viens leņķis ir 45°. Cik grādu ir otrs?",
         "atb": ["135"], "padoms": "180 - 45."},
        {"jaut": "Viens leņķis ir 30°. Cik grādu ir otrs?",
         "atb": ["150"], "padoms": "180 - 30."},
        {"jaut": "Viens leņķis ir 125°. Cik grādu ir otrs?",
         "atb": ["55"], "padoms": "180 - 125."},
        {"jaut": "Viens leņķis ir 72°. Cik grādu ir otrs?",
         "atb": ["108"], "padoms": "180 - 72."},
        {"jaut": "Abi leņķi ir vienādi. Cik grādu ir katrs?",
         "atb": ["90"], "padoms": "180 : 2."},
        {"jaut": "Viens leņķis ir 1°. Cik grādu ir otrs?",
         "atb": ["179"], "padoms": "180 - 1."},
    ], pamats=4,
        ievads="Vienmēr viens un tas pats rēķins: 180° mīnus zināmais."),

    Zimejums("Divi blakusleņķi",
             lenkis([(0, "A"), (125, "C"), (180, "B")],
                    loki=[(0, 125, "125°"), (125, 180, "55°")],
                    virsraksts="125° + 55° = 180°"),
             paskaidro="Viens leņķis ir plats, otrs - šaurs, bet kopā tie "
                       "vienmēr dod izstieptu leņķi.",
             ievads="Jo lielāks viens, jo mazāks otrs."),

    Varianti("Kāds ir otrs leņķis?", [
        {"jaut": "Cik ir abu blakusleņķu summa?",
         "opcijas": ["180°", "90°", "360°", "Tas atkarīgs"],
         "pareizi": 0,
         "padoms": "Izstiepts leņķis."},
        {"jaut": "Viens leņķis ir 40°. Kāds ir otrs?",
         "opcijas": ["140°", "50°", "320°", "40°"],
         "pareizi": 0,
         "padoms": "180 - 40."},
        {"jaut": "Ja viens leņķis ir taisns, kāds ir otrs?",
         "opcijas": ["Arī taisns", "Plats", "Šaurs", "Izstiepts"],
         "pareizi": 0,
         "padoms": "180 - 90 = 90."},
        {"jaut": "Ja viens leņķis ir šaurs, kāds ir otrs?",
         "opcijas": ["Plats", "Šaurs", "Taisns", "Izstiepts"],
         "pareizi": 0,
         "padoms": "Mazāks par 90 atņem no 180."},
        {"jaut": "Vai abi blakusleņķi var būt plati?",
         "opcijas": ["Nevar, summa pārsniegtu 180°", "Var",
                     "Var, ja tie ir vienādi", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Katrs plats leņķis ir vairāk par 90°."},
        {"jaut": "Viens leņķis ir 105°. Kāds ir otrs?",
         "opcijas": ["75°", "85°", "95°", "105°"],
         "pareizi": 0,
         "padoms": "180 - 105."},
    ], pamats=4),

    Pasaule("Cik pagriezies slīpais balsts?",
            Ievadi("", [
                {"jaut": "Balsts ar grīdu veido 60° leņķi. Cik grādu ir "
                         "leņķis no otras puses?",
                 "atb": ["120"], "padoms": "180 - 60."},
                {"jaut": "Cits balsts veido 35° leņķi. Cik grādu ir otrs?",
                 "atb": ["145"], "padoms": "180 - 35."},
                {"jaut": "Balsts stāv taisni. Cik grādu ir abi leņķi?",
                 "atb": ["90"], "padoms": "180 : 2."},
                {"jaut": "Leņķis no vienas puses ir 100°. Cik no otras?",
                 "atb": ["80"], "padoms": "180 - 100."},
            ]),
            pavediens="tehnika",
            konteksts="Konstrukcijās mēra vienu leņķi, bet zīmējumā jāieraksta "
                      "abi.",
            kapec="Otru var izrēķināt, nevis mērīt otrreiz."),

    Kopsavilkums([
        "Zinu, ka izstiepts leņķis ir 180°.",
        "Aprēķinu otro leņķi, no 180° atņemot zināmo.",
        "Zinu, ka divus tādus leņķus sauc par blakusleņķiem.",
        "Pārbaudu rezultātu, saskaitot abus leņķus.",
    ]),

    Majas([
        "Aprēķini blakusleņķus leņķiem 25°, 88° un 143°.",
        "Uzzīmē izstieptu leņķi un sadali to divos vienādos leņķos.",
        "Atrodi mājās vietu, kur divi leņķi kopā veido taisni.",
    ]),
]
