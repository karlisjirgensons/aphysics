# -*- coding: utf-8 -*-
"""9. klase, 34. stunda: «Kā to risinātu eksāmenā?»

Trapeces uzdevumi eksāmena formātā: 1. daļas īsās atbildes (leņķi,
viduslīnija, laukums) un 2. daļas izvērstais uzdevums, kurā jāapvieno
Pitagors, laukums un noformējums.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, restis)

TEMA = "Kā to risinātu eksāmenā?"

MERKIS = ("Risināsim eksāmena formāta uzdevumu par trapeci un noformēsim "
          "risinājumu.")

SATURS = [
    Sakums("Trapece eksāmenā - katru gadu",
           zimejums=restis([["uzdevums", "punkti", "kas jāzina"],
                            ["leņķis", "1", "∠A + ∠D = 180°"],
                            ["viduslīnija", "1", "pamatu vidējais"],
                            ["augstums no S", "2", "S = m · h"],
                            ["2. daļa", "3-5", "Pitagors, līdzība"]]),
           paraksts="Tipiski trapeces uzdevumi un to vērtība.",
           fakti=["1. daļā - īsa atbilde vai izvēle.",
                  "2. daļā - viss risinājums ar pamatojumu.",
                  "Zīmējumā atzīmē doto - tas palīdz arī vērtētājam."]),

    Doma("Noformējuma kārtība",
         "Skice → formula → vērtības → aprēķins → atbilde ar mērvienību.",
         soli=[
             "Uzzīmē un atzīmē: augstumu, pamatus, zināmās malas.",
             "Katram solim: ko aprēķini un ar kuru formulu.",
             "Starprezultātus nenoapaļo, ja nav prasīts.",
             "Atbildi raksti atsevišķā rindā.",
         ]),

    Paraugs("2. daļas uzdevums",
            uzd="Vienādsānu trapecē ABCD pamati AB = 18 cm un CD = 8 cm, "
                "sānu mala 13 cm. Aprēķini trapeces laukumu.",
            soli=[
                ("AH = {18 − 8|2} = 5 (cm)", "DH - augstums, △AHD."),
                ("DH = √(13^2 − 5^2) = √144 = 12 (cm)", "Pitagora teorēma."),
                ("S = {18 + 8|2} · 12 = 156 (cm²)", "Trapeces laukums."),
            ],
            atbilde="156 cm²"),

    Varianti("1. daļa: izvēlies", [
        {"jaut": "Trapecē ∠A = 48°. ∠D, kas pie tās pašas sānu malas, ir",
         "opcijas": ["132°", "48°", "42°", "142°"],
         "pareizi": 0, "padoms": "180° − 48°."},
        {"jaut": "Pamati 7 cm un 13 cm. Viduslīnija ir",
         "opcijas": ["10 cm", "20 cm", "6 cm", "3 cm"],
         "pareizi": 0, "padoms": "20 : 2."},
        {"jaut": "Pamati 6 cm un 10 cm, augstums 5 cm. Laukums ir",
         "opcijas": ["40 cm²", "80 cm²", "30 cm²", "300 cm²"],
         "pareizi": 0, "padoms": "8 · 5."},
    ]),

    Ievadi("Atbilde:", [
        {"jaut": "Trapecē DE ∥ CF, DE = 5 cm, CF = 14 cm, S = 57 cm². "
                 "Augstums (cm)?", "atb": ["6"], "padoms": "9,5 · h = 57."},
        {"jaut": "Vienādsānu trapecē pamati 10 un 4, augstums 4. Sānu mala?",
         "atb": ["5"], "padoms": "AH = 3."},
        {"jaut": "Viduslīnija 9, viens pamats 5. Otrs pamats?",
         "atb": ["13"], "padoms": "18 − 5."},
        {"jaut": "Vienādsānu trapecē ∠A = 55°. ∠C = ?°", "atb": ["125"],
         "padoms": "∠C = ∠D = 180 − 55."},
    ]),

    Pasaule("Rampa ratiņkrēslam",
            Ievadi("", [
                {"jaut": "Rampas sānu siena - taisnleņķa trapece: apakšā 6 m, "
                         "augšā (platforma) 1 m, augstums 0,5 m. Sienas "
                         "laukums (m²)?",
                 "atb": ["1,75"], "padoms": "3,5 · 0,5."},
                {"jaut": "Abām sānu sienām vajag apdari. Cik m²?",
                 "atb": ["3,5"], "padoms": "2 · 1,75."},
            ]),
            pavediens="skola",
            konteksts="Skolas ieejai būvē rampu ar platformu augšā; tās sānu "
                      "siena ir taisnleņķa trapece.",
            kapec="Materiālu daudzums ir trapeces laukums."),

    Kopsavilkums([
        "Risinu 1. daļas trapeces uzdevumus.",
        "Noformēju 2. daļas uzdevumu soli pa solim.",
        "Apvienoju Pitagoru un laukuma formulu.",
    ]),

    Majas([
        "Atkārto 9.2. tematu: veidi, leņķi, viduslīnija, laukums.",
        "Vienādsānu trapecē pamati 25 un 11, sānu mala 25. Aprēķini S.",
        "Uzraksti sev atgādni ar trapeces formulām.",
    ]),
]
