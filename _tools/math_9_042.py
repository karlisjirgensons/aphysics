# -*- coding: utf-8 -*-
"""9. klase, 42. stunda: «Kas ir sinuss?»

Pirmā attiecība iegūst vārdu: sin α = {pretkatete|hipotenūza}. Stunda sākas
ar lidmašīnas pacelšanos - ja zina skrejceļa leņķi un nolidoto ceļu,
augstumu dod sinuss.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, taisnlenka)

TEMA = "Kas ir sinuss?"

MERKIS = "Definēsim šaurā leņķa sinusu un pierakstīsim to zīmējumā."

SATURS = [
    Sakums("Cik augstu ir lidmašīna pēc 1 km?",
           zimejums=taisnlenka(10, 2.2, ("h", None, "1000 m"), "12°"),
           paraksts="Pacelšanās leņķis 12°: h = 1000 · sin 12° ≈ 208 m.",
           fakti=["sin α = pretkatete : hipotenūza.",
                  "sin 12° ≈ 0,208 - tas ir vienmēr, jebkurai lidmašīnai.",
                  "Sinuss ir skaitlis starp 0 un 1."]),

    Doma("Sinuss",
         "Taisnleņķa trijstūra šaurā leņķa sinuss ir pretkatetes attiecība "
         "pret hipotenūzu: sin α = {a|c}.",
         soli=[
             "Atrodi leņķi un hipotenūzu.",
             "Atrodi pretkateti - malu pretī leņķim.",
             "Dali: pretkatete : hipotenūza.",
             "No sin α = {a|c} izriet a = c · sin α.",
         ]),

    Slidnis("Leņķis aug - sinuss aug", [
        {"v": "α ≈ 17°", "teksts": "sin α = 3 : 10 = 0,3",
         "zim": taisnlenka(9.54, 3, ("3", None, "10"), "α")},
        {"v": "α = 30°", "teksts": "sin α = 5 : 10 = 0,5",
         "zim": taisnlenka(8.66, 5, ("5", None, "10"), "α")},
        {"v": "α ≈ 53°", "teksts": "sin α = 8 : 10 = 0,8",
         "zim": taisnlenka(6, 8, ("8", None, "10"), "α")},
    ], ievads="Hipotenūza paliek 10. Kas notiek ar pretkateti?"),

    Paraugs("Atrodi sinusu",
            uzd="△ABC, ∠C = 90°, BC = 7, AB = 25. Atrodi sin A un sin B.",
            soli=[
                ("sin A = {BC|AB} = {7|25} = 0,28", "Pretī A ir BC."),
                ("AC = √(625 − 49) = √576 = 24", "Pitagora teorēma."),
                ("sin B = {AC|AB} = {24|25} = 0,96", "Pretī B ir AC."),
            ],
            atbilde="sin A = 0,28; sin B = 0,96"),

    Ievadi("Aprēķini sinusu", [
        {"jaut": "Pretkatete 3, hipotenūza 5. sin α = ?", "atb": ["0,6"],
         "padoms": "3 : 5."},
        {"jaut": "Pretkatete 12, hipotenūza 13. sin α ≈ ? (līdz simtdaļām)",
         "atb": ["0,92"], "padoms": "12 : 13 ≈ 0,923."},
        {"jaut": "Katetes 6 un 8. Mazākā leņķa sinuss?", "atb": ["0,6"],
         "padoms": "Hipotenūza 10; pretī mazākajam - 6."},
        {"jaut": "sin α = 0,4, hipotenūza 15. Pretkatete?", "atb": ["6"],
         "padoms": "15 · 0,4."},
        {"jaut": "sin α = 0,75, pretkatete 9. Hipotenūza?", "atb": ["12"],
         "padoms": "9 : 0,75."},
        {"jaut": "Katetes 8 un 15. Lielākā leņķa sinuss? (daļa)",
         "atb": ["{15|17}", "15/17"], "tastatura": "text",
         "padoms": "Hipotenūza 17."},
    ], pamats=4),

    Varianti("Vai tā var būt?", [
        {"jaut": "sin α = 1,2",
         "opcijas": ["Nē - pretkatete nav garāka par hipotenūzu", "Jā",
                     "Jā, ja α > 45°", "Tikai platleņķim"],
         "pareizi": 0, "padoms": "Katete < hipotenūza."},
        {"jaut": "Ja α palielinās (šaurs), sin α...",
         "opcijas": ["palielinās", "samazinās", "nemainās", "kļūst negatīvs"],
         "pareizi": 0, "padoms": "Slīdnis."},
        {"jaut": "sin α = {BC|AB} (∠C = 90°). α ir leņķis...",
         "opcijas": ["A", "B", "C", "jebkurš"],
         "pareizi": 0, "padoms": "BC ir pretī A."},
    ]),

    Pasaule("Lidmašīnas pacelšanās",
            Ievadi("", [
                {"jaut": "Lidmašīna lido 2000 m pa taisni 10° leņķī. "
                         "sin 10° ≈ 0,174. Augstums (m)?", "atb": ["348"],
                 "padoms": "2000 · 0,174."},
                {"jaut": "Cik m jānolido, lai sasniegtu 870 m (sin 10° ≈ "
                         "0,174)?", "atb": ["5000"], "padoms": "870 : 0,174."},
            ]),
            pavediens="tehnika",
            konteksts="Pilots zina pacelšanās leņķi un ātrumu; augstumu "
                      "aprēķina ar sinusu.",
            kapec="Sinuss pārvērš slīpo ceļu augstumā."),

    Kopsavilkums([
        "Definēju sinusu: pretkatete : hipotenūza.",
        "Aprēķinu sinusu no malām.",
        "No sinusa un hipotenūzas atrodu pretkateti.",
    ]),

    Majas([
        "Trijstūrī 9, 40, 41 aprēķini abu šauro leņķu sinusus.",
        "Paskaidro, kāpēc sin α < 1.",
        "Uzzīmē trijstūri, kurā sin α = 0,5, un izmēri α.",
    ]),
]
