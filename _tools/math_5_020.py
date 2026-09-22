# -*- coding: utf-8 -*-
"""5. klase, 20. stunda: «Ko var un ko nevar aprēķināt?»

Stunda bez jautājuma uzdevuma beigās. Skolēns pierod, ka uzdevums vienmēr
pasaka, kas jārēķina; te viņam pašam jāsaprot, kuri jautājumi no dotajiem
datiem izriet un kuriem datu trūkst. Tas ir tas pats spriedums, ko vēlāk
prasa jebkurš teksta uzdevums.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Ko var un ko nevar aprēķināt?"

MERKIS = ("Mācīsimies izlasīt situācijas aprakstu bez jautājuma un spriest, "
          "ko no dotajiem datiem var aprēķināt un ko ne.")

SATURS = [
    Sakums("Uzdevums bez jautājuma",
           fakti=["Ekskursijā brauc trīs klases: 24, 22 un 26 skolēni.",
                  "Autobusā ir 50 vietas, muzeja biļete maksā 4 eiro.",
                  "Jautājuma nav. Ko no tā vispār var uzzināt?"]),

    Doma("Vispirms saraksti, kas ir zināms",
         "Aprēķināt var tikai to, kam pietiek doto skaitļu - pārējam trūkst "
         "datu.",
         soli=[
             "Izlasi aprakstu un izraksti visus skaitļus.",
             "Pieraksti, ko katrs skaitlis nozīmē.",
             "Uzdod jautājumu un pameklē, kuri skaitļi tam vajadzīgi.",
             "Ja kāda skaitļa trūkst, atbilde ir «nevar aprēķināt».",
         ],
         pieze="«Nevar aprēķināt» nav sliktāka atbilde nekā skaitlis. Sliktāk "
               "ir izdomāt trūkstošo skaitli pašam un turpināt rēķināt tā, it "
               "kā tas būtu dots."),

    Paraugs("Izšķiro jautājumus",
            uzd="Klases 24, 22 un 26 skolēni, autobusā 50 vietas, biļete "
                "4 eiro. Vai var aprēķināt: a) cik skolēnu kopā, b) cik ilgs "
                "ir brauciens?",
            soli=[
                ("a) 24 + 22 + 26 = 72",
                 "Visi trīs skaitļi ir doti, tāpēc summu var izrēķināt."),
                ("b) Brauciena ilgums - trūkst datu",
                 "Aprakstā nav ne attāluma, ne ātruma, ne laika."),
                ("Atbilde a) 72 skolēni, b) nevar aprēķināt",
                 "Abas atbildes ir pilnvērtīgas."),
            ],
            atbilde="a) 72 skolēni; b) nevar aprēķināt"),

    Ievadi("Aprēķini vai raksti «nevar»", [
        {"jaut": "Cik skolēnu brauc kopā? (24, 22 un 26)",
         "atb": ["72"], "padoms": "24 + 22 + 26."},
        {"jaut": "Cik kopā maksās biļetes visiem 72 skolēniem, ja viena ir "
                 "4 eiro?",
         "atb": ["288"], "padoms": "72 · 4."},
        {"jaut": "Par cik skolēnu vairāk ir lielākajā klasē nekā mazākajā?",
         "atb": ["4"], "padoms": "26 − 22."},
        {"jaut": "Cik ilgs ir brauciens? Raksti skaitli vai «nevar».",
         "atb": ["nevar"], "padoms": "Aprakstā nav ne attāluma, ne ātruma."},
        {"jaut": "Cik skolotāju brauc līdzi? Raksti skaitli vai «nevar».",
         "atb": ["nevar"], "padoms": "Par skolotājiem aprakstā nav neviena "
                                     "skaitļa."},
        {"jaut": "Cik vietu autobusā paliks brīvas, ja brauks tikai 24 un 22 "
                 "skolēni?",
         "atb": ["4"], "padoms": "50 − (24 + 22)."},
    ], pamats=4,
        ievads="Ja kāda skaitļa trūkst, atbilde ir «nevar»."),

    Varianti("Kam pietiek datu?", [
        {"jaut": "Zināms: veikalā nopirka 3 klades pa 2 eiro. Ko var "
                 "aprēķināt?",
         "opcijas": ["Cik samaksāja par kladēm",
                     "Cik naudas palika makā",
                     "Cik klades maksāja pērn",
                     "Cik lappušu ir kladē"],
         "pareizi": 0,
         "padoms": "Pietiek tikai tam, kam ir visi skaitļi."},
        {"jaut": "Zināms: klasē 24 skolēni, no tiem 13 meitenes. Ko var "
                 "aprēķināt?",
         "opcijas": ["Cik ir zēnu", "Cik skolēnu ir paralēlklasē",
                     "Cik meiteņu nāks rīt", "Cik skolēnu mīl matemātiku"],
         "pareizi": 0,
         "padoms": "24 − 13."},
        {"jaut": "Kāpēc nedrīkst pašam izdomāt trūkstošo skaitli?",
         "opcijas": ["Atbilde vairs nav par šo situāciju",
                     "Tas ir garāks risinājums",
                     "Skolotājs neredzēs",
                     "Drīkst, ja skaitlis ir apaļš"],
         "pareizi": 0,
         "padoms": "Izdomāts skaitlis dod izdomātu atbildi."},
        {"jaut": "Zināms: autobusā 50 vietas un brauc 72 skolēni. Ko var "
                 "aprēķināt?",
         "opcijas": ["Ka vienā autobusā visi neietilpst",
                     "Cik maksā autobuss",
                     "Cik ilgi jābrauc",
                     "Cik skolēnu sēdēs kopā"],
         "pareizi": 0,
         "padoms": "Salīdzini 72 ar 50."},
    ], pamats=4),

    Pasaule("Ko var uzzināt par ēdnīcu?",
            Ievadi("", [
                {"jaut": "Ēdnīcā ir 12 galdi, pie katra 6 vietas. Cik vietu "
                         "pavisam?",
                 "atb": ["72"], "padoms": "12 · 6."},
                {"jaut": "Pusdienās nāca 258 skolēni divās maiņās, pirmajā "
                         "140. Cik bija otrajā?",
                 "atb": ["118"], "padoms": "258 − 140."},
                {"jaut": "Cik ilgi katrs skolēns ēda? Raksti skaitli vai "
                         "«nevar».",
                 "atb": ["nevar"], "padoms": "Par laiku nav neviena skaitļa."},
                {"jaut": "Otrajā maiņā nāca 118 skolēni, bet vietu ir 72. "
                         "Par cik cilvēkiem vietu pietrūka?",
                 "atb": ["46"], "padoms": "118 − 72."},
            ]),
            pavediens="skola",
            konteksts="Skolas dati gandrīz nekad nav salikti tā, kā vajag - "
                      "daļa ir, daļas trūkst.",
            kapec="Vispirms noskaidro, kas ir zināms; tikai tad rēķini."),

    Kopsavilkums([
        "Izlasu situācijas aprakstu bez jautājuma un izrakstu zināmos datus.",
        "Spriežu, kuriem jautājumiem datu pietiek un kuriem ne.",
        "Atbildu «nevar aprēķināt», ja datu trūkst, un nepieņemu skaitļus "
        "pats.",
    ]),

    Majas([
        "Uzraksti par savu dienu piecu teikumu aprakstu ar skaitļiem, bez "
        "jautājuma.",
        "Pieraksti trīs jautājumus, uz kuriem no tā var atbildēt, un divus, "
        "uz kuriem nevar.",
        "Iedod aprakstu draugam un salīdziniet jautājumus.",
    ]),
]
