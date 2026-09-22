# -*- coding: utf-8 -*-
"""5. klase, 148. stunda: «Cik bija sākumā, ja zināmi procenti?»

Apgrieztais uzdevums, un tas ir 75. stundas atkārtojums ar procentiem: zināma
daļas vērtība, jāatrod veselais. Paņēmiens tas pats - vispirms viens
procents, tad simts. Tieši šo uzdevumu dzīvē sastop biežāk, nekā liekas:
atlaides summa ir zināma, sākotnējā cena - nē.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala)

TEMA = "Cik bija sākumā, ja zināmi procenti?"

MERKIS = ("Iemācīsimies aprēķināt veselo, ja zināma procentu skaitliskā "
          "vērtība.")

SATURS = [
    Sakums("Atlaide 16 eiro - cik maksāja prece?",
           zimejums=dala(10, 2, "20 % = 16 €"),
           paraksts="Ja 20 % ir 16 €, tad 1 % ir 0,8 €, bet 100 % - 80 €.",
           fakti=["Šoreiz zināma nevis cena, bet atlaides summa.",
                  "Vispirms jāatrod viens procents.",
                  "Tad to reizina ar 100."]),

    Doma("Vispirms viens procents, tad simts",
         "Ja zināma procentu vērtība, veselo atrod, dalot šo vērtību ar "
         "procentu skaitu un reizinot ar 100.",
         soli=[
             "Pieraksti, cik procentu un kāda ir to vērtība.",
             "Dali vērtību ar procentu skaitu - iegūsi vienu procentu.",
             "Reizini vienu procentu ar 100.",
             "Pārbaudi: aprēķini dotos procentus no atrastā veselā.",
             "Biežāk lietotos procentus var rēķināt kā daļu.",
         ],
         pieze="20 % ir {1|5}, tāpēc veselais ir piecas reizes lielāks par "
               "atlaidi: 16 · 5 = 80. Ar biežāk lietotajiem procentiem šis "
               "ceļš ir daudz īsāks."),

    Paraugs("20 % ir 16 €. Cik maksāja prece?",
            uzd="Aprēķini sākotnējo cenu.",
            soli=[
                ("16 : 20 = 0,8 (€)",
                 "Viens procents."),
                ("0,8 · 100 = 80 (€)",
                 "Simts procenti."),
                ("Vai arī: 20 % = {1|5}, tāpēc 16 · 5 = 80",
                 "Īsākais ceļš."),
                ("Pārbaude: 80 : 5 = 16",
                 "Atlaide sakrīt."),
            ],
            atbilde="Prece maksāja 80 €"),

    Ievadi("Atrodi veselo", [
        {"jaut": "20 % ir 16. Cik ir viss skaitlis?",
         "atb": ["80"], "padoms": "16 · 5."},
        {"jaut": "25 % ir 20. Cik ir viss skaitlis?",
         "atb": ["80"], "padoms": "20 · 4."},
        {"jaut": "50 % ir 30. Cik ir viss skaitlis?",
         "atb": ["60"], "padoms": "30 · 2."},
        {"jaut": "10 % ir 25. Cik ir viss skaitlis?",
         "atb": ["250"], "padoms": "25 · 10."},
        {"jaut": "1 % ir 4. Cik ir viss skaitlis?",
         "atb": ["400"], "padoms": "4 · 100."},
        {"jaut": "5 % ir 10. Cik ir viss skaitlis?",
         "atb": ["200"], "padoms": "10 : 5 · 100."},
        {"jaut": "75 % ir 150. Cik ir viss skaitlis?",
         "atb": ["200"], "padoms": "150 : 3 · 4."},
        {"jaut": "40 % ir 24. Cik ir viss skaitlis?",
         "atb": ["60"], "padoms": "24 : 40 · 100."},
    ], pamats=4,
        ievads="Dali ar procentu skaitu, reizini ar 100."),

    Zimejums("No daļas uz visu joslu",
             dala(10, 2, "divas daļas ir 16 €"),
             paskaidro="Ja divas daļas no desmit ir 16 €, viena daļa ir 8 €, "
                       "bet visas desmit - 80 €.",
             ievads="Shēma rāda ceļu no daļas uz veselo."),

    Varianti("Kā atrod veselo?", [
        {"jaut": "Zināma procentu vērtība. Kā atrod veselo?",
         "opcijas": ["Dala ar procentu skaitu, reizina ar 100",
                     "Reizina ar procentu skaitu",
                     "Dala ar 100",
                     "Atņem procentus"],
         "pareizi": 0,
         "padoms": "Vispirms viens procents."},
        {"jaut": "25 % ir 20. Cik ir viss skaitlis?",
         "opcijas": ["80", "45", "5", "500"],
         "pareizi": 0,
         "padoms": "20 · 4."},
        {"jaut": "50 % ir 30. Cik ir viss skaitlis?",
         "opcijas": ["60", "15", "80", "150"],
         "pareizi": 0,
         "padoms": "Puse."},
        {"jaut": "Veselais vienmēr ir...",
         "opcijas": ["Lielāks par procentu vērtību", "Mazāks par to",
                     "Vienāds ar to", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Ja procentu ir mazāk par 100."},
        {"jaut": "Kā pārbauda atbildi?",
         "opcijas": ["Aprēķina dotos procentus no atrastā veselā",
                     "Saskaita abus skaitļus",
                     "Dala ar 2",
                     "Pārbaudīt nevar"],
         "pareizi": 0,
         "padoms": "Jāiznāk dotajai vērtībai."},
        {"jaut": "10 % ir 25. Cik ir viss skaitlis?",
         "opcijas": ["250", "2,5", "35", "100"],
         "pareizi": 0,
         "padoms": "25 · 10."},
    ], pamats=4),

    Pasaule("Cik maksāja prece pirms atlaides?",
            Ievadi("", [
                {"jaut": "Atlaide 20 % bija 16 €. Cik eiro maksāja prece?",
                 "atb": ["80"], "padoms": "16 · 5."},
                {"jaut": "Atlaide 25 % bija 30 €. Cik eiro maksāja prece?",
                 "atb": ["120"], "padoms": "30 · 4."},
                {"jaut": "Atlaide 10 % bija 7 €. Cik eiro maksāja prece?",
                 "atb": ["70"], "padoms": "7 · 10."},
                {"jaut": "Atlaide 50 % bija 45 €. Cik eiro maksāja prece?",
                 "atb": ["90"], "padoms": "45 · 2."},
            ]),
            pavediens="veikals",
            konteksts="Čekā bieži redzama tikai ietaupītā summa, bet ne "
                      "sākotnējā cena.",
            kapec="No atlaides var atgriezties pie cenas ar diviem soļiem."),

    Kopsavilkums([
        "Atpazīstu uzdevumu, kurā dota procentu vērtība.",
        "Atrodu vienu procentu, dalot vērtību ar procentu skaitu.",
        "Aprēķinu veselo, reizinot vienu procentu ar 100.",
        "Pārbaudu atbildi, aprēķinot procentus no atrastā veselā.",
    ]),

    Majas([
        "Atrodi veselo: 30 % ir 45; 5 % ir 8; 60 % ir 120.",
        "Pārbaudi katru atbildi.",
        "Izdomā uzdevumu par atlaidi un atrisini to.",
    ]),
]
