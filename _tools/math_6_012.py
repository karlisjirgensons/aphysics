# -*- coding: utf-8 -*-
"""6. klase, 12. stunda: «Kā pārrēķināt recepti?»

Proporcionalitāte darbā. Recepte ir visbiežāk lietotā proporcija pasaulē, un
te parādās divi ceļi: caur vienu porciju un caur reizinātāju. Abi ir
pareizi, tāpēc stunda māca izvēlēties īsāko.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti)

TEMA = "Kā pārrēķināt recepti?"

MERKIS = ("Iemācīsimies aprēķināt sastāvdaļu daudzumu citam produkta "
          "daudzumam, izmantojot vienu porciju vai reizinātāju.")

SATURS = [
    Sakums("Recepte 4 cilvēkiem, bet mājās ir 6",
           fakti=["Recepte vienmēr ir rakstīta kādam vienam skaitlim.",
                  "Pārrēķināt var divos veidos: caur vienu porciju vai "
                  "reizinot.",
                  "Konditori vienmēr strādā ar vienas porcijas daudzumu."]),

    Doma("Vispirms viena porcija, tad cik vajag",
         "Ja daudzumi ir tieši proporcionāli, pietiek zināt vienu porciju - "
         "pārējais ir reizināšana.",
         soli=[
             "Izdali katru sastāvdaļu ar porciju skaitu receptē.",
             "Pieraksti, cik daudz vajag vienai porcijai.",
             "Reizini ar to porciju skaitu, kāds vajadzīgs.",
             "Ja jaunais skaitlis dalās ar veco, rēķini uzreiz ar "
             "reizinātāju.",
         ],
         pieze="No 4 uz 8 porcijām reizinātājs ir 2 - tur viena porcija nav "
               "jārēķina. No 4 uz 6 tas ir 1,5, un tad caur vienu porciju "
               "sanāk ātrāk."),

    Paraugs("No 4 porcijām uz 6",
            uzd="Receptē 4 porcijām: 200 g miltu, 300 ml piena, 2 olas. Cik "
                "vajag 6 porcijām?",
            soli=[
                ("200 : 4 = 50 g miltu vienai porcijai",
                 "Vispirms viena porcija."),
                ("300 : 4 = 75 ml piena; 2 : 4 = {1|2} olas",
                 "Tas pats pārējām sastāvdaļām."),
                ("Milti 6 · 50 = 300 g",
                 "Reizina ar vajadzīgo porciju skaitu."),
                ("Piens 6 · 75 = 450 ml; olas 6 · {1|2} = 3",
                 "Olas beidzot sanāk vesels skaitlis."),
            ],
            atbilde="300 g miltu, 450 ml piena, 3 olas"),

    Ievadi("Pārrēķini recepti", [
        {"jaut": "4 porcijām vajag 200 g miltu. Cik gramu vajag 1 porcijai?",
         "atb": ["50"], "padoms": "200 : 4."},
        {"jaut": "Cik gramu miltu vajag 10 porcijām?",
         "atb": ["500"], "padoms": "10 · 50."},
        {"jaut": "6 porcijām vajag 180 g rīsu. Cik gramu vajag 2 porcijām?",
         "atb": ["60"], "padoms": "180 : 6 = 30; 2 · 30."},
        {"jaut": "8 porcijām vajag 4 olas. Cik olas vajag 12 porcijām?",
         "atb": ["6"], "padoms": "Vienai porcijai {1|2} olas."},
        {"jaut": "3 porcijām vajag 450 ml ūdens. Cik ml vajag 5 porcijām?",
         "atb": ["750"], "padoms": "450 : 3 = 150; 5 · 150."},
        {"jaut": "Receptē 5 porcijām ir 250 g siera. Cik porciju var "
                 "pagatavot no 400 g siera?",
         "atb": ["8"], "padoms": "Vienai porcijai 50 g; 400 : 50."},
    ], pamats=4,
        ievads="Viena porcija ir atslēga - to izrēķina vienreiz."),

    Varianti("Kurš ceļš ir īsāks?", [
        {"jaut": "No 5 porcijām uz 10. Kā rēķināt ātrāk?",
         "opcijas": ["Reizināt visu ar 2", "Rēķināt vienu porciju",
                     "Dalīt ar 5", "Atņemt 5"],
         "pareizi": 0,
         "padoms": "10 : 5 = 2 - reizinātājs ir vesels."},
        {"jaut": "No 4 porcijām uz 7. Kā rēķināt ērtāk?",
         "opcijas": ["Caur vienu porciju", "Reizināt ar 7",
                     "Dalīt ar 7", "Atņemt 3 porcijas"],
         "pareizi": 0,
         "padoms": "7 : 4 nav vesels skaitlis."},
        {"jaut": "Receptē 2 olas 4 porcijām. Cik olas 1 porcijai?",
         "opcijas": ["{1|2}", "2", "4", "1"],
         "pareizi": 0,
         "padoms": "2 : 4."},
        {"jaut": "Kas notiek ar garšvielām, dubultojot recepti?",
         "opcijas": ["Arī tās dubultojas", "Tās paliek tādas pašas",
                     "Tās samazinās", "Tās vairs nav vajadzīgas"],
         "pareizi": 0,
         "padoms": "Visas sastāvdaļas ir proporcionālas porciju skaitam."},
    ], pamats=4),

    Pasaule("Ko gatavot klasei?",
            Ievadi("", [
                {"jaut": "Recepte 4 porcijām: 120 g auzu pārslu. Cik gramu "
                         "vajag 24 skolēniem?",
                 "atb": ["720"], "padoms": "24 : 4 = 6; 6 · 120."},
                {"jaut": "Tai pašai receptei 4 porcijām ir 2 banāni. Cik "
                         "banānu vajag 24 porcijām?",
                 "atb": ["12"], "padoms": "6 · 2."},
                {"jaut": "Viena porcija maksā 0,35 €. Cik eiro maksā "
                         "24 porcijas?",
                 "atb": ["8,4", "8,40", "8.4"], "padoms": "24 · 0,35."},
                {"jaut": "Budžets ir 12 €. Cik porcijas var pagatavot?",
                 "atb": ["34"], "padoms": "12 : 0,35 ir mazliet vairāk par "
                                          "34 - veselas porcijas ir 34."},
            ]),
            pavediens="virtuve",
            konteksts="Klases pasākumā recepte no interneta gandrīz nekad "
                      "nav rakstīta tieši tik cilvēkiem, cik jūsu ir.",
            kapec="Viena porcija savieno recepti ar jebkuru cilvēku skaitu."),

    Petijums("Pārrēķini īstu recepti",
             vajag="jebkura recepte no mājām vai interneta",
             soli=[
                 "Pieraksti, cik porcijām recepte ir domāta.",
                 "Izrēķini katras sastāvdaļas daudzumu vienai porcijai.",
                 "Pārrēķini recepti tieši tik porcijām, cik mājās ir cilvēku.",
                 "Pieraksti, kura sastāvdaļa sanāca ne vesels skaitlis.",
             ],
             secinajums="Vienas porcijas daudzumi ir īstā recepte - viss "
                        "pārējais no tiem tikai izriet."),

    Kopsavilkums([
        "Aprēķinu sastāvdaļu daudzumu vienai porcijai.",
        "Pārrēķinu recepti jebkuram porciju skaitam.",
        "Izvēlos īsāko ceļu: reizinātāju vai vienu porciju.",
        "Zinu, ka pārrēķinot mainās visas sastāvdaļas, ne tikai dažas.",
    ]),

    Majas([
        "Pārrēķini kādu mājas recepti divreiz mazākam daudzumam.",
        "Atrodi recepti, kurā viena sastāvdaļa nesanāk vesela, un pieraksti, "
        "ko ar to darīt.",
        "Izrēķini, cik maksā viena porcija tavam iecienītākajam ēdienam.",
    ]),
]
