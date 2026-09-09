# -*- coding: utf-8 -*-
"""13. temats "Apgaismojums un attēli". A daļa: 13.1.-13.5. stunda."""

from fiz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN     # noqa: F401

TEMATS = "13. temats. Apgaismojums un attēli"
KICKER = "FIZIKA I · 11. KLASE · 13. TEMATS: APGAISMOJUMS UN ATTĒLI"
KURSS = "FIZIKA I · 11. KLASE"
MAPE = "C:/aphysics/Fizika_1/13. Apgaismojums un attēli"

STUNDAS = [

dict(
    nr="13.1", virsraksts="Gaismas avoti un apgaismojums",
    jautajums="Kas nosaka labu darba vietas apgaismojumu?",
    apaksraksts="Avots un apgaismots ķermenis · E = I/r² · Luksi",
    merkis="Atšķirt gaismas avotu no apgaismota ķermeņa un skaidrot "
           "attāluma ietekmi uz apgaismojumu.",
    protu=["atšķirt gaismas avotu no apgaismota ķermeņa;",
           "izskaidrot, kā apgaismojums atkarīgs no attāluma;",
           "lietot E = I/r²;",
           "izvērtēt darba vietas apgaismojumu."],
    atkartojums="12. tematā noskaidrojām, ka gaisma ir elektromagnētisks "
                "vilnis. Šajā tematā skatīsimies, kā gaisma uzvedas "
                "praksē - kā tā izplatās, atstarojas un veido attēlus.",
    uzdevumu_apraksts="Apgaismojuma aprēķini",
    teorija=[
        ("Gaismas avoti", [
            ("divi",
             ("GAISMAS AVOTS", GOLD,
              ["Pats izstaro gaismu.",
               "Saule, spuldze, uguns,",
               "telefona ekrāns.",
               "Enerģija pārvēršas",
               "gaismā."]),
             ("APGAISMOTS ĶERMENIS", BLUE,
              ["Tikai atstaro gaismu.",
               "Mēness, grāmata, siena,",
               "cilvēks.",
               "Tumsā to neredz.",
               "Nav pats avots."])),
            ("formula", "APGAISMOJUMS",
             "E = I/r²        [E] = lukss (lx)",
             "I ir avota gaismas stiprums, r - attālums līdz virsmai. "
             "Apgaismojums samazinās kā attāluma kvadrāts: divreiz tālāk "
             "nozīmē četrreiz vājāk.", GOLD),
        ]),
        ("Apgaismojums praksē", [
            ("tabula",
             ["Vieta", "Vajadzīgais apgaismojums", "Kāpēc tāds"],
             [["Koridors", "100 lx", "Tikai orientācijai"],
              ["Klase, darba galds", "300-500 lx", "Lasīšanai un rakstīšanai"],
              ["Rasēšana, laboratorija", "750 lx", "Smalks darbs"],
              ["Saulaina diena ārā", "līdz 100 000 lx", "Dabiskais maksimums"]],
             [3.20, 3.80, 3.23]),
            ("panelis", "KĀ UZLABOT DARBA VIETU",
             ["Galvenais paņēmiens ir samazināt attālumu: pietuvinot "
              "lampu divas reizes, apgaismojums pieaug četras reizes.",
              "Gaisma jāvirza no kreisās puses (labročiem), lai roka "
              "nemestu ēnu uz darba virsmas.",
              "Jāizvairās no tiešiem atspīdumiem ekrānā - tie nogurdina "
              "acis vairāk nekā vājš apgaismojums."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Apgaismojums uz galda",
             teksts="Lampas gaismas stiprums ir 120 kandelas, tā atrodas\n"
                    "1,5 m virs galda. Aprēķini apgaismojumu!",
             dots=["I = 120 cd", "r = 1,5 m"],
             jaaprekina=["E = ?"],
             formulas=["E = I/r²"],
             aprekins=["1)  r² = 2,25 m²",
                       "2)  E = 120 : 2,25",
                       "3)  E ≈ 53 lx"],
             atbilde="E ≈ 53 lx",
             piezime="53 luksi darba galdam ir par maz - vajag vismaz "
                     "300 luksu."),
        dict(nr=2, virsraksts="Lampu pietuvina",
             teksts="To pašu lampu nolaiž līdz 0,75 m virs galda.\n"
                    "Aprēķini jauno apgaismojumu un salīdzini!",
             dots=["I = 120 cd", "r = 0,75 m", "E₁ ≈ 53 lx"],
             jaaprekina=["E₂ = ?"],
             formulas=["E = I/r²"],
             aprekins=["1)  r² = 0,5625 m²",
                       "2)  E₂ = 120 : 0,5625 ≈ 213 lx",
                       "3)  Attālums uz pusi - apgaismojums 4 reizes lielāks"],
             atbilde="E₂ ≈ 213 lx",
             piezime="Kvadrāta likums: attālums ir spēcīgākais "
                     "instruments apgaismojuma uzlabošanai."),
        dict(nr=3, virsraksts="Vajadzīgais gaismas stiprums",
             teksts="Uz galda 1,2 m attālumā vajag 350 lx.\n"
                    "Cik liels jābūt lampas gaismas stiprumam?",
             dots=["E = 350 lx", "r = 1,2 m"],
             jaaprekina=["I = ?"],
             formulas=["E = I/r²", "I = E·r²"],
             aprekins=["1)  r² = 1,44 m²",
                       "2)  I = 350 · 1,44",
                       "3)  I = 504 cd"],
             atbilde="I ≈ 5,0·10² cd",
             piezime="Aptuveni tāds ir 8 W LED spuldzes gaismas "
                     "stiprums."),
        dict(nr=4, virsraksts="Avots vai apgaismots",
             teksts="Nosaki, kas ir gaismas avots un kas apgaismots\n"
                    "ķermenis: a) Saule; b) Mēness; c) LED spuldze;\n"
                    "d) grāmatas lapa!",
             dots=["a) Saule", "b) Mēness", "c) LED", "d) lapa"],
             jaaprekina=["Avots vai apgaismots?"],
             formulas=["Avots izstaro pats",
                       "Apgaismots ķermenis atstaro"],
             aprekins=["1)  a) un c) - gaismas avoti",
                       "2)  b) un d) - apgaismoti ķermeņi",
                       "3)  Mēness spīd ar atstaroto Saules gaismu"],
             atbilde="Avoti: Saule un LED; pārējie atstaro",
             piezime="Tumsā apgaismotu ķermeni neredz - tas ir vienkāršs "
                     "veids, kā tos atšķirt."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Gaismas avots izstaro pats, apgaismots ķermenis atstaro.",
            "E = I/r²; apgaismojumu mēra luksos.",
            "Divreiz tuvāk nozīmē četrreiz spilgtāk.",
            "Darba galdam vajag 300-500 luksu.",
        ],
        majasdarbs=[
            "I = 200 cd, r = 2,0 m. Aprēķini E.",
            "E = 400 lx, r = 1,0 m. Aprēķini I.",
            "Novērtē savu darba vietu: kur ir lampa un kur krīt ēna.",
        ],
        pasvertejums=["Atšķiru avotu no apgaismota ķermeņa",
                      "Protu lietot E = I/r²",
                      "Saprotu kvadrāta likumu",
                      "Protu izvērtēt darba vietu"],
        nakama="Nākamā stunda: gaisma un krāsas."),
),

dict(
    nr="13.2", virsraksts="Gaisma un krāsas",
    jautajums="Kāpēc priekšmetu krāsas dažādā apgaismojumā atšķiras?",
    apaksraksts="Spektrs · Atstarošana un absorbcija · Krāsu sajaukšana",
    merkis="Skaidrot gaismas krāsu, atstarošanu un absorbciju un saistīt "
           "to ar praktiskiem piemēriem.",
    protu=["izskaidrot, kāpēc priekšmetiem ir krāsa;",
           "atšķirt atstarošanu no absorbcijas;",
           "izskaidrot krāsu maiņu citā apgaismojumā;",
           "nosaukt gaismas pamatkrāsas."],
    atkartojums="12. tematā redzējām, ka baltā gaisma satur visus viļņu "
                "garumus. Šodien noskaidrosim, kas ar tiem notiek, "
                "sastopoties ar priekšmetu.",
    uzdevumu_apraksts="Krāsas, atstarošana un absorbcija",
    teorija=[
        ("Kāpēc priekšmetam ir krāsa", [
            ("panelis", "ATSTAROŠANA UN ABSORBCIJA",
             ["Baltā gaisma satur visus redzamos viļņu garumus. "
              "Priekšmets daļu no tiem absorbē, daļu atstaro.",
              "Mēs redzam tieši ATSTAROTO gaismu: sarkans ābols atstaro "
              "sarkano un absorbē pārējās krāsas.",
              "Balts priekšmets atstaro gandrīz visu, melns - absorbē "
              "gandrīz visu un tāpēc saulē sakarst vairāk."], NAVY),
            ("kartitas", [
                ("BALTS", BLUE,
                 ["Atstaro visas krāsas.",
                  "Saulē mazāk sakarst.",
                  "Tāpēc vasarā velk",
                  "gaišas drēbes."]),
                ("MELNS", GREY,
                 ["Absorbē visas krāsas.",
                  "Sakarst visvairāk.",
                  "Tāpēc saules kolektori",
                  "ir melni."]),
                ("KRĀSAINS", GOLD,
                 ["Atstaro savu krāsu.",
                  "Pārējās absorbē.",
                  "Zaļa lapa atstaro",
                  "zaļo gaismu."]),
            ]),
        ]),
        ("Krāsas dažādā gaismā", [
            ("tabula",
             ["Priekšmets", "Baltā gaismā", "Sarkanā gaismā"],
             [["Balts papīrs", "Balts", "Sarkans"],
              ["Sarkans ābols", "Sarkans", "Sarkans"],
              ["Zila soma", "Zila", "Gandrīz melna"],
              ["Melns audums", "Melns", "Melns"]],
             [3.20, 3.40, 3.63]),
            ("panelis", "KUR TAS SVARĪGI",
             ["Skatuves apgaismojumā krāsainie prožektori pilnīgi maina "
              "kostīmu izskatu - to plāno iepriekš.",
              "Fotogrāfijā gaismas «temperatūra» maina krāsu toņus; "
              "tāpēc kamerā iestata baltā balansu.",
              "Veikalos gaļas un dārzeņu nodaļās izmanto dažādas "
              "spuldzes, lai preces izskatītos svaigākas."], GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Kāda krāsa būs redzama",
             teksts="Zilu somu apgaismo ar sarkanu gaismu.\n"
                    "Kāda tā izskatīsies un kāpēc?",
             dots=["Soma atstaro zilo", "Gaisma sarkana"],
             jaaprekina=["Kāda krāsa redzama?"],
             formulas=["Redzam atstaroto gaismu",
                       "Ja tādas krāsas nav - nav ko atstarot"],
             aprekins=["1)  Sarkanajā gaismā zilās nav",
                       "2)  Soma sarkano absorbē",
                       "3)  Atstarotās gaismas nav - soma izskatās melna"],
             atbilde="Soma izskatīsies gandrīz melna",
             piezime="Priekšmets nevar atstarot krāsu, kuras "
                     "apgaismojumā nav."),
        dict(nr=2, virsraksts="Kurš sakarst vairāk",
             teksts="Divi vienādi trauki ar ūdeni stāv saulē: viens balts,\n"
                    "otrs melns. Kurš sasils ātrāk un kāpēc?",
             dots=["Balts trauks", "Melns trauks", "Vienāda saule"],
             jaaprekina=["Kurš sasils ātrāk?"],
             formulas=["Melns absorbē vairāk enerģijas",
                       "Q = cmΔT"],
             aprekins=["1)  Melnais absorbē gandrīz visu gaismu",
                       "2)  Baltais lielāko daļu atstaro",
                       "3)  Melnais saņem vairāk enerģijas - sasilst ātrāk"],
             atbilde="Melnais trauks",
             piezime="Tas ir 8. temata siltuma jautājums, atrisināts ar "
                     "optikas argumentu."),
        dict(nr=3, virsraksts="Enerģija saules kolektorā",
             teksts="Melns saules kolektors ar laukumu 2,0 m² saņem\n"
                    "800 W uz kvadrātmetru un absorbē 90 %.\n"
                    "Aprēķini absorbēto jaudu!",
             dots=["S = 2,0 m²", "Plūsma 800 W/m²", "Absorbcija 90 %"],
             jaaprekina=["P = ?"],
             formulas=["P = plūsma · S · daļa"],
             aprekins=["1)  Krītošā jauda: 800 · 2,0 = 1600 W",
                       "2)  P = 0,90 · 1600",
                       "3)  P = 1440 W"],
             atbilde="P = 1440 W",
             piezime="Ar to pietiek, lai stundā sasildītu apmēram 15 kg "
                     "ūdens par 20 grādiem."),
        dict(nr=4, virsraksts="Krāsu filtrs",
             teksts="Balto gaismu laiž caur zaļu filtru un pēc tam uz\n"
                    "sarkanu priekšmetu. Ko redzēsim?",
             dots=["Filtrs izlaiž zaļo",
                   "Priekšmets atstaro sarkano"],
             jaaprekina=["Ko redzēsim?"],
             formulas=["Filtrs izlaiž vienu krāsu",
                       "Priekšmets atstaro savu krāsu"],
             aprekins=["1)  Pēc filtra ir tikai zaļā gaisma",
                       "2)  Sarkans priekšmets zaļo absorbē",
                       "3)  Atstarotās gaismas praktiski nav - melns"],
             atbilde="Priekšmets izskatīsies melns",
             piezime="Divi soļi pēc kārtas: vispirms filtrs, tad "
                     "priekšmeta virsma."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Priekšmeta krāsu nosaka tas, kuru gaismu tas atstaro.",
            "Balts atstaro visu, melns absorbē visu.",
            "Krāsu var redzēt tikai tad, ja tā ir apgaismojumā.",
            "Absorbētā gaisma pārvēršas siltumā.",
        ],
        majasdarbs=[
            "Kāda izskatīsies zaļa lapa sarkanā gaismā?",
            "S = 1,5 m², plūsma 700 W/m², absorbcija 85 %. Aprēķini P.",
            "Paskaidro, kāpēc vasarā velk gaišas drēbes.",
        ],
        pasvertejums=["Zinu, kāpēc ir krāsas",
                      "Atšķiru atstarošanu no absorbcijas",
                      "Protu paredzēt krāsu citā gaismā",
                      "Zinu saistību ar siltumu"],
        nakama="Nākamā stunda: atstarošanās un spoguļi."),
),

dict(
    nr="13.3", virsraksts="Atstarošanās un spoguļi",
    jautajums="Kur rodas attēls spogulī?",
    apaksraksts="α = β · Staru gaita · Šķietams attēls",
    merkis="Zīmēt staru gaitu plakanā spogulī un skaidrot attēla "
           "īpašības.",
    protu=["formulēt atstarošanās likumu;",
           "uzzīmēt staru gaitu plakanā spogulī;",
           "nosaukt attēla īpašības spogulī;",
           "atšķirt spoguļatstarošanos no izkliedes."],
    atkartojums="Iepriekšējā stundā gaisma no priekšmetiem atstarojās "
                "uz visām pusēm. Gludā virsmā tā atstarojas sakārtoti - "
                "un tā rodas attēls.",
    uzdevumu_apraksts="Atstarošanās leņķi un attēli",
    teorija=[
        ("Atstarošanās likums", [
            ("formula", "ATSTAROŠANĀS LIKUMS",
             "α = β        (krišanas leņķis = atstarošanās leņķis)",
             "Leņķus mēra no perpendikula (normāles) pret virsmu, nevis "
             "no pašas virsmas. Krītošais stars, atstarotais stars un "
             "normāle atrodas vienā plaknē.", GOLD),
            ("divi",
             ("SPOGUĻATSTAROŠANĀS", BLUE,
              ["Gluda virsma.",
               "Stari paliek paralēli.",
               "Rodas attēls.",
               "Spogulis, ūdens virsma,",
               "pulēts metāls."]),
             ("IZKLIEDE", GREEN,
              ["Nelīdzena virsma.",
               "Stari izkliedējas.",
               "Attēla nav.",
               "Papīrs, siena, audums.",
               "Tāpēc tos redzam no visām",
               "pusēm."])),
        ]),
        ("Attēls plakanā spogulī", [
            ("tabula",
             ["Īpašība", "Kāds ir attēls", "Kā to pierāda"],
             [["Veids", "Šķietams", "Stari tikai šķietami satiekas"],
              ["Izmērs", "Tikpat liels", "Γ = 1"],
              ["Attālums", "Tikpat tālu aiz spoguļa", "Simetrisks"],
              ["Orientācija", "Kreisā un labā mainās", "Spoguļsimetrija"]],
             [2.90, 3.60, 3.73]),
            ("panelis", "KĀ ZĪMĒT STARU GAITU",
             ["1. No priekšmeta punkta zīmē divus starus uz spoguli.",
              "2. Katram staram zīmē normāli un atstaro to pēc likuma "
              "α = β.",
              "3. Atstarotos starus pagarina AIZ spoguļa ar punktētu "
              "līniju.",
              "4. Kur punktētās līnijas krustojas, tur ir attēla punkts."],
             NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Atstarošanās leņķis",
             teksts="Stars krīt uz spoguli 30° leņķī pret VIRSMU.\n"
                    "Aprēķini krišanas un atstarošanās leņķi!",
             dots=["Leņķis pret virsmu 30°"],
             jaaprekina=["α = ?", "β = ?"],
             formulas=["Leņķi mēra no normāles", "α = 90° − 30°",
                       "β = α"],
             aprekins=["1)  α = 90° − 30° = 60°",
                       "2)  β = α",
                       "3)  β = 60°"],
             atbilde="α = β = 60°",
             piezime="Biežākā kļūda - leņķi mērīt no virsmas. Vienmēr "
                     "mēra no normāles."),
        dict(nr=2, virsraksts="Attālums līdz attēlam",
             teksts="Cilvēks stāv 1,2 m no spoguļa.\n"
                    "Cik tālu no viņa ir attēls?",
             dots=["a = 1,2 m"],
             jaaprekina=["Attālums = ?"],
             formulas=["Attēls tikpat tālu aiz spoguļa"],
             aprekins=["1)  Attēls ir 1,2 m aiz spoguļa",
                       "2)  Attālums = 1,2 + 1,2",
                       "3)  Attālums = 2,4 m"],
             atbilde="2,4 m",
             piezime="Tāpēc, ejot pret spoguli, attēls tuvojas divreiz "
                     "ātrāk nekā tu."),
        dict(nr=3, virsraksts="Cik garš spogulis",
             teksts="Cik garam jābūt spogulim, lai 1,70 m garš cilvēks\n"
                    "redzētu sevi visā augumā?",
             dots=["h = 1,70 m"],
             jaaprekina=["Spoguļa garums = ?"],
             formulas=["Vajadzīgs puse no auguma"],
             aprekins=["1)  Stars no galvas atstarojas pusceļā",
                       "2)  Tas pats attiecas uz kājām",
                       "3)  Spogulis = 1,70 : 2 = 0,85 m"],
             atbilde="0,85 m",
             piezime="Spoguļa garums nav atkarīgs no attāluma - tikai "
                     "no auguma."),
        dict(nr=4, virsraksts="Divi leņķi",
             teksts="Spogulis pagriezts par 10°. Par cik grādiem\n"
                    "pagriezīsies atstarotais stars, ja krītošais\n"
                    "paliek nemainīgs?",
             dots=["Spoguļa pagrieziens 10°",
                   "Krītošais stars nemainīgs"],
             jaaprekina=["Stara pagrieziens = ?"],
             formulas=["α = β",
                       "Pagriežot spoguli par φ, stars pagriežas par 2φ"],
             aprekins=["1)  Normāle pagriežas par 10°",
                       "2)  Mainās gan α, gan β - katrs par 10°",
                       "3)  Atstarotais stars pagriežas par 20°"],
             atbilde="Par 20°",
             piezime="Uz šī efekta balstās spoguļu galvanometri un "
                     "lāzera skeneri."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Atstarošanās likums: α = β, mērot no normāles.",
            "Gludā virsmā stari atstarojas sakārtoti, nelīdzenā - "
            "izkliedējas.",
            "Attēls plakanā spogulī ir šķietams un tikpat liels.",
            "Attēls atrodas tikpat tālu aiz spoguļa, cik priekšmets "
            "priekšā.",
        ],
        majasdarbs=[
            "Stars krīt 25° leņķī pret virsmu. Aprēķini α un β.",
            "Cilvēks 2,0 m no spoguļa. Cik tālu ir attēls?",
            "Uzzīmē staru gaitu punktam plakanā spogulī.",
        ],
        pasvertejums=["Zinu atstarošanās likumu",
                      "Protu zīmēt staru gaitu",
                      "Zinu attēla īpašības",
                      "Atšķiru izkliedi no spoguļatstarošanās"],
        nakama="Nākamā stunda: gaismas laušana."),
),

dict(
    nr="13.4", virsraksts="Gaismas laušana",
    jautajums="Kāpēc salmiņš ūdenī izskatās saliekts?",
    apaksraksts="n = sin α/sin β · v = c/n · Staru gaita uz robežas",
    merkis="Zīmēt un skaidrot staru gaitu uz divu vidu robežas un lietot "
           "laušanas likumu.",
    protu=["izskaidrot, kāpēc gaisma lūst;",
           "lietot laušanas likumu;",
           "noteikt, uz kuru pusi stars novirzās;",
           "aprēķināt gaismas ātrumu vidē."],
    atkartojums="6. tematā redzējām, ka vilnim, pārejot citā vidē, "
                "mainās ātrums. Gaismai tas pats notiek uz ūdens vai "
                "stikla robežas - un tāpēc stars lūst.",
    uzdevumu_apraksts="Laušanas likuma aprēķini",
    teorija=[
        ("Laušanas likums", [
            ("formula", "LAUŠANAS LIKUMS UN LAUŠANAS KOEFICIENTS",
             "n = sin α/sin β        n = c/v",
             "α ir krišanas leņķis, β - laušanas leņķis, abi mērīti no "
             "normāles. Laušanas koeficients n rāda, cik reižu gaismas "
             "ātrums vidē ir mazāks nekā vakuumā.", GOLD),
            ("tabula",
             ["Vide", "n", "Gaismas ātrums vidē"],
             [["Vakuums un gaiss", "1,00", "3,0·10⁸ m/s"],
              ["Ūdens", "1,33", "2,3·10⁸ m/s"],
              ["Stikls", "1,50", "2,0·10⁸ m/s"],
              ["Dimants", "2,42", "1,2·10⁸ m/s"]],
             [3.60, 2.40, 4.23]),
        ]),
        ("Uz kuru pusi lūst", [
            ("divi",
             ("BLĪVĀKĀ VIDĒ", BLUE,
              ["No gaisa ūdenī vai stiklā.",
               "Ātrums samazinās.",
               "Stars tuvojas normālei.",
               "β < α."]),
             ("RETĀKĀ VIDĒ", GREEN,
              ["No ūdens vai stikla gaisā.",
               "Ātrums palielinās.",
               "Stars attālinās no normāles.",
               "β > α."])),
            ("panelis", "KUR TO REDZ IKDIENĀ",
             ["Salmiņš glāzē izskatās salauzts, jo stari no tā daļas zem "
              "ūdens lūst, izejot gaisā.",
              "Baseina dibens šķiet tuvāks, nekā ir patiesībā - tāpēc "
              "dziļumu vienmēr pārbauda pirms lēciena.",
              "Zivs ūdenī redzama nedaudz citā vietā, nekā tā "
              "patiesībā ir."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Laušanas koeficients",
             teksts="Stars no gaisa ieiet ūdenī. Krišanas leņķa sinuss ir\n"
                    "0,80, laušanas leņķa sinuss 0,60.\n"
                    "Aprēķini laušanas koeficientu!",
             dots=["sin α = 0,80", "sin β = 0,60"],
             jaaprekina=["n = ?"],
             formulas=["n = sin α/sin β"],
             aprekins=["1)  n = 0,80 : 0,60",
                       "2)  n ≈ 1,33"],
             atbilde="n ≈ 1,33",
             piezime="1,33 ir tieši ūdens laušanas koeficients - "
                     "rezultāts ticams."),
        dict(nr=2, virsraksts="Gaismas ātrums ūdenī",
             teksts="Aprēķini gaismas ātrumu ūdenī!\n"
                    "(n = 1,33; c = 3,0·10⁸ m/s)",
             dots=["n = 1,33", "c = 3,0·10⁸ m/s"],
             jaaprekina=["v = ?"],
             formulas=["n = c/v", "v = c/n"],
             aprekins=["1)  v = 3,0·10⁸ : 1,33",
                       "2)  v ≈ 2,26·10⁸ m/s",
                       "3)  v ≈ 2,3·10⁸ m/s"],
             atbilde="v ≈ 2,3·10⁸ m/s",
             piezime="Ūdenī gaisma iet apmēram par ceturtdaļu lēnāk "
                     "nekā vakuumā."),
        dict(nr=3, virsraksts="Laušanas leņķis",
             teksts="Stars krīt uz stiklu (n = 1,50), krišanas leņķa\n"
                    "sinuss ir 0,90. Aprēķini laušanas leņķa sinusu!",
             dots=["n = 1,50", "sin α = 0,90"],
             jaaprekina=["sin β = ?"],
             formulas=["n = sin α/sin β", "sin β = sin α/n"],
             aprekins=["1)  sin β = 0,90 : 1,50",
                       "2)  sin β = 0,60",
                       "3)  β ≈ 37°"],
             atbilde="sin β = 0,60",
             piezime="Laušanas leņķis mazāks par krišanas - stars "
                     "tuvojas normālei, kā jābūt blīvākā vidē."),
        dict(nr=4, virsraksts="Uz kuru pusi",
             teksts="Nosaki, vai stars tuvojas normālei vai attālinās:\n"
                    "a) no gaisa stiklā; b) no ūdens gaisā;\n"
                    "c) no stikla dimantā!",
             dots=["n(gaiss) = 1,00", "n(ūdens) = 1,33",
                   "n(stikls) = 1,50", "n(dimants) = 2,42"],
             jaaprekina=["Uz kuru pusi lūst?"],
             formulas=["Blīvākā vidē - tuvojas normālei",
                       "Retākā vidē - attālinās"],
             aprekins=["1)  a) 1,00 → 1,50: tuvojas normālei",
                       "2)  b) 1,33 → 1,00: attālinās",
                       "3)  c) 1,50 → 2,42: tuvojas normālei"],
             atbilde="a) un c) tuvojas; b) attālinās",
             piezime="Salīdzina tikai laušanas koeficientus - lielāks n "
                     "vienmēr nozīmē lēnāku gaismu."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Gaisma lūst, jo dažādās vidēs tai ir dažāds ātrums.",
            "n = sin α/sin β un n = c/v.",
            "Blīvākā vidē stars tuvojas normālei.",
            "Ūdenī n = 1,33, stiklā n = 1,50.",
        ],
        majasdarbs=[
            "sin α = 0,75, sin β = 0,50. Aprēķini n.",
            "n = 1,50. Aprēķini gaismas ātrumu stiklā.",
            "Paskaidro, kāpēc baseina dibens šķiet tuvāks.",
        ],
        pasvertejums=["Zinu, kāpēc gaisma lūst",
                      "Protu lietot laušanas likumu",
                      "Protu noteikt novirzes virzienu",
                      "Protu rēķināt ātrumu vidē"],
        nakama="Nākamā stunda: pilnīga iekšējā atstarošanās."),
),

dict(
    nr="13.5", virsraksts="Pilnīga iekšējā atstarošanās",
    jautajums="Kā optiskā šķiedra vada gaismu?",
    apaksraksts="sin α₀ = 1/n · Robežleņķis · Optiskā šķiedra",
    merkis="Nosaukt pilnīgas iekšējās atstarošanās nosacījumus un "
           "skaidrot optiskās šķiedras darbību.",
    protu=["nosaukt abus nosacījumus pilnīgai atstarošanai;",
           "aprēķināt robežleņķi;",
           "izskaidrot optiskās šķiedras darbību;",
           "nosaukt lietojumus."],
    atkartojums="Iepriekšējā stundā, ejot retākā vidē, stars attālinājās "
                "no normāles. Šodien noskaidrosim, kas notiek, kad tas "
                "attālinās tik ļoti, ka vairs nevar izkļūt.",
    uzdevumu_apraksts="Robežleņķa aprēķini",
    teorija=[
        ("Robežleņķis", [
            ("formula", "PILNĪGAS IEKŠĒJĀS ATSTAROŠANĀS NOSACĪJUMS",
             "sin α₀ = 1/n        α > α₀",
             "Robežleņķis α₀ ir krišanas leņķis, pie kura lauztais stars "
             "slīd gar virsmu. Ja krišanas leņķis ir vēl lielāks, gaisma "
             "vairs neizkļūst - tā pilnībā atstarojas atpakaļ.", GOLD),
            ("divi",
             ("DIVI NOSACĪJUMI", GREEN,
              ["1. Gaisma iet no BLĪVĀKAS",
               "vides uz retāku.",
               "2. Krišanas leņķis ir",
               "lielāks par robežleņķi.",
               "Tikai tad atstarošanās",
               "ir pilnīga."]),
             ("ROBEŽLEŅĶI", BLUE,
              ["Ūdens (n = 1,33): 49°.",
               "Stikls (n = 1,50): 42°.",
               "Dimants (n = 2,42): 24°.",
               "Jo lielāks n, jo mazāks",
               "robežleņķis."])),
        ]),
        ("Lietojumi", [
            ("tabula",
             ["Lietojums", "Kā darbojas", "Ieguvums"],
             [["Optiskā šķiedra", "Stars atstarojas serdes iekšpusē",
               "Datu pārraide bez zudumiem"],
              ["Endoskops", "Šķiedru kūlis nes attēlu",
               "Izmeklējums bez operācijas"],
              ["Dimants", "Mazs robežleņķis", "Akmens spīd"],
              ["Prizmu binoklis", "Pilnīga atstarošanās prizmā",
               "Nav sudraba pārklājuma"]],
             [3.20, 4.00, 3.03]),
            ("panelis", "OPTISKĀ ŠĶIEDRA",
             ["Šķiedras serdei laušanas koeficients ir lielāks nekā "
              "apvalkam, tāpēc uz to robežas notiek pilnīga iekšējā "
              "atstarošanās.",
              "Stars cikcakā virzās pa serdi simtiem kilometru garumā ar "
              "nelieliem zudumiem.",
              "Tā darbojas gan interneta pamattīkls, gan medicīnas "
              "endoskopi."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Robežleņķis stiklam",
             teksts="Aprēķini robežleņķa sinusu stiklam (n = 1,50)!",
             dots=["n = 1,50"],
             jaaprekina=["sin α₀ = ?"],
             formulas=["sin α₀ = 1/n"],
             aprekins=["1)  sin α₀ = 1 : 1,50",
                       "2)  sin α₀ ≈ 0,667",
                       "3)  α₀ ≈ 42°"],
             atbilde="sin α₀ ≈ 0,67  (α₀ ≈ 42°)",
             piezime="Stariem, kas krīt stāvāk par 42°, no stikla "
                     "izkļūt neizdodas."),
        dict(nr=2, virsraksts="Robežleņķis ūdenim",
             teksts="Aprēķini robežleņķa sinusu ūdenim (n = 1,33) un\n"
                    "salīdzini ar stiklu!",
             dots=["n = 1,33", "Stiklam sin α₀ ≈ 0,67"],
             jaaprekina=["sin α₀ = ?"],
             formulas=["sin α₀ = 1/n"],
             aprekins=["1)  sin α₀ = 1 : 1,33",
                       "2)  sin α₀ ≈ 0,752",
                       "3)  α₀ ≈ 49° - lielāks nekā stiklam"],
             atbilde="sin α₀ ≈ 0,75  (α₀ ≈ 49°)",
             piezime="Mazāks n nozīmē lielāku robežleņķi - gaismai "
                     "vieglāk izkļūt."),
        dict(nr=3, virsraksts="Vai notiks atstarošanās",
             teksts="Stars stiklā (n = 1,50) krīt uz robežu ar gaisu\n"
                    "45° leņķī. Vai notiks pilnīga iekšējā\n"
                    "atstarošanās? (sin 45° ≈ 0,71)",
             dots=["n = 1,50", "α = 45°", "sin α₀ ≈ 0,667"],
             jaaprekina=["Vai notiks?"],
             formulas=["Notiek, ja α > α₀"],
             aprekins=["1)  α₀ ≈ 42°",
                       "2)  45° > 42°",
                       "3)  Jā, notiks pilnīga atstarošanās"],
             atbilde="Jā, jo 45° > 42°",
             piezime="Tieši 45° prizmas izmanto binokļos un "
                     "periskopos."),
        dict(nr=4, virsraksts="Dimanta spīdums",
             teksts="Dimantam n = 2,42. Aprēķini robežleņķa sinusu un\n"
                    "paskaidro, kāpēc dimants tik spēcīgi spīd!",
             dots=["n = 2,42"],
             jaaprekina=["sin α₀ = ?"],
             formulas=["sin α₀ = 1/n"],
             aprekins=["1)  sin α₀ = 1 : 2,42 ≈ 0,413",
                       "2)  α₀ ≈ 24°",
                       "3)  Gandrīz visi stari atstarojas iekšpusē"],
             atbilde="sin α₀ ≈ 0,41  (α₀ ≈ 24°)",
             piezime="Mazs robežleņķis nozīmē, ka gaisma daudzkārt "
                     "atstarojas akmens iekšienē, pirms izkļūst."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Pilnīga iekšējā atstarošanās notiek, ejot no blīvākas vides "
            "uz retāku.",
            "Otrs nosacījums: krišanas leņķis lielāks par robežleņķi.",
            "sin α₀ = 1/n; lielāks n nozīmē mazāku robežleņķi.",
            "Uz šī principa balstās optiskā šķiedra un endoskopi.",
        ],
        majasdarbs=[
            "n = 1,60. Aprēķini robežleņķa sinusu.",
            "Vai stars ūdenī ar α = 40° pilnīgi atstarosies?",
            "Paskaidro, kā optiskā šķiedra vada gaismu.",
        ],
        pasvertejums=["Zinu abus nosacījumus",
                      "Protu rēķināt robežleņķi",
                      "Zinu optiskās šķiedras darbību",
                      "Zinu lietojumus"],
        nakama="Nākamā stunda: lēcas un attēli."),
),

]
