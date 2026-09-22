# -*- coding: utf-8 -*-
"""5. klase, 79. stunda: «Kā salīdzināt divas ģimenes izdevumus?»

Stunda par to, kāpēc daļa vispār ir vajadzīga. Divas summas eiro ir
salīdzināmas tikai tad, ja abām ir viens un tas pats veselais; te tā nav, un
tieši tāpēc eiro jāpārvērš daļās. Skolēnam tas ir pirmais gadījums, kad
lielāks skaitlis nozīmē mazāku daļu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, kolonnas)

TEMA = "Kā salīdzināt divas ģimenes izdevumus?"

MERKIS = ("Mācīsimies salīdzināt situācijas, kurās veselie ir dažādi, "
          "izsakot vienu lielumu kā otra daļu.")

SATURS = [
    Sakums("Kurš tērē vairāk?",
           zimejums=kolonnas([("1. ģimene", 200), ("2. ģimene", 300)], " €"),
           paraksts="Pārtikai: 200 € un 300 €. Bet vai tas jau ir "
                    "salīdzinājums?",
           fakti=["Pirmajai ģimenei ienākumi ir 800 €, otrajai 1500 €.",
                  "Eiro skaitļi vien neko nepasaka.",
                  "Salīdzināt var tikai daļas no saviem ienākumiem."]),

    Doma("Katru skaitli izsaka kā daļu no sava veselā",
         "Ja veselie ir dažādi, lielumus salīdzina, katru izsakot kā daļu no "
         "sava veselā, un tad salīdzina daļas.",
         soli=[
             "Katrai situācijai atrodi savu veselo.",
             "Uzraksti daļu: dotais lielums pār savu veselo.",
             "Saīsini abas daļas.",
             "Salīdzini daļas, vajadzības gadījumā ar kopsaucēju.",
             "Formulē secinājumu vārdiem.",
         ],
         pieze="Lielāka summa eiro var būt mazāka daļa: 300 € no 1500 € ir "
               "{1|5}, bet 200 € no 800 € ir {1|4}. Pirmā ģimene tērē mazāk "
               "eiro, bet lielāku daļu no saviem ienākumiem."),

    Paraugs("200 € no 800 € vai 300 € no 1500 €?",
            uzd="Kura ģimene pārtikai atvēl lielāku daļu no ienākumiem?",
            soli=[
                ("1. ģimene: {200|800}",
                 "Izdevumi pār ienākumiem."),
                ("{200|800} = {1|4}",
                 "Abus locekļus dala ar 200."),
                ("2. ģimene: {300|1500}",
                 "Tas pats otrai ģimenei."),
                ("{300|1500} = {1|5}",
                 "Abus locekļus dala ar 300."),
                ("{1|4} > {1|5}",
                 "Ceturtdaļa ir lielāka par piektdaļu."),
            ],
            atbilde="Lielāku daļu atvēl pirmā ģimene"),

    Ievadi("Izsaki kā daļu no ienākumiem", [
        {"jaut": "200 € no 800 €. Kāda daļa? Atbildi raksti kā a/b.",
         "atb": ["1/4"], "padoms": "{200|800}."},
        {"jaut": "300 € no 1500 €. Kāda daļa? Atbildi raksti kā a/b.",
         "atb": ["1/5"], "padoms": "{300|1500}."},
        {"jaut": "250 € no 1000 €. Kāda daļa? Atbildi raksti kā a/b.",
         "atb": ["1/4"], "padoms": "{250|1000}."},
        {"jaut": "400 € no 1200 €. Kāda daļa? Atbildi raksti kā a/b.",
         "atb": ["1/3"], "padoms": "{400|1200}."},
        {"jaut": "150 € no 900 €. Kāda daļa? Atbildi raksti kā a/b.",
         "atb": ["1/6"], "padoms": "{150|900}."},
        {"jaut": "600 € no 1500 €. Kāda daļa? Atbildi raksti kā a/b.",
         "atb": ["2/5"], "padoms": "{600|1500}, abus dala ar 300."},
        {"jaut": "450 € no 1800 €. Kāda daļa? Atbildi raksti kā a/b.",
         "atb": ["1/4"], "padoms": "{450|1800}, abus dala ar 450."},
        {"jaut": "Kura daļa ir lielāka - {1|4} vai {1|5}? Ieraksti kā a/b.",
         "atb": ["1/4"], "padoms": "Ceturtdaļa ir lielāks gabals."},
    ], pamats=4,
        ievads="Katram savs veselais - tikai tad daļas var likt blakus."),

    Zimejums("Eiro un daļas nesakrīt",
             kolonnas([("1. ģim. €", 200), ("2. ģim. €", 300)], " €"),
             paskaidro="Stabiņos otrā ģimene tērē vairāk, bet daļās tā tērē "
                       "mazāk: {1|5} pret {1|4}.",
             ievads="Stabiņš rāda eiro, nevis daļu no ienākumiem."),

    Varianti("Ko salīdzina un ko ne?", [
        {"jaut": "Kāpēc eiro summas te nevar salīdzināt tieši?",
         "opcijas": ["Ģimeņu ienākumi ir dažādi",
                     "Summas ir pārāk lielas",
                     "Eiro nav mērvienība",
                     "Var gan salīdzināt"],
         "pareizi": 0,
         "padoms": "Veselie atšķiras."},
        {"jaut": "300 € no 1500 € ir...",
         "opcijas": ["{1|5}", "{1|3}", "{3|15} nesaīsināts", "{5|1}"],
         "pareizi": 0,
         "padoms": "Abus dala ar 300."},
        {"jaut": "Vai lielāka summa vienmēr ir lielāka daļa?",
         "opcijas": ["Nē", "Jā", "Tikai ar pāra skaitļiem",
                     "Tikai tad, ja veselie ir vienādi"],
         "pareizi": 0,
         "padoms": "300 € no 1500 € ir mazāka daļa nekā 200 € no 800 €."},
        {"jaut": "Kurš skaitlis ir saucējā?",
         "opcijas": ["Ienākumi", "Izdevumi", "Starpība", "Lielākais skaitlis"],
         "pareizi": 0,
         "padoms": "Saucējs ir veselais."},
        {"jaut": "Ģimene tērē {1|3} ienākumu. Ienākumi ir 1200 €. Cik eiro "
                 "tas ir?",
         "opcijas": ["400 €", "300 €", "3 €", "1200 €"],
         "pareizi": 0,
         "padoms": "1200 : 3."},
        {"jaut": "Kad divas summas eiro var salīdzināt tieši?",
         "opcijas": ["Kad veselie ir vienādi", "Vienmēr", "Nekad",
                     "Kad summas ir apaļas"],
         "pareizi": 0,
         "padoms": "Viens un tas pats veselais."},
    ], pamats=4),

    Pasaule("Kurš pirkums ir lielāks?",
            Ievadi("", [
                {"jaut": "Anna iztērēja 20 € no 80 € kabatas naudas. Kāda "
                         "daļa? Atbildi raksti kā a/b.",
                 "atb": ["1/4"], "padoms": "{20|80}."},
                {"jaut": "Roberts iztērēja 30 € no 150 €. Kāda daļa? Atbildi "
                         "raksti kā a/b.",
                 "atb": ["1/5"], "padoms": "{30|150}."},
                {"jaut": "Kurš iztērēja lielāku daļu? Ieraksti vārdu.",
                 "atb": ["Anna", "anna"], "padoms": "{1|4} > {1|5}."},
                {"jaut": "Elza iztērēja 40 € no 120 €. Kāda daļa? Atbildi "
                         "raksti kā a/b.",
                 "atb": ["1/3"], "padoms": "{40|120}."},
            ]),
            pavediens="veikals",
            konteksts="Divi cilvēki ar dažādu naudas daudzumu vienu un to "
                      "pašu summu izjūt pavisam dažādi.",
            kapec="Daļa no savas naudas ir godīgāks salīdzinājums nekā eiro."),

    Kopsavilkums([
        "Atrodu katrai situācijai savu veselo.",
        "Izsaku doto lielumu kā daļu no sava veselā.",
        "Salīdzinu iegūtās daļas, nevis sākotnējos skaitļus.",
        "Zinu, ka lielāka summa var būt mazāka daļa.",
    ]),

    Majas([
        "Izsaki 150 € no 600 € un 200 € no 1000 € kā daļas un salīdzini.",
        "Atrodi divus skaitļus, kur lielākais ir mazākā daļa.",
        "Uzraksti vienā teikumā, kāpēc daļas ir godīgāks salīdzinājums.",
    ]),
]
