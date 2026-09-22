# -*- coding: utf-8 -*-
"""6. klase, 125. stunda: «Ko nozīmē zīme skaitļa priekšā?»

Stunda par pierakstu. Viens un tas pats mīnuss izteiksmē var nozīmēt divas
lietas: darbību vai skaitļa zīmi. Kamēr šī divējādība nav izrunāta, garas
izteiksmes ar negatīviem skaitļiem palikt neizlasāmas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Ko nozīmē zīme skaitļa priekšā?"

MERKIS = ("Mācīsimies lasīt un pierakstīt izteiksmes, skaidrojot zīmju "
          "divējādo nozīmi.")

SATURS = [
    Sakums("Viens mīnuss, divas nozīmes",
           zimejums=restis([["5", "−", "(−3)"],
                            ["darbība", "", "zīme"]]),
           paraksts="Pirmais mīnuss ir atņemšana, otrais - skaitļa zīme. "
                    "Tāpēc negatīvu skaitli raksta iekavās.",
           fakti=["Zīme var būt darbība vai skaitļa daļa.",
                  "Divas zīmes pēc kārtas neraksta - starp tām liek iekavas.",
                  "Izteiksmi lasa pa daļām: skaitlis, darbība, skaitlis."]),

    Doma("Vispirms atrodi darbības, tad skaitļus",
         "Izteiksmē katra zīme ir vai nu darbība starp diviem skaitļiem, vai "
         "arī skaitļa zīme; negatīvu skaitli aiz darbības raksta iekavās.",
         soli=[
             "Atrodi izteiksmē visas darbību zīmes.",
             "Paskaties, kas ir aiz katras darbības.",
             "Ja aiz darbības ir iekavas, tajās ir skaitlis ar savu zīmi.",
             "Izlasi izteiksmi vārdiem.",
             "Pieraksti to pašu ar iekavām, ja to trūkst.",
         ],
         pieze="«5 − (−3)» lasa: «no pieciem atņem mīnus trīs». «5 − 3» "
               "lasa: «no pieciem atņem trīs». Iekavas ir vienīgais, kas "
               "abus atšķir."),

    Paraugs("Izlasi izteiksmi",
            uzd="Izlasi vārdiem: −7 + (−2) un −7 − (−2).",
            soli=[
                ("−7 + (−2)",
                 "Skaitlim mīnus septiņi pieskaita mīnus divi."),
                ("= −9",
                 "Abi soļi pa kreisi."),
                ("−7 − (−2)",
                 "No mīnus septiņiem atņem mīnus divi."),
                ("= −5",
                 "Solis pa labi - tāpēc rezultāts lielāks."),
            ],
            atbilde="−9 un −5"),

    Ievadi("Izrēķini ar iekavām", [
        {"jaut": "Cik ir −7 + (−2)?",
         "atb": ["-9", "−9"], "padoms": "Abi soļi pa kreisi."},
        {"jaut": "Cik ir −7 − (−2)?",
         "atb": ["-5", "−5"], "padoms": "Atņemt negatīvu nozīmē pieskaitīt."},
        {"jaut": "Cik ir 5 + (−3)?",
         "atb": ["2"], "padoms": "Trīs soļi pa kreisi."},
        {"jaut": "Cik ir 5 − (−3)?",
         "atb": ["8"], "padoms": "Trīs soļi pa labi."},
        {"jaut": "Cik ir −4 + (−4)?",
         "atb": ["-8", "−8"], "padoms": "Divi vienādi soļi pa kreisi."},
        {"jaut": "Cik ir −4 − (−4)?",
         "atb": ["0"], "padoms": "Pretēju skaitļu starpība."},
    ], pamats=4),

    Varianti("Kas tā par zīmi?", [
        {"jaut": "Izteiksmē 5 − (−3) pirmais mīnuss ir...",
         "opcijas": ["darbība", "skaitļa zīme",
                     "kļūda", "iekavas"],
         "pareizi": 0,
         "padoms": "Starp diviem skaitļiem."},
        {"jaut": "Otrais mīnuss tajā pašā izteiksmē ir...",
         "opcijas": ["skaitļa zīme", "darbība", "kļūda", "reizināšana"],
         "pareizi": 0,
         "padoms": "Tas ir iekavās."},
        {"jaut": "Kāpēc negatīvu skaitli raksta iekavās?",
         "opcijas": ["Lai divas zīmes nebūtu blakus",
                     "Lai izteiksme būtu garāka",
                     "Tā prasa likums", "Nav iemesla"],
         "pareizi": 0,
         "padoms": "5 −− 3 nav pieraksts."},
        {"jaut": "Kā lasa −7 + (−2)?",
         "opcijas": ["Mīnus septiņiem pieskaita mīnus divi",
                     "No mīnus septiņiem atņem divi",
                     "Septiņiem pieskaita divi",
                     "Mīnus septiņi reiz mīnus divi"],
         "pareizi": 0,
         "padoms": "Pluss ir darbība."},
    ], pamats=4),

    Pasaule("Ko rāda bankas izraksts?",
            Ievadi("", [
                {"jaut": "Kontā −50 €, pienāk ieraksts «+(−20) €». Cik eiro "
                         "ir kontā?",
                 "atb": ["-70", "−70"], "padoms": "−50 + (−20)."},
                {"jaut": "Tad atceļ maksājumu: «−(−20) €». Cik eiro ir "
                         "tagad?",
                 "atb": ["-50", "−50"], "padoms": "Atņemt negatīvu."},
                {"jaut": "Pienāk alga 120 €. Cik eiro ir kontā?",
                 "atb": ["70"], "padoms": "−50 + 120."},
                {"jaut": "Atceļ kļūdainu ieņēmumu 20 €. Cik eiro paliek?",
                 "atb": ["50"], "padoms": "70 − 20."},
            ]),
            pavediens="veikals",
            konteksts="Bankas izrakstā maksājuma atcelšana izskatās tieši kā "
                      "negatīva skaitļa atņemšana.",
            kapec="Atcelt izdevumu nozīmē naudu atgriezt - tāpēc rezultāts "
                  "aug."),

    Zimejums("Kad iekavas ir obligātas",
             restis([["−7 + (−2)", "−7 − (−2)"],
                     ["−9", "−5"]]),
             paskaidro="Tie paši skaitļi, bet cita darbība - un rezultāti "
                       "atšķiras par četriem.",
             ievads="Iekavas ir vienīgais, kas abas izteiksmes atšķir."),

    Kopsavilkums([
        "Atšķiru darbības zīmi no skaitļa zīmes.",
        "Rakstu negatīvu skaitli iekavās aiz darbības.",
        "Lasu izteiksmi vārdiem un aprēķinu tās vērtību.",
        "Pierakstu izteiksmi pareizi, ja tajā trūkst iekavu.",
    ]),

    Majas([
        "Izlasi vārdiem izteiksmes −3 + (−5) un −3 − (−5).",
        "Izrēķini abas un pieraksti, par cik tās atšķiras.",
        "Uzraksti trīs izteiksmes, kurās vajag iekavas.",
    ]),
]
