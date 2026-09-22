# -*- coding: utf-8 -*-
"""5. klase, 44. stunda: «Kāpēc reizinājumu sauc par kvadrātu?»

Nosaukums, kas nāk no ģeometrijas: a · a ir tieši kvadrāta laukums ar malu a.
Tas pats zīmējums vēlāk paskaidros arī kubu, un 5.6. tematā - laukuma
formulas. Te vārds «kvadrāts» pirmo reizi nozīmē abas lietas vienlaikus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kāpēc reizinājumu sauc par kvadrātu?"

MERKIS = ("Mācīsimies skaidrot, kāpēc divu vienādu skaitļu reizinājumu sauc "
          "par skaitļa kvadrātu.")

SATURS = [
    Sakums("Kāpēc tieši kvadrāts?",
           zimejums=restis([[""] * 5 for _ in range(5)]),
           paraksts="Kvadrāts ar malu 5: rindā 5 rūtiņas, rindu 5. Kopā "
                    "5 · 5 = 25.",
           fakti=["5² lasa: «pieci kvadrātā».",
                  "Skaitlis un figūra te ir viena un tā pati lieta."]),

    Doma("Kvadrātā abas malas ir vienādas",
         "a · a ir tieši tāda kvadrāta rūtiņu skaits, kura mala ir a.",
         soli=[
             "Uzzīmē kvadrātu ar malu a.",
             "Saskaiti rūtiņas rindā - to ir a.",
             "Saskaiti rindas - arī tās ir a.",
             "Rūtiņu skaits ir a · a, tas ir, a².",
         ],
         pieze="Tāpat trīs vienādu reizinātāju reizinājumu sauc par kubu: "
               "a³ ir mazo kubiņu skaits kubā, kura mala ir a. Tāpēc 2³ "
               "ir «divi "
               "kubā»."),

    Zimejums("Kvadrāts ar malu 4",
             restis([[""] * 4 for _ in range(4)]),
             paskaidro="4 · 4 = 16. Katrai malai 4 rūtiņas, kopā 16.",
             ievads="Cits kvadrāts - tā pati doma."),

    Paraugs("No malas uz laukumu un atpakaļ",
            uzd="Kvadrāta mala ir 6 rūtiņas. Cik rūtiņu tajā ir? Un kāda "
                "mala ir kvadrātam ar 49 rūtiņām?",
            soli=[
                ("6 · 6 = 36",
                 "Rūtiņu skaits ir malas kvadrāts."),
                ("Meklējam skaitli, kura kvadrāts ir 49",
                 "Tagad uzdevums ir apgriezts."),
                ("7 · 7 = 49",
                 "Pārbaudām pēc kārtas: 6 · 6 = 36, 7 · 7 = 49."),
                ("Mala ir 7 rūtiņas",
                 "Atbilde uz otro jautājumu."),
            ],
            atbilde="36 rūtiņas; mala 7"),

    Ievadi("Kvadrāti un kubi", [
        {"jaut": "Cik ir 5²?", "atb": ["25"], "padoms": "5 · 5."},
        {"jaut": "Cik ir 6²?", "atb": ["36"], "padoms": "6 · 6."},
        {"jaut": "Cik ir 9²?", "atb": ["81"], "padoms": "9 · 9."},
        {"jaut": "Kvadrātam ir 49 rūtiņas. Cik gara ir mala?", "atb": ["7"],
         "padoms": "7 · 7 = 49."},
        {"jaut": "Kvadrātam ir 100 rūtiņas. Cik gara ir mala?", "atb": ["10"],
         "padoms": "10 · 10 = 100."},
        {"jaut": "Cik ir 2³ - divi kubā?", "atb": ["8"],
         "padoms": "2 · 2 · 2."},
        {"jaut": "Cik ir 3³?", "atb": ["27"], "padoms": "3 · 3 · 3."},
        {"jaut": "Kubs salikts no 64 kubiņiem. Cik gara ir mala?",
         "atb": ["4"],
         "padoms": "4 · 4 · 4 = 64."},
    ], pamats=4,
        ievads="Kvadrāts - divas vienādas malas, kubs - trīs."),

    Varianti("Kur te ģeometrija?", [
        {"jaut": "Kāpēc a · a sauc par kvadrātu?",
         "opcijas": ["Tas ir kvadrāta ar malu a rūtiņu skaits",
                     "Jo abi skaitļi ir vienādi",
                     "Jo atbilde vienmēr ir pāra",
                     "Tas ir tikai nosaukums bez iemesla"],
         "pareizi": 0,
         "padoms": "Paskaties uz zīmējumu."},
        {"jaut": "Kā sauc a · a · a?",
         "opcijas": ["Kubs", "Kvadrāts", "Trijstūris", "Dubultkvadrāts"],
         "pareizi": 0,
         "padoms": "Trīs vienādas malas."},
        {"jaut": "Kurš skaitlis ir kāda skaitļa kvadrāts?",
         "opcijas": ["64", "60", "50", "45"],
         "pareizi": 0,
         "padoms": "8 · 8."},
        {"jaut": "Kvadrāta mala aug no 3 uz 6. Cik reižu aug rūtiņu skaits?",
         "opcijas": ["4 reizes", "2 reizes", "3 reizes", "6 reizes"],
         "pareizi": 0,
         "padoms": "9 un 36."},
    ], pamats=4),

    Pasaule("Cik punktu ir ekrānā?",
            Ievadi("", [
                {"jaut": "Ekrāna gabals ir 8 punktus plats un 8 augsts. Cik "
                         "punktu tajā ir?",
                 "atb": ["64"], "padoms": "8 · 8."},
                {"jaut": "Ikona ir 16 x 16 punkti. Cik punktu tajā ir?",
                 "atb": ["256"], "padoms": "16 · 16."},
                {"jaut": "Attēlā ir 100 punkti kvadrātā. Cik punktu ir vienā "
                         "malā?",
                 "atb": ["10"], "padoms": "10 · 10 = 100."},
                {"jaut": "Ja ikonas mala aug no 16 uz 32, cik reižu aug "
                         "punktu skaits?",
                 "atb": ["4"], "padoms": "Mala divreiz - laukums četrreiz."},
            ]),
            pavediens="dati",
            konteksts="Attēlu izmēru raksta kā «16 x 16» - un punktu skaits "
                      "ir tieši šis reizinājums.",
            kapec="Kad mala aug divreiz, punktu skaits aug četrreiz."),

    Kopsavilkums([
        "Skaidroju, kāpēc a · a sauc par skaitļa kvadrātu.",
        "Saistu pakāpi ar kvadrāta zīmējumu.",
        "Zinu, ka trīs vienādu reizinātāju reizinājumu sauc par kubu.",
        "Atrodu malu, ja zināms rūtiņu skaits.",
    ]),

    Majas([
        "Uzzīmē kvadrātus ar malu 2, 3, 4 un 5 un pieraksti rūtiņu skaitu.",
        "Atrodi visus skaitļus līdz 100, kas ir kāda skaitļa kvadrāts.",
        "Padomā, cik reižu aug laukums, ja malu palielina trīs reizes.",
    ]),
]
