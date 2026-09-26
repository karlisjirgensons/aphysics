# -*- coding: utf-8 -*-
"""3. klase, 96. stunda: «Kurš apgalvojums ir patiess?»

Mikrotemata noslēgums. Skolēns nevis rēķina, bet *spriež*: apgalvojums par
daļām jāpamato ar modeli vai jāapgāž ar pretpiemēru. Pretpiemērs te parādās
pirmo reizi kā pilnvērtīgs pierādījums.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kurš apgalvojums ir patiess?"

MERKIS = ("Izvērtēsim apgalvojumus par daļām un pamatosim tos ar modeli vai "
          "pretpiemēru.")

SATURS = [
    Sakums("Vai apgalvojumu var apgāzt ar vienu piemēru?",
           zimejums=restis([["apgalvojums", "spriedums"],
                            ["Lielāks saucējs - lielāka daļa", "aplams"],
                            ["1/8 < 1/4", "patiess"]],
                           "divi apgalvojumi"),
           paraksts="Lai apgāztu apgalvojumu, pietiek ar vienu pretpiemēru.",
           fakti=["Lai apgalvojums būtu patiess, tam jāder vienmēr.",
                  "Lai to apgāztu, pietiek ar vienu gadījumu, kad tas neder."]),

    Doma("Viens pretpiemērs apgāž apgalvojumu",
         "Patiess apgalvojums der visos gadījumos; aplamam pietiek ar vienu "
         "izņēmumu.",
         soli=[
             "Izlasi apgalvojumu un saproti, par ko tas runā.",
             "Izmēģini to uz diviem trim piemēriem.",
             "Ja kaut vienā tas neder, apgalvojums ir aplams.",
             "Pamato atbildi ar modeli vai skaitļiem.",
         ],
         pieze="Pretpiemērs jāizvēlas pēc iespējas vienkāršāks: {1|2} un "
               "{1|4} pietiek, lai apgāztu «lielāks saucējs - lielāka daļa»."),

    Paraugs("Vai apgalvojums ir patiess?",
            uzd="«Jo lielāks saucējs, jo lielāka daļa.» Vai tas ir patiess?",
            soli=[
                ("Pārbauda ar {1|2} un {1|4}",
                 "Saucēji 2 un 4."),
                ("{1|2} > {1|4}",
                 "Lielāks saucējs dod *mazāku* daļu."),
                ("Apgalvojums ir aplams",
                 "Pietiek ar šo vienu pretpiemēru."),
            ],
            atbilde="aplams; pretpiemērs {1|2} > {1|4}"),

    Petijums("Atrodi pretpiemēru",
             vajag="lapa un zīmulis",
             soli=[
                 "Izvēlies vienu apgalvojumu par daļām.",
                 "Izmēģini to uz trim dažādām daļām.",
                 "Ja atrodi gadījumu, kad tas neder, pieraksti to.",
                 "Uzzīmē modeli, kas pretpiemēru parāda.",
             ],
             secinajums="Viens skaidrs pretpiemērs ir pilnvērtīgs "
                        "pierādījums, ka apgalvojums ir aplams."),

    Ievadi("Pārbaudi ar skaitļiem", [
        {"jaut": "Cik ir {1|2} no 12?", "atb": ["6"], "padoms": "12 : 2."},
        {"jaut": "Cik ir {1|4} no 12?", "atb": ["3"], "padoms": "12 : 4."},
        {"jaut": "Kurš skaitlis ir lielāks - {1|2} vai {1|4} no 12? "
                 "Ieraksti lielāko.",
         "atb": ["6"], "padoms": "6 > 3."},
        {"jaut": "Cik ir {3|4} no 12?", "atb": ["9"], "padoms": "3 · 3."},
        {"jaut": "Cik ir {2|3} no 12?", "atb": ["8"], "padoms": "2 · 4."},
        {"jaut": "Kurš skaitlis ir lielāks - {3|4} vai {2|3} no 12? "
                 "Ieraksti lielāko.",
         "atb": ["9"], "padoms": "9 > 8."},
    ], pamats=4),

    Zimejums("Pretpiemērs zīmējumā",
             restis([["1/2 no 12", 6],
                     ["1/4 no 12", 3]],
                    "lielāks saucējs, mazāka daļa"),
             paskaidro="Skaitļi parāda to pašu, ko modelis: saucējs 4 dod "
                       "mazāku daļu nekā saucējs 2.",
             ievads="Tas pats pretpiemērs skaitļos."),

    Varianti("Patiess vai aplams?", [
        {"jaut": "«Jo lielāks saucējs, jo mazāka daļa.» Vai tas ir patiess?",
         "opcijas": ["Jā, ja skaitītāji ir vienādi", "Nē, nekad",
                     "Jā, vienmēr", "To nevar pateikt"],
         "pareizi": 0, "padoms": "Skaitītājiem jābūt vienādiem."},
        {"jaut": "«{3|4} vienmēr ir lielāks par {1|2}.» Vai tas ir patiess?",
         "opcijas": ["Jā, ja veselais ir viens un tas pats",
                     "Nē, nekad", "Jā, vienmēr", "Tikai lielām figūrām"],
         "pareizi": 0, "padoms": "Salīdzināt var tikai pie viena veselā."},
        {"jaut": "«Daļa vienmēr ir mazāka par 1.» Vai tas ir patiess?",
         "opcijas": ["Nē, {5|4} ir lielāks par 1", "Jā, vienmēr",
                     "Jā, ja saucējs ir liels", "To nevar pateikt"],
         "pareizi": 0, "padoms": "Pretpiemērs: {5|4}."},
        {"jaut": "Cik pretpiemēru vajag, lai apgāztu apgalvojumu?",
         "opcijas": ["Viens", "Divi", "Trīs", "Visi"],
         "pareizi": 0, "padoms": "Viens izņēmums pietiek."},
    ], pamats=4),

    Pasaule("Vai mežsarga apgalvojums ir pareizs?",
            Ievadi("", [
                {"jaut": "Mežā A 40 koki, {1|4} ir priedes. Cik priežu?",
                 "atb": ["10"], "padoms": "40 : 4."},
                {"jaut": "Mežā B 20 koki, {1|2} ir priedes. Cik priežu?",
                 "atb": ["10"], "padoms": "20 : 2."},
                {"jaut": "Vai abos mežos ir vienāds priežu skaits? Raksti "
                         "«jā» vai «nē».",
                 "atb": ["jā", "ja"], "padoms": "10 un 10.",
                 "tastatura": "text"},
                {"jaut": "Cik koku ir abos mežos kopā?", "atb": ["60"],
                 "padoms": "40 + 20."},
            ]),
            pavediens="daba",
            konteksts="Mazāka daļa no lielāka meža var dot tikpat koku, cik "
                      "lielāka daļa no maza meža.",
            kapec="Tieši tāpēc daļu nedrīkst salīdzināt, nezinot veselo."),

    Kopsavilkums([
        "Izvērtēju apgalvojumus par daļām.",
        "Pamatoju patiesu apgalvojumu ar modeli.",
        "Apgāžu aplamu apgalvojumu ar pretpiemēru.",
        "Zinu, ka viens pretpiemērs ir pietiekams.",
    ]),

    Majas([
        "Izvērtē apgalvojumu «{1|3} vienmēr ir lielāks par {1|4}».",
        "Atrodi pretpiemēru apgalvojumam «daļa vienmēr ir maza».",
        "Uzraksti savu apgalvojumu par daļām un pārbaudi to.",
    ]),
]
