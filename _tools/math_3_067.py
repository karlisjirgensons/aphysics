# -*- coding: utf-8 -*-
"""3. klase, 67. stunda: «Kā apkopot mērījumus?»

Mērījumu tabula ir pirmais datu pieraksts. Galvenais noteikums: katrā rindā
jābūt gan objektam, gan skaitlim, gan mērvienībai - citādi pēc nedēļas neviens
vairs nezinās, ko tieši mērīja.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kā apkopot mērījumus?"

MERKIS = ("Veidosim tabulu mērījumiem, precīzi norādot mērāmo objektu un "
          "mērvienību.")

SATURS = [
    Sakums("Ko nozīmē skaitlis 430 uz lapas?",
           zimejums=restis([["objekts", "mērījums", "vienība"],
                            ["klases garums", 780, "cm"],
                            ["klases platums", 620, "cm"],
                            ["durvju platums", 90, "cm"]],
                           "mērījumu tabula"),
           paraksts="Bez pirmās un pēdējās ailes skaitlis neko nestāsta.",
           fakti=["Mērījumu pieraksta tabulā ar trim ailēm.",
                  "Bez mērvienības skaitlis var nozīmēt jebko."]),

    Doma("Katrā rindā - objekts, skaitlis un mērvienība",
         "Tabula ir pieraksts, kuru var izlasīt arī pēc nedēļas un arī cits "
         "cilvēks.",
         soli=[
             "Uzzīmē tabulu ar trim ailēm.",
             "Pirmajā ailē pieraksti, ko mēri.",
             "Otrajā - mērījuma skaitli.",
             "Trešajā - mērvienību.",
             "Ja mērīji divreiz, pieraksti abus mērījumus.",
         ],
         pieze="Ja divi mērījumi atšķiras, tā nav kļūda - tā ir mērīšanas "
               "neprecizitāte. Tad ņem to, kas atkārtojas, vai mēra vēlreiz."),

    Paraugs("Kā pierakstīt mērījumu?",
            uzd="Klases garumu izmērīja divreiz: 782 cm un 778 cm. Kā to "
                "pierakstīt?",
            soli=[
                ("Abi mērījumi ir tuvu",
                 "Starpība ir tikai 4 cm."),
                ("782 + 778 = 1560; 1560 : 2 = 780",
                 "Ņem vidējo no abiem mērījumiem."),
                ("«Klases garums - 780 cm»",
                 "Tabulā ieraksta objektu, skaitli un mērvienību."),
            ],
            atbilde="780 cm"),

    Petijums("Aizpildi savu mērījumu tabulu",
             vajag="mērlente, lapa un lineāls",
             soli=[
                 "Uzzīmē tabulu ar trim ailēm.",
                 "Izmēri piecus klases objektus.",
                 "Katru izmēri divreiz un pieraksti abus skaitļus.",
                 "Ieraksti tabulā vidējo vērtību un mērvienību.",
             ],
             secinajums="Tabula ir gatava tad, kad to var izlasīt arī cits - "
                        "bez tava paskaidrojuma."),

    Ievadi("Strādā ar tabulu", [
        {"jaut": "Divi mērījumi: 782 cm un 778 cm. Kāda ir to summa?",
         "atb": ["1560"], "padoms": "782 + 778."},
        {"jaut": "Kāda ir vidējā vērtība?", "atb": ["780"],
         "padoms": "1560 : 2."},
        {"jaut": "Klase ir 780 cm un 620 cm. Cik centimetru ir perimetrs?",
         "atb": ["2800"], "padoms": "2 · 1400."},
        {"jaut": "Cik metru tas ir?", "atb": ["28"],
         "padoms": "2800 : 100."},
        {"jaut": "Divi mērījumi: 604 cm un 596 cm. Kāda ir vidējā vērtība?",
         "atb": ["600"], "padoms": "1200 : 2."},
        {"jaut": "Durvis ir 90 cm platas. Cik milimetru tas ir?",
         "atb": ["900"], "padoms": "90 · 10."},
    ], pamats=4),

    Zimejums("Slikta un laba tabula",
             restis([["slikti", "labi"],
                     ["780", "klases garums 780 cm"],
                     ["620", "klases platums 620 cm"]],
                    "ko nozīmē skaitlis"),
             paskaidro="Kreisajā pusē pēc nedēļas neviens nezinās, kas ir "
                       "780 - metri, centimetri vai soļi.",
             ievads="Salīdzini abas kolonnas."),

    Varianti("Kas tabulā pietrūkst?", [
        {"jaut": "Tabulā ierakstīts tikai «430». Kas pietrūkst?",
         "opcijas": ["Objekts un mērvienība", "Tikai mērvienība",
                     "Tikai objekts", "Nekas"],
         "pareizi": 0, "padoms": "Trīs ailes, no kurām divas tukšas."},
        {"jaut": "Divi mērījumi atšķiras par 4 cm. Ko darīt?",
         "opcijas": ["Ņemt vidējo vai mērīt vēlreiz", "Ņemt lielāko",
                     "Ņemt mazāko", "Abus izmest"],
         "pareizi": 0, "padoms": "Neliela atšķirība ir normāla."},
        {"jaut": "Kurš pieraksts ir pilnīgs?",
         "opcijas": ["loga platums 120 cm", "120", "platums 120",
                     "logs 120"],
         "pareizi": 0, "padoms": "Objekts, skaitlis un mērvienība."},
        {"jaut": "Kāpēc mēra divreiz?",
         "opcijas": ["Lai pamanītu kļūdu", "Lai būtu ilgāk",
                     "Tā prasa skolotājs", "Nav vajadzīgs"],
         "pareizi": 0, "padoms": "Viens mērījums var būt neprecīzs."},
    ], pamats=4),

    Pasaule("Kā pieraksta ceļojuma datus?",
            Ievadi("", [
                {"jaut": "1. diena 320 km, 2. diena 280 km. Cik kopā?",
                 "atb": ["600"], "padoms": "320 + 280."},
                {"jaut": "3. diena 250 km. Cik kopā trīs dienās?",
                 "atb": ["850"], "padoms": "600 + 250."},
                {"jaut": "Viss ceļš ir 1000 km. Cik atlicis?",
                 "atb": ["150"], "padoms": "1000 − 850."},
                {"jaut": "Cik kilometru vidēji nobrauca dienā trīs dienās?",
                 "atb": ["283"], "padoms": "850 : 3 ≈ 283."},
            ]),
            pavediens="celojums",
            konteksts="Ceļojuma dienasgrāmatā katrai dienai sava rinda - "
                      "datums, attālums un mērvienība.",
            kapec="Tikai tabulā redzams, cik ceļa jau paveikts un cik "
                  "atlicis."),

    Kopsavilkums([
        "Veidoju mērījumu tabulu ar trim ailēm.",
        "Pierakstu objektu, skaitli un mērvienību.",
        "Mēru divreiz un ņemu vidējo vērtību.",
        "Zinu, ka neliela atšķirība starp mērījumiem ir normāla.",
    ]),

    Majas([
        "Izmēri piecus mājas priekšmetus un pieraksti tos tabulā.",
        "Katru izmēri divreiz.",
        "Parādi tabulu mājiniekiem un pārbaudi, vai viņi to saprot bez "
        "paskaidrojuma.",
    ]),
]
