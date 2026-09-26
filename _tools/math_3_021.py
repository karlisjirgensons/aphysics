# -*- coding: utf-8 -*-
"""3. klase, 21. stunda: «Cik zīmuļus var nopirkt?»

Dalīšana ar naudu. Te pirmo reizi parādās atlikums: par 50 centiem pie cenas
7 centi var nopirkt 7 zīmuļus, un 1 cents paliek pāri. Dzīvē atlikums ir
normāls, un uzdevuma atbilde ir divi skaitļi, ne viens.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, kolonnas)

TEMA = "Cik zīmuļus var nopirkt?"

MERKIS = ("Risināsim sadzīves uzdevumus ar dalīšanu un sapratīsim, ko nozīmē "
          "atlikums.")

SATURS = [
    Sakums("Kāpēc veikalā nauda gandrīz nekad nepaliek tieši nulle?",
           zimejums=kolonnas([("1 zīmulis", 7), ("kabatā", 50)], " ct"),
           paraksts="50 ct dalās ar 7 nevienmērīgi - kaut kas paliks pāri.",
           fakti=["Dalot naudu ar cenu, bieži paliek atlikums.",
                  "Atlikums ir tas, kas vairs nepietiek vienai precei."]),

    Doma("Atlikums ir tas, kas nepietiek vēl vienai grupai",
         "Meklē lielāko reizinājumu, kas vēl ietilpst summā - pārējais ir "
         "atlikums.",
         soli=[
             "Pārbaudi cenas rindu: 7, 14, 21, 28, 35, 42, 49, 56.",
             "Atrodi pēdējo skaitli, kas vēl nav lielāks par summu.",
             "Reizinātājs pie tā ir preču skaits.",
             "Atņem šo skaitli no summas - paliek atlikums.",
         ],
         pieze="Atlikums vienmēr ir *mazāks* par cenu. Ja tas sanāk lielāks, "
               "vēl vienu preci varēja nopirkt."),

    Paraugs("Cik zīmuļus var nopirkt par 50 centiem?",
            uzd="Viens zīmulis maksā 7 ct. Cik zīmuļu var nopirkt par 50 ct "
                "un cik naudas paliks pāri?",
            soli=[
                ("7, 14, 21, 28, 35, 42, 49",
                 "Septiņnieku rinda - cik maksā 1, 2, 3, ... zīmuļi."),
                ("49 ≤ 50, bet 56 > 50",
                 "Septiņi zīmuļi vēl ietilpst, astoņi vairs ne."),
                ("50 − 49 = 1",
                 "Pāri paliek viens cents."),
            ],
            atbilde="7 zīmuļi; pāri paliek 1 ct"),

    Ievadi("Cik pietiek naudas?", [
        {"jaut": "Dzēšgumija maksā 6 ct. Cik dzēšgumiju var nopirkt par "
                 "42 ct?",
         "atb": ["7"], "padoms": "42 : 6."},
        {"jaut": "Cik dzēšgumiju var nopirkt par 40 ct?",
         "atb": ["6"], "padoms": "36 ≤ 40, bet 42 > 40."},
        {"jaut": "Cik centu paliks pāri no 40 ct?",
         "atb": ["4"], "padoms": "40 − 36."},
        {"jaut": "Pildspalva maksā 9 ct. Cik pildspalvu var nopirkt par "
                 "63 ct?",
         "atb": ["7"], "padoms": "63 : 9."},
        {"jaut": "Burtnīca maksā 8 ct. Cik burtnīcu var nopirkt par 50 ct?",
         "atb": ["6"], "padoms": "48 ≤ 50, bet 56 > 50."},
        {"jaut": "Cik centu paliks pāri no 50 ct?",
         "atb": ["2"], "padoms": "50 − 48."},
    ], pamats=4),

    Zimejums("Kur beidzas nauda",
             kolonnas([("5 gab.", 35), ("6 gab.", 42), ("7 gab.", 49),
                       ("8 gab.", 56)], " ct"),
             paskaidro="Ja kabatā ir 50 ct, pēdējais stabiņš jau ir par "
                       "augstu - tātad var nopirkt septiņus.",
             ievads="Zīmulis maksā 7 ct. Tā aug pirkuma summa."),

    Varianti("Vai atlikums ir pareizs?", [
        {"jaut": "Prece maksā 6 ct, kabatā 38 ct. Cik preču var nopirkt?",
         "opcijas": ["6", "7", "5", "8"],
         "pareizi": 0, "padoms": "36 ≤ 38, bet 42 > 38."},
        {"jaut": "Cik centu paliks pāri?",
         "opcijas": ["2", "6", "4", "0"],
         "pareizi": 0, "padoms": "38 − 36."},
        {"jaut": "Kurš atlikums *nevar* rasties, dalot ar 7?",
         "opcijas": ["8", "6", "3", "0"],
         "pareizi": 0, "padoms": "Atlikums vienmēr ir mazāks par dalītāju."},
        {"jaut": "Kabatā 45 ct, prece maksā 9 ct. Cik paliks pāri?",
         "opcijas": ["0", "9", "5", "4"],
         "pareizi": 0, "padoms": "45 : 9 = 5 bez atlikuma."},
    ], pamats=4),

    Pasaule("Ko nopirkt skolas somā?",
            Ievadi("", [
                {"jaut": "Kabatā ir 60 ct. Zīmulis maksā 8 ct. Cik zīmuļu "
                         "var nopirkt?",
                 "atb": ["7"], "padoms": "56 ≤ 60, bet 64 > 60."},
                {"jaut": "Cik centu paliks pāri?",
                 "atb": ["4"], "padoms": "60 − 56."},
                {"jaut": "Ja zīmuļus pārdod pa 6 ct, cik to var nopirkt par "
                         "60 ct?",
                 "atb": ["10"], "padoms": "60 : 6."},
                {"jaut": "Par cik centiem lētāk iznāk 7 zīmuļi pa 6 ct nekā "
                         "pa 8 ct?",
                 "atb": ["14"], "padoms": "56 − 42."},
            ]),
            pavediens="veikals",
            konteksts="Veikalā vispirms skatās cenu, tad kabatu - un tikai "
                      "tad izlemj, cik ņemt.",
            kapec="Dalīšana ar atlikumu pasaka gan preču skaitu, gan atlikušo "
                  "naudu."),

    Kopsavilkums([
        "Risinu sadzīves uzdevumus ar dalīšanu.",
        "Atrodu lielāko reizinājumu, kas vēl ietilpst summā.",
        "Izrēķinu atlikumu un zinu, ka tas ir mazāks par dalītāju.",
        "Atbildē nosaucu gan preču skaitu, gan atlikušo naudu.",
    ]),

    Majas([
        "Paskaties veikala čekā, cik maksā viena prece, un izrēķini, cik "
        "tādu varētu nopirkt par 5 eiro.",
        "Sadali 50 ct pa 6 ct un pasaki, cik paliek pāri.",
        "Izdomā pirkumu, kurā atlikums ir tieši 0.",
    ]),
]
