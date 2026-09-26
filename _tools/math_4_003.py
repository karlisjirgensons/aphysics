# -*- coding: utf-8 -*-
"""4. klase, 3. stunda: «Kā izvēlēties skaitļu taisnes soli?»

Skaitļu taisne līdz 1000 neietilpst burtnīcā ar soli 1. Tāpēc jāizvēlas
iedaļa - 10, 50 vai 100 - un jāsaprot, ka skaitlis starp iedaļām ir tikpat
īsts. Šī prasme vajadzīga diagrammām, mērogam un lineālam.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas,
                         Paraugs, Pasaule, Sakums, Varianti, Zimejums,
                         taisne)

TEMA = "Kā izvēlēties skaitļu taisnes soli?"

MERKIS = ("Izvēlēsimies skaitļu taisnei piemērotu soli un atliksim uz tās "
          "skaitļus līdz 1000.")

SATURS = [
    Sakums("Kā uz vienas lapas ielikt 1000 skaitļu?",
           zimejums=taisne(0, 1000, 100, [(368, "368")]),
           paraksts="Katra iedaļa ir 100 - tad visa taisne ietilpst.",
           fakti=["Ar soli 1 taisne līdz 1000 būtu 10 metrus gara.",
                  "Ar soli 100 tā ietilpst uz lapas.",
                  "Termometrs, lineāls un svari ir tās pašas taisnes."]),

    Doma("Solis ir tas, par cik aug katra nākamā iedaļa",
         "Izvēlies soli tā, lai visi vajadzīgie skaitļi ietilpst un vēl "
         "var saskatīt, kur katrs stāv.",
         soli=[
             "Paskaties, kāds ir lielākais skaitlis, ko vajag atlikt.",
             "Izvēlies ērtu soli: 1, 2, 5, 10, 50 vai 100.",
             "Uzraksti skaitļus pie iedaļām.",
             "Skaitli, kas nav uz iedaļas, noliec starp kaimiņiem.",
         ],
         pieze="650 ar soli 100 atrodas tieši pusē starp 600 un 700."),

    Paraugs("Kur ir 450?",
            uzd="Taisnei ir iedaļas 0, 100, 200, ... 1000. Kur jāatliek 450?",
            soli=[
                ("400 < 450 < 500",
                 "450 ir starp iedaļām 400 un 500."),
                ("450 − 400 = 50",
                 "No 400 līdz 450 ir 50 - puse no soļa."),
                ("Punkts tieši pusē starp 400 un 500", None),
            ],
            atbilde="pusē starp 400 un 500"),

    Kustiba("Aizbrauc līdz skaitlim", [
        {"jaut": "Taisnei solis ir 100. Aizved roveri līdz 700.",
         "atb": 700, "beigas": 1000, "iedala": 100,
         "merkis": "700", "objekts": "Rovers",
         "padoms": "Septītā iedaļa.",
         "stasts": "Rovers apstājas tur, kur tu pateiksi."},
        {"jaut": "Kur ir skaitlis, kas ir tieši pusē starp 200 un 300?",
         "atb": 250, "beigas": 1000, "iedala": 100,
         "merkis": "pusē", "objekts": "Rovers",
         "padoms": "200 + 50."},
        {"jaut": "Solis ir 50. Kura skaitļa iedaļa ir trešā pēc 0?",
         "atb": 150, "beigas": 500, "iedala": 50,
         "merkis": "3. iedaļa", "objekts": "Rovers",
         "padoms": "50 + 50 + 50."},
        {"jaut": "Solis ir 10. Kur ir desmitā iedaļa?",
         "atb": 100, "beigas": 200, "iedala": 10,
         "merkis": "10. iedaļa", "objekts": "Rovers",
         "padoms": "10 · 10."},
    ], pamats=2,
        ievads="Ieraksti skaitli un palaid roveri."),

    Zimejums("Viena taisne, trīs soļi",
             taisne(0, 500, 50, [(150, "150"), (325, "325")],
                    virsraksts="solis 50"),
             paskaidro="325 nav uz iedaļas - tas ir pusē starp 300 un 350.",
             ievads="Solis 50 der, ja lielākais skaitlis ir ap 500."),

    Varianti("Kādu soli izvēlēties?", [
        {"jaut": "Jāatliek 30, 70 un 90. Kāds solis ērtākais?",
         "opcijas": ["10", "1", "100", "500"], "pareizi": 0,
         "padoms": "Visi skaitļi ir pilni desmiti."},
        {"jaut": "Jāatliek 200, 600 un 900. Kāds solis ērtākais?",
         "opcijas": ["100", "1", "10", "1000"], "pareizi": 0,
         "padoms": "Visi ir pilni simti."},
        {"jaut": "Taisnes iedaļas: 0, 50, 100, 150. Kāds ir solis?",
         "opcijas": ["50", "100", "150", "5"], "pareizi": 0,
         "padoms": "Par cik aug katra nākamā iedaļa?"},
        {"jaut": "Solis 100. Kurš skaitlis ir tuvāk 400 nekā 500?",
         "opcijas": ["430", "470", "490", "455"], "pareizi": 0,
         "padoms": "Puse ir 450."},
    ], pamats=4),

    Ievadi("Nolasi no taisnes", [
        {"jaut": "Solis ir 100. Punkts ir pusē starp 800 un 900. Kāds "
                 "skaitlis?", "atb": ["850"], "padoms": "800 + 50."},
        {"jaut": "Solis ir 10. Punkts ir 3 iedaļas aiz 540. Kāds skaitlis?",
         "atb": ["570"], "padoms": "540 + 30."},
        {"jaut": "Solis ir 50. Punkts ir 2 iedaļas pirms 400. Kāds skaitlis?",
         "atb": ["300"], "padoms": "400 − 100."},
        {"jaut": "Cik iedaļu ar soli 50 ir no 0 līdz 1000?",
         "atb": ["20"], "padoms": "1000 : 50."},
    ]),

    Pasaule("Kur Gaujā ir laivu apmetne?",
            Ievadi("", [
                {"jaut": "Laivu maršruts ir 100 km, karte ar soli 10 km. "
                         "Apmetne ir 4. iedaļā. Cik km no starta?",
                 "atb": ["40"], "padoms": "4 · 10."},
                {"jaut": "Pusdienu vieta ir pusē starp 60 un 70 km. Cik km?",
                 "atb": ["65"], "padoms": "60 + 5."},
                {"jaut": "Cik km ir no 40 km apmetnes līdz 65 km pusdienām?",
                 "atb": ["25"], "padoms": "65 − 40."},
                {"jaut": "Cik iedaļu pa 10 km ir visā 100 km maršrutā?",
                 "atb": ["10"], "padoms": "100 : 10."},
            ]),
            pavediens="celojums",
            konteksts="Kartē maršrutu iezīmē ar iedaļām - tieši tā pati "
                      "skaitļu taisne.",
            kapec="Pareizi izvēlēts solis ļauj ar aci nolasīt attālumu."),

    Kopsavilkums([
        "Izvēlos skaitļu taisnei ērtu soli.",
        "Atlieku skaitli, kas atrodas starp iedaļām.",
        "Nolasu skaitli no taisnes, zinot soli.",
    ]),

    Majas([
        "Paskaties uz lineālu, termometru un virtuves svariem. Kāds solis ir "
        "katram?",
        "Uzzīmē taisni no 0 līdz 1000 ar soli 100 un atliec savas mājas "
        "numuru, dzimšanas gadu bez tūkstošiem un 500.",
        "Izdomā skaitli, kuru ir grūti atlikt ar soli 100, un pasaki, kāpēc.",
    ]),
]
