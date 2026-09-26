# -*- coding: utf-8 -*-
"""4. klase, 119. stunda: «Ko var uzzināt no teikuma par daļu?»

«{3|4} klases brauca ekskursijā» - no šī teikuma var uzzināt arī, ka {1|4}
nebrauca, un, ja zināms klases lielums, cik tieši skolēnu. Stunda māca
izspiest no teikuma visu informāciju: daļu, papildinājumu un skaitļus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, dala)

TEMA = "Ko var uzzināt no teikuma par daļu?"

MERKIS = ("Analizēsim sadzīves teikumu ar daļu un formulēsim, ko no tā var "
          "uzzināt.")

SATURS = [
    Sakums("«{3|4} klases brauca ekskursijā.» Ko vēl mēs zinām?",
           zimejums=dala(4, 3, "brauca 3/4, palika 1/4"),
           paraksts="Ja klasē 28 skolēni - brauca 21, palika 7.",
           fakti=["Viens teikums - vairākas ziņas.",
                  "Zinām arī to, kas *netika* teikts: {1|4} palika."]),

    Doma("Viens teikums - trīs ziņas",
         "No teikuma ar daļu var uzzināt daļu, tās papildinājumu līdz veselam "
         "un - ja veselais zināms - abu skaitliskās vērtības.",
         soli=[
             "Daļa: {3|4} brauca.",
             "Papildinājums: 1 − {3|4} = {1|4} nebrauca.",
             "Ja veselais zināms (28), vienu daļu: 28 : 4 = 7.",
             "Brauca 3 · 7 = 21, palika 7.",
         ],
         pieze="Ja veselais nav zināms, var salīdzināt: brauca 3 reizes "
               "vairāk nekā palika."),

    Paraugs("Mājdzīvnieku aptauja",
            uzd="«{2|5} klases skolēnu ir suns.» Klasē 25 skolēni. Ko var "
                "uzzināt?",
            soli=[
                ("{3|5} suņa nav", "Papildinājums."),
                ("25 : 5 = 5", "Viena piektdaļa."),
                ("suns ir 2 · 5 = 10 skolēniem", None),
                ("suņa nav 3 · 5 = 15 skolēniem", None),
            ],
            atbilde="10 ar suni, 15 bez suņa"),

    Ievadi("Uzzini vairāk", [
        {"jaut": "«{5|8} grāmatas izlasīts.» Kāda daļa vēl jāizlasa?",
         "atb": ["3/8"], "vieta": "piem., 1/2", "padoms": "1 − {5|8}."},
        {"jaut": "Grāmatā 240 lpp. Cik lappušu ir {1|8}?", "atb": ["30"],
         "padoms": "240 : 8."},
        {"jaut": "Cik lappušu izlasīts ({5|8})?", "atb": ["150"],
         "padoms": "5 · 30."},
        {"jaut": "Cik lappušu vēl jāizlasa?", "atb": ["90"],
         "padoms": "3 · 30."},
    ]),

    Varianti("Ko var uzzināt?", [
        {"jaut": "«{1|3} dienas guļu.» Ko var uzzināt, nerēķinot stundas?",
         "opcijas": ["{2|3} dienas negulu", "guļu 3 stundas",
                     "guļu naktī"], "pareizi": 0,
         "padoms": "Papildinājums."},
        {"jaut": "Diennaktī 24 h. Cik stundu tas ir ({1|3})?",
         "opcijas": ["8", "3", "12", "6"], "pareizi": 0,
         "padoms": "24 : 3."},
        {"jaut": "«{2|3} ceļa nobraukts, atlikuši 40 km.» Kāda daļa ir 40 "
                 "km?",
         "opcijas": ["{1|3}", "{2|3}", "{1|2}", "{3|3}"], "pareizi": 0,
         "padoms": "Atlikusī daļa."},
        {"jaut": "Ko nevar uzzināt no «{1|2} klases ir meitenes»?",
         "opcijas": ["meiteņu vārdus", "ka puse ir zēni",
                     "ka meiteņu un zēnu ir vienādi"], "pareizi": 0,
         "padoms": "Vārdu teikumā nav."},
    ], pamats=4),

    Pasaule("Ziņu virsraksti",
            Ievadi("", [
                {"jaut": "«{3|4} Latvijas skolēnu brauc uz skolu ar kājām vai "
                         "velosipēdu.» Skolā 400 skolēni. Cik tas būtu?",
                 "atb": ["300"], "padoms": "400 : 4 · 3."},
                {"jaut": "Cik skolēnu brauc ar autobusu vai auto?",
                 "atb": ["100"], "padoms": "{1|4} no 400."},
                {"jaut": "«{2|5} dzīvnieku patversmē ir kaķi.» Patversmē 60 "
                         "dzīvnieku. Cik kaķu?",
                 "atb": ["24"], "padoms": "60 : 5 · 2."},
                {"jaut": "Cik dzīvnieku nav kaķi?", "atb": ["36"],
                 "padoms": "60 − 24."},
            ]),
            pavediens="skola",
            konteksts="Ziņās bieži ir daļas - un gudrs lasītājs uzreiz "
                      "izrēķina, cik tas ir skaitļos.",
            kapec="Daļa kļūst saprotama, kad to pārvērš skaitlī."),

    Kopsavilkums([
        "No teikuma ar daļu uzzinu arī papildinājumu.",
        "Aprēķinu daļas skaitlisko vērtību, ja veselais zināms.",
        "Pamanu, ko teikums *nepasaka*.",
    ]),

    Majas([
        "Atrodi ziņās teikumu ar daļu un izraksti visu, ko no tā var uzzināt.",
        "Izveido teikumu ar daļu par savu ģimeni.",
        "Palūdz mājiniekiem uzminēt skaitļus no tava teikuma.",
    ]),
]
