# -*- coding: utf-8 -*-
"""Fizika I, 11. klase. LD1 - Siltuma māja: siltumizolācijas pētīšana."""

LD = {
    "nr": 1,
    "klase": "11. klase",
    "nosaukums": "Siltuma māja: siltumizolācijas pētīšana",
    "mape": "8. Siltums un siltuma procesi",
    "fails": "LD1. Siltuma māja - siltumizolācijas pētīšana_tt",
    "datums": "14.10.2026.",
    "svars": 9,
    "laiks": 80,
    "kopa": 25,
    "darba_forma": "3-4 cilvēku grupās",
    "jautajums": "Kurš siltumizolācijas materiāls vislabāk pasargā māju no "
                 "atdzišanas?",
    "merkis": "Salīdzināmos apstākļos izmērīt, cik ātri atdziest dažādi "
              "izolēti maketi, un ar datiem pamatot materiāla izvēli.",
    "hipoteze": "Pieraksti, kurš no pieejamajiem materiāliem, tavuprāt, "
                "izolēs vislabāk, un pamato ar materiāla uzbūvi.",
    "teorija": [
        "Siltuma daudzums:  Q = cmΔT   ·   c(ūdens) = 4200 J/(kg·°C)",
        "Atdzišanas ātrums:  v = ΔT / Δt,  [v] = °C/min",
        "Siltumvadītspēja λ:  jo mazāka, jo labāka izolācija. Poraini "
        "materiāli izolē labi, jo tajos ir nekustīgs gaiss.",
        "Godīgs salīdzinājums: vienādi trauki, vienāds ūdens daudzums, "
        "vienāda sākuma temperatūra, vienāds izolācijas biezums.",
    ],
    "piederumi": [
        "3-4 vienādi maketi (kartona kastes vai stikla burkas), termometri "
        "(0,5 °C) vai temperatūras sensori, hronometrs.",
        "Izolācijas materiāli: putuplasts, minerālvate, burbuļplēve, avīžu "
        "papīrs; līmlente, šķēres, lineāls biezuma kontrolei.",
        "Karsts ūdens (aptuveni 60 °C), mērtrauks, virtuves svari.",
    ],
    "drosiba": [
        "Karsts ūdens (60 °C) rada applaucēšanās risku - lej to skolotāja "
        "uzraudzībā, izmantojot piltuvi vai mērtrauku ar rokturi.",
        "Termometrus neizmanto par maisāmkociņu; stikla termometru nedrīkst "
        "atstāt bez atbalsta.",
        "Minerālvatei pieskaras ar cimdiem; pēc darba nomazgā rokas.",
    ],
    "gaita": [
        ("Saplāno pētījumu.", "Grupā vienojieties, kurš lielums ir "
         "neatkarīgais (izolācijas materiāls), kurš atkarīgais "
         "(temperatūra) un kuri lielumi jāsaglabā nemainīgi."),
        ("Sagatavo maketus.", "Katru maketu apliec ar vienu izolācijas "
         "materiālu vienādā biezumā (izmēri to ar lineālu!). Vienu maketu "
         "atstāj bez izolācijas - tā ir kontrole."),
        ("Ielej ūdeni.", "Katrā maketā ielej vienādu ūdens daudzumu "
         "(piemēram, 200 ml) ar vienādu sākuma temperatūru."),
        ("Nolasi sākuma temperatūru.", "Ievieto termometrus, pagaidi "
         "30 sekundes un pieraksti sākuma temperatūru t = 0 min."),
        ("Mēri temperatūru.", "Ik pēc 3 minūtēm 30 minūtes pieraksti visu "
         "maketu temperatūru. Termometrus no ūdens neizņem."),
        ("Reģistrē apstākļus.", "Pieraksti telpas temperatūru, ūdens "
         "daudzumu un izolācijas biezumu - bez tā rezultāti nav "
         "salīdzināmi."),
        ("Sakārto datus.", "Aizpildi tabulu un sagatavo datus grafikam."),
    ],
    "tabula": {
        "galva": ["t, min", "Bez izolācijas, °C", "Materiāls 1, °C",
                  "Materiāls 2, °C", "Materiāls 3, °C"],
        "rindas": 11,
        "platumi": [2.2, 4.0, 3.9, 3.9, 4.0],
    },
    "tabulas_note": "Tabulas galvenē ieraksti izmantoto materiālu "
                    "nosaukumus! Laika rindas: 0, 3, 6, ... 30 min.",
    "apstrade": [
        ("Temperatūras krituma aprēķins", "Katram maketam aprēķini kopējo "
         "temperatūras kritumu ΔT = T(sākuma) − T(30 min) un vidējo "
         "atdzišanas ātrumu v = ΔT / 30 min.", 5.0),
        ("Atdotā siltuma daudzums", "Vienam maketam pieraksti pilnu "
         "risinājumu siltuma daudzumam Q = cmΔT. Atceries: 200 ml ūdens "
         "masa ir 0,20 kg.", 5.5),
        ("Grafiks", "Uz vienām asīm uzzīmē visu maketu temperatūras "
         "atkarību no laika! Katrai līknei pievieno apzīmējumu.", 9.0),
    ],
    "jautajumi": [
        ("Kurš materiāls izolēja vislabāk? Atbildi pamato ar diviem "
         "konkrētiem skaitļiem no savas tabulas!", 2.4),
        ("Paskaidro ar daļiņu modeli, kāpēc labākais materiāls izolēja "
         "labāk!", 2.4),
        ("Kāpēc pētījumā vajadzīgs makets bez izolācijas?", 2.0),
        ("Nosauc trīs lielumus, kurus saglabājāt nemainīgus, un paskaidro, "
         "kāpēc katrs no tiem ir svarīgs!", 2.4),
        ("Nosauc divus kļūdu avotus un piedāvā, kā tos samazināt!", 2.4),
        ("Kuru materiālu ieteiktu īstas mājas siltināšanai? Papildus "
         "izolācijai nosauc vēl vienu apsvērumu!", 2.2),
    ],
    "sagatavosana": [
        "Ūdeni uzkarsē pirms stundas un tur termosā - tā visām grupām "
        "sākuma temperatūra ir vienāda.",
        "Katrai grupai sagatavo 4 vienādus maketus un vismaz 3 dažādus "
        "izolācijas materiālus; biezumu ierobežo ar iepriekš sagrieztām "
        "loksnēm.",
        "Mērījumu tabulu uzzīmē uz tāfeles; atgādina, ka jāreģistrē arī "
        "telpas temperatūra.",
        "Šis ir Siltuma mājas projekta pirmais posms - rezultātus izmantos "
        "PR1 prezentācijā 28.10.2026.",
    ],
    "gaidamie": [
        "30 minūtēs neizolēts makets atdziest par 18-25 °C, ar putuplastu - "
        "par 8-12 °C, ar minerālvati - par 7-11 °C.",
        "Visas līknes ir dilstošas un lēzenas beigās - atdzišanas ātrums "
        "samazinās, temperatūru starpībai ar apkārtni sarūkot.",
        "Ar m = 0,20 kg un ΔT = 20 °C atdotais siltums Q = 4200 · 0,20 · 20 "
        "= 1,68 · 10⁴ J ≈ 17 kJ.",
        "Ja visas līknes sakrīt, visdrīzāk atšķīrās izolācijas biezums vai "
        "maketi nebija vienādi noslēgti.",
    ],
    "atbildes": [
        "Atbilde individuāla; jāvērtē, vai nosaukti divi konkrēti skaitļi "
        "(piemēram, ΔT = 9 °C pret ΔT = 22 °C) un pareizs secinājums.",
        "Porainā materiālā ir daudz nekustīga gaisa; gaisa daļiņas ir tālu "
        "viena no otras un siltuma pārnese ar sadursmēm notiek lēni, bet "
        "poras neļauj izveidoties konvekcijas plūsmām.",
        "Kontroles makets rāda, cik ātri ūdens atdziest bez izolācijas; bez "
        "tā nav ar ko salīdzināt materiālu efektu.",
        "Piemēram: ūdens daudzums (nosaka siltuma daudzumu), sākuma "
        "temperatūra (nosaka temperatūru starpību ar apkārtni), izolācijas "
        "biezums (tieši ietekmē siltuma plūsmu).",
        "Piemēram: termometra nolasīšana ar nokavēšanos (samazina, mērot "
        "pēc hronometra signāla) un maketa vāka neblīvums (samazina, "
        "aizlīmējot spraugas visiem maketiem vienādi).",
        "Parasti minerālvate vai putuplasts. Papildus jāvērtē cena, "
        "ugunsdrošība, mitrumizturība un ietekme uz vidi.",
    ],
    "kriteriji": [
        ("Formulēta pārbaudāma hipotēze ar pamatojumu", 2),
        ("Saplānots godīgs salīdzinājums: nosaukti mainīgie un fiksētie "
         "lielumi", 3),
        ("Maketi sagatavoti ar vienādu izolācijas biezumu un kontroles "
         "maketu", 2),
        ("Temperatūra mērīta ik pēc 3 min 30 minūtes; dati tabulā ar "
         "mērvienībām", 4),
        ("Reģistrēti darba apstākļi (telpas temperatūra, ūdens daudzums, "
         "biezums)", 2),
        ("Pareizi aprēķināti temperatūras kritumi un atdzišanas ātrumi", 3),
        ("Pareizi aprēķināts siltuma daudzums Q = cmΔT ar pilnu pierakstu",
         3),
        ("Uzzīmēts grafiks ar visām līknēm, apzīmētām asīm un leģendu", 3),
        ("Secinājums pamatots ar datiem un skaidrots ar daļiņu modeli", 2),
        ("Protokols noformēts kārtīgi un iesniegts termiņā", 1),
    ],
    "piezimes": [
        "Ja skolā ir temperatūras sensori ar datu reģistrāciju, tos "
        "izmanto - tad var mērīt ik pēc 30 s un līknes ir gludākas.",
        "Grupas datus saglabā - tie ir pamatā PR1 prezentācijai un noder "
        "arī Siltuma mājas projekta noslēgumā.",
        "Ja atlicis laiks, grupas var samainīties ar datiem un pārbaudīt, "
        "vai citas grupas secinājums izriet no tās datiem.",
    ],
}
