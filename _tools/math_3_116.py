# -*- coding: utf-8 -*-
"""3. klase, 116. stunda: «Kurš laukums ir lielāks?»

Divi salīdzināšanas veidi: uzlikt figūras vienu uz otras vai izrēķināt
laukumus. Pirmais der tad, kad figūras ir rokā; otrais - vienmēr. Skolēns
mācās izvēlēties, kurš no tiem der konkrētajā situācijā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         kolonnas)

TEMA = "Kurš laukums ir lielāks?"

MERKIS = ("Salīdzināsim laukumus, figūras uzliekot vienu uz otras vai "
          "aprēķinot.")

SATURS = [
    Sakums("Kurš paklājs ir lielāks?",
           zimejums=kolonnas([("6 x 4", 24), ("5 x 5", 25)], " cm²"),
           paraksts="Ar aci to nepateikt - atšķirība ir tikai viens "
                    "kvadrātcentimetrs.",
           fakti=["Laukumus var salīdzināt, figūras uzliekot vienu uz otras.",
                  "Ja tas nav iespējams, laukumus izrēķina."]),

    Doma("Ja nevar uzlikt - izrēķini",
         "Uzlikšana der maziem gabaliem; lielām figūrām paliek tikai rēķins.",
         soli=[
             "Ja figūras var uzlikt vienu uz otras, izdari to.",
             "Ja nē, izmēri abu malas.",
             "Izrēķini abus laukumus.",
             "Salīdzini iegūtos skaitļus.",
         ],
         pieze="Lielāks perimetrs nenozīmē lielāku laukumu: taisnstūrim "
               "6 x 4 perimetrs ir 20 un laukums 24, bet 5 x 5 - perimetrs "
               "20 un laukums 25."),

    Paraugs("Kurš taisnstūris ir lielāks?",
            uzd="Salīdzini taisnstūrus 6 x 4 cm un 5 x 5 cm.",
            soli=[
                ("6 · 4 = 24 cm²",
                 "Pirmā laukums."),
                ("5 · 5 = 25 cm²",
                 "Otrā laukums."),
                ("24 < 25",
                 "Otrais ir lielāks, kaut perimetri ir vienādi."),
            ],
            atbilde="kvadrāts 5 x 5"),

    Petijums("Salīdzini divas figūras",
             vajag="rūtiņu lapa, šķēres un zīmulis",
             soli=[
                 "Izgriez taisnstūri 6 x 4 rūtiņas.",
                 "Izgriez kvadrātu 5 x 5 rūtiņas.",
                 "Uzliec vienu uz otra un paskaties, kurš ir lielāks.",
                 "Saskaiti rūtiņas abos un pārbaudi.",
             ],
             secinajums="Uzlikšana parāda atbildi, bet skaitīšana to "
                        "pierāda - un abas reizes atbilde ir tā pati."),

    Ievadi("Salīdzini laukumus", [
        {"jaut": "Taisnstūris 6 x 4. Cik ir laukums?", "atb": ["24"],
         "padoms": "6 · 4."},
        {"jaut": "Kvadrāts 5 x 5. Cik ir laukums?", "atb": ["25"],
         "padoms": "5 · 5."},
        {"jaut": "Par cik kvadrātvienībām otrais ir lielāks?",
         "atb": ["1"], "padoms": "25 − 24."},
        {"jaut": "Taisnstūris 8 x 3. Cik ir laukums?", "atb": ["24"],
         "padoms": "8 · 3."},
        {"jaut": "Taisnstūris 7 x 4. Cik ir laukums?", "atb": ["28"],
         "padoms": "7 · 4."},
        {"jaut": "Par cik 7 x 4 ir lielāks nekā 8 x 3?", "atb": ["4"],
         "padoms": "28 − 24."},
    ], pamats=4),

    Zimejums("Vienāds perimetrs, dažāds laukums",
             kolonnas([("9 x 1", 9), ("7 x 3", 21), ("5 x 5", 25)], " cm²"),
             paskaidro="Visiem trim perimetrs ir 20 cm, bet laukumi ir "
                       "pavisam dažādi.",
             ievads="Trīs taisnstūri ar vienādu perimetru."),

    Varianti("Kurš ir lielāks?", [
        {"jaut": "Kuram taisnstūrim laukums ir lielākais?",
         "opcijas": ["5 x 5", "6 x 4", "8 x 3", "9 x 1"],
         "pareizi": 0, "padoms": "25, 24, 24 un 9."},
        {"jaut": "Vai lielāks perimetrs nozīmē lielāku laukumu?",
         "opcijas": ["Nē", "Jā", "Tikai kvadrātiem", "Vienmēr"],
         "pareizi": 0, "padoms": "5 x 5 un 9 x 1 perimetri vienādi."},
        {"jaut": "Kad figūras var salīdzināt, tās uzliekot?",
         "opcijas": ["Kad tās ir rokā", "Vienmēr", "Nekad",
                     "Tikai taisnstūrus"],
         "pareizi": 0, "padoms": "Lielas figūras uzlikt nevar."},
        {"jaut": "Taisnstūris 10 x 2. Cik ir laukums?",
         "opcijas": ["20", "24", "12", "40"],
         "pareizi": 0, "padoms": "10 · 2."},
    ], pamats=4),

    Pasaule("Kurš paklājs der istabai?",
            Ievadi("", [
                {"jaut": "Istaba ir 4 m un 3 m. Cik kvadrātmetru ir grīda?",
                 "atb": ["12"], "padoms": "4 · 3."},
                {"jaut": "Paklājs ir 3 m un 2 m. Cik kvadrātmetru?",
                 "atb": ["6"], "padoms": "3 · 2."},
                {"jaut": "Cik kvadrātmetru grīdas paliks neklātas?",
                 "atb": ["6"], "padoms": "12 − 6."},
                {"jaut": "Otrs paklājs ir 4 m un 2 m. Cik kvadrātmetru?",
                 "atb": ["8"], "padoms": "4 · 2."},
            ]),
            pavediens="maja",
            konteksts="Paklāju izvēlas pēc laukuma, bet tam jāietilpst arī "
                      "pēc garuma un platuma.",
            kapec="Vienāds laukums vēl nenozīmē, ka paklājs ietilps."),

    Kopsavilkums([
        "Salīdzinu laukumus, figūras uzliekot vienu uz otras.",
        "Salīdzinu laukumus, tos aprēķinot.",
        "Zinu, ka vienāds perimetrs nenozīmē vienādu laukumu.",
        "Izvēlos piemērotāko salīdzināšanas veidu.",
    ]),

    Majas([
        "Salīdzini divu mājas priekšmetu virsmas laukumus.",
        "Izrēķini abus laukumus un pārbaudi savu spriedumu.",
        "Atrodi divas figūras ar vienādu perimetru un dažādu laukumu.",
    ]),
]
