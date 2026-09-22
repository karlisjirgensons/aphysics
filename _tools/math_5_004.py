# -*- coding: utf-8 -*-
"""5. klase, 4. stunda: «Kas kopīgs divām skaitļu kopām?»

Turpinājums 3. stundai: tur bija viena kopa, te divas. Venna diagramma
parāda, ka kopām var būt kopīga daļa, un ka «un» nozīmē tieši to vidējo
laukumu. Šo pašu attēlu 5.2. tematā lietos kopīgiem dalītājiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, venna)

TEMA = "Kas kopīgs divām skaitļu kopām?"

MERKIS = ("Iemācīsimies salikt divas skaitļu kopas Venna diagrammā un "
          "pateikt, kuri skaitļi pieder abām.")

SATURS = [
    Sakums("Kurš ir gan basketbolists, gan koristas?",
           zimejums=venna(["Anna", "Pēteris"], ["Marta", "Kārlis"],
                          ["Jānis"], ("Basketbols", "Koris")),
           paraksts="Jānis dara abus, tāpēc viņš ir vidū - un tikai vienu "
                    "reizi.",
           fakti=["Kas pieder abiem sarakstiem, to raksta pārklājumā."]),

    Doma("Vidējā daļa ir tā, kas der abiem",
         "Kas der abiem nosacījumiem, to raksta apļu kopīgajā daļā - un tikai "
         "vienu reizi.",
         soli=[
             "Uzraksti abas kopas melnrakstā.",
             "Atrodi skaitļus, kas ir abos sarakstos.",
             "Tos ieraksti apļu kopīgajā daļā.",
             "Pārējos ieraksti savā pusē - katru vienu reizi.",
         ],
         pieze="Ja kopīgo skaitļu nav, apļi zīmējumā nepārklājas."),

    Zimejums("Dalās ar 2 un dalās ar 3",
             venna([2, 4, 8, 10, 14, 16], [3, 9, 15, 21, 27, 33],
                   [6, 12, 18, 24, 30], ("Dalās ar 2", "Dalās ar 3")),
             paskaidro="Vidū ir skaitļi, kas dalās gan ar 2, gan ar 3 - tie "
                       "visi dalās arī ar 6.",
             ievads="Skaitļi no 1 līdz 33, sakārtoti divās kopās."),

    Paraugs("Kuri skaitļi būs vidū?",
            uzd="Skaitļiem no 1 līdz 20 atrodi tos, kas dalās ar 4 un ar 6.",
            soli=[
                ("Dalās ar 4: 4, 8, 12, 16, 20",
                 "Vispirms uzraksta pirmo kopu."),
                ("Dalās ar 6: 6, 12, 18",
                 "Tad otro kopu."),
                ("Abos sarakstos ir 12",
                 "Salīdzina sarakstus un atrod kopīgos skaitļus."),
            ],
            atbilde="vidējā daļā ir tikai 12"),

    Ievadi("Kas ir abās kopās?", [
        {"jaut": "No 1 līdz 30: kurš skaitlis dalās gan ar 5, gan ar 6?",
         "atb": ["30"], "padoms": "Skaiti pa 5 un pa 6 un meklē sastapšanos."},
        {"jaut": "No 1 līdz 20: cik skaitļu dalās gan ar 2, gan ar 5?",
         "atb": ["2"], "padoms": "10 un 20."},
        {"jaut": "No 1 līdz 40: kurš mazākais skaitlis dalās gan ar 4, gan "
                 "ar 10?", "atb": ["20"],
         "padoms": "Pārbaudi 20 - vai tas dalās ar abiem?"},
        {"jaut": "No 1 līdz 25: cik skaitļu dalās ar 3, bet nedalās ar 2?",
         "atb": ["4"], "padoms": "3, 9, 15, 21 - pāra skaitļus izlaid."},
        {"jaut": "No 1 līdz 50: kurš mazākais skaitlis dalās gan ar 6, gan "
                 "ar 8?", "atb": ["24"], "padoms": "Skaiti pa 8: 8, 16, 24."},
        {"jaut": "No 1 līdz 12: cik skaitļu nedalās ne ar 2, ne ar 3?",
         "atb": ["4"], "padoms": "1, 5, 7, 11."},
    ], pamats=4),

    Varianti("Kur liksi šo skaitli?", [
        {"jaut": "Kopas: «dalās ar 2» un «dalās ar 9». Kur liksi 18?",
         "opcijas": ["Kopīgajā daļā", "Tikai kreisajā aplī",
                     "Tikai labajā aplī", "Ārpus abiem apļiem"],
         "pareizi": 0,
         "padoms": "18 : 2 = 9 un 18 : 9 = 2 - abi dalījumi ir veseli."},
        {"jaut": "Kopas: «pāra skaitļi» un «skaitļi lielāki par 100». "
                 "Kur liksi 99?",
         "opcijas": ["Ārpus abiem apļiem", "Kopīgajā daļā",
                     "Tikai pāra skaitļu aplī", "Tikai lielo skaitļu aplī"],
         "pareizi": 0,
         "padoms": "99 nav pāra skaitlis un nav lielāks par 100."},
        {"jaut": "Kopas «dalās ar 10» un «dalās ar 5» - ko var teikt?",
         "opcijas": ["Viss, kas dalās ar 10, dalās arī ar 5",
                     "Kopīgu skaitļu nav",
                     "Viss, kas dalās ar 5, dalās arī ar 10",
                     "Abās kopās ir vieni un tie paši skaitļi"],
         "pareizi": 0,
         "padoms": "Pārbaudi ar 15 un ar 20."},
        {"jaut": "Ja divām kopām nav neviena kopīga skaitļa, tad zīmējumā "
                 "apļi...",
         "opcijas": ["nepārklājas", "pārklājas pusē",
                     "sakrīt pilnīgi", "ir viens otra iekšpusē"],
         "pareizi": 0,
         "padoms": "Kopīgajā daļā nebūtu ko ierakstīt."},
    ], pamats=4),

    Pasaule("Kuras dienas der abiem?",
            Ievadi("", [
                {"jaut": "Viens satelīts pārlido ik pēc 3 dienām, otrs ik "
                         "pēc 4. Pēc cik dienām abi reizē?",
                 "atb": ["12"], "padoms": "Meklē pirmo kopīgo skaitli."},
                {"jaut": "Ik pēc 5 un ik pēc 6 dienām - pēc cik dienām reizē?",
                 "atb": ["30"], "padoms": "Skaiti pa 6: 6, 12, 18, 24, 30."},
                {"jaut": "Ik pēc 2 un ik pēc 8 dienām - pēc cik dienām reizē?",
                 "atb": ["8"], "padoms": "8 jau dalās ar 2."},
                {"jaut": "Ik pēc 4 un ik pēc 10 dienām - pēc cik dienām?",
                 "atb": ["20"], "padoms": "20 dalās ar abiem."},
            ]),
            pavediens="kosmoss",
            konteksts="Divi satelīti riņķo ap Zemi ar dažādu periodu un "
                      "reizēm sastopas virs vienas vietas.",
            kapec="Tā aprēķina, kad abus var nofotografēt vienā attēlā."),

    Kopsavilkums([
        "Salieku divas skaitļu kopas Venna diagrammā.",
        "Zinu, ka kopīgajā daļā ir tie skaitļi, kas der abiem nosacījumiem.",
        "Katru skaitli ierakstu tikai vienu reizi.",
    ]),

    Majas([
        "Uzzīmē divus apļus: «mājas lietas, kas ir apaļas» un «lietas, "
        "kas ir sarkanas». Ieraksti vismaz sešas lietas.",
        "Uzraksti skaitļus no 1 līdz 20 divās kopās: dalās ar 3 un dalās ar "
        "5. Kas nonāk vidū?",
        "Padomā, vai viens aplis var pilnībā atrasties otra iekšpusē.",
    ]),
]
