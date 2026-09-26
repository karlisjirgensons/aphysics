# -*- coding: utf-8 -*-
"""8. klase, 71. stunda: «Precīzi vai aptuveni?»

Precīzā atbilde satur π (16π), aptuvenā - tuvinājumu (≈ 50,3). π ≈ 3,14
vai {22|7} der bez kalkulatora; kalkulatora poga π ir precīzāka.
Noapaļo tikai beigās - to jau mācījās 8.3. tematā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, rinkis)

TEMA = "Precīzi vai aptuveni?"

MERKIS = ("Aprēķināsim riņķa laukumu precīzi ar skaitli π un aptuveni ar tā "
          "tuvinājumu.")

SATURS = [
    Sakums("16π vai 50,24?",
           zimejums=rinkis(radiuss="r = 4 cm"),
           paraksts="S = 16π cm² ≈ 50,3 cm²",
           fakti=["Precīzā atbilde satur π: S = 16π cm².",
                  "Aptuvenā - ar tuvinājumu: π ≈ 3,14 vai π ≈ {22|7}.",
                  "Tuvinājumu noapaļo tikai pašās beigās."]),

    Doma("Divi atbildes veidi",
         "π ir iracionāls skaitlis, tāpēc precīzā atbilde to satur.",
         soli=[
             "Precīzi: atstāj π kā reizinātāju: S = 9π.",
             "Aptuveni: ievieto π ≈ 3,14 un noapaļo.",
             "Kalkulatorā lieto pogu π - tā ir precīzāka par 3,14.",
             "Izlasi uzdevumā, kādu atbildi prasa.",
         ],
         pieze="{22|7} ≈ 3,143 - ērti bez kalkulatora, ja r dalās ar 7."),

    Paraugs("Trīs veidi",
            uzd="Riņķa rādiuss ir 14 cm. Aprēķini laukumu precīzi un "
                "aptuveni.",
            soli=[
                ("S = π · 14^2 = 196π cm²", "Precīzi."),
                ("196 · {22|7} = 28 · 22 = 616 cm²", "Ar π ≈ {22|7}."),
                ("196 · 3,14 = 615,44 cm²", "Ar π ≈ 3,14."),
            ],
            atbilde="196π ≈ 616 cm²"),

    Ievadi("Aprēķini", [
        {"jaut": "r = 3. S = ?π", "atb": ["9"], "padoms": "3^2."},
        {"jaut": "r = 0,5. S = ?π", "atb": ["0,25"], "padoms": "0,5^2."},
        {"jaut": "d = 12. S = ?π", "atb": ["36"], "padoms": "r = 6."},
        {"jaut": "r = 7, π ≈ {22|7}. S?", "atb": ["154"],
         "padoms": "49 · {22|7}."},
        {"jaut": "r = 10, π ≈ 3,14. S?", "atb": ["314"],
         "padoms": "100 · 3,14."},
        {"jaut": "S = 25π. r = ?", "atb": ["5"], "padoms": "r^2 = 25."},
    ], pamats=4),

    Varianti("Spried", [
        {"jaut": "Kura atbilde ir precīza?",
         "opcijas": ["36π", "113,04", "113", "113,1"],
         "pareizi": 0, "padoms": "Pārējās ir tuvinājumi."},
        {"jaut": "Kāpēc noapaļo tikai beigās?",
         "opcijas": ["Lai kļūda neuzkrātos", "Tā ir ātrāk",
                     "Tā ir skaistāk", "Tam nav nozīmes"],
         "pareizi": 0, "padoms": "Katra noapaļošana pieliek kļūdu."},
        {"jaut": "r = 1 m. S ≈ ?",
         "opcijas": ["3,14 m²", "6,28 m²", "1 m²", "3,14 m"],
         "pareizi": 0, "padoms": "π · 1^2; mērvienība m²."},
    ]),

    Pasaule("Strūklakas baseins",
            Ievadi("", [
                {"jaut": "Apaļa baseina rādiuss ir 3 m. Dibena laukums "
                         "precīzi = ?π m²",
                 "atb": ["9"], "padoms": "3^2."},
                {"jaut": "Aptuveni (π ≈ 3,14), līdz desmitdaļām (m²)?",
                 "atb": ["28,3"], "padoms": "9 · 3,14 = 28,26."},
                {"jaut": "1 litrs krāsas sedz 4 m². Cik litru jāpērk "
                         "(veselos)?",
                 "atb": ["8"], "padoms": "28,26 : 4 ≈ 7,1 - uz augšu."},
            ]),
            pavediens="maja",
            konteksts="Projektētājs atstāj π līdz beigām, bet krāsu pērk "
                      "pēc noapaļota skaitļa.",
            kapec="Precīzā atbilde der jebkuram tālākam aprēķinam."),

    Kopsavilkums([
        "Pierakstu riņķa laukumu precīzi ar π.",
        "Aprēķinu aptuveno vērtību ar 3,14 vai {22|7}.",
        "Noapaļoju tikai beigās.",
    ]),

    Majas([
        "Aprēķini laukumu riņķim ar r = 21 cm precīzi un ar π ≈ {22|7}.",
        "Salīdzini rezultātus ar 3,14 un ar kalkulatora π.",
        "Atrodi mājās apaļu virsmu un aprēķini tās laukumu.",
    ]),
]
