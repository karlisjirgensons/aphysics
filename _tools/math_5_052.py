# -*- coding: utf-8 -*-
"""5. klase, 52. stunda: «Kā izskatās divas skaitļu taisnes?»

Josla parādīja, ka daudzums ir vienāds; skaitļu taisne parāda ko vairāk -
ka abas daļas ir *viens un tas pats skaitlis*, jo tās stāv vienā punktā. Divas
taisnes viena zem otras te ir nevis izrotājums, bet pierādījums: punkti sakrīt
vertikāli, un to redz bez rēķina.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kā izskatās divas skaitļu taisnes?"

MERKIS = ("Mācīsimies atlikt daļas ar dažādiem saucējiem uz divām skaitļu "
          "taisnēm un izlasīt no tām secinājumu.")

SATURS = [
    Sakums("Divas taisnes, viens punkts",
           zimejums=taisne(0, 1, 1, [(1 / 3.0, "1/3"), (2 / 3.0, "2/3")],
                           virsraksts="Trešdaļas"),
           paraksts="Vienību sadala trijās daļās - tā rodas {1|3} un {2|3}.",
           fakti=["Daļa nav tikai gabals, bet arī skaitlis.",
                  "Katram skaitlim uz taisnes ir sava vieta.",
                  "Ja divas daļas ir vienādas, to vietas sakrīt."]),

    Doma("Vienāds punkts - vienāds skaitlis",
         "Daļas ar dažādiem saucējiem ir vienādas tad, ja uz skaitļu taisnes "
         "tās nokļūst vienā un tajā pašā punktā.",
         soli=[
             "Uzzīmē divas vienāda garuma taisnes no 0 līdz 1.",
             "Pirmo vienību sadali tik daļās, cik rāda pirmais saucējs.",
             "Otro vienību sadali tik daļās, cik rāda otrais saucējs.",
             "Atzīmē abas daļas un paskaties, vai punkti ir viens zem otra.",
             "Ja punkti sakrīt, pieraksti vienādību.",
         ],
         pieze="Abām taisnēm jāsākas ar 0 un jābeidzas ar 1 vienā un tajā "
               "pašā vietā. Ja vienību izvēlas dažādu, punkti nesakrīt arī "
               "tad, kad daļas ir vienādas."),

    Zimejums("Augšējā taisne: trešdaļas",
             taisne(0, 1, 1, [(1 / 3.0, "1/3"), (2 / 3.0, "2/3")],
                    virsraksts="Vienība sadalīta 3 daļās"),
             paskaidro="Starp 0 un 1 ir divi atzīmēti punkti: {1|3} un "
                       "{2|3}.",
             ievads="Vispirms - taisne ar rupjākiem gabaliem."),

    Zimejums("Apakšējā taisne: sestdaļas",
             taisne(0, 1, 1, [(2 / 6.0, "2/6"), (3 / 6.0, "3/6"),
                              (4 / 6.0, "4/6")],
                    virsraksts="Vienība sadalīta 6 daļās"),
             paskaidro="{2|6} stāv tieši zem {1|3}, bet {4|6} - zem {2|3}. "
                       "Punkti sakrīt, tātad skaitļi ir vienādi.",
             ievads="Tā pati vienība, tikai sadalīta divreiz sīkāk."),

    Paraugs("Ko pasaka divas taisnes?",
            uzd="Uz augšējās taisnes atzīmēta {1|2}, uz apakšējās - {3|6}. "
                "Kāds secinājums no tā izriet?",
            soli=[
                ("Abas taisnes iet no 0 līdz 1",
                 "Vienība ir viena un tā pati - salīdzināt drīkst."),
                ("{1|2} ir taisnes vidū",
                 "Viens no diviem vienādiem gabaliem."),
                ("{3|6} arī ir taisnes vidū",
                 "Trīs no sešiem vienādiem gabaliem."),
                ("Punkti sakrīt",
                 "Vienā punktā - viens skaitlis."),
                ("{1|2} = {3|6}",
                 "Secinājumu pieraksta kā vienādību."),
            ],
            atbilde="{1|2} = {3|6}"),

    Ievadi("Kurš punkts sakrīt?", [
        {"jaut": "Uz sestdaļu taisnes - kura daļa stāv tur, kur {1|3}? "
                 "Atbildi raksti kā a/b.",
         "atb": ["2/6"], "padoms": "Trešdaļa ir divas sestdaļas."},
        {"jaut": "Uz sestdaļu taisnes - kura daļa stāv tur, kur {1|2}? "
                 "Atbildi raksti kā a/b.",
         "atb": ["3/6"], "padoms": "Puse ir trīs sestdaļas."},
        {"jaut": "Uz astotdaļu taisnes - kura daļa stāv tur, kur {1|4}? "
                 "Atbildi raksti kā a/b.",
         "atb": ["2/8"], "padoms": "Ceturtdaļa ir divas astotdaļas."},
        {"jaut": "Uz desmitdaļu taisnes - kura daļa stāv tur, kur {2|5}? "
                 "Atbildi raksti kā a/b.",
         "atb": ["4/10"], "padoms": "Abus locekļus reizina ar 2."},
        {"jaut": "Uz divpadsmitdaļu taisnes - kura daļa stāv tur, kur {2|3}? "
                 "Atbildi raksti kā a/b.",
         "atb": ["8/12"], "padoms": "Abus locekļus reizina ar 4."},
        {"jaut": "Uz devītdaļu taisnes - kura daļa stāv tur, kur {2|3}? "
                 "Atbildi raksti kā a/b.",
         "atb": ["6/9"], "padoms": "Abus locekļus reizina ar 3."},
    ], pamats=4,
        ievads="Jautājums vienmēr ir viens: cik sīko gabalu aizņem tā pati "
               "vieta."),

    Varianti("Ko redz uz taisnes?", [
        {"jaut": "Divas daļas atzīmētas vienā punktā. Ko tas nozīmē?",
         "opcijas": ["Tās ir viens un tas pats skaitlis",
                     "Tās ir blakus skaitļi",
                     "Viena ir mazliet lielāka",
                     "Tās nav salīdzināmas"],
         "pareizi": 0,
         "padoms": "Vienā punktā var stāvēt tikai viens skaitlis."},
        {"jaut": "Kāpēc abām taisnēm jābūt vienāda garuma?",
         "opcijas": ["Citādi vienība ir dažāda un punkti nesakrīt",
                     "Citādi zīmējums ir neglīts",
                     "Citādi iedaļu ir par daudz",
                     "Tam nav nozīmes"],
         "pareizi": 0,
         "padoms": "Salīdzina daļas no viena un tā paša veselā."},
        {"jaut": "Uz kuras taisnes iedaļas ir sīkākas?",
         "opcijas": ["Kur saucējs lielāks", "Kur saucējs mazāks",
                     "Kur skaitītājs lielāks", "Tas ir vienalga"],
         "pareizi": 0,
         "padoms": "Saucējs pasaka, cik daļās sadala vienību."},
        {"jaut": "Kur uz taisnes no 0 līdz 1 atrodas {6|6}?",
         "opcijas": ["Punktā 1", "Punktā 0", "Vidū", "Ārpus taisnes"],
         "pareizi": 0,
         "padoms": "Visi seši gabali kopā ir vesels."},
        {"jaut": "Kura daļa uz taisnes stāv tuvāk nullei?",
         "opcijas": ["{1|8}", "{1|4}", "{1|3}", "{1|2}"],
         "pareizi": 0,
         "padoms": "Jo sīkāks gabals, jo tuvāk sākumam."},
        {"jaut": "{2|6} un {1|3} atzīmētas uz divām taisnēm. Kurš pieraksts "
                 "ir pareizs?",
         "opcijas": ["{2|6} = {1|3}", "{2|6} > {1|3}", "{2|6} < {1|3}",
                     "{2|6} + {1|3}"],
         "pareizi": 0,
         "padoms": "Punkti sakrīt."},
    ], pamats=4),

    Pasaule("Divi mērtrauki uz letes",
            Ievadi("", [
                {"jaut": "Vienam mērtraukam ir 4 iedaļas, otram 8. Receptē "
                         "vajag {1|4} glāzes. Cik iedaļu tas ir uz otrā "
                         "trauka?",
                 "atb": ["2"], "padoms": "{1|4} = {2|8}."},
                {"jaut": "Tie paši trauki. Receptē vajag {3|4} glāzes. Cik "
                         "iedaļu uz otrā trauka?",
                 "atb": ["6"], "padoms": "{3|4} = {6|8}."},
                {"jaut": "Mērtraukam ir 6 iedaļas. Cik iedaļu ir puse "
                         "glāzes?",
                 "atb": ["3"], "padoms": "{1|2} = {3|6}."},
                {"jaut": "Mērtraukam ir 12 iedaļas. Cik iedaļu ir {2|3} "
                         "glāzes?",
                 "atb": ["8"], "padoms": "{2|3} = {8|12}."},
            ]),
            pavediens="virtuve",
            konteksts="Divi mērtrauki ir tās pašas divas skaitļu taisnes: "
                      "viena vienība, dažādas iedaļas.",
            kapec="Vienu un to pašu daudzumu katrs trauks nosauc ar savu "
                  "skaitli."),

    Kopsavilkums([
        "Atlieku daļas ar dažādiem saucējiem uz divām skaitļu taisnēm.",
        "Zinu, ka abām taisnēm jābūt vienādai vienībai.",
        "Secinu no sakrītošiem punktiem, ka daļas ir vienādas.",
        "Pierakstu secinājumu kā vienādību.",
    ]),

    Majas([
        "Uzzīmē divas vienāda garuma taisnes no 0 līdz 1: vienu ar "
        "ceturtdaļām, otru ar astotdaļām.",
        "Atzīmē uz tām {3|4} un pieraksti, kura astotdaļa nonāca tajā pašā "
        "punktā.",
        "Padomā, kura daļa uz piektdaļu taisnes stāv tur, kur {2|10}.",
    ]),
]
