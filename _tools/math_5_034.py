# -*- coding: utf-8 -*-
"""5. klase, 34. stunda: «Kā sadalīt pirmreizinātājos?»

Te satiekas 31. un 32. stunda: reizinājumu pagarina, kamēr visi reizinātāji ir
pirmskaitļi. Sadalījuma pieraksts ir stundas galvenais rezultāts - no tā
nākamajās stundās nolasa gan visus dalītājus, gan mazāko kopīgo dalāmo.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā sadalīt pirmreizinātājos?"

MERKIS = ("Iemācīsimies sadalīt skaitli pirmreizinātājos un pierakstīt "
          "rezultātu.")

SATURS = [
    Sakums("Kad sadalīšana beidzas?",
           fakti=["60 = 6 · 10 - abus vēl var sadalīt.",
                  "6 = 2 · 3 un 10 = 2 · 5 - tālāk nevar.",
                  "60 = 2 · 2 · 3 · 5. Visi četri ir pirmskaitļi."]),

    Doma("Dali ar mazāko pirmskaitli, kamēr paliek 1",
         "Sadalījums pirmreizinātājos ir vienīgais - lai kā sāktu, beigās "
         "sanāk tie paši reizinātāji.",
         soli=[
             "Dali skaitli ar 2, kamēr vien dalās.",
             "Tad mēģini 3, pēc tam 5, pēc tam 7.",
             "Katru dalītāju pieraksti blakus.",
             "Kad dalījums kļūst 1, sadalīšana ir galā.",
             "Pārbaudi: sareizini visus pierakstītos pirmskaitļus.",
         ],
         pieze="Vienalga, vai sāc ar 60 = 6 · 10 vai 60 = 4 · 15 - beigās "
               "abos gadījumos sanāk 2 · 2 · 3 · 5. Tieši tāpēc šo "
               "sadalījumu var izmantot kā skaitļa «pirkstu nospiedumu»."),

    Zimejums("Sadalīšanas soļi",
             restis([[60, 2], [30, 2], [15, 3], [5, 5], [1, ""]],
                    "kreisajā - skaitlis, labajā - dalītājs"),
             paskaidro="60 : 2 = 30, 30 : 2 = 15, 15 : 3 = 5, 5 : 5 = 1. "
                       "Labajā kolonnā salasāms: 2 · 2 · 3 · 5.",
             ievads="Tā to pieraksta stabiņā."),

    Paraugs("Sadali 60 pirmreizinātājos",
            uzd="Sadali 60 pirmreizinātājos un pieraksti rezultātu.",
            soli=[
                ("60 : 2 = 30",
                 "Sākam ar mazāko pirmskaitli."),
                ("30 : 2 = 15",
                 "Vēl reiz dalās ar 2."),
                ("15 : 3 = 5",
                 "Ar 2 vairs nedalās, mēģinām 3."),
                ("5 : 5 = 1",
                 "Palicis pats pirmskaitlis."),
                ("60 = 2 · 2 · 3 · 5",
                 "Pārbaude: 2 · 2 = 4, 4 · 3 = 12, 12 · 5 = 60."),
            ],
            atbilde="60 = 2 · 2 · 3 · 5"),

    Ievadi("Sadali pirmreizinātājos", [
        {"jaut": "Cik pirmreizinātāju ir skaitlim 60? (2 · 2 · 3 · 5)",
         "atb": ["4"], "padoms": "Saskaiti tos."},
        {"jaut": "Kurš ir lielākais 60 pirmreizinātājs?", "atb": ["5"],
         "padoms": "2 · 2 · 3 · 5."},
        {"jaut": "Cik reižu 2 parādās skaitļa 24 sadalījumā?", "atb": ["3"],
         "padoms": "24 = 2 · 2 · 2 · 3."},
        {"jaut": "Kurš ir vienīgais nepāra pirmreizinātājs skaitlim 24?",
         "atb": ["3"], "padoms": "24 = 2 · 2 · 2 · 3."},
        {"jaut": "Skaitlis 45 = 3 · 3 · ? Cik ir trūkstošais?",
         "atb": ["5"], "padoms": "45 : 9."},
        {"jaut": "Cik pirmreizinātāju ir skaitlim 100? (2 · 2 · 5 · 5)",
         "atb": ["4"], "padoms": "Saskaiti tos."},
        {"jaut": "Skaitlis 84 = 2 · 2 · 3 · ? Cik ir trūkstošais?",
         "atb": ["7"], "padoms": "84 : 12."},
        {"jaut": "Kurš ir mazākais pirmreizinātājs skaitlim 91?",
         "atb": ["7"], "padoms": "91 = 7 · 13."},
    ], pamats=4,
        ievads="Sāc ar mazāko pirmskaitli un dali, kamēr dalās."),

    Varianti("Vai sadalījums ir pareizs?", [
        {"jaut": "Kurš sadalījums ir pirmreizinātājos?",
         "opcijas": ["2 · 2 · 3 · 5", "4 · 15", "6 · 10", "2 · 30"],
         "pareizi": 0,
         "padoms": "Visiem reizinātājiem jābūt pirmskaitļiem."},
        {"jaut": "Kāpēc 60 = 4 · 15 vēl nav sadalījums pirmreizinātājos?",
         "opcijas": ["4 un 15 nav pirmskaitļi",
                     "Reizinātāju ir par maz",
                     "Rezultāts nav 60",
                     "Tas ir pareizs sadalījums"],
         "pareizi": 0,
         "padoms": "4 = 2 · 2 un 15 = 3 · 5."},
        {"jaut": "Skolēns sāka ar 60 = 6 · 10, biedrs - ar 60 = 4 · 15. Kas "
                 "sanāks beigās?",
         "opcijas": ["Abiem viens un tas pats sadalījums",
                     "Dažādi sadalījumi",
                     "Pirmajam īsāks",
                     "Otrajam vairāk reizinātāju"],
         "pareizi": 0,
         "padoms": "Sadalījums pirmreizinātājos ir vienīgais."},
        {"jaut": "Kā sadalīt pirmskaitli, piemēram 13?",
         "opcijas": ["Tas jau ir pirmreizinātājs", "13 = 1 · 13",
                     "13 = 3 · 4 + 1", "To nevar pierakstīt"],
         "pareizi": 0,
         "padoms": "Pirmskaitlis tālāk nesadalās."},
    ], pamats=4),

    Pasaule("Kā sapakot 60 flīzes?",
            Ievadi("", [
                {"jaut": "60 flīzes kastēs pa 2, kastes paletēs pa 2, paletes "
                         "kravās pa 3. Cik flīžu vienā kravā?",
                 "atb": ["12"], "padoms": "2 · 2 · 3."},
                {"jaut": "Cik tādu kravu sanāk no 60 flīzēm?",
                 "atb": ["5"], "padoms": "60 : 12."},
                {"jaut": "84 skrūves paciņās pa 2, paciņas kastēs pa 2, "
                         "kastes pa 3 plauktā. Cik plauktu vajag?",
                 "atb": ["7"], "padoms": "84 : 2 : 2 : 3."},
                {"jaut": "100 podiņus liek rindās pa 2, rindas pa 2 plauktos, "
                         "plaukti pa 5 skapī. Cik skapju vajag?",
                 "atb": ["5"], "padoms": "100 : 2 : 2 : 5."},
            ]),
            pavediens="maja",
            konteksts="Katrs iepakojuma līmenis ir viens reizinātājs - tāpēc "
                      "iepakojumu skaits ir skaitļa sadalījums.",
            kapec="Sadalījums pirmreizinātājos parāda visus iespējamos "
                  "iepakojumus."),

    Kopsavilkums([
        "Sadalu skaitli pirmreizinātājos, dalot ar mazāko pirmskaitli.",
        "Pierakstu rezultātu kā pirmskaitļu reizinājumu.",
        "Pārbaudu sadalījumu, sareizinot visus reizinātājus.",
        "Zinu, ka sadalījums pirmreizinātājos ir viens vienīgs.",
    ]),

    Majas([
        "Sadali pirmreizinātājos 72, 90 un 100.",
        "Sāc vienu no tiem divos dažādos veidos un pārbaudi, vai beigās sanāk "
        "tas pats.",
        "Atrodi skaitli, kura sadalījumā ir tikai divnieki.",
    ]),
]
