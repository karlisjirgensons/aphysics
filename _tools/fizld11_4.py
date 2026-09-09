# -*- coding: utf-8 -*-
"""Fizika I, 11. klase. LD4 - Difrakcijas režģa pētīšana."""

LD = {
    "nr": 4,
    "klase": "11. klase",
    "nosaukums": "Difrakcijas režģa pētīšana",
    "mape": "12. Elektromagnētiskie viļņi",
    "fails": "LD4. Difrakcijas režģa pētīšana_tt",
    "datums": "10.03.2027.",
    "svars": 7,
    "laiks": 80,
    "kopa": 20,
    "jautajums": "Cik liels ir lāzera gaismas viļņa garums un cik precīzi "
                 "to var noteikt ar difrakcijas režģi?",
    "merkis": "Ar difrakcijas režģi izmērīt maksimumu novietojumu, aprēķināt "
              "gaismas viļņa garumu un novērtēt mērījuma kļūdu.",
    "hipoteze": "Pieraksti, kādu viļņa garumu sagaidi izmantotajai lāzera "
                "krāsai un kādās robežās, tavuprāt, būs novirze.",
    "teorija": [
        "Difrakcijas režģis:  d · sin α = kλ   ⟹   λ = d · sin α / k",
        "Režģa periods:  d = 1 / N,  kur N - svītru skaits uz garuma "
        "vienību.",
        "Ja L - attālums līdz ekrānam un y - attālums no centra līdz "
        "k-tajam maksimumam, tad  tg α = y / L.",
        "Redzamās gaismas viļņu garumi:  sarkana 620-750 nm, zaļa "
        "495-570 nm, zila 450-495 nm.",
    ],
    "piederumi": [
        "Lāzera rādītājs (sarkans un, ja pieejams, zaļš), difrakcijas režģis "
        "ar zināmu svītru skaitu (100, 300 vai 600 svītras uz mm).",
        "Statīvs lāzera un režģa nostiprināšanai, ekrāns vai balta siena, "
        "mērlente (1 mm), lineāls.",
        "Tumšs aizkars vai iespēja aptumšot telpu.",
    ],
    "drosiba": [
        "NEKAD neskaties lāzera starā un nevērs to uz citiem cilvēkiem - "
        "tīklenes bojājums rodas ātrāk, nekā paspēj samirkšķināt acis.",
        "Lāzeru nostiprina statīvā un vērš uz ekrānu; stars nedrīkst iet "
        "acu augstumā.",
        "No darba zonas noņem spīdīgas virsmas (spoguļi, pulksteņi, "
        "telefonu ekrāni) - tās var atstarot staru.",
        "Lāzeru ieslēdz tikai mērījuma laikā; pēc darba nodod skolotājam.",
    ],
    "gaita": [
        ("Sagatavo iekārtu.", "Nostiprini lāzeru statīvā un vērs to "
         "perpendikulāri ekrānam. Pieraksti režģa svītru skaitu N."),
        ("Novieto režģi.", "Novieto režģi lāzera priekšā perpendikulāri "
         "staram, tuvu lāzera izejai."),
        ("Izmēri attālumu.", "Izmēri attālumu L no režģa līdz ekrānam. "
         "Izvēlies L tā, lai uz ekrāna būtu redzami vismaz pirmās un otrās "
         "kārtas maksimumi."),
        ("Atzīmē maksimumus.", "Uz ekrāna atzīmē centrālo maksimumu un "
         "pirmās un otrās kārtas maksimumus abās pusēs."),
        ("Mēri simetriski.", "Katrai kārtai izmēri attālumu 2y starp abiem "
         "simetriskajiem maksimumiem un dali uz pusēm - tā samazina "
         "centra noteikšanas kļūdu."),
        ("Atkārto.", "Atkārto mērījumus vismaz diviem dažādiem attālumiem "
         "L, lai pārbaudītu rezultāta noturību."),
        ("Aprēķini.", "Katrai rindai aprēķini tg α, sin α un λ."),
    ],
    "tabula": {
        "galva": ["Nr.", "L, m", "k", "2y, m", "y, m", "tg α", "sin α",
                  "λ, nm"],
        "rindas": 4,
        "platumi": [1.2, 2.2, 1.4, 2.4, 2.2, 2.4, 2.4, 3.0],
    },
    "apstrade": [
        ("Režģa perioda aprēķins", "Aprēķini režģa periodu d = 1 / N! "
         "Uzmanīgi ar mērvienībām: svītras uz mm jāpārveido uz m⁻¹.", 4.0),
        ("Viļņa garuma aprēķins", "Vienai izvēlētai rindai pieraksti pilnu "
         "risinājumu:  tg α = y / L,  sin α no tg α,  λ = d sin α / k.",
         6.5),
        ("Vidējā vērtība un novirze", "Aprēķini visu rindu λ vidējo "
         "aritmētisko un relatīvo novirzi no lāzera pasē norādītā viļņa "
         "garuma.", 4.5),
    ],
    "jautajumi": [
        ("Kādu viļņa garumu ieguvi? Salīdzini to ar lāzera marķējumā "
         "norādīto vērtību un aprēķini novirzi procentos!", 2.4),
        ("Vai λ, kas aprēķināts no pirmās un otrās kārtas maksimuma, ir "
         "vienāds? Ko tas liecina?", 2.4),
        ("Kāpēc mēra attālumu starp abiem simetriskajiem maksimumiem, nevis "
         "no centra līdz vienam?", 2.2),
        ("Kā mainītos difrakcijas aina, ja izmantotu režģi ar lielāku "
         "svītru skaitu uz mm? Pamato ar formulu!", 2.2),
        ("Nosauc divus kļūdu avotus un piedāvā, kā tos samazināt!", 2.4),
    ],
    "sagatavosana": [
        "Vismaz 4-5 darba vietas: lāzers statīvā, režģis, ekrāns, mērlente. "
        "Telpu aptumšot.",
        "Pirms darba obligāti pārrunāt lāzera drošību; lāzerus izdala tikai "
        "pēc tam un savāc uzreiz pēc mērījumiem.",
        "Atgādināt, ka sin α jāaprēķina no tg α (vai no y un √(y² + L²)), "
        "nevis jāpieņem sin α ≈ tg α, ja leņķis ir liels.",
        "Ja režģa svītru skaits nav zināms, to var noteikt ar zināma viļņa "
        "garuma lāzeru - tad darbs kļūst par apgriezto uzdevumu.",
    ],
    "gaidamie": [
        "Sarkanam lāzeram (650 nm) ar 300 svītru/mm režģi un L = 1,5 m "
        "pirmās kārtas maksimums ir aptuveni y = 0,32 m.",
        "Iegūtais λ parasti ir 600-700 nm; novirze no marķējuma 3-10 %.",
        "λ vērtībām no dažādām kārtām jāsakrīt dažu procentu robežās - tas "
        "apstiprina formulas pareizību.",
        "Ja λ sistemātiski iznāk par lielu, visbiežāk L izmērīts no lāzera, "
        "nevis no režģa.",
    ],
    "atbildes": [
        "Atbilde individuāla; jāvērtē korekts salīdzinājums un pareizi "
        "aprēķināta relatīvā novirze.",
        "Vērtībām jābūt tuvām. Sakritība liecina, ka formula d sin α = kλ "
        "apraksta parādību pareizi un kārtas skaitlis noteikts pareizi.",
        "Centrālā maksimuma precīzs centrs ir grūti nosakāms; mērot 2y un "
        "dalot uz pusēm, centra kļūda izkrīt no rezultāta.",
        "d = 1/N kļūtu mazāks, tāpēc sin α = kλ/d - lielāks: maksimumi "
        "attālinātos viens no otra un daļa augstāko kārtu vairs nebūtu "
        "redzama.",
        "Piemēram: neprecīzi izmērīts L (samazina, mērot no režģa "
        "plaknes un atkārtojot mērījumu) un izplūduši maksimumi (samazina, "
        "aptumšojot telpu un palielinot L).",
    ],
    "kriteriji": [
        ("Formulēta hipotēze ar skaitlisku prognozi", 2),
        ("Ievēroti lāzera drošības noteikumi visā darba laikā", 2),
        ("Pareizi aprēķināts režģa periods d ar mērvienību pārveidojumu", 2),
        ("Izmērīti L un maksimumu attālumi vismaz 4 rindām", 3),
        ("Mērījumi veikti simetriski (2y) un pierakstīti tabulā", 2),
        ("Pareizi aprēķināti tg α un sin α", 2),
        ("Pareizi aprēķināts λ ar pilnu risinājuma pierakstu", 3),
        ("Aprēķināta vidējā vērtība un relatīvā novirze", 2),
        ("Nosaukti divi kļūdu avoti ar konkrētiem uzlabojumiem", 1),
        ("Protokols noformēts kārtīgi un iesniegts termiņā", 1),
    ],
    "piezimes": [
        "Ja pieejami divu krāsu lāzeri, grupas var salīdzināt sarkano un "
        "zaļo - labi redzams, ka lielākam λ atbilst lielāks novirzes "
        "leņķis.",
        "Alternatīva bez lāzera: CD vai DVD disks kā atstarojošs režģis "
        "(d = 1,6 µm vai 0,74 µm) ar spuldzi - der demonstrējumam, bet "
        "precizitāte ir zemāka.",
    ],
}
