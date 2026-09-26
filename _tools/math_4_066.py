# -*- coding: utf-8 -*-
"""4. klase, 66. stunda: «Kā uzzīmēt trijstūri pēc nosacījumiem?»

Dots leņķis un divu malu garumi - trijstūris ir noteikts viennozīmīgi.
Kārtība: vispirms leņķis ar transportieri, tad uz malām atliek garumus ar
lineālu, tad savieno galus. Leņķu summu trijstūrī 4. klasē vēl neapskata.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Slidnis, Varianti,
                         lenkis)

TEMA = "Kā uzzīmēt trijstūri pēc nosacījumiem?"

MERKIS = ("Zīmēsim trijstūri, ja dots leņķa lielums un divu malu garumi.")

SATURS = [
    Sakums("Kā uzbūvēt jumta kopni?",
           zimejums=lenkis([(0, "B"), (50, "C")], loki=[(0, 50, "50°")]),
           paraksts="Leņķis A = 50°, AB = 6 m, AC = 5 m - atliek savienot B "
                    "un C.",
           fakti=["Jumta kopnes ir trijstūri - tie nesaliecas.",
                  "Galdnieks zina leņķi un divus garumus - ar to pietiek."]),

    Doma("Leņķis, divas malas, savieno",
         "Ja zināms leņķis un abu tā malu garumi, trijstūri var uzzīmēt tikai "
         "vienā veidā.",
         soli=[
             "Uzzīmē leņķi A ar transportieri.",
             "Uz vienas malas ar lineālu atliec AB.",
             "Uz otras malas atliec AC.",
             "Savieno B un C - trijstūris gatavs.",
         ],
         pieze="Trešo malu BC nevar izvēlēties - tā sanāk pati. To var "
               "izmērīt."),

    Slidnis("Zīmējam trijstūri",
            soli=[
                {"v": "1. leņķis A = 50°",
                 "teksts": "Transportieris virsotnē A.",
                 "zim": lenkis([(0, ""), (50, "")], loki=[(0, 50, "50°")])},
                {"v": "2. AB = 6 cm, AC = 5 cm",
                 "teksts": "Uz malām atliek garumus.",
                 "zim": lenkis([(0, "B"), (50, "C")], loki=[(0, 50, "50°")])},
                {"v": "3. savieno B un C", "teksts": "Trešā mala sanāk "
                 "pati - to izmēra."},
            ]),

    Paraugs("Taisnleņķa trijstūris",
            uzd="Uzzīmē trijstūri: ∠A = 90°, AB = 4 cm, AC = 3 cm. Izmēri BC.",
            soli=[
                ("∠A = 90°", "Ar uzstūri vai transportieri."),
                ("AB = 4 cm, AC = 3 cm", "Ar lineālu uz malām."),
                ("BC = 5 cm", "Izmēra ar lineālu."),
            ],
            atbilde="BC = 5 cm"),

    Varianti("Kārtība un pārbaude", [
        {"jaut": "Ko zīmē vispirms?",
         "opcijas": ["doto leņķi", "trešo malu", "jebko"], "pareizi": 0,
         "padoms": "Leņķis nosaka malu virzienus."},
        {"jaut": "Ar ko atliek malas garumu?",
         "opcijas": ["ar lineālu", "ar transportieri", "ar aci"],
         "pareizi": 0, "padoms": "Garums - lineāls."},
        {"jaut": "Ja leņķis 90°, trijstūris ir...",
         "opcijas": ["taisnleņķa", "šaurleņķa", "platleņķa"], "pareizi": 0,
         "padoms": "Viens taisns leņķis."},
        {"jaut": "Ja leņķis 120°, trijstūris ir...",
         "opcijas": ["platleņķa", "taisnleņķa", "šaurleņķa"], "pareizi": 0,
         "padoms": "Viens plats leņķis."},
    ], pamats=4),

    Ievadi("Mēri un rēķini", [
        {"jaut": "Trijstūra malas 4 cm, 3 cm un 5 cm. Perimetrs?",
         "atb": ["12"], "padoms": "4 + 3 + 5."},
        {"jaut": "Malas 6 cm, 5 cm un izmērītā 5 cm. Perimetrs?",
         "atb": ["16"], "padoms": "6 + 5 + 5."},
        {"jaut": "Perimetrs 20 cm, divas malas 7 cm un 6 cm. Trešā?",
         "atb": ["7"], "padoms": "20 − 13."},
        {"jaut": "Vienādmalu trijstūra mala 8 cm. Perimetrs?",
         "atb": ["24"], "padoms": "3 · 8."},
    ]),

    Pasaule("Ēģiptes virve",
            Ievadi("", [
                {"jaut": "Senie ēģiptieši ņēma virvi ar 12 mezgliem vienādos "
                         "attālumos. Cik atstarpju starp 13 mezgliem?",
                 "atb": ["12"], "padoms": "Viena mazāk nekā mezglu."},
                {"jaut": "Virvi izstiepa trijstūrī ar malām 3, 4 un ? "
                         "atstarpes (kopā 12). Cik ir trešā mala?",
                 "atb": ["5"], "padoms": "12 − 3 − 4."},
                {"jaut": "Starp malām 3 un 4 sanāk taisns leņķis. Cik "
                         "grādu?",
                 "atb": ["90"], "padoms": "Taisns."},
                {"jaut": "Ja atstarpe ir 2 m, cik garš ir šāda trijstūra "
                         "perimetrs?",
                 "atb": ["24"], "padoms": "12 · 2."},
            ]),
            pavediens="tehnika",
            konteksts="Ēģiptieši ar mezglotu virvi (3, 4, 5) iezīmēja taisnus "
                      "stūrus piramīdām.",
            kapec="Trīs garumi un viens leņķis - un stūris ir precīzs."),

    Petijums("Klases trijstūri",
             soli=[
                 "Visi zīmē trijstūri: ∠A = 60°, AB = 5 cm, AC = 4 cm.",
                 "Izmēra trešo malu BC.",
                 "Salīdziniet rezultātus klasē.",
                 "Izgrieziet un uzlieciet vienu uz otra.",
             ],
             vajag="transportieris, lineāls, šķēres",
             secinajums="Visiem sanāca vienādi trijstūri - nosacījumi tos "
                        "nosaka pilnīgi."),

    Kopsavilkums([
        "Zīmēju trijstūri pēc leņķa un divām malām.",
        "Ievēroju kārtību: leņķis, malas, savienojums.",
        "Izmēru trešo malu un aprēķinu perimetru.",
    ]),

    Majas([
        "Uzzīmē trijstūri: ∠A = 90°, AB = 6 cm, AC = 8 cm, un izmēri BC.",
        "Uztaisi «ēģiptiešu virvi» no auklas ar 12 vienādām daļām.",
        "Atrodi mājās trijstūri (pakaramais, jumts) un izmēri tā leņķi.",
    ]),
]
