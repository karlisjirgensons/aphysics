# -*- coding: utf-8 -*-
"""8. klase, 106. stunda: «Kā risināt uzdevumu ar četrstūri?»

Temata noslēgums pirms PD5: aprēķinu un pierādījuma uzdevumi, kuros
jāizvēlas, kuru četrstūra īpašību lietot. Paraugā romba leņķi atrod no
vienādmalu trijstūra, ko nogriež īsākā diagonāle.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, geometrija)

TEMA = "Kā risināt uzdevumu ar četrstūri?"

MERKIS = ("Risināsim aprēķinu un pierādījuma uzdevumu, lietojot četrstūru "
          "īpašības.")

SATURS = [
    Sakums("Romba īsākā diagonāle ir vienāda ar malu. Kādi ir leņķi?",
           zimejums=geometrija([("A", 0, 0), ("B", 4, 0), ("C", 6, 3.464),
                                ("D", 2, 3.464)],
                               nogriezni=["AB", "BC", "CD", "DA", "BD"],
                               svitras=[("AB", 1), ("BC", 1), ("CD", 1),
                                        ("DA", 1), ("BD", 1)],
                               iekrasot=[("ABD", 1)]),
           paraksts="△ABD ir vienādmalu, tāpēc ∠A = 60°.",
           fakti=["Vispirms nosaki četrstūra veidu.",
                  "Izraksti īpašības, kas var noderēt.",
                  "Meklē trijstūrus - tur der visi trijstūra likumi."]),

    Doma("Risināšanas plāns",
         "Četrstūra uzdevums bieži kļūst par trijstūra uzdevumu.",
         soli=[
             "Uzzīmē un atzīmē visu doto.",
             "Nosaki četrstūra veidu un tā īpašības.",
             "Atrodi trijstūri ar pietiekami daudz zināmu elementu.",
             "Aprēķini un pamato katru soli.",
             "Pārbaudi ar leņķu summu vai perimetru.",
         ]),

    Paraugs("Romba leņķi",
            uzd="Romba ABCD mala ir 4 cm, diagonāle BD = 4 cm. Atrodi romba "
                "leņķus.",
            soli=[
                ("AB = AD = BD = 4", "Romba malas un dotā diagonāle."),
                ("△ABD - vienādmalu, ∠A = 60°", "Visi leņķi 60°."),
                ("∠C = ∠A = 60°", "Pretējie leņķi."),
                ("∠B = ∠D = 180° − 60° = 120°", "Blakus leņķi."),
            ],
            atbilde="60°, 120°, 60°, 120°"),

    Ievadi("Aprēķini", [
        {"jaut": "Taisnstūra diagonāle ar malu veido 30°. Leņķis starp "
                 "diagonālēm (šaurais, °)?", "atb": ["60"],
         "padoms": "△AOB vienādsānu: 180 − 2 · 30 = 120; šaurais 60."},
        {"jaut": "Paralelogramā ∠A = 2∠B. ∠A?", "atb": ["120"],
         "padoms": "3∠B = 180°."},
        {"jaut": "Romba perimetrs 40, viena diagonāle 12, otra 16. S?",
         "atb": ["96"], "padoms": "{12 · 16|2}."},
        {"jaut": "Tam pašam rombam augstums (mala 10)?", "atb": ["9,6"],
         "padoms": "96 : 10."},
        {"jaut": "Kvadrāta diagonāle 12. S?", "atb": ["72"],
         "padoms": "{144|2}."},
    ]),

    Varianti("Kuru īpašību lietot?", [
        {"jaut": "Jāpierāda, ka taisnstūrī △AOB ir vienādsānu.",
         "opcijas": ["Diagonāles vienādas un dalās uz pusēm",
                     "Diagonāles perpendikulāras", "Malas vienādas",
                     "Leņķu summa 360°"],
         "pareizi": 0, "padoms": "AO = BO."},
        {"jaut": "Jāatrod romba leņķis starp diagonāli un malu.",
         "opcijas": ["Diagonāle ir bisektrise", "Diagonāles vienādas",
                     "Malas paralēlas", "Laukuma formula"],
         "pareizi": 0, "padoms": "Dala leņķi uz pusēm."},
        {"jaut": "Jāpierāda, ka četrstūris ir paralelograms, zinot, ka "
                 "diagonāles dalās uz pusēm.",
         "opcijas": ["Paralelograma pazīme", "Romba īpašība",
                     "Taisnstūra īpašība", "Pitagora teorēma"],
         "pareizi": 0, "padoms": "98. stunda."},
    ]),

    Pasaule("Logu rāmis",
            Ievadi("", [
                {"jaut": "Logs ir taisnstūris 120 cm × 90 cm, diagonāle "
                         "150 cm. Cik cm no diagonāļu krustpunkta līdz "
                         "stūrim?",
                 "atb": ["75"], "padoms": "150 : 2."},
                {"jaut": "Loga laukums (m²)?", "atb": ["1,08"],
                 "padoms": "1,2 · 0,9."},
                {"jaut": "Rāmja līstes garums (m)?", "atb": ["4,2"],
                 "padoms": "2 · (1,2 + 0,9)."},
            ]),
            pavediens="maja",
            konteksts="Logu meistars pārbauda rāmi ar diagonālēm un pērk "
                      "stiklu pēc laukuma.",
            kapec="Taisnstūra īpašības dod visus vajadzīgos izmērus."),

    Kopsavilkums([
        "Izvēlos piemērotu četrstūra īpašību.",
        "Pārveidoju četrstūra uzdevumu trijstūra uzdevumā.",
        "Pamatoju katru risinājuma soli.",
    ]),

    Majas([
        "Atrisini: romba leņķis 120°, īsākā diagonāle 5 cm - atrodi "
        "perimetru.",
        "Izdomā pierādījuma uzdevumu par paralelogramu un atrisini to.",
        "Atkārto tabulu «paralelograms - rombs - taisnstūris - kvadrāts».",
    ]),
]
