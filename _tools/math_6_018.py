# -*- coding: utf-8 -*-
"""6. klase, 18. stunda: «Ko nozīmē reizināt daļu ar veselu skaitli?»

Jauns temats. Reizināšana ar veselu skaitli ir vienīgā daļu darbība, ko var
saprast bez neviena jauna likuma - tā ir saskaitīšana, tikai īsāk pierakstīta.
Tāpēc modelis uz skaitļu taisnes te ir svarīgāks par formulu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Ko nozīmē reizināt daļu ar veselu skaitli?"

MERKIS = ("Mācīsimies modelēt vesela skaitļa un daļas reizinājumu uz skaitļu "
          "taisnes un pierakstīt rezultātu.")

SATURS = [
    Sakums("Trīsdimensiju printeris liek slāni pa slānim",
           zimejums=taisne(0, 2, 1, [(0.75, "3/4"), (1.5, "6/4")]),
           paraksts="Viens slānis ir {3|4} mm. Divi slāņi - {6|4} mm, tas "
                    "ir {1|2} mm vairāk nekā milimetrs.",
           fakti=["Printeris zina tikai vienu daļu - viena slāņa biezumu.",
                  "Detaļas augstums ir slāņu skaits reiz slāņa biezums.",
                  "Tāpēc 3D printerī reizināšana ar daļu notiek visu laiku."]),

    Doma("Reizināt nozīmē likt vienu un to pašu daļu vairākas reizes",
         "Reizinot daļu ar veselu skaitli, reizina skaitītāju; saucējs "
         "nemainās, jo daļas lielums paliek tas pats.",
         soli=[
             "Pieraksti, cik liela ir viena daļa.",
             "Atzīmē to uz skaitļu taisnes tik reižu, cik prasa reizinātājs.",
             "Reizini skaitītāju ar veselo skaitli.",
             "Saucēju atstāj neskartu.",
             "Ja iznāk neīsta daļa, izdali veselās daļas.",
         ],
         pieze="{3|4} · 2 ir tas pats, kas {3|4} + {3|4}. Saucējs pasaka, "
               "*cik lielas* ir daļas, un tās, liekot blakus, nekļūst ne "
               "lielākas, ne mazākas."),

    Paraugs("Četri slāņi pa {3|4} mm",
            uzd="Viens slānis ir {3|4} mm biezs. Cik biezi ir 4 slāņi?",
            soli=[
                ("{3|4} · 4",
                 "Reizinājums, nevis saskaitīšana četras reizes."),
                ("{3 · 4|4} = {12|4}",
                 "Reizina skaitītāju; saucējs paliek 4."),
                ("{12|4} = 3",
                 "12 : 4 = 3 - iznāk vesels skaitlis."),
                ("Pārbaude: {3|4} + {3|4} + {3|4} + {3|4} = 3",
                 "Tas pats rezultāts, saskaitot."),
            ],
            atbilde="3 mm"),

    Ievadi("Sareizini daļu ar veselo", [
        {"jaut": "Cik ir {1|5} · 3? Atbildi raksti kā a/b.",
         "atb": ["3/5"], "padoms": "Reizina tikai skaitītāju."},
        {"jaut": "Cik ir {2|7} · 2? Atbildi raksti kā a/b.",
         "atb": ["4/7"], "padoms": "2 · 2 = 4; saucējs paliek 7."},
        {"jaut": "Cik ir {3|8} · 4? Atbildi raksti kā a/b.",
         "atb": ["12/8", "3/2", "1 1/2"], "padoms": "3 · 4 = 12."},
        {"jaut": "Cik ir {1|4} · 8? Atbildi raksti kā vesels skaitlis.",
         "atb": ["2"], "padoms": "{8|4} = 2."},
        {"jaut": "Cik ir {2|3} · 6? Atbildi raksti kā vesels skaitlis.",
         "atb": ["4"], "padoms": "{12|3} = 4."},
        {"jaut": "Cik ir {5|6} · 3? Atbildi raksti kā a/b.",
         "atb": ["15/6", "5/2", "2 1/2"], "padoms": "5 · 3 = 15."},
    ], pamats=4,
        ievads="Saucējs reizinot nemainās - mainās tikai daļu skaits."),

    Zimejums("Seši gabali pa {1|3}",
             taisne(0, 2, 1, [(0.3333, "1/3"), (1.0, "3/3"), (2.0, "6/3")]),
             paskaidro="Trīs trešdaļas ir vesels; sešas trešdaļas ir divi "
                       "veseli.",
             ievads="Uz taisnes redz, kad neīsta daļa kļūst par veselu "
                    "skaitli."),

    Varianti("Kas notiek ar saucēju?", [
        {"jaut": "Reizinot {2|5} ar 3, kas notiek ar saucēju?",
         "opcijas": ["Nekas, tas paliek 5", "Tas kļūst 15",
                     "Tas kļūst 8", "Tas kļūst 3"],
         "pareizi": 0,
         "padoms": "Daļas lielums nemainās, mainās to skaits."},
        {"jaut": "Kurš pieraksts nozīmē to pašu, ko {3|7} · 4?",
         "opcijas": ["{3|7} + {3|7} + {3|7} + {3|7}", "{3|7} + 4",
                     "{12|28}", "{3|28}"],
         "pareizi": 0,
         "padoms": "Reizināšana ir vienādu saskaitāmo summa."},
        {"jaut": "{5|8} · 8 ir vienāds ar...",
         "opcijas": ["5", "{5|64}", "{13|8}", "40"],
         "pareizi": 0,
         "padoms": "{40|8} = 5."},
        {"jaut": "Kad reizinājums ar veselu skaitli ir vesels skaitlis?",
         "opcijas": ["Kad skaitītāja reizinājums dalās ar saucēju",
                     "Vienmēr", "Nekad",
                     "Kad reizinātājs ir pāra skaitlis"],
         "pareizi": 0,
         "padoms": "{12|4} ir vesels, {11|4} - nav."},
    ], pamats=4),

    Pasaule("Cik augsta būs detaļa?",
            Ievadi("", [
                {"jaut": "Viens slānis ir {1|4} mm. Cik mm augsti ir "
                         "12 slāņi?",
                 "atb": ["3"], "padoms": "{12|4} = 3."},
                {"jaut": "Viens slānis ir {2|5} mm. Cik mm augsti ir "
                         "10 slāņi?",
                 "atb": ["4"], "padoms": "{20|5} = 4."},
                {"jaut": "Viens slānis ir {3|10} mm. Cik mm augsti ir "
                         "20 slāņi?",
                 "atb": ["6"], "padoms": "{60|10} = 6."},
                {"jaut": "Detaļai jābūt 5 mm augstai, slānis ir {1|4} mm. "
                         "Cik slāņu vajag?",
                 "atb": ["20"], "padoms": "5 : {1|4} - cik ceturtdaļu ir "
                                          "piecos veselos."},
            ]),
            pavediens="tehnika",
            konteksts="Printeris nerēķina milimetrus - tas skaita slāņus, "
                      "un katrs slānis ir viena un tā pati daļa.",
            kapec="Reizināšana ar veselu skaitli ir vienīgā darbība, kas te "
                  "vajadzīga."),

    Kopsavilkums([
        "Attēloju daļas un vesela skaitļa reizinājumu uz skaitļu taisnes.",
        "Reizinu skaitītāju un atstāju saucēju neskartu.",
        "Pārveidoju neīstu daļu par jauktu vai veselu skaitli.",
        "Pārbaudu rezultātu, saskaitot vienādas daļas.",
    ]),

    Majas([
        "Uzzīmē skaitļu taisni no 0 līdz 3 un atzīmē uz tās {2|3} · 4.",
        "Atrodi mājās lietu, kuras izmērs ir daļa no centimetra, un "
        "izrēķini, cik būtu piecas tādas.",
        "Izdomā divus reizinājumus ar daļu, kuru rezultāts ir vesels "
        "skaitlis.",
    ]),
]
