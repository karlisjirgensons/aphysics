# -*- coding: utf-8 -*-
"""9. klase, 55. stunda: «Kā aprēķināt laukumu ar leņķi?»

Ja augstums nav dots, to dod sinuss: h = b · sin α. No tā trijstūra
laukums S = {1|2}ab · sin γ un paralelograma S = ab · sin α. Mērnieks tā
aprēķina zemes gabalu, izmērot tikai divas malas un leņķi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, geometrija)

TEMA = "Kā aprēķināt laukumu ar leņķi?"

MERKIS = ("Aprēķināsim figūras laukumu, izmantojot trigonometriskās "
          "sakarības.")

_TRIJSTURIS = geometrija([("A", 0, 0), ("B", 10, 0), ("C", 5, 4.2),
                          ("H", 5, 0, -90)],
                         nogriezni=["AB", "BC", "CA"], izcelti=["CH"],
                         taisni=["AHC"], lenki=[("BAC", "α")],
                         malas=[("AB", "c"), ("AC", "b"), ("CH", "h")])

_PARALELOGRAMS = geometrija([("A", 0, 0), ("B", 8, 0), ("C", 11, 4),
                             ("D", 3, 4), ("H", 3, 0, -90)],
                            nogriezni=["AB", "BC", "CD", "DA"],
                            izcelti=["DH"], taisni=["AHD"],
                            lenki=[("BAD", "α")],
                            malas=[("AB", "a"), ("AD", "b")])

SATURS = [
    Sakums("Augstuma nav - vai laukumu var atrast?",
           zimejums=_TRIJSTURIS,
           paraksts="h = b · sin α - augstumu dod sinuss.",
           fakti=["S = {1|2} · c · h = {1|2} · c · b · sin α.",
                  "Vajag divas malas un leņķi starp tām.",
                  "Tā mērnieki rēķina zemes gabalus."]),

    Slidnis("No augstuma uz formulu", [
        {"v": "1", "teksts": "Trijstūrī AHC: sin α = {h|b}",
         "zim": _TRIJSTURIS},
        {"v": "2", "teksts": "h = b · sin α", "zim": _TRIJSTURIS},
        {"v": "3", "teksts": "S = {1|2} · c · h = {1|2} · b · c · sin α",
         "zim": _TRIJSTURIS},
        {"v": "Paralelograms", "teksts": "S = a · h = a · b · sin α",
         "zim": _PARALELOGRAMS},
    ]),

    Doma("Laukums ar leņķi",
         "Trijstūrim S = {1|2}ab · sin γ, paralelogramam S = ab · sin α, kur "
         "leņķis ir starp malām a un b.",
         soli=[
             "Pārbaudi, vai leņķis ir STARP dotajām malām.",
             "Aprēķini sinusu (kalkulators vai īpašais leņķis).",
             "Reizini; trijstūrim - puse.",
         ],
         pieze="Ar 90° leņķi sin 90° = 1, un formula kļūst par parasto "
               "{1|2}ab."),

    Paraugs("Trijstūris ar 30°",
            uzd="Trijstūra malas 8 cm un 11 cm, leņķis starp tām 30°. Atrodi "
                "laukumu.",
            soli=[
                ("S = {1|2} · 8 · 11 · sin 30°", "Formula."),
                ("= {1|2} · 8 · 11 · {1|2} = 22", "sin 30° = {1|2}."),
            ],
            atbilde="22 cm²"),

    Ievadi("Aprēķini laukumu", [
        {"jaut": "Trijstūris: 6, 10, leņķis 30°. S = ?", "atb": ["15"],
         "padoms": "{1|2} · 60 · {1|2}."},
        {"jaut": "Paralelograms: 5, 8, leņķis 30°. S = ?", "atb": ["20"],
         "padoms": "40 · {1|2}."},
        {"jaut": "Rombs: mala 6, leņķis 30°. S = ?", "atb": ["18"],
         "padoms": "36 · {1|2}."},
        {"jaut": "Trijstūris: 12, 7, leņķis 90°. S = ?", "atb": ["42"],
         "padoms": "sin 90° = 1."},
        {"jaut": "Trijstūris: 10, 10, leņķis 50° (sin 50° ≈ 0,766). "
                 "S ≈ ? (līdz desmitdaļām)", "atb": ["38,3"],
         "padoms": "50 · 0,766."},
    ], pamats=3),

    Varianti("Pareizi vai nē?", [
        {"jaut": "Malas 5 un 7, leņķis 40° NAV starp tām. S = {1|2} · 5 · 7 · "
                 "sin 40°?",
         "opcijas": ["Nē - leņķim jābūt starp malām", "Jā", "Jā, bez {1|2}",
                     "Tikai platleņķim"],
         "pareizi": 0, "padoms": "Formulas nosacījums."},
        {"jaut": "Kurš leņķis dod lielāko laukumu (malas nemainās)?",
         "opcijas": ["90°", "30°", "60°", "150°"],
         "pareizi": 0, "padoms": "sin 90° = 1 - lielākais."},
    ]),

    Pasaule("Zemes gabals",
            Ievadi("", [
                {"jaut": "Trijstūra gabals: divas robežas 40 m un 50 m, leņķis "
                         "starp tām 60° (sin 60° ≈ 0,866). Laukums (m², līdz "
                         "veseliem)?", "atb": ["866"],
                 "padoms": "{1|2} · 2000 · 0,866."},
                {"jaut": "1 m² maksā 12 €. Cena (€, līdz veseliem)?",
                 "atb": ["10392", "10 392"], "padoms": "866 · 12."},
            ]),
            pavediens="maja",
            konteksts="Mērnieks gabalā izmēra divas robežas un leņķi starp "
                      "tām - pārējo aprēķina.",
            kapec="Laukums bez augstuma mērīšanas."),

    Kopsavilkums([
        "Izsaku augstumu ar sinusu.",
        "Lietoju S = {1|2}ab · sin γ.",
        "Aprēķinu paralelograma un romba laukumu ar leņķi.",
    ]),

    Majas([
        "Trijstūra malas 9 cm un 14 cm, leņķis 45°. Atrodi laukumu.",
        "Paralelograma malas 7 un 10, laukums 35. Kāds leņķis?",
        "Pārbaudi formulu uz rūtiņu lapas uzzīmētam trijstūrim.",
    ]),
]
