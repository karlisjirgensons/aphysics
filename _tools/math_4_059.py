# -*- coding: utf-8 -*-
"""4. klase, 59. stunda: «Kas kopīgs garuma un leņķa mērīšanai?»

Salīdzināšanas stunda: lineāls un transportieris, centimetrs un grāds.
Kopīgais - vienība, skala, sākuma nulle, precizitāte. Atšķirīgais - ko mēra
(attālumu vai pagriezienu) un ka leņķis nemainās no malu garuma.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Sakums, Varianti, Zimejums, restis)

TEMA = "Kas kopīgs garuma un leņķa mērīšanai?"

MERKIS = ("Salīdzināsim nogriežņa garuma un leņķa lieluma mērīšanu un "
          "raksturosim kopīgo un atšķirīgo.")

SATURS = [
    Sakums("Lineāls un transportieris - brāļi?",
           zimejums=restis([["", "garums", "leņķis"],
                            ["rīks", "lineāls", "transportieris"],
                            ["vienība", "cm, mm", "grāds °"],
                            ["sākums", "0 pie gala", "0 pie malas"]],
                           "divi mērījumi"),
           fakti=["Abiem rīkiem ir skala ar nulli.",
                  "Abiem jāliek nulle tieši pareizajā vietā."]),

    Doma("Mērīt nozīmē salīdzināt ar vienību",
         "Gan garumu, gan leņķi mēra, saskaitot, cik vienību ietilpst; "
         "atšķiras tikai vienība un rīks.",
         soli=[
             "Izvēlies rīku un vienību.",
             "Novieto nulli sākumā (nogriežņa galā vai uz leņķa malas).",
             "Nolasi skaitli pie otra gala vai otras malas.",
             "Pieraksti ar mērvienību: 7 cm vai 45°.",
         ],
         pieze="Atšķirība: nogriezni pagarinot, garums mainās; leņķa malas "
               "pagarinot, leņķis nemainās."),

    Zimejums("Kopīgais un atšķirīgais",
             restis([["", "kopīgs?"],
                     ["ir skala", "jā"],
                     ["jāsāk no 0", "jā"],
                     ["mērvienība", "dažāda"],
                     ["mainās, pagarinot", "tikai garums"]],
                    "salīdzinājums"),
             paskaidro="Trīs lietas kopīgas, divas - atšķirīgas.",
             ievads="Tabula apkopo, ko atradām."),

    Varianti("Garums vai leņķis?", [
        {"jaut": "Ko mēra grādos?",
         "opcijas": ["leņķi", "garumu", "masu", "laiku"], "pareizi": 0,
         "padoms": "°."},
        {"jaut": "Kas mainās, ja nogriezni pagarina?",
         "opcijas": ["garums", "leņķis", "nekas"], "pareizi": 0,
         "padoms": "Nogrieznis kļūst garāks."},
        {"jaut": "Kas notiek ar leņķi, ja tā malas pagarina?",
         "opcijas": ["nemainās", "palielinās", "samazinās"], "pareizi": 0,
         "padoms": "Leņķis ir pagrieziens, nevis garums."},
        {"jaut": "Kas kopīgs lineālam un transportierim?",
         "opcijas": ["skala ar nulli", "abi apaļi", "vienāda vienība",
                     "abi mēra gramos"], "pareizi": 0,
         "padoms": "Abiem ir iedaļas no 0."},
    ], pamats=4),

    Ievadi("Mēri un rēķini", [
        {"jaut": "Nogrieznis 7 cm, otrs 4 cm. Kopā cm?", "atb": ["11"],
         "padoms": "7 + 4."},
        {"jaut": "Leņķi 35° un 40° blakus. Kopā grādu?", "atb": ["75"],
         "padoms": "35 + 40."},
        {"jaut": "Cik mm ir 7 cm?", "atb": ["70"], "padoms": "7 · 10."},
        {"jaut": "Cik taisnu leņķu ir 360°?", "atb": ["4"],
         "padoms": "360 : 90."},
    ]),

    Pasaule("Kuģa navigācija",
            Varianti("", [
                {"jaut": "Kapteinis zina attālumu līdz ostai un virzienu. Kas "
                         "mērīts grādos?",
                 "opcijas": ["virziens", "attālums", "abi"], "pareizi": 0,
                 "padoms": "Virziens ir pagrieziens."},
                {"jaut": "Kurss 90° no ziemeļiem - kurp iet kuģis?",
                 "opcijas": ["uz austrumiem", "uz dienvidiem",
                             "uz rietumiem"], "pareizi": 0,
                 "padoms": "Ceturtdaļa apgrieziena pa labi no ziemeļiem."},
                {"jaut": "Kuģis pagriežas no kursa 90° uz 180°. Par cik "
                         "grādiem?",
                 "opcijas": ["90°", "180°", "270°"], "pareizi": 0,
                 "padoms": "180 − 90."},
            ]),
            pavediens="celojums",
            konteksts="Navigācijā vajag divus mērījumus: cik tālu (km) un "
                      "kurā virzienā (grādi).",
            kapec="Bez leņķa kuģis zinātu attālumu, bet ne ceļu."),

    Kopsavilkums([
        "Salīdzinu garuma un leņķa mērīšanu.",
        "Nosaucu kopīgo: skala, nulle, vienība.",
        "Nosaucu atšķirīgo: ko mēra un kas mainās, pagarinot.",
    ]),

    Majas([
        "Izmēri savas pildspalvas garumu un grāmatas atvēruma leņķi.",
        "Paskaidro kādam, kāpēc leņķis nemainās, pagarinot malas.",
        "Uzzīmē tabulu «lineāls un transportieris» savā burtnīcā.",
    ]),
]
