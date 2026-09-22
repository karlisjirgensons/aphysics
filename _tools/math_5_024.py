# -*- coding: utf-8 -*-
"""5. klase, 24. stunda: «Kurš paņēmiens ir racionālāks?»

Jauna temata sākums. 17. stundā saskaitāmos jau pārkārtoja; tagad tas pats
notiek ar reizinātājiem. Stundas mērķis nav «pareizais» paņēmiens, bet
izvēle: skolēns salīdzina divus ceļus un pasaka, kurš viņam ir ērtāks.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kurš paņēmiens ir racionālāks?"

MERKIS = ("Mācīsimies salīdzināt dažādus reizināšanas un dalīšanas "
          "paņēmienus un izvēlēties sev piemērotāko.")

SATURS = [
    Sakums("Trīs ceļi līdz vienai atbildei",
           fakti=["25 · 16 - rakstos, stabiņā, ar zīmuli.",
                  "Vai galvā: 25 · 4 = 100, un vēl reiz 4.",
                  "Atbilde abos gadījumos ir 400, ceļš ir dažāds."]),

    Doma("Reizinātājus drīkst pārkārtot un sadalīt",
         "Reizinājums nemainās, ja reizinātājus samaina vietām vai kādu no "
         "tiem sadala reizinātājos.",
         soli=[
             "Paskaties uz abiem reizinātājiem, pirms sāc rēķināt.",
             "Meklē, no kā var iznākt apaļš skaitlis: 25 · 4, 5 · 2, "
             "125 · 8.",
             "Sadali otru reizinātāju tā, lai tas pāris rastos.",
             "Reizini apaļo rezultātu ar atlikušo reizinātāju.",
         ],
         pieze="Dalīšanā noder tas pats: dalīt ar 50 ir tas pats, kas dalīt "
               "ar 100 un reizināt ar 2. Reizinātājus pārkārtot drīkst "
               "vienmēr, dalīšanā secību maina tikai apzināti."),

    Paraugs("Divi ceļi, viena atbilde",
            uzd="Aprēķini 25 · 16 divos veidos un izlem, kurš ir ērtāks.",
            soli=[
                ("1. ceļš: 25 · 16 stabiņā",
                 "Der vienmēr, bet prasa zīmuli un laiku."),
                ("2. ceļš: 16 = 4 · 4",
                 "Sadalām otro reizinātāju."),
                ("25 · 4 · 4 = 100 · 4 = 400",
                 "Pēc pirmā soļa skaitlis ir apaļš."),
                ("Galvā ātrāks ir otrais",
                 "Bet der tikai tad, ja pamana pāri 25 · 4."),
            ],
            atbilde="25 · 16 = 400"),

    Ievadi("Izrēķini galvā", [
        {"jaut": "25 · 12 = ?", "atb": ["300"],
         "padoms": "12 = 4 · 3; 25 · 4 = 100."},
        {"jaut": "50 · 18 = ?", "atb": ["900"],
         "padoms": "18 = 2 · 9; 50 · 2 = 100."},
        {"jaut": "125 · 8 = ?", "atb": ["1000"],
         "padoms": "Šis pāris ir vērts iegaumēt."},
        {"jaut": "4 · 17 · 25 = ?", "atb": ["1700"],
         "padoms": "Vispirms 4 · 25 = 100."},
        {"jaut": "35 · 2 · 5 = ?", "atb": ["350"],
         "padoms": "2 · 5 = 10."},
        {"jaut": "600 : 25 = ?", "atb": ["24"],
         "padoms": "600 : 100 = 6, tad reizini ar 4."},
        {"jaut": "1 400 : 50 = ?", "atb": ["28"],
         "padoms": "Dali ar 100 un reizini ar 2."},
        {"jaut": "16 · 250 = ?", "atb": ["4000"],
         "padoms": "16 = 4 · 4; 4 · 250 = 1 000."},
    ], pamats=4,
        ievads="Meklē pāri, no kura iznāk apaļš skaitlis."),

    Varianti("Kurš ceļš ir īsāks?", [
        {"jaut": "Kā ērtāk rēķināt 8 · 125?",
         "opcijas": ["Iegaumēt, ka sanāk 1 000", "Stabiņā",
                     "Saskaitīt 125 astoņas reizes", "Ar kalkulatoru"],
         "pareizi": 0,
         "padoms": "Šis pāris atkārtojas bieži."},
        {"jaut": "Kāpēc 25 · 16 ērti rēķināt kā 25 · 4 · 4?",
         "opcijas": ["Jo 25 · 4 dod apaļu 100",
                     "Jo 16 ir pāra skaitlis",
                     "Jo tā ir mazāk ciparu",
                     "Jo 4 ir mazs skaitlis"],
         "pareizi": 0,
         "padoms": "Ar apaļu skaitli tālāk rēķināt ir vieglāk."},
        {"jaut": "Kā ērtāk dalīt ar 50?",
         "opcijas": ["Dalīt ar 100 un reizināt ar 2",
                     "Dalīt ar 5 un tad ar 10",
                     "Reizināt ar 50", "Dalīt divreiz ar 25"],
         "pareizi": 0,
         "padoms": "50 · 2 = 100."},
        {"jaut": "Kurš paņēmiens ir «pareizais»?",
         "opcijas": ["Tas, kuru saproti un vari pārbaudīt",
                     "Vienmēr stabiņā", "Vienmēr galvā",
                     "Tas, kas ir grāmatā"],
         "pareizi": 0,
         "padoms": "Atbilde ir viena; ceļu drīkst izvēlēties."},
    ], pamats=4),

    Pasaule("Cik maksās viss grozs?",
            Ievadi("", [
                {"jaut": "25 paciņas pa 16 centiem. Cik centu kopā?",
                 "atb": ["400"], "padoms": "16 = 4 · 4; 25 · 4 = 100."},
                {"jaut": "8 kastes pa 125 gramiem. Cik gramu kopā?",
                 "atb": ["1000"], "padoms": "8 · 125."},
                {"jaut": "50 maizes klaipi pa 2 eiro. Cik eiro?",
                 "atb": ["100"], "padoms": "50 · 2."},
                {"jaut": "1 200 eiro jāsadala 25 vienādās daļās. Cik eiro "
                         "katrā?",
                 "atb": ["48"], "padoms": "1 200 : 100 = 12; 12 · 4."},
            ]),
            pavediens="veikals",
            konteksts="Veikalā kalkulatoru rokā netur - cenas pārbauda galvā, "
                      "ejot gar plauktu.",
            kapec="Apaļš starprezultāts ir tas, kas ļauj rēķināt galvā."),

    Kopsavilkums([
        "Salīdzinu vairākus paņēmienus vienam un tam pašam rēķinam.",
        "Pārkārtoju un sadalu reizinātājus, lai iznāktu apaļš skaitlis.",
        "Izvēlos sev ērtāko ceļu un pamatoju izvēli.",
        "Pārbaudu, vai atbilde abos ceļos sanāk viena un tā pati.",
    ]),

    Majas([
        "Izrēķini 24 · 25 divos veidos un salīdzini, kurš bija ātrāks.",
        "Iegaumē pārus 25 · 4, 125 · 8 un 5 · 2 - tie noder bieži.",
        "Atrodi čekā reizinājumu, kuru vari izrēķināt galvā.",
    ]),
]
