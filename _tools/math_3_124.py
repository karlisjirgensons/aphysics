# -*- coding: utf-8 -*-
"""3. klase, 124. stunda: «Cik litru vajag?»

Tilpums sadzīves uzdevumos. Te apvienojas viss, kas iemācīts: mērvienību
pārrēķini, reizināšana un dalīšana ar atlikumu, kā arī noapaļošana uz augšu -
jo pusi pudeles nopirkt nevar.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, kolonnas)

TEMA = "Cik litru vajag?"

MERKIS = ("Veiksim vienkāršus aprēķinus ar tilpumu sadzīves situācijā.")

SATURS = [
    Sakums("Cik pudeļu ūdens vajag klases pārgājienam?",
           zimejums=kolonnas([("vajag", 6), ("pudelē", 2)], " l"),
           paraksts="Sešiem litriem vajag trīs divlitru pudeles.",
           fakti=["1 l = 1000 ml.",
                  "Ja vajadzīgais daudzums nedalās, pudeļu skaitu noapaļo uz "
                  "augšu."]),

    Doma("Izdali vajadzīgo ar vienas pudeles tilpumu",
         "Ja dalījums nav vesels, pudeļu skaitu noapaļo uz augšu - citādi "
         "kādam nepietiks.",
         soli=[
             "Izrēķini, cik litru vajag pavisam.",
             "Izdali to ar vienas pudeles tilpumu.",
             "Ja iznāk atlikums, pieliec vēl vienu pudeli.",
             "Pārbaudi, vai pietiek visiem.",
         ],
         pieze="Tā ir tā pati noapaļošana uz augšu, kas 50. stundā bija ar "
               "autobusiem: daļu pudeles nopirkt nevar."),

    Paraugs("Cik pudeļu vajag?",
            uzd="Pārgājienā vajag 7 litrus ūdens. Vienā pudelē ir 2 litri. "
                "Cik pudeļu vajag?",
            soli=[
                ("7 : 2 = 3, atlikums 1",
                 "Trīs pudeles dod 6 litrus."),
                ("Viens litrs vēl trūkst",
                 "Ar sešiem litriem nepietiek."),
                ("Vajag 4 pudeles",
                 "Ceturtā pudele nosedz atlikumu."),
            ],
            atbilde="4 pudeles"),

    Ievadi("Cik vajag?", [
        {"jaut": "Vajag 6 litrus, pudelē 2 l. Cik pudeļu vajag?",
         "atb": ["3"], "padoms": "6 : 2."},
        {"jaut": "Vajag 7 litrus, pudelē 2 l. Cik pudeļu vajag?",
         "atb": ["4"], "padoms": "Trīs nepietiek."},
        {"jaut": "Vajag 5 litrus, pudelē 1,5 l. Cik pudeļu vajag?",
         "atb": ["4"], "padoms": "Trīs dod 4,5 l."},
        {"jaut": "Cik mililitru ir 3 litri?", "atb": ["3000"],
         "padoms": "3 · 1000."},
        {"jaut": "Katram no 12 bērniem vajag 500 ml. Cik litru vajag kopā?",
         "atb": ["6"], "padoms": "12 · 500 = 6000 ml."},
        {"jaut": "Cik divlitru pudeļu tas ir?", "atb": ["3"],
         "padoms": "6 : 2."},
    ], pamats=4),

    Zimejums("Cik pietiek",
             kolonnas([("3 pudeles", 6), ("vajag", 7), ("4 pudeles", 8)],
                      " l"),
             paskaidro="Trīs pudeles ir par maz, četras - tieši pietiek ar "
                       "rezervi.",
             ievads="Septiņi litri un divlitru pudeles."),

    Varianti("Cik pudeļu vajag?", [
        {"jaut": "Vajag 9 litrus, pudelē 2 l. Cik pudeļu vajag?",
         "opcijas": ["5", "4", "6", "9"],
         "pareizi": 0, "padoms": "Četras dod 8 litrus."},
        {"jaut": "Cik litru ir 2500 ml?",
         "opcijas": ["2,5", "25", "250", "0,25"],
         "pareizi": 0, "padoms": "2500 : 1000."},
        {"jaut": "Kad pudeļu skaitu noapaļo uz augšu?",
         "opcijas": ["Kad ir atlikums", "Vienmēr", "Nekad",
                     "Kad skaitlis ir liels"],
         "pareizi": 0, "padoms": "Daļu pudeles nopirkt nevar."},
        {"jaut": "20 bērniem pa 300 ml. Cik litru vajag?",
         "opcijas": ["6", "60", "600", "0,6"],
         "pareizi": 0, "padoms": "6000 ml."},
    ], pamats=4),

    Pasaule("Cik ūdens patērē skolas ēdnīca?",
            Ievadi("", [
                {"jaut": "Katram no 200 skolēniem vajag 250 ml ūdens. Cik "
                         "mililitru kopā?",
                 "atb": ["50000", "50 000"], "padoms": "200 · 250."},
                {"jaut": "Cik litru tas ir?", "atb": ["50"],
                 "padoms": "50 000 : 1000."},
                {"jaut": "Cik desmitlitru kannu tas ir?", "atb": ["5"],
                 "padoms": "50 : 10."},
                {"jaut": "Cik litru ūdens vajag nedēļā, ja skolā ir 5 "
                         "dienas?",
                 "atb": ["250"], "padoms": "5 · 50."},
            ]),
            pavediens="planeta",
            konteksts="Skolas ēdnīca patērē desmitiem litru dienā - un visu "
                      "to saplāno iepriekš.",
            kapec="Bez aprēķina ūdens vai nepietiek, vai paliek pāri."),

    Kopsavilkums([
        "Veicu aprēķinus ar tilpumu sadzīves situācijās.",
        "Pārvēršu litrus mililitros un otrādi.",
        "Noapaļoju pudeļu skaitu uz augšu.",
        "Pārbaudu, vai daudzums tiešām pietiek.",
    ]),

    Majas([
        "Izrēķini, cik ūdens tava ģimene izdzer dienā.",
        "Pārbaudi, cik litru ir mājas lielākajā pudelē.",
        "Izrēķini, cik pudeļu vajag 10 litriem.",
    ]),
]
