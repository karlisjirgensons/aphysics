# -*- coding: utf-8 -*-
"""Fizika I, 11. klase. ĀT1 — Svārstības, viļņi un skaņa (6.1.-6.3.).

Ātrais tests pirms PD1 «Mehāniskās svārstības un viļņi». Jautājumi
neatkārto PD1 abu variantu testa daļu.
"""

AT = {
    "nr": 1,
    "nosaukums": "Svārstības, viļņi un skaņa",
    "prieksmets": "Fizika I  |  11. klase",
    "sakne": "Fizika_1",
    "mape": "6. Mehāniskās svārstības un viļņi",
    "fails": "ĀT1. Svārstības, viļņi un skaņa_tt",
    "stundas": "1.-3.",
    "datums": "11.09.2026.",
    "laiks": 15,
    "apraksts": "Ātrais tests pirms temata pārbaudes darba. Pārbauda "
                "svārstību raksturlielumus un pašfrekvenci, matemātiskā "
                "svārsta perioda atkarību no garuma, skaņas izplatīšanos "
                "dažādās vidēs, atbalsi, ultraskaņu un sakarību v = λν.",
    "atgadne": [
        "T = t / N   ·   ν = 1 / T   ·   v = λν   ·   λ = v · T   ·   "
        "T = 2π√(l / g)",
        "Skaņas ātrums: gaisā ≈ 340 m/s  ·  ūdenī ≈ 1500 m/s  ·  tēraudā "
        "≈ 5000 m/s   ·   1 min = 60 s   ·   1 kHz = 10³ Hz",
    ],
    "struktura": [
        ("1.-3.", "Raksturo svārstības ar periodu, frekvenci un "
                  "pašfrekvenci; saista matemātiskā svārsta periodu ar "
                  "garumu", "6.1."),
        ("4., 5., 10., 11.", "Skaidro skaņas izplatīšanos un ātrumu dažādās "
                             "vidēs, atbalsi un ultraskaņu", "6.2."),
        ("6.-9.", "Nolasa viļņa grafiku un lieto sakarību v = λν", "6.3."),
        ("12.", "Atpazīst rezonansi ikdienas piemēros un atšķir to no citām "
                "parādībām", "6.1."),
    ],
    "jautajumi": [
        ("Kas ir svārstību sistēmas pašfrekvence?",
         ["lielākā iespējamā svārstību frekvence",
          "frekvence, ar kādu sistēma svārstās bez ārējas iedarbības",
          "ārējā spēka frekvence",
          "frekvence, pie kuras svārstības apstājas"], 1),

        ("Svārsta periods ir 0,25 s. Cik pilnas svārstības tas veic vienā "
         "minūtē?",
         ["15", "60", "25", "240"], 3),

        ("Kā mainās matemātiskā svārsta periods, ja tā garumu palielina "
         "4 reizes?",
         ["palielinās 2 reizes", "palielinās 4 reizes",
          "samazinās 2 reizes", "nemainās"], 0),

        ("Kurā vidē skaņa izplatās visātrāk?",
         ["gaisā", "ūdenī", "tēraudā", "visās vidēs vienādi"], 2),

        ("Kāda ir ultraskaņas frekvence?",
         ["mazāka par 20 Hz", "lielāka par 20 000 Hz",
          "no 20 Hz līdz 20 000 Hz", "tieši 1000 Hz"], 1),

        ("Viļņa grafikā uz horizontālās ass atlikts attālums. Ko šajā "
         "grafikā var tieši nolasīt?",
         ["periodu", "frekvenci", "viļņa ātrumu", "viļņa garumu"], 3),

        ("Skaņas vilnis no gaisa pāriet ūdenī. Kurš lielums nemainās?",
         ["frekvence", "viļņa garums", "izplatīšanās ātrums",
          "viļņa enerģija"], 0),

        ("Viļņa ātrums ir 12 m/s, periods — 0,50 s. Cik liels ir viļņa "
         "garums?",
         ["24 m", "0,042 m", "6,0 m", "12 m"], 2),

        ("Kā mainās viļņa garums, ja frekvenci palielina 2 reizes un ātrums "
         "nemainās?",
         ["palielinās 2 reizes", "samazinās 2 reizes", "nemainās",
          "palielinās 4 reizes"], 1),

        ("Zibens novērots 3,0 s pirms pērkona dārdiena. Cik tālu ir "
         "negaiss? (skaņas ātrums gaisā 340 m/s)",
         ["113 m", "340 m", "3400 m", "1020 m"], 3),

        ("Kas ir atbalss?",
         ["skaņas atstarošanās no šķēršļa",
          "skaņas frekvences maiņa",
          "divu skaņu rezonanse gaisā",
          "skaņas ātruma pieaugums"], 0),

        ("Kurš piemērs NAV saistīts ar rezonansi?",
         ["ģitāras korpuss pastiprina stīgas skaņu",
          "tiltu var iešūpot, ritmiski soļojot",
          "akmens iekrīt ūdenī un rada viļņus",
          "radiouztvērēju noskaņo uz raidstacijas frekvenci"], 2),
    ],
}
