# -*- coding: utf-8 -*-
"""9. klase, 147. stunda: «Kā lietot šīs sakarības?»

Mikrotemata noslēgums: apvilktās riņķa līnijas rādiuss taisnleņķa un
vienādmalu trijstūrim (R = {a√3|3}), leņķis uz diametra un praktiski
uzdevumi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, geometrija, uz_rinka)

TEMA = "Kā lietot šīs sakarības?"

MERKIS = ("Aprēķināsim nezināmos lielumus, lietojot apvilktās riņķa līnijas "
          "īpašības.")

_VIENADMALU = geometrija([uz_rinka("A", 210), uz_rinka("B", 330),
                          uz_rinka("C", 90), ("O", 0, 0, 0),
                          ("H", 0, -2.5, -90)],
                         nogriezni=["AB", "BC", "CA"], izcelti=["OA", "CH"],
                         taisni=["AHC"], rinki=[("O", 5)])

SATURS = [
    Sakums("Vienādmalu trijstūris aplī",
           zimejums=_VIENADMALU,
           paraksts="O dala augstumu CH attiecībā 2 : 1.",
           fakti=["R = {2|3} augstuma.",
                  "Augstums h = {a√3|2}, tātad R = {a√3|3}.",
                  "Mala 6 cm ⇒ R = 2√3 ≈ 3,46 cm."]),

    Doma("Rādiuss dažādiem trijstūriem",
         "Taisnleņķa: R = {c|2}. Vienādmalu: R = {a√3|3}. Citiem - "
         "konstruē vai aprēķina ar līdzību un Pitagoru.",
         soli=[
             "Nosaki trijstūra veidu.",
             "Taisnleņķa - puse hipotenūzas.",
             "Vienādmalu - {2|3} augstuma.",
             "Vienādsānu - centrs uz augstuma pret pamatu.",
         ]),

    Paraugs("Vienādsānu trijstūris",
            uzd="Vienādsānu trijstūra pamats 16 cm, augstums 15 cm. Atrodi R.",
            soli=[
                ("Centrs uz augstuma: OB = R, OH = 15 − R", "Skice."),
                ("R^2 = 8^2 + (15 − R)^2", "Pitagors △OHB."),
                ("R^2 = 64 + 225 − 30R + R^2 ⇒ 30R = 289", "Vienkāršo."),
                ("R = {289|30} ≈ 9,6 cm", "Aprēķins."),
            ],
            atbilde="≈ 9,6 cm"),

    Ievadi("Aprēķini", [
        {"jaut": "Taisnleņķa trijstūra katetes 7 un 24. R = ?", "atb": ["12,5"],
         "padoms": "c = 25."},
        {"jaut": "Vienādmalu trijstūra augstums 9. R = ?", "atb": ["6"],
         "padoms": "{2|3} · 9."},
        {"jaut": "R = 10; taisnleņķa trijstūra viena katete 12. Otra?",
         "atb": ["16"], "padoms": "c = 20."},
        {"jaut": "Kvadrāta mala 4 cm. Apvilktās riņķa līnijas R = 2√?",
         "atb": ["2"], "padoms": "Diagonāle 4√2."},
    ]),

    Varianti("Izvēlies", [
        {"jaut": "Taisnstūrim ar malām 6 un 8 apvilktās R = ?",
         "opcijas": ["5", "7", "10", "14"],
         "pareizi": 0, "padoms": "Puse diagonāles."},
        {"jaut": "Kurš apgalvojums patiess?",
         "opcijas": ["Ap katru trijstūri var apvilkt riņķa līniju",
                     "Ap katru četrstūri var apvilkt",
                     "Centrs vienmēr iekšā", "R vienmēr = mala"],
         "pareizi": 0, "padoms": "Trīs punkti - viena riņķa līnija."},
    ]),

    Pasaule("Apaļa galda virsma",
            Ievadi("", [
                {"jaut": "Uz apaļa galda jānoliek trijstūra paplāte ar malām "
                         "30, 40, 50 cm, visas virsotnes uz malas. Galda "
                         "diametrs (cm)?", "atb": ["50"],
                 "padoms": "30^2 + 40^2 = 50^2 - taisnleņķa."},
            ]),
            pavediens="maja",
            konteksts="Mēbeļu dizainers pielāgo galda izmēru, lai paplāte "
                      "pieskartos malām.",
            kapec="Taisnleņķa trijstūrim diametrs ir hipotenūza."),

    Kopsavilkums([
        "Aprēķinu R taisnleņķa un vienādmalu trijstūrim.",
        "Lietoju Pitagoru vienādsānu trijstūrim.",
        "Atrodu apvilkto riņķa līniju taisnstūrim.",
    ]),

    Majas([
        "Vienādmalu trijstūra mala 12. Atrodi R.",
        "Vienādsānu trijstūra pamats 10, sānu mala 13. Atrodi R.",
        "Izmēri apaļu šķīvi un iedomāto ievilkto trijstūri.",
    ]),
]
