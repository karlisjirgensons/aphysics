# -*- coding: utf-8 -*-
"""9. klase, 45. stunda: «Kā no vērtības atrast leņķi?»

Pretējais jautājums: zināma attiecība, jāatrod leņķis. Kalkulatorā tās ir
pogas SHIFT + sin (sin⁻¹), un tabulā meklē tuvāko vērtību. Skolēns
aprēķina leņķi no divām izmērītām malām.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, taisnlenka)

TEMA = "Kā no vērtības atrast leņķi?"

MERKIS = ("Noteiksim leņķa lielumu, ja zināma trigonometriskās sakarības "
          "vērtība.")

SATURS = [
    Sakums("Cik stāvs ir šis kalniņš?",
           zimejums=taisnlenka(8, 3, ("30 m", "80 m", None), "α = ?"),
           paraksts="tg α = 30 : 80 = 0,375 → α ≈ 20,6°.",
           fakti=["Zināmas malas - zināma attiecība.",
                  "Kalkulatorā SHIFT + tan dod leņķi.",
                  "Tā mēra slīpumu bez transportiera."]),

    Doma("No attiecības uz leņķi",
         "Ja sin α = 0,5, tad α = 30°: kalkulatorā SHIFT sin 0,5 =.",
         soli=[
             "Izvēlies sakarību pēc zināmajām malām.",
             "Aprēķini attiecību (skaitli).",
             "SHIFT + sin / cos / tan (vai sin⁻¹).",
             "Noapaļo leņķi, kā prasīts (parasti līdz grādiem).",
         ],
         pieze="Zināmas abas katetes → tg; katete un hipotenūza → sin vai "
               "cos."),

    Paraugs("Leņķis no malām",
            uzd="Kāpnes 5 m garas, to apakšgals 1,5 m no sienas. Kādu leņķi "
                "kāpnes veido ar zemi?",
            soli=[
                ("cos α = {1,5|5} = 0,3", "Piekatete : hipotenūza."),
                ("α = cos⁻¹ 0,3 ≈ 72,5°", "SHIFT cos."),
                ("72,5° < 75° - mazliet par lēzenu", "Ieteicams ap 75°."),
            ],
            atbilde="≈ 73°"),

    Ievadi("Atrodi leņķi (līdz grādiem)", [
        {"jaut": "sin α = 0,5. α = ?°", "atb": ["30"], "padoms": "SHIFT sin."},
        {"jaut": "tg α = 1. α = ?°", "atb": ["45"], "padoms": "Katetes vienādas."},
        {"jaut": "cos α = 0,8. α ≈ ?°", "atb": ["37"],
         "padoms": "36,87°."},
        {"jaut": "Katetes 5 un 12. Leņķis pretī 5 ≈ ?°", "atb": ["23"],
         "padoms": "tg α = 5 : 12 → 22,6°."},
        {"jaut": "Pretkatete 4, hipotenūza 9. α ≈ ?°", "atb": ["26"],
         "padoms": "sin α = 0,444 → 26,4°."},
        {"jaut": "tg α = 2. α ≈ ?°", "atb": ["63"], "padoms": "63,4°."},
    ], pamats=4),

    Varianti("Kuru sakarību lietot?", [
        {"jaut": "Zināmas abas katetes.",
         "opcijas": ["tg", "sin", "cos", "neviena"],
         "pareizi": 0, "padoms": "Pretkatete : piekatete."},
        {"jaut": "Zināma hipotenūza un piekatete.",
         "opcijas": ["cos", "sin", "tg", "Pitagors"],
         "pareizi": 0, "padoms": "Piekatete : hipotenūza."},
        {"jaut": "sin α = 1,3. α = ?",
         "opcijas": ["Tāda leņķa nav", "80°", "45°", "90°"],
         "pareizi": 0, "padoms": "sin ≤ 1."},
    ]),

    Pasaule("Slēpošanas nogāze",
            Kustiba("", [
                {"jaut": "Nogāze: 60 m kritums uz 200 m horizontāli. Slīpuma "
                         "leņķis līdz grādiem?",
                 "atb": 17, "beigas": 45, "iedala": 5, "mers": "°",
                 "merkis": "zilā trase", "objekts": "Slēpotājs",
                 "padoms": "tg α = 0,3 → 16,7°."},
                {"jaut": "Melnā trase: 100 m kritums uz 170 m. Leņķis līdz "
                         "grādiem?",
                 "atb": 30, "beigas": 45, "iedala": 5, "mers": "°",
                 "merkis": "melnā trase", "objekts": "Slēpotājs",
                 "padoms": "tg α ≈ 0,588 → 30,5°."},
            ]),
            pavediens="sports",
            konteksts="Trases grūtību nosaka slīpums: jo lielāks leņķis, jo "
                      "ātrāk slīd.",
            kapec="No kartes izmēriem tangenss dod leņķi."),

    Kopsavilkums([
        "Atrodu leņķi no sin, cos vai tg vērtības.",
        "Izvēlos sakarību pēc zināmajām malām.",
        "Noapaļoju leņķi un novērtēju rezultātu.",
    ]),

    Majas([
        "Izmēri kāpņu pakāpienu (augstums un dziļums) un aprēķini slīpumu.",
        "Atrodi leņķus trijstūrī 8, 15, 17.",
        "Pārbaudi: vai abu šauro leņķu summa ir 90°?",
    ]),
]
