# -*- coding: utf-8 -*-
"""9. klase, 49. stunda: «Kā katete saistās ar hipotenūzu?»

Katete pret 30° leņķi ir puse no hipotenūzas - tas ir sin 30° = {1|2}
vārdos. 2025. gada eksāmenā tieši tāds bija 18. uzdevums (FG = 8,
∠G = 30°, atrast EG), tikai tur jāpamana, ka meklē otru kateti.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, taisnlenka)

TEMA = "Kā katete saistās ar hipotenūzu?"

MERKIS = ("Lietosim sakarību, ka katete pret 30° ir puse no hipotenūzas.")

SATURS = [
    Sakums("Eksāmens 2025: FG = 8, ∠G = 30°. EG = ?",
           zimejums=taisnlenka(1.732, 1, ("?", "EG", "8"), "30°",
                               burti=("G", "F", "E")),
           paraksts="∠E = 90°. Katete pretī 30° ir EF.",
           fakti=["Katete pret 30° = puse no hipotenūzas: EF = 4.",
                  "EG pieskaras 30° leņķim - to dod cos 30°.",
                  "EG = 8 · {√3|2} = 4√3 cm."]),

    Doma("Katete pret 30°",
         "Taisnleņķa trijstūrī katete, kas atrodas pretī 30° leņķim, ir puse "
         "no hipotenūzas.",
         soli=[
             "Atrodi 30° leņķi un malu PRETĪ tam.",
             "Tā ir {1|2} hipotenūzas (un otrādi: hipotenūza = 2 · katete).",
             "Otru kateti dod Pitagors vai cos 30°.",
         ],
         pieze="Apgrieztā sakarība: ja katete ir puse no hipotenūzas, pretī "
               "tai ir 30° leņķis."),

    Paraugs("Eksāmena 18. uzdevums",
            uzd="△EFG, ∠E = 90°, FG = 8 cm, ∠G = 30°. Aprēķini EG.",
            soli=[
                ("EF = {FG|2} = 4 (cm)", "Katete pret 30°."),
                ("EG = √(8^2 − 4^2) = √48 = 4√3 (cm)", "Pitagora teorēma."),
                ("EG ≈ 6,93 cm", "Tuvinājums (ja prasīts)."),
            ],
            atbilde="EG = 4√3 cm"),

    Ievadi("Aprēķini", [
        {"jaut": "Hipotenūza 18, leņķis 30°. Katete pretī 30°?",
         "atb": ["9"], "padoms": "18 : 2."},
        {"jaut": "Katete pretī 30° ir 7. Hipotenūza?", "atb": ["14"],
         "padoms": "2 · 7."},
        {"jaut": "Hipotenūza 20, ∠B = 60°. Katete pretī ∠A?", "atb": ["10"],
         "padoms": "∠A = 30°."},
        {"jaut": "Hipotenūza 12, leņķis 30°. Otra katete = 6√?",
         "atb": ["3"], "padoms": "√(144 − 36) = √108 = 6√3."},
        {"jaut": "Katete 5, hipotenūza 10. Leņķis pretī katetei (°)?",
         "atb": ["30"], "padoms": "Apgrieztā sakarība."},
    ], pamats=3),

    Varianti("Kura mala?", [
        {"jaut": "∠A = 30°, ∠C = 90°. Puse no hipotenūzas ir...",
         "opcijas": ["BC", "AC", "AB", "neviena"],
         "pareizi": 0, "padoms": "Pretī A."},
        {"jaut": "∠B = 30°, ∠C = 90°, AB = 16. Kura mala ir 8?",
         "opcijas": ["AC", "BC", "AB", "neviena"],
         "pareizi": 0, "padoms": "Pretī B."},
        {"jaut": "Taisnleņķa trijstūrī katete 6, hipotenūza 12. Leņķi ir...",
         "opcijas": ["30°, 60°, 90°", "45°, 45°, 90°", "20°, 70°, 90°",
                     "nevar zināt"],
         "pareizi": 0, "padoms": "Katete = puse no hipotenūzas."},
    ]),

    Pasaule("Slīdkalniņš bērnu laukumā",
            Ievadi("", [
                {"jaut": "Slīdkalniņš 4 m garš, slīpums 30°. Cik m augsta ir "
                         "platforma?", "atb": ["2"], "padoms": "4 : 2."},
                {"jaut": "Drošībai platforma ne augstāk par 1,5 m. Cik m garu "
                         "30° slīdkalniņu drīkst likt?", "atb": ["3"],
                 "padoms": "2 · 1,5."},
            ]),
            pavediens="sports",
            konteksts="Bērnu slīdkalniņi bieži slīpi 30° leņķī - tad augstums "
                      "ir tieši puse no garuma.",
            kapec="Viena sakarība - bez kalkulatora.",
            zimejums=taisnlenka(3.46, 2, ("h", None, "4 m"), "30°")),

    Kopsavilkums([
        "Lietoju: katete pret 30° = puse hipotenūzas.",
        "Lietoju apgriezto sakarību leņķa noteikšanai.",
        "Atrisinu eksāmena uzdevumu ar 30° leņķi.",
    ]),

    Majas([
        "Pierādi sakarību ar vienādmalu trijstūri.",
        "△ABC, ∠C = 90°, ∠A = 60°, AB = 10. Atrodi AC un BC.",
        "Atrodi ap sevi slīpumu ~30° un pārbaudi ar mērlenti.",
    ]),
]
