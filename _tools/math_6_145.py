# -*- coding: utf-8 -*-
"""6. klase, 145. stunda: «Cik droši jau protu?»

Temata pēdējā mācību stunda pirms pārbaudes darba. Jaunu likumu nav - ir
patstāvīgs darbs ar visiem skaitļu veidiem un ar pašvērtējumu: kura vieta
vēl jāatkārto.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti)

TEMA = "Cik droši jau protu?"

MERKIS = ("Patstāvīgi aprēķināsim izteiksmju vērtības ar pozitīviem un "
          "negatīviem skaitļiem.")

SATURS = [
    Sakums("Pārbaudi sevi pirms pārbaudes darba",
           fakti=["Zīmju likums ir viens visiem skaitļu veidiem.",
                  "Daļām vajag kopsaucēju, decimāldaļām - līdzinātus "
                  "komatus.",
                  "Katru atbildi var pārbaudīt ar pretējo darbību."]),

    Doma("Viens likums, trīs pieraksti",
         "Saskaitīšana un atņemšana ar zīmēm strādā vienādi veseliem "
         "skaitļiem, parastajām daļām un decimāldaļām; atšķiras tikai "
         "sagatavošanās solis.",
         soli=[
             "Nosaki, kāda veida skaitļi ir izteiksmē.",
             "Veseliem skaitļiem sāc uzreiz ar zīmju likumu.",
             "Parastajām daļām vispirms atrodi kopsaucēju.",
             "Decimāldaļām līdzini komatus.",
             "Tad lieto to pašu zīmju likumu un pārbaudi atbildi.",
         ],
         pieze="Ja izteiksmē ir gan daļas, gan decimāldaļas, vispirms "
               "izvēlas vienu pierakstu. Citādi kopsaucējs un komats "
               "sanāk vienā rindā, un kļūda ir gandrīz droša."),

    Paraugs("Trīs izteiksmes pēc kārtas",
            uzd="Izrēķini −8 + 5 − (−3); −{1|2} + {1|4}; −2,4 + 0,9.",
            soli=[
                ("−8 + 5 + 3 = 0",
                 "Veseli skaitļi: uzreiz zīmju likums."),
                ("−{2|4} + {1|4} = −{1|4}",
                 "Daļas: vispirms kopsaucējs."),
                ("2,4 − 0,9 = 1,5, zīme mīnus",
                 "Decimāldaļas: līdzina komatus."),
                ("Rezultāts: 0; −{1|4}; −1,5",
                 "Viens likums, trīs sagatavošanās veidi."),
            ],
            atbilde="0; −{1|4}; −1,5"),

    Ievadi("Izrēķini patstāvīgi", [
        {"jaut": "Cik ir −8 + 5 − (−3)?",
         "atb": ["0"], "padoms": "−8 + 8."},
        {"jaut": "Cik ir −{1|2} + {1|4}? Atbildi raksti kā a/b.",
         "atb": ["-1/4", "−1/4"], "padoms": "Kopsaucējs 4."},
        {"jaut": "Cik ir −2,4 + 0,9?",
         "atb": ["-1,5", "−1,5", "-1.5"], "padoms": "2,4 − 0,9."},
        {"jaut": "Cik ir 7 − 13 + (−2)?",
         "atb": ["-8", "−8"], "padoms": "7 un −15."},
        {"jaut": "Cik ir −{3|4} − (−{1|4})? Atbildi raksti kā a/b.",
         "atb": ["-1/2", "−1/2", "-2/4", "−2/4"], "padoms": "−3 + 1 "
                                                            "ceturtdaļās."},
        {"jaut": "Cik ir −0,5 − (−1,5)?",
         "atb": ["1"], "padoms": "−0,5 + 1,5."},
    ], pamats=4,
        ievads="Katrai atbildei vispirms pasaki, kāda būs zīme."),

    Petijums("Izveido savu atkārtošanās lapu",
             vajag="burtnīca un šī temata uzdevumi",
             soli=[
                 "Izvēlies pa vienam uzdevumam no katras temata stundas.",
                 "Atrisini tos patstāvīgi, nelūkojoties piezīmēs.",
                 "Atzīmē tos, kuros kļūdījies.",
                 "Pieraksti katrai kļūdai cēloni: zīme, kopsaucējs vai "
                 "komats.",
                 "Atkārto tikai tās vietas, kur kļūdas atkārtojās.",
             ],
             secinajums="Atkārtot visu nav vajadzīgs - pietiek ar tām divām "
                        "trim vietām, kur kļūdas atkārtojas."),

    Varianti("Kas jādara vispirms?", [
        {"jaut": "Izteiksmē ar parastajām daļām pirmais solis ir...",
         "opcijas": ["atrast kopsaucēju", "lietot zīmju likumu",
                     "saīsināt", "pārbaudīt atbildi"],
         "pareizi": 0,
         "padoms": "Bez kopsaucēja skaitītājus saskaitīt nevar."},
        {"jaut": "Izteiksmē ar decimāldaļām pirmais solis ir...",
         "opcijas": ["līdzināt komatus", "atrast kopsaucēju",
                     "noapaļot", "saīsināt"],
         "pareizi": 0,
         "padoms": "Vietas vērtībām jāsakrīt."},
        {"jaut": "Ja izteiksmē ir gan daļas, gan decimāldaļas, vispirms...",
         "opcijas": ["izvēlas vienu pierakstu", "rēķina no kreisās uz labo",
                     "noapaļo visu", "izlaiž grūtāko"],
         "pareizi": 0,
         "padoms": "Viens pieraksts - viens likums."},
        {"jaut": "Zīmju likums ir...",
         "opcijas": ["viens visiem skaitļu veidiem",
                     "citāds daļām", "citāds decimāldaļām",
                     "atkarīgs no uzdevuma"],
         "pareizi": 0,
         "padoms": "Atšķiras tikai sagatavošanās."},
    ], pamats=4),

    Pasaule("Kāds ir kopējais rezultāts?",
            Ievadi("", [
                {"jaut": "Kontā: −45,50 €, iemaksā 60 €. Cik eiro ir kontā?",
                 "atb": ["14,5", "14,50", "14.5"], "padoms": "60 − 45,5."},
                {"jaut": "Tad rēķins 20,50 €. Cik eiro ir kontā?",
                 "atb": ["-6", "−6"], "padoms": "14,5 − 20,5."},
                {"jaut": "Temperatūra: −3,5 °C, pazeminās par 2,5 grādiem. "
                         "Cik grādu ir?",
                 "atb": ["-6", "−6"], "padoms": "−3,5 − 2,5."},
                {"jaut": "Par cik grādiem tai jāpaaugstinās, lai būtu 0 °C?",
                 "atb": ["6"], "padoms": "Modulis."},
            ]),
            pavediens="veikals",
            konteksts="Īstajos aprēķinos skaitļi reti ir veseli - tāpēc "
                      "zīmju likums jāprot visiem pierakstiem.",
            kapec="Viens likums der visur, ja sagatavošanās ir pareiza."),

    Kopsavilkums([
        "Patstāvīgi aprēķinu izteiksmes ar visu veidu skaitļiem.",
        "Zinu, ar ko jāsāk katram pieraksta veidam.",
        "Pārbaudu katru atbildi ar pretējo darbību.",
        "Zinu, kuras vietas man vēl jāatkārto.",
    ]),

    Majas([
        "Izrēķini piecas izteiksmes: divas ar veseliem, divas ar daļām, "
        "vienu ar decimāldaļām.",
        "Atzīmē tās, kurās nebiji drošs.",
        "Pieraksti, ko atkārtosi pirms pārbaudes darba.",
    ]),
]
