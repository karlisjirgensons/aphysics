# -*- coding: utf-8 -*-
"""6. klase, 52. stunda: «Kur liek komatu?»

Stunda par rakstu dalīšanu. Algoritms jau ir zināms; te tas jāpieraksta
stabiņā tā, lai komats nepazustu. Grūtākais gadījums - kad dalījums sākas ar
nulli un komatu - te tiek izspēlēts atsevišķi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kur liek komatu?"

MERKIS = ("Mācīsimies dalīt rakstos un skaidrot, kad rezultātā aiz "
          "veselajiem liek komatu.")

SATURS = [
    Sakums("Komatu liek brīdī, kad tiek pāri komatam",
           zimejums=restis([["1", "7", ",", "5", ":", "5"],
                            ["3", ",", "5", "", "", ""]]),
           paraksts="17,5 : 5 = 3,5. Komatu dalījumā liek tieši tad, kad "
                    "dalāmajā sākas desmitdaļas.",
           fakti=["Komatu neliek beigās - to liek darbības vidū.",
                  "Ja veselā daļa ir mazāka par dalītāju, dalījums sākas ar "
                  "nulli."]),

    Doma("Vispirms veselās, tad komats, tad pārējais",
         "Rakstu dalīšanā komatu dalījumā liek tajā brīdī, kad no dalāmā "
         "veselās daļas pāriet uz cipariem aiz komata.",
         soli=[
             "Izdali dalāmā veselo daļu ar dalītāju.",
             "Pieraksti veselo daļu dalījumā; ja tā ir mazāka par dalītāju, "
             "raksti 0.",
             "Liec komatu dalījumā.",
             "Turpini dalīt ciparus aiz komata, pierakstot nulles, ja vajag.",
             "Pārbaudi ar reizināšanu.",
         ],
         pieze="2,4 : 8: veselā daļa 2 ar 8 nedalās, tāpēc dalījums sākas ar "
               "«0,». Tas ir gaidāmi - rezultāts ir mazāks par vienu."),

    Paraugs("Kad dalījums sākas ar nulli",
            uzd="Cik ir 2,4 : 8?",
            soli=[
                ("2 : 8 = 0, atlikums 2",
                 "Veselā daļa ir mazāka par dalītāju."),
                ("Dalījums sākas ar «0,»",
                 "Liec nulli un komatu."),
                ("24 : 8 = 3",
                 "Atlikums 2 un cipars 4 dod 24."),
                ("2,4 : 8 = 0,3",
                 "Dalīšana beidzas."),
                ("Pārbaude: 0,3 · 8 = 2,4",
                 "Atgriežas dalāmais."),
            ],
            atbilde="0,3"),

    Ievadi("Dali rakstos", [
        {"jaut": "Cik ir 17,5 : 5?",
         "atb": ["3,5", "3.5"], "padoms": "175 : 5 = 35."},
        {"jaut": "Cik ir 2,4 : 8?",
         "atb": ["0,3", "0.3"], "padoms": "Dalījums sākas ar nulli."},
        {"jaut": "Cik ir 4,08 : 4?",
         "atb": ["1,02", "1.02"], "padoms": "408 : 4 = 102."},
        {"jaut": "Cik ir 0,72 : 6?",
         "atb": ["0,12", "0.12"], "padoms": "72 : 6 = 12."},
        {"jaut": "Cik ir 9,45 : 5?",
         "atb": ["1,89", "1.89"], "padoms": "945 : 5 = 189."},
        {"jaut": "Cik ir 1 : 8?",
         "atb": ["0,125", "0.125"], "padoms": "1,000 : 8."},
    ], pamats=4,
        ievads="Ja veselā daļa ir mazāka par dalītāju, sāc ar nulli."),

    Varianti("Kur ir komats?", [
        {"jaut": "Kad dalījums sākas ar «0,»?",
         "opcijas": ["Kad veselā daļa ir mazāka par dalītāju",
                     "Vienmēr", "Nekad",
                     "Kad dalītājs ir decimāldaļa"],
         "pareizi": 0,
         "padoms": "2 : 8 = 0 un atlikums."},
        {"jaut": "0,72 : 6 rezultāts ir...",
         "opcijas": ["0,12", "1,2", "12", "0,012"],
         "pareizi": 0,
         "padoms": "72 : 6 = 12; komats divas vietas."},
        {"jaut": "Skolēns ieguva 2,4 : 8 = 3. Kas nav labi?",
         "opcijas": ["Atbildei jābūt mazākai par 1",
                     "Jārēķina 24 : 8", "Nav kļūdas",
                     "Jābūt 0,03"],
         "pareizi": 0,
         "padoms": "Dalot ar 8, skaitlis sarūk astoņas reizes."},
        {"jaut": "Kāpēc 1 : 8 sanāk 0,125?",
         "opcijas": ["Jo dalāmajam pieraksta nulles",
                     "Jo 8 ir liels", "Jo komats ir vidū",
                     "Tā nav pareizi"],
         "pareizi": 0,
         "padoms": "1,000 : 8."},
    ], pamats=4),

    Pasaule("Cik ilgi katrs posms?",
            Ievadi("", [
                {"jaut": "Distance 4,8 km sadalīta 6 posmos. Cik km ir "
                         "viens posms?",
                 "atb": ["0,8", "0.8"], "padoms": "48 : 6 = 8."},
                {"jaut": "Skrējiens 7,5 km sadalīts 5 posmos. Cik km viens?",
                 "atb": ["1,5", "1.5"], "padoms": "75 : 5 = 15."},
                {"jaut": "Stafete 1,6 km, 4 dalībnieki. Cik km katram?",
                 "atb": ["0,4", "0.4"], "padoms": "16 : 4 = 4."},
                {"jaut": "Treniņš 2 h sadalīts 8 daļās. Cik h ir viena daļa?",
                 "atb": ["0,25", "0.25"], "padoms": "2,00 : 8."},
            ]),
            pavediens="sports",
            konteksts="Stafetē distanci dala vienādi, un rezultāts gandrīz "
                      "vienmēr ir decimāldaļa.",
            kapec="Komata vieta pasaka, vai posms ir 800 m vai 8 km."),

    Zimejums("Dalījums, kas sākas ar nulli",
             restis([["2", ",", "4", ":", "8"],
                     ["0", ",", "3", "", ""]]),
             paskaidro="Veselā daļa 2 ar 8 nedalās, tāpēc dalījums sākas ar "
                       "nulli un komatu.",
             ievads="Šis gadījums izskatās neparasts, bet tas ir biežākais."),

    Kopsavilkums([
        "Dalu decimāldaļas rakstos un ieliku komatu pareizajā vietā.",
        "Zinu, kad dalījums sākas ar nulli un komatu.",
        "Pierakstu nulles, ja dalīšana neapstājas.",
        "Pārbaudu rezultātu ar reizināšanu.",
    ]),

    Majas([
        "Izrēķini rakstos 3,6 : 9 un 5 : 8.",
        "Atrodi dalījumu, kurā rezultāts sākas ar «0,0».",
        "Paskaidro kādam mājās, kad dalījumā liek komatu.",
    ]),
]
