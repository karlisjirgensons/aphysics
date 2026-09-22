# -*- coding: utf-8 -*-
"""5. klase, 169. stunda: «Cik droši rēķinu ar daļām?»

Noslēguma stunda, un tā nav pārbaudes darbs: te skolēns pārbauda pats sevi.
Uzdevumi aptver visu, kas gada laikā darīts ar daļām un jauktiem skaitļiem,
un pēc katra bloka kopsavilkumā ir jautājums, kuru vēl vērts atkārtot.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala, restis)

TEMA = "Cik droši rēķinu ar daļām?"

MERKIS = ("Formatīvi pārbaudīsim darbības ar parastajām daļām un jauktiem "
          "skaitļiem.")

SATURS = [
    Sakums("Viss gads vienā stundā",
           zimejums=restis([["1/2", "3/4", "2 1/3"]],
                           virsraksts="Daļas, ar kurām gads pagāja"),
           paraksts="Saīsināšana, kopsaucējs, jaukti skaitļi - viss vienkopus.",
           fakti=["Šī nav pārbaude atzīmei.",
                  "Te pats vari redzēt, kas jau ir drošs.",
                  "Un kas vēl jāatkārto pirms 6. klases."]),

    Doma("Četras prasmes, kas jātur rokā",
         "Ar daļām 5. klasē jāprot četras lietas: saīsināt un paplašināt, "
         "salīdzināt, saskaitīt un atņemt ar dažādiem saucējiem, pārveidot "
         "jauktus skaitļus.",
         soli=[
             "Saīsini daļu līdz nesaīsināmai.",
             "Salīdzini divas daļas ar kopsaucēju.",
             "Saskaiti un atņem ar dažādiem saucējiem.",
             "Pārveido neīstu daļu par jauktu skaitli un atpakaļ.",
             "Pēc katra uzdevuma atzīmē, vai tas bija viegli.",
         ],
         pieze="Ja kāds no šiem soļiem vēl nav drošs, to var atkārtot pēc "
               "attiecīgās stundas kopsavilkuma - katrs no tiem ir mācīts "
               "atsevišķi 5.3. un 5.5. tematā."),

    Paraugs("Viens uzdevums no katra bloka",
            uzd="Saīsini {18|24}, salīdzini {2|3} un {3|4}, izrēķini "
                "2{1|2} + 1{1|3}.",
            soli=[
                ("{18|24} = {3|4}",
                 "Abus locekļus dala ar 6."),
                ("{2|3} = {8|12}, {3|4} = {9|12}",
                 "Kopsaucējs 12."),
                ("{2|3} < {3|4}",
                 "8 < 9."),
                ("2{1|2} + 1{1|3} = 3{5|6}",
                 "Kopsaucējs 6, veselie un daļas atsevišķi."),
            ],
            atbilde="{3|4}; {2|3} < {3|4}; 3{5|6}"),

    Ievadi("Pārbaudi sevi", [
        {"jaut": "Saīsini {18|24}. Atbildi raksti kā a/b.",
         "atb": ["3/4"], "padoms": "Abus dala ar 6."},
        {"jaut": "Saīsini {20|50}. Atbildi raksti kā a/b.",
         "atb": ["2/5"], "padoms": "Abus dala ar 10."},
        {"jaut": "Kura daļa ir lielāka - {2|3} vai {3|4}? Ieraksti kā a/b.",
         "atb": ["3/4"], "padoms": "Kopsaucējs 12."},
        {"jaut": "Cik ir {1|2} + {1|3}? Atbildi raksti kā a/b.",
         "atb": ["5/6"], "padoms": "{3|6} + {2|6}."},
        {"jaut": "Cik ir {3|4} - {1|6}? Atbildi raksti kā a/b.",
         "atb": ["7/12"], "padoms": "{9|12} - {2|12}."},
        {"jaut": "{11|4} kā jaukts skaitlis. Atbildi raksti kā a b/c.",
         "atb": ["2 3/4"], "padoms": "11 : 4."},
        {"jaut": "2{1|2} + 1{1|3} = ? Atbildi raksti kā a b/c.",
         "atb": ["3 5/6"], "padoms": "Kopsaucējs 6."},
        {"jaut": "3{1|4} - 1{3|4} = ? Atbildi raksti kā a b/c.",
         "atb": ["1 1/2", "1 2/4"], "padoms": "3{1|4} = 2{5|4}."},
    ], pamats=4,
        ievads="Pēc katra uzdevuma atzīmē sev, vai tas bija viegli."),

    Zimejums("Kopsaucējs joprojām ir atslēga",
             dala(12, 7, "7/12"),
             paskaidro="Gandrīz katrs daļu uzdevums sākas ar kopsaucēju - "
                       "gan salīdzinot, gan saskaitot, gan atņemot.",
             ievads="Viena prasme, kas noder visur."),

    Varianti("Kas vēl jāatkārto?", [
        {"jaut": "Ar ko sākas daļu saskaitīšana ar dažādiem saucējiem?",
         "opcijas": ["Ar kopsaucēja meklēšanu", "Ar saīsināšanu",
                     "Ar veselo atdalīšanu", "Ar novērtējumu"],
         "pareizi": 0,
         "padoms": "Vienādi gabali vispirms."},
        {"jaut": "Kā pārbauda, vai daļa ir nesaīsināma?",
         "opcijas": ["Meklē kopīgu dalītāju, lielāku par 1",
                     "Salīdzina skaitļu garumu",
                     "Dala ar 2",
                     "Pārbaudīt nevar"],
         "pareizi": 0,
         "padoms": "56. stunda."},
        {"jaut": "{11|4} kā jaukts skaitlis ir...",
         "opcijas": ["2{3|4}", "3{1|4}", "4{3|11}", "2{1|4}"],
         "pareizi": 0,
         "padoms": "11 : 4 = 2, atl. 3."},
        {"jaut": "Kad jāaizņemas veselais, atņemot jauktus skaitļus?",
         "opcijas": ["Kad mazināmā daļa ir mazāka", "Vienmēr", "Nekad",
                     "Kad saucēji ir vienādi"],
         "pareizi": 0,
         "padoms": "99. stunda."},
        {"jaut": "Cik ir {1|2} + {1|3}?",
         "opcijas": ["{5|6}", "{2|5}", "{1|6}", "{2|6}"],
         "pareizi": 0,
         "padoms": "{3|6} + {2|6}."},
        {"jaut": "Ko dara ar atbildi beigās?",
         "opcijas": ["Saīsina līdz nesaīsināmai", "Paplašina",
                     "Atstāj kā ir", "Noapaļo"],
         "pareizi": 0,
         "padoms": "Atbilde vienmēr nesaīsināma."},
    ], pamats=4),

    Pasaule("Klases kopsavilkums",
            Ievadi("", [
                {"jaut": "Klasē {1|4} skolēnu brauc ar autobusu, {1|3} nāk "
                         "kājām. Cik daļa kopā? Atbildi raksti kā a/b.",
                 "atb": ["7/12"], "padoms": "{3|12} + {4|12}."},
                {"jaut": "Cik daļa izmanto citu veidu? Atbildi raksti kā "
                         "a/b.",
                 "atb": ["5/12"], "padoms": "1 - {7|12}."},
                {"jaut": "Klasē 24 skolēni. Cik no tiem brauc ar autobusu?",
                 "atb": ["6"], "padoms": "24 : 4."},
                {"jaut": "Cik skolēnu nāk kājām?",
                 "atb": ["8"], "padoms": "24 : 3."},
            ]),
            pavediens="skola",
            konteksts="Pat vienkāršā klases aptaujā vienā uzdevumā satiekas "
                      "kopsaucējs, papildinājums līdz vienam un daļas "
                      "vērtība.",
            kapec="Tieši tāpēc šīs prasmes mācījām visu gadu."),

    Kopsavilkums([
        "Saīsinu un paplašinu daļas.",
        "Salīdzinu daļas ar kopsaucēju.",
        "Saskaitu un atņemu daļas ar dažādiem saucējiem.",
        "Pārveidoju jauktus skaitļus un neīstas daļas.",
    ]),

    Majas([
        "Atzīmē, kurš no četriem prasmju punktiem tev vēl nav drošs.",
        "Atkārto attiecīgās stundas kopsavilkumu.",
        "Izrēķini trīs uzdevumus par šo tematu.",
    ]),
]
