# -*- coding: utf-8 -*-
"""3. klase, 48. stunda: «Ko var nopirkt par šo naudu?»

Apgrieztais uzdevums iepriekšējai stundai: summa ir zināma, pirkums - nē.
Šeit atbilžu ir daudz, un skolēnam pašam jāpieraksta izteiksme, kas pamato
viņa izvēli. Tas ir pirmais solis uz budžetu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Ko var nopirkt par šo naudu?"

MERKIS = ("Izvēlēsimies preces par doto summu un pierakstīsim atbilstošu "
          "izteiksmi.")

SATURS = [
    Sakums("Kas ietilpst vienā eiro?",
           zimejums=restis([["prece", "cena"],
                            ["zīmulis", "15 ct"],
                            ["dzēšgumija", "25 ct"],
                            ["burtnīca", "40 ct"],
                            ["lineāls", "60 ct"]],
                           "klases veikaliņa cenas"),
           paraksts="Par 100 ct var nopirkt dažādus komplektus.",
           fakti=["Viens eiro ir 100 centi.",
                  "Par vienu summu var izvēlēties dažādas preces."]),

    Doma("Vispirms izvēlies, tad pārbaudi",
         "Saliec pirkumu, pieraksti izteiksmi un tikai tad pārbaudi, vai "
         "summa ietilpst kabatā.",
         soli=[
             "Izvēlies preces un to skaitu.",
             "Pieraksti izteiksmi: skaits reiz cena, pa preču veidiem.",
             "Aprēķini kopsummu.",
             "Salīdzini ar naudu, kas ir kabatā.",
             "Ja summa ir par lielu, noņem vienu preci un rēķini vēlreiz.",
         ],
         pieze="Izteiksme ir vajadzīga tieši tāpēc, ka izvēli gribas mainīt: "
               "pārrakstot vienu skaitli, visu rēķinu var atkārtot ātri."),

    Paraugs("Ko var nopirkt par 100 centiem?",
            uzd="Izvēlies pirkumu par 100 ct: zīmulis 15 ct, dzēšgumija "
                "25 ct, burtnīca 40 ct.",
            soli=[
                ("2 · 15 + 25 + 40",
                 "Divi zīmuļi, dzēšgumija un burtnīca."),
                ("30 + 25 + 40 = 95",
                 "Kopsumma."),
                ("100 − 95 = 5",
                 "Pāri paliek 5 ct - pirkums ietilpst."),
            ],
            atbilde="95 ct; paliek 5 ct"),

    Ievadi("Cik maksā pirkums?", [
        {"jaut": "2 zīmuļi pa 15 ct. Cik maksā?", "atb": ["30"],
         "padoms": "2 · 15."},
        {"jaut": "3 dzēšgumijas pa 25 ct. Cik maksā?", "atb": ["75"],
         "padoms": "3 · 25."},
        {"jaut": "1 burtnīca 40 ct un 2 zīmuļi pa 15 ct. Cik kopā?",
         "atb": ["70"], "padoms": "40 + 30."},
        {"jaut": "Cik paliks pāri no 100 ct?", "atb": ["30"],
         "padoms": "100 − 70."},
        {"jaut": "2 burtnīcas pa 40 ct un 1 lineāls 60 ct. Cik kopā?",
         "atb": ["140"], "padoms": "80 + 60."},
        {"jaut": "Cik centu pietrūkst, ja kabatā ir 100 ct?",
         "atb": ["40"], "padoms": "140 − 100."},
    ], pamats=4),

    Petijums("Saliec savu pirkumu",
             vajag="cenu saraksts un lapa",
             soli=[
                 "Izdomā, ka kabatā ir 150 ct.",
                 "Izvēlies preces un pieraksti izteiksmi.",
                 "Aprēķini kopsummu un atlikumu.",
                 "Pamaini vienu preci un salīdzini abus pirkumus.",
             ],
             secinajums="Ja izteiksme ir pierakstīta, jauno summu var "
                        "izrēķināt, nepārrakstot visu no jauna."),

    Zimejums("Divi pirkumi par vienu naudu",
             restis([["1. pirkums", "2 · 15 + 40 = 70"],
                     ["2. pirkums", "25 + 40 = 65"]],
                    "abi ietilpst 100 ct"),
             paskaidro="Abi pirkumi ir pareizi - izvēle ir par to, kas tev "
                       "vajadzīgāks.",
             ievads="Salīdzini abas izteiksmes."),

    Varianti("Vai pirkums ietilpst?", [
        {"jaut": "Kabatā 100 ct. Vai var nopirkt 2 burtnīcas pa 40 ct un "
                 "zīmuli 15 ct?",
         "opcijas": ["Jā, kopā 95 ct", "Nē, pietrūkst", "Jā, kopā 100 ct",
                     "Nē, jo burtnīcu ir divas"],
         "pareizi": 0, "padoms": "80 + 15."},
        {"jaut": "Kura izteiksme atbilst pirkumam «3 zīmuļi un 1 burtnīca»?",
         "opcijas": ["3 · 15 + 40", "3 + 15 + 40", "3 · (15 + 40)",
                     "15 + 40"],
         "pareizi": 0, "padoms": "Skaits reiz cena, tad pieskaita."},
        {"jaut": "Cik maksā 4 zīmuļi pa 15 ct?",
         "opcijas": ["60 ct", "45 ct", "19 ct", "75 ct"],
         "pareizi": 0, "padoms": "4 · 15."},
        {"jaut": "Ko darīt, ja summa ir par lielu?",
         "opcijas": ["Noņemt vienu preci un rēķināt vēlreiz",
                     "Aizmirst par rēķinu", "Pirkt tik un tā",
                     "Pieskaitīt vēl vienu preci"],
         "pareizi": 0, "padoms": "Izteiksmi pārrēķina."},
    ], pamats=4),

    Pasaule("Ko nopirkt klases svētkiem?",
            Ievadi("", [
                {"jaut": "Sula maksā 80 ct, cepumi 65 ct. Cik maksā abi?",
                 "atb": ["145"], "padoms": "80 + 65."},
                {"jaut": "Cik maksā 3 sulas pa 80 ct?",
                 "atb": ["240"], "padoms": "3 · 80."},
                {"jaut": "Klases kasē ir 500 ct. Cik paliks pēc 3 sulām?",
                 "atb": ["260"], "padoms": "500 − 240."},
                {"jaut": "Cik cepumu paciņu pa 65 ct vēl var nopirkt?",
                 "atb": ["4"], "padoms": "4 · 65 = 260."},
            ]),
            pavediens="veikals",
            konteksts="Klases pasākumam naudas ir tieši tik, cik savākts - "
                      "tāpēc pirkumu saliek uz papīra, ne veikalā.",
            kapec="Izteiksme ļauj izmēģināt vairākus variantus, neiztērējot "
                  "ne centa."),

    Kopsavilkums([
        "Izvēlos preces par doto summu.",
        "Pierakstu pirkumu kā izteiksmi.",
        "Aprēķinu kopsummu un atlikumu.",
        "Pamainu vienu preci un pārrēķinu summu.",
    ]),

    Majas([
        "Saliec pirkumu par 200 ct un pieraksti izteiksmi.",
        "Atrodi divus dažādus pirkumus ar vienādu summu.",
        "Paskaties mājas čekā, cik maksāja dārgākā prece.",
    ]),
]
