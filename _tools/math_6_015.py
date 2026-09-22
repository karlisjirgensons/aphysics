# -*- coding: utf-8 -*-
"""6. klase, 15. stunda: «Ko nozīmē mērogs 1 : 500?»

Mērogs ir attiecība, kurai viena puse ir papīrs, otra - pasaule. Stunda
vingrina abus virzienus: no kartes uz dabu un no dabas uz karti. Kustīgs
objekts te ir īstajā vietā - kartē nogrieztais gabals kļūst par īstu ceļu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Ko nozīmē mērogs 1 : 500?"

MERKIS = ("Iemācīsimies aprēķināt attālumu dabā, ja dots mērogs un attālums "
          "kartē, un otrādi.")

SATURS = [
    Sakums("Visa pilsēta ietilpst kabatā",
           fakti=["Mērogs 1 : 500 nozīmē: 1 cm kartē ir 500 cm dabā.",
                  "500 cm ir 5 m - tātad 1 cm kartē ir 5 m dabā.",
                  "Jo lielāks otrais skaitlis, jo sīkāka karte."]),

    Doma("Mērogs ir reizinātājs",
         "Attālumu dabā iegūst, kartes attālumu reizinot ar mēroga otro "
         "skaitli; pretējā virzienā - dalot.",
         soli=[
             "Pieraksti mērogu kā 1 : n.",
             "No kartes uz dabu: reizini kartes attālumu ar n.",
             "No dabas uz karti: dali dabas attālumu ar n.",
             "Pārvērt rezultātu ērtā mērvienībā - metros vai kilometros.",
             "Pārbaudi, vai atbilde ir ticama pēc lieluma.",
         ],
         pieze="Vienmēr abi attālumi vispirms ir vienā mērvienībā. 4 cm pie "
               "mēroga 1 : 500 dod 2000 cm, un tikai tad to raksta kā 20 m."),

    Paraugs("No kartes uz dabu",
            uzd="Kartē ar mērogu 1 : 500 divas mājas ir 7 cm attālumā. Cik "
                "metru tas ir dabā?",
            soli=[
                ("7 · 500 = 3500 cm",
                 "Kartes attālumu reizina ar mēroga skaitli."),
                ("3500 cm = 35 m",
                 "100 cm ir 1 m, tāpēc dala ar 100."),
                ("Pārbaude: 1 cm ir 5 m, tātad 7 cm ir 35 m",
                 "Tas pats rezultāts citā ceļā."),
            ],
            atbilde="35 m"),

    Ievadi("Mērogs abos virzienos", [
        {"jaut": "Mērogs 1 : 100. Cik centimetru dabā ir 3 cm kartē?",
         "atb": ["300"], "padoms": "3 · 100."},
        {"jaut": "Mērogs 1 : 500. Cik metru dabā ir 4 cm kartē?",
         "atb": ["20"], "padoms": "4 · 500 = 2000 cm = 20 m."},
        {"jaut": "Mērogs 1 : 1000. Cik metru dabā ir 6 cm kartē?",
         "atb": ["60"], "padoms": "6000 cm = 60 m."},
        {"jaut": "Mērogs 1 : 200. Istaba dabā ir 8 m. Cik cm tā ir plānā?",
         "atb": ["4"], "padoms": "800 cm : 200."},
        {"jaut": "Mērogs 1 : 25 000. Cik kilometru dabā ir 4 cm kartē?",
         "atb": ["1"], "padoms": "100 000 cm = 1 km."},
        {"jaut": "Mērogs 1 : 50. Detaļa dabā ir 150 cm. Cik cm ir zīmējumā?",
         "atb": ["3"], "padoms": "150 : 50."},
    ], pamats=4,
        ievads="Uz dabu - reizina; uz karti - dala."),

    Pasaule("Cik tālu tiešām ir mērķis?",
            Kustiba("", [
                {"jaut": "Kartē mērogā 1 : 1000 mērķis ir 5 cm attālumā. Cik "
                         "metru tas ir dabā?",
                 "atb": 50, "beigas": 100, "iedala": 20, "mers": "metri",
                 "merkis": "mērķis", "objekts": "Rovers",
                 "padoms": "5 · 1000 = 5000 cm = 50 m."},
                {"jaut": "Tā pati karte, mērķis 8 cm attālumā. Cik metru?",
                 "atb": 80, "beigas": 100, "iedala": 20, "mers": "metri",
                 "merkis": "mērķis", "objekts": "Rovers",
                 "padoms": "8000 cm = 80 m."},
                {"jaut": "Karte mērogā 1 : 500, mērķis 6 cm. Cik metru?",
                 "atb": 30, "beigas": 50, "iedala": 10, "mers": "metri",
                 "merkis": "mērķis", "objekts": "Rovers",
                 "padoms": "6 · 500 = 3000 cm = 30 m."},
                {"jaut": "Karte mērogā 1 : 2000, mērķis 2 cm. Cik metru?",
                 "atb": 40, "beigas": 50, "iedala": 10, "mers": "metri",
                 "merkis": "mērķis", "objekts": "Rovers",
                 "padoms": "2 · 2000 = 4000 cm = 40 m."},
            ]),
            pavediens="tehnika",
            konteksts="Roveram uz Marsa karte ir vienīgais ceļvedis - tas "
                      "aizbrauc tieši tik tālu, cik pateicis aprēķins.",
            kapec="Kļūdains mērogs nozīmē, ka mašīna apstājas nepareizā "
                  "vietā."),

    Varianti("Kura karte ir sīkāka?", [
        {"jaut": "Mērogs 1 : 100 vai 1 : 10 000 - kurā redz vairāk "
                 "sīkumu?",
         "opcijas": ["1 : 100", "1 : 10 000", "Abās vienādi",
                     "Nevar salīdzināt"],
         "pareizi": 0,
         "padoms": "Mazāks otrais skaitlis - lielāks palielinājums."},
        {"jaut": "Mērogā 1 : 500 viens centimetrs ir...",
         "opcijas": ["5 m", "500 m", "50 cm", "5 km"],
         "pareizi": 0,
         "padoms": "500 cm ir 5 m."},
        {"jaut": "Plānā istaba ir 5 cm, dabā 10 m. Kāds ir mērogs?",
         "opcijas": ["1 : 200", "1 : 50", "1 : 2", "1 : 1000"],
         "pareizi": 0,
         "padoms": "1000 cm : 5 cm."},
        {"jaut": "Kāpēc mērogā abi skaitļi ir bez mērvienībām?",
         "opcijas": ["Tā ir attiecība starp vienādiem lielumiem",
                     "Mērvienības aizmirsa pierakstīt",
                     "Tās vienmēr ir centimetri",
                     "Mērogs nav attiecība"],
         "pareizi": 0,
         "padoms": "Attiecību veido divi viena veida lielumi."},
    ], pamats=4),

    Kopsavilkums([
        "Izlasu mērogu un pasaku, cik dabā ir viens centimetrs kartē.",
        "Aprēķinu attālumu dabā, reizinot kartes attālumu ar mērogu.",
        "Aprēķinu attālumu kartē, dalot dabas attālumu ar mērogu.",
        "Pārvēršu rezultātu ērtākajā mērvienībā.",
    ]),

    Majas([
        "Atrodi karti telefonā un noskaidro, kāds ir tās mērogs.",
        "Izmēri savu istabu un izrēķini, cik cm tā būtu plānā 1 : 100.",
        "Izdomā, kāds mērogs vajadzīgs, lai visa Latvija ietilptu A4 lapā.",
    ]),
]
