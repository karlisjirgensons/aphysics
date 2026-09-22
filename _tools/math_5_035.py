# -*- coding: utf-8 -*-
"""5. klase, 35. stunda: «Ko par skaitli pasaka tā reizinātāji?»

Mikrotemata pēdējā stunda: sadalījums pirmreizinātājos vairs nav mērķis, bet
avots. No tā nolasa, vai skaitlis ir pāra, ar ko tas dalās un vai tas ir
kvadrāts - un nevienam no šiem jautājumiem vairs nav jāatbild ar dalīšanu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Ko par skaitli pasaka tā reizinātāji?"

MERKIS = ("Mācīsimies formulēt skaitļa īpašības pēc tā sadalījuma "
          "pirmreizinātājos.")

SATURS = [
    Sakums("Skaitli neredzam, sadalījumu - jā",
           fakti=["Kāds skaitlis sadalās kā 2 · 2 · 3 · 5.",
                  "Vai tas ir pāra? Vai tas dalās ar 6? Vai ar 9?",
                  "Uz visiem trim var atbildēt, skaitli neizrēķinot."]),

    Doma("Katrs dalītājs slēpjas reizinātājos",
         "Skaitlis dalās ar to, ko var salikt no tā pirmreizinātājiem.",
         soli=[
             "Paskaties, vai sadalījumā ir 2 - tad skaitlis ir pāra.",
             "Paskaties, vai ir 5 - tad skaitlis beidzas ar 0 vai 5.",
             "Lai pārbaudītu dalīšanu ar 6, meklē 2 un 3 kopā.",
             "Ja kāda reizinātāja nav, ar to skaitlis nedalās.",
         ],
         pieze="2 · 2 · 3 · 5 = 60. Tur ir 2 un 3, tāpēc 60 dalās ar 6. Bet "
               "trijnieks ir tikai viens, tāpēc ar 9 = 3 · 3 nedalās."),

    Paraugs("Nolasi īpašības no sadalījuma",
            uzd="Skaitlis sadalās kā 2 · 2 · 3 · 5. Vai tas dalās ar 4, 6, "
                "9 un 10?",
            soli=[
                ("Ar 4 dalās: 4 = 2 · 2, un abi divnieki ir",
                 "Divnieku sadalījumā ir tieši divi."),
                ("Ar 6 dalās: 6 = 2 · 3, un abi ir",
                 "Viens divnieks un viens trijnieks."),
                ("Ar 9 nedalās: 9 = 3 · 3, bet trijnieks ir tikai viens",
                 "Otra trijnieka sadalījumā nav."),
                ("Ar 10 dalās: 10 = 2 · 5",
                 "Abi reizinātāji atrodami."),
            ],
            atbilde="dalās ar 4, 6 un 10, bet ne ar 9"),

    Ievadi("Nolasi no sadalījuma 2 · 2 · 3 · 5", [
        {"jaut": "Kāds ir pats skaitlis?", "atb": ["60"],
         "padoms": "2 · 2 = 4, 4 · 3 = 12, 12 · 5."},
        {"jaut": "Vai tas dalās ar 4? Raksti dalījumu.", "atb": ["15"],
         "padoms": "60 : 4."},
        {"jaut": "Vai tas dalās ar 6? Raksti dalījumu.", "atb": ["10"],
         "padoms": "60 : 6."},
        {"jaut": "Cik ir 60 : 10?", "atb": ["6"],
         "padoms": "10 = 2 · 5."},
        {"jaut": "Skaitlis sadalās kā 2 · 3 · 3. Kāds ir pats skaitlis?",
         "atb": ["18"], "padoms": "2 · 9."},
        {"jaut": "Vai 18 dalās ar 9? Raksti dalījumu.", "atb": ["2"],
         "padoms": "Sadalījumā ir divi trijnieki."},
        {"jaut": "Skaitlis sadalās kā 3 · 3 · 5 · 5. Kāds ir pats skaitlis?",
         "atb": ["225"], "padoms": "9 · 25."},
        {"jaut": "Skaitlis sadalās kā 2 · 2 · 2. Kāds ir pats skaitlis?",
         "atb": ["8"], "padoms": "2 · 2 · 2."},
    ], pamats=4,
        ievads="Vispirms sareizini, ja vajag - bet mēģini nolasīt bez tā."),

    Varianti("Ko sadalījums pasaka?", [
        {"jaut": "Skaitļa sadalījumā nav neviena divnieka. Kāds ir skaitlis?",
         "opcijas": ["Nepāra", "Pāra", "Apaļš", "Pirmskaitlis"],
         "pareizi": 0,
         "padoms": "Pāra skaitlim vienmēr ir reizinātājs 2."},
        {"jaut": "Skaitlis sadalās kā 2 · 2 · 3 · 5. Vai tas dalās ar 9?",
         "opcijas": ["Nē, trijnieks ir tikai viens",
                     "Jā, jo ir trijnieks",
                     "Jā, jo skaitlis ir liels",
                     "Nevar zināt"],
         "pareizi": 0,
         "padoms": "9 = 3 · 3."},
        {"jaut": "Skaitļa sadalījumā ir 2 un 5. Ar ko tas noteikti dalās?",
         "opcijas": ["Ar 10", "Ar 7", "Ar 9", "Ar 25"],
         "pareizi": 0,
         "padoms": "2 · 5 = 10."},
        {"jaut": "Skaitlis sadalās kā 3 · 3 · 5 · 5. Kas par to zināms?",
         "opcijas": ["Tas ir kāda skaitļa kvadrāts",
                     "Tas ir pāra skaitlis",
                     "Tas ir pirmskaitlis",
                     "Tas dalās ar 2"],
         "pareizi": 0,
         "padoms": "3 · 5 = 15, un 15 · 15 = 225."},
        {"jaut": "Kurš skaitlis nedalās ar 6, ja sadalījums ir 2 · 2 · 2?",
         "opcijas": ["Pats šis skaitlis - 8", "Neviens",
                     "Skaitlis 12", "Skaitlis 24"],
         "pareizi": 0,
         "padoms": "6 = 2 · 3, bet trijnieka nav."},
        {"jaut": "Skaitļa sadalījumā ir viens vienīgs reizinātājs. Kas tas "
                 "par skaitli?",
         "opcijas": ["Pirmskaitlis", "Pāra skaitlis", "Kvadrāts",
                     "Skaitlis 1"],
         "pareizi": 0,
         "padoms": "Piemēram, 13 = 13."},
    ], pamats=4),

    Pasaule("Vai materiāls sadalīsies?",
            Ievadi("", [
                {"jaut": "Flīžu ir 60 (2 · 2 · 3 · 5). Cik flīžu būs katrā, "
                         "ja dala 6 vienādās daļās?",
                 "atb": ["10"], "padoms": "60 : 6."},
                {"jaut": "Vai tās var sadalīt 9 vienādās daļās? Raksti "
                         "atlikumu.",
                 "atb": ["6"], "padoms": "60 : 9 = 6, atlikums 6."},
                {"jaut": "Dēļu ir 18 (2 · 3 · 3). Cik dēļu būs katrā no "
                         "9 daļām?",
                 "atb": ["2"], "padoms": "18 : 9."},
                {"jaut": "Podiņu ir 225 (3 · 3 · 5 · 5). Cik rindu pa 15, "
                         "ja katrā rindā 15 podiņi?",
                 "atb": ["15"], "padoms": "225 : 15."},
            ]),
            pavediens="maja",
            konteksts="Pirms materiālu dala, var pateikt, vai tas sadalīsies "
                      "bez atlikuma - pietiek paskatīties uz reizinātājiem.",
            kapec="Ja vajadzīgā reizinātāja nav, sadalījums nesanāks."),

    Kopsavilkums([
        "Formulēju skaitļa īpašības pēc tā sadalījuma pirmreizinātājos.",
        "Nosaku, vai skaitlis ir pāra, neizrēķinot to.",
        "Pārbaudu dalāmību, meklējot vajadzīgos reizinātājus.",
        "Pamanu, kad skaitlis ir kāda skaitļa kvadrāts.",
    ]),

    Majas([
        "Sadali 180 pirmreizinātājos un pasaki, ar ko tas dalās: ar 4, 6, 9, "
        "10?",
        "Atrodi skaitli, kas dalās ar 4, bet nedalās ar 8.",
        "Izdomā skaitli pēc sadalījuma: divi divnieki un divi trijnieki.",
    ]),
]
