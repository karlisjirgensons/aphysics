# -*- coding: utf-8 -*-
"""7. klase, 30. stunda: «Kā aprēķina nogriežņa garumu?»

Ja punkts atrodas uz nogriežņa, tas sadala nogriezni divās daļās, un
garumi saskaitās: AC = AB + BC. No tā var izrēķināt jebkuru no trim
garumiem - tā ir pirmā ģeometrijas «formula», ko lieto pierādījumos.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas,
                         Paraugs, Pasaule, Sakums, Varianti, Zimejums,
                         geometrija)

TEMA = "Kā aprēķina nogriežņa garumu?"

MERKIS = ("Aprēķināsim nogriežņa garumu kā citu nogriežņu garumu summu vai "
          "starpību.")

_ABC = geometrija([("A", 0, 0), ("B", 5, 0), ("C", 8, 0)],
                  nogriezni=["AC"], malas=[("AB", "5 cm"), ("BC", "3 cm")])

SATURS = [
    Sakums("Rīga - Sigulda - Cēsis",
           zimejums=_ABC,
           paraksts="AC = AB + BC = 5 cm + 3 cm = 8 cm",
           fakti=["Ja Sigulda ir uz ceļa, ceļš Rīga-Cēsis ir divu posmu "
                  "summa.",
                  "Zinot kopējo garumu un vienu posmu, atrod otru."]),

    Doma("Daļas kopā ir viss",
         "Ja punkts B atrodas uz nogriežņa AC, tad AC = AB + BC. No tā "
         "izriet arī AB = AC − BC un BC = AC − AB.",
         soli=[
             "Uzzīmē skici un atzīmē zināmos garumus.",
             "Nosaki, kurš nogrieznis ir viss un kuri - daļas.",
             "Uzraksti vienādību: viss = daļa + daļa.",
             "Ievieto skaitļus un aprēķini.",
         ],
         pieze="Ja punktu secība nav dota, var būt vairāki gadījumi - "
               "katram vajag savu skici."),

    Paraugs("Divi gadījumi",
            uzd="Uz taisnes atzīmēti punkti A, B, C. AB = 7 cm, BC = 3 cm. "
                "Cik garš var būt AC?",
            soli=[
                ("1. gadījums: B ir starp A un C", "Uzzīmē skici."),
                ("AC = AB + BC = 7 + 3 = 10 (cm)", "Daļas saskaita."),
                ("2. gadījums: C ir starp A un B", "Cita skice."),
                ("AC = AB − BC = 7 − 3 = 4 (cm)", "AB ir viss."),
            ],
            atbilde="AC = 10 cm vai AC = 4 cm"),

    Zimejums("Otrs gadījums: C starp A un B",
             geometrija([("A", 0, 0), ("C", 4, 0), ("B", 7, 0)],
                        nogriezni=["AB"],
                        malas=[("AC", "?"), ("CB", "3 cm")]),
             paskaidro="Tagad viss ir AB = 7 cm, un AC = 7 − 3 = 4 (cm)."),

    Ievadi("Aprēķini", [
        {"jaut": "B ∈ AC, AB = 4,5 cm, BC = 2,7 cm. Cik cm ir AC?",
         "atb": ["7,2"], "padoms": "4,5 + 2,7."},
        {"jaut": "B ∈ AC, AC = 12 cm, AB = 8,4 cm. Cik cm ir BC?",
         "atb": ["3,6"], "padoms": "12 − 8,4."},
        {"jaut": "Punkti A, B, C, D uz taisnes šādā secībā. AB = 2, BC = 3, "
                 "CD = 4 (cm). Cik cm ir AD?",
         "atb": ["9"], "padoms": "2 + 3 + 4."},
        {"jaut": "Tajā pašā zīmējumā - cik cm ir BD?",
         "atb": ["7"], "padoms": "3 + 4."},
        {"jaut": "B ∈ AC, AB ir 3 reizes garāks par BC, AC = 20 cm. Cik "
                 "cm ir BC?",
         "atb": ["5"], "padoms": "4 daļas = 20 cm."},
        {"jaut": "B ∈ AC, AB par 4 cm garāks nekā BC, AC = 16 cm. Cik cm "
                 "ir AB?",
         "atb": ["10"], "padoms": "BC = (16 − 4) : 2 = 6."},
    ], pamats=4),

    Pasaule("Kur ir autobuss?",
            Kustiba("", [
                {"jaut": "No Rīgas līdz Cēsīm ir 90 km. Autobuss ir 38 km "
                         "no Cēsīm. Cik km tas ir no Rīgas?",
                 "atb": 52, "beigas": 90, "iedala": 10, "mers": "km",
                 "merkis": "autobuss", "objekts": "Autobuss",
                 "padoms": "90 − 38."},
                {"jaut": "Sigulda ir 53 km no Rīgas. Cik km no Siguldas "
                         "līdz Cēsīm? (Brauc līdz šim attālumam no 0.)",
                 "atb": 37, "beigas": 90, "iedala": 10, "mers": "km",
                 "merkis": "Cēsis no Siguldas", "objekts": "Auto",
                 "padoms": "90 − 53."},
            ]),
            pavediens="celojums",
            konteksts="Ceļa zīmes rāda attālumu līdz pilsētām - un tie ir "
                      "nogriežņu garumi uz viena ceļa.",
            kapec="Kopējais ceļš = posms + posms."),

    Varianti("Kurš spriedums pareizs?", [
        {"jaut": "AB = 5 cm, BC = 5 cm. Vai AC noteikti ir 10 cm?",
         "opcijas": ["Nē - punkti var nebūt uz vienas taisnes vai C var "
                     "sakrist ar A",
                     "Jā, vienmēr", "Jā, ja B ir vidū", "AC = 0 vienmēr"],
         "pareizi": 0,
         "padoms": "Vajag zināt, ka B ir starp A un C."},
        {"jaut": "B ∈ AC. Kurš nogrieznis ir garākais?",
         "opcijas": ["AC", "AB", "BC", "Nevar zināt"],
         "pareizi": 0,
         "padoms": "Viss ir garāks par daļu."},
    ]),

    Kopsavilkums([
        "Lietoju AC = AB + BC, ja B atrodas uz AC.",
        "Izsaku daļu kā starpību: AB = AC − BC.",
        "Zīmēju skici katram iespējamam gadījumam.",
        "Rakstu mērvienību pie atbildes.",
    ]),

    Majas([
        "Uzraksti uzdevumu ar diviem gadījumiem un atrisini to.",
        "Izmēri ceļu no mājām līdz skolai kartē pa posmiem.",
        "A, B, C, D uz taisnes; AC = 9, BD = 8, AD = 12. Atrodi BC.",
    ]),
]
