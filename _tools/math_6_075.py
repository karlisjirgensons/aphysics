# -*- coding: utf-8 -*-
"""6. klase, 75. stunda: «Kā rēķināt saliktam ķermenim?»

Mikrotemata noslēgums. Salikts ķermenis ir pirmais uzdevums, kurā pašam
jāizlemj, kā to sadalīt - un dalīt var vairākos veidos, visi pareizi. Otrs
ceļš, atņemšana, parāda, ka izvēle ir tikai ērtības jautājums.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā rēķināt saliktam ķermenim?"

MERKIS = ("Iemācīsimies aprēķināt tilpumu ķermenim, ko var sadalīt "
          "taisnstūra paralēlskaldņos.")

SATURS = [
    Sakums("Sadali un saskaiti",
           zimejums=restis([["A", "A", "B"],
                            ["A", "A", "B"]],
                           "divi kvadri vienā ķermenī"),
           paraksts="Salikto ķermeni sadala divās kastēs, katrai rēķina "
                    "tilpumu un saskaita.",
           fakti=["Saliktu ķermeni var sadalīt vairākos veidos.",
                  "Var arī rēķināt lielo kasti un atņemt iztrūkstošo daļu.",
                  "Abi ceļi dod vienu atbildi."]),

    Doma("Divi ceļi: saskaitīt vai atņemt",
         "Salikta ķermeņa tilpumu iegūst, sadalot to kvadros un saskaitot, "
         "vai arī no lielākas kastes atņemot trūkstošo daļu.",
         soli=[
             "Apskati ķermeni un atrodi, kur to sadalīt.",
             "Pieraksti katras daļas trīs izmērus.",
             "Aprēķini katras daļas tilpumu.",
             "Saskaiti tilpumus.",
             "Pārbaudi otrā ceļā: lielā kaste mīnus iztrūkums.",
         ],
         pieze="Izvēlies to sadalījumu, kurā izmērus var nolasīt tieši no "
               "zīmējuma. Ja kāds izmērs jāizrēķina, tas ir vēl viens solis, "
               "kurā var iezagties kļūda."),

    Paraugs("Divi ceļi vienam ķermenim",
            uzd="Ķermenis sastāv no kastes 6 x 4 x 2 cm, uz kuras uzlikta "
                "kaste 2 x 4 x 3 cm. Cik liels ir tilpums?",
            soli=[
                ("Apakšējā daļa: 6 · 4 · 2 = 48 cm³",
                 "Pirmais kvadrs."),
                ("Augšējā daļa: 2 · 4 · 3 = 24 cm³",
                 "Otrais kvadrs."),
                ("48 + 24 = 72 cm³",
                 "Kopējais tilpums."),
                ("Pārbaude: liela kaste 6 x 4 x 5 ir 120 cm³",
                 "No tās trūkst 4 · 4 · 3 = 48 cm³; 120 − 48 = 72."),
            ],
            atbilde="72 cm³"),

    Ievadi("Aprēķini salikto tilpumu", [
        {"jaut": "Daļa A ir 6 x 4 x 2 cm. Cik cm³ ir tās tilpums?",
         "atb": ["48"], "padoms": "24 · 2."},
        {"jaut": "Daļa B ir 2 x 4 x 3 cm. Cik cm³?",
         "atb": ["24"], "padoms": "8 · 3."},
        {"jaut": "Cik cm³ ir abām daļām kopā?",
         "atb": ["72"], "padoms": "48 + 24."},
        {"jaut": "Liela kaste 10 x 5 x 4 cm. Cik cm³ ir tās tilpums?",
         "atb": ["200"], "padoms": "50 · 4."},
        {"jaut": "No tās izgriezts kubs ar šķautni 2 cm. Cik cm³ paliek?",
         "atb": ["192"], "padoms": "200 − 8."},
        {"jaut": "Ķermenis no divām kastēm 5 x 2 x 2 un 3 x 2 x 2. Cik cm³ "
                 "kopā?",
         "atb": ["32"], "padoms": "20 + 12."},
    ], pamats=4),

    Varianti("Kurš ceļš ir ērtāks?", [
        {"jaut": "Ķermenim trūkst viena stūra. Kurš ceļš ir ātrāks?",
         "opcijas": ["Lielā kaste mīnus stūris",
                     "Sadalīt piecās daļās",
                     "Skaitīt kubus pa vienam", "Abi vienlīdz gari"],
         "pareizi": 0,
         "padoms": "Atņemšana te ir viens solis."},
        {"jaut": "Ķermenis ir divas kastes blakus. Kurš ceļš ir ātrāks?",
         "opcijas": ["Saskaitīt abas", "Atņemt no lielākas",
                     "Skaitīt kubus", "Nevar rēķināt"],
         "pareizi": 0,
         "padoms": "Sadalījums ir acīmredzams."},
        {"jaut": "Vai dažādi sadalījumi dod dažādas atbildes?",
         "opcijas": ["Nē, atbilde ir viena", "Jā, vienmēr",
                     "Jā, dažreiz", "Atkarīgs no ķermeņa"],
         "pareizi": 0,
         "padoms": "Tilpums nemainās no tā, kā to rēķina."},
        {"jaut": "Ķermenis 6 x 4 x 5 bez kuba 2 x 2 x 2. Cik cm³?",
         "opcijas": ["112", "120", "8", "128"],
         "pareizi": 0,
         "padoms": "120 − 8."},
    ], pamats=4),

    Pasaule("Cik betona vajag pamatiem?",
            Ievadi("", [
                {"jaut": "Pamats 4 m x 3 m x 0,5 m. Cik m³ betona vajag?",
                 "atb": ["6"], "padoms": "12 · 0,5."},
                {"jaut": "Blakus vēl viens pamats 2 m x 3 m x 0,5 m. Cik m³?",
                 "atb": ["3"], "padoms": "6 · 0,5."},
                {"jaut": "Cik m³ betona vajag abiem kopā?",
                 "atb": ["9"], "padoms": "6 + 3."},
                {"jaut": "Viena kravas mašīna atved 3 m³. Cik reižu tai "
                         "jābrauc?",
                 "atb": ["3"], "padoms": "9 : 3."},
            ]),
            pavediens="maja",
            konteksts="Pamatu forma reti ir vienkārša kaste - to sadala "
                      "daļās un katrai rēķina atsevišķi.",
            kapec="Betonu pasūta kubikmetros, tāpēc kļūda maksā vienu "
                  "kravu."),

    Zimejums("Tas pats ķermenis, cits sadalījums",
             restis([["A", "B", "B"],
                     ["A", "C", "C"]],
                    "trīs daļas vietā divu"),
             paskaidro="Sadalījums cits, bet daļu tilpumu summa ir tā pati.",
             ievads="Sadalīt var vairākos veidos - atbilde nemainās."),

    Kopsavilkums([
        "Sadalu saliktu ķermeni kvadros un saskaitu to tilpumus.",
        "Lietoju arī otro ceļu: lielā kaste mīnus iztrūkums.",
        "Izvēlos to sadalījumu, kurā izmēri ir tieši doti.",
        "Pārbaudu atbildi otrā ceļā.",
    ]),

    Majas([
        "Uzzīmē saliktu ķermeni no divām kastēm un aprēķini tā tilpumu.",
        "Aprēķini to pašu tilpumu otrā ceļā.",
        "Atrodi mājās priekšmetu, kura tilpumu var rēķināt kā divu kastu "
        "summu.",
    ]),
]
