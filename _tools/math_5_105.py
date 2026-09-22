# -*- coding: utf-8 -*-
"""5. klase, 105. stunda: «Kā izmantot jauktus skaitļus dzīvē?»

Stunda, kurā viss temats saliekas kopā: uzdevumā ir vairākas darbības,
mērvienības un jautājums, kas prasa atbildi teikumā. Grūtākais te nav rēķins,
bet secība - tāpēc 83. stundas četri soļi paliek spēkā, tikai skaitļi tagad
ir jaukti.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā izmantot jauktus skaitļus dzīvē?"

MERKIS = ("Mācīsimies risināt situācijas uzdevumu ar jauktiem skaitļiem un "
          "mērvienībām, izpildot līdz trim darbībām.")

SATURS = [
    Sakums("Trīs dienas, viens jautājums",
           zimejums=restis([["2 1/2", "1 3/4", "3 1/4"]],
                           virsraksts="Pirmdiena, otrdiena, trešdiena"),
           paraksts="Kopā 7{1|2} km - bet to vajag izrēķināt trīs soļos.",
           fakti=["Katras dienas attālums ir jaukts skaitlis.",
                  "Saucēji atšķiras, tāpēc vajadzīgs kopsaucējs.",
                  "Atbilde ir teikums ar mērvienību."]),

    Doma("Viens jautājums, vairākas darbības",
         "Situācijas uzdevumā ar jauktiem skaitļiem izraksta doto, plāno "
         "darbību secību, izpilda tās pa vienai un atbild teikumā.",
         soli=[
             "Izraksti, kas dots un kas jāatrod.",
             "Nosaki, cik darbību vajadzēs.",
             "Izpildi darbības pa vienai, katru savā rindā.",
             "Novērtē, vai atbilde ir ticama.",
             "Uzraksti atbildi ar mērvienību.",
         ],
         pieze="Ja darbību ir vairākas, starprezultātus neaizmirst pierakstīt "
               "ar mērvienību. Tieši tur pazūd kilometri un paliek tikai "
               "skaitļi, kurus vēlāk vairs nevar salikt kopā."),

    Paraugs("Trīs dienu kopgarums",
            uzd="Pirmdien noskrieti 2{1|2} km, otrdien 1{3|4} km, trešdien "
                "3{1|4} km. Cik kilometru kopā?",
            soli=[
                ("Kopsaucējs ir 4",
                 "4 dalās ar 2 un 4."),
                ("2{2|4} + 1{3|4} = 3{5|4} = 4{1|4}",
                 "Pirmās divas dienas."),
                ("4{1|4} + 3{1|4} = 7{2|4}",
                 "Pieskaita trešo dienu."),
                ("7{2|4} = 7{1|2}",
                 "Saīsina rezultātu."),
                ("Atbilde: 7{1|2} km",
                 "Teikums ar mērvienību."),
            ],
            atbilde="Kopā noskrieti 7{1|2} km"),

    Ievadi("Rēķini pa soļiem", [
        {"jaut": "2{1|2} + 1{3|4} = ? Atbildi raksti kā a b/c.",
         "atb": ["4 1/4"], "padoms": "2{2|4} + 1{3|4} = 3{5|4}."},
        {"jaut": "4{1|4} + 3{1|4} = ? Atbildi raksti kā a b/c.",
         "atb": ["7 1/2", "7 2/4"], "padoms": "{2|4} = {1|2}."},
        {"jaut": "Plānoti 10 km, noskrieti 7{1|2} km. Cik palicis? Atbildi "
                 "raksti kā a b/c.",
         "atb": ["2 1/2"], "padoms": "10 = 9{2|2}."},
        {"jaut": "1{1|3} + 2{1|6} = ? Atbildi raksti kā a b/c.",
         "atb": ["3 1/2", "3 3/6"], "padoms": "{2|6} + {1|6} = {3|6}."},
        {"jaut": "5 - 1{2|5} = ? Atbildi raksti kā a b/c.",
         "atb": ["3 3/5"], "padoms": "5 = 4{5|5}."},
        {"jaut": "3{1|2} + 2{1|2} = ? Ieraksti skaitli.",
         "atb": ["6"], "padoms": "{2|2} = 1."},
        {"jaut": "Trīs reizes pa 1{1|2} km. Cik kilometru kopā? Atbildi "
                 "raksti kā a b/c.",
         "atb": ["4 1/2"], "padoms": "1{1|2} + 1{1|2} + 1{1|2}."},
        {"jaut": "Četras reizes pa {3|4} h. Cik stundas kopā? Ieraksti "
                 "skaitli.",
         "atb": ["3"], "padoms": "{12|4} = 3."},
    ], pamats=4,
        ievads="Katru soli izpildi atsevišķi un pieraksti ar mērvienību."),

    Zimejums("Trīs starprezultāti",
             restis([["4 1/4", "7 1/2", "2 1/2"]],
                    virsraksts="Pēc pirmā, otrā un trešā soļa"),
             paskaidro="Pirmais skaitlis ir divu dienu summa, otrais - trīs "
                       "dienu, trešais - cik vēl trūkst līdz 10 km.",
             ievads="Katrs solis dod savu skaitli, un neviens nepazūd."),

    Varianti("Kā risina daudzsoļu uzdevumu?", [
        {"jaut": "Ar ko sāk?",
         "opcijas": ["Izraksta doto un prasīto", "Sāk rēķināt",
                     "Uzraksta atbildi", "Novērtē"],
         "pareizi": 0,
         "padoms": "Vispirms jāsaprot uzdevums."},
        {"jaut": "Kāpēc starprezultātus raksta ar mērvienību?",
         "opcijas": ["Lai vēlāk zinātu, ko ar ko saskaitīt",
                     "Lai pieraksts būtu garāks",
                     "Lai atbilde būtu precīzāka",
                     "Tas nav vajadzīgs"],
         "pareizi": 0,
         "padoms": "Kilometri un stundas nesaskaitās."},
        {"jaut": "Cik ir 2{1|2} + 1{3|4}?",
         "opcijas": ["4{1|4}", "3{4|6}", "3{5|4} un tas ir galīgi",
                     "4{3|4}"],
         "pareizi": 0,
         "padoms": "3{5|4} = 4{1|4}."},
        {"jaut": "Plānoti 10 km, noskrieti 7{1|2} km. Cik palicis?",
         "opcijas": ["2{1|2} km", "3{1|2} km", "2 km", "17{1|2} km"],
         "pareizi": 0,
         "padoms": "10 - 7{1|2}."},
        {"jaut": "Kā pārbaudīt, vai atbilde ir ticama?",
         "opcijas": ["Novērtēt ar noapaļotiem skaitļiem",
                     "Pārrakstīt atbildi",
                     "Saīsināt daļu",
                     "Pārbaudīt nevar"],
         "pareizi": 0,
         "padoms": "100. stundas paņēmiens."},
        {"jaut": "Kā izskatās atbilde?",
         "opcijas": ["Teikums ar skaitli un mērvienību", "Tikai skaitlis",
                     "Tikai daļa", "Izteiksme"],
         "pareizi": 0,
         "padoms": "Atbild uz uzdoto jautājumu."},
    ], pamats=4),

    Pasaule("Nedēļas treniņu plāns",
            Ievadi("", [
                {"jaut": "Pirmdien 2{1|2} km, otrdien 1{3|4} km. Cik kopā? "
                         "Atbildi raksti kā a b/c.",
                 "atb": ["4 1/4"], "padoms": "2{2|4} + 1{3|4}."},
                {"jaut": "Trešdien vēl 3{1|4} km. Cik kopā trijās dienās? "
                         "Atbildi raksti kā a b/c.",
                 "atb": ["7 1/2", "7 2/4"], "padoms": "4{1|4} + 3{1|4}."},
                {"jaut": "Nedēļas mērķis ir 10 km. Cik vēl jānoskrien? "
                         "Atbildi raksti kā a b/c.",
                 "atb": ["2 1/2"], "padoms": "10 - 7{1|2}."},
                {"jaut": "Ja atlikušo sadala divās vienādās dienās, cik "
                         "kilometru katrā? Atbildi raksti kā a b/c.",
                 "atb": ["1 1/4"], "padoms": "Puse no 2{1|2} km."},
            ]),
            pavediens="sports",
            konteksts="Treniņu plānā ir gan kopsumma, gan atlikums, gan "
                      "sadalījums pa dienām.",
            kapec="Trīs darbības pēc kārtas atbild uz visiem trim "
                  "jautājumiem."),

    Kopsavilkums([
        "Izrakstu uzdevuma doto un prasīto.",
        "Plānoju, cik darbību un kādā secībā vajadzēs.",
        "Pierakstu katru starprezultātu ar mērvienību.",
        "Novērtēju atbildi un uzrakstu to teikumā.",
    ]),

    Majas([
        "Atrisini: pirmdien 3{1|4} h, otrdien 2{1|2} h, trešdien 1{3|4} h. "
        "Cik stundu kopā?",
        "Izdomā uzdevumu ar trim darbībām par savu nedēļu.",
        "Pārbaudi savu atbildi ar novērtējumu.",
    ]),
]
