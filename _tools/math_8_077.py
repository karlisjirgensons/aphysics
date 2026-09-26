# -*- coding: utf-8 -*-
"""8. klase, 77. stunda: «Kā zīmē cilindru?»

Cilindra elementi: divi vienādi riņķa pamati, augstums (ass), veidule.
Zīmējumā riņķi kļūst par elipsēm, apakšējās elipses aizmugure ir punktēta.
Cilindrs rodas, griežot taisnstūri ap malu - to var pētīt GeoGebra 3D.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, kermenis)

TEMA = "Kā zīmē cilindru?"

MERKIS = ("Zīmēsim cilindru, arī ar digitāliem rīkiem, un raksturosim tā "
          "elementus.")

SATURS = [
    Sakums("Kā uzzīmēt bundžu?",
           zimejums=kermenis("cilindrs"),
           paraksts="Pamati - vienādi riņķi, sānu virsma - izliekta.",
           fakti=["Cilindram ir divi vienādi riņķa pamati.",
                  "Augstums h ir attālums starp pamatiem.",
                  "Zīmējumā riņķi izskatās kā elipses."]),

    Doma("Cilindra elementi",
         "Cilindrs rodas, griežot taisnstūri ap vienu tā malu.",
         soli=[
             "Pamata rādiuss r un diametrs d = 2r.",
             "Ass - nogrieznis starp pamatu centriem; tā garums ir h.",
             "Veidule - sānu virsmas nogrieznis, paralēls asij; arī tā "
             "garums ir h.",
             "Zīmē: augšējā elipse, divas veidules, apakšējā elipse ar "
             "punktētu aizmuguri.",
         ],
         pieze="Digitālā rīkā (piemēram, GeoGebra 3D) cilindru var pagriezt "
               "un apskatīt no visām pusēm."),

    Paraugs("Uzzīmē cilindru",
            uzd="Uzzīmē cilindru ar r = 2 cm un h = 5 cm.",
            soli=[
                ("Elipse ar platumu 4 cm", "Augšējais pamats: platums = d."),
                ("Divas vertikālas līnijas pa 5 cm", "Veidules."),
                ("Apakšējā elipse", "Priekšpuse vesela, aizmugure "
                                    "punktēta."),
                ("Atzīmē r un h", "Izmēri."),
            ],
            atbilde="Cilindrs ar d = 4 cm un h = 5 cm"),

    Ievadi("Aprēķini", [
        {"jaut": "Cilindra diametrs ir 10 cm. Rādiuss (cm)?", "atb": ["5"],
         "padoms": "{10|2}."},
        {"jaut": "Veidule ir 7 cm. Augstums (cm)?", "atb": ["7"],
         "padoms": "Veidule = h."},
        {"jaut": "r = 3 cm. Pamata riņķa līnijas garums (cm, π ≈ 3,14)?",
         "atb": ["18,84"], "padoms": "2 · 3,14 · 3."},
        {"jaut": "Cik pamatu ir cilindram?", "atb": ["2"],
         "padoms": "Augšā un apakšā."},
    ]),

    Varianti("Spried", [
        {"jaut": "Kas rodas, griežot taisnstūri ap vienu malu?",
         "opcijas": ["Cilindrs", "Konuss", "Lode", "Prizma"],
         "pareizi": 0, "padoms": "Mala kļūst par asi."},
        {"jaut": "Cilindra griezums paralēli pamatam ir...",
         "opcijas": ["riņķis", "taisnstūris", "trijstūris", "kvadrāts"],
         "pareizi": 0, "padoms": "Tāds pats kā pamats."},
        {"jaut": "Cilindra griezums caur asi ir...",
         "opcijas": ["taisnstūris d × h", "riņķis", "trijstūris",
                     "elipse"],
         "pareizi": 0, "padoms": "Divas veidules un divi diametri."},
    ]),

    Pasaule("Konservu bundža",
            Ievadi("", [
                {"jaut": "Bundžas diametrs ir 8 cm, augstums - 11 cm. "
                         "Rādiuss (cm)?",
                 "atb": ["4"], "padoms": "{8|2}."},
                {"jaut": "Cik cm gara ir etiķete ap bundžu (π ≈ 3,14, līdz "
                         "desmitdaļām)?",
                 "atb": ["25,1"], "padoms": "3,14 · 8 = 25,12."},
                {"jaut": "Etiķete klāj visu sānu virsmu. Tās platums (cm)?",
                 "atb": ["11"], "padoms": "Platums = h."},
            ]),
            pavediens="virtuve",
            konteksts="Bundža ir cilindrs; etiķete ir tā sānu virsma, "
                      "atritināta taisnstūrī.",
            kapec="Etiķetes garums ir pamata riņķa līnijas garums."),

    Kopsavilkums([
        "Nosaucu cilindra elementus: pamatus, asi, veiduli.",
        "Zīmēju cilindru ar punktētu neredzamo daļu.",
        "Saistu etiķetes garumu ar riņķa līnijas garumu.",
    ]),

    Majas([
        "Uzzīmē krūzi vai bundžu kā cilindru un atzīmē r un h.",
        "GeoGebra 3D uzzīmē cilindru un pagriez to.",
        "Izmēri bundžu un aprēķini etiķetes izmērus.",
    ]),
]
