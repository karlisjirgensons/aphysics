# -*- coding: utf-8 -*-
"""1. temats. B daļa: 1.8.-1.13. stunda (grafiki, mērījumi, pētījums)."""

from fiz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN     # noqa: F401
from fiz_t01a import TEMATS, KICKER, KURSS, MAPE              # noqa: F401

STUNDAS = [

dict(
    nr="1.8", virsraksts="Kustības vienādojums un grafiki",
    jautajums="Ko par kustību pastāsta grafiks?",
    apaksraksts="x = x₀ + vt · Grafiks x(t) · Grafiks v(t)",
    merkis="Iemācīties pierakstīt vienmērīgas kustības vienādojumu un "
           "saistīt to ar x(t) un v(t) grafikiem.",
    protu=["pierakstīt kustības vienādojumu x = x₀ + vt;",
           "no vienādojuma nolasīt x₀ un v;",
           "atpazīt kustības virzienu pēc grafika slīpuma;",
           "uzzīmēt x(t) grafiku pēc vienādojuma."],
    atkartojums="1.7. stundā: v = s/t. Ja pievienojam sākuma koordinātu, "
                "iegūstam vienādojumu, kas pasaka ķermeņa vietu jebkurā "
                "brīdī.",
    uzdevumu_apraksts="Kustības vienādojums un grafika lasīšana",
    teorija=[
        ("Kustības vienādojums", [
            ("formula", "VIENMĒRĪGA KUSTĪBA",
             "x = x₀ + vₓ · t",
             "x₀ - sākuma koordināta (kur ķermenis bija, kad t = 0); "
             "vₓ - ātruma projekcija ar zīmi; x - koordināta laikā t.",
             GOLD),
            ("kartitas", [
                ("x₀", BLUE,
                 ["Grafika krustpunkts ar y asi.",
                  "Var būt pozitīva, negatīva vai nulle."]),
                ("vₓ > 0", GREEN,
                 ["Grafiks x(t) aug.",
                  "Kustība ass pozitīvajā virzienā."]),
                ("vₓ < 0", RED,
                 ["Grafiks x(t) dilst.",
                  "Kustība pretēji asij."]),
            ]),
        ]),
        ("Divi grafiki - divas atbildes", [
            ("divi",
             ("GRAFIKS  x(t)", BLUE,
              ["Taisne; slīpums = ātrums vₓ.",
               "Stāvāka taisne - lielāks ātrums.",
               "Horizontāla taisne - miers (v = 0).",
               "Krustpunkti - ķermeņi satiekas."]),
             ("GRAFIKS  v(t)", GREEN,
              ["Horizontāla taisne (v = const).",
               "Laukums zem taisnes = ceļš.",
               "Virs t ass - kustība uz priekšu.",
               "Zem t ass - kustība atpakaļ."])),
            ("panelis", "KĀ NOLASĪT ĀTRUMU NO x(t)",
             ["Izvēlas divus ērtus punktus uz taisnes un rēķina:",
              "vₓ = (x₂ − x₁)/(t₂ − t₁)",
              "Vienības noteikti pieraksta - no grafika ass."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Vienādojuma lasīšana",
             teksts="Dots kustības vienādojums x = 20 − 4t  (m; s).\n"
                    "Nosaki sākuma koordinātu, ātrumu un virzienu!",
             dots=["x = 20 − 4t"],
             jaaprekina=["x₀ = ?", "vₓ = ?", "virziens = ?"],
             formulas=["x = x₀ + vₓt"],
             aprekins=["1)  x₀ = 20 m",
                       "2)  vₓ = −4 m/s",
                       "3)  Mīnuss → kustība pretēji x asij"],
             atbilde="x₀ = 20 m ;  vₓ = −4 m/s ;  kustība pretēji asij.",
             piezime="Zīme pie t koeficienta vienmēr rāda virzienu."),
        dict(nr=2, virsraksts="Koordināta dotā brīdī",
             teksts="x = −6 + 3t  (m; s).\n"
                    "Kur ķermenis atradīsies pēc 5 s un kad tas šķērsos\n"
                    "koordinātu sākumpunktu?",
             dots=["x₀ = −6 m", "vₓ = 3 m/s", "t = 5 s"],
             jaaprekina=["x(5 s) = ?", "t (x = 0) = ?"],
             formulas=["x = x₀ + vₓt", "0 = x₀ + vₓt"],
             aprekins=["1)  x = −6 + 3·5 = −6 + 15 = 9 m",
                       "2)  0 = −6 + 3t → 3t = 6",
                       "3)  t = 2,0 s"],
             atbilde="x = 9 m ;   sākumpunktu šķērso pēc 2,0 s.",
             piezime="Nulles vietu atrod, pielīdzinot koordinātu nullei."),
        dict(nr=3, virsraksts="Ātrums no grafika",
             teksts="Grafikā x(t) taisne iet caur punktiem (0 s; 4 m) un\n"
                    "(8 s; 28 m). Aprēķini ātrumu un uzraksti "
                    "vienādojumu!",
             dots=["(t₁; x₁) = (0 s; 4 m)", "(t₂; x₂) = (8 s; 28 m)"],
             jaaprekina=["vₓ = ?", "x(t) = ?"],
             formulas=["vₓ = (x₂ − x₁)/(t₂ − t₁)", "x = x₀ + vₓt"],
             aprekins=["1)  Δx = 28 − 4 = 24 m",
                       "2)  Δt = 8 − 0 = 8 s",
                       "3)  vₓ = 24 : 8 = 3,0 m/s ;  x = 4 + 3t"],
             atbilde="vₓ = 3,0 m/s ;   x = 4 + 3t  (m; s)",
             piezime="x₀ nolasa krustpunktā ar x asi."),
        dict(nr=4, virsraksts="Ceļš no v(t) grafika",
             teksts="Grafikā v(t) ātrums ir nemainīgs 12 m/s no t = 0\n"
                    "līdz t = 15 s. Aprēķini ceļu!",
             dots=["v = 12 m/s", "t = 15 s"],
             jaaprekina=["s = ?"],
             formulas=["s = laukums zem v(t) grafika", "s = v · t"],
             aprekins=["1)  Laukums - taisnstūris",
                       "2)  s = 12 · 15",
                       "3)  s = 180 m"],
             atbilde="s = 180 m",
             piezime="Laukums zem v(t) grafika VIENMĒR ir ceļš - arī "
                     "nevienmērīgā kustībā."),
        dict(nr=5, virsraksts="Vienādojuma sastādīšana",
             teksts="Ķermenis sāk kustību no punkta x₀ = −15 m un kustas "
                    "gar\nx asi ar 5,0 m/s. Uzraksti vienādojumu un "
                    "atrodi x pēc 6,0 s!",
             dots=["x₀ = −15 m", "vₓ = 5,0 m/s", "t = 6,0 s"],
             jaaprekina=["x(t) = ?", "x(6,0 s) = ?"],
             formulas=["x = x₀ + vₓt"],
             aprekins=["1)  x = −15 + 5t  (m; s)",
                       "2)  x = −15 + 5 · 6,0",
                       "3)  x = −15 + 30 = 15 m"],
             atbilde="x = −15 + 5t  (m; s) ;   x(6,0 s) = 15 m",
             piezime="Vienādojumā vienmēr norāda mērvienības iekavās - "
                     "citādi tas nav pilnīgs."),
        dict(nr=6, virsraksts="Ceļš un pārvietojums no v(t)",
             teksts="v(t) grafikā vₓ = 6,0 m/s no 0 līdz 10 s un\n"
                    "vₓ = −4,0 m/s no 10 līdz 20 s. Aprēķini ceļu un "
                    "pārvietojumu!",
             dots=["v₁ = 6,0 m/s, t₁ = 10 s", "v₂ = −4,0 m/s, t₂ = 10 s"],
             jaaprekina=["s = ?", "sₓ = ?"],
             formulas=["s = |v₁|t₁ + |v₂|t₂", "sₓ = v₁t₁ + v₂t₂"],
             aprekins=["1)  s₁ = 6,0 · 10 = 60 m ;  s₂ = 4,0 · 10 = 40 m",
                       "2)  s = 60 + 40 = 100 m",
                       "3)  sₓ = 60 − 40 = 20 m"],
             atbilde="s = 100 m ;   sₓ = 20 m",
             piezime="Laukums zem ass ir negatīvs pārvietojumam, bet "
                     "ceļam to skaita pēc moduļa."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Vienmērīgas kustības vienādojums: x = x₀ + vₓt.",
            "x(t) grafika slīpums ir ātrums.",
            "Laukums zem v(t) grafika ir ceļš.",
            "Zīme pie vₓ rāda kustības virzienu.",
        ],
        majasdarbs=[
            "x = 15 − 5t. Nosaki x₀, vₓ un kad ķermenis būs punktā x = 0.",
            "Taisne x(t) iet caur (2 s; 10 m) un (6 s; 2 m). Uzraksti "
            "vienādojumu.",
            "v = 8,0 m/s, t no 0 līdz 12 s. Aprēķini ceļu no v(t) "
            "grafika.",
        ],
        pasvertejums=["Protu pierakstīt vienādojumu",
                      "Protu nolasīt x₀ un v",
                      "Protu lasīt x(t) grafiku",
                      "Protu atrast ceļu no v(t)"],
        nakama="Nākamā stunda: grafiku lasīšana un satikšanās uzdevumi."),
),

dict(
    nr="1.9", virsraksts="Grafiku lasīšana",
    jautajums="Kur satiksies divi ķermeņi?",
    apaksraksts="Krustpunkts · Divi vienādojumi · Grafiskais risinājums",
    merkis="Iemācīties risināt satikšanās uzdevumus gan grafiski, gan "
           "ar vienādojumu sistēmu.",
    protu=["uzrakstīt vienādojumus diviem ķermeņiem;",
           "atrast satikšanās laiku un vietu;",
           "interpretēt grafiku krustpunktu;",
           "pārbaudīt atbildi abās metodēs."],
    atkartojums="1.8. stundā: x = x₀ + vt. Ja kustas divi ķermeņi, "
                "vienādojumi ir divi, un satikšanās nozīmē x₁ = x₂.",
    uzdevumu_apraksts="Satikšanās, panākšana un grafiku krustpunkti",
    teorija=[
        ("Satikšanās nosacījums", [
            ("formula", "DIVI ĶERMEŅI SATIEKAS",
             "x₁ = x₂        x₀₁ + v₁t = x₀₂ + v₂t",
             "Satikšanās brīdī abu ķermeņu koordinātas ir vienādas. No "
             "šī vienādojuma atrod laiku t, pēc tam - vietu x.", GOLD),
            ("kartitas", [
                ("PRETIM", RED,
                 ["Ātrumiem pretējas zīmes.",
                  "Attālums samazinās ātri.",
                  "t = (x₀₂ − x₀₁)/(v₁ + v₂)"]),
                ("PANĀKŠANA", BLUE,
                 ["Ātrumiem viena zīme.",
                  "Panāk, ja v₁ > v₂.",
                  "t = Δx/(v₁ − v₂)"]),
                ("GRAFISKI", GREEN,
                 ["Krustpunkts x(t) grafikā.",
                  "Abscisa - laiks.",
                  "Ordināta - vieta."]),
            ]),
        ]),
        ("Risinājuma soļi", [
            ("panelis", "KĀ RISINĀT SATIKŠANĀS UZDEVUMU",
             ["1) Izvēlas asi un sākumpunktu.  2) Pieraksta abus "
              "vienādojumus ar pareizām zīmēm.  3) Pielīdzina x₁ = x₂ un "
              "atrod t.  4) Ievieto t vienā vienādojumā un atrod x.  "
              "5) Pārbauda ticamību."], NAVY),
            ("tabula",
             ["Situācija", "Ātrumu zīmes", "Laiks līdz satikšanai"],
             [["Brauc pretim", "v₁ > 0, v₂ < 0", "t = L / (v₁ + |v₂|)"],
              ["Panāk", "v₁ > 0, v₂ > 0", "t = L / (v₁ − v₂)"],
              ["Attālinās", "v₁ > 0, v₂ < 0", "nesatiekas"]],
             [5.20, 4.10, 3.93]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Brauc pretim",
             teksts="Divas automašīnas izbrauc vienlaikus pretim viena "
                    "otrai\nno punktiem, kas ir 180 km attālumā, ar "
                    "ātrumiem\n60 km/h un 80 km/h. Pēc cik ilga laika tās "
                    "satiksies?",
             dots=["L = 180 km", "v₁ = 60 km/h", "v₂ = 80 km/h"],
             jaaprekina=["t = ?", "x = ?"],
             formulas=["x₁ = 60t", "x₂ = 180 − 80t", "x₁ = x₂"],
             aprekins=["1)  60t = 180 − 80t",
                       "2)  140t = 180 → t = 1,29 h ≈ 1 h 17 min",
                       "3)  x = 60 · 1,29 ≈ 77 km no pirmās"],
             atbilde="t ≈ 1,3 h ;   x ≈ 77 km no pirmās automašīnas.",
             piezime="Pārbaude: 80 · 1,29 ≈ 103 km;  77 + 103 = 180 ✔"),
        dict(nr=2, virsraksts="Panākšana",
             teksts="Kravas auto brauc 60 km/h. Pēc 30 min no tās pašas\n"
                    "vietas izbrauc vieglā automašīna ar 90 km/h.\n"
                    "Pēc cik ilga laika tā panāks kravas auto?",
             dots=["v₁ = 60 km/h", "v₂ = 90 km/h", "Δt = 0,50 h"],
             jaaprekina=["t = ?"],
             formulas=["Sākuma atstatums L = v₁·Δt",
                       "t = L / (v₂ − v₁)"],
             aprekins=["1)  L = 60 · 0,50 = 30 km",
                       "2)  Δv = 90 − 60 = 30 km/h",
                       "3)  t = 30 : 30 = 1,0 h"],
             atbilde="t = 1,0 h pēc vieglās automašīnas izbraukšanas.",
             piezime="Panākšanā izšķir ātrumu STARPĪBA."),
        dict(nr=3, virsraksts="Grafiku krustpunkts",
             teksts="Doti vienādojumi x₁ = 5 + 2t un x₂ = 45 − 3t  (m; s).\n"
                    "Atrodi satikšanās laiku un vietu!",
             dots=["x₁ = 5 + 2t", "x₂ = 45 − 3t"],
             jaaprekina=["t = ?", "x = ?"],
             formulas=["x₁ = x₂"],
             aprekins=["1)  5 + 2t = 45 − 3t",
                       "2)  5t = 40 → t = 8,0 s",
                       "3)  x = 5 + 2·8 = 21 m"],
             atbilde="t = 8,0 s ;   x = 21 m",
             piezime="Pārbaude otrā vienādojumā: 45 − 3·8 = 21 ✔"),
        dict(nr=4, virsraksts="Vai panāks",
             teksts="x₁ = 10 + 4t un x₂ = 100 + 4t  (m; s).\n"
                    "Vai pirmais ķermenis panāks otro? Pamato!",
             dots=["v₁ = 4 m/s", "v₂ = 4 m/s", "Δx = 90 m"],
             jaaprekina=["Vai satiksies?"],
             formulas=["x₁ = x₂ → 10 + 4t = 100 + 4t"],
             aprekins=["1)  10 + 4t = 100 + 4t",
                       "2)  10 = 100 - nav risinājuma",
                       "3)  Ātrumi vienādi → attālums nemainās"],
             atbilde="Nepanāks: ātrumi ir vienādi, attālums paliek 90 m.",
             piezime="Ja vienādojumam nav risinājuma, tam ir fizikāla "
                     "jēga."),
        dict(nr=5, virsraksts="Attālums starp automašīnām",
             teksts="x₁ = 5 + 10t un x₂ = 65 + 5t  (m; s).\n"
                    "Pēc cik ilga laika attālums starp tām būs 20 m?",
             dots=["x₁ = 5 + 10t", "x₂ = 65 + 5t", "Δx = 20 m"],
             jaaprekina=["t = ?"],
             formulas=["Δx = x₂ − x₁"],
             aprekins=["1)  Δx = (65 + 5t) − (5 + 10t) = 60 − 5t",
                       "2)  60 − 5t = 20 → 5t = 40",
                       "3)  t = 8,0 s"],
             atbilde="t = 8,0 s",
             piezime="Sākumā attālums bija 60 m un samazinās par 5 m "
                     "katrā sekundē."),
        dict(nr=6, virsraksts="Trīs posmi x(t) grafikā",
             teksts="x(t) grafikā: no 0 līdz 10 s x aug no 0 līdz 30 m;\n"
                    "no 10 līdz 20 s x = 30 m; no 20 līdz 30 s x krīt "
                    "līdz 0.\nAtrodi ātrumu katrā posmā un vidējo "
                    "ātrumu!",
             dots=["I: 0 → 30 m, 10 s", "II: 30 m, 10 s",
                   "III: 30 → 0 m, 10 s"],
             jaaprekina=["v₁, v₂, v₃ = ?", "v(vid) = ?"],
             formulas=["vₓ = Δx/Δt", "v(vid) = s / t"],
             aprekins=["1)  v₁ = 30 : 10 = 3,0 m/s ;  v₂ = 0",
                       "2)  v₃ = (0 − 30) : 10 = −3,0 m/s",
                       "3)  s = 30 + 0 + 30 = 60 m ;  "
                       "v(vid) = 60 : 30 = 2,0 m/s"],
             atbilde="v₁ = 3,0 m/s ;  v₂ = 0 ;  v₃ = −3,0 m/s ;  "
                     "v(vid) = 2,0 m/s",
             piezime="Horizontāls posms x(t) grafikā nozīmē mieru, "
                     "nevis vienmērīgu kustību."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Satikšanās nosacījums: x₁ = x₂.",
            "Grafiski satikšanās ir x(t) grafiku krustpunkts.",
            "Pretim - ātrumus saskaita; panākot - atņem.",
            "Atbildi vienmēr pārbauda otrā vienādojumā.",
        ],
        majasdarbs=[
            "x₁ = 2 + 6t, x₂ = 62 − 4t. Atrodi t un x.",
            "Divi velosipēdisti 24 km attālumā brauc pretim ar 12 km/h "
            "un 18 km/h. Kad satiksies?",
            "Vilciens 80 km/h panāk kravas auto 50 km/h, kas ir 15 km "
            "priekšā. Cik ilgi?",
        ],
        pasvertejums=["Protu uzrakstīt abus vienādojumus",
                      "Protu atrast satikšanās laiku",
                      "Protu lasīt krustpunktu grafikā",
                      "Protu pārbaudīt atbildi"],
        nakama="Nākamā stunda: vidējais ātrums."),
),

dict(
    nr="1.10", virsraksts="Vidējais ātrums",
    jautajums="Kāds ir ātrums, ja tas mainās?",
    apaksraksts="v(vid) = s(kop)/t(kop) · Biežākā kļūda · Momentānais "
                "ātrums",
    merkis="Iemācīties pareizi aprēķināt vidējo ātrumu un saprast, kāpēc "
           "to nedrīkst rēķināt kā ātrumu vidējo aritmētisko.",
    protu=["definēt vidējo ātrumu;",
           "aprēķināt to vairāku posmu kustībā;",
           "paskaidrot, kāpēc vidējais aritmētiskais parasti ir "
           "nepareizs;",
           "atšķirt vidējo ātrumu no momentānā."],
    atkartojums="1.7. stundā ātrums bija nemainīgs. Reālā kustībā tas "
                "mainās, tāpēc vajadzīgs vidējais ātrums.",
    uzdevumu_apraksts="Vidējais ātrums vairākos posmos",
    teorija=[
        ("Kā rēķina pareizi", [
            ("formula", "VIDĒJAIS ĀTRUMS",
             "v(vid) = s(kopējais) / t(kopējais)",
             "Vienmēr: viss ceļš dalīts ar visu laiku. Nekad nesaskaita "
             "ātrumus un nedala ar posmu skaitu, ja posmu laiki "
             "atšķiras.", GOLD),
            ("divi",
             ("PAREIZI", GREEN,
              ["1) Aprēķina katra posma ceļu.",
               "2) Aprēķina katra posma laiku.",
               "3) v(vid) = Σs / Σt.",
               "Der jebkurai kustībai."]),
             ("BIEŽĀKĀ KĻŪDA", RED,
              ["v(vid) = (v₁ + v₂)/2.",
               "Der TIKAI tad, ja abu posmu LAIKI ir vienādi.",
               "Ja vienādi ir CEĻI - atbilde ir nepareiza."])),
        ]),
        ("Vidējais un momentānais", [
            ("tabula",
             ["Lielums", "Ko raksturo", "Kur redzams"],
             [["Momentānais ātrums", "Ātrums vienā brīdī", "Spidometrā"],
              ["Vidējais ātrums", "Visu braucienu kopā",
               "s/t aprēķinā"],
              ["Vidējais ātruma modulis", "Ceļš dalīts ar laiku",
               "Navigācijas lietotnē"]],
             [5.20, 4.60, 3.43]),
            ("panelis", "PIEMĒRS AR SKAITĻIEM",
             ["Puse ceļa ar 40 km/h, otra puse ar 60 km/h. Vidējais "
              "aritmētiskais dotu 50 km/h, bet pareizā atbilde ir "
              "48 km/h - lēnajā posmā pavadīts vairāk laika."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Divi posmi ar dotiem laikiem",
             teksts="Automašīna 2,0 h brauc ar 90 km/h un 1,0 h ar "
                    "60 km/h.\nAprēķini vidējo ātrumu!",
             dots=["v₁ = 90 km/h, t₁ = 2,0 h", "v₂ = 60 km/h, t₂ = 1,0 h"],
             jaaprekina=["v(vid) = ?"],
             formulas=["s = v·t", "v(vid) = (s₁ + s₂)/(t₁ + t₂)"],
             aprekins=["1)  s₁ = 90·2,0 = 180 km ;  s₂ = 60·1,0 = 60 km",
                       "2)  s = 240 km ;  t = 3,0 h",
                       "3)  v(vid) = 240 : 3,0 = 80 km/h"],
             atbilde="v(vid) = 80 km/h",
             piezime="Šeit vidējais aritmētiskais (75) būtu nepareizs."),
        dict(nr=2, virsraksts="Vienādi ceļa posmi",
             teksts="Pusi ceļa automašīna brauc ar 40 km/h, otru pusi ar\n"
                    "60 km/h. Aprēķini vidējo ātrumu!",
             dots=["v₁ = 40 km/h", "v₂ = 60 km/h", "s₁ = s₂ = s/2"],
             jaaprekina=["v(vid) = ?"],
             formulas=["t = s/v", "v(vid) = s / (t₁ + t₂)"],
             aprekins=["1)  Pieņem s = 120 km → s₁ = s₂ = 60 km",
                       "2)  t₁ = 60:40 = 1,5 h ;  t₂ = 60:60 = 1,0 h",
                       "3)  v(vid) = 120 : 2,5 = 48 km/h"],
             atbilde="v(vid) = 48 km/h",
             piezime="Atbilde nav atkarīga no izvēlētā s - pārbaudi ar "
                     "citu skaitli!"),
        dict(nr=3, virsraksts="Ar apstāšanos",
             teksts="Velosipēdists 20 min brauc ar 18 km/h, tad 10 min\n"
                    "atpūšas. Aprēķini vidējo ātrumu visā laikā!",
             dots=["v₁ = 18 km/h", "t₁ = 20 min", "t₂ = 10 min, v₂ = 0"],
             jaaprekina=["v(vid) = ?"],
             formulas=["s = v·t", "v(vid) = s / t(kop)"],
             aprekins=["1)  t₁ = 1/3 h → s = 18 · 1/3 = 6,0 km",
                       "2)  t(kop) = 30 min = 0,50 h",
                       "3)  v(vid) = 6,0 : 0,50 = 12 km/h"],
             atbilde="v(vid) = 12 km/h",
             piezime="Atpūtas laiks arī ietilpst kopējā laikā."),
        dict(nr=4, virsraksts="Vidējais ātrums un pārvietojums",
             teksts="Skrējējs noskrien 400 m apli 80 s laikā un "
                    "atgriežas\nstartā. Aprēķini vidējo ātruma moduli un "
                    "vidējo ātrumu pēc pārvietojuma!",
             dots=["s = 400 m", "t = 80 s", "|s⃗| = 0"],
             jaaprekina=["v(vid) pēc ceļa = ?", "v(vid) pēc s⃗ = ?"],
             formulas=["v = s/t", "v⃗(vid) = s⃗/t"],
             aprekins=["1)  v = 400 : 80 = 5,0 m/s",
                       "2)  |s⃗| = 0",
                       "3)  |v⃗(vid)| = 0 : 80 = 0 m/s"],
             atbilde="Pēc ceļa 5,0 m/s ;   pēc pārvietojuma 0 m/s.",
             piezime="Eksāmenā vienmēr precizē, kurš vidējais ātrums "
                     "domāts."),
        dict(nr=5, virsraksts="Trīs posmi",
             teksts="Autobuss veic 10 km 30 min laikā, 5 km 10 min "
                    "laikā un\n15 km 20 min laikā. Aprēķini vidējo "
                    "ātrumu!",
             dots=["s₁ = 10 km, t₁ = 30 min", "s₂ = 5 km, t₂ = 10 min",
                   "s₃ = 15 km, t₃ = 20 min"],
             jaaprekina=["v(vid) = ?"],
             formulas=["v(vid) = (s₁ + s₂ + s₃)/(t₁ + t₂ + t₃)"],
             aprekins=["1)  s = 10 + 5 + 15 = 30 km",
                       "2)  t = 30 + 10 + 20 = 60 min = 1,0 h",
                       "3)  v(vid) = 30 : 1,0 = 30 km/h"],
             atbilde="v(vid) = 30 km/h ≈ 8,3 m/s",
             piezime="Vidējo ātrumu vienmēr rēķina kā KOPĒJO ceļu "
                     "dalītu ar KOPĒJO laiku."),
        dict(nr=6, virsraksts="Nezināmais otrais ātrums",
             teksts="Pirmo pusi ceļa automašīna brauc ar 40 km/h. Ar "
                    "kādu\nātrumu jābrauc otrā puse, lai vidējais "
                    "ātrums būtu 60 km/h?",
             dots=["v₁ = 40 km/h", "v(vid) = 60 km/h", "s₁ = s₂ = s/2"],
             jaaprekina=["v₂ = ?"],
             formulas=["t = s / v(vid)", "t = t₁ + t₂"],
             aprekins=["1)  Pieņem s = 120 km → t = 120 : 60 = 2,0 h",
                       "2)  t₁ = 60 : 40 = 1,5 h → t₂ = 0,50 h",
                       "3)  v₂ = 60 : 0,50 = 120 km/h"],
             atbilde="v₂ = 120 km/h",
             piezime="Trīskāršs ātrums otrā pusē - tāpēc vidējais "
                     "ātrums nekad nav vidējais aritmētiskais."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "v(vid) = viss ceļš dalīts ar visu laiku.",
            "Vidējo aritmētisko drīkst lietot tikai pie vienādiem laikiem.",
            "Apstāšanās laiks arī ietilpst kopējā laikā.",
            "Momentānais ātrums ir spidometra rādījums.",
        ],
        majasdarbs=[
            "1,5 h ar 80 km/h un 0,50 h ar 40 km/h. Aprēķini v(vid).",
            "Pusi ceļa ar 30 km/h, pusi ar 70 km/h. Aprēķini v(vid).",
            "Paskaidro, kāpēc atbilde 2. uzdevumā nav 50 km/h.",
        ],
        pasvertejums=["Protu aprēķināt vidējo ātrumu",
                      "Protu izvairīties no tipiskās kļūdas",
                      "Protu ņemt vērā apstāšanās laiku",
                      "Protu atšķirt vidējo un momentāno"],
        nakama="Nākamā stunda: mērierīces un mērījumu kļūdas."),
),

dict(
    nr="1.11", virsraksts="Mērierīces un mērījumu kļūdas",
    jautajums="Cik precīzs ir mērījums?",
    apaksraksts="Iedaļas vērtība · Absolūtā kļūda · Relatīvā kļūda",
    merkis="Iemācīties noteikt mērierīces iedaļas vērtību, pierakstīt "
           "mērījuma rezultātu ar kļūdu un aprēķināt relatīvo kļūdu.",
    protu=["noteikt mērierīces iedaļas vērtību;",
           "novērtēt absolūto kļūdu;",
           "pierakstīt rezultātu formā x ± Δx;",
           "aprēķināt relatīvo kļūdu procentos."],
    atkartojums="Līdz šim skaitļus pieņēmām par precīziem. Reālā "
                "mērījumā vienmēr ir kļūda - un to jāprot novērtēt.",
    uzdevumu_apraksts="Iedaļas vērtība, absolūtā un relatīvā kļūda",
    teorija=[
        ("Mērījuma kļūdas", [
            ("kartitas", [
                ("IEDAĻAS VĒRTĪBA  C", BLUE,
                 ["Divu blakus svītriņu starpība.",
                  "C = (a₂ − a₁) / n",
                  "n - iedaļu skaits starp tām."]),
                ("ABSOLŪTĀ KĻŪDA  Δx", RED,
                 ["Parasti puse iedaļas vērtības.",
                  "Δx = C / 2",
                  "Mērvienība - tāda pati kā lielumam."]),
                ("RELATĪVĀ KĻŪDA  δ", GOLD,
                 ["δ = Δx / x · 100 %",
                  "Bez mērvienības.",
                  "Rāda mērījuma kvalitāti."]),
            ]),
            ("formula", "REZULTĀTA PIERAKSTS",
             "x = (x(izmērītais) ± Δx)  vienība",
             "Piemērs:  l = (24,5 ± 0,5) cm. Kļūdu noapaļo līdz vienam "
             "zīmīgam ciparam, un rezultātu - līdz tai pašai vietai.",
             GOLD),
        ]),
        ("Tiešā un netiešā mērīšana", [
            ("divi",
             ("TIEŠĀ MĒRĪŠANA", BLUE,
              ["Lielumu nolasa tieši no ierīces.",
               "Garums ar lineālu, laiks ar hronometru.",
               "Δx ≈ pusiedaļa (vai ierīces pase)."]),
             ("NETIEŠĀ MĒRĪŠANA", GREEN,
              ["Lielumu aprēķina no citiem.",
               "Piemērs: v = s/t; ρ = m/V.",
               "Relatīvās kļūdas SASKAITA: "
               "δv = δs + δt."])),
            ("panelis", "PRAKTISKS NOTEIKUMS",
             ["Ja mēra ar lineālu (C = 1 mm), Δl = 0,5 mm. Mērot 5 cm "
              "garumu, δ = 1 %, bet mērot 5 mm - δ = 10 %. Tāpēc mērīt "
              "izdevīgi pēc iespējas lielākus lielumus."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Iedaļas vērtība",
             teksts="Uz mērcilindra starp atzīmēm 100 ml un 200 ml ir\n"
                    "5 iedaļas. Nosaki iedaļas vērtību un absolūto kļūdu!",
             dots=["a₁ = 100 ml", "a₂ = 200 ml", "n = 5"],
             jaaprekina=["C = ?", "ΔV = ?"],
             formulas=["C = (a₂ − a₁)/n", "ΔV = C/2"],
             aprekins=["1)  C = (200 − 100) : 5",
                       "2)  C = 20 ml",
                       "3)  ΔV = 20 : 2 = 10 ml"],
             atbilde="C = 20 ml ;   ΔV = 10 ml",
             piezime="Rupja mērierīce - lielai precizitātei tā neder."),
        dict(nr=2, virsraksts="Relatīvā kļūda",
             teksts="Ar lineālu (C = 1 mm) izmērīts garums 8,4 cm.\n"
                    "Pieraksti rezultātu ar kļūdu un aprēķini relatīvo "
                    "kļūdu!",
             dots=["l = 8,4 cm", "C = 1 mm = 0,1 cm"],
             jaaprekina=["Δl = ?", "δ = ?"],
             formulas=["Δl = C/2", "δ = Δl/l · 100 %"],
             aprekins=["1)  Δl = 0,1 : 2 = 0,05 cm",
                       "2)  l = (8,40 ± 0,05) cm",
                       "3)  δ = 0,05 : 8,4 · 100 % ≈ 0,6 %"],
             atbilde="l = (8,40 ± 0,05) cm ;   δ ≈ 0,6 %",
             piezime="Zem 1 % - ļoti labs mērījums lineālam."),
        dict(nr=3, virsraksts="Netiešā mērīšana",
             teksts="Izmērīts s = (12,0 ± 0,1) m un t = (4,0 ± 0,2) s.\n"
                    "Aprēķini ātrumu un tā relatīvo kļūdu!",
             dots=["s = 12,0 m, Δs = 0,1 m", "t = 4,0 s, Δt = 0,2 s"],
             jaaprekina=["v = ?", "δv = ?"],
             formulas=["v = s/t", "δv = δs + δt"],
             aprekins=["1)  v = 12,0 : 4,0 = 3,0 m/s",
                       "2)  δs = 0,1:12,0 = 0,8 % ;  δt = 0,2:4,0 = 5,0 %",
                       "3)  δv = 0,8 + 5,0 = 5,8 % → Δv ≈ 0,2 m/s"],
             atbilde="v = (3,0 ± 0,2) m/s ;   δ ≈ 6 %",
             piezime="Kopējo kļūdu nosaka neprecīzākais mērījums - "
                     "šeit laiks."),
        dict(nr=4, virsraksts="Kuru mērīt izdevīgāk",
             teksts="Ar to pašu lineālu (Δl = 0,5 mm) mēra 20 mm un\n"
                    "200 mm garumu. Salīdzini relatīvās kļūdas!",
             dots=["Δl = 0,5 mm", "l₁ = 20 mm", "l₂ = 200 mm"],
             jaaprekina=["δ₁ = ?", "δ₂ = ?"],
             formulas=["δ = Δl/l · 100 %"],
             aprekins=["1)  δ₁ = 0,5 : 20 · 100 % = 2,5 %",
                       "2)  δ₂ = 0,5 : 200 · 100 % = 0,25 %",
                       "3)  δ₁ ir 10 reižu lielāka"],
             atbilde="δ₁ = 2,5 % ;   δ₂ = 0,25 %",
             piezime="Tāpēc svārsta darbā mēra 20 svārstības, nevis "
                     "vienu."),
        dict(nr=5, virsraksts="Termometra iedaļas vērtība",
             teksts="Uz termometra starp atzīmēm 20 °C un 30 °C ir "
                    "5 iedaļas.\nNosaki iedaļas vērtību un mērījuma "
                    "absolūto kļūdu!",
             dots=["a₁ = 20 °C", "a₂ = 30 °C", "n = 5"],
             jaaprekina=["C = ?", "ΔT = ?"],
             formulas=["C = (a₂ − a₁)/n", "ΔT = C/2"],
             aprekins=["1)  C = (30 − 20) : 5",
                       "2)  C = 2 °C",
                       "3)  ΔT = 2 : 2 = 1 °C"],
             atbilde="C = 2 °C ;   ΔT = 1 °C",
             piezime="Rezultātu pieraksta ar tikpat cipariem aiz komata, "
                     "cik ir kļūdā."),
        dict(nr=6, virsraksts="Vidējā vērtība ar kļūdu",
             teksts="Izmērīti laiki 2,31 s; 2,34 s un 2,29 s.\n"
                    "Aprēķini vidējo vērtību, absolūto un relatīvo kļūdu!",
             dots=["t₁ = 2,31 s", "t₂ = 2,34 s", "t₃ = 2,29 s"],
             jaaprekina=["t(vid) = ?", "Δt = ?", "δ = ?"],
             formulas=["t(vid) = (t₁+t₂+t₃)/3",
                       "Δt = lielākā novirze", "δ = Δt/t(vid) · 100 %"],
             aprekins=["1)  t(vid) = (2,31+2,34+2,29) : 3 = 2,31 s",
                       "2)  Novirzes: 0,00; 0,03; 0,02 → Δt = 0,03 s",
                       "3)  δ = 0,03 : 2,31 · 100 % ≈ 1,3 %"],
             atbilde="t = (2,31 ± 0,03) s ;   δ ≈ 1,3 %",
             piezime="Šī ir vienkāršotā metode, ko lieto skolas "
                     "laboratorijas darbos."),
        dict(nr=7, virsraksts="Laukuma kļūda",
             teksts="Izmērīts a = (5,0 ± 0,1) cm un b = (8,0 ± 0,1) cm.\n"
                    "Aprēķini laukumu un tā kļūdu!",
             dots=["a = 5,0 cm, Δa = 0,1 cm", "b = 8,0 cm, Δb = 0,1 cm"],
             jaaprekina=["S = ?", "δS = ?", "ΔS = ?"],
             formulas=["S = a · b", "δS = δa + δb", "ΔS = δS · S"],
             aprekins=["1)  S = 5,0 · 8,0 = 40 cm²",
                       "2)  δa = 2,0 % ;  δb = 1,3 % → δS = 3,3 %",
                       "3)  ΔS = 0,033 · 40 ≈ 1,3 cm²"],
             atbilde="S = (40 ± 1) cm² ;   δ ≈ 3 %",
             piezime="Reizinot lielumus, relatīvās kļūdas SASKAITA."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Iedaļas vērtība C = (a₂ − a₁)/n.",
            "Absolūtā kļūda tiešā mērījumā parasti ir C/2.",
            "Rezultātu pieraksta formā x = (x ± Δx) vienība.",
            "Netiešā mērījumā relatīvās kļūdas saskaita.",
        ],
        majasdarbs=[
            "Starp 20 °C un 30 °C ir 10 iedaļas. Nosaki C un ΔT.",
            "m = (250 ± 5) g. Aprēķini relatīvo kļūdu.",
            "V = (50 ± 2) cm³, m = (135 ± 1) g. Aprēķini ρ un δρ.",
        ],
        pasvertejums=["Protu noteikt iedaļas vērtību",
                      "Protu novērtēt absolūto kļūdu",
                      "Protu pierakstīt rezultātu ar kļūdu",
                      "Protu aprēķināt relatīvo kļūdu"],
        nakama="Nākamā stunda: pētījuma plānošana."),
),

dict(
    nr="1.12", virsraksts="Pētījuma plānošana",
    jautajums="Kā pētījumu padarīt godīgu?",
    apaksraksts="Mainīgie · Hipotēze · Datu tabula · Atkārtojumi",
    merkis="Iemācīties formulēt pētāmo jautājumu un hipotēzi, noteikt "
           "mainīgos lielumus un sagatavot datu tabulu LD1 darbam.",
    protu=["formulēt pētāmo jautājumu un hipotēzi;",
           "atšķirt neatkarīgo, atkarīgo un fiksētos lielumus;",
           "sagatavot datu tabulu;",
           "pamatot atkārtojumu nepieciešamību."],
    atkartojums="1.11. stundā mācījāmies novērtēt viena mērījuma kļūdu. "
                "Tagad plānosim veselu pētījumu - nākamajā stundā to "
                "veiksim (LD1).",
    uzdevumu_apraksts="Mainīgo noteikšana un pētījuma plāna sastādīšana",
    teorija=[
        ("Pētījuma mainīgie", [
            ("kartitas", [
                ("NEATKARĪGAIS", BLUE,
                 ["To maina pētnieks.",
                  "LD1: renītes augstums h.",
                  "Uz grafika - x ass."]),
                ("ATKARĪGAIS", GREEN,
                 ["To mēra.",
                  "LD1: laiks t (un no tā v).",
                  "Uz grafika - y ass."]),
                ("FIKSĒTIE", GOLD,
                 ["Tos tur nemainīgus.",
                  "LD1: ceļš s, lodīte, renīte.",
                  "Bez tiem salīdzinājums nav godīgs."]),
            ]),
            ("formula", "HIPOTĒZE",
             "Ja palielina ... , tad ... , jo ...",
             "Hipotēzei jābūt pārbaudāmai ar mērījumu un jāsatur "
             "pamatojums. «Būs interesanti» nav hipotēze.", GOLD),
        ]),
        ("Godīgs salīdzinājums", [
            ("panelis", "KĀPĒC ATKĀRTO MĒRĪJUMUS",
             ["Katrā mērījumā ir nejauša kļūda. Trīs atkārtojumi ļauj "
              "aprēķināt vidējo un pamanīt izlecošu vērtību. Ja trīs "
              "rezultāti atšķiras stipri, mērījums jāatkārto vēlreiz."],
             NAVY),
            ("tabula",
             ["Plāna solis", "Ko pieraksta", "LD1 piemērs"],
             [["Jautājums", "Ko tieši pēta", "Kā v atkarīgs no h"],
              ["Hipotēze", "Prognoze ar pamatojumu", "v augs, jo..."],
              ["Mainīgie", "Neatkarīgais, atkarīgais, fiksētie",
               "h; t; s, lodīte"],
              ["Tabula", "Slejas ar mērvienībām", "h, cm; t₁-t₃, s"],
              ["Atkārtojumi", "Cik reižu", "3 katram h"]],
             [4.20, 5.10, 4.03]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Mainīgo noteikšana",
             teksts="Pēta, kā atsperes pagarinājums ir atkarīgs no "
                    "pieliktās\nmasas. Nosaki visus trīs mainīgo veidus!",
             dots=["pēta x atkarību no m"],
             jaaprekina=["neatkarīgais = ?", "atkarīgais = ?",
                         "fiksētie = ?"],
             formulas=["Neatkarīgo maina, atkarīgo mēra"],
             aprekins=["1)  Neatkarīgais: masa m",
                       "2)  Atkarīgais: pagarinājums x",
                       "3)  Fiksētie: atspere, temperatūra, "
                       "nolasīšanas veids"],
             atbilde="Maina m, mēra x, nemaina atsperi un apstākļus.",
             piezime="Ja nomaina atsperi, dati vairs nav salīdzināmi."),
        dict(nr=2, virsraksts="Hipotēzes formulēšana",
             teksts="Pētāmais jautājums: kā lodītes vidējais ātrums ir\n"
                    "atkarīgs no renītes augstuma? Formulē hipotēzi!",
             dots=["neatkarīgais: h", "atkarīgais: v"],
             jaaprekina=["hipotēze = ?"],
             formulas=["Ja ..., tad ..., jo ..."],
             aprekins=["1)  Ja palielina renītes augstumu,",
                       "2)  tad lodītes vidējais ātrums palielinās,",
                       "3)  jo lielākā augstumā tā iegūst vairāk "
                       "enerģijas."],
             atbilde="Ja h palielinās, tad v(vid) palielinās, jo pieaug "
                     "sākuma potenciālā enerģija.",
             piezime="Hipotēze var arī neapstiprināties - tas nav "
                     "sliktāks rezultāts."),
        dict(nr=3, virsraksts="Tabulas sagatavošana",
             teksts="Sagatavo mērījumu tabulas galveni pētījumam ar "
                    "5 dažādiem\naugstumiem un 3 atkārtojumiem katrā!",
             dots=["5 augstumi", "3 atkārtojumi"],
             jaaprekina=["slejas = ?", "rindas = ?"],
             formulas=["Katrai slejai - lielums un mērvienība"],
             aprekins=["1)  Slejas: Nr.; h, cm; s, m; t₁, s; t₂, s; "
                       "t₃, s;",
                       "2)  t(vid), s;  v(vid), m/s",
                       "3)  Rindas: 5 (pa vienai katram augstumam)"],
             atbilde="8 slejas, 5 datu rindas; mērvienības galvenē.",
             piezime="Mērvienību raksta galvenē, nevis pie katra skaitļa."),
        dict(nr=4, virsraksts="Izlecošs mērījums",
             teksts="Vienam augstumam iegūti laiki 1,82 s; 1,79 s un\n"
                    "2,64 s. Ko darīt ar trešo mērījumu?",
             dots=["t₁ = 1,82 s", "t₂ = 1,79 s", "t₃ = 2,64 s"],
             jaaprekina=["kā rīkoties?"],
             formulas=["Salīdzina ar pārējo izkliedi"],
             aprekins=["1)  t₁ un t₂ atšķiras par 0,03 s",
                       "2)  t₃ atšķiras par ~0,8 s - daudz vairāk",
                       "3)  Mērījumu atkārto; ja atkārtojas 1,8 s, "
                       "t₃ izslēdz"],
             atbilde="Mērījumu atkārto; izlecošo vērtību neiekļauj "
                     "vidējā, bet protokolā piemin.",
             piezime="Datus nedrīkst izmest klusējot - vienmēr pamato."),
        dict(nr=5, virsraksts="Fiksējamie apstākļi",
             teksts="Pēta, kā berzes spēks ir atkarīgs no virsmas "
                    "veida.\nKurus apstākļus nedrīkst mainīt?",
             dots=["neatkarīgais: virsmas veids", "atkarīgais: F(berzes)"],
             jaaprekina=["fiksētie lielumi = ?"],
             formulas=["Vienā mērījumu sērijā maina TIKAI vienu lielumu"],
             aprekins=["1)  Tas pats ķermenis - masa nemainās",
                       "2)  Tas pats dinamometrs un vilkšanas veids",
                       "3)  Vienmērīga kustība un vienāds saskares "
                       "laukums"],
             atbilde="Nemaina masu, dinamometru, vilkšanas veidu un "
                     "kustības raksturu.",
             piezime="Ja maina divus lielumus reizē, secinājumu izdarīt "
                     "nevar."),
        dict(nr=6, virsraksts="Mērījumu skaits",
             teksts="Cik reizes katrā punktā jāatkārto mērījums un "
                    "kāpēc?\nPamato ar kļūdas argumentu!",
             dots=["viens mērījums vienā punktā"],
             jaaprekina=["n = ?", "pamatojums = ?"],
             formulas=["Atkārtojumi samazina nejaušo kļūdu"],
             aprekins=["1)  Ar vienu mērījumu izlecošu vērtību nepamana",
                       "2)  Ar trim var aprēķināt vidējo un izkliedi",
                       "3)  Skolā parasti pietiek ar 3 līdz 5 "
                       "atkārtojumiem"],
             atbilde="Vismaz 3 atkārtojumi katrā punktā - lai varētu "
                     "aprēķināt vidējo un pamanīt izlecošu mērījumu.",
             piezime="Sistemātisko kļūdu atkārtojumi NEsamazina - to "
                     "novērš tikai ierīces pārbaude."),
        dict(nr=7, virsraksts="Kļūdains plāns",
             teksts="Skolēns katrā mērījumā vienlaikus maina renītes\n"
                    "augstumu UN lodītes veidu. Kāpēc rezultāts neder?",
             dots=["maina h un lodīti vienlaikus"],
             jaaprekina=["kļūda = ?", "labojums = ?"],
             formulas=["Vienā sērijā maina vienu neatkarīgo lielumu"],
             aprekins=["1)  Mainās divi lielumi reizē",
                       "2)  Nevar zināt, kurš izraisīja ātruma maiņu",
                       "3)  Labojums: visu sēriju veic ar vienu lodīti"],
             atbilde="Plāns neder - jāfiksē lodīte un jāmaina tikai "
                     "augstums.",
             piezime="Otru lodīti var pārbaudīt atsevišķā sērijā un "
                     "rezultātus salīdzināt."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Pētījumā ir neatkarīgais, atkarīgais un fiksētie lielumi.",
            "Hipotēze: «Ja ..., tad ..., jo ...» - pārbaudāma ar "
            "mērījumu.",
            "Datu tabulā mērvienības raksta galvenē.",
            "Atkārtojumi ļauj pamanīt un novērtēt nejaušas kļūdas.",
        ],
        majasdarbs=[
            "Sagatavo LD1 protokola 1.-3. sadaļu (hipotēze, piederumi, "
            "gaita).",
            "Formulē hipotēzi pētījumam par ūdens atdzišanas ātrumu.",
            "Nosauc trīs fiksētos lielumus pētījumā par berzes spēku.",
        ],
        pasvertejums=["Protu formulēt hipotēzi",
                      "Protu noteikt mainīgos",
                      "Protu sagatavot tabulu",
                      "Esmu gatavs LD1"],
        nakama="Nākamā stunda: LD1 - lodītes vidējais ātrums."),
),

dict(
    nr="1.13", virsraksts="Datu apstrāde un grafiks",
    jautajums="Kā no mērījumiem iegūst secinājumu?",
    apaksraksts="Vidējā vērtība · Grafiks · Tendence · Secinājums",
    merkis="Iemācīties apstrādāt LD1 mērījumus: aprēķināt vidējās "
           "vērtības, uzzīmēt grafiku un formulēt pamatotu secinājumu.",
    protu=["aprēķināt vidējo vērtību no atkārtojumiem;",
           "uzzīmēt grafiku ar apzīmētām asīm un mērogu;",
           "aprakstīt tendenci grafikā;",
           "formulēt secinājumu ar konkrētiem datiem."],
    atkartojums="LD1 mērījumi ir veikti. Tagad no skaitļiem jāiegūst "
                "atbilde uz pētāmo jautājumu - un tā jāpamato.",
    uzdevumu_apraksts="Vidējās vērtības, grafiks un secinājums",
    teorija=[
        ("Datu apstrādes soļi", [
            ("kartitas", [
                ("1. VIDĒJĀ VĒRTĪBA", BLUE,
                 ["t(vid) = (t₁+t₂+t₃)/3",
                  "Izlecošās vērtības atzīmē."]),
                ("2. APRĒĶINS", GREEN,
                 ["v = s / t(vid)",
                  "Katrai rindai atsevišķi."]),
                ("3. GRAFIKS", GOLD,
                 ["Neatkarīgais uz x ass.",
                  "Atkarīgais uz y ass."]),
            ]),
            ("formula", "LABA GRAFIKA PAZĪMES",
             "asis apzīmētas ar lielumu un mērvienību  ·  ērts mērogs  ·  "
             "punkti skaidri  ·  izlīdzināta līkne, nevis lauzta līnija",
             "Punktus nesavieno ar lauztu līniju - zīmē gludu līkni vai "
             "taisni, kas iet cauri punktu mākonim.", GOLD),
        ]),
        ("No grafika uz secinājumu", [
            ("panelis", "SECINĀJUMA STRUKTŪRA",
             ["1) Atbilde uz pētāmo jautājumu.  2) Divi konkrēti skaitļi "
              "no saviem datiem.  3) Vai hipotēze apstiprinājās.  "
              "4) Kļūdu avots un uzlabojums.  Bez skaitļiem secinājums "
              "nav pamatots."], NAVY),
            ("tabula",
             ["Grafika forma", "Ko tā nozīmē", "Piemērs"],
             [["Augoša taisne", "Tieši proporcionāla saistība",
               "F(x) atsperei"],
              ["Augoša līkne", "Aug, bet ne proporcionāli",
               "v(h) renītē"],
              ["Horizontāla", "Lielums nemainās", "v(t) vienmērīgā"],
              ["Dilstoša", "Viens aug, otrs sarūk", "T(t) atdzišana"]],
             [4.30, 5.20, 3.83]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Vidējā vērtība",
             teksts="Laiki vienam augstumam: 1,42 s; 1,38 s; 1,45 s.\n"
                    "Aprēķini vidējo laiku un vidējo ātrumu, ja "
                    "s = 0,80 m!",
             dots=["t₁ = 1,42 s", "t₂ = 1,38 s", "t₃ = 1,45 s",
                   "s = 0,80 m"],
             jaaprekina=["t(vid) = ?", "v = ?"],
             formulas=["t(vid) = (t₁+t₂+t₃)/3", "v = s/t(vid)"],
             aprekins=["1)  Σt = 1,42 + 1,38 + 1,45 = 4,25 s",
                       "2)  t(vid) = 4,25 : 3 = 1,42 s",
                       "3)  v = 0,80 : 1,42 = 0,56 m/s"],
             atbilde="t(vid) = 1,42 s ;   v = 0,56 m/s",
             piezime="Vidējo noapaļo līdz tikpat cipariem, cik ir "
                     "mērījumos."),
        dict(nr=2, virsraksts="Mēroga izvēle",
             teksts="Grafikā jāattēlo augstumi no 5 cm līdz 25 cm uz "
                    "10 cm\ngaras ass. Kādu mērogu izvēlēties?",
             dots=["h no 5 līdz 25 cm", "ass garums 10 cm"],
             jaaprekina=["mērogs = ?"],
             formulas=["Mērogs = diapazons / ass garums"],
             aprekins=["1)  Diapazons: 25 − 0 = 25 cm (sākot no nulles)",
                       "2)  25 : 10 = 2,5 cm(h) uz 1 cm(ass)",
                       "3)  Ērtāk: 1 cm(ass) atbilst 2,5 cm vai 5 cm"],
             atbilde="Mērogs 1 cm atbilst 2,5 cm (vai 5 cm ērtākai lasīšanai).",
             piezime="Mērogam jābūt ērtam - 1, 2, 5 vai 10 vienības uz "
                     "iedaļu."),
        dict(nr=3, virsraksts="Tendences apraksts",
             teksts="Dati: h = 5 cm → v = 0,30 m/s; h = 15 cm → "
                    "v = 0,50 m/s;\nh = 25 cm → v = 0,63 m/s. Apraksti "
                    "tendenci!",
             dots=["3 datu pāri"],
             jaaprekina=["tendence = ?"],
             formulas=["Salīdzina pieaugumus"],
             aprekins=["1)  h aug 5 reizes (5 → 25 cm)",
                       "2)  v aug 2,1 reizes (0,30 → 0,63 m/s)",
                       "3)  Aug, bet lēnāk nekā h → līkne, ne taisne"],
             atbilde="v pieaug, palielinoties h, bet ne proporcionāli - "
                     "grafiks ir augoša līkne.",
             piezime="Šeit v ~ √h - to pierādīsim 2. tematā."),
        dict(nr=4, virsraksts="Secinājuma formulēšana",
             teksts="Uzraksti secinājumu pētījumam, izmantojot 3. uzdevuma\n"
                    "datus!",
             dots=["v(5 cm) = 0,30 m/s", "v(25 cm) = 0,63 m/s"],
             jaaprekina=["secinājums = ?"],
             formulas=["Atbilde + skaitļi + hipotēze + kļūdas"],
             aprekins=["1)  Palielinot h, v(vid) palielinās.",
                       "2)  Pie h = 5 cm v = 0,30 m/s; pie 25 cm - "
                       "0,63 m/s, t. i., 2,1 reizes vairāk.",
                       "3)  Hipotēze apstiprinājās; galvenais kļūdu "
                       "avots - reakcijas laiks."],
             atbilde="Secinājums pamatots ar diviem konkrētiem "
                     "skaitļiem un norādītu kļūdu avotu.",
             piezime="Tieši šādu struktūru vērtē arī PR1 prezentācijā."),
        dict(nr=5, virsraksts="Taisnes slīpums grafikā",
             teksts="s(t) grafikā taisne iet caur (0 s; 0 m) un\n"
                    "(4,0 s; 10 m). Atrodi slīpumu un tā fizikālo jēgu!",
             dots=["(0 s; 0 m)", "(4,0 s; 10 m)"],
             jaaprekina=["k = ?", "jēga = ?"],
             formulas=["k = Δs / Δt"],
             aprekins=["1)  Δs = 10 − 0 = 10 m",
                       "2)  Δt = 4,0 − 0 = 4,0 s",
                       "3)  k = 10 : 4,0 = 2,5 m/s"],
             atbilde="k = 2,5 m/s - tas ir kustības ātrums.",
             piezime="Grafika slīpumam vienmēr ir fizikāla jēga un "
                     "mērvienība."),
        dict(nr=6, virsraksts="Starpvērtības nolasīšana",
             teksts="Dati: h = 15 cm → v = 0,50 m/s;  h = 25 cm → "
                    "v = 0,63 m/s.\nNovērtē v pie h = 20 cm!",
             dots=["v(15 cm) = 0,50 m/s", "v(25 cm) = 0,63 m/s"],
             jaaprekina=["v(20 cm) = ?"],
             formulas=["Interpolācija: v ≈ (v₁ + v₂)/2, ja h ir vidū"],
             aprekins=["1)  20 cm ir tieši starp 15 un 25 cm",
                       "2)  v ≈ (0,50 + 0,63) : 2",
                       "3)  v ≈ 0,57 m/s"],
             atbilde="v ≈ 0,57 m/s (nolasīts no grafika līknes).",
             piezime="Interpolēt drīkst; ekstrapolēt tālu ārpus datiem - "
                     "nē."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Vidējo vērtību rēķina no atkārtojumiem; izlecošās atzīmē.",
            "Grafikam vajag apzīmētas asis, mērvienības un ērtu mērogu.",
            "Punktus izlīdzina ar līkni, nevis savieno lauztā līnijā.",
            "Secinājums bez konkrētiem skaitļiem nav pamatots.",
        ],
        majasdarbs=[
            "Pabeidz LD1 protokolu un iesniedz e-klasē.",
            "Sagatavo PR1 prezentāciju: 5 slaidi vai plāns uz lapas.",
            "Aprēķini vidējo no 2,15 s; 2,20 s; 2,18 s un novērtē "
            "izkliedi.",
        ],
        pasvertejums=["Protu aprēķināt vidējo vērtību",
                      "Protu uzzīmēt grafiku",
                      "Protu aprakstīt tendenci",
                      "Protu formulēt pamatotu secinājumu"],
        nakama="Nākamā stunda: PR1 - pētījuma rezultātu prezentācija."),
),

]
