# -*- coding: utf-8 -*-
"""6. klase, 55. stunda: «Kurš pieraksts ir ērtāks?»

Stunda par izvēli. Abi pieraksti ir pareizi, bet konkrētam aprēķinam viens
gandrīz vienmēr ir ērtāks - un tieši šī izvēle atšķir ātru risinājumu no
gara. Skolēns to pamato pats, nevis saņem gatavu likumu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kurš pieraksts ir ērtāks?"

MERKIS = ("Mācīsimies izvēlēties daļskaitļu pieraksta veidu konkrētam "
          "aprēķinam un pamatot izvēli.")

SATURS = [
    Sakums("Viens un tas pats skaitlis, divi darba veidi",
           fakti=["{1|3} · 9 ir viegli; 0,333 · 9 ir aptuveni un neērti.",
                  "0,25 + 0,5 ir viegli; {1|4} + {1|2} prasa kopsaucēju.",
                  "Pieraksta izvēle ir daļa no risinājuma, ne nejaušība."]),

    Doma("Izvēlies pēc darbības un pēc saucēja",
         "Parastās daļas ir ērtākas reizināšanai un dalīšanai un tad, kad "
         "saucējs nedalās ar 10; decimāldaļas - saskaitīšanai, "
         "salīdzināšanai un darbam ar kalkulatoru.",
         soli=[
             "Paskaties, kura darbība uzdevumā ir galvenā.",
             "Pārbaudi, vai saucēju var precīzi pārvērst decimāldaļā.",
             "Ja nevar - strādā ar parastajām daļām.",
             "Ja skaitļi jāsalīdzina - pārej uz decimāldaļām.",
             "Pieraksti, kāpēc izvēlējies tieši šo veidu.",
         ],
         pieze="Nekad nejauc abus vienā darbībā, tos nepārveidojot: "
               "«{1|3} + 0,5» vispirms jāpieraksta vienā veidā, citādi "
               "kļūda ir gandrīz droša."),

    Paraugs("Divas izteiksmes, divas izvēles",
            uzd="Kurš pieraksts ir ērtāks: {2|3} · 12 un {1|4} + 0,3?",
            soli=[
                ("{2|3} · 12 - parastā daļa",
                 "12 dalās ar 3, tāpēc saīsina un iznāk 8."),
                ("Decimālpierakstā būtu 0,666... · 12",
                 "Rezultāts nebūtu precīzs."),
                ("{1|4} + 0,3 - decimāldaļas",
                 "{1|4} = 0,25, un 0,25 + 0,3 = 0,55."),
                ("Parastajās daļās būtu {1|4} + {3|10}",
                 "Kopsaucējs 20 - ilgāk."),
            ],
            atbilde="pirmajā - parastās daļas, otrajā - decimāldaļas"),

    Ievadi("Izrēķini ērtākajā veidā", [
        {"jaut": "Cik ir {2|3} · 12?",
         "atb": ["8"], "padoms": "Saīsina 12 ar 3."},
        {"jaut": "Cik ir {1|4} + 0,3?",
         "atb": ["0,55", "0.55"], "padoms": "0,25 + 0,3."},
        {"jaut": "Cik ir {1|5} · 45?",
         "atb": ["9"], "padoms": "45 : 5."},
        {"jaut": "Cik ir 0,5 + {1|2}?",
         "atb": ["1"], "padoms": "Abi ir puse."},
        {"jaut": "Cik ir {3|4} · 0,8?",
         "atb": ["0,6", "0.6"], "padoms": "0,75 · 0,8 vai {3|4} · {4|5}."},
        {"jaut": "Cik ir {1|3} · 21?",
         "atb": ["7"], "padoms": "21 : 3."},
    ], pamats=4,
        ievads="Pirms rēķini, izlem, kurā pierakstā strādāsi."),

    Varianti("Kurš pieraksts te ir ērtāks?", [
        {"jaut": "{1|3} no 60 - kurā pierakstā rēķināt?",
         "opcijas": ["Parastajās daļās", "Decimāldaļās",
                     "Abi vienlīdz ērti", "Nevienā"],
         "pareizi": 0,
         "padoms": "60 : 3 = 20 ir precīzi."},
        {"jaut": "0,25 + 0,4 - kurā pierakstā rēķināt?",
         "opcijas": ["Decimāldaļās", "Parastajās daļās",
                     "Abi vienlīdz ērti", "Nevienā"],
         "pareizi": 0,
         "padoms": "Saskaitīšana bez kopsaucēja."},
        {"jaut": "Kurš skaitlis ir lielāks: {3|8} vai 0,4?",
         "opcijas": ["0,4", "{3|8}", "Vienādi", "Nevar salīdzināt"],
         "pareizi": 0,
         "padoms": "{3|8} = 0,375."},
        {"jaut": "Kāpēc salīdzināšanai ērtākas ir decimāldaļas?",
         "opcijas": ["Jo cipari stāv pa vietām un tos var salīdzināt uzreiz",
                     "Jo tās vienmēr ir precīzas",
                     "Jo tām nav saucēja", "Tās nav ērtākas"],
         "pareizi": 0,
         "padoms": "Salīdzina pa vietas vērtībām."},
    ], pamats=4),

    Pasaule("Kurš skrēja ātrāk?",
            Ievadi("", [
                {"jaut": "Viens veica {3|4} distances, otrs 0,8. Kurš "
                         "vairāk? Raksti «pirmais» vai «otrais».",
                 "atb": ["otrais"], "padoms": "{3|4} = 0,75."},
                {"jaut": "Trešais veica {7|10}. Cik tas ir decimāldaļā?",
                 "atb": ["0,7", "0.7"], "padoms": "{7|10}."},
                {"jaut": "Distance ir 20 km. Cik km veica pirmais?",
                 "atb": ["15"], "padoms": "{3|4} · 20."},
                {"jaut": "Cik km veica otrais?",
                 "atb": ["16"], "padoms": "0,8 · 20."},
            ]),
            pavediens="sports",
            konteksts="Sacensību rezultātus publicē gan daļās, gan "
                      "decimālpierakstā - salīdzināt var tikai vienā veidā.",
            kapec="Pareiza pieraksta izvēle padara salīdzināšanu vienkāršu."),

    Kopsavilkums([
        "Izvēlos pieraksta veidu pēc darbības un saucēja.",
        "Pamatoju savu izvēli vienā teikumā.",
        "Pārveidoju abus skaitļus vienā veidā pirms darbības.",
        "Salīdzinu daļskaitļus, pārejot uz decimālpierakstu.",
    ]),

    Majas([
        "Izrēķini {2|5} · 35 un 0,4 + {1|2} ērtākajā veidā.",
        "Sakārto augošā secībā {2|5}, 0,3 un {1|4}.",
        "Pieraksti divus gadījumus, kuros parastā daļa ir ērtāka.",
    ]),
]
