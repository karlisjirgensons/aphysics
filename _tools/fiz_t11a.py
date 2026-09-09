# -*- coding: utf-8 -*-
"""11. temats "Elektromagnētisms". A daļa: 11.1.-11.5. stunda."""

from fiz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN     # noqa: F401

TEMATS = "11. temats. Elektromagnētisms"
KICKER = "FIZIKA I · 11. KLASE · 11. TEMATS: ELEKTROMAGNĒTISMS"
KURSS = "FIZIKA I · 11. KLASE"
MAPE = "C:/aphysics/Fizika_1/11. Elektromagnētisms"

STUNDAS = [

dict(
    nr="11.1", virsraksts="Magnēti un elektromagnēti",
    jautajums="Kā elektriskā strāva rada magnētisko lauku?",
    apaksraksts="Magnētiskās līnijas · Elektromagnēts · [B] = tesla",
    merkis="Attēlot vienkāršu magnētisko lauku un skaidrot elektromagnēta "
           "darbību.",
    protu=["nosaukt magnēta polus un to mijiedarbību;",
           "attēlot magnētiskā lauka līnijas;",
           "izskaidrot, kā strāva rada magnētisko lauku;",
           "nosaukt, kas pastiprina elektromagnētu."],
    atkartojums="10. tematā strāva bija lādiņu kustība. Šodien "
                "noskaidrosim, ka ap katru strāvas vadu rodas vēl viens "
                "lauks - magnētiskais.",
    uzdevumu_apraksts="Magnētiskais lauks un elektromagnēts",
    teorija=[
        ("Magnētiskais lauks", [
            ("panelis", "PAMATFAKTI PAR MAGNĒTIEM",
             ["Katram magnētam ir ziemeļu un dienvidu pols; vienādi poli "
              "atgrūžas, pretēji pievelkas.",
              "Atsevišķu polu iegūt nevar: pārlaužot magnētu, rodas divi "
              "jauni magnēti ar abiem poliem.",
              "Magnētiskā lauka līnijas ir noslēgtas: ārpus magnēta tās "
              "iet no ziemeļu pola uz dienvidu polu.",
              "Lauka stiprumu raksturo magnētiskā indukcija B; to mēra "
              "teslās (T)."], NAVY),
            ("kartitas", [
                ("TAISNS VADS", BLUE,
                 ["Līnijas ir riņķa līnijas",
                  "ap vadu.",
                  "Virzienu nosaka ar",
                  "labās rokas likumu."]),
                ("SPOLE", GREEN,
                 ["Lauks kā stieņa magnētam.",
                  "Iekšpusē vienmērīgs.",
                  "Poli atkarīgi no",
                  "strāvas virziena."]),
                ("ELEKTROMAGNĒTS", GOLD,
                 ["Spole ar dzelzs serdi.",
                  "Serde pastiprina laukam",
                  "simtiem reižu.",
                  "Var izslēgt."]),
            ]),
        ]),
        ("Kur to izmanto", [
            ("tabula",
             ["Ierīce", "Kā darbojas", "Kāpēc elektromagnēts"],
             [["Metāllūžņu celtnis", "Ieslēdz un izslēdz lauku",
               "Var atlaist kravu"],
              ["Elektriskais zvans", "Serde pievelk āmuriņu",
               "Ātri pārslēdzas"],
              ["Relejs", "Maza strāva slēdz lielu",
               "Droša vadība"],
              ["Skaļrunis", "Spole kustas laukā", "Atveido skaņu"]],
             [3.40, 3.60, 3.23]),
            ("panelis", "KAS PASTIPRINA ELEKTROMAGNĒTU",
             ["Lielāka strāva - stiprāks lauks; tāpēc elektromagnētiem "
              "vajag jaudīgu barošanu.",
              "Vairāk vijumu spolē - stiprāks lauks pie tās pašas "
              "strāvas.",
              "Dzelzs serde pastiprina lauku visvairāk; tā ir "
              "elektromagnēta galvenā atšķirība no parastas spoles."],
             GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Kā pastiprināt",
             teksts="Elektromagnēts pie 0,50 A strāvas notur 2,0 kg\n"
                    "kravu. Nosauc trīs veidus, kā palielināt tā spēku,\n"
                    "un paskaidro katru!",
             dots=["I = 0,50 A", "m = 2,0 kg", "Spole ar serdi"],
             jaaprekina=["Kā pastiprināt?"],
             formulas=["Lauks aug ar strāvu",
                       "Lauks aug ar vijumu skaitu",
                       "Serde pastiprina lauku"],
             aprekins=["1)  Palielināt strāvu",
                       "2)  Uztīt vairāk vijumu",
                       "3)  Izmantot dzelzs serdi"],
             atbilde="Strāva, vijumu skaits, serde",
             piezime="Vijumu skaitu palielināt ir drošāk nekā strāvu - "
                     "spole mazāk karst."),
        dict(nr=2, virsraksts="Kravas svars",
             teksts="Cik lielu spēku elektromagnētam jārada, lai noturētu\n"
                    "150 kg metāllūžņu? (g = 9,8 m/s²)",
             dots=["m = 150 kg", "g = 9,8 m/s²"],
             jaaprekina=["F = ?"],
             formulas=["F = mg"],
             aprekins=["1)  F = 150 · 9,8",
                       "2)  F = 1470 N",
                       "3)  F ≈ 1,5 kN"],
             atbilde="F ≈ 1,5·10³ N",
             piezime="Praksē celtnim rezervi ņem vismaz divkāršu - "
                     "krava nedrīkst nokrist."),
        dict(nr=3, virsraksts="Zvana jauda",
             teksts="Elektriskā zvana spole pie 12 V patērē 0,60 A.\n"
                    "Aprēķini jaudu un spoles pretestību!",
             dots=["U = 12 V", "I = 0,60 A"],
             jaaprekina=["P = ?", "R = ?"],
             formulas=["P = UI", "R = U/I"],
             aprekins=["1)  P = 12 · 0,60 = 7,2 W",
                       "2)  R = 12 : 0,60",
                       "3)  R = 20 Ω"],
             atbilde="P = 7,2 W;  R = 20 Ω",
             piezime="Elektromagnētiskās ierīces rēķina ar tiem pašiem "
                     "10. temata likumiem."),
        dict(nr=4, virsraksts="Polu noteikšana",
             teksts="Spolei strāva plūst tā, ka, skatoties no priekšas,\n"
                    "tā iet pretēji pulksteņrādītāja virzienam.\n"
                    "Kurš pols ir vērsts pret skatītāju?",
             dots=["Strāva pretēji pulksteņrādītājam",
                   "Skatās no spoles gala"],
             jaaprekina=["Kurš pols?"],
             formulas=["Labās rokas likums spolei",
                       "Pirksti - strāvas virzienā",
                       "Īkšķis rāda ziemeļu polu"],
             aprekins=["1)  Pirkstus liek strāvas virzienā",
                       "2)  Īkšķis rāda uz skatītāju",
                       "3)  Pret skatītāju ir ZIEMEĻU pols"],
             atbilde="Ziemeļu pols",
             piezime="Mainot strāvas virzienu, poli apmainās vietām - "
                     "tā darbojas maiņstrāvas ierīces."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Magnētam vienmēr ir divi poli; atsevišķu polu nav.",
            "Ap strāvas vadu rodas magnētiskais lauks.",
            "Spole ar dzelzs serdi ir elektromagnēts.",
            "Lauku pastiprina strāva, vijumu skaits un serde.",
        ],
        majasdarbs=[
            "Uzzīmē stieņa magnēta lauka līnijas.",
            "m = 80 kg krava. Aprēķini vajadzīgo spēku.",
            "Nosauc trīs elektromagnēta lietojumus sadzīvē.",
        ],
        pasvertejums=["Zinu magnēta īpašības",
                      "Protu attēlot lauka līnijas",
                      "Zinu, kā strāva rada lauku",
                      "Zinu, kas pastiprina elektromagnētu"],
        nakama="Nākamā stunda: elektromotors un spēks uz strāvas vadu."),
),

dict(
    nr="11.2", virsraksts="Elektromotors un spēks uz vadu",
    jautajums="Kāpēc elektromotors griežas?",
    apaksraksts="F = BIl · Kreisās rokas likums · Rāmis laukā",
    merkis="Skaidrot spēka iedarbību uz strāvas vadu un lietot F = BIl "
           "perpendikulārā laukā.",
    protu=["izskaidrot, kāpēc uz strāvas vadu laukā darbojas spēks;",
           "lietot F = BIl;",
           "noteikt spēka virzienu;",
           "izskaidrot elektromotora darbību."],
    atkartojums="Iepriekšējā stundā strāva radīja magnētisko lauku. "
                "Tagad būs otrādi: gatavs lauks iedarbosies uz strāvas "
                "vadu ar spēku.",
    uzdevumu_apraksts="Spēka uz vadu aprēķini",
    teorija=[
        ("Spēks uz strāvas vadu", [
            ("formula", "AMPĒRA SPĒKS",
             "F = B · I · l        B = F/Il        [B] = tesla (T)",
             "Formula der, ja vads ir perpendikulārs laukam. B ir "
             "magnētiskā indukcija, I - strāva, l - vada garums laukā. "
             "Ja vads ir paralēls laukam, spēks ir nulle.", GOLD),
            ("kartitas", [
                ("VIRZIENS", BLUE,
                 ["Nosaka ar kreisās rokas",
                  "likumu.",
                  "Spēks perpendikulārs",
                  "gan laukam, gan strāvai."]),
                ("KAS PALIELINA F", GREEN,
                 ["Stiprāks lauks B.",
                  "Lielāka strāva I.",
                  "Garāks vads l laukā."]),
                ("KAD F = 0", GREY,
                 ["Vads paralēls laukam.",
                  "Strāva izslēgta.",
                  "Vads ārpus lauka."]),
            ]),
        ]),
        ("Elektromotors", [
            ("panelis", "KĀ GRIEŽAS MOTORS",
             ["Rāmī ar strāvu magnētiskajā laukā uz pretējām malām "
              "spēki ir vērsti pretēji - rodas griezes moments.",
              "Kad rāmis pagriežas par pusapgriezienu, kolektors maina "
              "strāvas virzienu, un griešanās turpinās.",
              "Motorā elektroenerģija pārvēršas mehāniskajā enerģijā; "
              "ģeneratorā notiek pretējais."], NAVY),
            ("tabula",
             ["Ierīce", "Kas ievadīts", "Kas iegūts"],
             [["Elektromotors", "Elektroenerģija", "Mehāniskā enerģija"],
              ["Ģenerators", "Mehāniskā enerģija", "Elektroenerģija"],
              ["Skaļrunis", "Elektriskais signāls", "Skaņas viļņi"],
              ["Mikrofons", "Skaņas viļņi", "Elektriskais signāls"]],
             [3.20, 3.40, 3.63]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Spēks uz vadu",
             teksts="Vads 0,20 m garumā atrodas laukā ar indukciju\n"
                    "0,40 T perpendikulāri, un caur to plūst 3,0 A.\n"
                    "Aprēķini spēku!",
             dots=["l = 0,20 m", "B = 0,40 T", "I = 3,0 A"],
             jaaprekina=["F = ?"],
             formulas=["F = BIl"],
             aprekins=["1)  F = 0,40 · 3,0 · 0,20",
                       "2)  F = 0,24 N"],
             atbilde="F = 0,24 N",
             piezime="Spēks neliels, bet motorā vijumu ir simtiem - un "
                     "spēki summējas."),
        dict(nr=2, virsraksts="Meklē strāvu",
             teksts="Uz 0,15 m garu vadu laukā 0,50 T darbojas spēks\n"
                    "0,30 N. Aprēķini strāvu!",
             dots=["l = 0,15 m", "B = 0,50 T", "F = 0,30 N"],
             jaaprekina=["I = ?"],
             formulas=["F = BIl", "I = F/Bl"],
             aprekins=["1)  Bl = 0,50 · 0,15 = 0,075",
                       "2)  I = 0,30 : 0,075",
                       "3)  I = 4,0 A"],
             atbilde="I = 4,0 A",
             piezime="No vienas formulas var izteikt visus četrus "
                     "lielumus."),
        dict(nr=3, virsraksts="Magnētiskā indukcija",
             teksts="Vads 0,25 m garumā ar strāvu 2,0 A laukā izjūt\n"
                    "spēku 0,10 N. Aprēķini magnētisko indukciju!",
             dots=["l = 0,25 m", "I = 2,0 A", "F = 0,10 N"],
             jaaprekina=["B = ?"],
             formulas=["F = BIl", "B = F/Il"],
             aprekins=["1)  Il = 2,0 · 0,25 = 0,50",
                       "2)  B = 0,10 : 0,50",
                       "3)  B = 0,20 T"],
             atbilde="B = 0,20 T",
             piezime="0,2 teslas ir tipisks skolas magnēta lauks; MRI "
                     "iekārtā tas ir 1,5-3 T."),
        dict(nr=4, virsraksts="Motora vijumi",
             teksts="Motora rāmī ir 200 vijumi, katrs 0,10 m garš,\n"
                    "laukā 0,30 T, strāva 1,5 A.\n"
                    "Aprēķini kopējo spēku uz vienu rāmja malu!",
             dots=["N = 200", "l = 0,10 m", "B = 0,30 T", "I = 1,5 A"],
             jaaprekina=["F = ?"],
             formulas=["F₁ = BIl", "F = N · F₁"],
             aprekins=["1)  F₁ = 0,30 · 1,5 · 0,10 = 0,045 N",
                       "2)  F = 200 · 0,045",
                       "3)  F = 9,0 N"],
             atbilde="F = 9,0 N",
             piezime="Tieši vijumu skaits padara mazu motoru "
                     "pietiekami spēcīgu."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Uz strāvas vadu magnētiskajā laukā darbojas spēks F = BIl.",
            "Spēka virzienu nosaka ar kreisās rokas likumu.",
            "Ja vads ir paralēls laukam, spēks ir nulle.",
            "Motorā elektroenerģija pārvēršas mehāniskajā enerģijā.",
        ],
        majasdarbs=[
            "B = 0,25 T, I = 4,0 A, l = 0,30 m. Aprēķini F.",
            "F = 0,50 N, B = 0,20 T, l = 0,50 m. Aprēķini I.",
            "Paskaidro, kāpēc motora rāmim vajag kolektoru.",
        ],
        pasvertejums=["Zinu, kad rodas spēks",
                      "Protu lietot F = BIl",
                      "Protu noteikt virzienu",
                      "Zinu motora darbību"],
        nakama="Nākamā stunda: lādēta daļiņa magnētiskajā laukā."),
),

dict(
    nr="11.3", virsraksts="Daļiņa magnētiskajā laukā",
    jautajums="Kāpēc lādētas daļiņas novirzās?",
    apaksraksts="Lorenca spēks F = qvB · Riņķa kustība · Ziemeļblāzma",
    merkis="Kvalitatīvi skaidrot Lorenca spēku un tā izraisīto kustības "
           "virziena maiņu.",
    protu=["izskaidrot, kad uz lādiņu laukā darbojas spēks;",
           "lietot F = qvB vienkāršā gadījumā;",
           "izskaidrot, kāpēc daļiņa kustas pa riņķa līniju;",
           "izskaidrot ziemeļblāzmas rašanos."],
    atkartojums="Iepriekšējā stundā spēks darbojās uz vadu ar strāvu. "
                "Bet strāva ir kustīgi lādiņi - tātad spēks darbojas uz "
                "katru atsevišķu lādiņu.",
    uzdevumu_apraksts="Lorenca spēks un daļiņu kustība",
    teorija=[
        ("Lorenca spēks", [
            ("formula", "SPĒKS UZ KUSTĪGU LĀDIŅU",
             "F = q · v · B        (v perpendikulāra B)",
             "Spēks darbojas tikai uz KUSTĪGU lādiņu un ir "
             "perpendikulārs gan ātrumam, gan laukam. Tāpēc tas maina "
             "kustības virzienu, bet ne ātruma lielumu.", GOLD),
            ("divi",
             ("KAD SPĒKS IR", GREEN,
              ["Lādiņš kustas.",
               "Ātrums nav paralēls laukam.",
               "Lielākais spēks, ja",
               "v ⊥ B."]),
             ("KAD SPĒKA NAV", GREY,
              ["Lādiņš nekustas (v = 0).",
               "Ātrums paralēls laukam.",
               "Daļiņa neitrāla (q = 0).",
               "Nav lauka (B = 0)."])),
        ]),
        ("Kur to redz", [
            ("panelis", "KUSTĪBA PA RIŅĶA LĪNIJU",
             ["Spēks vienmēr ir perpendikulārs ātrumam - tieši tāpat kā "
              "centrtieces spēks 2. tematā. Tāpēc daļiņa kustas pa riņķa "
              "līniju.",
              "Darbs, ko veic Lorenca spēks, ir nulle: spēks ir "
              "perpendikulārs pārvietojumam, tāpēc enerģija nemainās.",
              "Uz šī principa balstās daļiņu paātrinātāji un masas "
              "spektrometri."], NAVY),
            ("tabula",
             ["Parādība", "Kas notiek", "Rezultāts"],
             [["Ziemeļblāzma", "Saules daļiņas novirzās uz poliem",
               "Gaisma augšējos slāņos"],
              ["Zemes lauks", "Aizsargā no kosmiskā starojuma",
               "Dzīvība iespējama"],
              ["Kineskops", "Elektronu kūlis novirzīts", "Attēls ekrānā"],
              ["Paātrinātājs", "Daļiņas tur pa apli", "Pēta vielas uzbūvi"]],
             [3.20, 4.20, 2.83]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Spēks uz elektronu",
             teksts="Elektrons ar ātrumu 2,0·10⁶ m/s ielido laukā 0,50 T\n"
                    "perpendikulāri. Aprēķini spēku!\n"
                    "(q = 1,6·10⁻¹⁹ C)",
             dots=["v = 2,0·10⁶ m/s", "B = 0,50 T", "q = 1,6·10⁻¹⁹ C"],
             jaaprekina=["F = ?"],
             formulas=["F = qvB"],
             aprekins=["1)  qv = 1,6·10⁻¹⁹ · 2,0·10⁶ = 3,2·10⁻¹³",
                       "2)  F = 3,2·10⁻¹³ · 0,50",
                       "3)  F = 1,6·10⁻¹³ N"],
             atbilde="F = 1,6·10⁻¹³ N",
             piezime="Spēks sīks, bet elektrona masa ir vēl daudz "
                     "mazāka - tāpēc tas strauji novirzās."),
        dict(nr=2, virsraksts="Kad spēka nav",
             teksts="Nosaki, vai uz daļiņu darbojas Lorenca spēks:\n"
                    "a) nekustīgs elektrons laukā; b) neitrons kustībā;\n"
                    "c) protons, kas kustas pa lauka līniju.",
             dots=["a) v = 0", "b) q = 0", "c) v paralēls B"],
             jaaprekina=["Vai ir spēks?"],
             formulas=["F = qvB", "Vajag q, v un leņķi"],
             aprekins=["1)  a) v = 0, tāpēc F = 0",
                       "2)  b) neitrons neitrāls, F = 0",
                       "3)  c) v paralēls B, tāpēc F = 0"],
             atbilde="Nevienā gadījumā spēka nav",
             piezime="Vajadzīgi visi trīs nosacījumi: lādiņš, kustība un "
                     "leņķis pret lauku."),
        dict(nr=3, virsraksts="Protons laukā",
             teksts="Protons ar ātrumu 5,0·10⁵ m/s kustas perpendikulāri\n"
                    "laukam 0,20 T. Aprēķini spēku!\n"
                    "(q = 1,6·10⁻¹⁹ C)",
             dots=["v = 5,0·10⁵ m/s", "B = 0,20 T", "q = 1,6·10⁻¹⁹ C"],
             jaaprekina=["F = ?"],
             formulas=["F = qvB"],
             aprekins=["1)  qv = 1,6·10⁻¹⁹ · 5,0·10⁵ = 8,0·10⁻¹⁴",
                       "2)  F = 8,0·10⁻¹⁴ · 0,20",
                       "3)  F = 1,6·10⁻¹⁴ N"],
             atbilde="F = 1,6·10⁻¹⁴ N",
             piezime="Protona lādiņš ir tāds pats kā elektronam, bet "
                     "zīme pretēja - tāpēc tas novirzās uz otru pusi."),
        dict(nr=4, virsraksts="Ziemeļblāzma",
             teksts="Paskaidro, kāpēc ziemeļblāzmu redz tieši polu\n"
                    "tuvumā, nevis pie ekvatora!",
             dots=["Saules vējš - lādētas daļiņas",
                   "Zemes magnētiskais lauks"],
             jaaprekina=["Kāpēc pie poliem?"],
             formulas=["F = qvB",
                       "Spēks liek kustēties pa spirāli"],
             aprekins=["1)  Lādētās daļiņas novirzās gar lauka līnijām",
                       "2)  Līnijas satek kopā pie poliem",
                       "3)  Tur daļiņas iekļūst atmosfērā un ierosina gāzes"],
             atbilde="Lauka līnijas virza daļiņas uz poliem",
             piezime="Tas pats lauks pasargā visu planētu no Saules "
                     "daļiņu plūsmas."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Lorenca spēks darbojas tikai uz kustīgu lādiņu.",
            "F = qvB, ja ātrums ir perpendikulārs laukam.",
            "Spēks maina virzienu, nevis ātruma lielumu.",
            "Ziemeļblāzma rodas, daļiņām nonākot pie magnētiskajiem "
            "poliem.",
        ],
        majasdarbs=[
            "q = 1,6·10⁻¹⁹ C, v = 1,0·10⁶ m/s, B = 0,30 T. Aprēķini F.",
            "Paskaidro, kāpēc Lorenca spēks neveic darbu.",
            "Nosauc divus lietojumus, kur daļiņas virza ar magnētisko "
            "lauku.",
        ],
        pasvertejums=["Zinu, kad rodas Lorenca spēks",
                      "Protu lietot F = qvB",
                      "Saprotu riņķa kustību",
                      "Protu izskaidrot ziemeļblāzmu"],
        nakama="Nākamā stunda: elektromagnētiskā indukcija."),
),

dict(
    nr="11.4", virsraksts="Elektromagnētiskā indukcija",
    jautajums="Kā kustīgs magnēts var radīt strāvu?",
    apaksraksts="Φ = BS · ε = ΔΦ/Δt · Lenca likums",
    merkis="Skaidrot magnētiskās plūsmas izmaiņas un noteikt, kas "
           "palielina inducēto spriegumu.",
    protu=["izskaidrot, kas ir magnētiskā plūsma;",
           "nosaukt, kad rodas inducētais spriegums;",
           "lietot ε = ΔΦ/Δt;",
           "nosaukt, kas palielina inducēto spriegumu."],
    atkartojums="Līdz šim strāva radīja magnētisko lauku. Šodien būs "
                "pretējais un vēl svarīgāks atklājums: mainīgs "
                "magnētiskais lauks rada strāvu.",
    uzdevumu_apraksts="Indukcijas aprēķini",
    teorija=[
        ("Magnētiskā plūsma", [
            ("formula", "PLŪSMA UN INDUKCIJAS LIKUMS",
             "Φ = B · S        ε = ΔΦ/Δt        [Φ] = vēbers (Wb)",
             "Magnētiskā plūsma raksturo, cik daudz lauka līniju iet caur "
             "kontūru. Inducētais spriegums rodas TIKAI tad, kad plūsma "
             "MAINĀS - un jo ātrāk, jo lielāks spriegums.", GOLD),
            ("divi",
             ("SPRIEGUMS RODAS", GREEN,
              ["Magnētu kustina.",
               "Spoli kustina.",
               "Maina lauka stiprumu.",
               "Griež rāmi laukā."]),
             ("SPRIEGUMA NAV", GREY,
              ["Magnēts nekustas.",
               "Lauks nemainās.",
               "Plūsma ir nemainīga.",
               "Kaut arī lauks ir stiprs."])),
        ]),
        ("Kas palielina spriegumu", [
            ("tabula",
             ["Faktors", "Kā rīkojas", "Kāpēc"],
             [["Kustības ātrums", "Kustina ātrāk", "Plūsma mainās straujāk"],
              ["Vijumu skaits", "Vairāk vijumu", "Katrs vijums pievieno"],
              ["Lauka stiprums", "Stiprāks magnēts", "Lielāka plūsmas izmaiņa"],
              ["Spoles laukums", "Lielāks laukums", "Vairāk lauka līniju"]],
             [3.20, 3.20, 3.83]),
            ("panelis", "LENCA LIKUMS",
             ["Inducētā strāva vienmēr ir vērsta tā, lai PRETOTOS "
              "plūsmas izmaiņai, kas to radījusi.",
              "Tāpēc, tuvinot magnētu spolei, tā to atgrūž, bet, "
              "attālinot - pievelk.",
              "Tas ir enerģijas nezūdamības likums indukcijā: elektrību "
              "iegūst tikai tad, ja veic mehānisku darbu."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Magnētiskā plūsma",
             teksts="Spoles laukums ir 0,020 m², lauka indukcija 0,50 T\n"
                    "perpendikulāri laukumam. Aprēķini plūsmu!",
             dots=["S = 0,020 m²", "B = 0,50 T"],
             jaaprekina=["Φ = ?"],
             formulas=["Φ = BS"],
             aprekins=["1)  Φ = 0,50 · 0,020",
                       "2)  Φ = 0,010 Wb"],
             atbilde="Φ = 1,0·10⁻² Wb",
             piezime="Vēbers ir tesla reiz kvadrātmetrs."),
        dict(nr=2, virsraksts="Inducētais spriegums",
             teksts="Spolē plūsma 0,20 s laikā mainās no 0,010 Wb līdz\n"
                    "nullei. Aprēķini inducēto spriegumu!",
             dots=["ΔΦ = 0,010 Wb", "Δt = 0,20 s"],
             jaaprekina=["ε = ?"],
             formulas=["ε = ΔΦ/Δt"],
             aprekins=["1)  ε = 0,010 : 0,20",
                       "2)  ε = 0,050 V"],
             atbilde="ε = 0,050 V",
             piezime="Jo ātrāk plūsma mainās, jo lielāks spriegums - "
                     "tāpēc magnētu kustina ātri."),
        dict(nr=3, virsraksts="Vairāki vijumi",
             teksts="Tā pati plūsmas izmaiņa notiek spolē ar 500\n"
                    "vijumiem. Aprēķini inducēto spriegumu!",
             dots=["ΔΦ = 0,010 Wb", "Δt = 0,20 s", "N = 500"],
             jaaprekina=["ε = ?"],
             formulas=["ε = N · ΔΦ/Δt"],
             aprekins=["1)  Vienam vijumam: 0,050 V",
                       "2)  ε = 500 · 0,050",
                       "3)  ε = 25 V"],
             atbilde="ε = 25 V",
             piezime="Tieši tāpēc ģeneratoros un transformatoros ir "
                     "simtiem un tūkstošiem vijumu."),
        dict(nr=4, virsraksts="Kad sprieguma nav",
             teksts="Magnēts nekustīgi guļ spoles iekšpusē.\n"
                    "Voltmetrs rāda nulli. Paskaidro, kāpēc, un nosauc,\n"
                    "ko darīt, lai spriegums parādītos!",
             dots=["Magnēts nekustas", "Lauks stiprs",
                   "Voltmetrs rāda 0"],
             jaaprekina=["Kāpēc ε = 0?"],
             formulas=["ε = ΔΦ/Δt", "Ja ΔΦ = 0, tad ε = 0"],
             aprekins=["1)  Plūsma ir liela, bet NEMAINĀS",
                       "2)  ΔΦ = 0, tāpēc ε = 0",
                       "3)  Jākustina magnēts vai spole"],
             atbilde="Spriegumu rada tikai plūsmas IZMAIŅA",
             piezime="Tā ir biežākā kļūda: jauc lauka stiprumu ar tā "
                     "izmaiņu."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Magnētiskā plūsma Φ = BS.",
            "Inducētais spriegums rodas tikai no plūsmas IZMAIŅAS.",
            "ε = ΔΦ/Δt; vairāki vijumi spriegumu reizina.",
            "Lenca likums: inducētā strāva pretojas izmaiņai.",
        ],
        majasdarbs=[
            "B = 0,40 T, S = 0,050 m². Aprēķini Φ.",
            "ΔΦ = 0,020 Wb, Δt = 0,10 s, N = 200. Aprēķini ε.",
            "Paskaidro, kāpēc nekustīgs magnēts strāvu nerada.",
        ],
        pasvertejums=["Zinu, kas ir plūsma",
                      "Zinu, kad rodas spriegums",
                      "Protu lietot indukcijas likumu",
                      "Zinu Lenca likumu"],
        nakama="Nākamā stunda: ģenerators un indukcijas lietojumi."),
),

dict(
    nr="11.5", virsraksts="Ģenerators un indukcijas lietojumi",
    jautajums="Kā elektrību iegūst elektrostacijā?",
    apaksraksts="Ģenerators · Enerģijas pārvērtības · Indukcijas "
                "lietojumi",
    merkis="Salīdzināt motoru un ģeneratoru un skaidrot enerģijas "
           "pārvērtības elektrostacijā.",
    protu=["izskaidrot ģeneratora darbību;",
           "salīdzināt motoru un ģeneratoru;",
           "izsekot enerģijas pārvērtībām elektrostacijā;",
           "nosaukt indukcijas lietojumus sadzīvē."],
    atkartojums="Iepriekšējā stundā noskaidrojām, ka plūsmas izmaiņa "
                "rada spriegumu. Ģenerators ir ierīce, kas šo izmaiņu "
                "uztur nepārtraukti.",
    uzdevumu_apraksts="Ģeneratori un enerģijas pārvērtības",
    teorija=[
        ("Ģenerators", [
            ("panelis", "KĀ TAS DARBOJAS",
             ["Ģeneratorā rāmis (vai spole) griežas magnētiskajā laukā, "
              "tāpēc plūsma caur to nepārtraukti mainās.",
              "Kad rāmja plakne ir paralēla laukam, plūsma mainās "
              "visstraujāk un spriegums ir vislielākais.",
              "Katrā pusapgriezienā sprieguma zīme mainās - tā rodas "
              "maiņstrāva."], NAVY),
            ("tabula",
             ["Elektrostacija", "Kas griež turbīnu", "Enerģijas ceļš"],
             [["Hidroelektrostacija", "Ūdens plūsma",
               "Potenciālā → mehāniskā → elektriskā"],
              ["Termoelektrostacija", "Tvaiks",
               "Ķīmiskā → siltuma → mehāniskā → elektriskā"],
              ["Vēja stacija", "Vējš", "Mehāniskā → elektriskā"],
              ["Atomelektrostacija", "Tvaiks",
               "Kodolenerģija → siltuma → elektriskā"]],
             [3.40, 2.80, 6.03]),
        ]),
        ("Kur vēl izmanto indukciju", [
            ("kartitas", [
                ("INDUKCIJAS PLĪTS", RED,
                 ["Mainīgs lauks katlā",
                  "rada virpuļstrāvas.",
                  "Silst pats katls,",
                  "nevis plīts virsma."]),
                ("BEZVADU LĀDĒŠANA", BLUE,
                 ["Divas spoles blakus.",
                  "Mainīgs lauks pārnes",
                  "enerģiju bez kontakta.",
                  "Telefoni, zobu birstes."]),
                ("MIKROFONS", GREEN,
                 ["Membrāna kustina spoli.",
                  "Rodas mainīgs spriegums.",
                  "Skaņa kļūst par signālu."]),
            ]),
            ("panelis", "MOTORS UN ĢENERATORS IR VIENA IERĪCE",
             ["Ja motoram pievada strāvu, tas griežas; ja to griež ar "
              "roku, tas rada spriegumu.",
              "Velosipēda dinamo un elektroauto rekuperācijas bremzes "
              "izmanto tieši šo pārslēgšanos.",
              "Elektroauto bremzējot motors kļūst par ģeneratoru un "
              "uzlādē akumulatoru."], GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Ģeneratora spriegums",
             teksts="Ģeneratora spolē ar 800 vijumiem plūsma 0,010 s\n"
                    "laikā mainās par 0,0015 Wb.\n"
                    "Aprēķini inducēto spriegumu!",
             dots=["N = 800", "ΔΦ = 0,0015 Wb", "Δt = 0,010 s"],
             jaaprekina=["ε = ?"],
             formulas=["ε = N · ΔΦ/Δt"],
             aprekins=["1)  ΔΦ : Δt = 0,0015 : 0,010 = 0,15 V",
                       "2)  ε = 800 · 0,15",
                       "3)  ε = 120 V"],
             atbilde="ε = 120 V",
             piezime="Palielinot vijumu skaitu vai griešanās ātrumu, "
                     "spriegumu var vēl paaugstināt."),
        dict(nr=2, virsraksts="Hidroelektrostacija",
             teksts="Ūdens ar masu 5000 kg nokrīt no 12 m augstuma\n"
                    "sekundē. Aprēķini pieejamo jaudu, ja lietderība ir\n"
                    "85 %! (g = 9,8 m/s²)",
             dots=["m = 5000 kg sekundē", "h = 12 m", "η = 0,85"],
             jaaprekina=["P = ?"],
             formulas=["Ep = mgh", "P = Ep/t", "P(lietd.) = ηP"],
             aprekins=["1)  Ep = 5000 · 9,8 · 12 = 588 000 J",
                       "2)  P = 588 000 : 1 = 588 kW",
                       "3)  P(lietd.) = 0,85 · 588 = 500 kW"],
             atbilde="P ≈ 500 kW",
             piezime="Enerģijas pārvērtības: potenciālā → mehāniskā → "
                     "elektriskā."),
        dict(nr=3, virsraksts="Velosipēda dinamo",
             teksts="Dinamo pie 6,0 V nodrošina 0,50 A strāvu.\n"
                    "Aprēķini jaudu un enerģiju, kas iegūta 10 minūtēs!",
             dots=["U = 6,0 V", "I = 0,50 A", "t = 10 min = 600 s"],
             jaaprekina=["P = ?", "E = ?"],
             formulas=["P = UI", "E = Pt"],
             aprekins=["1)  P = 6,0 · 0,50 = 3,0 W",
                       "2)  E = 3,0 · 600",
                       "3)  E = 1800 J"],
             atbilde="P = 3,0 W;  E = 1800 J",
             piezime="Šo enerģiju dod tavas kājas - tāpēc ar dinamo "
                     "braukt ir mazliet grūtāk."),
        dict(nr=4, virsraksts="Motors vai ģenerators",
             teksts="Nosaki, kas ir ievadītā un kas iegūtā enerģija:\n"
                    "a) veļasmašīnas motors; b) vēja turbīna;\n"
                    "c) elektroauto bremzēšana.",
             dots=["a) veļasmašīna", "b) vēja turbīna",
                   "c) rekuperācija"],
             jaaprekina=["Motors vai ģenerators?"],
             formulas=["Motors: elektriskā → mehāniskā",
                       "Ģenerators: mehāniskā → elektriskā"],
             aprekins=["1)  a) motors - elektrība kļūst par griešanos",
                       "2)  b) ģenerators - vējš kļūst par elektrību",
                       "3)  c) ģenerators - kustība uzlādē akumulatoru"],
             atbilde="a) motors;  b) un c) ģenerators",
             piezime="Viena un tā pati mašīna var strādāt abos "
                     "režīmos - atšķiras tikai enerģijas virziens."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Ģeneratorā griežas spole magnētiskajā laukā.",
            "Motors un ģenerators ir viena ierīce ar pretēju enerģijas "
            "plūsmu.",
            "Elektrostacijā enerģija iziet vairākas pārvērtības.",
            "Indukciju izmanto plītīs, bezvadu lādētājos un mikrofonos.",
        ],
        majasdarbs=[
            "N = 500, ΔΦ = 0,0020 Wb, Δt = 0,020 s. Aprēķini ε.",
            "Uzraksti enerģijas pārvērtību ķēdi termoelektrostacijā.",
            "Nosauc trīs indukcijas lietojumus mājās.",
        ],
        pasvertejums=["Zinu ģeneratora darbību",
                      "Protu salīdzināt ar motoru",
                      "Zinu enerģijas pārvērtības",
                      "Zinu indukcijas lietojumus"],
        nakama="Nākamā stunda: maiņstrāva un tās grafiks."),
),

]
