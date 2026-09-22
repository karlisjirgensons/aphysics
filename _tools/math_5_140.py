# -*- coding: utf-8 -*-
"""5. klase, 140. stunda: «Cik apmēram sanāks?»

Tas pats novērtējums, kas 100. stundā bija jauktiem skaitļiem, tagad ar
komatu. Decimāldaļām tas ir vēl vajadzīgāks: pazaudēts komats maina atbildi
desmitkārt, un tieši to novērtējums pamana uzreiz. Tāpēc te nav svarīgi
rēķināt precīzi - svarīgi ir zināt, kādai atbildei jāsanāk.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Cik apmēram sanāks?"

MERKIS = ("Mācīsimies novērtēt rezultāta aptuveno vērtību, salīdzinot to ar "
          "veselu skaitli.")

SATURS = [
    Sakums("Apmēram cik būs 3,9 + 2,1?",
           zimejums=taisne(0, 8, 2, [(3.9, "3,9"), (2.1, "2,1")],
                           virsraksts="Abi skaitļi tuvu veseliem"),
           paraksts="3,9 ir gandrīz 4, bet 2,1 - gandrīz 2. Summa būs ap 6.",
           fakti=["Precīzs rēķins prasa laiku.",
                  "Novērtējums pasaka, kādai atbildei jāsanāk.",
                  "Ja atbilde ir 0,6 vai 60, kaut kas ir greizi."]),

    Doma("Noapaļo līdz veselam",
         "Aptuveno rezultātu iegūst, katru skaitli noapaļojot līdz tuvākajam "
         "veselam skaitlim un izpildot darbību ar tiem.",
         soli=[
             "Paskaties uz pirmo ciparu aiz komata.",
             "Mazāks par 5 - noapaļo uz leju; 5 vai lielāks - uz augšu.",
             "Izpildi darbību ar noapaļotajiem skaitļiem.",
             "Salīdzini precīzo atbildi ar novērtējumu.",
             "Ja tās atšķiras vairāk nekā par 1, meklē kļūdu.",
         ],
         pieze="Novērtējums vispirms pamana komata kļūdu. Ja gaidīji 6, bet "
               "iznāca 0,6, komats ir nobīdījies par vienu vietu - un tieši "
               "tā ir biežākā kļūda ar decimāldaļām."),

    Paraugs("Novērtē 3,9 + 2,1",
            uzd="Novērtē summu un tad izrēķini to precīzi.",
            soli=[
                ("3,9 ir apmēram 4",
                 "Pirmais cipars aiz komata ir 9."),
                ("2,1 ir apmēram 2",
                 "Pirmais cipars ir 1."),
                ("Apmēram 4 + 2 = 6",
                 "Novērtējums."),
                ("Precīzi: 3,9 + 2,1 = 6",
                 "Šoreiz sakrīt tieši."),
            ],
            atbilde="Apmēram 6; precīzi arī 6"),

    Ievadi("Novērtē rezultātu", [
        {"jaut": "Līdz kuram veselam noapaļo 3,9?",
         "atb": ["4"], "padoms": "9 ir lielāks par 5."},
        {"jaut": "Līdz kuram veselam noapaļo 2,1?",
         "atb": ["2"], "padoms": "1 ir mazāks par 5."},
        {"jaut": "Cik apmēram ir 3,9 + 2,1?",
         "atb": ["6"], "padoms": "4 + 2."},
        {"jaut": "Cik apmēram ir 7,8 - 2,2?",
         "atb": ["6"], "padoms": "8 - 2."},
        {"jaut": "Cik apmēram ir 5,4 + 3,6?",
         "atb": ["9"], "padoms": "5 + 4."},
        {"jaut": "Līdz kuram veselam noapaļo 4,5?",
         "atb": ["5"], "padoms": "5 noapaļo uz augšu."},
        {"jaut": "Cik apmēram ir 12,3 - 4,8?",
         "atb": ["7"], "padoms": "12 - 5."},
        {"jaut": "Cik apmēram ir 0,9 + 0,8?",
         "atb": ["2"], "padoms": "1 + 1."},
    ], pamats=4,
        ievads="Noapaļo abus skaitļus un izpildi darbību ar veseliem."),

    Zimejums("Tuvākais veselais",
             taisne(0, 5, 1, [(3.9, "3,9"), (4.2, "4,2")],
                    virsraksts="Abi noapaļojas līdz 4"),
             paskaidro="3,9 ir mazliet zem četrinieka, 4,2 - mazliet "
                       "virs. Abi noapaļojas līdz vienam un tam pašam "
                       "skaitlim.",
             ievads="Uz taisnes redz, kurš veselais ir tuvāk."),

    Varianti("Vai atbilde ir ticama?", [
        {"jaut": "Cik apmēram ir 3,9 + 2,1?",
         "opcijas": ["6", "0,6", "60", "5"],
         "pareizi": 0,
         "padoms": "4 + 2."},
        {"jaut": "Novērtējums ir 6, bet atbilde iznāca 0,6. Ko tas nozīmē?",
         "opcijas": ["Komats ir nobīdījies", "Viss kārtībā",
                     "Jānoapaļo citādi", "Atbilde ir precīzāka"],
         "pareizi": 0,
         "padoms": "Desmitkārt mazāk."},
        {"jaut": "Līdz kuram veselam noapaļo 6,7?",
         "opcijas": ["7", "6", "6,5", "70"],
         "pareizi": 0,
         "padoms": "7 ir lielāks par 5."},
        {"jaut": "Cik apmēram ir 9,1 - 3,9?",
         "opcijas": ["5", "6", "4", "13"],
         "pareizi": 0,
         "padoms": "9 - 4."},
        {"jaut": "Kāpēc novērtē pirms rēķina?",
         "opcijas": ["Lai zinātu, kādai atbildei jāsanāk",
                     "Lai nerēķinātu vispār",
                     "Lai atbilde būtu precīzāka",
                     "Tas nav vajadzīgs"],
         "pareizi": 0,
         "padoms": "Novērtējums ir pārbaude."},
        {"jaut": "Kuru ciparu skatās, noapaļojot?",
         "opcijas": ["Pirmo aiz komata", "Pēdējo aiz komata",
                     "Pirmo pirms komata", "Visus"],
         "pareizi": 0,
         "padoms": "Desmitdaļas izšķir."},
    ], pamats=4),

    Pasaule("Vai naudas pietiks?",
            Ievadi("", [
                {"jaut": "Preces maksā 3,9 € un 2,1 €. Cik apmēram eiro "
                         "vajag?",
                 "atb": ["6"], "padoms": "4 + 2."},
                {"jaut": "Preces maksā 5,4 € un 3,6 €. Cik apmēram eiro "
                         "vajag?",
                 "atb": ["9"], "padoms": "5 + 4."},
                {"jaut": "Ir 10 €, prece maksā 7,8 €. Cik apmēram eiro "
                         "paliks?",
                 "atb": ["2"], "padoms": "10 - 8."},
                {"jaut": "Ir 20 €, preces maksā 8,9 € un 6,2 €. Cik apmēram "
                         "eiro paliks?",
                 "atb": ["5"], "padoms": "20 - 9 - 6."},
            ]),
            pavediens="maja",
            konteksts="Pie kases nav laika precīziem rēķiniem - jāzina "
                      "tikai, vai naudas pietiks.",
            kapec="Novērtējums to pasaka dažās sekundēs."),

    Kopsavilkums([
        "Noapaļoju decimāldaļu līdz tuvākajam veselam skaitlim.",
        "Novērtēju summas vai starpības aptuveno vērtību.",
        "Salīdzinu precīzo atbildi ar novērtējumu.",
        "Pamanu komata kļūdu, salīdzinot ar novērtējumu.",
    ]),

    Majas([
        "Novērtē un tad izrēķini 8,7 + 4,4 un 15,2 - 6,8.",
        "Atrodi piemēru, kurā novērtējums un atbilde atšķiras gandrīz par "
        "vienu.",
        "Uzraksti, kā novērtējums palīdz pamanīt komata kļūdu.",
    ]),
]
