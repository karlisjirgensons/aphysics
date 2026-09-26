# -*- coding: utf-8 -*-
"""3. klase, 6. stunda: «Kas jauns ir reizinājumos ar 7?»

Septiņnieku rinda ir tā, kuru visbiežāk sauc par grūtāko. Patiesībā jaunu
tajā ir maz: gandrīz visus reizinājumus skolēns jau zina no otras puses, un
pāri paliek tikai daži. Stunda to arī parāda - vispirms saskaita, cik īsti
vēl ir jāiemācās.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kas jauns ir reizinājumos ar 7?"

MERKIS = ("Modelēsim reizinājumus ar 7, papildināsim reizināšanas tabulu un "
          "atradīsim, cik maz tajā ir patiešām jauna.")

SATURS = [
    Sakums("Cik septiņnieku reizinājumu tu vēl nezini?",
           zimejums=restis([[7, 14, 21, 28, 35],
                            [42, 49, 56, 63, 70]],
                           "visa septiņnieku rinda"),
           paraksts="Pirmos piecus tu jau proti no 2, 3, 4 un 5 rindām.",
           fakti=["Nedēļā ir 7 dienas, tāpēc septiņnieku rinda ir kalendārs.",
                  "Tiešām jauns tajā ir tikai 7 · 7, 7 · 8 un 7 · 9."]),

    Doma("Septiņnieku rindā jauna ir tikai beigu daļa",
         "2 · 7, 3 · 7, 4 · 7, 5 · 7 un 6 · 7 tu jau zini - tos māca citas "
         "rindas.",
         soli=[
             "Pieraksti septiņnieku rindu: 7, 14, 21, 28, 35, 42, 49, 56, "
             "63, 70.",
             "Apvelc tos, ko jau proti no citām rindām.",
             "Paliek pāri 7 · 7 = 49, 7 · 8 = 56 un 7 · 9 = 63.",
             "Tikai šos trīs vajag iegaumēt no jauna.",
         ],
         pieze="Ja aizmirsti 7 · 8, ej no 7 · 7 = 49 un pieskaiti vēl 7 - "
               "sanāk 56. Viena zināma vieta palīdz kaimiņam."),

    Paraugs("Cik dienu ir 6 nedēļās?",
            uzd="Vienā nedēļā ir 7 dienas. Cik dienu ir 6 nedēļās?",
            soli=[
                ("6 nedēļas, katrā 7 dienas",
                 "Grupas ir nedēļas, grupas lielums - dienas."),
                ("5 · 7 = 35",
                 "Piecas nedēļas - šo proti no piecnieku rindas."),
                ("35 + 7 = 42",
                 "Sestā nedēļa pieliek vēl septiņas dienas."),
            ],
            atbilde="42 dienas"),

    Ievadi("Septiņnieku rinda", [
        {"jaut": "3 · 7 = ?", "atb": ["21"], "padoms": "7, 14, 21."},
        {"jaut": "7 · 7 = ?", "atb": ["49"], "padoms": "42 + 7."},
        {"jaut": "8 · 7 = ?", "atb": ["56"], "padoms": "49 + 7."},
        {"jaut": "9 · 7 = ?", "atb": ["63"], "padoms": "70 − 7."},
        {"jaut": "6 · 7 = ?", "atb": ["42"], "padoms": "35 + 7."},
        {"jaut": "10 · 7 = ?", "atb": ["70"], "padoms": "Septiņi desmiti."},
    ], pamats=4),

    Zimejums("Trīs jaunie reizinājumi",
             restis([["7 · 7", "7 · 8", "7 · 9"],
                     [49, 56, 63]],
                    "šos trīs iegaumē no jauna"),
             paskaidro="Katrs nākamais ir par 7 lielāks nekā iepriekšējais.",
             ievads="Šie ir vienīgie, kurus citas rindas nemāca."),

    Varianti("Vai atbilde ir ticama?", [
        {"jaut": "Cik ir 7 · 8?",
         "opcijas": ["56", "54", "15", "63"],
         "pareizi": 0, "padoms": "49 + 7."},
        {"jaut": "Kurš skaitlis *nav* septiņnieku rindā?",
         "opcijas": ["45", "42", "49", "56"],
         "pareizi": 0, "padoms": "Visi rindas skaitļi dalās ar 7."},
        {"jaut": "Cik nedēļu ir 63 dienās?",
         "opcijas": ["9", "7", "8", "10"],
         "pareizi": 0, "padoms": "63 : 7."},
        {"jaut": "7 · 7 ir par cik lielāks nekā 7 · 6?",
         "opcijas": ["par 7", "par 1", "par 6", "par 13"],
         "pareizi": 0, "padoms": "Pieliek vēl vienu septiņnieku grupu."},
    ], pamats=4),

    Pasaule("Cik dienu ilgst ceļojums?",
            Ievadi("", [
                {"jaut": "Ceļojums ilgst 3 nedēļas. Cik tās ir dienas?",
                 "atb": ["21"], "padoms": "3 · 7."},
                {"jaut": "Cik dienu ir 8 nedēļās?",
                 "atb": ["56"], "padoms": "8 · 7."},
                {"jaut": "Brauciens ilga 49 dienas. Cik tās ir nedēļas?",
                 "atb": ["7"], "padoms": "49 : 7."},
                {"jaut": "Līdz brīvdienām atlikušas 4 nedēļas un vēl 3 "
                         "dienas. Cik dienu tas ir?",
                 "atb": ["31"], "padoms": "4 · 7 = 28; 28 + 3."},
            ]),
            pavediens="celojums",
            konteksts="Ceļojuma garumu parasti saka nedēļās, bet biļetes un "
                      "naktis skaita dienās.",
            kapec="Pārrēķinot nedēļas dienās, uzreiz redz, cik daudz laika "
                  "tiešām ir."),

    Kopsavilkums([
        "Zinu visu septiņnieku rindu no 7 līdz 70.",
        "Zinu, ka jauni tajā ir tikai 7 · 7, 7 · 8 un 7 · 9.",
        "No viena reizinājuma atrodu tā kaimiņu, pieskaitot vai atņemot 7.",
        "Pārrēķinu nedēļas dienās un dienas nedēļās.",
    ]),

    Majas([
        "Paskaties kalendārā: cik dienu ir no šodienas līdz tai pašai "
        "dienai pēc 5 nedēļām?",
        "Pasaki skaļi septiņnieku rindu uz priekšu un atpakaļ.",
        "Uzraksti trīs jaunos reizinājumus uz lapiņas un pielīmē to pie "
        "spoguļa.",
    ]),
]
