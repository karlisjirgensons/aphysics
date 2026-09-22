# -*- coding: utf-8 -*-
"""6. klase, 53. stunda: «Cik apmēram būs dalījums?»

Mikrotemata noslēgums. Tas pats novērtēšanas rīks, kas bija parastajām
daļām, tagad dalīšanai ar decimāldaļām - un te tas ir vēl svarīgāks, jo
komata kļūda maina atbildi desmitkārt, nevis mazliet.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Cik apmēram būs dalījums?"

MERKIS = ("Mācīsimies novērtēt dalījuma aptuveno vērtību un salīdzināt "
          "dalījumus bez precīziem aprēķiniem.")

SATURS = [
    Sakums("Vispirms pasaki, cik apmēram",
           fakti=["29,4 : 2,9 ir apmēram 30 : 3, tātad ap 10.",
                  "Ja atbilde sanāk 1 vai 100, kļūda ir komata vietā.",
                  "Novērtējums ir viena rinda galvā, ne burtnīcā."]),

    Doma("Noapaļo abus skaitļus līdz ērtiem",
         "Dalījuma aptuveno vērtību iegūst, noapaļojot dalāmo un dalītāju "
         "tā, lai tie dalītos gludi.",
         soli=[
             "Noapaļo dalītāju līdz tuvākajam ērtajam skaitlim.",
             "Noapaļo dalāmo līdz skaitlim, kas ar to dalās.",
             "Izrēķini noapaļoto dalījumu galvā.",
             "Pārbaudi virzienu: dalītājs mazāks par 1 nozīmē lielāku "
             "rezultātu.",
             "Izrēķini precīzi un salīdzini.",
         ],
         pieze="Novērtējot dalīšanu, dalāmo pielāgo dalītājam, nevis otrādi: "
               "29,4 : 2,9 labāk noapaļot kā 30 : 3, nevis kā 29 : 3."),

    Paraugs("Novērtē un tad izrēķini",
            uzd="Cik apmēram ir 47,6 : 0,49?",
            soli=[
                ("0,49 ir apmēram 0,5",
                 "Dalītājs mazāks par 1 - rezultāts būs lielāks par 47,6."),
                ("47,6 ir apmēram 48",
                 "48 ar 0,5 dalās gludi."),
                ("48 : 0,5 = 96",
                 "Dalot ar pusi, skaitlis dubultojas."),
                ("Precīzi: 47,6 : 0,49 ir apmēram 97,1",
                 "Novērtējums bija tuvu."),
            ],
            atbilde="apmēram 96"),

    Ievadi("Novērtē dalījumu", [
        {"jaut": "Cik apmēram ir 29,4 : 2,9? Raksti veselu skaitli.",
         "atb": ["10"], "padoms": "30 : 3."},
        {"jaut": "Cik apmēram ir 61,5 : 0,21? Raksti veselu skaitli.",
         "atb": ["300"], "padoms": "60 : 0,2."},
        {"jaut": "Cik apmēram ir 8,1 : 0,9? Raksti veselu skaitli.",
         "atb": ["9"], "padoms": "8,1 : 0,9 ir tieši 9."},
        {"jaut": "18 : 0,5 ir lielāks vai mazāks par 18? Raksti «lielāks» "
                 "vai «mazāks».",
         "atb": ["lielāks"], "padoms": "Dalītājs mazāks par 1."},
        {"jaut": "18 : 1,5 ir lielāks vai mazāks par 18?",
         "atb": ["mazāks"], "padoms": "Dalītājs lielāks par 1."},
        {"jaut": "Cik apmēram ir 99,5 : 4,9? Raksti veselu skaitli.",
         "atb": ["20"], "padoms": "100 : 5."},
    ], pamats=4,
        ievads="Vispirms virziens, tad aptuvenais skaitlis."),

    Varianti("Vai atbilde ir ticama?", [
        {"jaut": "6,3 : 0,7 skolēns ieguva 0,9. Vai tas ir ticami?",
         "opcijas": ["Nē, jābūt ap 9", "Jā, tas ir pareizi",
                     "Nevar spriest", "Jā, jo skaitļi ir mazi"],
         "pareizi": 0,
         "padoms": "Dalot ar skaitli, kas mazāks par 1, rezultāts aug."},
        {"jaut": "Kurš dalījums ir lielāks: 12 : 0,4 vai 12 : 0,6?",
         "opcijas": ["12 : 0,4", "12 : 0,6", "Vienādi", "Nevar zināt"],
         "pareizi": 0,
         "padoms": "Mazāks dalītājs dod lielāku rezultātu."},
        {"jaut": "Kurš dalījums ir mazāks: 20 : 4 vai 20 : 5?",
         "opcijas": ["20 : 5", "20 : 4", "Vienādi", "Nevar zināt"],
         "pareizi": 0,
         "padoms": "Lielāks dalītājs dod mazāku rezultātu."},
        {"jaut": "Kāpēc novērtē pirms rēķina?",
         "opcijas": ["Lai pamanītu komata kļūdu",
                     "Lai nerēķinātu vispār",
                     "Lai būtu garāks pieraksts", "Tas nav vajadzīgs"],
         "pareizi": 0,
         "padoms": "Komata kļūda maina atbildi desmitkārt."},
    ], pamats=4),

    Pasaule("Vai pietiks materiāla?",
            Ievadi("", [
                {"jaut": "Ir 19,6 m auduma, vienam krēslam 1,9 m. Cik "
                         "apmēram krēslu? Raksti veselu skaitli.",
                 "atb": ["10"], "padoms": "20 : 2."},
                {"jaut": "Ir 48,5 kg krāsas, vienai sienai 0,49 kg. Cik "
                         "apmēram sienu? Raksti veselu skaitli.",
                 "atb": ["100"], "padoms": "48 : 0,5 ir 96, ap simtu."},
                {"jaut": "Ir 30,2 m vada, vienam savienojumam 0,48 m. Cik "
                         "apmēram savienojumu? Raksti veselu skaitli.",
                 "atb": ["60"], "padoms": "30 : 0,5."},
                {"jaut": "Ir 12,3 l līmes, vienai plāksnei 0,24 l. Cik "
                         "apmēram plākšņu? Raksti veselu skaitli.",
                 "atb": ["50"], "padoms": "12 : 0,25."},
            ]),
            pavediens="maja",
            konteksts="Pirms sākt darbu, jāzina nevis precīzs skaitlis, bet "
                      "tas, vai materiāla pietiks.",
            kapec="Novērtējums atbild uz šo jautājumu vienā rindā."),

    Kopsavilkums([
        "Novērtēju dalījuma aptuveno vērtību, noapaļojot abus skaitļus.",
        "Salīdzinu dalījumus, tos neizrēķinot.",
        "Zinu, kā dalītāja lielums nosaka rezultāta virzienu.",
        "Pamanu komata kļūdu, pirms to izlabo kāds cits.",
    ]),

    Majas([
        "Novērtē un tad izrēķini 81,6 : 3,9.",
        "Atrodi divus dalījumus, kuru novērtējums ir vienāds.",
        "Novērtē, cik reižu 0,33 l glāze ietilpst 1,5 l pudelē.",
    ]),
]
