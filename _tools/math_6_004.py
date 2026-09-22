# -*- coding: utf-8 -*-
"""6. klase, 4. stunda: «Kādi lielumi veido attiecību 1 pret 10?»

Uzdevums apgriezts otrādi: dota attiecība, jāatrod lielumi. Tas prasa vairāk
nekā rēķināšana - jāizvēlas divi lielumi, kurus vispār ir jēga salīdzināt,
un tas ir arī vienīgais veids pārliecināties, vai attiecība ir saprasta.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kādi lielumi veido attiecību 1 pret 10?"

MERKIS = ("Mācīsimies pašiem izdomāt lielumus, kas veido doto attiecību, un "
          "pamatot, kāpēc tie der.")

SATURS = [
    Sakums("Kur dzīvo attiecība 1 pret 10?",
           fakti=["1 cm pret 10 cm - viens pret desmit.",
                  "10 centi pret 1 eiro - arī viens pret desmit.",
                  "Bet 1 kg pret 10 m nav attiecība: tos nesalīdzina."]),

    Doma("Salīdzināt var tikai viena veida lielumus",
         "Attiecībā abiem lielumiem jābūt vienā mērvienībā - citādi dalījums "
         "neko nenozīmē.",
         soli=[
             "Izvēlies, ko salīdzināsi: garumus, masas, laikus, naudu.",
             "Paņem vienu vērtību - to, kura ir mazākā daļa.",
             "Reizini to ar otro attiecības skaitli.",
             "Pārbaudi, vai abi ir vienā mērvienībā.",
             "Pārliecinies, vai piemērs ir no dzīves, ne tikai skaitļi.",
         ],
         pieze="Ja mērvienības atšķiras, tās vispirms jāpārveido: 1 m pret "
               "10 cm nav 1 pret 10, jo 1 m = 100 cm - īstenībā tas ir "
               "10 pret 1."),

    Paraugs("Izdomā piemēru attiecībai 1 pret 10",
            uzd="Kādi divi lielumi veido attiecību 1 pret 10?",
            soli=[
                ("Izvēlos garumus",
                 "Abi būs centimetros - viena mērvienība."),
                ("Pirmais: 1 cm - zīmuļa resnums",
                 "Mazākā daļa ir viens."),
                ("Otrais: 1 · 10 = 10 cm - plaukstas platums",
                 "Otro iegūst, reizinot ar 10."),
                ("Pārbaude: 1 : 10 - abi centimetros",
                 "Piemērs der."),
            ],
            atbilde="piemēram, 1 cm un 10 cm"),

    Ievadi("Atrodi otro lielumu", [
        {"jaut": "Attiecība 1 pret 10. Pirmais ir 3 kg. Cik ir otrais? (kg)",
         "atb": ["30"], "padoms": "3 · 10."},
        {"jaut": "Attiecība 1 pret 10. Otrais ir 50 cm. Cik ir pirmais? (cm)",
         "atb": ["5"], "padoms": "50 : 10."},
        {"jaut": "Attiecība 1 pret 4. Pirmais ir 7 l. Cik ir otrais? (l)",
         "atb": ["28"], "padoms": "7 · 4."},
        {"jaut": "Attiecība 2 pret 5. Pirmais ir 6 m. Cik ir otrais? (m)",
         "atb": ["15"], "padoms": "6 : 2 = 3; 3 · 5."},
        {"jaut": "1 m un 10 cm - cik centimetru ir pirmajā lielumā?",
         "atb": ["100"], "padoms": "1 m = 100 cm."},
        {"jaut": "Tad kāda ir attiecība 1 m pret 10 cm? Raksti ar kolu.",
         "atb": ["10:1"], "padoms": "100 : 10, saīsināts."},
    ], pamats=4,
        ievads="Abiem lielumiem jābūt vienā mērvienībā."),

    Varianti("Vai tas ir 1 pret 10?", [
        {"jaut": "Kurš pāris veido attiecību 1 pret 10?",
         "opcijas": ["2 kg un 20 kg", "2 kg un 10 kg", "10 kg un 1 kg",
                     "2 kg un 20 m"],
         "pareizi": 0,
         "padoms": "Otrajam jābūt desmitreiz lielākam."},
        {"jaut": "Kāpēc 1 kg un 10 m neveido attiecību?",
         "opcijas": ["Tie ir dažāda veida lielumi",
                     "Jo 10 ir par lielu",
                     "Jo kilogramus nevar dalīt",
                     "Tie veido, tikai apgrieztu"],
         "pareizi": 0,
         "padoms": "Ko nozīmētu kilograms, dalīts ar metru?"},
        {"jaut": "1 stunda pret 10 minūtēm - kāda ir attiecība?",
         "opcijas": ["6 : 1", "1 : 10", "10 : 1", "1 : 6"],
         "pareizi": 0,
         "padoms": "1 h = 60 min; 60 : 10."},
        {"jaut": "Kurš piemērs attiecībai 1 pret 100 ir no dzīves?",
         "opcijas": ["1 cents un 1 eiro", "1 cents un 10 centi",
                     "1 metrs un 1 kilometrs", "1 minūte un 1 stunda"],
         "pareizi": 0,
         "padoms": "1 eiro ir 100 centi."},
    ], pamats=4),

    Pasaule("Kādas attiecības ir mājā?",
            Ievadi("", [
                {"jaut": "Sienas biezums 20 cm, istabas platums 400 cm. "
                         "Attiecība ar kolu?",
                 "atb": ["1:20"], "padoms": "20 : 400, abus dali ar 20."},
                {"jaut": "Flīze 30 cm, siena 300 cm. Cik flīžu ietilpst "
                         "rindā?",
                 "atb": ["10"], "padoms": "300 : 30."},
                {"jaut": "Krāsas bundža 1 l, vajag 10 l. Cik bundžu jāpērk?",
                 "atb": ["10"], "padoms": "10 : 1."},
                {"jaut": "Dēlis 2 m, dēļu kaudze 20 m. Attiecība ar kolu?",
                 "atb": ["1:10"], "padoms": "2 : 20, abus dali ar 2."},
            ]),
            pavediens="maja",
            konteksts="Remontā attiecību parasti nezina - to ievāc pats, "
                      "izmērot divas lietas vienā mērvienībā.",
            kapec="Attiecība ir jēdzīga tikai tad, ja abus lielumus mēra "
                  "vienādi."),

    Kopsavilkums([
        "Minu piemērus lielumiem, kas veido doto attiecību.",
        "Pamatoju, kāpēc mans piemērs der.",
        "Zinu, ka abiem lielumiem jābūt vienā mērvienībā.",
        "Pārveidoju mērvienības, pirms rakstu attiecību.",
    ]),

    Majas([
        "Izdomā trīs piemērus attiecībai 1 pret 10 - garumam, masai un "
        "naudai.",
        "Atrodi mājās divas lietas, kuru garumi ir aptuveni 1 pret 2.",
        "Padomā, kāda ir tava auguma attiecība pret istabas augstumu.",
    ]),
]
