# -*- coding: utf-8 -*-
"""12. temats. B daļa: 12.5.-12.7. stunda.

LD4 «Difrakcijas režģa pētīšana» notiek pēc 12.5. stundas;
12.7. ir pēdējā mācību stunda pirms PD7.
"""

from fiz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN     # noqa: F401
from fiz_t12a import TEMATS, KICKER, KURSS, MAPE              # noqa: F401

STUNDAS = [

dict(
    nr="12.5", virsraksts="LD4 sagatavošana",
    jautajums="Kā noteikt gaismas viļņa garumu?",
    apaksraksts="Mērāmie attālumi · sin α = x/√(x² + L²) · Lāzera drošība",
    merkis="Noteikt mērāmos attālumus, izvēlēties aprēķina shēmu un "
           "sagatavot LD4 datu tabulu.",
    protu=["uzzīmēt darba shēmu ar attālumiem;",
           "izteikt sinusu no izmērītajiem attālumiem;",
           "sagatavot datu tabulu;",
           "nosaukt lāzera drošības noteikumus."],
    atkartojums="Iepriekšējā stundā apguvām režģa formulu. Laboratorijas "
                "darbā ar to noteiksim lāzera gaismas viļņa garumu.",
    uzdevumu_apraksts="Mērījumu shēma un aprēķinu sagatavošana",
    teorija=[
        ("Mērījumu shēma", [
            ("formula", "NO ATTĀLUMIEM UZ VIĻŅA GARUMU",
             "sin α = x/√(x² + L²)        λ = d·sin α/k",
             "L ir attālums no režģa līdz ekrānam, x - attālums no "
             "centrālā maksimuma līdz k-tās kārtas maksimumam. Ja x ir "
             "daudz mazāks par L, var lietot arī tan α = x/L.", GOLD),
            ("tabula",
             ["k", "x (m)", "L (m)", "sin α", "λ (m)"],
             [["1", "", "1,50", "", ""],
              ["2", "", "1,50", "", ""],
              ["1", "", "2,00", "", ""],
              ["2", "", "2,00", "", ""]],
             [1.80, 2.60, 2.60, 2.60, 2.63]),
        ]),
        ("Gaita un drošība", [
            ("panelis", "DARBA GAITA",
             ["1. Nostiprina lāzeru, režģi un ekrānu uz vienas taisnes; "
              "izmēra L.",
              "2. Uz ekrāna atzīmē centrālo maksimumu un pirmās un otrās "
              "kārtas maksimumus abās pusēs.",
              "3. Izmēra attālumu starp simetriskajiem maksimumiem un dala "
              "ar 2 - tā precizitāte ir labāka.",
              "4. Atkārto ar citu L; aprēķina λ katrai rindai un salīdzina."],
             NAVY),
            ("panelis", "LĀZERA DROŠĪBA",
             ["Nekad neskatās lāzera starā un nevērš to pret citiem - pat "
              "vājš stars var bojāt tīkleni.",
              "Staru vērš uz ekrānu, nevis uz spoguļojošām virsmām; "
              "noņem rokas pulksteni un spožas rotaslietas.",
              "Lāzeru ieslēdz tikai mērījuma laikā un nepārvieto "
              "ieslēgtu."], RED),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Sinuss no attālumiem",
             teksts="Attālums līdz ekrānam L = 1,50 m, pirmās kārtas\n"
                    "maksimums ir x = 0,40 m no centra.\n"
                    "Aprēķini sin α!",
             dots=["L = 1,50 m", "x = 0,40 m", "k = 1"],
             jaaprekina=["sin α = ?"],
             formulas=["sin α = x/√(x² + L²)"],
             aprekins=["1)  x² + L² = 0,16 + 2,25 = 2,41",
                       "2)  √2,41 ≈ 1,55",
                       "3)  sin α = 0,40 : 1,55 ≈ 0,258"],
             atbilde="sin α ≈ 0,26",
             piezime="Saucējā ir attālums no režģa līdz maksimumam - "
                     "taisnleņķa trijstūra hipotenūza."),
        dict(nr=2, virsraksts="Viļņa garums",
             teksts="Režģim d = 2·10⁻⁶ m, pirmajai kārtai sin α = 0,258.\n"
                    "Aprēķini viļņa garumu!",
             dots=["d = 2·10⁻⁶ m", "k = 1", "sin α = 0,258"],
             jaaprekina=["λ = ?"],
             formulas=["λ = d·sin α/k"],
             aprekins=["1)  d·sin α = 2·10⁻⁶ · 0,258",
                       "2)  = 5,16·10⁻⁷",
                       "3)  λ ≈ 5,2·10⁻⁷ m = 520 nm"],
             atbilde="λ ≈ 520 nm",
             piezime="Zaļā lāzera viļņa garums ir 532 nm - mūsu "
                     "rezultāts tam ir ļoti tuvs."),
        dict(nr=3, virsraksts="Simetriskie maksimumi",
             teksts="Attālums starp pirmās kārtas maksimumiem abās pusēs\n"
                    "ir 0,84 m. Cik liels ir x vienam maksimumam un\n"
                    "kāpēc tā mēra?",
             dots=["Attālums starp maksimumiem 0,84 m"],
             jaaprekina=["x = ?"],
             formulas=["x = attālums/2"],
             aprekins=["1)  x = 0,84 : 2",
                       "2)  x = 0,42 m",
                       "3)  Centra atrašanas kļūda izzūd"],
             atbilde="x = 0,42 m",
             piezime="Mērot no viena maksimuma līdz otram, centra "
                     "noteikšanas kļūda uz rezultātu neietekmē."),
        dict(nr=4, virsraksts="Kļūdas novērtējums",
             teksts="Izmērītais viļņa garums ir 520 nm, patiesais 532 nm.\n"
                    "Aprēķini relatīvo novirzi procentos!",
             dots=["λ(izm.) = 520 nm", "λ(pat.) = 532 nm"],
             jaaprekina=["δ = ?"],
             formulas=["Δλ = λ(pat.) − λ(izm.)", "δ = Δλ/λ"],
             aprekins=["1)  Δλ = 532 − 520 = 12 nm",
                       "2)  δ = 12 : 532 ≈ 0,023",
                       "3)  δ ≈ 2,3 %"],
             atbilde="δ ≈ 2,3 %",
             piezime="Skolas apstākļos līdz 5 % novirze ir labs "
                     "rezultāts."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Viļņa garumu nosaka no izmērītajiem attālumiem x un L.",
            "sin α = x/√(x² + L²); pēc tam λ = d·sin α/k.",
            "Mēra starp simetriskajiem maksimumiem un dala ar 2.",
            "Lāzera starā nekad neskatās.",
        ],
        majasdarbs=[
            "L = 2,00 m, x = 0,55 m. Aprēķini sin α.",
            "d = 2·10⁻⁶ m, sin α = 0,30, k = 1. Aprēķini λ.",
            "Sagatavo LD4 datu tabulu ar četrām rindām.",
        ],
        pasvertejums=["Protu uzzīmēt shēmu",
                      "Protu izteikt sinusu",
                      "Esmu sagatavojis tabulu",
                      "Zinu lāzera drošību"],
        nakama="Nākamā stunda: LD4 - difrakcijas režģa pētīšana "
               "dubultstundā."),
),

dict(
    nr="12.6", virsraksts="Polarizācija un optiskie lietojumi",
    jautajums="Kā darbojas polarizācijas filtrs?",
    apaksraksts="Šķērsvilnis · Polarizācijas filtrs · Brilles un ekrāni",
    merkis="Skaidrot polarizācijas efektu un nosaukt tā lietojumus.",
    protu=["izskaidrot, kas ir polarizēta gaisma;",
           "izskaidrot filtra darbību;",
           "pamatot, kāpēc polarizācija pierāda šķērsviļņa dabu;",
           "nosaukt polarizācijas lietojumus."],
    atkartojums="6. tematā atšķīrām šķērsviļņus un garenviļņus. "
                "Polarizācija ir tieši tā parādība, kas pierāda, ka "
                "gaisma ir šķērsvilnis.",
    uzdevumu_apraksts="Polarizācija un tās lietojumi",
    teorija=[
        ("Polarizēta gaisma", [
            ("panelis", "KAS IR POLARIZĀCIJA",
             ["Parastā gaismā elektriskais lauks svārstās visos "
              "virzienos, kas ir perpendikulāri izplatīšanās virzienam.",
              "Polarizācijas filtrs izlaiž tikai vienā plaknē svārstošos "
              "viļņus - gaisma kļūst polarizēta un tās intensitāte "
              "samazinās apmēram uz pusi.",
              "Divi filtri, pagriezti par 90°, gaismu gandrīz pilnīgi "
              "aptur. Garenviļņiem, piemēram, skaņai, šādas parādības "
              "nav - tāpēc polarizācija pierāda, ka gaisma ir "
              "šķērsvilnis."], NAVY),
            ("divi",
             ("FILTRI PARALĒLI", GREEN,
              ["Ass virzieni sakrīt.",
               "Gaisma iziet cauri.",
               "Ekrāns paliek gaišs."]),
             ("FILTRI KRUSTĀM", RED,
              ["Asis pagrieztas par 90°.",
               "Gaisma neiziet.",
               "Ekrāns kļūst tumšs."])),
        ]),
        ("Kur to izmanto", [
            ("tabula",
             ["Lietojums", "Kā darbojas", "Ieguvums"],
             [["Saulesbrilles", "Aptur atstaroto gaismu",
               "Mazāk apžilbina"],
              ["Fotofiltrs", "Noņem atspīdumus", "Skaidrāks attēls"],
              ["LCD ekrāns", "Divi filtri un kristāli",
               "Vada gaismas plūsmu"],
              ["3D kino", "Katrai acij sava plakne", "Telpisks attēls"]],
             [3.20, 3.60, 3.43]),
            ("panelis", "KĀPĒC ATSTAROTĀ GAISMA IR POLARIZĒTA",
             ["Atstarojoties no ūdens, ceļa vai stikla, gaisma daļēji "
              "polarizējas horizontālā plaknē.",
              "Tāpēc polarizācijas brillēs filtra ass ir vertikāla - tā "
              "aptur tieši šo apžilbinošo atspīdumu.",
              "Paskatoties caur šādām brillēm uz telefona ekrānu un "
              "pagriežot galvu, ekrāns kļūst tumšs - tas ir tiešs "
              "pierādījums."], GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Intensitāte pēc filtra",
             teksts="Uz polarizācijas filtru krīt nepolarizēta gaisma ar\n"
                    "intensitāti 800 vienību. Cik liela tā ir pēc\n"
                    "filtra?",
             dots=["I₀ = 800 vienību", "Nepolarizēta gaisma"],
             jaaprekina=["I = ?"],
             formulas=["Nepolarizētai gaismai: I = I₀/2"],
             aprekins=["1)  Filtrs izlaiž vienu plakni",
                       "2)  I = 800 : 2",
                       "3)  I = 400 vienību"],
             atbilde="I = 400 vienību",
             piezime="Puse enerģijas paliek filtrā - tāpēc caur "
                     "polarizācijas brillēm pasaule izskatās tumšāka."),
        dict(nr=2, virsraksts="Divi filtri",
             teksts="Aiz pirmā filtra ir 400 vienību. Otrs filtrs\n"
                    "pagriezts par 90°. Cik daudz iziet cauri?",
             dots=["I₁ = 400 vienību", "Leņķis 90°"],
             jaaprekina=["I₂ = ?"],
             formulas=["Krustām novietoti filtri gaismu aptur"],
             aprekins=["1)  Pirmais filtrs deva vertikālu plakni",
                       "2)  Otrais izlaiž tikai horizontālo",
                       "3)  I₂ ≈ 0"],
             atbilde="I₂ ≈ 0 - gaisma neiziet",
             piezime="Tieši šo eksperimentu izmanto, lai pierādītu "
                     "gaismas šķērsviļņa dabu."),
        dict(nr=3, virsraksts="Kāpēc skaņu nevar polarizēt",
             teksts="Paskaidro, kāpēc skaņas vilni nevar polarizēt, bet\n"
                    "gaismas vilni var!",
             dots=["Skaņa - garenvilnis",
                   "Gaisma - šķērsvilnis"],
             jaaprekina=["Kāpēc atšķirība?"],
             formulas=["Polarizācija iespējama tikai šķērsviļņiem"],
             aprekins=["1)  Garenvilnī svārstības ir PA izplatīšanās virzienu",
                       "2)  Nav dažādu plakņu, ko atlasīt",
                       "3)  Šķērsvilnim plakņu ir bezgalīgi daudz"],
             atbilde="Polarizēt var tikai šķērsviļņus",
             piezime="Tāpēc polarizācija bija galvenais pierādījums, ka "
                     "gaisma ir šķērsvilnis."),
        dict(nr=4, virsraksts="Brilles uz ūdens",
             teksts="Makšķernieks ar polarizācijas brillēm redz zivis\n"
                    "ūdenī, bet bez tām - tikai atspīdumu.\n"
                    "Paskaidro, kāpēc!",
             dots=["Atstarotā gaisma polarizēta horizontāli",
                   "Filtra ass vertikāla"],
             jaaprekina=["Kāpēc redz labāk?"],
             formulas=["Filtrs aptur vienu plakni"],
             aprekins=["1)  No ūdens atstarotā gaisma ir horizontāli polarizēta",
                       "2)  Vertikālā filtra ass to aptur",
                       "3)  Paliek gaisma no ūdens dziļuma"],
             atbilde="Filtrs aptur atstaroto atspīdumu",
             piezime="Tas pats iemesls, kāpēc autobraucējiem šādas "
                     "brilles palīdz saulainā laikā."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Polarizēta gaisma svārstās vienā plaknē.",
            "Filtrs nepolarizētas gaismas intensitāti samazina uz pusi.",
            "Divi krustām novietoti filtri gaismu aptur.",
            "Polarizācija pierāda, ka gaisma ir šķērsvilnis.",
        ],
        majasdarbs=[
            "I₀ = 600 vienību. Cik būs pēc viena filtra?",
            "Paskaidro, kāpēc skaņu nevar polarizēt.",
            "Nosauc trīs polarizācijas lietojumus sadzīvē.",
        ],
        pasvertejums=["Zinu, kas ir polarizācija",
                      "Zinu filtra darbību",
                      "Protu pamatot šķērsviļņa dabu",
                      "Zinu lietojumus"],
        nakama="Nākamā stunda: datu analīze un nostiprināšana pirms "
               "PD7."),
),

dict(
    nr="12.7", virsraksts="Datu analīze un nostiprināšana",
    jautajums="Vai izmērītais viļņa garums ir ticams?",
    apaksraksts="Mērvienību pārbaude · Novirzes · c = λf un d·sin α = kλ",
    merkis="Pārbaudīt mērvienības, skaidrot novirzes un risināt temata "
           "uzdevumus, pārbaudot kārtas skaitļa vērtības.",
    protu=["pārbaudīt mērvienības aprēķinā;",
           "novērtēt rezultāta ticamību;",
           "izskaidrot novirzes cēloņus;",
           "risināt temata kombinētos uzdevumus."],
    atkartojums="Šī ir temata pēdējā mācību stunda. PD7 prasīs "
                "orientēties spektrā, skaidrot difrakciju un analizēt "
                "režģa datus.",
    uzdevumu_apraksts="Kombinēti uzdevumi pirms PD7",
    teorija=[
        ("Ticamības pārbaude", [
            ("tabula",
             ["Pārbaude", "Kas jāsanāk", "Ja nesanāk"],
             [["Redzamās gaismas λ", "400-700 nm", "Kļūda pakāpēs"],
              ["sin α", "Ne vairāk par 1", "Kārta par lielu"],
              ["Kārta k", "Vesels skaitlis", "Pārrēķini ceļu starpību"],
              ["EM viļņa ātrums", "3·10⁸ m/s vakuumā", "Kļūda vienībās"]],
             [3.20, 3.20, 3.83]),
            ("panelis", "BIEŽĀKIE NOVIRŽU CĒLOŅI",
             ["Neprecīzi izmērīts L vai x - tie ir galvenie kļūdu avoti, "
              "jo abi ietilpst sinusa aprēķinā.",
              "Režģis nav perpendikulārs staram - leņķi izkropļojas.",
              "Maksimuma centrs nolasīts neprecīzi; to novērš, mērot "
              "starp simetriskiem maksimumiem."], RED),
        ]),
        ("PD7 sagatavošanās", [
            ("divi",
             ("KAS BŪS PD7", BLUE,
              ["Spektra daļu sakārtošana.",
               "Difrakcijas skaidrojums.",
               "Aprēķins ar c = λf.",
               "Aprēķins ar režģa formulu.",
               "Datu ticamības vērtējums."]),
             ("FORMULAS", GREEN,
              ["c = λf;  λ = c/f",
               "d = 1/N",
               "d·sin α = kλ",
               "sin α = x/√(x² + L²)",
               "c = 3·10⁸ m/s"])),
            ("panelis", "PĒDĒJAIS PADOMS",
             ["Pakāpes rakstiet uzreiz zinātniskajā pierakstā: 500 nm ir "
              "5·10⁻⁷ m, nevis 500·10⁻⁹ m aprēķinā.",
              "Pēc katra aprēķina pajautā: vai skaitlis ir tajā mērogā, "
              "ko gaidīju?",
              "Skaidrojuma uzdevumos lieto terminus: superpozīcija, ceļu "
              "starpība, maksimums, difrakcija."], GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Vai rezultāts ticams",
             teksts="Skolēns aprēķināja gaismas viļņa garumu un ieguva\n"
                    "λ = 5·10⁻⁴ m. Vai tas ir ticams redzamajai gaismai?\n"
                    "Kur varētu būt kļūda?",
             dots=["λ(izm.) = 5·10⁻⁴ m",
                   "Redzamā gaisma: 4-7·10⁻⁷ m"],
             jaaprekina=["Vai ticams?"],
             formulas=["Redzamā gaisma 400-700 nm"],
             aprekins=["1)  5·10⁻⁴ m = 500 µm",
                       "2)  Tas ir 1000 reižu par lielu",
                       "3)  Visticamāk, d ņemts milimetros, nevis metros"],
             atbilde="Nav ticams - kļūda mērvienībās",
             piezime="Tūkstoškārtīga kļūda gandrīz vienmēr nozīmē "
                     "milimetrus, kas nav pārrēķināti metros."),
        dict(nr=2, virsraksts="Radio un gaisma",
             teksts="Salīdzini radioviļņa (f = 100 MHz) un zaļās gaismas\n"
                    "(λ = 500 nm) viļņa garumus. Cik reižu tie atšķiras?",
             dots=["f₁ = 1,0·10⁸ Hz", "λ₂ = 5·10⁻⁷ m",
                   "c = 3·10⁸ m/s"],
             jaaprekina=["λ₁ = ?", "Attiecība = ?"],
             formulas=["λ = c/f"],
             aprekins=["1)  λ₁ = 3·10⁸ : 1,0·10⁸ = 3,0 m",
                       "2)  3,0 : 5·10⁻⁷ = 6·10⁶",
                       "3)  Atšķiras 6 miljonus reižu"],
             atbilde="λ₁ = 3,0 m;  atšķirība ≈ 6·10⁶ reižu",
             piezime="Viens un tas pats viļņu veids - bet mērogi "
                     "pilnīgi atšķirīgi."),
        dict(nr=3, virsraksts="Kārtas pārbaude",
             teksts="Režģim d = 1,5·10⁻⁶ m, gaisma λ = 600 nm.\n"
                    "Vai var novērot trešās kārtas maksimumu?",
             dots=["d = 1,5·10⁻⁶ m", "λ = 6·10⁻⁷ m", "k = 3"],
             jaaprekina=["sin α = ?"],
             formulas=["sin α = kλ/d", "sin α ≤ 1"],
             aprekins=["1)  kλ = 3 · 6·10⁻⁷ = 1,8·10⁻⁶",
                       "2)  sin α = 1,8·10⁻⁶ : 1,5·10⁻⁶ = 1,2",
                       "3)  1,2 > 1 - tāda maksimuma nav"],
             atbilde="Nē, trešā kārta nav iespējama",
             piezime="Sinuss virs viena vienmēr nozīmē, ka šī kārta "
                     "vienkārši neeksistē."),
        dict(nr=4, virsraksts="No mērījumiem uz λ",
             teksts="LD4 dati: d = 2·10⁻⁶ m, k = 2, x = 0,90 m,\n"
                    "L = 1,50 m. Aprēķini viļņa garumu!",
             dots=["d = 2·10⁻⁶ m", "k = 2", "x = 0,90 m", "L = 1,50 m"],
             jaaprekina=["λ = ?"],
             formulas=["sin α = x/√(x² + L²)", "λ = d·sin α/k"],
             aprekins=["1)  x² + L² = 0,81 + 2,25 = 3,06;  √3,06 ≈ 1,75",
                       "2)  sin α = 0,90 : 1,75 ≈ 0,514",
                       "3)  λ = 2·10⁻⁶ · 0,514 : 2 ≈ 5,1·10⁻⁷ m"],
             atbilde="λ ≈ 514 nm",
             piezime="Rezultāts ir redzamās gaismas diapazonā - ticams."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Redzamās gaismas viļņa garums ir 400-700 nm.",
            "sin α nekad nepārsniedz 1 - tā ir kārtas pārbaude.",
            "Mērvienību kļūda ir biežākais neticamu rezultātu cēlonis.",
            "Novirzes rada neprecīzi izmērīti attālumi un režģa "
            "novietojums.",
        ],
        majasdarbs=[
            "Atkārto 12.1.-12.6. stundas kopsavilkumus.",
            "d = 2·10⁻⁶ m, k = 1, x = 0,50 m, L = 1,80 m. Aprēķini λ.",
            "Sagatavo formulu lapu PD7.",
        ],
        pasvertejums=["Protu pārbaudīt mērvienības",
                      "Protu novērtēt ticamību",
                      "Zinu noviržu cēloņus",
                      "Esmu gatavs PD7"],
        nakama="Nākamā stunda: PD7 - elektromagnētiskie viļņi un "
               "difrakcija."),
),

]
