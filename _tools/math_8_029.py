# -*- coding: utf-8 -*-
"""8. klase, 29. stunda: «Kā salīdzināt pakāpes?»

2^{30} un 3^{20} ir par lielu, lai izrēķinātu ar roku, bet salīdzināt var:
abus pārraksta ar vienādu kāpinātāju (8^{10} un 9^{10}). Divi likumi -
vienāda bāze vai vienāds kāpinātājs - un pārveidojums, kas vienu no tiem
padara pieejamu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, restis)

TEMA = "Kā salīdzināt pakāpes?"

MERKIS = ("Salīdzināsim pakāpes, izmantojot vienādas bāzes vai vienādus "
          "kāpinātājus.")

SATURS = [
    Sakums("Kurš ir lielāks: 2³⁰ vai 3²⁰?",
           zimejums=restis([["2³⁰", "=", "(2³)¹⁰", "=", "8¹⁰"],
                            ["3²⁰", "=", "(3²)¹⁰", "=", "9¹⁰"]]),
           paraksts="Vienāds kāpinātājs - salīdzina bāzes.",
           fakti=["8 < 9, tātad 8¹⁰ < 9¹⁰.",
                  "Tātad 2³⁰ < 3²⁰.",
                  "Ne viens, ne otrs nav jāizrēķina."]),

    Doma("Divi salīdzināšanas likumi",
         "Pakāpes var salīdzināt bez aprēķina, ja tām ir vienāda bāze vai "
         "vienāds kāpinātājs.",
         soli=[
             "Vienāda bāze a > 1: lielāks kāpinātājs - lielāka pakāpe.",
             "Vienāda bāze 0 < a < 1: otrādi! ({1|2})^5 < ({1|2})^3.",
             "Vienāds pozitīvs kāpinātājs, pozitīvas bāzes: lielāka bāze - "
             "lielāka pakāpe.",
             "Ja nekas nav vienāds - pārveido: 4^5 = 2^{10}.",
         ]),

    Slidnis("Salīdzini 27^4 un 9^6", [
        {"v": "27^4 ? 9^6", "teksts": "Bāzes un kāpinātāji dažādi"},
        {"v": "(3^3)^4 ? (3^2)^6", "teksts": "Abas bāzes ir 3 pakāpes"},
        {"v": "3^{12} ? 3^{12}", "teksts": "Vienāda bāze, vienāds kāpinātājs"},
        {"v": "27^4 = 9^6", "teksts": "Tās ir vienādas!"},
    ]),

    Paraugs("Bāze mazāka par 1",
            uzd="Salīdzini (0,5)^4 un (0,5)^6.",
            soli=[
                ("(0,5)^4 = 0,0625", "Reizina ar 0,5 - kļūst mazāks."),
                ("(0,5)^6 = 0,015625", "Vēl divas reizes mazāk."),
                ("(0,5)^4 > (0,5)^6", "Lielāks kāpinātājs - mazāka vērtība."),
            ],
            atbilde="(0,5)^4 > (0,5)^6"),

    Varianti("Kurš ir lielāks?", [
        {"jaut": "5^{12} vai 5^9?",
         "opcijas": ["5^{12}", "5^9", "Vienādi", "Nevar noteikt"],
         "pareizi": 0, "padoms": "Bāze > 1."},
        {"jaut": "7^{10} vai 6^{10}?",
         "opcijas": ["7^{10}", "6^{10}", "Vienādi", "Nevar noteikt"],
         "pareizi": 0, "padoms": "Vienāds kāpinātājs."},
        {"jaut": "({1|3})^2 vai ({1|3})^5?",
         "opcijas": ["({1|3})^2", "({1|3})^5", "Vienādi", "Nevar noteikt"],
         "pareizi": 0, "padoms": "Bāze < 1."},
        {"jaut": "2^{40} vai 3^{30}?",
         "opcijas": ["3^{30} = 27^{10}", "2^{40} = 16^{10}", "Vienādi",
                     "Nevar noteikt"],
         "pareizi": 0, "padoms": "Kāpinātājs 10."},
        {"jaut": "4^{15} vai 8^{10}?",
         "opcijas": ["Vienādi - abi 2^{30}", "4^{15}", "8^{10}",
                     "Nevar noteikt"],
         "pareizi": 0, "padoms": "Bāze 2."},
    ], pamats=3),

    Ievadi("Atrodi kāpinātāju", [
        {"jaut": "Lielākais veselais n, kuram 2^n < 100?",
         "atb": ["6"], "padoms": "2^6 = 64, 2^7 = 128."},
        {"jaut": "Mazākais veselais n, kuram 3^n > 1000?",
         "atb": ["7"], "padoms": "3^6 = 729, 3^7 = 2187."},
        {"jaut": "9^5 = 3^?",
         "atb": ["10"], "padoms": "(3^2)^5."},
        {"jaut": "Mazākais veselais n, kuram 10^−n < 0,0005?",
         "atb": ["4"], "padoms": "10^−4 = 0,0001."},
    ]),

    Pasaule("Cik ilgi krāt?",
            Ievadi("", [
                {"jaut": "Noguldījums katru gadu pieaug 2 reizes (spēlē). No "
                         "1 € pēc cik gadiem būs vairāk par 1000 €?",
                 "atb": ["10"], "padoms": "2^{10} = 1024."},
                {"jaut": "Cits noguldījums pieaug 4 reizes ik 2 gados. Vai tas "
                         "ir ātrāk? (4 = 2^2) Pēc 10 gadiem cik €?",
                 "atb": ["1024"], "padoms": "4^5 = 2^{10}."},
                {"jaut": "Trešais pieaug 3 reizes gadā. Pēc cik gadiem "
                         "pārsniegs 1000 €?",
                 "atb": ["7"], "padoms": "3^7 = 2187."},
            ]),
            pavediens="veikals",
            konteksts="Salīdzinot piedāvājumus ar dažādiem periodiem, tos "
                      "pārraksta ar vienādu bāzi vai laiku.",
            kapec="«4 reizes ik 2 gadus» un «2 reizes gadā» ir tas pats."),

    Kopsavilkums([
        "Salīdzinu pakāpes ar vienādu bāzi.",
        "Salīdzinu pakāpes ar vienādu kāpinātāju.",
        "Zinu, ka bāzei starp 0 un 1 salīdzinājums apgriežas.",
        "Pārveidoju pakāpes, lai tās varētu salīdzināt.",
    ]),

    Majas([
        "Salīdzini: 3^{40} un 4^{30}; 25^3 un 5^7; (0,2)^3 un (0,2)^2.",
        "Atrodi lielāko n, kuram 5^n < 10 000.",
        "Izdomā divas pakāpes, kas izskatās dažādas, bet ir vienādas.",
    ]),
]
