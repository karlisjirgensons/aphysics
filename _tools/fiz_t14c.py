# -*- coding: utf-8 -*-
"""14. temats. C daļa: 14.9.-14.11. stunda.

14.11. ir pēdējā temata mācību stunda pirms PD9.
"""

from fiz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN     # noqa: F401
from fiz_t14a import TEMATS, KICKER, KURSS, MAPE              # noqa: F401

STUNDAS = [

dict(
    nr="14.9", virsraksts="Galaktikas un Visuma izplešanās",
    jautajums="Kādi novērojumi pamato Visuma modeļus?",
    apaksraksts="Galaktikas · Sarkanā nobīde · v = H·r",
    merkis="Raksturot Visuma struktūru un skaidrot sarkanās nobīdes un "
           "izplešanās saistību, atšķirot datus no interpretācijas.",
    protu=["raksturot Visuma struktūru;",
           "izskaidrot sarkano nobīdi;",
           "saistīt nobīdi ar izplešanos;",
           "atšķirt datus no to interpretācijas."],
    atkartojums="Iepriekšējā stundā spektri pastāstīja par zvaigznēm. "
                "Šodien tie paši spektri pastāstīs par visu Visumu.",
    uzdevumu_apraksts="Sarkanā nobīde un attālumi",
    teorija=[
        ("Visuma struktūra", [
            ("tabula",
             ["Mērogs", "Objekts", "Aptuvenais izmērs"],
             [["Zvaigžņu sistēma", "Saules sistēma", "Gaismas stundas"],
              ["Galaktika", "Piena Ceļš", "100 000 gaismas gadu"],
              ["Galaktiku kopa", "Vietējā kopa", "Miljoni gaismas gadu"],
              ["Novērojamais Visums", "Visas kopas", "Miljardi gaismas gadu"]],
             [3.20, 3.20, 3.83]),
            ("panelis", "SARKANĀ NOBĪDE",
             ["Tālu galaktiku spektros zināmās līnijas ir nobīdītas uz "
              "sarkano pusi - to viļņa garums ir lielāks, nekā izmērīts "
              "laboratorijā.",
              "To izskaidro ar galaktiku attālināšanos: jo tālāka "
              "galaktika, jo lielāka nobīde.",
              "Tas ir galvenais novērojums, uz kura balstās Visuma "
              "izplešanās modelis."], NAVY),
        ]),
        ("Izplešanās", [
            ("formula", "HABLA SAKARĪBA",
             "v = H·r        H ≈ 70 km/s uz megaparseku",
             "Galaktikas attālināšanās ātrums ir tieši proporcionāls "
             "attālumam līdz tai. Tas nozīmē, ka izplešas pati telpa - "
             "nevis galaktikas lido prom no viena centra.", GOLD),
            ("divi",
             ("KAS IR DATI", GREEN,
              ["Izmērītie spektri.",
               "Līniju nobīdes lielums.",
               "Attālumi līdz galaktikām.",
               "To var pārbaudīt",
               "atkārtoti."]),
             ("KAS IR INTERPRETĀCIJA", GOLD,
              ["Secinājums par izplešanos.",
               "Visuma vecuma novērtējums.",
               "Modeļi par nākotni.",
               "Tie balstās uz datiem,",
               "bet nav paši dati."])),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Ātrums no attāluma",
             teksts="Galaktika atrodas 100 Mpc attālumā.\n"
                    "Aprēķini tās attālināšanās ātrumu!\n"
                    "(H = 70 km/s uz Mpc)",
             dots=["r = 100 Mpc", "H = 70 km/s uz Mpc"],
             jaaprekina=["v = ?"],
             formulas=["v = H·r"],
             aprekins=["1)  v = 70 · 100",
                       "2)  v = 7000 km/s",
                       "3)  v = 7,0·10⁶ m/s"],
             atbilde="v = 7000 km/s",
             piezime="Tas ir apmēram 2 % no gaismas ātruma - un tomēr "
                     "galaktika ir salīdzinoši tuva."),
        dict(nr=2, virsraksts="Attālums no ātruma",
             teksts="Galaktikas attālināšanās ātrums ir 21 000 km/s.\n"
                    "Cik tālu tā atrodas? (H = 70 km/s uz Mpc)",
             dots=["v = 21 000 km/s", "H = 70 km/s uz Mpc"],
             jaaprekina=["r = ?"],
             formulas=["v = H·r", "r = v/H"],
             aprekins=["1)  r = 21 000 : 70",
                       "2)  r = 300 Mpc"],
             atbilde="r = 300 Mpc",
             piezime="Tieši tā astronomi nosaka attālumus līdz tālām "
                     "galaktikām - pēc sarkanās nobīdes."),
        dict(nr=3, virsraksts="Nobīde un virziens",
             teksts="Vienas galaktikas spektrā līnijas nobīdītas uz\n"
                    "sarkano pusi, citas - uz zilo.\n"
                    "Ko tas nozīmē par katras kustību?",
             dots=["1. galaktika: sarkanā nobīde",
                   "2. galaktika: zilā nobīde"],
             jaaprekina=["Kustības virziens = ?"],
             formulas=["Sarkanā nobīde - attālinās",
                       "Zilā nobīde - tuvojas"],
             aprekins=["1)  Sarkanā nobīde - viļņa garums lielāks",
                       "2)  Avots attālinās",
                       "3)  Zilā nobīde - avots tuvojas"],
             atbilde="Pirmā attālinās, otrā tuvojas",
             piezime="Andromedas galaktika tuvojas Piena Ceļam - tai "
                     "ir zilā nobīde."),
        dict(nr=4, virsraksts="Dati vai interpretācija",
             teksts="Nosaki, kas ir dati un kas interpretācija:\n"
                    "a) līnija nobīdīta par 5 nm; b) galaktika "
                    "attālinās;\nc) Visums izplešas jau 13,8 miljardus gadu.",
             dots=["a) izmērīta nobīde", "b) secinājums par kustību",
                   "c) secinājums par vecumu"],
             jaaprekina=["Dati vai interpretācija?"],
             formulas=["Dati - izmērīts",
                       "Interpretācija - izsecināts no modeļa"],
             aprekins=["1)  a) dati - tiešs mērījums",
                       "2)  b) interpretācija pēc Doplera efekta",
                       "3)  c) interpretācija pēc izplešanās modeļa"],
             atbilde="a) dati; b) un c) interpretācija",
             piezime="Interpretācija var mainīties, ja mainās modelis - "
                     "dati paliek."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Visums sastāv no galaktikām, kopām un to struktūrām.",
            "Tālu galaktiku spektros ir sarkanā nobīde.",
            "v = H·r - jo tālāk galaktika, jo ātrāk tā attālinās.",
            "Zinātnē nošķir datus no to interpretācijas.",
        ],
        majasdarbs=[
            "r = 50 Mpc, H = 70 km/s uz Mpc. Aprēķini v.",
            "v = 14 000 km/s. Aprēķini attālumu.",
            "Uzraksti pa vienam datu un interpretācijas piemēram.",
        ],
        pasvertejums=["Zinu Visuma struktūru",
                      "Saprotu sarkano nobīdi",
                      "Protu lietot Habla sakarību",
                      "Atšķiru datus no interpretācijas"],
        nakama="Nākamā stunda: kosmosa izpēte un informācijas avoti."),
),

dict(
    nr="14.10", virsraksts="Kosmosa izpēte un informācijas avoti",
    jautajums="Kā izvērtēt zinātnisku ziņu par kosmosu?",
    apaksraksts="Avots · Pierādījumi · Secinājums, nenoteiktība, "
                "spekulācija",
    merkis="Atrast apgalvojuma avotu un pierādījumus un nošķirt pamatotu "
           "secinājumu no nenoteiktības un spekulācijas.",
    protu=["nosaukt galvenos kosmosa izpētes veidus;",
           "atrast apgalvojuma avotu;",
           "novērtēt pierādījumu kvalitāti;",
           "atšķirt secinājumu no spekulācijas."],
    atkartojums="Visā tematā esam nošķīruši novēroto no izsecinātā. "
                "Šodien šo prasmi lietosim ziņām, ko lasām katru dienu.",
    uzdevumu_apraksts="Ziņu izvērtēšana un aprēķini",
    teorija=[
        ("Kā pēta kosmosu", [
            ("tabula",
             ["Metode", "Ko dod", "Ierobežojums"],
             [["Optiskie teleskopi", "Attēli redzamajā gaismā",
               "Traucē atmosfēra un mākoņi"],
              ["Kosmiskie teleskopi", "Attēli bez atmosfēras",
               "Ļoti dārgi"],
              ["Radioteleskopi", "Radioviļņu avoti", "Zema izšķirtspēja"],
              ["Kosmiskie zondi", "Tieši mērījumi uz vietas",
               "Ilgs lidojuma laiks"]],
             [3.20, 3.60, 3.43]),
            ("panelis", "KĀPĒC VAJAG DAŽĀDAS METODES",
             ["Katra spektra daļa pastāsta ko citu: radioviļņi - par "
              "gāzes mākoņiem, rentgens - par karstiem procesiem.",
              "Tāpēc vienu un to pašu objektu pēta vairākos viļņu garumu "
              "diapazonos.",
              "Secinājums ir daudz drošāks, ja to apstiprina vairākas "
              "neatkarīgas metodes."], NAVY),
        ]),
        ("Ziņas izvērtēšana", [
            ("divi",
             ("PAMATOTS SECINĀJUMS", GREEN,
              ["Norādīts avots un metode.",
               "Ir skaitļi un nenoteiktība.",
               "Rezultātu apstiprina citi.",
               "Piemērs: «Mērījumi rāda,",
               "ka ... ar 5 % kļūdu.»"]),
             ("SPEKULĀCIJA", RED,
              ["Avots nav norādīts.",
               "Nav skaitļu.",
               "Lieto vārdus «varētu",
               "nozīmēt», «zinātnieki",
               "šokēti».",
               "Nav pārbaudāms."])),
            ("panelis", "ČETRI JAUTĀJUMI KATRAI ZIŅAI",
             ["1. Kas ir avots - pētījums, aģentūra vai anonīms "
              "ieraksts?",
              "2. Kādi ir dati - kas tieši izmērīts un ar kādu metodi?",
              "3. Cik liela ir nenoteiktība - vai minēta kļūda?",
              "4. Vai secinājums tiešām izriet no datiem, vai tas ir "
              "pievienots virsraksta dēļ?"], GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Signāla ceļš līdz Marsam",
             teksts="Marss ir 2,3·10¹¹ m attālumā no Zemes.\n"
                    "Cik ilgi radio signāls iet turp un atpakaļ?\n"
                    "(c = 3,0·10⁸ m/s)",
             dots=["s = 2,3·10¹¹ m", "c = 3,0·10⁸ m/s"],
             jaaprekina=["t = ?"],
             formulas=["t = s/c", "Turp un atpakaļ: 2t"],
             aprekins=["1)  t = 2,3·10¹¹ : 3,0·10⁸ ≈ 767 s",
                       "2)  Turp un atpakaļ: 2 · 767 ≈ 1534 s",
                       "3)  Apmēram 26 minūtes"],
             atbilde="≈ 26 minūtes",
             piezime="Tāpēc marsohodus nevar vadīt tiešā laikā - tiem "
                     "vajag savu autonomiju."),
        dict(nr=2, virsraksts="Teleskopa izšķirtspēja",
             teksts="Divi teleskopi novēro vienu galaktiku: viens uz\n"
                    "Zemes, otrs orbītā. Kāpēc orbītā redzamība ir\n"
                    "labāka?",
             dots=["Teleskops uz Zemes",
                   "Teleskops orbītā"],
             jaaprekina=["Kāpēc atšķirība?"],
             formulas=["Atmosfēra izkliedē un absorbē gaismu"],
             aprekins=["1)  Atmosfēra izkliedē gaismu - attēls mirgo",
                       "2)  Daļu spektra atmosfēra absorbē",
                       "3)  Orbītā šo traucējumu nav"],
             atbilde="Orbītā netraucē atmosfēra",
             piezime="Tieši tāpēc kosmiskie teleskopi ir dārgi, bet "
                     "nepieciešami."),
        dict(nr=3, virsraksts="Izvērtē ziņu",
             teksts="Virsraksts: «Zinātnieki atklājuši dzīvību uz\n"
                    "eksoplanētas!» Tekstā: spektrā atrasta gāze, kas uz\n"
                    "Zemes rodas arī bioloģiski. Izvērtē virsrakstu!",
             dots=["Dati: gāze spektrā",
                   "Virsraksts: atklāta dzīvība"],
             jaaprekina=["Vai virsraksts pamatots?"],
             formulas=["Secinājumam jāizriet no datiem"],
             aprekins=["1)  Dati rāda tikai gāzes klātbūtni",
                       "2)  Gāze var rasties arī bez dzīvības",
                       "3)  Virsraksts iet tālāk par datiem"],
             atbilde="Virsraksts nav pamatots ar datiem",
             piezime="Tipiska kļūda ziņās: iespējamu skaidrojumu "
                     "pasniegt kā pierādītu faktu."),
        dict(nr=4, virsraksts="Cik gaismas gadu",
             teksts="Eksoplanēta atrodas 4,0·10¹⁷ m attālumā.\n"
                    "Cik tas ir gaismas gados un cik ilgi signāls\n"
                    "nāktu no turienes? (1 g.g. ≈ 9,5·10¹⁵ m)",
             dots=["s = 4,0·10¹⁷ m", "1 g.g. ≈ 9,5·10¹⁵ m"],
             jaaprekina=["Attālums = ?", "t = ?"],
             formulas=["n = s/(1 g.g.)"],
             aprekins=["1)  n = 4,0·10¹⁷ : 9,5·10¹⁵",
                       "2)  n ≈ 42 gaismas gadi",
                       "3)  Signāls nāktu 42 gadus"],
             atbilde="≈ 42 gaismas gadi",
             piezime="Attālums gaismas gados uzreiz pasaka arī signāla "
                     "ceļa laiku gados."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Kosmosu pēta ar teleskopiem dažādos viļņu garumos un ar "
            "zondēm.",
            "Drošs secinājums balstās uz vairākām neatkarīgām metodēm.",
            "Ziņai vienmēr jautā: avots, dati, nenoteiktība, secinājums.",
            "Spekulācijā nav ne skaitļu, ne pārbaudāma avota.",
        ],
        majasdarbs=[
            "s = 1,2·10¹² m. Cik ilgi iet signāls?",
            "Atrodi ziņu par kosmosu un atbildi uz četriem jautājumiem.",
            "Uzraksti, kā virsrakstu varētu formulēt precīzāk.",
        ],
        pasvertejums=["Zinu izpētes metodes",
                      "Protu atrast avotu",
                      "Protu novērtēt pierādījumus",
                      "Atšķiru secinājumu no spekulācijas"],
        nakama="Nākamā stunda: temata kopsavilkums pirms PD9."),
),

dict(
    nr="14.11", virsraksts="Atoma un Visuma kopsavilkums",
    jautajums="Kā savienot atoma un kosmosa pētījumus?",
    apaksraksts="Spektri · Enerģija · Novērojumi · Gatavošanās PD9",
    merkis="Ar īsu skaidrojumu sasaistīt spektrus, enerģiju un "
           "astronomijas novērojumus un labot būtiskākās kļūdas.",
    protu=["sasaistīt atoma un astronomijas jautājumus;",
           "izvēlēties pareizo sakarību;",
           "labot biežākās temata kļūdas;",
           "sagatavoties PD9."],
    atkartojums="Šī ir gan temata, gan visa kursa satura pēdējā jaunā "
                "stunda. PD9 vērtēs atoma, kodola un Visuma pamatidejas.",
    uzdevumu_apraksts="Kombinēti uzdevumi pirms PD9",
    teorija=[
        ("Kā viss saistās kopā", [
            ("panelis", "VIENS PAVEDIENS CAURI TEMATAM",
             ["Elektronu pārejas atomā rada spektra līnijas; tās pašas "
              "līnijas redzam zvaigžņu spektros.",
              "No līnijām nosaka sastāvu, no nepārtrauktā fona - "
              "temperatūru, no nobīdes - kustību.",
              "Tā atoma fizika kļūst par instrumentu, ar ko pētīt "
              "objektus miljardu gaismas gadu attālumā."], NAVY),
            ("tabula",
             ["Kad lietot", "Formula", "Ko pārbaudīt"],
             [["Fotona enerģija", "E = hf;  E = hc/λ", "λ metros"],
              ["Kodola sastāvs", "A = Z + N", "Z nosaka elementu"],
              ["Pussabrukšana", "N = N₀/2ⁿ", "n vesels skaitlis"],
              ["Kodolenerģija", "E = mc²", "Masa kilogramos"],
              ["Izplešanās", "v = H·r", "Attālums megaparsekos"]],
             [3.00, 3.60, 3.63]),
        ]),
        ("PD9 sagatavošanās", [
            ("divi",
             ("KAS BŪS PD9", BLUE,
              ["Atoma un kodola uzbūve.",
               "Spektru veidi.",
               "Pussabrukšanas aprēķins.",
               "Starojuma drošība.",
               "Apgalvojuma izvērtēšana."]),
             ("BIEŽĀKĀS KĻŪDAS", RED,
              ["Jauc Z un A.",
               "Gaismas gadu sauc par laiku.",
               "Jauc apstarošanu ar",
               "piesārņojumu.",
               "Neatšķir datus no",
               "interpretācijas."])),
            ("panelis", "PĒDĒJAIS PADOMS",
             ["Pakāpes rakstiet zinātniskajā pierakstā un pārbaudiet "
              "kārtu - šajā tematā skaitļi ir ļoti lieli un ļoti mazi.",
              "Skaidrojuma uzdevumos vispirms nosauc novēroto, tad "
              "secinājumu.",
              "Ja jautā par risku vai apgalvojumu, atbildē vienmēr min "
              "skaitli vai salīdzinājumu ar fonu."], GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="No spektra uz sastāvu",
             teksts="Zvaigznes spektrā līnija ir λ = 486 nm.\n"
                    "Aprēķini fotona enerģiju!\n"
                    "(h = 6,63·10⁻³⁴ J·s; c = 3,0·10⁸ m/s)",
             dots=["λ = 4,86·10⁻⁷ m", "h = 6,63·10⁻³⁴ J·s",
                   "c = 3,0·10⁸ m/s"],
             jaaprekina=["E = ?"],
             formulas=["E = hc/λ"],
             aprekins=["1)  hc ≈ 1,99·10⁻²⁵",
                       "2)  E = 1,99·10⁻²⁵ : 4,86·10⁻⁷",
                       "3)  E ≈ 4,1·10⁻¹⁹ J"],
             atbilde="E ≈ 4,1·10⁻¹⁹ J",
             piezime="486 nm ir ūdeņraža zilā līnija - viena no "
                     "biežāk izmantotajām astronomijā."),
        dict(nr=2, virsraksts="Kodols un pussabrukšana",
             teksts="Izotopam A = 90, Z = 38, pussabrukšanas periods\n"
                    "29 gadi. Cik neitronu kodolā un cik vielas paliks\n"
                    "pēc 58 gadiem?",
             dots=["A = 90", "Z = 38", "T = 29 gadi", "t = 58 gadi"],
             jaaprekina=["N = ?", "Daļa = ?"],
             formulas=["N = A − Z", "n = t/T", "N = N₀/2ⁿ"],
             aprekins=["1)  N = 90 − 38 = 52 neitroni",
                       "2)  n = 58 : 29 = 2",
                       "3)  Paliek ceturtā daļa jeb 25 %"],
             atbilde="52 neitroni;  paliek 25 %",
             piezime="Tas ir stroncijs-90 - viens no bīstamākajiem "
                     "avāriju izotopiem."),
        dict(nr=3, virsraksts="Enerģija no masas",
             teksts="Kodolreakcijā pazūd 4,0·10⁻⁴ kg masas.\n"
                    "Aprēķini atbrīvoto enerģiju! (c = 3,0·10⁸ m/s)",
             dots=["m = 4,0·10⁻⁴ kg", "c = 3,0·10⁸ m/s"],
             jaaprekina=["E = ?"],
             formulas=["E = mc²"],
             aprekins=["1)  c² = 9,0·10¹⁶",
                       "2)  E = 4,0·10⁻⁴ · 9,0·10¹⁶",
                       "3)  E = 3,6·10¹³ J"],
             atbilde="E = 3,6·10¹³ J",
             piezime="Tas ir apmēram tikpat, cik saražo Latvijas "
                       "elektrostacijas dažās stundās."),
        dict(nr=4, virsraksts="Izvērtē apgalvojumu",
             teksts="Apgalvojums: «Datortomogrāfija ir bīstama, jo deva\n"
                    "ir 10 mSv.» Salīdzini ar dabisko fonu (2,5 mSv\n"
                    "gadā) un izvērtē!",
             dots=["D = 10 mSv", "Fons = 2,5 mSv gadā"],
             jaaprekina=["Cik gadu fons?"],
             formulas=["n = D/D(fons)"],
             aprekins=["1)  n = 10 : 2,5 = 4",
                       "2)  Deva atbilst 4 gadu dabiskajam fonam",
                       "3)  Tā nav niecīga, bet nav arī akūti bīstama"],
             atbilde="Deva ≈ 4 gadu fons",
             piezime="Pareizā atbilde nav «bīstami» vai «nav "
                     "bīstami» - tā ir salīdzinājums ar skaitli."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Atoma spektri ir instruments visa Visuma pētīšanai.",
            "Temata formulas: E = hf, A = Z + N, N = N₀/2ⁿ, E = mc², "
            "v = H·r.",
            "Devu vienmēr salīdzina ar dabisko fonu.",
            "Zinātniskā atbilde balstās uz datiem un skaitļiem.",
        ],
        majasdarbs=[
            "Atkārto 14.1.-14.10. stundas kopsavilkumus.",
            "A = 137, Z = 55. Aprēķini N.",
            "Sagatavo formulu lapu PD9.",
        ],
        pasvertejums=["Saprotu temata kopsakarības",
                      "Protu izvēlēties formulu",
                      "Zinu biežākās kļūdas",
                      "Esmu gatavs PD9"],
        nakama="Nākamā stunda: PD9 - atoms un Visums."),
),

]
