# -*- coding: utf-8 -*-
"""Fizika I, 10. klase. LD4 - Mehāniskās enerģijas nezūdamības pārbaude."""

LD = {
    "nr": 4,
    "klase": "10. klase",
    "nosaukums": "Mehāniskās enerģijas nezūdamības pārbaude",
    "mape": "5. Enerģija un darbs",
    "fails": "LD4. Mehāniskās enerģijas nezūdamības pārbaude_tt",
    "datums": "05.05.2027.",
    "svars": 9,
    "laiks": 80,
    "kopa": 20,
    "jautajums": "Cik liela daļa potenciālās enerģijas pārvēršas "
                 "kinētiskajā enerģijā, lodītei noripojot pa slīpu renīti?",
    "merkis": "Salīdzināt ķermeņa potenciālo enerģiju sākumā ar kinētisko "
              "enerģiju beigās un novērtēt, cik liela daļa enerģijas "
              "zaudēta berzē.",
    "hipoteze": "Pieraksti, vai Ek beigās būs vienāda ar Ep sākumā, un "
                "paskaidro, kāpēc.",
    "teorija": [
        "Potenciālā enerģija:  Ep = mgh   ·   Kinētiskā enerģija:  "
        "Ek = ½mv²",
        "Enerģijas nezūdamība bez berzes:  Ep = Ek   ·   ar berzi:  "
        "Ep = Ek + Q",
        "Horizontālas izlidošanas ātrums:  v = s · √(g / (2H)),  kur H - "
        "galda augstums, s - lidojuma attālums.",
        "Enerģijas saglabāšanās daļa:  η = Ek / Ep · 100 %",
    ],
    "piederumi": [
        "Renīte ar atzīmētu starta punktu, metāla lodīte, statīvs vai "
        "grāmatas augstuma iestatīšanai.",
        "Mērlente, lineāls, svari (0,1 g), kopējamais papīrs un balta "
        "lapa lodītes nokrišanas vietas atzīmēšanai.",
    ],
    "drosiba": [
        "Lodīte izlido no galda - grīdas zonā priekšā nedrīkst atrasties "
        "cilvēki vai priekšmeti.",
        "Lodītes lidojuma zonā nestāv; pēc katra mēģinājuma lodīti savāc.",
        "Renīti un statīvu nostiprina, lai tie nenokristu no galda.",
    ],
    "gaita": [
        ("Izmēri lodīti.", "Ar svariem nosaki lodītes masu m un ieraksti "
         "to protokolā."),
        ("Sagatavo renīti.", "Nostiprini renīti uz galda tā, lai lodīte "
         "no tās izlido horizontāli tieši pie galda malas."),
        ("Izmēri augstumus.", "Izmēri lodītes krišanas augstumu h uz renītes "
         "(no starta punkta līdz renītes izejai) un galda augstumu H no "
         "izejas punkta līdz grīdai."),
        ("Sagatavo nokrišanas vietu.", "Uz grīdas noliec baltu lapu un virsū "
         "kopējamo papīru, lai lodīte atstātu atzīmi."),
        ("Palaid lodīti.", "Palaid lodīti no starta punkta bez grūdiena. "
         "Izmēri horizontālo attālumu s no galda malas līdz atzīmei."),
        ("Atkārto.", "Katram augstumam h veic 3 palaišanas un ieraksti visus "
         "trīs attālumus; aprēķini vidējo."),
        ("Maini augstumu.", "Atkārto mērījumus trim dažādiem augstumiem h "
         "(piemēram, 10 cm, 20 cm un 30 cm)."),
    ],
    "tabula": {
        "galva": ["Nr.", "h, m", "s₁, m", "s₂, m", "s₃, m", "s(vid), m",
                  "v, m/s", "Ep, J", "Ek, J"],
        "rindas": 3,
        "platumi": [1.1, 1.9, 1.9, 1.9, 1.9, 2.4, 2.3, 2.3, 2.3],
    },
    "apstrade": [
        ("Ātruma aprēķins", "Vienai izvēlētai rindai pieraksti pilnu "
         "risinājumu ātrumam v = s · √(g / (2H)). Vispirms pieraksti H!",
         5.0),
        ("Enerģiju aprēķins", "Tai pašai rindai aprēķini Ep = mgh un "
         "Ek = ½mv².", 5.0),
        ("Enerģijas saglabāšanās daļa", "Aprēķini η = Ek / Ep · 100 % visām "
         "trim rindām un salīdzini rezultātus.", 4.5),
    ],
    "jautajumi": [
        ("Cik liela enerģijas daļa saglabājās? Vai Ek ir mazāka vai lielāka "
         "par Ep un kāpēc?", 2.4),
        ("Kur nonāca trūkstošā enerģija? Nosauc vismaz divus enerģijas "
         "zuduma ceļus!", 2.2),
        ("Vai η ir vienāds visiem trim augstumiem? Ko tas liecina?", 2.2),
        ("Nosauc divus kļūdu avotus un piedāvā, kā tos samazināt!", 2.4),
        ("Vai iegūtais rezultāts ir pretrunā ar enerģijas nezūdamības "
         "likumu? Atbildi pamato!", 2.2),
    ],
    "sagatavosana": [
        "Katrai grupai: renīte, lodīte, mērlente, kopējamais papīrs, balta "
        "lapa, līmlente. Svarus var izmantot kopīgi.",
        "Pirms darba kopā izvedina formulu v = s√(g/(2H)) no horizontālas "
        "mešanas: H = ½gt² un s = vt.",
        "Uzsvērt, ka lodītei jāizlido horizontāli - renītes gala posmam "
        "jābūt horizontālam.",
    ],
    "gaidamie": [
        "Tipiski η iznāk 60-85 %: daļa enerģijas paliek lodītes rotācijā un "
        "zūd berzē.",
        "Ar h = 0,20 m un H = 0,90 m attālums s parasti ir 0,55-0,70 m, "
        "ātrums 1,3-1,6 m/s.",
        "η parasti ir līdzīgs visiem augstumiem - tas liecina, ka zudumi ir "
        "proporcionāli sākuma enerģijai.",
        "Ja η > 100 %, kļūdaini izmērīts h vai H; ja η < 40 %, lodīte "
        "neizlido horizontāli.",
    ],
    "atbildes": [
        "Ek ir mazāka par Ep (parasti 60-85 %), jo daļa enerģijas pārvēršas "
        "rotācijas enerģijā un siltumā berzes dēļ.",
        "Berze starp lodīti un renīti, gaisa pretestība un lodītes "
        "griešanās (rotācijas kinētiskā enerģija, kas netiek ieskaitīta).",
        "η ir aptuveni vienāds - zudumi aug proporcionāli sākuma enerģijai, "
        "jo berzes ceļš un apstākļi ir līdzīgi.",
        "Piemēram: neprecīzi noteikta nokrišanas vieta (samazina, veicot "
        "vairāk palaišanu un ņemot vidējo) un renītes gala neprecīzs "
        "horizontālums (samazina, pārbaudot ar līmeņrādi).",
        "Nē. Enerģija nepazūd - tā pāriet citos veidos (siltumā, rotācijā). "
        "Nezūdamības likums attiecas uz visu enerģiju, ne tikai uz "
        "mehānisko translācijas enerģiju.",
    ],
    "kriteriji": [
        ("Formulēta hipotēze ar pamatojumu", 2),
        ("Pareizi izmērīta masa, augstumi h un H", 3),
        ("Katram augstumam trīs palaišanas, dati tabulā ar mērvienībām", 3),
        ("Pareizi aprēķināti ātrumi ar pilnu risinājuma pierakstu", 3),
        ("Pareizi aprēķinātas Ep un Ek vērtības", 3),
        ("Aprēķināts η visām trim rindām", 2),
        ("Pamatots, kur nonāk trūkstošā enerģija", 2),
        ("Izskaidrots, kāpēc rezultāts nav pretrunā ar nezūdamības likumu",
         1),
        ("Protokols noformēts kārtīgi un iesniegts termiņā", 1),
    ],
    "piezimes": [
        "Darbs ir pēdējais 10. klases laboratorijas darbs un tieši gatavo "
        "PD6; enerģijas bilances pieraksts Ep = Ek + Q ir eksāmena "
        "tipveida solis.",
        "Ja nav svaru, masu var ņemt no lodītes marķējuma - tad protokolā "
        "jānorāda, ka masa nav mērīta, bet dota.",
    ],
}
