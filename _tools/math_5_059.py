# -*- coding: utf-8 -*-
"""5. klase, 59. stunda: «Kad starprezultātu nesaīsina?»

Mikrotemata noslēgums, un vienīgā stunda, kurā pareizā atbilde ir «nedari».
Skolēns, iemācījies saīsināt, saīsina visu pēc kārtas - arī tur, kur pēc brīža
saucējs atkal būs vajadzīgs. Tāpēc te nav jauna rēķina, bet ir sprieduma
uzdevums: kurā vietā saīsināšana palīdz un kurā - traucē.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kad starprezultātu nesaīsina?"

MERKIS = ("Mācīsimies spriest, kad starprezultātu ir izdevīgi atstāt "
          "nesaīsinātu, un pamatot savu izvēli.")

SATURS = [
    Sakums("Saīsināt tūlīt vai pagaidīt?",
           zimejums=restis([["2/6", "3/6", "4/6"],
                            ["1/3", "1/2", "2/3"]],
                           virsraksts="Viena rinda ērta, otra - ne"),
           paraksts="Augšējā rindā daļas var sakārtot uzreiz; apakšējā - "
                    "vēl jādomā.",
           fakti=["Saīsināta daļa ir īsāka, bet ne vienmēr ērtāka.",
                  "Ar vienu saucēju daļas salīdzina bez rēķina.",
                  "Tāpēc dažreiz starprezultātu atstāj kā ir."]),

    Doma("Saīsina atbildi, nevis katru soli",
         "Starprezultātu atstāj nesaīsinātu tad, ja tā saucējs tūlīt būs "
         "vajadzīgs vēlreiz; galarezultātu saīsina vienmēr.",
         soli=[
             "Paskaties, kas notiks nākamajā solī.",
             "Ja daļas vēl jāsalīdzina vai jāsaskaita - atstāj kopīgo "
             "saucēju.",
             "Ja tas ir pēdējais solis - saīsini.",
             "Pieraksti, kāpēc izvēlējies tā.",
         ],
         pieze="{2|6} un {3|6} ar vienu acu uzmetienu ir sakārtojamas, bet "
               "{1|3} un {1|2} - vairs ne. Tāpēc kopīgo saucēju tur, kamēr "
               "tas strādā, un noņem tikai beigās."),

    Paraugs("Sakārto {1|2}, {1|3} un {2|3}",
            uzd="Sakārto trīs daļas augošā secībā. Kur saīsināt un kur nē?",
            soli=[
                ("Kopīgais saucējs ir 6",
                 "6 dalās ar 2 un 3."),
                ("{1|2} = {3|6}, {1|3} = {2|6}, {2|3} = {4|6}",
                 "Starprezultāti - ar vienu saucēju."),
                ("{2|6} < {3|6} < {4|6}",
                 "Salīdzina tikai skaitītājus; te saīsināt nedrīkst."),
                ("Atbildē: {1|3} < {1|2} < {2|3}",
                 "Tikai beigās atgriežas pie īsākā pieraksta."),
            ],
            atbilde="{1|3} < {1|2} < {2|3}"),

    Ievadi("Ar kopīgo saucēju", [
        {"jaut": "{1|2} un {1|3} pārrakstīja ar saucēju 6. Kāds skaitītājs "
                 "ir pirmajai?",
         "atb": ["3"], "padoms": "{1|2} = {3|6}."},
        {"jaut": "Tās pašas daļas. Kāds skaitītājs ir otrajai?",
         "atb": ["2"], "padoms": "{1|3} = {2|6}."},
        {"jaut": "{3|4} un {5|8} pārraksta ar saucēju 8. Kāds skaitītājs ir "
                 "pirmajai?",
         "atb": ["6"], "padoms": "{3|4} = {6|8}."},
        {"jaut": "{2|5} un {3|10} pārraksta ar saucēju 10. Kāds skaitītājs "
                 "ir pirmajai?",
         "atb": ["4"], "padoms": "{2|5} = {4|10}."},
        {"jaut": "Ar saucēju 12: kāds skaitītājs ir daļai {2|3}?",
         "atb": ["8"], "padoms": "12 : 3 = 4; 2 · 4."},
        {"jaut": "Ar saucēju 12: kāds skaitītājs ir daļai {3|4}?",
         "atb": ["9"], "padoms": "12 : 4 = 3; 3 · 3."},
        {"jaut": "Gala atbilde iznāca {6|8}. Kā to raksta saīsinātu? Atbildi "
                 "raksti kā a/b.",
         "atb": ["3/4"], "padoms": "Abus dala ar 2."},
        {"jaut": "Gala atbilde iznāca {10|15}. Kā to raksta saīsinātu? "
                 "Atbildi raksti kā a/b.",
         "atb": ["2/3"], "padoms": "Abus dala ar 5."},
    ], pamats=4,
        ievads="Kamēr daļas vēl salīdzina, saucēju tur; atbildi saīsina."),

    Zimejums("Kamēr saucējs strādā",
             restis([["1/2", "1/3", "2/3"],
                     ["3/6", "2/6", "4/6"]],
                    virsraksts="Apakšējā rindā secība redzama uzreiz"),
             paskaidro="Apakšā skaitītāji ir 3, 2 un 4 - vairāk nekas nav "
                       "jārēķina. Ja tos saīsinātu, salīdzināšana sāktos no "
                       "gala.",
             ievads="Kopīgais saucējs ir darbarīks, ne kļūda."),

    Varianti("Saīsināt vai atstāt?", [
        {"jaut": "Daļas jāsakārto pēc lieluma. Vai starprezultātus saīsina?",
         "opcijas": ["Nē, kopīgais saucējs vajadzīgs salīdzināšanai",
                     "Jā, vienmēr",
                     "Jā, lai skaitļi ir mazāki",
                     "Tas ir vienalga"],
         "pareizi": 0,
         "padoms": "Ar vienu saucēju pietiek salīdzināt skaitītājus."},
        {"jaut": "Aprēķins pabeigts, iznāca {8|12}. Ko dara tagad?",
         "opcijas": ["Saīsina līdz {2|3}", "Atstāj kā ir",
                     "Paplašina", "Pārraksta ar saucēju 24"],
         "pareizi": 0,
         "padoms": "Atbildi vienmēr raksta nesaīsināmu."},
        {"jaut": "Kāpēc starprezultāta saīsināšana var traucēt?",
         "opcijas": ["Kopīgais saucējs pazūd un jāatrod no jauna",
                     "Skaitļi kļūst pārāk mazi",
                     "Daļa kļūst nepareiza",
                     "Tā netraucē nekad"],
         "pareizi": 0,
         "padoms": "Nākamajā solī to atkal vajadzēs."},
        {"jaut": "Divas daļas ar vienu saucēju. Kā uzzina, kura lielāka?",
         "opcijas": ["Salīdzina skaitītājus", "Salīdzina saucējus",
                     "Saīsina abas", "Saskaita tās"],
         "pareizi": 0,
         "padoms": "Gabali ir vienādi, atšķiras tikai to skaits."},
        {"jaut": "Kurš apgalvojums ir patiess?",
         "opcijas": ["Atbildi saīsina, starprezultātu - pēc vajadzības",
                     "Saīsināt drīkst tikai atbildi",
                     "Starprezultātu saīsina vienmēr",
                     "Saīsināt nedrīkst nekad"],
         "pareizi": 0,
         "padoms": "Izvēle ir atkarīga no nākamā soļa."},
        {"jaut": "Pēc salīdzināšanas atbildē raksta...",
         "opcijas": ["Sākotnējās daļas pareizā secībā",
                     "Daļas ar kopīgo saucēju",
                     "Tikai skaitītājus",
                     "Tikai lielāko daļu"],
         "pareizi": 0,
         "padoms": "Jautāja par dotajām daļām."},
    ], pamats=4),

    Pasaule("Kurš veikals ir lētāks?",
            Ievadi("", [
                {"jaut": "Viens veikals dod atlaidi {1|4}, otrs {3|10}. "
                         "Pārraksti abas ar saucēju 20. Kāds skaitītājs ir "
                         "pirmajai?",
                 "atb": ["5"], "padoms": "{1|4} = {5|20}."},
                {"jaut": "Tās pašas atlaides. Kāds skaitītājs ir otrajai ar "
                         "saucēju 20?",
                 "atb": ["6"], "padoms": "{3|10} = {6|20}."},
                {"jaut": "Kurš skaitītājs ir lielāks - 5 vai 6? Ieraksti "
                         "lielāko.",
                 "atb": ["6"], "padoms": "Lielāka atlaide - lielāks "
                                         "skaitītājs."},
                {"jaut": "Trešais veikals dod atlaidi {2|5}. Cik tas ir "
                         "divdesmitdaļu?",
                 "atb": ["8"], "padoms": "{2|5} = {8|20}."},
            ]),
            pavediens="veikals",
            konteksts="Atlaides salīdzina ar vienu saucēju; saīsināt tās "
                      "pa vidu nozīmētu sākt no jauna.",
            kapec="Kopīgo saucēju noņem tikai tad, kad atbilde jau zināma."),

    Kopsavilkums([
        "Spriežu, vai starprezultātu saīsināt vai atstāt.",
        "Pamatoju savu izvēli ar nākamo darbības soli.",
        "Salīdzinu daļas ar kopīgu saucēju, salīdzinot skaitītājus.",
        "Galarezultātu vienmēr pierakstu kā nesaīsināmu daļu.",
    ]),

    Majas([
        "Sakārto augošā secībā {3|4}, {2|3} un {5|6} un pieraksti, kur "
        "saīsināji.",
        "Atrodi uzdevumu, kurā saīsināšana pa vidu būtu traucējusi.",
        "Uzraksti savu ieteikumu vienā teikumā: kad saīsināt un kad ne.",
    ]),
]
