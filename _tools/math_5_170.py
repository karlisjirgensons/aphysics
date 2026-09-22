# -*- coding: utf-8 -*-
"""5. klase, 170. stunda: «Ko es protu ar decimāldaļām un procentiem?»

Otrā noslēguma stunda. Decimāldaļas un procenti 5. klasē parādījās pēdējie,
tāpēc tos atkārto atsevišķi. Divas prasmes te ir svarīgākās par visām
pārējām: salīdzināt skaitļus ar komatu un atrast procentus no skaitļa.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, kvadrats,
                         restis)

TEMA = "Ko es protu ar decimāldaļām un procentiem?"

MERKIS = ("Atkārtosim decimāldaļu salīdzināšanu un procentu aprēķināšanu no "
          "skaitļa.")

SATURS = [
    Sakums("Trīs valodas vienam skaitlim",
           zimejums=restis([["1/4", "0,25", "25 %"]],
                           virsraksts="Viens skaitlis, trīs pieraksti"),
           paraksts="Pāreja starp tiem ir visa 5.7. temata kodols.",
           fakti=["Daļa, decimāldaļa un procenti ir viens skaitlis.",
                  "Salīdzināt var tikai vienā valodā.",
                  "Rēķināt - tajā, kura ir ērtāka."]),

    Doma("Divas prasmes, kas noder visbiežāk",
         "No visa temata ikdienā visbiežāk vajag divas prasmes: salīdzināt "
         "decimāldaļas un aprēķināt procentus no skaitļa.",
         soli=[
             "Salīdzinot decimāldaļas, izlīdzini ciparu skaitu ar nullēm.",
             "Salīdzini pa šķirām no kreisās uz labo.",
             "Procentus rēķini caur vienu procentu vai caur daļu.",
             "Biežākos pārus zini no galvas: 25 %, 50 %, 75 %.",
             "Atbildi vienmēr pārbaudi ar novērtējumu.",
         ],
         pieze="0,45 nav lielāks par 0,5, un 25 % no 80 ir 20, nevis 25. "
               "Abas ir tās kļūdas, kas atkārtojas visbiežāk - tāpēc tieši "
               "tās te ir jāpārbauda."),

    Paraugs("Divi uzdevumi no temata",
            uzd="Salīdzini 0,45 un 0,5; aprēķini 25 % no 80.",
            soli=[
                ("0,5 = 0,50",
                 "Izlīdzina ciparu skaitu."),
                ("0,45 < 0,50",
                 "45 simtdaļas pret 50."),
                ("25 % = {1|4}",
                 "Biežāk lietotais pāris."),
                ("80 : 4 = 20",
                 "Procentu vērtība."),
            ],
            atbilde="0,45 < 0,5; 25 % no 80 ir 20"),

    Ievadi("Pārbaudi sevi", [
        {"jaut": "Kurš skaitlis ir lielāks - 0,45 vai 0,5? Ieraksti to.",
         "atb": ["0,5", "0,50"], "padoms": "0,50 pret 0,45."},
        {"jaut": "Kurš skaitlis ir lielāks - 0,8 vai 0,79? Ieraksti to.",
         "atb": ["0,8", "0,80"], "padoms": "0,80 pret 0,79."},
        {"jaut": "Cik ir 3,45 + 1,2? Ieraksti skaitli.",
         "atb": ["4,65"], "padoms": "1,2 = 1,20."},
        {"jaut": "Cik ir 5 - 2,35?",
         "atb": ["2,65"], "padoms": "5,00 - 2,35."},
        {"jaut": "Cik ir 25 % no 80?",
         "atb": ["20"], "padoms": "80 : 4."},
        {"jaut": "Cik ir 10 % no 250?",
         "atb": ["25"], "padoms": "250 : 10."},
        {"jaut": "20 % ir 16. Cik ir viss skaitlis?",
         "atb": ["80"], "padoms": "16 · 5."},
        {"jaut": "0,3 procentos. Ieraksti skaitli.",
         "atb": ["30"], "padoms": "0,30."},
    ], pamats=4,
        ievads="Pēc katra uzdevuma atzīmē, vai tas bija viegls."),

    Zimejums("Procents ir simtdaļa",
             kvadrats(10, 10, 5, 5, virsraksts="25 rūtiņas no 100",
                      paraksts="25 %"),
             paskaidro="Simta kvadrāts ir vienkāršākais veids, kā pārbaudīt "
                       "sevi: cik rūtiņu, tik procentu.",
             ievads="Viens attēls, kas izskaidro visu tematu."),

    Varianti("Kur bija biežākās kļūdas?", [
        {"jaut": "Kurš skaitlis ir lielāks - 0,45 vai 0,5?",
         "opcijas": ["0,5", "0,45", "Vienādi", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "0,50 pret 0,45."},
        {"jaut": "Cik ir 25 % no 80?",
         "opcijas": ["20", "25", "40", "2"],
         "pareizi": 0,
         "padoms": "80 : 4."},
        {"jaut": "0,3 procentos ir...",
         "opcijas": ["30 %", "3 %", "0,3 %", "300 %"],
         "pareizi": 0,
         "padoms": "0,30."},
        {"jaut": "Ko dara pirms decimāldaļu atņemšanas?",
         "opcijas": ["Izlīdzina ciparu skaitu ar nullēm", "Noapaļo",
                     "Saīsina", "Neko"],
         "pareizi": 0,
         "padoms": "139. stunda."},
        {"jaut": "20 % ir 16. Cik ir viss skaitlis?",
         "opcijas": ["80", "3,2", "36", "320"],
         "pareizi": 0,
         "padoms": "16 · 5."},
        {"jaut": "Kāds ir 50 % otrs nosaukums?",
         "opcijas": ["Puse", "Ceturtdaļa", "Trešdaļa", "Viss"],
         "pareizi": 0,
         "padoms": "{1|2}."},
    ], pamats=4),

    Pasaule("Čeks un atlaide",
            Ievadi("", [
                {"jaut": "Prece maksā 80 €, atlaide 25 %. Cik eiro ir "
                         "atlaide?",
                 "atb": ["20"], "padoms": "80 : 4."},
                {"jaut": "Cik eiro būs jāmaksā?",
                 "atb": ["60"], "padoms": "80 - 20."},
                {"jaut": "Pirkumi 3,45 € un 2,8 €. Cik eiro kopā?",
                 "atb": ["6,25"], "padoms": "3,45 + 2,80."},
                {"jaut": "Bija 10 €. Cik eiro palika?",
                 "atb": ["3,75"], "padoms": "10,00 - 6,25."},
            ]),
            pavediens="veikals",
            konteksts="Viens veikala apmeklējums izmanto visu, kas šajā "
                      "tematā mācīts.",
            kapec="Tieši tāpēc decimāldaļas un procenti mācīti kopā."),

    Kopsavilkums([
        "Salīdzinu decimāldaļas, izlīdzinot ciparu skaitu.",
        "Saskaitu un atņemu decimāldaļas kolonnā.",
        "Aprēķinu procentus no skaitļa.",
        "Atrodu veselo, ja zināma procentu vērtība.",
    ]),

    Majas([
        "Atzīmē, kurš prasmju punkts tev vēl nav drošs.",
        "Atkārto attiecīgās stundas kopsavilkumu.",
        "Atrodi čeku un pārbaudi vienu summu ar kolonnu.",
    ]),
]
