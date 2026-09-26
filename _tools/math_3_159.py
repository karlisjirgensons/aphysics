# -*- coding: utf-8 -*-
"""3. klase, 159. stunda: «Cik gara ir visu šķautņu summa?»

Kvadra šķautņu summa ir pirmā formula, kurā ir trīs dažādi burti. To iegūst
no skaitīšanas: katrs no trim izmēriem parādās tieši četras reizes, tāpēc
summa ir 4 · (a + b + c).
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         kermenis)

TEMA = "Cik gara ir visu šķautņu summa?"

MERKIS = ("Mērīsim šķautnes un pierakstīsim izteiksmi visu šķautņu garumu "
          "summai.")

SATURS = [
    Sakums("Cik daudz stieples vajag kastes karkasam?",
           zimejums=kermenis("kvadrs", virsraksts="a, b un c"),
           paraksts="Katrs no trim izmēriem atkārtojas četras reizes.",
           fakti=["Kvadram ir 12 šķautnes, bet tikai trīs dažādi garumi.",
                  "Katrs garums atkārtojas tieši četras reizes."]),

    Doma("Katrs izmērs atkārtojas četras reizes",
         "Visu šķautņu summa ir 4 · a + 4 · b + 4 · c jeb 4 · (a + b + c).",
         soli=[
             "Izmēri trīs dažādus šķautņu garumus: a, b un c.",
             "Katru reizini ar 4.",
             "Saskaiti visus trīs rezultātus.",
             "Vai arī vispirms saskaiti a + b + c un reizini ar 4.",
         ],
         pieze="Kubam visi trīs izmēri ir vienādi, tāpēc summa ir "
               "12 · a - vienkāršāk nekā vispārīgā formula."),

    Petijums("Izmēri kastītes šķautnes",
             vajag="kartona kastīte, lineāls un aukla",
             soli=[
                 "Izmēri kastītes garumu, platumu un augstumu.",
                 "Izrēķini visu šķautņu summu.",
                 "Aptin auklu ap visām šķautnēm un izmēri to.",
                 "Salīdzini abus rezultātus.",
             ],
             secinajums="Aprēķins un mērījums sakrīt - tas apstiprina, ka "
                        "katrs izmērs tiešām atkārtojas četras reizes."),

    Paraugs("Cik gara ir šķautņu summa?",
            uzd="Kvadra izmēri ir 5 cm, 4 cm un 3 cm. Cik gara ir visu "
                "šķautņu summa?",
            soli=[
                ("5 + 4 + 3 = 12",
                 "Trīs dažādie izmēri."),
                ("4 · 12 = 48",
                 "Katrs atkārtojas četras reizes."),
                ("48 cm",
                 "Tik gara stieple vajadzīga karkasam."),
            ],
            atbilde="48 cm"),

    Ievadi("Aprēķini šķautņu summu", [
        {"jaut": "Kvadrs 5, 4 un 3 cm. Cik centimetru ir šķautņu summa?",
         "atb": ["48"], "padoms": "4 · 12."},
        {"jaut": "Kvadrs 10, 6 un 4 cm. Cik ir šķautņu summa?",
         "atb": ["80"], "padoms": "4 · 20."},
        {"jaut": "Kubs ar malu 5 cm. Cik ir šķautņu summa?", "atb": ["60"],
         "padoms": "12 · 5."},
        {"jaut": "Kubs ar malu 8 cm. Cik ir šķautņu summa?", "atb": ["96"],
         "padoms": "12 · 8."},
        {"jaut": "Kvadrs 7, 5 un 2 cm. Cik ir šķautņu summa?",
         "atb": ["56"], "padoms": "4 · 14."},
        {"jaut": "Šķautņu summa 48 cm, kubs. Cik gara ir viena mala?",
         "atb": ["4"], "padoms": "48 : 12."},
    ], pamats=4),

    Zimejums("Kubs",
             kermenis("kubs", virsraksts="visas malas vienādas"),
             paskaidro="Kubam visas 12 šķautnes ir vienāda garuma, tāpēc "
                       "summa ir 12 · a.",
             ievads="Īpašais gadījums."),

    Varianti("Kurš rēķins der?", [
        {"jaut": "Kurš rēķins dod kvadra šķautņu summu?",
         "opcijas": ["4 · (a + b + c)", "a · b · c", "2 · (a + b)",
                     "a + b + c"],
         "pareizi": 0, "padoms": "Katrs izmērs četras reizes."},
        {"jaut": "Kurš rēķins dod kuba šķautņu summu?",
         "opcijas": ["12 · a", "6 · a", "a · a · a", "4 · a"],
         "pareizi": 0, "padoms": "12 vienādas šķautnes."},
        {"jaut": "Kvadrs 6, 5 un 4 cm. Cik ir šķautņu summa?",
         "opcijas": ["60 cm", "15 cm", "120 cm", "30 cm"],
         "pareizi": 0, "padoms": "4 · 15."},
        {"jaut": "Cik reižu katrs izmērs parādās kvadra šķautnēs?",
         "opcijas": ["4", "2", "3", "12"],
         "pareizi": 0, "padoms": "12 : 3."},
    ], pamats=4),

    Pasaule("Cik stieples vajag karkasam?",
            Ievadi("", [
                {"jaut": "Karkass 5, 4 un 3 cm. Cik centimetru stieples "
                         "vajag?",
                 "atb": ["48"], "padoms": "4 · 12."},
                {"jaut": "Cik centimetru vajag 5 tādiem karkasiem?",
                 "atb": ["240"], "padoms": "5 · 48."},
                {"jaut": "Cik metru tas ir? Raksti ar komatu.",
                 "atb": ["2,4", "2.4"], "padoms": "240 : 100."},
                {"jaut": "Stieples spolē ir 300 cm. Cik karkasu var "
                         "izgatavot?",
                 "atb": ["6"], "padoms": "300 : 48 ar atlikumu."},
            ]),
            pavediens="tehnika",
            konteksts="Karkasu izgatavo no stieples, un tās garums ir tieši "
                      "visu šķautņu summa.",
            kapec="Ar formulu materiālu var pasūtīt, neko vēl neuzbūvējot."),

    Kopsavilkums([
        "Aprēķinu visu šķautņu garumu summu.",
        "Zinu, ka katrs izmērs atkārtojas četras reizes.",
        "Lietoju izteiksmi 4 · (a + b + c).",
        "Zinu, ka kubam summa ir 12 · a.",
    ]),

    Majas([
        "Izmēri mājas kastīti un izrēķini tās šķautņu summu.",
        "Pārbaudi rezultātu ar auklu.",
        "Izrēķini, cik stieples vajag kubam ar malu 10 cm.",
    ]),
]
