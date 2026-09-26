# -*- coding: utf-8 -*-
"""9. klase, 56. stunda: «Kā to risinātu eksāmenā?»

Trigonometrija eksāmena formātā: 1. daļā - katete pret 30° un vērtību
izvēle, 2. daļā - uzdevums, kurā jāplāno soļi (figūra → taisnleņķa
trijstūris → sakarība → atbilde). Formulu lapā trigonometrijas nav.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, restis, taisnlenka)

TEMA = "Kā to risinātu eksāmenā?"

MERKIS = ("Plānosim risinājuma soļus un risināsim eksāmena formāta "
          "uzdevumu.")

SATURS = [
    Sakums("Ko jāatceras bez formulu lapas",
           zimejums=restis([["sakarība", "formula"],
                            ["sin α", "pretkatete : hipotenūza"],
                            ["cos α", "piekatete : hipotenūza"],
                            ["tg α", "pretkatete : piekatete"]]),
           paraksts="Plus īpašo leņķu tabula (48. stunda).",
           fakti=["Formulu lapā ir Pitagors, bet nav sin, cos, tg.",
                  "Kalkulators atļauts tikai 2. daļā.",
                  "1. daļā - īpašie leņķi un katete pret 30°."]),

    Doma("Plāns 2. daļas uzdevumam",
         "Skice → taisnleņķa trijstūris → sakarība → aprēķins → pārbaude.",
         soli=[
             "Uzzīmē un atzīmē visus dotos lielumus.",
             "Iekrāso taisnleņķa trijstūri, kurā strādāsi.",
             "Pieraksti sakarību vārdos un ar skaitļiem.",
             "Starprezultātus apaļo tikai, ja prasīts.",
             "Pārbaudi ar Pitagoru vai novērtējumu.",
         ]),

    Paraugs("2. daļas uzdevums",
            uzd="No 1,6 m augstuma skolēns redz torņa galotni 35° leņķī pret "
                "horizontu. Līdz tornim 40 m. Aprēķini torņa augstumu "
                "(līdz metriem).",
            soli=[
                ("tg 35° = {x|40}", "x - torņa daļa virs acu līmeņa."),
                ("x = 40 · tg 35° ≈ 40 · 0,700 = 28,0 (m)", "Aprēķins."),
                ("h = 28,0 + 1,6 = 29,6 ≈ 30 (m)", "Pieskaita acu augstumu!"),
            ],
            atbilde="≈ 30 m"),

    Varianti("1. daļa", [
        {"jaut": "△RKN, ∠K = 90°, ∠N = 30°, RN = 14 cm. RK = ?",
         "opcijas": ["7 cm", "14 cm", "7√3 cm", "28 cm"],
         "pareizi": 0, "padoms": "Katete pret 30°."},
        {"jaut": "sin 60° = ?",
         "opcijas": ["{√3|2}", "{1|2}", "√3", "{√2|2}"],
         "pareizi": 0, "padoms": "Tabula."},
        {"jaut": "tg α = 1. α = ?",
         "opcijas": ["45°", "30°", "60°", "90°"],
         "pareizi": 0, "padoms": "Katetes vienādas."},
        {"jaut": "Kurš apgalvojums ir patiess šauram leņķim?",
         "opcijas": ["sin α < 1", "tg α < 1", "cos α > 1", "sin α > cos α"],
         "pareizi": 0, "padoms": "Katete < hipotenūza."},
    ]),

    Ievadi("Atbilde:", [
        {"jaut": "△ABC, ∠C = 90°, AB = 10, ∠A = 30°. BC = ?", "atb": ["5"],
         "padoms": "Puse."},
        {"jaut": "Tajā pašā trijstūrī AC = 5√?", "atb": ["3"],
         "padoms": "10 · cos 30° = 5√3."},
        {"jaut": "Katetes 9 un 12. cos lielākajam leņķim? (decimāldaļa)",
         "atb": ["0,6"], "padoms": "Piekatete 9, hipotenūza 15."},
        {"jaut": "Kāpnes 5 m, leņķis ar zemi 60°. Attālums no sienas (m)?",
         "atb": ["2,5"], "padoms": "5 · cos 60°."},
    ]),

    Pasaule("Bāka jūrā",
            Ievadi("", [
                {"jaut": "No 30 m augstas bākas kuģi redz 6° leņķī zem "
                         "horizonta (tg 6° ≈ 0,105). Attālums līdz kuģim "
                         "(m, līdz veseliem)?", "atb": ["286"],
                 "padoms": "30 : 0,105 = 285,7."},
                {"jaut": "Pēc brīža leņķis 10° (tg 10° ≈ 0,176). Attālums (m, "
                         "līdz veseliem)?", "atb": ["170"],
                 "padoms": "30 : 0,176 = 170,5."},
                {"jaut": "Cik m kuģis pietuvojās?", "atb": ["116"],
                 "padoms": "286 − 170."},
            ]),
            pavediens="celojums",
            konteksts="Bākas uzraugs attālumu līdz kuģim nosaka pēc leņķa un "
                      "bākas augstuma.",
            kapec="Divi mērījumi - un zināms kuģa ceļš.",
            zimejums=taisnlenka(8, 1.5, ("30 m", "?", None), "6°")),

    Kopsavilkums([
        "Plānoju trigonometrijas uzdevuma risinājumu.",
        "Risinu 1. daļas uzdevumus bez kalkulatora.",
        "Nepiemirstu pieskaitīt acu augstumu u. c. papildu garumus.",
    ]),

    Majas([
        "Atkārto 9.3. tematu - nākamajā stundā pārbaudes darbs.",
        "Vienādsānu trijstūra sānu mala 12 cm, pamata leņķis 30°. Atrodi "
        "laukumu.",
        "Izmēri kāda koka augstumu ar leņķi (telefona lietotne «līmeņrādis»).",
    ]),
]
