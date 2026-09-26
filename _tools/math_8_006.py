# -*- coding: utf-8 -*-
"""8. klase, 6. stunda: «Kas ir aritmētiskais vidējais?»

Vidējais ir vērtība, kas sanāktu katram, ja visu sadalītu vienlīdzīgi.
Stabiņu «nolīdzināšana» slīdnī to parāda bez formulas; formula nāk pēc tam.
Eksāmena uzdevums iet pretējā virzienā - no vidējā atrod trūkstošo vērtību.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, kolonnas)

TEMA = "Kas ir aritmētiskais vidējais?"

MERKIS = ("Aprēķināsim aritmētisko vidējo un sapratīsim, ko tas raksturo.")


def _dienas(vertibas):
    return kolonnas(list(zip(["P", "O", "T", "C", "Pk"], vertibas)))


SATURS = [
    Sakums("Cik ģitāru veikals pārdod dienā?",
           zimejums=_dienas([2, 4, 3, 5, 6]),
           paraksts="Pirmdiena - piektdiena: 20 ģitāru.",
           fakti=["Ja katru dienu pārdotu vienādi, tās būtu 4 dienā.",
                  "4 ir aritmētiskais vidējais.",
                  "Vidējais var nesakrist ne ar vienu no datiem."]),

    Slidnis("Nolīdzini stabiņus", [
        {"v": "2, 4, 3, 5, 6", "teksts": "Summa 20",
         "zim": _dienas([2, 4, 3, 5, 6])},
        {"v": "4, 4, 3, 5, 4",
         "teksts": "No piektdienas 2 pārceļ uz pirmdienu",
         "zim": _dienas([4, 4, 3, 5, 4])},
        {"v": "4, 4, 4, 4, 4",
         "teksts": "No ceturtdienas 1 pārceļ uz trešdienu",
         "zim": _dienas([4, 4, 4, 4, 4])},
    ], ievads="Pārceļot nekas nepazūd - summa paliek 20."),

    Doma("Vidējais = summa : skaits",
         "Aritmētiskais vidējais ir visu vērtību summa, dalīta ar vērtību "
         "skaitu. Tas ir «taisnīgās dalīšanas» rezultāts.",
         soli=[
             "Saskaiti visas vērtības.",
             "Saskaiti, cik vērtību ir (n).",
             "Dali summu ar n.",
             "Pārbaude: vidējais ir starp mazāko un lielāko vērtību.",
         ],
         pieze="Ja zināms vidējais un n, tad summa = vidējais · n. No tā "
               "atrod trūkstošo vērtību."),

    Paraugs("Trūkstošā vērtība",
            uzd="Ģitāras: 2, 4, 3, 5, x. Vidēji dienā pārdeva 4. Cik pārdeva "
                "piektdienā?",
            soli=[
                ("Summa = 4 · 5 = 20", "No vidējā."),
                ("2 + 4 + 3 + 5 = 14", "Zināmās dienas."),
                ("x = 20 − 14 = 6", "Trūkstošā."),
            ],
            atbilde="6 ģitāras"),

    Ievadi("Aprēķini vidējo", [
        {"jaut": "7, 9, 8, 10, 6",
         "atb": ["8"], "padoms": "40 : 5."},
        {"jaut": "1,2; 1,5; 1,8; 1,1",
         "atb": ["1,4", "1.4"], "padoms": "5,6 : 4."},
        {"jaut": "−3, 5, −1, 7",
         "atb": ["2"], "padoms": "8 : 4."},
        {"jaut": "Vidējais no 4 skaitļiem ir 12. Kāda ir summa?",
         "atb": ["48"], "padoms": "12 · 4."},
        {"jaut": "Atzīmes 7, 8, 6, x; vidējā 7,5. Kāds ir x?",
         "atb": ["9"], "padoms": "30 − 21."},
        {"jaut": "Piecu skaitļu vidējais 10. Pievieno 16. Kāds jaunais "
                 "vidējais?",
         "atb": ["11"], "padoms": "(50 + 16) : 6."},
    ], pamats=4),

    Varianti("Ko vidējais nozīmē?", [
        {"jaut": "Ģimenē vidēji 2,3 bērni. Ko tas nozīmē?",
         "opcijas": ["Bērnu skaits dalīts ar ģimeņu skaitu ir 2,3",
                     "Katrā ģimenē ir 2,3 bērni",
                     "Lielākajā daļā ģimeņu ir 2 bērni",
                     "Kļūda - bērnu nevar būt 2,3"],
         "pareizi": 0, "padoms": "Vidējais nav jābūt datu vērtībai."},
        {"jaut": "Visām vērtībām pieskaita 3. Kas notiek ar vidējo?",
         "opcijas": ["Palielinās par 3", "Nemainās",
                     "Palielinās 3 reizes", "Nevar zināt"],
         "pareizi": 0, "padoms": "Summa pieaug par 3n."},
    ]),

    Pasaule("Mana skrējiena nedēļa",
            Ievadi("", [
                {"jaut": "Noskrēju 3,2; 4; 5,1 un 3,7 km. Cik km vidēji "
                         "vienā reizē?",
                 "atb": ["4"], "padoms": "16 : 4."},
                {"jaut": "Cik km jānoskrien piektajā reizē, lai vidējais "
                         "būtu 4,5 km?",
                 "atb": ["6,5", "6.5"], "padoms": "4,5 · 5 − 16."},
                {"jaut": "Vidējais temps 6 min uz km. Cik minūšu ilgst 4 km "
                         "skrējiens?",
                 "atb": ["24"], "padoms": "6 · 4."},
            ]),
            pavediens="sports",
            konteksts="Sporta lietotnes rāda vidējo attālumu un tempu - "
                      "tieši tā plāno nākamo treniņu.",
            kapec="No vidējā mērķa atrod, cik vēl jāizdara."),

    Kopsavilkums([
        "Aprēķinu aritmētisko vidējo.",
        "No vidējā atrodu summu un trūkstošo vērtību.",
        "Pārbaudu, ka vidējais ir starp mazāko un lielāko.",
        "Skaidroju, ko vidējais nozīmē situācijā.",
    ]),

    Majas([
        "Atrodi savu atzīmju vidējo vienā mācību priekšmetā.",
        "Aprēķini, kāda atzīme vajadzīga, lai vidējais pieaugtu par 0,5.",
        "Nedēļu pieraksti soļu skaitu un atrodi vidējo dienā.",
    ]),
]
