# -*- coding: utf-8 -*-
"""7. klase, 165. stunda: «Vai atrisinājums ir reāls?»

Matemātiski x ≥ 2 ir bezgalīgi daudz skaitļu, bet situācijai ir robežas:
lifta ietilpība, dienas garums, cilvēka vecums. Stunda iemāca no
atrisinājumu kopas izvēlēties jēgpilnās vērtības.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Vai atrisinājums ir reāls?"

MERKIS = ("Izvērtēsim, kuras atrisinājumu kopas vērtības ir jēgpilnas "
          "dotajā situācijā.")

SATURS = [
    Sakums("x ≥ 2 stundas - bet dienā ir tikai 24",
           zimejums=taisne(0, 26, 2, intervali=[(2, 24, True, True)]),
           paraksts="Matemātika: x ≥ 2. Situācija: 2 ≤ x ≤ 24.",
           fakti=["Nevienādība nezina par situācijas robežām.",
                  "Tās jāpievieno pašam.",
                  "Bieži iznāk divkārša nevienādība."]),

    Doma("Pievieno situācijas robežas",
         "Pēc nevienādības atrisināšanas atrisinājumu kopu sašaurina ar "
         "situācijas robežām: lielums nav negatīvs, ir vesels, nepārsniedz "
         "fizisko robežu.",
         soli=[
             "Atrisini nevienādību.",
             "Uzraksti situācijas robežas (≥ 0, vesels, ≤ maksimums).",
             "Atrodi šķēlumu.",
             "Atbildi ar jēgpilnu kopu.",
         ]),

    Paraugs("Autostāvvieta",
            uzd="Stāvvietā 1,5 € stundā, ir 10 €. Stāvvieta atvērta 8:00-20:00. "
                "Cik stundu var stāvēt?",
            soli=[
                ("1,5t ≤ 10 ⇒ t ≤ 6,67", "Nauda."),
                ("t ≤ 12", "Darba laiks."),
                ("Pilnas stundas: 0-6", "Šķēlums."),
            ],
            atbilde="Ne vairāk kā 6 pilnas stundas."),

    Varianti("Jēgpilna atbilde?", [
        {"jaut": "Aprēķināts: skolēnu skaits x ≥ −3.",
         "opcijas": ["x = 0; 1; 2; ... (nevar būt negatīvs)", "x ≥ −3",
                     "x = −3", "Nav atbildes"],
         "pareizi": 0, "padoms": "Skaits ≥ 0."},
        {"jaut": "Aprēķināts: vecums v < 150.",
         "opcijas": ["Formāli pareizi, bet reāli v < ~120", "Pareizi",
                     "v ≥ 150", "Nav jēgas"],
         "pareizi": 0, "padoms": "Reāla robeža."},
        {"jaut": "Aprēķināts: laiks t > 30 min līdz stundas beigām "
                 "(stunda 40 min, pagājušas 20).",
         "opcijas": ["Neiespējami - atlikušas tikai 20 min", "t > 30",
                     "t = 30", "t = 40"],
         "pareizi": 0, "padoms": "Robeža 20."},
    ]),

    Ievadi("Aprēķini jēgpilnu atbildi", [
        {"jaut": "Liftā ≤ 8 cilvēki, un kravai vēl 500 kg ≥ 75n. Cik "
                 "cilvēku var braukt?",
         "atb": ["6"], "padoms": "n ≤ 6,67 un n ≤ 8."},
        {"jaut": "Ūdens baseinā 2 m dziļš, līmenis ceļas 0,3 m stundā. Pēc "
                 "cik pilnām stundām būs vismaz 1,5 m?",
         "atb": ["5"], "padoms": "0,3t ≥ 1,5."},
    ]),

    Pasaule("Dronu lidojums",
            Ievadi("", [
                {"jaut": "Drons lido 25 min ar pilnu akumulatoru, jāatgriežas "
                         "ar ≥ 20 % rezervi. Cik min var lidot?",
                 "atb": ["20"], "padoms": "0,8 · 25."},
                {"jaut": "Ātrums 30 km/h. Cik km var aizlidot un atgriezties "
                         "(turp un atpakaļ kopā)?",
                 "atb": ["10"], "padoms": "30 · {1|3} h."},
                {"jaut": "Likums: ne tālāk par 500 m no pilota. Cik km var "
                         "aizlidot vienā virzienā reāli?",
                 "atb": ["0,5"], "padoms": "Likums ir stingrāks."},
            ]),
            pavediens="tehnika",
            konteksts="Drona lidojumu ierobežo gan akumulators, gan likums - "
                      "atbilde ir abu šķēlums.",
            kapec="Reālā atbilde ir stingrākā robeža."),

    Kopsavilkums([
        "Pievienoju situācijas robežas atrisinājumam.",
        "Atrodu šķēlumu ar reālajām iespējām.",
        "Izvēlos veselus vai nenegatīvus skaitļus.",
        "Atbildu ar jēgpilnu kopu.",
    ]),

    Majas([
        "Izdomā uzdevumu, kur matemātiskā atbilde nav reāla.",
        "Atrisini un sašaurini ar robežām.",
        "Atrodi likumu, kas ierobežo kādu lielumu.",
    ]),
]
