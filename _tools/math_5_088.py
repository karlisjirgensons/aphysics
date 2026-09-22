# -*- coding: utf-8 -*-
"""5. klase, 88. stunda: «Kā daļa raksturo iespējamību?»

Iepriekšējā stunda skaitīja to, kas jau noticis; šī paredz to, kas notiks.
Abas reizes atbilde ir daļa, bet saucējs nāk no dažādām vietām: biežumā tas
ir mēģinājumu skaits, iespējamībā - visu iznākumu skaits. Tieši šo atšķirību
stunda arī tur uzmanības centrā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala, taisne)

TEMA = "Kā daļa raksturo iespējamību?"

MERKIS = ("Mācīsimies skaitliski raksturot notikuma iespējamību ar daļu un "
          "formulēt secinājumu.")

SATURS = [
    Sakums("Seši skaitļi uz kauliņa",
           zimejums=dala(6, 1, "1/6"),
           paraksts="Katram skaitlim ir viena iespēja no sešām.",
           fakti=["Spēļu kauliņam ir 6 vienādi iespējami iznākumi.",
                  "Sešnieks ir viens no tiem.",
                  "Tātad tā iespējamība ir {1|6}."]),

    Doma("Labvēlīgie pret visiem",
         "Notikuma iespējamību izsaka kā daļu: labvēlīgo iznākumu skaits pār "
         "visu vienādi iespējamo iznākumu skaitu.",
         soli=[
             "Saskaiti visus vienādi iespējamos iznākumus - tas ir saucējs.",
             "Saskaiti, cik no tiem der notikumam - tas ir skaitītājs.",
             "Uzraksti daļu un saīsini to.",
             "Salīdzini ar 0, {1|2} un 1.",
             "Formulē secinājumu vārdiem.",
         ],
         pieze="Iespējamība nekad nav mazāka par 0 vai lielāka par 1. Ja "
               "notikums nevar notikt, tā ir 0; ja notiek noteikti - 1. "
               "Viss pārējais atrodas starp tiem."),

    Paraugs("Kāda ir iespējamība uzmest pāra skaitli?",
            uzd="Met spēļu kauliņu. Kāda ir iespējamība, ka uzkritīs pāra "
                "skaitlis?",
            soli=[
                ("Visi iznākumi: 1, 2, 3, 4, 5, 6",
                 "Saucējs ir 6."),
                ("Labvēlīgie: 2, 4, 6",
                 "Skaitītājs ir 3."),
                ("{3|6} = {1|2}",
                 "Saīsina abus locekļus."),
                ("Iespējamība ir {1|2}",
                 "Tieši puse - tikpat, cik nepāra skaitlim."),
            ],
            atbilde="Iespējamība ir {1|2}"),

    Ievadi("Aprēķini iespējamību", [
        {"jaut": "Kauliņš. Kāda iespējamība uzmest sešnieku? Atbildi raksti "
                 "kā a/b.",
         "atb": ["1/6"], "padoms": "Viens iznākums no sešiem."},
        {"jaut": "Kauliņš. Kāda iespējamība uzmest pāra skaitli? Atbildi "
                 "raksti kā a/b.",
         "atb": ["1/2", "3/6"], "padoms": "2, 4 un 6."},
        {"jaut": "Kauliņš. Kāda iespējamība uzmest skaitli, lielāku par 4? "
                 "Atbildi raksti kā a/b.",
         "atb": ["1/3", "2/6"], "padoms": "5 un 6."},
        {"jaut": "Monēta. Kāda iespējamība uzmest ģerboni? Atbildi raksti kā "
                 "a/b.",
         "atb": ["1/2"], "padoms": "Viens no diviem."},
        {"jaut": "Maisā 10 bumbiņas, 3 sarkanas. Kāda iespējamība izvilkt "
                 "sarkanu? Atbildi raksti kā a/b.",
         "atb": ["3/10"], "padoms": "{3|10}."},
        {"jaut": "Maisā 12 bumbiņas, 4 zilas. Kāda iespējamība izvilkt zilu? "
                 "Atbildi raksti kā a/b.",
         "atb": ["1/3", "4/12"], "padoms": "Abus dala ar 4."},
        {"jaut": "Kauliņš. Kāda iespējamība uzmest skaitli, mazāku par 7? "
                 "Ieraksti skaitli.",
         "atb": ["1"], "padoms": "Visi seši der."},
        {"jaut": "Kauliņš. Kāda iespējamība uzmest 7? Ieraksti skaitli.",
         "atb": ["0"], "padoms": "Neviens iznākums neder."},
    ], pamats=4,
        ievads="Saucējā - visi iznākumi, skaitītājā - tikai derīgie."),

    Zimejums("No neiespējama līdz drošam",
             taisne(0, 1, 1, [(1 / 6.0, "1/6"), (1 / 2.0, "1/2")],
                    virsraksts="Iespējamība vienmēr ir starp 0 un 1"),
             paskaidro="Pie 0 ir neiespējams notikums, pie 1 - drošs. "
                       "Sešnieks ar {1|6} atrodas tuvāk nullei, pāra "
                       "skaitlis ar {1|2} - tieši vidū.",
             ievads="Visas iespējamības var salikt uz vienas taisnes."),

    Varianti("Cik liela ir iespējamība?", [
        {"jaut": "Kurš skaitlis ir saucējā?",
         "opcijas": ["Visu iznākumu skaits", "Labvēlīgo iznākumu skaits",
                     "Mēģinājumu skaits", "Spēlētāju skaits"],
         "pareizi": 0,
         "padoms": "Saucējs ir viss, kas var notikt."},
        {"jaut": "Kāda ir neiespējama notikuma iespējamība?",
         "opcijas": ["0", "1", "{1|2}", "{1|6}"],
         "pareizi": 0,
         "padoms": "Neviens iznākums neder."},
        {"jaut": "Kāda ir droša notikuma iespējamība?",
         "opcijas": ["1", "0", "{1|2}", "{6|1}"],
         "pareizi": 0,
         "padoms": "Visi iznākumi der."},
        {"jaut": "Vai iespējamība var būt {7|6}?",
         "opcijas": ["Nē, tā nav lielāka par 1", "Jā", "Tikai ar kauliņu",
                     "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Labvēlīgo nav vairāk par visiem."},
        {"jaut": "Ar ko iespējamība atšķiras no biežuma?",
         "opcijas": ["Iespējamību rēķina pirms mēģinājuma",
                     "Tās ir viens un tas pats",
                     "Biežumam nav saucēja",
                     "Iespējamība ir vesels skaitlis"],
         "pareizi": 0,
         "padoms": "Biežums nāk no datiem."},
        {"jaut": "Maisā 8 bumbiņas, 2 zaļas. Kāda iespējamība izvilkt "
                 "zaļu?",
         "opcijas": ["{1|4}", "{1|2}", "{2|6}", "{1|8}"],
         "pareizi": 0,
         "padoms": "{2|8}."},
    ], pamats=4),

    Pasaule("Kurš atbildēs pie tāfeles?",
            Ievadi("", [
                {"jaut": "Klasē 24 skolēni. Kāda iespējamība, ka izsauks "
                         "tieši tevi? Atbildi raksti kā a/b.",
                 "atb": ["1/24"], "padoms": "Viens no 24."},
                {"jaut": "Klasē 24 skolēni, 12 no tiem zēni. Kāda "
                         "iespējamība, ka izsauks zēnu? Atbildi raksti kā "
                         "a/b.",
                 "atb": ["1/2", "12/24"], "padoms": "Puse klases."},
                {"jaut": "Klasē 20 skolēni, 5 sēž pirmajā rindā. Kāda "
                         "iespējamība, ka izsauks kādu no tiem? Atbildi "
                         "raksti kā a/b.",
                 "atb": ["1/4", "5/20"], "padoms": "{5|20}."},
                {"jaut": "Klasē 20 skolēni. Kāda iespējamība, ka izsauks "
                         "kādu no klases? Ieraksti skaitli.",
                 "atb": ["1"], "padoms": "Drošs notikums."},
            ]),
            pavediens="skola",
            konteksts="Pie tāfeles izsauc vienu no visiem, un katram ir "
                      "vienādas izredzes.",
            kapec="Daļa pasaka, cik lielas tās izredzes patiesībā ir."),

    Kopsavilkums([
        "Saskaitu visus vienādi iespējamos iznākumus.",
        "Izsaku notikuma iespējamību kā daļu.",
        "Zinu, ka iespējamība vienmēr ir starp 0 un 1.",
        "Atšķiru iespējamību no eksperimentā izmērītā biežuma.",
    ]),

    Majas([
        "Aprēķini iespējamību uzmest kauliņā skaitli, mazāku par 3.",
        "Izdomā notikumu, kura iespējamība ir {1|4}.",
        "Uzraksti vienu neiespējamu un vienu drošu notikumu.",
    ]),
]
