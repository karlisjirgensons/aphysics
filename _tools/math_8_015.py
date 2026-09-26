# -*- coding: utf-8 -*-
"""8. klase, 15. stunda: «Kā prezentēt rezultātus?»

Pētījuma bloka noslēgums pirms pārbaudes darba. Prezentācija ir stāsts ar
skaitļiem: jautājums, metode, rezultāts diagrammā, secinājums. Stundā
skolēns sagatavo savu prezentāciju un atkārto visus temata rādītājus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, restis)

TEMA = "Kā prezentēt rezultātus?"

MERKIS = ("Prezentēsim pētījuma rezultātus un atbildēsim uz klasesbiedru "
          "jautājumiem.")

SATURS = [
    Sakums("Četri slaidi - viens pētījums",
           zimejums=restis([["1", "jautājums"],
                            ["2", "metode un izlase"],
                            ["3", "diagramma un rādītāji"],
                            ["4", "secinājums"]]),
           paraksts="Katrs slaids atbild uz vienu jautājumu.",
           fakti=["Klausītājs atceras vienu skaitli - izvēlies to.",
                  "Diagrammai vajag virsrakstu un asu nosaukumus.",
                  "Secinājums atbild uz 1. slaida jautājumu."]),

    Doma("Laba prezentācija",
         "Prezentācija nav visu datu saraksts. Tā pasaka, ko pētīji, kā un "
         "ko atklāji - un pierāda to ar skaitļiem.",
         soli=[
             "Sāc ar jautājumu, kas klausītājam liekas interesants.",
             "Pasaki izlasi: cik, kas, kā savākts.",
             "Parādi vienu piemērotu diagrammu.",
             "Nosauc 2-3 rādītājus, ne visus.",
             "Secinājums un viens ierobežojums.",
         ],
         pieze="Sagatavojies jautājumiem: «Kāpēc tieši šī izlase?», «Kāpēc "
               "mediāna, nevis vidējais?»"),

    Varianti("Kā uzlabot slaidu?", [
        {"jaut": "Slaidā ir visi 60 izmērītie skaitļi.",
         "opcijas": ["Aizstāt ar diagrammu un 2 rādītājiem",
                     "Rakstīt mazākā fontā",
                     "Pievienot vēl datus", "Nolasīt visus skaļi"],
         "pareizi": 0, "padoms": "Apkopo."},
        {"jaut": "Diagrammai nav asu nosaukumu.",
         "opcijas": ["Pievienot nosaukumus un mērvienības",
                     "Nekas nav jādara", "Nomainīt krāsu",
                     "Pievienot bildes"],
         "pareizi": 0, "padoms": "Ko rāda ass?"},
        {"jaut": "Datos ir viena liela novirze. Kuru centru nosaukt?",
         "opcijas": ["Mediānu (un pieminēt novirzi)", "Tikai vidējo",
                     "Tikai modu", "Nekādu"],
         "pareizi": 0, "padoms": "Novirze pavelk vidējo."},
    ]),

    Ievadi("Temata atkārtojums", [
        {"jaut": "Dati: 4, 9, 6, 4, 7. Vidējais?",
         "atb": ["6"], "padoms": "30 : 5."},
        {"jaut": "Mediāna?",
         "atb": ["6"], "padoms": "4; 4; 6; 7; 9."},
        {"jaut": "Moda?",
         "atb": ["4"], "padoms": "Divas reizes."},
        {"jaut": "Amplitūda?",
         "atb": ["5"], "padoms": "9 − 4."},
        {"jaut": "Relatīvais biežums vērtībai 4 procentos?",
         "atb": ["40", "40 %", "40%"], "padoms": "2 : 5."},
        {"jaut": "Sektors 25 %. Cik grādu?",
         "atb": ["90", "90°"], "padoms": "{1|4} no 360°."},
    ], pamats=4),

    Petijums("Sagatavo savu prezentāciju",
             vajag="savi pētījuma dati",
             soli=[
                 "1. slaids: pētījuma jautājums.",
                 "2. slaids: izlase un metode vienā teikumā.",
                 "3. slaids: diagramma + vidējais, mediāna, amplitūda.",
                 "4. slaids: secinājums ar skaitli un viens ierobežojums.",
                 "Izdomā divus jautājumus, ko tev varētu uzdot, un atbildes.",
             ],
             secinajums="Prezentācija ilgst 2 minūtes - tik ilgi klausītājs "
                        "notur uzmanību uz vienu diagrammu."),

    Pasaule("Klases pētījuma rezultāts",
            Ievadi("", [
                {"jaut": "Somas svars (kg) 5 skolēniem: 4,5; 6; 7,5; 5; 8. "
                         "Vidējais?",
                 "atb": ["6,2", "6.2"], "padoms": "31 : 5."},
                {"jaut": "Skolēnam, kas sver 50 kg, norma ir ≤ 10 %. Cik kg?",
                 "atb": ["5"], "padoms": "0,1 · 50."},
                {"jaut": "Cik somu no 5 ir smagākas par 5 kg?",
                 "atb": ["3"], "padoms": "6; 7,5; 8."},
            ]),
            pavediens="skola",
            konteksts="Somas svara pētījums ir klasisks skolēnu pētījums - "
                      "ar svariem to var izdarīt vienā starpbrīdī.",
            kapec="Secinājums ar normu un skaitli pārliecina vairāk par "
                  "«somas ir smagas»."),

    Kopsavilkums([
        "Veidoju prezentāciju: jautājums, metode, rezultāts, secinājums.",
        "Izvēlos vienu diagrammu un 2-3 rādītājus.",
        "Atbildu uz jautājumiem par izlasi un rādītājiem.",
        "Atkārtoju visus temata rādītājus pirms pārbaudes darba.",
    ]),

    Majas([
        "Pabeidz 4 slaidu prezentāciju.",
        "Izmēģini to 2 minūtēs mājiniekam.",
        "Atkārto vidējo, mediānu, modu, amplitūdu un relatīvo biežumu.",
    ]),
]
