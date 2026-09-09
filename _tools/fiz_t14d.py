# -*- coding: utf-8 -*-
"""Gada noslēguma bloks: gatavošanās eksāmenam (14.12.-14.15. stunda).

Plānā (fiz_plan_11.py NOSL) šīs ir četras stundas pēc PD9. Faili glabājas
14. temata mapē, jo tā ir mācību gada pēdējā tematiskā mape.
"""

from fiz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN     # noqa: F401
from fiz_t14a import KURSS, MAPE                              # noqa: F401

TEMATS = "Gatavošanās eksāmenam"
KICKER = "FIZIKA I · 11. KLASE · GATAVOŠANĀS EKSĀMENAM"

STUNDAS = [

dict(
    nr="14.12", virsraksts="Eksāmena 1. daļa",
    jautajums="Kā ātri izvēlēties pareizo atbildi?",
    apaksraksts="24 jautājumi 40 minūtēs · Izslēgšanas metode · Tipiskās "
                "kļūdas",
    merkis="Trenēt eksāmena 1. daļas formātu un analizēt tipiskās izvēles "
           "kļūdas.",
    protu=["plānot laiku 1. daļai;",
           "lietot izslēgšanas metodi;",
           "pārbaudīt atbildi ar mērvienībām;",
           "atpazīt tipiskās izvēles kļūdas."],
    atkartojums="Divu gadu saturs ir apgūts. Tagad mācāmies to lietot "
                "eksāmena formātā - un pirmā daļa prasa nevis garus "
                "aprēķinus, bet ātrumu un precizitāti.",
    uzdevumu_apraksts="Izvēles jautājumu risināšana",
    teorija=[
        ("1. daļas formāts", [
            ("panelis", "24 JAUTĀJUMI 40 MINŪTĒS",
             ["Vidēji viens jautājums minūtē un vēl 16 minūtes rezervē "
              "grūtākajiem un pārbaudei.",
              "Vispirms izpilda visus, ko zini uzreiz; grūtos atzīmē un "
              "atgriezies pie tiem vēlāk.",
              "Neatstāj nevienu tukšu - par nepareizu atbildi punktus "
              "neatņem."], NAVY),
            ("kartitas", [
                ("IZSLĒGŠANA", BLUE,
                 ["Svītro acīmredzami",
                  "nepareizās.",
                  "Bieži paliek divas -",
                  "izvēle kļūst vienkārša."]),
                ("MĒRVIENĪBAS", GREEN,
                 ["Pārbaudi atbildes",
                  "mērvienību.",
                  "Nepareiza vienība nozīmē",
                  "nepareizu atbildi."]),
                ("KĀRTA", GOLD,
                 ["Novērtē skaitļa kārtu.",
                  "Vai atbilde ir",
                  "saprātīgā mērogā?"]),
            ]),
        ]),
        ("Tipiskās izvēles kļūdas", [
            ("tabula",
             ["Kļūda", "Kā izpaužas", "Kā izvairīties"],
             [["Nelasa līdz galam", "Izvēlas pirmo derīgo",
               "Izlasa visus variantus"],
              ["Jauc lielumus", "Masa un svars, ceļš un pārvietojums",
               "Pasvītro doto"],
              ["Neievēro «nav pareizi»", "Meklē pareizo apgalvojumu",
               "Aplūko jautājuma formu"],
              ["Steidzas pēdējās minūtēs", "Atstāj tukšas atbildes",
               "Atstāj 5 min rezervē"]],
             [3.00, 4.00, 3.23]),
            ("panelis", "PĒDĒJĀS PIECAS MINŪTES",
             ["Pārbaudi, vai visas atbildes ir ierakstītas atbilžu lapā, "
              "nevis tikai uzdevumu burtnīcā.",
              "Pārliecinies, ka numuri nav nobīdījušies - viena nobīde "
              "sabojā visas nākamās atbildes.",
              "Neko nemaini bez iemesla: pirmā izvēle biežāk ir pareiza "
              "nekā pārdomātā, ja nav jauna argumenta."], RED),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Ātrā izvēle ar mērvienībām",
             teksts="Kura atbilde nevar būt pareiza jautājumā par jaudu:\n"
                    "A) 60 W;  B) 1,5 kW;  C) 12 J;  D) 800 W?\n"
                    "Pamato bez aprēķina!",
             dots=["Jautājums par jaudu", "[P] = vats"],
             jaaprekina=["Kura nederīga?"],
             formulas=["P = A/t", "[P] = W"],
             aprekins=["1)  Jaudu mēra vatos",
                       "2)  C variantā ir džouli - enerģijas vienība",
                       "3)  C nevar būt pareiza"],
             atbilde="C - nepareiza mērvienība",
             piezime="Mērvienību pārbaude bieži izslēdz vienu vai divus "
                     "variantus bez aprēķina."),
        dict(nr=2, virsraksts="Kārtas novērtējums",
             teksts="Mājas spuldzei pie 230 V un R = 500 Ω strāva ir:\n"
                    "A) 0,46 A;  B) 4,6 A;  C) 46 A;  D) 460 A.\n"
                    "Izvēlies un pamato!",
             dots=["U = 230 V", "R = 500 Ω"],
             jaaprekina=["I = ?"],
             formulas=["I = U/R"],
             aprekins=["1)  I = 230 : 500",
                       "2)  I = 0,46 A",
                       "3)  Pārējie varianti pārsniegtu drošinātāju"],
             atbilde="A) 0,46 A",
             piezime="Mājas ķēdē 16 A ir robeža - viss lielākais uzreiz "
                     "izslēdzams."),
        dict(nr=3, virsraksts="Izslēgšanas metode",
             teksts="Ķermenis kustas vienmērīgi pa apli. Kurš apgalvojums\n"
                    "ir pareizs? A) ātrums nemainās; B) paātrinājums ir\n"
                    "nulle; C) kopspēks ir nulle; D) paātrinājums vērsts\n"
                    "uz centru.",
             dots=["Vienmērīga kustība pa riņķa līniju"],
             jaaprekina=["Pareizais apgalvojums?"],
             formulas=["Centrtieces paātrinājums vērsts uz centru"],
             aprekins=["1)  A nepareizs - virziens mainās",
                       "2)  B un C nepareizi - ir centrtieces paātrinājums",
                       "3)  Paliek D"],
             atbilde="D - paātrinājums vērsts uz centru",
             piezime="Trīs varianti izslēgti ar vienu argumentu - "
                     "kustības virziens mainās."),
        dict(nr=4, virsraksts="Laika plānošana",
             teksts="1. daļā ir 24 jautājumi un 40 minūtes.\n"
                    "Cik laika vidēji vienam jautājumam un cik paliek\n"
                    "rezervē, ja 18 atbild pa 1 minūtei?",
             dots=["24 jautājumi", "t = 40 min",
                   "18 jautājumi pa 1 min"],
             jaaprekina=["Vidēji = ?", "Rezerve = ?"],
             formulas=["Vidēji = t/n"],
             aprekins=["1)  Vidēji: 40 : 24 ≈ 1,7 min",
                       "2)  18 · 1 = 18 min",
                       "3)  Paliek 22 min sešiem grūtākajiem"],
             atbilde="≈ 1,7 min vidēji;  22 min rezervē",
             piezime="Ātri atbildot uz zināmajiem, grūtajiem paliek "
                     "gandrīz 4 minūtes katram."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "1. daļā ir 24 jautājumi 40 minūtēs.",
            "Vispirms atbild uz zināmajiem, grūtos atstāj vēlākam.",
            "Izslēgšanas metode un mērvienības atrisina daudz jautājumu.",
            "Tukšas atbildes neatstāj.",
        ],
        majasdarbs=[
            "Izpildi vienu eksāmena parauga 1. daļu ar pulksteni.",
            "Pieraksti, kuros jautājumos kļūdījies un kāpēc.",
            "Atkārto tos tematus, kuros bija visvairāk kļūdu.",
        ],
        pasvertejums=["Protu plānot laiku",
                      "Protu lietot izslēgšanu",
                      "Pārbaudu mērvienības",
                      "Zinu tipiskās kļūdas"],
        nakama="Nākamā stunda: eksāmena 2. daļa - īsās atbildes."),
),

dict(
    nr="14.13", virsraksts="Eksāmena 2. daļa: īsās atbildes",
    jautajums="Kā uzrakstīt atbildi bez risinājuma?",
    apaksraksts="Mērvienības · Grafika nolasīšana · Jēdziena nosaukšana",
    merkis="Trenēt īso atbilžu uzdevumus: mērvienības, grafiku "
           "nolasīšanu un jēdzienu nosaukšanu.",
    protu=["nosaukt lielumu mērvienības;",
           "nolasīt vērtību no grafika;",
           "nosaukt jēdzienu pēc apraksta;",
           "uzrakstīt īsu, precīzu atbildi."],
    atkartojums="Iepriekšējā stundā trenējām izvēles jautājumus. Īsajās "
                "atbildēs risinājums nav jāraksta, bet atbildei jābūt "
                "precīzai - arī mērvienībā.",
    uzdevumu_apraksts="Īso atbilžu treniņš",
    teorija=[
        ("Ko prasa īsās atbildes", [
            ("tabula",
             ["Uzdevuma veids", "Ko raksta", "Biežākā kļūda"],
             [["Nosauc mērvienību", "Vienu vārdu vai simbolu",
               "Sajauc J un W"],
              ["Nolasi no grafika", "Skaitli ar mērvienību",
               "Aizmirst mērvienību"],
              ["Nosauc jēdzienu", "Terminu, ne skaidrojumu",
               "Raksta veselu teikumu"],
              ["Viena darbība", "Rezultātu ar mērvienību",
               "Neveic pārrēķinu"]],
             [3.20, 3.60, 3.43]),
            ("panelis", "ATBILDES PIERAKSTS",
             ["Atbild tieši uz jautājumu: ja prasa mērvienību, raksta "
              "mērvienību, nevis formulu.",
              "Skaitlisku atbildi vienmēr raksta ar mērvienību - bez tās "
              "punktu nedod.",
              "Ja atbilde ir termins, pietiek ar vienu vārdu; garš "
              "teikums tikai palielina kļūdas iespēju."], NAVY),
        ]),
        ("Kursa mērvienības", [
            ("tabula",
             ["Lielums", "Simbols", "Mērvienība"],
             [["Spēks", "F", "ņūtons (N)"],
              ["Darbs un enerģija", "A, E", "džouls (J)"],
              ["Jauda", "P", "vats (W)"],
              ["Spriegums", "U", "volts (V)"],
              ["Magnētiskā indukcija", "B", "tesla (T)"]],
             [4.00, 2.20, 4.03]),
            ("panelis", "GRAFIKU NOLASĪŠANA",
             ["Vispirms izlasi asu apzīmējumus un mērvienības - tikai tad "
              "meklē vērtību.",
              "Slīpums bieži ir atsevišķs lielums: v(t) grafikā tas ir "
              "paātrinājums, s(t) grafikā - ātrums.",
              "Laukums zem grafika arī ir lielums: v(t) grafikā tas ir "
              "ceļš."], GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Mērvienības",
             teksts="Nosauc mērvienības: a) jaudai; b) magnētiskajai\n"
                    "indukcijai; c) vielas daudzumam; d) apgaismojumam.",
             dots=["a) jauda", "b) magnētiskā indukcija",
                   "c) vielas daudzums", "d) apgaismojums"],
             jaaprekina=["Mērvienības = ?"],
             formulas=["Katram lielumam sava SI vienība"],
             aprekins=["1)  a) vats (W);  b) tesla (T)",
                       "2)  c) mols (mol)",
                       "3)  d) lukss (lx)"],
             atbilde="W;  T;  mol;  lx",
             piezime="Mērvienību sarakstu vērts pārrakstīt uz vienas "
                     "lapas un atkārtot pirms eksāmena."),
        dict(nr=2, virsraksts="Nolasīšana no grafika",
             teksts="v(t) grafikā ātrums 4 sekundēs pieaug no 2 m/s\n"
                    "līdz 10 m/s. Nosaki paātrinājumu un veikto ceļu!",
             dots=["v₁ = 2 m/s", "v₂ = 10 m/s", "t = 4 s"],
             jaaprekina=["a = ?", "s = ?"],
             formulas=["a = Δv/t", "s = (v₁ + v₂)t/2"],
             aprekins=["1)  Δv = 8 m/s;  a = 8 : 4 = 2 m/s²",
                       "2)  Vidējais ātrums: (2 + 10) : 2 = 6 m/s",
                       "3)  s = 6 · 4 = 24 m"],
             atbilde="a = 2 m/s²;  s = 24 m",
             piezime="Slīpums dod paātrinājumu, laukums zem līnijas - "
                     "ceļu."),
        dict(nr=3, virsraksts="Nosauc jēdzienu",
             teksts="Nosauc jēdzienu: a) enerģija, kas piemīt kustīgam\n"
                    "ķermenim; b) laiks, kurā sabrūk puse kodolu;\n"
                    "c) attālums starp diviem viļņa kalniem.",
             dots=["a) kustīga ķermeņa enerģija",
                   "b) puse kodolu sabrūk",
                   "c) starp diviem kalniem"],
             jaaprekina=["Jēdzieni = ?"],
             formulas=["Atbild ar terminu, ne skaidrojumu"],
             aprekins=["1)  a) kinētiskā enerģija",
                       "2)  b) pussabrukšanas periods",
                       "3)  c) viļņa garums"],
             atbilde="Kinētiskā enerģija; pussabrukšanas periods; viļņa "
                     "garums",
             piezime="Viens termins ir pilnvērtīga atbilde - garāks "
                     "teikums punktus nepievieno."),
        dict(nr=4, virsraksts="Viena darbība ar pārrēķinu",
             teksts="Ierīces jauda ir 1,5 kW, tā strādā 20 minūtes.\n"
                    "Cik enerģijas tā patērē kilovatstundās?",
             dots=["P = 1,5 kW", "t = 20 min"],
             jaaprekina=["E = ?"],
             formulas=["E = Pt", "t stundās"],
             aprekins=["1)  t = 20 : 60 ≈ 0,33 h",
                       "2)  E = 1,5 · 0,33",
                       "3)  E ≈ 0,50 kWh"],
             atbilde="E ≈ 0,50 kWh",
             piezime="Bez minūšu pārrēķina stundās atbilde būtu 30 "
                     "reižu par lielu."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Īsajā atbildē raksta tieši to, ko prasa jautājums.",
            "Skaitliskai atbildei vienmēr pievieno mērvienību.",
            "Grafikā slīpums un laukums ir atsevišķi lielumi.",
            "Jēdziena nosaukšanai pietiek ar terminu.",
        ],
        majasdarbs=[
            "Uzraksti 15 kursa lielumu mērvienības no galvas.",
            "Izpildi vienu eksāmena parauga īso atbilžu daļu.",
            "Pārbaudi, cik reizes aizmirsi mērvienību.",
        ],
        pasvertejums=["Zinu mērvienības",
                      "Protu nolasīt grafiku",
                      "Protu nosaukt jēdzienus",
                      "Rakstu īsi un precīzi"],
        nakama="Nākamā stunda: eksāmena 2. daļa - pilni risinājumi."),
),

dict(
    nr="14.14", virsraksts="Eksāmena 2. daļa: risinājumi",
    jautajums="Kā pierakstīt pilnu risinājumu?",
    apaksraksts="Dots → Jāaprēķina → Formulas → Aprēķins → Atbilde",
    merkis="Pierakstīt risinājumu latviešu standartā un vērtēt to pēc "
           "eksāmena kritērijiem.",
    protu=["pierakstīt risinājumu pilnā formā;",
           "izcelt katru vērtējamo soli;",
           "pārbaudīt mērvienības un ticamību;",
           "novērtēt savu risinājumu pēc kritērijiem."],
    atkartojums="Visu divu gadu garumā uzdevumus risinājām tieši šajā "
                "formā. Eksāmenā par katru soli ir atsevišķi punkti - "
                "arī tad, ja gala atbilde ir kļūdaina.",
    uzdevumu_apraksts="Pilna risinājuma pieraksts",
    teorija=[
        ("Risinājuma struktūra", [
            ("tabula",
             ["Solis", "Ko raksta", "Par ko dod punktus"],
             [["Dots", "Lielumi ar mērvienībām", "Pareizs pārrēķins SI"],
              ["Jāaprēķina", "Meklētais lielums", "Saprasts uzdevums"],
              ["Formulas", "Vispārīgā formā", "Pareiza sakarība"],
              ["Aprēķins", "Skaitļi pa soļiem", "Pareiza darbība"],
              ["Atbilde", "Rezultāts ar mērvienību", "Precīza atbilde"]],
             [2.60, 3.60, 4.03]),
            ("panelis", "KĀPĒC KATRS SOLIS IR SVARĪGS",
             ["Vērtētājs punktus liek par soļiem, ne tikai par gala "
              "skaitli: pareiza formula dod punktu arī tad, ja tālāk ir "
              "rēķina kļūda.",
              "Ja risinājums ir tikai skaitļu virkne bez formulām, lielāko "
              "daļu punktu zaudē.",
              "Tāpēc pat tad, ja uzdevumu nepabeidz, pieraksta doto un "
              "formulas."], NAVY),
        ]),
        ("Pašvērtējums pēc kritērijiem", [
            ("divi",
             ("PILNS PUNKTU SKAITS", GREEN,
              ["Visi lielumi SI vienībās.",
               "Formulas vispārīgā formā.",
               "Aprēķins pa soļiem.",
               "Atbilde ar mērvienību.",
               "Rezultāts saprātīgi",
               "noapaļots."]),
             ("BIEŽĀKIE ZAUDĒJUMI", RED,
              ["Nav pārrēķinātas vienības.",
               "Formula uzreiz ar skaitļiem.",
               "Trūkst mērvienības atbildē.",
               "Atbilde nav izcelta.",
               "Nav pārbaudīta ticamība."])),
            ("panelis", "PĒDĒJĀ PĀRBAUDE PIRMS NODOŠANAS",
             ["Vai katram uzdevumam ir skaidri redzama atbilde ar "
              "mērvienību?",
              "Vai skaitļu kārtas ir saprātīgas - vai atbilde atbilst "
              "reālai situācijai?",
              "Vai visi uzdevumi ir vismaz iesākti? Nepabeigts risinājums "
              "dod vairāk punktu nekā tukša lapa."], GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Mehānikas uzdevums",
             teksts="Ķermenis ar masu 4,0 kg no miera stāvokļa 5,0 s\n"
                    "laikā sasniedz ātrumu 20 m/s.\n"
                    "Aprēķini paātrinājumu un kopspēku!",
             dots=["m = 4,0 kg", "v₀ = 0", "v = 20 m/s", "t = 5,0 s"],
             jaaprekina=["a = ?", "F = ?"],
             formulas=["a = Δv/t", "F = ma"],
             aprekins=["1)  a = 20 : 5,0 = 4,0 m/s²",
                       "2)  F = 4,0 · 4,0",
                       "3)  F = 16 N"],
             atbilde="a = 4,0 m/s²;  F = 16 N",
             piezime="Divi lielumi - divas formulas; katra dod savu "
                     "punktu."),
        dict(nr=2, virsraksts="Siltuma uzdevums",
             teksts="Cik siltuma vajag, lai 1,5 kg ūdens sasildītu no\n"
                    "15 °C līdz 100 °C? (c = 4200 J/(kg·K))",
             dots=["m = 1,5 kg", "t₁ = 15 °C", "t₂ = 100 °C",
                   "c = 4200 J/(kg·K)"],
             jaaprekina=["Q = ?"],
             formulas=["Q = cmΔT", "ΔT = t₂ − t₁"],
             aprekins=["1)  ΔT = 100 − 15 = 85 K",
                       "2)  Q = 4200 · 1,5 · 85",
                       "3)  Q = 535 500 J ≈ 5,4·10⁵ J"],
             atbilde="Q ≈ 5,4·10⁵ J",
             piezime="Noapaļošana zinātniskajā pierakstā ir daļa no "
                     "pareizas atbildes."),
        dict(nr=3, virsraksts="Elektrības uzdevums",
             teksts="Ierīce pie 230 V patērē 3,0 A.\n"
                    "Aprēķini pretestību, jaudu un patēriņu 2 stundās!",
             dots=["U = 230 V", "I = 3,0 A", "t = 2 h"],
             jaaprekina=["R = ?", "P = ?", "E = ?"],
             formulas=["R = U/I", "P = UI", "E = Pt"],
             aprekins=["1)  R = 230 : 3,0 ≈ 77 Ω",
                       "2)  P = 230 · 3,0 = 690 W = 0,69 kW",
                       "3)  E = 0,69 · 2 = 1,38 kWh"],
             atbilde="R ≈ 77 Ω;  P = 690 W;  E ≈ 1,4 kWh",
             piezime="Trīs jautājumi - trīs atbildes, katra ar savu "
                     "mērvienību."),
        dict(nr=4, virsraksts="Novērtē risinājumu",
             teksts="Skolēns rakstīja: «230 : 500 = 0,46». Nosauc, kas\n"
                    "šajā pierakstā trūkst, lai iegūtu pilnu punktu\n"
                    "skaitu!",
             dots=["Ir tikai viena darbība",
                   "Nav formulas un mērvienību"],
             jaaprekina=["Kā trūkst?"],
             formulas=["Dots → Jāaprēķina → Formulas → Aprēķins → Atbilde"],
             aprekins=["1)  Trūkst dotā ar mērvienībām",
                       "2)  Trūkst formulas I = U/R",
                       "3)  Trūkst atbildes ar mērvienību: I = 0,46 A"],
             atbilde="Trūkst dotā, formulas un mērvienības",
             piezime="Skaitlis bija pareizs, bet punktu skaits būtu "
                     "aptuveni puse no iespējamā."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Risinājumu pieraksta piecos soļos.",
            "Punktus dod par katru soli atsevišķi.",
            "Formulu vispirms raksta vispārīgā formā.",
            "Nepabeigts risinājums ir vērtīgāks par tukšu lapu.",
        ],
        majasdarbs=[
            "Izpildi divus eksāmena parauga 2. daļas uzdevumus pilnā "
            "formā.",
            "Novērtē savu risinājumu pēc pieciem soļiem.",
            "Pieraksti, kurš solis tev visbiežāk pietrūkst.",
        ],
        pasvertejums=["Zinu risinājuma struktūru",
                      "Rakstu formulas vispārīgi",
                      "Pievienoju mērvienības",
                      "Protu novērtēt savu darbu"],
        nakama="Nākamā stunda: gada noslēgums un atkārtošanas plāns."),
),

dict(
    nr="14.15", virsraksts="Gada noslēgums",
    jautajums="Kas jāatkārto pirms eksāmena?",
    apaksraksts="Divu gadu saturs · Atgādne · Personīgs plāns",
    merkis="Apkopot divu gadu saturu vienā atgādnē, novērtēt savu "
           "sniegumu un ieplānot atkārtošanu.",
    protu=["nosaukt visu 14 tematu galvenās idejas;",
           "izveidot personīgu formulu atgādni;",
           "novērtēt savas stiprās un vājās puses;",
           "sastādīt atkārtošanas plānu."],
    atkartojums="Divos gados esam izgājuši ceļu no vienmērīgas kustības "
                "līdz Visuma izplešanās modelim. Šodien to saliksim "
                "vienā kartē.",
    uzdevumu_apraksts="Pašvērtējums un atkārtošanas plāns",
    teorija=[
        ("Divu gadu karte", [
            ("tabula",
             ["Bloks", "Temati", "Galvenās sakarības"],
             [["Mehānika", "1.-5.", "v = s/t;  F = ma;  A = Fs;  E = mv²/2"],
              ["Viļņi un siltums", "6.-8.", "v = λf;  Q = cmΔT;  Q = ΔU + A"],
              ["Elektrība", "9.-11.", "I = U/R;  P = UI;  U₁/U₂ = N₁/N₂"],
              ["Optika un atoms", "12.-14.", "c = λf;  E = hf;  A = Z + N"]],
             [2.60, 2.20, 6.43]),
            ("panelis", "KO EKSĀMENĀ PRASA VISBIEŽĀK",
             ["Grafiku lasīšana - kustības, siltuma, elektrības un viļņu "
              "grafiki visos tematos.",
              "Mērvienību pārrēķins un ticamības novērtējums - tas dod "
              "punktus katrā uzdevumā.",
              "Datu un secinājuma nošķiršana - prasme, ko trenējām no "
              "1. temata līdz pēdējam."], NAVY),
        ]),
        ("Atkārtošanas plāns", [
            ("divi",
             ("KĀ ATKĀRTOT EFEKTĪVI", GREEN,
              ["Risini uzdevumus, nevis",
               "tikai lasi konspektu.",
               "Sāc ar vājākajiem tematiem.",
               "Katru dienu pa nedaudz,",
               "nevis viss pēdējā vakarā.",
               "Pārbaudi sevi bez atgādnes."]),
             ("KĀ NEATKĀRTOT", RED,
              ["Pārlasīt visu pēc kārtas.",
               "Atkārtot tikai to, ko jau",
               "labi proti.",
               "Mācīties pēdējā naktī.",
               "Skatīties atrisinājumu,",
               "pirms pats mēģināji."])),
            ("panelis", "PERSONĪGĀ ATGĀDNE",
             ["Uz vienas A4 lapas uzraksti katra bloka galvenās formulas "
              "un to lietošanas nosacījumus.",
              "Blakus katrai formulai pieraksti vienu tipisku uzdevumu, "
              "kurā to lieto.",
              "Šo lapu pārraksti pats - pārrakstīšana iemāca labāk nekā "
              "gatavas atgādnes lasīšana."], GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Kombinēts mehānikas uzdevums",
             teksts="Ķermenis ar masu 2,0 kg krīt no 5,0 m augstuma.\n"
                    "Aprēķini potenciālo enerģiju un ātrumu tieši pirms\n"
                    "zemes! (g = 9,8 m/s²)",
             dots=["m = 2,0 kg", "h = 5,0 m", "g = 9,8 m/s²"],
             jaaprekina=["Ep = ?", "v = ?"],
             formulas=["Ep = mgh", "Ep = Ek", "Ek = mv²/2"],
             aprekins=["1)  Ep = 2,0 · 9,8 · 5,0 = 98 J",
                       "2)  v² = 2 · 9,8 · 5,0 = 98",
                       "3)  v ≈ 9,9 m/s"],
             atbilde="Ep = 98 J;  v ≈ 9,9 m/s",
             piezime="Enerģijas nezūdamība savieno divus tematus - tieši "
                     "tādi ir eksāmena uzdevumi."),
        dict(nr=2, virsraksts="Kombinēts elektrības uzdevums",
             teksts="Sildītājs ar pretestību 50 Ω pieslēgts 230 V.\n"
                    "Cik ilgi tas sildīs 2,0 kg ūdens par 30 K?\n"
                    "(c = 4200 J/(kg·K))",
             dots=["R = 50 Ω", "U = 230 V", "m = 2,0 kg", "ΔT = 30 K"],
             jaaprekina=["t = ?"],
             formulas=["P = U²/R", "Q = cmΔT", "t = Q/P"],
             aprekins=["1)  P = 52 900 : 50 = 1058 W",
                       "2)  Q = 4200 · 2,0 · 30 = 252 000 J",
                       "3)  t = 252 000 : 1058 ≈ 238 s ≈ 4,0 min"],
             atbilde="t ≈ 240 s ≈ 4,0 min",
             piezime="Trīs temati vienā uzdevumā: elektrība, jauda un "
                     "siltums."),
        dict(nr=3, virsraksts="Kombinēts viļņu uzdevums",
             teksts="Radiostacija raida ar frekvenci 90 MHz.\n"
                    "Aprēķini viļņa garumu un fotona enerģiju!\n"
                    "(c = 3,0·10⁸ m/s; h = 6,63·10⁻³⁴ J·s)",
             dots=["f = 9,0·10⁷ Hz", "c = 3,0·10⁸ m/s",
                   "h = 6,63·10⁻³⁴ J·s"],
             jaaprekina=["λ = ?", "E = ?"],
             formulas=["λ = c/f", "E = hf"],
             aprekins=["1)  λ = 3,0·10⁸ : 9,0·10⁷ ≈ 3,3 m",
                       "2)  E = 6,63·10⁻³⁴ · 9,0·10⁷",
                       "3)  E ≈ 6,0·10⁻²⁶ J"],
             atbilde="λ ≈ 3,3 m;  E ≈ 6,0·10⁻²⁶ J",
             piezime="Fotona enerģija ir niecīga - tāpēc radioviļņi ir "
                     "nejonizējoši."),
        dict(nr=4, virsraksts="Personīgais plāns",
             teksts="Novērtē katru bloku no 1 līdz 4 un izvēlies divus\n"
                    "vājākos. Cik uzdevumu izpildīsi katrā līdz\n"
                    "eksāmenam?",
             dots=["Četri bloki", "Vērtējums 1-4",
                   "Laiks līdz eksāmenam"],
             jaaprekina=["Plāns = ?"],
             formulas=["Sāc ar vājāko bloku",
                       "Regulāri, nevis vienā vakarā"],
             aprekins=["1)  Novērtē visus četrus blokus",
                       "2)  Izvēlies divus ar zemāko vērtējumu",
                       "3)  Katram - vismaz 10 uzdevumi"],
             atbilde="Personīgs pašvērtējums un konkrēts plāns",
             piezime="Divi bloki pa 10 uzdevumiem ir reāls plāns - un ar "
                     "to pietiek, lai jūtami uzlabotu rezultātu."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Divu gadu saturs ir četri bloki: mehānika, viļņi un "
            "siltums, elektrība, optika un atoms.",
            "Eksāmenā visbiežāk prasa grafikus, mērvienības un "
            "pamatojumu.",
            "Efektīva atkārtošana nozīmē uzdevumu risināšanu, ne "
            "pārlasīšanu.",
            "Personīgā atgādne jāraksta pašam.",
        ],
        majasdarbs=[
            "Uzraksti savu A4 atgādni ar visu četru bloku formulām.",
            "Pabeidz pašvērtējumu un atkārtošanas plānu.",
            "Izpildi vienu pilnu eksāmena paraugu ar pulksteni.",
        ],
        pasvertejums=["Zinu visu bloku galvenās idejas",
                      "Man ir sava atgādne",
                      "Esmu novērtējis savas prasmes",
                      "Man ir atkārtošanas plāns"],
        nakama="Veiksmi eksāmenā - un paldies par divu gadu darbu!"),
),

]
