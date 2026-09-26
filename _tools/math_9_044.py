# -*- coding: utf-8 -*-
"""9. klase, 44. stunda: «Kā noteikt vērtību?»

Sinusa, kosinusa un tangensa vērtības dod kalkulators (režīms DEG!) vai
tabula. Svarīgākā kļūda ir režīms RAD - tad sin 30 = −0,988. Stundā
skolēns arī novērtē, vai kalkulatora skaitlis ir ticams.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, restis, taisnlenka)

TEMA = "Kā noteikt vērtību?"

MERKIS = ("Lietosim tabulu vai digitālos rīkus, lai noteiktu sinusa, "
          "kosinusa un tangensa vērtības.")

_TABULA = restis([["α", "sin α", "cos α", "tg α"],
                  ["10°", "0,174", "0,985", "0,176"],
                  ["20°", "0,342", "0,940", "0,364"],
                  ["40°", "0,643", "0,766", "0,839"],
                  ["50°", "0,766", "0,643", "1,192"],
                  ["70°", "0,940", "0,342", "2,747"]])

SATURS = [
    Sakums("sin 30 = −0,988?!",
           zimejums=_TABULA,
           paraksts="Vērtības līdz tūkstošdaļām.",
           fakti=["Kalkulatoram jābūt režīmā DEG (grādi).",
                  "Režīmā RAD sin 30 = −0,988 - tā nav mūsu vērtība.",
                  "Šaura leņķa sin un cos vienmēr ir starp 0 un 1."]),

    Doma("Kā lietot kalkulatoru",
         "Pārbaudi režīmu DEG → nospied sin, cos vai tan → ievadi leņķi → "
         "noapaļo, kā prasīts.",
         soli=[
             "Pārbaude: sin 30° jābūt 0,5.",
             "Starprezultātus neapaļo pārāk agri (vismaz 3 zīmes).",
             "cos α = sin(90° − α) - tabulā redzams: cos 20° = sin 70°.",
             "tg aug ļoti strauji pie 90°: tg 89° ≈ 57.",
         ]),

    Ievadi("Nosaki ar kalkulatoru (līdz tūkstošdaļām)", [
        {"jaut": "sin 25° ≈ ?", "atb": ["0,423"], "padoms": "0,4226..."},
        {"jaut": "cos 25° ≈ ?", "atb": ["0,906"], "padoms": "0,9063..."},
        {"jaut": "tg 25° ≈ ?", "atb": ["0,466"], "padoms": "0,4663..."},
        {"jaut": "sin 64° ≈ ?", "atb": ["0,899"], "padoms": "0,8988..."},
        {"jaut": "tg 60° ≈ ?", "atb": ["1,732"], "padoms": "√3."},
        {"jaut": "cos 80° ≈ ?", "atb": ["0,174"], "padoms": "= sin 10°."},
    ], pamats=4),

    Varianti("Vai ticams?", [
        {"jaut": "Kalkulators: cos 40° = −0,667.",
         "opcijas": ["Nē - režīms RAD", "Jā", "Jā, jo 40 > 30",
                     "Kosinuss vienmēr negatīvs"],
         "pareizi": 0, "padoms": "Šauram leņķim cos > 0."},
        {"jaut": "Kurš lielāks: sin 20° vai sin 70°?",
         "opcijas": ["sin 70°", "sin 20°", "vienādi", "nevar zināt"],
         "pareizi": 0, "padoms": "Sinuss aug."},
        {"jaut": "Kurš lielāks: cos 20° vai cos 70°?",
         "opcijas": ["cos 20°", "cos 70°", "vienādi", "nevar zināt"],
         "pareizi": 0, "padoms": "Kosinuss dilst."},
        {"jaut": "tg 45° = ?",
         "opcijas": ["1", "0,5", "0,707", "√3"],
         "pareizi": 0, "padoms": "Katetes vienādas."},
    ]),

    Petijums("Pārbaudi tabulu ar zīmējumu", [
        "Uzzīmē taisnleņķa trijstūri ar leņķi 40° un hipotenūzu 10 cm.",
        "Izmēri pretkateti un piekateti.",
        "Aprēķini sin 40°, cos 40° un tg 40° no mērījumiem.",
        "Salīdzini ar tabulu. Cik liela ir kļūda?",
    ], vajag="transportieris, lineāls, kalkulators"),

    Pasaule("Saules baterijas slīpums",
            Ievadi("", [
                {"jaut": "Panelis 1,6 m garš, slīpums 40°. Augstums "
                         "(m, līdz simtdaļām)? sin 40° ≈ 0,643",
                 "atb": ["1,03"], "padoms": "1,6 · 0,643 = 1,029."},
                {"jaut": "Cik m zemes tas aizņem horizontāli? cos 40° ≈ 0,766 "
                         "(līdz simtdaļām)", "atb": ["1,23"],
                 "padoms": "1,6 · 0,766 = 1,226."},
            ]),
            pavediens="planeta",
            konteksts="Latvijā saules paneļus liek ap 35-45° leņķī pret "
                      "horizontu, lai pusdienas saule krīt gandrīz taisni.",
            kapec="sin dod augstumu, cos - aizņemto vietu.",
            zimejums=taisnlenka(7.66, 6.43, ("h", "?", "1,6 m"), "40°")),

    Kopsavilkums([
        "Nosaku sin, cos, tg vērtības ar kalkulatoru (DEG).",
        "Lasu vērtības tabulā.",
        "Novērtēju, vai vērtība ir ticama.",
    ]),

    Majas([
        "Aizpildi tabulu leņķiem 15°, 35°, 55°, 75°.",
        "Atrodi pāri, kur sin α = cos β. Kāda ir α + β?",
        "Pārbaudi sava telefona kalkulatoru: kur ir DEG/RAD?",
    ]),
]
