# -*- coding: utf-8 -*-
"""6. klase, 161. stunda: «Kad izmantot kalkulatoru?»

Kalkulators nav aizliegts un nav arī risinājums. Tas ir rīks, kuram ir sava
vieta: garos skaitļos un pārbaudē. Bet tas neatbild uz jautājumu, kura
darbība vajadzīga, un tieši to skolēns izlemj pats.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti)

TEMA = "Kad izmantot kalkulatoru?"

MERKIS = ("Izlemsim, kad kalkulators palīdz un kad rēķināt ātrāk ir pašam.")

SATURS = [
    Sakums("Kalkulators nezina, ko tu meklē",
           fakti=["Kalkulators izpilda darbību, bet neizvēlas to.",
                  "Novērtējums vajadzīgs arī tad, kad rēķina mašīna.",
                  "Ievadot skaitli greizi, arī atbilde būs greiza."]),

    Doma("Vispirms plāns, tad rīks",
         "Kalkulatoru lieto tad, kad darbība ir izvēlēta un skaitļi ir "
         "gari; galvā rēķina tad, kad skaitļi ir apaļi vai zināmi.",
         soli=[
             "Izlem, kura darbība vajadzīga.",
             "Novērtē, kāda būs atbilde.",
             "Ja skaitļi ir apaļi, rēķini galvā.",
             "Ja gari - ievadi kalkulatorā uzmanīgi.",
             "Salīdzini rezultātu ar novērtējumu.",
         ],
         pieze="Negatīvus skaitļus kalkulatorā ievada ar īpašu taustiņu, "
               "nevis ar atņemšanas zīmi. Ja to sajauc, rezultāts ir "
               "pavisam cits."),

    Paraugs("Kad rēķināt pašam",
            uzd="Kuras no šīm darbībām der galvas rēķinam: 25 · 4; "
                "1234 · 56; 0,5 · 88; (−3) · (−7)?",
            soli=[
                ("25 · 4 = 100",
                 "Apaļi skaitļi - galvā."),
                ("1234 · 56",
                 "Gari skaitļi - kalkulators."),
                ("0,5 · 88 = 44",
                 "Puse no 88 - galvā."),
                ("(−3) · (−7) = 21",
                 "Mazi skaitļi - galvā."),
            ],
            atbilde="trīs no četrām der galvas rēķinam"),

    Ievadi("Rēķini galvā", [
        {"jaut": "Cik ir 25 · 4?",
         "atb": ["100"], "padoms": "Apaļs rezultāts."},
        {"jaut": "Cik ir 0,5 · 88?",
         "atb": ["44"], "padoms": "Puse no 88."},
        {"jaut": "Cik ir (−3) · (−7)?",
         "atb": ["21"], "padoms": "Vienādas zīmes."},
        {"jaut": "Cik apmēram ir 1234 · 56? Raksti tūkstošos, piemēram "
                 "70000.",
         "atb": ["70000", "70 000"], "padoms": "1200 · 60."},
        {"jaut": "Cik ir 0,25 · 40?",
         "atb": ["10"], "padoms": "Ceturtdaļa no 40."},
        {"jaut": "Cik ir (−100) : 4?",
         "atb": ["-25", "−25"], "padoms": "Apaļs skaitlis."},
    ], pamats=4,
        ievads="Pirms lietot kalkulatoru, pamēģini galvā."),

    Petijums("Pārbaudi kalkulatoru",
             vajag="kalkulators un burtnīca",
             soli=[
                 "Izvēlies piecas darbības ar negatīviem skaitļiem.",
                 "Katrai vispirms pieraksti novērtējumu.",
                 "Izrēķini tās kalkulatorā.",
                 "Salīdzini ar novērtējumu.",
                 "Atzīmē, kurās kalkulatorā ievadīji skaitli greizi.",
             ],
             secinajums="Kalkulators kļūdās reti - kļūdās tas, kurš ievada. "
                        "Tāpēc novērtējums vajadzīgs arī tad."),

    Varianti("Kalkulators vai galva?", [
        {"jaut": "Kalkulators neatbild uz jautājumu...",
         "opcijas": ["kura darbība ir vajadzīga",
                     "cik ir reizinājums", "cik ir dalījums",
                     "cik ir summa"],
         "pareizi": 0,
         "padoms": "Darbību izvēlas cilvēks."},
        {"jaut": "Kad novērtējums ir vajadzīgs?",
         "opcijas": ["Vienmēr, arī ar kalkulatoru",
                     "Tikai bez kalkulatora",
                     "Tikai lieliem skaitļiem", "Nekad"],
         "pareizi": 0,
         "padoms": "Tas pamana ievades kļūdu."},
        {"jaut": "Cik ir 0,5 · 88?",
         "opcijas": ["44", "4,4", "440", "88,5"],
         "pareizi": 0,
         "padoms": "Puse."},
        {"jaut": "Kā kalkulatorā ievada negatīvu skaitli?",
         "opcijas": ["Ar zīmes maiņas taustiņu",
                     "Ar atņemšanas zīmi",
                     "Ar iekavām", "Nevar ievadīt"],
         "pareizi": 0,
         "padoms": "Atņemšana ir cita darbība."},
    ], pamats=4),

    Pasaule("Vai rēķins ir ticams?",
            Ievadi("", [
                {"jaut": "24 preces pa 1,5 €. Cik apmēram eiro? Raksti "
                         "veselu skaitli.",
                 "atb": ["36"], "padoms": "24 · 1,5."},
                {"jaut": "Kalkulators rāda 360. Vai tas ir ticami? Raksti "
                         "«jā» vai «nē».",
                 "atb": ["nē", "ne"], "padoms": "Desmitkārt par daudz."},
                {"jaut": "Kur visticamāk ir kļūda? Raksti «ievadē» vai "
                         "«kalkulatorā».",
                 "atb": ["ievadē", "ievade"], "padoms": "Komats pazudis."},
                {"jaut": "Cik eiro maksā 24 preces pa 15 €?",
                 "atb": ["360"], "padoms": "Tad 360 būtu pareizi."},
            ]),
            pavediens="veikals",
            konteksts="Kases kļūdu pamana tas, kurš novērtēja summu jau "
                      "pirms tam.",
            kapec="Novērtējums ir vienīgā pārbaude, kas strādā uzreiz."),

    Kopsavilkums([
        "Izlemju, kura darbība vajadzīga, pirms ņemu kalkulatoru.",
        "Novērtēju atbildi arī tad, kad rēķina mašīna.",
        "Rēķinu galvā apaļus un zināmus skaitļus.",
        "Pamanu ievades kļūdu, salīdzinot ar novērtējumu.",
    ]),

    Majas([
        "Izrēķini galvā 0,25 · 80; 50 · 6; (−4) · (−9).",
        "Izrēķini kalkulatorā 1276 · 43 un pieraksti novērtējumu.",
        "Pieraksti, cik tālu novērtējums bija no rezultāta.",
    ]),
]
