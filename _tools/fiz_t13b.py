# -*- coding: utf-8 -*-
"""13. temats. B daļa: 13.6.-13.10. stunda.

13.8. ir formatīvs praktiskais darbs; tā mērījumus izmanto 13.9. stundā.
13.10. ir pēdējā mācību stunda pirms PD8.
"""

from fiz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN     # noqa: F401
from fiz_t13a import TEMATS, KICKER, KURSS, MAPE              # noqa: F401

STUNDAS = [

dict(
    nr="13.6", virsraksts="Lēcas un attēli",
    jautajums="Kā lēca veido attēlu?",
    apaksraksts="Savācējlēca · f = ab/(a + b) · Γ = b/a",
    merkis="Konstruēt attēlu savācējlēcā, atšķirt īstu attēlu no "
           "šķietama un lietot lēcas formulu.",
    protu=["atšķirt savācējlēcu no izkliedētājlēcas;",
           "konstruēt attēlu ar diviem stariem;",
           "atšķirt īstu attēlu no šķietama;",
           "lietot lēcas formulu un palielinājumu."],
    atkartojums="Iepriekšējās stundās gaisma lūza uz vienas robežas. "
                "Lēcā tā lūst divreiz - un tieši tāpēc stari savācas "
                "vienā punktā.",
    uzdevumu_apraksts="Lēcas formula un palielinājums",
    teorija=[
        ("Lēcas pamatlielumi", [
            ("formula", "LĒCAS FORMULA UN PALIELINĀJUMS",
             "f = ab/(a + b)        D = 1/f        Γ = b/a",
             "a ir attālums no priekšmeta līdz lēcai, b - no lēcas līdz "
             "attēlam, f - fokusa attālums. To pašu sakarību raksta arī "
             "kā apgriezto vērtību summu. Optisko stiprumu D mēra "
             "dioptrijās.", GOLD),
            ("divi",
             ("SAVĀCĒJLĒCA", GREEN,
              ["Vidū biezāka.",
               "Savāc starus fokusā.",
               "f > 0;  D > 0.",
               "Veido īstu vai šķietamu",
               "attēlu."]),
             ("IZKLIEDĒTĀJLĒCA", BLUE,
              ["Vidū plānāka.",
               "Izkliedē starus.",
               "f < 0;  D < 0.",
               "Vienmēr veido šķietamu",
               "samazinātu attēlu."])),
        ]),
        ("Attēla veidi savācējlēcā", [
            ("tabula",
             ["Priekšmeta vieta", "Attēls", "Kur izmanto"],
             [["a > 2f", "Īsts, apgriezts, samazināts", "Fotoaparāts"],
              ["a = 2f", "Īsts, apgriezts, vienāds", "Kopēšana"],
              ["f < a < 2f", "Īsts, apgriezts, palielināts", "Projektors"],
              ["a < f", "Šķietams, tiešs, palielināts", "Lupa"]],
             [2.90, 4.40, 2.93]),
            ("panelis", "KĀ KONSTRUĒ ATTĒLU",
             ["1. Stars, kas iet paralēli optiskajai asij, pēc lēcas iet "
              "caur fokusu.",
              "2. Stars, kas iet caur lēcas centru, virzienu nemaina.",
              "3. Kur šie divi stari krustojas, tur ir attēla punkts; ja "
              "krustojas tikai to pagarinājumi, attēls ir šķietams.",
              "Īstu attēlu var uztvert uz ekrāna, šķietamu - nevar."],
             NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Fokusa attālums",
             teksts="Priekšmets ir 0,30 m no lēcas, ass attēls veidojas\n"
                    "0,60 m aiz lēcas. Aprēķini fokusa attālumu!",
             dots=["a = 0,30 m", "b = 0,60 m"],
             jaaprekina=["f = ?"],
             formulas=["f = ab/(a + b)"],
             aprekins=["1)  ab = 0,30 · 0,60 = 0,18",
                       "2)  a + b = 0,90",
                       "3)  f = 0,18 : 0,90 = 0,20 m"],
             atbilde="f = 0,20 m",
             piezime="Pārbaude: fokusa attālums vienmēr ir mazāks par "
                     "abiem attālumiem a un b."),
        dict(nr=2, virsraksts="Optiskais stiprums",
             teksts="Aprēķini iepriekšējās lēcas optisko stiprumu!",
             dots=["f = 0,20 m"],
             jaaprekina=["D = ?"],
             formulas=["D = 1/f"],
             aprekins=["1)  D = 1 : 0,20",
                       "2)  D = 5,0 dioptrijas"],
             atbilde="D = 5,0 dpt",
             piezime="Dioptrija ir viens dalīts ar metru - tāpēc f "
                     "vienmēr izsaka metros."),
        dict(nr=3, virsraksts="Palielinājums",
             teksts="Priekšmets ir 0,30 m no lēcas, attēls 0,60 m aiz\n"
                    "tās. Priekšmeta augstums ir 4,0 cm.\n"
                    "Aprēķini palielinājumu un attēla augstumu!",
             dots=["a = 0,30 m", "b = 0,60 m", "h = 4,0 cm"],
             jaaprekina=["Γ = ?", "H = ?"],
             formulas=["Γ = b/a", "H = Γ · h"],
             aprekins=["1)  Γ = 0,60 : 0,30 = 2,0",
                       "2)  H = 2,0 · 4,0",
                       "3)  H = 8,0 cm"],
             atbilde="Γ = 2,0;  H = 8,0 cm",
             piezime="Attēls ir divreiz lielāks un apgriezts - tāds ir "
                     "projektora režīms."),
        dict(nr=4, virsraksts="Kur veidosies attēls",
             teksts="Lēcai f = 0,10 m, priekšmets ir 0,15 m no tās.\n"
                    "Aprēķini attālumu līdz attēlam!",
             dots=["f = 0,10 m", "a = 0,15 m"],
             jaaprekina=["b = ?"],
             formulas=["f = ab/(a + b)", "b = af/(a − f)"],
             aprekins=["1)  a − f = 0,15 − 0,10 = 0,05",
                       "2)  af = 0,15 · 0,10 = 0,015",
                       "3)  b = 0,015 : 0,05 = 0,30 m"],
             atbilde="b = 0,30 m",
             piezime="Priekšmets starp f un 2f - attēls īsts, apgriezts "
                     "un palielināts."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Savācējlēca savāc starus, izkliedētājlēca tos izkliedē.",
            "f = ab/(a + b);  D = 1/f;  Γ = b/a.",
            "Īstu attēlu var uztvert uz ekrāna, šķietamu - nevar.",
            "Attēla veids atkarīgs no priekšmeta attāluma pret f un 2f.",
        ],
        majasdarbs=[
            "a = 0,40 m, b = 0,40 m. Aprēķini f un Γ.",
            "f = 0,25 m. Aprēķini optisko stiprumu.",
            "Uzzīmē attēla konstrukciju, ja a = 3f.",
        ],
        pasvertejums=["Atšķiru lēcu veidus",
                      "Protu konstruēt attēlu",
                      "Protu lietot lēcas formulu",
                      "Protu rēķināt palielinājumu"],
        nakama="Nākamā stunda: acs, brilles un fotoaparāts."),
),

dict(
    nr="13.7", virsraksts="Acs, brilles un fotoaparāts",
    jautajums="Kā koriģē redzes defektus un fokusē attēlu?",
    apaksraksts="Acs kā optiska sistēma · Tuvredzība un tālredzība · "
                "Fokusēšana",
    merkis="Skaidrot acs un fotoaparāta darbību un pamatot lēcas izvēli "
           "redzes korekcijai.",
    protu=["nosaukt acs optiskās daļas;",
           "izskaidrot, kā acs fokusē attēlu;",
           "atšķirt tuvredzību no tālredzības;",
           "pamatot savācēj- vai izkliedētājlēcas izvēli."],
    atkartojums="Iepriekšējā stundā lēca veidoja attēlu uz ekrāna. Acī "
                "«ekrāns» ir tīklene, bet fotoaparātā - matrica.",
    uzdevumu_apraksts="Redzes korekcija un fokusēšana",
    teorija=[
        ("Acs kā optiska sistēma", [
            ("tabula",
             ["Acs daļa", "Ko dara", "Analogs fotoaparātā"],
             [["Radzene un lēca", "Lauž gaismu", "Objektīvs"],
              ["Varavīksnene", "Regulē gaismas daudzumu", "Diafragma"],
              ["Tīklene", "Uztver attēlu", "Matrica"],
              ["Redzes nervs", "Nodod signālu", "Procesors"]],
             [3.20, 3.60, 3.43]),
            ("panelis", "KĀ ACS FOKUSĒ",
             ["Acī attālums līdz tīklenei ir nemainīgs, tāpēc fokusēšanu "
              "panāk, MAINOT LĒCAS FORMU - to sauc par akomodāciju.",
              "Fotoaparātā otrādi: lēcas forma nemainās, bet objektīvu "
              "pavirza tuvāk vai tālāk no matricas.",
              "Attēls uz tīklenes ir īsts, apgriezts un samazināts; smadzenes "
              "to «apgriež» atpakaļ."], NAVY),
        ]),
        ("Redzes defekti", [
            ("divi",
             ("TUVREDZĪBA", BLUE,
              ["Attēls veidojas PRIEKŠĀ",
               "tīklenei.",
               "Tālu neredz skaidri.",
               "Acs ābols par garu.",
               "Koriģē ar",
               "IZKLIEDĒTĀJLĒCU (D < 0)."]),
             ("TĀLREDZĪBA", GOLD,
              ["Attēls veidojas AIZ",
               "tīklenes.",
               "Tuvu neredz skaidri.",
               "Acs ābols par īsu.",
               "Koriģē ar",
               "SAVĀCĒJLĒCU (D > 0)."])),
            ("panelis", "KĀ NOLASĪT RECEPTI",
             ["Briļļu receptē optiskais stiprums norādīts dioptrijās: "
              "−2,5 dpt nozīmē izkliedētājlēcu tuvredzībai.",
              "Pozitīvs skaitlis, piemēram +1,5 dpt, ir savācējlēca "
              "tālredzībai.",
              "Jo lielāks skaitlis, jo stiprāka lēca un jo lielāka "
              "korekcija."], GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Briļļu optiskais stiprums",
             teksts="Brillēm fokusa attālums ir 0,50 m (savācējlēca).\n"
                    "Aprēķini optisko stiprumu un nosaki, kādu defektu\n"
                    "tās koriģē!",
             dots=["f = 0,50 m", "Savācējlēca"],
             jaaprekina=["D = ?"],
             formulas=["D = 1/f"],
             aprekins=["1)  D = 1 : 0,50",
                       "2)  D = +2,0 dpt",
                       "3)  Pozitīvs - koriģē tālredzību"],
             atbilde="D = +2,0 dpt - tālredzība",
             piezime="Zīme uzreiz pasaka lēcas veidu un defektu."),
        dict(nr=2, virsraksts="Tuvredzības brilles",
             teksts="Receptē norādīts −2,5 dpt.\n"
                    "Aprēķini fokusa attālumu un nosaki lēcas veidu!",
             dots=["D = −2,5 dpt"],
             jaaprekina=["f = ?"],
             formulas=["D = 1/f", "f = 1/D"],
             aprekins=["1)  f = 1 : (−2,5)",
                       "2)  f = −0,40 m",
                       "3)  Negatīvs - izkliedētājlēca"],
             atbilde="f = −0,40 m - izkliedētājlēca",
             piezime="Negatīvs fokusa attālums nozīmē, ka fokuss ir "
                     "šķietams."),
        dict(nr=3, virsraksts="Attēls uz matricas",
             teksts="Fotoaparāta objektīvam f = 0,050 m, priekšmets\n"
                    "atrodas 2,0 m attālumā. Cik tālu no objektīva\n"
                    "jābūt matricai?",
             dots=["f = 0,050 m", "a = 2,0 m"],
             jaaprekina=["b = ?"],
             formulas=["b = af/(a − f)"],
             aprekins=["1)  a − f = 2,0 − 0,050 = 1,95",
                       "2)  af = 2,0 · 0,050 = 0,10",
                       "3)  b = 0,10 : 1,95 ≈ 0,051 m"],
             atbilde="b ≈ 0,051 m = 51 mm",
             piezime="Attēls veidojas gandrīz tieši fokusā - tāpēc "
                     "tāliem objektiem objektīvu gandrīz nekustina."),
        dict(nr=4, virsraksts="Attēla izmērs",
             teksts="Tajā pašā fotoaparātā fotografē 1,7 m garu cilvēku\n"
                    "no 2,0 m. Cik liels būs attēls uz matricas?\n"
                    "(b ≈ 0,051 m)",
             dots=["a = 2,0 m", "b = 0,051 m", "h = 1,7 m"],
             jaaprekina=["H = ?"],
             formulas=["Γ = b/a", "H = Γ · h"],
             aprekins=["1)  Γ = 0,051 : 2,0 ≈ 0,0255",
                       "2)  H = 0,0255 · 1,7",
                       "3)  H ≈ 0,043 m = 43 mm"],
             atbilde="H ≈ 43 mm",
             piezime="Matrica ir apmēram 24 mm augsta - tātad cilvēks "
                     "kadrā neietilptu, jāatkāpjas tālāk."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Acs fokusē, mainot lēcas formu; fotoaparāts - pārvietojot "
            "objektīvu.",
            "Attēls uz tīklenes ir īsts, apgriezts un samazināts.",
            "Tuvredzību koriģē ar izkliedētājlēcu (D < 0).",
            "Tālredzību koriģē ar savācējlēcu (D > 0).",
        ],
        majasdarbs=[
            "D = +1,5 dpt. Aprēķini f un nosaki defektu.",
            "f = −0,25 m. Aprēķini D.",
            "Paskaidro atšķirību starp acs un fotoaparāta fokusēšanu.",
        ],
        pasvertejums=["Zinu acs optiskās daļas",
                      "Zinu, kā acs fokusē",
                      "Atšķiru redzes defektus",
                      "Protu izvēlēties lēcu"],
        nakama="Nākamā stunda: praktiskais darbs - attēls lēcā."),
),

dict(
    nr="13.8", virsraksts="Praktiskais darbs: attēls lēcā",
    jautajums="Kā iegūt asu attēlu uz ekrāna?",
    apaksraksts="Mērījumi a un b · Fokusa attālums · Formatīvs darbs",
    merkis="Iegūt asu attēlu uz ekrāna, mainot attālumus, un noteikt "
           "aptuvenu fokusa attālumu.",
    protu=["saslēgt optisko soliņu ar avotu, lēcu un ekrānu;",
           "iegūt asu attēlu;",
           "izmērīt attālumus a un b;",
           "aprēķināt fokusa attālumu no mērījumiem."],
    atkartojums="Divās iepriekšējās stundās lēcas formulu lietojām "
                "aprēķinos. Šodien to pārbaudīsim ar mērījumiem - "
                "mērījumus saglabā nākamajai stundai.",
    uzdevumu_apraksts="Mērījumu plānošana un fokusa attāluma aprēķins",
    teorija=[
        ("Darba gaita", [
            ("panelis", "KĀ IEGŪT ASU ATTĒLU",
             ["1. Uz optiskā soliņa novieto gaismas avotu (svecīti vai "
              "spuldzīti ar figūru), lēcu un ekrānu vienā līnijā.",
              "2. Priekšmetu novieto tālāk par 2f; ekrānu pārvieto, līdz "
              "attēls ir viskrasākais.",
              "3. Izmēra a un b; atkārto vēl trīs reizes ar citu a.",
              "4. Katrai rindai aprēķina f un salīdzina rezultātus."],
             NAVY),
            ("tabula",
             ["Mērījums", "a (m)", "b (m)", "f = ab/(a + b)"],
             [["1.", "", "", ""],
              ["2.", "", "", ""],
              ["3.", "", "", ""],
              ["4.", "", "", ""]],
             [2.60, 3.00, 3.00, 3.63]),
        ]),
        ("Precizitāte un drošība", [
            ("divi",
             ("KĀ UZLABOT PRECIZITĀTI", GREEN,
              ["Ekrānu virza uz priekšu",
               "un atpakaļ, meklējot",
               "asuma vidu.",
               "Attālumus mēra no lēcas",
               "vidus.",
               "Katru mērījumu atkārto."]),
             ("KĻŪDU AVOTI", RED,
              ["Asuma robeža ir plata -",
               "grūti noteikt centru.",
               "Lēca nav perpendikulāra",
               "asij.",
               "Priekšmets, lēca un ekrāns",
               "nav vienā līnijā."])),
            ("panelis", "DROŠĪBA UN PIEZĪMES",
             ["Ja izmanto svecīti, mati un piedurknes jāsavāc; blakus "
              "jābūt paliktnim.",
              "Spuldzīte pēc darba ir karsta - to netaustām uzreiz.",
              "Mērījumus pieraksta tabulā un SAGLABĀ - nākamajā stundā "
              "tos analizēsim."], RED),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Fokusa attālums no mērījuma",
             teksts="Mērījumā a = 0,40 m un b = 0,24 m.\n"
                    "Aprēķini fokusa attālumu!",
             dots=["a = 0,40 m", "b = 0,24 m"],
             jaaprekina=["f = ?"],
             formulas=["f = ab/(a + b)"],
             aprekins=["1)  ab = 0,40 · 0,24 = 0,096",
                       "2)  a + b = 0,64",
                       "3)  f = 0,096 : 0,64 = 0,15 m"],
             atbilde="f = 0,15 m",
             piezime="Pārbaude: f ir mazāks par abiem attālumiem - kā "
                     "jābūt."),
        dict(nr=2, virsraksts="Otrs mērījums",
             teksts="Otrā mērījumā a = 0,50 m un b = 0,21 m.\n"
                    "Aprēķini f un salīdzini ar pirmo (0,15 m)!",
             dots=["a = 0,50 m", "b = 0,21 m", "f₁ = 0,15 m"],
             jaaprekina=["f₂ = ?"],
             formulas=["f = ab/(a + b)"],
             aprekins=["1)  ab = 0,50 · 0,21 = 0,105",
                       "2)  a + b = 0,71",
                       "3)  f₂ = 0,105 : 0,71 ≈ 0,148 m"],
             atbilde="f₂ ≈ 0,15 m",
             piezime="Abi rezultāti sakrīt - lēcas fokusa attālums "
                     "nemainās, tā ir lēcas īpašība."),
        dict(nr=3, virsraksts="Palielinājums mērījumā",
             teksts="Pirmajā mērījumā a = 0,40 m, b = 0,24 m, priekšmeta\n"
                    "augstums 3,0 cm. Aprēķini palielinājumu un attēla\n"
                    "augstumu!",
             dots=["a = 0,40 m", "b = 0,24 m", "h = 3,0 cm"],
             jaaprekina=["Γ = ?", "H = ?"],
             formulas=["Γ = b/a", "H = Γ · h"],
             aprekins=["1)  Γ = 0,24 : 0,40 = 0,60",
                       "2)  H = 0,60 · 3,0",
                       "3)  H = 1,8 cm"],
             atbilde="Γ = 0,60;  H = 1,8 cm",
             piezime="Γ < 1 nozīmē samazinātu attēlu - priekšmets bija "
                     "tālāk par 2f."),
        dict(nr=4, virsraksts="Vidējais rezultāts",
             teksts="Četros mērījumos ieguva f = 0,150; 0,148; 0,153 un\n"
                    "0,149 m. Aprēķini vidējo vērtību!",
             dots=["f₁ = 0,150 m", "f₂ = 0,148 m",
                   "f₃ = 0,153 m", "f₄ = 0,149 m"],
             jaaprekina=["f(vid.) = ?"],
             formulas=["f(vid.) = summa/4"],
             aprekins=["1)  Summa = 0,600 m",
                       "2)  f(vid.) = 0,600 : 4",
                       "3)  f(vid.) = 0,150 m"],
             atbilde="f(vid.) = 0,150 m",
             piezime="Vairāki mērījumi un vidējā vērtība vienmēr ir "
                     "precīzāki nekā viens mērījums."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Asu attēlu meklē, pārvietojot ekrānu.",
            "No a un b aprēķina fokusa attālumu.",
            "Fokusa attālums ir lēcas īpašība - visos mērījumos vienāds.",
            "Vairāku mērījumu vidējā vērtība ir precīzāka.",
        ],
        majasdarbs=[
            "a = 0,60 m, b = 0,20 m. Aprēķini f un Γ.",
            "Pieraksti savus četrus mērījumus tabulā.",
            "Aprēķini savu vidējo fokusa attālumu.",
        ],
        pasvertejums=["Protu saslēgt optisko soliņu",
                      "Protu iegūt asu attēlu",
                      "Protu izmērīt a un b",
                      "Protu aprēķināt f"],
        nakama="Nākamā stunda: lēcas pētījuma datu analīze."),
),

dict(
    nr="13.9", virsraksts="Lēcas pētījuma datu analīze",
    jautajums="Vai staru shēma atbilst novērojumam?",
    apaksraksts="f un Γ no mērījumiem · Salīdzinājums ar shēmu · Kļūdas",
    merkis="Pēc saglabātajiem mērījumiem aprēķināt fokusa attālumu un "
           "palielinājumu, salīdzināt ar staru shēmu un izvērtēt kļūdas.",
    protu=["aprēķināt f un Γ no visiem mērījumiem;",
           "salīdzināt aprēķinu ar staru shēmu;",
           "novērtēt relatīvo novirzi;",
           "nosaukt kļūdu avotus."],
    atkartojums="Iepriekšējā stundā ieguvām mērījumus. Šodien "
                "pārbaudīsim, vai tie sakrīt ar teoriju - un cik lielas "
                "ir novirzes.",
    uzdevumu_apraksts="Mērījumu apstrāde un vērtēšana",
    teorija=[
        ("Kā apstrādā datus", [
            ("panelis", "TRĪS SOĻI",
             ["1. Katrai rindai aprēķina f pēc formulas un pieraksta "
              "tabulā.",
              "2. Aprēķina vidējo vērtību un salīdzina ar lēcas "
              "nominālo fokusa attālumu, ja tas zināms.",
              "3. Aprēķina relatīvo novirzi procentos un nosauc "
              "iespējamos kļūdu cēloņus."], NAVY),
            ("tabula",
             ["Pārbaude", "Kas jāsanāk", "Ja nesanāk"],
             [["f visos mērījumos", "Gandrīz vienāds", "Mērīts no citas vietas"],
              ["f pret a un b", "Mazāks par abiem", "Kļūda formulā"],
              ["Γ, ja a > 2f", "Mazāks par 1", "Sajaukts a ar b"],
              ["Attēls uz ekrāna", "Vienmēr apgriezts", "Nav īstais attēls"]],
             [3.20, 3.20, 3.83]),
        ]),
        ("Kļūdu avoti", [
            ("divi",
             ("SISTEMĀTISKĀS", RED,
              ["Attālumus mēra no lēcas",
               "rāmja, nevis vidus.",
               "Lineāls nolasīts no",
               "cita gala.",
               "Vienmēr novirza uz",
               "vienu pusi."]),
             ("NEJAUŠĀS", GOLD,
              ["Asuma vietu katrs",
               "nosaka nedaudz citādi.",
               "Ekrāns nav precīzi",
               "perpendikulārs.",
               "Novirza uz abām pusēm -",
               "vidējā vērtība palīdz."])),
            ("panelis", "SECINĀJUMA PIERAKSTS",
             ["Secinājumā min skaitli: «Vidējais fokusa attālums ir "
              "0,150 m, kas no nominālā 0,15 m atšķiras par mazāk nekā "
              "1 %.»",
              "Norādi galveno kļūdu avotu un to, kā to varētu samazināt.",
              "Salīdzini ar staru shēmu: vai attēla veids (īsts, "
              "apgriezts, samazināts) sakrita ar novēroto."], GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Fokusa attālums no datiem",
             teksts="Mērījumā a = 0,45 m, b = 0,225 m.\n"
                    "Aprēķini f un Γ!",
             dots=["a = 0,45 m", "b = 0,225 m"],
             jaaprekina=["f = ?", "Γ = ?"],
             formulas=["f = ab/(a + b)", "Γ = b/a"],
             aprekins=["1)  ab = 0,45 · 0,225 = 0,10125",
                       "2)  f = 0,10125 : 0,675 = 0,15 m",
                       "3)  Γ = 0,225 : 0,45 = 0,50"],
             atbilde="f = 0,15 m;  Γ = 0,50",
             piezime="Γ = 0,5 nozīmē divreiz samazinātu apgrieztu "
                     "attēlu."),
        dict(nr=2, virsraksts="Relatīvā novirze",
             teksts="Izmērītais f = 0,153 m, lēcas nominālais f = 0,150 m.\n"
                    "Aprēķini relatīvo novirzi procentos!",
             dots=["f(izm.) = 0,153 m", "f(nom.) = 0,150 m"],
             jaaprekina=["δ = ?"],
             formulas=["Δf = f(izm.) − f(nom.)", "δ = Δf/f"],
             aprekins=["1)  Δf = 0,153 − 0,150 = 0,003 m",
                       "2)  δ = 0,003 : 0,150 = 0,02",
                       "3)  δ = 2 %"],
             atbilde="δ = 2 %",
             piezime="Divi procenti optiskajā soliņā ir labs "
                     "rezultāts."),
        dict(nr=3, virsraksts="Vai dati saskan",
             teksts="Skolēns ieguva f = 0,15 m, bet vienā mērījumā\n"
                    "a = 0,10 m un attēls uz ekrāna neveidojās.\n"
                    "Paskaidro, kāpēc!",
             dots=["f = 0,15 m", "a = 0,10 m",
                   "Attēls neveidojas"],
             jaaprekina=["Kāpēc?"],
             formulas=["Ja a < f, attēls ir šķietams",
                       "Šķietamu attēlu uz ekrāna neuztver"],
             aprekins=["1)  a = 0,10 m < f = 0,15 m",
                       "2)  Lēca darbojas kā lupa",
                       "3)  Attēls šķietams - uz ekrāna to nav"],
             atbilde="Priekšmets bija tuvāk par fokusu",
             piezime="Tas nav mērījuma kļūda, bet fizikāls "
                     "likumsakarīgums."),
        dict(nr=4, virsraksts="Salīdzinājums ar shēmu",
             teksts="Mērījumā a = 0,20 m, f = 0,15 m. Aprēķini b un Γ un\n"
                    "nosaki, kāds attēls jāgaida pēc staru shēmas!",
             dots=["a = 0,20 m", "f = 0,15 m"],
             jaaprekina=["b = ?", "Γ = ?"],
             formulas=["b = af/(a − f)", "Γ = b/a"],
             aprekins=["1)  a − f = 0,05;  af = 0,03",
                       "2)  b = 0,03 : 0,05 = 0,60 m",
                       "3)  Γ = 0,60 : 0,20 = 3,0"],
             atbilde="b = 0,60 m;  Γ = 3,0",
             piezime="f < a < 2f - attēls īsts, apgriezts un "
                     "palielināts; tieši tā rāda arī staru shēma."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Katram mērījumam aprēķina f un salīdzina rezultātus.",
            "Relatīvā novirze parāda mērījuma kvalitāti.",
            "Sistemātiskās kļūdas novirza uz vienu pusi, nejaušās - uz "
            "abām.",
            "Aprēķinam un staru shēmai jādod viens un tas pats attēla "
            "veids.",
        ],
        majasdarbs=[
            "a = 0,35 m, b = 0,26 m. Aprēķini f un Γ.",
            "f(izm.) = 0,148 m, f(nom.) = 0,150 m. Aprēķini novirzi.",
            "Uzraksti sava pētījuma secinājumu ar skaitli.",
        ],
        pasvertejums=["Protu apstrādāt datus",
                      "Protu rēķināt novirzi",
                      "Zinu kļūdu veidus",
                      "Protu salīdzināt ar shēmu"],
        nakama="Nākamā stunda: optikas nostiprināšana pirms PD8."),
),

dict(
    nr="13.10", virsraksts="Optikas nostiprināšana",
    jautajums="Kā izvēlēties pareizu staru shēmu?",
    apaksraksts="Staru zīmējumi · Lēcas un palielinājums · Gatavošanās PD8",
    merkis="Lasīt un labot staru zīmējumus un risināt lēcas vai "
           "palielinājuma uzdevumus.",
    protu=["atrast kļūdu staru zīmējumā;",
           "izvēlēties pareizo sakarību;",
           "risināt kombinētus optikas uzdevumus;",
           "sagatavoties PD8."],
    atkartojums="Šī ir temata pēdējā mācību stunda. PD8 prasīs skaidrot "
                "atstarošanos un laušanu, konstruēt attēlu un saistīt "
                "optiku ar redzi.",
    uzdevumu_apraksts="Kombinēti uzdevumi pirms PD8",
    teorija=[
        ("Temata formulu karte", [
            ("tabula",
             ["Kad lietot", "Formula", "Ko pārbaudīt"],
             [["Apgaismojums", "E = I/r²", "Attālums metros"],
              ["Atstarošanās", "α = β", "Leņķi no normāles"],
              ["Laušana", "n = sin α/sin β;  v = c/n", "Uz kuru pusi lūst"],
              ["Robežleņķis", "sin α₀ = 1/n", "No blīvākas uz retāku"],
              ["Lēca", "f = ab/(a + b);  Γ = b/a", "f mazāks par a un b"]],
             [3.00, 3.80, 3.43]),
            ("panelis", "BIEŽĀKĀS KĻŪDAS ZĪMĒJUMOS",
             ["Leņķus mēra no virsmas, nevis no normāles - tā ir "
              "biežākā kļūda visā tematā.",
              "Staru caur lēcas centru zīmē lauztu; patiesībā tas "
              "virzienu nemaina.",
              "Šķietamu attēlu zīmē ar nepārtrauktu līniju; tas vienmēr "
              "jāzīmē punktēti."], RED),
        ]),
        ("PD8 sagatavošanās", [
            ("divi",
             ("KAS BŪS PD8", BLUE,
              ["Atstarošanās un laušanas",
               "skaidrojums.",
               "Staru gaitas zīmējums.",
               "Attēla konstrukcija lēcā.",
               "Aprēķins ar lēcas formulu.",
               "Saistība ar redzi."]),
             ("KĀ SAGATAVOTIES", GREEN,
              ["Uzzīmē visus četrus lēcas",
               "gadījumus pēc atmiņas.",
               "Atkārto, kad attēls ir",
               "īsts un kad šķietams.",
               "Izrēķini pa vienam",
               "uzdevumam no katra veida."])),
            ("panelis", "PĒDĒJAIS PADOMS",
             ["Zīmējumā vispirms atzīmē fokusus abās lēcas pusēs un "
              "attālumu 2f - tad attēla veids ir redzams uzreiz.",
              "Aprēķinā pēc katras darbības pārbaudi, vai f ir mazāks "
              "par a un b.",
              "Skaidrojumos lieto terminus: normāle, krišanas leņķis, "
              "laušanas koeficients, īsts un šķietams attēls."], GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Laušana un ātrums",
             teksts="Stars no gaisa ieiet vidē, kurā gaismas ātrums ir\n"
                    "2,0·10⁸ m/s. Aprēķini laušanas koeficientu un\n"
                    "robežleņķa sinusu! (c = 3,0·10⁸ m/s)",
             dots=["v = 2,0·10⁸ m/s", "c = 3,0·10⁸ m/s"],
             jaaprekina=["n = ?", "sin α₀ = ?"],
             formulas=["n = c/v", "sin α₀ = 1/n"],
             aprekins=["1)  n = 3,0·10⁸ : 2,0·10⁸ = 1,50",
                       "2)  sin α₀ = 1 : 1,50",
                       "3)  sin α₀ ≈ 0,67"],
             atbilde="n = 1,50;  sin α₀ ≈ 0,67",
             piezime="Tie ir stikla parametri - divi soļi no viena "
                     "dotā lieluma."),
        dict(nr=2, virsraksts="Lēca un attēls",
             teksts="Lēcai f = 0,20 m, priekšmets ir 0,60 m attālumā,\n"
                    "augstums 5,0 cm. Aprēķini b, Γ un attēla augstumu!",
             dots=["f = 0,20 m", "a = 0,60 m", "h = 5,0 cm"],
             jaaprekina=["b = ?", "Γ = ?", "H = ?"],
             formulas=["b = af/(a − f)", "Γ = b/a", "H = Γ · h"],
             aprekins=["1)  b = 0,60 · 0,20 : 0,40 = 0,30 m",
                       "2)  Γ = 0,30 : 0,60 = 0,50",
                       "3)  H = 0,50 · 5,0 = 2,5 cm"],
             atbilde="b = 0,30 m;  Γ = 0,50;  H = 2,5 cm",
             piezime="a > 2f - attēls īsts, apgriezts un samazināts, kā "
                     "arī sanāca."),
        dict(nr=3, virsraksts="Apgaismojums un attālums",
             teksts="Lampa 2,0 m attālumā dod 50 lx.\n"
                    "Cik būs, ja to pietuvina līdz 1,0 m?",
             dots=["E₁ = 50 lx", "r₁ = 2,0 m", "r₂ = 1,0 m"],
             jaaprekina=["E₂ = ?"],
             formulas=["E = I/r²", "E ~ 1/r²"],
             aprekins=["1)  Attālums samazināts 2 reizes",
                       "2)  Apgaismojums aug 2² = 4 reizes",
                       "3)  E₂ = 50 · 4 = 200 lx"],
             atbilde="E₂ = 200 lx",
             piezime="Kvadrāta likumu var lietot arī bez gaismas "
                     "stipruma - tikai ar attiecību."),
        dict(nr=4, virsraksts="Atrodi kļūdu zīmējumā",
             teksts="Skolēns uzzīmēja: stars caur lēcas centru lūst uz\n"
                    "leju, bet šķietamo attēlu attēloja ar nepārtrauktu\n"
                    "līniju. Atrodi abas kļūdas!",
             dots=["Stars caur centru lūzis",
                   "Šķietams attēls ar pilnu līniju"],
             jaaprekina=["Kļūdas = ?"],
             formulas=["Stars caur centru virzienu nemaina",
                       "Šķietamu attēlu zīmē punktēti"],
             aprekins=["1)  Stars caur optisko centru iet taisni",
                       "2)  Šķietamā attēla stari ir tikai pagarinājumi",
                       "3)  Tos zīmē ar punktētu līniju"],
             atbilde="Divas kļūdas: lauzts centrālais stars un pilna "
                     "līnija",
             piezime="Abas kļūdas PD8 maksā punktus - pat ja aprēķins "
                     "ir pareizs."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Temata sakarības: E = I/r², α = β, n = sin α/sin β, "
            "sin α₀ = 1/n, f = ab/(a + b).",
            "Leņķus vienmēr mēra no normāles.",
            "Stars caur lēcas centru virzienu nemaina.",
            "Šķietamu attēlu zīmē ar punktētu līniju.",
        ],
        majasdarbs=[
            "Atkārto 13.1.-13.9. stundas kopsavilkumus.",
            "f = 0,10 m, a = 0,30 m, h = 6,0 cm. Aprēķini b, Γ un H.",
            "Sagatavo formulu lapu PD8.",
        ],
        pasvertejums=["Protu atrast kļūdu zīmējumā",
                      "Protu izvēlēties formulu",
                      "Protu risināt kombinētus uzdevumus",
                      "Esmu gatavs PD8"],
        nakama="Nākamā stunda: PD8 - apgaismojums un attēli."),
),

]
