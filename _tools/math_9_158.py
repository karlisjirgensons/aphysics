# -*- coding: utf-8 -*-
"""9. klase, 158. stunda: «Kur tas noder dzīvē?»

Pieskares un ievilktās riņķa līnijas lietojums: siksnas pārvads (taisnie
siksnas gabali ir kopējās pieskares), satelīta redzamība (pieskare no
punkta), logs trijstūra frontonā (r = S : p). Varianti māca izvēlēties:
«vienādi tālu no punktiem» - apvilktā, «no taisnēm» - ievilktā.
"""

from math_saturs import (Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, geometrija)

TEMA = "Kur tas noder dzīvē?"

MERKIS = ("Risināsim praktiskus uzdevumus ar pieskarēm un ievilktām riņķa "
          "līnijām.")

_SIKSNA = geometrija([("O_1", 0, 0, -90), ("O_2", 10, 0, -90),
                      ("_T1", 0, 3), ("_T2", 10, 3), ("_T3", 0, -3),
                      ("_T4", 10, -3)],
                     nogriezni=[("_T1", "_T2"), ("_T3", "_T4"),
                                ("O_1", "O_2"), ("O_1", "_T1"),
                                ("O_2", "_T2")],
                     taisni=[("O_1", "_T1", "_T2")],
                     malas=[(("O_1", "O_2"), "d")],
                     rinki=[("O_1", 3), ("O_2", 3)])

SATURS = [
    Sakums("Velosipēda ķēde un pieskares",
           zimejums=_SIKSNA,
           paraksts="Taisnie siksnas gabali ir abu ratu kopējās pieskares.",
           fakti=["Pieskare ⊥ rādiusam - O_1T_1T_2O_2 ir taisnstūris.",
                  "Vienādiem ratiem taisnais gabals = d.",
                  "Ap katru ratu siksna iet pa pusi riņķa līnijas."]),

    Paraugs("Siksnas garums",
            uzd="Divi vienādi skriemeļi, r = 10 cm, centri 50 cm viens no "
                "otra. Cik gara ir siksna?",
            soli=[
                ("2 · 50 = 100 cm", "Divi taisnie gabali, katrs = d."),
                ("2 · {1|2} · 2π · 10 = 20π ≈ 62,8 cm",
                 "Divas pusriņķa līnijas."),
                ("100 + 62,8 ≈ 163 cm", "Kopā."),
            ],
            atbilde="≈ 163 cm"),

    Varianti("Kuru riņķa līniju vajag?", [
        {"jaut": "Aka vienādā attālumā no trim mājām.",
         "opcijas": ["apvilkto (vidusperpendikuli)",
                     "ievilkto (bisektrises)"], "jaukt": False,
         "pareizi": 0, "padoms": "Vienādi tālu no punktiem."},
        {"jaut": "Strūklaka vienādā attālumā no trim ceļiem.",
         "opcijas": ["apvilkto (vidusperpendikuli)",
                     "ievilkto (bisektrises)"], "jaukt": False,
         "pareizi": 1, "padoms": "Vienādi tālu no taisnēm."},
        {"jaut": "Mazākais apaļais galdauts, kas nosedz trijstūra galdu.",
         "opcijas": ["apvilkto (vidusperpendikuli)",
                     "ievilkto (bisektrises)"], "jaukt": False,
         "pareizi": 0, "padoms": "Galdautam jāiet caur virsotnēm."},
        {"jaut": "Lielākais apaļais spogulis trijstūra nišā.",
         "opcijas": ["apvilkto (vidusperpendikuli)",
                     "ievilkto (bisektrises)"], "jaukt": False,
         "pareizi": 1, "padoms": "Spogulis pieskaras malām."},
    ]),

    Ievadi("Aprēķini", [
        {"jaut": "Apaļa pica, d = 32 cm. Mazākās kvadrātiskās kastes mala "
                 "(cm)?", "atb": ["32"], "padoms": "Aplis ievilkts kvadrātā."},
        {"jaut": "Kvadrātiskā galda mala 80 cm. Mazākā apaļā galdauta "
                 "diametrs (cm)? Noapaļo līdz veselam.", "atb": ["113"],
         "padoms": "Diagonāle 80√2."},
        {"jaut": "Frontons - vienādsānu trijstūris: pamats 8 m, sānu malas "
                 "5 m, augstums 3 m. Apaļa loga lielākais r (cm)? Noapaļo "
                 "līdz veselam.", "atb": ["133"],
         "padoms": "S = 12, p = 9, r = 12 : 9 m."},
    ]),

    Pasaule("Velosipēda ķēde",
            Ievadi("", [
                {"jaut": "Zobratu r = 5 cm abiem, centri 40 cm viens no otra. "
                         "Cik cm ir abi taisnie ķēdes gabali kopā?",
                 "atb": ["80"], "padoms": "2 · 40."},
                {"jaut": "Visas ķēdes garums (cm)? π ≈ 3,14; noapaļo līdz "
                         "veselam.", "atb": ["111"],
                 "padoms": "80 + 2π · 5 = 111,4."},
            ]),
            pavediens="sports",
            konteksts="Vienkāršotā modelī abi zobrati ir vienādi, un ķēde tos "
                      "apņem kā siksna.",
            kapec="Ķēdes taisnie gabali ir kopējās pieskares - tie ir tikpat "
                  "gari kā attālums starp centriem.",
            zimejums=_SIKSNA),

    Pasaule("GPS satelīts",
            Ievadi("", [
                {"jaut": "Satelīts 20 200 km virs Zemes (R = 6370 km). Cik km "
                         "līdz tālākajam punktam, ko tas redz? Noapaļo līdz "
                         "simtiem.", "atb": ["25800"],
                 "padoms": "√(26 570^2 − 6370^2) ≈ 25 795."},
            ]),
            pavediens="kosmoss",
            konteksts="Satelīts «redz» Zemi līdz vietai, kur skata līnija tai "
                      "pieskaras.",
            kapec="Tas pats taisnleņķa trijstūris centrs-satelīts-pieskares "
                  "punkts, ko lietojām horizontam."),

    Kopsavilkums([
        "Atpazīstu pieskares un ievilktas riņķa līnijas dzīves situācijās.",
        "Izvēlos: vienādi tālu no punktiem vai no taisnēm.",
        "Aprēķinu siksnas garumu un pieskares nogriezni.",
    ]),

    Majas([
        "Izmēri velosipēda zobratus un aprēķini ķēdes garumu.",
        "Atrodi mājās priekšmetu, kurā aplis ievilkts kvadrātā.",
        "Uz kartes atzīmē trīs ceļus un atrodi punktu vienādi tālu no tiem.",
    ]),
]
