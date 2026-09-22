# -*- coding: utf-8 -*-
"""5. klase, 83. stunda: «Kā atrisināt uzdevumu ar daļām?»

Mikrotemata noslēgums: viss, kas mācīts atsevišķi, te sastopas vienā
uzdevumā. Jaunā ir tikai kārtība - lasīt, zīmēt, rēķināt, atbildēt -, un
tieši tā ir tas, kas uzdevumu padara risināmu. Bez pirmā soļa pārējie trīs
neko nedod.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala)

TEMA = "Kā atrisināt uzdevumu ar daļām?"

MERKIS = ("Mācīsimies risināt situācijas uzdevumu, izsakot vienu skaitli kā "
          "otra skaitļa daļu.")

SATURS = [
    Sakums("Četri soļi, ne trīs",
           zimejums=dala(4, 3, "3/4 iztērēti"),
           paraksts="Lasi - zīmē - rēķini - atbildi. Tieši šādā secībā.",
           fakti=["Visbiežākā kļūda ir sākt ar rēķinu.",
                  "Zīmējums pasaka, ko ar ko dalīt.",
                  "Atbilde ir teikums, nevis skaitlis."]),

    Doma("Lasi, zīmē, rēķini, atbildi",
         "Uzdevumu ar daļām risina četros soļos: izlasa un pieraksta doto, "
         "uzzīmē shēmu, izrēķina un uzraksta atbildi ar mērvienību.",
         soli=[
             "Izraksti, kas dots un kas jāatrod.",
             "Nosaki veselo un uzzīmē joslu.",
             "Atrodi vienas daļas vērtību.",
             "Izrēķini prasīto.",
             "Uzraksti atbildi pilnā teikumā.",
         ],
         pieze="Ja uzdevumā zināms veselais, dala ar saucēju; ja zināma "
               "daļas vērtība, dala ar skaitītāju. Shēma uzreiz parāda, "
               "kurš no abiem gadījumiem ir šis."),

    Paraugs("No 32 € iztērēti {3|4}",
            uzd="Annai bija 32 €, viņa iztērēja {3|4}. Cik eiro palika?",
            soli=[
                ("Dots: 32 €, daļa {3|4}",
                 "Veselais un daļa."),
                ("Josla: 4 daļas, katra 8 €",
                 "32 : 4 = 8."),
                ("Iztērēti 8 · 3 = 24 (€)",
                 "Trīs ceturtdaļas."),
                ("Palika 32 - 24 = 8 (€)",
                 "Vai arī uzreiz: viena ceturtdaļa."),
                ("Atbilde: palika 8 €",
                 "Teikums ar mērvienību."),
            ],
            atbilde="Palika 8 €"),

    Ievadi("Atrisini uzdevumu", [
        {"jaut": "Bija 32 €, iztērēti {3|4}. Cik eiro iztērēti?",
         "atb": ["24"], "padoms": "32 : 4 · 3."},
        {"jaut": "Cik eiro palika?",
         "atb": ["8"], "padoms": "32 - 24."},
        {"jaut": "Bija 45 €, iztērēti {2|3}. Cik eiro iztērēti?",
         "atb": ["30"], "padoms": "45 : 3 · 2."},
        {"jaut": "Bija 60 €, iztērēta {1|5}. Cik eiro palika?",
         "atb": ["48"], "padoms": "60 - 12."},
        {"jaut": "Iztērēti 24 €, tas ir {3|5} naudas. Cik eiro bija sākumā?",
         "atb": ["40"], "padoms": "24 : 3 · 5."},
        {"jaut": "No 50 precēm pārdotas {3|10}. Cik preču pārdots?",
         "atb": ["15"], "padoms": "50 : 10 · 3."},
        {"jaut": "Cik preču palika nepārdotas?",
         "atb": ["35"], "padoms": "50 - 15."},
        {"jaut": "Pārdotas 18 preces, tas ir {2|5} no visām. Cik preču bija?",
         "atb": ["45"], "padoms": "18 : 2 · 5."},
    ], pamats=4,
        ievads="Vispirms izlasi, kas dots, tikai tad ķeries pie rēķina."),

    Zimejums("Kas iztērēts un kas palicis",
             dala(4, 3, "3/4"),
             paskaidro="Iekrāsotās trīs ceturtdaļas ir 24 €, tukšā "
                       "ceturtdaļa - 8 €. Abus skaitļus nolasa no vienas "
                       "shēmas.",
             ievads="Shēmā atbilde ir redzama pirms rēķina pabeigšanas."),

    Varianti("Kurš solis ir pirmais?", [
        {"jaut": "Ar ko sāk uzdevuma risināšanu?",
         "opcijas": ["Izraksta doto un prasīto", "Sāk rēķināt",
                     "Uzraksta atbildi", "Saīsina daļu"],
         "pareizi": 0,
         "padoms": "Vispirms jāsaprot uzdevums."},
        {"jaut": "Uzdevumā zināms veselais. Ko dara ar saucēju?",
         "opcijas": ["Dala veselo ar to", "Reizina veselo ar to",
                     "Atņem to", "Neko"],
         "pareizi": 0,
         "padoms": "Viena daļa = veselais : saucējs."},
        {"jaut": "Uzdevumā zināma daļas vērtība. Ko dara vispirms?",
         "opcijas": ["Dala vērtību ar skaitītāju",
                     "Dala vērtību ar saucēju",
                     "Reizina ar saucēju",
                     "Saskaita abus"],
         "pareizi": 0,
         "padoms": "Vispirms viena daļa."},
        {"jaut": "Kā izskatās pareiza atbilde?",
         "opcijas": ["Teikums ar skaitli un mērvienību",
                     "Tikai skaitlis",
                     "Tikai daļa",
                     "Zīmējums"],
         "pareizi": 0,
         "padoms": "Atbild uz uzdoto jautājumu."},
        {"jaut": "Bija 40 €, iztērēta {1|4}. Cik palika?",
         "opcijas": ["30 €", "10 €", "40 €", "4 €"],
         "pareizi": 0,
         "padoms": "40 - 10."},
        {"jaut": "Kāpēc shēmu zīmē pirms rēķina?",
         "opcijas": ["Tā redz, ko ar ko dalīt", "Tā ir tradīcija",
                     "Tā atbilde ir precīzāka", "Tas nav vajadzīgs"],
         "pareizi": 0,
         "padoms": "Shēma parāda uzdevuma uzbūvi."},
    ], pamats=4),

    Pasaule("Iepirkšanās ar sarakstu",
            Ievadi("", [
                {"jaut": "Budžets 60 €, pārtikai iztērēta {1|3}. Cik eiro?",
                 "atb": ["20"], "padoms": "60 : 3."},
                {"jaut": "Vēl {1|4} budžeta iztērēta drēbēm. Cik eiro?",
                 "atb": ["15"], "padoms": "60 : 4."},
                {"jaut": "Cik eiro palika?",
                 "atb": ["25"], "padoms": "60 - 20 - 15."},
                {"jaut": "Drēbēm iztērēti 15 €, tas ir {1|4} budžeta. Cik "
                         "eiro ir viss budžets?",
                 "atb": ["60"], "padoms": "15 · 4."},
            ]),
            pavediens="veikals",
            konteksts="Veikalā uzdevums nekad nav uzrakstīts - to saliek "
                       "pats no čeka un budžeta.",
            kapec="Kārtība «lasi, zīmē, rēķini, atbildi» der jebkuram "
                  "uzdevumam."),

    Kopsavilkums([
        "Izrakstu, kas uzdevumā dots un kas jāatrod.",
        "Uzzīmēju shēmu, pirms sāku rēķināt.",
        "Izvēlos pareizo rēķinu atkarībā no tā, kas ir zināms.",
        "Uzrakstu atbildi pilnā teikumā ar mērvienību.",
    ]),

    Majas([
        "Atrisini: bija 84 €, iztērētas {5|7}. Cik palika?",
        "Izdomā uzdevumu par savu kabatas naudu un atrisini to.",
        "Pieraksti četrus risināšanas soļus saviem vārdiem.",
    ]),
]
