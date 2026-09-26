# -*- coding: utf-8 -*-
"""4. klase, 10. stunda: «Kur skaitlis stāv uz skaitļu taisnes?»

3. stundā taisne sniedzās līdz 1000; tagad - līdz 10 000. Solis 1000 vai
500, un skaitļi starp iedaļām. Tas pats prasmju pāris vajadzīgs laika
asij vēsturē un diagrammu mērogam.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas,
                         Paraugs, Pasaule, Sakums, Varianti, Zimejums,
                         laika_ass, taisne)

TEMA = "Kur skaitlis stāv uz skaitļu taisnes?"

MERKIS = ("Izveidosim skaitļu taisni ar izvēlētu vienību un atliksim uz tās "
          "četrciparu skaitļus.")

SATURS = [
    Sakums("Kad cilvēki sāka rakstīt?",
           zimejums=laika_ass([(1201, "Rīga"), (1918, "Latvija"),
                               (2026, "šodien")], 1000, 2100, 100),
           paraksts="Laika ass ir skaitļu taisne ar soli 100 gadi.",
           fakti=["Vecākie raksti ir apmēram 5000 gadu veci.",
                  "Laika asī katrs gads ir punkts uz taisnes."]),

    Doma("Taisnes solis jāizvēlas pēc lielākā skaitļa",
         "Līdz 10 000 ērts solis ir 1000; ja vajag precīzāk, taisni "
         "sadala sīkāk.",
         soli=[
             "Nosaki lielāko skaitli, kas jāatliek.",
             "Izvēlies soli: 1000, 500 vai 100.",
             "Atrodi divas iedaļas, starp kurām skaitlis stāv.",
             "Novērtē, vai tas tuvāk kreisajai vai labajai iedaļai.",
         ],
         pieze="7500 ar soli 1000 ir tieši pusē starp 7000 un 8000."),

    Paraugs("Kur ir 3200?",
            uzd="Taisnes solis ir 1000. Kur atlikt 3200?",
            soli=[
                ("3000 < 3200 < 4000",
                 "Starp trešo un ceturto iedaļu."),
                ("3200 − 3000 = 200",
                 "200 no 1000 ir maza daļa."),
                ("tuvu 3000", "Punkts ir daudz tuvāk kreisajai iedaļai."),
            ],
            atbilde="nedaudz pa labi no 3000"),

    Kustiba("Aizved līdz skaitlim", [
        {"jaut": "Solis ir 1000. Aizved kuģi līdz 6000.",
         "atb": 6000, "beigas": 10000, "iedala": 1000,
         "merkis": "6000", "objekts": "Kuģis",
         "padoms": "Sestā iedaļa.",
         "stasts": "Kuģis peld pa skaitļu taisni."},
        {"jaut": "Kurš skaitlis ir pusē starp 4000 un 5000?",
         "atb": 4500, "beigas": 10000, "iedala": 1000,
         "merkis": "pusē", "objekts": "Kuģis",
         "padoms": "4000 + 500."},
        {"jaut": "Solis 500. Kur ir septītā iedaļa?",
         "atb": 3500, "beigas": 5000, "iedala": 500,
         "merkis": "7. iedaļa", "objekts": "Kuģis",
         "padoms": "7 · 500."},
        {"jaut": "Kurš skaitlis ir par 1000 mazāks nekā 10 000?",
         "atb": 9000, "beigas": 10000, "iedala": 1000,
         "merkis": "?", "objekts": "Kuģis",
         "padoms": "10 000 − 1000."},
    ], pamats=2,
        ievads="Ieraksti skaitli un spied «Palaist»."),

    Zimejums("Taisne līdz 10 000",
             taisne(0, 10000, 1000, [(2500, "2500"), (7800, "7800")]),
             paskaidro="2500 ir pusē starp 2000 un 3000; 7800 - tuvāk "
                       "8000.",
             ievads="Solis 1000 - desmit iedaļas."),

    Ievadi("Nolasi no taisnes", [
        {"jaut": "Solis 1000. Punkts ir pusē starp 8000 un 9000.",
         "atb": ["8500"], "padoms": "8000 + 500."},
        {"jaut": "Solis 100. Punkts ir 3 iedaļas pēc 4700.",
         "atb": ["5000"], "padoms": "4700 + 300."},
        {"jaut": "Solis 500. Punkts ir 2 iedaļas pirms 3000.",
         "atb": ["2000"], "padoms": "3000 − 1000."},
        {"jaut": "Cik iedaļu ar soli 500 ir no 0 līdz 10 000?",
         "atb": ["20"], "padoms": "Katrā tūkstotī divas."},
    ]),

    Varianti("Kurš tuvāk?", [
        {"jaut": "Vai 6300 ir tuvāk 6000 vai 7000?",
         "opcijas": ["6000", "7000", "vienādi"], "pareizi": 0,
         "padoms": "Puse ir 6500."},
        {"jaut": "Vai 4500 ir tuvāk 4000 vai 5000?",
         "opcijas": ["vienādi", "4000", "5000"], "pareizi": 0,
         "padoms": "Tieši pusē."},
        {"jaut": "Starp kurām iedaļām ar soli 1000 ir 9090?",
         "opcijas": ["9000 un 10 000", "8000 un 9000", "900 un 1000",
                     "9090 un 9100"], "pareizi": 0,
         "padoms": "9 tūkstoši un vēl mazliet."},
        {"jaut": "Kāds solis taisnei, kur ir 1200, 1400, 1600?",
         "opcijas": ["200", "100", "1000", "400"], "pareizi": 0,
         "padoms": "Par cik aug katrs nākamais?"},
    ], pamats=4),

    Pasaule("Cik augstu lido?",
            Ievadi("", [
                {"jaut": "Lidmašīna lido 10 000 m augstumā, putns - 1000 m. "
                         "Cik reižu augstāk lido lidmašīna?",
                 "atb": ["10"], "padoms": "Cik tūkstošu ir 10 000?"},
                {"jaut": "Mākoņi ir 2000 m augstumā. Par cik metriem "
                         "lidmašīna ir augstāk?",
                 "atb": ["8000"], "padoms": "10 000 − 2000."},
                {"jaut": "Lidmašīna nolaižas līdz pusei no 10 000 m. Cik "
                         "augstu tā ir?",
                 "atb": ["5000"], "padoms": "Puse no 10 000."},
                {"jaut": "Tad tā nolaižas vēl par 1500 m. Kādā augstumā?",
                 "atb": ["3500"], "padoms": "5000 − 1500."},
            ]),
            pavediens="tehnika",
            konteksts="Pilota ekrānā augstums ir skaitļu taisne, kas iet "
                      "uz augšu.",
            kapec="Kas nolasa taisni, tas uzreiz redz, cik vēl līdz "
                  "mērķim."),

    Kopsavilkums([
        "Izvēlos skaitļu taisnes soli līdz 10 000.",
        "Atlieku četrciparu skaitli starp iedaļām.",
        "Nosaku, kurai iedaļai skaitlis ir tuvāk.",
    ]),

    Majas([
        "Uzzīmē laika asi no 1900 līdz 2100 ar soli 20 un atzīmē savas "
        "ģimenes dzimšanas gadus.",
        "Atrodi kartē attālumu līdz Parīzei vai Romai un atliec uz taisnes ar "
        "soli 1000 km.",
        "Izdomā skaitli, kas ir tuvu 5000, bet mazāks par to.",
    ]),
]
