# -*- coding: utf-8 -*-
"""6. klase, 23. stunda: «Kā reizinājumu parādīt kvadrātā?»

Jauns mikrotemats sākas ar attēlu, ne ar likumu. Kvadrāts ar malu 1 ir
vienīgais modelis, kurā uzreiz redz, kāpēc reizinot saucēji sareizinās -
un kāpēc rezultāts sanāk mazāks par abiem reizinātājiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         kvadrats)

TEMA = "Kā reizinājumu parādīt kvadrātā?"

MERKIS = ("Mācīsimies attēlot divu īstu daļu reizinājumu kvadrātā ar malu 1 "
          "un paskaidrot, ko izsaka katrs skaitlis.")

SATURS = [
    Sakums("Cik liela ir daļa no daļas?",
           zimejums=kvadrats(4, 3, 3, 2, paraksts="6 rūtiņas no 12"),
           paraksts="Kvadrāta mala ir 1. Iekrāsotas {3|4} platumā un {2|3} "
                    "augstumā - kopā {6|12}, tas ir {1|2}.",
           fakti=["Reizinājums kvadrātā ir laukums, nevis skaitļu virkne.",
                  "Saucēji sadala malas; skaitītāji pasaka, cik ņem."]),

    Doma("Reizinājums ir laukums",
         "Divu daļu reizinājums ir taisnstūra laukums kvadrātā ar malu 1: "
         "saucēju reizinājums ir rūtiņu skaits, skaitītāju - iekrāsoto.",
         soli=[
             "Sadali kvadrāta horizontālo malu pirmās daļas saucēja daļās.",
             "Sadali vertikālo malu otrās daļas saucēja daļās.",
             "Iekrāso tik kolonnu un rindu, cik pasaka skaitītāji.",
             "Saskaiti visas rūtiņas - tas ir saucējs.",
             "Saskaiti iekrāsotās - tas ir skaitītājs.",
         ],
         pieze="Tieši tāpēc {3|4} · {2|3} = {6|12}: rūtiņu ir 4 · 3, "
               "iekrāsotas ir 3 · 2. Zīmējums pierāda likumu, nevis tikai "
               "to ilustrē."),

    Slidnis("Maini otro reizinātāju",
            [{"v": "{1|2} · {1|4}", "teksts": "{1|8} no kvadrāta",
              "josla": 12, "zim": kvadrats(2, 4, 1, 1)},
             {"v": "{1|2} · {2|4}", "teksts": "{2|8} = {1|4}",
              "josla": 25, "zim": kvadrats(2, 4, 1, 2)},
             {"v": "{1|2} · {3|4}", "teksts": "{3|8} no kvadrāta",
              "josla": 37, "zim": kvadrats(2, 4, 1, 3)},
             {"v": "{1|2} · {4|4}", "teksts": "{4|8} = {1|2}",
              "josla": 50, "zim": kvadrats(2, 4, 1, 4)}],
            ievads="Spied soli pa solim: pirmais reizinātājs paliek, otrais "
                   "aug. Iekrāsotais laukums aug tieši tikpat reižu."),

    Paraugs("Uzzīmē {2|3} · {3|5}",
            uzd="Attēlo reizinājumu {2|3} · {3|5} kvadrātā ar malu 1.",
            soli=[
                ("Horizontāli - 3 daļas, vertikāli - 5",
                 "Saucēji sadala malas."),
                ("Rūtiņu kopā 3 · 5 = 15",
                 "Tas būs reizinājuma saucējs."),
                ("Iekrāso 2 kolonnas un 3 rindas",
                 "Skaitītāji pasaka, cik ņemt."),
                ("Iekrāsotas 2 · 3 = 6 rūtiņas",
                 "Tas ir reizinājuma skaitītājs."),
                ("{2|3} · {3|5} = {6|15} = {2|5}",
                 "Rezultātu saīsina ar 3."),
            ],
            atbilde="{6|15} = {2|5}"),

    Ievadi("Nolasi no kvadrāta", [
        {"jaut": "Kvadrāts sadalīts 3 x 4 rūtiņās. Cik rūtiņu tajā ir?",
         "atb": ["12"], "padoms": "3 · 4.",
         "zim": kvadrats(3, 4, 2, 3)},
        {"jaut": "Iekrāsotas 2 kolonnas un 3 rindas. Cik rūtiņu ir "
                 "iekrāsotas?",
         "atb": ["6"], "padoms": "2 · 3."},
        {"jaut": "Kāds ir reizinājuma {2|3} · {3|4} saucējs?",
         "atb": ["12"], "padoms": "Saucēju reizinājums."},
        {"jaut": "Kāds ir tā skaitītājs?",
         "atb": ["6"], "padoms": "Skaitītāju reizinājums."},
        {"jaut": "Cik rūtiņu ir kvadrātā, ja malas dalītas 5 un 6 daļās?",
         "atb": ["30"], "padoms": "5 · 6."},
        {"jaut": "Reizinājumā {4|5} · {2|6} iekrāsotas ir cik rūtiņas?",
         "atb": ["8"], "padoms": "4 · 2."},
    ], pamats=4),

    Zimejums("Simta kvadrāts",
             kvadrats(10, 10, 4, 7, paraksts="28 no 100"),
             paskaidro="{4|10} · {7|10} = {28|100}. Tas pats modelis der "
                       "arī decimāldaļām: 0,4 · 0,7 = 0,28.",
             ievads="Ja malas dala desmit daļās, rūtiņu ir tieši 100."),

    Varianti("Ko pasaka katrs skaitlis?", [
        {"jaut": "Ko kvadrātā nozīmē saucēji?",
         "opcijas": ["Cik daļās sadala malas", "Cik rūtiņu iekrāso",
                     "Cik liels ir kvadrāts", "Cik reižu reizina"],
         "pareizi": 0,
         "padoms": "Saucējs vienmēr saka, cik vienādu daļu."},
        {"jaut": "Ko nozīmē skaitītāji?",
         "opcijas": ["Cik kolonnu un rindu iekrāso",
                     "Cik rūtiņu ir kopā", "Cik liels ir rezultāts",
                     "Cik reižu saīsina"],
         "pareizi": 0,
         "padoms": "Skaitītājs saka, cik daļu ņem."},
        {"jaut": "Kāpēc rezultāts ir mazāks par abām daļām?",
         "opcijas": ["Jo ņem daļu no daļas",
                     "Jo rūtiņas ir mazas",
                     "Jo saucēji ir lieli",
                     "Tas nav mazāks"],
         "pareizi": 0,
         "padoms": "Puse no puses ir ceturtdaļa."},
        {"jaut": "Kvadrātā iekrāsotas 9 no 20 rūtiņām. Kāds ir reizinājums?",
         "opcijas": ["{9|20}", "{20|9}", "{9|9}", "{29|20}"],
         "pareizi": 0,
         "padoms": "Iekrāsotās pret visām."},
    ], pamats=4),

    Pasaule("Cik lielu daļu aizņem dobe?",
            Ievadi("", [
                {"jaut": "Dārzs ir kvadrāts. Dobe aizņem {1|2} platumā un "
                         "{1|3} garumā. Kāds ir tās saucējs?",
                 "atb": ["6"], "padoms": "2 · 3."},
                {"jaut": "Cik liela daļa no dārza tā ir? Atbildi raksti kā "
                         "a/b.",
                 "atb": ["1/6"], "padoms": "{1|2} · {1|3}."},
                {"jaut": "Otra dobe aizņem {2|3} platumā un {3|4} garumā. "
                         "Cik rūtiņu ir kopā, ja malas dala 3 un 4 daļās?",
                 "atb": ["12"], "padoms": "3 · 4."},
                {"jaut": "Cik liela daļa no dārza ir otrā dobe? Atbildi "
                         "raksti kā a/b.",
                 "atb": ["1/2", "6/12"], "padoms": "{6|12} saīsināts."},
            ]),
            pavediens="skola",
            konteksts="Skolas dārzā dobi mēra nevis metros, bet daļās no "
                      "visa laukuma - tā vieglāk salīdzināt.",
            kapec="Daļa no daļas vienmēr ir mazāka par abām."),

    Kopsavilkums([
        "Attēloju divu daļu reizinājumu kvadrātā ar malu 1.",
        "Paskaidroju, ko nozīmē saucēji un ko - skaitītāji.",
        "Nolasu rezultātu kā iekrāsoto rūtiņu daļu no visām.",
        "Saprotu, kāpēc reizinājums sanāk mazāks par abiem reizinātājiem.",
    ]),

    Majas([
        "Uzzīmē kvadrātu un attēlo tajā {1|2} · {2|5}.",
        "Atrodi reizinājumu, kura zīmējumā iekrāsotas tieši 6 rūtiņas.",
        "Paskaidro kādam mājās, kāpēc puse no puses ir ceturtdaļa.",
    ]),
]
