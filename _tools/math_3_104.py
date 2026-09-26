# -*- coding: utf-8 -*-
"""3. klase, 104. stunda: «Kur dzīvē noder daļas?»

Temata pēdējā mācību stunda pirms pārbaudes darba. Visas prasmes - daļas
pieraksts, salīdzināšana, decimāldaļas un daļa no skaita - te sastopas
sadzīves uzdevumos, kur skolēnam pašam jāizvēlas, kuru no tām lietot.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kur dzīvē noder daļas?"

MERKIS = ("Risināsim sadzīves uzdevumus, kuros jānosaka daļa no lieluma vai "
          "skaita.")

SATURS = [
    Sakums("Cik reizes dienā tu satiec daļas?",
           zimejums=restis([["kur", "daļa"],
                            ["pulkstenis", "pusstunda"],
                            ["veikals", "0,99 eiro"],
                            ["recepte", "1/2 glāzes"],
                            ["sports", "3/4 distances"]],
                           "daļas ap mums"),
           paraksts="Daļas nav tikai burtnīcā - tās ir visur.",
           fakti=["Pulkstenis, nauda, receptes un sports - visur ir daļas.",
                  "Daļa vienmēr atbild uz jautājumu «cik no visa»."]),

    Doma("Vispirms atrodi veselo",
         "Katrā uzdevumā vispirms noskaidro, kas ir veselais, un tikai tad "
         "rēķini daļu.",
         soli=[
             "Izlasi uzdevumu un atrodi veselo.",
             "Nosaki, kāda daļa tiek prasīta.",
             "Izdali veselo ar saucēju.",
             "Reizini ar skaitītāju un pieraksti atbildi ar vārdu.",
         ],
         pieze="Ja uzdevumā ir divi dažādi veselie, tos nedrīkst salīdzināt "
               "tieši - vispirms jāizrēķina skaitļi."),

    Paraugs("Cik maksā prece ar atlaidi?",
            uzd="Prece maksā 60 ct. Atlaide ir {1|4} no cenas. Cik jāmaksā?",
            soli=[
                ("60 : 4 = 15",
                 "Atlaide ir 15 centi."),
                ("60 − 15 = 45",
                 "Cena pēc atlaides."),
                ("45 ct",
                 "Pārbaude: 45 ir {3|4} no 60."),
            ],
            atbilde="45 ct"),

    Ievadi("Daļas dzīvē", [
        {"jaut": "Prece maksā 60 ct, atlaide {1|4}. Cik centu ir atlaide?",
         "atb": ["15"], "padoms": "60 : 4."},
        {"jaut": "Cik centu jāmaksā pēc atlaides?", "atb": ["45"],
         "padoms": "60 − 15."},
        {"jaut": "Receptei vajag {1|2} no 400 g miltu. Cik gramu?",
         "atb": ["200"], "padoms": "400 : 2."},
        {"jaut": "Distance 600 m, noskrieti {2|3}. Cik metru?",
         "atb": ["400"], "padoms": "600 : 3 = 200; 2 · 200."},
        {"jaut": "Filma ilgst 90 min, noskatīta {1|3}. Cik minūšu?",
         "atb": ["30"], "padoms": "90 : 3."},
        {"jaut": "Klasē 24 skolēni, {3|4} ir sporta pulciņā. Cik skolēnu?",
         "atb": ["18"], "padoms": "24 : 4 = 6; 3 · 6."},
    ], pamats=4),

    Zimejums("Kur daļas parādās",
             restis([["situācija", "veselais", "daļa"],
                     ["atlaide", "cena", "1/4"],
                     ["recepte", "miltu daudzums", "1/2"],
                     ["distance", "visi metri", "2/3"]],
                    "trīs uzdevumi, viena shēma"),
             paskaidro="Katrā uzdevumā vispirms meklē veselo - pārējais ir "
                       "tas pats rēķins.",
             ievads="Trīs dažādas situācijas, viens paņēmiens."),

    Varianti("Kurš rēķins der?", [
        {"jaut": "Prece 80 ct, atlaide {1|4}. Cik centu ir atlaide?",
         "opcijas": ["20", "4", "60", "76"],
         "pareizi": 0, "padoms": "80 : 4."},
        {"jaut": "Cik ir {3|5} no 100?",
         "opcijas": ["60", "20", "35", "40"],
         "pareizi": 0, "padoms": "100 : 5 = 20; 3 · 20."},
        {"jaut": "Ko meklē vispirms?",
         "opcijas": ["Veselo", "Atbildi", "Saucēju", "Mērvienību"],
         "pareizi": 0, "padoms": "Bez veselā daļu izrēķināt nevar."},
        {"jaut": "Prece 0,80 eiro. Cik centu tas ir?",
         "opcijas": ["80", "8", "800", "0,8"],
         "pareizi": 0, "padoms": "Aiz komata ir centi."},
    ], pamats=4),

    Pasaule("Cik izdevīgāka ir akcija?",
            Ievadi("", [
                {"jaut": "Prece maksā 120 ct. Atlaide {1|3}. Cik centu ir "
                         "atlaide?",
                 "atb": ["40"], "padoms": "120 : 3."},
                {"jaut": "Cik centu jāmaksā?", "atb": ["80"],
                 "padoms": "120 − 40."},
                {"jaut": "Otra prece maksā 90 ct, atlaide {1|2}. Cik centu "
                         "jāmaksā?",
                 "atb": ["45"], "padoms": "90 : 2."},
                {"jaut": "Cik centu maksās abas preces ar atlaidēm?",
                 "atb": ["125"], "padoms": "80 + 45."},
            ]),
            pavediens="veikals",
            konteksts="Akcijās atlaidi raksta kā daļu no cenas - un divas "
                      "atlaides var salīdzināt tikai centos.",
            kapec="{1|2} no mazas cenas var būt mazāk nekā {1|3} no lielas."),

    Kopsavilkums([
        "Risinu sadzīves uzdevumus ar daļām.",
        "Vispirms atrodu veselo, tad rēķinu daļu.",
        "Pārvēršu daļas un decimāldaļas.",
        "Pārbaudu, vai atbilde ir saprātīga.",
    ]),

    Majas([
        "Atrodi veikalā akciju un izrēķini, cik liela ir atlaide centos.",
        "Izrēķini, cik ir {3|4} no tavas nedēļas kabatas naudas.",
        "Pārlasi tematu un atzīmē, kas vēl jāatkārto pirms pārbaudes darba.",
    ], ievads="Šī ir pēdējā stunda pirms pārbaudes darba."),
]
