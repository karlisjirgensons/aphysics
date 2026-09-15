# -*- coding: utf-8 -*-
"""Fizika I, 10. klase. ĀT1 — Kustība, ātrums un grafiki (6.-11. stunda).

Ātrais tests starp PD1 (vektori, 5. stunda) un PD2 (kustība, 23. stunda).
Jautājumi neatkārto ne PD1, ne PD2 saturu.
"""

AT = {
    "nr": 1,
    "nosaukums": "Kustība, ātrums un grafiki",
    "prieksmets": "Fizika I  |  10. klase",
    "sakne": "Fizika_1",
    "mape": "1. Ievads pētniecībā. Vienmērīga un nevienmērīga kustība",
    "fails": "ĀT1. Kustība, ātrums un grafiki_tt",
    "stundas": "6.-11.",
    "datums": "07.10.2026.",
    "laiks": 15,
    "apraksts": "Ātrais tests pēc vienmērīgas kustības bloka. Pārbauda "
                "mehāniskās kustības un relatīvās kustības izpratni, ceļa un "
                "pārvietojuma nošķiršanu, sakarību v = s/t, kustības "
                "vienādojumu, grafiku lasīšanu un vidējo ātrumu.",
    "atgadne": [
        "v = s / t   ·   s = v · t   ·   x = x₀ + v · t   ·   no km/h uz m/s "
        "dala ar 3,6",
        "Vidējais ātrums:  v(vid.) = s(kopā) / t(kopā)   ·   riņķa līnijas "
        "garums l = 2πr   ·   π ≈ 3,14",
    ],
    "struktura": [
        ("1.-3.", "Skaidro mehānisko kustību un relatīvo kustību; nosaka, "
                  "kad ķermeni drīkst uzskatīt par materiālu punktu",
         "1.5."),
        ("4., 5.", "Atšķir trajektoriju, ceļu un pārvietojumu; nosaka "
                   "pārvietojuma moduli vienkāršā trajektorijā", "1.6."),
        ("6.-8.", "Lieto sakarību v = s/t, pārvērš m/s un km/h, lieto "
                  "kustības vienādojumu x = x₀ + vt", "1.7., 1.8."),
        ("9., 12.", "Atpazīst vienmērīgas kustības grafikus un nosaka divu "
                    "ķermeņu satikšanās laiku", "1.8., 1.9."),
        ("10., 11.", "Aprēķina vidējo ātrumu un pamato, kāpēc tas nav "
                     "ātrumu vidējais aritmētiskais", "1.10."),
    ],
    "jautajumi": [
        ("Ko fizikā sauc par mehānisko kustību?",
         ["ķermeņa formas maiņu",
          "ķermeņa masas maiņu",
          "ķermeņa stāvokļa maiņu pret citiem ķermeņiem laika gaitā",
          "ķermeņa temperatūras maiņu"], 2),

        ("Kad ķermeni drīkst uzskatīt par materiālu punktu?",
         ["kad tā izmēri ir mazi salīdzinājumā ar veicamo ceļu",
          "kad tā masa ir maza",
          "kad tas kustas lēni",
          "jebkurā gadījumā"], 0),

        ("Pasažieris sēž kustīgā vilcienā. Pret ko viņš atrodas miera "
         "stāvoklī?",
         ["pret sliedēm", "pret staciju", "pret vagonu",
          "pret ceļmalas kokiem"], 2),

        ("Kas ir trajektorija?",
         ["nobrauktā ceļa garums",
          "līnija, pa kuru ķermenis pārvietojas",
          "vektors no sākuma punkta uz beigu punktu",
          "ātruma izmaiņa laikā"], 1),

        ("Ķermenis veic pusapli pa riņķa līniju, kuras rādiuss ir 10 m. Cik "
         "liels ir pārvietojuma modulis?",
         ["10 m", "20 m", "31 m", "63 m"], 1),

        ("Cik m/s ir 108 km/h?",
         ["10,8 m/s", "39 m/s", "300 m/s", "30 m/s"], 3),

        ("Ķermenis vienmērīgi nobrauc 60 m 4 s laikā. Cik liels ir tā "
         "ātrums?",
         ["240 m/s", "15 m/s", "0,067 m/s", "64 m/s"], 1),

        ("Kustības vienādojums ir x = 12 − 4t (SI vienībās). Kurā vietā "
         "ķermenis atrodas brīdī t = 2 s?",
         ["4 m", "8 m", "20 m", "−4 m"], 0),

        ("Kāds izskatās vienmērīgas taisnvirziena kustības v(t) grafiks?",
         ["taisne caur koordinātu sākumpunktu",
          "horizontāla taisne",
          "parabola",
          "lauzta līnija"], 1),

        ("Ķermenis pirmos 100 m veic 20 s, nākamos 100 m — 30 s. Cik liels "
         "ir vidējais ātrums visā ceļā?",
         ["5,0 m/s", "4,2 m/s", "4,0 m/s", "3,3 m/s"], 2),

        ("Kāpēc vidējo ātrumu nedrīkst rēķināt kā posmu ātrumu vidējo "
         "aritmētisko?",
         ["jo ātrums ir vektoriāls lielums",
          "jo mērvienības nesakrīt",
          "jo ceļš vienmēr ir lielāks par pārvietojumu",
          "jo posmos pavadītais laiks parasti ir atšķirīgs"], 3),

        ("Divu ķermeņu kustību apraksta x₁ = 2t un x₂ = 30 − 3t (SI "
         "vienībās). Pēc cik ilga laika tie satiksies?",
         ["3 s", "5 s", "6 s", "15 s"], 2),
    ],
}
