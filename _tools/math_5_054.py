# -*- coding: utf-8 -*-
"""5. klase, 54. stunda: «Kā daļu pierakstīt citādi bez modeļa?»

Mikrotemata noslēgums. Joslas un taisnes ir izdarījušas savu darbu - tagad
skolēns pats formulē, ko darīt bez zīmējuma. Tāpēc stundas galvenais
rezultāts nav atbildes, bet ieteikumu saraksts: ar ko reizināt, kā pārbaudīt
un kad tā vispār nevar izdarīt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā daļu pierakstīt citādi bez modeļa?"

MERKIS = ("Formulēsim ieteikumus, kā daļu pierakstīt ar citu saucēju, "
          "neizmantojot zīmējumu.")

SATURS = [
    Sakums("Zīmējums beidzas, kārtula paliek",
           zimejums=restis([["1/2", "2/4", "3/6", "4/8"],
                            ["1/3", "2/6", "3/9", "4/12"],
                            ["2/5", "4/10", "6/15", "8/20"]],
                           virsraksts="Katra rinda - viena un tā pati daļa"),
           paraksts="Neviena josla nav zīmēta - tikai reizināts.",
           fakti=["Ar saucēju 100 josla vairs nav zīmējama.",
                  "Bet reizināt var arī ar 50.",
                  "Tāpēc vajag kārtulu, nevis zīmuli."]),

    Doma("Vispirms noskaidro reizinātāju",
         "Lai daļu pierakstītu ar jaunu saucēju, atrodi, cik reižu jaunais "
         "saucējs ir lielāks par veco, un reizini ar to pašu skaitli arī "
         "skaitītāju.",
         soli=[
             "Pārbaudi, vai jaunais saucējs dalās ar veco.",
             "Izdali jauno saucēju ar veco - tas ir reizinātājs.",
             "Reizini skaitītāju ar šo reizinātāju.",
             "Pieraksti jauno daļu un liec vienādības zīmi.",
             "Pārbaudi: vai abi locekļi reizināti ar vienu skaitli.",
         ],
         pieze="Ja jaunais saucējs ar veco nedalās, tā pierakstīt nevar: "
               "{1|3} ar saucēju 8 neuzrakstīsi, jo 8 : 3 nav vesels "
               "skaitlis."),

    Paraugs("Pieraksti {3|4} ar saucēju 20",
            uzd="Uzraksti daļu {3|4} ar saucēju 20 un pārbaudi rezultātu.",
            soli=[
                ("20 : 4 = 5",
                 "Jaunais saucējs dalās ar veco - reizinātājs ir 5."),
                ("3 · 5 = 15",
                 "Ar to pašu skaitli reizina skaitītāju."),
                ("{3|4} = {15|20}",
                 "Jaunais pieraksts."),
                ("Pārbaude: 15 : 5 = 3 un 20 : 5 = 4",
                 "Abi locekļi dalās atpakaļ ar to pašu skaitli."),
            ],
            atbilde="{3|4} = {15|20}"),

    Ievadi("Bez zīmējuma", [
        {"jaut": "{1|4} pieraksti ar saucēju 16. Kāds ir skaitītājs?",
         "atb": ["4"], "padoms": "16 : 4 = 4; 1 · 4."},
        {"jaut": "{2|5} pieraksti ar saucēju 25. Kāds ir skaitītājs?",
         "atb": ["10"], "padoms": "25 : 5 = 5; 2 · 5."},
        {"jaut": "{3|8} pieraksti ar saucēju 24. Kāds ir skaitītājs?",
         "atb": ["9"], "padoms": "24 : 8 = 3; 3 · 3."},
        {"jaut": "{7|10} pieraksti ar saucēju 100. Kāds ir skaitītājs?",
         "atb": ["70"], "padoms": "100 : 10 = 10; 7 · 10."},
        {"jaut": "{1|2} pieraksti ar saucēju 100. Kāds ir skaitītājs?",
         "atb": ["50"], "padoms": "100 : 2 = 50."},
        {"jaut": "{5|6} pieraksti ar saucēju 36. Kāds ir skaitītājs?",
         "atb": ["30"], "padoms": "36 : 6 = 6; 5 · 6."},
        {"jaut": "{4|9} pieraksti ar saucēju 45. Kāds ir skaitītājs?",
         "atb": ["20"], "padoms": "45 : 9 = 5; 4 · 5."},
        {"jaut": "{2|3} pieraksti ar saucēju 300. Kāds ir skaitītājs?",
         "atb": ["200"], "padoms": "300 : 3 = 100; 2 · 100."},
    ], pamats=4,
        ievads="Divi soļi: cik reižu lielāks saucējs, tik reižu lielāks "
               "skaitītājs."),

    Zimejums("Trīs daļu saimes",
             restis([["1/2", "3/6", "5/10", "50/100"],
                     ["1/4", "2/8", "5/20", "25/100"],
                     ["3/5", "6/10", "9/15", "60/100"]],
                    virsraksts="Vienā rindā - viens un tas pats skaitlis"),
             paskaidro="Katrā rindā skaitļi aug, bet daļas vērtība ir viena. "
                       "Pēdējā ailē saucējs ir 100 - tādu joslu vairs "
                       "nezīmē.",
             ievads="Modelis te vairs nav vajadzīgs - pietiek ar reizinātāju."),

    Varianti("Pārbaudi ieteikumu", [
        {"jaut": "Ar ko jāreizina skaitītājs?",
         "opcijas": ["Ar to pašu, ar ko saucējs",
                     "Ar jauno saucēju",
                     "Ar veco saucēju",
                     "Ar skaitītāju pašu"],
         "pareizi": 0,
         "padoms": "Abiem locekļiem viens un tas pats reizinātājs."},
        {"jaut": "Vai {1|3} var pierakstīt ar saucēju 8?",
         "opcijas": ["Nevar, jo 8 nedalās ar 3", "Var, skaitītājs būs 2",
                     "Var, skaitītājs būs 3", "Var vienmēr"],
         "pareizi": 0,
         "padoms": "Reizinātājam jābūt veselam skaitlim."},
        {"jaut": "Kā pārbaudīt jauno pierakstu?",
         "opcijas": ["Izdalīt abus locekļus ar reizinātāju",
                     "Saskaitīt abus locekļus",
                     "Salīdzināt skaitītājus",
                     "Pārbaude nav vajadzīga"],
         "pareizi": 0,
         "padoms": "Jāatgriežas pie sākotnējās daļas."},
        {"jaut": "{2|7} pierakstīja kā {6|14}. Kur ir kļūda?",
         "opcijas": ["Skaitītājs reizināts ar 3, saucējs ar 2",
                     "Kļūdas nav",
                     "Saucējs reizināts ar 3",
                     "Skaitītājs reizināts ar 2"],
         "pareizi": 0,
         "padoms": "Reizinātājiem jāsakrīt."},
        {"jaut": "Kāpēc ar nulli reizināt nedrīkst?",
         "opcijas": ["Saucējs kļūtu 0", "Skaitītājs kļūtu 0",
                     "Iznāktu pārāk maza daļa", "Drīkst gan"],
         "pareizi": 0,
         "padoms": "Saucējs nekad nav nulle."},
        {"jaut": "Kurš solis ir pirmais?",
         "opcijas": ["Izdalīt jauno saucēju ar veco",
                     "Reizināt skaitītāju",
                     "Uzzīmēt joslu",
                     "Pierakstīt vienādību"],
         "pareizi": 0,
         "padoms": "Vispirms jāzina reizinātājs."},
    ], pamats=4),

    Pasaule("Recepte uz simtdaļām",
            Ievadi("", [
                {"jaut": "Uz iepakojuma rakstīts {1|4} kilograma. Cik tas ir "
                         "simtdaļu? Atbildi raksti kā skaitītāju.",
                 "atb": ["25"], "padoms": "100 : 4 = 25."},
                {"jaut": "Receptē ir {3|5} litra sulas. Cik tas ir "
                         "desmitdaļu? Atbildi raksti kā skaitītāju.",
                 "atb": ["6"], "padoms": "10 : 5 = 2; 3 · 2."},
                {"jaut": "Receptē ir {1|2} litra ūdens. Cik tas ir "
                         "simtdaļu?",
                 "atb": ["50"], "padoms": "100 : 2 = 50."},
                {"jaut": "Receptē ir {4|5} kilograma miltu. Cik tas ir "
                         "simtdaļu?",
                 "atb": ["80"], "padoms": "100 : 5 = 20; 4 · 20."},
            ]),
            pavediens="virtuve",
            konteksts="Uz iepakojumiem daļas raksta ar saucēju 10 vai 100, "
                      "bet receptē tās ir ceturtdaļas un piektdaļas.",
            kapec="Pārrakstīt no vienas valodas otrā var bez jebkāda "
                  "zīmējuma."),

    Kopsavilkums([
        "Atrodu reizinātāju, dalot jauno saucēju ar veco.",
        "Pierakstu daļu ar jaunu saucēju, nelietojot modeli.",
        "Pārbaudu rezultātu, dalot abus locekļus atpakaļ.",
        "Zinu, kad tā pierakstīt nevar: ja saucēji nedalās.",
    ]),

    Majas([
        "Uzraksti savus trīs ieteikumus, kā daļu pierakstīt ar citu saucēju.",
        "Pieraksti {3|4}, {2|5} un {1|8} ar saucēju 40.",
        "Atrodi daļu, ko ar saucēju 100 pierakstīt nevar, un paskaidro, "
        "kāpēc.",
    ]),
]
