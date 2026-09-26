# -*- coding: utf-8 -*-
"""9. klase, 166. stunda: «Kā noformē risinājumu?»

Izvērstajā uzdevumā vērtē ne tikai atbildi: formula vai darbība, tad
ievietotās vērtības, tad rezultāts ar mērvienību un atbilde. Biežākās
punktu zaudēšanas vietas - tikai atbilde bez risinājuma, noapaļošana
starprezultātos, trūkstoša mērvienība un pārrakstīšanās kļūda.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti)

TEMA = "Kā noformē risinājumu?"

MERKIS = ("Atkārtosim risinājuma noformēšanas prasības un biežākās punktu "
          "zaudēšanas vietas.")

SATURS = [
    Sakums("Pareiza atbilde - bet tikai 1 punkts no 3. Kāpēc?",
           fakti=["Izvērstā uzdevumā punktus dod par katru soli.",
                  "Formula → vērtības → rezultāts → atbilde.",
                  "Noapaļo tikai beigās, mērvienību raksti vienmēr."]),

    Doma("Risinājuma kārtība",
         "Vērtētājam jāredz, ko tu darīji: katra rinda seko no iepriekšējās.",
         soli=[
             "Uzraksti formulu vai darbību ar burtiem.",
             "Ievieto vērtības.",
             "Aprēķini rezultātu ar mērvienību.",
             "Uzraksti atbildi - teikumu vai «Atbilde: ...».",
         ],
         pieze="Ģeometrijā katram apgalvojumam pievieno pamatojumu: «jo "
               "pieskare ⊥ rādiusam», «jo leņķu summa 180°»."),

    Paraugs("Pasākuma izmaksas",
            uzd="Telpas īre 280 €, par katru dalībnieku 25 €. Aprēķini "
                "izmaksas 100 dalībniekiem.",
            soli=[
                ("I = 280 + 25 · x", "Izteiksme ar burtu."),
                ("I = 280 + 25 · 100", "Ievieto x = 100."),
                ("I = 2780 €", "Rezultāts ar mērvienību."),
            ],
            atbilde="pasākums izmaksās 2780 €"),

    Varianti("Kur zaudē punktus?", [
        {"jaut": "Izvērstā uzdevumā uzrakstīta tikai atbilde «2780 €».",
         "opcijas": ["zaudē risinājuma punktus", "pilni punkti"],
         "jaukt": False, "pareizi": 0, "padoms": "Risinājums nav redzams."},
        {"jaut": "Starprezultāts noapaļots līdz veseliem, galarezultāts "
                 "sanāk cits.",
         "opcijas": ["zaudē punktu", "pilni punkti"], "jaukt": False,
         "pareizi": 0, "padoms": "Noapaļo tikai beigās."},
        {"jaut": "Laukums uzrakstīts «48» bez cm^2.",
         "opcijas": ["var zaudēt punktu", "pilni punkti"], "jaukt": False,
         "pareizi": 0, "padoms": "Mērvienība ir daļa no atbildes."},
        {"jaut": "Svītrots nepareizs mēģinājums, blakus pareizs risinājums.",
         "opcijas": ["vērtē pareizo", "zaudē visus punktus"], "jaukt": False,
         "pareizi": 0, "padoms": "Svītroto nevērtē."},
    ]),

    Ievadi("Noapaļo tikai beigās", [
        {"jaut": "2,46 · 3,5 - noapaļo rezultātu līdz desmitdaļām.",
         "atb": ["8,6"], "padoms": "2,46 · 3,5 = 8,61."},
        {"jaut": "Ja vispirms noapaļo 2,46 ≈ 2,5, tad 2,5 · 3,5 = ?",
         "atb": ["8,75"], "padoms": "Cits rezultāts - tātad kļūda."},
        {"jaut": "√50 · √2 = ? (neapaļo!)", "atb": ["10"],
         "padoms": "√100."},
    ]),

    Pasaule("Pasākums skolā",
            Ievadi("", [
                {"jaut": "Uzraksti izmaksu izteiksmi x dalībniekiem.",
                 "atb": ["280 + 25x", "25x + 280", "280 + 25·x",
                         "25·x + 280", "280+25*x", "25*x+280"],
                 "tastatura": "text", "padoms": "Nemainīgā daļa + 25 · x."},
                {"jaut": "Budžets 1530 €. Cik dalībnieku var uzaicināt?",
                 "atb": ["50"], "padoms": "280 + 25x = 1530."},
            ]),
            pavediens="skola",
            konteksts="Tieši šāds uzdevums bija 2025. gada eksāmena 6. "
                      "uzdevumā.",
            kapec="Izteiksme ar burtu ir pirmā risinājuma rinda - par to "
                  "dod punktu pat tad, ja rēķinā kļūdies."),

    Kopsavilkums([
        "Rakstu risinājumu: formula, vērtības, rezultāts, atbilde.",
        "Noapaļoju tikai galarezultātu.",
        "Zinu biežākās punktu zaudēšanas vietas.",
    ]),

    Majas([
        "Pārraksti vienu sava kontroldarba uzdevumu pilnā noformējumā.",
        "Palūdz klasesbiedram «novērtēt» tavu risinājumu - vai viss "
        "saprotams?",
        "Uzraksti sev atgādni ar 4 noformēšanas soļiem.",
    ]),
]
