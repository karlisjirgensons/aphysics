# -*- coding: utf-8 -*-
"""9. klase, 46. stunda: «Kāds ir 30° leņķa sinuss?»

Precīzas vērtības bez kalkulatora: vienādmalu trijstūri ar malu 2 augstums
sadala divos taisnleņķa trijstūros ar leņķiem 30° un 60°, katetēm 1 un √3.
No tā visas sešas vērtības.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Pasaule, Sakums, Slidnis,
                         Varianti, Ievadi, geometrija, restis, taisnlenka)

TEMA = "Kāds ir 30° leņķa sinuss?"

MERKIS = ("Iegūsim 30° un 60° leņķu vērtības no vienādmalu trijstūra "
          "īpašībām.")

_H = 1.732

_VIENADMALU = geometrija([("A", 0, 0), ("B", 2, 0), ("C", 1, _H),
                          ("D", 1, 0)],
                         nogriezni=["AB", "BC", "CA"], izcelti=["CD"],
                         taisni=["ADC"], iekrasot=[("ADC", 1)],
                         lenki=[("DCA", "30°"), ("DAC", "60°")],
                         malas=[("AC", "2"), ("AD", "1"), ("CD", "√3")])

SATURS = [
    Sakums("sin 30° = 0,5 - precīzi. Kāpēc?",
           zimejums=_VIENADMALU,
           paraksts="Vienādmalu trijstūris ar malu 2, augstums CD.",
           fakti=["Augstums sadala 60° leņķi uz pusēm - 30°.",
                  "AD = 1 (puse no malas), AC = 2.",
                  "sin 30° = {AD|AC} = {1|2}."]),

    Slidnis("Iegūstam vērtības", [
        {"v": "Augstums", "teksts": "CD = √(2^2 − 1^2) = √3",
         "zim": _VIENADMALU},
        {"v": "30°", "teksts": "sin 30° = {1|2}, cos 30° = {√3|2}, "
                               "tg 30° = {1|√3} = {√3|3}",
         "zim": taisnlenka(1.732, 1, ("1", "√3", "2"), "30°")},
        {"v": "60°", "teksts": "sin 60° = {√3|2}, cos 60° = {1|2}, "
                               "tg 60° = √3",
         "zim": taisnlenka(1, 1.732, ("√3", "1", "2"), "60°")},
    ]),

    Doma("30° un 60°",
         "sin 30° = cos 60° = {1|2}; cos 30° = sin 60° = {√3|2}; "
         "tg 30° = {√3|3}, tg 60° = √3.",
         soli=[
             "Iegaumē trijstūri: 1, √3, 2.",
             "Pretī 30° - īsākā katete 1.",
             "Pretī 60° - katete √3.",
             "Pārbaude ar kalkulatoru: {√3|2} ≈ 0,866.",
         ]),

    Varianti("Izvēlies precīzo vērtību", [
        {"jaut": "cos 30° = ?",
         "opcijas": ["{√3|2}", "{1|2}", "√3", "{√2|2}"],
         "pareizi": 0, "padoms": "Piekatete √3, hipotenūza 2."},
        {"jaut": "tg 60° = ?",
         "opcijas": ["√3", "{√3|3}", "{1|2}", "1"],
         "pareizi": 0, "padoms": "√3 : 1."},
        {"jaut": "sin 60° = ?",
         "opcijas": ["{√3|2}", "{1|2}", "{√3|3}", "2"],
         "pareizi": 0, "padoms": "Pretī 60° ir √3."},
        {"jaut": "tg 30° = ?",
         "opcijas": ["{√3|3}", "√3", "{1|2}", "{√3|2}"],
         "pareizi": 0, "padoms": "{1|√3} = {√3|3}."},
    ]),

    Ievadi("Aprēķini bez kalkulatora", [
        {"jaut": "Hipotenūza 14, leņķis 30°. Pretkatete?", "atb": ["7"],
         "padoms": "14 · {1|2}."},
        {"jaut": "Hipotenūza 10, leņķis 60°. Piekatete?", "atb": ["5"],
         "padoms": "cos 60° = {1|2}."},
        {"jaut": "sin 30° + cos 60° = ?", "atb": ["1"],
         "padoms": "{1|2} + {1|2}."},
        {"jaut": "2 · sin 30° · tg 60° = √?", "atb": ["3"],
         "padoms": "2 · {1|2} · √3."},
    ]),

    Pasaule("Vienādmalu jumts",
            Ievadi("", [
                {"jaut": "Jumta frontons - vienādmalu trijstūris ar malu 8 m. "
                         "Jumta augstums = 4√3 m ≈ ? m (līdz desmitdaļām)",
                 "atb": ["6,9"], "padoms": "4 · 1,732."},
                {"jaut": "Frontona laukums ≈ ? m² (līdz veseliem)",
                 "atb": ["28"], "padoms": "{8 · 6,93|2} ≈ 27,7."},
            ]),
            pavediens="maja",
            konteksts="Ja jumta slīpnes ir tikpat garas kā mājas platums, "
                      "frontons ir vienādmalu trijstūris ar 60° slīpumu.",
            kapec="Augstums = mala · sin 60° = mala · {√3|2}.",
            zimejums=restis([["mala", "augstums"], ["2", "√3"],
                             ["8", "4√3"]])),

    Kopsavilkums([
        "Iegūstu 30° un 60° vērtības no vienādmalu trijstūra.",
        "Zinu: sin 30° = {1|2}, cos 30° = {√3|2}.",
        "Aprēķinu malas bez kalkulatora.",
    ]),

    Majas([
        "Uzzīmē vienādmalu trijstūri ar malu 6 cm un pārbaudi sin 30° ar "
        "mērījumu.",
        "Aprēķini: sin 60° · cos 30° + sin 30° · cos 60°.",
        "Paskaidro, kāpēc sin 30° = cos 60°.",
    ]),
]
