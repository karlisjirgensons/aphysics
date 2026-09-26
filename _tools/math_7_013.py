# -*- coding: utf-8 -*-
"""7. klase, 13. stunda: «Ko nozīmē «liela varbūtība»?»

Varbūtība ikdienā skan laika prognozē, sporta ziņās un reklāmā. Stunda
sakārto vārdus «neiespējami», «maz ticami», «droši» uz skalas no 0 līdz 1
un parāda, ka 70 % lietus nozīmē, nevis «līs 70 % dienas».
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Sakums, Varianti, Zimejums, taisne)

TEMA = "Ko nozīmē «liela varbūtība»?"

MERKIS = ("Iemācīsimies novērtēt notikuma varbūtību uz skalas no 0 līdz 1 "
          "un saprast, ko tā nozīmē ziņās.")

SATURS = [
    Sakums("Lietus varbūtība 70 %. Ņemt lietussargu?",
           zimejums=taisne(0, 1, 0.5, [(0, "0"), (0.7, "0,7"), (1, "1")],
                           sikas=5),
           paraksts="No 10 šādām dienām apmēram 7 ir lietainas.",
           fakti=["70 % nenozīmē, ka lietus līs 70 % dienas.",
                  "Tas nozīmē: šādos laikapstākļos līst 7 dienās no 10.",
                  "Varbūtība ir skaitlis no 0 līdz 1 jeb no 0 % līdz 100 %."]),

    Doma("Varbūtība ir skaitlis no 0 līdz 1",
         "Notikuma varbūtība parāda, cik ticams ir notikums: 0 - "
         "neiespējams, 1 - drošs, un visi pārējie ir starp tiem.",
         soli=[
             "0 - notikums nenotiks nekad (neiespējams).",
             "Tuvu 0 - maz ticams.",
             "{1|2} = 0,5 - notikums ir tikpat ticams, cik neticams.",
             "Tuvu 1 - ļoti ticams.",
             "1 - notikums notiks noteikti (drošs).",
         ],
         pieze="Varbūtību raksta kā daļu, decimāldaļu vai procentos: "
               "{1|4} = 0,25 = 25 %."),

    Varianti("Novieto uz skalas", [
        {"jaut": "Rīt saule uzlēks austrumos.",
         "opcijas": ["1 - drošs", "0,5", "tuvu 0", "0 - neiespējams"],
         "pareizi": 0, "jaukt": False,
         "padoms": "Tas notiek vienmēr."},
        {"jaut": "Metot kauliņu, uzkritīs 7.",
         "opcijas": ["1 - drošs", "0,5", "tuvu 0", "0 - neiespējams"],
         "pareizi": 3, "jaukt": False,
         "padoms": "Uz kauliņa nav 7."},
        {"jaut": "Metot monētu, uzkritīs ģerbonis.",
         "opcijas": ["1 - drošs", "0,5", "tuvu 0", "0 - neiespējams"],
         "pareizi": 1, "jaukt": False,
         "padoms": "Divi vienādi iespējami iznākumi."},
        {"jaut": "Tu laimēsi loterijas galveno balvu.",
         "opcijas": ["1 - drošs", "0,5", "tuvu 0", "0 - neiespējams"],
         "pareizi": 2, "jaukt": False,
         "padoms": "Iespējams, bet ļoti maz ticams."},
    ], pamats=4),

    Varianti("Ko nozīmē ziņa?", [
        {"jaut": "«Operācija ir veiksmīga 95 % gadījumu.» Kas ir patiess?",
         "opcijas": ["No 100 operācijām apmēram 95 izdodas",
                     "Katra operācija izdodas par 95 %",
                     "95 pacienti izveseļojas pilnīgi",
                     "5 % operāciju nemaz nenotiek"],
         "pareizi": 0,
         "padoms": "Varbūtība runā par daudziem gadījumiem."},
        {"jaut": "Kura varbūtība ir lielākā?",
         "opcijas": ["{4|5}", "0,75", "70 %", "{2|3}"],
         "pareizi": 0,
         "padoms": "{4|5} = 0,8; {2|3} ≈ 0,67."},
        {"jaut": "Kura varbūtība nav iespējama?",
         "opcijas": ["1,2", "0", "{1|3}", "99 %"],
         "pareizi": 0,
         "padoms": "Varbūtība nav lielāka par 1."},
    ]),

    Ievadi("Pārveido", [
        {"jaut": "Pieraksti {3|4} procentos (tikai skaitli).",
         "atb": ["75"], "padoms": "3 : 4 = 0,75."},
        {"jaut": "Pieraksti 40 % decimāldaļā.",
         "atb": ["0,4"], "padoms": "40 : 100."},
        {"jaut": "Pieraksti {1|5} decimāldaļā.",
         "atb": ["0,2"], "padoms": "1 : 5."},
        {"jaut": "Pieraksti 0,05 procentos (tikai skaitli).",
         "atb": ["5"], "padoms": "0,05 · 100."},
    ]),

    Pasaule("Laika prognoze",
            Ievadi("", [
                {"jaut": "Lietus varbūtība 30 %. Apmēram cik no 20 "
                         "šādām dienām ir lietainas?",
                 "atb": ["6"], "padoms": "30 % no 20."},
                {"jaut": "Kāda ir varbūtība, ka nelīs? Atbildi procentos "
                         "(tikai skaitli).",
                 "atb": ["70"], "padoms": "100 − 30."},
                {"jaut": "Futbolā prognozē: mājinieki uzvar 45 %, "
                         "neizšķirts 25 %. Cik % viesi uzvar?",
                 "atb": ["30"], "padoms": "Kopā 100 %."},
            ]),
            pavediens="planeta",
            konteksts="Sinoptiķi aprēķina varbūtību no tūkstošiem līdzīgu "
                      "dienu datu.",
            kapec="Varbūtība palīdz izlemt, pat ja nākotni nezinām."),

    Zimejums("Varbūtības skala",
             taisne(0, 1, 0.25, [(0, "0"), (0.5, "0,5"), (1, "1")],
                    sikas=5),
             paskaidro="Jo tuvāk labajam galam, jo ticamāks notikums."),

    Kopsavilkums([
        "Zinu, ka varbūtība ir skaitlis no 0 līdz 1.",
        "Novietoju notikumus uz varbūtības skalas.",
        "Pārveidoju varbūtību daļā, decimāldaļā un procentos.",
        "Skaidroju, ko nozīmē varbūtība ziņās.",
    ]),

    Majas([
        "Atrodi ziņās vai reklāmā varbūtību un paskaidro to.",
        "Uzraksti 5 notikumus un sakārto tos no maz ticamā līdz drošam.",
        "Pieraksti rītdienas lietus varbūtību un pārbaudi, vai lija.",
    ]),
]
