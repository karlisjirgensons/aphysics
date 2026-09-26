# -*- coding: utf-8 -*-
"""3. klase, 73. stunda: «Kā sadalīt riņķi vienādās daļās?»

Daļskaitļu temata sākums. Pirms jebkura pieraksta ir jādabū rokās pati doma:
daļa ir *vienāda* daļa no veselā. Locīšana to pārbauda pati - ja locījumi
sakrīt, daļas ir vienādas; ja ne, tad nav.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         dala, rinkis)

TEMA = "Kā sadalīt riņķi vienādās daļās?"

MERKIS = ("Salocīsim riņķi un taisnstūri 2, 4 un 8 vienādās daļās un "
          "nosauksim iegūtās daļas.")

SATURS = [
    Sakums("Kā sadalīt picu, lai nevienam nebūtu mazāk?",
           zimejums=rinkis(sektors=90, virsraksts="viena ceturtdaļa",
                           paraksts="1/4"),
           fakti=["Daļa ir *vienāda* daļa no veselā.",
                  "Ja gabali nav vienādi, tie nav daļas.",
                  "Locot papīru uz pusēm, daļas sanāk vienādas pašas."]),

    Doma("Daļa nozīmē vienādas daļas",
         "Sadalīt veselo daļās nozīmē sadalīt to tā, lai visi gabali būtu "
         "tieši vienādi.",
         soli=[
             "Saloc riņķi uz pusēm - sanāk divas vienādas daļas.",
             "Saloc vēlreiz - sanāk četras.",
             "Vēlreiz - sanāk astoņas.",
             "Atloc un pārbaudi: vai visas daļas sakrīt?",
         ],
         pieze="Katrs locījums daļu skaitu divkāršo, bet katras daļas lielumu "
               "samazina uz pusi: 2, 4, 8, 16."),

    Petijums("Saloc riņķi un taisnstūri",
             vajag="papīra riņķis, taisnstūris un zīmulis",
             soli=[
                 "Saloc riņķi uz pusēm un atloc - apvelc locījuma līniju.",
                 "Saloc vēlreiz un atloc - tagad ir četras daļas.",
                 "Saloc trešo reizi - astoņas daļas.",
                 "To pašu izdari ar taisnstūri.",
                 "Uzliec daļas vienu uz otras un pārbaudi, vai tās sakrīt.",
             ],
             secinajums="Trīs locījumi dod astoņas vienādas daļas - un "
                        "vienādību var pārbaudīt, tās uzliekot."),

    Paraugs("Cik daļu sanāks pēc trim locījumiem?",
            uzd="Lapu saloka trīs reizes uz pusēm. Cik vienādu daļu sanāks?",
            soli=[
                ("1 locījums → 2 daļas",
                 "Pirmais locījums sadala uz pusēm."),
                ("2 locījumi → 4 daļas",
                 "Katra puse sadalās vēl uz pusēm."),
                ("3 locījumi → 8 daļas",
                 "Katrs locījums daļu skaitu divkāršo."),
            ],
            atbilde="8 daļas"),

    Ievadi("Cik daļu sanāk?", [
        {"jaut": "Cik daļu sanāk pēc 2 locījumiem uz pusēm?",
         "atb": ["4"], "padoms": "2 · 2."},
        {"jaut": "Cik daļu sanāk pēc 4 locījumiem uz pusēm?",
         "atb": ["16"], "padoms": "8 · 2."},
        {"jaut": "Cik locījumu vajag, lai sanāktu 8 daļas?",
         "atb": ["3"], "padoms": "2, 4, 8."},
        {"jaut": "Picu sadala 8 vienādās daļās. Cik gabalu saņem 4 bērni, ja "
                 "visiem vienādi?",
         "atb": ["2"], "padoms": "8 : 4."},
        {"jaut": "Picu sadala 4 daļās, apēd 1. Cik daļu palika?",
         "atb": ["3"], "padoms": "4 − 1."},
        {"jaut": "Cik astotdaļu ir vienā pusē?",
         "atb": ["4"], "padoms": "8 : 2."},
    ], pamats=4),

    Zimejums("Viena puse un viena ceturtdaļa",
             dala(4, 1, "1/4", "riņķis sadalīts četrās daļās"),
             paskaidro="Iekrāsotā daļa ir viena no četrām vienādām daļām.",
             ievads="Tā izskatās viena ceturtdaļa."),

    Varianti("Vai tās ir daļas?", [
        {"jaut": "Picu sagrieza divos nevienādos gabalos. Vai tās ir puses?",
         "opcijas": ["Nē, daļām jābūt vienādām", "Jā, gabalu ir divi",
                     "Jā, ja abi ir lieli", "To nevar pateikt"],
         "pareizi": 0, "padoms": "Daļa nozīmē vienādu daļu."},
        {"jaut": "Cik daļu sanāk, salokot lapu divas reizes uz pusēm?",
         "opcijas": ["4", "2", "3", "8"],
         "pareizi": 0, "padoms": "Katrs locījums divkāršo."},
        {"jaut": "Kura daļa ir lielāka?",
         "opcijas": ["Puse", "Ceturtdaļa", "Astotdaļa", "Visas vienādas"],
         "pareizi": 0, "padoms": "Jo mazāk daļu, jo lielāka katra."},
        {"jaut": "Cik ceturtdaļu ir visā veselajā?",
         "opcijas": ["4", "2", "8", "1"],
         "pareizi": 0, "padoms": "Četras ceturtdaļas ir viens vesels."},
    ], pamats=4),

    Pasaule("Kā sadalīt kūku?",
            Ievadi("", [
                {"jaut": "Kūku sadala 8 vienādās daļās. Cik daļu saņem "
                         "katrs no 4 bērniem?",
                 "atb": ["2"], "padoms": "8 : 4."},
                {"jaut": "Cik daļu saņem katrs, ja bērnu ir 8?",
                 "atb": ["1"], "padoms": "8 : 8."},
                {"jaut": "Kūku sadala 4 daļās, apēd 3. Cik daļu palika?",
                 "atb": ["1"], "padoms": "4 − 3."},
                {"jaut": "Divas kūkas pa 8 daļām. Cik daļu kopā?",
                 "atb": ["16"], "padoms": "2 · 8."},
            ]),
            pavediens="virtuve",
            konteksts="Kūku un picu vienmēr griež vienādos gabalos - tieši "
                      "tāpēc tās griež no vidus.",
            kapec="Vienādas daļas ir vienīgais veids, kā sadalīt taisnīgi."),

    Kopsavilkums([
        "Zinu, ka daļa ir vienāda daļa no veselā.",
        "Salocu riņķi un taisnstūri 2, 4 un 8 vienādās daļās.",
        "Nosaucu iegūtās daļas: puse, ceturtdaļa, astotdaļa.",
        "Pārbaudu daļu vienādību, tās uzliekot vienu uz otras.",
    ]),

    Majas([
        "Saloc papīra lapu trīs reizes uz pusēm un saskaiti daļas.",
        "Sadali ābolu vai maizes šķēli četrās vienādās daļās.",
        "Atrodi mājās kaut ko, kas jau ir sadalīts vienādās daļās.",
    ]),
]
