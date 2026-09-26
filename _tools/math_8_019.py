# -*- coding: utf-8 -*-
"""8. klase, 19. stunda: «Kā dala pakāpes?»

Dalīšanu atklāj kā saīsināšanu: daļā {a^5|a^2} divi reizinātāji augšā un
lejā saīsinās, paliek trīs. Kāpinātājus atņem. Pagaidām m > n - nulles un
negatīvais kāpinātājs nāks pēc dažām stundām.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, restis)

TEMA = "Kā dala pakāpes?"

MERKIS = ("Formulēsim un lietosim pakāpju dalīšanas īpašību.")

SATURS = [
    Sakums("Cik reižu miljons ir lielāks par tūkstoti?",
           zimejums=restis([["10⁶", ":", "10³", "=", "10³"],
                            ["1 000 000", ":", "1000", "=", "1000"]]),
           paraksts="Sešas nulles mīnus trīs nulles - paliek trīs.",
           fakti=["Dalot pakāpes ar vienādām bāzēm, kāpinātājus atņem.",
                  "Tas ir tas pats, kas saīsināt daļu.",
                  "Bāze nedrīkst būt 0 - ar nulli nedala."]),

    Slidnis("Saīsini daļu", [
        {"v": "{a^5|a^2}", "teksts": "Augšā 5 reizinātāji, lejā 2"},
        {"v": "{a · a · a · a · a|a · a}", "teksts": "Izraksti"},
        {"v": "a · a · a", "teksts": "Divi a saīsinās"},
        {"v": "a^3", "teksts": "5 − 2 = 3"},
        {"v": "a^m : a^n = a^{m − n}", "teksts": "Ja a ≠ 0"},
    ]),

    Doma("Dalīšanas īpašība",
         "Dalot pakāpes ar vienādām bāzēm (a ≠ 0), bāzi atstāj, bet no "
         "dalāmā kāpinātāja atņem dalītāja kāpinātāju: a^m : a^n = a^{m − n}.",
         soli=[
             "Pārbaudi, vai bāzes vienādas.",
             "Atņem: dalāmā kāpinātājs mīnus dalītāja kāpinātājs.",
             "Dalījumu var rakstīt arī kā daļu: {a^m|a^n}.",
             "Ja izteiksmē ir reizināšana un dalīšana - dari pēc kārtas.",
         ],
         pieze="Ko darīt, ja m = n vai m < n? To noskaidrosim, pētot "
               "pakāpes ar kāpinātāju 0 un negatīvu kāpinātāju."),

    Paraugs("Reizināšana un dalīšana kopā",
            uzd="Vienkāršo {x^7 · x^3|x^4}.",
            soli=[
                ("x^7 · x^3 = x^{10}", "Skaitītājā saskaita."),
                ("x^{10} : x^4 = x^6", "Dala - atņem."),
            ],
            atbilde="x^6"),

    Ievadi("Pieraksti kā vienu pakāpi", [
        {"jaut": "a^9 : a^4", "atb": ["a^5"], "padoms": "9 − 4.",
         "tastatura": "text"},
        {"jaut": "{7^8|7^6} - aprēķini vērtību", "atb": ["49"],
         "padoms": "7^2."},
        {"jaut": "y^{12} : y", "atb": ["y^11", "y^{11}"],
         "padoms": "y = y^1.", "tastatura": "text"},
        {"jaut": "{b^5 · b^4|b^3}", "atb": ["b^6"], "padoms": "9 − 3.",
         "tastatura": "text"},
        {"jaut": "{2^10|2^7} - aprēķini", "atb": ["8"], "padoms": "2^3."},
        {"jaut": "x^? : x^5 = x^4. Kāds kāpinātājs trūkst?",
         "atb": ["9"], "padoms": "? − 5 = 4."},
    ], pamats=4),

    Varianti("Atrodi kļūdu", [
        {"jaut": "a^8 : a^2 = a^4",
         "opcijas": ["Kļūda: jābūt a^6", "Pareizi", "Kļūda: jābūt a^{10}",
                     "Kļūda: jābūt 1^6"],
         "pareizi": 0, "padoms": "Atņem, nedala."},
        {"jaut": "6^5 : 6^3 = 1^2",
         "opcijas": ["Kļūda: jābūt 6^2", "Pareizi", "Kļūda: jābūt 36^2",
                     "Kļūda: jābūt 6^8"],
         "pareizi": 0, "padoms": "Bāze paliek 6."},
        {"jaut": "{10^9|10^3} ir...",
         "opcijas": ["miljons", "tūkstotis", "miljards", "3"],
         "pareizi": 0, "padoms": "10^6."},
    ]),

    Pasaule("Zvaigznes un planētas",
            Ievadi("", [
                {"jaut": "Saules masa ir apmēram 2 · 10^{30} kg, Zemes - "
                         "6 · 10^{24} kg. Cik reižu 10^{30} lielāks par "
                         "10^{24}? Atbildi kā 10^?",
                 "atb": ["10^6", "1000000"], "padoms": "30 − 24.",
                 "tastatura": "text"},
                {"jaut": "Tātad Saule ir apmēram {2|6} · 10^6 reižu smagāka. "
                         "Cik tūkstošu reižu? (noapaļo līdz veseliem)",
                 "atb": ["333"], "padoms": "{1|3} · 1 000 000 ≈ 333 000."},
                {"jaut": "Gaisma veic 3 · 10^8 m/s. Attālums līdz Saulei "
                         "1,5 · 10^{11} m. Cik sekundēs gaisma to veic?",
                 "atb": ["500"], "padoms": "0,5 · 10^3."},
            ]),
            pavediens="kosmoss",
            konteksts="Astronomijā skaitļi ir tik lieli, ka tos salīdzina, "
                      "dalot pakāpes - nulles neviens neskaita.",
            kapec="Saules gaisma līdz mums nāk ap 8 minūtēm."),

    Kopsavilkums([
        "Pamatoju a^m : a^n = a^{m − n} ar saīsināšanu.",
        "Dalu pakāpes ar vienādām bāzēm.",
        "Vienkāršoju izteiksmes ar reizināšanu un dalīšanu.",
    ]),

    Majas([
        "Vienkāršo: 3^9 : 3^5, {x^6 · x^2|x^3}, 10^8 : 10^5.",
        "Aprēķini 10^8 : 10^5, izrakstot nulles.",
        "Uzraksti trīs dalījumus, kuru rezultāts ir 2^4.",
    ]),
]
