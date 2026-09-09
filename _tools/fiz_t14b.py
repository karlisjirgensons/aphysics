# -*- coding: utf-8 -*-
"""14. temats. B daļa: 14.5.-14.8. stunda."""

from fiz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN     # noqa: F401
from fiz_t14a import TEMATS, KICKER, KURSS, MAPE              # noqa: F401

STUNDAS = [

dict(
    nr="14.5", virsraksts="Dalīšanās un sintēze",
    jautajums="Kā iegūst kodolenerģiju un kā spīd Saule?",
    apaksraksts="E = mc² · Dalīšanās reaktorā · Sintēze zvaigznēs",
    merkis="Skaidrot kodolu dalīšanās un sintēzes atšķirību un salīdzināt "
           "ieguvumus, riskus un enerģijas izcelsmi.",
    protu=["izskaidrot kodolu dalīšanos;",
           "izskaidrot kodolu sintēzi;",
           "lietot E = mc² vienkāršā aprēķinā;",
           "salīdzināt abu procesu ieguvumus un riskus."],
    atkartojums="Iepriekšējā stundā kodoli sabruka paši. Šodien "
                "redzēsim divus procesus, kuros kodoli mainās, "
                "atbrīvojot milzīgu enerģiju.",
    uzdevumu_apraksts="Kodolenerģijas aprēķini",
    teorija=[
        ("Divi kodolprocesi", [
            ("formula", "MASAS UN ENERĢIJAS SAISTĪBA",
             "E = mc²        c = 3,0·10⁸ m/s",
             "Kodolreakcijās produktu masa ir mazāk nekā izejvielu; šī "
             "masas starpība pārvēršas enerģijā. Tā kā c² ir milzīgs "
             "skaitlis, jau niecīga masa dod ļoti daudz enerģijas.",
             GOLD),
            ("divi",
             ("DALĪŠANĀS", RED,
              ["Smags kodols sadalās",
               "divos vieglākos.",
               "Ierosina neitrons.",
               "Notiek reaktorā.",
               "Rodas radioaktīvi",
               "atkritumi."]),
             ("SINTĒZE", GOLD,
              ["Divi viegli kodoli",
               "saplūst vienā.",
               "Vajag ļoti augstu T.",
               "Notiek zvaigznēs.",
               "Atkritumu praktiski",
               "nav."])),
        ]),
        ("Ieguvumi un riski", [
            ("tabula",
             ["Enerģijas avots", "Ieguvums", "Risks vai problēma"],
             [["Kodolreaktors", "Daudz enerģijas, bez CO₂",
               "Atkritumi, avāriju sekas"],
              ["Ogles un gāze", "Vienkārša tehnoloģija",
               "CO₂ un gaisa piesārņojums"],
              ["Sintēze (nākotnē)", "Degviela no ūdens",
               "Tehnoloģija vēl netiek izmantota"],
              ["Saules un vēja", "Atjaunojami", "Atkarīgi no laika apstākļiem"]],
             [3.20, 3.60, 3.43]),
            ("panelis", "KĀPĒC SAULE SPĪD",
             ["Saules kodolā ūdeņraža kodoli saplūst hēlijā; katrā "
              "sekundē apmēram 4 miljoni tonnu masas pārvēršas enerģijā.",
              "Šis process notiek jau 4,6 miljardus gadu un turpināsies "
              "vēl aptuveni tikpat ilgi.",
              "Uz Zemes sintēzi tehnoloģiski īstenot ir grūti, jo "
              "vajadzīga miljonu grādu temperatūra un plazmas "
              "noturēšana."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Enerģija no masas",
             teksts="Kodolreakcijā pazūd 1,0·10⁻³ kg masas.\n"
                    "Cik enerģijas atbrīvojas? (c = 3,0·10⁸ m/s)",
             dots=["m = 1,0·10⁻³ kg", "c = 3,0·10⁸ m/s"],
             jaaprekina=["E = ?"],
             formulas=["E = mc²"],
             aprekins=["1)  c² = 9,0·10¹⁶",
                       "2)  E = 1,0·10⁻³ · 9,0·10¹⁶",
                       "3)  E = 9,0·10¹³ J"],
             atbilde="E = 9,0·10¹³ J",
             piezime="Viens grams masas dod tikpat daudz enerģijas, cik "
                     "sadedzinot vairākus tūkstošus tonnu ogļu."),
        dict(nr=2, virsraksts="Cik masas pazūd",
             teksts="Reaktors gada laikā saražo 3,0·10¹⁶ J enerģijas.\n"
                    "Cik masas tam atbilst? (c = 3,0·10⁸ m/s)",
             dots=["E = 3,0·10¹⁶ J", "c = 3,0·10⁸ m/s"],
             jaaprekina=["m = ?"],
             formulas=["E = mc²", "m = E/c²"],
             aprekins=["1)  c² = 9,0·10¹⁶",
                       "2)  m = 3,0·10¹⁶ : 9,0·10¹⁶",
                       "3)  m ≈ 0,33 kg"],
             atbilde="m ≈ 0,33 kg",
             piezime="Trešdaļa kilograma masas gadā - tā ir milzīga "
                     "enerģija no niecīga daudzuma."),
        dict(nr=3, virsraksts="Saules zudums sekundē",
             teksts="Saule sekundē izstaro 3,8·10²⁶ J enerģijas.\n"
                    "Cik masas tā zaudē sekundē? (c = 3,0·10⁸ m/s)",
             dots=["E = 3,8·10²⁶ J", "c = 3,0·10⁸ m/s"],
             jaaprekina=["m = ?"],
             formulas=["m = E/c²"],
             aprekins=["1)  c² = 9,0·10¹⁶",
                       "2)  m = 3,8·10²⁶ : 9,0·10¹⁶",
                       "3)  m ≈ 4,2·10⁹ kg"],
             atbilde="m ≈ 4,2·10⁹ kg sekundē",
             piezime="Četri miljoni tonnu sekundē - un tomēr tā ir "
                     "niecīga daļa no Saules masas."),
        dict(nr=4, virsraksts="Dalīšanās vai sintēze",
             teksts="Nosaki procesu: a) urāna kodols sadalās, saņemot\n"
                    "neitronu; b) ūdeņraža kodoli saplūst hēlijā;\n"
                    "c) process Saules kodolā.",
             dots=["a) urāns un neitrons", "b) ūdeņradis → hēlijs",
                   "c) Saules kodols"],
             jaaprekina=["Kurš process?"],
             formulas=["Dalīšanās - smags kodols sadalās",
                       "Sintēze - vieglie saplūst"],
             aprekins=["1)  a) dalīšanās",
                       "2)  b) sintēze",
                       "3)  c) sintēze"],
             atbilde="a) dalīšanās; b) un c) sintēze",
             piezime="Reaktoros pagaidām izmanto tikai dalīšanos; "
                     "sintēze joprojām ir pētniecības stadijā."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Dalīšanās: smags kodols sadalās; sintēze: vieglie saplūst.",
            "E = mc²; niecīga masa dod milzīgu enerģiju.",
            "Reaktoros notiek dalīšanās, zvaigznēs - sintēze.",
            "Katram enerģijas avotam ir gan ieguvumi, gan riski.",
        ],
        majasdarbs=[
            "m = 2,0·10⁻³ kg. Aprēķini E.",
            "E = 9,0·10¹⁴ J. Aprēķini masas zudumu.",
            "Salīdzini dalīšanos un sintēzi - divas atšķirības.",
        ],
        pasvertejums=["Zinu, kas ir dalīšanās",
                      "Zinu, kas ir sintēze",
                      "Protu lietot E = mc²",
                      "Protu salīdzināt riskus"],
        nakama="Nākamā stunda: starojuma lietojumi un drošība."),
),

dict(
    nr="14.6", virsraksts="Starojuma lietojumi un drošība",
    jautajums="Kā izvērtēt apgalvojumu par starojuma risku?",
    apaksraksts="Apstarošana un piesārņojums · Laiks, attālums, ekranēšana",
    merkis="Nošķirt apstarošanu no radioaktīva piesārņojuma un pamatot "
           "aizsardzību ar laiku, attālumu un ekranēšanu.",
    protu=["atšķirt apstarošanu no piesārņojuma;",
           "nosaukt trīs aizsardzības principus;",
           "salīdzināt starojuma devas;",
           "izvērtēt apgalvojumu par risku."],
    atkartojums="14.4. stundā apguvām starojuma veidus. Šodien "
                "noskaidrosim, kā ar tiem rīkoties droši un kā vērtēt "
                "to, ko par starojumu raksta.",
    uzdevumu_apraksts="Devas un aizsardzība",
    teorija=[
        ("Divi dažādi jēdzieni", [
            ("divi",
             ("APSTAROŠANA", BLUE,
              ["Starojums iet cauri",
               "ķermenim.",
               "Pēc tam cilvēks NAV",
               "radioaktīvs.",
               "Piemērs: rentgens,",
               "staru terapija."]),
             ("PIESĀRŅOJUMS", RED,
              ["Radioaktīva viela nokļūst",
               "uz ādas vai organismā.",
               "Tā turpina starot.",
               "Vajag mazgāšanu un",
               "medicīnisku palīdzību.",
               "Piemērs: radioaktīvi putekļi."])),
            ("panelis", "TRĪS AIZSARDZĪBAS PRINCIPI",
             ["LAIKS: jo īsāku laiku atrodas starojuma tuvumā, jo mazāka "
              "deva.",
              "ATTĀLUMS: deva samazinās kā attāluma kvadrāts - divreiz "
              "tālāk nozīmē četrreiz mazāk.",
              "EKRANĒŠANA: alfa aptur papīrs, beta - alumīnijs, gamma - "
              "svins vai betons."], NAVY),
        ]),
        ("Devas un lietojumi", [
            ("tabula",
             ["Situācija", "Aptuvenā deva", "Piezīme"],
             [["Dabiskais fons gadā", "2-3 mSv", "Nenovēršams"],
              ["Krūškurvja rentgens", "0,1 mSv", "Vienreizējs"],
              ["Datortomogrāfija", "5-10 mSv", "Tikai pēc indikācijām"],
              ["Robeža darbiniekiem", "20 mSv gadā", "Stingri kontrolē"]],
             [3.60, 2.80, 3.63]),
            ("panelis", "KUR STAROJUMU IZMANTO",
             ["Medicīnā: diagnostikā (rentgens, izotopu izmeklējumi) un "
              "audzēju ārstēšanā.",
              "Rūpniecībā: metināto šuvju pārbaudei un materiālu biezuma "
              "kontrolei.",
              "Zinātnē: atradumu datēšanai ar oglekli-14 un iežu vecuma "
              "noteikšanai."], GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Attālums un deva",
             teksts="1,0 m attālumā no avota deva ir 80 µSv stundā.\n"
                    "Cik tā būs 2,0 m attālumā?",
             dots=["D₁ = 80 µSv/h", "r₁ = 1,0 m", "r₂ = 2,0 m"],
             jaaprekina=["D₂ = ?"],
             formulas=["D ~ 1/r²", "D₂ = D₁/4"],
             aprekins=["1)  Attālums pieaudzis 2 reizes",
                       "2)  Deva samazinās 4 reizes",
                       "3)  D₂ = 80 : 4 = 20 µSv stundā"],
             atbilde="D₂ = 20 µSv stundā",
             piezime="Attālums ir vienkāršākais un efektīvākais "
                     "aizsardzības līdzeklis."),
        dict(nr=2, virsraksts="Laiks un deva",
             teksts="Deva ir 20 µSv stundā. Cik lielu devu darbinieks\n"
                    "saņem 15 minūtēs?",
             dots=["Jauda 20 µSv/h", "t = 15 min = 0,25 h"],
             jaaprekina=["D = ?"],
             formulas=["D = jauda · t"],
             aprekins=["1)  D = 20 · 0,25",
                       "2)  D = 5,0 µSv"],
             atbilde="D = 5,0 µSv",
             piezime="Salīdzinājumam: krūškurvja rentgens dod apmēram "
                     "100 µSv."),
        dict(nr=3, virsraksts="Salīdzini ar fonu",
             teksts="Dabiskais fons gadā ir 2,5 mSv. Cik procentu no tā\n"
                    "ir viens krūškurvja rentgens (0,10 mSv)?",
             dots=["Fons = 2,5 mSv gadā", "Rentgens = 0,10 mSv"],
             jaaprekina=["Daļa = ?"],
             formulas=["Daļa = D/D(fons)"],
             aprekins=["1)  0,10 : 2,5 = 0,04",
                       "2)  Daļa = 4 %",
                       "3)  Tas atbilst apmēram 15 dienu fonam"],
             atbilde="4 % no gada fona",
             piezime="Salīdzinājums ar fonu ir labākais veids, kā "
                     "saprast, vai deva ir liela."),
        dict(nr=4, virsraksts="Izvērtē apgalvojumu",
             teksts="Ziņā rakstīts: «Pēc rentgena cilvēks kļūst\n"
                    "radioaktīvs un ir bīstams citiem.»\n"
                    "Izvērtē apgalvojumu!",
             dots=["Rentgens - apstarošana",
                   "Radioaktīva viela organismā nenokļūst"],
             jaaprekina=["Vai pamatots?"],
             formulas=["Apstarošana ≠ piesārņojums"],
             aprekins=["1)  Rentgena starojums iet cauri un pazūd",
                       "2)  Radioaktīva viela ķermenī nepaliek",
                       "3)  Cilvēks nekļūst radioaktīvs"],
             atbilde="Apgalvojums nav pamatots",
             piezime="Izotopu izmeklējumos gan pacients īslaicīgi ir "
                     "starojuma avots - tur nosacījumi ir citi."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Apstarošana beidzas līdz ar starojumu; piesārņojums "
            "turpinās.",
            "Aizsardzība: laiks, attālums, ekranēšana.",
            "Deva samazinās kā attāluma kvadrāts.",
            "Devu vienmēr salīdzina ar dabisko fonu.",
        ],
        majasdarbs=[
            "D₁ = 120 µSv/h pie 1,0 m. Cik būs pie 3,0 m?",
            "Jauda 40 µSv/h, t = 30 min. Aprēķini devu.",
            "Atrodi ziņu par starojumu un izvērtē tās pamatojumu.",
        ],
        pasvertejums=["Atšķiru apstarošanu no piesārņojuma",
                      "Zinu trīs aizsardzības principus",
                      "Protu rēķināt devas",
                      "Protu izvērtēt apgalvojumu"],
        nakama="Nākamā stunda: Saules sistēma un novērojumi."),
),

dict(
    nr="14.7", virsraksts="Saules sistēma un novērojumi",
    jautajums="Ko varam novērot un ko secinām netieši?",
    apaksraksts="Saules sistēmas uzbūve · Tiešs novērojums · Secinājums "
                "no modeļa",
    merkis="Orientēties Saules sistēmā un atšķirt tiešu novērojumu no "
           "mērījuma un no modeļa izrietoša secinājuma.",
    protu=["nosaukt Saules sistēmas objektus;",
           "salīdzināt planētu grupas;",
           "atšķirt novērojumu no secinājuma;",
           "izmantot 4. temata sakarības astronomijā."],
    atkartojums="4. tematā aprēķinājām pavadoņu orbītas un Keplera "
                "likumus. Šodien tos pašus likumus lietosim visai Saules "
                "sistēmai.",
    uzdevumu_apraksts="Saules sistēmas aprēķini un secinājumi",
    teorija=[
        ("Saules sistēmas uzbūve", [
            ("tabula",
             ["Grupa", "Piemēri", "Raksturīgais"],
             [["Iekšējās planētas", "Merkurs, Venera, Zeme, Marss",
               "Akmens, mazas, tuvu"],
              ["Asteroīdu josla", "Ceresa un mazie ķermeņi",
               "Starp Marsu un Jupiteru"],
              ["Ārējās planētas", "Jupiters, Saturns, Urāns, Neptūns",
               "Gāzu milži, tālu"],
              ["Mazie ķermeņi", "Komētas, meteoroīdi", "Ledus un ieži"]],
             [3.00, 4.40, 2.83]),
            ("panelis", "MĒROGS, KO GRŪTI IEDOMĀTIES",
             ["Attālumu no Zemes līdz Saulei (1,5·10¹¹ m) sauc par "
              "astronomisko vienību; gaisma to veic 8 minūtēs.",
              "Līdz Neptūnam gaisma iet apmēram 4 stundas, bet līdz "
              "tuvākajai zvaigznei - vairāk nekā 4 gadus.",
              "Tāpēc astronomijā attālumus mēra gaismas gados un "
              "astronomiskajās vienībās, nevis metros."], NAVY),
        ]),
        ("Novērojums, mērījums, secinājums", [
            ("divi",
             ("TIEŠS NOVĒROJUMS", GREEN,
              ["Redzam planētas disku",
               "teleskopā.",
               "Redzam Mēness fāzes.",
               "Fotografējam Marsa virsmu.",
               "To var apstiprināt",
               "atkārtoti."]),
             ("SECINĀJUMS NO MODEĻA", GOLD,
              ["Planētas masa no",
               "pavadoņa kustības.",
               "Zvaigznes sastāvs no",
               "spektra.",
               "Nav redzēts tieši, bet",
               "izriet no likumiem."])),
            ("panelis", "KĀPĒC ŠĪ ATŠĶIRĪBA IR SVARĪGA",
             ["Zinātnē vienmēr norāda, kas ir izmērīts un kas - "
              "izsecināts; tas ļauj citiem pārbaudīt rezultātu.",
              "Secinājums ir tik drošs, cik drošs ir modelis, uz kuru tas "
              "balstās.",
              "Tāpēc jaunas teorijas pārbauda ar jauniem novērojumiem, "
              "nevis ar pārliecības spēku."], GREY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Gaismas ceļš",
             teksts="Attālums no Saules līdz Zemei ir 1,5·10¹¹ m.\n"
                    "Cik ilgi gaisma to veic? (c = 3,0·10⁸ m/s)",
             dots=["s = 1,5·10¹¹ m", "c = 3,0·10⁸ m/s"],
             jaaprekina=["t = ?"],
             formulas=["t = s/c"],
             aprekins=["1)  t = 1,5·10¹¹ : 3,0·10⁸",
                       "2)  t = 500 s",
                       "3)  t ≈ 8,3 minūtes"],
             atbilde="t ≈ 500 s ≈ 8,3 min",
             piezime="Mēs vienmēr redzam Sauli tādu, kāda tā bija pirms "
                     "astoņām minūtēm."),
        dict(nr=2, virsraksts="Gaismas gads",
             teksts="Cik metru ir viens gaismas gads?\n"
                    "(c = 3,0·10⁸ m/s; gadā 3,15·10⁷ s)",
             dots=["c = 3,0·10⁸ m/s", "t = 3,15·10⁷ s"],
             jaaprekina=["s = ?"],
             formulas=["s = ct"],
             aprekins=["1)  s = 3,0·10⁸ · 3,15·10⁷",
                       "2)  s ≈ 9,5·10¹⁵ m",
                       "3)  Tas ir apmēram 63 000 astronomisko vienību"],
             atbilde="s ≈ 9,5·10¹⁵ m",
             piezime="Gaismas gads ir attāluma, nevis laika "
                     "mērvienība - tā ir bieža kļūda."),
        dict(nr=3, virsraksts="Svars uz citas planētas",
             teksts="Uz Marsa brīvās krišanas paātrinājums ir 3,7 m/s².\n"
                    "Cik liels ir 70 kg smaga cilvēka svars uz Marsa un\n"
                    "uz Zemes? (g = 9,8 m/s²)",
             dots=["m = 70 kg", "g(Marss) = 3,7 m/s²",
                   "g(Zeme) = 9,8 m/s²"],
             jaaprekina=["P₁ = ?", "P₂ = ?"],
             formulas=["P = mg"],
             aprekins=["1)  Uz Zemes: 70 · 9,8 = 686 N",
                       "2)  Uz Marsa: 70 · 3,7 = 259 N",
                       "3)  Apmēram 2,6 reizes mazāk"],
             atbilde="Zeme: 686 N;  Marss: 259 N",
             piezime="Masa nemainās - mainās tikai svars, jo atšķiras "
                     "gravitācijas lauks."),
        dict(nr=4, virsraksts="Novērojums vai secinājums",
             teksts="Nosaki, kas ir tiešs novērojums un kas secinājums:\n"
                    "a) Jupiteram ir joslas; b) Saules sastāvs ir\n"
                    "galvenokārt ūdeņradis; c) Marsam ir divi pavadoņi.",
             dots=["a) teleskopa attēls", "b) spektra analīze",
                   "c) teleskopa attēls"],
             jaaprekina=["Novērojums vai secinājums?"],
             formulas=["Novērojums - redzams tieši",
                       "Secinājums - izriet no modeļa"],
             aprekins=["1)  a) tiešs novērojums",
                       "2)  b) secinājums no spektra modeļa",
                       "3)  c) tiešs novērojums"],
             atbilde="a) un c) novērojumi; b) secinājums",
             piezime="Secinājums nav vājāks par novērojumu - bet tas ir "
                     "atkarīgs no modeļa pareizības."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Saules sistēmā ir akmens planētas, gāzu milži un mazie "
            "ķermeņi.",
            "Attālumus mēra astronomiskajās vienībās un gaismas gados.",
            "Gaismas gads ir attālums, nevis laiks.",
            "Zinātnē nošķir novēroto no izsecinātā.",
        ],
        majasdarbs=[
            "s = 7,8·10¹¹ m (līdz Jupiteram). Cik ilgi iet gaisma?",
            "m = 60 kg, g = 1,6 m/s² (Mēness). Aprēķini svaru.",
            "Nosauc pa vienam novērojuma un secinājuma piemēram.",
        ],
        pasvertejums=["Zinu Saules sistēmas uzbūvi",
                      "Saprotu mērogus",
                      "Protu rēķināt gaismas ceļu",
                      "Atšķiru novērojumu no secinājuma"],
        nakama="Nākamā stunda: zvaigznes un to evolūcija."),
),

dict(
    nr="14.8", virsraksts="Zvaigznes un to evolūcija",
    jautajums="Kāpēc zvaigznes atšķiras un mainās?",
    apaksraksts="Krāsa un temperatūra · Zvaigžņu mūžs · Datu lasīšana",
    merkis="Skaidrot zvaigžņu krāsu, temperatūru un evolūcijas "
           "pamatidejas un lasīt vienkāršu datu kopu.",
    protu=["saistīt zvaigznes krāsu ar temperatūru;",
           "nosaukt zvaigznes evolūcijas posmus;",
           "izskaidrot, no kā atkarīgs zvaigznes mūžs;",
           "lasīt vienkāršu zvaigžņu datu tabulu."],
    atkartojums="14.2. stundā spektri pastāstīja par vielas sastāvu. "
                "Šodien tie pastāstīs arī par zvaigznes temperatūru un "
                "nākotni.",
    uzdevumu_apraksts="Zvaigžņu dati un salīdzinājumi",
    teorija=[
        ("Krāsa un temperatūra", [
            ("tabula",
             ["Krāsa", "Virsmas temperatūra", "Piemērs"],
             [["Zilgani balta", "20 000-30 000 K", "Rigels"],
              ["Balta", "apmēram 10 000 K", "Sīriuss"],
              ["Dzeltena", "apmēram 5800 K", "Saule"],
              ["Sarkana", "3000-4000 K", "Betelgeize"]],
             [3.00, 4.00, 3.23]),
            ("panelis", "KO KRĀSA PASAKA",
             ["Karstākas zvaigznes izstaro vairāk īsviļņu gaismas, tāpēc "
              "izskatās zilganas; vēsākas - sarkanas.",
              "Tas ir tas pats nepārtrauktais spektrs, ko apguvām "
              "14.2. stundā - tikai tā maksimums nobīdās.",
              "Tāpēc zvaigznes temperatūru var noteikt, vispār "
              "nepieskaroties tai - pietiek ar krāsu."], NAVY),
        ]),
        ("Zvaigznes mūžs", [
            ("divi",
             ("KĀ SAULE", GOLD,
              ["Vidēja masa.",
               "Mūžs apmēram 10 miljardi",
               "gadu.",
               "Beigās kļūst par sarkano",
               "milzi, tad balto punduri."]),
             ("DAUDZ SMAGĀKA", RED,
              ["Liela masa.",
               "Degvielu iztērē ātri -",
               "daži miljoni gadu.",
               "Beidzas ar supernovu,",
               "paliek neitronu zvaigzne",
               "vai melnais caurums."])),
            ("panelis", "NO KĀ RODAS ELEMENTI",
             ["Zvaigznēs sintēzē rodas elementi līdz dzelzij; smagākie "
              "rodas supernovu sprādzienos.",
              "Tāpēc vielas, no kā sastāv Zeme un mēs paši, ir radušās "
              "senās zvaigznēs.",
              "Zvaigžņu evolūcija ir arī stāsts par to, no kurienes "
              "nākuši ķīmiskie elementi."], GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Kura zvaigzne karstāka",
             teksts="Zvaigzne A ir zilgani balta, zvaigzne B - sarkana.\n"
                    "Kura ir karstāka un aptuveni cik reižu?",
             dots=["A: zilgani balta ≈ 25 000 K",
                   "B: sarkana ≈ 3500 K"],
             jaaprekina=["Attiecība = ?"],
             formulas=["Zilgana - karstāka",
                       "Sarkana - vēsāka"],
             aprekins=["1)  A karstāka",
                       "2)  25 000 : 3500 ≈ 7",
                       "3)  Apmēram 7 reizes karstāka"],
             atbilde="A ir apmēram 7 reizes karstāka",
             piezime="Krāsa ir ātrākais veids, kā novērtēt zvaigznes "
                     "temperatūru."),
        dict(nr=2, virsraksts="Zvaigznes mūžs",
             teksts="Saules mūžs ir apmēram 10 miljardi gadu, bet\n"
                    "smagai zvaigznei - 10 miljoni gadu.\n"
                    "Cik reižu tie atšķiras?",
             dots=["t₁ = 1,0·10¹⁰ gadi", "t₂ = 1,0·10⁷ gadi"],
             jaaprekina=["Attiecība = ?"],
             formulas=["Attiecība = t₁/t₂"],
             aprekins=["1)  1,0·10¹⁰ : 1,0·10⁷",
                       "2)  Attiecība = 1000",
                       "3)  Saule dzīvo 1000 reižu ilgāk"],
             atbilde="1000 reižu",
             piezime="Lielāka masa nozīmē ātrāku degvielas patēriņu un "
                     "īsāku mūžu."),
        dict(nr=3, virsraksts="Attālums gaismas gados",
             teksts="Sīriuss atrodas 8,1·10¹⁶ m attālumā.\n"
                    "Cik tas ir gaismas gados?\n"
                    "(1 gaismas gads ≈ 9,5·10¹⁵ m)",
             dots=["s = 8,1·10¹⁶ m", "1 g.g. = 9,5·10¹⁵ m"],
             jaaprekina=["Attālums = ?"],
             formulas=["n = s/(1 g.g.)"],
             aprekins=["1)  n = 8,1·10¹⁶ : 9,5·10¹⁵",
                       "2)  n ≈ 8,5",
                       "3)  Attālums ≈ 8,5 gaismas gadi"],
             atbilde="≈ 8,5 gaismas gadi",
             piezime="Sīriusa gaisma, ko redzam šovakar, ceļā ir bijusi "
                     "kopš 2018. gada."),
        dict(nr=4, virsraksts="Datu lasīšana",
             teksts="Zvaigzne X: krāsa sarkana, mūžs 12 miljardi gadu.\n"
                    "Zvaigzne Y: krāsa zila, mūžs 8 miljoni gadu.\n"
                    "Kurai masa lielāka un kā to pamato?",
             dots=["X: sarkana, ilgs mūžs",
                   "Y: zila, īss mūžs"],
             jaaprekina=["Kurai lielāka masa?"],
             formulas=["Lielāka masa - karstāka un īsāks mūžs"],
             aprekins=["1)  Y ir zila - tātad karstāka",
                       "2)  Y mūžs daudz īsāks",
                       "3)  Abas pazīmes norāda uz lielāku masu"],
             atbilde="Zvaigznei Y masa ir lielāka",
             piezime="Divas neatkarīgas pazīmes, kas norāda uz vienu "
                     "secinājumu - tas padara to drošāku."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Zvaigznes krāsa norāda tās virsmas temperatūru.",
            "Zilas zvaigznes ir karstas, sarkanas - vēsas.",
            "Lielāka masa nozīmē īsāku mūžu.",
            "Ķīmiskie elementi ir radušies zvaigznēs un supernovās.",
        ],
        majasdarbs=[
            "s = 4,0·10¹⁶ m. Cik tas ir gaismas gados?",
            "Salīdzini divas zvaigznes: 6000 K un 20 000 K.",
            "Uzraksti Saules evolūcijas posmus.",
        ],
        pasvertejums=["Saistu krāsu ar temperatūru",
                      "Zinu evolūcijas posmus",
                      "Zinu, no kā atkarīgs mūžs",
                      "Protu lasīt datu tabulu"],
        nakama="Nākamā stunda: galaktikas un Visuma izplešanās."),
),

]
