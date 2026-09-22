# -*- coding: utf-8 -*-
"""6. klase, 27. stunda: «Daļa no skaitļa vai reizinājums?»

Mikrotemata noslēgums. 5. klasē daļu no skaitļa rēķināja divos soļos - dalīja
un reizināja. Tagad izrādās, ka tas viss ir viena reizināšana, un abi ceļi
ved uz vienu atbildi. Secinājumu formulē paši skolēni.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Daļa no skaitļa vai reizinājums?"

MERKIS = ("Salīdzināsim daļas no vesela skaitļa aprēķinu ar reizinājumu un "
          "formulēsim secinājumu.")

SATURS = [
    Sakums("Divi ceļi, viena atbilde",
           fakti=["{3|5} no 40: dala ar 5, reizina ar 3 - iznāk 24.",
                  "{3|5} · 40: reizina ar 3, dala ar 5 - atkal 24.",
                  "Vārds «no» matemātikā nozīmē reizināšanu."]),

    Doma("«No» nozīmē «reiz»",
         "Daļa no skaitļa un daļas reizinājums ar to skaitli ir viena un tā "
         "pati darbība - tikai izteikta ar dažādiem vārdiem.",
         soli=[
             "Pieraksti uzdevumu ar vārdiem: «kāda daļa no kāda skaitļa».",
             "Aizstāj vārdu «no» ar reizināšanas zīmi.",
             "Izrēķini kā parastu reizinājumu, saīsinot pirms reizināšanas.",
             "Pārbaudi otrā ceļā: dali ar saucēju, reizini ar skaitītāju.",
             "Salīdzini abas atbildes - tām jāsakrīt.",
         ],
         pieze="Ērtāk ir tas ceļš, kurā dalīšana sanāk gluda. {5|6} no 42: "
               "vispirms 42 : 6 = 7, tad 7 · 5 = 35. Reizinot vispirms, "
               "nāktos rēķināt 210 : 6."),

    Paraugs("Divi ceļi vienam uzdevumam",
            uzd="Cik ir {3|8} no 56?",
            soli=[
                ("Pirmais ceļš: 56 : 8 = 7",
                 "Vispirms viena astotdaļa."),
                ("7 · 3 = 21",
                 "Tad trīs astotdaļas."),
                ("Otrais ceļš: {3|8} · 56",
                 "Tas pats kā reizinājums."),
                ("Saīsina 56 un 8: {3|1} · 7 = 21",
                 "Tā pati atbilde."),
            ],
            atbilde="21"),

    Ievadi("Aprēķini daļu no skaitļa", [
        {"jaut": "Cik ir {2|3} no 21?",
         "atb": ["14"], "padoms": "21 : 3 = 7; 7 · 2."},
        {"jaut": "Cik ir {3|4} no 48?",
         "atb": ["36"], "padoms": "48 : 4 = 12; 12 · 3."},
        {"jaut": "Cik ir {5|6} no 54?",
         "atb": ["45"], "padoms": "54 : 6 = 9; 9 · 5."},
        {"jaut": "Cik ir {7|10} no 90?",
         "atb": ["63"], "padoms": "90 : 10 = 9; 9 · 7."},
        {"jaut": "Cik ir {2|5} no 35?",
         "atb": ["14"], "padoms": "35 : 5 = 7."},
        {"jaut": "{3|7} no kāda skaitļa ir 12. Kāds ir tas skaitlis?",
         "atb": ["28"], "padoms": "Viena septītdaļa ir 4."},
    ], pamats=4,
        ievads="Izvēlies to ceļu, kurā dalīšana sanāk bez atlikuma."),

    Varianti("Kurš pieraksts ir tas pats?", [
        {"jaut": "«{2|5} no 30» ir tas pats, kas...",
         "opcijas": ["{2|5} · 30", "30 : {2|5}", "{2|5} + 30", "30 − {2|5}"],
         "pareizi": 0,
         "padoms": "Vārds «no» nozīmē reizināšanu."},
        {"jaut": "Kurš ceļš ir ērtāks uzdevumam «{4|9} no 45»?",
         "opcijas": ["Vispirms 45 : 9", "Vispirms 4 · 45",
                     "Vispirms 45 : 4", "Abi vienlīdz grūti"],
         "pareizi": 0,
         "padoms": "45 dalās ar 9 gludi."},
        {"jaut": "{1|2} no {1|3} ir...",
         "opcijas": ["{1|6}", "{1|5}", "{2|3}", "{1|2}"],
         "pareizi": 0,
         "padoms": "Arī te «no» ir reizināšana."},
        {"jaut": "Kāpēc abi ceļi dod vienu atbildi?",
         "opcijas": ["Jo reizināšanas secību drīkst mainīt",
                     "Jo skaitļi ir mazi",
                     "Tā ir sakritība",
                     "Tie ne vienmēr dod vienu atbildi"],
         "pareizi": 0,
         "padoms": "{3|8} · 56 var rēķināt no abām pusēm."},
    ], pamats=4),

    Pasaule("Cik maksā ar atlaidi?",
            Ievadi("", [
                {"jaut": "Prece maksā 60 €, cena ir {3|4} no sākotnējās. Cik "
                         "eiro tagad?",
                 "atb": ["45"], "padoms": "60 : 4 = 15; 15 · 3."},
                {"jaut": "Cik eiro ir ietaupīts?",
                 "atb": ["15"], "padoms": "60 − 45 vai {1|4} no 60."},
                {"jaut": "Otra prece maksā 84 €, cena ir {2|3} no "
                         "sākotnējās. Cik eiro tagad?",
                 "atb": ["56"], "padoms": "84 : 3 = 28; 28 · 2."},
                {"jaut": "Trešā prece pēc atlaides maksā 36 €, kas ir {3|5} "
                         "no sākotnējās. Cik eiro tā maksāja?",
                 "atb": ["60"], "padoms": "Viena piektdaļa ir 12."},
            ]),
            pavediens="veikals",
            konteksts="Veikalā cenu zīmē reti raksta daļās, bet atlaide "
                      "vienmēr ir daļa no sākotnējās cenas.",
            kapec="Viens un tas pats rēķins der gan daļām, gan procentiem."),

    Kopsavilkums([
        "Zinu, ka «daļa no skaitļa» ir reizināšana.",
        "Rēķinu abos ceļos un izvēlos ērtāko.",
        "Pārbaudu, vai abas atbildes sakrīt.",
        "Atrodu skaitli, ja zināma tā daļa.",
    ]),

    Majas([
        "Izrēķini {5|8} no 64 abos ceļos.",
        "Atrodi skaitli, kura {2|7} ir 10.",
        "Pieraksti trīs teikumus ar vārdu «no» un pārraksti tos ar "
        "reizināšanas zīmi.",
    ]),
]
