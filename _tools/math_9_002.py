# -*- coding: utf-8 -*-
"""9. klase, 2. stunda: «Ko dara paralēlas taisnes leņķī?»

Talesa teorēmas vispārinājums: paralēlas taisnes, krustojot leņķa malas,
nogriež uz tām proporcionālus nogriežņus. Slīdnis bīda otro taisni un rāda,
ka attiecība uz abām malām mainās vienādi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, geometrija)

TEMA = "Ko dara paralēlas taisnes leņķī?"

MERKIS = ("Noteiksim proporcionālus nogriežņus, ja leņķa malas krusto "
          "paralēlas taisnes.")

# Otrā malas virziens; A_1 ir uz tā tikpat tālu kā A uz pirmās (t = 1).
_DX, _DY = 2.0, 2.4


def _lenkis(ob, malas=()):
    """Leņķis O ar paralēlām taisnēm AA_1 un BB_1; OA = 3, OB = ob."""
    t = ob / 3.0
    return geometrija([("O", 0, 0), ("A", 3, 0), ("B", ob, 0),
                       ("A_1", _DX, _DY), ("B_1", _DX * t, _DY * t)],
                      nogriezni=[("O", "B"), ("O", "B_1"), ("A", "A_1"),
                                 ("B", "B_1")],
                      izcelti=[("A", "A_1"), ("B", "B_1")],
                      malas=list(malas))


SATURS = [
    Sakums("Kāpēc ēnas ir proporcionālas?",
           zimejums=_lenkis(7, [("OA", "3"), ("AB", "4")]),
           paraksts="Saules stari ir paralēli - tie nogriež proporcionālus "
                    "nogriežņus.",
           fakti=["Paralēlas taisnes krusto abas leņķa malas.",
                  "Uz vienas malas OA : AB = 3 : 4.",
                  "Tad arī uz otras OA_1 : A_1B_1 = 3 : 4."]),

    Doma("Paralēlas taisnes leņķī",
         "Ja paralēlas taisnes krusto leņķa malas, tās nogriež uz malām "
         "proporcionālus nogriežņus: {OA|AB} = {OA_1|A_1B_1}.",
         soli=[
             "Pārliecinies, ka taisnes tiešām ir paralēlas.",
             "Uz katras malas nosauc nogriežņus no virsotnes.",
             "Pieraksti proporciju: atbilstošais pret atbilstošo.",
             "Der arī {OA|OB} = {OA_1|OB_1} - visa mala pret daļu.",
         ],
         pieze="Ja nogriežņi uz vienas malas ir vienādi, tad vienādi ir arī "
               "uz otras - tā ir Talesa teorēma."),

    Slidnis("Bīdi otro taisni", [
        {"v": "OB = 6", "teksts": "OA : AB = 3 : 3 un OA_1 : A_1B_1 = 3 : 3",
         "zim": _lenkis(6)},
        {"v": "OB = 7,5", "teksts": "OA : AB = 3 : 4,5 = 2 : 3 - uz abām malām",
         "zim": _lenkis(7.5)},
        {"v": "OB = 9", "teksts": "OA : AB = 3 : 6 = 1 : 2 - uz abām malām",
         "zim": _lenkis(9)},
    ], ievads="Taisne BB_1 paliek paralēla AA_1. Kas notiek ar attiecībām?"),

    Paraugs("Atrodi nogriezni",
            uzd="AA_1 ∥ BB_1. OA = 3 cm, AB = 4 cm, OA_1 = 4,5 cm. Atrodi "
                "A_1B_1.",
            soli=[
                ("{OA|AB} = {OA_1|A_1B_1}", "Paralēlas taisnes leņķī."),
                ("{3|4} = {4,5|A_1B_1}", "Ievieto zināmos."),
                ("A_1B_1 = {4 · 4,5|3} = 6", "Krusteniskā reizināšana."),
            ],
            atbilde="A_1B_1 = 6 cm"),

    Ievadi("Aprēķini (AA_1 ∥ BB_1)", [
        {"jaut": "OA = 2, AB = 6, OA_1 = 3. A_1B_1 = ?", "atb": ["9"],
         "padoms": "{2|6} = {3|x}."},
        {"jaut": "OA = 5, AB = 5, OA_1 = 7. A_1B_1 = ?", "atb": ["7"],
         "padoms": "Vienādi nogriežņi - vienādi arī uz otras malas."},
        {"jaut": "OA = 4, OB = 10, OA_1 = 6. OB_1 = ?", "atb": ["15"],
         "padoms": "{OA|OB} = {OA_1|OB_1}."},
        {"jaut": "OA_1 = 8, A_1B_1 = 12, OA = 6. AB = ?", "atb": ["9"],
         "padoms": "{6|x} = {8|12}."},
        {"jaut": "OA = 3, OB = 12, OB_1 = 20. OA_1 = ?", "atb": ["5"],
         "padoms": "OB ir 4 reizes garāks par OA."},
        {"jaut": "OA = 2,5, AB = 5, A_1B_1 = 7. OA_1 = ?", "atb": ["3,5"],
         "padoms": "AB = 2 · OA, tātad arī A_1B_1 = 2 · OA_1."},
    ], pamats=4),

    Varianti("Kura proporcija ir pareiza?", [
        {"jaut": "AA_1 ∥ BB_1 leņķī O.",
         "opcijas": ["{OA|AB} = {OA_1|A_1B_1}", "{OA|AB} = {A_1B_1|OA_1}",
                     "{OA|OA_1} = {OB_1|OB}", "OA + AB = OA_1 + A_1B_1"],
         "pareizi": 0, "padoms": "Uz katras malas tā pati secība."},
        {"jaut": "Ja taisnes AA_1 un BB_1 NAV paralēlas, tad...",
         "opcijas": ["proporcija var nebūt spēkā", "proporcija ir vienmēr",
                     "nogriežņi vienmēr vienādi", "leņķis ir taisns"],
         "pareizi": 0, "padoms": "Teorēmas nosacījums ir paralelitāte."},
        {"jaut": "OA = AB. Ko var secināt?",
         "opcijas": ["OA_1 = A_1B_1", "OA = OA_1", "AB = A_1B_1",
                     "OB = OB_1"],
         "pareizi": 0, "padoms": "Talesa teorēma."},
    ]),

    Pasaule("Zemes gabali starp ielām",
            Ievadi("", [
                {"jaut": "Divas ielas iziet no viena krustojuma. Paralēlas "
                         "robežas uz pirmās ielas nogriež 30 m un 45 m. Uz "
                         "otras pirmais gabals ir 40 m. Otrais (m)?",
                 "atb": ["60"], "padoms": "{30|45} = {40|x}."},
                {"jaut": "Cik m ir abu gabalu kopējā fasāde gar otro ielu?",
                 "atb": ["100"], "padoms": "40 + 60."},
                {"jaut": "Cik reizes otrā gabala fasāde garāka par pirmo?",
                 "atb": ["1,5"], "padoms": "60 : 40."},
            ]),
            pavediens="maja",
            konteksts="Zemes gabalu robežas bieži ir paralēlas - tad fasāžu "
                      "garumi uz abām ielām ir proporcionāli.",
            kapec="Mērnieks izmēra vienu ielu un otru izrēķina."),

    Kopsavilkums([
        "Formulēju, ko paralēlas taisnes nogriež uz leņķa malām.",
        "Pierakstu pareizu proporciju.",
        "Aprēķinu nezināmo nogriezni.",
    ]),

    Majas([
        "Uzzīmē leņķi un divas paralēlas taisnes, izmēri nogriežņus un "
        "pārbaudi proporciju.",
        "OA = 4 cm, AB = 6 cm, OA_1 = 5 cm. Aprēķini A_1B_1.",
        "Paskaidro, kāpēc teorēmā vajag paralēlas taisnes.",
    ]),
]
