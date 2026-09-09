# -*- coding: utf-8 -*-
"""1. temats "Ievads pētniecībā. Vienmērīga un nevienmērīga kustība".

A daļa: 1.1.-1.7. stunda (vektori un vienmērīga kustība).
"""

from fiz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN     # noqa: F401

TEMATS = "1. temats. Ievads pētniecībā. Vienmērīga un nevienmērīga kustība"
KICKER = "FIZIKA I · 10. KLASE · 1. TEMATS: IEVADS PĒTNIECĪBĀ UN KUSTĪBA"
KURSS = "FIZIKA I · 10. KLASE"
MAPE = ("C:/aphysics/Fizika_1/"
        "1. Ievads pētniecībā. Vienmērīga un nevienmērīga kustība")

STUNDAS = [

dict(
    nr="1.1", virsraksts="Fizika kā zinātne",
    jautajums="Kāpēc fiziķi mēra, nevis min?",
    apaksraksts="Modelis · Mērījums · SI · Lielumu pieraksts",
    merkis="Saprast, kā fizika veido zināšanas: no novērojuma līdz "
           "modelim un mērījumam, un iemācīties pierakstīt fizikālu "
           "lielumu ar mērvienību.",
    protu=["nosaukt fizikas pētīšanas soļus;",
           "atšķirt fizikālu lielumu no tā mērvienības;",
           "lietot SI pamatvienības un decimālos priedēkļus;",
           "pārveidot lielumus SI vienībās."],
    atkartojums="Pamatskolā jau mērīji garumu, laiku un masu. Tagad "
                "mācīsimies to darīt tā, lai rezultātu var pārbaudīt cits "
                "cilvēks.",
    uzdevumu_apraksts="Mērvienību pārveidošana un lielumu pieraksts",
    teorija=[
        ("Kā fizika iegūst zināšanas", [
            ("kartitas", [
                ("NOVĒROJUMS", BLUE,
                 ["Pamanām parādību dabā vai tehnikā.",
                  "Piemērs: automašīna bremzē."]),
                ("MODELIS", GREEN,
                 ["Vienkāršots apraksts ar formulām.",
                  "Piemērs: vienmērīgi paātrināta kustība."]),
                ("MĒRĪJUMS", GOLD,
                 ["Skaitliska pārbaude ar mērierīci.",
                  "Piemērs: bremzēšanas ceļa mērīšana."]),
            ]),
            ("panelis", "KĀPĒC MĒRA, NEVIS MIN",
             ["Mērījumu var atkārtot un pārbaudīt. Minējumu - nē. Fizikā "
              "apgalvojums ir vērtīgs tikai tad, ja pastāv veids, kā to "
              "pārbaudīt ar mērījumu."], NAVY),
        ]),
        ("SI pamatvienības un priedēkļi", [
            ("tabula",
             ["Lielums", "Apzīmējums", "SI vienība"],
             [["Garums", "l, s, h, d", "metrs (m)"],
              ["Laiks", "t", "sekunde (s)"],
              ["Masa", "m", "kilograms (kg)"],
              ["Temperatūra", "T", "kelvins (K)"],
              ["Strāvas stiprums", "I", "ampērs (A)"]],
             [5.10, 3.60, 3.53]),
            ("formula", "BIEŽĀKIE PRIEDĒKĻI",
             "k (kilo) = 10³      c (centi) = 10⁻²      "
             "m (mili) = 10⁻³      µ (mikro) = 10⁻⁶",
             "1 km = 1000 m;  1 cm = 0,01 m;  1 ms = 0,001 s. "
             "Aprēķinos vienmēr vispirms pāriet uz SI vienībām.", GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Garuma pārveidošana",
             teksts="Sporta zāles garums ir 42 m, platums 2400 cm.\n"
                    "Izsaki abus lielumus metros un aprēķini laukumu!",
             dots=["a = 42 m", "b = 2400 cm"],
             jaaprekina=["b (m) = ?", "S = ?"],
             formulas=["1 cm = 0,01 m", "S = a · b"],
             aprekins=["1)  b = 2400 · 0,01 = 24 m",
                       "2)  S = 42 · 24",
                       "3)  S = 1008 m² ≈ 1,0·10³ m²"],
             atbilde="b = 24 m ;   S ≈ 1,0·10³ m²",
             piezime="Pirms reizināšanas abiem lielumiem jābūt vienādās "
                     "vienībās."),
        dict(nr=2, virsraksts="Ātruma pārveidošana",
             teksts="Automašīnas ātrums ir 90 km/h.\n"
                    "Izsaki to metros sekundē!",
             dots=["v = 90 km/h"],
             jaaprekina=["v (m/s) = ?"],
             formulas=["1 km/h = 1000 m : 3600 s", "v(m/s) = v(km/h) : 3,6"],
             aprekins=["1)  90 km/h = 90 · 1000 m : 3600 s",
                       "2)  v = 90 000 : 3600",
                       "3)  v = 25 m/s"],
             atbilde="v = 25 m/s",
             piezime="Ātri: dala ar 3,6. Atpakaļ - reizina ar 3,6."),
        dict(nr=3, virsraksts="Laika pārveidošana",
             teksts="Vilciena brauciens ilgst 2 h 15 min.\n"
                    "Izsaki laiku sekundēs!",
             dots=["t = 2 h 15 min"],
             jaaprekina=["t (s) = ?"],
             formulas=["1 h = 3600 s", "1 min = 60 s"],
             aprekins=["1)  2 h = 2 · 3600 = 7200 s",
                       "2)  15 min = 15 · 60 = 900 s",
                       "3)  t = 7200 + 900 = 8100 s"],
             atbilde="t = 8100 s = 8,1·10³ s",
             piezime="Lielus skaitļus ērti pierakstīt standartformā."),
        dict(nr=4, virsraksts="Blīvuma vienības",
             teksts="Alumīnija blīvums ir 2,7 g/cm³.\n"
                    "Izsaki to kilogramos uz kubikmetru!",
             dots=["ρ = 2,7 g/cm³"],
             jaaprekina=["ρ (kg/m³) = ?"],
             formulas=["1 g = 10⁻³ kg", "1 cm³ = 10⁻⁶ m³"],
             aprekins=["1)  1 g/cm³ = 10⁻³ kg : 10⁻⁶ m³",
                       "2)  1 g/cm³ = 1000 kg/m³",
                       "3)  ρ = 2,7 · 1000 = 2700 kg/m³"],
             atbilde="ρ = 2,7·10³ kg/m³",
             piezime="Šis pārveidojums fizikā vajadzīgs ļoti bieži - "
                     "vērts iegaumēt."),
        dict(nr=5, virsraksts="Laukuma vienības",
             teksts="Zemesgabala laukums ir 0,45 ha.\n"
                    "Izsaki to kvadrātmetros! (1 ha = 10⁴ m²)",
             dots=["S = 0,45 ha"],
             jaaprekina=["S (m²) = ?"],
             formulas=["1 ha = 10⁴ m²"],
             aprekins=["1)  S = 0,45 · 10⁴ m²",
                       "2)  S = 4500 m²",
                       "3)  S = 4,5·10³ m²"],
             atbilde="S = 4,5·10³ m²",
             piezime="Laukuma vienībās priedēklis kāpināts kvadrātā: "
                     "1 km² = 10⁶ m²."),
        dict(nr=6, virsraksts="Tilpuma vienības",
             teksts="Ūdens pudelē ir 250 ml ūdens.\n"
                    "Izsaki tilpumu kubikmetros! (1 ml = 1 cm³)",
             dots=["V = 250 ml"],
             jaaprekina=["V (m³) = ?"],
             formulas=["1 ml = 1 cm³", "1 cm³ = 10⁻⁶ m³"],
             aprekins=["1)  V = 250 cm³",
                       "2)  V = 250 · 10⁻⁶ m³",
                       "3)  V = 2,5·10⁻⁴ m³"],
             atbilde="V = 2,5·10⁻⁴ m³",
             piezime="Noder atcerēties: 1 litrs = 10⁻³ m³."),
        dict(nr=7, virsraksts="Priedēkļi standartformā",
             teksts="Gaismas viļņa garums ir 550 nm, bet procesora\n"
                    "frekvence 3,2 GHz. Izsaki abus lielumus SI "
                    "pamatvienībās!",
             dots=["λ = 550 nm", "f = 3,2 GHz"],
             jaaprekina=["λ (m) = ?", "f (Hz) = ?"],
             formulas=["1 nm = 10⁻⁹ m", "1 GHz = 10⁹ Hz"],
             aprekins=["1)  λ = 550 · 10⁻⁹ m",
                       "2)  λ = 5,5·10⁻⁷ m",
                       "3)  f = 3,2 · 10⁹ Hz"],
             atbilde="λ = 5,5·10⁻⁷ m ;   f = 3,2·10⁹ Hz",
             piezime="Standartformā skaitlis vienmēr ir no 1 līdz 10."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Fizika iet ceļu: novērojums → modelis → mērījums → "
            "secinājums.",
            "Fizikāls lielums vienmēr sastāv no skaitļa un mērvienības.",
            "SI pamatvienības: m, s, kg, K, A.",
            "Aprēķinu sāk ar pāreju uz SI vienībām.",
        ],
        majasdarbs=[
            "Izsaki metros: 350 cm; 2,4 km; 18 mm.",
            "Izsaki m/s: 54 km/h; 120 km/h; 5,4 km/h.",
            "Izsaki kg/m³: 7,8 g/cm³ (tērauds); 0,92 g/cm³ (ledus).",
        ],
        pasvertejums=["Protu nosaukt pētīšanas soļus",
                      "Protu lietot SI vienības",
                      "Protu pārveidot mērvienības",
                      "Protu pierakstīt lielumu ar vienību"],
        nakama="Nākamā stunda: skalāri un vektori."),
),

dict(
    nr="1.2", virsraksts="Skalāri un vektori",
    jautajums="Ar ko ātrums atšķiras no ceļa?",
    apaksraksts="Skalārs · Vektors · Modulis · Virziens",
    merkis="Iemācīties atšķirt skalāru lielumu no vektora un pareizi "
           "pierakstīt vektoru ar moduli un virzienu.",
    protu=["atšķirt skalāru no vektora;",
           "nosaukt vektora moduli un virzienu;",
           "pareizi pierakstīt vektoriālus lielumus;",
           "attēlot vektoru zīmējumā ar mērogu."],
    atkartojums="1.1. stundā: lielumam vajag skaitli un mērvienību. "
                "Dažiem lielumiem ar to nepietiek - vajag arī virzienu.",
    uzdevumu_apraksts="Vektora modulis, virziens un mērogs",
    teorija=[
        ("Divi lielumu veidi", [
            ("divi",
             ("SKALĀRS", BLUE,
              ["Pilnībā nosaka skaitlis un mērvienība.",
               "Piemēri: ceļš s, laiks t, masa m, temperatūra T, "
               "enerģija E.",
               "Pieraksta bez bultiņas: s = 120 m."]),
             ("VEKTORS", RED,
              ["Vajag arī virzienu.",
               "Piemēri: pārvietojums, ātrums, paātrinājums, spēks.",
               "Pieraksta ar bultiņu vai treknrakstā: v⃗, F⃗."])),
            ("panelis", "KĀPĒC TAS SVARĪGI",
             ["«Automašīna brauc 50 km/h» - ar to nepietiek, lai zinātu, "
              "kur tā nonāks. Vajag arī virzienu. Tāpēc ātrums ir "
              "vektors, bet ātruma modulis (spidometra rādījums) - "
              "skalārs."], NAVY),
        ]),
        ("Vektors zīmējumā", [
            ("kartitas", [
                ("SĀKUMPUNKTS", GREY,
                 ["Vieta, kur vektors sākas.",
                  "Spēkam - pielikšanas punkts."]),
                ("GARUMS", BLUE,
                 ["Attēlo moduli izvēlētā mērogā.",
                  "Piemērs: 1 cm ↔ 10 N."]),
                ("BULTA", RED,
                 ["Rāda virzienu.",
                  "Bez bultas zīmējums nav vektors."]),
            ]),
            ("formula", "MODULIS",
             "|v⃗| = v        v⃗ = 0  tikai tad, ja  v = 0",
             "Vektora modulis vienmēr ir pozitīvs skaitlis ar "
             "mērvienību. Mīnusa zīme pie vektora projekcijas nozīmē "
             "virzienu, nevis negatīvu garumu.", GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Skalārs vai vektors",
             teksts="Doti lielumi: 5 kg;  12 m uz austrumiem;  300 K;\n"
                    "20 N lejup;  8 s;  15 m/s uz ziemeļiem.\n"
                    "Sadali tos divās grupās!",
             dots=["6 dažādi lielumi"],
             jaaprekina=["skalāri = ?", "vektori = ?"],
             formulas=["Vektoram ir norādīts virziens"],
             aprekins=["1)  Skalāri: 5 kg; 300 K; 8 s",
                       "2)  Vektori: 12 m uz austrumiem;",
                       "     20 N lejup; 15 m/s uz ziemeļiem"],
             atbilde="Skalāri: masa, temperatūra, laiks. Vektori: "
                     "pārvietojums, spēks, ātrums.",
             piezime="Pazīme: ja nosaukts virziens, lielums ir vektors."),
        dict(nr=2, virsraksts="Vektora attēlošana",
             teksts="Spēks F = 40 N vērsts horizontāli pa labi.\n"
                    "Kāds būs vektora garums zīmējumā, ja mērogs ir\n"
                    "1 cm ↔ 10 N?",
             dots=["F = 40 N", "mērogs: 1 cm ↔ 10 N"],
             jaaprekina=["l = ?"],
             formulas=["l = F : (spēks uz 1 cm)"],
             aprekins=["1)  l = 40 N : 10 N/cm",
                       "2)  l = 4,0 cm"],
             atbilde="Bultas garums 4,0 cm, vērsta pa labi.",
             piezime="Mērogu vienmēr pieraksta blakus zīmējumam."),
        dict(nr=3, virsraksts="Modulis no zīmējuma",
             teksts="Zīmējumā ātruma vektors ir 6,5 cm garš.\n"
                    "Mērogs: 1 cm ↔ 4,0 m/s. Cik liels ir ātrums?",
             dots=["l = 6,5 cm", "mērogs: 1 cm ↔ 4,0 m/s"],
             jaaprekina=["v = ?"],
             formulas=["v = l · (ātrums uz 1 cm)"],
             aprekins=["1)  v = 6,5 · 4,0",
                       "2)  v = 26 m/s"],
             atbilde="v = 26 m/s",
             piezime="Pārbaudi: 26 m/s ≈ 94 km/h - reāls automašīnas "
                     "ātrums."),
        dict(nr=4, virsraksts="Ceļš un pārvietojums",
             teksts="Skolēns aiziet 30 m uz priekšu un pēc tam 30 m "
                    "atpakaļ.\nCik liels ir noietais ceļš un cik liels "
                    "pārvietojums?",
             dots=["s₁ = 30 m", "s₂ = 30 m (atpakaļ)"],
             jaaprekina=["s = ?", "|d⃗| = ?"],
             formulas=["s = s₁ + s₂  (skalārs)",
                       "d⃗ - vektors no sākuma uz beigām"],
             aprekins=["1)  s = 30 + 30 = 60 m",
                       "2)  Sākuma un beigu punkts sakrīt",
                       "3)  |d⃗| = 0"],
             atbilde="s = 60 m ;   |d⃗| = 0 m",
             piezime="Šis piemērs vislabāk parāda atšķirību starp skalāru "
                     "un vektoru."),
        dict(nr=5, virsraksts="Kad vektori ir vienādi",
             teksts="Uz kasti darbojas divi spēki pa 20 N: viens pa "
                    "labi,\notrs pa kreisi. Vai šie vektori ir vienādi? "
                    "Pamato!",
             dots=["F₁ = 20 N (pa labi)", "F₂ = 20 N (pa kreisi)"],
             jaaprekina=["Vai F⃗₁ = F⃗₂ ?"],
             formulas=["Vektori vienādi, ja sakrīt modulis UN virziens"],
             aprekins=["1)  Moduļi vienādi: 20 N = 20 N",
                       "2)  Virzieni pretēji",
                       "3)  Tātad F⃗₁ ≠ F⃗₂, bet F₁ = F₂"],
             atbilde="Moduļi vienādi, vektori nav vienādi: F⃗₂ = −F⃗₁.",
             piezime="Vektoru salīdzina pēc diviem raksturlielumiem, "
                     "ne tikai pēc skaitļa."),
        dict(nr=6, virsraksts="Mēroga izvēle",
             teksts="Spēks 250 N zīmējumā jāattēlo ar aptuveni 5 cm "
                    "garu\nbultu. Kādu ērtu mērogu izvēlēties?",
             dots=["F = 250 N", "l ≈ 5 cm"],
             jaaprekina=["mērogs = ?", "l = ?"],
             formulas=["mērogs = F : l"],
             aprekins=["1)  250 N : 5 cm = 50 N/cm",
                       "2)  Ērts mērogs: 1 cm ↔ 50 N",
                       "3)  Tad l = 250 : 50 = 5,0 cm"],
             atbilde="Mērogs 1 cm ↔ 50 N; bultas garums 5,0 cm.",
             piezime="Mērogam izvēlas apaļu skaitli: 1, 2, 5, 10, 50, "
                     "100."),
        dict(nr=7, virsraksts="Vai ātrums mainījās",
             teksts="Automašīna brauc 60 km/h uz ziemeļiem, pēc līkuma "
                    "tā\nbrauc 60 km/h uz austrumiem. Vai ātrums "
                    "mainījās?",
             dots=["v₁ = 60 km/h (Z)", "v₂ = 60 km/h (A)"],
             jaaprekina=["Vai v⃗ mainījās?"],
             formulas=["v⃗ mainās, ja mainās modulis vai virziens"],
             aprekins=["1)  Modulis nemainījās: 60 = 60 km/h",
                       "2)  Virziens mainījās: Z → A",
                       "3)  Tātad ātruma vektors ir mainījies"],
             atbilde="Ātruma modulis nemainījās, bet vektors v⃗ "
                     "mainījās.",
             piezime="Tāpēc līkumā automašīnai ir paātrinājums, kaut "
                     "spidometrs rāda to pašu."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Skalāru nosaka skaitlis ar mērvienību; vektoram vajag arī "
            "virzienu.",
            "Vektoru pieraksta ar bultiņu: v⃗, F⃗, a⃗.",
            "Vektora modulis ir pozitīvs skaitlis: |v⃗| = v.",
            "Zīmējumā vektora garums atbilst modulim izvēlētā mērogā.",
        ],
        majasdarbs=[
            "Nosauc trīs skalārus un trīs vektorus no ikdienas.",
            "Uzzīmē spēku 25 N pa kreisi mērogā 1 cm ↔ 5 N.",
            "Cilvēks apstaigā 400 m stadionu. Cik liels ir ceļš un cik "
            "pārvietojums?",
        ],
        pasvertejums=["Protu atšķirt skalāru no vektora",
                      "Protu pierakstīt vektoru",
                      "Protu attēlot vektoru mērogā",
                      "Protu nolasīt moduli no zīmējuma"],
        nakama="Nākamā stunda: darbības ar vektoriem."),
),

dict(
    nr="1.3", virsraksts="Darbības ar vektoriem",
    jautajums="Kā saskaita divus spēkus?",
    apaksraksts="Trijstūra likums · Paralelograma likums · Atņemšana",
    merkis="Iemācīties saskaitīt un atņemt vektorus ģeometriski un "
           "aprēķināt kopvektora moduli vienkāršos gadījumos.",
    protu=["saskaitīt vektorus pēc trijstūra likuma;",
           "lietot paralelograma likumu;",
           "atņemt vektorus;",
           "aprēķināt kopvektora moduli, ja vektori ir paralēli vai "
           "perpendikulāri."],
    atkartojums="1.2. stundā: vektoram ir modulis un virziens. Tagad "
                "mācīsimies vektorus saskaitīt - tas vajadzīgs katrā "
                "spēku uzdevumā.",
    uzdevumu_apraksts="Kopvektora modulis dažādos virzienos",
    teorija=[
        ("Vektoru saskaitīšana", [
            ("kartitas", [
                ("VIENĀ VIRZIENĀ", GREEN,
                 ["Moduļus saskaita.",
                  "F = F₁ + F₂",
                  "Virziens paliek tas pats."]),
                ("PRETĒJI", RED,
                 ["Moduļus atņem.",
                  "F = |F₁ − F₂|",
                  "Virziens - lielākajam."]),
                ("PERPENDIKULĀRI", BLUE,
                 ["Pitagora teorēma.",
                  "F = √(F₁² + F₂²)",
                  "tg α = F₂ / F₁"]),
            ]),
            ("panelis", "TRIJSTŪRA LIKUMS",
             ["Otrā vektora sākumu pieliek pirmā vektora galam. Kopvektors "
              "iet no pirmā sākuma līdz otrā galam. Rezultāts nav atkarīgs "
              "no saskaitīšanas secības: a⃗ + b⃗ = b⃗ + a⃗."], NAVY),
        ]),
        ("Atņemšana un mērogs", [
            ("formula", "VEKTORU ATŅEMŠANA",
             "a⃗ − b⃗ = a⃗ + (−b⃗)",
             "Vektoru −b⃗ iegūst, pagriežot b⃗ par 180°. Tāpēc atņemšana "
             "vienmēr ir saskaitīšana ar pretējo vektoru.", GOLD),
            ("tabula",
             ["Gadījums", "Kopvektora modulis", "Piemērs"],
             [["Vienā virzienā", "F = F₁ + F₂", "3 N + 4 N = 7 N"],
              ["Pretēji", "F = |F₁ − F₂|", "|3 N − 4 N| = 1 N"],
              ["Perpendikulāri", "F = √(F₁² + F₂²)", "√(3² + 4²) = 5 N"],
              ["Leņķī α", "kosinusu teorēma", "zīmē mērogā"]],
             [4.20, 4.60, 3.43]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Spēki vienā virzienā",
             teksts="Divi cilvēki stumj kasti vienā virzienā ar spēkiem\n"
                    "F₁ = 120 N un F₂ = 80 N. Cik liels ir kopspēks?",
             dots=["F₁ = 120 N", "F₂ = 80 N", "viens virziens"],
             jaaprekina=["F = ?"],
             formulas=["F = F₁ + F₂"],
             aprekins=["1)  F = 120 + 80",
                       "2)  F = 200 N"],
             atbilde="F = 200 N tajā pašā virzienā",
             piezime="Vienā virzienā vērstiem vektoriem moduļus vienkārši "
                     "saskaita."),
        dict(nr=2, virsraksts="Pretēji vērsti spēki",
             teksts="Uz kasti darbojas vilkšanas spēks 150 N un berzes "
                    "spēks\n60 N pretējā virzienā. Cik liels ir kopspēks?",
             dots=["F₁ = 150 N", "F₂ = 60 N (pretēji)"],
             jaaprekina=["F = ?"],
             formulas=["F = |F₁ − F₂|"],
             aprekins=["1)  F = |150 − 60|",
                       "2)  F = 90 N",
                       "3)  Virziens - kā F₁ (lielākajam)"],
             atbilde="F = 90 N vilkšanas virzienā",
             piezime="Ja spēki būtu vienādi, kopspēks būtu nulle un "
                     "ātrums nemainītos."),
        dict(nr=3, virsraksts="Perpendikulāri spēki",
             teksts="Uz laivu darbojas airu spēks 40 N uz priekšu un\n"
                    "straumes spēks 30 N sāniski. Cik liels ir kopspēks?",
             dots=["F₁ = 40 N", "F₂ = 30 N", "α = 90°"],
             jaaprekina=["F = ?"],
             formulas=["F = √(F₁² + F₂²)"],
             aprekins=["1)  F₁² = 1600 N² ;  F₂² = 900 N²",
                       "2)  F² = 1600 + 900 = 2500 N²",
                       "3)  F = √2500 = 50 N"],
             atbilde="F = 50 N",
             piezime="Trijnieks 3-4-5 fizikas uzdevumos parādās ļoti "
                     "bieži."),
        dict(nr=4, virsraksts="Pārvietojumu saskaitīšana",
             teksts="Tūrists nostaigā 300 m uz ziemeļiem, tad 400 m uz\n"
                    "austrumiem. Cik liels ir ceļš un cik pārvietojums?",
             dots=["s₁ = 300 m (Z)", "s₂ = 400 m (A)"],
             jaaprekina=["s = ?", "|d⃗| = ?"],
             formulas=["s = s₁ + s₂", "|d⃗| = √(s₁² + s₂²)"],
             aprekins=["1)  s = 300 + 400 = 700 m",
                       "2)  |d⃗|² = 90 000 + 160 000 = 250 000 m²",
                       "3)  |d⃗| = 500 m"],
             atbilde="s = 700 m ;   |d⃗| = 500 m",
             piezime="Pārvietojums nekad nav lielāks par ceļu."),
        dict(nr=5, virsraksts="Trīs spēki uz vienas taisnes",
             teksts="Uz ķermeni gar vienu taisni darbojas 50 N un 30 N "
                    "pa\nlabi un 100 N pa kreisi. Cik liels ir "
                    "kopspēks?",
             dots=["F₁ = 50 N (pa labi)", "F₂ = 30 N (pa labi)",
                   "F₃ = 100 N (pa kreisi)"],
             jaaprekina=["F = ?"],
             formulas=["F(labi) = F₁ + F₂", "F = |F(labi) − F₃|"],
             aprekins=["1)  F(labi) = 50 + 30 = 80 N",
                       "2)  F = |80 − 100| = 20 N",
                       "3)  Virziens - pa kreisi"],
             atbilde="F = 20 N pa kreisi",
             piezime="Vispirms saskaita vienā virzienā vērstos, tikai "
                     "tad atņem."),
        dict(nr=6, virsraksts="Trešais spēks līdzsvaram",
             teksts="Uz gredzenu darbojas divi perpendikulāri spēki "
                    "60 N un\n80 N. Cik liels spēks tos līdzsvaro?",
             dots=["F₁ = 60 N", "F₂ = 80 N", "α = 90°"],
             jaaprekina=["F₃ = ?"],
             formulas=["F = √(F₁² + F₂²)", "F₃ = F (pretējā virzienā)"],
             aprekins=["1)  F² = 3600 + 6400 = 10 000 N²",
                       "2)  F = 100 N",
                       "3)  F₃ = 100 N pretēji kopspēkam"],
             atbilde="F₃ = 100 N, vērsts pretēji kopspēkam.",
             piezime="Līdzsvarā visu spēku vektoru summa ir nulle."),
        dict(nr=7, virsraksts="Ātruma izmaiņa",
             teksts="Bumbiņa lido pret sienu ar 8,0 m/s un atlec atpakaļ "
                    "ar\n8,0 m/s. Cik liela ir ātruma izmaiņa "
                    "Δv⃗ = v⃗₂ − v⃗₁?",
             dots=["v₁ = 8,0 m/s (uz sienu)",
                   "v₂ = 8,0 m/s (no sienas)"],
             jaaprekina=["|Δv⃗| = ?"],
             formulas=["Δv⃗ = v⃗₂ − v⃗₁ = v⃗₂ + (−v⃗₁)"],
             aprekins=["1)  −v⃗₁ ir 8,0 m/s virzienā no sienas",
                       "2)  v⃗₂ un −v⃗₁ ir vienā virzienā",
                       "3)  |Δv⃗| = 8,0 + 8,0 = 16 m/s"],
             atbilde="|Δv⃗| = 16 m/s virzienā prom no sienas.",
             piezime="Modulis nemainījās, bet izmaiņa nav nulle - tāpēc "
                     "siena darbojas ar spēku."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Vektorus saskaita ģeometriski - pēc trijstūra vai "
            "paralelograma likuma.",
            "Vienā virzienā moduļus saskaita, pretēji - atņem.",
            "Perpendikulāriem vektoriem F = √(F₁² + F₂²).",
            "a⃗ − b⃗ = a⃗ + (−b⃗).",
        ],
        majasdarbs=[
            "F₁ = 8 N un F₂ = 6 N. Aprēķini kopspēku, ja tie ir: "
            "a) vienā virzienā; b) pretēji; c) perpendikulāri.",
            "Cilvēks iet 60 m uz dienvidiem, tad 80 m uz rietumiem. "
            "Aprēķini ceļu un pārvietojumu.",
            "Uzzīmē mērogā divus perpendikulārus spēkus 30 N un 40 N un "
            "to kopspēku.",
        ],
        pasvertejums=["Protu saskaitīt vektorus zīmējot",
                      "Protu aprēķināt kopvektoru",
                      "Protu atņemt vektorus",
                      "Protu izvēlēties pareizo gadījumu"],
        nakama="Nākamā stunda: vektora projekcijas."),
),

dict(
    nr="1.4", virsraksts="Vektora projekcijas",
    jautajums="Kā vektoru pierakstīt ar skaitļiem?",
    apaksraksts="Koordinātu ass · Projekcija · Zīme · Modulis",
    merkis="Iemācīties atrast vektora projekcijas uz koordinātu asīm un "
           "no projekcijām aprēķināt vektora moduli un virzienu.",
    protu=["atrast vektora projekciju uz ass;",
           "pareizi noteikt projekcijas zīmi;",
           "aprēķināt moduli no projekcijām;",
           "saskaitīt vektorus, izmantojot projekcijas."],
    atkartojums="1.3. stundā vektorus saskaitījām zīmējot. Projekcijas "
                "ļauj to izdarīt ar skaitļiem - precīzi un ātri.",
    uzdevumu_apraksts="Projekcijas, zīmes un modulis",
    teorija=[
        ("Kas ir projekcija", [
            ("formula", "PROJEKCIJAS UZ ASĪM",
             "aₓ = a · cos α        a_y = a · sin α        "
             "a = √(aₓ² + a_y²)",
             "Leņķi α mēra no x ass. Projekcija ir SKALĀRS - tā var būt "
             "pozitīva, negatīva vai nulle.", GOLD),
            ("kartitas", [
                ("POZITĪVA", GREEN,
                 ["Vektora projekcija vērsta uz ass pozitīvo pusi.",
                  "Piemērs: aₓ = +5 m/s"]),
                ("NEGATĪVA", RED,
                 ["Projekcija vērsta pretēji asij.",
                  "Piemērs: aₓ = −5 m/s"]),
                ("NULLE", GREY,
                 ["Vektors perpendikulārs asij.",
                  "Piemērs: a_y = 0"]),
            ]),
        ]),
        ("Kāpēc projekcijas ir ērtas", [
            ("panelis", "SASKAITĪŠANA AR PROJEKCIJĀM",
             ["Katru vektoru sadala projekcijās uz x un y.  Projekcijas "
              "saskaita atsevišķi:  Rₓ = a ₓ + bₓ  un  R_y = a_y + b_y.",
              "Pēc tam moduli atrod ar Pitagora teorēmu:",
              "R = √(Rₓ² + R_y²)"], NAVY),
            ("tabula",
             ["Leņķis α", "cos α", "sin α", "Piemērs"],
             [["0°", "1", "0", "vektors gar x asi"],
              ["30°", "0,87", "0,50", "slīpa plakne"],
              ["45°", "0,71", "0,71", "vienādas projekcijas"],
              ["60°", "0,50", "0,87", "stāva plakne"],
              ["90°", "0", "1", "vektors gar y asi"]],
             [2.90, 2.60, 2.60, 4.13]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Projekcijas aprēķins",
             teksts="Spēks F = 100 N vērsts 30° leņķī pret horizontu.\n"
                    "Aprēķini abas projekcijas!",
             dots=["F = 100 N", "α = 30°"],
             jaaprekina=["Fₓ = ?", "F_y = ?"],
             formulas=["Fₓ = F · cos α", "F_y = F · sin α"],
             aprekins=["1)  Fₓ = 100 · cos 30° = 100 · 0,87",
                       "2)  Fₓ = 87 N",
                       "3)  F_y = 100 · sin 30° = 100 · 0,50 = 50 N"],
             atbilde="Fₓ = 87 N ;   F_y = 50 N",
             piezime="Pārbaude: √(87² + 50²) ≈ 100 N ✔"),
        dict(nr=2, virsraksts="Modulis no projekcijām",
             teksts="Ātruma projekcijas ir vₓ = −6,0 m/s un\n"
                    "v_y = 8,0 m/s. Aprēķini ātruma moduli!",
             dots=["vₓ = −6,0 m/s", "v_y = 8,0 m/s"],
             jaaprekina=["v = ?"],
             formulas=["v = √(vₓ² + v_y²)"],
             aprekins=["1)  vₓ² = 36 ;  v_y² = 64",
                       "2)  v² = 36 + 64 = 100 m²/s²",
                       "3)  v = 10 m/s"],
             atbilde="v = 10 m/s",
             piezime="Modulis vienmēr ir pozitīvs, kaut arī projekcija "
                     "bija negatīva."),
        dict(nr=3, virsraksts="Projekcijas zīme",
             teksts="Ķermenis kustas pa x asi pa kreisi ar ātrumu "
                    "12 m/s.\nKāda ir ātruma projekcija uz x ass?",
             dots=["v = 12 m/s", "virziens pa kreisi"],
             jaaprekina=["vₓ = ?"],
             formulas=["Zīme - pēc virziena attiecībā pret asi"],
             aprekins=["1)  x ass pozitīvais virziens - pa labi",
                       "2)  Kustība - pretēji asij",
                       "3)  vₓ = −12 m/s"],
             atbilde="vₓ = −12 m/s",
             piezime="Mīnusa zīme nozīmē virzienu, nevis negatīvu "
                     "ātrumu."),
        dict(nr=4, virsraksts="Saskaitīšana ar projekcijām",
             teksts="Uz ķermeni darbojas F₁ = 30 N gar x asi un\n"
                    "F₂ = 40 N gar y asi. Aprēķini kopspēku un leņķi!",
             dots=["F₁ₓ = 30 N", "F₂_y = 40 N"],
             jaaprekina=["F = ?", "tg α = ?"],
             formulas=["Rₓ = 30 N ;  R_y = 40 N",
                       "F = √(Rₓ² + R_y²)", "tg α = R_y / Rₓ"],
             aprekins=["1)  F² = 900 + 1600 = 2500 N²",
                       "2)  F = 50 N",
                       "3)  tg α = 40 : 30 = 1,33 → α ≈ 53°"],
             atbilde="F = 50 N ;   α ≈ 53° no x ass",
             piezime="Šo metodi izmantosim visos spēku uzdevumos."),
        dict(nr=5, virsraksts="Projekcijas 60° leņķī",
             teksts="Virve velk ragavas ar spēku 200 N, kas vērsts 60° "
                    "leņķī\npret horizontu. Aprēķini abas projekcijas!",
             dots=["F = 200 N", "α = 60°"],
             jaaprekina=["Fₓ = ?", "F_y = ?"],
             formulas=["Fₓ = F · cos α", "F_y = F · sin α"],
             aprekins=["1)  Fₓ = 200 · cos 60° = 200 · 0,50",
                       "2)  Fₓ = 100 N",
                       "3)  F_y = 200 · sin 60° = 200 · 0,87 = 173 N"],
             atbilde="Fₓ = 100 N ;   F_y ≈ 1,7·10² N",
             piezime="Jo stāvāks leņķis, jo mazāka horizontālā "
                     "projekcija - vilkt kļūst neizdevīgi."),
        dict(nr=6, virsraksts="Leņķis no projekcijām",
             teksts="Pārvietojuma projekcijas ir dₓ = 9,0 m un\n"
                    "d_y = 12 m. Aprēķini moduli un leņķi pret x asi!",
             dots=["dₓ = 9,0 m", "d_y = 12 m"],
             jaaprekina=["d = ?", "α = ?"],
             formulas=["d = √(dₓ² + d_y²)", "tg α = d_y / dₓ"],
             aprekins=["1)  d² = 81 + 144 = 225 m²",
                       "2)  d = 15 m",
                       "3)  tg α = 12 : 9,0 = 1,33 → α ≈ 53°"],
             atbilde="d = 15 m ;   α ≈ 53° pret x asi",
             piezime="Atkal 3-4-5 trijstūris, reizināts ar 3."),
        dict(nr=7, virsraksts="Trīs spēki projekcijās",
             teksts="Uz ķermeni darbojas F₁ = 40 N gar +x, F₂ = 30 N gar "
                    "+y\nun F₃ = 20 N gar −x. Aprēķini kopspēku!",
             dots=["F₁ₓ = 40 N", "F₂_y = 30 N", "F₃ₓ = −20 N"],
             jaaprekina=["R = ?"],
             formulas=["Rₓ = F₁ₓ + F₃ₓ", "R_y = F₂_y",
                       "R = √(Rₓ² + R_y²)"],
             aprekins=["1)  Rₓ = 40 − 20 = 20 N",
                       "2)  R_y = 30 N",
                       "3)  R = √(400 + 900) = √1300 ≈ 36 N"],
             atbilde="R ≈ 36 N",
             piezime="Projekciju metode der jebkuram spēku skaitam - "
                     "zīmējums vairs nav vajadzīgs."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Projekcija ir skalārs ar zīmi: aₓ = a·cos α, a_y = a·sin α.",
            "Zīme rāda virzienu attiecībā pret asi.",
            "Modulis: a = √(aₓ² + a_y²) - vienmēr pozitīvs.",
            "Vektorus ērti saskaitīt, saskaitot projekcijas atsevišķi.",
        ],
        majasdarbs=[
            "F = 60 N, α = 60°. Aprēķini abas projekcijas.",
            "vₓ = 9,0 m/s, v_y = −12 m/s. Aprēķini moduli.",
            "Sagatavojies PD1: atkārto vektoru saskaitīšanu un "
            "projekcijas.",
        ],
        pasvertejums=["Protu aprēķināt projekcijas",
                      "Protu noteikt zīmi",
                      "Protu atrast moduli",
                      "Esmu gatavs PD1"],
        nakama="Nākamā stunda: PD1 - Vektori un fizikālie lielumi."),
),

dict(
    nr="1.5", virsraksts="Mehāniskā kustība",
    jautajums="Kustas vai stāv - salīdzinot ar ko?",
    apaksraksts="Atskaites sistēma · Materiālais punkts · Trajektorija",
    merkis="Saprast, ka kustība vienmēr ir relatīva, un iemācīties "
           "izvēlēties atskaites sistēmu un vienkāršotu modeli.",
    protu=["nosaukt atskaites sistēmas daļas;",
           "paskaidrot, kāpēc kustība ir relatīva;",
           "pamatot, kad ķermeni var uzskatīt par materiālu punktu;",
           "atšķirt trajektoriju no ceļa."],
    atkartojums="Iepriekšējās stundās mācījāmies aprakstīt lielumus. "
                "Tagad sākam aprakstīt kustību - fizikas pamatuzdevumu.",
    uzdevumu_apraksts="Atskaites sistēma un relatīvā kustība",
    teorija=[
        ("Atskaites sistēma", [
            ("kartitas", [
                ("ATSKAITES ĶERMENIS", BLUE,
                 ["Pret ko mēra stāvokli.",
                  "Piemērs: Zeme, vilciens, ceļa mala."]),
                ("KOORDINĀTU SISTĒMA", GREEN,
                 ["Ass vai asis ar sākumpunktu.",
                  "Ļauj pierakstīt stāvokli ar skaitli."]),
                ("PULKSTENIS", GOLD,
                 ["Mēra laiku.",
                  "Bez laika kustību aprakstīt nevar."]),
            ]),
            ("panelis", "KUSTĪBA IR RELATĪVA",
             ["Pasažieris vilcienā sēž nekustīgi attiecībā pret vagonu, "
              "bet pārvietojas 120 km/h attiecībā pret Zemi. Abi "
              "apgalvojumi ir pareizi - atšķiras tikai atskaites "
              "ķermenis. Tāpēc uzdevumā vienmēr jānorāda, pret ko mēra."],
             NAVY),
        ]),
        ("Vienkāršošana un trajektorija", [
            ("divi",
             ("MATERIĀLAIS PUNKTS", BLUE,
              ["Ķermeni uzskata par punktu, ja tā izmēri ir mazi "
               "salīdzinājumā ar ceļu.",
               "Lidmašīna lidojumā Rīga-Roma - punkts.",
               "Tā pati lidmašīna, novietojot angārā - nav punkts."]),
             ("TRAJEKTORIJA", GREEN,
              ["Līnija, pa kuru ķermenis kustas.",
               "Taisnvirziena vai līklīnijas kustība.",
               "Trajektorijas garums = ceļš s."])),
            ("formula", "SVARĪGI ATCERĒTIES",
             "Trajektorijas forma ir atkarīga no atskaites sistēmas.",
             "Krītošs akmens vilcienā: pasažierim - taisne lejup; "
             "cilvēkam uz perona - parabola.", GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Kustība vai miers",
             teksts="Autobusa pasažieris sēž krēslā. Autobuss brauc "
                    "60 km/h.\nVai pasažieris kustas? Atbildi pamato "
                    "abām atskaites sistēmām!",
             dots=["v(autobusa) = 60 km/h"],
             jaaprekina=["v pret autobusu = ?", "v pret Zemi = ?"],
             formulas=["Kustība ir relatīva"],
             aprekins=["1)  Pret autobusu: v = 0 (miers)",
                       "2)  Pret Zemi: v = 60 km/h",
                       "3)  Abas atbildes ir pareizas"],
             atbilde="Pret autobusu - miers; pret Zemi - 60 km/h.",
             piezime="Vienmēr norādi atskaites ķermeni!"),
        dict(nr=2, virsraksts="Materiālais punkts",
             teksts="Kuros gadījumos automašīnu (garums 4,5 m) var "
                    "uzskatīt\npar materiālu punktu:\n"
                    "a) brauciens Rīga-Liepāja 200 km;\n"
                    "b) iebraukšana garāžā 6 m?",
             dots=["l = 4,5 m", "a) s = 200 km", "b) s = 6 m"],
             jaaprekina=["Vai var uzskatīt par punktu?"],
             formulas=["Var, ja l ≪ s"],
             aprekins=["1)  a) 4,5 m ≪ 200 000 m → var",
                       "2)  b) 4,5 m ≈ 6 m → nevar",
                       "3)  Izšķir izmēru attiecība"],
             atbilde="a) var;  b) nevar - izmēri ir būtiski.",
             piezime="Modelis der tikai noteiktos apstākļos."),
        dict(nr=3, virsraksts="Trajektorija",
             teksts="Velosipēda ritenim ir atzīme uz riepas.\n"
                    "Kāda ir atzīmes trajektorija: a) pret velosipēdistu; "
                    "b) pret ceļu?",
             dots=["ritenis rit bez slīdēšanas"],
             jaaprekina=["trajektorijas forma"],
             formulas=["Trajektorija atkarīga no atskaites sistēmas"],
             aprekins=["1)  a) Pret velosipēdistu - riņķa līnija",
                       "2)  b) Pret ceļu - cikloīda (velkošas cilpas)",
                       "3)  Viens un tas pats punkts, divas formas"],
             atbilde="a) riņķa līnija;  b) cikloīda.",
             piezime="Tas pierāda, ka trajektorija nav ķermeņa īpašība."),
        dict(nr=4, virsraksts="Koordināta uz ass",
             teksts="Uz x ass ķermenis atrodas punktā x₁ = 12 m, pēc "
                    "kāda laika\nx₂ = −5 m. Aprēķini pārvietojuma "
                    "projekciju!",
             dots=["x₁ = 12 m", "x₂ = −5 m"],
             jaaprekina=["dₓ = ?"],
             formulas=["dₓ = x₂ − x₁"],
             aprekins=["1)  dₓ = −5 − 12",
                       "2)  dₓ = −17 m",
                       "3)  Modulis |d| = 17 m, virziens - pretēji asij"],
             atbilde="dₓ = −17 m ;   |d⃗| = 17 m",
             piezime="Pārvietojuma projekciju vienmēr rēķina kā beigu "
                     "mīnus sākuma koordināta."),
        dict(nr=5, virsraksts="Atskaites sistēma lidmašīnā",
             teksts="Lidmašīna lido ar 900 km/h. Stjuarts iet pa salonu "
                    "uz\npriekšu ar 4 km/h. Kāds ir viņa ātrums pret "
                    "lidmašīnu un pret Zemi?",
             dots=["v(lidmašīnas) = 900 km/h", "v(stjuarta) = 4 km/h"],
             jaaprekina=["v pret lidmašīnu = ?", "v pret Zemi = ?"],
             formulas=["Ātrums ir atkarīgs no atskaites ķermeņa"],
             aprekins=["1)  Pret lidmašīnu: v = 4 km/h",
                       "2)  Pret Zemi: v = 900 + 4",
                       "3)  v = 904 km/h"],
             atbilde="Pret lidmašīnu 4 km/h ;   pret Zemi 904 km/h.",
             piezime="Abas vērtības ir pareizas - atšķiras tikai "
                     "atskaites ķermenis."),
        dict(nr=6, virsraksts="Zeme kā materiāls punkts",
             teksts="Vai Zemi (R = 6400 km) var uzskatīt par materiālu "
                    "punktu:\na) aprakstot kustību ap Sauli "
                    "(1,5·10⁸ km);\nb) aprakstot diennakts maiņu?",
             dots=["R(Zemes) = 6,4·10³ km", "a) L = 1,5·10⁸ km"],
             jaaprekina=["Vai var uzskatīt par punktu?"],
             formulas=["Var, ja izmēri ≪ attālums"],
             aprekins=["1)  a) 6,4·10³ ≪ 1,5·10⁸ km → var",
                       "2)  b) griešanās notiek ap pašas asi",
                       "3)  b) izmēri ir būtiski → nevar"],
             atbilde="a) var;  b) nevar - punktam griešanos aprakstīt "
                     "nevar.",
             piezime="Viens un tas pats ķermenis vienā uzdevumā ir "
                     "punkts, citā - nav."),
        dict(nr=7, virsraksts="Ceļš un koordināta uz ass",
             teksts="Ķermenis pa x asi pāriet no x₀ = 4 m uz x₁ = 20 m "
                    "un\ntad uz x₂ = −6 m. Aprēķini ceļu un "
                    "pārvietojuma projekciju!",
             dots=["x₀ = 4 m", "x₁ = 20 m", "x₂ = −6 m"],
             jaaprekina=["s = ?", "dₓ = ?"],
             formulas=["s = |x₁ − x₀| + |x₂ − x₁|", "dₓ = x₂ − x₀"],
             aprekins=["1)  s₁ = |20 − 4| = 16 m",
                       "2)  s₂ = |−6 − 20| = 26 m ;  s = 42 m",
                       "3)  dₓ = −6 − 4 = −10 m"],
             atbilde="s = 42 m ;   dₓ = −10 m",
             piezime="Ceļu saskaita pa posmiem, pārvietojumu rēķina "
                     "tikai no gala koordinātām."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Atskaites sistēma = atskaites ķermenis + koordinātu sistēma "
            "+ pulkstenis.",
            "Kustība un miers ir relatīvi jēdzieni.",
            "Materiālais punkts der, ja ķermeņa izmēri ir mazi pret ceļu.",
            "Trajektorijas forma ir atkarīga no atskaites sistēmas.",
        ],
        majasdarbs=[
            "Nosauc divus gadījumus, kad Zemi var uzskatīt par materiālu "
            "punktu, un divus, kad nevar.",
            "x₁ = −8 m, x₂ = 15 m. Aprēķini pārvietojuma projekciju.",
            "Apraksti lidmašīnas propellera gala trajektoriju pret "
            "lidmašīnu un pret zemi.",
        ],
        pasvertejums=["Protu nosaukt atskaites sistēmas daļas",
                      "Protu pamatot kustības relativitāti",
                      "Protu lietot materiālā punkta modeli",
                      "Protu aprēķināt pārvietojuma projekciju"],
        nakama="Nākamā stunda: ceļš un pārvietojums."),
),

dict(
    nr="1.6", virsraksts="Ceļš un pārvietojums",
    jautajums="Kāpēc ceļš un pārvietojums nav viens un tas pats?",
    apaksraksts="s - skalārs · d⃗ - vektors · s ≥ |d⃗|",
    merkis="Iemācīties atšķirt ceļu no pārvietojuma un aprēķināt abus "
           "lielumus dažādās trajektorijās.",
    protu=["definēt ceļu un pārvietojumu;",
           "aprēķināt abus lielumus dotai trajektorijai;",
           "pamatot, kāpēc s ≥ |d⃗|;",
           "noteikt, kad ceļš ir vienāds ar pārvietojumu."],
    atkartojums="1.5. stundā: trajektorija ir līnija, pa kuru ķermenis "
                "kustas. Tās garums ir ceļš. Bet no sākuma līdz beigām "
                "ved arī taisne - pārvietojums.",
    uzdevumu_apraksts="Ceļš un pārvietojums dažādās trajektorijās",
    teorija=[
        ("Divi kustības raksturlielumi", [
            ("divi",
             ("CEĻŠ  s", BLUE,
              ["Trajektorijas garums.",
               "SKALĀRS - tikai skaitlis ar mērvienību.",
               "Vienmēr pieaug, nekad nesamazinās.",
               "Mēra metros."]),
             ("PĀRVIETOJUMS  d⃗", RED,
              ["Vektors no sākuma uz beigu punktu.",
               "VEKTORS - modulis un virziens.",
               "Var būt nulle, arī ja ceļš nav nulle.",
               "Mēra metros."])),
            ("formula", "SVARĪGĀKĀ SAKARĪBA",
             "s ≥ |d⃗|        s = |d⃗|  tikai taisnvirziena kustībā "
             "bez atgriešanās",
             "Ceļš nekad nevar būt mazāks par pārvietojuma moduli.", GOLD),
        ]),
        ("Tipiskās situācijas", [
            ("tabula",
             ["Situācija", "Ceļš s", "Pārvietojums |d⃗|"],
             [["Taisni 100 m uz priekšu", "100 m", "100 m"],
              ["50 m turp un 50 m atpakaļ", "100 m", "0 m"],
              ["Aplis ar rādiusu R (viss)", "2πR", "0 m"],
              ["Puse apļa ar rādiusu R", "πR", "2R"]],
             [6.20, 3.10, 3.93]),
            ("panelis", "KUR TAS SVARĪGI",
             ["Navigācijas lietotne rāda gan attālumu pa ceļu (ceļš), gan "
              "attālumu taisnā līnijā (pārvietojuma modulis). Degvielas "
              "patēriņš ir atkarīgs no ceļa, bet mobilā signāla stiprums - "
              "no pārvietojuma."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Turp un atpakaļ",
             teksts="Skrējējs noskrien 400 m pa stadionu un atgriežas "
                    "starta\nvietā. Aprēķini ceļu un pārvietojumu!",
             dots=["viens aplis = 400 m"],
             jaaprekina=["s = ?", "|d⃗| = ?"],
             formulas=["s = trajektorijas garums",
                       "d⃗ - no sākuma uz beigām"],
             aprekins=["1)  s = 400 m",
                       "2)  Sākuma un beigu punkts sakrīt",
                       "3)  |d⃗| = 0 m"],
             atbilde="s = 400 m ;   |d⃗| = 0 m",
             piezime="Ceļš nav nulle, bet pārvietojums ir - tas ir "
                     "normāli."),
        dict(nr=2, virsraksts="Puse apļa",
             teksts="Ķermenis pārvietojas pa pusapli ar rādiusu 20 m.\n"
                    "Aprēķini ceļu un pārvietojumu! (π ≈ 3,14)",
             dots=["R = 20 m", "puse apļa"],
             jaaprekina=["s = ?", "|d⃗| = ?"],
             formulas=["s = πR", "|d⃗| = 2R (diametrs)"],
             aprekins=["1)  s = 3,14 · 20 = 62,8 m",
                       "2)  |d⃗| = 2 · 20 = 40 m",
                       "3)  Pārbaude: 62,8 > 40 ✔"],
             atbilde="s = 62,8 m ;   |d⃗| = 40 m",
             piezime="s vienmēr lielāks vai vienāds ar |d⃗|."),
        dict(nr=3, virsraksts="Lauzta trajektorija",
             teksts="Cilvēks iet 90 m uz ziemeļiem, tad 120 m uz "
                    "austrumiem.\nAprēķini ceļu un pārvietojumu!",
             dots=["s₁ = 90 m (Z)", "s₂ = 120 m (A)"],
             jaaprekina=["s = ?", "|d⃗| = ?"],
             formulas=["s = s₁ + s₂", "|d⃗| = √(s₁² + s₂²)"],
             aprekins=["1)  s = 90 + 120 = 210 m",
                       "2)  |d⃗|² = 8100 + 14 400 = 22 500 m²",
                       "3)  |d⃗| = 150 m"],
             atbilde="s = 210 m ;   |d⃗| = 150 m",
             piezime="Atkal 3-4-5 trijstūris, tikai reizināts ar 30."),
        dict(nr=4, virsraksts="Kad tie sakrīt",
             teksts="Automašīna brauc pa taisnu šoseju 12 km vienā "
                    "virzienā\nun neapgriežas. Salīdzini ceļu un "
                    "pārvietojumu!",
             dots=["taisna trajektorija", "s = 12 km"],
             jaaprekina=["|d⃗| = ?"],
             formulas=["Taisnvirziena kustībā bez atgriešanās  s = |d⃗|"],
             aprekins=["1)  Trajektorija - taisne",
                       "2)  Virziens nemainās",
                       "3)  |d⃗| = 12 km = 1,2·10⁴ m"],
             atbilde="s = |d⃗| = 12 km",
             piezime="Tas ir vienīgais gadījums, kad abi lielumi ir "
                     "vienādi."),
        dict(nr=5, virsraksts="Ceturtdaļa apļa",
             teksts="Ķermenis pārvietojas pa ceturtdaļu riņķa līnijas "
                    "ar\nrādiusu 50 m. Aprēķini ceļu un pārvietojumu! "
                    "(π ≈ 3,14)",
             dots=["R = 50 m", "ceturtdaļa apļa"],
             jaaprekina=["s = ?", "|d⃗| = ?"],
             formulas=["s = 2πR : 4", "|d⃗| = R√2"],
             aprekins=["1)  s = 2 · 3,14 · 50 : 4 = 78,5 m",
                       "2)  |d⃗| = 50 · 1,41",
                       "3)  |d⃗| ≈ 71 m"],
             atbilde="s ≈ 78,5 m ;   |d⃗| ≈ 71 m",
             piezime="Gala punktus savieno horda - tā ir kvadrāta "
                     "diagonāle ar malu R."),
        dict(nr=6, virsraksts="Lifts augšup un lejup",
             teksts="Lifts paceļas par 12 m, tad nolaižas par 5 m.\n"
                    "Aprēķini ceļu un pārvietojumu!",
             dots=["s₁ = 12 m (augšup)", "s₂ = 5 m (lejup)"],
             jaaprekina=["s = ?", "|d⃗| = ?"],
             formulas=["s = s₁ + s₂", "d_y = s₁ − s₂"],
             aprekins=["1)  s = 12 + 5 = 17 m",
                       "2)  d_y = 12 − 5 = 7 m",
                       "3)  |d⃗| = 7 m augšup"],
             atbilde="s = 17 m ;   |d⃗| = 7 m augšup",
             piezime="Pretējos virzienos vērstus pārvietojumus atņem, "
                     "ceļus - vienmēr saskaita."),
        dict(nr=7, virsraksts="Pusotrs aplis",
             teksts="Skrējējs veic 1,5 apļus pa 400 m stadionu.\n"
                    "Aprēķini ceļu un pārvietojumu! (π ≈ 3,14)",
             dots=["viens aplis = 400 m", "n = 1,5"],
             jaaprekina=["s = ?", "|d⃗| = ?"],
             formulas=["s = n · 400 m", "400 = 2πR", "|d⃗| = 2R"],
             aprekins=["1)  s = 1,5 · 400 = 600 m",
                       "2)  R = 400 : (2 · 3,14) = 63,7 m",
                       "3)  |d⃗| = 2 · 63,7 ≈ 127 m"],
             atbilde="s = 600 m ;   |d⃗| ≈ 1,3·10² m",
             piezime="Pēc pusotra apļa skrējējs ir stadiona pretējā "
                     "pusē - tur beidzas pārvietojums."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Ceļš s ir trajektorijas garums - skalārs.",
            "Pārvietojums d⃗ ir vektors no sākuma uz beigu punktu.",
            "Vienmēr s ≥ |d⃗|.",
            "s = |d⃗| tikai taisnvirziena kustībā vienā virzienā.",
        ],
        majasdarbs=[
            "Ķermenis apiet kvadrātu ar malu 25 m. Aprēķini ceļu un "
            "pārvietojumu.",
            "Cilvēks iet 200 m uz priekšu un 80 m atpakaļ. Aprēķini "
            "abus lielumus.",
            "Aplis R = 5,0 m; ķermenis veic ceturtdaļu apļa. Aprēķini "
            "ceļu un pārvietojumu.",
        ],
        pasvertejums=["Protu definēt ceļu un pārvietojumu",
                      "Protu tos aprēķināt",
                      "Protu pamatot s ≥ |d⃗|",
                      "Protu atpazīt, kad tie sakrīt"],
        nakama="Nākamā stunda: vienmērīga taisnvirziena kustība."),
),

dict(
    nr="1.7", virsraksts="Vienmērīga taisnvirziena kustība",
    jautajums="Ko nozīmē 20 metri sekundē?",
    apaksraksts="v = s/t · v = const · Mērvienības",
    merkis="Iemācīties lietot sakarību v = s/t vienmērīgā taisnvirziena "
           "kustībā un pārveidot ātruma mērvienības.",
    protu=["definēt vienmērīgu taisnvirziena kustību;",
           "lietot v = s/t un izteikt no tās s un t;",
           "pārveidot km/h un m/s;",
           "pārbaudīt rezultāta ticamību."],
    atkartojums="1.6. stundā: taisnvirziena kustībā s = |d⃗|. Tagad "
                "pievienojam laiku un iegūstam ātrumu.",
    uzdevumu_apraksts="Ātrums, ceļš un laiks vienmērīgā kustībā",
    teorija=[
        ("Ātrums vienmērīgā kustībā", [
            ("formula", "PAMATSAKARĪBA",
             "v = s / t        s = v · t        t = s / v",
             "Vienmērīgā taisnvirziena kustībā ātrums nemainās: par "
             "vienādiem laika sprīžiem ķermenis veic vienādus ceļus. "
             "[v] = m/s.", GOLD),
            ("kartitas", [
                ("VIENMĒRĪGA", GREEN,
                 ["v = const",
                  "Piemērs: eskalators, konveijers.",
                  "Grafiks v(t) - horizontāla taisne."]),
                ("NEVIENMĒRĪGA", RED,
                 ["v mainās.",
                  "Piemērs: pilsētas satiksme.",
                  "Lieto vidējo ātrumu."]),
                ("MĒRVIENĪBAS", BLUE,
                 ["1 m/s = 3,6 km/h",
                  "km/h → m/s: dala ar 3,6",
                  "m/s → km/h: reizina ar 3,6"]),
            ]),
        ]),
        ("Tipiski ātrumi", [
            ("tabula",
             ["Objekts", "Ātrums m/s", "Ātrums km/h"],
             [["Cilvēks iet", "1,4", "5"],
              ["Velosipēds", "5,6", "20"],
              ["Automašīna pilsētā", "13,9", "50"],
              ["Skaņa gaisā", "340", "1224"],
              ["Gaisma vakuumā", "3,0·10⁸", "1,08·10⁹"]],
             [5.60, 3.50, 3.13]),
            ("panelis", "TICAMĪBAS PĀRBAUDE",
             ["Pirms atbildes pieraksta vienmēr novērtē: vai skaitlis ir "
              "reāls? Ja cilvēka ātrums iznāk 50 m/s, kaut kur ir kļūda - "
              "tas ir 180 km/h."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Ātruma aprēķins",
             teksts="Vilciens 240 km attālumu veic 2 h 40 min laikā.\n"
                    "Aprēķini ātrumu m/s un km/h!",
             dots=["s = 240 km = 2,4·10⁵ m", "t = 2 h 40 min = 9600 s"],
             jaaprekina=["v = ?"],
             formulas=["v = s / t"],
             aprekins=["1)  t = 2·3600 + 40·60 = 9600 s",
                       "2)  v = 240 000 : 9600 = 25 m/s",
                       "3)  v = 25 · 3,6 = 90 km/h"],
             atbilde="v = 25 m/s = 90 km/h",
             piezime="Reāls vilciena ātrums - ticamības pārbaude "
                     "izturēta."),
        dict(nr=2, virsraksts="Ceļa aprēķins",
             teksts="Velosipēdists brauc ar ātrumu 18 km/h 45 minūtes.\n"
                    "Cik lielu ceļu viņš veic?",
             dots=["v = 18 km/h = 5,0 m/s", "t = 45 min = 2700 s"],
             jaaprekina=["s = ?"],
             formulas=["s = v · t"],
             aprekins=["1)  v = 18 : 3,6 = 5,0 m/s",
                       "2)  t = 45 · 60 = 2700 s",
                       "3)  s = 5,0 · 2700 = 13 500 m = 13,5 km"],
             atbilde="s = 1,35·10⁴ m = 13,5 km",
             piezime="Var arī rēķināt km un h: 18 · 0,75 = 13,5 km ✔"),
        dict(nr=3, virsraksts="Laika aprēķins",
             teksts="Skaņas ātrums gaisā ir 340 m/s. Pēc cik ilga laika\n"
                    "atskan pērkons, ja zibens uzsper 1,7 km attālumā?",
             dots=["v = 340 m/s", "s = 1,7 km = 1700 m"],
             jaaprekina=["t = ?"],
             formulas=["t = s / v"],
             aprekins=["1)  s = 1,7 · 1000 = 1700 m",
                       "2)  t = 1700 : 340",
                       "3)  t = 5,0 s"],
             atbilde="t = 5,0 s",
             piezime="Praktisks noteikums: 3 sekundes ≈ 1 km."),
        dict(nr=4, virsraksts="Divi posmi",
             teksts="Automašīna 30 min brauc ar 60 km/h, tad 30 min ar\n"
                    "100 km/h. Cik lielu kopējo ceļu tā veic?",
             dots=["v₁ = 60 km/h", "v₂ = 100 km/h", "t₁ = t₂ = 0,50 h"],
             jaaprekina=["s = ?"],
             formulas=["s₁ = v₁t₁", "s₂ = v₂t₂", "s = s₁ + s₂"],
             aprekins=["1)  s₁ = 60 · 0,50 = 30 km",
                       "2)  s₂ = 100 · 0,50 = 50 km",
                       "3)  s = 30 + 50 = 80 km"],
             atbilde="s = 80 km = 8,0·10⁴ m",
             piezime="Katram posmam ar nemainīgu ātrumu formulu lieto "
                     "atsevišķi."),
        dict(nr=5, virsraksts="Reakcijas ceļš",
             teksts="Automašīna brauc ar 108 km/h. Cik lielu ceļu tā "
                    "veic\nvadītāja reakcijas laikā 0,80 s?",
             dots=["v = 108 km/h", "t = 0,80 s"],
             jaaprekina=["v (m/s) = ?", "s = ?"],
             formulas=["v(m/s) = v(km/h) : 3,6", "s = v · t"],
             aprekins=["1)  v = 108 : 3,6 = 30 m/s",
                       "2)  s = 30 · 0,80",
                       "3)  s = 24 m"],
             atbilde="s = 24 m",
             piezime="Šo ceļu automašīna veic, pirms vadītājs vēl "
                     "pieskaras bremzēm."),
        dict(nr=6, virsraksts="Gaismas ceļš",
             teksts="Attālums no Zemes līdz Mēnesim ir 3,84·10⁸ m.\n"
                    "Cik ilgā laikā to veic gaisma? (c = 3,0·10⁸ m/s)",
             dots=["s = 3,84·10⁸ m", "c = 3,0·10⁸ m/s"],
             jaaprekina=["t = ?"],
             formulas=["t = s / c"],
             aprekins=["1)  t = 3,84·10⁸ : 3,0·10⁸",
                       "2)  t = 1,28 s",
                       "3)  t ≈ 1,3 s"],
             atbilde="t ≈ 1,3 s",
             piezime="Tāpēc sarunā ar Mēnesi atbildi dzird tikai pēc "
                     "aptuveni 2,6 s."),
        dict(nr=7, virsraksts="Divi velosipēdisti",
             teksts="Divi velosipēdisti vienlaikus izbrauc no vienas "
                    "vietas\nvienā virzienā ar 5,0 m/s un 7,0 m/s. Cik "
                    "liels attālums starp tiem ir pēc 10 min?",
             dots=["v₁ = 5,0 m/s", "v₂ = 7,0 m/s", "t = 10 min = 600 s"],
             jaaprekina=["Δs = ?"],
             formulas=["s = v · t", "Δs = s₂ − s₁"],
             aprekins=["1)  s₁ = 5,0 · 600 = 3000 m",
                       "2)  s₂ = 7,0 · 600 = 4200 m",
                       "3)  Δs = 4200 − 3000 = 1200 m"],
             atbilde="Δs = 1200 m = 1,2 km",
             piezime="Ātrāk: Δs = (v₂ − v₁)·t = 2,0 · 600 = 1200 m."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Vienmērīgā taisnvirziena kustībā v = const.",
            "v = s/t;  s = v·t;  t = s/v.",
            "1 m/s = 3,6 km/h.",
            "Rezultātu vienmēr pārbauda pēc ticamības.",
        ],
        majasdarbs=[
            "s = 4,5 km, t = 15 min. Aprēķini v (m/s un km/h).",
            "v = 72 km/h, t = 25 s. Aprēķini s.",
            "Gaismai no Saules līdz Zemei (1,5·10¹¹ m) - cik ilgi? "
            "(c = 3,0·10⁸ m/s)",
        ],
        pasvertejums=["Protu lietot v = s/t",
                      "Protu izteikt s un t",
                      "Protu pārveidot mērvienības",
                      "Protu pārbaudīt ticamību"],
        nakama="Nākamā stunda: kustības vienādojums un grafiki."),
),

]
