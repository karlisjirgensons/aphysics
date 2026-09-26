# -*- coding: utf-8 -*-
"""7. klase, 43. stunda: «Kādas vērtības mainīgajam ir iespējamas?»

Formula pati par sevi atļauj jebkuru skaitli, bet situācija - ne. Cilvēku
skaits ir naturāls, laiks nav negatīvs, svece nevar būt īsāka par 0.
Stunda iemāca noteikt, kādas vērtības mainīgajam ir jēgpilnas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kādas vērtības mainīgajam ir iespējamas?"

MERKIS = ("Noteiksim, kuri skaitļi var būt mainīgā vērtības konkrētajā "
          "situācijā.")

SATURS = [
    Sakums("Vai var nopirkt 2,5 biļetes?",
           fakti=["Formulā S = 6n var ievietot n = 2,5.",
                  "Bet biļetes pērk veselas - n ir naturāls skaitlis.",
                  "Situācija ierobežo formulu."]),

    Doma("Situācija nosaka iespējamās vērtības",
         "Mainīgā iespējamās vērtības ir tie skaitļi, kas situācijā ir "
         "jēgpilni. Tās nosaka lieluma daba (vesels, nenegatīvs) un "
         "situācijas robežas (sākums un beigas).",
         soli=[
             "Jautā: vai lielums var būt daļskaitlis?",
             "Vai tas var būt negatīvs vai nulle?",
             "Vai ir augšējā robeža (tilpums, laiks līdz beigām)?",
             "Pieraksti: n ∈ N vai 0 ≤ t ≤ 5.",
         ],
         pieze="Naturālo skaitļu kopa N = {1; 2; 3; ...}. Ja der arī nulle, "
               "raksta n = 0; 1; 2; ..."),

    Paraugs("Sveces augstums",
            uzd="Svece 20 cm, sadeg 4 cm stundā: h = 20 − 4t. Kādas "
                "vērtības var pieņemt t un h?",
            soli=[
                ("Svece sadeg, kad h = 0: 20 − 4t = 0, t = 5",
                 "Augšējā robeža laikam."),
                ("0 ≤ t ≤ 5 (h)", "Laiks nav negatīvs."),
                ("0 ≤ h ≤ 20 (cm)", "Augstums no pilna līdz nullei."),
                ("t var būt daļskaitlis: t = 2,5", "Laiks rit nepārtraukti."),
            ],
            atbilde="0 ≤ t ≤ 5; 0 ≤ h ≤ 20"),

    Zimejums("Laika iespējamās vērtības",
             taisne(0, 6, 1, intervali=[(0, 5, True, True)]),
             paskaidro="Svītrotā daļa: no 0 līdz 5 ieskaitot."),

    Varianti("Kādas vērtības der?", [
        {"jaut": "Skolēnu skaits klasē n",
         "opcijas": ["Naturāli skaitļi", "Jebkuri skaitļi",
                     "Decimāldaļas", "Negatīvi skaitļi"],
         "pareizi": 0,
         "padoms": "Nav pusskolēnu."},
        {"jaut": "Temperatūra ārā T (°C)",
         "opcijas": ["Arī negatīvi un daļskaitļi", "Tikai naturāli",
                     "Tikai pozitīvi", "Tikai veseli"],
         "pareizi": 0,
         "padoms": "Ziemā −5,5 °C."},
        {"jaut": "Laiks t lejupielādē, kas ilgst 40 s",
         "opcijas": ["0 ≤ t ≤ 40", "t > 40", "t ∈ N", "t < 0"],
         "pareizi": 0,
         "padoms": "No sākuma līdz beigām."},
        {"jaut": "Metienu skaits kauliņam",
         "opcijas": ["0; 1; 2; 3; ...", "Jebkuri", "Tikai 1-6",
                     "Decimāldaļas"],
         "pareizi": 0,
         "padoms": "Skaits - vesels, nenegatīvs."},
    ], pamats=4),

    Ievadi("Atrodi robežas", [
        {"jaut": "Vannā 180 l, ietek 12 l/min: V = 12t. Lielākā "
                 "iespējamā t vērtība (min)?",
         "atb": ["15"], "padoms": "Kad vanna pilna."},
        {"jaut": "Kontā 50 €, katru dienu tērē 4 €. Cik pilnu dienu var "
                 "tērēt?",
         "atb": ["12"], "padoms": "50 : 4 = 12,5 - pilnas 12."},
        {"jaut": "Autobusā 45 vietas. Lielākais pasažieru sēdvietās "
                 "skaits?",
         "atb": ["45"], "padoms": "Ne vairāk kā vietu."},
        {"jaut": "S = 6n, budžets 40 €. Lielākais n?",
         "atb": ["6"], "padoms": "40 : 6 ≈ 6,7 - veseli."},
    ]),

    Pasaule("Lifts un krava",
            Ievadi("", [
                {"jaut": "Lifts pārvadā līdz 630 kg. Cilvēks ar mantām "
                         "ir vidēji 90 kg. Cik cilvēku drīkst iekāpt?",
                 "atb": ["7"], "padoms": "630 : 90."},
                {"jaut": "Ja iekāpj 5 cilvēki, cik kg vēl drīkst iekraut?",
                 "atb": ["180"], "padoms": "630 − 450."},
                {"jaut": "Vai cilvēku skaits var būt 6,5? Raksti «jā» vai "
                         "«nē».",
                 "atb": ["nē", "ne"], "padoms": "Skaits ir vesels."},
            ]),
            pavediens="tehnika",
            konteksts="Liftā ir uzraksts ar kravnesību un cilvēku skaitu - "
                      "tā ir mainīgā augšējā robeža.",
            kapec="Formula dod skaitli, situācija - robežas."),

    Kopsavilkums([
        "Nosaku, vai mainīgais var būt daļskaitlis vai negatīvs.",
        "Atrodu situācijas robežas.",
        "Pierakstu iespējamās vērtības ar nevienādību.",
        "Atšķiru formulas atļauto no situācijas atļautā.",
    ]),

    Majas([
        "Atrodi 3 lielumus ar dažādām iespējamām vērtībām.",
        "Pieraksti robežas savam ceļam uz skolu (laiks, attālums).",
        "Izdomā situāciju, kur mainīgais var būt negatīvs.",
    ]),
]
