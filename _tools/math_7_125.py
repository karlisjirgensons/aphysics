# -*- coding: utf-8 -*-
"""7. klase, 125. stunda: «Kā pārbaudīt pārveidojumu?»

Pārveidojumu var pārbaudīt divējādi: izpildot to atpakaļ (atverot iekavas
pēc iznešanas) vai ievietojot mainīgā vietā skaitli. Skaitlis ātri atrod
kļūdu, bet nepierāda pareizību - tāpēc labāk pārbaudīt ar diviem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā pārbaudīt pārveidojumu?"

MERKIS = ("Pārbaudīsim pārveidojuma pareizību, ievietojot mainīgā "
          "skaitlisku vērtību.")

SATURS = [
    Sakums("Pārbaude ar skaitli - 10 sekundēs",
           zimejums=restis([["x", "sākumā: 2(x + 3) − x", "beigās: x + 6"],
                            ["2", "8", "8"],
                            ["5", "11", "11"]]),
           paraksts="Abiem skaitļiem sakrīt - visticamāk, pareizi.",
           fakti=["Ja nesakrīt - noteikti kļūda.",
                  "Ja sakrīt ar diviem skaitļiem - gandrīz droši pareizi.",
                  "Pilns pierādījums - pārveidojumu likumi."]),

    Doma("Ievieto vienu un to pašu skaitli",
         "Pārveidojumu pārbauda, ievietojot to pašu mainīgā vērtību "
         "sākotnējā un iegūtajā izteiksmē. Vērtībām jāsakrīt. Ja tās "
         "atšķiras, pārveidojumā ir kļūda.",
         soli=[
             "Izvēlies skaitli, kas nav 0 vai 1 (piemēram, 2 vai 3).",
             "Aprēķini sākotnējās izteiksmes vērtību.",
             "Aprēķini iegūtās izteiksmes vērtību.",
             "Salīdzini. Drošībai - vēl ar citu skaitli.",
         ],
         pieze="Lineārām izteiksmēm pietiek ar diviem dažādiem skaitļiem: ja "
               "abi sakrīt, izteiksmes ir identiski vienādas."),

    Paraugs("Pārbaudi iznešanu",
            uzd="Vai 18x − 24 = 6(3x − 4)? Pārbaudi divējādi.",
            soli=[
                ("Atver iekavas: 6 · 3x − 6 · 4 = 18x − 24", "Sakrīt."),
                ("x = 2: 36 − 24 = 12", "Sākotnējā."),
                ("6(6 − 4) = 12", "Iegūtā."),
                ("Pareizi", "Abas pārbaudes sakrīt."),
            ],
            atbilde="Pareizi."),

    Ievadi("Pārbaudi ar x = 2", [
        {"jaut": "3(x − 1) + 2x = 5x − 3. Kreisā puse, ja x = 2?",
         "atb": ["7"], "padoms": "3 + 4."},
        {"jaut": "Labā puse, ja x = 2?",
         "atb": ["7"], "padoms": "10 − 3."},
        {"jaut": "4 − (x + 3) = 1 − x. Kreisā puse, ja x = 2?",
         "atb": ["−1", "-1"], "padoms": "4 − 5."},
        {"jaut": "Vai pārveidojums 4 − (x + 3) = 7 − x ir pareizs? Raksti "
                 "«jā» vai «nē».",
         "atb": ["nē", "ne"], "padoms": "Pie x = 2: −1 un 5."},
    ]),

    Varianti("Spried", [
        {"jaut": "Pārbaudē ar x = 1 vērtības sakrīt. Vai tas pierāda "
                 "pārveidojumu?",
         "opcijas": ["Nē - viens skaitlis var sakrist nejauši",
                     "Jā, vienmēr", "Jā, ja x = 1", "Pārbaude nav vajadzīga"],
         "pareizi": 0, "padoms": "Sk. x² un x pie 1."},
        {"jaut": "Pārbaudē vērtības atšķiras. Ko tas nozīmē?",
         "opcijas": ["Pārveidojumā noteikti ir kļūda",
                     "Varbūt pareizi", "Skaitlis ir slikts",
                     "Jāņem cits skaitlis"],
         "pareizi": 0, "padoms": "Identiski vienādām vienmēr sakrīt."},
        {"jaut": "Kāpēc labāk neņemt x = 0?",
         "opcijas": ["Daudzi saskaitāmie pazūd - kļūda var palikt "
                     "nepamanīta",
                     "Ar 0 nevar reizināt", "0 nav skaitlis",
                     "Tas ir aizliegts"],
         "pareizi": 0, "padoms": "3x un 5x abi ir 0."},
    ]),

    Pasaule("Excel formulas pārbaude",
            Ievadi("", [
                {"jaut": "Grāmatvedis vienkāršoja 1,21(c − 10) + 12,1 uz "
                         "1,21c. Pārbaudi ar c = 100: kreisā puse?",
                 "atb": ["121"], "padoms": "1,21 · 90 + 12,1."},
                {"jaut": "Labā puse ar c = 100?",
                 "atb": ["121"], "padoms": "1,21 · 100."},
                {"jaut": "Vai pārveidojums pareizs? Raksti «jā» vai «nē».",
                 "atb": ["jā", "ja"], "padoms": "1,21 · 10 = 12,1."},
            ]),
            pavediens="dati",
            konteksts="Pirms formulu ieviest tabulā ar tūkstošiem rindu, to "
                      "pārbauda ar dažiem skaitļiem.",
            kapec="Pārbaude pasargā no dārgām kļūdām."),

    Kopsavilkums([
        "Pārbaudu pārveidojumu, ievietojot skaitli.",
        "Pārbaudu iznešanu, atverot iekavas.",
        "Zinu, ka viena sakritība nepierāda.",
        "Pārbaudei neizvēlos 0 un 1.",
    ]),

    Majas([
        "Pārbaudi 3 savus pārveidojumus ar x = 2 un x = 3.",
        "Izdomā pārveidojumu, kas der pie x = 1, bet ir aplams.",
        "Pārbaudi: 5(a − 2) − 3(a − 4) = 2a + 2.",
    ]),
]
