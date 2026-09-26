# -*- coding: utf-8 -*-
"""2. klase, 3. stunda: «Kurš neiederas?»

Apgriezts uzdevums: grupā viens ir lieks. Lai to atrastu, vispirms jāatrod
pazīme, kas ir visiem pārējiem - tāpēc stunda trenē to pašu domāšanu, ko
iepriekšējā, un liek to pamatot vārdos.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, bildes)

TEMA = "Kurš neiederas?"

MERKIS = ("Šodien atradīsim grupā lieko priekšmetu vai skaitli un "
          "paskaidrosim, kāpēc tas neiederas.")

SATURS = [
    Sakums("Kurš te ir lieks?",
           zimejums=bildes([["abols", "abols", "bumba", "abols"]]),
           paraksts="Trīs augļi un viena bumba.",
           fakti=["Liekais ir tas, kuram nav pārējo kopīgās pazīmes.",
                  "Dažreiz der vairākas atbildes - svarīgs ir pamatojums."]),

    Doma("Kā atrast lieko",
         "Vispirms atrodi, kas kopīgs gandrīz visiem.",
         soli=[
             "Salīdzini priekšmetus pa pāriem.",
             "Atrodi pazīmi, kas ir visiem, izņemot vienu.",
             "Tas viens ir liekais.",
             "Pasaki pamatojumu: «... neiederas, jo ...».",
         ]),

    Varianti("Atrodi lieko", [
        {"jaut": "Kura figūra neiederas?",
         "zim": bildes([["kvadrats", "trijsturis", "aplis", "kvadrats"]]),
         "opcijas": ["aplis", "trijstūris", "kvadrāts"], "pareizi": 0,
         "padoms": "Kurai figūrai nav stūru?"},
        {"jaut": "Kurš skaitlis neiederas: 10, 20, 35, 40?",
         "opcijas": ["35", "10", "40"], "pareizi": 0,
         "padoms": "Pārējie beidzas ar 0."},
        {"jaut": "Kurš neiederas: suns, kaķis, zivs, galds?",
         "opcijas": ["galds", "zivs", "kaķis"], "pareizi": 0,
         "padoms": "Pārējie ir dzīvnieki."},
        {"jaut": "Kurš skaitlis neiederas: 3, 7, 12, 5?",
         "opcijas": ["12", "3", "5"], "pareizi": 0,
         "padoms": "Pārējie ir viencipara skaitļi."},
        {"jaut": "Kurš neiederas: pirmdiena, jūlijs, trešdiena, "
                 "piektdiena?",
         "opcijas": ["jūlijs", "trešdiena", "pirmdiena"], "pareizi": 0,
         "padoms": "Pārējās ir nedēļas dienas."},
        {"jaut": "Kurš skaitlis neiederas: 11, 22, 33, 45?",
         "opcijas": ["45", "22", "11"], "pareizi": 0,
         "padoms": "Pārējiem abi cipari ir vienādi."},
    ], pamats=4),

    Varianti("Kāpēc neiederas?", [
        {"jaut": "Grupa: 2, 4, 6, 9. Kāpēc 9 neiederas?",
         "opcijas": ["Pārējie ir, skaitot pa 2", "9 ir lielākais",
                     "9 ir divciparu skaitlis"], "pareizi": 0,
         "padoms": "2, 4, 6, 8... - kur ir 9?"},
        {"jaut": "Grupa: mašīna, autobuss, velosipēds, laiva. Kāpēc laiva "
                 "neiederas?",
         "opcijas": ["Tā brauc pa ūdeni", "Tā ir liela",
                     "Tai ir riteņi"], "pareizi": 0,
         "padoms": "Pārējie brauc pa ceļu."},
        {"jaut": "Grupa: 5, 10, 15, 16. Kurš neiederas un kāpēc?",
         "opcijas": ["16 - pārējie ir, skaitot pa 5",
                     "5 - tas ir viencipara", "10 - tas beidzas ar 0"],
         "pareizi": 0, "padoms": "5, 10, 15 - kas nāk tālāk?"},
        {"jaut": "Grupa: 8, 18, 28, 30. Kurš neiederas?",
         "opcijas": ["30 - tas nebeidzas ar 8", "8 - viencipara skaitlis",
                     "Neviens"],
         "pareizi": 0, "padoms": "Paskaties uz pēdējo ciparu."},
    ]),

    Pasaule("Kas neiederas iepirkumu grozā?",
            Varianti("", [
                {"jaut": "Grozā: piens, siers, jogurts, zobu pasta. Kas "
                         "nav piena produkts?",
                 "opcijas": ["zobu pasta", "siers", "jogurts"],
                 "pareizi": 0, "padoms": "Zobu pastu neēd."},
                {"jaut": "Makā: 1 €, 2 €, 5 €, 50 c. Kas nav vesels eiro?",
                 "opcijas": ["50 c", "1 €", "5 €"], "pareizi": 0,
                 "padoms": "c - tie ir centi."},
            ]),
            pavediens="veikals",
            konteksts="Veikalā preces liek plauktos pa grupām.",
            kapec="Ja kaut kas neiederas, to ātri pamana."),

    Kopsavilkums([
        "Atrodu grupā lieko priekšmetu vai skaitli.",
        "Pamatoju: «... neiederas, jo ...».",
        "Zinu, ka dažreiz der vairākas atbildes, ja tās pamato.",
    ]),

    Majas([
        "Noliec uz galda 3 karotes un 1 dakšiņu. Lai mājinieks atrod lieko.",
        "Izdomā skaitļu grupu ar vienu lieku skaitli.",
        "Pastāsti, kāpēc tas neiederas.",
    ]),
]
