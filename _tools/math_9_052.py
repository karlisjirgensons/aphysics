# -*- coding: utf-8 -*-
"""9. klase, 52. stunda: «Kā aprēķināt leņķi?»

Divas zināmas malas → attiecība → leņķis ar SHIFT. Tad otrs šaurais leņķis
90° − α. Stunda sākas ar Pizas torni: novirze no vertikāles 3,9 m pie
augstuma ~56 m.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, taisnlenka)

TEMA = "Kā aprēķināt leņķi?"

MERKIS = ("Aprēķināsim šaurā leņķa lielumu, ja zināmas divas malas.")

SATURS = [
    Sakums("Cik grādu sasvēries Pizas tornis?",
           zimejums=taisnlenka(1.5, 8, ("56 m", "3,9 m", None), None,
                               otrs="φ"),
           paraksts="Novirze 3,9 m uz ~56 m augstumu.",
           fakti=["tg φ = 3,9 : 56 ≈ 0,070.",
                  "φ ≈ 4° - tik maz, bet pamanāms ar aci.",
                  "Leņķi aprēķina no divām malām."]),

    Doma("Leņķis no divām malām",
         "Izvēlies sakarību ar abām zināmajām malām, aprēķini skaitli un "
         "nospied SHIFT sin / cos / tan.",
         soli=[
             "Pretkatete + piekatete → tg.",
             "Pretkatete + hipotenūza → sin.",
             "Piekatete + hipotenūza → cos.",
             "Otrs šaurais leņķis: 90° − α.",
         ]),

    Paraugs("Abi šaurie leņķi",
            uzd="Taisnleņķa trijstūra katetes 7 cm un 24 cm. Atrodi šauros "
                "leņķus.",
            soli=[
                ("tg α = {7|24} ≈ 0,2917", "Leņķis pretī 7."),
                ("α ≈ 16,3°", "SHIFT tan."),
                ("β = 90° − 16,3° = 73,7°", "Summa 90°."),
            ],
            atbilde="≈ 16° un ≈ 74°"),

    Ievadi("Aprēķini leņķi (līdz grādiem)", [
        {"jaut": "Katetes 6 un 8. Leņķis pretī 6?", "atb": ["37"],
         "padoms": "tg α = 0,75."},
        {"jaut": "Pretkatete 9, hipotenūza 15. α?", "atb": ["37"],
         "padoms": "sin α = 0,6."},
        {"jaut": "Piekatete 4, hipotenūza 10. α?", "atb": ["66"],
         "padoms": "cos α = 0,4 → 66,4°."},
        {"jaut": "Katetes 10 un 10. α?", "atb": ["45"],
         "padoms": "tg α = 1."},
        {"jaut": "Katetes 2 un 7. Lielākais šaurais leņķis?", "atb": ["74"],
         "padoms": "tg β = 3,5 → 74,1°."},
        {"jaut": "α = 38°. Otrs šaurais leņķis?", "atb": ["52"],
         "padoms": "90 − 38."},
    ], pamats=4),

    Varianti("Kā labāk?", [
        {"jaut": "Zināmas hipotenūza 13 un katete 5. Leņķi pretī 5 atrod ar...",
         "opcijas": ["sin", "tg", "cos", "Pitagoru"],
         "pareizi": 0, "padoms": "Pretkatete un hipotenūza."},
        {"jaut": "Aprēķināts α = 95° taisnleņķa trijstūrī. Tas nozīmē...",
         "opcijas": ["kļūda - šaurais leņķis < 90°", "viss kārtībā",
                     "trijstūris platleņķa", "jānoapaļo"],
         "pareizi": 0, "padoms": "Šaurais leņķis."},
    ]),

    Pasaule("Kāpņu stāvums",
            Ievadi("", [
                {"jaut": "Pakāpiena augstums 17 cm, dziļums 29 cm. Kāpņu "
                         "slīpums līdz grādiem?", "atb": ["30"],
                 "padoms": "tg α = 17 : 29 ≈ 0,586 → 30,4°."},
                {"jaut": "Bēniņu kāpnes: augstums 20 cm, dziļums 20 cm. "
                         "Slīpums?", "atb": ["45"], "padoms": "tg α = 1."},
            ]),
            pavediens="maja",
            konteksts="Ērtas kāpnes mājā ir ap 30-35° slīpas; stāvākas ir "
                      "grūtāk kāpt.",
            kapec="Pakāpiena izmēri dod leņķi ar tangensu."),

    Kopsavilkums([
        "Aprēķinu leņķi no divām malām.",
        "Izvēlos pareizo sakarību.",
        "Atrodu otru šauro leņķi.",
    ]),

    Majas([
        "Izmēri kāpnes mājās un aprēķini slīpumu.",
        "Trijstūrī 20, 21, 29 atrodi abus šauros leņķus.",
        "Kādā leņķī pret zemi jāpiesien 10 m aukla, lai pūķis būtu 8 m augstu?",
    ]),
]
