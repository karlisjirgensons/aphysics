# -*- coding: utf-8 -*-
"""9. klase, 51. stunda: «Kā aprēķināt nezināmo malu?»

Viens algoritms: kura mala zināma, kura jāatrod, kādā attiecībā pret leņķi
tās stāv - tas izvēlas sin, cos vai tg. Pēc tam viena reizināšana vai
dalīšana. Skolēns izvēlas sakarību, pirms rēķina.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, restis, taisnlenka)

TEMA = "Kā aprēķināt nezināmo malu?"

MERKIS = ("Aprēķināsim taisnleņķa trijstūra malas, ja dots šaurais leņķis un "
          "viena mala.")

SATURS = [
    Sakums("Kurš no trim - sin, cos vai tg?",
           zimejums=restis([["zināms", "meklē", "lieto"],
                            ["hipotenūza", "pretkatete", "sin"],
                            ["hipotenūza", "piekatete", "cos"],
                            ["piekatete", "pretkatete", "tg"]]),
           paraksts="Izvēli nosaka divas malas: zināmā un meklējamā.",
           fakti=["Neizmanto Pitagoru, ja zināma tikai viena mala.",
                  "Parasti reizina, ja meklē kateti; dala, ja meklē hipotenūzu.",
                  "Leņķis vienmēr «skatās» no savas virsotnes."]),

    Doma("Algoritms",
         "Nosauc malas attiecībā pret leņķi → izvēlies sakarību → atrisini "
         "vienādojumu.",
         soli=[
             "Atzīmē: zināmā mala, meklējamā mala, leņķis.",
             "Pretkatete / piekatete / hipotenūza - pret DOTO leņķi.",
             "Pieraksti, piem., sin 35° = {x|12}.",
             "x = 12 · sin 35° ≈ 12 · 0,574 ≈ 6,88.",
         ]),

    Slidnis("Trīs situācijas", [
        {"v": "sin", "teksts": "c = 12, α = 35°: a = 12 · sin 35° ≈ 6,88",
         "zim": taisnlenka(9.83, 6.88, ("a = ?", None, "12"), "35°")},
        {"v": "cos", "teksts": "c = 12, α = 35°: b = 12 · cos 35° ≈ 9,83",
         "zim": taisnlenka(9.83, 6.88, (None, "b = ?", "12"), "35°")},
        {"v": "tg", "teksts": "b = 10, α = 35°: a = 10 · tg 35° ≈ 7,00",
         "zim": taisnlenka(10, 7, ("a = ?", "10", None), "35°")},
    ]),

    Paraugs("Meklē hipotenūzu",
            uzd="Pretkatete 5 cm, α = 20°. Atrodi hipotenūzu.",
            soli=[
                ("sin 20° = {5|c}", "Pretkatete un hipotenūza."),
                ("c = {5|sin 20°} ≈ {5|0,342}", "Dala!"),
                ("c ≈ 14,6 cm", "Pārbaude: c > 5."),
            ],
            atbilde="≈ 14,6 cm"),

    Ievadi("Aprēķini (līdz desmitdaļām)", [
        {"jaut": "c = 20, α = 40° (sin 40° ≈ 0,643). Pretkatete?",
         "atb": ["12,9"], "padoms": "20 · 0,643 = 12,86."},
        {"jaut": "c = 15, α = 60°. Piekatete?", "atb": ["7,5"],
         "padoms": "cos 60° = 0,5."},
        {"jaut": "Piekatete 8, α = 50° (tg 50° ≈ 1,192). Pretkatete?",
         "atb": ["9,5"], "padoms": "8 · 1,192 = 9,54."},
        {"jaut": "Piekatete 6, α = 30° (cos 30° ≈ 0,866). Hipotenūza?",
         "atb": ["6,9"], "padoms": "6 : 0,866 = 6,93."},
        {"jaut": "Pretkatete 9, α = 25° (tg 25° ≈ 0,466). Piekatete?",
         "atb": ["19,3"], "padoms": "9 : 0,466 = 19,31."},
        {"jaut": "c = 50, α = 12° (sin 12° ≈ 0,208). Pretkatete?",
         "atb": ["10,4"], "padoms": "50 · 0,208."},
    ], pamats=4),

    Varianti("Kura formula?", [
        {"jaut": "Zināma hipotenūza c un α. Piekatete b = ?",
         "opcijas": ["c · cos α", "c · sin α", "c : cos α", "c · tg α"],
         "pareizi": 0, "padoms": "cos α = {b|c}."},
        {"jaut": "Zināma pretkatete a un α. Hipotenūza c = ?",
         "opcijas": ["{a|sin α}", "a · sin α", "{a|cos α}", "a · tg α"],
         "pareizi": 0, "padoms": "sin α = {a|c}."},
        {"jaut": "Zināma piekatete b un α. Pretkatete a = ?",
         "opcijas": ["b · tg α", "{b|tg α}", "b · sin α", "b · cos α"],
         "pareizi": 0, "padoms": "tg α = {a|b}."},
    ]),

    Pasaule("Pūķa aukla",
            Ievadi("", [
                {"jaut": "Aukla 60 m, leņķis ar zemi 50° (sin 50° ≈ 0,766). "
                         "Cik m augstu ir pūķis (līdz veseliem)?",
                 "atb": ["46"], "padoms": "60 · 0,766 = 45,96."},
                {"jaut": "Cik m tālu (horizontāli) tas ir? cos 50° ≈ 0,643 "
                         "(līdz veseliem)", "atb": ["39"],
                 "padoms": "60 · 0,643 = 38,58."},
            ]),
            pavediens="daba",
            konteksts="Pūķa auklas garumu un leņķi var izmērīt uz zemes; "
                      "augstumu - tikai aprēķināt.",
            kapec="sin dod augstumu, cos - attālumu."),

    Kopsavilkums([
        "Izvēlos sin, cos vai tg pēc zināmās un meklējamās malas.",
        "Aprēķinu kateti (reizinot) vai hipotenūzu (dalot).",
        "Pārbaudu: katete < hipotenūza.",
    ]),

    Majas([
        "c = 30, α = 28°. Atrodi abas katetes.",
        "Pārbaudi atbildi ar Pitagora teorēmu.",
        "Izmēri auklas garumu un leņķi pūķim vai karogam.",
    ]),
]
