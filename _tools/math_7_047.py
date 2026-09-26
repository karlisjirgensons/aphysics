# -*- coding: utf-8 -*-
"""7. klase, 47. stunda: «Kurš brauc ātrāk?»

Ja divu objektu kustība attēlota vienā grafikā, ātrāk brauc tas, kura
taisne ir stāvāka: vienā un tajā pašā laikā tas nobrauc vairāk. Stunda
iemāca salīdzināt ātrumus no grafika un pamatot secinājumu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, plakne)

TEMA = "Kurš brauc ātrāk?"

MERKIS = ("Salīdzināsim divu objektu ātrumus pēc to grafikiem un pamatosim "
          "secinājumu.")

_DIVI = plakne(grafiki=[(15, 0, "A"), (10, 0, "B")],
               no_x=0, lidz_x=4, no_y=0, lidz_y=60, solis=1, solis_y=15,
               x_nos="t, h", y_nos="s, km")

SATURS = [
    Sakums("Elektriskais skrejritenis pret velosipēdu",
           zimejums=_DIVI,
           paraksts="A - skrejritenis, B - velosipēds.",
           fakti=["Pēc 2 h: A ir 30 km, B - 20 km.",
                  "Stāvākā taisne - lielākais ātrums.",
                  "Grafikā to redz bez rēķināšanas."]),

    Doma("Stāvāka taisne - lielāks ātrums",
         "Ja divu vienmērīgu kustību grafiki ir vienā plaknē, lielāks ātrums "
         "ir tam, kura taisne ir stāvāka: tajā pašā laikā ceļš ir garāks.",
         soli=[
             "Izvēlies vienu laika brīdi (piemēram, t = 1 h).",
             "Nolasi abu objektu ceļu šajā brīdī.",
             "Kuram ceļš lielāks - tam lielāks ātrums.",
             "Aprēķini ātrumus: v = s : t.",
         ],
         pieze="Salīdzina arī otrādi: vienam un tam pašam ceļam - kuram "
               "vajag mazāk laika."),

    Paraugs("Nolasi un aprēķini",
            uzd="Sākuma grafikā aprēķini abu ātrumus un par cik km tie "
                "attālināsies viens no otra 3 stundās.",
            soli=[
                ("A: 45 km 3 h - v = 15 km/h", "Nolasa punktu (3; 45)."),
                ("B: 30 km 3 h - v = 10 km/h", "Punkts (3; 30)."),
                ("45 − 30 = 15 (km)", "Starpība pēc 3 h."),
            ],
            atbilde="15 km/h un 10 km/h; 15 km"),

    Varianti("Salīdzini", [
        {"jaut": "Kura taisne atbilst lielākam ātrumam?",
         "opcijas": ["Stāvākā", "Lēzenākā", "Garākā uz papīra",
                     "Tā, kas augstāk kreisajā pusē"],
         "pareizi": 0,
         "padoms": "Vienā laikā - vairāk km."},
        {"jaut": "A grafiks iet caur (2; 50), B - caur (3; 60). Kurš ātrāks?",
         "opcijas": ["A (25 km/h)", "B (20 km/h)", "Vienādi",
                     "Nevar zināt"],
         "pareizi": 0,
         "padoms": "50 : 2 un 60 : 3."},
        {"jaut": "Divi grafiki sakrīt. Ko tas nozīmē?",
         "opcijas": ["Ātrumi vienādi un sāka kopā",
                     "Viens stāv uz vietas", "Viņi brauc pretī",
                     "Nekas"],
         "pareizi": 0,
         "padoms": "Vienā laikā - viens ceļš."},
    ]),

    Ievadi("Aprēķini ātrumus", [
        {"jaut": "Grafiks caur (4; 60). Ātrums km/h?",
         "atb": ["15"], "padoms": "60 : 4."},
        {"jaut": "A: 15 km/h, B: 10 km/h. Par cik km A ir priekšā pēc "
                 "5 h?",
         "atb": ["25"], "padoms": "(15 − 10) · 5."},
        {"jaut": "Cik h vajag B, lai nobrauktu 45 km?",
         "atb": ["4,5"], "padoms": "45 : 10."},
        {"jaut": "Cik h vajag A tiem pašiem 45 km?",
         "atb": ["3"], "padoms": "45 : 15."},
    ]),

    Pasaule("Kurš piegādās ātrāk?",
            Ievadi("", [
                {"jaut": "Kurjers ar velosipēdu: 18 km/h. Kurjers ar "
                         "auto pilsētā: 24 km/h. Cik minūšu ātrāk auto "
                         "veiks 6 km?",
                 "atb": ["5"], "padoms": "Velo 20 min, auto 15 min."},
                {"jaut": "Auto 10 min meklē stāvvietu. Kurš piegādās "
                         "ātrāk - «velo» vai «auto»?",
                 "atb": ["velo", "velosipēds", "velosipeds"],
                 "padoms": "Auto: 15 + 10 = 25 min > 20.",
                 "tastatura": "text"},
                {"jaut": "Dronam 36 km/h. Cik minūtēs tas veiks 6 km?",
                 "atb": ["10"], "padoms": "6 : 36 h = 10 min."},
            ]),
            pavediens="tehnika",
            konteksts="Piegādes lietotnes salīdzina transporta veidus pēc "
                      "ātruma un laika.",
            kapec="Ātrums nav viss - svarīgs arī kopējais laiks."),

    Zimejums("Velosipēds un drons",
             plakne(grafiki=[(18, 0, "velo"), (36, 0, "drons")],
                    no_x=0, lidz_x=2, no_y=0, lidz_y=36, solis=0.5,
                    solis_y=9, x_nos="t, h", y_nos="km"),
             paskaidro="Drona taisne ir divreiz stāvāka - divreiz ātrāk."),

    Kopsavilkums([
        "Salīdzinu ātrumus pēc taišņu slīpuma.",
        "Nolasu punktus no grafika un aprēķinu v = s : t.",
        "Aprēķinu, par cik objekti attālinās.",
        "Pamatoju secinājumu ar skaitļiem.",
    ]),

    Majas([
        "Uzzīmē grafiku savai un drauga iešanai uz skolu.",
        "Salīdzini skriešanas un iešanas ātrumu.",
        "Izdomā uzdevumu ar diviem grafikiem vienā plaknē.",
    ]),
]
