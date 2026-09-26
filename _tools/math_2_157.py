# -*- coding: utf-8 -*-
"""2. klase, 157. stunda: «Vai vienmēr dalās bez atlikuma?»

Pētījums: kuri skaitļi līdz 50 dalās ar 3, 4 vai 5 bez atlikuma? Tie ir
tabulu skaitļi. 17 : 5 - sanāk 3 un paliek 2. Atlikumu nosauc, bet ar to
vēl nerēķina.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, bildes, simta_kvadrats)

TEMA = "Vai vienmēr dalās bez atlikuma?"

MERKIS = ("Šodien noteiksim, kurus skaitļus līdz 50 var izdalīt ar 3, 4 vai "
          "5 bez atlikuma.")

_JA_NE = ["dalās", "nedalās"]

SATURS = [
    Sakums("17 konfektes 5 bērniem - vai izdosies vienādi?",
           zimejums=bildes([[("ripina", 3)]] * 5 + [[("ripina*", 2)]]),
           paraksts="Katram 3, un 2 paliek pāri.",
           fakti=["17 nedalās ar 5 bez atlikuma.",
                  "15 un 20 dalās - tie ir tabulā ar 5.",
                  "Paliekošās sauc par atlikumu."]),

    Doma("Dalās vai nedalās",
         "Skaitlis dalās ar 5, ja tas ir reizināšanas ar 5 tabulā.",
         soli=[
             "Atceries tabulu: 5, 10, 15, 20 ...",
             "Ja skaitlis tur ir - dalās bez atlikuma.",
             "Ja nav - paliks atlikums.",
             "Ar 5: skaitlis beidzas ar 0 vai 5.",
         ]),

    Varianti("Dalās bez atlikuma?", [
        {"jaut": "24 ar 4", "opcijas": _JA_NE, "jaukt": False,
         "pareizi": 0, "padoms": "4 · 6 = 24."},
        {"jaut": "22 ar 5", "opcijas": _JA_NE, "jaukt": False,
         "pareizi": 1, "padoms": "Nebeidzas ar 0 vai 5."},
        {"jaut": "27 ar 3", "opcijas": _JA_NE, "jaukt": False,
         "pareizi": 0, "padoms": "3 · 9 = 27."},
        {"jaut": "30 ar 4", "opcijas": _JA_NE, "jaukt": False,
         "pareizi": 1, "padoms": "28, 32 - 30 nav."},
    ]),

    Petijums("Simta kvadrāta pētījums", [
        "Simta kvadrātā līdz 50 iekrāso visus, kas dalās ar 5.",
        "Ar citu krāsu - kas dalās ar 4.",
        "Kuri skaitļi iekrāsoti abās krāsās?",
        "Kuri nav iekrāsoti nevienā?",
    ], vajag="simta kvadrāta lapa, 2 krāsas",
             secinajums="20 un 40 dalās gan ar 4, gan ar 5."),

    Ievadi("Atlikums", [
        {"jaut": "17 : 5 - cik katram, ja atlikums 2?", "atb": ["3"],
         "padoms": "5 · 3 = 15."},
        {"jaut": "14 : 3 - cik paliek pāri, ja katram 4?", "atb": ["2"],
         "padoms": "3 · 4 = 12."},
        {"jaut": "Cik skaitļu no 1 līdz 50 dalās ar 5?", "atb": ["10"],
         "zim": simta_kvadrats(1, 50, izcelt=list(range(5, 51, 5))),
         "padoms": "5, 10 ... 50."},
        {"jaut": "Kurš ir lielākais skaitlis līdz 50, kas dalās ar 4?",
         "atb": ["48"], "padoms": "4 · 12 = 48."},
    ]),

    Pasaule("Komandas sporta dienā",
            Varianti("", [
                {"jaut": "26 bērni jāsadala komandās pa 4. Vai visi tiks "
                         "komandās?",
                 "opcijas": ["Nē - 6 komandas un 2 paliek", "Jā"],
                 "jaukt": False, "pareizi": 0, "padoms": "4 · 6 = 24."},
                {"jaut": "Kādās komandās var sadalīt 26 bērnus bez "
                         "atlikuma?", "opcijas": ["pa 2", "pa 3", "pa 5"],
                 "pareizi": 0, "padoms": "26 ir pāra."},
            ]),
            pavediens="sports",
            konteksts="Sporta dienā visiem jābūt komandās.",
            kapec="Atlikums nozīmē, ka kāds paliek ārpusē."),

    Kopsavilkums([
        "Nosaku, vai skaitlis dalās bez atlikuma.",
        "Izmantoju reizināšanas tabulas.",
        "Zinu, kas ir atlikums.",
    ]),

    Majas([
        "Mēģini sadalīt 23 karotes 4 kaudzītēs vienādi.",
        "Cik paliek pāri?",
        "Atrodi skaitli, kas dalās gan ar 3, gan ar 4.",
    ]),
]
