# -*- coding: utf-8 -*-
"""Fizika I, 10. klase. LD1 - Lodītes vidējais ātrums uz slīpas renītes."""

LD = {
    "nr": 1,
    "klase": "10. klase",
    "nosaukums": "Lodītes vidējais ātrums uz slīpas renītes",
    "mape": "1. Ievads pētniecībā. Vienmērīga un nevienmērīga kustība",
    "fails": "LD1. Lodītes vidējais ātrums uz slīpas renītes_tt",
    "datums": "07.10.2026.",
    "svars": 9,
    "laiks": 80,
    "kopa": 20,
    "jautajums": "Kā mainās lodītes vidējais ātrums, palielinoties renītes "
                 "slīpumam?",
    "merkis": "Plānot un veikt pētījumu, kurā izmēra lodītes vidējo ātrumu "
              "pie dažādiem renītes slīpuma leņķiem, un pamatot secinājumu "
              "ar datiem.",
    "hipoteze": "Pieraksti savu prognozi pilnā teikumā! Norādi, kā mainīsies "
                "vidējais ātrums, palielinot renītes augstumu, un kāpēc.",
    "teorija": [
        "Vidējais ātrums:  v(vid) = s / t   ·   [v] = m/s",
        "Mērījumu izkliedi samazina, katru mērījumu atkārtojot vismaz "
        "3 reizes un rēķinot vidējo aritmētisko.",
        "Neatkarīgais mainīgais - renītes augstums h; atkarīgais - laiks t; "
        "fiksētie lielumi - ceļš s, lodīte, renīte, palaišanas veids.",
    ],
    "piederumi": [
        "Renīte (aptuveni 1 m gara), metāla vai stikla lodīte, atbalsts "
        "augstuma maiņai (grāmatas vai statīvs).",
        "Mērlente vai lineāls (precizitāte 1 mm), hronometrs vai telefona "
        "sekundmērītājs (0,01 s), atdures kluči renītes galā.",
    ],
    "drosiba": [
        "Lodīte renītes galā jāaptur ar atduri - tā nedrīkst nokrist uz "
        "grīdas vai kājas.",
        "Renīti nostiprina tā, lai tā nevar noslīdēt no galda.",
        "Pēc darba lodītes savāc un noliek atpakaļ kastē.",
    ],
    "gaita": [
        ("Sagatavo renīti.", "Novieto renīti uz galda un nostiprini "
         "apakšējo galu ar atduri. Uz renītes atzīmē starta un finiša "
         "līniju; izmēri attālumu s starp tām un ieraksti tabulā."),
        ("Iestati pirmo slīpumu.", "Paceļ renītes augšējo galu par "
         "h₁ = 5 cm. Izmēri augstumu ar lineālu no galda virsmas."),
        ("Veic mērījumu.", "Palaid lodīti no starta līnijas bez grūdiena "
         "(tikai atlaid). Ar hronometru mēri laiku no palaišanas līdz "
         "finiša līnijai."),
        ("Atkārto.", "Katram augstumam mērījumu atkārto 3 reizes un ieraksti "
         "visus trīs laikus; pēc tam aprēķini vidējo laiku."),
        ("Maini slīpumu.", "Atkārto 2.-4. soli augstumiem 10 cm, 15 cm, "
         "20 cm un 25 cm. Ceļu s un lodīti nemaini!"),
        ("Sakārto datus.", "Aizpildi tabulu; katrai rindai aprēķini vidējo "
         "laiku un vidējo ātrumu."),
    ],
    "tabula": {
        "galva": ["Nr.", "h, cm", "s, m", "t₁, s", "t₂, s", "t₃, s",
                  "t(vid), s", "v(vid), m/s"],
        "rindas": 5,
        "platumi": [1.2, 2.0, 2.0, 2.2, 2.2, 2.2, 3.0, 3.2],
    },
    "apstrade": [
        ("Vidējā laika aprēķins", "Vienai izvēlētai rindai parādi, kā "
         "aprēķināts vidējais laiks:  t(vid) = (t₁ + t₂ + t₃) / 3.", 3.6),
        ("Vidējā ātruma aprēķins", "Tai pašai rindai pieraksti pilnu "
         "risinājumu vidējam ātrumam pēc formulas v(vid) = s / t(vid).", 5.0),
        ("Grafiks", "Uzzīmē grafiku v(vid) atkarībā no h! Uz asīm norādi "
         "lielumus un mērvienības, izvēlies ērtu mērogu.", 8.0),
    ],
    "jautajumi": [
        ("Kā mainās lodītes vidējais ātrums, palielinoties renītes "
         "augstumam? Atbildi pamato ar diviem konkrētiem skaitļiem no savas "
         "tabulas!", 2.4),
        ("Vai tava hipotēze apstiprinājās? Atbildi pamato!", 2.0),
        ("Nosauc divus lielumus, kurus pētījumā vajadzēja saglabāt "
         "nemainīgus, un paskaidro, kāpēc!", 2.2),
        ("Nosauc vienu kļūdu avotu šajā mērījumā un piedāvā, kā to "
         "samazināt!", 2.2),
        ("Vai izmērītais ātrums ir lodītes momentānais ātrums finišā? "
         "Atbildi pamato!", 2.0),
    ],
    "sagatavosana": [
        "Katrai grupai: renīte, lodīte, lineāls, mērlente, hronometrs, "
        "atduris un 5 vienāda biezuma paliktņi vai statīvs ar skalu.",
        "Pirms darba kopā ar klasi pārrunā, kurš lielums ir neatkarīgais, "
        "kurš atkarīgais un kuri lielumi jāsaglabā nemainīgi.",
        "Uz tāfeles atstāj mērījumu tabulas paraugu, lai visi datus "
        "reģistrē vienādi.",
    ],
    "gaidamie": [
        "Ar s ≈ 0,80 m un augstumiem 5-25 cm laiki parasti ir robežās "
        "1,5-3,0 s, bet vidējais ātrums - aptuveni 0,3-0,6 m/s.",
        "Vidējais ātrums monotoni pieaug, palielinoties augstumam; grafiks "
        "v(h) ir augoša līkne, nevis taisne (v ~ √h).",
        "Trīs atkārtojumu izkliede parasti ir 0,05-0,20 s; ja izkliede ir "
        "lielāka, mērījums jāatkārto.",
        "Biežākā kļūda - lodīte tiek pagrūsta; tad pirmais laiks izkrīt no "
        "kopējās likumsakarības.",
    ],
    "atbildes": [
        "Vidējais ātrums palielinās. Piemēram, pie h = 5 cm v ≈ 0,30 m/s, "
        "bet pie h = 25 cm v ≈ 0,60 m/s - divas reizes lielāks.",
        "Atbilde atkarīga no hipotēzes; jāvērtē pamatojums ar datiem, nevis "
        "prognozes pareizība.",
        "Ceļš s un lodīte (masa, materiāls). Ja mainītos ceļš, laiki nebūtu "
        "salīdzināmi; cita lodīte mainītu berzi un ripošanas apstākļus.",
        "Reakcijas laiks, ieslēdzot un izslēdzot hronometru (līdz 0,2 s). "
        "Samazina, izmantojot garāku ceļu, vairākus atkārtojumus vai "
        "fotoslēdzi.",
        "Nē, tas ir vidējais ātrums visā ceļā. Kustība ir paātrināta, tāpēc "
        "momentānais ātrums finišā ir lielāks par vidējo.",
    ],
    "kriteriji": [
        ("Formulēta pārbaudāma hipotēze ar pamatojumu", 2),
        ("Pareizi izmērīts un pierakstīts ceļš un visi augstumi", 2),
        ("Katram augstumam veikti 3 mērījumi, dati tabulā ar mērvienībām", 3),
        ("Pareizi aprēķināti vidējie laiki", 2),
        ("Pareizi aprēķināti vidējie ātrumi ar pilnu risinājuma pierakstu",
         3),
        ("Uzzīmēts grafiks ar apzīmētām asīm un ērtu mērogu", 3),
        ("Secinājums pamatots ar konkrētiem datiem", 2),
        ("Nosaukti fiksētie lielumi un kļūdu avots ar uzlabojumu", 2),
        ("Protokols noformēts kārtīgi un iesniegts termiņā", 1),
    ],
    "piezimes": [
        "Ja klasē nav pietiekami daudz renīšu, grupas var strādāt ar "
        "dažādiem ceļa garumiem - tad noslēgumā salīdzina grafiku formu, "
        "nevis absolūtās vērtības.",
        "Šis darbs sagatavo PR1 prezentāciju: katra grupa nākamajā stundā "
        "5 minūtēs izklāsta jautājumu, metodi, grafiku un secinājumu.",
    ],
}
