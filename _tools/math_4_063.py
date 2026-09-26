# -*- coding: utf-8 -*-
"""4. klase, 63. stunda: «Kā papildināt zīmējumu?»

Dots stars un leņķis; jāpievieno vēl viens dota lieluma leņķis. Bieži
iespējami divi zīmējumi - jauno staru var likt uz vienu vai otru pusi. Tas
dod divas dažādas atbildes kopējam leņķim (summa vai starpība) - pirmā
tikšanās ar uzdevumu, kuram ir vairāk nekā viens atrisinājums.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, lenkis)

TEMA = "Kā papildināt zīmējumu?"

MERKIS = ("Papildināsim zīmējumu ar dota lieluma leņķi un spriedīsim, cik "
          "veidos to var izdarīt.")

SATURS = [
    Sakums("Kur likt jauno staru?",
           zimejums=lenkis([(0, "A"), (50, "B"), (80, "C?"), (20, "C?")],
                           loki=[(0, 50, "50°")]),
           paraksts="∠AOB = 50°. Jāpievieno ∠BOC = 30° - bet uz kuru pusi?",
           fakti=["Staru OC var likt aiz OB vai starp OA un OB.",
                  "Tāpēc ∠AOC var būt 80° vai 20°."]),

    Doma("Divas puses - divas iespējas",
         "Pievienojot leņķi pie esoša stara, jaunais stars var iet uz vienu "
         "vai otru pusi; kopējais leņķis tad ir summa vai starpība.",
         soli=[
             "Uz ārpusi: ∠AOC = ∠AOB + ∠BOC.",
             "Uz iekšpusi: ∠AOC = ∠AOB − ∠BOC.",
             "Uzzīmē abus variantus.",
             "Ja uzdevumā teikts «ārpus leņķa AOB», der tikai viens.",
         ],
         pieze="Ja ∠BOC ir lielāks par ∠AOB, uz iekšpusi stars aiziet otrpus "
               "OA."),

    Paraugs("∠AOB = 70°, pievieno 40°",
            uzd="∠AOB = 70°. Uzzīmē ∠BOC = 40°. Cik var būt ∠AOC?",
            soli=[
                ("70° + 40° = 110°", "Ja OC ārpus ∠AOB."),
                ("70° − 40° = 30°", "Ja OC iekšpusē."),
            ],
            atbilde="110° vai 30°"),

    Zimejums("Blakus leņķi uz taisnes",
             lenkis([(0, "A"), (65, "B"), (180, "C")],
                    loki=[(0, 65, "65°"), (65, 180, "?")]),
             paskaidro="Stari OA un OC veido taisni (180°), tāpēc "
                       "∠BOC = 180° − 65° = 115°.",
             ievads="Kad viena mala turpinās taisnē, otrs leņķis ir 180° "
                    "mīnus pirmais."),

    Ievadi("Aprēķini", [
        {"jaut": "∠AOB = 50°, ∠BOC = 30° ārpusē. ∠AOC = ?", "atb": ["80"],
         "padoms": "50 + 30."},
        {"jaut": "∠AOB = 50°, ∠BOC = 30° iekšpusē. ∠AOC = ?", "atb": ["20"],
         "padoms": "50 − 30."},
        {"jaut": "Uz taisnes: viens leņķis 65°. Otrs = ?", "atb": ["115"],
         "padoms": "180 − 65."},
        {"jaut": "Uz taisnes: viens leņķis 90°. Otrs = ?", "atb": ["90"],
         "padoms": "180 − 90."},
        {"jaut": "Taisnu leņķi sadala stars; viena daļa 35°. Otra = ?",
         "atb": ["55"], "padoms": "90 − 35."},
        {"jaut": "∠AOB = 100°, ∠BOC = 45° ārpusē. ∠AOC = ?", "atb": ["145"],
         "padoms": "100 + 45."},
    ], pamats=4),

    Varianti("Cik atrisinājumu?", [
        {"jaut": "∠AOB = 60°. Pievieno ∠BOC = 20°. Cik iespējamu ∠AOC?",
         "opcijas": ["2", "1", "3", "bezgalīgi daudz"], "pareizi": 0,
         "padoms": "Uz ārpusi un iekšpusi."},
        {"jaut": "Ja teikts «OC ārpus ∠AOB», cik atrisinājumu?",
         "opcijas": ["1", "2", "0"], "pareizi": 0,
         "padoms": "Viena puse izslēgta."},
        {"jaut": "Blakus leņķi uz taisnes kopā ir...",
         "opcijas": ["180°", "90°", "360°", "100°"], "pareizi": 0,
         "padoms": "Izstiepts leņķis."},
    ]),

    Pasaule("Grāmatplaukta atbalsts",
            Ievadi("", [
                {"jaut": "Plaukta atbalsts ar sienu veido 90°. Slīpā "
                         "atsaite ar plauktu veido 50°. Cik grādu ar sienu?",
                 "atb": ["40"], "padoms": "90 − 50."},
                {"jaut": "Durvis atvērtas 70° no sienas. Cik grādu vēl līdz "
                         "taisnei (180°)?",
                 "atb": ["110"], "padoms": "180 − 70."},
                {"jaut": "Lampas kāja noliekta 30° no vertikāles. Cik grādu "
                         "no horizontāles?",
                 "atb": ["60"], "padoms": "90 − 30."},
                {"jaut": "Klēpjdators atvērts 115°. Par cik grādiem jāatver "
                         "vēl, lai tas būtu plakans (180°)?",
                 "atb": ["65"], "padoms": "180 − 115."},
            ]),
            pavediens="maja",
            konteksts="Mājās leņķi bieži papildina viens otru līdz 90° vai "
                      "180° - pie sienas, grīdas vai galda.",
            kapec="Zinot vienu leņķi, otru var aprēķināt, nemērot."),

    Kopsavilkums([
        "Papildinu zīmējumu ar dota lieluma leņķi.",
        "Zinu, ka bieži ir divi atrisinājumi.",
        "Aprēķinu leņķi, ja kopā tie veido 90° vai 180°.",
    ]),

    Majas([
        "Uzzīmē ∠AOB = 80° un pievieno ∠BOC = 25° abos veidos.",
        "Izmēri, cik grādos atvērtas jūsu istabas durvis, un aprēķini, cik "
        "līdz 180°.",
        "Izdomā uzdevumu, kuram ir divas atbildes.",
    ]),
]
