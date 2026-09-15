# -*- coding: utf-8 -*-
"""Fizika I, 10. klase. Formatīvais darbs Nr. 1 — Kustība, ātrums un grafiki.

Saturs 1. temata 5.-10. stundai (mehāniskā kustība, ceļš un pārvietojums,
vienmērīga kustība, kustības vienādojums, grafiki, vidējais ātrums). Tas pats
tvērums, kas ĀT1 darba lapai, tikai katram sasniedzamajam rezultātam te ir
vairāki līdzvērtīgi jautājumi, no kuriem lapa izlozē vienu.

Jaunu variantu pievieno, ierakstot grupā vēl vienu jautājumu - pārējais
(uzbūve, atbilžu tabula, vērtēšanas skala) mainās pats.

Daļas raksta ar {skaitītājs|saucējs}: «v = {s|t}». Mērvienības (km/h, m/s)
raksta parasti.
"""

FD = {
    "nr": 1,
    "nosaukums": "Kustība, ātrums un grafiki",
    "prieksmets": "Fizika I  |  10. klase",
    "kicker": "1. temats · 5.-10. stunda · 12 jautājumi · 15 minūtes",
    "sakne": "Fizika_1",
    "mape": "1. Ievads pētniecībā. Vienmērīga un nevienmērīga kustība",
    "fails": "Formatīvais darbs_tt",
    "laiks": 15,
    "apraksts": "Formatīvais darbs pēc vienmērīgas kustības bloka. Pārbauda "
                "mehāniskās un relatīvās kustības izpratni, ceļa un "
                "pārvietojuma nošķiršanu, sakarību v = {s|t}, kustības "
                "vienādojumu, grafiku lasīšanu un vidējo ātrumu.",
    "atgadne": [
        "v = {s|t}   ·   s = v · t   ·   t = {s|v}   ·   x = x₀ + v · t"
        "   ·   no km/h uz m/s dala ar 3,6",
        "Vidējais ātrums:  v(vid) = {s(kopā)|t(kopā)}   ·   riņķa līnijas "
        "garums l = 2πr   ·   π ≈ 3,14",
    ],
    "grupas": [
        # ------------------------------------------------ 1. mehāniskā kustība
        {"sr": "Skaidro, kas fizikā ir mehāniskā kustība",
         "stunda": "1.5.",
         "jautajumi": [
             ("Ko fizikā sauc par mehānisko kustību?",
              ["ķermeņa formas maiņu",
               "ķermeņa masas maiņu",
               "ķermeņa stāvokļa maiņu pret citiem ķermeņiem laika gaitā",
               "ķermeņa temperatūras maiņu"], 2),

             ("Kurš apgalvojums par mehānisko kustību ir pareizs?",
              ["kustība vienmēr notiek pa taisnu līniju",
               "ķermeņa novietojums mainās pret atskaites ķermeni",
               "kustība nav atkarīga no atskaites ķermeņa izvēles",
               "kustībā ķermeņa masa vienmēr mainās"], 1),

             ("Kas noteikti jāizvēlas, lai varētu aprakstīt ķermeņa "
              "mehānisko kustību?",
              ["ķermeņa masa un tilpums",
               "atskaites ķermenis, koordinātu ass un pulkstenis",
               "ķermeņa temperatūra un blīvums",
               "tikai nobrauktais ceļš"], 1),
         ]},

        # ------------------------------------------------ 2. materiāls punkts
        {"sr": "Nosaka, kad ķermeni drīkst uzskatīt par materiālu punktu",
         "stunda": "1.5.",
         "jautajumi": [
             ("Kad ķermeni drīkst uzskatīt par materiālu punktu?",
              ["kad tā izmēri ir mazi salīdzinājumā ar veicamo ceļu",
               "kad tā masa ir maza",
               "kad tas kustas lēni",
               "jebkurā gadījumā"], 0),

             ("Kurā gadījumā Zemi drīkst uzskatīt par materiālu punktu?",
              ["aprēķinot Zemes kustību ap Sauli",
               "aprakstot diennakts maiņu uz Zemes",
               "mērot Zemes rādiusu",
               "pētot vēja virzienu Latvijā"], 0),

             ("Kurā gadījumā automašīnu NEDRĪKST uzskatīt par materiālu "
              "punktu?",
              ["braucot no Rīgas uz Liepāju",
               "iebraucot autostāvvietā starp divām citām mašīnām",
               "aprēķinot vidējo ātrumu 100 km garā ceļā",
               "atzīmējot tās atrašanās vietu Latvijas kartē"], 1),
         ]},

        # ------------------------------------------------ 3. relatīvā kustība
        {"sr": "Skaidro kustības relativitāti un izvēlas atskaites ķermeni",
         "stunda": "1.5.",
         "jautajumi": [
             ("Pasažieris sēž kustīgā vilcienā. Pret ko viņš atrodas miera "
              "stāvoklī?",
              ["pret sliedēm", "pret staciju", "pret vagonu",
               "pret ceļmalas kokiem"], 2),

             ("Kāpēc saka, ka mehāniskā kustība ir relatīva?",
              ["jo ātrums vienmēr mainās",
               "jo kustības apraksts ir atkarīgs no atskaites ķermeņa izvēles",
               "jo trajektorija vienmēr ir līkne",
               "jo ceļš ir vektoriāls lielums"], 1),

             ("Divi vilcieni brauc pa blakus sliedēm vienā virzienā, katrs ar "
              "ātrumu 20 m/s. Cik liels ir viena vilciena ātrums pret otru?",
              ["0 m/s", "10 m/s", "20 m/s", "40 m/s"], 0),
         ]},

        # --------------------------------------- 4. trajektorija un ceļš
        {"sr": "Atšķir trajektoriju, ceļu un pārvietojumu",
         "stunda": "1.6.",
         "jautajumi": [
             ("Kas ir trajektorija?",
              ["nobrauktā ceļa garums",
               "līnija, pa kuru ķermenis pārvietojas",
               "vektors no sākuma punkta uz beigu punktu",
               "ātruma izmaiņa laikā"], 1),

             ("Ar ko pārvietojums atšķiras no ceļa?",
              ["pārvietojums ir vektors, bet ceļš — skalārs lielums",
               "pārvietojums vienmēr ir lielāks nekā ceļš",
               "ceļš ir vektors, bet pārvietojums — skalārs lielums",
               "tie ir viens un tas pats lielums"], 0),

             ("Kurā gadījumā ceļš ir vienāds ar pārvietojuma moduli?",
              ["kustībā pa riņķa līniju",
               "taisnvirziena kustībā bez virziena maiņas",
               "atgriežoties sākuma punktā",
               "jebkurā kustībā"], 1),
         ]},

        # ------------------------------------------- 5. pārvietojuma aprēķins
        {"sr": "Nosaka pārvietojuma moduli vienkāršā trajektorijā",
         "stunda": "1.6.",
         "jautajumi": [
             ("Ķermenis veic pusapli pa riņķa līniju, kuras rādiuss ir 10 m. "
              "Cik liels ir pārvietojuma modulis?",
              ["10 m", "20 m", "31 m", "63 m"], 1),

             ("Tūrists noiet 3 km uz austrumiem un pēc tam 4 km uz "
              "ziemeļiem. Cik liels ir viņa pārvietojuma modulis?",
              ["1 km", "5 km", "7 km", "12 km"], 1),

             ("Skrējējs noskrien pilnu apli pa 400 m stadiona celiņu. Cik "
              "liels ir viņa pārvietojuma modulis?",
              ["0 m", "127 m", "200 m", "400 m"], 0),
         ]},

        # ----------------------------------------------- 6. mērvienību maiņa
        {"sr": "Pārvērš ātrumu no km/h uz m/s un otrādi",
         "stunda": "1.7.",
         "jautajumi": [
             ("Cik m/s ir 108 km/h?",
              ["10,8 m/s", "30 m/s", "39 m/s", "300 m/s"], 1),

             ("Cik km/h ir 15 m/s?",
              ["4,2 km/h", "25 km/h", "54 km/h", "150 km/h"], 2),

             ("Kurš no ātrumiem ir vislielākais?",
              ["36 km/h", "12 m/s", "0,6 km/min", "600 m/min"], 1),
         ]},

        # ------------------------------------------------ 7. sakarība v = s/t
        {"sr": "Lieto sakarību v = {s|t} vienmērīgā kustībā",
         "stunda": "1.7.",
         "jautajumi": [
             ("Ķermenis vienmērīgi nobrauc 60 m 4 s laikā. Cik liels ir tā "
              "ātrums?",
              ["0,067 m/s", "15 m/s", "64 m/s", "240 m/s"], 1),

             ("Velosipēdists brauc vienmērīgi ar ātrumu 5 m/s. Cik tālu viņš "
              "aizbrauks 3 minūtēs?",
              ["15 m", "36 m", "150 m", "900 m"], 3),

             ("Cik ilgā laikā automašīna, braucot vienmērīgi ar ātrumu "
              "72 km/h, veiks 3 km?",
              ["24 s", "41,7 s", "150 s", "216 s"], 2),
         ]},

        # -------------------------------------------- 8. kustības vienādojums
        {"sr": "Lieto kustības vienādojumu x = x₀ + v · t",
         "stunda": "1.8.",
         "jautajumi": [
             ("Kustības vienādojums ir x = 12 − 4t (SI vienībās). Kurā vietā "
              "ķermenis atrodas brīdī t = 2 s?",
              ["4 m", "8 m", "20 m", "−4 m"], 0),

             ("Ķermeņa kustību apraksta vienādojums x = −6 + 3t (SI "
              "vienībās). Kāda ir sākuma koordināta un ātrums?",
              ["x₀ = 3 m;  v = −6 m/s",
               "x₀ = −6 m;  v = 3 m/s",
               "x₀ = 6 m;  v = 3 m/s",
               "x₀ = −6 m;  v = −3 m/s"], 1),

             ("Ķermenis sāk kustību no koordinātas x₀ = 5 m ar ātrumu 2 m/s "
              "pretēji x ass virzienam. Kāds ir tā kustības vienādojums?",
              ["x = 5 + 2t", "x = 5 − 2t", "x = −5 + 2t", "x = 2 + 5t"], 1),
         ]},

        # ------------------------------------------------------- 9. grafiki
        {"sr": "Lasa vienmērīgas kustības v(t) un x(t) grafikus",
         "stunda": "1.8., 1.9.",
         "jautajumi": [
             ("Kāds izskatās vienmērīgas taisnvirziena kustības v(t) "
              "grafiks?",
              ["taisne caur koordinātu sākumpunktu",
               "horizontāla taisne",
               "parabola",
               "lauzta līnija"], 1),

             ("Ko x(t) grafikā parāda taisnes slīpums?",
              ["nobraukto ceļu", "ķermeņa ātrumu", "kustības laiku",
               "sākuma koordinātu"], 1),

             ("Kā v(t) grafikā nosaka nobraukto ceļu?",
              ["līknes garumu", "laukumu zem grafika", "līnijas slīpumu",
               "krustpunktu ar laika asi"], 1),
         ]},

        # ---------------------------------------- 10. vidējais ātrums (rēķins)
        {"sr": "Aprēķina vidējo ātrumu vairāku posmu kustībā",
         "stunda": "1.10.",
         "jautajumi": [
             ("Ķermenis pirmos 100 m veic 20 s, nākamos 100 m — 30 s. Cik "
              "liels ir vidējais ātrums?",
              ["3,3 m/s", "4,0 m/s", "4,2 m/s", "5,0 m/s"], 1),

             ("Automašīna 2 h brauc ar ātrumu 60 km/h un pēc tam 1 h ar "
              "ātrumu 90 km/h. Cik liels ir vidējais ātrums?",
              ["65 km/h", "70 km/h", "75 km/h", "80 km/h"], 1),

             ("Tūrists 3 km noiet ar ātrumu 6 km/h un nākamos 3 km — ar "
              "ātrumu 3 km/h. Cik liels ir vidējais ātrums?",
              ["3,5 km/h", "4 km/h", "4,5 km/h", "5 km/h"], 1),
         ]},

        # -------------------------------------- 11. vidējais ātrums (izpratne)
        {"sr": "Pamato, kāpēc vidējais ātrums nav ātrumu vidējais "
               "aritmētiskais",
         "stunda": "1.10.",
         "jautajumi": [
             ("Kāpēc vidējo ātrumu nedrīkst rēķināt kā posmu ātrumu vidējo "
              "aritmētisko?",
              ["jo ātrums ir vektoriāls lielums",
               "jo mērvienības nesakrīt",
               "jo ceļš vienmēr ir lielāks par pārvietojumu",
               "jo posmos pavadītais laiks parasti ir atšķirīgs"], 3),

             ("Kā aprēķina vidējo ātrumu?",
              ["posmu ātrumus saskaita",
               "visu ceļu dala ar visu kustības laiku",
               "lielāko ātrumu dala ar mazāko",
               "pārvietojumu dala ar posmu skaitu"], 1),

             ("Ķermenis pusi ceļa veic ar ātrumu 10 m/s, otru pusi — ar "
              "ātrumu 30 m/s. Cik liels ir vidējais ātrums?",
              ["12 m/s", "15 m/s", "20 m/s", "25 m/s"], 1),
         ]},

        # --------------------------------------------------- 12. satikšanās
        {"sr": "Nosaka divu ķermeņu satikšanās laiku un vietu",
         "stunda": "1.9.",
         "jautajumi": [
             ("Divu ķermeņu kustību apraksta x₁ = 2t un x₂ = 30 − 3t (SI "
              "vienībās). Pēc cik ilga laika tie satiksies?",
              ["3 s", "5 s", "6 s", "15 s"], 2),

             ("Divu ķermeņu kustību apraksta x₁ = 10 + 4t un x₂ = 40 + t (SI "
              "vienībās). Pēc cik ilga laika pirmais ķermenis panāks otro?",
              ["5 s", "8 s", "10 s", "30 s"], 2),

             ("Divu ķermeņu x(t) grafiki krustojas punktā t = 4 s; x = 12 m. "
              "Ko tas nozīmē?",
              ["abiem ķermeņiem ir vienāds ātrums",
               "ceturtajā sekundē abi ķermeņi atrodas vienā vietā",
               "abi ķermeņi apstājas",
               "abi ķermeņi ir veikuši vienādu ceļu"], 1),
         ]},
    ],
}
