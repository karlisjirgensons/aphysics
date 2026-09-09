# -*- coding: utf-8 -*-
"""8. temats. B daļa: 8.5.-8.8. stunda.

8.5. stunda seko LD1 mērījumiem un sagatavo PR1 prezentāciju;
8.8. stunda ir pēdējā pirms PD3.
"""

from fiz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN     # noqa: F401
from fiz_t08a import TEMATS, KICKER, KURSS, MAPE              # noqa: F401

STUNDAS = [

dict(
    nr="8.5", virsraksts="Mērījumu datu sakārtošana",
    jautajums="Kā mērījumi kļūst par pamatotu secinājumu?",
    apaksraksts="Grafiks T(t) · Modeļu salīdzināšana · PR1 struktūra",
    merkis="Izveidot temperatūras un laika grafiku, salīdzināt modeļus un "
           "sagatavot rezultātu prezentāciju.",
    protu=["izveidot grafiku no mērījumu tabulas;",
           "salīdzināt divu modeļu atdzišanas līknes;",
           "nosaukt mērījumu neprecizitātes cēloņus;",
           "sakārtot prezentāciju piecos soļos."],
    atkartojums="1. tematā jau veidojām grafikus un vērtējām mērījumu "
                "kļūdas. Tagad tas pats darbs, bet ar LD1 «Siltuma māja» "
                "datiem.",
    uzdevumu_apraksts="Datu apstrāde un secinājumi",
    teorija=[
        ("No tabulas uz grafiku", [
            ("panelis", "GRAFIKA NOTEIKUMI",
             ["Uz horizontālās ass liek laiku (neatkarīgo lielumu), uz "
              "vertikālās - temperatūru (atkarīgo lielumu).",
              "Abas asis apzīmē ar lielumu un mērvienību; mērogu izvēlas "
              "tā, lai punkti aizņemtu vismaz pusi lapas.",
              "Punktus savieno ar gludu līkni, nevis ar lauztu līniju - "
              "atdzišana notiek pakāpeniski."], NAVY),
            ("divi",
             ("LABA IZOLĀCIJA", GREEN,
              ["Līkne lēzena.",
               "Temperatūra krīt lēni.",
               "Pēc 20 min starpība maza.",
               "Atdzišanas ātrums mazs."]),
             ("VĀJA IZOLĀCIJA", RED,
              ["Līkne stāva.",
               "Temperatūra krīt strauji.",
               "Pēc 20 min starpība liela.",
               "Atdzišanas ātrums liels."])),
        ]),
        ("Neprecizitātes un prezentācija", [
            ("tabula",
             ["Neprecizitāte", "Cēlonis", "Kā samazināt"],
             [["Nevienāda sākuma T", "Ūdens lej dažādā laikā",
               "Lej vienlaikus"],
              ["Termometra novietojums", "Dažāds dziļums",
               "Fiksē dziļumu"],
              ["Telpas caurvējš", "Konvekcija ap modeli", "Aizver logu"],
              ["Reti mērījumi", "Zūd līknes forma", "Mēra ik 2 min"]],
             [3.30, 3.40, 3.53]),
            ("panelis", "PR1 PREZENTĀCIJAS STRUKTŪRA",
             ["1. Jautājums - ko pētījām un kāpēc tas ir svarīgi.",
              "2. Metode - modeļi, mērījumi, fiksētie lielumi.",
              "3. Grafiks - abas līknes vienā attēlā.",
              "4. Secinājums - atbilde uz jautājumu ar skaitli.",
              "5. Ierobežojumi - kas varēja ietekmēt rezultātu."], GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Atdzišanas ātrums no tabulas",
             teksts="Modelī temperatūra 0. minūtē bija 62 °C, bet\n"
                    "20. minūtē 47 °C. Aprēķini vidējo atdzišanas\n"
                    "ātrumu!",
             dots=["t₁ = 62 °C", "t₂ = 47 °C", "τ = 20 min"],
             jaaprekina=["v = ?"],
             formulas=["ΔT = t₁ − t₂", "v = ΔT/τ"],
             aprekins=["1)  ΔT = 62 − 47 = 15 K",
                       "2)  v = 15 : 20",
                       "3)  v = 0,75 grādi minūtē"],
             atbilde="v = 0,75 °C/min",
             piezime="Vidējais ātrums ir ērtākais viens skaitlis, ar ko "
                     "salīdzināt divus modeļus."),
        dict(nr=2, virsraksts="Divu modeļu salīdzinājums",
             teksts="Siltinātais modelis 20 min atdzisa par 15 K,\n"
                    "nesiltinātais - par 24 K. Cik procentu lēnāk\n"
                    "atdzisa siltinātais modelis?",
             dots=["ΔT₁ = 15 K", "ΔT₂ = 24 K", "τ = 20 min"],
             jaaprekina=["Uzlabojums = ?"],
             formulas=["Starpība = ΔT₂ − ΔT₁", "Daļa = (ΔT₂ − ΔT₁)/ΔT₂"],
             aprekins=["1)  Starpība = 24 − 15 = 9 K",
                       "2)  9 : 24 = 0,375",
                       "3)  Uzlabojums ≈ 38 %"],
             atbilde="Siltinātais atdziest ≈ 38 % lēnāk",
             piezime="Secinājumā vienmēr jābūt skaitlim - «bija labāk» "
                     "nav pietiekami."),
        dict(nr=3, virsraksts="Zaudētā enerģija",
             teksts="Modelī ir 0,30 kg ūdens, kas 20 min laikā atdziest\n"
                    "par 15 K. Cik enerģijas aizplūda?\n"
                    "(c = 4200 J/(kg·K))",
             dots=["m = 0,30 kg", "ΔT = 15 K", "c = 4200 J/(kg·K)"],
             jaaprekina=["Q = ?"],
             formulas=["Q = cmΔT"],
             aprekins=["1)  Q = 4200 · 0,30 · 15",
                       "2)  Q = 18 900 J",
                       "3)  Q ≈ 18,9 kJ"],
             atbilde="Q ≈ 1,9·10⁴ J",
             piezime="Šī enerģija aizgāja caur sienām, vāku un spraugām - "
                     "tieši to izolācija samazina."),
        dict(nr=4, virsraksts="Vidējā jauda",
             teksts="Iepriekšējā uzdevumā 18 900 J aizplūda 20 minūtēs.\n"
                    "Aprēķini vidējo siltuma zudumu jaudu!",
             dots=["Q = 18 900 J", "τ = 20 min = 1200 s"],
             jaaprekina=["P = ?"],
             formulas=["P = Q/t"],
             aprekins=["1)  τ = 20 · 60 = 1200 s",
                       "2)  P = 18 900 : 1200",
                       "3)  P ≈ 15,8 W"],
             atbilde="P ≈ 16 W",
             piezime="Jauda vatos ir tas pats lielums, ko rēķina īstām "
                     "mājām - tikai daudz mazākā mērogā."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Grafikā laiks ir uz horizontālās ass, temperatūra - uz "
            "vertikālās.",
            "Lēzena līkne nozīmē labu izolāciju.",
            "Secinājumā jābūt skaitlim, ne tikai vārdiem.",
            "Prezentācijā ir pieci soļi: jautājums, metode, grafiks, "
            "secinājums, ierobežojumi.",
        ],
        majasdarbs=[
            "Uzzīmē abu modeļu līknes vienā grafikā.",
            "Aprēķini abu modeļu vidējo atdzišanas ātrumu.",
            "Sagatavo PR1 runu - viena minūte katram solim.",
        ],
        pasvertejums=["Protu uzzīmēt grafiku",
                      "Protu salīdzināt līknes",
                      "Zinu neprecizitāšu cēloņus",
                      "Esmu sagatavojis PR1"],
        nakama="Nākamā stunda: PR1 prezentācijas, pēc tam pirmais "
               "termodinamikas likums."),
),

dict(
    nr="8.6", virsraksts="Pirmais termodinamikas likums",
    jautajums="Kā siltums un darbs maina iekšējo enerģiju?",
    apaksraksts="Q = ΔU + A · A = pΔV · Enerģijas nezūdamība",
    merkis="Ar vienkāršu piemēru skaidrot pirmo termodinamikas likumu un "
           "aprēķināt gāzes darbu pie nemainīga spiediena.",
    protu=["formulēt pirmo termodinamikas likumu;",
           "noteikt katra locekļa zīmi;",
           "aprēķināt gāzes darbu A = pΔV;",
           "aprēķināt iekšējās enerģijas izmaiņu."],
    atkartojums="8.1. stundā noskaidrojām, ka iekšējo enerģiju var mainīt "
                "divējādi - ar siltumu un ar darbu. Šodien to pierakstīsim "
                "kā vienādojumu.",
    uzdevumu_apraksts="Siltums, darbs un iekšējā enerģija",
    teorija=[
        ("Pirmais termodinamikas likums", [
            ("formula", "ENERĢIJAS NEZŪDAMĪBA SILTUMA PROCESOS",
             "Q = ΔU + A        A = p · ΔV",
             "Gāzei pievadītais siltums Q daļēji palielina iekšējo "
             "enerģiju ΔU, daļēji tiek tērēts darbam A, ko gāze veic, "
             "izplešoties.", GOLD),
            ("kartitas", [
                ("Q - SILTUMS", RED,
                 ["Q > 0: gāzei pievada.",
                  "Q < 0: gāze atdod.",
                  "Mēra džoulos."]),
                ("ΔU - ENERĢIJA", BLUE,
                 ["Atkarīga tikai no T.",
                  "T aug - ΔU > 0.",
                  "T krīt - ΔU < 0."]),
                ("A - DARBS", GREEN,
                 ["Izplešas: A > 0.",
                  "Saspiež: A < 0.",
                  "A = pΔV."]),
            ]),
        ]),
        ("Procesi un to īpatnības", [
            ("tabula",
             ["Process", "Kas nemainās", "Likums šajā gadījumā"],
             [["Izotermisks", "Temperatūra", "ΔU = 0, tāpēc Q = A"],
              ["Izohorisks", "Tilpums", "A = 0, tāpēc Q = ΔU"],
              ["Izobārisks", "Spiediens", "Q = ΔU + pΔV"],
              ["Adiabātisks", "Nav siltuma apmaiņas", "Q = 0, ΔU = −A"]],
             [3.00, 3.40, 3.83]),
            ("panelis", "PIEMĒRS NO SADZĪVES",
             ["Velosipēda pumpis sasilst, jo, saspiežot gaisu, tiek "
              "veikts darbs - iekšējā enerģija pieaug bez siltuma "
              "pievadīšanas.",
              "Aerosola balons atdziest, jo gāze izplešoties veic darbu "
              "un tērē savu iekšējo enerģiju.",
              "Abos gadījumos darbojas viens un tas pats likums, tikai "
              "ar pretējām zīmēm."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Gāzes darbs",
             teksts="Gāze pie nemainīga spiediena 200 kPa izplešas no\n"
                    "0,010 m³ līdz 0,025 m³. Aprēķini gāzes darbu!",
             dots=["p = 200 kPa = 200 000 Pa",
                   "V₁ = 0,010 m³", "V₂ = 0,025 m³"],
             jaaprekina=["A = ?"],
             formulas=["A = pΔV", "ΔV = V₂ − V₁"],
             aprekins=["1)  ΔV = 0,025 − 0,010 = 0,015 m³",
                       "2)  A = 200 000 · 0,015",
                       "3)  A = 3000 J"],
             atbilde="A = 3,0·10³ J",
             piezime="Darbs pozitīvs - gāze izplešas un stumj virzuli."),
        dict(nr=2, virsraksts="Iekšējās enerģijas izmaiņa",
             teksts="Gāzei pievadīti 5000 J siltuma, un tā veikusi\n"
                    "3000 J darbu. Par cik mainījās iekšējā enerģija?",
             dots=["Q = 5000 J", "A = 3000 J"],
             jaaprekina=["ΔU = ?"],
             formulas=["Q = ΔU + A", "ΔU = Q − A"],
             aprekins=["1)  ΔU = 5000 − 3000",
                       "2)  ΔU = 2000 J"],
             atbilde="ΔU = 2,0·10³ J",
             piezime="Iekšējā enerģija pieauga - tātad gāzes temperatūra "
                     "paaugstinājās."),
        dict(nr=3, virsraksts="Izohorisks process",
             teksts="Slēgtā traukā ar nemainīgu tilpumu gāzei pievada\n"
                    "1200 J siltuma. Cik liels ir darbs un par cik\n"
                    "mainās iekšējā enerģija?",
             dots=["Q = 1200 J", "V = const"],
             jaaprekina=["A = ?", "ΔU = ?"],
             formulas=["A = pΔV", "ΔV = 0", "Q = ΔU + A"],
             aprekins=["1)  ΔV = 0, tāpēc A = 0",
                       "2)  ΔU = Q − 0",
                       "3)  ΔU = 1200 J"],
             atbilde="A = 0;  ΔU = 1200 J",
             piezime="Ja gāze nevar izplesties, viss siltums paliek "
                     "iekšējā enerģijā."),
        dict(nr=4, virsraksts="Saspiešana bez siltuma",
             teksts="Pumpī gaisu saspiež, veicot 800 J darbu. Siltums\n"
                    "apkārtnei netiek atdots. Par cik mainās gāzes\n"
                    "iekšējā enerģija?",
             dots=["A = −800 J (gāzi saspiež)", "Q = 0"],
             jaaprekina=["ΔU = ?"],
             formulas=["Q = ΔU + A", "ΔU = Q − A"],
             aprekins=["1)  ΔU = 0 − (−800)",
                       "2)  ΔU = +800 J",
                       "3)  Temperatūra paaugstinās"],
             atbilde="ΔU = 800 J",
             piezime="Tieši tāpēc pumpja gals kļūst silts, kaut siltums "
                     "no ārpuses nav pievadīts."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Q = ΔU + A - pirmais termodinamikas likums.",
            "Gāzes darbs pie nemainīga spiediena A = pΔV.",
            "Izohoriskā procesā A = 0, izotermiskā ΔU = 0.",
            "Zīmes rāda virzienu: pievada vai atdod, izplešas vai "
            "saspiež.",
        ],
        majasdarbs=[
            "p = 150 kPa, ΔV = 0,020 m³. Aprēķini A.",
            "Q = 4000 J, A = 1500 J. Aprēķini ΔU.",
            "Paskaidro, kāpēc gāze izplešoties atdziest.",
        ],
        pasvertejums=["Protu formulēt likumu",
                      "Protu noteikt zīmes",
                      "Protu rēķināt A = pΔV",
                      "Protu rēķināt ΔU"],
        nakama="Nākamā stunda: siltuma dzinēji un lietderības "
               "koeficients."),
),

dict(
    nr="8.7", virsraksts="Siltuma dzinēji un energoefektivitāte",
    jautajums="Kāpēc visu siltumu nevar pārvērst lietderīgā darbā?",
    apaksraksts="η = A/Q₁ · η = (Q₁ − Q₂)/Q₁ · Enerģijas taupīšana",
    merkis="Skaidrot siltuma dzinēja darbību, aprēķināt lietderības "
           "koeficientu un pamatot enerģijas taupīšanas risinājumus.",
    protu=["nosaukt siltuma dzinēja trīs daļas;",
           "aprēķināt η = A/Q₁;",
           "aprēķināt η no siltuma daudzumiem;",
           "salīdzināt enerģijas taupīšanas risinājumus."],
    atkartojums="5. tematā lietderības koeficientu rēķinājām mehānikā. "
                "Siltuma dzinējā ir tas pats jēdziens - tikai ievadītā "
                "enerģija ir siltums.",
    uzdevumu_apraksts="Lietderības koeficienta aprēķini",
    teorija=[
        ("Siltuma dzinējs", [
            ("formula", "LIETDERĪBAS KOEFICIENTS",
             "η = A/Q₁        η = (Q₁ − Q₂)/Q₁        η · 100 %",
             "Q₁ ir no sildītāja saņemtais siltums, Q₂ - dzesētājam "
             "atdotais, A - lietderīgais darbs. Daļu siltuma atdot ir "
             "obligāti, tāpēc η vienmēr ir mazāks par 1.", GOLD),
            ("kartitas", [
                ("SILDĪTĀJS", RED,
                 ["Dod siltumu Q₁.",
                  "Degviela vai tvaiks.",
                  "Augsta temperatūra."]),
                ("DARBA VIELA", BLUE,
                 ["Gāze cilindrā.",
                  "Izplešas un veic darbu A.",
                  "Pārnes enerģiju."]),
                ("DZESĒTĀJS", GREEN,
                 ["Saņem siltumu Q₂.",
                  "Apkārtējais gaiss.",
                  "Zema temperatūra."]),
            ]),
        ]),
        ("Efektivitāte praksē", [
            ("tabula",
             ["Iekārta", "Lietderība", "Kur aiziet pārējais"],
             [["Iekšdedzes dzinējs", "25-35 %", "Izplūdes gāzes, dzesēšana"],
              ["Tvaika turbīna", "35-45 %", "Kondensators, berze"],
              ["Elektromotors", "85-95 %", "Sildīšanās vados"],
              ["LED spuldze", "40-50 %", "Siltums radiatorā"]],
             [3.60, 2.60, 4.03]),
            ("panelis", "KĀPĒC 100 % NAV IESPĒJAMS",
             ["Lai dzinējs strādātu nepārtraukti, gāzei pēc izplešanās "
              "jāatgriežas sākuma stāvoklī - un tam obligāti jāatdod "
              "siltums dzesētājam.",
              "Tāpēc daļa enerģijas vienmēr aiziet apkārtējā vidē; to "
              "nosaka otrais termodinamikas likums.",
              "Praktiskais secinājums: enerģiju lētāk ir ietaupīt (labāka "
              "izolācija, mazāks patēriņš) nekā saražot."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Lietderība no darba",
             teksts="Dzinējs no degvielas saņem 20 000 J siltuma un veic\n"
                    "6000 J lietderīga darba. Aprēķini lietderības\n"
                    "koeficientu procentos!",
             dots=["Q₁ = 20 000 J", "A = 6000 J"],
             jaaprekina=["η = ?"],
             formulas=["η = A/Q₁"],
             aprekins=["1)  η = 6000 : 20 000",
                       "2)  η = 0,30",
                       "3)  η = 30 %"],
             atbilde="η = 30 %",
             piezime="Tipiska benzīna dzinēja vērtība - divas trešdaļas "
                     "enerģijas aiziet siltumā."),
        dict(nr=2, virsraksts="Lietderība no siltumiem",
             teksts="Dzinējs saņem 50 000 J un atdod dzesētājam\n"
                    "35 000 J. Aprēķini lietderības koeficientu!",
             dots=["Q₁ = 50 000 J", "Q₂ = 35 000 J"],
             jaaprekina=["η = ?"],
             formulas=["A = Q₁ − Q₂", "η = (Q₁ − Q₂)/Q₁"],
             aprekins=["1)  A = 50 000 − 35 000 = 15 000 J",
                       "2)  η = 15 000 : 50 000",
                       "3)  η = 0,30 = 30 %"],
             atbilde="η = 30 %",
             piezime="Abas formulas dod vienu rezultātu - izvēlas to, "
                     "kurai ir dotie lielumi."),
        dict(nr=3, virsraksts="Cik daudz degvielas",
             teksts="Dzinējam ar lietderību 25 % jāveic 30 000 J darba.\n"
                    "Cik daudz siltuma tam jāsaņem?",
             dots=["η = 25 % = 0,25", "A = 30 000 J"],
             jaaprekina=["Q₁ = ?"],
             formulas=["η = A/Q₁", "Q₁ = A/η"],
             aprekins=["1)  Q₁ = 30 000 : 0,25",
                       "2)  Q₁ = 120 000 J"],
             atbilde="Q₁ = 1,2·10⁵ J",
             piezime="Četras reizes vairāk, nekā tiek izmantots - "
                     "pārējais aizsilda apkārtni."),
        dict(nr=4, virsraksts="Kas atmaksājas",
             teksts="Mājā apkurei tērē 20 000 kWh gadā. Siltināšana\n"
                    "samazina patēriņu par 35 %. Cik kilovatstundu\n"
                    "ietaupa gadā?",
             dots=["W = 20 000 kWh", "Ietaupījums 35 %"],
             jaaprekina=["ΔW = ?"],
             formulas=["ΔW = W · 0,35"],
             aprekins=["1)  ΔW = 20 000 · 0,35",
                       "2)  ΔW = 7000 kWh",
                       "3)  Paliek 13 000 kWh gadā"],
             atbilde="ΔW = 7000 kWh",
             piezime="Ietaupīta kilovatstunda ir lētāka par saražotu - "
                     "tāpēc siltina pirms katlu maiņas."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Siltuma dzinējam ir sildītājs, darba viela un dzesētājs.",
            "η = A/Q₁ un η = (Q₁ − Q₂)/Q₁.",
            "Lietderība vienmēr ir mazāka par 100 %.",
            "Enerģiju ietaupīt ir lētāk nekā saražot.",
        ],
        majasdarbs=[
            "Q₁ = 40 000 J, A = 12 000 J. Aprēķini η.",
            "Q₁ = 60 000 J, Q₂ = 45 000 J. Aprēķini η.",
            "Nosauc trīs veidus, kā mājā samazināt enerģijas patēriņu.",
        ],
        pasvertejums=["Zinu dzinēja daļas",
                      "Protu rēķināt η no darba",
                      "Protu rēķināt η no siltumiem",
                      "Protu pamatot taupīšanu"],
        nakama="Nākamā stunda: temata nostiprināšana pirms PD3."),
),

dict(
    nr="8.8", virsraksts="Siltuma procesu nostiprināšana",
    jautajums="Kā pamatot energoefektīvu izvēli?",
    apaksraksts="Q = cmΔT · Q = λm · Q = ΔU + A · η = A/Q₁ · Gatavošanās PD3",
    merkis="Risināt siltuma bilances uzdevumus, savienot temata formulas "
           "un labot biežākās kļūdas pirms PD3.",
    protu=["izvēlēties pareizo formulu katram posmam;",
           "savienot vairākus posmus vienā uzdevumā;",
           "atpazīt biežākās kļūdas;",
           "pamatot energoefektīvu izvēli ar skaitļiem."],
    atkartojums="Šī ir temata pēdējā mācību stunda. Nākamajā stundā ir "
                "PD3, kas vērtē tikai jau mācīto saturu.",
    uzdevumu_apraksts="Kombinēti uzdevumi pirms PD3",
    teorija=[
        ("Temata formulu karte", [
            ("tabula",
             ["Kad lietot", "Formula", "Ko nedrīkst aizmirst"],
             [["Mainās temperatūra", "Q = cmΔT", "ΔT kelvinos vai grādos"],
              ["Kūst vai sasalst", "Q = λm", "Temperatūra nemainās"],
              ["Iztvaiko vai kondensē", "Q = Lm", "L ir ļoti liels"],
              ["Gāze izplešas", "Q = ΔU + A", "A = pΔV"],
              ["Dzinēja efektivitāte", "η = A/Q₁", "η vienmēr < 1"]],
             [3.40, 3.00, 3.83]),
            ("panelis", "BIEŽĀKĀS KĻŪDAS PD3",
             ["Sildīšanas un kušanas posmus rēķina kopā ar vienu "
              "formulu - tie vienmēr jāsadala.",
              "Tilpumu atstāj litros vai spiedienu kilopaskālos - pirms "
              "aprēķina viss jāpārrēķina SI vienībās.",
              "Lietderību raksta lielāku par 100 % - tā vienmēr ir "
              "kļūda aprēķinā."], RED),
        ]),
        ("Kā izvēlēties risinājumu", [
            ("divi",
             ("VIENS POSMS", BLUE,
              ["Temperatūra mainās vienmērīgi.",
               "Viena formula.",
               "Piemērs: ūdens sildīšana",
               "no 20 līdz 80 grādiem."]),
             ("VAIRĀKI POSMI", GREEN,
              ["Grafikā ir lūzumi.",
               "Katram posmam sava formula.",
               "Rezultātus saskaita.",
               "Piemērs: ledus → ūdens →",
               "tvaiks."])),
            ("panelis", "PD3 NOFORMĒJUMS",
             ["Dots → Jāaprēķina → Formulas → Aprēķins → Atbilde; katrs "
              "solis dod punktus atsevišķi.",
              "Ja uzdevumā ir vairāki posmi, tos numurē: Q₁, Q₂, Q₃ un "
              "beigās saskaita.",
              "Atbildi noapaļo saprātīgi un pieraksta ar mērvienību."],
             NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Trīs posmi",
             teksts="Cik siltuma vajag, lai 0,50 kg ledus no 0 °C\n"
                    "izkausētu un ūdeni uzsildītu līdz 100 °C?\n"
                    "(λ = 3,3·10⁵ J/kg; c = 4200 J/(kg·K))",
             dots=["m = 0,50 kg", "λ = 3,3·10⁵ J/kg", "ΔT = 100 K",
                   "c = 4200 J/(kg·K)"],
             jaaprekina=["Q = ?"],
             formulas=["Q₁ = λm", "Q₂ = cmΔT", "Q = Q₁ + Q₂"],
             aprekins=["1)  Q₁ = 3,3·10⁵ · 0,50 = 165 000 J",
                       "2)  Q₂ = 4200 · 0,50 · 100 = 210 000 J",
                       "3)  Q = 375 000 J"],
             atbilde="Q = 3,75·10⁵ J",
             piezime="Divi posmi - divas formulas. Tas ir tipisks PD3 "
                     "uzdevums."),
        dict(nr=2, virsraksts="Bilance ar zudumiem",
             teksts="Tējkanna ar lietderību 80 % patērē 400 000 J\n"
                    "elektroenerģijas. Cik siltuma saņem ūdens un par cik\n"
                    "sasilst 1,0 kg ūdens? (c = 4200 J/(kg·K))",
             dots=["W = 400 000 J", "η = 0,80", "m = 1,0 kg"],
             jaaprekina=["Q = ?", "ΔT = ?"],
             formulas=["Q = ηW", "ΔT = Q/cm"],
             aprekins=["1)  Q = 0,80 · 400 000 = 320 000 J",
                       "2)  cm = 4200 · 1,0 = 4200",
                       "3)  ΔT = 320 000 : 4200 ≈ 76 K"],
             atbilde="Q = 3,2·10⁵ J;  ΔT ≈ 76 K",
             piezime="Piektā daļa enerģijas aizgāja korpusa un gaisa "
                     "sildīšanai."),
        dict(nr=3, virsraksts="Gāzes darbs un siltums",
             teksts="Gāzei pievadīti 8000 J siltuma. Tā izplešas pie\n"
                    "spiediena 100 kPa par 0,030 m³.\n"
                    "Aprēķini darbu un iekšējās enerģijas izmaiņu!",
             dots=["Q = 8000 J", "p = 100 000 Pa", "ΔV = 0,030 m³"],
             jaaprekina=["A = ?", "ΔU = ?"],
             formulas=["A = pΔV", "Q = ΔU + A", "ΔU = Q − A"],
             aprekins=["1)  A = 100 000 · 0,030 = 3000 J",
                       "2)  ΔU = 8000 − 3000",
                       "3)  ΔU = 5000 J"],
             atbilde="A = 3,0·10³ J;  ΔU = 5,0·10³ J",
             piezime="Lielākā daļa siltuma palika gāzē - tāpēc tā "
                     "sasila."),
        dict(nr=4, virsraksts="Energoefektīva izvēle",
             teksts="Mājas apkurei gadā vajag 60 GJ. Katls A: η = 75 %,\n"
                    "katls B: η = 90 %. Cik enerģijas no degvielas prasa\n"
                    "katrs un cik B ietaupa?",
             dots=["Q = 60 GJ", "η(A) = 0,75", "η(B) = 0,90"],
             jaaprekina=["Q(A) = ?", "Q(B) = ?", "Ietaupījums = ?"],
             formulas=["η = Q/Q₁", "Q₁ = Q/η"],
             aprekins=["1)  Q(A) = 60 : 0,75 = 80 GJ",
                       "2)  Q(B) = 60 : 0,90 ≈ 66,7 GJ",
                       "3)  Ietaupījums ≈ 13,3 GJ gadā"],
             atbilde="Q(A) = 80 GJ;  Q(B) ≈ 67 GJ",
             piezime="Skaitlis pamato izvēli labāk nekā apgalvojums, ka "
                     "«B ir efektīvāks»."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Katram posmam sava formula: cmΔT, λm, Lm.",
            "Vairāku posmu uzdevumā rezultātus saskaita.",
            "Pirms aprēķina visu pārrēķina SI vienībās.",
            "Lietderība pamato energoefektīvu izvēli ar skaitli.",
        ],
        majasdarbs=[
            "Atkārto 8.1.-8.7. stundas kopsavilkumus.",
            "m = 0,30 kg ledus izkausē un uzsilda līdz 50 °C. Aprēķini Q.",
            "Sagatavo formulu lapu PD3.",
        ],
        pasvertejums=["Protu izvēlēties formulu",
                      "Protu rēķināt vairākus posmus",
                      "Zinu biežākās kļūdas",
                      "Esmu gatavs PD3"],
        nakama="Nākamā stunda: PD3 - siltums un siltuma procesi."),
),

]
