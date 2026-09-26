# -*- coding: utf-8 -*-
"""2. klase, 89. stunda: «Kādi skaitļi der nevienādībā?»

Vienādībā der viens skaitlis, nevienādībā - daudzi: □ + 5 < 12 der 0, 1,
2 ... 6. Skaitļu taisne rāda, kur der: visi pa kreisi no robežas. Tā
sagatavo intervālus, kas nāks daudz vēlāk.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, taisne)

TEMA = "Kādi skaitļi der nevienādībā?"

MERKIS = ("Šodien nosauksim vairākus skaitļus, ar kuriem nevienādība ir "
          "patiesa.")

SATURS = [
    Sakums("Kuri skaitļi der: □ + 5 < 12?",
           zimejums=taisne(0, 12, 1, atzimes=[(0, "0"), (3, "3"),
                                              (6, "6"), (7, "7?")]),
           paraksts="Der 0, 1, 2, 3, 4, 5, 6. 7 vairs neder: 7 + 5 = 12.",
           fakti=["Vienādībā der viens skaitlis.",
                  "Nevienādībā - daudzi.",
                  "Atrodi robežu un pārbaudi skaitļus blakus tai."]),

    Doma("Daudz atbilžu",
         "Vispirms atrodi skaitli, ar kuru būtu vienādība, - tā ir robeža.",
         soli=[
             "□ + 5 = 12 → □ = 7. Tā ir robeža.",
             "«<»: der skaitļi, kas mazāki par robežu.",
             "«>»: der skaitļi, kas lielāki par robežu.",
             "Pārbaudi vienu skaitli no katras puses.",
         ]),

    Varianti("Vai der?", [
        {"jaut": "□ + 5 < 12. Vai der 6?", "opcijas": ["Jā", "Nē"],
         "jaukt": False, "pareizi": 0, "padoms": "11 < 12."},
        {"jaut": "□ + 5 < 12. Vai der 7?", "opcijas": ["Jā", "Nē"],
         "jaukt": False, "pareizi": 1, "padoms": "12 nav mazāks par 12."},
        {"jaut": "□ − 10 > 20. Vai der 35?", "opcijas": ["Jā", "Nē"],
         "jaukt": False, "pareizi": 0, "padoms": "25 > 20."},
        {"jaut": "□ − 10 > 20. Vai der 30?", "opcijas": ["Jā", "Nē"],
         "jaukt": False, "pareizi": 1, "padoms": "20 nav lielāks par 20."},
    ]),

    Ievadi("Robeža un derīgie", [
        {"jaut": "□ + 20 < 50. Kāds ir lielākais skaitlis, kas der?",
         "atb": ["29"], "padoms": "Robeža 30 - tas vairs neder."},
        {"jaut": "□ + 20 < 50. Cik skaitļu no 25 līdz 35 der?",
         "atb": ["5"], "padoms": "25, 26, 27, 28, 29."},
        {"jaut": "40 − □ > 30. Kāds ir lielākais derīgais skaitlis?",
         "atb": ["9"], "padoms": "40 − 10 = 30 - neder."},
        {"jaut": "□ > 95. Cik divciparu skaitļu der?", "atb": ["4"],
         "padoms": "96, 97, 98, 99."},
    ]),

    Pasaule("Vai laivā pietiks vietas?",
            Ievadi("", [
                {"jaut": "Laiva iztur mazāk nekā 100 kg. Tētis sver 78 kg. "
                         "Cik smags var būt bērns, lai 78 + □ < 100? "
                         "Lielākais vesels skaitlis?", "atb": ["21"],
                 "mers": "kg", "padoms": "78 + 22 = 100 - jau par daudz."},
            ]),
            pavediens="celojums",
            konteksts="Uz laivas ir uzraksts: kopā mazāk nekā 100 kg.",
            kapec="Nevienādība saka, kas ir drošs."),

    Kopsavilkums([
        "Zinu, ka nevienādībai der vairāki skaitļi.",
        "Atrodu robežu ar vienādību.",
        "Nosaucu derīgos skaitļus un pārbaudu tos.",
    ]),

    Majas([
        "Uzraksti 5 skaitļus, kas der: □ + 10 < 25.",
        "Uzraksti 5 skaitļus, kas der: □ − 5 > 40.",
        "Kurš ir mazākais derīgais skaitlis otrajā?",
    ]),
]
