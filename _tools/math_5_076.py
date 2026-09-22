# -*- coding: utf-8 -*-
"""5. klase, 76. stunda: «Kā uzzīmēt visu nogriezni?»

Tas pats uzdevums, kas iepriekšējā stundā, tikai ar lineālu rokās. Zīmējot
kļūda paliek redzama: ja gabaliņi nav vienādi, nogrieznis vienkārši neiznāk
pareizs. Tāpēc te rēķins un zīmējums pārbauda viens otru - izmērītais garums
sakrīt ar izrēķināto vai nesakrīt nemaz.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Petijums, Varianti, Zimejums, dala)

TEMA = "Kā uzzīmēt visu nogriezni?"

MERKIS = ("Iemācīsimies uzzīmēt visu nogriezni, ja dota tā noteikta daļa.")

SATURS = [
    Sakums("Dots gabals - uzzīmē visu",
           zimejums=dala(3, 2, "2/3 = 6 cm"),
           paraksts="Ja 6 cm ir divas trešdaļas, viena trešdaļa ir 3 cm.",
           fakti=["Dots nogrieznis, kas ir {2|3} no meklētā.",
                  "Vienu trešdaļu atrod, dalot doto ar 2.",
                  "Visu nogriezni zīmē no trim tādām trešdaļām."]),

    Doma("Sadali doto, tad pieliec klāt",
         "Lai uzzīmētu visu nogriezni, doto gabalu sadala tik vienādās "
         "daļās, cik rāda skaitītājs, un atliek tik daļas, cik rāda saucējs.",
         soli=[
             "Izmēri doto nogriezni.",
             "Dali tā garumu ar skaitītāju - iegūsi vienas daļas garumu.",
             "Reizini vienas daļas garumu ar saucēju.",
             "Uzzīmē nogriezni ar iegūto garumu.",
             "Pārbaudi: doto gabalu tajā jāsatur tieši skaitītāja reizes.",
         ],
         pieze="Zīmējot der arī cirkulis: vienas daļas garumu atliek pa "
               "vienam, nemērot katru reizi no jauna. Tā visi gabali iznāk "
               "tiešām vienādi."),

    Paraugs("{2|3} nogriežņa ir 6 cm",
            uzd="Uzzīmē visu nogriezni, ja tā divas trešdaļas ir 6 cm garas.",
            soli=[
                ("6 : 2 = 3 (cm)",
                 "Viena trešdaļa."),
                ("3 · 3 = 9 (cm)",
                 "Trīs trešdaļas - viss nogrieznis."),
                ("Zīmē nogriezni 9 cm garu",
                 "Ar lineālu no punkta A."),
                ("Pārbaude: 6 cm gabals tajā ietilpst ar 3 cm atlikumu",
                 "Atlikums ir tieši viena trešdaļa."),
            ],
            atbilde="Viss nogrieznis ir 9 cm garš"),

    Petijums("Uzzīmē un pārbaudi",
             soli=["Uzzīmē nogriezni, kas ir 8 cm garš, un pieņem, ka tas ir "
                   "{4|5} no meklētā.",
                   "Sadali to četros vienādos gabalos - katrs būs 2 cm.",
                   "Pieliec klāt vēl vienu tādu gabalu.",
                   "Izmēri iegūto nogriezni un pieraksti garumu.",
                   "Salīdzini izmērīto ar izrēķināto: 8 : 4 · 5."],
             vajag="lineāls, zīmulis, rūtiņu lapa",
             secinajums="Izmērītais un izrēķinātais garums sakrīt - 10 cm."),

    Ievadi("Cik garš ir viss nogrieznis?", [
        {"jaut": "{1|2} nogriežņa ir 5 cm. Cik centimetru ir viss "
                 "nogrieznis?",
         "atb": ["10"], "padoms": "5 · 2."},
        {"jaut": "{2|3} nogriežņa ir 6 cm. Cik centimetru ir viss "
                 "nogrieznis?",
         "atb": ["9"], "padoms": "6 : 2 · 3."},
        {"jaut": "{3|4} nogriežņa ir 9 cm. Cik centimetru ir viss "
                 "nogrieznis?",
         "atb": ["12"], "padoms": "9 : 3 · 4."},
        {"jaut": "{4|5} nogriežņa ir 8 cm. Cik centimetru ir viss "
                 "nogrieznis?",
         "atb": ["10"], "padoms": "8 : 4 · 5."},
        {"jaut": "{2|5} nogriežņa ir 4 cm. Cik centimetru ir viss "
                 "nogrieznis?",
         "atb": ["10"], "padoms": "4 : 2 · 5."},
        {"jaut": "{3|8} nogriežņa ir 6 cm. Cik centimetru ir viss "
                 "nogrieznis?",
         "atb": ["16"], "padoms": "6 : 3 · 8."},
        {"jaut": "{2|3} nogriežņa ir 6 cm. Cik centimetru ir viena "
                 "trešdaļa?",
         "atb": ["3"], "padoms": "6 : 2."},
        {"jaut": "{5|6} nogriežņa ir 10 cm. Cik centimetru ir viss "
                 "nogrieznis?",
         "atb": ["12"], "padoms": "10 : 5 · 6."},
    ], pamats=4,
        ievads="Vispirms viena daļa centimetros, tikai tad viss nogrieznis."),

    Zimejums("Trīs vienādi gabali",
             dala(3, 2, "2/3"),
             paskaidro="Iekrāsotais gabals ir dotais nogrieznis, tukšais - "
                       "tas, kas vēl jāpieliek klāt.",
             ievads="Zīmējot vispirms atliek vienu daļu, tad pārējās."),

    Varianti("Kā zīmē visu nogriezni?", [
        {"jaut": "Ar ko sāk, zīmējot visu nogriezni?",
         "opcijas": ["Atrod vienas daļas garumu", "Zīmē visu uzreiz",
                     "Mēra ar cirkuli", "Dala ar saucēju"],
         "pareizi": 0,
         "padoms": "Vienu daļu atrod, dalot ar skaitītāju."},
        {"jaut": "{3|4} nogriežņa ir 12 cm. Cik garš ir viss nogrieznis?",
         "opcijas": ["16 cm", "9 cm", "48 cm", "15 cm"],
         "pareizi": 0,
         "padoms": "12 : 3 · 4."},
        {"jaut": "Kāpēc gabaliem jābūt tieši vienādiem?",
         "opcijas": ["Citādi tās nav daļas", "Citādi zīmējums nav glīts",
                     "Citādi nevar mērīt", "Tas nav svarīgi"],
         "pareizi": 0,
         "padoms": "Daļas pēc definīcijas ir vienādas."},
        {"jaut": "Dotais gabals ir {5|6}. Cik daļas vēl jāpieliek klāt?",
         "opcijas": ["Viena", "Piecas", "Sešas", "Neviena"],
         "pareizi": 0,
         "padoms": "6 - 5 = 1."},
        {"jaut": "Kā pārbaudīt uzzīmēto nogriezni?",
         "opcijas": ["Izmērīt to un salīdzināt ar aprēķinu",
                     "Uzzīmēt vēlreiz",
                     "Saskaitīt gabalus",
                     "Pārbaudīt nevar"],
         "pareizi": 0,
         "padoms": "Mērījumam jāsakrīt ar rēķinu."},
        {"jaut": "Dotais gabals ir {7|4} no nogriežņa. Ko tas nozīmē?",
         "opcijas": ["Dotais ir garāks par nogriezni",
                     "Tā nevar būt",
                     "Dotais ir īsāks",
                     "Tie ir vienādi"],
         "pareizi": 0,
         "padoms": "Neīsta daļa ir lielāka par vienu."},
    ], pamats=4),

    Pasaule("Cik gara ir visa taka?",
            Ievadi("", [
                {"jaut": "Kartē {2|5} takas ir 4 cm. Cik centimetru ir visa "
                         "taka?",
                 "atb": ["10"], "padoms": "4 : 2 · 5."},
                {"jaut": "Noieta {3|4} takas, tas ir 6 km. Cik kilometru ir "
                         "visa taka?",
                 "atb": ["8"], "padoms": "6 : 3 · 4."},
                {"jaut": "Kartē {1|3} maršruta ir 5 cm. Cik centimetru ir "
                         "viss maršruts?",
                 "atb": ["15"], "padoms": "5 · 3."},
                {"jaut": "Noieta {5|8} takas, tas ir 10 km. Cik kilometru ir "
                         "visa taka?",
                 "atb": ["16"], "padoms": "10 : 5 · 8."},
            ]),
            pavediens="celojums",
            konteksts="Kartē bieži redzams tikai takas gabals, bet plānot "
                      "vajag visu maršrutu.",
            kapec="Uzzīmēts nogrieznis parāda to, ko rēķins tikai pasaka."),

    Kopsavilkums([
        "Aprēķinu vienas daļas garumu no dotā nogriežņa.",
        "Uzzīmēju visu nogriezni, ja dota tā daļa.",
        "Atlieku vienādas daļas ar lineālu vai cirkuli.",
        "Pārbaudu zīmējumu, salīdzinot mērījumu ar aprēķinu.",
    ]),

    Majas([
        "Uzzīmē nogriezni, kura {3|5} ir 6 cm.",
        "Uzzīmē nogriezni, kura {2|7} ir 4 cm.",
        "Pārbaudi abus zīmējumus ar lineālu.",
    ]),
]
