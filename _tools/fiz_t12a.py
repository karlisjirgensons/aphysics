# -*- coding: utf-8 -*-
"""12. temats "Elektromagnētiskie viļņi". A daļa: 12.1.-12.4. stunda."""

from fiz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN     # noqa: F401

TEMATS = "12. temats. Elektromagnētiskie viļņi"
KICKER = "FIZIKA I · 11. KLASE · 12. TEMATS: ELEKTROMAGNĒTISKIE VIĻŅI"
KURSS = "FIZIKA I · 11. KLASE"
MAPE = "C:/aphysics/Fizika_1/12. Elektromagnētiskie viļņi"

STUNDAS = [

dict(
    nr="12.1", virsraksts="EM viļņi un svārstību kontūrs",
    jautajums="Kā signāls pārvietojas bez vada?",
    apaksraksts="Mainīgi lauki · Svārstību kontūrs · c = λf",
    merkis="Skaidrot mainīga elektriskā un magnētiskā lauka saistību, "
           "atpazīt enerģijas maiņu svārstību kontūrā un lietot c = λf.",
    protu=["izskaidrot, kā rodas elektromagnētiskais vilnis;",
           "nosaukt EM viļņa īpašības;",
           "izskaidrot enerģijas maiņu svārstību kontūrā;",
           "lietot c = λf."],
    atkartojums="11. tematā mainīgs magnētiskais lauks radīja elektrisko "
                "spriegumu. Izrādās, ka arī mainīgs elektriskais lauks "
                "rada magnētisko - un tā rodas vilnis.",
    uzdevumu_apraksts="EM viļņu garumi un frekvences",
    teorija=[
        ("Elektromagnētiskais vilnis", [
            ("formula", "EM VIĻŅA PAMATSAKARĪBA",
             "c = λf        λ = c/f        c = 3·10⁸ m/s",
             "Mainīgs elektriskais lauks rada magnētisko, tas savukārt "
             "elektrisko - un šis process izplatās telpā kā vilnis. "
             "Vakuumā visi EM viļņi izplatās ar gaismas ātrumu.", GOLD),
            ("divi",
             ("MEHĀNISKS VILNIS", BLUE,
              ["Vajadzīga vide.",
               "Vakuumā neizplatās.",
               "Ātrums atkarīgs no vides.",
               "Skaņa gaisā 340 m/s.",
               "Piemērs: skaņa."]),
             ("EM VILNIS", GREEN,
              ["Vide NAV vajadzīga.",
               "Vakuumā izplatās.",
               "Vakuumā vienmēr c.",
               "Ātrums 3·10⁸ m/s.",
               "Piemērs: gaisma, radio."])),
        ]),
        ("Svārstību kontūrs", [
            ("panelis", "ENERĢIJAS MAIŅA KONTŪRĀ",
             ["Svārstību kontūrs ir kondensators un spole, savienoti "
              "ķēdē. Uzlādēts kondensators izlādējas caur spoli.",
              "Enerģija pārmaiņus ir elektriskā lauka enerģija "
              "kondensatorā un magnētiskā lauka enerģija spolē - gluži "
              "kā svārstā mainās potenciālā un kinētiskā enerģija.",
              "Ja kontūrs ir savienots ar antenu, šīs svārstības izstaro "
              "elektromagnētisko vilni."], NAVY),
            ("tabula",
             ["Kontūra stāvoklis", "Kur enerģija", "Analoģija svārstā"],
             [["Kondensators uzlādēts", "Elektriskajā laukā",
               "Svārsts galējā punktā"],
              ["Strāva maksimāla", "Magnētiskajā laukā",
               "Svārsts līdzsvarā"],
              ["Kondensators pretēji uzlādēts", "Elektriskajā laukā",
               "Otrs galējais punkts"],
              ["Cikls atkārtojas", "Pārmaiņus abos", "Periodiskas svārstības"]],
             [3.60, 3.00, 3.63]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Radioviļņa garums",
             teksts="Radiostacija raida ar frekvenci 100 MHz.\n"
                    "Aprēķini viļņa garumu! (c = 3·10⁸ m/s)",
             dots=["f = 100 MHz = 1,0·10⁸ Hz", "c = 3·10⁸ m/s"],
             jaaprekina=["λ = ?"],
             formulas=["c = λf", "λ = c/f"],
             aprekins=["1)  λ = 3·10⁸ : 1,0·10⁸",
                       "2)  λ = 3,0 m"],
             atbilde="λ = 3,0 m",
             piezime="Tāpēc FM radio antenas garums ir aptuveni metrs - "
                     "ceturtdaļa viļņa garuma."),
        dict(nr=2, virsraksts="Mikroviļņu frekvence",
             teksts="Mikroviļņu krāsns vilnis ir 12,2 cm garš.\n"
                    "Aprēķini frekvenci! (c = 3·10⁸ m/s)",
             dots=["λ = 12,2 cm = 0,122 m", "c = 3·10⁸ m/s"],
             jaaprekina=["f = ?"],
             formulas=["c = λf", "f = c/λ"],
             aprekins=["1)  f = 3·10⁸ : 0,122",
                       "2)  f ≈ 2,46·10⁹ Hz",
                       "3)  f ≈ 2,45 GHz"],
             atbilde="f ≈ 2,45 GHz",
             piezime="2,45 gigaherci - tieši šo frekvenci izmanto arī "
                     "Wi-Fi tīkli."),
        dict(nr=3, virsraksts="Redzamā gaisma",
             teksts="Sarkanās gaismas viļņa garums ir 700 nm.\n"
                    "Aprēķini frekvenci! (1 nm = 10⁻⁹ m)",
             dots=["λ = 700 nm = 7,0·10⁻⁷ m", "c = 3·10⁸ m/s"],
             jaaprekina=["f = ?"],
             formulas=["f = c/λ"],
             aprekins=["1)  λ = 700 · 10⁻⁹ = 7,0·10⁻⁷ m",
                       "2)  f = 3·10⁸ : 7,0·10⁻⁷",
                       "3)  f ≈ 4,3·10¹⁴ Hz"],
             atbilde="f ≈ 4,3·10¹⁴ Hz",
             piezime="Simttūkstoš reižu augstāka frekvence nekā radio - "
                     "bet tas ir tas pats viļņu veids."),
        dict(nr=4, virsraksts="Signāla ceļa laiks",
             teksts="Satelīts atrodas 36 000 km augstumā.\n"
                    "Cik ilgi signāls no tā nonāk līdz Zemei?\n"
                    "(c = 3·10⁸ m/s)",
             dots=["s = 36 000 km = 3,6·10⁷ m", "c = 3·10⁸ m/s"],
             jaaprekina=["t = ?"],
             formulas=["s = ct", "t = s/c"],
             aprekins=["1)  t = 3,6·10⁷ : 3·10⁸",
                       "2)  t = 0,12 s",
                       "3)  Turp un atpakaļ: 0,24 s"],
             atbilde="t = 0,12 s",
             piezime="Tieši šī aizture ir jūtama satelīta telefona "
                     "sarunās."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Mainīgi elektriskie un magnētiskie lauki rada EM vilni.",
            "EM viļņiem vide nav vajadzīga; vakuumā ātrums ir 3·10⁸ m/s.",
            "c = λf - tā pati sakarība, ko lietojām 6. tematā.",
            "Svārstību kontūrā enerģija mainās starp kondensatoru un "
            "spoli.",
        ],
        majasdarbs=[
            "f = 88 MHz. Aprēķini λ.",
            "λ = 0,30 m. Aprēķini f.",
            "Cik ilgi gaisma no Saules (1,5·10¹¹ m) nāk līdz Zemei?",
        ],
        pasvertejums=["Zinu, kā rodas EM vilnis",
                      "Zinu EM viļņa īpašības",
                      "Saprotu svārstību kontūru",
                      "Protu lietot c = λf"],
        nakama="Nākamā stunda: elektromagnētiskais spektrs."),
),

dict(
    nr="12.2", virsraksts="EM spektrs un informācijas izvērtēšana",
    jautajums="Kas kopīgs radio, redzamajai gaismai un rentgenstarojumam?",
    apaksraksts="Spektra daļas · Lietojumi · Jonizējošs starojums",
    merkis="Sakārtot spektra daļas, saistīt tās ar lietojumiem un atšķirt "
           "jonizējošu starojumu no nejonizējoša.",
    protu=["sakārtot spektra daļas pēc viļņa garuma;",
           "nosaukt katras daļas lietojumu;",
           "atšķirt jonizējošu un nejonizējošu starojumu;",
           "izvērtēt apgalvojumu par starojuma kaitīgumu."],
    atkartojums="Iepriekšējā stundā noskaidrojām, ka visi EM viļņi "
                "izplatās vienādi. Atšķiras tikai viļņa garums - un "
                "tieši tas nosaka to īpašības.",
    uzdevumu_apraksts="Spektra daļas un enerģija",
    teorija=[
        ("Elektromagnētiskais spektrs", [
            ("tabula",
             ["Spektra daļa", "Viļņa garums", "Lietojums"],
             [["Radioviļņi", "> 1 m", "Radio, TV, mobilie tīkli"],
              ["Mikroviļņi", "1 mm - 1 m", "Wi-Fi, krāsns, radars"],
              ["Infrasarkanais", "700 nm - 1 mm", "Termokameras, pults"],
              ["Redzamā gaisma", "400-700 nm", "Redze, apgaismojums"],
              ["Ultravioletais", "10-400 nm", "Sauļošanās, dezinfekcija"],
              ["Rentgens un gamma", "< 10 nm", "Medicīna, defektoskopija"]],
             [3.20, 3.20, 3.83]),
            ("panelis", "VIENA SAKARĪBA VISAM SPEKTRAM",
             ["Jo īsāks viļņa garums, jo augstāka frekvence un jo lielāka "
              "viena fotona enerģija.",
              "Tāpēc radioviļņi ir nekaitīgi, bet rentgenstarojums var "
              "bojāt šūnas.",
              "Visas spektra daļas ir viens un tas pats fizikālais "
              "process - atšķiras tikai mērogs."], NAVY),
        ]),
        ("Jonizējošs un nejonizējošs", [
            ("divi",
             ("NEJONIZĒJOŠS", GREEN,
              ["Radio, mikroviļņi,",
               "infrasarkanais, redzamā",
               "gaisma.",
               "Enerģija par mazu,",
               "lai izrautu elektronu.",
               "Var tikai sasildīt."]),
             ("JONIZĒJOŠS", RED,
              ["Ultravioletais (daļēji),",
               "rentgens, gamma.",
               "Izrauj elektronus no",
               "atomiem.",
               "Var bojāt DNS - tāpēc",
               "vajag aizsardzību."])),
            ("panelis", "KĀ IZVĒRTĒT APGALVOJUMU",
             ["Jautā: kāda ir starojuma frekvence? Wi-Fi un mobilie "
              "tīkli ir nejonizējoši - to fotonu enerģija ir miljoniem "
              "reižu mazāka nekā rentgenam.",
              "Jautā: kāda ir deva un kāds ir avots? Bez skaitļiem "
              "apgalvojums nav pārbaudāms.",
              "Jautā: kur publicēts pētījums? Zinātnisks avots norāda "
              "metodi, izlasi un nenoteiktību."], GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Sakārto spektru",
             teksts="Sakārto pēc AUGOŠA viļņa garuma: rentgens,\n"
                    "radioviļņi, redzamā gaisma, mikroviļņi!",
             dots=["Rentgens < 10 nm", "Gaisma 400-700 nm",
                   "Mikroviļņi 1 mm - 1 m", "Radio > 1 m"],
             jaaprekina=["Secība = ?"],
             formulas=["Īsāks vilnis - lielāka enerģija"],
             aprekins=["1)  Rentgens - vismazākais garums",
                       "2)  Tad redzamā gaisma un mikroviļņi",
                       "3)  Radioviļņi - vislielākais garums"],
             atbilde="Rentgens → gaisma → mikroviļņi → radio",
             piezime="Pēc frekvences secība ir tieši pretēja - to "
                     "biežāk jauc."),
        dict(nr=2, virsraksts="Wi-Fi viļņa garums",
             teksts="Wi-Fi frekvence ir 5,0 GHz.\n"
                    "Aprēķini viļņa garumu un nosaki spektra daļu!",
             dots=["f = 5,0 GHz = 5,0·10⁹ Hz", "c = 3·10⁸ m/s"],
             jaaprekina=["λ = ?"],
             formulas=["λ = c/f"],
             aprekins=["1)  λ = 3·10⁸ : 5,0·10⁹",
                       "2)  λ = 0,06 m = 6,0 cm",
                       "3)  Tas ir mikroviļņu diapazons"],
             atbilde="λ = 6,0 cm - mikroviļņi",
             piezime="Mikroviļņi ir nejonizējoši - tie var tikai "
                     "nedaudz sasildīt audus."),
        dict(nr=3, virsraksts="UV starojums",
             teksts="Ultravioletā starojuma viļņa garums ir 300 nm.\n"
                    "Aprēķini frekvenci un salīdzini ar redzamo gaismu\n"
                    "(500 nm)!",
             dots=["λ₁ = 300 nm", "λ₂ = 500 nm", "c = 3·10⁸ m/s"],
             jaaprekina=["f₁ = ?", "Kurš enerģiskāks?"],
             formulas=["f = c/λ"],
             aprekins=["1)  f₁ = 3·10⁸ : 3,0·10⁻⁷ = 1,0·10¹⁵ Hz",
                       "2)  f₂ = 3·10⁸ : 5,0·10⁻⁷ = 6,0·10¹⁴ Hz",
                       "3)  UV frekvence lielāka - enerģija lielāka"],
             atbilde="f₁ = 1,0·10¹⁵ Hz - UV enerģiskāks",
             piezime="Tieši tāpēc UV izraisa apdegumus, bet redzamā "
                     "gaisma - ne."),
        dict(nr=4, virsraksts="Izvērtē apgalvojumu",
             teksts="Ziņā apgalvots: «Wi-Fi starojums ir bīstams, jo tas\n"
                    "ir tāds pats kā rentgens.» Izvērtē apgalvojumu ar\n"
                    "fizikas argumentiem!",
             dots=["Wi-Fi: 5·10⁹ Hz",
                   "Rentgens: 10¹⁸ Hz",
                   "Jonizācijai vajag ~10¹⁵ Hz"],
             jaaprekina=["Vai apgalvojums pamatots?"],
             formulas=["Enerģija aug ar frekvenci",
                       "Jonizē tikai augstas frekvences"],
             aprekins=["1)  Frekvences atšķiras ~10⁸ reižu",
                       "2)  Wi-Fi ir nejonizējošs starojums",
                       "3)  Apgalvojums nav pamatots"],
             atbilde="Apgalvojums nav pamatots",
             piezime="Pareizs arguments vienmēr balstās uz skaitļiem, "
                     "nevis uz vārda «starojums» skanējumu."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Visas spektra daļas ir viens un tas pats EM vilnis.",
            "Jo īsāks vilnis, jo augstāka frekvence un lielāka enerģija.",
            "Jonizējošs starojums izrauj elektronus no atomiem.",
            "Apgalvojumu izvērtē pēc frekvences, devas un avota.",
        ],
        majasdarbs=[
            "f = 2,45 GHz. Aprēķini λ.",
            "Sakārto pēc frekvences: UV, radio, gamma, gaisma.",
            "Atrodi vienu ziņu par starojumu un izvērtē tās pamatojumu.",
        ],
        pasvertejums=["Zinu spektra daļas",
                      "Zinu to lietojumus",
                      "Atšķiru jonizējošu starojumu",
                      "Protu izvērtēt apgalvojumu"],
        nakama="Nākamā stunda: interference un difrakcija."),
),

dict(
    nr="12.3", virsraksts="Interference un difrakcija",
    jautajums="Kāpēc viļņi pastiprina vai dzēš cits citu?",
    apaksraksts="Superpozīcija · Ceļu starpība · Difrakcija",
    merkis="Skaidrot superpozīciju un atpazīt interferences un "
           "difrakcijas pazīmes.",
    protu=["izskaidrot viļņu superpozīciju;",
           "nosaukt maksimuma un minimuma nosacījumu;",
           "izskaidrot difrakciju;",
           "atpazīt interferenci dabas parādībās."],
    atkartojums="6. tematā mācījāmies viļņu pamatlielumus. Tagad "
                "skatīsimies, kas notiek, kad divi viļņi satiekas vienā "
                "vietā.",
    uzdevumu_apraksts="Ceļu starpība un maksimumi",
    teorija=[
        ("Superpozīcija", [
            ("formula", "MAKSIMUMA UN MINIMUMA NOSACĪJUMS",
             "Maksimums: Δd = kλ        Minimums: Δd = (2k + 1)λ/2",
             "Δd ir ceļu starpība - cik daudz viena viļņa ceļš ir garāks "
             "par otra. Ja tā ir vesels viļņu garumu skaits, viļņi "
             "pastiprinās; ja pusgarumu nepāra skaits - dzēšas.", GOLD),
            ("divi",
             ("PASTIPRINĀŠANĀS", GREEN,
              ["Viļņi nāk vienā fāzē.",
               "Kalns sakrīt ar kalnu.",
               "Δd = 0, λ, 2λ, 3λ ...",
               "Rodas gaišā josla vai",
               "skaļa vieta."]),
             ("DZĒŠANĀS", RED,
              ["Viļņi nāk pretējā fāzē.",
               "Kalns sakrīt ar ieleju.",
               "Δd = λ/2, 3λ/2 ...",
               "Rodas tumšā josla vai",
               "klusa vieta."])),
        ]),
        ("Difrakcija", [
            ("panelis", "VIĻŅI LIECAS AP ŠĶĒRSLI",
             ["Difrakcija ir viļņa novirze no taisnas izplatīšanās, ejot "
              "gar šķērsli vai caur šauru spraugu.",
              "Efekts ir manāms, ja spraugas platums ir salīdzināms ar "
              "viļņa garumu - tāpēc skaņu (λ ≈ 1 m) dzirdam aiz stūra, "
              "bet gaismu (λ ≈ 0,5 µm) tur neredzam.",
              "Tieši difrakcija pierāda, ka gaisma ir vilnis."], NAVY),
            ("tabula",
             ["Parādība", "Kas notiek", "Kur redzams"],
             [["Ziepju burbulis", "Interference plēvītē", "Krāsainas joslas"],
              ["Eļļas plankums", "Interference uz ūdens", "Varavīksnes toņi"],
              ["CD virsma", "Difrakcija uz celiņiem", "Spektra krāsas"],
              ["Skaņa aiz stūra", "Difrakcija", "Dzirdam neredzot"]],
             [3.20, 3.40, 3.63]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Maksimums vai minimums",
             teksts="Divi viļņi ar λ = 0,60 m nāk no diviem avotiem.\n"
                    "Ceļu starpība ir 1,80 m. Vai punktā būs maksimums?",
             dots=["λ = 0,60 m", "Δd = 1,80 m"],
             jaaprekina=["Maksimums vai minimums?"],
             formulas=["Maksimums: Δd = kλ", "k = Δd/λ"],
             aprekins=["1)  k = 1,80 : 0,60 = 3",
                       "2)  k ir vesels skaitlis",
                       "3)  Tātad maksimums (3. kārtas)"],
             atbilde="Maksimums, k = 3",
             piezime="Ja iznāktu 3,5 - būtu minimums. Vesels skaitlis "
                     "nozīmē pastiprināšanos."),
        dict(nr=2, virsraksts="Ceļu starpība minimumam",
             teksts="Viļņa garums ir 0,40 m. Kāda ir mazākā ceļu\n"
                    "starpība, pie kuras viļņi dzēšas?",
             dots=["λ = 0,40 m", "Pirmais minimums: k = 0"],
             jaaprekina=["Δd = ?"],
             formulas=["Minimums: Δd = (2k + 1)λ/2", "k = 0"],
             aprekins=["1)  Δd = (2·0 + 1) · 0,40 : 2",
                       "2)  Δd = 0,40 : 2",
                       "3)  Δd = 0,20 m"],
             atbilde="Δd = 0,20 m",
             piezime="Pusviļņa garums - tieši tik daudz vajag, lai "
                     "kalns sakristu ar ieleju."),
        dict(nr=3, virsraksts="Skaņas interference",
             teksts="Divi skaļruņi izstaro skaņu ar λ = 0,68 m.\n"
                    "Klausītājam attālumi līdz tiem ir 5,44 m un 4,08 m.\n"
                    "Vai viņš dzirdēs skaļu vai klusu skaņu?",
             dots=["λ = 0,68 m", "d₁ = 5,44 m", "d₂ = 4,08 m"],
             jaaprekina=["Δd = ?", "Maksimums vai minimums?"],
             formulas=["Δd = d₁ − d₂", "k = Δd/λ"],
             aprekins=["1)  Δd = 5,44 − 4,08 = 1,36 m",
                       "2)  k = 1,36 : 0,68 = 2",
                       "3)  Vesels skaitlis - skaļa skaņa"],
             atbilde="Maksimums, k = 2 - skaņa skaļa",
             piezime="Pārejot dažus desmitus centimetru, klausītājs "
                     "nokļūtu klusajā zonā."),
        dict(nr=4, virsraksts="Kad redzama difrakcija",
             teksts="Paskaidro, kāpēc skaņu dzirdam aiz stūra, bet\n"
                    "gaismu tur neredzam! (skaņa λ ≈ 1 m,\n"
                    "gaisma λ ≈ 5·10⁻⁷ m; durvis 1 m platas)",
             dots=["λ(skaņa) ≈ 1 m", "λ(gaisma) ≈ 5·10⁻⁷ m",
                   "Sprauga 1 m"],
             jaaprekina=["Kāpēc atšķirība?"],
             formulas=["Difrakcija manāma, ja λ ≈ spraugas platums"],
             aprekins=["1)  Skaņai λ ≈ spraugas platums - stipra difrakcija",
                       "2)  Gaismai λ ir miljons reižu mazāks",
                       "3)  Gaismas difrakcija praktiski nemanāma"],
             atbilde="Skaņas vilnis ir salīdzināms ar durvju platumu",
             piezime="Uz šaurām spraugām (matiņa platumā) arī gaismas "
                     "difrakcija kļūst labi redzama."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Superpozīcijā viļņi saskaitās - pastiprinās vai dzēšas.",
            "Maksimums: Δd = kλ; minimums: nepāra pusviļņu skaits.",
            "Difrakcija ir viļņa liekšanās ap šķērsli.",
            "Difrakcija ir manāma, ja sprauga ir viļņa garuma mērogā.",
        ],
        majasdarbs=[
            "λ = 0,50 m, Δd = 2,0 m. Maksimums vai minimums?",
            "λ = 0,60 m. Aprēķini mazāko ceļu starpību minimumam.",
            "Nosauc divus interferences piemērus dabā.",
        ],
        pasvertejums=["Saprotu superpozīciju",
                      "Zinu maksimuma nosacījumu",
                      "Zinu minimuma nosacījumu",
                      "Protu izskaidrot difrakciju"],
        nakama="Nākamā stunda: difrakcijas režģis."),
),

dict(
    nr="12.4", virsraksts="Difrakcijas režģis",
    jautajums="Kā režģis sadala gaismu?",
    apaksraksts="d·sin α = kλ · Režģa periods · Maksimumu kārtas",
    merkis="Skaidrot režģa periodu un maksimumu kārtu un lietot sakarību "
           "d·sin α = kλ.",
    protu=["izskaidrot, kas ir režģa periods;",
           "lietot d·sin α = kλ;",
           "aprēķināt viļņa garumu no mērījumiem;",
           "izskaidrot, kāpēc režģis sadala balto gaismu."],
    atkartojums="Iepriekšējā stundā divas spraugas deva interferences "
                "ainu. Režģī tādu spraugu ir tūkstošiem - un aina kļūst "
                "asa un spilgta.",
    uzdevumu_apraksts="Difrakcijas režģa aprēķini",
    teorija=[
        ("Režģa formula", [
            ("formula", "DIFRAKCIJAS REŽĢA NOSACĪJUMS",
             "d·sin α = kλ        d = 1/N",
             "d ir režģa periods - attālums starp divām blakus "
             "spraugām; N ir svītru skaits uz vienu milimetru vai metru. "
             "k ir maksimuma kārta: 0, 1, 2 ...", GOLD),
            ("kartitas", [
                ("d - PERIODS", BLUE,
                 ["Attālums starp spraugām.",
                  "Mēra metros.",
                  "Jo vairāk svītru,",
                  "jo mazāks d."]),
                ("k - KĀRTA", GREEN,
                 ["Vesels skaitlis.",
                  "k = 0 - centrā.",
                  "k = 1 - pirmais",
                  "maksimums."]),
                ("α - LEŅĶIS", GOLD,
                 ["Novirze no centra.",
                  "Lielāks λ - lielāks α.",
                  "Sarkanā novirzās",
                  "vairāk par zilo."]),
            ]),
        ]),
        ("Kāpēc rodas spektrs", [
            ("panelis", "BALTĀ GAISMA SADALĀS",
             ["Baltā gaisma satur visus viļņu garumus. Katram no tiem "
              "maksimums veidojas savā leņķī, jo formulā ir λ.",
              "Sarkanajai gaismai λ ir lielāks, tāpēc tā novirzās "
              "vairāk; violetajai - vismazāk.",
              "Tā rodas spektrs. To pašu principu izmanto "
              "spektrometros, ar kuriem pēta vielu un zvaigžņu sastāvu."],
             NAVY),
            ("tabula",
             ["Lielums", "Kā ietekmē ainu", "Praktiskā nozīme"],
             [["Vairāk svītru", "Maksimumi tālāk", "Asāks spektrs"],
              ["Lielāks λ", "Lielāks leņķis", "Sarkanā tālāk no centra"],
              ["Augstāka kārta", "Lielāks leņķis", "Vājāka spilgtums"],
              ["Ekrāns tālāk", "Attālumi lielāki", "Vieglāk mērīt"]],
             [3.20, 3.40, 3.63]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Režģa periods",
             teksts="Režģim ir 500 svītru uz milimetru.\n"
                    "Aprēķini režģa periodu metros!",
             dots=["N = 500 svītru uz mm", "1 mm = 10⁻³ m"],
             jaaprekina=["d = ?"],
             formulas=["d = 1/N"],
             aprekins=["1)  N = 500 000 svītru uz metru",
                       "2)  d = 1 : 500 000",
                       "3)  d = 2·10⁻⁶ m = 2 µm"],
             atbilde="d = 2·10⁻⁶ m",
             piezime="Periods ir daži mikrometri - tikai dažas reizes "
                     "lielāks par gaismas viļņa garumu."),
        dict(nr=2, virsraksts="Viļņa garums no leņķa",
             teksts="Uz režģa ar d = 2·10⁻⁶ m pirmās kārtas maksimums\n"
                    "ir leņķī, kura sinuss ir 0,25.\n"
                    "Aprēķini viļņa garumu!",
             dots=["d = 2·10⁻⁶ m", "k = 1", "sin α = 0,25"],
             jaaprekina=["λ = ?"],
             formulas=["d·sin α = kλ", "λ = d·sin α/k"],
             aprekins=["1)  d·sin α = 2·10⁻⁶ · 0,25 = 5·10⁻⁷",
                       "2)  λ = 5·10⁻⁷ : 1",
                       "3)  λ = 5·10⁻⁷ m = 500 nm"],
             atbilde="λ = 500 nm",
             piezime="500 nanometru ir zaļā gaisma - tieši tur acs ir "
                     "visjutīgākā."),
        dict(nr=3, virsraksts="Otrās kārtas maksimums",
             teksts="Tam pašam režģim un gaismai (λ = 500 nm) aprēķini\n"
                    "sinusu otrās kārtas maksimumam!",
             dots=["d = 2·10⁻⁶ m", "λ = 5·10⁻⁷ m", "k = 2"],
             jaaprekina=["sin α = ?"],
             formulas=["d·sin α = kλ", "sin α = kλ/d"],
             aprekins=["1)  kλ = 2 · 5·10⁻⁷ = 1·10⁻⁶",
                       "2)  sin α = 1·10⁻⁶ : 2·10⁻⁶",
                       "3)  sin α = 0,50"],
             atbilde="sin α = 0,50  (α = 30°)",
             piezime="Otrā kārta ir divreiz tālāk pēc sinusa, bet "
                     "manāmi vājāka."),
        dict(nr=4, virsraksts="Cik kārtu redzams",
             teksts="Režģim d = 2·10⁻⁶ m, gaisma λ = 500 nm.\n"
                    "Cik maksimumu kārtu vispār var novērot?\n"
                    "(sin α nevar būt lielāks par 1)",
             dots=["d = 2·10⁻⁶ m", "λ = 5·10⁻⁷ m", "sin α ≤ 1"],
             jaaprekina=["k(max) = ?"],
             formulas=["sin α = kλ/d", "sin α ≤ 1", "k ≤ d/λ"],
             aprekins=["1)  k ≤ 2·10⁻⁶ : 5·10⁻⁷",
                       "2)  k ≤ 4",
                       "3)  Redzamas kārtas 0, 1, 2, 3 un 4"],
             atbilde="k(max) = 4",
             piezime="Fizikāla robeža: sinusam nevar būt vērtība virs "
                     "viena - tā ir laba ticamības pārbaude."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "d·sin α = kλ - difrakcijas režģa pamatsakarība.",
            "Režģa periods d = 1/N.",
            "Lielākam viļņa garumam atbilst lielāks leņķis.",
            "Kārtu skaitu ierobežo nosacījums sin α ≤ 1.",
        ],
        majasdarbs=[
            "N = 300 svītru uz mm. Aprēķini d.",
            "d = 4·10⁻⁶ m, k = 1, sin α = 0,15. Aprēķini λ.",
            "Aprēķini, cik kārtu redzamas, ja d = 3·10⁻⁶ m un λ = 600 nm.",
        ],
        pasvertejums=["Zinu, kas ir režģa periods",
                      "Protu lietot režģa formulu",
                      "Protu aprēķināt viļņa garumu",
                      "Protu noteikt kārtu skaitu"],
        nakama="Nākamā stunda: LD4 sagatavošana."),
),

]
