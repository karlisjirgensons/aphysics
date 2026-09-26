# -*- coding: utf-8 -*-
"""9. klase, 50. stunda: «Kā pārbaudīt rezultātu?»

Trīs pārbaudes, kas aizņem pusminūti: hipotenūza ir garākā mala, lielākā
leņķa pretī ir lielākā mala, un Pitagors apstiprina malas, kas iegūtas ar
trigonometriju. Skolēns meklē kļūdainus rezultātus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, taisnlenka)

TEMA = "Kā pārbaudīt rezultātu?"

MERKIS = ("Pārbaudīsim aprēķinu ar Pitagora teorēmu vai novērtējumu.")

SATURS = [
    Sakums("Katete 13 cm, hipotenūza 12 cm?",
           zimejums=taisnlenka(4, 3, ("13?", "5", "12"), "α"),
           paraksts="Kaut kas nav kārtībā.",
           fakti=["Hipotenūza vienmēr ir garākā mala.",
                  "Pretī lielākajam leņķim - lielākā mala.",
                  "Pitagors: a^2 + b^2 = c^2 - ātra pārbaude."]),

    Doma("Trīs ātras pārbaudes",
         "Pirms atbildi pieraksti, pārbaudi: garumu secība, Pitagors, "
         "novērtējums.",
         soli=[
             "Katete < hipotenūza; sin un cos < 1.",
             "Leņķis 30° → pretkatete ir mazākā; 60° → lielākā katete.",
             "Iegūtās malas ievieto a^2 + b^2 = c^2.",
             "Novērtē: sin 40° ≈ 0,64, tātad pretkatete ≈ {2|3} hipotenūzas.",
         ]),

    Paraugs("Pārbaude ar Pitagoru",
            uzd="Hipotenūza 10, α = 37°. Aprēķinātās katetes: a = 6,02, "
                "b = 7,99. Pārbaudi.",
            soli=[
                ("6,02^2 + 7,99^2 ≈ 36,2 + 63,8 = 100,0", "Kvadrātu summa."),
                ("10^2 = 100", "Hipotenūzas kvadrāts."),
                ("Sakrīt - aprēķins pareizs", "Noapaļošanas robežās."),
            ],
            atbilde="rezultāts ir ticams"),

    Varianti("Atrodi kļūdu", [
        {"jaut": "Hipotenūza 10, α = 30°. Skolēns: pretkatete 8,66.",
         "opcijas": ["Sajauca sin ar cos - jābūt 5", "Pareizi",
                     "Jābūt 20", "Jābūt 10"],
         "pareizi": 0, "padoms": "Pretī 30° - puse."},
        {"jaut": "Hipotenūza 5, α = 50°. Skolēns: pretkatete 6,0.",
         "opcijas": ["Katete garāka par hipotenūzu - kļūda",
                     "Pareizi", "Jānoapaļo", "Jābūt 60"],
         "pareizi": 0, "padoms": "Katete < 5."},
        {"jaut": "Katetes 3 un 4. Skolēns: mazākais leņķis 53°.",
         "opcijas": ["Tas ir lielākais; mazākais ≈ 37°", "Pareizi",
                     "Leņķis 45°", "Leņķis 90°"],
         "pareizi": 0, "padoms": "Pretī 3 ir mazākais leņķis."},
        {"jaut": "Kalkulatorā: sin 30° = −0,988.",
         "opcijas": ["Režīms RAD - pārslēdz uz DEG", "Pareizi",
                     "Sinuss var būt negatīvs", "Jānoapaļo"],
         "pareizi": 0, "padoms": "sin 30° = 0,5."},
    ]),

    Ievadi("Pārbaudi un atbildi", [
        {"jaut": "Katetes 9 un 12. Hipotenūza?", "atb": ["15"],
         "padoms": "81 + 144 = 225."},
        {"jaut": "Hipotenūza 26, katete 10. Otra katete?", "atb": ["24"],
         "padoms": "676 − 100 = 576."},
        {"jaut": "Hipotenūza 10, α = 53°, sin 53° ≈ 0,8. Pretkatete?",
         "atb": ["8"], "padoms": "10 · 0,8."},
        {"jaut": "Tajā pašā trijstūrī piekatete (Pitagors)?", "atb": ["6"],
         "padoms": "√(100 − 64)."},
    ]),

    Pasaule("Antenas troses",
            Ievadi("", [
                {"jaut": "Antena 12 m augsta, trose piestiprināta galā un "
                         "zemē 5 m no pamata. Troses garums (m)?",
                 "atb": ["13"], "padoms": "√(144 + 25)."},
                {"jaut": "Leņķis starp trosi un zemi līdz grādiem? tg α = 2,4",
                 "atb": ["67"], "padoms": "SHIFT tan 2,4 → 67,4°."},
                {"jaut": "Pārbaude: 13 · sin 67,4° ≈ ? (līdz veseliem)",
                 "atb": ["12"], "padoms": "Jāiegūst antenas augstums."},
            ]),
            pavediens="tehnika",
            konteksts="Mobilo sakaru antenas masts tiek nostiprināts ar "
                      "trosēm pie zemes.",
            kapec="Divi ceļi uz vienu skaitli - pārbaude ir ieslēgta."),

    Kopsavilkums([
        "Pārbaudu malu secību un sin, cos < 1.",
        "Pārbaudu malas ar Pitagora teorēmu.",
        "Pamanu kļūdas režīmā un sakarību sajaukšanā.",
    ]),

    Majas([
        "Atrisini divus uzdevumus no iepriekšējām stundām un pārbaudi ar "
        "Pitagoru.",
        "Uzraksti sev «pārbaudes sarakstu» trīs punktos.",
        "Izveido uzdevumu ar apzinātu kļūdu draugam.",
    ]),
]
