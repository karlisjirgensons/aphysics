# -*- coding: utf-8 -*-
"""Fizika I, 10. klase. LD3 - Atsperes stinguma koeficienta noteikšana."""

LD = {
    "nr": 3,
    "klase": "10. klase",
    "nosaukums": "Atsperes stinguma koeficienta noteikšana",
    "mape": "3. Mijiedarbība un spēks",
    "fails": "LD3. Atsperes stinguma koeficienta noteikšana_tt",
    "datums": "27.01.2027.",
    "svars": 9,
    "laiks": 80,
    "kopa": 20,
    "jautajums": "Kā atsperes pagarinājums ir atkarīgs no pieliktā spēka un "
                 "cik liels ir atsperes stinguma koeficients?",
    "merkis": "Eksperimentāli pārbaudīt Huka likumu un no grafika noteikt "
              "atsperes stinguma koeficientu.",
    "hipoteze": "Pieraksti, kāda būs F(x) grafika forma un ko nozīmēs tā "
                "slīpums.",
    "teorija": [
        "Huka likums:  F = k · x,  kur x - pagarinājums   ·   "
        "[k] = N/m",
        "Atsvara svars:  F = mg,  g = 9,81 m/s²   ·   1 g = 0,001 kg",
        "No grafika F(x):  k = ΔF / Δx - taisnes slīpums.",
    ],
    "piederumi": [
        "Statīvs ar turētāju, spirālatspere, atsvaru komplekts (5 × 50 g "
        "vai 5 × 100 g), atsvaru pakaramais.",
        "Lineāls ar milimetru skalu, nostiprināts vertikāli blakus atsperei; "
        "papildu - dinamometrs pārbaudei.",
    ],
    "drosiba": [
        "Atsperi nedrīkst izstiept tālāk par ražotāja norādīto robežu - tā "
        "zaudē elastību un var atsisties.",
        "Zem atsvariem novieto mīkstu paliktni; kāju zem atsvariem "
        "neturēt.",
        "Statīvu nostiprina; atsvarus pieliek pa vienam, uzmanīgi.",
    ],
    "gaita": [
        ("Sagatavo iekārtu.", "Iekar atsperi statīvā un piestiprini "
         "pakaramo. Blakus vertikāli nostiprini lineālu."),
        ("Nolasi sākuma stāvokli.", "Bez atsvariem nolasi atsperes apakšējā "
         "gala stāvokli x₀ un ieraksti to tabulā."),
        ("Pieliec pirmo atsvaru.", "Uzliec pirmo atsvaru, pagaidi, līdz "
         "atspere nomierinās, un nolasi jauno stāvokli."),
        ("Aprēķini pagarinājumu.", "Pagarinājums x = (nolasījums) − x₀. "
         "Pierakstīt gan nolasījumu, gan pagarinājumu."),
        ("Papildini slodzi.", "Pievieno atsvarus pa vienam līdz pieciem "
         "un katrā solī nolasi stāvokli."),
        ("Pārbaudi atgriezeniskumu.", "Noņem atsvarus pa vienam un pārbaudi, "
         "vai atspere atgriežas sākuma stāvoklī. Ja neatgriežas, atzīmē to "
         "protokolā."),
    ],
    "tabula": {
        "galva": ["Nr.", "m, kg", "F = mg, N", "Nolasījums, m",
                  "x, m", "k = F/x, N/m"],
        "rindas": 5,
        "platumi": [1.4, 2.6, 3.0, 3.8, 3.0, 4.2],
    },
    "apstrade": [
        ("Spēka aprēķins", "Vienai izvēlētai rindai pieraksti pilnu "
         "risinājumu spēkam F = mg.", 4.2),
        ("Stinguma koeficients no viena mērījuma", "Tai pašai rindai "
         "aprēķini k = F / x.", 4.2),
        ("Grafiks un slīpums", "Uzzīmē grafiku F(x)! Novelc vislabāk "
         "atbilstošo taisni caur punktiem un no tās slīpuma nosaki k. "
         "Pieraksti aprēķinu k = ΔF / Δx.", 8.5),
    ],
    "jautajumi": [
        ("Kāda ir F(x) grafika forma un ko tā liecina par Huka likuma "
         "izpildīšanos?", 2.2),
        ("Salīdzini k, kas iegūts no atsevišķa mērījuma, ar k no grafika "
         "slīpuma! Kura vērtība ir ticamāka un kāpēc?", 2.4),
        ("Ko nozīmētu, ja grafika beigās punkti sāktu atkāpties no "
         "taisnes?", 2.2),
        ("Nosauc divus kļūdu avotus un piedāvā, kā tos samazināt!", 2.4),
        ("Cik liela masa vajadzīga, lai šo atsperi pagarinātu par 10 cm? "
         "Aprēķini!", 2.4),
    ],
    "sagatavosana": [
        "Katrai grupai: statīvs, atspere (k aptuveni 20-50 N/m), atsvaru "
        "komplekts, lineāls. Atsperes iepriekš pārbaudīt, lai tās nebūtu "
        "izstieptas.",
        "Uz tāfeles atgādina, ka x ir pagarinājums, nevis atsperes garums.",
        "Pārrunāt, kā uzzīmēt vislabāk atbilstošo taisni: caur punktu "
        "mākoni, nevis savienojot punktus.",
    ],
    "gaidamie": [
        "Skolas atsperēm k parasti ir 15-50 N/m; pie 500 g slodzes "
        "pagarinājums ir 0,10-0,30 m.",
        "F(x) punkti veido taisni, kas iet caur koordinātu sākumpunktu - tas "
        "apstiprina Huka likumu izmantotajā diapazonā.",
        "k no grafika slīpuma parasti atšķiras no atsevišķa mērījuma par "
        "2-8 %.",
        "Ja atspere pēc atsvaru noņemšanas neatgriežas sākuma stāvoklī, "
        "elastības robeža ir pārsniegta - tie mērījumi jāizslēdz.",
    ],
    "atbildes": [
        "Taisne caur koordinātu sākumpunktu; tas nozīmē, ka pagarinājums ir "
        "tieši proporcionāls spēkam, t. i., Huka likums izpildās.",
        "Ticamāka ir vērtība no grafika slīpuma, jo tā izmanto visus "
        "mērījumus un daļēji izlīdzina atsevišķu nolasījumu kļūdas.",
        "Ka pārsniegta elastības robeža - atspere sāk deformēties plastiski "
        "un Huka likums vairs neder.",
        "Piemēram: nolasīšana ar paralaksi (samazina, skatoties acu "
        "līmenī perpendikulāri skalai) un atsperes svārstības (samazina, "
        "gaidot, līdz tā nomierinās).",
        "No F = kx un F = mg:  m = kx/g. Ar k = 30 N/m un x = 0,10 m "
        "iznāk m = 3,0 : 9,81 ≈ 0,31 kg.",
    ],
    "kriteriji": [
        ("Formulēta hipotēze par grafika formu", 2),
        ("Pareizi nolasīts sākuma stāvoklis un visi pieci nolasījumi", 3),
        ("Pareizi aprēķināti pagarinājumi x", 2),
        ("Pareizi aprēķināti spēki F = mg ar pilnu pierakstu", 3),
        ("Uzzīmēts grafiks F(x) ar apzīmētām asīm un mērogu", 3),
        ("No grafika slīpuma noteikts k ar aprēķinu", 3),
        ("Salīdzinātas abas k vērtības un pamatots, kura ticamāka", 2),
        ("Nosaukti divi kļūdu avoti ar uzlabojumiem", 1),
        ("Protokols noformēts kārtīgi un iesniegts termiņā", 1),
    ],
    "piezimes": [
        "Grupām, kas tiek galā ātri, var iedot otru atsperi un uzdot "
        "salīdzināt abu stingumu, kā arī prognozēt virknes slēguma "
        "rezultātu.",
        "Šis darbs ir tiešs sagatavošanās solis PD4 uzdevumiem par "
        "elastības spēku.",
    ],
}
