# -*- coding: utf-8 -*-
"""7. klase, 17. stunda: «Vai loterijā ir izdevīgi spēlēt?»

Loteriju var izvērtēt ar matemātiku: cik biļešu, cik laimestu, cik vidēji
atgūst no katra iztērētā eiro. Stunda aprēķina laimesta varbūtību un
vidējo laimestu uz biļeti un secina, kāpēc loterija vienmēr pelna.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Simulacija, Varianti, Zimejums,
                         restis)

TEMA = "Vai loterijā ir izdevīgi spēlēt?"

MERKIS = ("Izvērtēsim loteriju: aprēķināsim laimesta varbūtību un to, cik "
          "vidēji atgūst no vienas biļetes.")

SATURS = [
    Sakums("1000 biļešu, katra 2 €. Kurš vienmēr laimē?",
           fakti=["Loterija pārdod biļetes par 2000 €.",
                  "Laimestos izmaksā, piemēram, 1000 €.",
                  "Pārējais paliek rīkotājam - viņš laimē vienmēr."]),

    Doma("Vidējais laimests uz biļeti",
         "Ja visu laimestu summu izdala ar biļešu skaitu, iegūst vidējo "
         "laimestu uz vienu biļeti. Ja tas ir mazāks par biļetes cenu, "
         "spēlētāji kopumā zaudē.",
         soli=[
             "Saskaiti laimējošās biļetes un aprēķini P(laimēt).",
             "Aprēķini visu laimestu summu.",
             "Izdali to ar biļešu skaitu - vidējais laimests.",
             "Salīdzini ar biļetes cenu.",
         ],
         pieze="Viens var laimēt daudz, bet vidēji katrs spēlētājs zaudē "
               "starpību. Tāpēc loterija ir izklaide, nevis ienākumi."),

    Zimejums("Loterijas laimesti",
             restis([["laimests", "biļešu skaits", "summa"],
                     ["500 €", "1", "500 €"],
                     ["50 €", "6", "300 €"],
                     ["5 €", "40", "200 €"],
                     ["kopā", "47", "1000 €"]]),
             paskaidro="1000 biļešu, katra 2 €."),

    Paraugs("Izvērtē loteriju",
            uzd="Izmanto tabulu. Kāda ir varbūtība laimēt kaut ko? Cik vidēji "
                "atgūst no vienas biļetes?",
            soli=[
                ("P(laimēt) = {47|1000} = 0,047 = 4,7 %",
                 "47 laimējošas no 1000."),
                ("Vidējais laimests: 1000 € : 1000 = 1 €",
                 "Visi laimesti, dalīti ar biļetēm."),
                ("Biļete maksā 2 €, vidēji atgūst 1 €",
                 "Salīdzina."),
                ("Vidēji zaudē 1 € no katras biļetes",
                 "Izdevīgi rīkotājam."),
            ],
            atbilde="P = 4,7 %; vidēji atgūst 1 € no 2 €"),

    Simulacija("Pērc biļetes", ["zaudē", "5 €", "50 €", "500 €"],
               [1, 2, 3], "laimē kaut ko", teorija="{47|1000} = 0,047",
               svari=[953, 40, 6, 1],
               ievads="Katrs metiens ir viena nopirkta biļete no tās pašas "
                       "loterijas."),

    Ievadi("Aprēķini", [
        {"jaut": "Loterijā 500 biļešu, laimē 25. P(laimēt) procentos "
                 "(tikai skaitli)?",
         "atb": ["5"], "padoms": "25 : 500."},
        {"jaut": "Laimesti kopā 600 €, biļešu 400. Vidējais laimests "
                 "(€)?",
         "atb": ["1,5"], "padoms": "600 : 400."},
        {"jaut": "Biļete 3 €, vidējais laimests 1,5 €. Cik € vidēji "
                 "zaudē ar vienu biļeti?",
         "atb": ["1,5"], "padoms": "3 − 1,5."},
        {"jaut": "Pērk 10 biļetes pa 3 €, vidējais laimests 1,5 €. Cik € "
                 "vidēji zaudē?",
         "atb": ["15"], "padoms": "10 · 1,5."},
    ]),

    Varianti("Spried", [
        {"jaut": "Ja nopērk visas 1000 biļetes par 2 €, ko iegūst?",
         "opcijas": ["Visus laimestus - 1000 €, zaudē 1000 €",
                     "Garantētu peļņu", "Tikai galveno balvu",
                     "Neko"],
         "pareizi": 0,
         "padoms": "Iztērē 2000 €, laimē 1000 €."},
        {"jaut": "Draugs saka: «Es jau 5 reizes nelaimēju, tagad noteikti "
                 "laimēšu.» Vai viņam ir taisnība?",
         "opcijas": ["Nē - katra biļete ir neatkarīga",
                     "Jā - varbūtība pieaug",
                     "Jā, pēc 5 reizēm P = 1",
                     "Nē - tagad P = 0"],
         "pareizi": 0,
         "padoms": "Loterija neatceras iepriekšējās biļetes."},
    ]),

    Pasaule("Skolas labdarības loterija",
            Ievadi("", [
                {"jaut": "Skola pārdod 300 biļetes pa 1 €. Balvas kopā "
                         "vērtas 90 €. Cik € paliek labdarībai?",
                 "atb": ["210"], "padoms": "300 − 90."},
                {"jaut": "Balvu ir 15. P(laimēt) procentos (tikai "
                         "skaitli)?",
                 "atb": ["5"], "padoms": "15 : 300."},
                {"jaut": "Vidējā balvas vērtība uz biļeti (€)?",
                 "atb": ["0,3"], "padoms": "90 : 300."},
            ]),
            pavediens="speles",
            konteksts="Labdarības loterijā zaudējums ir ziedojums - un to "
                      "var aprēķināt iepriekš.",
            kapec="Matemātika parāda, kur nonāk nauda."),

    Kopsavilkums([
        "Aprēķinu laimesta varbūtību loterijā.",
        "Aprēķinu vidējo laimestu uz vienu biļeti.",
        "Salīdzinu to ar biļetes cenu un izdaru secinājumu.",
        "Zinu, ka iepriekšējie zaudējumi neietekmē nākamo biļeti.",
    ]),

    Majas([
        "Atrodi kādas loterijas noteikumus un aprēķini P(laimēt).",
        "Izdomā loteriju, kas būtu godīga: vidējais laimests = cena.",
        "Paskaidro, kāpēc rīkotājs tādu nerīkotu.",
    ]),
]
