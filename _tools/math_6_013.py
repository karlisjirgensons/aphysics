# -*- coding: utf-8 -*-
"""6. klase, 13. stunda: «Ko stāsta tabula un grafiks?»

Proporcionalitāte iegūst seju. Tabula ir precīza, bet klusa; grafiks pasaka
vienā acu uzmetienā to, ko tabulā vēl jāizlasa. Šī ir arī pirmā stunda, kur
6. klasē parādās koordinātu plakne - pagaidām tikai pirmais kvadrants.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, plakne, restis)

TEMA = "Ko stāsta tabula un grafiks?"

MERKIS = ("Mācīsimies apkopot proporcionālu lielumu datus tabulā un attēlot "
          "tos grafiski.")

SATURS = [
    Sakums("Kāpēc datus zīmē, nevis tikai raksta?",
           zimejums=plakne(lauzta=[(0, 0), (1, 2), (2, 4), (3, 6), (4, 8)],
                           no_x=0, lidz_x=5, no_y=0, lidz_y=10, solis=1,
                           x_nos="kg", y_nos="€"),
           paraksts="Katrs kilograms maksā 2 €. Punkti izkārtojas taisnē, "
                    "kas sākas nullē.",
           fakti=["Tieši proporcionālu lielumu grafiks vienmēr ir taisne.",
                  "Tā iet caur nulli: nav preces - nav maksas."]),

    Doma("Tabula glabā, grafiks parāda",
         "Tieši proporcionāliem lielumiem punkti grafikā sakrīt uz vienas "
         "taisnes, kas sākas koordinātu sākumpunktā.",
         soli=[
             "Izveido tabulu: augšējā rindā viens lielums, apakšējā - otrs.",
             "Aizpildi to, reizinot vienas vienības vērtību.",
             "Atliec katru pāri kā punktu plaknē.",
             "Savieno punktus - ja tie ir uz vienas taisnes, lielumi ir "
             "proporcionāli.",
             "Pārbaudi, vai taisne iet caur punktu (0; 0).",
         ],
         pieze="Ja punkti nav uz vienas taisnes vai taisne nesākas nullē, "
               "lielumi nav tieši proporcionāli - un to redz ātrāk nekā "
               "izrēķina."),

    Zimejums("Tā izskatās tabula",
             restis([["kg", "1", "2", "3", "4"],
                     ["€", "2", "4", "6", "8"]]),
             paskaidro="Augšējā rindā - masa, apakšējā - cena. Katra kolonna "
                       "ir viens punkts grafikā.",
             ievads="Tabulā skaitļi stāv pa pāriem."),

    Paraugs("No tabulas uz grafiku",
            uzd="1 kg ābolu maksā 2 €. Izveido tabulu līdz 4 kg un attēlo "
                "datus grafikā.",
            soli=[
                ("1 kg → 2 €",
                 "Vienas vienības vērtība ir grafika slīpums."),
                ("2 kg → 4 €; 3 kg → 6 €; 4 kg → 8 €",
                 "Katrs nākamais ir par 2 € lielāks."),
                ("Punkti (1; 2), (2; 4), (3; 6), (4; 8)",
                 "Pirmais skaitlis - uz horizontālās ass."),
                ("Visi punkti uz vienas taisnes caur (0; 0)",
                 "Tā ir tiešas proporcionalitātes pazīme."),
            ],
            atbilde="taisne caur koordinātu sākumpunktu"),

    Ievadi("Aizpildi tabulu", [
        {"jaut": "1 kg maksā 3 €. Cik eiro maksā 4 kg?",
         "atb": ["12"], "padoms": "4 · 3."},
        {"jaut": "Tā pati cena. Cik kilogramu var nopirkt par 21 €?",
         "atb": ["7"], "padoms": "21 : 3."},
        {"jaut": "Grafikā punkts ir (5; 15). Cik maksā viena vienība?",
         "atb": ["3"], "padoms": "15 : 5.",
         "zim": plakne(punkti=[(5, 15, "(5; 15)")], no_x=0, lidz_x=6,
                       no_y=0, lidz_y=18, solis=3)},
        {"jaut": "Tabulā: 2 → 10, 4 → 20, 6 → ? Kāds skaitlis trūkst?",
         "atb": ["30"], "padoms": "Viena vienība ir 5."},
        {"jaut": "Caur kuru punktu iet katra tiešas proporcionalitātes "
                 "taisne? Ieraksti pirmo koordinātu.",
         "atb": ["0"], "padoms": "Punkts (0; 0)."},
        {"jaut": "Punkts (3; 12) ir uz taisnes. Kāda ir y vērtība, ja x ir 7?",
         "atb": ["28"], "padoms": "Viena vienība ir 4."},
    ], pamats=4),

    Varianti("Ko grafiks pastāsta?", [
        {"jaut": "Punkti nav uz vienas taisnes. Ko tas nozīmē?",
         "opcijas": ["Lielumi nav tieši proporcionāli",
                     "Tabula ir aizpildīta nepareizi",
                     "Grafiks ir par mazu", "Tas nekad nenotiek"],
         "pareizi": 0,
         "padoms": "Proporcionalitātei punkti vienmēr ir uz taisnes."},
        {"jaut": "Taisne ir stāvāka. Ko tas nozīmē?",
         "opcijas": ["Viena vienība maksā vairāk", "Datu ir vairāk",
                     "Grafiks ir nepareizs", "Cena krītas"],
         "pareizi": 0,
         "padoms": "Slīpums ir vienas vienības vērtība."},
        {"jaut": "Taisne nesākas nullē. Kas tas varētu būt?",
         "opcijas": ["Maksa ar pamatcenu, piemēram abonēšanu",
                     "Tieša proporcionalitāte",
                     "Kļūda zīmējumā", "Nekas tāds nav iespējams"],
         "pareizi": 0,
         "padoms": "Ja bez precēm jau kaut kas jāmaksā, nulle nesakrīt."},
        {"jaut": "Kurš tabulas pāris veido punktu (4; 20)?",
         "opcijas": ["4 kg par 20 €", "20 kg par 4 €",
                     "4 € par 20 kg", "Nevar noteikt"],
         "pareizi": 0,
         "padoms": "Pirmais skaitlis ir horizontālajā asī."},
    ], pamats=4),

    Pasaule("Cik maksās skolas ekskursija?",
            Ievadi("", [
                {"jaut": "Autobusa biļete vienam skolēnam ir 4 €. Cik eiro "
                         "maksā 25 biļetes?",
                 "atb": ["100"], "padoms": "25 · 4."},
                {"jaut": "Cik skolēni var braukt par 60 €?",
                 "atb": ["15"], "padoms": "60 : 4."},
                {"jaut": "Grafikā punkts ir (10; 40). Cik maksā viena "
                         "biļete?",
                 "atb": ["4"], "padoms": "40 : 10."},
                {"jaut": "Ja biļete kļūtu par 1 € dārgāka, cik eiro maksātu "
                         "25 biļetes?",
                 "atb": ["125"], "padoms": "25 · 5."},
            ]),
            pavediens="skola",
            konteksts="Skolotājs rāda vienu grafiku, un vecāki uzreiz redz, "
                      "cik maksās brauciens jebkuram skaitam.",
            kapec="Viens punkts uz taisnes pasaka visu pārējo taisni."),

    Kopsavilkums([
        "Apkopoju proporcionālu lielumu datus tabulā.",
        "Attēloju tabulas pārus kā punktus koordinātu plaknē.",
        "Zinu, ka tiešas proporcionalitātes grafiks ir taisne caur nulli.",
        "No grafika slīpuma nolasu vienas vienības vērtību.",
    ]),

    Majas([
        "Izveido tabulu savam ceļam uz skolu: 1, 2, 3 un 4 gājieni turp un "
        "atpakaļ.",
        "Uzzīmē šo tabulu kā grafiku rūtiņu lapā.",
        "Atrodi internetā grafiku, kas *nav* taisne, un pieraksti, ko tas "
        "attēlo.",
    ]),
]
