# -*- coding: utf-8 -*-
"""Fizika I, 11. klase. LD2 - Oma likums un rezistoru slēgumi."""

LD = {
    "nr": 2,
    "klase": "11. klase",
    "nosaukums": "Oma likums un rezistoru slēgumi",
    "mape": "10. Līdzstrāva",
    "fails": "LD2. Oma likums un rezistoru slēgumi_tt",
    "datums": "16.12.2026.",
    "svars": 8,
    "laiks": 80,
    "kopa": 22,
    "jautajums": "Kā strāva ķēdē ir atkarīga no sprieguma un kā mainās "
                 "kopējā pretestība virknes un paralēlajā slēgumā?",
    "merkis": "Eksperimentāli pārbaudīt Oma likumu, no I(U) grafika noteikt "
              "rezistora pretestību un salīdzināt izmērīto ekvivalento "
              "pretestību ar aprēķināto.",
    "hipoteze": "Pieraksti, kāda būs I(U) grafika forma un kā mainīsies "
                "kopējā pretestība, divus rezistorus saslēdzot vispirms "
                "virknē, tad paralēli.",
    "teorija": [
        "Oma likums:  I = U / R   ⟹   R = U / I   ·   [R] = Ω",
        "Virknē:  I = const;  R = R₁ + R₂   ·   Paralēli:  U = const;  "
        "R = R₁R₂ / (R₁ + R₂)",
        "No I(U) grafika:  R = ΔU / ΔI - apgriezts taisnes slīpumam.",
        "Ampērmetru slēdz virknē, voltmetru - paralēli pētāmajam "
        "elementam.",
    ],
    "piederumi": [
        "Zemsprieguma barošanas bloks (0-12 V DC) vai baterijas ar "
        "turētāju, slēdzis, savienojošie vadi.",
        "Divi rezistori ar zināmām vērtībām (piemēram, 47 Ω un 100 Ω), "
        "reostats vai sprieguma dalītājs.",
        "Ampērmetrs (līdz 0,5 A) un voltmetrs (līdz 12 V) vai divi "
        "multimetri.",
    ],
    "drosiba": [
        "Strādā tikai ar zemspriegumu (līdz 12 V) - 230 V tīklam "
        "eksperimentā nepieskaras.",
        "Ķēdi slēdz pie IZSLĒGTA barošanas bloka; ieslēdz tikai pēc tam, "
        "kad skolotājs pārbaudījis shēmu.",
        "Ampērmetru nekad neslēdz paralēli avotam - tas ir īsslēgums. "
        "Sāc ar lielāko mēraparāta diapazonu.",
        "Ja rezistors vai vadi sasilst, nekavējoties izslēdz barošanu.",
    ],
    "gaita": [
        ("Uzzīmē shēmu.", "Pirms slēgšanas protokolā uzzīmē ķēdes shēmu ar "
         "avotu, slēdzi, rezistoru, ampērmetru un voltmetru."),
        ("Saslēdz ķēdi.", "Saslēdz ķēdi ar vienu rezistoru R₁. Ampērmetru "
         "slēdz virknē, voltmetru - paralēli rezistoram. Parādi shēmu "
         "skolotājam."),
        ("Mēri I(U).", "Pakāpeniski palielinot spriegumu (piemēram, 2, 4, "
         "6, 8, 10 V), katrā solī nolasi U un I; ieraksti tabulā."),
        ("Aprēķini R.", "Katrai rindai aprēķini R = U / I un pārliecinies, "
         "vai vērtības ir tuvas."),
        ("Virknes slēgums.", "Saslēdz R₁ un R₂ virknē. Pie viena izvēlēta "
         "sprieguma izmēri kopējo strāvu un spriegumu; aprēķini izmērīto "
         "ekvivalento pretestību."),
        ("Paralēlais slēgums.", "Saslēdz R₁ un R₂ paralēli. Pie tā paša "
         "sprieguma izmēri kopējo strāvu; aprēķini ekvivalento "
         "pretestību."),
        ("Salīdzini.", "Abiem slēgumiem aprēķini teorētisko ekvivalento "
         "pretestību un salīdzini to ar izmērīto."),
    ],
    "tabula": {
        "galva": ["Nr.", "U, V", "I, A", "R = U/I, Ω"],
        "rindas": 5,
        "platumi": [2.0, 5.0, 5.0, 6.0],
    },
    "tabulas_note": "Pirmā tabula - viens rezistors R₁. Slēgumu rezultātus "
                    "pieraksti 5. sadaļā.",
    "apstrade": [
        ("Pretestība no viena mērījuma", "Vienai izvēlētai rindai pieraksti "
         "pilnu risinājumu:  R = U / I.", 4.0),
        ("Grafiks I(U)", "Uzzīmē grafiku I(U)! Novelc vislabāk atbilstošo "
         "taisni un no tās nosaki pretestību R = ΔU / ΔI.", 8.5),
        ("Virknes un paralēlais slēgums", "Pieraksti abu slēgumu mērījumus "
         "(U, I) un aprēķini izmērīto un teorētisko ekvivalento pretestību. "
         "Salīdzini tās procentos.", 7.0),
    ],
    "jautajumi": [
        ("Kāda ir I(U) grafika forma un ko tā liecina par Oma likuma "
         "izpildīšanos?", 2.2),
        ("Salīdzini izmērīto un teorētisko ekvivalento pretestību abiem "
         "slēgumiem! Cik liela ir novirze procentos?", 2.4),
        ("Kāpēc paralēlajā slēgumā kopējā pretestība ir mazāka par mazāko "
         "rezistoru? Paskaidro!", 2.2),
        ("Kāpēc mājās ierīces slēdz paralēli, nevis virknē?", 2.2),
        ("Nosauc divus kļūdu avotus un piedāvā, kā tos samazināt!", 2.4),
    ],
    "sagatavosana": [
        "Katrai grupai: barošanas bloks, slēdzis, 2 rezistori, ampērmetrs, "
        "voltmetrs, 8-10 vadi. Rezistorus izvēlēties tā, lai strāva "
        "nepārsniegtu 0,25 A.",
        "Pirms darba atkārtot mēraparātu slēgšanu un diapazona izvēli; "
        "pārbaudīt katras grupas shēmu PIRMS barošanas ieslēgšanas.",
        "Uz tāfeles uzzīmēt visu trīs shēmu paraugus (viens rezistors, "
        "virkne, paralēli).",
    ],
    "gaidamie": [
        "Ar R₁ = 47 Ω pie 2-10 V strāva ir 0,04-0,21 A; R vērtības tabulā "
        "sakrīt 2-5 % robežās.",
        "I(U) grafiks ir taisne caur koordinātu sākumpunktu - Oma likums "
        "izpildās.",
        "Virknē: R ≈ 147 Ω; paralēli: R ≈ 32 Ω. Izmērītās vērtības parasti "
        "atšķiras par 3-8 % vadu un mēraparātu pretestības dēļ.",
        "Ja izmērītā virknes pretestība ir manāmi lielāka, pieskaitījusies "
        "ampērmetra un vadu pretestība.",
    ],
    "atbildes": [
        "Taisne caur koordinātu sākumpunktu; strāva ir tieši proporcionāla "
        "spriegumam, tātad Oma likums izpildās un R ir konstants.",
        "Atbilde individuāla; novirze parasti 3-8 %. Jāvērtē pareizs "
        "relatīvās novirzes aprēķins.",
        "Paralēlais slēgums dod strāvai vairākus ceļus - kopējais "
        "šķērsgriezums palielinās, tāpēc pretestība samazinās, tāpat kā "
        "biezākam vadam.",
        "Katra ierīce saņem pilnu tīkla spriegumu un darbojas neatkarīgi; "
        "virknē vienas ierīces atslēgšana pārtrauktu visu ķēdi un "
        "spriegums sadalītos.",
        "Piemēram: mēraparātu pašu pretestība (samazina, izmantojot "
        "digitālos multimetrus) un rezistora sasilšana (samazina, mērot "
        "ātri un neieslēdzot ķēdi ilgstoši).",
    ],
    "kriteriji": [
        ("Formulēta hipotēze par grafiku un slēgumiem", 2),
        ("Uzzīmēta pareiza ķēdes shēma ar mēraparātiem", 3),
        ("Ķēde saslēgta droši un pareizi (skolotāja pārbaude)", 2),
        ("Veikti 5 mērījumi ar vienu rezistoru, dati tabulā", 3),
        ("Pareizi aprēķinātas R vērtības ar pilnu pierakstu", 2),
        ("Uzzīmēts grafiks I(U) ar apzīmētām asīm un noteikts R no "
         "slīpuma", 3),
        ("Izmērīta un aprēķināta ekvivalentā pretestība abiem slēgumiem",
         4),
        ("Salīdzinātas izmērītās un teorētiskās vērtības ar novirzi "
         "procentos", 2),
        ("Protokols noformēts kārtīgi un iesniegts termiņā", 1),
    ],
    "piezimes": [
        "Ja grupu skaits ir liels, mērījumus var organizēt divās stacijās: "
        "vienā I(U) mērījums, otrā slēgumu salīdzinājums.",
        "Ātrākajām grupām - uzdevums prognozēt un pēc tam izmērīt "
        "jaukta slēguma (R₁ paralēli R₂, virknē ar R₃) pretestību.",
    ],
}
