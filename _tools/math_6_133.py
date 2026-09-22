# -*- coding: utf-8 -*-
"""6. klase, 133. stunda: «Kā izlasīt garu izteiksmi?»

Izteiksme ar trim vai četrām darbībām ir pirmais uzdevums, kurā pirms
rēķināšanas jāizveido plāns. Skolēns vispirms izstāsta, ko darīs, un tikai
tad rēķina - tieši tā, kā to prasa arī turpmākajās klasēs.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā izlasīt garu izteiksmi?"

MERKIS = ("Lasīsim izteiksmi ar 3-4 darbībām, aprakstīsim veicamās darbības "
          "un aprēķināsim vērtību.")

SATURS = [
    Sakums("Vispirms plāns, tad rēķins",
           zimejums=restis([["−8", "+", "(−5)", "−", "(−6)", "+", "3"]]),
           paraksts="Četri saskaitāmie pēc pārveidošanas: −8; −5; +6; +3.",
           fakti=["Garu izteiksmi vispirms pārraksta par summu.",
                  "Tad sagrupē pozitīvos un negatīvos.",
                  "Iekavas ar darbību zīmi priekšā apstrādā vispirms."]),

    Doma("Pārraksti, sagrupē, saskaiti",
         "Garu izteiksmi risina trijos soļos: visas atņemšanas pārraksta kā "
         "saskaitīšanu, saskaitāmos sagrupē pēc zīmes un saskaita divas "
         "grupas.",
         soli=[
             "Izlasi izteiksmi un nosauc visas darbības.",
             "Pārraksti katru atņemšanu kā pretējā skaitļa pieskaitīšanu.",
             "Pieraksti visus saskaitāmos vienā rindā ar zīmēm.",
             "Saskaiti atsevišķi pozitīvos un negatīvos.",
             "Saskaiti abas summas.",
         ],
         pieze="Ja izteiksmē ir iekavas ar vairākiem saskaitāmajiem, tās "
               "izrēķina vispirms. Bez iekavām saskaitīšana un atņemšana "
               "notiek no kreisās uz labo - bet grupēšana to atvieglo."),

    Paraugs("Četras darbības",
            uzd="Cik ir −8 + (−5) − (−6) + 3?",
            soli=[
                ("−8 + (−5) − (−6) + 3",
                 "Sākotnējā izteiksme."),
                ("= −8 + (−5) + 6 + 3",
                 "Atņemšanu pārraksta."),
                ("Pozitīvie: 6 + 3 = 9",
                 "Pirmā grupa."),
                ("Negatīvie: −8 + (−5) = −13",
                 "Otrā grupa."),
                ("9 + (−13) = −4",
                 "Beigu darbība."),
            ],
            atbilde="−4"),

    Ievadi("Izrēķini garu izteiksmi", [
        {"jaut": "Cik ir −8 + (−5) − (−6) + 3?",
         "atb": ["-4", "−4"], "padoms": "9 un −13."},
        {"jaut": "Cik ir 5 − 8 + (−2)?",
         "atb": ["-5", "−5"], "padoms": "5 un −10."},
        {"jaut": "Cik ir −3 − (−7) + (−4)?",
         "atb": ["0"], "padoms": "7 un −7."},
        {"jaut": "Cik ir 10 − (−2) − 15?",
         "atb": ["-3", "−3"], "padoms": "12 un −15."},
        {"jaut": "Cik ir −6 + 9 − (−1) − 8?",
         "atb": ["-4", "−4"], "padoms": "10 un −14."},
        {"jaut": "Cik ir (−4 + 9) − (3 − 8)?",
         "atb": ["10"], "padoms": "5 − (−5)."},
    ], pamats=4,
        ievads="Vispirms izstāsti, ko darīsi, tikai tad rēķini."),

    Varianti("Ar ko sākt?", [
        {"jaut": "Izteiksmē ar iekavām vispirms izrēķina...",
         "opcijas": ["iekavas", "pirmo darbību",
                     "pēdējo darbību", "negatīvos skaitļus"],
         "pareizi": 0,
         "padoms": "Iekavas vienmēr pirmās."},
        {"jaut": "Bez iekavām saskaitīšanu un atņemšanu veic...",
         "opcijas": ["no kreisās uz labo", "no labās uz kreiso",
                     "vispirms saskaitīšanu", "vispirms atņemšanu"],
         "pareizi": 0,
         "padoms": "Vienādas prioritātes darbības."},
        {"jaut": "−5 − (−3) pārrakstīts ir...",
         "opcijas": ["−5 + 3", "−5 − 3", "5 + 3", "5 − 3"],
         "pareizi": 0,
         "padoms": "Divas maiņas reizē."},
        {"jaut": "Kāpēc izdevīgi grupēt pēc zīmes?",
         "opcijas": ["Jo zīme mainās tikai vienu reizi",
                     "Jo skaitļi kļūst mazāki",
                     "Jo tā ir ātrāk rakstīt", "Nav izdevīgi"],
         "pareizi": 0,
         "padoms": "Mazāk vietu, kur kļūdīties."},
    ], pamats=4),

    Pasaule("Kāds ir dienas rezultāts?",
            Ievadi("", [
                {"jaut": "Kontā: −80 + 150 − 40 + (−20) €. Cik eiro ir "
                         "ienākumi?",
                 "atb": ["150"], "padoms": "Tikai pozitīvie."},
                {"jaut": "Cik eiro ir izdevumi kopā?",
                 "atb": ["140"], "padoms": "80 + 40 + 20."},
                {"jaut": "Cik eiro ir kontā?",
                 "atb": ["10"], "padoms": "150 − 140."},
                {"jaut": "Ja vēl pienāktu rēķins 25 €, cik eiro būtu kontā?",
                 "atb": ["-15", "−15"], "padoms": "10 − 25."},
            ]),
            pavediens="veikals",
            konteksts="Dienas beigās konta izmaiņas ir viena gara izteiksme, "
                      "un atlikums ir tās vērtība.",
            kapec="Grupēšana pēc zīmes ir tieši tas, ko dara bankas "
                  "pārskats."),

    Zimejums("Izteiksme pēc pārrakstīšanas",
             restis([["−8", "−5", "+6", "+3"],
                     ["negatīvie", "", "pozitīvie", ""]]),
             paskaidro="Divas grupas: −13 un 9. Beigās paliek viena darbība.",
             ievads="Tā izskatās izteiksme pēc otrā soļa."),

    Kopsavilkums([
        "Izlasu garu izteiksmi un nosaucu visas darbības.",
        "Pārrakstu atņemšanas kā saskaitīšanas.",
        "Sagrupēju saskaitāmos pēc zīmes.",
        "Aprēķinu izteiksmes vērtību.",
    ]),

    Majas([
        "Izrēķini −9 + 4 − (−6) + (−2).",
        "Pieraksti visus soļus atsevišķās rindās.",
        "Izdomā savu izteiksmi ar četrām darbībām un atrisini to.",
    ]),
]
