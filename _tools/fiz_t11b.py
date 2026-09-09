# -*- coding: utf-8 -*-
"""11. temats. B daļa: 11.6.-11.10. stunda.

LD3 «Transformatora darbības pētīšana» notiek pēc 11.9. stundas;
11.10. ir pēdējā mācību stunda pirms PD6.
"""

from fiz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN     # noqa: F401
from fiz_t11a import TEMATS, KICKER, KURSS, MAPE              # noqa: F401

STUNDAS = [

dict(
    nr="11.6", virsraksts="Maiņstrāva",
    jautajums="Ar ko maiņstrāva atšķiras no līdzstrāvas?",
    apaksraksts="Periods un frekvence · 50 Hz · Efektīvās vērtības",
    merkis="Lasīt maiņstrāvas grafiku un skaidrot frekvences un efektīvo "
           "vērtību jēgu.",
    protu=["atšķirt maiņstrāvu no līdzstrāvas;",
           "nolasīt maiņstrāvas grafiku;",
           "aprēķināt periodu un frekvenci;",
           "izskaidrot, ko nozīmē 230 V."],
    atkartojums="6. tematā svārstības un periodu jau mācījāmies. "
                "Maiņstrāva ir tieši tāda pati periodiska svārstība - "
                "tikai svārstās spriegums un strāva.",
    uzdevumu_apraksts="Maiņstrāvas grafiks un raksturlielumi",
    teorija=[
        ("Maiņstrāva un līdzstrāva", [
            ("divi",
             ("LĪDZSTRĀVA", BLUE,
              ["Virziens nemainās.",
               "Grafiks - horizontāla līnija.",
               "Avoti: baterijas,",
               "akumulatori, saules panelis.",
               "Elektronikā un auto."]),
             ("MAIŅSTRĀVA", GREEN,
              ["Virziens periodiski mainās.",
               "Grafiks - sinusoīda.",
               "Avots: ģenerators.",
               "Latvijā 50 Hz.",
               "Mājas tīklā un rūpniecībā."])),
            ("formula", "MAIŅSTRĀVAS RAKSTURLIELUMI",
             "T = 1/f        f = 50 Hz        U(ef) = U(max)/√2",
             "Periods rāda, cik ilgi notiek viena pilna svārstība. "
             "Efektīvā vērtība ir tā līdzstrāva, kas sildītājā dotu tādu "
             "pašu siltuma daudzumu - tieši to rāda voltmetrs.", GOLD),
        ]),
        ("Ko nozīmē 230 volti", [
            ("tabula",
             ["Lielums", "Vērtība Latvijā", "Piezīme"],
             [["Frekvence", "50 Hz", "50 svārstības sekundē"],
              ["Periods", "0,02 s", "T = 1/f"],
              ["Efektīvais spriegums", "230 V", "To rāda voltmetrs"],
              ["Maksimālais spriegums", "≈ 325 V", "Sinusoīdas virsotne"]],
             [3.60, 3.00, 3.63]),
            ("panelis", "KĀPĒC TIEŠI MAIŅSTRĀVA",
             ["Maiņstrāvas spriegumu var viegli paaugstināt un pazemināt "
              "ar transformatoru - līdzstrāvai tas ir daudz grūtāk.",
              "Tieši tāpēc elektrību pārvada ar maiņstrāvu: augstā "
              "spriegumā zudumi ir mazi.",
              "Ierīces, kurām vajag līdzstrāvu, savā lādētājā satur "
              "transformatoru un diožu taisngriezi."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Periods no frekvences",
             teksts="Latvijas elektrotīkla frekvence ir 50 Hz.\n"
                    "Aprēķini periodu un svārstību skaitu minūtē!",
             dots=["f = 50 Hz", "t = 1 min = 60 s"],
             jaaprekina=["T = ?", "N = ?"],
             formulas=["T = 1/f", "N = t/T"],
             aprekins=["1)  T = 1 : 50 = 0,02 s",
                       "2)  N = 60 : 0,02",
                       "3)  N = 3000 svārstības"],
             atbilde="T = 0,02 s;  N = 3000",
             piezime="Tā pati formula, ko lietojām 6. tematā - "
                     "svārstības ir svārstības."),
        dict(nr=2, virsraksts="Maksimālais spriegums",
             teksts="Efektīvais spriegums ir 230 V.\n"
                    "Aprēķini maksimālo spriegumu! (√2 ≈ 1,41)",
             dots=["U(ef) = 230 V", "√2 ≈ 1,41"],
             jaaprekina=["U(max) = ?"],
             formulas=["U(ef) = U(max)/√2", "U(max) = U(ef)·√2"],
             aprekins=["1)  U(max) = 230 · 1,41",
                       "2)  U(max) ≈ 324 V"],
             atbilde="U(max) ≈ 325 V",
             piezime="Izolācija rozetē jāaprēķina uz 325 V, nevis "
                     "230 V - tas ir svarīgi drošībai."),
        dict(nr=3, virsraksts="Grafika nolasīšana",
             teksts="Maiņstrāvas grafikā viena pilna svārstība aizņem\n"
                    "0,025 s, bet maksimālais spriegums ir 12 V.\n"
                    "Aprēķini frekvenci un efektīvo spriegumu!",
             dots=["T = 0,025 s", "U(max) = 12 V", "√2 ≈ 1,41"],
             jaaprekina=["f = ?", "U(ef) = ?"],
             formulas=["f = 1/T", "U(ef) = U(max)/√2"],
             aprekins=["1)  f = 1 : 0,025 = 40 Hz",
                       "2)  U(ef) = 12 : 1,41",
                       "3)  U(ef) ≈ 8,5 V"],
             atbilde="f = 40 Hz;  U(ef) ≈ 8,5 V",
             piezime="Grafikā redz maksimālo vērtību, bet voltmetrs "
                     "rāda efektīvo - tās nesajauc."),
        dict(nr=4, virsraksts="Jauda maiņstrāvā",
             teksts="Sildītājs pie 230 V patērē 4,0 A.\n"
                    "Aprēķini jaudu un patēriņu 3 stundās!",
             dots=["U = 230 V", "I = 4,0 A", "t = 3 h"],
             jaaprekina=["P = ?", "E = ?"],
             formulas=["P = UI", "E = Pt"],
             aprekins=["1)  P = 230 · 4,0 = 920 W",
                       "2)  P = 0,92 kW",
                       "3)  E = 0,92 · 3 = 2,76 kWh"],
             atbilde="P = 920 W;  E ≈ 2,8 kWh",
             piezime="Ar efektīvajām vērtībām jaudu rēķina tāpat kā "
                     "līdzstrāvā - tieši tāpēc tās ir ieviestas."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Maiņstrāvā virziens periodiski mainās.",
            "Latvijā frekvence ir 50 Hz, periods 0,02 s.",
            "230 V ir efektīvā vērtība; maksimālā ir apmēram 325 V.",
            "Ar efektīvajām vērtībām jaudu rēķina kā līdzstrāvā.",
        ],
        majasdarbs=[
            "f = 60 Hz. Aprēķini periodu.",
            "U(max) = 170 V. Aprēķini efektīvo spriegumu.",
            "Nosauc trīs ierīces ar līdzstrāvu un trīs ar maiņstrāvu.",
        ],
        pasvertejums=["Atšķiru maiņstrāvu no līdzstrāvas",
                      "Protu lasīt grafiku",
                      "Protu rēķināt T un f",
                      "Zinu, ko nozīmē 230 V"],
        nakama="Nākamā stunda: transformators un LD3 plāns."),
),

dict(
    nr="11.7", virsraksts="Transformators un LD3 plāns",
    jautajums="Kāpēc elektrības pārvadē maina spriegumu?",
    apaksraksts="U₁/U₂ = N₁/N₂ · Paaugstinošs un pazeminošs · LD3 plāns",
    merkis="Skaidrot transformatora darbības nosacījumu, lietot vijumu un "
           "spriegumu attiecību un sagatavot LD3 mērījumus.",
    protu=["izskaidrot transformatora darbību;",
           "nosaukt, kāpēc tas strādā tikai ar maiņstrāvu;",
           "lietot U₁/U₂ = N₁/N₂;",
           "sagatavot LD3 mērījumu tabulu."],
    atkartojums="11.4. stundā noskaidrojām, ka spriegumu rada plūsmas "
                "IZMAIŅA. Transformators ir tiešs šī likuma "
                "pielietojums.",
    uzdevumu_apraksts="Transformatora aprēķini un LD3 plānošana",
    teorija=[
        ("Transformators", [
            ("formula", "VIJUMU UN SPRIEGUMU ATTIECĪBA",
             "U₁/U₂ = N₁/N₂        U₂ = U₁N₂/N₁",
             "Uz kopīgas serdes ir divas spoles. Primārā spole rada "
             "mainīgu plūsmu, kas sekundārajā inducē spriegumu. Spriegumi "
             "attiecas tāpat kā vijumu skaiti.", GOLD),
            ("divi",
             ("PAAUGSTINOŠS", RED,
              ["N₂ > N₁.",
               "Spriegums pieaug.",
               "Strāva samazinās.",
               "Lieto elektrostacijā",
               "pirms pārvades līnijas."]),
             ("PAZEMINOŠS", GREEN,
              ["N₂ < N₁.",
               "Spriegums samazinās.",
               "Strāva pieaug.",
               "Lieto apakšstacijā",
               "un lādētājos."])),
        ]),
        ("LD3 sagatavošana", [
            ("panelis", "KĀPĒC TIKAI MAIŅSTRĀVA",
             ["Transformators darbojas TIKAI ar maiņstrāvu: līdzstrāvā "
              "plūsma nemainās, tāpēc sekundārajā spolē spriegums "
              "neinducējas.",
              "Jauda abās spolēs ir gandrīz vienāda: I₁U₁ ≈ I₂U₂; "
              "paaugstinot spriegumu, strāva tikpat reižu samazinās.",
              "LD3 uzdevums: mērīt U₁ un U₂ vairākām vijumu attiecībām un "
              "pārbaudīt, vai sakarība izpildās."], NAVY),
            ("tabula",
             ["N₁", "N₂", "U₁ (V)", "U₂ (V) - izmērītais"],
             [["600", "300", "6,0", ""],
              ["600", "600", "6,0", ""],
              ["600", "1200", "6,0", ""],
              ["300", "600", "6,0", ""]],
             [2.40, 2.40, 3.00, 4.43]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Pazeminošs transformators",
             teksts="Transformatoram N₁ = 1000 vijumi, N₂ = 50 vijumi,\n"
                    "U₁ = 230 V. Aprēķini sekundāro spriegumu!",
             dots=["N₁ = 1000", "N₂ = 50", "U₁ = 230 V"],
             jaaprekina=["U₂ = ?"],
             formulas=["U₁/U₂ = N₁/N₂", "U₂ = U₁N₂/N₁"],
             aprekins=["1)  U₁N₂ = 230 · 50 = 11 500",
                       "2)  U₂ = 11 500 : 1000",
                       "3)  U₂ = 11,5 V"],
             atbilde="U₂ = 11,5 V",
             piezime="Tieši tā darbojas zvana vai durvju domofona "
                     "barošanas bloks."),
        dict(nr=2, virsraksts="Paaugstinošs transformators",
             teksts="Elektrostacijā U₁ = 10 kV, N₁ = 500 vijumi,\n"
                    "N₂ = 16 500 vijumi. Aprēķini sekundāro spriegumu!",
             dots=["U₁ = 10 kV", "N₁ = 500", "N₂ = 16 500"],
             jaaprekina=["U₂ = ?"],
             formulas=["U₂ = U₁N₂/N₁"],
             aprekins=["1)  N₂ : N₁ = 16 500 : 500 = 33",
                       "2)  U₂ = 10 · 33",
                       "3)  U₂ = 330 kV"],
             atbilde="U₂ = 330 kV",
             piezime="330 kilovoltu līnijas ir Latvijas pārvades tīkla "
                     "pamats."),
        dict(nr=3, virsraksts="Vijumu skaits",
             teksts="Lādētājam vajag 12 V no 230 V tīkla. Primārajā spolē\n"
                    "ir 1150 vijumu. Cik vijumu vajag sekundārajā?",
             dots=["U₁ = 230 V", "U₂ = 12 V", "N₁ = 1150"],
             jaaprekina=["N₂ = ?"],
             formulas=["U₁/U₂ = N₁/N₂", "N₂ = N₁U₂/U₁"],
             aprekins=["1)  N₁U₂ = 1150 · 12 = 13 800",
                       "2)  N₂ = 13 800 : 230",
                       "3)  N₂ = 60 vijumu"],
             atbilde="N₂ = 60 vijumu",
             piezime="Attiecība 230 : 12 ir apmēram 19 - tik reižu "
                     "atšķiras arī vijumu skaiti."),
        dict(nr=4, virsraksts="Strāva sekundārajā spolē",
             teksts="Transformators no 230 V dod 11,5 V. Sekundārajā ķēdē\n"
                    "strāva ir 2,0 A. Aprēķini strāvu primārajā spolē,\n"
                    "pieņemot, ka zudumu nav!",
             dots=["U₁ = 230 V", "U₂ = 11,5 V", "I₂ = 2,0 A"],
             jaaprekina=["I₁ = ?"],
             formulas=["I₁U₁ = I₂U₂", "I₁ = I₂U₂/U₁"],
             aprekins=["1)  I₂U₂ = 2,0 · 11,5 = 23 W",
                       "2)  I₁ = 23 : 230",
                       "3)  I₁ = 0,10 A"],
             atbilde="I₁ = 0,10 A",
             piezime="Spriegums samazināts 20 reizes - strāva tikpat "
                     "reižu pieaugusi. Jauda paliek tā pati."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Transformators darbojas tikai ar maiņstrāvu.",
            "U₁/U₂ = N₁/N₂.",
            "Paaugstinot spriegumu, strāva samazinās; jauda saglabājas.",
            "LD3 pārbaudīsim šo sakarību ar mērījumiem.",
        ],
        majasdarbs=[
            "N₁ = 800, N₂ = 200, U₁ = 24 V. Aprēķini U₂.",
            "U₁ = 230 V, U₂ = 5,0 V, N₁ = 920. Aprēķini N₂.",
            "Sagatavo LD3 datu tabulu ar četrām vijumu attiecībām.",
        ],
        pasvertejums=["Zinu transformatora darbību",
                      "Zinu, kāpēc vajag maiņstrāvu",
                      "Protu lietot vijumu attiecību",
                      "Esmu sagatavojis LD3 tabulu"],
        nakama="Nākamā stunda: elektroenerģijas pārvade."),
),

dict(
    nr="11.8", virsraksts="Elektroenerģijas pārvade",
    jautajums="Kāpēc pārvadei izmanto augstu spriegumu?",
    apaksraksts="Zudumi P = I²R · Augstsprieguma līnijas · Pārvades ķēde",
    merkis="Skaidrot strāvas un siltuma zudumu saistību un analizēt "
           "enerģijas pārvades ķēdi.",
    protu=["izskaidrot, kāpēc vados rodas zudumi;",
           "lietot P = I²R;",
           "izskaidrot, kāpēc augsts spriegums samazina zudumus;",
           "izsekot pārvades ķēdei no stacijas līdz rozetei."],
    atkartojums="10. tematā vados zaudēto jaudu jau rēķinājām ar P = I²R. "
                "Šodien redzēsim, kāpēc tieši šī formula nosaka visu "
                "pārvades tīkla uzbūvi.",
    uzdevumu_apraksts="Pārvades zudumu aprēķini",
    teorija=[
        ("Zudumi vados", [
            ("formula", "SILTUMA ZUDUMI PĀRVADES LĪNIJĀ",
             "P = I²R        P = UI",
             "Zudumi ir atkarīgi no strāvas KVADRĀTA. Ja to pašu jaudu "
             "pārvada ar 10 reizes lielāku spriegumu, strāva samazinās "
             "10 reizes, bet zudumi - 100 reizes.", GOLD),
            ("tabula",
             ["Spriegums", "Strāva (1 MW)", "Zudumi pie R = 10 Ω"],
             [["1 kV", "1000 A", "10 000 kW - neiespējami"],
              ["10 kV", "100 A", "100 kW"],
              ["110 kV", "9,1 A", "0,83 kW"],
              ["330 kV", "3,0 A", "0,09 kW"]],
             [2.80, 3.40, 4.03]),
        ]),
        ("Pārvades ķēde", [
            ("panelis", "NO STACIJAS LĪDZ ROZETEI",
             ["Ģenerators saražo apmēram 10 kV; paaugstinošais "
              "transformators to paceļ līdz 110-330 kV.",
              "Augstsprieguma līnijas pārvada enerģiju simtiem kilometru "
              "ar nelieliem zudumiem.",
              "Apakšstacijās spriegumu pakāpeniski pazemina: 110 kV → "
              "20 kV → 400/230 V mājās."], NAVY),
            ("divi",
             ("KĀPĒC NE ZEMSPRIEGUMS", RED,
              ["Tā pati jauda prasa",
               "milzīgu strāvu.",
               "Zudumi aug ar I².",
               "Vadi būtu jāveido",
               "neiespējami biezi."]),
             ("KĀPĒC NE VĒL AUGSTĀKS", GOLD,
              ["Vajag lielākus attālumus",
               "starp vadiem.",
               "Dārgāka izolācija.",
               "Augstāki balsti.",
               "Izvēlas saprātīgu robežu."])),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Zudumi pie mazas strāvas",
             teksts="Pārvades līnijas pretestība ir 8,0 Ω, strāva 20 A.\n"
                    "Aprēķini siltuma zudumus!",
             dots=["R = 8,0 Ω", "I = 20 A"],
             jaaprekina=["P = ?"],
             formulas=["P = I²R"],
             aprekins=["1)  I² = 400",
                       "2)  P = 400 · 8,0",
                       "3)  P = 3200 W = 3,2 kW"],
             atbilde="P = 3,2 kW",
             piezime="Šī jauda vienkārši sasilda vadus - tā ir "
                     "zaudēta."),
        dict(nr=2, virsraksts="Strāvu divkāršo",
             teksts="Tajā pašā līnijā strāva pieaug līdz 40 A.\n"
                    "Aprēķini zudumus un salīdzini ar iepriekšējiem!",
             dots=["R = 8,0 Ω", "I = 40 A", "P₁ = 3,2 kW"],
             jaaprekina=["P₂ = ?"],
             formulas=["P = I²R"],
             aprekins=["1)  I² = 1600",
                       "2)  P₂ = 1600 · 8,0 = 12 800 W",
                       "3)  P₂ = 12,8 kW - četras reizes vairāk"],
             atbilde="P₂ = 12,8 kW",
             piezime="Strāva divkāršojās - zudumi pieauga četrkārt. Tas "
                     "ir kvadrāta efekts."),
        dict(nr=3, virsraksts="Kāda strāva vajadzīga",
             teksts="Jāpārvada 500 kW jaudas. Aprēķini strāvu, ja\n"
                    "spriegums ir a) 10 kV; b) 110 kV!",
             dots=["P = 500 kW = 500 000 W",
                   "U₁ = 10 000 V", "U₂ = 110 000 V"],
             jaaprekina=["I₁ = ?", "I₂ = ?"],
             formulas=["P = UI", "I = P/U"],
             aprekins=["1)  I₁ = 500 000 : 10 000 = 50 A",
                       "2)  I₂ = 500 000 : 110 000 ≈ 4,5 A",
                       "3)  Strāva samazinājusies 11 reizes"],
             atbilde="I₁ = 50 A;  I₂ ≈ 4,5 A",
             piezime="Zudumi samazinās 11² ≈ 120 reizes - tieši tāpēc "
                     "spriegumu paaugstina."),
        dict(nr=4, virsraksts="Zudumu daļa",
             teksts="Līnijā pārvada 500 kW, zudumi ir 3,2 kW.\n"
                    "Cik procentu enerģijas zaudē pārvadē?",
             dots=["P = 500 kW", "P(zud.) = 3,2 kW"],
             jaaprekina=["Daļa = ?"],
             formulas=["Daļa = P(zud.)/P"],
             aprekins=["1)  3,2 : 500 = 0,0064",
                       "2)  Daļa = 0,64 %",
                       "3)  Līdz patērētājam nonāk 99,4 %"],
             atbilde="Zudumi ≈ 0,64 %",
             piezime="Latvijas pārvades tīklā zudumi ir daži procenti - "
                     "tas ir labs rādītājs."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Zudumi vados P = I²R - atkarīgi no strāvas kvadrāta.",
            "Augstāks spriegums nozīmē mazāku strāvu un mazākus zudumus.",
            "Pārvades ķēde: ģenerators → paaugstinošais → līnija → "
            "pazeminošais.",
            "Spriegumu izvēlas kā kompromisu starp zudumiem un izolācijas "
            "izmaksām.",
        ],
        majasdarbs=[
            "R = 5,0 Ω, I = 30 A. Aprēķini zudumus.",
            "P = 200 kW, U = 20 kV. Aprēķini strāvu.",
            "Uzraksti pārvades ķēdi no stacijas līdz mājas rozetei.",
        ],
        pasvertejums=["Zinu, kāpēc rodas zudumi",
                      "Protu lietot P = I²R",
                      "Saprotu kvadrāta efektu",
                      "Zinu pārvades ķēdi"],
        nakama="Nākamā stunda: dati, enerģija un lietojumi."),
),

dict(
    nr="11.9", virsraksts="Dati, enerģija un lietojumi",
    jautajums="Kā atšķirt motora, ģeneratora un transformatora darbību?",
    apaksraksts="Enerģijas plūsma · Grafiku analīze · Biežākās kļūdas",
    merkis="Salīdzināt ierīces un enerģijas plūsmu un labot grafiku un "
           "spriegumu attiecību uzdevumu kļūdas.",
    protu=["atšķirt trīs elektromagnētiskās ierīces;",
           "izsekot enerģijas plūsmai;",
           "atrast kļūdu transformatora aprēķinā;",
           "pārbaudīt datu ticamību."],
    atkartojums="Temata galvenās ierīces jau apgūtas. Šodien tās "
                "salīdzināsim un iemācīsimies pamanīt kļūdas - pēc tam "
                "seko LD3.",
    uzdevumu_apraksts="Ierīču salīdzināšana un kļūdu meklēšana",
    teorija=[
        ("Trīs ierīces", [
            ("tabula",
             ["Ierīce", "Kas ievadīts", "Kas iegūts", "Kas kustas"],
             [["Motors", "Elektroenerģija", "Mehāniskā", "Rotors griežas"],
              ["Ģenerators", "Mehāniskā", "Elektroenerģija", "Rotors griežas"],
              ["Transformators", "Maiņstrāva", "Maiņstrāva", "Nekas nekustas"],
              ["Elektromagnēts", "Elektroenerģija", "Magnētiskais lauks",
               "Serde pievelk"]],
             [2.90, 2.90, 2.90, 3.53]),
            ("panelis", "GALVENĀ ATŠĶIRĪBA",
             ["Transformatorā nekas nekustas - plūsmu maina pati "
              "maiņstrāva. Tāpēc tas nedarbojas ar līdzstrāvu.",
              "Motorā un ģeneratorā rotors griežas; atšķiras tikai "
              "enerģijas virziens.",
              "Ja uzdevumā minēta līdzstrāva un transformators - tā "
              "vienmēr ir kļūda uzdevuma nosacījumos."], NAVY),
        ]),
        ("Biežākās kļūdas", [
            ("divi",
             ("GRAFIKĀ", RED,
              ["Sajauc maksimālo un",
               "efektīvo vērtību.",
               "Periodu nolasa starp",
               "kalnu un ieleju.",
               "Aizmirst, ka f = 1/T."]),
             ("APRĒĶINĀ", GOLD,
              ["Apgriež vijumu attiecību.",
               "Kilovoltus neatstāj voltos.",
               "Aizmirst, ka jauda",
               "abās spolēs vienāda.",
               "Neizvērtē, vai atbilde",
               "saprātīga."])),
            ("panelis", "ĀTRĀ PĀRBAUDE TRANSFORMATORAM",
             ["Ja sekundārajā spolē vijumu ir MAZĀK, tad spriegumam "
              "jābūt MAZĀKAM - un otrādi.",
              "Jaudas pārbaude: I₁U₁ ≈ I₂U₂. Ja abas puses stipri "
              "atšķiras, aprēķinā ir kļūda.",
              "Šīs divas pārbaudes atklāj gandrīz visas biežākās "
              "kļūdas."], GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Kura ierīce",
             teksts="Nosaki ierīci: a) vējš griež spoli un rodas strāva;\n"
                    "b) maiņstrāva vienā spolē rada spriegumu otrā;\n"
                    "c) strāva liek griezties rotoram.",
             dots=["a) vējš un strāva", "b) divas spoles",
                   "c) strāva un griešanās"],
             jaaprekina=["Kura ierīce?"],
             formulas=["Ģenerators: mehāniskā → elektriskā",
                       "Transformators: maina spriegumu",
                       "Motors: elektriskā → mehāniskā"],
             aprekins=["1)  a) ģenerators",
                       "2)  b) transformators",
                       "3)  c) motors"],
             atbilde="a) ģenerators; b) transformators; c) motors",
             piezime="Atslēga ir enerģijas virziens - kas ievadīts un "
                     "kas iegūts."),
        dict(nr=2, virsraksts="Atrodi kļūdu",
             teksts="Skolēns rēķināja: N₁ = 100, N₂ = 500, U₁ = 12 V,\n"
                    "un ieguva U₂ = 2,4 V. Vai tas ir pareizi?\n"
                    "Aprēķini pareizi!",
             dots=["N₁ = 100", "N₂ = 500", "U₁ = 12 V"],
             jaaprekina=["U₂ = ?"],
             formulas=["U₂ = U₁N₂/N₁"],
             aprekins=["1)  N₂ > N₁, tātad U₂ jābūt LIELĀKAM",
                       "2)  U₂ = 12 · 500 : 100",
                       "3)  U₂ = 60 V"],
             atbilde="U₂ = 60 V - skolēns attiecību apgriezis",
             piezime="Pirmā pārbaude vienmēr: vairāk vijumu - lielāks "
                     "spriegums."),
        dict(nr=3, virsraksts="Jaudas pārbaude",
             teksts="Transformatorā U₁ = 230 V, I₁ = 0,50 A,\n"
                    "U₂ = 23 V. Aprēķini I₂ un pārbaudi jaudas!",
             dots=["U₁ = 230 V", "I₁ = 0,50 A", "U₂ = 23 V"],
             jaaprekina=["I₂ = ?"],
             formulas=["I₁U₁ = I₂U₂", "I₂ = I₁U₁/U₂"],
             aprekins=["1)  P₁ = 230 · 0,50 = 115 W",
                       "2)  I₂ = 115 : 23",
                       "3)  I₂ = 5,0 A;  P₂ = 23 · 5,0 = 115 W"],
             atbilde="I₂ = 5,0 A",
             piezime="Jaudas sakrīt - tātad aprēķins ir pareizs."),
        dict(nr=4, virsraksts="Grafika kļūda",
             teksts="Skolēns no maiņstrāvas grafika nolasīja T = 0,01 s\n"
                    "(no kalna līdz ielejai) un ieguva f = 100 Hz.\n"
                    "Atrodi kļūdu!",
             dots=["Nolasīts 0,01 s", "Kalns līdz ielejai",
                   "Iegūts f = 100 Hz"],
             jaaprekina=["Pareizais f = ?"],
             formulas=["No kalna līdz ielejai ir pusperiods",
                       "f = 1/T"],
             aprekins=["1)  0,01 s ir PUSE perioda",
                       "2)  T = 2 · 0,01 = 0,02 s",
                       "3)  f = 1 : 0,02 = 50 Hz"],
             atbilde="f = 50 Hz",
             piezime="Tā ir tā pati kļūda, ko mācījāmies pamanīt "
                     "6. tematā ar viļņu grafikiem."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Motors, ģenerators un transformators atšķiras ar enerģijas "
            "plūsmu.",
            "Transformatorā nekas nekustas un vajadzīga maiņstrāva.",
            "Vairāk vijumu - lielāks spriegums.",
            "Jaudas pārbaude I₁U₁ ≈ I₂U₂ atklāj aprēķina kļūdas.",
        ],
        majasdarbs=[
            "N₁ = 200, N₂ = 1000, U₁ = 10 V. Aprēķini U₂.",
            "U₁ = 230 V, I₁ = 0,20 A, U₂ = 46 V. Aprēķini I₂.",
            "Sagatavojies LD3: atkārto shēmu un drošības noteikumus.",
        ],
        pasvertejums=["Protu atšķirt ierīces",
                      "Zinu enerģijas plūsmu",
                      "Protu atrast kļūdu aprēķinā",
                      "Esmu gatavs LD3"],
        nakama="Nākamā stunda: LD3 - transformatora darbības pētīšana "
               "dubultstundā."),
),

dict(
    nr="11.10", virsraksts="Elektromagnētisma nostiprināšana",
    jautajums="Kā izskaidrot elektromagnētisku ierīci?",
    apaksraksts="Skaidrojuma struktūra · Visas temata sakarības · "
                "Gatavošanās PD6",
    merkis="Ar shēmu un īsu tekstu izskaidrot vienas ierīces darbību, "
           "izmantojot apgūtās sakarības.",
    protu=["izskaidrot ierīces darbību piecos soļos;",
           "izvēlēties pareizo sakarību;",
           "risināt temata kombinētos uzdevumus;",
           "sagatavoties PD6."],
    atkartojums="Šī ir temata pēdējā mācību stunda. PD6 prasīs gan "
                "skaidrojumu, gan grafika lasīšanu, gan transformatora "
                "aprēķinu.",
    uzdevumu_apraksts="Kombinēti uzdevumi pirms PD6",
    teorija=[
        ("Kā izskaidrot ierīci", [
            ("panelis", "PIECI SOĻI SKAIDROJUMĀ",
             ["1. Kas ierīcē ir: spole, magnēts, serde, rotors.",
              "2. Kas tajā mainās vai kustas.",
              "3. Kurš likums darbojas: indukcija vai spēks laukā.",
              "4. Kāda enerģija ievadīta, kāda iegūta un kur to lieto."],
             NAVY),
            ("tabula",
             ["Kad lietot", "Formula", "Ko pārbaudīt"],
             [["Spēks uz vadu", "F = BIl", "Vads perpendikulārs laukam"],
              ["Spēks uz lādiņu", "F = qvB", "Lādiņš kustas"],
              ["Plūsma", "Φ = BS", "Laukums kvadrātmetros"],
              ["Indukcija", "ε = ΔΦ/Δt", "Plūsma MAINĀS"],
              ["Transformators", "U₁/U₂ = N₁/N₂", "Vairāk vijumu - vairāk V"]],
             [3.00, 3.20, 4.03]),
        ]),
        ("PD6 sagatavošanās", [
            ("divi",
             ("KAS BŪS PD6", BLUE,
              ["Magnētisma piemēra",
               "skaidrojums.",
               "Indukcijas skaidrojums.",
               "Maiņstrāvas grafiks.",
               "Transformatora aprēķins."]),
             ("BIEŽĀKĀS KĻŪDAS", RED,
              ["Jauc lauka stiprumu ar",
               "tā izmaiņu.",
               "Apgriež vijumu attiecību.",
               "Grafikā nolasa pusperiodu.",
               "Aizmirst, ka transformators",
               "nestrādā ar līdzstrāvu."])),
            ("panelis", "PĒDĒJAIS PADOMS",
             ["Uzraksti formulu lapu pats un pieraksti blakus, KAD katru "
              "formulu lieto.",
              "Skaidrojuma uzdevumos raksti īsi, bet ar fizikas "
              "terminiem: plūsma, indukcija, lauks.",
              "Aprēķinos vispirms pārbaudi loģiku (lielāks vai mazāks), "
              "tikai tad rēķini."], GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Spēks motorā",
             teksts="Motora vads 0,12 m laukā 0,45 T, strāva 2,5 A.\n"
                    "Aprēķini spēku uz vienu vadu!",
             dots=["l = 0,12 m", "B = 0,45 T", "I = 2,5 A"],
             jaaprekina=["F = ?"],
             formulas=["F = BIl"],
             aprekins=["1)  F = 0,45 · 2,5 · 0,12",
                       "2)  F = 0,135 N",
                       "3)  F ≈ 0,14 N"],
             atbilde="F ≈ 0,14 N",
             piezime="Ar simtiem vijumu kopējais spēks jau ir "
                     "desmitiem ņūtonu."),
        dict(nr=2, virsraksts="Indukcija spolē",
             teksts="Spolē ar 400 vijumiem plūsma 0,050 s laikā mainās\n"
                    "par 0,0025 Wb. Aprēķini inducēto spriegumu!",
             dots=["N = 400", "ΔΦ = 0,0025 Wb", "Δt = 0,050 s"],
             jaaprekina=["ε = ?"],
             formulas=["ε = N · ΔΦ/Δt"],
             aprekins=["1)  ΔΦ : Δt = 0,0025 : 0,050 = 0,050 V",
                       "2)  ε = 400 · 0,050",
                       "3)  ε = 20 V"],
             atbilde="ε = 20 V",
             piezime="Vijumu skaits ir reizinātājs - to nekad "
                     "neaizmirst."),
        dict(nr=3, virsraksts="Transformators un jauda",
             teksts="Transformators no 230 V dod 46 V. Sekundārajā ķēdē\n"
                    "pieslēgta 92 W spuldze. Aprēķini abas strāvas!",
             dots=["U₁ = 230 V", "U₂ = 46 V", "P = 92 W"],
             jaaprekina=["I₂ = ?", "I₁ = ?"],
             formulas=["P = UI", "I₁U₁ = I₂U₂"],
             aprekins=["1)  I₂ = 92 : 46 = 2,0 A",
                       "2)  P₁ = P₂ = 92 W",
                       "3)  I₁ = 92 : 230 = 0,40 A"],
             atbilde="I₂ = 2,0 A;  I₁ = 0,40 A",
             piezime="Spriegums pazemināts 5 reizes - strāva pieaugusi "
                     "5 reizes."),
        dict(nr=4, virsraksts="Izskaidro ierīci",
             teksts="Izskaidro indukcijas plīts darbību piecos soļos:\n"
                    "kas tajā ir, kas mainās, kurš likums darbojas,\n"
                    "enerģijas pārvērtība un kur to lieto!",
             dots=["Spole zem virsmas",
                   "Maiņstrāva 20-50 kHz",
                   "Metāla katls"],
             jaaprekina=["Skaidrojums = ?"],
             formulas=["ε = ΔΦ/Δt", "P = I²R"],
             aprekins=["1)  Spolē plūst augstas frekvences maiņstrāva",
                       "2)  Mainīgs lauks katla dibenā inducē virpuļstrāvas",
                       "3)  Tās sasilda katlu: elektriskā → siltuma"],
             atbilde="Indukcija rada strāvas pašā katlā",
             piezime="Tāpēc plīts virsma paliek gandrīz auksta, bet "
                     "katls sasilst - un stikla trauks nesilst vispār."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Ierīces skaidrojums: uzbūve, izmaiņa, likums, enerģija, "
            "lietojums.",
            "Temata formulas: F = BIl, F = qvB, Φ = BS, ε = ΔΦ/Δt, "
            "U₁/U₂ = N₁/N₂.",
            "Indukcija darbojas tikai pie plūsmas izmaiņas.",
            "Transformatorā jauda saglabājas.",
        ],
        majasdarbs=[
            "Atkārto 11.1.-11.9. stundas kopsavilkumus.",
            "B = 0,30 T, I = 3,0 A, l = 0,20 m. Aprēķini F.",
            "Sagatavo formulu lapu PD6 un uzraksti, kad katru lieto.",
        ],
        pasvertejums=["Protu izskaidrot ierīci",
                      "Protu izvēlēties formulu",
                      "Protu risināt kombinētus uzdevumus",
                      "Esmu gatavs PD6"],
        nakama="Nākamā stunda: PD6 - elektromagnētisms."),
),

]
