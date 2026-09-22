# -*- coding: utf-8 -*-
"""6. klase, 28. stunda: «Kā dalījumu parādīt uz skaitļu taisnes?»

Dalīšana ar daļu sākas tur, kur to var saskaitīt. Uz skaitļu taisnes
jautājums «cik reižu ietilpst» ir redzams, un atbildi var pārbaudīt ar
reizināšanu - vēl pirms parādās jebkāds algoritms.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kā dalījumu parādīt uz skaitļu taisnes?"

MERKIS = ("Mācīsimies attēlot divu daļu dalījumu uz skaitļu taisnes un "
          "pārbaudīt rezultātu ar reizināšanu.")

SATURS = [
    Sakums("Cik {1|4} gabalu ir {3|4} metros?",
           zimejums=taisne(0, 1, 1, [(0.25, "1/4"), (0.5, "2/4"),
                                     (0.75, "3/4")]),
           paraksts="No 0 līdz {3|4} ietilpst tieši trīs ceturtdaļas: "
                    "{3|4} : {1|4} = 3.",
           fakti=["Dalīšana ar daļu joprojām jautā: cik reižu ietilpst?",
                  "Uz taisnes to var vienkārši saskaitīt."]),

    Doma("Mēro ar mazāko gabalu",
         "Daļu dalot ar daļu, skaita, cik reižu dalītājs ietilpst dalāmajā - "
         "uz skaitļu taisnes to var izmērīt ar vienu un to pašu soli.",
         soli=[
             "Atzīmē uz taisnes dalāmo.",
             "Sadali taisni tik daļās, cik liels ir dalītāja saucējs.",
             "Skaiti, cik dalītāja soļu ietilpst līdz dalāmajam.",
             "Pieraksti dalījumu.",
             "Pārbaudi ar reizināšanu: rezultāts reiz dalītājs dod dalāmo.",
         ],
         pieze="Ja abām daļām ir viens saucējs, dalīšana kļūst pavisam "
               "vienkārša: {6|8} : {2|8} = 6 : 2 = 3. Vienādi lielus gabalus "
               "atliek tikai saskaitīt."),

    Paraugs("Cik reižu {1|6} ietilpst {5|6}?",
            uzd="Attēlo un izrēķini {5|6} : {1|6}.",
            soli=[
                ("Sadali nogriezni no 0 līdz 1 sešās daļās",
                 "Saucējs ir 6."),
                ("Dalāmais {5|6} ir pie piektās iedaļas",
                 "Tur beidzas mērīšana."),
                ("Ietilpst 5 soļi pa {1|6}",
                 "Tik reižu dalītājs ietilpst."),
                ("Pārbaude: 5 · {1|6} = {5|6}",
                 "Rezultāts sakrīt ar dalāmo."),
            ],
            atbilde="5"),

    Zimejums("Vienāds saucējs - vienkāršs dalījums",
             taisne(0, 1, 1, [(0.25, "2/8"), (0.75, "6/8")]),
             paskaidro="{6|8} : {2|8} = 3, jo no nulles līdz {6|8} ietilpst "
                       "trīs soļi pa {2|8}.",
             ievads="Ja gabali ir vienādi, atliek saskaitīt soļus."),

    Ievadi("Saskaiti soļus", [
        {"jaut": "Cik ir {4|5} : {1|5}?",
         "atb": ["4"], "padoms": "Četri soļi pa {1|5}."},
        {"jaut": "Cik ir {6|7} : {2|7}?",
         "atb": ["3"], "padoms": "6 : 2."},
        {"jaut": "Cik ir {8|9} : {4|9}?",
         "atb": ["2"], "padoms": "8 : 4."},
        {"jaut": "Cik ir {3|4} : {1|4}?",
         "atb": ["3"], "padoms": "Trīs soļi pa ceturtdaļai."},
        {"jaut": "Cik ir {9|10} : {3|10}?",
         "atb": ["3"], "padoms": "9 : 3."},
        {"jaut": "Cik ir {1|2} : {1|8}? Vispirms pieraksti {1|2} kā {4|8}.",
         "atb": ["4"], "padoms": "{4|8} : {1|8} = 4."},
    ], pamats=4,
        ievads="Ja saucēji ir vienādi, dali tikai skaitītājus."),

    Varianti("Ko rāda taisne?", [
        {"jaut": "Uz taisnes redzams, ka {1|3} ietilpst {2|3} divas reizes. "
                 "Kāds ir dalījums?",
         "opcijas": ["2", "{2|9}", "{1|2}", "{3|2}"],
         "pareizi": 0,
         "padoms": "Divi soļi."},
        {"jaut": "Kāpēc {6|8} : {2|8} = 6 : 2?",
         "opcijas": ["Jo gabali ir vienāda lieluma",
                     "Jo saucējus atmet vienmēr",
                     "Jo 8 dalās ar 2", "Tā nav pareizi"],
         "pareizi": 0,
         "padoms": "Vienādus gabalus var vienkārši saskaitīt."},
        {"jaut": "Kā pārbaudīt dalījumu {5|6} : {1|6} = 5?",
         "opcijas": ["5 · {1|6} = {5|6}", "5 : {1|6}",
                     "{5|6} · 5", "{5|6} + {1|6}"],
         "pareizi": 0,
         "padoms": "Rezultāts reiz dalītājs."},
        {"jaut": "Ko darīt, ja saucēji ir dažādi?",
         "opcijas": ["Pārveidot par vienu kopsaucēju",
                     "Dalīt saucējus", "Atmest saucējus",
                     "Dalīt nevar"],
         "pareizi": 0,
         "padoms": "{1|2} var pārrakstīt kā {4|8}."},
    ], pamats=4),

    Pasaule("Cik porciju sanāks?",
            Ievadi("", [
                {"jaut": "Ir {3|4} kg riekstu, vienai porcijai {1|4} kg. Cik "
                         "porciju sanāks?",
                 "atb": ["3"], "padoms": "Trīs soļi pa {1|4}."},
                {"jaut": "Ir {5|8} l sulas, vienai glāzei {1|8} l. Cik "
                         "glāžu?",
                 "atb": ["5"], "padoms": "5 : 1."},
                {"jaut": "Ir {6|10} kg miltu, vienai maizei {2|10} kg. Cik "
                         "maizes klaipu?",
                 "atb": ["3"], "padoms": "6 : 2."},
                {"jaut": "Ir {1|2} kg sviesta, vienai receptei {1|8} kg. Cik "
                         "reizes pietiks?",
                 "atb": ["4"], "padoms": "{4|8} : {1|8}."},
            ]),
            pavediens="virtuve",
            konteksts="Virtuvē visbiežākais jautājums nav «cik ir kopā», bet "
                      "«cik reižu pietiks».",
            kapec="Dalīšana ar daļu atbild tieši uz šo jautājumu."),

    Kopsavilkums([
        "Attēloju divu daļu dalījumu uz skaitļu taisnes.",
        "Skaitu, cik reižu dalītājs ietilpst dalāmajā.",
        "Dalu daļas ar vienādiem saucējiem, dalot tikai skaitītājus.",
        "Pārbaudu dalījumu ar reizināšanu.",
    ]),

    Majas([
        "Uzzīmē taisni no 0 līdz 1 un parādi uz tās {7|8} : {1|8}.",
        "Atrodi divus dalījumus, kuru rezultāts ir 4.",
        "Pieraksti vārdiem, ko nozīmē {3|5} : {1|5}.",
    ]),
]
