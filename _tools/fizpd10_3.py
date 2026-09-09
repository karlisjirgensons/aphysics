# -*- coding: utf-8 -*-
"""Fizika I, 10. klase. PD3 - Vienmērīgi paātrināta kustība (25.-40. st.)."""

PD = {
    "nr": 3,
    "klase": "10. klase",
    "nosaukums": "Vienmērīgi paātrināta kustība",
    "mape": "2. Vienmērīga paātrināta kustība",
    "fails": "PD3. Vienmērīgi paātrināta kustība_tt",
    "stundas": "25.-40.",
    "datums": "16.12.2026.",
    "kopa": 30,
    "laiks": 40,
    "apraksts": "Darbs pārbauda vienmērīgi paātrinātas kustības "
                "vienādojumus un grafikus, brīvo krišanu, vertikāli un "
                "horizontāli mestu ķermeni un kustību pa riņķa līniju.",
    "atgadne": [
        "a = (v − v₀) / t   ·   v = v₀ + at   ·   s = v₀t + at² / 2   ·   "
        "v² − v₀² = 2as",
        "Brīvā krišana:  g = 9,8 m/s² (aprēķinos drīkst 10 m/s²)   ·   "
        "h = gt² / 2   ·   v = gt",
        "Riņķa kustība:  T = t / N   ·   ν = 1 / T   ·   v = 2πR / T   ·   "
        "a = v² / R",
        "π ≈ 3,14   ·   laukums zem v(t) grafika = pārvietojums",
    ],
    "struktura": [
        ("1.", "Atpazīst paātrinātu kustību, lasa v(t) grafikus, skaidro "
               "brīvo krišanu un riņķa kustību", "25.-38.", 10),
        ("2.", "Nolasa v(t) grafiku: nosaka paātrinājumu un pārvietojumu",
         "26., 27.", 5),
        ("3.", "Aprēķina bremzēšanas ceļu un laiku", "29.", 5),
        ("4.", "Risina brīvās krišanas vai mešanas uzdevumu", "30.-34.", 5),
        ("5.", "Aprēķina riņķa kustības raksturlielumus", "35.-37.", 5),
    ],
    "varianti": [
        {
            "nr": "1. variants",
            "tests": [
                ("Kādā virzienā vērsts paātrinājums, ja ķermenis bremzē?",
                 ["ātruma virzienā", "pretēji ātrumam",
                  "perpendikulāri ātrumam", "vertikāli lejup"], 1),
                ("Ķermeņa ātrums 4 s laikā pieaug no 2 m/s līdz 10 m/s. Cik "
                 "liels ir paātrinājums?",
                 ["8 m/s²", "3 m/s²", "2 m/s²", "0,5 m/s²"], 2),
                ("Ko v(t) grafikā nozīmē taisnes slīpums?",
                 ["pārvietojumu", "ceļu", "laiku", "paātrinājumu"], 3),
                ("Kurš grafiks atbilst vienmērīgi paātrinātai kustībai bez "
                 "sākuma ātruma?",
                 ["horizontāla v(t) līnija",
                  "taisne v(t), kas iziet caur koordinātu sākumpunktu",
                  "parabola v(t)", "horizontāla x(t) līnija"], 1),
                ("Divi ķermeņi ar dažādu masu krīt brīvi bez gaisa "
                 "pretestības. Ko var teikt par to paātrinājumu?",
                 ["abiem vienāds", "smagākajam lielāks",
                  "vieglākajam lielāks", "atkarīgs no formas"], 0),
                ("Ķermenis brīvi krīt 2,0 s. Cik liels ir tā ātrums "
                 "(g = 10 m/s²)?",
                 ["5 m/s", "10 m/s", "20 m/s", "40 m/s"], 2),
                ("Ķermeni izsviež vertikāli augšup. Cik liels ir tā ātrums "
                 "augstākajā punktā?",
                 ["maksimālais", "nulle", "vienāds ar sākuma ātrumu",
                  "puse no sākuma ātruma"], 1),
                ("Horizontāli mests ķermenis. Kas nosaka krišanas laiku "
                 "(bez gaisa pretestības)?",
                 ["tikai sākuma ātrums", "tikai masa",
                  "tikai augstums", "masa un ātrums"], 2),
                ("Kāda ir centrtieces paātrinājuma virziens?",
                 ["uz riņķa centru", "pa kustības virzienu",
                  "pretēji kustības virzienam", "prom no riņķa centra"], 0),
                ("Ķermenis veic 30 apgriezienus minūtē. Cik liels ir "
                 "periods?",
                 ["30 s", "0,5 s", "2 s", "60 s"], 2),
            ],
            "uzdevumi": [
                {"tips": "parveide", "virs": "Kustība pēc v(t) grafika",
                 "punkti": 5,
                 "note": "Ķermeņa ātrums vienmērīgi pieaug no 4 m/s (t = 0) "
                         "līdz 24 m/s (t = 10 s). Aizpildi rindas! Par katru "
                         "pareizu atbildi - 1 punkts.",
                 "rindas": [
                     ("Sākuma ātrums  v₀ = ..................... m/s",
                      "4 m/s"),
                     ("Ātruma izmaiņa  Δv = ..................... m/s",
                      "20 m/s"),
                     ("Paātrinājums  a = ..................... m/s²",
                      "2 m/s²"),
                     ("Pārvietojums 10 s laikā  s = ..................... m",
                      "140 m"),
                     ("Ātrums pie t = 15 s  v = ..................... m/s",
                      "34 m/s"),
                 ]},

                {"tips": "aprekins", "virs": "Bremzēšanas ceļš", "punkti": 5,
                 "vieta": 7.5,
                 "teksts": "Automašīna, kas brauc ar ātrumu 72 km/h, sāk "
                           "vienmērīgi bremzēt un apstājas pēc 5,0 s. "
                           "Aprēķini paātrinājumu un bremzēšanas ceļu!",
                 "risinajums": [
                     "Dots:  v₀ = 72 km/h = 20 m/s;  v = 0;  t = 5,0 s",
                     "Jāaprēķina:  a = ?  s = ?",
                     "Formulas:  a = (v − v₀) / t;  s = (v₀ + v)t / 2",
                     "Aprēķins:  1) v₀ = 72 : 3,6 = 20 m/s",
                     "                   2) a = (0 − 20) : 5,0 = −4,0 m/s²",
                     "                   3) s = (20 + 0) · 5,0 : 2 = 50 m",
                     "Atbilde:  a = −4,0 m/s² (bremzēšana), s = 50 m.",
                 ],
                 "kriteriji": [
                     "1 p - ātrums pārvērsts m/s un pieraksts «Dots»;",
                     "1 p - pierakstītas abas formulas;",
                     "2 p - pareizs paātrinājums ar zīmi un mērvienību;",
                     "1 p - pareizs bremzēšanas ceļš ar mērvienību.",
                 ]},

                {"tips": "aprekins", "virs": "Horizontāli mests ķermenis",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "No 20 m augsta torņa horizontāli izsviež bumbiņu "
                           "ar ātrumu 15 m/s. Gaisa pretestību neievēro, "
                           "g = 10 m/s². Aprēķini lidojuma laiku un "
                           "attālumu no torņa pamatnes, kur bumbiņa nokrīt!",
                 "risinajums": [
                     "Dots:  h = 20 m;  v₀ = 15 m/s;  g = 10 m/s²",
                     "Jāaprēķina:  t = ?  L = ?",
                     "Formulas:  h = gt² / 2;  L = v₀t",
                     "Aprēķins:  1) t = √(2h / g) = √(2 · 20 : 10) = "
                     "√4,0 = 2,0 s",
                     "                   2) L = 15 m/s · 2,0 s = 30 m",
                     "Atbilde:  t = 2,0 s;  L = 30 m.",
                 ],
                 "kriteriji": [
                     "1 p - kustība sadalīta vertikālā un horizontālā "
                     "komponentē;",
                     "1 p - pierakstītas formulas h = gt²/2 un L = v₀t;",
                     "2 p - pareizi aprēķināts laiks t = 2,0 s;",
                     "1 p - pareizs attālums 30 m ar mērvienību.",
                 ]},

                {"tips": "jautajumi", "virs": "Kustība pa riņķa līniju",
                 "punkti": 5, "vieta": 7.0,
                 "ievads": "Karuseļa sēdeklis atrodas R = 4,0 m attālumā no "
                           "ass un veic vienu apgriezienu 8,0 s laikā.",
                 "jaut": [
                     ("Nosaki kustības periodu T!", 1),
                     ("Aprēķini frekvenci ν!", 1),
                     ("Aprēķini lineāro ātrumu v!", 1),
                     ("Aprēķini centrtieces paātrinājumu a!", 1),
                     ("Pamato, kā mainītos lineārais ātrums, ja sēdeklis "
                      "atrastos divreiz tuvāk asij (periods nemainīgs)!", 1),
                 ],
                 "atbildes": [
                     "1) T = 8,0 s.   (1 p)",
                     "2) ν = 1 / T = 1 : 8,0 = 0,125 Hz ≈ 0,13 Hz.   (1 p)",
                     "3) v = 2πR / T = 2 · 3,14 · 4,0 : 8,0 ≈ 3,1 m/s.   "
                     "(1 p)",
                     "4) a = v² / R = 3,1² : 4,0 ≈ 2,4 m/s².   (1 p)",
                     "5) Ātrums samazinātos divas reizes (v ~ R pie "
                     "nemainīga T), tātad v ≈ 1,6 m/s.   (1 p)",
                 ]},
            ],
        },
        {
            "nr": "2. variants",
            "tests": [
                ("Kādā virzienā vērsts paātrinājums, ja ķermeņa ātrums "
                 "pieaug?",
                 ["pretēji ātrumam", "ātruma virzienā",
                  "perpendikulāri ātrumam", "vienmēr lejup"], 1),
                ("Ķermeņa ātrums 5 s laikā samazinās no 20 m/s līdz 5 m/s. "
                 "Cik liels ir paātrinājuma modulis?",
                 ["15 m/s²", "5 m/s²", "3 m/s²", "4 m/s²"], 2),
                ("Ko v(t) grafikā nozīmē laukums zem līnijas?",
                 ["paātrinājumu", "laiku", "masu", "pārvietojumu"], 3),
                ("Kurš x(t) grafiks atbilst vienmērīgi paātrinātai "
                 "kustībai?",
                 ["horizontāla līnija", "slīpa taisne", "parabola",
                  "lauzta līnija"], 2),
                ("Kas notiek ar brīvi krītoša ķermeņa ātrumu katrā sekundē "
                 "(g = 10 m/s²)?",
                 ["nemainās", "pieaug par 10 m/s",
                  "pieaug par 5 m/s", "samazinās par 10 m/s"], 1),
                ("No cik liela augstuma ķermenis brīvi krīt 3,0 s "
                 "(g = 10 m/s²)?",
                 ["15 m", "30 m", "45 m", "90 m"], 2),
                ("Ķermeni izsviež vertikāli augšup ar ātrumu 20 m/s. Cik "
                 "ilgi tas ceļas (g = 10 m/s²)?",
                 ["1,0 s", "2,0 s", "4,0 s", "20 s"], 1),
                ("Horizontāli mestam ķermenim horizontālā virzienā kustība "
                 "ir:",
                 ["vienmērīga", "vienmērīgi paātrināta",
                  "vienmērīgi palēnināta", "svārstību kustība"], 0),
                ("Vienmērīgā riņķa kustībā nemainīgs paliek:",
                 ["ātruma vektors", "paātrinājuma vektors",
                  "pārvietojums", "ātruma modulis"], 3),
                ("Frekvence ir 4 Hz. Cik liels ir periods?",
                 ["4 s", "0,4 s", "0,25 s", "40 s"], 2),
            ],
            "uzdevumi": [
                {"tips": "parveide", "virs": "Kustība pēc v(t) grafika",
                 "punkti": 5,
                 "note": "Ķermeņa ātrums vienmērīgi samazinās no 30 m/s "
                         "(t = 0) līdz 6 m/s (t = 8 s). Aizpildi rindas! Par "
                         "katru pareizu atbildi - 1 punkts.",
                 "rindas": [
                     ("Sākuma ātrums  v₀ = ..................... m/s",
                      "30 m/s"),
                     ("Ātruma izmaiņa  Δv = ..................... m/s",
                      "−24 m/s"),
                     ("Paātrinājums  a = ..................... m/s²",
                      "−3 m/s²"),
                     ("Pārvietojums 8 s laikā  s = ..................... m",
                      "144 m"),
                     ("Laiks līdz apstāšanās brīdim  t = ..................."
                      "... s", "10 s"),
                 ]},

                {"tips": "aprekins", "virs": "Ieskriešanās ceļš",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "Vilciens no miera stāvokļa vienmērīgi paātrinās "
                           "un pēc 40 s sasniedz ātrumu 54 km/h. Aprēķini "
                           "paātrinājumu un ceļu, ko vilciens šajā laikā "
                           "veic!",
                 "risinajums": [
                     "Dots:  v₀ = 0;  v = 54 km/h = 15 m/s;  t = 40 s",
                     "Jāaprēķina:  a = ?  s = ?",
                     "Formulas:  a = (v − v₀) / t;  s = (v₀ + v)t / 2",
                     "Aprēķins:  1) v = 54 : 3,6 = 15 m/s",
                     "                   2) a = 15 : 40 = 0,375 m/s² ≈ "
                     "0,38 m/s²",
                     "                   3) s = 15 · 40 : 2 = 300 m",
                     "Atbilde:  a ≈ 0,38 m/s²;  s = 300 m.",
                 ],
                 "kriteriji": [
                     "1 p - ātrums pārvērsts m/s un pieraksts «Dots»;",
                     "1 p - pierakstītas abas formulas;",
                     "2 p - pareizs paātrinājums ar mērvienību;",
                     "1 p - pareizs ceļš ar mērvienību.",
                 ]},

                {"tips": "aprekins", "virs": "Horizontāli mests ķermenis",
                 "punkti": 5, "vieta": 7.5,
                 "teksts": "No 45 m augsta tilta horizontāli izsviež akmeni "
                           "ar ātrumu 8,0 m/s. Gaisa pretestību neievēro, "
                           "g = 10 m/s². Aprēķini lidojuma laiku un "
                           "horizontālo attālumu, ko akmens veic!",
                 "risinajums": [
                     "Dots:  h = 45 m;  v₀ = 8,0 m/s;  g = 10 m/s²",
                     "Jāaprēķina:  t = ?  L = ?",
                     "Formulas:  h = gt² / 2;  L = v₀t",
                     "Aprēķins:  1) t = √(2h / g) = √(2 · 45 : 10) = "
                     "√9,0 = 3,0 s",
                     "                   2) L = 8,0 m/s · 3,0 s = 24 m",
                     "Atbilde:  t = 3,0 s;  L = 24 m.",
                 ],
                 "kriteriji": [
                     "1 p - kustība sadalīta vertikālā un horizontālā "
                     "komponentē;",
                     "1 p - pierakstītas formulas h = gt²/2 un L = v₀t;",
                     "2 p - pareizi aprēķināts laiks t = 3,0 s;",
                     "1 p - pareizs attālums 24 m ar mērvienību.",
                 ]},

                {"tips": "jautajumi", "virs": "Kustība pa riņķa līniju",
                 "punkti": 5, "vieta": 7.0,
                 "ievads": "Velosipēda ritenis ar rādiusu R = 0,35 m veic "
                           "120 apgriezienus minūtē.",
                 "jaut": [
                     ("Aprēķini periodu T!", 1),
                     ("Aprēķini frekvenci ν!", 1),
                     ("Aprēķini riteņa malas punkta lineāro ātrumu v!", 1),
                     ("Aprēķini centrtieces paātrinājumu a!", 1),
                     ("Pamato, kāpēc riteņa centrā esošā punkta lineārais "
                      "ātrums ir mazāks!", 1),
                 ],
                 "atbildes": [
                     "1) T = 60 s : 120 = 0,50 s.   (1 p)",
                     "2) ν = 1 / T = 2,0 Hz.   (1 p)",
                     "3) v = 2πR / T = 2 · 3,14 · 0,35 : 0,50 ≈ 4,4 m/s.   "
                     "(1 p)",
                     "4) a = v² / R = 4,4² : 0,35 ≈ 55 m/s².   (1 p)",
                     "5) Visi riteņa punkti apgriezienu veic vienādā laikā "
                     "(vienāds T), bet tuvāk asij esošais punkts veic mazāku "
                     "riņķa līniju, tāpēc v = 2πR/T ir mazāks.   (1 p)",
                 ]},
            ],
        },
    ],
}
