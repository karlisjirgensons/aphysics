# -*- coding: utf-8 -*-
"""6. klase, 164. stunda: «Kā rēķini palīdz plānot budžetu?»

Praktiska stunda ar skolēnam svarīgu tematu. Budžets ir vienkārša izteiksme -
ienākumi mīnus izdevumi -, bet tieši tajā parādās viss gads: procenti, daļas
un negatīvie skaitļi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         dala)

TEMA = "Kā rēķini palīdz plānot budžetu?"

MERKIS = ("Plānosim budžetu, lietojot procentus, daļas un darbības ar "
          "zīmēm.")

SATURS = [
    Sakums("Budžets ir viena izteiksme",
           zimejums=dala(10, 4, "40 % uzkrājumam"),
           paraksts="No katriem 10 eiro četri paliek malā. Pārējais ir "
                    "izdevumiem.",
           fakti=["Budžets ir ienākumi mīnus izdevumi.",
                  "Ja rezultāts ir negatīvs, izdevumi ir par lieliem.",
                  "Uzkrājumu parasti plāno procentos, ne eiro."]),

    Doma("Vispirms sadali procentos, tad eiro",
         "Budžetu plāno divos soļos: ienākumus sadala procentos pa mērķiem "
         "un tikai tad pārrēķina eiro.",
         soli=[
             "Pieraksti mēneša ienākumus.",
             "Sadali tos procentos: uzkrājums, izdevumi, rezerve.",
             "Pārbaudi, vai procentu summa ir 100 %.",
             "Pārrēķini katru daļu eiro.",
             "Pārbaudi, vai kopsumma sakrīt ar ienākumiem.",
         ],
         pieze="Ja izdevumi pārsniedz ienākumus, rezultāts ir negatīvs - un "
               "tas ir tieši tas gadījums, kad negatīvs skaitlis kaut ko "
               "nozīmē: trūkstošo summu."),

    Paraugs("Sadali mēneša budžetu",
            uzd="Mēneša ienākumi 50 €. Uzkrājumam 40 %, pārējais - "
                "izdevumiem. Cik eiro katram?",
            soli=[
                ("1 % no 50 ir 0,5 €",
                 "50 : 100."),
                ("Uzkrājums: 40 · 0,5 = 20 €",
                 "40 procenti."),
                ("Izdevumiem paliek 60 %",
                 "100 − 40."),
                ("60 · 0,5 = 30 €",
                 "Pārbaude: 20 + 30 = 50."),
            ],
            atbilde="20 € uzkrājumam, 30 € izdevumiem"),

    Ievadi("Aprēķini budžetu", [
        {"jaut": "Ienākumi 50 €, uzkrājumam 40 %. Cik eiro tas ir?",
         "atb": ["20"], "padoms": "50 · 0,4."},
        {"jaut": "Cik eiro paliek izdevumiem?",
         "atb": ["30"], "padoms": "50 − 20."},
        {"jaut": "Izdevumi bija 35 €. Cik eiro pietrūka?",
         "atb": ["5"], "padoms": "30 − 35 = −5."},
        {"jaut": "Ienākumi 80 €, uzkrājumam 25 %. Cik eiro tas ir?",
         "atb": ["20"], "padoms": "80 : 4."},
        {"jaut": "Ienākumi 120 €, izdevumi 145 €. Kāds ir rezultāts eiro?",
         "atb": ["-25", "−25"], "padoms": "120 − 145."},
        {"jaut": "Cik eiro jāietaupa, lai rezultāts būtu nulle?",
         "atb": ["25"], "padoms": "Pretējais skaitlis."},
    ], pamats=4),

    Petijums("Saplāno savu mēnesi",
             vajag="burtnīca",
             soli=[
                 "Pieraksti savus mēneša ienākumus.",
                 "Sadali tos procentos: uzkrājums, tēriņi, dāvanas.",
                 "Pārbaudi, vai procentu summa ir 100 %.",
                 "Pārrēķini katru daļu eiro.",
                 "Pieraksti, kas notiktu, ja tēriņi pieaugtu par 20 %.",
             ],
             secinajums="Ja tēriņi pieaug par 20 %, uzkrājums sarūk - un "
                        "tieši to plāns parāda jau iepriekš."),

    Varianti("Ko nozīmē rezultāts?", [
        {"jaut": "Budžeta rezultāts ir −25 €. Tas nozīmē...",
         "opcijas": ["izdevumi pārsniedz ienākumus par 25 €",
                     "ietaupīti 25 €", "ienākumi ir 25 €",
                     "kļūdu rēķinā"],
         "pareizi": 0,
         "padoms": "Negatīvs skaitlis - trūkums."},
        {"jaut": "Ienākumi 60 €, uzkrājumam 25 %. Cik eiro?",
         "opcijas": ["15", "25", "45", "6"],
         "pareizi": 0,
         "padoms": "60 : 4."},
        {"jaut": "Procentu summai budžetā jābūt...",
         "opcijas": ["100 %", "50 %", "atkarīgi no summas", "jebkādai"],
         "pareizi": 0,
         "padoms": "Visi ienākumi ir kopums."},
        {"jaut": "Ja tēriņi pieaug par 20 %, uzkrājums...",
         "opcijas": ["sarūk", "aug", "nemainās", "kļūst negatīvs"],
         "pareizi": 0,
         "padoms": "Ienākumi paliek tie paši."},
    ], pamats=4),

    Pasaule("Vai pietiks dāvanai?",
            Ievadi("", [
                {"jaut": "Mēnesī ietaupa 12 €. Cik eiro būs pēc 4 mēnešiem?",
                 "atb": ["48"], "padoms": "4 · 12."},
                {"jaut": "Dāvana maksā 60 €. Cik eiro pietrūkst pēc "
                         "4 mēnešiem?",
                 "atb": ["12"], "padoms": "48 − 60 = −12."},
                {"jaut": "Pēc cik mēnešiem pietiks?",
                 "atb": ["5"], "padoms": "60 : 12."},
                {"jaut": "Ja ietaupītu 15 € mēnesī, pēc cik mēnešiem "
                         "pietiktu?",
                 "atb": ["4"], "padoms": "60 : 15."},
            ]),
            pavediens="veikals",
            konteksts="Uzkrājuma plāns pasaka, cik ilgi jāgaida - un vai "
                      "vispār ir vērts.",
            kapec="Negatīvs rezultāts te nozīmē trūkstošo summu."),

    Kopsavilkums([
        "Plānoju budžetu, sadalot ienākumus procentos.",
        "Pārrēķinu procentus eiro un pārbaudu kopsummu.",
        "Saprotu, ko nozīmē negatīvs budžeta rezultāts.",
        "Aprēķinu, pēc cik mēnešiem pietiks uzkrājuma.",
    ]),

    Majas([
        "Sadali 60 € budžetu: 30 % uzkrājumam, pārējais tēriņiem.",
        "Aprēķini, cik eiro ir katrai daļai.",
        "Pieraksti, pēc cik mēnešiem uzkrātu 90 €.",
    ]),
]
