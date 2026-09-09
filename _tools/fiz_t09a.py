# -*- coding: utf-8 -*-
"""9. temats "Elektriskie lādiņi". A daļa: 9.1.-9.6. stunda."""

from fiz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN     # noqa: F401

TEMATS = "9. temats. Elektriskie lādiņi un elektriskais lauks"
KICKER = "FIZIKA I · 11. KLASE · 9. TEMATS: ELEKTRISKIE LĀDIŅI"
KURSS = "FIZIKA I · 11. KLASE"
MAPE = "C:/aphysics/Fizika_1/9. Elektriskie lādiņi"

STUNDAS = [

dict(
    nr="9.1", virsraksts="Lādiņš un elektrizācija",
    jautajums="Kāpēc apģērbs elektrizējas?",
    apaksraksts="Divu veidu lādiņi · Lādiņa nezūdamība · Vadītāji un "
                "izolatori",
    merkis="Skaidrot elektrizāciju ar lādiņa pārnesi un nošķirt vadītājus "
           "no izolatoriem.",
    protu=["nosaukt divu veidu lādiņus un to mijiedarbību;",
           "izskaidrot elektrizāciju ar elektronu pārnesi;",
           "formulēt lādiņa nezūdamības likumu;",
           "atšķirt vadītājus no izolatoriem."],
    atkartojums="7. tematā noskaidrojām, ka atomā ir kodols un elektroni. "
                "Tieši elektronu pārvietošanās izskaidro visu, kas notiek "
                "šajā tematā.",
    uzdevumu_apraksts="Lādiņa nezūdamība un elektronu skaits",
    teorija=[
        ("Elektriskais lādiņš", [
            ("panelis", "DIVU VEIDU LĀDIŅI",
             ["Ir pozitīvi un negatīvi lādiņi. Vienādi lādiņi atgrūžas, "
              "pretēji - pievelkas.",
              "Lādiņu mēra kulonos (C). Mazākais brīvais lādiņš ir "
              "elementārlādiņš e = 1,6·10⁻¹⁹ C - tāds ir elektronam un "
              "protonam.",
              "Ķermenis ir neitrāls, ja protonu un elektronu skaits "
              "sakrīt."], NAVY),
            ("divi",
             ("KĀ RODAS LĀDIŅŠ", BLUE,
              ["Berzējot pāriet ELEKTRONI.",
               "Kas zaudē elektronus -",
               "kļūst pozitīvs.",
               "Kas iegūst - negatīvs.",
               "Protoni nekustas."]),
             ("LĀDIŅA NEZŪDAMĪBA", GREEN,
              ["Slēgtā sistēmā lādiņu",
               "summa nemainās.",
               "Lādiņš netiek radīts,",
               "tikai pārdalīts.",
               "Piemērs: +q un −q kopā."])),
        ]),
        ("Vadītāji un izolatori", [
            ("tabula",
             ["Grupa", "Piemēri", "Kāpēc"],
             [["Vadītāji", "Metāli, sāls šķīdums, cilvēks",
               "Ir brīvie lādiņnesēji"],
              ["Izolatori", "Stikls, gumija, plastmasa",
               "Lādiņi saistīti vietā"],
              ["Pusvadītāji", "Silīcijs, germānijs",
               "Vada tikai noteiktos apstākļos"],
              ["Zemējums", "Vads uz zemi", "Novada lieko lādiņu"]],
             [2.90, 4.20, 3.13]),
            ("panelis", "KĀPĒC ELEKTRIZĒJAS APĢĒRBS",
             ["Sintētiskas drēbes ir izolatori: berzējoties uzkrātie "
              "lādiņi paliek uz vietas un nevar aizplūst.",
              "Sausā gaisā efekts ir spēcīgāks - mitrs gaiss vada un "
              "lādiņu novada.",
              "Tāpēc degvielas cisternām ir zemējuma ķēde, bet "
              "elektronikas remontā lieto antistatisko aproci."], BLUE),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Elektronu skaits",
             teksts="Ķermenim ir lādiņš −3,2·10⁻⁹ C.\n"
                    "Cik liekus elektronus tas ieguvis?\n"
                    "(e = 1,6·10⁻¹⁹ C)",
             dots=["q = −3,2·10⁻⁹ C", "e = 1,6·10⁻¹⁹ C"],
             jaaprekina=["N = ?"],
             formulas=["q = N · e", "N = q/e"],
             aprekins=["1)  N = 3,2·10⁻⁹ : 1,6·10⁻¹⁹",
                       "2)  N = 2·10¹⁰",
                       "3)  Ķermenis ieguvis 2·10¹⁰ elektronu"],
             atbilde="N = 2·10¹⁰ elektronu",
             piezime="Lādiņš vienmēr ir elementārlādiņa vesels "
                     "daudzkārtnis."),
        dict(nr=2, virsraksts="Lādiņš pēc pieskaršanās",
             teksts="Divas vienādas metāla lodītes ar lādiņiem +8 nC un\n"
                    "−2 nC saskaras un tiek atdalītas.\n"
                    "Kāds lādiņš ir katrai?",
             dots=["q₁ = +8 nC", "q₂ = −2 nC", "Lodītes vienādas"],
             jaaprekina=["q = ?"],
             formulas=["Lādiņa nezūdamība", "q = (q₁ + q₂)/2"],
             aprekins=["1)  Kopējais lādiņš: 8 + (−2) = 6 nC",
                       "2)  q = 6 : 2",
                       "3)  q = +3 nC katrai"],
             atbilde="q = +3 nC katrai lodītei",
             piezime="Kopējais lādiņš saglabājās - tas tikai pārdalījās "
                     "vienādi."),
        dict(nr=3, virsraksts="Ķermeņa lādiņš",
             teksts="No neitrāla ķermeņa aiziet 5·10¹⁰ elektronu.\n"
                    "Kāds lādiņš tam rodas? (e = 1,6·10⁻¹⁹ C)",
             dots=["N = 5·10¹⁰", "e = 1,6·10⁻¹⁹ C"],
             jaaprekina=["q = ?"],
             formulas=["q = N · e"],
             aprekins=["1)  q = 5·10¹⁰ · 1,6·10⁻¹⁹",
                       "2)  q = 8·10⁻⁹ C",
                       "3)  Lādiņš POZITĪVS - elektroni aizgāja"],
             atbilde="q = +8·10⁻⁹ C = +8 nC",
             piezime="Zīmi nosaka virziens: aiziet elektroni - paliek "
                     "pozitīvs lādiņš."),
        dict(nr=4, virsraksts="Vadītājs vai izolators",
             teksts="Nosaki, kurš materiāls novadīs uzkrāto lādiņu:\n"
                    "a) gumijas cimds; b) mitra roka; c) sausa vilna.\n"
                    "Paskaidro katru gadījumu!",
             dots=["a) gumija", "b) mitra roka", "c) sausa vilna"],
             jaaprekina=["Vada vai nevada?"],
             formulas=["Vadītājā ir brīvie lādiņnesēji",
                       "Izolatorā lādiņi saistīti"],
             aprekins=["1)  a) gumija - izolators, nenovada",
                       "2)  b) mitra roka - vadītājs, novada",
                       "3)  c) sausa vilna - izolators, uzkrāj"],
             atbilde="Novada tikai mitra roka",
             piezime="Tāpēc mitrās rokas ar elektrību ir bīstamas - "
                     "ķermenis kļūst par labu vadītāju."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Ir pozitīvi un negatīvi lādiņi; vienādi atgrūžas.",
            "Elektrizācija ir elektronu pārnese, nevis lādiņa radīšana.",
            "Slēgtā sistēmā lādiņu summa saglabājas.",
            "Vadītājos ir brīvie lādiņnesēji, izolatoros - nav.",
        ],
        majasdarbs=[
            "q = 4,8·10⁻⁹ C. Cik elektronu tas ir?",
            "Lodītes ar +10 nC un +4 nC saskaras. Kāds lādiņš katrai?",
            "Paskaidro, kāpēc ziemā apģērbs elektrizējas vairāk.",
        ],
        pasvertejums=["Zinu lādiņu veidus",
                      "Protu izskaidrot elektrizāciju",
                      "Zinu lādiņa nezūdamību",
                      "Atšķiru vadītājus no izolatoriem"],
        nakama="Nākamā stunda: lādiņu mijiedarbība un Kulona likums."),
),

dict(
    nr="9.2", virsraksts="Lādiņu mijiedarbība",
    jautajums="Kā attālums ietekmē elektrisko spēku?",
    apaksraksts="Kulona likums F = kq₁q₂/r² · Attāluma kvadrāts",
    merkis="Lietot Kulona likumu vienkāršam lādiņu pārim un izskaidrot "
           "attāluma ietekmi.",
    protu=["noteikt, vai lādiņi pievelkas vai atgrūžas;",
           "lietot Kulona likumu;",
           "izskaidrot attāluma kvadrāta ietekmi;",
           "salīdzināt elektrisko un gravitācijas spēku."],
    atkartojums="4. tematā gravitācijas likumā spēks arī bija apgriezti "
                "proporcionāls attāluma kvadrātam. Kulona likumam ir "
                "tieši tāda pati forma.",
    uzdevumu_apraksts="Kulona likuma aprēķini",
    teorija=[
        ("Kulona likums", [
            ("formula", "LĀDIŅU MIJIEDARBĪBAS SPĒKS",
             "F = kq₁q₂/r²        k = 9·10⁹",
             "Spēks ir tieši proporcionāls lādiņu reizinājumam un "
             "apgriezti proporcionāls attāluma kvadrātam. Konstante "
             "k = 9·10⁹ N·m²/C². Spēks vērsts pa taisni starp "
             "lādiņiem.", GOLD),
            ("kartitas", [
                ("VIENĀDI LĀDIŅI", RED,
                 ["Abi + vai abi −.",
                  "Spēki ATGRŪŽ.",
                  "Vērsti prom viens no otra."]),
                ("PRETĒJI LĀDIŅI", GREEN,
                 ["Viens +, otrs −.",
                  "Spēki PIEVELK.",
                  "Vērsti viens pret otru."]),
                ("ATTĀLUMS", BLUE,
                 ["r divkāršo - F krīt",
                  "četras reizes.",
                  "r trīskāršo - deviņas."]),
            ]),
        ]),
        ("Divi līdzīgi likumi", [
            ("tabula",
             ["Pazīme", "Kulona likums", "Gravitācijas likums"],
             [["Formula", "F = kq₁q₂/r²", "F = Gm₁m₂/r²"],
              ["Kas mijiedarbojas", "Lādiņi", "Masas"],
              ["Virziens", "Pievelk vai atgrūž", "Tikai pievelk"],
              ["Stiprums", "Ļoti liels", "Ļoti mazs"]],
             [3.00, 3.60, 3.63]),
            ("panelis", "CIK LIELA IR STARPĪBA",
             ["Diviem elektroniem elektriskais atgrūšanās spēks ir apmēram "
              "10⁴² reižu lielāks nekā gravitācijas pievilkšanās.",
              "Tomēr ikdienā gravitāciju jūtam vairāk, jo ķermeņi ir "
              "gandrīz neitrāli - pozitīvie un negatīvie lādiņi "
              "kompensējas.",
              "Tieši elektriskie spēki notur atomus molekulās un "
              "cietvielās."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Spēks starp diviem lādiņiem",
             teksts="Divi lādiņi 2·10⁻⁶ C un 3·10⁻⁶ C atrodas 0,30 m\n"
                    "attālumā. Aprēķini spēku! (k = 9·10⁹ N·m²/C²)",
             dots=["q₁ = 2·10⁻⁶ C", "q₂ = 3·10⁻⁶ C", "r = 0,30 m",
                   "k = 9·10⁹"],
             jaaprekina=["F = ?"],
             formulas=["F = kq₁q₂/r²"],
             aprekins=["1)  q₁q₂ = 6·10⁻¹² C²",
                       "2)  r² = 0,09 m²",
                       "3)  F = 9·10⁹ · 6·10⁻¹² : 0,09 = 0,60 N"],
             atbilde="F = 0,60 N",
             piezime="Abi lādiņi pozitīvi - tātad spēki tos atgrūž."),
        dict(nr=2, virsraksts="Attālumu divkāršo",
             teksts="Iepriekšējos lādiņus attālina no 0,30 m līdz 0,60 m.\n"
                    "Kā mainās spēks? Aprēķini jauno vērtību!",
             dots=["F₁ = 0,60 N", "r₁ = 0,30 m", "r₂ = 0,60 m"],
             jaaprekina=["F₂ = ?"],
             formulas=["F ~ 1/r²", "F₂ = F₁/4"],
             aprekins=["1)  Attālums pieaudzis 2 reizes",
                       "2)  Spēks samazinās 2² = 4 reizes",
                       "3)  F₂ = 0,60 : 4 = 0,15 N"],
             atbilde="F₂ = 0,15 N",
             piezime="Attāluma kvadrāts nozīmē: divreiz tālāk - četrreiz "
                     "vājāk."),
        dict(nr=3, virsraksts="Meklē lādiņu",
             teksts="Divi vienādi lādiņi 0,10 m attālumā atgrūžas ar\n"
                    "spēku 0,90 N. Aprēķini katra lādiņa lielumu!\n"
                    "(k = 9·10⁹ N·m²/C²)",
             dots=["F = 0,90 N", "r = 0,10 m", "q₁ = q₂ = q"],
             jaaprekina=["q = ?"],
             formulas=["F = kq²/r²", "q² = Fr²/k"],
             aprekins=["1)  Fr² = 0,90 · 0,01 = 0,009",
                       "2)  q² = 0,009 : 9·10⁹ = 1·10⁻¹²",
                       "3)  q = 1·10⁻⁶ C = 1 µC"],
             atbilde="q = 1·10⁻⁶ C",
             piezime="Mikrokulons ir tipisks statiskās elektrības "
                     "lādiņš."),
        dict(nr=4, virsraksts="Pievelk vai atgrūž",
             teksts="Nosaki spēka virzienu un aprēķini lielumu diviem\n"
                    "lādiņiem +5·10⁻⁶ C un −4·10⁻⁶ C, kas atrodas\n"
                    "0,20 m attālumā. (k = 9·10⁹ N·m²/C²)",
             dots=["q₁ = +5·10⁻⁶ C", "q₂ = −4·10⁻⁶ C", "r = 0,20 m"],
             jaaprekina=["F = ?", "Virziens = ?"],
             formulas=["F = kq₁q₂/r²"],
             aprekins=["1)  q₁q₂ = 20·10⁻¹² = 2·10⁻¹¹",
                       "2)  r² = 0,04 m²",
                       "3)  F = 9·10⁹ · 2·10⁻¹¹ : 0,04 = 4,5 N"],
             atbilde="F = 4,5 N, lādiņi pievelkas",
             piezime="Spēka lielumā zīmes neieliek - virzienu nosaka "
                     "atsevišķi pēc lādiņu zīmēm."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "F = kq₁q₂/r²; k = 9·10⁹ N·m²/C².",
            "Vienādi lādiņi atgrūžas, pretēji pievelkas.",
            "Divreiz lielāks attālums - četrreiz mazāks spēks.",
            "Kulona un gravitācijas likumam ir vienāda forma.",
        ],
        majasdarbs=[
            "q₁ = 1·10⁻⁶ C, q₂ = 4·10⁻⁶ C, r = 0,20 m. Aprēķini F.",
            "Kā mainīsies spēks, ja attālumu samazinās 3 reizes?",
            "Salīdzini Kulona un gravitācijas likumu - divas līdzības un "
            "viena atšķirība.",
        ],
        pasvertejums=["Protu noteikt spēka virzienu",
                      "Protu lietot Kulona likumu",
                      "Saprotu attāluma kvadrātu",
                      "Protu salīdzināt abus likumus"],
        nakama="Nākamā stunda: elektriskā lauka modelis."),
),

dict(
    nr="9.3", virsraksts="Elektriskā lauka modelis",
    jautajums="Kā parādīt neredzama elektriskā lauka darbību?",
    apaksraksts="E = F/q · Lauka līnijas · [E] = N/C",
    merkis="Lasīt lauka līniju attēlu, noteikt spēka virzienu un lietot "
           "sakarību E = F/q.",
    protu=["izskaidrot, kas ir elektriskais lauks;",
           "lasīt lauka līniju attēlu;",
           "lietot E = F/q;",
           "noteikt spēka virzienu lādiņam laukā."],
    atkartojums="4. tematā gravitācijas lauku attēlojām ar līnijām. "
                "Elektriskais lauks ir tāds pats modelis - tikai avots "
                "ir lādiņš, nevis masa.",
    uzdevumu_apraksts="Lauka intensitātes aprēķini",
    teorija=[
        ("Elektriskais lauks", [
            ("formula", "LAUKA INTENSITĀTE",
             "E = F/q        F = qE        [E] = N/C",
             "Lauka intensitāte rāda, cik liels spēks darbojas uz vienu "
             "kulonu lādiņa. Tā ir vektors: virziens sakrīt ar spēku, "
             "kas darbotos uz POZITĪVU lādiņu.", GOLD),
            ("divi",
             ("LAUKA LĪNIJAS", BLUE,
              ["Sākas pie + lādiņa,",
               "beidzas pie − lādiņa.",
               "Nekad nekrustojas.",
               "Blīvākas - lauks stiprāks."]),
             ("SPĒKA VIRZIENS", GREEN,
              ["Pozitīvam lādiņam -",
               "pa lauka virzienu.",
               "Negatīvam lādiņam -",
               "pretēji laukam."])),
        ]),
        ("Lauks dažādās situācijās", [
            ("tabula",
             ["Avots", "Līniju attēls", "Lauka stiprums"],
             [["Punktveida +", "Stari uz āru", "Krītas kā 1/r²"],
              ["Punktveida −", "Stari uz iekšu", "Krītas kā 1/r²"],
              ["Divas plāksnes", "Paralēlas līnijas", "Vienmērīgs"],
              ["Vadītāja iekšpuse", "Nav līniju", "E = 0"]],
             [3.20, 3.40, 3.63]),
            ("panelis", "VIENMĒRĪGS LAUKS",
             ["Starp divām paralēlām lādētām plāksnēm lauka līnijas ir "
              "paralēlas un vienādi blīvas - lauks ir vienmērīgs.",
              "Tādā laukā uz lādiņu visur darbojas vienāds spēks, tāpēc "
              "aprēķini ir vienkārši.",
              "Vadītāja iekšienē lauks ir nulle - tāpēc metāla korpuss "
              "pasargā elektroniku."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Lauka intensitāte",
             teksts="Uz lādiņu 2·10⁻⁶ C laukā darbojas spēks 0,50 N.\n"
                    "Aprēķini lauka intensitāti!",
             dots=["q = 2·10⁻⁶ C", "F = 0,50 N"],
             jaaprekina=["E = ?"],
             formulas=["E = F/q"],
             aprekins=["1)  E = 0,50 : 2·10⁻⁶",
                       "2)  E = 2,5·10⁵ N/C"],
             atbilde="E = 2,5·10⁵ N/C",
             piezime="Intensitāte nav atkarīga no ievietotā lādiņa - to "
                     "nosaka lauka avots."),
        dict(nr=2, virsraksts="Spēks uz lādiņu",
             teksts="Laukā ar intensitāti 400 N/C ievieto lādiņu\n"
                    "5·10⁻⁸ C. Aprēķini spēku!",
             dots=["E = 400 N/C", "q = 5·10⁻⁸ C"],
             jaaprekina=["F = ?"],
             formulas=["E = F/q", "F = qE"],
             aprekins=["1)  F = 5·10⁻⁸ · 400",
                       "2)  F = 2·10⁻⁵ N"],
             atbilde="F = 2·10⁻⁵ N",
             piezime="Spēks mazs, bet uz vieglu putekļu daļiņu ar to "
                     "pietiek."),
        dict(nr=3, virsraksts="Meklē lādiņu",
             teksts="Laukā ar intensitāti 1,2·10⁴ N/C uz lādiņu darbojas\n"
                    "spēks 0,024 N. Aprēķini lādiņu!",
             dots=["E = 1,2·10⁴ N/C", "F = 0,024 N"],
             jaaprekina=["q = ?"],
             formulas=["E = F/q", "q = F/E"],
             aprekins=["1)  q = 0,024 : 1,2·10⁴",
                       "2)  q = 2·10⁻⁶ C",
                       "3)  q = 2 µC"],
             atbilde="q = 2·10⁻⁶ C",
             piezime="No vienas formulas var izteikt visus trīs "
                     "lielumus."),
        dict(nr=4, virsraksts="Virziens laukā",
             teksts="Vienmērīgā laukā, kas vērsts pa labi, ievieto\n"
                    "a) pozitīvu un b) negatīvu lādiņu.\n"
                    "Uz kuru pusi darbojas spēks katrā gadījumā?",
             dots=["Lauks vērsts pa labi", "a) q > 0", "b) q < 0"],
             jaaprekina=["Spēka virziens = ?"],
             formulas=["F = qE", "Zīme nosaka virzienu"],
             aprekins=["1)  a) q > 0: spēks pa lauka virzienu - pa labi",
                       "2)  b) q < 0: spēks pretēji laukam - pa kreisi",
                       "3)  Lielums abos gadījumos F = qE"],
             atbilde="a) pa labi;  b) pa kreisi",
             piezime="Lauka virzienu vienmēr nosaka pēc pozitīva "
                     "lādiņa - tā ir vienošanās."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Elektriskais lauks ir modelis, kas apraksta lādiņa iedarbību.",
            "E = F/q; intensitāti mēra ņūtonos uz kulonu.",
            "Lauka līnijas sākas pie + un beidzas pie − lādiņa.",
            "Vadītāja iekšienē lauks ir nulle.",
        ],
        majasdarbs=[
            "F = 0,80 N, q = 4·10⁻⁶ C. Aprēķini E.",
            "E = 250 N/C, q = 6·10⁻⁸ C. Aprēķini F.",
            "Uzzīmē lauka līnijas pozitīvam un negatīvam lādiņam.",
        ],
        pasvertejums=["Zinu, kas ir lauks",
                      "Protu lasīt lauka līnijas",
                      "Protu lietot E = F/q",
                      "Protu noteikt spēka virzienu"],
        nakama="Nākamā stunda: spriegums un enerģija elektriskajā laukā."),
),

dict(
    nr="9.4", virsraksts="Spriegums un enerģija",
    jautajums="Ko nozīmē spriegums?",
    apaksraksts="U = A/q · E = U/d · [U] = volts",
    merkis="Saistīt spriegumu ar enerģiju uz vienu lādiņa vienību un pēc "
           "parauga lietot U = A/q un E = U/d.",
    protu=["izskaidrot sprieguma jēgu;",
           "lietot U = A/q;",
           "lietot E = U/d vienmērīgā laukā;",
           "aprēķināt lādiņa pārvietošanas darbu."],
    atkartojums="5. tematā darbs bija spēka un ceļa reizinājums. "
                "Elektriskajā laukā darbs ir atkarīgs no lādiņa un "
                "sprieguma - un tas ir daudz ērtāk.",
    uzdevumu_apraksts="Spriegums, darbs un lauka intensitāte",
    teorija=[
        ("Spriegums", [
            ("formula", "SPRIEGUMS UN DARBS",
             "U = A/q        A = qU        [U] = volts (V)",
             "Spriegums rāda, cik daudz darba lauks paveic, pārvietojot "
             "vienu kulonu lādiņa. Viens volts ir viens džouls uz vienu "
             "kulonu.", GOLD),
            ("kartitas", [
                ("U - SPRIEGUMS", BLUE,
                 ["Enerģija uz lādiņu.",
                  "Mēra voltos.",
                  "Rozetē 230 V."]),
                ("A - DARBS", GREEN,
                 ["Lauka paveiktais darbs.",
                  "Mēra džoulos.",
                  "A = qU."]),
                ("q - LĀDIŅŠ", GOLD,
                 ["Pārvietotais lādiņš.",
                  "Mēra kulonos.",
                  "q = A/U."]),
            ]),
        ]),
        ("Spriegums vienmērīgā laukā", [
            ("formula", "SAITE STARP U UN E",
             "E = U/d        U = E · d",
             "Vienmērīgā laukā starp divām plāksnēm, kas atrodas "
             "attālumā d, lauka intensitāte ir sprieguma un attāluma "
             "attiecība. Tāpēc intensitāti bieži mēra voltos uz metru.",
             GOLD),
            ("panelis", "SPRIEGUMS SADZĪVĒ",
             ["Baterija 1,5 V, telefona lādētājs 5 V, rozete 230 V, "
              "augstsprieguma līnija 110 000 V.",
              "Bīstamību nosaka nevis spriegums viens pats, bet strāva "
              "caur ķermeni - tomēr lielāks spriegums padara to "
              "iespējamu.",
              "Sausa āda ir slikts vadītājs, mitra - labs; tāpēc "
              "elektroierīces nelieto ar slapjām rokām."], RED),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Darbs no sprieguma",
             teksts="Cik lielu darbu paveic lauks, pārvietojot lādiņu\n"
                    "0,50 C pie sprieguma 12 V?",
             dots=["q = 0,50 C", "U = 12 V"],
             jaaprekina=["A = ?"],
             formulas=["U = A/q", "A = qU"],
             aprekins=["1)  A = 0,50 · 12",
                       "2)  A = 6,0 J"],
             atbilde="A = 6,0 J",
             piezime="Volts reiz kulons dod džoulu - mērvienības "
                     "sakrīt."),
        dict(nr=2, virsraksts="Spriegums no darba",
             teksts="Pārvietojot lādiņu 2,0·10⁻³ C, lauks paveic\n"
                    "0,46 J darba. Aprēķini spriegumu!",
             dots=["q = 2,0·10⁻³ C", "A = 0,46 J"],
             jaaprekina=["U = ?"],
             formulas=["U = A/q"],
             aprekins=["1)  U = 0,46 : 2,0·10⁻³",
                       "2)  U = 230 V"],
             atbilde="U = 230 V",
             piezime="Tieši tāds spriegums ir mājas rozetē."),
        dict(nr=3, virsraksts="Lauks starp plāksnēm",
             teksts="Starp divām plāksnēm 0,020 m attālumā ir spriegums\n"
                    "600 V. Aprēķini lauka intensitāti!",
             dots=["U = 600 V", "d = 0,020 m"],
             jaaprekina=["E = ?"],
             formulas=["E = U/d"],
             aprekins=["1)  E = 600 : 0,020",
                       "2)  E = 30 000 V/m",
                       "3)  E = 3·10⁴ V/m"],
             atbilde="E = 3·10⁴ V/m",
             piezime="Volts uz metru un ņūtons uz kulonu ir viena un tā "
                     "pati mērvienība."),
        dict(nr=4, virsraksts="Spriegums no lauka",
             teksts="Vienmērīgā laukā ar intensitāti 5000 V/m plāksnes\n"
                    "atrodas 0,015 m attālumā.\n"
                    "Aprēķini spriegumu starp tām!",
             dots=["E = 5000 V/m", "d = 0,015 m"],
             jaaprekina=["U = ?"],
             formulas=["E = U/d", "U = E · d"],
             aprekins=["1)  U = 5000 · 0,015",
                       "2)  U = 75 V"],
             atbilde="U = 75 V",
             piezime="Jo tuvāk plāksnes, jo mazāks spriegums vajadzīgs "
                     "tam pašam laukam."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Spriegums ir enerģija uz vienu lādiņa vienību: U = A/q.",
            "Darbs elektriskajā laukā A = qU.",
            "Vienmērīgā laukā E = U/d.",
            "Volts uz metru ir tā pati vienība, kas ņūtons uz kulonu.",
        ],
        majasdarbs=[
            "q = 0,20 C, U = 9,0 V. Aprēķini A.",
            "A = 1,2 J, q = 0,050 C. Aprēķini U.",
            "U = 400 V, d = 0,010 m. Aprēķini E.",
        ],
        pasvertejums=["Saprotu sprieguma jēgu",
                      "Protu lietot U = A/q",
                      "Protu lietot E = U/d",
                      "Protu rēķināt darbu"],
        nakama="Nākamā stunda: vadītāji un kondensatori."),
),

dict(
    nr="9.5", virsraksts="Vadītāji un kondensatori",
    jautajums="Kur izmanto lādiņu pārdali un enerģijas uzkrāšanu?",
    apaksraksts="Ekranēšana · C = q/U · [C] = farads",
    merkis="Skaidrot ekranēšanu un kondensatora darbības ideju un pēc "
           "parauga lietot sakarību C = q/U.",
    protu=["izskaidrot lādiņu pārdali vadītājā;",
           "nosaukt ekranēšanas piemērus;",
           "izskaidrot kondensatora uzbūvi;",
           "lietot C = q/U."],
    atkartojums="Iepriekšējā stundā noskaidrojām, ka vadītāja iekšienē "
                "lauks ir nulle. Šodien redzēsim, kā to izmanto "
                "aizsardzībā un enerģijas uzkrāšanā.",
    uzdevumu_apraksts="Kondensatora kapacitātes aprēķini",
    teorija=[
        ("Lādiņi vadītājā", [
            ("panelis", "LĀDIŅI IZVIETOJAS UZ VIRSMAS",
             ["Vadītājā brīvie lādiņi atgrūžas un pārvietojas, līdz "
              "izvietojas uz ārējās virsmas - iekšienē lauks kļūst "
              "nulle.",
              "Tāpēc metāla korpuss pasargā elektroniku no ārējiem "
              "laukiem; to sauc par ekranēšanu jeb Faradeja būri.",
              "Automašīna zibens laikā ir droša tieši šī iemesla dēļ - "
              "strāva plūst pa virsmu, nevis caur salonu."], NAVY),
            ("divi",
             ("KUR EKRANĒ", BLUE,
              ["Mikroviļņu krāsns durvis.",
               "Ekranēti vadi.",
               "Automašīnas virsbūve.",
               "Bankas kartes maciņš."]),
             ("KUR NEEKRANĒ", RED,
              ["Koka vai plastmasas māja.",
               "Atvērtas durvis vai logs.",
               "Izolatora korpuss.",
               "Nesavienots metāls."])),
        ]),
        ("Kondensators", [
            ("formula", "KAPACITĀTE",
             "C = q/U        q = CU        [C] = farads (F)",
             "Kondensators ir divas plāksnes ar izolatoru starp tām. "
             "Kapacitāte rāda, cik lielu lādiņu tas uzkrāj pie viena "
             "volta sprieguma. Praksē lieto mikrofaradus.", GOLD),
            ("tabula",
             ["Kur izmanto", "Kāpēc tur", "Tipiskā kapacitāte"],
             [["Fotoaparāta zibspuldze", "Ātri atdod enerģiju",
               "100-1000 µF"],
              ["Datora barošana", "Izlīdzina spriegumu", "1000 µF"],
              ["Radio uztvērējs", "Noskaņo frekvenci", "Daži pF"],
              ["Skārienekrāns", "Reaģē uz pirkstu", "Daži pF"]],
             [3.60, 3.40, 3.23]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Kondensatora kapacitāte",
             teksts="Kondensators pie sprieguma 12 V uzkrāj lādiņu\n"
                    "6,0·10⁻⁴ C. Aprēķini kapacitāti!",
             dots=["U = 12 V", "q = 6,0·10⁻⁴ C"],
             jaaprekina=["C = ?"],
             formulas=["C = q/U"],
             aprekins=["1)  C = 6,0·10⁻⁴ : 12",
                       "2)  C = 5,0·10⁻⁵ F",
                       "3)  C = 50 µF"],
             atbilde="C = 5,0·10⁻⁵ F",
             piezime="Farads ir ļoti liela vienība - praksē gandrīz "
                     "vienmēr lieto mikrofaradus."),
        dict(nr=2, virsraksts="Uzkrātais lādiņš",
             teksts="Kondensatoru ar kapacitāti 220 µF pieslēdz\n"
                    "spriegumam 9,0 V. Cik lielu lādiņu tas uzkrāj?",
             dots=["C = 220 µF = 2,2·10⁻⁴ F", "U = 9,0 V"],
             jaaprekina=["q = ?"],
             formulas=["C = q/U", "q = CU"],
             aprekins=["1)  q = 2,2·10⁻⁴ · 9,0",
                       "2)  q = 1,98·10⁻³ C",
                       "3)  q ≈ 2,0 mC"],
             atbilde="q ≈ 2,0·10⁻³ C",
             piezime="Mikrofaradi vienmēr jāpārrēķina farados pirms "
                     "aprēķina."),
        dict(nr=3, virsraksts="Spriegums uz kondensatora",
             teksts="Kondensators ar kapacitāti 100 µF uzkrājis lādiņu\n"
                    "5,0·10⁻³ C. Aprēķini spriegumu!",
             dots=["C = 100 µF = 1,0·10⁻⁴ F", "q = 5,0·10⁻³ C"],
             jaaprekina=["U = ?"],
             formulas=["C = q/U", "U = q/C"],
             aprekins=["1)  U = 5,0·10⁻³ : 1,0·10⁻⁴",
                       "2)  U = 50 V"],
             atbilde="U = 50 V",
             piezime="Uzlādēts kondensators paliek bīstams arī pēc "
                     "atslēgšanas - tāpēc to izlādē."),
        dict(nr=4, virsraksts="Ekranēšana",
             teksts="Paskaidro, kāpēc mobilajam telefonam metāla kastē\n"
                    "zūd signāls, bet kartona kastē - nē!",
             dots=["Metāla kaste - vadītājs",
                   "Kartona kaste - izolators"],
             jaaprekina=["Kāpēc atšķirība?"],
             formulas=["Vadītājā E = 0",
                       "Lādiņi pārvietojas uz virsmu"],
             aprekins=["1)  Metālā brīvie lādiņi pārvietojas",
                       "2)  Tie kompensē ārējo lauku - iekšpusē E = 0",
                       "3)  Kartonā brīvo lādiņu nav - lauks iekļūst"],
             atbilde="Metāls ekranē, kartons - nē",
             piezime="Tas pats princips: Faradeja būris pasargā gan no "
                     "signāla, gan no zibens."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Vadītājā lādiņi izvietojas uz virsmas, iekšpusē E = 0.",
            "Ekranēšana pasargā no ārējiem elektriskajiem laukiem.",
            "Kondensators uzkrāj lādiņu un enerģiju.",
            "C = q/U; kapacitāti mēra farados.",
        ],
        majasdarbs=[
            "q = 3,0·10⁻⁴ C, U = 6,0 V. Aprēķini C.",
            "C = 470 µF, U = 12 V. Aprēķini q.",
            "Nosauc trīs vietas, kur sadzīvē izmanto ekranēšanu.",
        ],
        pasvertejums=["Zinu, kur izvietojas lādiņi",
                      "Protu izskaidrot ekranēšanu",
                      "Zinu kondensatora uzbūvi",
                      "Protu lietot C = q/U"],
        nakama="Nākamā stunda: elektrostatika sadzīvē un gatavošanās "
               "PD4."),
),

dict(
    nr="9.6", virsraksts="Elektrostatika sadzīvē",
    jautajums="Kā izskaidrot zibeni un elektrostatisko aizsardzību?",
    apaksraksts="Zibens · Zemējums · Drošība · Gatavošanās PD4",
    merkis="Ar lauka un lādiņa modeļiem pamatot drošu rīcību un "
           "nostiprināt temata pamataprēķinus.",
    protu=["izskaidrot zibens rašanos;",
           "pamatot zemējuma un zibensnovedēja nozīmi;",
           "nosaukt drošas rīcības noteikumus;",
           "risināt temata kombinētos uzdevumus."],
    atkartojums="Šī ir temata pēdējā mācību stunda. Nākamajā stundā ir "
                "PD4, kurā būs gan skaidrojumi, gan attēla analīze, gan "
                "aprēķins.",
    uzdevumu_apraksts="Kombinēti uzdevumi pirms PD4",
    teorija=[
        ("Zibens un aizsardzība", [
            ("panelis", "KĀ RODAS ZIBENS",
             ["Mākonī ledus kristāli un ūdens pilieni saduroties apmainās "
              "ar lādiņiem: apakšdaļa kļūst negatīva, augšdaļa - "
              "pozitīva.",
              "Kad lauka intensitāte pārsniedz gaisa izturību (apmēram "
              "3·10⁶ V/m), gaiss kļūst vadošs un notiek izlāde.",
              "Zibensnovedējs ir smails metāla stienis ar zemējumu - pie "
              "smailēm lauks ir stiprākais, tāpēc izlāde notiek tur."],
             NAVY),
            ("tabula",
             ["Situācija", "Kāpēc bīstami", "Kā rīkoties"],
             [["Atklāts lauks", "Cilvēks ir augstākais punkts",
               "Meklēt zemu vietu"],
              ["Zem koka", "Koks pievelk izlādi", "Neatrasties zem koka"],
              ["Degvielas uzpilde", "Dzirkstele aizdedzina tvaikus",
               "Pieskarties metālam"],
              ["Elektronikas remonts", "Statiskā izlāde bojā mikroshēmas",
               "Antistatiskā aproce"]],
             [3.20, 3.90, 3.13]),
        ]),
        ("Gatavošanās PD4", [
            ("divi",
             ("KAS BŪS PD4", BLUE,
              ["Elektrizācijas skaidrojums.",
               "Lauka līniju attēls.",
               "Kulona likuma aprēķins.",
               "Spriegums un darbs.",
               "Kondensators."]),
             ("FORMULAS", GREEN,
              ["F = kq₁q₂/r²",
               "E = F/q",
               "U = A/q",
               "E = U/d",
               "C = q/U"])),
            ("panelis", "BIEŽĀKĀS KĻŪDAS",
             ["Lādiņu atstāj mikrokulonos vai nanokulonos - pirms "
              "aprēķina viss jāpārrēķina kulonos.",
              "Kulona likumā aizmirst kāpināt attālumu kvadrātā.",
              "Sajauc lauka intensitāti E un spriegumu U - pirmais ir "
              "uz vienu metru, otrais uz visu attālumu."], RED),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Gaisa izturība",
             teksts="Gaiss kļūst vadošs, ja lauka intensitāte pārsniedz\n"
                    "3·10⁶ V/m. Cik liels spriegums vajadzīgs izlādei\n"
                    "pār 2,0 mm gaisa spraugu?",
             dots=["E = 3·10⁶ V/m", "d = 2,0 mm = 0,0020 m"],
             jaaprekina=["U = ?"],
             formulas=["E = U/d", "U = E · d"],
             aprekins=["1)  U = 3·10⁶ · 0,0020",
                       "2)  U = 6000 V"],
             atbilde="U = 6·10³ V",
             piezime="Tāpēc statiskās elektrības dzirkstele no pirksta "
                     "nozīmē vairākus tūkstošus voltu."),
        dict(nr=2, virsraksts="Divi lādiņi",
             teksts="Divi lādiņi 3·10⁻⁶ C un 6·10⁻⁶ C atrodas 0,15 m\n"
                    "attālumā. Aprēķini spēku! (k = 9·10⁹ N·m²/C²)",
             dots=["q₁ = 3·10⁻⁶ C", "q₂ = 6·10⁻⁶ C", "r = 0,15 m"],
             jaaprekina=["F = ?"],
             formulas=["F = kq₁q₂/r²"],
             aprekins=["1)  q₁q₂ = 1,8·10⁻¹¹",
                       "2)  r² = 0,0225 m²",
                       "3)  F = 9·10⁹ · 1,8·10⁻¹¹ : 0,0225 = 7,2 N"],
             atbilde="F = 7,2 N",
             piezime="Mikrokuloni ir mazi lādiņi, bet spēks jau ir "
                     "jūtams."),
        dict(nr=3, virsraksts="Enerģija kondensatorā",
             teksts="Zibspuldzes kondensators (C = 500 µF) uzlādēts līdz\n"
                    "300 V. Cik lielu lādiņu tas uzkrājis?",
             dots=["C = 500 µF = 5,0·10⁻⁴ F", "U = 300 V"],
             jaaprekina=["q = ?"],
             formulas=["C = q/U", "q = CU"],
             aprekins=["1)  q = 5,0·10⁻⁴ · 300",
                       "2)  q = 0,15 C"],
             atbilde="q = 0,15 C",
             piezime="Šo lādiņu kondensators atdod tūkstošdaļsekundē - "
                     "tāpēc zibsnis ir tik spilgts."),
        dict(nr=4, virsraksts="Darbs laukā",
             teksts="Lādiņu 4,0·10⁻⁶ C pārvieto starp punktiem, kuru\n"
                    "sprieguma starpība ir 250 V.\n"
                    "Cik lielu darbu paveic lauks?",
             dots=["q = 4,0·10⁻⁶ C", "U = 250 V"],
             jaaprekina=["A = ?"],
             formulas=["U = A/q", "A = qU"],
             aprekins=["1)  A = 4,0·10⁻⁶ · 250",
                       "2)  A = 1,0·10⁻³ J",
                       "3)  A = 1,0 mJ"],
             atbilde="A = 1,0·10⁻³ J",
             piezime="Mazs darbs - bet miljoniem tādu lādiņu kopā dod "
                     "reālu enerģiju."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Zibens rodas, kad lauks pārsniedz gaisa izturību.",
            "Zibensnovedējs un zemējums novada lādiņu drošā ceļā.",
            "Statiskā izlāde ir bīstama degvielai un elektronikai.",
            "Temata formulas: Kulona likums, E = F/q, U = A/q, C = q/U.",
        ],
        majasdarbs=[
            "Atkārto 9.1.-9.5. stundas kopsavilkumus.",
            "E = 3·10⁶ V/m, d = 5,0 mm. Aprēķini U.",
            "Sagatavo formulu lapu PD4.",
        ],
        pasvertejums=["Protu izskaidrot zibeni",
                      "Zinu aizsardzības principus",
                      "Protu risināt temata uzdevumus",
                      "Esmu gatavs PD4"],
        nakama="Nākamā stunda: PD4 - elektriskie lādiņi un elektriskais "
               "lauks."),
),

]
