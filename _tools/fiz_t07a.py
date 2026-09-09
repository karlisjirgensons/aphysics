# -*- coding: utf-8 -*-
"""7. temats "Atoma un vielas uzbūve". A daļa: 7.1.-7.6. stunda."""

from fiz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN     # noqa: F401

TEMATS = "7. temats. Atoma un vielas uzbūve"
KICKER = "FIZIKA I · 11. KLASE · 7. TEMATS: ATOMA UN VIELAS UZBŪVE"
KURSS = "FIZIKA I · 11. KLASE"
MAPE = "C:/aphysics/Fizika_1/7. Atoma un vielas uzbūve"

STUNDAS = [

dict(
    nr="7.1", virsraksts="Daļiņu modelis un temperatūra",
    jautajums="Kā temperatūra saistīta ar daļiņu kustību?",
    apaksraksts="Daļiņu modelis · T = t + 273 · ν = m/M",
    merkis="Skaidrot vielas daļiņu modeli, pāriet starp Celsija un "
           "Kelvina skalu un lietot vielas daudzumu.",
    protu=["nosaukt daļiņu modeļa pamatatziņas;",
           "pāriet no grādiem uz kelviniem un atpakaļ;",
           "aprēķināt vielas daudzumu ν = m/M;",
           "aprēķināt daļiņu skaitu vielā."],
    atkartojums="10. klasē pētījām ķermeņu kustību. Tagad tas pats "
                "skatījums, tikai daļiņu līmenī - un tieši daļiņu "
                "kustība nosaka temperatūru.",
    uzdevumu_apraksts="Temperatūras skalas un vielas daudzums",
    teorija=[
        ("Vielas daļiņu modelis", [
            ("panelis", "TRĪS PAMATATZIŅAS",
             ["Viela sastāv no daļiņām - atomiem un molekulām - starp "
              "kurām ir tukšums.",
              "Daļiņas nepārtraukti un haotiski kustas; jo augstāka "
              "temperatūra, jo ātrāk.",
              "Starp daļiņām darbojas pievilkšanās un atgrūšanās spēki - "
              "tie nosaka vielas agregātstāvokli."], NAVY),
            ("kartitas", [
                ("CIETVIELA", BLUE,
                 ["Daļiņas ciešā kārtībā.",
                  "Svārstās ap vietu.",
                  "Sava forma un tilpums."]),
                ("ŠĶIDRUMS", GREEN,
                 ["Daļiņas blakus, bet slīd.",
                  "Maina vietas.",
                  "Sava tilpuma, bez formas."]),
                ("GĀZE", GOLD,
                 ["Daļiņas tālu viena no otras.",
                  "Kustas brīvi un ātri.",
                  "Aizpilda visu trauku."]),
            ]),
        ]),
        ("Temperatūra un vielas daudzums", [
            ("formula", "KELVINA SKALA UN VIELAS DAUDZUMS",
             "T = t + 273        ν = m/M        [ν] = mol",
             "Kelvina skala sākas absolūtajā nullē, kur daļiņu kustība "
             "ir vismazākā. Vielas daudzumu mēra molos; vienā molā ir "
             "6,02·10²³ daļiņas.", GOLD),
            ("tabula",
             ["Situācija", "Celsija skalā", "Kelvina skalā"],
             [["Absolūtā nulle", "−273 °C", "0 K"],
              ["Ledus kūst", "0 °C", "273 K"],
              ["Istabas temperatūra", "20 °C", "293 K"],
              ["Ūdens vārās", "100 °C", "373 K"]],
             [4.30, 3.00, 2.93]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="No grādiem uz kelviniem",
             teksts="Gaisa temperatūra vasarā ir 25 °C, ziemā −18 °C.\n"
                    "Izsaki abas temperatūras kelvinos!",
             dots=["t₁ = 25 °C", "t₂ = −18 °C"],
             jaaprekina=["T₁ = ?", "T₂ = ?"],
             formulas=["T = t + 273"],
             aprekins=["1)  T₁ = 25 + 273 = 298 K",
                       "2)  T₂ = −18 + 273 = 255 K"],
             atbilde="T₁ = 298 K;  T₂ = 255 K",
             piezime="Kelvinos temperatūra nekad nav negatīva - zemāk "
                     "par absolūto nulli nevar atdzist."),
        dict(nr=2, virsraksts="No kelviniem uz grādiem",
             teksts="Gāzes temperatūra ir 350 K.\n"
                    "Cik tas ir Celsija grādos?",
             dots=["T = 350 K"],
             jaaprekina=["t = ?"],
             formulas=["T = t + 273", "t = T − 273"],
             aprekins=["1)  t = 350 − 273",
                       "2)  t = 77 °C"],
             atbilde="t = 77 °C",
             piezime="Temperatūras STARPĪBA abās skalās ir vienāda: "
                     "10 °C starpība ir arī 10 K starpība."),
        dict(nr=3, virsraksts="Vielas daudzums",
             teksts="Traukā ir 36 g ūdens (M = 18 g/mol).\n"
                    "Aprēķini vielas daudzumu!",
             dots=["m = 36 g", "M = 18 g/mol"],
             jaaprekina=["ν = ?"],
             formulas=["ν = m/M"],
             aprekins=["1)  ν = 36 : 18",
                       "2)  ν = 2,0 mol"],
             atbilde="ν = 2,0 mol",
             piezime="Molmasu M ņem no periodiskās tabulas: ūdenim "
                     "2 · 1 + 16 = 18 g/mol."),
        dict(nr=4, virsraksts="Daļiņu skaits",
             teksts="Cik molekulu ir 2,0 mol ūdens?\n"
                    "(N_A = 6,02·10²³ mol⁻¹)",
             dots=["ν = 2,0 mol", "N_A = 6,02·10²³ mol⁻¹"],
             jaaprekina=["N = ?"],
             formulas=["N = ν · N_A"],
             aprekins=["1)  N = 2,0 · 6,02·10²³",
                       "2)  N = 1,204·10²⁴",
                       "3)  N ≈ 1,2·10²⁴ molekulas"],
             atbilde="N ≈ 1,2·10²⁴",
             piezime="Divās ēdamkarotēs ūdens ir vairāk molekulu nekā "
                     "smilšu graudu uz visas Zemes."),
        dict(nr=5, virsraksts="Masa no vielas daudzuma",
             teksts="Traukā ir 0,50 mol oglekļa dioksīda "
                    "(M = 44 g/mol).\nAprēķini gāzes masu!",
             dots=["ν = 0,50 mol", "M = 44 g/mol"],
             jaaprekina=["m = ?"],
             formulas=["ν = m/M", "m = ν · M"],
             aprekins=["1)  m = 0,50 · 44",
                       "2)  m = 22 g",
                       "3)  m = 0,022 kg"],
             atbilde="m = 22 g = 0,022 kg",
             piezime="Molmasu iegūst no periodiskās tabulas: "
                     "12 + 2 · 16 = 44 g/mol."),
        dict(nr=6, virsraksts="Vielas daudzums no daļiņu skaita",
             teksts="Gāzes paraugā ir 3,01·10²³ molekulas.\n"
                    "Aprēķini vielas daudzumu! "
                    "(N_A = 6,02·10²³ mol⁻¹)",
             dots=["N = 3,01·10²³", "N_A = 6,02·10²³ mol⁻¹"],
             jaaprekina=["ν = ?"],
             formulas=["N = ν · N_A", "ν = N/N_A"],
             aprekins=["1)  ν = 3,01·10²³ : 6,02·10²³",
                       "2)  ν = 0,50 mol",
                       "3)  Pārbaude: 0,50 · 6,02·10²³ = 3,01·10²³ ✔"],
             atbilde="ν = 0,50 mol",
             piezime="Avogadro skaitlis ir tilts starp daļiņu skaitu un "
                     "vielas daudzumu."),
        dict(nr=7, virsraksts="Temperatūras starpība",
             teksts="Ūdeni sasilda no 15 °C līdz 85 °C.\n"
                    "Izsaki abas temperatūras kelvinos un aprēķini\n"
                    "temperatūras starpību abās skalās!",
             dots=["t₁ = 15 °C", "t₂ = 85 °C"],
             jaaprekina=["T₁ = ?", "T₂ = ?", "ΔT = ?"],
             formulas=["T = t + 273", "ΔT = T₂ − T₁"],
             aprekins=["1)  T₁ = 288 K ;  T₂ = 358 K",
                       "2)  ΔT = 358 − 288 = 70 K",
                       "3)  Celsija skalā: 85 − 15 = 70 °C"],
             atbilde="T₁ = 288 K;  T₂ = 358 K;  ΔT = 70 K = 70 °C",
             piezime="Starpība abās skalās ir vienāda - tāpēc siltuma "
                     "aprēķinos to var neparveidot."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Viela sastāv no daļiņām, kas nepārtraukti kustas.",
            "Jo augstāka temperatūra, jo ātrāka daļiņu kustība.",
            "T = t + 273; absolūtā nulle ir 0 K jeb −273 °C.",
            "ν = m/M; vienā molā ir 6,02·10²³ daļiņas.",
        ],
        majasdarbs=[
            "Izsaki kelvinos: 0 °C, 37 °C, −40 °C.",
            "m = 88 g oglekļa dioksīda, M = 44 g/mol. Aprēķini ν.",
            "Cik molekulu ir 0,50 mol gāzes?",
        ],
        pasvertejums=["Zinu daļiņu modeļa atziņas",
                      "Protu pāriet uz kelviniem",
                      "Protu rēķināt vielas daudzumu",
                      "Protu rēķināt daļiņu skaitu"],
        nakama="Nākamā stunda: difūzija un termiskā izplešanās."),
),

dict(
    nr="7.2", virsraksts="Difūzija un izplešanās",
    jautajums="Kāpēc smarža izplatās un tiltiem vajag spraugas?",
    apaksraksts="Difūzija · Brauna kustība · Δl = α · l₀ · ΔT",
    merkis="Ar daļiņu modeli skaidrot difūziju un termisko izplešanos un "
           "aprēķināt garuma izmaiņu.",
    protu=["izskaidrot difūziju ar daļiņu kustību;",
           "nosaukt, kas paātrina difūziju;",
           "aprēķināt Δl = α · l₀ · ΔT;",
           "izskaidrot spraugas sliedēs un tiltos."],
    atkartojums="Iepriekšējā stundā noskaidrojām, ka daļiņas kustas jo "
                "ātrāk, jo augstāka temperatūra. Šodien redzēsim divas "
                "šīs kustības sekas.",
    uzdevumu_apraksts="Termiskā izplešanās aprēķinos",
    teorija=[
        ("Difūzija", [
            ("panelis", "KAS IR DIFŪZIJA",
             ["Difūzija ir vielu savstarpēja sajaukšanās daļiņu haotiskās "
              "kustības dēļ. Tā notiek bez maisīšanas un jebkurā "
              "agregātstāvoklī.",
              "Difūzija ir ātrāka, ja temperatūra ir augstāka un ja "
              "daļiņas var kustēties brīvāk.",
              "Brauna kustība - sīku daļiņu haotiska raustīšanās "
              "šķidrumā - ir tiešs pierādījums, ka molekulas kustas."],
             NAVY),
            ("divi",
             ("ĀTRA DIFŪZIJA", GREEN,
              ["Gāzēs: smarža istabā",
               "izplatās dažās minūtēs.",
               "Karstā ūdenī: tēja",
               "izplatās uzreiz.",
               "Daļiņas kustas brīvi."]),
             ("LĒNA DIFŪZIJA", BLUE,
              ["Aukstā ūdenī: tēja",
               "izplatās daudz lēnāk.",
               "Cietvielās: metāli saplūst",
               "gados, nevis minūtēs.",
               "Daļiņas ir saistītas."])),
        ]),
        ("Termiskā izplešanās", [
            ("formula", "GARUMA IZMAIŅA",
             "Δl = α · l₀ · ΔT        l = l₀ + Δl",
             "α ir lineārās izplešanās koeficients, l₀ - sākuma garums, "
             "ΔT - temperatūras izmaiņa. Sildot daļiņas svārstās "
             "plašāk, tāpēc ķermenis kļūst garāks.", GOLD),
            ("tabula",
             ["Materiāls", "α (K⁻¹)", "Kur tas svarīgi"],
             [["Tērauds", "12·10⁻⁶", "Sliedes, tiltu konstrukcijas"],
              ["Betons", "12·10⁻⁶", "Ceļa plātnes, tilti"],
              ["Alumīnijs", "24·10⁻⁶", "Logu rāmji, radiatori"],
              ["Stikls", "9·10⁻⁶", "Trauki, termometri"]],
             [3.30, 2.60, 4.33]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Sliedes vasarā",
             teksts="Tērauda sliede ir 25 m gara. Temperatūra paaugstinās\n"
                    "par 40 K. Par cik pagarinās sliede?\n"
                    "(α = 12·10⁻⁶ K⁻¹)",
             dots=["l₀ = 25 m", "ΔT = 40 K", "α = 12·10⁻⁶ K⁻¹"],
             jaaprekina=["Δl = ?"],
             formulas=["Δl = α · l₀ · ΔT"],
             aprekins=["1)  Δl = 12·10⁻⁶ · 25 · 40",
                       "2)  Δl = 0,012 m",
                       "3)  Δl = 12 mm"],
             atbilde="Δl = 12 mm",
             piezime="Tieši tāpēc starp sliedēm atstāj spraugas - citādi "
                     "sliedes izliektos."),
        dict(nr=2, virsraksts="Tilta sprauga",
             teksts="Betona tilta laidums ir 60 m. Gada laikā temperatūra\n"
                    "mainās par 50 K. Cik plata sprauga vajadzīga?\n"
                    "(α = 12·10⁻⁶ K⁻¹)",
             dots=["l₀ = 60 m", "ΔT = 50 K", "α = 12·10⁻⁶ K⁻¹"],
             jaaprekina=["Δl = ?"],
             formulas=["Δl = α · l₀ · ΔT"],
             aprekins=["1)  Δl = 12·10⁻⁶ · 60 · 50",
                       "2)  Δl = 0,036 m",
                       "3)  Δl = 36 mm"],
             atbilde="Δl ≈ 36 mm",
             piezime="Praksē spraugu izveido nedaudz platāku - ar "
                     "drošības rezervi."),
        dict(nr=3, virsraksts="Divi dažādi metāli",
             teksts="Tērauda un alumīnija stieņi ir 10 m gari un tiek\n"
                    "sasildīti par 60 K. Salīdzini pagarinājumus!\n"
                    "(α₁ = 12·10⁻⁶ K⁻¹; α₂ = 24·10⁻⁶ K⁻¹)",
             dots=["l₀ = 10 m", "ΔT = 60 K",
                   "α₁ = 12·10⁻⁶ K⁻¹", "α₂ = 24·10⁻⁶ K⁻¹"],
             jaaprekina=["Δl₁ = ?", "Δl₂ = ?"],
             formulas=["Δl = α · l₀ · ΔT"],
             aprekins=["1)  Δl₁ = 12·10⁻⁶ · 10 · 60 = 7,2 mm",
                       "2)  Δl₂ = 24·10⁻⁶ · 10 · 60 = 14,4 mm",
                       "3)  Alumīnijs izplešas divreiz vairāk"],
             atbilde="Δl₁ = 7,2 mm;  Δl₂ = 14,4 mm",
             piezime="Divu metālu sloksni sildot, tā izliecas - tā "
                     "darbojas bimetāla slēdzis."),
        dict(nr=4, virsraksts="Stikla trauks",
             teksts="Stikla trauka mala ir 0,50 m. Trauku ielej verdošu\n"
                    "ūdeni, un temperatūra pieaug par 80 K.\n"
                    "Par cik pagarinās mala? (α = 9·10⁻⁶ K⁻¹)",
             dots=["l₀ = 0,50 m", "ΔT = 80 K", "α = 9·10⁻⁶ K⁻¹"],
             jaaprekina=["Δl = ?"],
             formulas=["Δl = α · l₀ · ΔT"],
             aprekins=["1)  Δl = 9·10⁻⁶ · 0,50 · 80",
                       "2)  Δl = 3,6·10⁻⁴ m",
                       "3)  Δl = 0,36 mm"],
             atbilde="Δl = 0,36 mm",
             piezime="Biezs stikls plīst tāpēc, ka iekšpuse sasilst "
                     "ātrāk nekā ārpuse un izplešas nevienmērīgi."),
        dict(nr=5, virsraksts="Vara vads vasarā",
             teksts="Vara vads ir 100 m garš. Temperatūra paaugstinās "
                    "par\n30 K. Par cik tas pagarinās? "
                    "(α = 17·10⁻⁶ K⁻¹)",
             dots=["l₀ = 100 m", "ΔT = 30 K", "α = 17·10⁻⁶ K⁻¹"],
             jaaprekina=["Δl = ?"],
             formulas=["Δl = α · l₀ · ΔT"],
             aprekins=["1)  Δl = 17·10⁻⁶ · 100 · 30",
                       "2)  Δl = 0,051 m",
                       "3)  Δl = 51 mm"],
             atbilde="Δl = 51 mm ≈ 5,1 cm",
             piezime="Tāpēc elektrolīnijas vasarā nokarājas zemāk nekā "
                     "ziemā."),
        dict(nr=6, virsraksts="Sākuma garums",
             teksts="Tērauda stienis, sasildot par 50 K, pagarinājās par\n"
                    "6,0 mm. Cik garš tas bija sākumā? "
                    "(α = 12·10⁻⁶ K⁻¹)",
             dots=["Δl = 6,0 mm = 0,0060 m", "ΔT = 50 K",
                   "α = 12·10⁻⁶ K⁻¹"],
             jaaprekina=["l₀ = ?"],
             formulas=["Δl = α l₀ ΔT", "l₀ = Δl/(α·ΔT)"],
             aprekins=["1)  α·ΔT = 12·10⁻⁶ · 50 = 6,0·10⁻⁴",
                       "2)  l₀ = 0,0060 : 6,0·10⁻⁴",
                       "3)  l₀ = 10 m"],
             atbilde="l₀ = 10 m",
             piezime="Formulu var izteikt pret jebkuru no četriem "
                     "lielumiem."),
        dict(nr=7, virsraksts="Temperatūras izmaiņa",
             teksts="Tērauda sliede (l₀ = 20 m) pagarinājās par 9,6 mm.\n"
                    "Par cik mainījās temperatūra? "
                    "(α = 12·10⁻⁶ K⁻¹)",
             dots=["l₀ = 20 m", "Δl = 9,6 mm = 0,0096 m",
                   "α = 12·10⁻⁶ K⁻¹"],
             jaaprekina=["ΔT = ?"],
             formulas=["Δl = α l₀ ΔT", "ΔT = Δl/(α·l₀)"],
             aprekins=["1)  α·l₀ = 12·10⁻⁶ · 20 = 2,4·10⁻⁴ m/K",
                       "2)  ΔT = 0,0096 : 2,4·10⁻⁴",
                       "3)  ΔT = 40 K"],
             atbilde="ΔT = 40 K",
             piezime="Pēc sliedes pagarinājuma var noteikt, cik stipri "
                     "tā sasilusi saulē."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Difūzija ir vielu sajaukšanās daļiņu kustības dēļ.",
            "Augstāka temperatūra - ātrāka difūzija.",
            "Δl = α · l₀ · ΔT; α mēra kelvina apgrieztajās vienībās.",
            "Spraugas sliedēs un tiltos atstāj termiskajai izplešanās.",
        ],
        majasdarbs=[
            "l₀ = 40 m, ΔT = 30 K, α = 12·10⁻⁶ K⁻¹. Aprēķini Δl.",
            "Kāpēc karstā ūdenī cukurs izšķīst ātrāk? Paskaidro ar "
            "daļiņu modeli.",
            "Alumīnija stienis 5,0 m, ΔT = 50 K. Aprēķini Δl.",
        ],
        pasvertejums=["Protu izskaidrot difūziju",
                      "Zinu, kas to paātrina",
                      "Protu rēķināt Δl",
                      "Protu izskaidrot spraugas"],
        nakama="Nākamā stunda: šķidrumu īpašības un virsmas spraigums."),
),

dict(
    nr="7.3", virsraksts="Šķidrumu īpašības",
    jautajums="Kāpēc ūdens veido pilienus un paceļas kapilāros?",
    apaksraksts="Virsmas spraigums σ = F/l · Slapināšana · Kapilaritāte",
    merkis="Skaidrot virsmas spraigumu, slapināšanu un kapilaritāti un "
           "lietot sakarību σ = F/l.",
    protu=["izskaidrot virsmas spraigumu ar daļiņu mijiedarbību;",
           "lietot σ = F/l;",
           "atšķirt slapinošu un neslapinošu šķidrumu;",
           "nosaukt kapilaritātes piemērus dabā."],
    atkartojums="Daļiņu modelis paskaidroja gan difūziju, gan "
                "izplešanos. Šodien tas pats modelis paskaidros, kāpēc "
                "ūdens virsma uzvedas kā plēve.",
    uzdevumu_apraksts="Virsmas spraiguma aprēķini",
    teorija=[
        ("Virsmas spraigums", [
            ("formula", "VIRSMAS SPRAIGUMS",
             "σ = F/l        F = σ · l        [σ] = N/m",
             "Šķidruma iekšienē daļiņu pievelk no visām pusēm, bet uz "
             "virsmas - tikai no apakšas. Tāpēc virsma savelkas un "
             "uzvedas kā izstiepta plēve.", GOLD),
            ("kartitas", [
                ("PILIENS", BLUE,
                 ["Virsma savelkas",
                  "mazākajā laukumā.",
                  "Tāpēc piliens ir apaļš."]),
                ("ZIEPJŪDENS", GREEN,
                 ["Ziepes samazina σ.",
                  "Virsma vieglāk stiepjas.",
                  "Tāpēc rodas burbuļi."]),
                ("ŪDENSMĒRĪTĀJS", GOLD,
                 ["Kukainis stāv uz virsmas.",
                  "Virsmas plēve to notur.",
                  "Ūdenim σ = 0,073 N/m."]),
            ]),
        ]),
        ("Slapināšana un kapilaritāte", [
            ("divi",
             ("SLAPINA", BLUE,
              ["Šķidruma daļiņas pievelkas",
               "traukam stiprāk nekā",
               "cita citai.",
               "Malas paceļas uz augšu.",
               "Piemērs: ūdens stiklā."]),
             ("NESLAPINA", RED,
              ["Šķidruma daļiņas pievelkas",
               "cita citai stiprāk nekā",
               "traukam.",
               "Malas nolaižas.",
               "Piemērs: dzīvsudrabs stiklā."])),
            ("panelis", "KAPILARITĀTE",
             ["Šaurās caurulītēs - kapilāros - slapinošs šķidrums "
              "paceļas, bet neslapinošs nolaižas. Jo šaurāks kapilārs, "
              "jo lielāks efekts.",
              "Dabā un sadzīvē: ūdens paceļas augu stumbros, mitrums - "
              "augsnē un ķieģeļu sienā, dvielis uzsūc ūdeni.",
              "Būvniecībā tāpēc liek hidroizolāciju - lai mitrums pa "
              "kapilāriem neceltos sienā."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Virsmas spraiguma koeficients",
             teksts="Lai atrautu 0,20 m garu stiepli no šķidruma virsmas,\n"
                    "vajag 0,014 N lielu spēku.\n"
                    "Aprēķini virsmas spraiguma koeficientu!",
             dots=["F = 0,014 N", "l = 0,20 m"],
             jaaprekina=["σ = ?"],
             formulas=["σ = F/l"],
             aprekins=["1)  σ = 0,014 : 0,20",
                       "2)  σ = 0,07 N/m"],
             atbilde="σ = 0,07 N/m",
             piezime="Iznākums ir tuvu ūdens vērtībai 0,073 N/m - "
                     "acīmredzot mērīts ūdens."),
        dict(nr=2, virsraksts="Virsmas spēks",
             teksts="Uz 0,10 m garas robežlīnijas ūdens virsmā darbojas\n"
                    "virsmas spraigums (σ = 0,073 N/m).\n"
                    "Aprēķini spēku!",
             dots=["σ = 0,073 N/m", "l = 0,10 m"],
             jaaprekina=["F = ?"],
             formulas=["σ = F/l", "F = σ · l"],
             aprekins=["1)  F = 0,073 · 0,10",
                       "2)  F = 0,0073 N",
                       "3)  F = 7,3 mN"],
             atbilde="F = 7,3·10⁻³ N",
             piezime="Spēks ir mazs, bet ar to pietiek, lai noturētu "
                     "vieglu kukaini."),
        dict(nr=3, virsraksts="Robežlīnijas garums",
             teksts="Virsmas spraiguma spēks ir 0,022 N, bet šķidruma\n"
                    "virsmas spraiguma koeficients 0,055 N/m.\n"
                    "Aprēķini robežlīnijas garumu!",
             dots=["F = 0,022 N", "σ = 0,055 N/m"],
             jaaprekina=["l = ?"],
             formulas=["σ = F/l", "l = F/σ"],
             aprekins=["1)  l = 0,022 : 0,055",
                       "2)  l = 0,40 m"],
             atbilde="l = 0,40 m",
             piezime="No vienas formulas var izteikt jebkuru no trim "
                     "lielumiem."),
        dict(nr=4, virsraksts="Ūdens un ziepjūdens",
             teksts="Salīdzini spēku uz 0,05 m garas līnijas tīrā ūdenī\n"
                    "(σ₁ = 0,073 N/m) un ziepjūdenī (σ₂ = 0,040 N/m)!",
             dots=["l = 0,05 m", "σ₁ = 0,073 N/m", "σ₂ = 0,040 N/m"],
             jaaprekina=["F₁ = ?", "F₂ = ?"],
             formulas=["F = σ · l"],
             aprekins=["1)  F₁ = 0,073 · 0,05 ≈ 3,7·10⁻³ N",
                       "2)  F₂ = 0,040 · 0,05 = 2,0·10⁻³ N",
                       "3)  Ziepjūdenī spēks ir gandrīz divreiz mazāks"],
             atbilde="F₁ ≈ 3,7 mN;  F₂ = 2,0 mN",
             piezime="Tāpēc ziepjūdens labāk iesūcas audumā - virsma "
                     "vairs tik stipri nepretojas."),
        dict(nr=5, virsraksts="Adata uz ūdens virsmas",
             teksts="Uz ūdens virsmas uzliek 4,0 cm garu adatu ar masu\n"
                    "0,30 g. Virsmas spraigums darbojas gar abām adatas\n"
                    "pusēm. Vai adata noturēsies? (σ = 0,073 N/m; "
                    "g = 9,8 m/s²)",
             dots=["l = 0,040 m", "m = 3,0·10⁻⁴ kg",
                   "σ = 0,073 N/m"],
             jaaprekina=["F = ?", "mg = ?"],
             formulas=["F = σ · 2l", "mg = smaguma spēks"],
             aprekins=["1)  F = 0,073 · 2 · 0,040 = 5,8·10⁻³ N",
                       "2)  mg = 3,0·10⁻⁴ · 9,8 = 2,9·10⁻³ N",
                       "3)  5,8·10⁻³ > 2,9·10⁻³ → noturēsies"],
             atbilde="Adata noturēsies: virsmas spēks ir divreiz lielāks "
                     "par smaguma spēku.",
             piezime="Adata nepeld Arhimēda spēka dēļ - to notur tieši "
                     "virsmas plēvīte."),
        dict(nr=6, virsraksts="Ūdens un spirts",
             teksts="Salīdzini virsmas spraiguma spēku uz 0,10 m garas\n"
                    "līnijas ūdenī (σ₁ = 0,073 N/m) un spirtā\n"
                    "(σ₂ = 0,022 N/m)!",
             dots=["l = 0,10 m", "σ₁ = 0,073 N/m", "σ₂ = 0,022 N/m"],
             jaaprekina=["F₁ = ?", "F₂ = ?"],
             formulas=["F = σ · l"],
             aprekins=["1)  F₁ = 0,073 · 0,10 = 7,3·10⁻³ N",
                       "2)  F₂ = 0,022 · 0,10 = 2,2·10⁻³ N",
                       "3)  F₁ : F₂ ≈ 3,3"],
             atbilde="F₁ = 7,3 mN;  F₂ = 2,2 mN - ūdenī 3,3 reizes "
                     "lielāks.",
             piezime="Spirta lāse uz galda izplūst plakana, ūdens lāse "
                     "paliek apaļa - tieši šī atšķirība."),
        dict(nr=7, virsraksts="Piliena atraušanās",
             teksts="Ūdens piliens atraujas no caurulītes ar rādiusu\n"
                    "1,0 mm. Aprēķini noturošo spēku un piliena masu!\n"
                    "(σ = 0,073 N/m; π = 3,14; g = 9,8 m/s²)",
             dots=["r = 1,0·10⁻³ m", "σ = 0,073 N/m"],
             jaaprekina=["l = ?", "F = ?", "m = ?"],
             formulas=["l = 2πr", "F = σl", "m = F/g"],
             aprekins=["1)  l = 2 · 3,14 · 1,0·10⁻³ = 6,3·10⁻³ m",
                       "2)  F = 0,073 · 6,3·10⁻³ = 4,6·10⁻⁴ N",
                       "3)  m = 4,6·10⁻⁴ : 9,8 ≈ 4,7·10⁻⁵ kg = 47 mg"],
             atbilde="F ≈ 4,6·10⁻⁴ N ;   m ≈ 47 mg",
             piezime="Piliens atraujas tieši tad, kad tā svars pārsniedz "
                     "virsmas spraiguma spēku."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Virsmas spraigumu rada daļiņu nevienmērīga pievilkšanās "
            "virsmā.",
            "σ = F/l; virsmas spraigumu mēra ņūtonos uz metru.",
            "Slapinošs šķidrums kapilārā paceļas, neslapinošs - nolaižas.",
            "Kapilaritāte darbojas augsnē, augos un dvielī.",
        ],
        majasdarbs=[
            "F = 0,030 N, l = 0,25 m. Aprēķini σ.",
            "σ = 0,073 N/m, l = 0,20 m. Aprēķini F.",
            "Paskaidro, kāpēc ziepes palīdz mazgāt traukus.",
        ],
        pasvertejums=["Protu izskaidrot virsmas spraigumu",
                      "Protu lietot σ = F/l",
                      "Protu atšķirt slapināšanu",
                      "Zinu kapilaritātes piemērus"],
        nakama="Nākamā stunda: gāzes spiediens un tilpums."),
),

dict(
    nr="7.4", virsraksts="Gāzes spiediens un tilpums",
    jautajums="Kāpēc saspiestu gāzi kļūst grūtāk saspiest?",
    apaksraksts="p = F/S · Izotermisks process · p₁V₁ = p₂V₂",
    merkis="Skaidrot gāzes spiedienu ar daļiņu kustību un lietot "
           "sakarību p₁V₁ = p₂V₂.",
    protu=["izskaidrot spiedienu ar daļiņu triecieniem;",
           "nosaukt, no kā atkarīgs gāzes spiediens;",
           "lietot p₁V₁ = p₂V₂;",
           "no tabulas vai grafika noteikt sakarību starp p un V."],
    atkartojums="10. klasē spiedienu rēķinājām kā p = F/S. Gāzēm spiedienu "
                "rada nevis viens spēks, bet miljardi daļiņu triecienu.",
    uzdevumu_apraksts="Izotermiskā procesa aprēķini",
    teorija=[
        ("Kas rada gāzes spiedienu", [
            ("panelis", "SPIEDIENS IR DAĻIŅU TRIECIENI",
             ["Gāzes daļiņas kustas haotiski un atsitas pret trauka "
              "sienām. Katrs trieciens ir sīks grūdiens; kopā tie rada "
              "spiedienu.",
              "Spiediens ir lielāks, ja triecienu ir vairāk vai ja tie "
              "ir stiprāki.",
              "Saspiežot gāzi, daļiņas ir tuvāk sienām un atsitas "
              "biežāk - tāpēc saspiest kļūst arvien grūtāk."], NAVY),
            ("kartitas", [
                ("VAIRĀK DAĻIŅU", BLUE,
                 ["Vairāk triecienu",
                  "vienā sekundē.",
                  "Spiediens pieaug."]),
                ("AUGSTĀKA T", RED,
                 ["Daļiņas kustas ātrāk.",
                  "Triecieni stiprāki.",
                  "Spiediens pieaug."]),
                ("MAZĀKS TILPUMS", GREEN,
                 ["Sienas tuvāk.",
                  "Triecieni biežāki.",
                  "Spiediens pieaug."]),
            ]),
        ]),
        ("Izotermisks process", [
            ("formula", "BOILA UN MARIOTA LIKUMS",
             "p₁V₁ = p₂V₂        (T = const)",
             "Nemainīgā temperatūrā spiediena un tilpuma reizinājums "
             "paliek nemainīgs: cik reižu tilpumu samazina, tik reižu "
             "spiediens pieaug.", GOLD),
            ("tabula",
             ["Mērījums", "p (kPa)", "V (L)", "p · V"],
             [["1.", "100", "6,0", "600"],
              ["2.", "150", "4,0", "600"],
              ["3.", "300", "2,0", "600"],
              ["4.", "600", "1,0", "600"]],
             [2.60, 3.00, 3.00, 3.63]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Gāzi saspiež",
             teksts="Gāzes tilpums 2,0 L pie 100 kPa spiediena. To saspiež\n"
                    "līdz 0,50 L nemainīgā temperatūrā.\n"
                    "Aprēķini spiedienu!",
             dots=["p₁ = 100 kPa", "V₁ = 2,0 L", "V₂ = 0,50 L"],
             jaaprekina=["p₂ = ?"],
             formulas=["p₁V₁ = p₂V₂", "p₂ = p₁V₁/V₂"],
             aprekins=["1)  p₂ = 100 · 2,0 : 0,50",
                       "2)  p₂ = 400 kPa"],
             atbilde="p₂ = 400 kPa",
             piezime="Tilpums samazināts 4 reizes - spiediens pieaudzis "
                     "tieši 4 reizes."),
        dict(nr=2, virsraksts="Gāze izplešas",
             teksts="Gāze ar tilpumu 3,0 L un spiedienu 200 kPa izplešas,\n"
                    "līdz spiediens ir 150 kPa. Temperatūra nemainās.\n"
                    "Aprēķini tilpumu!",
             dots=["p₁ = 200 kPa", "V₁ = 3,0 L", "p₂ = 150 kPa"],
             jaaprekina=["V₂ = ?"],
             formulas=["p₁V₁ = p₂V₂", "V₂ = p₁V₁/p₂"],
             aprekins=["1)  V₂ = 200 · 3,0 : 150",
                       "2)  V₂ = 4,0 L"],
             atbilde="V₂ = 4,0 L",
             piezime="Spiediens samazinājās - tilpums pieauga. Lielumi "
                     "ir apgriezti proporcionāli."),
        dict(nr=3, virsraksts="Šļirce",
             teksts="Šļircē ir 20 ml gaisa pie 100 kPa. Virzuli iespiež,\n"
                    "līdz tilpums ir 8,0 ml (T nemainās).\n"
                    "Aprēķini spiedienu!",
             dots=["p₁ = 100 kPa", "V₁ = 20 ml", "V₂ = 8,0 ml"],
             jaaprekina=["p₂ = ?"],
             formulas=["p₁V₁ = p₂V₂", "p₂ = p₁V₁/V₂"],
             aprekins=["1)  p₂ = 100 · 20 : 8,0",
                       "2)  p₂ = 250 kPa"],
             atbilde="p₂ = 250 kPa",
             piezime="Tilpumu abās pusēs var atstāt mililitros - "
                     "svarīgi, lai vienības ir vienādas."),
        dict(nr=4, virsraksts="Tabulas pārbaude",
             teksts="Mērījumos ieguva: p = 250 kPa pie V = 2,4 L.\n"
                    "Vai šis punkts atbilst tabulai, kur p·V = 600?\n"
                    "Ja nē, kāds tilpums būtu pareizs?",
             dots=["p = 250 kPa", "V = 2,4 L", "p·V = 600 (tabula)"],
             jaaprekina=["Vai atbilst?", "V = ?"],
             formulas=["p₁V₁ = p₂V₂", "V = p₁V₁/p"],
             aprekins=["1)  250 · 2,4 = 600 - reizinājums sakrīt",
                       "2)  Punkts atbilst tabulai",
                       "3)  Pārbaudei: 600 : 250 = 2,4 L"],
             atbilde="Atbilst: p·V = 600",
             piezime="Reizinājuma pārbaude ir ātrākais veids, kā "
                     "pārliecināties, vai dati apraksta izotermu."),
        dict(nr=5, virsraksts="Burbulis paceļas",
             teksts="Gaisa burbulis ar tilpumu 2,0 cm³ atrodas dziļumā, "
                    "kur\nspiediens ir 300 kPa. Kāds būs tā tilpums pie "
                    "virsmas\n(100 kPa), ja temperatūra nemainās?",
             dots=["V₁ = 2,0 cm³", "p₁ = 300 kPa", "p₂ = 100 kPa"],
             jaaprekina=["V₂ = ?"],
             formulas=["p₁V₁ = p₂V₂", "V₂ = p₁V₁/p₂"],
             aprekins=["1)  p₁V₁ = 300 · 2,0 = 600",
                       "2)  V₂ = 600 : 100",
                       "3)  V₂ = 6,0 cm³"],
             atbilde="V₂ = 6,0 cm³ - trīs reizes lielāks.",
             piezime="Tāpēc nirējam nedrīkst aizturēt elpu, ceļoties "
                     "augšup - gaiss plaušās izplešas."),
        dict(nr=6, virsraksts="Cik reižu jāsaspiež",
             teksts="Cik reižu jāsamazina gāzes tilpums, lai spiediens\n"
                    "pieaugtu 5 reizes nemainīgā temperatūrā?",
             dots=["p₂ = 5p₁", "T = const"],
             jaaprekina=["V₁/V₂ = ?"],
             formulas=["p₁V₁ = p₂V₂", "V₁/V₂ = p₂/p₁"],
             aprekins=["1)  p₁V₁ = 5p₁ · V₂",
                       "2)  V₁ = 5V₂",
                       "3)  V₁/V₂ = 5"],
             atbilde="Tilpums jāsamazina 5 reizes.",
             piezime="Izotermā p un V ir apgriezti proporcionāli - "
                     "izmaiņas reizes vienmēr sakrīt."),
        dict(nr=7, virsraksts="Divi savienoti trauki",
             teksts="Trauku ar 3,0 L gāzes pie 200 kPa savieno ar tukšu\n"
                    "2,0 L trauku. Aprēķini spiedienu pēc savienošanas\n"
                    "(T nemainās)!",
             dots=["V₁ = 3,0 L", "p₁ = 200 kPa", "V₂ = 5,0 L"],
             jaaprekina=["p₂ = ?"],
             formulas=["p₁V₁ = p₂V₂", "p₂ = p₁V₁/V₂"],
             aprekins=["1)  Kopējais tilpums: 3,0 + 2,0 = 5,0 L",
                       "2)  p₂ = 200 · 3,0 : 5,0",
                       "3)  p₂ = 120 kPa"],
             atbilde="p₂ = 120 kPa",
             piezime="Gāze izplešas visā pieejamajā tilpumā - tāpēc "
                     "spiediens krīt."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Gāzes spiedienu rada daļiņu triecieni pret trauka sienām.",
            "Spiediens pieaug, ja daļiņu vairāk, tās ātrākas vai tilpums "
            "mazāks.",
            "Nemainīgā temperatūrā p₁V₁ = p₂V₂.",
            "p un V ir apgriezti proporcionāli lielumi.",
        ],
        majasdarbs=[
            "p₁ = 120 kPa, V₁ = 5,0 L, V₂ = 2,0 L. Aprēķini p₂.",
            "p₁ = 300 kPa, V₁ = 1,0 L, p₂ = 100 kPa. Aprēķini V₂.",
            "Paskaidro, kāpēc velosipēda pumpi kļūst grūtāk spiest.",
        ],
        pasvertejums=["Protu izskaidrot gāzes spiedienu",
                      "Zinu, no kā tas atkarīgs",
                      "Protu lietot p₁V₁ = p₂V₂",
                      "Protu pārbaudīt tabulas datus"],
        nakama="Nākamā stunda: gāzes temperatūra un izoprocesi."),
),

dict(
    nr="7.5", virsraksts="Gāzes temperatūra un stāvoklis",
    jautajums="Kā mainās gāzes spiediens vai tilpums, to sildot?",
    apaksraksts="Izohorisks p₁/T₁ = p₂/T₂ · Izobārisks V₁/T₁ = V₂/T₂",
    merkis="Atpazīt izoprocesus un lietot spiediena, tilpuma un "
           "temperatūras sakarības.",
    protu=["atšķirt izotermisku, izohorisku un izobārisku procesu;",
           "lietot p₁/T₁ = p₂/T₂;",
           "lietot V₁/T₁ = V₂/T₂;",
           "temperatūru aprēķinos vienmēr izteikt kelvinos."],
    atkartojums="Iepriekšējā stundā temperatūra bija nemainīga. Tagad "
                "mainīsim tieši temperatūru un skatīsimies, kas notiek "
                "ar spiedienu vai tilpumu.",
    uzdevumu_apraksts="Izoprocesi sadzīves piemēros",
    teorija=[
        ("Trīs izoprocesi", [
            ("formula", "IZOHORISKS UN IZOBĀRISKS PROCESS",
             "p₁/T₁ = p₂/T₂  (V = const)        V₁/T₁ = V₂/T₂  (p = const)",
             "Izohoriskā procesā tilpums nemainās un spiediens ir tieši "
             "proporcionāls temperatūrai; izobāriskā procesā nemainās "
             "spiediens, bet tilpums aug līdz ar temperatūru.", GOLD),
            ("kartitas", [
                ("IZOTERMISKS", BLUE,
                 ["T = const.",
                  "p₁V₁ = p₂V₂.",
                  "Piemērs: lēni saspiesta",
                  "šļirce."]),
                ("IZOHORISKS", GREEN,
                 ["V = const.",
                  "p₁/T₁ = p₂/T₂.",
                  "Piemērs: sasildīts",
                  "aerosola balons."]),
                ("IZOBĀRISKS", GOLD,
                 ["p = const.",
                  "V₁/T₁ = V₂/T₂.",
                  "Piemērs: balons",
                  "aukstumā saraujas."]),
            ]),
        ]),
        ("Piemēri un biežākā kļūda", [
            ("tabula",
             ["Situācija", "Kas nemainās", "Kas notiek"],
             [["Riepa sasilst braucot", "Tilpums", "Spiediens pieaug"],
              ["Balons ienests no sala", "Spiediens", "Tilpums pieaug"],
              ["Šļirce lēni saspiesta", "Temperatūra", "Spiediens pieaug"],
              ["Aerosols pie uguns", "Tilpums", "Spiediens - bīstami!"]],
             [4.00, 3.00, 3.23]),
            ("panelis", "TEMPERATŪRA VIENMĒR KELVINOS",
             ["Izoprocesu formulās temperatūru raksta TIKAI kelvinos. Ar "
              "Celsija grādiem iznāk aplama atbilde, jo skala nesākas "
              "nullē.",
              "Piemērs: sildot no 10 °C uz 20 °C, temperatūra kelvinos "
              "pieaug no 283 K uz 293 K - tikai par 3,5 %, nevis "
              "divkārši.",
              "Tāpēc pirmais solis vienmēr ir pārrēķins T = t + 273."],
             RED),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Riepa sasilst",
             teksts="Riepā spiediens 200 kPa pie 280 K. Braucot gaiss\n"
                    "sasilst līdz 310 K (tilpums nemainās).\n"
                    "Aprēķini spiedienu!",
             dots=["p₁ = 200 kPa", "T₁ = 280 K", "T₂ = 310 K"],
             jaaprekina=["p₂ = ?"],
             formulas=["p₁/T₁ = p₂/T₂", "p₂ = p₁T₂/T₁"],
             aprekins=["1)  p₂ = 200 · 310 : 280",
                       "2)  p₂ ≈ 221 kPa"],
             atbilde="p₂ ≈ 221 kPa",
             piezime="Tāpēc riepu spiedienu mēra aukstām riepām - "
                     "siltās rādījums ir lielāks."),
        dict(nr=2, virsraksts="Balons aukstumā",
             teksts="Balona tilpums ir 2,0 L pie 300 K. To iznes ārā,\n"
                    "kur temperatūra ir 270 K (spiediens nemainās).\n"
                    "Aprēķini tilpumu!",
             dots=["V₁ = 2,0 L", "T₁ = 300 K", "T₂ = 270 K"],
             jaaprekina=["V₂ = ?"],
             formulas=["V₁/T₁ = V₂/T₂", "V₂ = V₁T₂/T₁"],
             aprekins=["1)  V₂ = 2,0 · 270 : 300",
                       "2)  V₂ = 1,8 L"],
             atbilde="V₂ = 1,8 L",
             piezime="Balons ziemā saraujas un istabā atkal atgūst "
                     "iepriekšējo tilpumu."),
        dict(nr=3, virsraksts="Aerosola balons",
             teksts="Aerosolā spiediens ir 300 kPa pie 20 °C. To atstāj\n"
                    "saulē, kur temperatūra pieaug līdz 60 °C.\n"
                    "Aprēķini spiedienu!",
             dots=["p₁ = 300 kPa", "t₁ = 20 °C", "t₂ = 60 °C"],
             jaaprekina=["p₂ = ?"],
             formulas=["T = t + 273", "p₁/T₁ = p₂/T₂", "p₂ = p₁T₂/T₁"],
             aprekins=["1)  T₁ = 293 K;  T₂ = 333 K",
                       "2)  p₂ = 300 · 333 : 293",
                       "3)  p₂ ≈ 341 kPa"],
             atbilde="p₂ ≈ 341 kPa",
             piezime="Tāpēc uz aerosoliem raksta brīdinājumu nesildīt "
                     "virs 50 °C."),
        dict(nr=4, virsraksts="Kļūda ar grādiem",
             teksts="Skolēns gāzi sildīja no 10 °C līdz 20 °C un secināja,\n"
                    "ka spiediens divkāršosies. Pārbaudi, vai tā ir!\n"
                    "(p₁ = 100 kPa)",
             dots=["p₁ = 100 kPa", "t₁ = 10 °C", "t₂ = 20 °C"],
             jaaprekina=["p₂ = ?"],
             formulas=["T = t + 273", "p₂ = p₁T₂/T₁"],
             aprekins=["1)  T₁ = 283 K;  T₂ = 293 K",
                       "2)  p₂ = 100 · 293 : 283",
                       "3)  p₂ ≈ 104 kPa - nevis 200 kPa"],
             atbilde="p₂ ≈ 104 kPa",
             piezime="Grādos temperatūra divkāršojās, bet kelvinos "
                     "pieauga tikai par 3,5 % - tāpēc skala ir svarīga."),
        dict(nr=5, virsraksts="Tilpums, gāzi sildot",
             teksts="Gāzes tilpums ir 5,0 L pie 250 K. To sasilda līdz\n"
                    "350 K nemainīgā spiedienā. Aprēķini tilpumu!",
             dots=["V₁ = 5,0 L", "T₁ = 250 K", "T₂ = 350 K"],
             jaaprekina=["V₂ = ?"],
             formulas=["V₁/T₁ = V₂/T₂", "V₂ = V₁T₂/T₁"],
             aprekins=["1)  V₂ = 5,0 · 350 : 250",
                       "2)  V₂ = 7,0 L",
                       "3)  Pieaugums 40 %"],
             atbilde="V₂ = 7,0 L",
             piezime="Nemainīgā spiedienā tilpums ir tieši proporcionāls "
                     "temperatūrai KELVINOS."),
        dict(nr=6, virsraksts="Temperatūra no spiediena",
             teksts="Slēgtā traukā spiediens pieaug no 150 kPa līdz\n"
                    "200 kPa. Sākuma temperatūra bija 300 K.\n"
                    "Aprēķini gala temperatūru grādos!",
             dots=["p₁ = 150 kPa", "p₂ = 200 kPa", "T₁ = 300 K"],
             jaaprekina=["T₂ = ?", "t₂ = ?"],
             formulas=["p₁/T₁ = p₂/T₂", "T₂ = T₁p₂/p₁",
                       "t = T − 273"],
             aprekins=["1)  T₂ = 300 · 200 : 150",
                       "2)  T₂ = 400 K",
                       "3)  t₂ = 400 − 273 = 127 °C"],
             atbilde="T₂ = 400 K = 127 °C",
             piezime="Atbildi bieži prasa grādos - pārrēķinu neaizmirsti "
                     "veikt beigās."),
        dict(nr=7, virsraksts="Mainās viss uzreiz",
             teksts="Gāzei p₁ = 100 kPa, V₁ = 2,0 L, T₁ = 300 K.\n"
                    "Pēc saspiešanas V₂ = 1,0 L un T₂ = 450 K.\n"
                    "Aprēķini jauno spiedienu!",
             dots=["p₁ = 100 kPa", "V₁ = 2,0 L", "T₁ = 300 K",
                   "V₂ = 1,0 L", "T₂ = 450 K"],
             jaaprekina=["p₂ = ?"],
             formulas=["p₁V₁/T₁ = p₂V₂/T₂",
                       "p₂ = p₁V₁T₂/(T₁V₂)"],
             aprekins=["1)  p₁V₁/T₁ = 100 · 2,0 : 300 = 0,667",
                       "2)  p₂ = 0,667 · 450 : 1,0",
                       "3)  p₂ = 300 kPa"],
             atbilde="p₂ = 300 kPa",
             piezime="Apvienotais gāzes likums der, kad mainās visi trīs "
                     "lielumi - pārējie likumi ir tā īpašgadījumi."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Izohoriskā procesā V = const un p₁/T₁ = p₂/T₂.",
            "Izobāriskā procesā p = const un V₁/T₁ = V₂/T₂.",
            "Izotermiskā procesā T = const un p₁V₁ = p₂V₂.",
            "Temperatūru formulās vienmēr izsaka kelvinos.",
        ],
        majasdarbs=[
            "p₁ = 150 kPa, T₁ = 300 K, T₂ = 330 K. Aprēķini p₂.",
            "V₁ = 5,0 L, T₁ = 290 K, T₂ = 320 K. Aprēķini V₂.",
            "Nosauc pa vienam katra izoprocesa piemēram no sadzīves.",
        ],
        pasvertejums=["Protu atšķirt izoprocesus",
                      "Protu lietot p un T sakarību",
                      "Protu lietot V un T sakarību",
                      "Neaizmirstu pāriet uz kelviniem"],
        nakama="Nākamā stunda: ideālās gāzes vienādojums un modeļa "
               "robežas."),
),

dict(
    nr="7.6", virsraksts="Modeļi un vienkārši aprēķini",
    jautajums="Ko gāzes modelis palīdz paredzēt?",
    apaksraksts="pV = νRT · R = 8,31 J/(mol·K) · Modeļa robežas",
    merkis="Pēc parauga lietot vienādojumu pV = νRT un izvērtēt modeļa "
           "ierobežojumus.",
    protu=["nosaukt lielumus vienādojumā pV = νRT;",
           "izteikt p, V vai ν no vienādojuma;",
           "pārbaudīt mērvienības pirms aprēķina;",
           "nosaukt, kad ideālās gāzes modelis vairs neder."],
    atkartojums="Iepriekšējās divās stundās katrs likums saistīja divus "
                "lielumus. Tagad tos apvienosim vienā vienādojumā, kas "
                "apraksta gāzes stāvokli.",
    uzdevumu_apraksts="Ideālās gāzes vienādojuma lietošana",
    teorija=[
        ("Ideālās gāzes vienādojums", [
            ("formula", "STĀVOKĻA VIENĀDOJUMS",
             "pV = νRT        R = 8,31 J/(mol·K)",
             "Vienādojums saista spiedienu, tilpumu, vielas daudzumu un "
             "temperatūru. Visi iepriekšējie izoprocesi ir šī "
             "vienādojuma atsevišķi gadījumi.", GOLD),
            ("kartitas", [
                ("p - SPIEDIENS", BLUE,
                 ["Aprēķinos paskālos.",
                  "1 kPa = 1000 Pa.",
                  "Atmosfēra ≈ 100 kPa."]),
                ("V - TILPUMS", GREEN,
                 ["Aprēķinos kubikmetros.",
                  "1 L = 0,001 m³.",
                  "1 ml = 10⁻⁶ m³."]),
                ("T - TEMPERATŪRA", GOLD,
                 ["Aprēķinos kelvinos.",
                  "T = t + 273.",
                  "Nekad ne grādos."]),
            ]),
        ]),
        ("Kad modelis der", [
            ("tabula",
             ["Situācija", "Vai modelis der", "Kāpēc"],
             [["Gaiss istabā", "Der labi", "Daļiņas tālu, spēki mazi"],
              ["Gāze balonā", "Der", "Parasts spiediens un T"],
              ["Ļoti augsts spiediens", "Neder", "Daļiņu tilpums svarīgs"],
              ["Tuvu sašķidrināšanai", "Neder", "Pievilkšanās spēki lieli"]],
             [3.60, 3.20, 3.43]),
            ("panelis", "MODELIS IR VIENKĀRŠOJUMS",
             ["Ideālās gāzes modelī pieņem, ka daļiņām nav tilpuma un "
              "starp tām nedarbojas pievilkšanās spēki.",
              "Parastos apstākļos šis vienkāršojums dod ļoti precīzu "
              "rezultātu - tāpēc to lieto tehnikā un meteoroloģijā.",
              "Fizikā modeli vienmēr izvērtē: der tas vai neder, atkarīgs "
              "no apstākļiem, nevis no formulas skaistuma."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Spiediens no vienādojuma",
             teksts="Traukā ar tilpumu 0,050 m³ ir 2,0 mol gāzes\n"
                    "300 K temperatūrā. Aprēķini spiedienu!\n"
                    "(R = 8,31 J/(mol·K))",
             dots=["V = 0,050 m³", "ν = 2,0 mol", "T = 300 K"],
             jaaprekina=["p = ?"],
             formulas=["pV = νRT", "p = νRT/V"],
             aprekins=["1)  νRT = 2,0 · 8,31 · 300 = 4986 J",
                       "2)  p = 4986 : 0,050",
                       "3)  p ≈ 1,0·10⁵ Pa = 100 kPa"],
             atbilde="p ≈ 1,0·10⁵ Pa",
             piezime="Iznākums ir apmēram atmosfēras spiediens - "
                     "saprātīgs rezultāts."),
        dict(nr=2, virsraksts="Viens mols normālos apstākļos",
             teksts="Cik lielu tilpumu aizņem 1,0 mol gāzes pie 101 kPa\n"
                    "un 273 K? (R = 8,31 J/(mol·K))",
             dots=["ν = 1,0 mol", "p = 101 kPa = 101 000 Pa",
                   "T = 273 K"],
             jaaprekina=["V = ?"],
             formulas=["pV = νRT", "V = νRT/p"],
             aprekins=["1)  νRT = 1,0 · 8,31 · 273 ≈ 2269 J",
                       "2)  V = 2269 : 101 000",
                       "3)  V ≈ 0,0225 m³ ≈ 22,5 L"],
             atbilde="V ≈ 22,5 L",
             piezime="Tā ir zināmā vērtība: normālos apstākļos viens "
                     "mols gāzes aizņem apmēram 22,4 litrus."),
        dict(nr=3, virsraksts="Vielas daudzums balonā",
             teksts="Balonā ar tilpumu 0,010 m³ spiediens ir 2,0·10⁵ Pa,\n"
                    "temperatūra 300 K. Aprēķini vielas daudzumu!\n"
                    "(R = 8,31 J/(mol·K))",
             dots=["V = 0,010 m³", "p = 2,0·10⁵ Pa", "T = 300 K"],
             jaaprekina=["ν = ?"],
             formulas=["pV = νRT", "ν = pV/RT"],
             aprekins=["1)  pV = 2,0·10⁵ · 0,010 = 2000 J",
                       "2)  RT = 8,31 · 300 = 2493",
                       "3)  ν = 2000 : 2493 ≈ 0,80 mol"],
             atbilde="ν ≈ 0,80 mol",
             piezime="Zinot ν un molmasu, var atrast arī gāzes masu: "
                     "m = νM."),
        dict(nr=4, virsraksts="Mērvienību pārrēķins",
             teksts="Traukā ir 20 L gāzes pie 27 °C un 150 kPa.\n"
                    "Aprēķini vielas daudzumu!\n"
                    "(R = 8,31 J/(mol·K))",
             dots=["V = 20 L = 0,020 m³", "t = 27 °C",
                   "p = 150 kPa = 150 000 Pa"],
             jaaprekina=["ν = ?"],
             formulas=["T = t + 273", "ν = pV/RT"],
             aprekins=["1)  T = 27 + 273 = 300 K",
                       "2)  pV = 150 000 · 0,020 = 3000 J",
                       "3)  ν = 3000 : (8,31 · 300) ≈ 1,2 mol"],
             atbilde="ν ≈ 1,2 mol",
             piezime="Trīs pārrēķini pirms aprēķina: litri kubikmetros, "
                     "kilopaskāli paskālos, grādi kelvinos."),
        dict(nr=5, virsraksts="Gāzes masa balonā",
             teksts="Balonā ir 0,80 mol slāpekļa (M = 28 g/mol).\n"
                    "Aprēķini gāzes masu!",
             dots=["ν = 0,80 mol", "M = 28 g/mol"],
             jaaprekina=["m = ?"],
             formulas=["m = νM"],
             aprekins=["1)  m = 0,80 · 28",
                       "2)  m = 22,4 g",
                       "3)  m ≈ 0,022 kg"],
             atbilde="m ≈ 22 g",
             piezime="Zinot pV = νRT, no spiediena un tilpuma var "
                     "noteikt arī gāzes masu."),
        dict(nr=6, virsraksts="Temperatūra no stāvokļa vienādojuma",
             teksts="Traukā ar tilpumu 0,020 m³ ir 2,0 mol gāzes pie\n"
                    "spiediena 2,5·10⁵ Pa. Aprēķini temperatūru!\n"
                    "(R = 8,31 J/(mol·K))",
             dots=["V = 0,020 m³", "ν = 2,0 mol", "p = 2,5·10⁵ Pa"],
             jaaprekina=["T = ?"],
             formulas=["pV = νRT", "T = pV/(νR)"],
             aprekins=["1)  pV = 2,5·10⁵ · 0,020 = 5000 J",
                       "2)  νR = 2,0 · 8,31 = 16,62",
                       "3)  T = 5000 : 16,62 ≈ 301 K = 28 °C"],
             atbilde="T ≈ 3,0·10² K ≈ 28 °C",
             piezime="Ticamības pārbaude: istabas temperatūra - "
                     "saprātīgs rezultāts."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "pV = νRT saista spiedienu, tilpumu, vielas daudzumu un "
            "temperatūru.",
            "Aprēķinos lieto paskālus, kubikmetrus un kelvinus.",
            "Normālos apstākļos viens mols gāzes aizņem apmēram 22,4 L.",
            "Ideālās gāzes modelis neder pie ļoti augsta spiediena vai "
            "zemas temperatūras.",
        ],
        majasdarbs=[
            "ν = 3,0 mol, V = 0,10 m³, T = 300 K. Aprēķini p.",
            "p = 100 kPa, V = 0,050 m³, T = 290 K. Aprēķini ν.",
            "Atkārto 7.1.-7.6. stundu kopsavilkumus - nākamā stunda ir "
            "PD2.",
        ],
        pasvertejums=["Zinu vienādojuma lielumus",
                      "Protu izteikt p, V un ν",
                      "Protu pārrēķināt mērvienības",
                      "Zinu modeļa robežas"],
        nakama="Nākamā stunda: PD2 - atoma un vielas uzbūve."),
),

]
