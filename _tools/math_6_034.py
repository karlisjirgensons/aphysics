# -*- coding: utf-8 -*-
"""6. klase, 34. stunda: «Kā dalīt ar jauktu skaitli?»

Divi jau zināmi soļi vienā uzdevumā: pārveidot un apgriezt. Stunda vingrina
to secību, jo apgrieztu jauktu skaitli pierakstīt nevar - vispirms tam
jākļūst par neīstu daļu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā dalīt ar jauktu skaitli?"

MERKIS = ("Mācīsimies dalīt ar jauktu skaitli un pārbaudīt rezultātu.")

SATURS = [
    Sakums("Apgriezt jauktu skaitli nevar",
           fakti=["Vispirms 2{1|3} kļūst par {7|3}, un tikai tad - par {3|7}.",
                  "Divi soļi vienmēr vienā secībā: pārveido, tad apgriez.",
                  "Pārbaude ir tā pati: rezultāts reiz dalītājs."]),

    Doma("Pārveido, apgriez, sareizini",
         "Dalot ar jauktu skaitli, to vispirms pārveido par neīstu daļu, tad "
         "aizstāj ar apgriezto un reizina.",
         soli=[
             "Pārveido abus jauktos skaitļus par neīstām daļām.",
             "Atrodi dalītāja apgriezto skaitli.",
             "Aizstāj dalīšanu ar reizināšanu.",
             "Saīsini un sareizini.",
             "Atdali veselās daļas un pārbaudi.",
         ],
         pieze="Ja dalāmais ir vesels skaitlis, to arī raksta kā daļu: "
               "6 = {6|1}. Tad visi uzdevumi izskatās vienādi."),

    Paraugs("Dali ar jauktu skaitli",
            uzd="Cik ir 5{1|4} : 1{3|4}?",
            soli=[
                ("5{1|4} = {21|4}; 1{3|4} = {7|4}",
                 "Abi kļūst par neīstām daļām."),
                ("{21|4} : {7|4} = {21|4} · {4|7}",
                 "Dalītāju apgriež."),
                ("Saīsina 21 ar 7 un 4 ar 4: {3|1} · {1|1}",
                 "Paliek tikai mazi skaitļi."),
                ("= 3",
                 "Rezultāts ir vesels skaitlis."),
                ("Pārbaude: 3 · 1{3|4} = {21|4} = 5{1|4}",
                 "Atgriežas dalāmais."),
            ],
            atbilde="3"),

    Ievadi("Izdali ar jauktu skaitli", [
        {"jaut": "Cik ir 4{1|2} : 1{1|2}?",
         "atb": ["3"], "padoms": "{9|2} · {2|3}."},
        {"jaut": "Cik ir 3 : 1{1|2}?",
         "atb": ["2"], "padoms": "{3|1} · {2|3}."},
        {"jaut": "Cik ir 2{2|3} : 1{1|3}?",
         "atb": ["2"], "padoms": "{8|3} · {3|4}."},
        {"jaut": "Cik ir 7{1|2} : 2{1|2}?",
         "atb": ["3"], "padoms": "{15|2} · {2|5}."},
        {"jaut": "Cik ir 1{1|5} : 2{2|5}? Atbildi raksti kā a/b.",
         "atb": ["1/2"], "padoms": "{6|5} · {5|12}."},
        {"jaut": "Cik ir 6{1|4} : 1{1|4}?",
         "atb": ["5"], "padoms": "{25|4} · {4|5}."},
    ], pamats=4,
        ievads="Divi soļi vienā un tajā pašā secībā."),

    Pasaule("Cik reižu iztīrīs lauku?",
            Kustiba("", [
                {"jaut": "Robotam pietiek enerģijas 7{1|2} stundām, viens "
                         "aplis prasa 1{1|4} stundas. Cik apļu?",
                 "atb": 6, "beigas": 12, "iedala": 2, "mers": "apļi",
                 "merkis": "apļu skaits", "objekts": "Robots",
                 "padoms": "{15|2} · {4|5}."},
                {"jaut": "Pēc uzlādes pietiek 10 stundām, aplis prasa 2{1|2} "
                         "stundas. Cik apļu?",
                 "atb": 4, "beigas": 12, "iedala": 2, "mers": "apļi",
                 "merkis": "apļu skaits", "objekts": "Robots",
                 "padoms": "{10|1} · {2|5}."},
                {"jaut": "Mazākā laukā aplis prasa {5|6} stundas, enerģijas "
                         "ir 5 stundām. Cik apļu?",
                 "atb": 6, "beigas": 12, "iedala": 2, "mers": "apļi",
                 "merkis": "apļu skaits", "objekts": "Robots",
                 "padoms": "5 · {6|5}."},
                {"jaut": "Enerģijas ir 4{1|2} stundām, aplis prasa {3|4} "
                         "stundas. Cik apļu?",
                 "atb": 6, "beigas": 12, "iedala": 2, "mers": "apļi",
                 "merkis": "apļu skaits", "objekts": "Robots",
                 "padoms": "{9|2} · {4|3}."},
            ]),
            pavediens="tehnika",
            konteksts="Robots apstājas tieši tad, kad enerģija beidzas - "
                      "apļu skaitu var izrēķināt jau iepriekš.",
            kapec="Dalīšana ar jauktu skaitli atbild uz «cik reižu pietiks»."),

    Varianti("Kāda ir pareizā secība?", [
        {"jaut": "Kas jādara vispirms, dalot ar 2{1|3}?",
         "opcijas": ["Jāpārveido par {7|3}", "Jāapgriež, nepārveidojot",
                     "Jāsaīsina", "Jāsaskaita"],
         "pareizi": 0,
         "padoms": "Apgriezt var tikai daļu, ne jauktu skaitli."},
        {"jaut": "6 : 1{1|2} ir vienāds ar...",
         "opcijas": ["6 · {2|3}", "6 · {3|2}", "{1|6} · {3|2}", "6 · 1{1|2}"],
         "pareizi": 0,
         "padoms": "{3|2} apgrieztais ir {2|3}."},
        {"jaut": "Kāds ir rezultāts, ja dalāmais un dalītājs ir vienādi?",
         "opcijas": ["1", "0", "Pats skaitlis", "2"],
         "pareizi": 0,
         "padoms": "Jebkurš skaitlis, dalīts pats ar sevi."},
        {"jaut": "Dalot ar 1{1|2}, rezultāts būs...",
         "opcijas": ["mazāks par dalāmo", "lielāks par dalāmo",
                     "tāds pats", "vienmēr vesels"],
         "pareizi": 0,
         "padoms": "1{1|2} ir lielāks par 1."},
    ], pamats=4),

    Kopsavilkums([
        "Pārveidoju jauktu skaitli par neīstu daļu pirms dalīšanas.",
        "Aizstāju dalīšanu ar reizināšanu ar apgriezto skaitli.",
        "Saīsinu pirms reizināšanas un atdalu veselās daļas.",
        "Pārbaudu rezultātu ar reizināšanu.",
    ]),

    Majas([
        "Izrēķini 8{1|3} : 1{2|3} un pieraksti pārbaudi.",
        "Atrodi divus jauktus skaitļus, kuru dalījums ir tieši 2.",
        "Pieraksti, cik reižu 1{1|2} l pudele ietilpst 9 l kannā.",
    ]),
]
