# -*- coding: utf-8 -*-
"""7. klase, 108. stunda: «Kā konstruēt trijstūri pēc dotiem lielumiem?»

Trīs konstrukcijas atbilst trim vienādības pazīmēm: pēc trim malām (mmm),
pēc divām malām un leņķa starp tām (mlm), pēc malas un pieleņķiem (lml).
Stunda apvieno iepriekš apgūtās konstrukcijas un pārbauda, kad konstrukcija
nav iespējama.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Petijums, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā konstruēt trijstūri pēc dotiem lielumiem?"

MERKIS = ("Ar cirkuli un lineālu konstruēsim trijstūrus atbilstoši "
          "dotiem elementiem.")

SATURS = [
    Sakums("Trīs dati - viens trijstūris",
           zimejums=restis([["dots", "konstrukcija"],
                            ["3 malas", "nogrieznis + 2 loki"],
                            ["2 malas + leņķis starp", "leņķis + 2 malas"],
                            ["mala + 2 pieleņķi", "nogrieznis + 2 leņķi"]]),
           fakti=["Katrai vienādības pazīmei - sava konstrukcija.",
                  "Konstrukcija parāda, ka trijstūris ir tikai viens."]),

    Doma("Konstrukciju plāns",
         "Konstrukciju sāk ar vienu zināmu nogriezni vai leņķi un pievieno "
         "pārējos elementus ar cirkuli un lineālu. Pirms tam pārbauda, vai "
         "trijstūris vispār eksistē.",
         soli=[
             "mmm: pārbaudi trijstūra nevienādību; atliec vienu malu, no "
             "galiem - loki.",
             "mlm: konstruē leņķi, uz malām atliec abas malas, savieno.",
             "lml: atliec malu, pie galiem konstruē leņķus, krustpunkts.",
             "lml: pārbaudi, vai leņķu summa ir mazāka par 180°.",
         ],
         pieze="Ja loki nekrustojas vai stari nekrustojas - trijstūris ar "
               "šiem datiem neeksistē."),

    Paraugs("Pēc malas un pieleņķiem",
            uzd="Konstruē trijstūri: AB = 6 cm, ∠A = 45°, ∠B = 60°.",
            soli=[
                ("45° + 60° = 105° < 180°", "Eksistē."),
                ("Atliek AB = 6 cm", "Lineāls un cirkulis."),
                ("Pie A konstruē 45°: 90° bisektrise", "(89. stunda)"),
                ("Pie B konstruē 60°: vienādmalu trijstūra leņķis",
                 "Loki ar rādiusu AB."),
                ("Stari krustojas punktā C", "Gatavs."),
            ],
            atbilde="△ABC - viens (līdz ar spoguļattēlu)."),

    Varianti("Vai var konstruēt?", [
        {"jaut": "Malas 3, 4, 8 cm",
         "opcijas": ["Nē", "Jā"], "pareizi": 0, "jaukt": False,
         "padoms": "3 + 4 < 8."},
        {"jaut": "Mala 5 cm, pieleņķi 100° un 90°",
         "opcijas": ["Nē", "Jā"], "pareizi": 0, "jaukt": False,
         "padoms": "Summa > 180°."},
        {"jaut": "Malas 5 un 7 cm, leņķis starp tām 150°",
         "opcijas": ["Jā", "Nē"], "pareizi": 0, "jaukt": False,
         "padoms": "Jebkurš leņķis līdz 180° der."},
        {"jaut": "Kādu leņķi var konstruēt bez transportiera?",
         "opcijas": ["60° (vienādmalu trijstūris)", "37°", "71°", "13°"],
         "pareizi": 0, "padoms": "Loki ar vienādu rādiusu."},
    ], pamats=4),

    Petijums("Konstruē trīs trijstūrus",
             ["mmm: malas 5, 6, 7 cm.",
              "mlm: malas 5 un 6 cm, leņķis starp tām 60°.",
              "lml: mala 6 cm, pieleņķi 45° un 60°.",
              "Izmēri trūkstošos elementus un salīdzini ar klasesbiedru."],
             vajag="cirkulis, lineāls, zīmulis",
             secinajums="Visiem klasē trijstūri sakrīt - konstrukcija dod "
                         "vienu trijstūri."),

    Zimejums("Kā konstruē 60° un 45°",
             restis([["60°", "vienādmalu trijstūris: loki ar rādiusu AB"],
                     ["90°", "perpendikuls (90. stunda)"],
                     ["45°", "90° bisektrise"],
                     ["30°", "60° bisektrise"]]),
             paskaidro="Tikai cirkulis un lineāls."),

    Pasaule("Mērnieks laukā",
            Varianti("", [
                {"jaut": "Mērniekam jāatliek trijstūrveida gabals ar malām "
                         "30 m, 40 m, 50 m. Kā to izdarīt ar divām virvēm?",
                 "opcijas": ["Kā mmm konstrukcija: virves kā loki no "
                             "galiem",
                             "Uz aci", "Ar kompasu", "Nevar"],
                 "pareizi": 0, "padoms": "Virve = cirkulis."},
                {"jaut": "Kāds ir šis trijstūris (30, 40, 50)?",
                 "opcijas": ["Taisnleņķa", "Vienādsānu", "Platleņķa",
                             "Vienādmalu"],
                 "pareizi": 0,
                 "padoms": "Seno ēģiptiešu «virvju» taisnais leņķis "
                           "(3 : 4 : 5)."},
                {"jaut": "Kāpēc ēģiptieši to lietoja?",
                 "opcijas": ["Lai iegūtu taisnu leņķi celtnēm",
                             "Lai mērītu upes", "Rotājumiem",
                             "Spēlēm"],
                 "pareizi": 0, "padoms": "Piramīdu stūri."},
            ]),
            pavediens="maja",
            konteksts="Senajā Ēģiptē ar virvi ar 12 mezgliem veidoja "
                      "trijstūri 3 : 4 : 5 un ieguva taisnu leņķi.",
            kapec="Konstrukcija ar virvi = konstrukcija ar cirkuli."),

    Kopsavilkums([
        "Konstruēju trijstūri pēc mmm, mlm un lml.",
        "Pārbaudu, vai trijstūris eksistē.",
        "Konstruēju 60°, 90°, 45° un 30° bez transportiera.",
        "Saistu konstrukcijas ar vienādības pazīmēm.",
    ]),

    Majas([
        "Konstruē trijstūri 3, 4, 5 cm un izmēri lielāko leņķi.",
        "Konstruē vienādsānu trijstūri ar sānu 5 cm un virsotnes leņķi 30°.",
        "Izveido virvi ar 12 mezgliem un iegūsti taisnu leņķi.",
    ]),
]
