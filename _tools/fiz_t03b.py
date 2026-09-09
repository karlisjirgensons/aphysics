# -*- coding: utf-8 -*-
"""3. temats. B daļa: 3.8.-3.14. stunda (elastība, berze, slīpā plakne)."""

from fiz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN     # noqa: F401
from fiz_t03a import TEMATS, KICKER, KURSS, MAPE              # noqa: F401

STUNDAS = [

dict(
    nr="3.8", virsraksts="Elastības spēks. Huka likums",
    jautajums="No kā atkarīgs atsperes spēks?",
    apaksraksts="F = kx · Stinguma koeficients · Elastības robeža",
    merkis="Iemācīties lietot Huka likumu un saprast, kad tas ir spēkā.",
    protu=["formulēt Huka likumu;",
           "aprēķināt spēku, pagarinājumu vai stinguma koeficientu;",
           "nolasīt k no F(x) grafika;",
           "nosaukt elastības robežas nozīmi."],
    atkartojums="3.7. stundā redzējām, ka balsta reakcija ir elastības "
                "spēks. Tagad izpētīsim elastības spēku precīzi - ar "
                "atsperi.",
    uzdevumu_apraksts="Huka likums un stinguma koeficients",
    teorija=[
        ("Huka likums", [
            ("formula", "ELASTĪBAS SPĒKS",
             "F = k · x        k = F / x        [k] = N/m",
             "x ir PAGARINĀJUMS (vai saīsinājums), nevis atsperes garums. "
             "Elastības spēks vienmēr vērsts PRETĒJI deformācijai.", GOLD),
            ("kartitas", [
                ("LIELS k", BLUE,
                 ["Stinga atspere.",
                  "Grūti izstiept.",
                  "Piemērs: automašīnas atspere."]),
                ("MAZS k", GREEN,
                 ["Mīksta atspere.",
                  "Viegli izstiept.",
                  "Piemērs: dinamometra atspere."]),
                ("ELASTĪBAS ROBEŽA", RED,
                 ["Pēc tās Huka likums neder.",
                  "Atspere neatgriežas.",
                  "Plastiska deformācija."]),
            ]),
        ]),
        ("Grafiks F(x)", [
            ("panelis", "KO RĀDA GRAFIKS",
             ["Huka likuma apgabalā F(x) ir TAISNE caur koordinātu "
              "sākumpunktu; tās slīpums ir stinguma koeficients:",
              "k = ΔF/Δx",
              "Kad grafiks sāk liekties, elastības robeža ir "
              "pārsniegta - tālāk formula F = kx vairs neder."], NAVY),
            ("tabula",
             ["Objekts", "Aptuvenais k", "Piezīme"],
             [["Dinamometra atspere", "20-100 N/m", "Skolas komplekts"],
              ["Lodīšu pildspalvas atspere", "~300 N/m", "Maza, bet "
               "stinga"],
              ["Automašīnas atspere", "~30 000 N/m", "Tur veselu masu"],
              ["Batuta gumija", "~500 N/m", "Liels pagarinājums"]],
             [5.10, 3.40, 3.73]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Stinguma koeficients",
             teksts="Atsperi ar 4,0 N spēku izstiepj par 8,0 cm.\n"
                    "Aprēķini stinguma koeficientu!",
             dots=["F = 4,0 N", "x = 8,0 cm = 0,080 m"],
             jaaprekina=["k = ?"],
             formulas=["F = kx", "k = F/x"],
             aprekins=["1)  x = 8,0 cm = 0,080 m",
                       "2)  k = 4,0 : 0,080",
                       "3)  k = 50 N/m"],
             atbilde="k = 50 N/m",
             piezime="Mērvienība N/m nozīmē: 50 N vajag 1 m "
                     "pagarinājumam."),
        dict(nr=2, virsraksts="Pagarinājums no masas",
             teksts="Pie atsperes (k = 200 N/m) piekar 2,0 kg atsvaru.\n"
                    "Par cik atspere pagarinās? (g = 9,8 m/s²)",
             dots=["k = 200 N/m", "m = 2,0 kg", "g = 9,8 m/s²"],
             jaaprekina=["x = ?"],
             formulas=["F = mg", "x = F/k"],
             aprekins=["1)  F = 2,0 · 9,8 = 19,6 N",
                       "2)  x = 19,6 : 200",
                       "3)  x = 0,098 m ≈ 9,8 cm"],
             atbilde="x ≈ 9,8 cm",
             piezime="Līdzsvarā elastības spēks ir vienāds ar smaguma "
                     "spēku."),
        dict(nr=3, virsraksts="k no grafika",
             teksts="F(x) grafikā taisne iet caur (0,05 m; 3,0 N) un\n"
                    "(0,20 m; 12 N). Aprēķini stinguma koeficientu!",
             dots=["(0,05; 3,0)", "(0,20; 12)"],
             jaaprekina=["k = ?"],
             formulas=["k = ΔF/Δx"],
             aprekins=["1)  ΔF = 12 − 3,0 = 9,0 N",
                       "2)  Δx = 0,20 − 0,05 = 0,15 m",
                       "3)  k = 9,0 : 0,15 = 60 N/m"],
             atbilde="k = 60 N/m",
             piezime="No slīpuma iegūtais k ir ticamāks nekā no viena "
                     "punkta - tā tiks vērtēts LD3 darbā."),
        dict(nr=4, virsraksts="Divas atsperes virknē",
             teksts="Divas vienādas atsperes (k = 100 N/m) savieno "
                    "virknē\nun pakar 1,0 kg atsvaru. Par cik pagarinās "
                    "katra un\nkopā? (g = 9,8 m/s²)",
             dots=["k = 100 N/m katrai", "m = 1,0 kg"],
             jaaprekina=["x₁ = ?", "x(kop) = ?"],
             formulas=["Katrā atsperē tas pats spēks", "x = F/k"],
             aprekins=["1)  F = 1,0 · 9,8 = 9,8 N (abās vienāds)",
                       "2)  x₁ = 9,8 : 100 = 0,098 m",
                       "3)  x(kop) = 2 · 0,098 = 0,196 m ≈ 20 cm"],
             atbilde="Katra pagarinās par 9,8 cm; kopā ≈ 20 cm.",
             piezime="Virknē sistēma kļūst MĪKSTĀKA: k(kop) = 50 N/m."),
        dict(nr=5, virsraksts="Spēks no pagarinājuma",
             teksts="Atsperi ar stinguma koeficientu 250 N/m izstiepj "
                    "par\n6,0 cm. Cik liels ir elastības spēks?",
             dots=["k = 250 N/m", "x = 6,0 cm = 0,060 m"],
             jaaprekina=["F = ?"],
             formulas=["F = kx"],
             aprekins=["1)  x = 6,0 cm = 0,060 m",
                       "2)  F = 250 · 0,060",
                       "3)  F = 15 N"],
             atbilde="F = 15 N, vērsts pretēji deformācijai.",
             piezime="Pagarinājumu vienmēr pārveido metros, pirms lieto "
                     "Huka likumu."),
        dict(nr=6, virsraksts="Divas atsperes paralēli",
             teksts="Divas vienādas atsperes (k = 100 N/m) novietotas "
                    "blakus\nun tur 1,0 kg atsvaru. Par cik tās "
                    "pagarinās? (g = 9,8 m/s²)",
             dots=["k = 100 N/m katrai", "m = 1,0 kg", "paralēli"],
             jaaprekina=["x = ?", "k(kop) = ?"],
             formulas=["Slodze sadalās uz pusēm", "x = F/(2k)"],
             aprekins=["1)  F = 1,0 · 9,8 = 9,8 N",
                       "2)  Katrai atsperei 4,9 N",
                       "3)  x = 4,9 : 100 = 0,049 m = 4,9 cm"],
             atbilde="x = 4,9 cm ;   k(kop) = 200 N/m",
             piezime="Paralēli sistēma kļūst STINGRĀKA, virknē - "
                     "mīkstāka."),
        dict(nr=7, virsraksts="k no atsperes garuma",
             teksts="Atsperes brīvais garums ir 20 cm. Piekarot 3,0 kg\n"
                    "atsvaru, tās garums kļūst 26 cm. Aprēķini k! "
                    "(g = 9,8 m/s²)",
             dots=["l₀ = 20 cm", "l = 26 cm", "m = 3,0 kg"],
             jaaprekina=["x = ?", "k = ?"],
             formulas=["x = l − l₀", "F = mg", "k = F/x"],
             aprekins=["1)  x = 26 − 20 = 6,0 cm = 0,060 m",
                       "2)  F = 3,0 · 9,8 = 29,4 N",
                       "3)  k = 29,4 : 0,060 = 490 N/m"],
             atbilde="k = 490 N/m ≈ 4,9·10² N/m",
             piezime="Huka likumā lieto PAGARINĀJUMU, nevis pilno "
                     "atsperes garumu."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Huka likums: F = kx, kur x ir pagarinājums.",
            "k ir stinguma koeficients, [k] = N/m.",
            "F(x) grafika slīpums ir k.",
            "Pēc elastības robežas Huka likums vairs neder.",
        ],
        majasdarbs=[
            "F = 6,0 N, x = 12 cm. Aprēķini k.",
            "k = 250 N/m, m = 3,0 kg. Aprēķini x.",
            "Sagatavo LD3 hipotēzi par F(x) grafika formu.",
        ],
        pasvertejums=["Protu formulēt Huka likumu",
                      "Protu rēķināt k, F un x",
                      "Protu nolasīt k no grafika",
                      "Protu paskaidrot elastības robežu"],
        nakama="Nākamā stunda: LD3 sagatavošana."),
),

dict(
    nr="3.9", virsraksts="LD3 sagatavošana",
    jautajums="Ko un kā mērīsim atsperei?",
    apaksraksts="Mainīgie · Mērījumu plāns · Grafika mērogs",
    merkis="Sagatavot LD3 laboratorijas darbu: noteikt mainīgos, "
           "izplānot mērījumus un paredzēt grafika formu.",
    protu=["formulēt hipotēzi par F(x) grafiku;",
           "noteikt mainīgos un fiksētos lielumus;",
           "izvēlēties mērījumu diapazonu un mērogu;",
           "paredzēt kļūdu avotus."],
    atkartojums="1.12. stundā mācījāmies plānot pētījumu, 3.8. stundā - "
                "Huka likumu. Tagad tos savienojam konkrētam darbam.",
    uzdevumu_apraksts="Mērījumu plānošana un grafika sagatavošana",
    teorija=[
        ("LD3 pētījuma plāns", [
            ("tabula",
             ["Elements", "LD3 gadījumā", "Kāpēc"],
             [["Pētāmais jautājums", "Kā x atkarīgs no F", "Huka likuma "
               "pārbaude"],
              ["Neatkarīgais", "Slodze m (tātad F)", "To maina pētnieks"],
              ["Atkarīgais", "Pagarinājums x", "To mēra"],
              ["Fiksētie", "Atspere, lineāla stāvoklis", "Salīdzināmība"],
              ["Atkārtojumi", "5 slodzes + atgriešanās", "Kļūdu kontrole"]],
             [3.90, 4.30, 4.03]),
            ("formula", "KO APRĒĶINĀS",
             "F = mg   →   k = F / x   →   k no grafika slīpuma "
             "k = ΔF/Δx",
             "Divas k vērtības salīdzina; ticamāka ir tā, kas iegūta no "
             "grafika, jo izmanto visus mērījumus.", GOLD),
        ]),
        ("Ko sagatavot iepriekš", [
            ("panelis", "PIRMS MĒRĪJUMIEM",
             ["1) Uzzīmē tabulu ar slejām m, F, nolasījums, x, k.  "
              "2) Novērtē gaidāmo diapazonu: ar k ≈ 30 N/m un 500 g "
              "slodzi x ≈ 16 cm.  3) Izvēlies grafika mērogu tā, lai "
              "punkti aizņemtu vismaz pusi lapas."], NAVY),
            ("kartitas", [
                ("DROŠĪBA", RED,
                 ["Nepārsniegt atsperes robežu.",
                  "Zem atsvariem - paliktnis.",
                  "Statīvu nostiprināt."]),
                ("PRECIZITĀTE", BLUE,
                 ["Nolasīt acu līmenī.",
                  "Gaidīt, līdz nomierinās.",
                  "Sākuma stāvokli fiksēt."]),
                ("PĀRBAUDE", GREEN,
                 ["Noņemt atsvarus pa vienam.",
                  "Vai atgriežas sākumā?",
                  "Ja nē - robeža pārsniegta."]),
            ]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Gaidāmais pagarinājums",
             teksts="Atsperei k ≈ 40 N/m. Plāno slodzes 100, 200, 300,\n"
                    "400 un 500 g. Aprēķini gaidāmo pagarinājumu "
                    "diapazonu!\n(g = 9,8 m/s²)",
             dots=["k = 40 N/m", "m no 0,10 līdz 0,50 kg"],
             jaaprekina=["x(min) = ?", "x(max) = ?"],
             formulas=["F = mg", "x = F/k"],
             aprekins=["1)  F(min) = 0,10 · 9,8 = 0,98 N → "
                       "x = 0,025 m",
                       "2)  F(max) = 0,50 · 9,8 = 4,9 N → x = 0,123 m",
                       "3)  Diapazons 2,5-12,3 cm"],
             atbilde="x no 2,5 cm līdz 12,3 cm - ērti mērāms ar lineālu.",
             piezime="Ja diapazons būtu zem 1 cm, relatīvā kļūda būtu "
                     "pārāk liela."),
        dict(nr=2, virsraksts="Mēroga izvēle",
             teksts="Grafikā F no 0 līdz 5,0 N (ass 10 cm) un x no 0 "
                    "līdz\n0,13 m (ass 12 cm). Izvēlies ērtu mērogu abām "
                    "asīm!",
             dots=["F līdz 5,0 N, ass 10 cm", "x līdz 0,13 m, ass 12 cm"],
             jaaprekina=["mērogs = ?"],
             formulas=["Mērogs = diapazons / ass garums"],
             aprekins=["1)  F: 5,0 : 10 = 0,50 N/cm → ņem 0,50 N/cm",
                       "2)  x: 0,13 : 12 ≈ 0,011 m/cm → ņem 0,02 m/cm",
                       "3)  Tad x ass aizņems 6,5 cm - pieņemami"],
             atbilde="F ass: 1 cm ↔ 0,50 N;  x ass: 1 cm ↔ 0,02 m.",
             piezime="Mērogam vienmēr izvēlas 1, 2 vai 5 vienības uz "
                     "iedaļu."),
        dict(nr=3, virsraksts="Kļūdas novērtējums",
             teksts="Lineāla iedaļas vērtība 1 mm. Novērtē relatīvo "
                    "kļūdu\npagarinājumam 2,5 cm un 12,3 cm!",
             dots=["Δx = 0,5 mm", "x₁ = 25 mm", "x₂ = 123 mm"],
             jaaprekina=["δ₁ = ?", "δ₂ = ?"],
             formulas=["δ = Δx/x · 100 %"],
             aprekins=["1)  δ₁ = 0,5 : 25 · 100 % = 2,0 %",
                       "2)  δ₂ = 0,5 : 123 · 100 % = 0,4 %",
                       "3)  Mazajām slodzēm kļūda 5 reižu lielāka"],
             atbilde="δ₁ = 2,0 % ;   δ₂ = 0,4 %",
             piezime="Tāpēc svarīgi izmantot pilnu slodžu diapazonu."),
        dict(nr=4, virsraksts="Hipotēzes formulēšana",
             teksts="Formulē LD3 hipotēzi par grafika formu un par to,\n"
                    "ko nozīmēs tā slīpums!",
             dots=["pēta x atkarību no F"],
             jaaprekina=["hipotēze = ?"],
             formulas=["Ja ..., tad ..., jo ..."],
             aprekins=["1)  Ja slodzi palielina vienādos soļos,",
                       "2)  tad pagarinājums pieaugs vienādos soļos un "
                       "F(x) būs taisne caur nulli,",
                       "3)  jo pēc Huka likuma F = kx; slīpums dos k."],
             atbilde="F(x) būs taisne caur koordinātu sākumpunktu; tās "
                     "slīpums ir stinguma koeficients k.",
             piezime="Hipotēzē noteikti jāpasaka arī, ko nozīmēs "
                     "slīpums."),
        dict(nr=5, virsraksts="LD3 tabulas sagatavošana",
             teksts="Sagatavo mērījumu tabulas galveni LD3 darbam ar "
                    "piecām\nslodzēm un diviem atkārtojumiem katrai!",
             dots=["5 slodzes", "2 atkārtojumi"],
             jaaprekina=["slejas = ?", "rindas = ?"],
             formulas=["Katrai slejai - lielums un mērvienība"],
             aprekins=["1)  Slejas: Nr.; m, kg; F, N; l₁, m; l₂, m;",
                       "2)  l(vid), m;  x, m;  k, N/m",
                       "3)  Rindas: 5 (pa vienai katrai slodzei)"],
             atbilde="8 slejas un 5 datu rindas; mērvienības tikai "
                     "galvenē.",
             piezime="Tā pati tabulas uzbūve, ko mācījāmies "
                     "1.12. stundā."),
        dict(nr=6, virsraksts="k no divām mērījumu rindām",
             teksts="Mērījumi: m = 0,20 kg → x = 4,8 cm;\n"
                    "m = 0,40 kg → x = 9,7 cm. Aprēķini k pēc "
                    "pieauguma! (g = 9,8 m/s²)",
             dots=["m₁ = 0,20 kg, x₁ = 0,048 m",
                   "m₂ = 0,40 kg, x₂ = 0,097 m"],
             jaaprekina=["ΔF = ?", "Δx = ?", "k = ?"],
             formulas=["F = mg", "k = ΔF/Δx"],
             aprekins=["1)  ΔF = (0,40 − 0,20) · 9,8 = 1,96 N",
                       "2)  Δx = 0,097 − 0,048 = 0,049 m",
                       "3)  k = 1,96 : 0,049 = 40 N/m"],
             atbilde="k = 40 N/m",
             piezime="Rēķinot pēc pieauguma, izzūd sistemātiska nulles "
                     "nobīde - tāpēc šī metode ir precīzāka."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "LD3: maina slodzi, mēra pagarinājumu, atspere ir fiksēta.",
            "Gaidāmo diapazonu var aprēķināt iepriekš.",
            "Mazām vērtībām relatīvā kļūda ir lielāka.",
            "Hipotēzē jānorāda gan grafika forma, gan slīpuma nozīme.",
        ],
        majasdarbs=[
            "Sagatavo LD3 protokola 1.-3. sadaļu.",
            "k ≈ 60 N/m, m līdz 0,60 kg. Aprēķini gaidāmo x diapazonu.",
            "Atkārto Huka likumu un F(x) grafika lasīšanu.",
        ],
        pasvertejums=["Protu formulēt hipotēzi",
                      "Protu paredzēt diapazonu",
                      "Protu izvēlēties mērogu",
                      "Esmu gatavs LD3"],
        nakama="Nākamā stunda: LD3 - atsperes stinguma koeficients."),
),

dict(
    nr="3.10", virsraksts="Berzes spēks",
    jautajums="Kāpēc kastes grūti pabīdīt?",
    apaksraksts="F(b) = µN · Miera un slīdes berze · Ripošanas berze",
    merkis="Iemācīties aprēķināt berzes spēku un atšķirt miera berzi no "
           "slīdes berzes.",
    protu=["lietot F(b) = µN;",
           "atšķirt miera, slīdes un ripošanas berzi;",
           "novērtēt berzes koeficientu tipiskiem materiāliem;",
           "nosaukt, kad berze ir noderīga un kad kaitīga."],
    atkartojums="3.7. stundā: N nosaka berzi. Tagad izpētīsim berzes "
                "spēku pašu - vienu no biežāk sastopamajiem spēkiem "
                "uzdevumos.",
    uzdevumu_apraksts="Berzes spēks un berzes koeficients",
    teorija=[
        ("Berzes veidi", [
            ("kartitas", [
                ("MIERA BERZE", BLUE,
                 ["Ķermenis vēl nekustas.",
                  "F(b) = pieliktais spēks.",
                  "Maksimums: F = µ(0)N."]),
                ("SLĪDES BERZE", GREEN,
                 ["Ķermenis slīd.",
                  "F(b) = µN - aptuveni nemainīga.",
                  "Nedaudz mazāka par miera berzi."]),
                ("RIPOŠANAS BERZE", GOLD,
                 ["Ķermenis rit.",
                  "10-100 reižu mazāka.",
                  "Tāpēc izgudroja riteni."]),
            ]),
            ("formula", "SLĪDES BERZES SPĒKS",
             "F(b) = µ · N        µ - berzes koeficients (bez "
             "mērvienības)",
             "Berzes spēks nav atkarīgs no saskares laukuma, bet ir "
             "atkarīgs no materiāliem un no balsta reakcijas N.", GOLD),
        ]),
        ("Berzes koeficienti", [
            ("tabula",
             ["Materiālu pāris", "µ (slīdes)", "Piezīme"],
             [["Riepa - sauss asfalts", "0,7-0,8", "Laba bremzēšana"],
              ["Riepa - slapjš asfalts", "0,4-0,5", "Ceļš divreiz garāks"],
              ["Riepa - ledus", "0,1-0,2", "Ļoti bīstami"],
              ["Koks - koks", "0,3-0,5", "Tipisks uzdevumos"],
              ["Tērauds - tērauds ar eļļu", "0,05-0,1", "Eļļošana"]],
             [4.60, 3.40, 4.23]),
            ("panelis", "BERZE - DRAUGS UN IENAIDNIEKS",
             ["Noderīga: iešana, bremzēšana, naglas turēšanās, mezgli. "
              "Kaitīga: dzinēja detaļu nodilums, enerģijas zudumi. "
              "Palielina ar raupjumu un spiedienu; samazina ar eļļošanu, "
              "gultņiem un ripošanu."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Berzes spēks",
             teksts="Kaste (m = 40 kg) slīd pa horizontālu grīdu;\n"
                    "µ = 0,35. Aprēķini berzes spēku! (g = 9,8 m/s²)",
             dots=["m = 40 kg", "µ = 0,35", "g = 9,8 m/s²"],
             jaaprekina=["N = ?", "F(b) = ?"],
             formulas=["N = mg", "F(b) = µN"],
             aprekins=["1)  N = 40 · 9,8 = 392 N",
                       "2)  F(b) = 0,35 · 392",
                       "3)  F(b) = 137 ≈ 1,4·10² N"],
             atbilde="F(b) ≈ 1,4·10² N",
             piezime="Lai kaste kustētos vienmērīgi, jāvelk tieši ar šo "
                     "spēku."),
        dict(nr=2, virsraksts="Berzes koeficients",
             teksts="Lai 25 kg kasti vilktu vienmērīgi pa horizontālu "
                    "grīdu,\nvajag 75 N. Aprēķini berzes koeficientu! "
                    "(g = 9,8 m/s²)",
             dots=["m = 25 kg", "F = 75 N (vienmērīgi)"],
             jaaprekina=["µ = ?"],
             formulas=["Vienmērīgi → F = F(b)", "µ = F(b)/N"],
             aprekins=["1)  N = 25 · 9,8 = 245 N",
                       "2)  F(b) = F = 75 N",
                       "3)  µ = 75 : 245 ≈ 0,31"],
             atbilde="µ ≈ 0,31",
             piezime="Vienmērīgas kustības nosacījums ļauj berzi "
                     "izmērīt tieši."),
        dict(nr=3, virsraksts="Bremzēšanas ceļš un berze",
             teksts="Automašīna brauc 20 m/s. Aprēķini bremzēšanas ceļu\n"
                    "uz sausa (µ = 0,75) un slapja (µ = 0,40) asfalta! "
                    "(g = 9,8 m/s²)",
             dots=["v₀ = 20 m/s", "µ₁ = 0,75", "µ₂ = 0,40"],
             jaaprekina=["s₁ = ?", "s₂ = ?"],
             formulas=["a = µg", "s = v₀²/(2a)"],
             aprekins=["1)  a₁ = 0,75 · 9,8 = 7,35 m/s² → "
                       "s₁ = 400 : 14,7 = 27 m",
                       "2)  a₂ = 0,40 · 9,8 = 3,92 m/s² → "
                       "s₂ = 400 : 7,84 = 51 m",
                       "3)  s₂ / s₁ ≈ 1,9"],
             atbilde="s₁ ≈ 27 m ;   s₂ ≈ 51 m - gandrīz divreiz garāks.",
             piezime="Masa saīsinās: bremzēšanas ceļš nav atkarīgs no "
                     "automašīnas masas."),
        dict(nr=4, virsraksts="Paātrinājums ar berzi",
             teksts="Kasti (m = 30 kg) velk ar 150 N; µ = 0,25.\n"
                    "Aprēķini paātrinājumu! (g = 9,8 m/s²)",
             dots=["m = 30 kg", "F = 150 N", "µ = 0,25"],
             jaaprekina=["a = ?"],
             formulas=["N = mg", "F(b) = µN", "a = (F − F(b))/m"],
             aprekins=["1)  N = 30 · 9,8 = 294 N",
                       "2)  F(b) = 0,25 · 294 = 73,5 N",
                       "3)  a = (150 − 73,5) : 30 = 2,55 ≈ 2,6 m/s²"],
             atbilde="a ≈ 2,6 m/s²",
             piezime="Vienmēr vispirms N, tad F(b), tad kopspēks."),
        dict(nr=5, virsraksts="Masas ietekme uz berzi",
             teksts="Kastes masu palielina no 20 kg līdz 40 kg;\n"
                    "µ = 0,30 nemainās. Kā mainās berzes spēks? "
                    "(g = 9,8 m/s²)",
             dots=["m₁ = 20 kg", "m₂ = 40 kg", "µ = 0,30"],
             jaaprekina=["F(b1) = ?", "F(b2) = ?"],
             formulas=["N = mg", "F(b) = µmg"],
             aprekins=["1)  F(b1) = 0,30 · 20 · 9,8 = 58,8 N",
                       "2)  F(b2) = 0,30 · 40 · 9,8 = 117,6 N",
                       "3)  F(b2) : F(b1) = 2"],
             atbilde="Berzes spēks palielinās 2 reizes - tikpat, cik "
                     "masa.",
             piezime="Berzes spēks ir tieši proporcionāls balsta "
                     "reakcijai, tātad arī masai."),
        dict(nr=6, virsraksts="Spēks vienmērīgai vilkšanai",
             teksts="Cik liels spēks vajadzīgs, lai 60 kg kasti vilktu\n"
                    "vienmērīgi pa horizontālu grīdu, ja µ = 0,20? "
                    "(g = 9,8 m/s²)",
             dots=["m = 60 kg", "µ = 0,20", "v = const"],
             jaaprekina=["F = ?"],
             formulas=["v = const → F = F(b)", "F(b) = µmg"],
             aprekins=["1)  N = 60 · 9,8 = 588 N",
                       "2)  F(b) = 0,20 · 588",
                       "3)  F = 117,6 ≈ 1,2·10² N"],
             atbilde="F ≈ 1,2·10² N",
             piezime="Vienmērīgai kustībai vilkšanas spēks ir tieši "
                     "vienāds ar berzi."),
        dict(nr=7, virsraksts="µ no bremzēšanas ceļa",
             teksts="Automašīna no 15 m/s apstājas 25 m garā bremzēšanas\n"
                    "ceļā. Aprēķini berzes koeficientu! (g = 9,8 m/s²)",
             dots=["v₀ = 15 m/s", "v = 0", "s = 25 m"],
             jaaprekina=["a = ?", "µ = ?"],
             formulas=["v₀² = 2as", "a = µg", "µ = a/g"],
             aprekins=["1)  a = 225 : (2 · 25) = 4,5 m/s²",
                       "2)  µ = 4,5 : 9,8",
                       "3)  µ ≈ 0,46"],
             atbilde="µ ≈ 0,46 (mitrs asfalts)",
             piezime="Pēc bremzēšanas pēdām uz ceļa policija tieši šādi "
                     "nosaka sākuma ātrumu."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "F(b) = µN; µ nav mērvienības.",
            "Miera berze var būt lielāka par slīdes berzi.",
            "Ripošanas berze ir daudz mazāka par slīdes berzi.",
            "Bremzēšanas ceļš nav atkarīgs no masas: s = v₀²/(2µg).",
        ],
        majasdarbs=[
            "m = 50 kg, µ = 0,20. Aprēķini F(b).",
            "F = 90 N vilkšanai vienmērīgi, m = 35 kg. Aprēķini µ.",
            "v₀ = 15 m/s, µ = 0,15 (ledus). Aprēķini bremzēšanas ceļu.",
        ],
        pasvertejums=["Protu lietot F(b) = µN",
                      "Protu atšķirt berzes veidus",
                      "Protu rēķināt bremzēšanas ceļu",
                      "Protu atrast paātrinājumu ar berzi"],
        nakama="Nākamā stunda: uzdevumi par berzi."),
),

dict(
    nr="3.11", virsraksts="Uzdevumi par berzi",
    jautajums="Cik liels spēks jāpieliek, lai kaste kustētos?",
    apaksraksts="Miera berze · Slīpi vērsts spēks · Vairāki soļi",
    merkis="Nostiprināt berzes uzdevumu risināšanu, tostarp gadījumos, "
           "kad spēks vērsts leņķī.",
    protu=["noteikt, vai ķermenis sāks kustēties;",
           "risināt uzdevumus ar slīpi vērstu spēku;",
           "kombinēt berzi ar kinemātiku;",
           "pamatot, kāpēc vilkt ir vieglāk nekā stumt."],
    atkartojums="3.10. stundā: F(b) = µN. Šodien lietosim to sarežģītākās "
                "situācijās - ar leņķī vērstiem spēkiem un vairākiem "
                "soļiem.",
    uzdevumu_apraksts="Berze ar slīpi vērstu spēku un kustības sākums",
    teorija=[
        ("Vai ķermenis sāks kustēties", [
            ("formula", "KUSTĪBAS SĀKUMA NOSACĪJUMS",
             "Ja  F(pielikts) > µ₀ · N  →  ķermenis sāk kustēties        "
             "Ja  F(pielikts) ≤ µ₀ · N  →  paliek mierā",
             "Miera stāvoklī berzes spēks pielāgojas pieliktajam spēkam "
             "un nekad nav lielāks par maksimumu µ₀N.", GOLD),
            ("panelis", "TIPISKĀ KĻŪDA",
             ["Ja kaste stāv mierā un uz to darbojas 20 N, bet maksimālā "
              "miera berze ir 50 N, tad berzes spēks ir 20 N - NEVIS "
              "50 N. Formulu F(b) = µN lieto tikai slīdēšanas gadījumā "
              "vai maksimuma novērtēšanai."], NAVY),
        ]),
        ("Vilkt vai stumt", [
            ("divi",
             ("VILKT SLĪPI UZ AUGŠU", GREEN,
              ["N = mg − F·sin α.",
               "N samazinās → berze mazāka.",
               "Vieglāk pārvietot.",
               "Tā konstruēti čemodānu rokturi."]),
             ("STUMT SLĪPI UZ LEJU", RED,
              ["N = mg + F·sin α.",
               "N palielinās → berze lielāka.",
               "Grūtāk pārvietot.",
               "Tāpēc smagu kasti labāk vilkt."])),
            ("tabula",
             ["Solis", "Ko rēķina", "Formula"],
             [["1", "Spēka projekcijas", "Fₓ = F cos α; F_y = F sin α"],
              ["2", "Balsta reakcija", "N = mg ∓ F sin α"],
              ["3", "Berzes spēks", "F(b) = µN"],
              ["4", "Paātrinājums", "a = (Fₓ − F(b))/m"]],
             [1.90, 4.30, 6.03]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Vai sāks kustēties",
             teksts="Uz 15 kg kasti darbojas horizontāls spēks 40 N;\n"
                    "µ₀ = 0,40. Vai kaste sāks kustēties? "
                    "(g = 9,8 m/s²)",
             dots=["m = 15 kg", "F = 40 N", "µ₀ = 0,40"],
             jaaprekina=["F(b,max) = ?", "vai kustēsies?"],
             formulas=["N = mg", "F(b,max) = µ₀N"],
             aprekins=["1)  N = 15 · 9,8 = 147 N",
                       "2)  F(b,max) = 0,40 · 147 = 58,8 N",
                       "3)  40 N < 58,8 N → nekustēsies"],
             atbilde="Kaste paliks mierā; berzes spēks ir 40 N.",
             piezime="Berze pielāgojas pieliktajam spēkam, līdz sasniedz "
                     "maksimumu."),
        dict(nr=2, virsraksts="Slīpi vērsts spēks",
             teksts="Kasti (m = 20 kg) velk ar 100 N spēku 30° leņķī uz "
                    "augšu;\nµ = 0,30. Aprēķini paātrinājumu! "
                    "(sin 30° = 0,50; cos 30° = 0,87; g = 9,8 m/s²)",
             dots=["m = 20 kg", "F = 100 N", "α = 30°", "µ = 0,30"],
             jaaprekina=["a = ?"],
             formulas=["N = mg − F sin α", "F(b) = µN",
                       "a = (F cos α − F(b))/m"],
             aprekins=["1)  N = 196 − 100·0,50 = 146 N",
                       "2)  F(b) = 0,30 · 146 = 43,8 N",
                       "3)  a = (87 − 43,8) : 20 = 2,16 ≈ 2,2 m/s²"],
             atbilde="a ≈ 2,2 m/s²",
             piezime="Ja vilktu horizontāli, N = 196 N un a būtu tikai "
                     "2,1 m/s² - slīpā vilkšana ir izdevīgāka."),
        dict(nr=3, virsraksts="Stumt slīpi uz leju",
             teksts="To pašu kasti stumj ar 100 N 30° leņķī uz leju.\n"
                    "Aprēķini paātrinājumu un salīdzini ar 2. uzdevumu!",
             dots=["m = 20 kg", "F = 100 N", "α = 30° (lejup)",
                   "µ = 0,30"],
             jaaprekina=["a = ?"],
             formulas=["N = mg + F sin α", "F(b) = µN",
                       "a = (F cos α − F(b))/m"],
             aprekins=["1)  N = 196 + 50 = 246 N",
                       "2)  F(b) = 0,30 · 246 = 73,8 N",
                       "3)  a = (87 − 73,8) : 20 = 0,66 m/s²"],
             atbilde="a ≈ 0,66 m/s² - 3 reizes mazāks nekā velkot.",
             piezime="Tas fizikāli pamato, kāpēc čemodānus velk, nevis "
                     "stumj."),
        dict(nr=4, virsraksts="Berze un ceļš",
             teksts="Ķermenis ar 12 m/s slīd pa horizontālu virsmu un\n"
                    "apstājas berzes dēļ; µ = 0,25. Aprēķini ceļu un "
                    "laiku! (g = 9,8 m/s²)",
             dots=["v₀ = 12 m/s", "µ = 0,25", "v = 0"],
             jaaprekina=["s = ?", "t = ?"],
             formulas=["a = −µg", "s = v₀²/(2µg)", "t = v₀/(µg)"],
             aprekins=["1)  a = −0,25 · 9,8 = −2,45 m/s²",
                       "2)  s = 144 : (2·2,45) = 29,4 ≈ 29 m",
                       "3)  t = 12 : 2,45 ≈ 4,9 s"],
             atbilde="s ≈ 29 m ;   t ≈ 4,9 s",
             piezime="Masa neietekmē rezultātu - tā saīsinās abās "
                     "formulās."),
        dict(nr=5, virsraksts="Minimālais spēks kustības sākšanai",
             teksts="Cik liels horizontāls spēks vajadzīgs, lai 30 kg\n"
                    "kaste sāktu kustēties, ja µ₀ = 0,45? "
                    "(g = 9,8 m/s²)",
             dots=["m = 30 kg", "µ₀ = 0,45", "g = 9,8 m/s²"],
             jaaprekina=["F(min) = ?"],
             formulas=["N = mg", "F(min) = µ₀N"],
             aprekins=["1)  N = 30 · 9,8 = 294 N",
                       "2)  F(min) = 0,45 · 294",
                       "3)  F(min) = 132,3 ≈ 1,3·10² N"],
             atbilde="F(min) ≈ 1,3·10² N",
             piezime="Kad kaste sāk slīdēt, vajadzīgais spēks kļūst "
                     "mazāks - slīdēšanas berze ir mazāka par miera "
                     "berzi."),
        dict(nr=6, virsraksts="Kaste uz kravas platformas",
             teksts="Uz kravas automašīnas platformas stāv kaste; "
                    "µ₀ = 0,30.\nAr cik lielu paātrinājumu automašīna "
                    "drīkst palielināt\nātrumu, lai kaste neslīdētu? "
                    "(g = 9,8 m/s²)",
             dots=["µ₀ = 0,30", "g = 9,8 m/s²"],
             jaaprekina=["a(max) = ?"],
             formulas=["Kasti paātrina berze: ma ≤ µ₀mg",
                       "a(max) = µ₀g"],
             aprekins=["1)  ma = F(b) ≤ µ₀mg",
                       "2)  Masa saīsinās: a ≤ µ₀g",
                       "3)  a(max) = 0,30 · 9,8 = 2,94 m/s²"],
             atbilde="a(max) ≈ 2,9 m/s²",
             piezime="Rezultāts nav atkarīgs no kastes masas - tā "
                     "saīsinās abās pusēs."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Miera berze pielāgojas pieliktajam spēkam līdz µ₀N.",
            "Velkot slīpi uz augšu, N un berze samazinās.",
            "Stumjot slīpi uz leju, N un berze palielinās.",
            "Berzes uzdevumos masa bieži saīsinās.",
        ],
        majasdarbs=[
            "m = 25 kg, F = 60 N horizontāli, µ₀ = 0,30. Vai sāks "
            "kustēties?",
            "m = 18 kg, F = 80 N 45° uz augšu, µ = 0,25. Aprēķini a. "
            "(sin 45° = cos 45° = 0,71)",
            "v₀ = 8,0 m/s, µ = 0,20. Aprēķini s un t līdz apstāšanās.",
        ],
        pasvertejums=["Protu noteikt, vai sāksies kustība",
                      "Protu strādāt ar slīpi vērstu spēku",
                      "Protu kombinēt berzi ar kinemātiku",
                      "Protu pamatot, kāpēc vilkt vieglāk"],
        nakama="Nākamā stunda: slīpā plakne."),
),

dict(
    nr="3.12", virsraksts="Slīpā plakne",
    jautajums="Kā spēku sadala uz slīpas virsmas?",
    apaksraksts="mg sin α · mg cos α · Asis gar plakni",
    merkis="Iemācīties sadalīt smaguma spēku uz slīpas plaknes un "
           "uzrakstīt kustības vienādojumus.",
    protu=["izvēlēties asis gar slīpo plakni;",
           "sadalīt smaguma spēku divās projekcijās;",
           "aprēķināt paātrinājumu bez berzes;",
           "pamatot, kāpēc N = mg cos α."],
    atkartojums="3.7. stundā redzējām N = mg cos α. Tagad izpratīsim, no "
                "kurienes tas nāk, un iemācīsimies rēķināt kustību pa "
                "slīpu plakni.",
    uzdevumu_apraksts="Smaguma spēka sadalīšana un paātrinājums",
    teorija=[
        ("Asis un projekcijas", [
            ("formula", "SMAGUMA SPĒKA PROJEKCIJAS",
             "Gar plakni:  mg · sin α        "
             "Perpendikulāri plaknei:  mg · cos α",
             "Asis izvēlas GAR plakni un PERPENDIKULĀRI tai - tad "
             "paātrinājums ir tikai pa vienu asi, un uzdevums kļūst "
             "vienkāršs.", GOLD),
            ("tabula",
             ["Leņķis α", "sin α", "cos α", "a bez berzes"],
             [["10°", "0,17", "0,98", "1,7 m/s²"],
              ["30°", "0,50", "0,87", "4,9 m/s²"],
              ["45°", "0,71", "0,71", "6,9 m/s²"],
              ["60°", "0,87", "0,50", "8,5 m/s²"],
              ["90°", "1", "0", "9,8 m/s² (krišana)"]],
             [2.90, 2.60, 2.60, 4.13]),
        ]),
        ("Vienādojumi", [
            ("panelis", "DIVI VIENĀDOJUMI",
             ["Gar plakni:  mg·sin α − F(b) = ma  →  a = g(sin α − "
              "µ·cos α).  Perpendikulāri:  N − mg·cos α = 0  →  "
              "N = mg·cos α.  Ievēro: masa saīsinās, tāpēc paātrinājums "
              "nav atkarīgs no masas."], NAVY),
            ("kartitas", [
                ("BEZ BERZES", GREEN,
                 ["a = g sin α",
                  "Jo stāvāka plakne, jo lielāks a.",
                  "Pie α = 90° a = g."]),
                ("AR BERZI", BLUE,
                 ["a = g(sin α − µ cos α)",
                  "Var būt arī nulle.",
                  "Ja negatīvs - nekustas."]),
                ("SLĪDĒŠANAS SĀKUMS", GOLD,
                 ["tg α = µ₀",
                  "Kritiskais leņķis.",
                  "Tā mēra µ."]),
            ]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Paātrinājums bez berzes",
             teksts="Ķermenis slīd pa gludu slīpu plakni ar leņķi 30°.\n"
                    "Aprēķini paātrinājumu! (sin 30° = 0,50; "
                    "g = 9,8 m/s²)",
             dots=["α = 30°", "berzes nav", "g = 9,8 m/s²"],
             jaaprekina=["a = ?"],
             formulas=["a = g · sin α"],
             aprekins=["1)  sin 30° = 0,50",
                       "2)  a = 9,8 · 0,50",
                       "3)  a = 4,9 m/s²"],
             atbilde="a = 4,9 m/s², vērsts gar plakni lejup.",
             piezime="Tieši puse no g - loģiski, jo sin 30° = 0,5."),
        dict(nr=2, virsraksts="Paātrinājums ar berzi",
             teksts="Tā pati plakne, bet µ = 0,20. Aprēķini "
                    "paātrinājumu!\n(sin 30° = 0,50; cos 30° = 0,87)",
             dots=["α = 30°", "µ = 0,20", "g = 9,8 m/s²"],
             jaaprekina=["a = ?"],
             formulas=["a = g(sin α − µ cos α)"],
             aprekins=["1)  µ cos α = 0,20 · 0,87 = 0,174",
                       "2)  sin α − µ cos α = 0,50 − 0,174 = 0,326",
                       "3)  a = 9,8 · 0,326 = 3,2 m/s²"],
             atbilde="a ≈ 3,2 m/s²",
             piezime="Berze samazināja paātrinājumu par trešdaļu."),
        dict(nr=3, virsraksts="Kritiskais leņķis",
             teksts="Pie kāda plaknes leņķa ķermenis sāks slīdēt, ja\n"
                    "µ₀ = 0,50? Kā šo faktu izmanto berzes koeficienta\n"
                    "mērīšanai?",
             dots=["µ₀ = 0,50"],
             jaaprekina=["α = ?"],
             formulas=["Slīdēšana sākas, ja mg sin α > µ₀ mg cos α",
                       "tg α = µ₀"],
             aprekins=["1)  tg α = 0,50",
                       "2)  α = arctg 0,50",
                       "3)  α ≈ 27°"],
             atbilde="α ≈ 27°. Pakāpeniski ceļot plakni un fiksējot "
                     "leņķi, kurā sākas slīdēšana, var izmērīt µ₀.",
             piezime="Vienkāršs un precīzs veids berzes koeficienta "
                     "noteikšanai."),
        dict(nr=4, virsraksts="Balsta reakcija un berze",
             teksts="Kaste (m = 40 kg) uz plaknes ar leņķi 25°;\n"
                    "µ = 0,35. Aprēķini N un berzes spēku!\n"
                    "(sin 25° = 0,42; cos 25° = 0,91; g = 9,8 m/s²)",
             dots=["m = 40 kg", "α = 25°", "µ = 0,35"],
             jaaprekina=["N = ?", "F(b) = ?"],
             formulas=["N = mg cos α", "F(b) = µN"],
             aprekins=["1)  mg = 40 · 9,8 = 392 N",
                       "2)  N = 392 · 0,91 = 357 N",
                       "3)  F(b) = 0,35 · 357 = 125 ≈ 1,3·10² N"],
             atbilde="N ≈ 3,6·10² N ;   F(b) ≈ 1,3·10² N",
             piezime="Salīdzini: mg sin α = 165 N > 125 N, tāpēc kaste "
                     "slīdēs."),
        dict(nr=5, virsraksts="Vai noturēsies uz plaknes",
             teksts="Kaste stāv uz plaknes ar leņķi 15°; µ₀ = 0,30.\n"
                    "Vai tā noslīdēs? (sin 15° = 0,26; cos 15° = 0,97)",
             dots=["α = 15°", "µ₀ = 0,30"],
             jaaprekina=["tg α = ?", "vai slīdēs?"],
             formulas=["Slīd, ja tg α > µ₀"],
             aprekins=["1)  tg 15° = 0,26 : 0,97 = 0,27",
                       "2)  µ₀ = 0,30",
                       "3)  0,27 < 0,30 → nenoslīdēs"],
             atbilde="Kaste paliks mierā, jo tg α < µ₀.",
             piezime="Kritiskais leņķis šeit ir arctg 0,30 ≈ 17°."),
        dict(nr=6, virsraksts="Bremzēšana, slīdot augšup",
             teksts="Ķermenis slīd augšup pa plakni ar leņķi 30°;\n"
                    "µ = 0,20. Aprēķini paātrinājumu!\n"
                    "(sin 30° = 0,50; cos 30° = 0,87; g = 9,8 m/s²)",
             dots=["α = 30°", "µ = 0,20", "kustība augšup"],
             jaaprekina=["a = ?"],
             formulas=["Augšup berze vērsta lejup",
                       "a = g(sin α + µ cos α)"],
             aprekins=["1)  µ cos α = 0,20 · 0,87 = 0,174",
                       "2)  sin α + µ cos α = 0,50 + 0,174 = 0,674",
                       "3)  a = 9,8 · 0,674 = 6,6 m/s² (bremzēšana)"],
             atbilde="a ≈ 6,6 m/s², vērsts gar plakni lejup.",
             piezime="Slīdot augšup, berze un smaguma spēka projekcija "
                     "darbojas VIENĀ virzienā - tāpēc a ir lielāks nekā "
                     "slīdot lejup."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Asis izvēlas gar plakni un perpendikulāri tai.",
            "Gar plakni: mg sin α; perpendikulāri: mg cos α.",
            "a = g(sin α − µ cos α); masa saīsinās.",
            "Slīdēšana sākas, kad tg α = µ₀.",
        ],
        majasdarbs=[
            "α = 40°, berzes nav (sin 40° = 0,64). Aprēķini a.",
            "α = 20°, µ = 0,15 (sin 20° = 0,34; cos 20° = 0,94). "
            "Aprēķini a.",
            "µ₀ = 0,70. Aprēķini kritisko leņķi.",
        ],
        pasvertejums=["Protu izvēlēties asis",
                      "Protu sadalīt smaguma spēku",
                      "Protu rēķināt a ar berzi un bez tās",
                      "Protu atrast kritisko leņķi"],
        nakama="Nākamā stunda: uzdevumi par slīpo plakni."),
),

dict(
    nr="3.13", virsraksts="Uzdevumi: slīpā plakne",
    jautajums="Kad ķermenis sāk slīdēt?",
    apaksraksts="Kombinēti uzdevumi · Ātrums plaknes galā · Līdzsvars",
    merkis="Nostiprināt slīpās plaknes uzdevumus, kombinējot dinamiku "
           "ar kinemātiku.",
    protu=["kombinēt slīpās plaknes formulas ar kinemātiku;",
           "aprēķināt ātrumu plaknes galā;",
           "atrast spēku, kas notur ķermeni;",
           "risināt uzdevumus ar mainīgu leņķi."],
    atkartojums="3.12. stundā ieguvām a = g(sin α − µ cos α). Šodien šo "
                "paātrinājumu izmantosim kinemātikas formulās.",
    uzdevumu_apraksts="Slīpā plakne kopā ar kinemātiku",
    teorija=[
        ("Divu soļu shēma", [
            ("panelis", "TIPISKS RISINĀJUMA CEĻŠ",
             ["1. solis - no spēkiem atrod paātrinājumu:",
              "a = g(sin α − µ cos α)",
              "2. solis - ar kinemātikas formulām atrod ātrumu, laiku "
              "vai ceļu:",
              "v² = 2as;  s = at²/2",
              "Ja jautā par noturēšanu, tad a = 0 un meklē vajadzīgo "
              "spēku."], NAVY),
            ("tabula",
             ["Jautājums", "1. solis", "2. solis"],
             [["Ātrums plaknes galā", "a = g(sin α − µ cos α)",
               "v = √(2as)"],
              ["Nolaišanās laiks", "tas pats a", "t = √(2s/a)"],
              ["Noturošais spēks", "a = 0", "F = mg sin α + µN vai −"],
              ["Vai slīdēs", "salīdzina mg sin α un µN", "secinājums"]],
             [3.90, 4.60, 3.73]),
        ]),
        ("Uzmanību ar zīmēm", [
            ("kartitas", [
                ("SLĪD LEJUP", BLUE,
                 ["Berze vērsta uz augšu.",
                  "a = g(sin α − µ cos α)"]),
                ("VELK UZ AUGŠU", RED,
                 ["Berze vērsta lejup.",
                  "F = mg sin α + µmg cos α"]),
                ("NOTUR MIERĀ", GREEN,
                 ["a = 0.",
                  "Berze var palīdzēt vai traucēt."]),
            ]),
            ("formula", "SPĒKS, LAI VILKTU AUGŠUP VIENMĒRĪGI",
             "F = mg (sin α + µ · cos α)",
             "Velkot uz augšu, gan smaguma spēka komponente, gan berze "
             "darbojas pretī - tāpēc spēki saskaitās.", GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Ātrums plaknes galā",
             teksts="Ķermenis no miera slīd 8,0 m pa plakni ar leņķi 30°;\n"
                    "µ = 0,20. Aprēķini ātrumu plaknes galā!\n"
                    "(sin 30° = 0,50; cos 30° = 0,87)",
             dots=["s = 8,0 m", "α = 30°", "µ = 0,20", "v₀ = 0"],
             jaaprekina=["a = ?", "v = ?"],
             formulas=["a = g(sin α − µ cos α)", "v = √(2as)"],
             aprekins=["1)  a = 9,8(0,50 − 0,174) = 3,19 m/s²",
                       "2)  2as = 2 · 3,19 · 8,0 = 51,1 m²/s²",
                       "3)  v = 7,15 ≈ 7,1 m/s"],
             atbilde="v ≈ 7,1 m/s",
             piezime="Bez berzes būtu 8,9 m/s - berze «apēd» ceturto "
                     "daļu ātruma."),
        dict(nr=2, virsraksts="Nolaišanās laiks",
             teksts="Izmantojot 1. uzdevuma datus, aprēķini nolaišanās\n"
                    "laiku!",
             dots=["s = 8,0 m", "a = 3,19 m/s²", "v₀ = 0"],
             jaaprekina=["t = ?"],
             formulas=["s = at²/2", "t = √(2s/a)"],
             aprekins=["1)  2s/a = 16 : 3,19 = 5,02 s²",
                       "2)  t = 2,24 s",
                       "3)  Pārbaude: v = at = 3,19 · 2,24 = 7,1 m/s ✔"],
             atbilde="t ≈ 2,2 s",
             piezime="Pārbaude ar otru formulu apstiprina rezultātu."),
        dict(nr=3, virsraksts="Vilkšana augšup",
             teksts="Kasti (m = 50 kg) velk vienmērīgi augšup pa plakni\n"
                    "ar leņķi 20°; µ = 0,30. Aprēķini vajadzīgo spēku!\n"
                    "(sin 20° = 0,34; cos 20° = 0,94; g = 9,8 m/s²)",
             dots=["m = 50 kg", "α = 20°", "µ = 0,30", "vienmērīgi"],
             jaaprekina=["F = ?"],
             formulas=["F = mg(sin α + µ cos α)"],
             aprekins=["1)  mg = 50 · 9,8 = 490 N",
                       "2)  sin α + µ cos α = 0,34 + 0,282 = 0,622",
                       "3)  F = 490 · 0,622 = 305 ≈ 3,0·10² N"],
             atbilde="F ≈ 3,0·10² N",
             piezime="Bez slīpās plaknes tieši pacelt vajadzētu 490 N - "
                     "plakne ir vienkāršais mehānisms."),
        dict(nr=4, virsraksts="Vai noturēsies",
             teksts="Kaste stāv uz plaknes ar leņķi 35°; µ₀ = 0,60.\n"
                    "Vai tā noslīdēs? (sin 35° = 0,57; cos 35° = 0,82)",
             dots=["α = 35°", "µ₀ = 0,60"],
             jaaprekina=["vai slīdēs?"],
             formulas=["Slīd, ja mg sin α > µ₀ mg cos α",
                       "jeb tg α > µ₀"],
             aprekins=["1)  tg 35° = 0,57 : 0,82 = 0,70",
                       "2)  µ₀ = 0,60",
                       "3)  0,70 > 0,60 → slīdēs"],
             atbilde="Kaste noslīdēs, jo tg α > µ₀.",
             piezime="Kritiskais leņķis šeit ir arctg 0,60 ≈ 31°."),
        dict(nr=5, virsraksts="Cik tālu uzslīdēs",
             teksts="Ķermenim plaknes apakšā dod ātrumu 6,0 m/s augšup;\n"
                    "α = 30°, µ = 0,20. Cik tālu tas uzslīdēs?\n"
                    "(sin 30° = 0,50; cos 30° = 0,87; g = 9,8 m/s²)",
             dots=["v₀ = 6,0 m/s", "α = 30°", "µ = 0,20", "v = 0"],
             jaaprekina=["a = ?", "s = ?"],
             formulas=["a = g(sin α + µ cos α)", "s = v₀²/(2a)"],
             aprekins=["1)  a = 9,8 · (0,50 + 0,174) = 6,61 m/s²",
                       "2)  v₀² = 36 m²/s²",
                       "3)  s = 36 : (2 · 6,61) = 2,7 m"],
             atbilde="s ≈ 2,7 m gar plakni",
             piezime="Bez berzes ķermenis uzslīdētu 3,7 m - berze "
                     "saīsina ceļu par ceturto daļu."),
        dict(nr=6, virsraksts="Plaknes garums un spēks",
             teksts="Kravu (m = 80 kg) paceļ 1,5 m augstumā pa gludu "
                    "plakni\nar leņķi 30°. Aprēķini plaknes garumu un "
                    "vajadzīgo spēku!\n(sin 30° = 0,50; g = 9,8 m/s²)",
             dots=["m = 80 kg", "h = 1,5 m", "α = 30°", "berzes nav"],
             jaaprekina=["l = ?", "F = ?"],
             formulas=["h = l · sin α", "F = mg · sin α"],
             aprekins=["1)  l = 1,5 : 0,50 = 3,0 m",
                       "2)  mg = 80 · 9,8 = 784 N",
                       "3)  F = 784 · 0,50 = 392 N"],
             atbilde="l = 3,0 m ;   F = 392 N ≈ 3,9·10² N",
             piezime="Ceļš divreiz garāks, spēks divreiz mazāks - "
                     "vienkāršais mehānisms spēku ietaupa, darbu - nē."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Vispirms atrod a, tad lieto kinemātikas formulas.",
            "Slīdot lejup berze vērsta augšup un otrādi.",
            "Velkot augšup: F = mg(sin α + µ cos α).",
            "Slīdēšanas nosacījums: tg α > µ₀.",
        ],
        majasdarbs=[
            "s = 12 m, α = 25°, µ = 0,15. Aprēķini a, v un t. "
            "(sin 25° = 0,42; cos 25° = 0,91)",
            "m = 30 kg, α = 15°, µ = 0,25. Aprēķini spēku vilkšanai "
            "augšup. (sin 15° = 0,26; cos 15° = 0,97)",
            "µ₀ = 0,45. Vai kaste noturēsies uz plaknes ar 20° leņķi?",
        ],
        pasvertejums=["Protu atrast a uz slīpas plaknes",
                      "Protu apvienot ar kinemātiku",
                      "Protu rēķināt vilkšanas spēku",
                      "Protu noteikt, vai slīdēs"],
        nakama="Nākamā stunda: ķermeņu sistēmas."),
),

dict(
    nr="3.14", virsraksts="Ķermeņu sistēmas",
    jautajums="Kā rēķina ar diviem saistītiem ķermeņiem?",
    apaksraksts="Kopējā masa · Virves spraigums · Divi vienādojumi",
    merkis="Iemācīties risināt uzdevumus par diviem vai vairākiem "
           "saistītiem ķermeņiem.",
    protu=["uzrakstīt vienādojumus katram ķermenim;",
           "izmantot kopējās masas metodi;",
           "aprēķināt virves spraigumu;",
           "pārbaudīt rezultātu abās metodēs."],
    atkartojums="Līdz šim rēķinājām vienu ķermeni. Reālās situācijās "
                "bieži ir divi saistīti ķermeņi - vilcējs un piekabe, "
                "divi atsvari pār bloku.",
    uzdevumu_apraksts="Saistīti ķermeņi un virves spraigums",
    teorija=[
        ("Divas metodes", [
            ("divi",
             ("KOPĒJĀS MASAS METODE", GREEN,
              ["Sistēmu skata kā vienu ķermeni.",
               "a = ΣF(ārējie) / Σm.",
               "Ātri atrod paātrinājumu.",
               "Spraigumu neatrod."]),
             ("ATSEVIŠĶO ĶERMEŅU METODE", BLUE,
              ["Katram ķermenim savs vienādojums.",
               "Iekšējie spēki parādās.",
               "Atrod arī spraigumu T.",
               "Divi vienādojumi, divi nezināmie."])),
            ("formula", "TIPISKS PIEMĒRS",
             "m₁ un m₂ savienoti ar virvi, velk ar spēku F:        "
             "a = F / (m₁ + m₂)        T = m₂ · a",
             "Spraigumu vienmēr atrod, rakstot vienādojumu TAM ķermenim, "
             "uz kuru darbojas mazāk spēku.", GOLD),
        ]),
        ("Bloks un divi atsvari", [
            ("panelis", "ATVUDA MAŠĪNA",
             ["Divi atsvari pār bloku: smagākais velk vieglāko.",
              "a = (m₁ − m₂)g/(m₁ + m₂)",
              "T = 2m₁m₂g/(m₁ + m₂)",
              "Ja masas vienādas, a = 0 un T = mg."], NAVY),
            ("tabula",
             ["Sistēma", "Paātrinājums", "Spraigums"],
             [["Divi ķermeņi, velk ar F", "a = F/(m₁+m₂)", "T = m₂a"],
              ["Bloks, divi atsvari", "a = (m₁−m₂)g/(m₁+m₂)",
               "T = 2m₁m₂g/(m₁+m₂)"],
              ["Kaste velk kasti ar berzi", "a = (F − µΣmg)/Σm",
               "T = m₂(a + µg)"]],
             [4.30, 4.30, 3.63]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Divi ķermeņi uz gludas virsmas",
             teksts="Divas kastes (m₁ = 3,0 kg un m₂ = 5,0 kg) savienotas\n"
                    "ar virvi; pirmo velk ar 24 N. Berzes nav.\n"
                    "Aprēķini paātrinājumu un virves spraigumu!",
             dots=["m₁ = 3,0 kg", "m₂ = 5,0 kg", "F = 24 N"],
             jaaprekina=["a = ?", "T = ?"],
             formulas=["a = F/(m₁+m₂)", "T = m₂a"],
             aprekins=["1)  Σm = 8,0 kg",
                       "2)  a = 24 : 8,0 = 3,0 m/s²",
                       "3)  T = 5,0 · 3,0 = 15 N"],
             atbilde="a = 3,0 m/s² ;   T = 15 N",
             piezime="Pārbaude 1. ķermenim: 24 − 15 = 9 N = 3,0 · 3,0 ✔"),
        dict(nr=2, virsraksts="Atsvari pār bloku",
             teksts="Pār bloku pārmesta virve ar atsvariem 4,0 kg un\n"
                    "6,0 kg. Aprēķini paātrinājumu un spraigumu! "
                    "(g = 9,8 m/s²)",
             dots=["m₁ = 6,0 kg", "m₂ = 4,0 kg", "g = 9,8 m/s²"],
             jaaprekina=["a = ?", "T = ?"],
             formulas=["a = (m₁−m₂)g/(m₁+m₂)", "T = m₂(g + a)"],
             aprekins=["1)  a = (6,0 − 4,0) · 9,8 : 10,0 = 1,96 m/s²",
                       "2)  T = 4,0 · (9,8 + 1,96)",
                       "3)  T = 4,0 · 11,76 = 47 N"],
             atbilde="a ≈ 2,0 m/s² ;   T ≈ 47 N",
             piezime="Pārbaude smagajam: 58,8 − 47 = 11,8 N = "
                     "6,0 · 1,96 ✔"),
        dict(nr=3, virsraksts="Ar berzi",
             teksts="Divas kastes (2,0 kg un 4,0 kg) uz virsmas ar\n"
                    "µ = 0,20 velk ar 30 N. Aprēķini paātrinājumu!\n"
                    "(g = 9,8 m/s²)",
             dots=["m₁ = 2,0 kg", "m₂ = 4,0 kg", "F = 30 N",
                   "µ = 0,20"],
             jaaprekina=["a = ?"],
             formulas=["F(b) = µ(m₁+m₂)g", "a = (F − F(b))/Σm"],
             aprekins=["1)  Σm = 6,0 kg ;  N = 58,8 N",
                       "2)  F(b) = 0,20 · 58,8 = 11,8 N",
                       "3)  a = (30 − 11,8) : 6,0 = 3,03 ≈ 3,0 m/s²"],
             atbilde="a ≈ 3,0 m/s²",
             piezime="Berzi rēķina no KOPĒJĀS masas, jo abas kastes "
                     "spiež uz virsmu."),
        dict(nr=4, virsraksts="Automašīna ar piekabi",
             teksts="Automašīna (1200 kg) velk piekabi (400 kg) ar\n"
                    "paātrinājumu 1,5 m/s². Aprēķini vilcēja spēku uz\n"
                    "piekabi un dzinēja radīto kopspēku!",
             dots=["m₁ = 1200 kg", "m₂ = 400 kg", "a = 1,5 m/s²"],
             jaaprekina=["T = ?", "F = ?"],
             formulas=["T = m₂a", "F = (m₁+m₂)a"],
             aprekins=["1)  T = 400 · 1,5 = 600 N",
                       "2)  Σm = 1600 kg",
                       "3)  F = 1600 · 1,5 = 2400 N"],
             atbilde="T = 6,0·10² N ;   F = 2,4·10³ N",
             piezime="Sakabes spēks ir tikai ceturtā daļa no kopējā - "
                     "proporcionāli masām."),
        dict(nr=5, virsraksts="Trīs kastes virknē",
             teksts="Trīs kastes (1,0 kg; 2,0 kg; 3,0 kg) savienotas ar\n"
                    "virvēm un tiek vilktas ar 12 N. Berzes nav.\n"
                    "Aprēķini paātrinājumu un abu virvju spraigumus!",
             dots=["m₁ = 1,0 kg", "m₂ = 2,0 kg", "m₃ = 3,0 kg",
                   "F = 12 N"],
             jaaprekina=["a = ?", "T₁ = ?", "T₂ = ?"],
             formulas=["a = F/Σm", "T₁ = (m₂+m₃)a", "T₂ = m₃a"],
             aprekins=["1)  Σm = 6,0 kg → a = 12 : 6,0 = 2,0 m/s²",
                       "2)  T₁ = (2,0 + 3,0) · 2,0 = 10 N",
                       "3)  T₂ = 3,0 · 2,0 = 6,0 N"],
             atbilde="a = 2,0 m/s² ;   T₁ = 10 N ;   T₂ = 6,0 N",
             piezime="Katra virve velk tikai to masu, kas atrodas aiz "
                     "tās."),
        dict(nr=6, virsraksts="Kaste uz galda un pār bloku",
             teksts="Uz gluda galda ir 2,0 kg kaste, savienota pār bloku\n"
                    "ar 3,0 kg atsvaru. Aprēķini paātrinājumu un virves\n"
                    "spraigumu! (g = 9,8 m/s²)",
             dots=["m₁ = 2,0 kg (uz galda)", "m₂ = 3,0 kg (karājas)",
                   "berzes nav"],
             jaaprekina=["a = ?", "T = ?"],
             formulas=["a = m₂g/(m₁+m₂)", "T = m₁a"],
             aprekins=["1)  Σm = 5,0 kg",
                       "2)  a = 3,0 · 9,8 : 5,0 = 5,88 m/s²",
                       "3)  T = 2,0 · 5,88 = 11,8 N"],
             atbilde="a ≈ 5,9 m/s² ;   T ≈ 12 N",
             piezime="Pārbaude atsvaram: 29,4 − 11,8 = 17,6 N = "
                     "3,0 · 5,88 ✔"),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Paātrinājumu ātri atrod ar kopējās masas metodi.",
            "Spraigumu atrod, rakstot vienādojumu vienam ķermenim.",
            "Blokam: a = (m₁−m₂)g/(m₁+m₂).",
            "Rezultātu vienmēr pārbauda otram ķermenim.",
        ],
        majasdarbs=[
            "m₁ = 2,0 kg, m₂ = 6,0 kg, F = 32 N, berzes nav. Aprēķini a "
            "un T.",
            "Bloks: m₁ = 5,0 kg, m₂ = 3,0 kg. Aprēķini a un T.",
            "Automašīna 1000 kg, piekabe 500 kg, a = 2,0 m/s². Aprēķini "
            "T un F.",
        ],
        pasvertejums=["Protu lietot kopējās masas metodi",
                      "Protu rēķināt spraigumu",
                      "Protu strādāt ar bloku",
                      "Protu pārbaudīt rezultātu"],
        nakama="Nākamā stunda: spiediens cietās vielās."),
),

]
