# -*- coding: utf-8 -*-
"""6. klase, 6. stunda: «Ko var uzzināt no pieraksta 1 : 3 : 4?»

Pirmā stunda jaunā mikrotematā. Līdz šim attiecība tikai salīdzināja divus
lielumus; tagad no tās sāk rēķināt. Viss balstās uz vienu skaitli - cik
vienādu daļu ir kopā -, tāpēc tieši to šī stunda māca atrast.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums, dala)

TEMA = "Ko var uzzināt no pieraksta 1 : 3 : 4?"

MERKIS = ("Iemācīsimies no attiecības pieraksta noteikt, cik vienādu daļu "
          "ir kopā, un cik no tām pienākas katram.")

SATURS = [
    Sakums("Raķetes dzinējs strādā pēc attiecības",
           zimejums=dala(8, 1, "1 daļa ūdeņraža, 7 daļas skābekļa"),
           paraksts="Attiecība 1 : 7. Kopā ir 8 vienādas daļas.",
           fakti=["Dzinējā skābekli un ūdeņradi sajauc attiecībā ap 1 : 7.",
                  "Ja attiecību nesamēro, dzinējs vai nu smok, vai plīst.",
                  "Inženieris vispirms saskaita daļas, tikai tad tonnas."]),

    Doma("Vispirms saskaiti daļas",
         "Attiecības skaitļu summa pasaka, cik vienādu daļu ir visā kopumā.",
         soli=[
             "Saskaiti visus attiecības skaitļus - tas ir daļu skaits.",
             "Izdali kopumu ar daļu skaitu - tā ir viena daļa.",
             "Katram reizini vienu daļu ar viņa skaitli.",
             "Pārbaudi: visu daļu summai jābūt vienādai ar kopumu.",
         ],
         pieze="Attiecībā 1 : 3 : 4 kopā ir 8 daļas. Ja kopums ir 800 kg, "
               "viena daļa ir 100 kg - un tālāk viss ir reizināšana."),

    Slidnis("Viena daļa aug - attiecība paliek",
            [{"v": "1 daļa = 10 kg", "teksts": "10 kg : 30 kg : 40 kg, "
                                               "kopā 80 kg", "josla": 12},
             {"v": "1 daļa = 25 kg", "teksts": "25 kg : 75 kg : 100 kg, "
                                               "kopā 200 kg", "josla": 25},
             {"v": "1 daļa = 50 kg", "teksts": "50 kg : 150 kg : 200 kg, "
                                               "kopā 400 kg", "josla": 50},
             {"v": "1 daļa = 100 kg", "teksts": "100 kg : 300 kg : 400 kg, "
                                                "kopā 800 kg", "josla": 100}],
            ievads="Spied soli pa solim: mainās daļas lielums, bet attiecība "
                   "1 : 3 : 4 paliek tā pati."),

    Paraugs("No attiecības uz kilogramiem",
            uzd="Betonu gatavo, cementu, smiltis un granti ņemot attiecībā "
                "1 : 3 : 4. Pavisam vajag 800 kg. Cik ir katras vielas?",
            soli=[
                ("1 + 3 + 4 = 8 daļas",
                 "Vispirms - cik vienādu daļu ir kopā."),
                ("800 : 8 = 100 kg",
                 "Tik sver viena daļa."),
                ("Cements 1 · 100 = 100 kg",
                 "Katram reizina vienu daļu ar viņa skaitli."),
                ("Smiltis 3 · 100 = 300 kg; grants 4 · 100 = 400 kg",
                 "Tā paša reizināšana pārējiem."),
                ("100 + 300 + 400 = 800 kg",
                 "Pārbaude: summa sakrīt ar kopumu."),
            ],
            atbilde="100 kg cementa, 300 kg smilšu, 400 kg grants"),

    Ievadi("Cik daļu un cik katram?", [
        {"jaut": "Attiecība 2 : 5. Cik vienādu daļu ir kopā?",
         "atb": ["7"], "padoms": "2 + 5."},
        {"jaut": "Attiecība 1 : 3 : 4, kopums 400 kg. Cik sver viena daļa?",
         "atb": ["50"], "padoms": "400 : 8.", "mers": "atbildi kilogramos"},
        {"jaut": "Tā pati attiecība un kopums. Cik kilogramu ir grants?",
         "atb": ["200"], "padoms": "4 · 50."},
        {"jaut": "Attiecība 3 : 7, kopums 100 €. Cik eiro ir viena daļa?",
         "atb": ["10"], "padoms": "3 + 7 = 10 daļas; 100 : 10."},
        {"jaut": "Attiecība 2 : 3 : 5, kopums 60 l. Cik litru ir viena daļa?",
         "atb": ["6"], "padoms": "2 + 3 + 5 = 10; 60 : 10."},
        {"jaut": "Tā pati attiecība un kopums. Cik litru ir lielākajai daļai?",
         "atb": ["30"], "padoms": "5 · 6."},
    ], pamats=4,
        ievads="Vienmēr divi soļi: cik daļu kopā, tad cik ir viena daļa."),

    Varianti("Kur slēpjas kļūda?", [
        {"jaut": "Attiecība 1 : 4, kopums 100. Skolēns rēķina 100 : 4 = 25. "
                 "Kas nav labi?",
         "opcijas": ["Daļu ir 5, nevis 4", "Jādala ar 1",
                     "Jāreizina, nevis jādala", "Viss ir pareizi"],
         "pareizi": 0,
         "padoms": "Daļu skaits ir abu skaitļu summa."},
        {"jaut": "Kopums 90, attiecība 2 : 3 : 4. Cik sver viena daļa?",
         "opcijas": ["10", "9", "30", "22,5"],
         "pareizi": 0,
         "padoms": "2 + 3 + 4 = 9 daļas; 90 : 9."},
        {"jaut": "Kā pārbaudīt, vai sadalījums ir pareizs?",
         "opcijas": ["Saskaitīt visas daļas un salīdzināt ar kopumu",
                     "Paskatīties, vai skaitļi ir apaļi",
                     "Pārbaudīt, vai lielākā daļa ir pirmā",
                     "Pārbaude nav vajadzīga"],
         "pareizi": 0,
         "padoms": "Ja summa nesakrīt, kaut kur pazuda daļa."},
        {"jaut": "Attiecībā 1 : 3 : 4 kopums ir 24 kg. Kura daļa ir 9 kg?",
         "opcijas": ["Neviena", "Pirmā", "Otrā", "Trešā"],
         "pareizi": 0,
         "padoms": "Viena daļa ir 3 kg; daļas ir 3 kg, 9 kg un 12 kg."},
    ], pamats=4),

    Pasaule("Cik degvielas ielej raķetē?",
            Ievadi("", [
                {"jaut": "Degvielu un skābekli ielej attiecībā 1 : 7. Kopā "
                         "800 t. Cik tonnu ir degvielas?",
                 "atb": ["100"], "padoms": "8 daļas; 800 : 8 = 100."},
                {"jaut": "Tā pati raķete. Cik tonnu ir skābekļa?",
                 "atb": ["700"], "padoms": "7 · 100."},
                {"jaut": "Mazākā raķetē kopā ir 400 t. Cik tonnu degvielas?",
                 "atb": ["50"], "padoms": "400 : 8."},
                {"jaut": "Sakarsētu gāzu plūsmā ūdens un pārējo vielu "
                         "attiecība ir 5 : 1. Kopā 600 kg. Cik ūdens?",
                 "atb": ["500"], "padoms": "6 daļas; 600 : 6 = 100; 5 · 100."},
            ]),
            pavediens="tehnika",
            konteksts="Raķetes masa ir zināma jau pirms starta, bet sadalīt "
                      "to pa tvertnēm palīdz tikai attiecība.",
            kapec="Viena daļa ir atslēga: to atrod vienreiz un tad izmanto "
                  "visiem."),

    Zimejums("Astoņas vienādas daļas",
             dala(8, 3, "3 daļas no 8"),
             paskaidro="Ja viena daļa ir 100 kg, tad šīs trīs daļas ir "
                       "300 kg. Josla parāda to pašu, ko rēķins.",
             ievads="Tā izskatās attiecība 1 : 3 : 4, ja to saliek vienā "
                    "joslā: 1 daļa, tad 3, tad 4."),

    Kopsavilkums([
        "Saskaitu attiecības skaitļus un zinu, cik daļu ir kopā.",
        "Atrodu vienas daļas lielumu, dalot kopumu ar daļu skaitu.",
        "Aprēķinu katra lieluma daudzumu, reizinot vienu daļu.",
        "Pārbaudu rezultātu: visu daļu summa ir kopums.",
    ]),

    Majas([
        "Sadali 60 minūtes attiecībā 1 : 2 : 3 un pieraksti trīs skaitļus.",
        "Atrodi mājās produktu, uz kura sastāvā ir divas galvenās "
        "sastāvdaļas, un uzmini to attiecību.",
        "Izdomā kopumu, kuru attiecībā 1 : 3 : 4 sadalīt *nevar* veselos "
        "skaitļos, un paskaidro, kāpēc.",
    ]),
]
