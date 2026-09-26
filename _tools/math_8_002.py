# -*- coding: utf-8 -*-
"""8. klase, 2. stunda: «Kāpēc dati vispirms jāsakārto?»

Nesakārtotā sarakstā mazāko, lielāko un vidū esošo vērtību meklē ar acīm;
sakārtotā tās stāv savās vietās. Slīdnis parāda sakārtošanu pa soļiem, lai
redz, ka tas ir algoritms, nevis minēšana.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, restis)

TEMA = "Kāpēc dati vispirms jāsakārto?"

MERKIS = ("Sakārtosim datu kopu augošā secībā un sapratīsim, kāpēc tas "
          "palīdz to lasīt.")

_DATI = [8.4, 7.9, 9.1, 8.2, 7.9, 8.8, 8.0]


def _rinda(vertibas):
    return restis([[str(v).replace(".", ",") for v in vertibas]])


SATURS = [
    Sakums("Kurš skrēja ātrāk?",
           zimejums=_rinda(_DATI),
           paraksts="60 m skrējiena rezultāti sekundēs - tādā secībā, kā "
                    "skrēja.",
           fakti=["Ātrāko šajā rindā jāmeklē ar acīm.",
                  "Sakārtotā rindā tas stāv pirmajā vietā.",
                  "Sakārtošana ir pirmais solis jebkurai analīzei."]),

    Doma("Sakārtota datu kopa",
         "Datu kopu sakārto augošā secībā - no mazākās līdz lielākajai "
         "vērtībai. Vienādas vērtības paliek visas: ja divi skrēja 7,9 s, "
         "sakārtotajā rindā 7,9 ir divreiz.",
         soli=[
             "Saskaiti, cik vērtību ir (n).",
             "Atrodi mazāko un ieraksti to pirmo; izsvītro no saraksta.",
             "Atkārto, līdz saraksts tukšs.",
             "Pārbaudi: sakārtotajā rindā jābūt tikpat vērtību - n.",
         ],
         pieze="Izklājlapā to dara viena poga «Kārtot», bet pārbaudīt "
               "skaitu vajag vienmēr."),

    Slidnis("Sakārto pa soļiem", [
        {"v": "Sākums", "teksts": "7 rezultāti, nav kārtības",
         "zim": _rinda(_DATI)},
        {"v": "Mazākais", "teksts": "7,9 - divas reizes",
         "zim": _rinda([7.9, 7.9])},
        {"v": "Tālāk", "teksts": "8,0 un 8,2",
         "zim": _rinda([7.9, 7.9, 8.0, 8.2])},
        {"v": "Gatavs", "teksts": "7 vērtības - neviena nepazuda",
         "zim": _rinda(sorted(_DATI))},
    ], ievads="Katrā solī paņem mazāko no atlikušajām."),

    Ievadi("Lasi sakārtotu kopu", [
        {"jaut": "Sakārto: 12, 5, 9, 5, 14, 7. Kāda ir trešā vērtība?",
         "atb": ["7"], "padoms": "5; 5; 7; 9; 12; 14."},
        {"jaut": "Tajā pašā kopā: kāda ir lielākā vērtība?",
         "atb": ["14"], "padoms": "Pēdējā."},
        {"jaut": "Sakārto: 3,4; 2,9; 3,1; 3,0. Kāda ir otrā vērtība?",
         "atb": ["3", "3,0"], "padoms": "2,9; 3,0; 3,1; 3,4."},
        {"jaut": "Datu kopā 15 vērtību. Kurā vietā sakārtotajā rindā ir "
                 "vidējā pēc kārtas?",
         "atb": ["8"], "padoms": "7 pirms tās, 7 pēc."},
        {"jaut": "Sakārto: −2, 4, 0, −5, 3. Kāda ir pirmā vērtība?",
         "atb": ["−5", "-5"], "padoms": "Negatīvie ir mazāki."},
        {"jaut": "Sakārtotā kopā: 11, 13, 13, 16, x, 20. Kāds var būt "
                 "lielākais veselais x?",
         "atb": ["20"], "padoms": "x nedrīkst pārsniegt 20."},
    ], pamats=4),

    Varianti("Kas ir pareizi sakārtots?", [
        {"jaut": "Augošā secībā:",
         "opcijas": ["0,8; 1,05; 1,5; 2", "0,8; 1,5; 1,05; 2",
                     "1,05; 0,8; 1,5; 2", "2; 1,5; 1,05; 0,8"],
         "pareizi": 0, "padoms": "1,05 < 1,5."},
        {"jaut": "Kopā 4, 7, 7, 9 izmeta vienu 7. Kas slikti?",
         "opcijas": ["Pazuda viena vērtība", "Nekas - tās ir vienādas",
                     "Jāsakārto dilstoši", "Jāpieliek 8"],
         "pareizi": 0, "padoms": "Katrs mērījums skaitās."},
        {"jaut": "Kāpēc pirms analīzes kopu sakārto?",
         "opcijas": ["Lai uzreiz redzētu mazāko, lielāko un vidu",
                     "Lai vērtības kļūtu lielākas",
                     "Lai būtu mazāk vērtību", "Tā prasa skolotājs"],
         "pareizi": 0, "padoms": "Katra vērtība atrodas savā vietā."},
    ]),

    Pasaule("Sporta dienas rezultāti",
            Ievadi("", [
                {"jaut": "Tāllēkšana (m): 3,85; 4,10; 3,60; 4,35; 3,95. "
                         "Kurš rezultāts ir sakārtotās rindas vidū?",
                 "atb": ["3,95", "3.95"], "padoms": "3,60; 3,85; 3,95; ..."},
                {"jaut": "Par cik metriem labākais pārspēj sliktāko?",
                 "atb": ["0,75", "0.75"], "padoms": "4,35 − 3,60."},
                {"jaut": "Kurā vietā ir 4,10 m, ja 1. vieta ir tālākais "
                         "lēciens?",
                 "atb": ["2"], "padoms": "Dilstošā secībā."},
            ]),
            pavediens="sports",
            konteksts="Tiesnesis vietas nosaka no sakārtota saraksta - "
                      "skrējienā augošā, lēcienā dilstošā secībā.",
            kapec="Sakārtots saraksts ir gatavs protokols."),

    Kopsavilkums([
        "Sakārtoju datu kopu augošā un dilstošā secībā.",
        "Nepazaudēju vienādās vērtības.",
        "Sakārtotā kopā atrodu mazāko, lielāko un vidējo pēc kārtas.",
    ]),

    Majas([
        "Pieraksti ģimenes locekļu vecumus un sakārto tos.",
        "Nedēļu pieraksti, cik minūšu ej uz skolu, un sakārto.",
        "Uzraksti, kura vērtība ir sakārtotās rindas vidū.",
    ]),
]
