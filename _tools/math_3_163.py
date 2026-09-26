# -*- coding: utf-8 -*-
"""3. klase, 163. stunda: «Kāds taisnstūris vajadzīgs cilindram?»

Cilindra sānu virsma atlokās par taisnstūri - un tā platums ir tieši riņķa
apkārtmērs. Precīzi to rēķināt 3. klasē vēl nevar, bet izmērīt ar auklu -
var, un tieši tas ir stundas praktiskais atklājums.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         kermenis, restis)

TEMA = "Kāds taisnstūris vajadzīgs cilindram?"

MERKIS = ("Piemeklēsim taisnstūri cilindra sānu virsmai un izveidosim "
          "modeli.")

SATURS = [
    Sakums("Kā no plakanas lapas sanāk cilindrs?",
           zimejums=kermenis("cilindrs", virsraksts="cilindrs"),
           paraksts="Sānu virsma ir taisnstūris, satīts caurulē.",
           fakti=["Cilindra sānu virsma atlokās par taisnstūri.",
                  "Taisnstūra platums ir tieši riņķa apkārtmērs."]),

    Doma("Taisnstūra platums ir riņķa apkārtmērs",
         "Lai taisnstūris apliektos ap riņķi bez spraugas un bez pārklāšanās, "
         "tā platumam jābūt tieši tikpat garam, cik riņķa līnijai.",
         soli=[
             "Aptin auklu ap riņķa līniju un izmēri to.",
             "Šis garums būs taisnstūra platums.",
             "Cilindra augstums būs taisnstūra otra mala.",
             "Izgriez taisnstūri un satin to caurulē.",
         ],
         pieze="Ja taisnstūris ir par šauru, paliek sprauga; ja par platu - "
               "malas pārklājas un cilindrs kļūst mazāks."),

    Petijums("Uztaisi cilindru",
             vajag="papīrs, aukla, lineāls, šķēres un līmlente",
             soli=[
                 "Uzzīmē un izgriez divus vienādus riņķus.",
                 "Aptin auklu ap vienu riņķi un izmēri auklas garumu.",
                 "Izgriez taisnstūri ar šo platumu un izvēlētu augstumu.",
                 "Satin taisnstūri un pielīmē abus riņķus.",
             ],
             secinajums="Cilindrs sanāk tikai tad, ja taisnstūra platums "
                        "sakrīt ar riņķa apkārtmēru."),

    Paraugs("Cik plats taisnstūris vajadzīgs?",
            uzd="Riņķa apkārtmērs ir 18 cm, cilindra augstums 10 cm. Kādi "
                "ir taisnstūra izmēri?",
            soli=[
                ("Platums = apkārtmērs = 18 cm",
                 "Tā mala apliecas ap riņķi."),
                ("Augstums = 10 cm",
                 "Otra mala ir cilindra augstums."),
                ("Taisnstūris 18 x 10 cm",
                 "Laukums: 18 · 10 = 180 cm²."),
            ],
            atbilde="18 cm x 10 cm"),

    Ievadi("Cilindra daļas", [
        {"jaut": "Apkārtmērs 18 cm, augstums 10 cm. Cik kvadrātcentimetru "
                 "ir sānu virsmas laukums?",
         "atb": ["180"], "padoms": "18 · 10."},
        {"jaut": "Apkārtmērs 25 cm, augstums 8 cm. Cik ir sānu laukums?",
         "atb": ["200"], "padoms": "25 · 8."},
        {"jaut": "Cik plakanu skaldņu ir cilindram?", "atb": ["2"],
         "padoms": "Augšējais un apakšējais riņķis."},
        {"jaut": "Cik riņķu vajag vienam cilindram?", "atb": ["2"],
         "padoms": "Augša un apakša."},
        {"jaut": "Cik riņķu vajag 6 cilindriem?", "atb": ["12"],
         "padoms": "6 · 2."},
        {"jaut": "Apkārtmērs 30 cm, augstums 12 cm. Cik ir sānu laukums?",
         "atb": ["360"], "padoms": "30 · 12."},
    ], pamats=4),

    Zimejums("Cilindra trīs daļas",
             restis([["daļa", "forma", "skaits"],
                     ["sāni", "taisnstūris", 1],
                     ["augša", "riņķis", 1],
                     ["apakša", "riņķis", 1]],
                    "cilindra izklājums"),
             paskaidro="Cilindra izklājumā ir viens taisnstūris un divi "
                       "vienādi riņķi.",
             ievads="Trīs daļas, no kurām saliek cilindru."),

    Varianti("Kas vajadzīgs cilindram?", [
        {"jaut": "Kāda forma ir cilindra sānu virsmai, to atlokot?",
         "opcijas": ["Taisnstūris", "Riņķis", "Trīsstūris", "Kvadrāts"],
         "pareizi": 0, "padoms": "To var satīt caurulē."},
        {"jaut": "Kam jābūt vienādam ar taisnstūra platumu?",
         "opcijas": ["Riņķa apkārtmēram", "Riņķa rādiusam",
                     "Cilindra augstumam", "Nekam"],
         "pareizi": 0, "padoms": "Tā mala apliecas ap riņķi."},
        {"jaut": "Cik riņķu ir cilindra izklājumā?",
         "opcijas": ["2", "1", "4", "0"],
         "pareizi": 0, "padoms": "Augša un apakša."},
        {"jaut": "Kas notiek, ja taisnstūris ir par šauru?",
         "opcijas": ["Paliek sprauga", "Malas pārklājas",
                     "Cilindrs kļūst augstāks", "Nekas"],
         "pareizi": 0, "padoms": "Tas neapliecas līdz galam."},
    ], pamats=4),

    Pasaule("Cik papīra vajag etiķetei?",
            Ievadi("", [
                {"jaut": "Bundžas apkārtmērs 25 cm, augstums 12 cm. Cik "
                         "kvadrātcentimetru ir etiķete?",
                 "atb": ["300"], "padoms": "25 · 12."},
                {"jaut": "Cik kvadrātcentimetru vajag 10 etiķetēm?",
                 "atb": ["3000"], "padoms": "10 · 300."},
                {"jaut": "Etiķetes pārklājas par 1 cm. Cik plata ir īstā "
                         "etiķete?",
                 "atb": ["26"], "padoms": "25 + 1."},
                {"jaut": "Cik kvadrātcentimetru tad ir viena etiķete?",
                 "atb": ["312"], "padoms": "26 · 12."},
            ]),
            pavediens="veikals",
            konteksts="Konservu bundžas etiķete ir tieši tāds pats "
                      "taisnstūris - tikai ar nelielu pārlaidumu līmēšanai.",
            kapec="Bez pārlaiduma etiķete neturētos kopā."),

    Kopsavilkums([
        "Zinu, ka cilindra sānu virsma ir taisnstūris.",
        "Zinu, ka tā platums ir riņķa apkārtmērs.",
        "Izmēru apkārtmēru ar auklu.",
        "Izveidoju cilindra modeli no trim daļām.",
    ]),

    Majas([
        "Aptin auklu ap glāzi un izmēri tās apkārtmēru.",
        "Izgriez taisnstūri un uztaisi cilindru.",
        "Izrēķini tā sānu virsmas laukumu.",
    ]),
]
