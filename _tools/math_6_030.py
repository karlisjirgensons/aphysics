# -*- coding: utf-8 -*-
"""6. klase, 30. stunda: «Kāpēc dalīšanu var aizstāt ar reizināšanu?»

Algoritma stunda. Likumu «dalīt nozīmē reizināt ar apgriezto» var iemācīties
no galvas, bet tad tas aizmirstas. Te tas tiek izvests: no tā, ko skolēni
jau redzēja uz skaitļu taisnes, un no apgrieztā skaitļa.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kāpēc dalīšanu var aizstāt ar reizināšanu?"

MERKIS = ("Formulēsim algoritmu dalīšanai ar parasto daļu un pamatosim, "
          "kāpēc tas strādā.")

SATURS = [
    Sakums("Viens likums visai dalīšanai",
           fakti=["{3|4} : {1|2} ir tas pats, kas {3|4} · {2|1}.",
                  "Dalīšana ar daļu ir reizināšana ar tās apgriezto skaitli.",
                  "Tāpēc dalīšanai nav vajadzīgs atsevišķs algoritms."]),

    Doma("Dalīt ar daļu nozīmē reizināt ar apgriezto",
         "Ja dalītāju reizina ar tā apgriezto skaitli, iznāk 1 - tāpēc arī "
         "dalāmo drīkst reizināt ar to pašu apgriezto skaitli.",
         soli=[
             "Pieraksti dalījumu.",
             "Atrodi dalītāja apgriezto skaitli.",
             "Aizstāj dalīšanas zīmi ar reizināšanu un dalītāju - ar "
             "apgriezto.",
             "Saīsini un sareizini.",
             "Pārbaudi ar reizināšanu: rezultāts reiz dalītājs dod dalāmo.",
         ],
         pieze="Pārbaudi uz zināma piemēra: {6|8} : {2|8} = 3 no iepriekšējās "
               "stundas. Pēc algoritma {6|8} · {8|2} = {48|16} = 3 - tas "
               "pats."),

    Paraugs("No dalīšanas uz reizināšanu",
            uzd="Cik ir {3|4} : {2|5}?",
            soli=[
                ("Dalītājs ir {2|5}",
                 "Tā apgrieztais skaitlis ir {5|2}."),
                ("{3|4} · {5|2}",
                 "Dalīšana kļūst par reizināšanu."),
                ("= {15|8}",
                 "3 · 5 un 4 · 2."),
                ("= 1{7|8}",
                 "Neīsto daļu pārveido par jauktu skaitli."),
                ("Pārbaude: {15|8} · {2|5} = {30|40} = {3|4}",
                 "Atgriežas dalāmais."),
            ],
            atbilde="{15|8} = 1{7|8}"),

    Ievadi("Izdali, reizinot ar apgriezto", [
        {"jaut": "Cik ir {1|2} : {1|4}?",
         "atb": ["2"], "padoms": "{1|2} · {4|1}."},
        {"jaut": "Cik ir {2|3} : {4|9}? Atbildi raksti kā a/b.",
         "atb": ["3/2", "1 1/2"], "padoms": "{2|3} · {9|4}."},
        {"jaut": "Cik ir {5|6} : {5|12}?",
         "atb": ["2"], "padoms": "{5|6} · {12|5}."},
        {"jaut": "Cik ir {3|8} : {3|4}? Atbildi raksti kā a/b.",
         "atb": ["1/2"], "padoms": "{3|8} · {4|3}."},
        {"jaut": "Cik ir {7|10} : {7|10}?",
         "atb": ["1"], "padoms": "Skaitlis, dalīts pats ar sevi."},
        {"jaut": "Cik ir {4|5} : 2? Atbildi raksti kā a/b.",
         "atb": ["2/5"], "padoms": "2 = {2|1}; apgrieztais ir {1|2}."},
    ], pamats=4,
        ievads="Viens solis: apgriez dalītāju un maini zīmi."),

    Varianti("Ko tieši apgriež?", [
        {"jaut": "{2|3} : {5|7}. Kuru daļu apgriež?",
         "opcijas": ["Otro, {5|7}", "Pirmo, {2|3}", "Abas", "Nevienu"],
         "pareizi": 0,
         "padoms": "Apgriež dalītāju."},
        {"jaut": "Kāpēc dalīšanu drīkst aizstāt ar reizināšanu?",
         "opcijas": ["Jo skaitļa un apgrieztā reizinājums ir 1",
                     "Jo tā ir vieglāk", "Jo saucēji sakrīt",
                     "Tas ir tikai paņēmiens bez pamatojuma"],
         "pareizi": 0,
         "padoms": "Reizinot ar 1, nekas nemainās."},
        {"jaut": "{3|5} : 3 ir vienāds ar...",
         "opcijas": ["{3|5} · {1|3}", "{3|5} · 3",
                     "{5|3} · {1|3}", "{3|5} : {1|3}"],
         "pareizi": 0,
         "padoms": "3 = {3|1}, apgrieztais ir {1|3}."},
        {"jaut": "Skolēns rēķina {1|2} : {1|4} = {1|8}. Kur ir kļūda?",
         "opcijas": ["Viņš reizināja, neapgriežot dalītāju",
                     "Viņš apgrieza pirmo daļu",
                     "Viņš saskaitīja", "Kļūdas nav"],
         "pareizi": 0,
         "padoms": "Pareizi ir {1|2} · {4|1} = 2."},
    ], pamats=4),

    Pasaule("Cik reižu pietiks?",
            Ievadi("", [
                {"jaut": "Ir {3|4} l krāsas, vienam solam vajag {1|8} l. "
                         "Cik solu var nokrāsot?",
                 "atb": ["6"], "padoms": "{3|4} · {8|1} = 6."},
                {"jaut": "Ir {2|3} kg javas, vienai flīzei vajag {1|12} kg. "
                         "Cik flīžu var pielikt?",
                 "atb": ["8"], "padoms": "{2|3} · 12."},
                {"jaut": "Ir {5|6} m lentes, vienai dāvanai {5|24} m. Cik "
                         "dāvanu var iesaiņot?",
                 "atb": ["4"], "padoms": "{5|6} · {24|5}."},
                {"jaut": "Ir {7|8} l laka, vienam plauktam {7|16} l. Cik "
                         "plauktu pietiks?",
                 "atb": ["2"], "padoms": "{7|8} · {16|7}."},
            ]),
            pavediens="maja",
            konteksts="Remontā materiāls ir dots, un jautājums vienmēr ir "
                      "viens: cik reižu ar to pietiks?",
            kapec="Dalīšana ar daļu atbild vienā darbībā."),

    Kopsavilkums([
        "Formulēju algoritmu: dalīt ar daļu nozīmē reizināt ar apgriezto.",
        "Pamatoju, kāpēc tas strādā.",
        "Pielietoju to arī tad, kad dalītājs ir vesels skaitlis.",
        "Pārbaudu rezultātu ar reizināšanu.",
    ]),

    Majas([
        "Izrēķini {5|9} : {10|3} un pieraksti pārbaudi.",
        "Pārbaudi ar algoritmu vienu no iepriekšējās stundas uzdevumiem.",
        "Paskaidro kādam mājās, kāpēc dalot ar {1|2} skaitlis dubultojas.",
    ]),
]
