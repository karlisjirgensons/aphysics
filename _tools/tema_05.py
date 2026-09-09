# -*- coding: utf-8 -*-
"""10.5. temats "Materiālu veidi un īpašības" — fizikas daļa, 8 stundas."""

import sys
import dz_common as C
from dz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN

TEMATS = "5. temats. Materiālu veidi un īpašības"
KICKER = "DABASZINĪBAS · 10. KLASE · 5. TEMATS: MATERIĀLU VEIDI UN ĪPAŠĪBAS"
MAPE = "C:/aphysics/Dabaszinibas/5. Materiālu veidi un īpašības"

STUNDAS = [

dict(
    nr="5.1", virsraksts="Materiālu fizikālās īpašības",
    jautajums="Pēc kā izvēlas materiālu?",
    apaksraksts="Blīvums · Cietība · Kušanas temperatūra · Izturība",
    merkis="Iemācīties salīdzināt materiālus pēc fizikālajām īpašībām un "
           "pamatot materiāla izvēli ar aprēķinu.",
    protu=["nosaukt materiālu galvenās fizikālās īpašības;",
           "lietot ρ = m/V un salīdzināt blīvumus;",
           "aprēķināt ķermeņa masu pēc tilpuma un blīvuma;",
           "pamatot materiāla izvēli konkrētam uzdevumam."],
    atkartojums="3.11. stundā noskaidrojām, ka vielas īpašības nosaka "
                "kristālrežģa veids. Tagad skatīsim, kā šīs īpašības mēra un "
                "izmanto praksē.",
    uzdevumu_apraksts="Blīvums, masa un materiāla izvēle",
    teorija=[
        ("Ar ko raksturo materiālu", [
            ("kartitas", [
                ("BLĪVUMS  ρ", BLUE,
                 ["ρ = m / V   [kg/m³]", "Cik smaga ir vienība tilpuma.",
                  "Nosaka konstrukcijas svaru."]),
                ("IZTURĪBA", RED,
                 ["Cik lielu slodzi materiāls iztur.",
                  "Raksturo ar spriegumu σ = F/S.",
                  "Nosaka drošību."]),
                ("KUŠANAS TEMPERATŪRA", GOLD,
                 ["Pie kādas t° materiāls kūst.",
                  "Nosaka, kur to drīkst lietot.",
                  "Volframs 3422 °C, alva 232 °C."]),
            ]),
            ("tabula",
             ["Materiāls", "Blīvums, kg/m³", "Kušanas t°, °C", "Lietojums"],
             [["Alumīnijs", "2700", "660", "lidmašīnas, iepakojums"],
              ["Dzelzs (tērauds)", "7800", "1538", "konstrukcijas, mašīnas"],
              ["Varš", "8900", "1085", "elektrības vadi"],
              ["Koks (priede)", "500", "deg", "būvniecība, mēbeles"],
              ["Polietilēns", "950", "130", "iepakojums, caurules"]],
             [3.03, 2.80, 2.60, 3.80]),
        ]),
        ("Kā izvēlas materiālu", [
            ("formula", "MASA NO BLĪVUMA UN TILPUMA",
             "ρ = m / V        m = ρ · V        V = m / ρ",
             "Viena sakarība trim uzdevumiem. Vienmēr pārbaudi mērvienības: "
             "kg/m³ · m³ = kg.", GOLD),
            ("panelis", "IZVĒLES KRITĒRIJI",
             ["Lidmašīnai — maza blīvuma un liela izturība (alumīnijs, "
              "kompozīti). Elektrības vadam — laba elektrovadītspēja "
              "(varš, alumīnijs).",
              "Katlam — augsta kušanas temperatūra un siltumvadītspēja. "
              "Loga rāmim — mazs siltumvadītspējas koeficients."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Detaļas masa",
             teksts="Alumīnija detaļas tilpums ir 250 cm³, blīvums "
                    "2700 kg/m³.\nAprēķini detaļas masu!",
             dots=["V = 250 cm³", "ρ = 2700 kg/m³"],
             jaaprekina=["m = ?"],
             formulas=["ρ = m / V", "m = ρ · V"],
             aprekins=["1)  V = 250 cm³ = 2,50·10⁻⁴ m³",
                       "2)  m = 2700 kg/m³ · 2,50·10⁻⁴ m³",
                       "3)  m = 0,675 kg = 675 g"],
             atbilde="m = 0,675 kg",
             piezime="Pārbaude: kg/m³ · m³ = kg — mērvienības sakrīt."),
        dict(nr=2, virsraksts="Kurš materiāls ir vieglāks?",
             teksts="Detaļas tilpums ir 500 cm³. To var izgatavot no "
                    "alumīnija (2700 kg/m³) vai tērauda (7800 kg/m³).\n"
                    "Par cik gramiem alumīnija detaļa ir vieglāka?",
             dots=["V = 500 cm³", "ρ₁ = 2700 kg/m³", "ρ₂ = 7800 kg/m³"],
             jaaprekina=["Δm = ?"],
             formulas=["m = ρ · V", "Δm = m₂ − m₁"],
             aprekins=["1)  V = 5,00·10⁻⁴ m³",
                       "2)  m₁ = 2700 · 5,00·10⁻⁴ = 1,35 kg",
                       "3)  m₂ = 7800 · 5,00·10⁻⁴ = 3,90 kg",
                       "4)  Δm = 3,90 − 1,35 = 2,55 kg"],
             atbilde="Δm = 2,55 kg — alumīnija detaļa ir gandrīz 3× vieglāka",
             piezime="Tieši tāpēc lidmašīnās izmanto alumīniju, nevis "
                     "tēraudu."),
        dict(nr=3, virsraksts="Nezināma materiāla noteikšana",
             teksts="Parauga masa ir 178 g, tilpums 20,0 cm³.\n"
                    "Aprēķini blīvumu un nosaki materiālu pēc tabulas!",
             dots=["m = 178 g", "V = 20,0 cm³"],
             jaaprekina=["ρ = ?"],
             formulas=["ρ = m / V"],
             aprekins=["1)  m = 0,178 kg ;  V = 2,00·10⁻⁵ m³",
                       "2)  ρ = 0,178 : 2,00·10⁻⁵",
                       "3)  ρ = 8900 kg/m³"],
             atbilde="ρ = 8900 kg/m³ — materiāls ir varš",
             piezime="Blīvums ir vielas “pase” — pēc tā materiālu var "
                     "atpazīt."),
        dict(nr=4, virsraksts="Tilpums pēc masas",
             teksts="Nepieciešams 2,0 kg smags svina atsvars. Svina blīvums "
                    "ir 11 300 kg/m³.\nAprēķini atsvara tilpumu cm³!",
             dots=["m = 2,0 kg", "ρ = 11 300 kg/m³"],
             jaaprekina=["V = ?  (cm³)"],
             formulas=["ρ = m / V", "V = m / ρ"],
             aprekins=["1)  V = 2,0 kg : 11 300 kg/m³",
                       "2)  V = 1,77·10⁻⁴ m³",
                       "3)  V = 177 cm³"],
             atbilde="V ≈ 1,8·10⁻⁴ m³ = 177 cm³",
             piezime="Svins ir tik blīvs, ka 2 kg ietilpst mazā kubiciņā."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Materiālu raksturo blīvums, izturība, cietība un kušanas "
            "temperatūra.",
            "ρ = m/V — no divām vērtībām vienmēr var atrast trešo.",
            "Blīvums ļauj atpazīt materiālu un aprēķināt konstrukcijas svaru.",
            "Materiālu izvēlas pēc uzdevuma: viegls, izturīgs, karstumizturīgs "
            "vai vadošs.",
        ],
        majasdarbs=[
            "V = 120 cm³ tērauda detaļa (7800 kg/m³). Aprēķini masu.",
            "m = 54 g, V = 20 cm³. Nosaki blīvumu un materiālu.",
            "Cik liels tilpums ir 5,0 kg alumīnija (2700 kg/m³)?",
        ],
        pasvertejums=["Protu nosaukt materiālu īpašības",
                      "Protu lietot ρ = m/V", "Protu atpazīt materiālu",
                      "Protu pamatot izvēli"],
        nakama="Nākamā stunda: mehāniskais spriegums."),
),

dict(
    nr="5.2", virsraksts="Mehāniskais spriegums",
    jautajums="Kāpēc trosei ir slodzes robeža?",
    apaksraksts="σ = F/S · Stiprības robeža · Drošības rezerve",
    merkis="Iemācīties lietot σ = F/S, salīdzināt materiālu stiprību un "
           "pamatot drošības rezervi konstrukcijās.",
    protu=["skaidrot, kas ir mehāniskais spriegums;",
           "lietot σ = F/S un F = mg;",
           "salīdzināt spriegumu ar stiprības robežu;",
           "aprēķināt drošības koeficientu."],
    atkartojums="1.3. stundā mācījāmies, ka spiedienu rēķina p = F/S. "
                "Spriegums σ tiek rēķināts tāpat, bet raksturo materiāla "
                "iekšējo slodzi.",
    uzdevumu_apraksts="Spriegums, slodze un drošības rezerve",
    teorija=[
        ("Kas ir mehāniskais spriegums", [
            ("formula", "MEHĀNISKAIS SPRIEGUMS",
             "σ = F / S        [σ] = Pa = N/m²        F = m · g",
             "F — slodzes spēks [N], S — šķērsgriezuma laukums [m²]. "
             "Jo lielāks laukums, jo mazāks spriegums pie tās pašas slodzes.",
             GOLD),
            ("divi",
             ("KAS NOTIEK MATERIĀLĀ", BLUE,
              ["Slodze izstiepj daļiņu saites.",
               "Jo lielāks σ, jo vairāk izstieptas saites.",
               "Pārsniedzot robežu, saites plīst."]),
             ("STIPRĪBAS ROBEŽA  σ(max)", RED,
              ["Lielākais spriegums, ko materiāls iztur.",
               "Tērauds ~500 MPa, alumīnijs ~200 MPa,",
               "koks ~50 MPa, betons spiedē ~30 MPa.",
               "1 MPa = 10⁶ Pa"])),
        ]),
        ("Drošības rezerve", [
            ("formula", "DROŠĪBAS KOEFICIENTS",
             "k = σ(max) / σ",
             "Konstrukcijas projektē tā, lai k būtu 2–10 — atkarībā no tā, "
             "cik bīstamas ir sekas, ja tā salūztu.", GOLD),
            ("panelis", "KĀPĒC VAJAG REZERVI",
             ["Materiālā var būt slēpti defekti  ·  slodze var būt lielāka "
              "par plānoto  ·  materiāls laika gaitā nolietojas  ·  "
              "temperatūra un korozija maina īpašības.",
              "Tāpēc liftu trosēm k ≥ 10, bet parastām konstrukcijām "
              "pietiek ar k = 2–3."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Spriegums trosē",
             teksts="Trose ar šķērsgriezuma laukumu 2,0 cm² tur 800 kg "
                    "smagu kravu. g = 9,81 m/s².\n"
                    "Aprēķini mehānisko spriegumu trosē!",
             dots=["m = 800 kg", "S = 2,0 cm²", "g = 9,81 m/s²"],
             jaaprekina=["σ = ?"],
             formulas=["F = m · g", "σ = F / S"],
             aprekins=["1)  F = 800 · 9,81 = 7,85·10³ N",
                       "2)  S = 2,0 cm² = 2,0·10⁻⁴ m²",
                       "3)  σ = 7,85·10³ : 2,0·10⁻⁴ = 3,9·10⁷ Pa"],
             atbilde="σ ≈ 3,9·10⁷ Pa = 39 MPa",
             piezime="Tērauda stiprības robeža ~500 MPa, tātad rezerve ir "
                     "liela."),
        dict(nr=2, virsraksts="Drošības koeficients",
             teksts="Trosē spriegums ir 39 MPa, tērauda stiprības robeža "
                    "500 MPa.\nAprēķini drošības koeficientu un novērtē, vai "
                    "trose ir droša!",
             dots=["σ = 39 MPa", "σ(max) = 500 MPa"],
             jaaprekina=["k = ?"],
             formulas=["k = σ(max) / σ"],
             aprekins=["1)  k = 500 MPa : 39 MPa",
                       "2)  k = 12,8"],
             atbilde="k ≈ 13 — trose ir droša arī liftam",
             piezime="Liftu trosēm prasa k ≥ 10, tātad nosacījums izpildīts."),
        dict(nr=3, virsraksts="Nepieciešamais laukums",
             teksts="Stienim jātur 5,0 t krava. Materiāla pieļaujamais "
                    "spriegums ir 100 MPa. g = 9,81 m/s².\n"
                    "Aprēķini nepieciešamo šķērsgriezuma laukumu cm²!",
             dots=["m = 5,0 t = 5,0·10³ kg", "σ = 100 MPa = 1,0·10⁸ Pa"],
             jaaprekina=["S = ?  (cm²)"],
             formulas=["F = m · g", "σ = F / S", "S = F / σ"],
             aprekins=["1)  F = 5,0·10³ · 9,81 = 4,9·10⁴ N",
                       "2)  S = 4,9·10⁴ : 1,0·10⁸ = 4,9·10⁻⁴ m²",
                       "3)  S = 4,9 cm²"],
             atbilde="S ≈ 4,9·10⁻⁴ m² = 4,9 cm²",
             piezime="Praksē izvēlas nākamo standarta izmēru uz augšu."),
        dict(nr=4, virsraksts="Vai stieple izturēs?",
             teksts="Vara stieples diametrs ir 2,0 mm (S = 3,14 mm²), tai "
                    "pakar 60 kg. Vara stiprības robeža ir 220 MPa.\n"
                    "Vai stieple izturēs? Pamato ar aprēķinu!",
             dots=["m = 60 kg", "S = 3,14 mm²", "σ(max) = 220 MPa"],
             jaaprekina=["σ = ?", "Vai σ < σ(max)?"],
             formulas=["F = m · g", "σ = F / S"],
             aprekins=["1)  F = 60 · 9,81 = 5,9·10² N",
                       "2)  S = 3,14 mm² = 3,14·10⁻⁶ m²",
                       "3)  σ = 589 : 3,14·10⁻⁶ = 1,9·10⁸ Pa = 190 MPa",
                       "4)  190 MPa < 220 MPa"],
             atbilde="Izturēs, bet rezerve maza: k = 220/190 ≈ 1,2",
             piezime="Tik maza rezerve praksē nav pieļaujama — vajag biezāku "
                     "stiepli."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "σ = F/S — mehāniskais spriegums, mēra paskālos.",
            "Slodzes spēku aprēķina F = mg.",
            "Materiāls iztur, ja σ < σ(max) — stiprības robežas.",
            "Drošības koeficients k = σ(max)/σ; konstrukcijām k = 2–10.",
        ],
        majasdarbs=[
            "S = 5,0 cm², m = 1,2 t. Aprēķini spriegumu.",
            "σ(max) = 400 MPa, σ = 80 MPa. Aprēķini k.",
            "Cik liels S vajadzīgs 800 kg kravai, ja σ = 50 MPa?",
        ],
        pasvertejums=["Protu skaidrot spriegumu", "Protu lietot σ = F/S",
                      "Protu salīdzināt ar stiprības robežu",
                      "Protu aprēķināt drošības koeficientu"],
        nakama="Nākamā stunda: elastība un plastiskums."),
),

dict(
    nr="5.3", virsraksts="Elastība un plastiskums",
    jautajums="Kāpēc atspere atgriežas, bet plastilīns nē?",
    apaksraksts="Elastīga un plastiska deformācija · Huka likums · Fe = −kΔx",
    merkis="Iemācīties atšķirt elastīgu deformāciju no plastiskās un lietot "
           "Huka likumu atsperes aprēķinos.",
    protu=["atšķirt elastīgu un plastisku deformāciju;",
           "skaidrot deformāciju ar daļiņu saitēm;",
           "lietot Fe = −kΔx un aprēķināt stinguma koeficientu;",
           "nolasīt deformācijas grafiku."],
    atkartojums="5.2. stundā mācījāmies par spriegumu. Šodien skatīsim, kas "
                "ar materiālu notiek, kad slodze to izstiepj.",
    uzdevumu_apraksts="Huka likums un atsperes deformācija",
    teorija=[
        ("Divi deformācijas veidi", [
            ("divi",
             ("ELASTĪGA DEFORMĀCIJA", GREEN,
              ["Pēc slodzes noņemšanas forma ATJAUNOJAS.",
               "Daļiņu saites tikai izstiepjas, bet neplīst.",
               "Piemēri: atspere, gumija, tērauda sija.",
               "Šeit darbojas Huka likums."]),
             ("PLASTISKA DEFORMĀCIJA", RED,
              ["Forma paliek mainīta arī pēc slodzes noņemšanas.",
               "Daļiņas pārvietojas jaunās vietās.",
               "Piemēri: plastilīns, māls, kalts metāls.",
               "Izmanto metālu apstrādē un liešanā."])),
            ("panelis", "ELASTĪBAS ROBEŽA",
             ["Katram materiālam ir robeža: līdz tai deformācija ir elastīga, "
              "pēc tās — plastiska, un vēl tālāk materiāls plīst.",
              "Tāpēc konstrukcijas projektē tā, lai slodze paliktu elastīgajā "
              "apgabalā."], NAVY),
        ]),
        ("Huka likums", [
            ("formula", "HUKA LIKUMS",
             "Fe = −k · Δx        k = F / Δx        [k] = N/m",
             "Fe — elastības spēks, Δx — pagarinājums, k — stinguma "
             "koeficients. Mīnuss rāda, ka spēks vērsts pretēji "
             "deformācijai.", GOLD),
            ("kartitas", [
                ("STINGUMA KOEFICIENTS", BLUE,
                 ["Cik liels spēks vajadzīgs, lai izstieptu par 1 m.",
                  "k = 200 N/m nozīmē:",
                  "1 cm pagarinājumam vajag 2 N."]),
                ("GRAFIKS  F(Δx)", GREEN,
                 ["Elastīgajā apgabalā — taisne.",
                  "Taisnes slīpums ir k.",
                  "Aiz elastības robežas līnija liecas."]),
                ("PRAKSĒ", GOLD,
                 ["Atsperu svari, amortizatori,",
                  "atsperu matrači, dinamometri.",
                  "Visi darbojas elastīgajā apgabalā."]),
            ]),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Stinguma koeficients",
             teksts="Atsperi ar 12 N lielu spēku izstiepj par 6,0 cm.\n"
                    "Aprēķini atsperes stinguma koeficientu!",
             dots=["F = 12 N", "Δx = 6,0 cm"],
             jaaprekina=["k = ?"],
             formulas=["Fe = k · Δx", "k = F / Δx"],
             aprekins=["1)  Δx = 6,0 cm = 0,060 m",
                       "2)  k = 12 N : 0,060 m",
                       "3)  k = 2,0·10² N/m"],
             atbilde="k = 200 N/m",
             piezime="Vienmēr pārvērs centimetrus metros — citādi k iznāks "
                     "100 reižu par mazu."),
        dict(nr=2, virsraksts="Pagarinājums zem kravas",
             teksts="Atsperei ar k = 250 N/m pakar 2,0 kg smagu atsvaru. "
                    "g = 9,81 m/s².\nPar cik centimetriem atspere "
                    "pagarināsies?",
             dots=["k = 250 N/m", "m = 2,0 kg", "g = 9,81 m/s²"],
             jaaprekina=["Δx = ?  (cm)"],
             formulas=["F = m · g", "Δx = F / k"],
             aprekins=["1)  F = 2,0 · 9,81 = 19,6 N",
                       "2)  Δx = 19,6 N : 250 N/m = 0,0785 m",
                       "3)  Δx = 7,9 cm"],
             atbilde="Δx ≈ 7,9 cm",
             piezime="Tieši šo sakarību izmanto atsperu svaros."),
        dict(nr=3, virsraksts="Grafika slīpums",
             teksts="F(Δx) grafikā pie Δx = 4,0 cm spēks ir 10 N, bet pie "
                    "Δx = 12,0 cm spēks ir 30 N.\n"
                    "Aprēķini stinguma koeficientu un pārbaudi, vai "
                    "deformācija ir elastīga!",
             dots=["Δx₁ = 4,0 cm ;  F₁ = 10 N",
                   "Δx₂ = 12,0 cm ;  F₂ = 30 N"],
             jaaprekina=["k = ?"],
             formulas=["k = ΔF / Δ(Δx)"],
             aprekins=["1)  ΔF = 30 − 10 = 20 N",
                       "2)  Δ(Δx) = 0,120 − 0,040 = 0,080 m",
                       "3)  k = 20 : 0,080 = 250 N/m"],
             atbilde="k = 250 N/m — attiecība nemainīga, deformācija elastīga",
             piezime="Ja F/Δx abos punktos sakrīt, grafiks ir taisne un Huka "
                     "likums izpildās."),
        dict(nr=4, virsraksts="Divas atsperes",
             teksts="Pirmās atsperes k₁ = 150 N/m, otrās k₂ = 400 N/m. Abām "
                    "pakar vienādu 3,0 kg kravu.\n"
                    "Cik reižu vairāk pagarinās pirmā atspere?",
             dots=["k₁ = 150 N/m ;  k₂ = 400 N/m", "m = 3,0 kg"],
             jaaprekina=["n = ?"],
             formulas=["Δx = F / k", "n = Δx₁ / Δx₂ = k₂ / k₁"],
             aprekins=["1)  F = 3,0 · 9,81 = 29,4 N",
                       "2)  Δx₁ = 29,4 : 150 = 0,196 m",
                       "3)  Δx₂ = 29,4 : 400 = 0,0736 m",
                       "4)  n = 0,196 : 0,0736 = 2,7"],
             atbilde="n ≈ 2,7 reizes",
             piezime="To varēja aprēķināt arī īsāk: n = k₂/k₁ = 400/150 = 2,7."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Elastīgā deformācijā forma atjaunojas, plastiskajā — paliek "
            "mainīta.",
            "Huka likums Fe = −kΔx darbojas tikai līdz elastības robežai.",
            "k = F/Δx — stinguma koeficients, mēra N/m.",
            "F(Δx) grafika slīpums elastīgajā apgabalā ir k.",
        ],
        majasdarbs=[
            "F = 25 N izstiepj atsperi par 10 cm. Aprēķini k.",
            "k = 300 N/m, pakarts 1,5 kg. Aprēķini pagarinājumu cm.",
            "Nosauc divus elastīgas un divus plastiskas deformācijas "
            "piemērus.",
        ],
        pasvertejums=["Protu atšķirt deformācijas veidus",
                      "Protu lietot Huka likumu",
                      "Protu aprēķināt k un Δx",
                      "Protu nolasīt F(Δx) grafiku"],
        nakama="Nākamā stunda: siltumvadītspēja."),
),

dict(
    nr="5.4", virsraksts="Siltumvadītspēja",
    jautajums="Kāpēc metāls šķiet aukstāks par koku?",
    apaksraksts="Siltuma pārnese · Siltumvadītspēja · Siltumizolācija",
    merkis="Iemācīties salīdzināt materiālu siltumvadītspēju un pamatot "
           "siltumizolācijas materiāla izvēli mājoklim.",
    protu=["salīdzināt materiālus pēc siltumvadītspējas;",
           "skaidrot, kāpēc metāls šķiet aukstāks;",
           "aprēķināt siltuma zudumus caur sienu;",
           "pamatot siltumizolācijas materiāla izvēli."],
    atkartojums="3.11. stundā noskaidrojām, ka metālos ir brīvie elektroni. "
                "Tieši tie pārnes ne tikai lādiņu, bet arī siltumu.",
    uzdevumu_apraksts="Siltumvadītspēja un siltuma zudumi",
    teorija=[
        ("Kāpēc materiāli vada siltumu dažādi", [
            ("panelis", "SILTUMVADĪTSPĒJA  λ",
             ["Siltumvadītspēja rāda, cik viegli siltums izplatās materiālā. "
              "Mērvienība: W/(m·K).",
              "Metālos siltumu pārnes brīvie elektroni — tāpēc tie vada ļoti "
              "labi. Kokā un putuplastā ir gaisa poras, un gaiss vada "
              "siltumu ļoti slikti."], NAVY),
            ("tabula",
             ["Materiāls", "λ, W/(m·K)", "Vadītspēja", "Lietojums"],
             [["Varš", "400", "ļoti laba", "radiatori, katli"],
              ["Alumīnijs", "230", "ļoti laba", "siltummaiņi"],
              ["Tērauds", "50", "laba", "konstrukcijas"],
              ["Stikls", "1,0", "vāja", "logi"],
              ["Koks", "0,15", "ļoti vāja", "sienas, rāmji"],
              ["Minerālvate", "0,04", "izolators", "siltumizolācija"]],
             [3.03, 2.40, 2.60, 4.20]),
        ]),
        ("Siltuma zudumi un izolācija", [
            ("formula", "SILTUMA PLŪSMA CAUR SIENU",
             "P = λ · S · Δt / d",
             "P — siltuma jauda [W], S — laukums [m²], Δt — temperatūru "
             "starpība [K vai °C], d — sienas biezums [m].", GOLD),
            ("divi",
             ("KĀPĒC METĀLS ŠĶIET AUKSTĀKS", BLUE,
              ["Metāls un koks istabā ir VIENĀDĀ temperatūrā.",
               "Bet metāls ātri aizvada siltumu no rokas,",
               "tāpēc āda atdziest un mēs jūtam aukstumu.",
               "Mēs jūtam nevis temperatūru, bet siltuma plūsmu."]),
             ("KĀ SAMAZINĀT ZUDUMUS", GREEN,
              ["Izvēlēties materiālu ar mazu λ.",
               "Palielināt izolācijas biezumu d.",
               "Novērst siltuma tiltus un caurvēju.",
               "Logiem — vairākas stikla kārtas ar gaisu starp tām."])),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Siltuma zudumi caur sienu",
             teksts="Sienas laukums ir 20 m², biezums 0,30 m, "
                    "λ = 0,60 W/(m·K). Iekšā 21 °C, ārā 1 °C.\n"
                    "Aprēķini siltuma zudumu jaudu!",
             dots=["S = 20 m²", "d = 0,30 m", "λ = 0,60 W/(m·K)",
                   "Δt = 20 °C"],
             jaaprekina=["P = ?"],
             formulas=["P = λ · S · Δt / d"],
             aprekins=["1)  Δt = 21 − 1 = 20 °C",
                       "2)  P = 0,60 · 20 · 20 : 0,30",
                       "3)  P = 240 : 0,30 = 800 W"],
             atbilde="P = 800 W",
             piezime="Tas ir gandrīz kā viens sildītājs, kas strādā "
                     "nepārtraukti."),
        dict(nr=2, virsraksts="Izolācijas efekts",
             teksts="Tai pašai sienai pievieno 10 cm minerālvates "
                    "(λ = 0,040 W/(m·K)), kas viena pati dotu 160 W "
                    "zudumus.\nCik reižu samazinātos zudumi, ja siena "
                    "zaudētu 800 W?",
             dots=["P₁ = 800 W", "P₂ = 160 W"],
             jaaprekina=["n = ?"],
             formulas=["n = P₁ / P₂"],
             aprekins=["1)  n = 800 W : 160 W",
                       "2)  n = 5,0"],
             atbilde="n = 5,0 reizes mazāki zudumi",
             piezime="10 cm minerālvates aizstāj gandrīz pusotru metru "
                     "ķieģeļu sienas."),
        dict(nr=3, virsraksts="Nepieciešamais biezums",
             teksts="Jāpanāk, lai caur 15 m² sienu pie Δt = 25 °C zudumi "
                    "nepārsniegtu 300 W. Materiāla λ = 0,040 W/(m·K).\n"
                    "Cik biezs izolācijas slānis vajadzīgs?",
             dots=["S = 15 m²", "Δt = 25 °C", "λ = 0,040 W/(m·K)",
                   "P = 300 W"],
             jaaprekina=["d = ?  (cm)"],
             formulas=["P = λ·S·Δt / d", "d = λ·S·Δt / P"],
             aprekins=["1)  λ·S·Δt = 0,040 · 15 · 25 = 15 W·m",
                       "2)  d = 15 : 300 = 0,050 m",
                       "3)  d = 5,0 cm"],
             atbilde="d = 0,050 m = 5,0 cm",
             piezime="Praksē liek biezāku slāni, jo siltums izplūst arī caur "
                     "logiem un jumtu."),
        dict(nr=4, virsraksts="Divu materiālu salīdzinājums",
             teksts="Divas vienāda izmēra un biezuma sienas: viena no koka "
                    "(λ = 0,15), otra no tērauda (λ = 50).\n"
                    "Cik reižu vairāk siltuma zaudē tērauda siena?",
             dots=["λ₁ = 0,15 W/(m·K)", "λ₂ = 50 W/(m·K)"],
             jaaprekina=["n = ?"],
             formulas=["P ~ λ", "n = λ₂ / λ₁"],
             aprekins=["1)  n = 50 : 0,15",
                       "2)  n = 333"],
             atbilde="n ≈ 3,3·10² reižu vairāk",
             piezime="Tāpēc metāla konstrukcijās vienmēr paredz "
                     "siltumizolāciju — citādi rodas siltuma tilti."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Siltumvadītspēju raksturo λ [W/(m·K)]: metāliem liela, "
            "izolatoriem maza.",
            "P = λ·S·Δt/d — siltuma zudumi aug ar laukumu un temperatūru "
            "starpību, sarūk ar biezumu.",
            "Metāls šķiet aukstāks, jo ātri aizvada siltumu no ādas.",
            "Laba izolācija = mazs λ un pietiekams biezums.",
        ],
        majasdarbs=[
            "S = 10 m², d = 0,20 m, λ = 0,50, Δt = 18 °C. Aprēķini P.",
            "Cik biezs slānis (λ = 0,04) vajadzīgs, lai caur 12 m² pie "
            "Δt = 20 °C zudumi būtu 200 W?",
            "Paskaidro, kāpēc ziemā metāla margas šķiet aukstākas par koka "
            "margām.",
        ],
        pasvertejums=["Protu salīdzināt λ vērtības",
                      "Protu aprēķināt siltuma zudumus",
                      "Protu noteikt vajadzīgo biezumu",
                      "Protu pamatot izolācijas izvēli"],
        nakama="Nākamā stunda: elektrovadītspēja."),
),

dict(
    nr="5.5", virsraksts="Elektrovadītspēja",
    jautajums="Kas vada elektrisko strāvu un kas ne?",
    apaksraksts="Vadītāji · Dielektriķi · Pusvadītāji · R = ρl/S",
    merkis="Iemācīties nošķirt vadītājus, dielektriķus un pusvadītājus un "
           "aprēķināt vadītāja pretestību pēc tā izmēriem un materiāla.",
    protu=["nošķirt vadītājus, dielektriķus un pusvadītājus;",
           "saistīt vadītspēju ar vielas uzbūvi;",
           "lietot R = ρ·l/S;",
           "pamatot vada materiāla un biezuma izvēli."],
    atkartojums="3.11. stundā: metāliskajā režģī ir brīvie elektroni. Tieši "
                "tie padara metālus par labiem elektrības vadītājiem.",
    uzdevumu_apraksts="Vadītāja pretestība un materiāla izvēle",
    teorija=[
        ("Trīs materiālu grupas", [
            ("kartitas", [
                ("VADĪTĀJI", BLUE,
                 ["Daudz brīvo lādiņnesēju.",
                  "Metāli, grafīts, sāļu šķīdumi.",
                  "Maza īpatnējā pretestība ρ.",
                  "Lieto vados un kontaktos."]),
                ("DIELEKTRIĶI", RED,
                 ["Praktiski nav brīvo lādiņnesēju.",
                  "Gumija, stikls, plastmasa, sauss koks.",
                  "Ļoti liela pretestība.",
                  "Lieto izolācijai."]),
                ("PUSVADĪTĀJI", GREEN,
                 ["Vadītspēja starp abām grupām.",
                  "Silīcijs, germānijs.",
                  "Vadītspēja aug, sildot un apgaismojot.",
                  "Lieto diodēs, tranzistoros, čipos."]),
            ]),
            ("formula", "VADĪTĀJA PRETESTĪBA",
             "R = ρ · l / S        [R] = Ω",
             "ρ — īpatnējā pretestība [Ω·m], l — vada garums [m], "
             "S — šķērsgriezuma laukums [m²]. Garāks vads — lielāka "
             "pretestība; biezāks vads — mazāka.", GOLD),
        ]),
        ("Materiālu izvēle elektrotehnikā", [
            ("tabula",
             ["Materiāls", "ρ, Ω·m", "Grupa", "Kur lieto"],
             [["Sudrabs", "1,6·10⁻⁸", "vadītājs", "precīzi kontakti"],
              ["Varš", "1,7·10⁻⁸", "vadītājs", "elektroinstalācija"],
              ["Alumīnijs", "2,8·10⁻⁸", "vadītājs", "gaisvadu līnijas"],
              ["Nihroms", "1,1·10⁻⁶", "vadītājs", "sildelementi"],
              ["Silīcijs", "~10³", "pusvadītājs", "mikroshēmas"],
              ["Gumija", "~10¹³", "dielektriķis", "vadu izolācija"]],
             [2.83, 2.30, 2.60, 4.50]),
            ("panelis", "KĀPĒC AUGSTSPRIEGUMA LĪNIJĀS IR ALUMĪNIJS",
             ["Varam ir mazāka pretestība, bet alumīnijs ir gandrīz trīs "
              "reizes vieglāks un lētāks. Gariem gaisvadiem svarīgāks ir "
              "svars, tāpēc izvēlas alumīniju; mājas instalācijā — varu."],
             NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Vara vada pretestība",
             teksts="Vara vada garums ir 50 m, šķērsgriezuma laukums "
                    "1,5 mm², ρ = 1,7·10⁻⁸ Ω·m.\n"
                    "Aprēķini vada pretestību!",
             dots=["l = 50 m", "S = 1,5 mm²", "ρ = 1,7·10⁻⁸ Ω·m"],
             jaaprekina=["R = ?"],
             formulas=["R = ρ · l / S"],
             aprekins=["1)  S = 1,5 mm² = 1,5·10⁻⁶ m²",
                       "2)  R = 1,7·10⁻⁸ · 50 : 1,5·10⁻⁶",
                       "3)  R = 8,5·10⁻⁷ : 1,5·10⁻⁶ = 0,57 Ω"],
             atbilde="R ≈ 0,57 Ω",
             piezime="Maza pretestība nozīmē mazus enerģijas zudumus vadā."),
        dict(nr=2, virsraksts="Divreiz garāks vads",
             teksts="Vada pretestība ir 4,0 Ω. To nomaina pret tāda paša "
                    "materiāla un biezuma vadu, kas ir divreiz garāks.\n"
                    "Kāda būs jaunā pretestība? Pamato ar formulu!",
             dots=["R₁ = 4,0 Ω", "l₂ = 2·l₁", "S un ρ nemainās"],
             jaaprekina=["R₂ = ?"],
             formulas=["R = ρ·l/S", "R ~ l"],
             aprekins=["1)  R ~ l, ja ρ un S nemainās",
                       "2)  R₂ = 2 · R₁",
                       "3)  R₂ = 2 · 4,0 = 8,0 Ω"],
             atbilde="R₂ = 8,0 Ω",
             piezime="Divreiz garāks vads — divreiz lielāka pretestība."),
        dict(nr=3, virsraksts="Vajadzīgais šķērsgriezums",
             teksts="Alumīnija vadam (ρ = 2,8·10⁻⁸ Ω·m) 200 m garumā "
                    "pretestība nedrīkst pārsniegt 1,0 Ω.\n"
                    "Aprēķini nepieciešamo šķērsgriezuma laukumu mm²!",
             dots=["l = 200 m", "ρ = 2,8·10⁻⁸ Ω·m", "R = 1,0 Ω"],
             jaaprekina=["S = ?  (mm²)"],
             formulas=["R = ρ·l/S", "S = ρ·l/R"],
             aprekins=["1)  S = 2,8·10⁻⁸ · 200 : 1,0",
                       "2)  S = 5,6·10⁻⁶ m²",
                       "3)  S = 5,6 mm²"],
             atbilde="S = 5,6·10⁻⁶ m² = 5,6 mm²",
             piezime="Praksē izvēlas standarta vadu 6 mm²."),
        dict(nr=4, virsraksts="Sildelements",
             teksts="Nihroma stieples (ρ = 1,1·10⁻⁶ Ω·m) garums ir 2,0 m, "
                    "S = 0,10 mm².\nAprēķini pretestību un paskaidro, kāpēc "
                    "sildelementos lieto nihromu, nevis varu!",
             dots=["l = 2,0 m", "S = 0,10 mm²", "ρ = 1,1·10⁻⁶ Ω·m"],
             jaaprekina=["R = ?"],
             formulas=["R = ρ · l / S"],
             aprekins=["1)  S = 0,10 mm² = 1,0·10⁻⁷ m²",
                       "2)  R = 1,1·10⁻⁶ · 2,0 : 1,0·10⁻⁷",
                       "3)  R = 2,2·10⁻⁶ : 1,0·10⁻⁷ = 22 Ω"],
             atbilde="R = 22 Ω — liela pretestība rada daudz siltuma",
             piezime="Nihroma ρ ir ~65 reižu lielāks nekā varam, un tas "
                     "neoksidējas augstā temperatūrā."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Vadītājos ir brīvi lādiņnesēji, dielektriķos to praktiski nav.",
            "Pusvadītāju vadītspēja aug, tos sildot vai apgaismojot.",
            "R = ρ·l/S: garāks vads — lielāka R, biezāks vads — mazāka R.",
            "Materiālu izvēlas pēc ρ, svara un cenas: varš mājās, alumīnijs "
            "līnijās, nihroms sildītājos.",
        ],
        majasdarbs=[
            "l = 100 m, S = 2,5 mm², ρ = 1,7·10⁻⁸ Ω·m. Aprēķini R.",
            "Vada S palielina divas reizes. Kā mainās R?",
            "Cik garš nihroma vads (ρ = 1,1·10⁻⁶, S = 0,20 mm²) dod "
            "R = 55 Ω?",
        ],
        pasvertejums=["Protu nošķirt materiālu grupas",
                      "Protu lietot R = ρl/S",
                      "Protu aprēķināt vajadzīgo šķērsgriezumu",
                      "Protu pamatot materiāla izvēli"],
        nakama="Nākamā stunda: materiālu grupas."),
),

dict(
    nr="5.6", virsraksts="Materiālu grupas",
    jautajums="Ar ko metāli atšķiras no polimēriem?",
    apaksraksts="Metāli · Keramika · Polimēri · Kompozīti",
    merkis="Iemācīties salīdzināt četras materiālu grupas pēc uzbūves, "
           "īpašībām un lietojuma un izvēlēties grupu konkrētam uzdevumam.",
    protu=["nosaukt četras materiālu grupas;",
           "salīdzināt tās pēc blīvuma, izturības un vadītspējas;",
           "saistīt īpašības ar uzbūvi;",
           "izvēlēties materiālu grupu dotai situācijai."],
    atkartojums="5.1.–5.5. stundā mācījāmies atsevišķas īpašības. Šodien "
                "saliksim tās kopā un salīdzināsim materiālu grupas.",
    uzdevumu_apraksts="Grupu salīdzināšana ar aprēķiniem",
    teorija=[
        ("Četras materiālu grupas", [
            ("tabula",
             ["Grupa", "Uzbūve", "Blīvums", "Izturība", "Vadītspēja",
              "Piemēri"],
             [["Metāli", "metāliskais režģis", "liels", "liela, kaļami",
               "ļoti laba", "tērauds, Al, Cu"],
              ["Keramika", "jonu/atomu režģis", "vidējs",
               "cieta, trausla", "nevada", "porcelāns, betons"],
              ["Polimēri", "garas molekulu ķēdes", "mazs",
               "elastīgi, mīksti", "nevada", "PE, PVC, gumija"],
              ["Kompozīti", "divu materiālu savienojums", "mazs",
               "ļoti liela", "atkarīga", "stiklšķiedra, ogļšķiedra"]],
             [2.13, 2.90, 1.50, 2.10, 1.80, 1.80]),
        ]),
        ("Kā izvēlas grupu", [
            ("kartitas", [
                ("VAJAG IZTURĪBU UN VADĪTSPĒJU", BLUE,
                 ["→ METĀLI", "Konstrukcijas, vadi, mašīnas.",
                  "Trūkums: smagi un korodē."]),
                ("VAJAG KARSTUMIZTURĪBU", GOLD,
                 ["→ KERAMIKA", "Krāsnis, izolatori, flīzes.",
                  "Trūkums: trausla."]),
                ("VAJAG VIEGLUMU UN ELASTĪBU", GREEN,
                 ["→ POLIMĒRI vai KOMPOZĪTI",
                  "Iepakojums, caurules, lidmašīnu detaļas.",
                  "Trūkums: zema kušanas temperatūra."]),
            ]),
            ("panelis", "KOMPOZĪTS — labākais no diviem",
             ["Kompozītā apvieno divus materiālus tā, lai katrs dotu savu "
              "labāko īpašību: ogļšķiedra dod izturību, sveķi — formu un "
              "saistību.",
              "Rezultāts: materiāls, kas ir vieglāks par alumīniju, bet "
              "izturīgāks par tēraudu. Tāpēc to lieto lidmašīnās, "
              "velosipēdos un vēja ģeneratoru lāpstiņās."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Svara ietaupījums",
             teksts="Detaļas tilpums ir 2,0·10⁻³ m³. To var izgatavot no "
                    "tērauda (7800 kg/m³) vai ogļšķiedras kompozīta "
                    "(1600 kg/m³).\nPar cik kilogramiem kompozīts ir "
                    "vieglāks?",
             dots=["V = 2,0·10⁻³ m³", "ρ₁ = 7800 kg/m³", "ρ₂ = 1600 kg/m³"],
             jaaprekina=["Δm = ?"],
             formulas=["m = ρ · V", "Δm = m₁ − m₂"],
             aprekins=["1)  m₁ = 7800 · 2,0·10⁻³ = 15,6 kg",
                       "2)  m₂ = 1600 · 2,0·10⁻³ = 3,2 kg",
                       "3)  Δm = 15,6 − 3,2 = 12,4 kg"],
             atbilde="Δm = 12,4 kg — kompozīts gandrīz 5× vieglāks",
             piezime="Tāpēc lidmašīnu korpusos arvien vairāk lieto "
                     "kompozītus."),
        dict(nr=2, virsraksts="Īpatnējā izturība",
             teksts="Tērauda σ(max) = 500 MPa, ρ = 7800 kg/m³. Ogļšķiedras "
                    "σ(max) = 600 MPa, ρ = 1600 kg/m³.\n"
                    "Aprēķini abiem īpatnējo izturību σ/ρ un salīdzini!",
             dots=["Tērauds: 500 MPa ;  7800 kg/m³",
                   "Kompozīts: 600 MPa ;  1600 kg/m³"],
             jaaprekina=["j₁ = ?", "j₂ = ?"],
             formulas=["j = σ(max) / ρ"],
             aprekins=["1)  j₁ = 5,0·10⁸ : 7800 = 6,4·10⁴ Pa·m³/kg",
                       "2)  j₂ = 6,0·10⁸ : 1600 = 3,8·10⁵ Pa·m³/kg",
                       "3)  j₂ / j₁ = 3,8·10⁵ : 6,4·10⁴ = 5,9"],
             atbilde="Kompozīts pēc īpatnējās izturības ~6× labāks",
             piezime="Aviācijā svarīga nevis izturība vien, bet izturība uz "
                     "masas vienību."),
        dict(nr=3, virsraksts="Keramikas flīze",
             teksts="Keramikas flīzes izmēri 30 cm × 30 cm × 8,0 mm, "
                    "blīvums 2300 kg/m³.\nAprēķini vienas flīzes masu!",
             dots=["a = b = 30 cm ;  d = 8,0 mm", "ρ = 2300 kg/m³"],
             jaaprekina=["m = ?"],
             formulas=["V = a · b · d", "m = ρ · V"],
             aprekins=["1)  V = 0,30 · 0,30 · 8,0·10⁻³ = 7,2·10⁻⁴ m³",
                       "2)  m = 2300 · 7,2·10⁻⁴",
                       "3)  m = 1,66 kg"],
             atbilde="m ≈ 1,7 kg",
             piezime="Zinot vienas flīzes masu, var aprēķināt slodzi uz "
                     "pārsegumu."),
        dict(nr=4, virsraksts="Polimēra caurule",
             teksts="Polietilēna caurules (950 kg/m³) garums 6,0 m, sienas "
                    "tilpums 3,0·10⁻³ m³. Tāda pati tērauda caurule svērtu "
                    "23,4 kg.\nCik reižu polimēra caurule ir vieglāka?",
             dots=["V = 3,0·10⁻³ m³", "ρ = 950 kg/m³", "m₂ = 23,4 kg"],
             jaaprekina=["m₁ = ?", "n = ?"],
             formulas=["m = ρ · V", "n = m₂ / m₁"],
             aprekins=["1)  m₁ = 950 · 3,0·10⁻³ = 2,85 kg",
                       "2)  n = 23,4 : 2,85",
                       "3)  n = 8,2"],
             atbilde="m₁ = 2,85 kg ;   n ≈ 8,2 reizes vieglāka",
             piezime="Polimēra caurules arī nekorodē — tāpēc tās aizstāj "
                     "metāla ūdensvadus."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Četras grupas: metāli, keramika, polimēri, kompozīti.",
            "Metāli — izturīgi un vadoši; keramika — cieta un trausla.",
            "Polimēri — viegli un elastīgi; kompozīti apvieno labākās "
            "īpašības.",
            "Aviācijā svarīga īpatnējā izturība σ/ρ, nevis izturība vien.",
        ],
        majasdarbs=[
            "Salīdzini alumīnija (2700) un polietilēna (950) detaļas masu "
            "pie V = 1,5·10⁻³ m³.",
            "Aprēķini īpatnējo izturību alumīnijam (200 MPa; 2700 kg/m³).",
            "Kurai grupai pieder: porcelāns, gumija, misiņš, stiklšķiedra?",
        ],
        pasvertejums=["Protu nosaukt grupas",
                      "Protu salīdzināt īpašības",
                      "Protu aprēķināt masu un izturību",
                      "Protu izvēlēties grupu"],
        nakama="Nākamā stunda: moderni materiāli."),
),

dict(
    nr="5.7", virsraksts="Moderni materiāli",
    jautajums="Kādus materiālus rada mūsdienās?",
    apaksraksts="Nanomateriāli · Kompozīti · Viedie materiāli",
    merkis="Raksturot moderno materiālu īpašības un pamatot jaunu materiālu "
           "izstrādes nepieciešamību, arī Latvijā.",
    protu=["nosaukt moderno materiālu veidus un īpašības;",
           "novērtēt nanomateriālu izmēru kārtu;",
           "aprēķināt virsmas laukuma pieaugumu sasmalcinot;",
           "pamatot jaunu materiālu izstrādes nepieciešamību."],
    atkartojums="1.2. stundā noskaidrojām, ka nanometrs ir 10⁻⁹ m. Tieši "
                "šajā mērogā strādā nanotehnoloģijas.",
    uzdevumu_apraksts="Nanomateriālu mērogs un virsmas laukums",
    teorija=[
        ("Moderno materiālu veidi", [
            ("kartitas", [
                ("NANOMATERIĀLI", BLUE,
                 ["Daļiņas 1–100 nm.",
                  "Milzīgs virsmas laukums.",
                  "Grafēns, oglekļa nanocaurulītes.",
                  "Lieto akumulatoros, filtros, pārklājumos."]),
                ("KOMPOZĪTI", GREEN,
                 ["Divu materiālu apvienojums.",
                  "Ogļšķiedra, stiklšķiedra, dzelzsbetons.",
                  "Viegli un ļoti izturīgi.",
                  "Lidmašīnas, vēja ģeneratori, sports."]),
                ("VIEDIE MATERIĀLI", GOLD,
                 ["Maina īpašības atkarībā no apstākļiem.",
                  "Formas atmiņas sakausējumi.",
                  "Fotohromie stikli, pjezomateriāli.",
                  "Medicīna, sensori, būvniecība."]),
            ]),
            ("panelis", "KĀPĒC NANOMĒROGĀ ĪPAŠĪBAS MAINĀS",
             ["Sasmalcinot vielu, tās kopējais virsmas laukums strauji aug. "
              "Uz virsmas esošie atomi uzvedas citādi nekā iekšienē — tāpēc "
              "nanodaļiņām mainās krāsa, ķīmiskā aktivitāte un stiprība.",
              "Piemēram, grafēns — viena oglekļa atoma biezs slānis — ir "
              "~200 reižu izturīgāks par tēraudu."], NAVY),
        ]),
        ("Kāpēc vajag jaunus materiālus", [
            ("divi",
             ("IEMESLI", BLUE,
              ["Vieglākas un drošākas konstrukcijas.",
               "Mazāks enerģijas patēriņš.",
               "Aizstāt retas un dārgas izejvielas.",
               "Videi draudzīgāka ražošana un pārstrāde."]),
             ("LATVIJĀ", GREEN,
              ["Koksnes kompozīti un modificēta koksne.",
               "Siltumizolācijas materiāli no lina un kaņepēm.",
               "Optiskās šķiedras un plāno kārtiņu tehnoloģijas.",
               "Augstas pievienotās vērtības produkti no vietējiem "
               "resursiem."])),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Nanodaļiņas izmērs",
             teksts="Nanodaļiņas diametrs ir 20 nm, atoma diametrs "
                    "0,20 nm.\nCik atomu izvietotos gar nanodaļiņas "
                    "diametru?",
             dots=["d = 20 nm", "d(atoma) = 0,20 nm"],
             jaaprekina=["N = ?"],
             formulas=["N = d / d(atoma)"],
             aprekins=["1)  N = 20 nm : 0,20 nm",
                       "2)  N = 1,0·10²"],
             atbilde="N = 100 atomu",
             piezime="Tik maza daļiņa, ka liela daļa tās atomu atrodas uz "
                     "virsmas."),
        dict(nr=2, virsraksts="Virsmas laukuma pieaugums",
             teksts="Kubs ar malu 1,0 cm sadalīts kubiņos ar malu 1,0 mm.\n"
                    "Cik kubiņu rodas un cik reižu palielinās kopējais "
                    "virsmas laukums?",
             dots=["a₁ = 1,0 cm = 10 mm", "a₂ = 1,0 mm"],
             jaaprekina=["N = ?", "n = ?"],
             formulas=["N = (a₁/a₂)³", "S = 6a²", "n = N·S₂ / S₁"],
             aprekins=["1)  N = (10 : 1)³ = 1000 kubiņu",
                       "2)  S₁ = 6 · 10² = 600 mm²",
                       "3)  S₂(kopā) = 1000 · 6 · 1² = 6000 mm²",
                       "4)  n = 6000 : 600 = 10"],
             atbilde="N = 1000 kubiņu ;   virsma palielinās 10 reižu",
             piezime="Sadalot vēl sīkāk — līdz nanoizmēram — virsma "
                     "palielinās tūkstošiem reižu."),
        dict(nr=3, virsraksts="Grafēna izturība",
             teksts="Grafēna stiprības robeža ir 1,3·10¹¹ Pa, tērauda — "
                    "5,0·10⁸ Pa.\nCik reižu grafēns ir izturīgāks?",
             dots=["σ₁ = 1,3·10¹¹ Pa", "σ₂ = 5,0·10⁸ Pa"],
             jaaprekina=["n = ?"],
             formulas=["n = σ₁ / σ₂"],
             aprekins=["1)  n = 1,3·10¹¹ : 5,0·10⁸",
                       "2)  n = 2,6·10²"],
             atbilde="n = 260 reižu izturīgāks par tēraudu",
             piezime="Grafēns ir tikai viena atoma biezs, tāpēc praksē to "
                     "izmanto kā piedevu citiem materiāliem."),
        dict(nr=4, virsraksts="Kompozīta sastāvs",
             teksts="Kompozīta paraugā ir 0,60 kg sveķu (ρ = 1200 kg/m³) un "
                    "0,90 kg ogļšķiedras (ρ = 1800 kg/m³).\n"
                    "Aprēķini kompozīta vidējo blīvumu!",
             dots=["m₁ = 0,60 kg ;  ρ₁ = 1200 kg/m³",
                   "m₂ = 0,90 kg ;  ρ₂ = 1800 kg/m³"],
             jaaprekina=["ρ = ?"],
             formulas=["V = m / ρ", "ρ = (m₁+m₂) / (V₁+V₂)"],
             aprekins=["1)  V₁ = 0,60 : 1200 = 5,0·10⁻⁴ m³",
                       "2)  V₂ = 0,90 : 1800 = 5,0·10⁻⁴ m³",
                       "3)  ρ = 1,50 kg : 1,0·10⁻³ m³ = 1500 kg/m³"],
             atbilde="ρ = 1,5·10³ kg/m³",
             piezime="Vidējais blīvums vienmēr ir starp abu komponentu "
                     "blīvumiem."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Nanomateriālu daļiņas ir 1–100 nm; to virsmas laukums ir milzīgs.",
            "Sasmalcinot materiālu, kopējais virsmas laukums strauji aug.",
            "Kompozīti apvieno divu materiālu labākās īpašības.",
            "Jaunus materiālus izstrādā, lai taupītu enerģiju, resursus un "
            "samazinātu ietekmi uz vidi.",
        ],
        majasdarbs=[
            "Nanodaļiņa 50 nm, atoms 0,25 nm. Cik atomu gar diametru?",
            "Kubu ar malu 2,0 cm sadala kubiņos ar malu 2,0 mm. Cik to ir?",
            "Nosauc divus modernus materiālus un to lietojumu.",
        ],
        pasvertejums=["Protu nosaukt moderno materiālu veidus",
                      "Protu novērtēt nanomērogu",
                      "Protu aprēķināt virsmas pieaugumu",
                      "Protu pamatot jaunu materiālu vajadzību"],
        nakama="Nākamā stunda: materiāla izvēle ar aprēķinu — gatavošanās "
               "PD3."),
),

dict(
    nr="5.8", virsraksts="Materiāla izvēle ar aprēķinu",
    jautajums="Kā pamatot izvēli ar skaitļiem?",
    apaksraksts="Nostiprināšana · Jauktie uzdevumi · Gatavošanās PD3",
    merkis="Nostiprināt temata saturu un iemācīties ar aprēķiniem pamatot "
           "materiāla izvēli dotai situācijai.",
    protu=["izvēlēties pareizo formulu temata uzdevumos;",
           "apvienot vairākas sakarības vienā risinājumā;",
           "pamatot materiāla izvēli ar skaitļiem;",
           "pārbaudīt mērvienības un rezultāta ticamību."],
    atkartojums="Šī ir pēdējā stunda pirms PD3. Atkārtojam: ρ = m/V, "
                "σ = F/S, Fe = kΔx, siltuma zudumi un R = ρl/S.",
    uzdevumu_apraksts="Jauktie temata uzdevumi — gatavošanās PD3",
    teorija=[
        ("Temata formulas vienuviet", [
            ("tabula",
             ["Kas jāatrod", "Formula", "Kur lieto"],
             [["Blīvums, masa, tilpums", "ρ = m / V", "materiāla atpazīšana"],
              ["Slodzes spēks", "F = m · g", "konstrukcijas"],
              ["Mehāniskais spriegums", "σ = F / S", "izturība"],
              ["Drošības koeficients", "k = σ(max) / σ", "projektēšana"],
              ["Elastības spēks", "Fe = k · Δx", "atsperes"],
              ["Siltuma zudumi", "P = λ·S·Δt / d", "izolācija"],
              ["Vadītāja pretestība", "R = ρ · l / S", "elektrotehnika"]],
             [3.63, 4.60, 4.00]),
        ]),
        ("Kā pamato izvēli", [
            ("kartitas", [
                ("1. NOSAKI PRASĪBU", BLUE,
                 ["Kas ir svarīgākais?",
                  "Svars, izturība, vadītspēja",
                  "vai siltumizolācija?"]),
                ("2. APRĒĶINI", GREEN,
                 ["Aprēķini vajadzīgo lielumu",
                  "katram materiālam.",
                  "Lieto vienas un tās pašas vienības."]),
                ("3. SALĪDZINI UN PAMATO", GOLD,
                 ["Salīdzini skaitļus.",
                  "Atbildē nosauc materiālu",
                  "UN paskaidro, kāpēc tieši to."]),
            ]),
            ("panelis", "BIEŽĀKĀS KĻŪDAS PD",
             ["cm³ nepārvērš m³ (kļūda 10⁶ reižu)  ·  mm² nepārvērš m² "
              "(10⁶)  ·  aizmirst F = mg un lieto masu spēka vietā  ·  "
              "MPa nepārvērš Pa  ·  atbildē trūkst mērvienības."], RED),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Jaukts: masa un spriegums",
             teksts="Tērauda stienis (7800 kg/m³) ir 2,0 m garš, "
                    "S = 4,0 cm². Tam pakar 1,5 t kravu.\n"
                    "Aprēķini stieņa masu un spriegumu tajā!",
             dots=["l = 2,0 m ;  S = 4,0 cm²", "ρ = 7800 kg/m³",
                   "m(kr) = 1,5·10³ kg"],
             jaaprekina=["m = ?", "σ = ?"],
             formulas=["V = S · l", "m = ρ · V", "σ = F / S"],
             aprekins=["1)  V = 4,0·10⁻⁴ · 2,0 = 8,0·10⁻⁴ m³",
                       "2)  m = 7800 · 8,0·10⁻⁴ = 6,24 kg",
                       "3)  F = 1,5·10³ · 9,81 = 1,47·10⁴ N",
                       "4)  σ = 1,47·10⁴ : 4,0·10⁻⁴ = 3,7·10⁷ Pa"],
             atbilde="m ≈ 6,2 kg ;   σ ≈ 37 MPa",
             piezime="Stieņa paša svars (6 kg) ir niecīgs salīdzinājumā ar "
                     "1,5 t kravu."),
        dict(nr=2, virsraksts="Jaukts: divu materiālu izvēle",
             teksts="Detaļai V = 1,0·10⁻³ m³ jābūt vieglai un jāiztur "
                    "12 kN slodze pie S = 2,0 cm². Alumīnijs: 2700 kg/m³, "
                    "σ(max) = 200 MPa. Tērauds: 7800 kg/m³, 500 MPa.\n"
                    "Kuru izvēlēties?",
             dots=["F = 12 kN ;  S = 2,0 cm²", "Al: 2700 ;  200 MPa",
                   "Fe: 7800 ;  500 MPa"],
             jaaprekina=["σ = ?", "Materiāls = ?"],
             formulas=["σ = F / S", "k = σ(max) / σ", "m = ρ · V"],
             aprekins=["1)  σ = 1,2·10⁴ : 2,0·10⁻⁴ = 6,0·10⁷ Pa = 60 MPa",
                       "2)  k(Al) = 200 : 60 = 3,3  →  iztur",
                       "3)  m(Al) = 2700 · 1,0·10⁻³ = 2,7 kg",
                       "4)  m(Fe) = 7800 · 1,0·10⁻³ = 7,8 kg"],
             atbilde="Alumīnijs: iztur (k = 3,3) un ir 2,9× vieglāks",
             piezime="Ja abi iztur, izvēlas vieglāko — tā ir pamatota "
                     "izvēle."),
        dict(nr=3, virsraksts="Jaukts: izolācija",
             teksts="Mājas siena 40 m², λ = 0,50 W/(m·K), d = 0,25 m. "
                    "Iekšā 22 °C, ārā −8 °C.\n"
                    "Aprēķini zudumu jaudu un enerģiju, kas aizplūst "
                    "diennaktī (kWh)!",
             dots=["S = 40 m² ;  d = 0,25 m", "λ = 0,50 W/(m·K)",
                   "Δt = 30 °C ;  t = 24 h"],
             jaaprekina=["P = ?", "A = ?  (kWh)"],
             formulas=["P = λ·S·Δt / d", "A = P · t"],
             aprekins=["1)  P = 0,50 · 40 · 30 : 0,25 = 2400 W",
                       "2)  P = 2,4 kW",
                       "3)  A = 2,4 kW · 24 h = 58 kWh"],
             atbilde="P = 2,4 kW ;   A ≈ 58 kWh diennaktī",
             piezime="Pie 0,20 EUR/kWh tas ir ~11,50 EUR dienā tikai caur "
                     "vienu sienu."),
        dict(nr=4, virsraksts="Jaukts: vads un atspere",
             teksts="a) Vara vads (ρ = 1,7·10⁻⁸ Ω·m), l = 25 m, "
                    "S = 1,0 mm². b) Atspere ar k = 500 N/m, kurai pakar "
                    "4,0 kg.\nAprēķini vada pretestību un atsperes "
                    "pagarinājumu!",
             dots=["l = 25 m ;  S = 1,0 mm²", "ρ = 1,7·10⁻⁸ Ω·m",
                   "k = 500 N/m ;  m = 4,0 kg"],
             jaaprekina=["R = ?", "Δx = ?"],
             formulas=["R = ρ·l/S", "F = mg", "Δx = F / k"],
             aprekins=["1)  R = 1,7·10⁻⁸ · 25 : 1,0·10⁻⁶ = 0,43 Ω",
                       "2)  F = 4,0 · 9,81 = 39,2 N",
                       "3)  Δx = 39,2 : 500 = 0,0785 m = 7,9 cm"],
             atbilde="R ≈ 0,43 Ω ;   Δx ≈ 7,9 cm",
             piezime="Divas dažādas formulas vienā uzdevumā — tieši tā mēdz "
                     "būt pārbaudes darbā."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Materiāla izvēli pamato ar aprēķinu, nevis ar vārdiem.",
            "Vispirms nosaka prasību, tad rēķina, tad salīdzina.",
            "Visas temata formulas ir datu bukletā — jāizvēlas pareizā.",
            "Vienmēr pārvērs cm³, mm², MPa un pārbauda mērvienības.",
        ],
        majasdarbs=[
            "Atkārto 5.1.–5.7. stundas kopsavilkumus un formulas.",
            "Izpildi vienu uzdevumu no katras stundas mājasdarba.",
            "Pārbaudi, vai katrā risinājumā ir visi pieci soļi un "
            "mērvienības.",
        ],
        pasvertejums=["Protu izvēlēties formulu",
                      "Protu apvienot vairākas sakarības",
                      "Protu pamatot izvēli ar skaitļiem",
                      "Esmu gatavs pārbaudes darbam"],
        nakama="Nākamā stunda: PD3 — Materiālu veidi un fizikālās īpašības."),
),
]


def build():
    return C.build_theme(TEMATS, KICKER, MAPE, STUNDAS)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for path, n in build():
        print("%3d slaidi  %s" % (n, path.replace("\\", "/").split("/")[-1]))
