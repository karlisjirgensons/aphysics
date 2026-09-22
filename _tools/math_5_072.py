# -*- coding: utf-8 -*-
"""5. klase, 72. stunda: «Kas ir daļa un kas - tās vērtība?»

Jauna temata pirmā stunda, un tā sākas ar nošķīrumu, ko skolēni parasti
nemana: {3|4} ir skaitlis, bet 750 g ir tā vērtība. Viena un tā pati daļa
no dažādiem veselajiem dod dažādas vērtības, tāpēc katrā uzdevumā jāzina
abi - gan daļa, gan veselais.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums, dala)

TEMA = "Kas ir daļa un kas - tās vērtība?"

MERKIS = ("Mācīsimies nošķirt lielumus, kas raksturo pašu daļu, no tiem, kas "
          "raksturo daļas skaitlisko vērtību.")

SATURS = [
    Sakums("Puse ceļa - cik tas ir kilometros?",
           zimejums=dala(2, 1, "1/2 ceļa"),
           paraksts="Daļa ir viena un tā pati, bet kilometru skaits - nē.",
           fakti=["Puse no 40 km ir 20 km.",
                  "Puse no 300 km ir 150 km.",
                  "Daļa abās reizēs ir {1|2}, bet vērtība - cita."]),

    Doma("Daļa ir skaitlis, vērtība ir daudzums",
         "Daļa pasaka, cik lielu gabalu ņem; daļas skaitliskā vērtība "
         "pasaka, cik daudz tas ir konkrētajā veselajā.",
         soli=[
             "Atrodi uzdevumā veselo - no kā ņem daļu.",
             "Atrodi daļu - cik lielu gabalu ņem.",
             "Daļa ir skaitlis bez mērvienības.",
             "Vērtība vienmēr ir ar mērvienību: km, kg, minūtes.",
             "Bez veselā vērtību aprēķināt nevar.",
         ],
         pieze="«Trešdaļa» pati par sevi neko nesver. Trešdaļa no 9 kg ir "
               "3 kg, bet trešdaļa no 30 kg ir 10 kg - viena un tā pati "
               "daļa, divas dažādas vērtības."),

    Slidnis("Viena daļa, dažādi veselie",
            [{"v": "{1|2} no 40 km", "teksts": "vērtība 20 km", "josla": 50},
             {"v": "{1|2} no 100 km", "teksts": "vērtība 50 km",
              "josla": 50},
             {"v": "{1|2} no 300 km", "teksts": "vērtība 150 km",
              "josla": 50},
             {"v": "{1|2} no 500 km", "teksts": "vērtība 250 km",
              "josla": 50}],
            ievads="Spied soli pa solim: josla nekustas, bet kilometru skaits "
                   "mainās katru reizi."),

    Paraugs("Kur ir daļa un kur - tās vērtība?",
            uzd="Ceļš ir 240 km garš; nobraukta {1|3} ceļa, tas ir 80 km. "
                "Nosauc veselo, daļu un daļas vērtību.",
            soli=[
                ("Veselais ir 240 km",
                 "No kā ņem daļu."),
                ("Daļa ir {1|3}",
                 "Skaitlis bez mērvienības."),
                ("Vērtība ir 80 km",
                 "Daudzums ar mērvienību."),
                ("240 : 3 = 80",
                 "Vērtību iegūst, dalot veselo ar saucēju."),
            ],
            atbilde="Veselais 240 km, daļa {1|3}, vērtība 80 km"),

    Ievadi("Aprēķini daļas vērtību", [
        {"jaut": "Cik ir {1|2} no 40 km? Atbildi kilometros.",
         "atb": ["20"], "padoms": "40 : 2."},
        {"jaut": "Cik ir {1|3} no 90 km? Atbildi kilometros.",
         "atb": ["30"], "padoms": "90 : 3."},
        {"jaut": "Cik ir {1|4} no 120 km? Atbildi kilometros.",
         "atb": ["30"], "padoms": "120 : 4."},
        {"jaut": "Cik ir {1|5} no 200 km? Atbildi kilometros.",
         "atb": ["40"], "padoms": "200 : 5."},
        {"jaut": "Cik ir {1|3} no 9 kg? Atbildi kilogramos.",
         "atb": ["3"], "padoms": "9 : 3."},
        {"jaut": "Cik ir {1|3} no 30 kg? Atbildi kilogramos.",
         "atb": ["10"], "padoms": "30 : 3."},
        {"jaut": "Cik ir {1|6} no 60 minūtēm? Atbildi minūtēs.",
         "atb": ["10"], "padoms": "60 : 6."},
        {"jaut": "Cik ir {1|4} no 60 minūtēm? Atbildi minūtēs.",
         "atb": ["15"], "padoms": "60 : 4."},
    ], pamats=4,
        ievads="Vienmēr paskaties, no kā ņem daļu - citādi atbilde ir "
               "nezināma."),

    Zimejums("Puse no gara un puse no īsa",
             dala(2, 1, "1/2"),
             paskaidro="Josla ir viena un tā pati, bet, ja tā apzīmē 40 km, "
                       "puse ir 20 km; ja 300 km, puse ir 150 km.",
             ievads="Modelis rāda daļu, nevis vērtību."),

    Varianti("Daļa vai vērtība?", [
        {"jaut": "«Nobraukta {1|3} ceļa» - kas tas ir?",
         "opcijas": ["Daļa", "Daļas vērtība", "Veselais", "Mērvienība"],
         "pareizi": 0,
         "padoms": "Skaitlis bez mērvienības."},
        {"jaut": "«Nobraukti 80 km» - kas tas ir?",
         "opcijas": ["Daļas vērtība", "Daļa", "Saucējs", "Skaitītājs"],
         "pareizi": 0,
         "padoms": "Daudzums ar mērvienību."},
        {"jaut": "Vai {1|2} no 40 km un {1|2} no 300 km ir viena un tā pati "
                 "daļa?",
         "opcijas": ["Jā, daļa ir viena, vērtības atšķiras",
                     "Nē, daļas ir dažādas",
                     "Jā, arī vērtības ir vienādas",
                     "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Daļa neatkarīga no veselā."},
        {"jaut": "Kas jāzina, lai aprēķinātu daļas vērtību?",
         "opcijas": ["Veselais un daļa", "Tikai daļa", "Tikai veselais",
                     "Tikai mērvienība"],
         "pareizi": 0,
         "padoms": "Bez veselā nav ko dalīt."},
        {"jaut": "Kurš no tiem ir lielākais?",
         "opcijas": ["{1|4} no 200 km", "{1|2} no 80 km", "{1|3} no 90 km",
                     "{1|5} no 200 km"],
         "pareizi": 0,
         "padoms": "50 km, 40 km, 30 km un 40 km."},
        {"jaut": "Kā aprēķina pamatdaļas vērtību?",
         "opcijas": ["Veselo dala ar saucēju", "Veselo reizina ar saucēju",
                     "Veselo dala ar skaitītāju", "Saucēju dala ar veselo"],
         "pareizi": 0,
         "padoms": "Sadala tik gabalos, cik rāda saucējs."},
    ], pamats=4),

    Pasaule("Cik tālu jau esam tikuši?",
            Ievadi("", [
                {"jaut": "Ceļojums ir 360 km garš, nobraukta {1|3}. Cik "
                         "kilometru tas ir?",
                 "atb": ["120"], "padoms": "360 : 3."},
                {"jaut": "Tas pats ceļojums. Cik kilometru ir {1|4} ceļa?",
                 "atb": ["90"], "padoms": "360 : 4."},
                {"jaut": "Brauciens ilgst 6 stundas. Cik minūtes ir {1|6} no "
                         "vienas stundas?",
                 "atb": ["10"], "padoms": "60 : 6."},
                {"jaut": "Bagāža sver 24 kg. Cik kilogramu ir {1|8} bagāžas?",
                 "atb": ["3"], "padoms": "24 : 8."},
            ]),
            pavediens="celojums",
            konteksts="Ceļā visu mēra daļās: puse ceļa, trešdaļa laika, "
                      "ceturtdaļa degvielas.",
            kapec="Katra daļa kaut ko nozīmē tikai kopā ar savu veselo."),

    Kopsavilkums([
        "Nošķiru daļu no daļas skaitliskās vērtības.",
        "Atrodu uzdevumā veselo, no kā ņem daļu.",
        "Aprēķinu pamatdaļas vērtību, dalot veselo ar saucēju.",
        "Zinu, ka viena daļa no dažādiem veselajiem dod dažādas vērtības.",
    ]),

    Majas([
        "Uzraksti trīs teikumus, kuros ir daļa, un trīs, kuros ir tās "
        "vērtība.",
        "Aprēķini {1|4} no sava ceļa uz skolu.",
        "Atrodi veselo, kuram {1|2} ir tieši 25 km.",
    ]),
]
