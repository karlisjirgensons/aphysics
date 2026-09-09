# -*- coding: utf-8 -*-
"""10. temats "Līdzstrāva". B daļa: 10.6.-10.10. stunda.

10.6. sagatavo LD2 (Oma likums un rezistoru slēgumi), kas notiek
nākamajā dubultstundā.
"""

from fiz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN     # noqa: F401
from fiz_t10a import TEMATS, KICKER, KURSS, MAPE              # noqa: F401

STUNDAS = [

dict(
    nr="10.6", virsraksts="LD2 sagatavošana",
    jautajums="Ko un kā mērīsim elektriskajā ķēdē?",
    apaksraksts="Shēma · Mēraparātu diapazoni · Datu tabula",
    merkis="Uzzīmēt LD2 shēmu, noteikt mērāmos lielumus un diapazonus un "
           "sagatavot datu tabulu.",
    protu=["uzzīmēt darba shēmu ar apzīmējumiem;",
           "izvēlēties mēraparāta diapazonu;",
           "sagatavot datu tabulu;",
           "nosaukt drošības noteikumus."],
    atkartojums="Iepriekšējās stundās apguvām Oma likumu un abus "
                "slēgumus. Laboratorijas darbā to pašu pārbaudīsim ar "
                "mērījumiem.",
    uzdevumu_apraksts="Mērījumu plānošana un diapazoni",
    teorija=[
        ("LD2 plāns", [
            ("panelis", "PĒTĀMAIS JAUTĀJUMS UN GAITA",
             ["Jautājums: kā mainās strāva, mainot spriegumu uz "
              "rezistora, un vai R paliek nemainīga?",
              "Gaita: saslēdz ķēdi ar avotu, rezistoru, ampērmetru "
              "virknē un voltmetru paralēli; maina spriegumu 5 soļos un "
              "pieraksta U un I.",
              "Otrā daļa: saslēdz divus rezistorus vispirms virknē, tad "
              "paralēli, un salīdzina izmērīto R ar aprēķināto."],
             NAVY),
            ("tabula",
             ["Mērījums", "U (V)", "I (A)", "R = U/I"],
             [["1.", "2,0", "", ""],
              ["2.", "4,0", "", ""],
              ["3.", "6,0", "", ""],
              ["4.", "8,0", "", ""]],
             [2.60, 3.00, 3.00, 3.63]),
        ]),
        ("Mēraparāti un drošība", [
            ("divi",
             ("DIAPAZONA IZVĒLE", BLUE,
              ["Sāk ar LIELĀKO diapazonu.",
               "Ja rādījums mazs -",
               "pārslēdz uz mazāku.",
               "Gaidāmā strāva līdz 0,5 A -",
               "izvēlas 1 A diapazonu."]),
             ("KĻŪDU AVOTI", RED,
              ["Vāji kontakti.",
               "Rezistors sakarst - R aug.",
               "Nolasa pa daļai skalas.",
               "Nesagaida rādījuma",
               "nostabilizēšanos."])),
            ("panelis", "DROŠĪBAS NOTEIKUMI LD2",
             ["Ķēdi saslēdz ar IZSLĒGTU avotu; ieslēdz tikai pēc "
              "skolotāja pārbaudes.",
              "Ampērmetru nekad neslēdz paralēli avotam - tas ir "
              "īsslēgums.",
              "Spriegums nepārsniedz 12 V; ja kāds elements sakarst vai "
              "smird, avotu nekavējoties izslēdz."], RED),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Gaidāmā strāva",
             teksts="Ķēdē būs rezistors 47 Ω un spriegums līdz 12 V.\n"
                    "Cik liela būs lielākā strāva un kādu ampērmetra\n"
                    "diapazonu izvēlēties?",
             dots=["R = 47 Ω", "U(max) = 12 V"],
             jaaprekina=["I(max) = ?"],
             formulas=["I = U/R"],
             aprekins=["1)  I = 12 : 47 ≈ 0,26 A",
                       "2)  Vajag diapazonu virs 0,26 A",
                       "3)  Izvēlas 1 A diapazonu"],
             atbilde="I ≈ 0,26 A;  diapazons 1 A",
             piezime="Diapazonu vienmēr izvēlas ar rezervi, bet ne pārāk "
                     "lielu - citādi nolasīšana kļūst neprecīza."),
        dict(nr=2, virsraksts="Pretestība no mērījuma",
             teksts="Mērījumā ieguva U = 6,0 V un I = 0,125 A.\n"
                    "Aprēķini pretestību un salīdzini ar nominālo 47 Ω!",
             dots=["U = 6,0 V", "I = 0,125 A", "R(nom) = 47 Ω"],
             jaaprekina=["R = ?"],
             formulas=["R = U/I"],
             aprekins=["1)  R = 6,0 : 0,125 = 48 Ω",
                       "2)  Starpība: 48 − 47 = 1 Ω",
                       "3)  Novirze apmēram 2 %"],
             atbilde="R = 48 Ω - atbilst nominālam",
             piezime="Rezistoriem pieļaujamā novirze parasti ir 5 % - "
                     "2 % ir labs rezultāts."),
        dict(nr=3, virsraksts="Paredzi rezultātu",
             teksts="LD2 otrajā daļā būs rezistori 47 Ω un 100 Ω.\n"
                    "Aprēķini gaidāmo pretestību virknē un paralēli!",
             dots=["R₁ = 47 Ω", "R₂ = 100 Ω"],
             jaaprekina=["R(virknē) = ?", "R(paralēli) = ?"],
             formulas=["R = R₁ + R₂", "R = R₁R₂/(R₁ + R₂)"],
             aprekins=["1)  Virknē: 47 + 100 = 147 Ω",
                       "2)  R₁R₂ = 4700;  R₁ + R₂ = 147",
                       "3)  Paralēli: 4700 : 147 ≈ 32 Ω"],
             atbilde="147 Ω virknē;  ≈ 32 Ω paralēli",
             piezime="Paredzētais rezultāts palīdz uzreiz pamanīt "
                     "mērījuma kļūdu."),
        dict(nr=4, virsraksts="Kļūdas novērtējums",
             teksts="Voltmetra nolasīšanas kļūda ir 0,1 V pie rādījuma\n"
                    "6,0 V. Cik procentu tā ir?",
             dots=["U = 6,0 V", "ΔU = 0,1 V"],
             jaaprekina=["Relatīvā kļūda = ?"],
             formulas=["δ = ΔU/U"],
             aprekins=["1)  δ = 0,1 : 6,0",
                       "2)  δ ≈ 0,017",
                       "3)  δ ≈ 1,7 %"],
             atbilde="δ ≈ 1,7 %",
             piezime="Jo lielāks rādījums skalā, jo mazāka relatīvā "
                     "kļūda - tāpēc mēra tuvāk skalas beigām."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Pirms mērījumiem uzzīmē shēmu un sagatavo tabulu.",
            "Mēraparāta diapazonu izvēlas ar nelielu rezervi.",
            "Gaidāmo rezultātu aprēķina iepriekš.",
            "Ķēdi saslēdz ar izslēgtu avotu.",
        ],
        majasdarbs=[
            "Uzzīmē LD2 shēmu ar visiem apzīmējumiem.",
            "Sagatavo datu tabulu ar 5 mērījumiem.",
            "Aprēķini gaidāmo strāvu pie 10 V un R = 100 Ω.",
        ],
        pasvertejums=["Protu uzzīmēt shēmu",
                      "Protu izvēlēties diapazonu",
                      "Esmu sagatavojis tabulu",
                      "Zinu drošības noteikumus"],
        nakama="Nākamā stunda: LD2 - mērījumi dubultstundā."),
),

dict(
    nr="10.7", virsraksts="Jauda un elektroenerģija",
    jautajums="Cik enerģijas patērē mājokļa ierīces?",
    apaksraksts="P = UI · E = Pt · 1 kWh = 3,6·10⁶ J · Tarifs",
    merkis="Lietot P = UI un E = Pt, pāriet starp enerģijas mērvienībām "
           "un aprēķināt izmaksas pēc tarifa.",
    protu=["lietot P = UI;",
           "lietot P = I²R un P = U²/R;",
           "aprēķināt enerģiju E = Pt;",
           "pārrēķināt džoulus kilovatstundās un aprēķināt izmaksas."],
    atkartojums="5. tematā jauda bija darbs dalīts ar laiku. "
                "Elektriskajā ķēdē jauda ir sprieguma un strāvas "
                "reizinājums - bet jēga ir tā pati.",
    uzdevumu_apraksts="Jaudas un patēriņa aprēķini",
    teorija=[
        ("Elektriskā jauda", [
            ("formula", "JAUDA UN ENERĢIJA",
             "P = UI        P = I²R        P = U²/R        E = Pt",
             "Jauda rāda, cik enerģijas ierīce patērē vienā sekundē. "
             "Otro un trešo formu iegūst, ievietojot Oma likumu; "
             "izvēlas to, kurai ir dotie lielumi.", GOLD),
            ("tabula",
             ["Ierīce", "Jauda", "Strāva pie 230 V"],
             [["LED spuldze", "10 W", "0,04 A"],
              ["Dators", "150 W", "0,65 A"],
              ["Tējkanna", "2000 W", "8,7 A"],
              ["Elektriskā plīts", "6000 W", "26 A"]],
             [3.40, 3.00, 3.83]),
        ]),
        ("Enerģija un izmaksas", [
            ("panelis", "KILOVATSTUNDA",
             ["Elektroenerģiju rēķina kilovatstundās: 1 kWh = 1000 W · "
              "3600 s = 3,6·10⁶ J.",
              "Skaitītājs mēra tieši kilovatstundas; rēķinā to reizina "
              "ar tarifu.",
              "Ērtā formula sadzīvei: E (kWh) = P (kW) · t (h)."], NAVY),
            ("divi",
             ("MAZS PATĒRIŅŠ", GREEN,
              ["LED spuldze 10 W.",
               "Rūteris 8 W.",
               "Telefona lādētājs 5 W.",
               "Diennaktī - dažas kWh",
               "mēnesī."]),
             ("LIELS PATĒRIŅŠ", RED,
              ["Elektriskā apkure 2000 W.",
               "Boileris 2000 W.",
               "Plīts 6000 W.",
               "Tieši šīs ierīces nosaka",
               "rēķinu."])),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Ierīces jauda",
             teksts="Caur ierīci pie 230 V plūst 2,5 A strāva.\n"
                    "Aprēķini jaudu!",
             dots=["U = 230 V", "I = 2,5 A"],
             jaaprekina=["P = ?"],
             formulas=["P = UI"],
             aprekins=["1)  P = 230 · 2,5",
                       "2)  P = 575 W"],
             atbilde="P = 575 W",
             piezime="Apmēram tāda jauda ir mikroviļņu krāsnij."),
        dict(nr=2, virsraksts="Jauda no pretestības",
             teksts="Sildelementa pretestība ir 46 Ω, spriegums 230 V.\n"
                    "Aprēķini jaudu!",
             dots=["R = 46 Ω", "U = 230 V"],
             jaaprekina=["P = ?"],
             formulas=["P = U²/R"],
             aprekins=["1)  U² = 230² = 52 900",
                       "2)  P = 52 900 : 46",
                       "3)  P = 1150 W"],
             atbilde="P = 1150 W",
             piezime="Kad zināma pretestība un spriegums, šī forma ir "
                     "ātrākā."),
        dict(nr=3, virsraksts="Patēriņš kilovatstundās",
             teksts="Tējkanna ar jaudu 2000 W darbojas 15 minūtes dienā.\n"
                    "Cik kilovatstundu tā patērē mēnesī (30 dienās)?",
             dots=["P = 2000 W = 2,0 kW", "t = 15 min = 0,25 h",
                   "30 dienas"],
             jaaprekina=["E = ?"],
             formulas=["E = Pt", "E(mēnesī) = E · 30"],
             aprekins=["1)  Dienā: 2,0 · 0,25 = 0,50 kWh",
                       "2)  Mēnesī: 0,50 · 30",
                       "3)  E = 15 kWh"],
             atbilde="E = 15 kWh mēnesī",
             piezime="Kilovatus reiz stundas - tā ir ātrākā sadzīves "
                     "forma."),
        dict(nr=4, virsraksts="Izmaksas",
             teksts="Cik maksā iepriekšējais patēriņš, ja tarifs ir\n"
                    "0,20 eiro par kilovatstundu? Un cik maksātu\n"
                    "vecā 2400 W tējkanna ar to pašu lietošanas laiku?",
             dots=["E₁ = 15 kWh", "Tarifs 0,20 EUR/kWh",
                   "P₂ = 2,4 kW"],
             jaaprekina=["Izmaksas = ?"],
             formulas=["Cena = E · tarifs", "E = Pt"],
             aprekins=["1)  Cena₁ = 15 · 0,20 = 3,00 EUR",
                       "2)  E₂ = 2,4 · 0,25 · 30 = 18 kWh",
                       "3)  Cena₂ = 18 · 0,20 = 3,60 EUR"],
             atbilde="3,00 EUR pret 3,60 EUR",
             piezime="Starpība ir maza, jo tējkanna ar lielāku jaudu "
                     "vārītu ūdeni ātrāk - jārēķina reālais laiks."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "P = UI; ja zināma pretestība, P = I²R vai P = U²/R.",
            "E = Pt; 1 kWh = 3,6·10⁶ J.",
            "Sadzīvē ērti: kilovati reiz stundas.",
            "Izmaksas = patēriņš kilovatstundās reiz tarifs.",
        ],
        majasdarbs=[
            "U = 230 V, I = 4,0 A. Aprēķini P.",
            "P = 1500 W, t = 2,0 h. Aprēķini E kilovatstundās.",
            "Aprēķini savas mājas apgaismojuma patēriņu mēnesī.",
        ],
        pasvertejums=["Protu lietot P = UI",
                      "Protu izvēlēties jaudas formulu",
                      "Protu rēķināt kilovatstundas",
                      "Protu aprēķināt izmaksas"],
        nakama="Nākamā stunda: reāls strāvas avots un EDS."),
),

dict(
    nr="10.8", virsraksts="Reāls strāvas avots",
    jautajums="Kāpēc baterijas spriegums slodzē samazinās?",
    apaksraksts="EDS ε · Iekšējā pretestība r · I = ε/(R + r)",
    merkis="Skaidrot EDS un iekšējo pretestību un lietot pilnas ķēdes Oma "
           "likumu vienkāršai ķēdei.",
    protu=["izskaidrot, kas ir EDS;",
           "izskaidrot iekšējo pretestību;",
           "lietot I = ε/(R + r);",
           "aprēķināt spriegumu uz avota poliem."],
    atkartojums="Līdz šim avota spriegumu uzskatījām par nemainīgu. "
                "Reālam avotam ir arī sava pretestība - un tieši tāpēc "
                "spriegums slodzē krīt.",
    uzdevumu_apraksts="Pilnas ķēdes Oma likums",
    teorija=[
        ("Reāls avots", [
            ("formula", "PILNAS ĶĒDES OMA LIKUMS",
             "I = ε/(R + r)        U = ε − Ir",
             "ε ir elektrodzinējspēks - avota spriegums bez slodzes, "
             "r - avota iekšējā pretestība, R - ārējās ķēdes pretestība. "
             "Spriegums uz poliem vienmēr ir mazāks par EDS.", GOLD),
            ("kartitas", [
                ("ε - EDS", BLUE,
                 ["Avota īpašība.",
                  "Mēra tukšgaitā.",
                  "AA baterijai 1,5 V."]),
                ("r - IEKŠĒJĀ R", RED,
                 ["Avota iekšpuse.",
                  "Jaunai baterijai maza.",
                  "Izlādētai - liela."]),
                ("U - UZ POLIEM", GREEN,
                 ["To mēra voltmetrs.",
                  "U = ε − Ir.",
                  "Slodzē vienmēr mazāks."]),
            ]),
        ]),
        ("Kur to redz", [
            ("tabula",
             ["Situācija", "Kas notiek", "Kāpēc"],
             [["Bez slodzes", "U ≈ ε", "Strāva gandrīz nulle"],
              ["Neliela slodze", "U mazliet krīt", "Ir zudumi uz r"],
              ["Startera ieslēgšana", "Lukturi paspīd vājāk", "Liela I uz r"],
              ["Izlādēta baterija", "U strauji krīt", "r ir pieaugusi"]],
             [3.20, 3.40, 3.63]),
            ("panelis", "ĪSSLĒGUMA STRĀVA",
             ["Ja ārējā pretestība R kļūst gandrīz nulle, strāvu ierobežo "
              "tikai iekšējā pretestība: I = ε/r.",
              "Tā ir ļoti liela strāva - avots karst un var sabojāties, "
              "tāpēc īsslēgums ir bīstams.",
              "Litija akumulatoriem r ir ļoti maza, tāpēc tiem obligāti "
              "ir aizsardzības shēma."], RED),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Strāva pilnā ķēdē",
             teksts="Baterijai ε = 9,0 V un r = 1,0 Ω. Tai pieslēdz\n"
                    "rezistoru 17 Ω. Aprēķini strāvu!",
             dots=["ε = 9,0 V", "r = 1,0 Ω", "R = 17 Ω"],
             jaaprekina=["I = ?"],
             formulas=["I = ε/(R + r)"],
             aprekins=["1)  R + r = 17 + 1,0 = 18 Ω",
                       "2)  I = 9,0 : 18",
                       "3)  I = 0,50 A"],
             atbilde="I = 0,50 A",
             piezime="Iekšējo pretestību pieskaita ārējai - tā ir "
                     "vienīgā atšķirība no parastā Oma likuma."),
        dict(nr=2, virsraksts="Spriegums uz poliem",
             teksts="Iepriekšējā ķēdē aprēķini spriegumu uz baterijas\n"
                    "poliem!",
             dots=["ε = 9,0 V", "r = 1,0 Ω", "I = 0,50 A"],
             jaaprekina=["U = ?"],
             formulas=["U = ε − Ir"],
             aprekins=["1)  Ir = 0,50 · 1,0 = 0,50 V",
                       "2)  U = 9,0 − 0,50",
                       "3)  U = 8,5 V"],
             atbilde="U = 8,5 V",
             piezime="Pārbaude ar ārējo pretestību: 0,50 · 17 = 8,5 V - "
                     "sakrīt."),
        dict(nr=3, virsraksts="Iekšējā pretestība",
             teksts="Bez slodzes voltmetrs rāda 1,50 V, bet ar rezistoru\n"
                    "2,8 Ω strāva ir 0,50 A. Aprēķini iekšējo\n"
                    "pretestību!",
             dots=["ε = 1,50 V", "R = 2,8 Ω", "I = 0,50 A"],
             jaaprekina=["r = ?"],
             formulas=["ε = I(R + r)", "R + r = ε/I"],
             aprekins=["1)  R + r = 1,50 : 0,50 = 3,0 Ω",
                       "2)  r = 3,0 − 2,8",
                       "3)  r = 0,20 Ω"],
             atbilde="r = 0,20 Ω",
             piezime="Tieši tā iekšējo pretestību nosaka praksē - ar "
                     "diviem mērījumiem."),
        dict(nr=4, virsraksts="Izlādēta baterija",
             teksts="Baterijai ε = 1,5 V, bet iekšējā pretestība\n"
                    "pieaugusi līdz 5,0 Ω. Aprēķini spriegumu uz poliem,\n"
                    "ja ārējā pretestība ir 10 Ω!",
             dots=["ε = 1,5 V", "r = 5,0 Ω", "R = 10 Ω"],
             jaaprekina=["I = ?", "U = ?"],
             formulas=["I = ε/(R + r)", "U = ε − Ir"],
             aprekins=["1)  I = 1,5 : 15 = 0,10 A",
                       "2)  Ir = 0,10 · 5,0 = 0,50 V",
                       "3)  U = 1,5 − 0,50 = 1,0 V"],
             atbilde="U = 1,0 V",
             piezime="Trešdaļa sprieguma pazūd pašā baterijā - tāpēc "
                     "izlādēta baterija ierīci vairs nedarbina."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "EDS ir avota spriegums bez slodzes.",
            "Reālam avotam ir iekšējā pretestība r.",
            "I = ε/(R + r) - pilnas ķēdes Oma likums.",
            "U = ε − Ir; slodzē spriegums vienmēr krīt.",
        ],
        majasdarbs=[
            "ε = 12 V, r = 0,50 Ω, R = 5,5 Ω. Aprēķini I un U.",
            "ε = 4,5 V, I = 0,30 A, R = 14 Ω. Aprēķini r.",
            "Paskaidro, kāpēc, iedarbinot auto, lukturi paspīd vājāk.",
        ],
        pasvertejums=["Zinu, kas ir EDS",
                      "Saprotu iekšējo pretestību",
                      "Protu lietot pilnas ķēdes likumu",
                      "Protu rēķināt U uz poliem"],
        nakama="Nākamā stunda: vadītspēja dažādās vidēs."),
),

dict(
    nr="10.9", virsraksts="Vadītspēja dažādās vidēs",
    jautajums="Kas vada strāvu metālā, šķīdumā un pusvadītājā?",
    apaksraksts="Elektroni · Joni · Pusvadītāji un diode",
    merkis="Salīdzināt lādiņnesējus dažādās vidēs un skaidrot diodes "
           "darbības pamatideju.",
    protu=["nosaukt lādiņnesējus metālā, šķīdumā un gāzē;",
           "izskaidrot pusvadītāja atšķirību;",
           "izskaidrot diodes darbības ideju;",
           "nosaukt lietojumus katrai videi."],
    atkartojums="Līdz šim strāva plūda pa metāla vadu. Šodien "
                "noskaidrosim, ka lādiņnesēji var būt arī citādi - un "
                "tieši tas ļauj būvēt elektroniku.",
    uzdevumu_apraksts="Lādiņnesēji un pusvadītāji",
    teorija=[
        ("Lādiņnesēji dažādās vidēs", [
            ("tabula",
             ["Vide", "Lādiņnesēji", "Lietojums"],
             [["Metāls", "Brīvie elektroni", "Vadi, kontakti"],
              ["Elektrolīts", "Pozitīvie un negatīvie joni",
               "Baterijas, galvanizācija"],
              ["Gāze (jonizēta)", "Joni un elektroni",
               "Neona lampas, zibens"],
              ["Pusvadītājs", "Elektroni un caurumi",
               "Diodes, tranzistori, LED"]],
             [2.90, 4.40, 2.93]),
            ("panelis", "KĀ ATŠĶIRAS PUSVADĪTĀJS",
             ["Tīrā silīcijā brīvo lādiņnesēju ir maz, tāpēc tas vada "
              "slikti - bet ne kā izolators.",
              "Pievienojot niecīgu piejaukumu, vadītspēju var palielināt "
              "tūkstošiem reižu; tā rada n-tipa un p-tipa pusvadītājus.",
              "Sildot metāla pretestība pieaug, bet pusvadītāja - "
              "samazinās: rodas vairāk brīvo lādiņnesēju."], NAVY),
        ]),
        ("Diode", [
            ("divi",
             ("TIEŠAIS VIRZIENS", GREEN,
              ["Diode vada strāvu.",
               "Pretestība maza.",
               "Uz silīcija diodes",
               "paliek apmēram 0,7 V.",
               "LED izstaro gaismu."]),
             ("PRETĒJAIS VIRZIENS", RED,
              ["Diode strāvu nevada.",
               "Pretestība ļoti liela.",
               "Strāva praktiski nulle.",
               "Tāpēc diodi lieto",
               "taisngriežos."])),
            ("panelis", "KUR TO IZMANTO",
             ["Taisngriezis pārvērš maiņstrāvu līdzstrāvā - katrs "
              "lādētājs sākas ar diodēm.",
              "LED ir diode, kas, vadot strāvu, izstaro gaismu; tās "
              "lietderība ir daudz augstāka nekā kvēlspuldzei.",
              "Tranzistors ir divas savienotas pārejas - uz tā balstās "
              "visa mūsdienu elektronika."], GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Kurš lādiņnesējs",
             teksts="Nosaki lādiņnesējus: a) vara vadā; b) sāls ūdenī;\n"
                    "c) neona lampā; d) silīcija diodē.",
             dots=["a) varš", "b) sāls šķīdums", "c) jonizēta gāze",
                   "d) silīcijs"],
             jaaprekina=["Lādiņnesēji = ?"],
             formulas=["Metālā - elektroni",
                       "Šķīdumā - joni",
                       "Pusvadītājā - elektroni un caurumi"],
             aprekins=["1)  a) brīvie elektroni",
                       "2)  b) pozitīvie un negatīvie joni",
                       "3)  c) joni un elektroni;  d) elektroni un caurumi"],
             atbilde="Katrā vidē savi lādiņnesēji",
             piezime="Strāva vienmēr ir sakārtota lādiņu kustība - "
                     "atšķiras tikai, kas tieši kustas."),
        dict(nr=2, virsraksts="Spriegums uz LED",
             teksts="LED ķēdē ir 5,0 V avots un rezistors 220 Ω. Uz LED\n"
                    "paliek 2,0 V. Aprēķini strāvu ķēdē!",
             dots=["ε = 5,0 V", "U(LED) = 2,0 V", "R = 220 Ω"],
             jaaprekina=["I = ?"],
             formulas=["U(R) = ε − U(LED)", "I = U/R"],
             aprekins=["1)  U(R) = 5,0 − 2,0 = 3,0 V",
                       "2)  I = 3,0 : 220",
                       "3)  I ≈ 0,0136 A ≈ 14 mA"],
             atbilde="I ≈ 14 mA",
             piezime="Rezistors LED ķēdē ir obligāts - bez tā strāva "
                     "būtu par lielu un LED izdegtu."),
        dict(nr=3, virsraksts="Pretestība un temperatūra",
             teksts="Metāla vada pretestība sildot pieaug, pusvadītāja -\n"
                    "samazinās. Paskaidro abus gadījumus ar daļiņu\n"
                    "modeli!",
             dots=["Metāls: R aug", "Pusvadītājs: R krīt"],
             jaaprekina=["Kāpēc atšķirība?"],
             formulas=["Metālā elektronu skaits nemainās",
                       "Pusvadītājā rodas jauni lādiņnesēji"],
             aprekins=["1)  Metālā joni svārstās plašāk - traucē kustību",
                       "2)  Pusvadītājā siltums atbrīvo jaunus elektronus",
                       "3)  Jaunie lādiņnesēji uzvar pār traucējumiem"],
             atbilde="Metālā traucējumi, pusvadītājā - jauni nesēji",
             piezime="Uz šīs īpašības balstās termistori - temperatūras "
                     "sensori."),
        dict(nr=4, virsraksts="Diode ķēdē",
             teksts="Diodi pieslēdz tiešajā virzienā ar 12 V avotu un\n"
                    "rezistoru 1,0 kΩ. Uz diodes paliek 0,7 V.\n"
                    "Aprēķini strāvu!",
             dots=["ε = 12 V", "U(d) = 0,7 V", "R = 1,0 kΩ = 1000 Ω"],
             jaaprekina=["I = ?"],
             formulas=["U(R) = ε − U(d)", "I = U/R"],
             aprekins=["1)  U(R) = 12 − 0,7 = 11,3 V",
                       "2)  I = 11,3 : 1000",
                       "3)  I = 0,0113 A ≈ 11 mA"],
             atbilde="I ≈ 11 mA",
             piezime="Pretējā virzienā strāva būtu praktiski nulle - "
                     "tāda ir diodes galvenā īpašība."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Metālā strāvu nes elektroni, šķīdumā - joni.",
            "Pusvadītājos strāvu nes elektroni un caurumi.",
            "Sildot metāla pretestība aug, pusvadītāja - krīt.",
            "Diode vada strāvu tikai vienā virzienā.",
        ],
        majasdarbs=[
            "Nosauc lādiņnesējus trijās dažādās vidēs.",
            "ε = 9,0 V, U(LED) = 2,0 V, R = 330 Ω. Aprēķini I.",
            "Paskaidro, kur sadzīvē izmanto diodes.",
        ],
        pasvertejums=["Zinu lādiņnesējus katrā vidē",
                      "Saprotu pusvadītāju",
                      "Zinu diodes darbību",
                      "Protu rēķināt LED ķēdi"],
        nakama="Nākamā stunda: elektrodrošība un aizsardzība."),
),

dict(
    nr="10.10", virsraksts="Elektrodrošība un aizsardzība",
    jautajums="Kā pasargā drošinātājs un zemējums?",
    apaksraksts="Pārslodze · Īsslēgums · Drošinātājs · Zemējums",
    merkis="Skaidrot pārslodzi un īsslēgumu un izvērtēt drošu "
           "elektroierīču lietošanu.",
    protu=["atšķirt pārslodzi no īsslēguma;",
           "izskaidrot drošinātāja darbību;",
           "izskaidrot zemējuma nozīmi;",
           "aprēķināt, vai ķēde ir pārslogota."],
    atkartojums="Iepriekšējās stundās rēķinājām strāvu un jaudu. Šodien "
                "tie paši aprēķini pateiks, kad ķēde kļūst bīstama.",
    uzdevumu_apraksts="Drošinātāji un pieļaujamā slodze",
    teorija=[
        ("Divi bīstamie gadījumi", [
            ("divi",
             ("PĀRSLODZE", GOLD,
              ["Pieslēgtas par daudz ierīču.",
               "Strāva pārsniedz pieļaujamo.",
               "Vadi pakāpeniski sakarst.",
               "Var aizdegties izolācija.",
               "Aizsargā automātslēdzis."]),
             ("ĪSSLĒGUMS", RED,
              ["Fāze savienojas ar nulli.",
               "Pretestība gandrīz nulle.",
               "Strāva simtiem ampēru.",
               "Notiek acumirklī.",
               "Aizsargā drošinātājs."])),
            ("panelis", "KĀ DARBOJAS AIZSARDZĪBA",
             ["Drošinātājs vai automātslēdzis ir virknē ar visu ķēdi: "
              "pārsniedzot nominālo strāvu, tas ķēdi pārtrauc.",
              "Zemējums novada bojājuma strāvu uz zemi, lai korpuss "
              "nekļūtu bīstams.",
              "Noplūdes aizsardzība salīdzina ienākošo un izejošo strāvu; "
              "ja tās atšķiras, ķēdi atslēdz milisekundēs."], NAVY),
        ]),
        ("Drošība praksē", [
            ("tabula",
             ["Situācija", "Kas notiek", "Pareizā rīcība"],
             [["Sadalītājā daudz ierīču", "Pārslodze, vadi karst",
               "Sadalīt pa rozetēm"],
              ["Bojāta izolācija", "Korpusā parādās spriegums",
               "Zemējums, remonts"],
              ["Ierīce ūdenī", "Ķermenis kļūst vadītājs",
               "Vispirms atslēgt strāvu"],
              ["Smaka un dzirksteles", "Sākas īsslēgums",
               "Izslēgt automātslēdzi"]],
             [3.40, 3.40, 3.43]),
            ("panelis", "CILVĒKS UN STRĀVA",
             ["Bīstama ir strāva caur ķermeni: jau no 30 mA tā ir "
              "dzīvībai bīstama.",
              "Sausas ādas pretestība ir daži tūkstoši omu, mitras - "
              "daudz mazāka; tāpēc mitrās telpās prasības ir stingrākas.",
              "Palīdzot cietušajam, vispirms atslēdz strāvu - citādi "
              "glābējs kļūst par nākamo cietušo."], RED),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Vai drošinātājs izturēs",
             teksts="Rozetes ķēdē ar 16 A drošinātāju vienlaikus ieslēdz\n"
                    "tējkannu 2000 W un sildītāju 1500 W (230 V).\n"
                    "Vai drošinātājs nostrādās?",
             dots=["P₁ = 2000 W", "P₂ = 1500 W", "U = 230 V",
                   "I(dr) = 16 A"],
             jaaprekina=["I = ?"],
             formulas=["P = UI", "I = P/U"],
             aprekins=["1)  P = 2000 + 1500 = 3500 W",
                       "2)  I = 3500 : 230 ≈ 15,2 A",
                       "3)  15,2 A < 16 A - vēl iztur"],
             atbilde="I ≈ 15,2 A - drošinātājs neizslēgsies",
             piezime="Rezerve ir maza: vēl viena ierīce ķēdi jau "
                     "pārslogotu."),
        dict(nr=2, virsraksts="Trešā ierīce",
             teksts="Iepriekšējā ķēdē papildus ieslēdz matu fēnu 1200 W.\n"
                    "Aprēķini kopējo strāvu un secini, kas notiks!",
             dots=["P = 3500 + 1200 = 4700 W", "U = 230 V",
                   "I(dr) = 16 A"],
             jaaprekina=["I = ?"],
             formulas=["I = P/U"],
             aprekins=["1)  I = 4700 : 230",
                       "2)  I ≈ 20,4 A",
                       "3)  20,4 A > 16 A - drošinātājs nostrādās"],
             atbilde="I ≈ 20,4 A - ķēde tiks atslēgta",
             piezime="Tieši tāpēc lielas jaudas ierīces neslēdz vienā "
                     "sadalītājā."),
        dict(nr=3, virsraksts="Īsslēguma strāva",
             teksts="Ķēdē ar 230 V spriegumu izolācija bojāta, un\n"
                    "pretestība kļuvusi 0,20 Ω.\n"
                    "Aprēķini īsslēguma strāvu!",
             dots=["U = 230 V", "R = 0,20 Ω"],
             jaaprekina=["I = ?"],
             formulas=["I = U/R"],
             aprekins=["1)  I = 230 : 0,20",
                       "2)  I = 1150 A"],
             atbilde="I = 1150 A",
             piezime="Vairāk nekā tūkstotis ampēru - tāpēc automātslēdzim "
                     "jānostrādā simtdaļsekundēs."),
        dict(nr=4, virsraksts="Strāva caur cilvēku",
             teksts="Cilvēka ķermeņa pretestība mitrās rokās ir 1500 Ω.\n"
                    "Cik liela strāva plūstu pie 230 V un vai tā ir\n"
                    "bīstama? (bīstama no 30 mA)",
             dots=["U = 230 V", "R = 1500 Ω", "Robeža 30 mA"],
             jaaprekina=["I = ?"],
             formulas=["I = U/R"],
             aprekins=["1)  I = 230 : 1500",
                       "2)  I ≈ 0,153 A = 153 mA",
                       "3)  153 mA ir 5 reizes virs bīstamās robežas"],
             atbilde="I ≈ 153 mA - dzīvībai bīstami",
             piezime="Sausām rokām pretestība ir desmitkārt lielāka - "
                     "tāpēc mitrums elektrības tuvumā ir tik bīstams."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Pārslodze rodas no par daudz ierīcēm, īsslēgums - no bojātas "
            "izolācijas.",
            "Drošinātājs pārtrauc ķēdi, ja strāva pārsniedz nominālo.",
            "Zemējums novada bojājuma strāvu drošā ceļā.",
            "Cilvēkam bīstama ir strāva jau no 30 mA.",
        ],
        majasdarbs=[
            "P = 4000 W, U = 230 V. Aprēķini I un salīdzini ar 16 A.",
            "U = 230 V, R = 0,50 Ω. Aprēķini īsslēguma strāvu.",
            "Nosauc trīs drošas rīcības noteikumus mājās.",
        ],
        pasvertejums=["Atšķiru pārslodzi no īsslēguma",
                      "Zinu drošinātāja darbību",
                      "Zinu zemējuma nozīmi",
                      "Protu novērtēt slodzi"],
        nakama="Nākamā stunda: ekvivalentā pretestība jauktos slēgumos."),
),

]
