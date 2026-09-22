# -*- coding: utf-8 -*-
"""5. klase, 13. stunda: «Kā pārstāstīt tekstu ar lieliem skaitļiem?»

Autentisks teksts ar lieliem skaitļiem - ziņa, enciklopēdijas rindkopa - un
uzdevums to pārstāstīt tā, lai to var noklausīties un atcerēties. Precizitāte
te ir nevis mērķis, bet izvēle: kuru skaitli drīkst noapaļot un kuru ne.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā pārstāstīt tekstu ar lieliem skaitļiem?"

MERKIS = ("Mācīsimies pārstāstīt tekstu ar lieliem skaitļiem, aizstājot tos "
          "ar aptuvenām vērtībām, nesabojājot jēgu.")

SATURS = [
    Sakums("Kuru skaitli tu atcerēsies rīt?",
           fakti=["«Latvijā ir 2 256 ezeri, kas lielāki par 1 ha.»",
                  "«Latvijā ir vairāk nekā divi tūkstoši ezeru.»",
                  "Viens teikums ir precīzs, otrs - atceramies."]),

    Doma("Pārstāstot skaitli aizstāj ar apaļu, bet ne ar citu",
         "Aptuvenam skaitlim jāpaliek patiesam: «vairāk nekā» drīkst tikai "
         "tad, ja tiešām ir vairāk.",
         soli=[
             "Izlasi teikumu un atrodi, kas tajā ir galvenais.",
             "Noapaļo skaitli līdz tādai šķirai, kas vēl ko pasaka.",
             "Pieliec vārdu «ap», «gandrīz» vai «vairāk nekā».",
             "Pārlasi: vai teikums joprojām ir patiess?",
         ],
         pieze="«Gandrīz» lieto, ja skaitlis ir mazāks par apaļo, «vairāk "
               "nekā» - ja lielāks. 2 973 ir gandrīz 3 000; 3 042 ir vairāk "
               "nekā 3 000."),

    Paraugs("Pārstāsti ziņu",
            uzd="«Pagājušajā gadā muzeju apmeklēja 48 317 cilvēku, no tiem "
                "9 842 bija skolēni.» Kā to pateikt vienā elpas vilcienā?",
            soli=[
                ("48 317 → ap 48 tūkstošiem",
                 "Līdz tūkstošiem: skaitlis paliek saprotams un patiess."),
                ("9 842 → gandrīz 10 tūkstoši",
                 "Skaitlis ir mazliet mazāks par apaļo, tāpēc «gandrīz»."),
                ("«Muzeju apmeklēja ap 48 tūkstošiem cilvēku, gandrīz "
                 "desmitā daļa - skolēni.»",
                 "Abi skaitļi noapaļoti, jēga palikusi."),
            ],
            atbilde="ap 48 tūkstošiem apmeklētāju, no tiem gandrīz 10 "
                    "tūkstoši skolēnu"),

    Ievadi("Kā skaitli pateiktu pārstāstā?", [
        {"jaut": "«Pilsētā dzīvo 9 843 iedzīvotāji.» Cik apmēram? "
                 "(tūkstošos)",
         "atb": ["10000"], "padoms": "Gandrīz desmit tūkstoši."},
        {"jaut": "«Ceļā izlietoti 1 212 litri degvielas.» Cik apmēram? "
                 "(simtos)",
         "atb": ["1200"], "padoms": "Tuvākais simts."},
        {"jaut": "«Grāmatā ir 384 lappuses.» Cik apmēram? (simtos)",
         "atb": ["400"], "padoms": "Vairāk nekā puse simta pāri trim "
                                   "simtiem."},
        {"jaut": "«Upes garums ir 1 020 km.» Cik apmēram? (simtos)",
         "atb": ["1000"], "padoms": "Nedaudz vairāk nekā tūkstotis."},
        {"jaut": "«Koncertu noskatījās 152 706 cilvēku.» Cik apmēram? "
                 "(tūkstošos)",
         "atb": ["153000"], "padoms": "706 ir vairāk nekā puse tūkstoša."},
        {"jaut": "«Zoodārzā mīt 3 049 dzīvnieki.» Cik apmēram? (tūkstošos)",
         "atb": ["3000"], "padoms": "Nedaudz vairāk nekā trīs tūkstoši."},
    ], pamats=4,
        ievads="Noapaļo līdz prasītajai šķirai un uzraksti tikai skaitli."),

    Varianti("Vai pārstāsts ir godīgs?", [
        {"jaut": "Tekstā: 2 973 koki. Pārstāstā: «vairāk nekā trīs tūkstoši "
                 "koku.» Vai der?",
         "opcijas": ["Nē, koku ir mazāk par 3 000",
                     "Jā, skaitlis noapaļots pareizi",
                     "Jā, jo 2 973 ir apaļš skaitlis",
                     "Nē, jo kokus nedrīkst skaitīt"],
         "pareizi": 0,
         "padoms": "Noapaļot drīkst, bet «vairāk nekā» maina teikuma nozīmi."},
        {"jaut": "Tekstā: 48 317 apmeklētāji. Kurš pārstāsts ir labākais?",
         "opcijas": ["Ap 48 tūkstošiem", "Ap 50 tūkstošiem",
                     "Ap 40 tūkstošiem", "Ap 5 tūkstošiem"],
         "pareizi": 0,
         "padoms": "Izvēlies apaļāko skaitli, kas vēl ir tuvu īstajam."},
        {"jaut": "Kāpēc pārstāstā nepasaka «48 317»?",
         "opcijas": ["Tādu skaitli neatceras",
                     "Tas ir nepareizs skaitlis",
                     "Tas ir par mazu",
                     "Lielus skaitļus nedrīkst izrunāt"],
         "pareizi": 0,
         "padoms": "Padomā, ko tu atcerēsies pēc stundas."},
        {"jaut": "Kurā tekstā skaitli noapaļot nedrīkst?",
         "opcijas": ["Bankas izrakstā", "Ziņā par koncertu",
                     "Sarunā ar draugu", "Ceļojuma stāstā"],
         "pareizi": 0,
         "padoms": "Kur par katru vienību kāds maksā?"},
    ], pamats=4),

    Pasaule("Kā izstāstīt ziņu par dabu?",
            Ievadi("", [
                {"jaut": "«Latvijā ir 2 256 ezeri.» Cik apmēram? (tūkstošos)",
                 "atb": ["2000"], "padoms": "Divi tūkstoši ar nelielu "
                                            "pārpalikumu."},
                {"jaut": "«Mežs aizņem 3 379 000 ha.» Cik apmēram? "
                         "(miljonos)",
                 "atb": ["3000000"], "padoms": "Trīs miljoni ar mazliet."},
                {"jaut": "«Latvijā ligzdo 217 putnu sugas.» Cik apmēram? "
                         "(simtos)",
                 "atb": ["200"], "padoms": "Tuvākais simts."},
                {"jaut": "«Gaujas garums ir 452 km.» Cik apmēram? (simtos)",
                 "atb": ["500"], "padoms": "52 ir vairāk nekā puse simta."},
            ]),
            pavediens="daba",
            konteksts="Ziņās par dabu skaitļi ir lieli un nekad nav zināmi "
                      "līdz pēdējai vienībai.",
            kapec="Apaļš skaitlis paliek atmiņā; precīzais paliek reģistrā."),

    Kopsavilkums([
        "Pārstāstu tekstu, aizstājot lielus skaitļus ar aptuveniem.",
        "Izvēlos šķiru, līdz kurai noapaļot, lai jēga nepazustu.",
        "Lietoju «gandrīz» un «vairāk nekā» tā, lai teikums paliek patiess.",
    ]),

    Majas([
        "Atrodi ziņu ar vismaz trim lieliem skaitļiem un pārstāsti to trijos "
        "teikumos.",
        "Pasvītro, kurš skaitlis tavā pārstāstā ir precīzs un kurš aptuvens.",
        "Palūdz kādam pārstāstīt tavu pārstāstu - vai skaitļi izdzīvoja?",
    ]),
]
