# -*- coding: utf-8 -*-
"""5. klase, 57. stunda: «Pa soļiem vai uzreiz?»

Saīsināšana jau zināma, te parādās izvēle. Ar lieliem skaitļiem lielāko
kopīgo dalītāju ieraudzīt grūti, un skolēns apstājas pusceļā. Tāpēc stunda
atzīst abus paņēmienus par labiem un māca tikai vienu lietu: lai kuru izvēlas,
beigās jāpārbauda, vai vairs nav ko dalīt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Pa soļiem vai uzreiz?"

MERKIS = ("Mācīsimies saīsināt daļas ar lieliem skaitļiem, izvēloties sev "
          "ērtāko paņēmienu.")

SATURS = [
    Sakums("Lieli skaitļi, viena un tā pati daļa",
           zimejums=restis([["144/180", ":2", "72/90"],
                            ["72/90", ":2", "36/45"],
                            ["36/45", ":9", "4/5"]],
                           virsraksts="Viens ceļš, trīs soļi"),
           paraksts="{144|180} nav jāsaīsina uzreiz - var arī pa druskai.",
           fakti=["Lielākais kopīgais dalītājs ne vienmēr ir redzams.",
                  "Divi mazi soļi ir tikpat pareizi kā viens liels.",
                  "Svarīgi ir tikai nokļūt līdz galam."]),

    Doma("Abi ceļi ved uz vienu daļu",
         "Daļu var saīsināt ar lielāko kopīgo dalītāju uzreiz vai ar "
         "mazākiem dalītājiem pa soļiem - rezultāts ir viens un tas pats.",
         soli=[
             "Paskaties, vai abi skaitļi dalās ar 2, 3, 5 vai 10.",
             "Ja redzi lielāko kopīgo dalītāju - dali ar to uzreiz.",
             "Ja neredzi - dali ar jebkuru kopīgo dalītāju.",
             "Atkārto, kamēr kopīga dalītāja vairs nav.",
             "Beigās pārbaudi: vai daļa tiešām ir nesaīsināma.",
         ],
         pieze="Pa soļiem ir drošāk, ar lielāko dalītāju - ātrāk. Kļūda ir "
               "tikai viena: apstāties pusceļā un domāt, ka darbs padarīts."),

    Paraugs("Saīsini {144|180}",
            uzd="Saīsini daļu {144|180} līdz nesaīsināmai. Parādi abus ceļus.",
            soli=[
                ("Pa soļiem: {144|180} = {72|90}",
                 "Abus dala ar 2."),
                ("{72|90} = {36|45}",
                 "Vēlreiz ar 2."),
                ("{36|45} = {4|5}",
                 "Abus dala ar 9."),
                ("Uzreiz: 144 : 36 = 4 un 180 : 36 = 5",
                 "Lielākais kopīgais dalītājs ir 36."),
                ("{4|5} - kopīga dalītāja nav",
                 "Abi ceļi noved pie tās pašas daļas."),
            ],
            atbilde="{144|180} = {4|5}"),

    Ievadi("Saīsini līdz nesaīsināmai", [
        {"jaut": "Saīsini {24|36}. Atbildi raksti kā a/b.",
         "atb": ["2/3"], "padoms": "Lielākais kopīgais dalītājs ir 12."},
        {"jaut": "Saīsini {45|60}. Atbildi raksti kā a/b.",
         "atb": ["3/4"], "padoms": "Abus dala ar 15."},
        {"jaut": "Saīsini {36|48}. Atbildi raksti kā a/b.",
         "atb": ["3/4"], "padoms": "Abus dala ar 12."},
        {"jaut": "Saīsini {50|75}. Atbildi raksti kā a/b.",
         "atb": ["2/3"], "padoms": "Abus dala ar 25."},
        {"jaut": "Saīsini {120|150}. Atbildi raksti kā a/b.",
         "atb": ["4/5"], "padoms": "Abus dala ar 30."},
        {"jaut": "Saīsini {84|96}. Atbildi raksti kā a/b.",
         "atb": ["7/8"], "padoms": "Abus dala ar 12."},
        {"jaut": "Saīsini {200|500}. Atbildi raksti kā a/b.",
         "atb": ["2/5"], "padoms": "Abus dala ar 100."},
        {"jaut": "Saīsini {180|240}. Atbildi raksti kā a/b.",
         "atb": ["3/4"], "padoms": "Abus dala ar 60."},
    ], pamats=4,
        ievads="Ja lielo dalītāju neredzi, sāc ar 2 vai 5 - galarezultāts "
               "būs tas pats."),

    Zimejums("Divi ceļi, viena daļa",
             restis([["120/150", ":10", "12/15", ":3", "4/5"],
                     ["120/150", ":30", "4/5", "", ""]],
                    virsraksts="Augšā - pa soļiem, apakšā - uzreiz"),
             paskaidro="Pirmajā rindā ir divi mazi soļi, otrajā - viens "
                       "liels. Nesaīsināmā daļa abās rindās ir {4|5}.",
             ievads="Paņēmienu izvēlas pats, atbilde nemainās."),

    Varianti("Kurš paņēmiens der?", [
        {"jaut": "Vai drīkst saīsināt vairākos soļos?",
         "opcijas": ["Drīkst, rezultāts ir tas pats",
                     "Nedrīkst, jādala ar lielāko dalītāju",
                     "Drīkst tikai ar 2",
                     "Drīkst tikai pirmskaitļiem"],
         "pareizi": 0,
         "padoms": "Katrs solis ir pareiza saīsināšana."},
        {"jaut": "{36|48} saīsināja kā {18|24}. Vai darbs padarīts?",
         "opcijas": ["Nav, var dalīt ar 6", "Ir", "Nav, jādala ar 2",
                     "Nav, jāreizina"],
         "pareizi": 0,
         "padoms": "18 un 24 abi dalās ar 6."},
        {"jaut": "Kā pārbaudīt, vai daļa vairs nesaīsinās?",
         "opcijas": ["Meklēt kopīgu dalītāju, lielāku par 1",
                     "Salīdzināt skaitļu garumu",
                     "Skatīties, vai skaitītājs ir mazs",
                     "Pārbaudīt nevar"],
         "pareizi": 0,
         "padoms": "Nesaīsināmai daļai kopīgs dalītājs ir tikai 1."},
        {"jaut": "Ar kuru skaitli ērtāk sākt, ja abi locekļi beidzas ar 0?",
         "opcijas": ["Ar 10", "Ar 3", "Ar 7", "Ar 9"],
         "pareizi": 0,
         "padoms": "Nulles var noņemt uzreiz."},
        {"jaut": "{84|96} saīsināja pa soļiem: vispirms ar 2, tad ar 2, tad "
                 "ar 3. Ar kādu skaitli tas būtu uzreiz?",
         "opcijas": ["Ar 12", "Ar 6", "Ar 4", "Ar 8"],
         "pareizi": 0,
         "padoms": "2 · 2 · 3."},
        {"jaut": "Kurš apgalvojums ir patiess?",
         "opcijas": ["Abi paņēmieni dod vienu nesaīsināmu daļu",
                     "Pa soļiem iznāk cita daļa",
                     "Uzreiz saīsināt drīkst tikai pirmskaitļus",
                     "Nesaīsināmu daļu var iegūt tikai vienā veidā"],
         "pareizi": 0,
         "padoms": "Nesaīsināmā daļa ir viena vienīga."},
    ], pamats=4),

    Pasaule("Cik liela daļa no čeka?",
            Ievadi("", [
                {"jaut": "Čeka summa 150 €, no tiem 120 € par pārtiku. Kāda "
                         "daļa tā ir? Atbildi raksti kā a/b.",
                 "atb": ["4/5"], "padoms": "{120|150}, abus dala ar 30."},
                {"jaut": "Čeka summa 240 €, no tiem 180 € par pārtiku. Kāda "
                         "daļa tā ir? Atbildi raksti kā a/b.",
                 "atb": ["3/4"], "padoms": "{180|240}, abus dala ar 60."},
                {"jaut": "Čeka summa 96 €, no tiem 84 € par pārtiku. Kāda "
                         "daļa tā ir? Atbildi raksti kā a/b.",
                 "atb": ["7/8"], "padoms": "{84|96}, abus dala ar 12."},
                {"jaut": "Čeka summa 500 €, no tiem 200 € par pārtiku. Kāda "
                         "daļa tā ir? Atbildi raksti kā a/b.",
                 "atb": ["2/5"], "padoms": "{200|500}, abus dala ar 100."},
            ]),
            pavediens="veikals",
            konteksts="Budžetā neviens nerunā par {120|150} - runā par "
                      "četrām piektdaļām.",
            kapec="Saīsināta daļa ir tā pati summa, tikai saprotami "
                  "pateikta."),

    Kopsavilkums([
        "Saīsinu daļu ar lielāko kopīgo dalītāju.",
        "Saīsinu daļu vairākos mazākos soļos.",
        "Izvēlos sev ērtāko paņēmienu un pamatoju izvēli.",
        "Pārbaudu, vai iegūtā daļa ir nesaīsināma.",
    ]),

    Majas([
        "Saīsini {60|144} abos veidos un salīdzini rezultātus.",
        "Atrodi daļu, kuru ērtāk saīsināt pa soļiem, un paskaidro, kāpēc.",
        "Uzraksti daļu, kuras abi locekļi ir trīsciparu skaitļi, un saīsini "
        "to.",
    ]),
]
