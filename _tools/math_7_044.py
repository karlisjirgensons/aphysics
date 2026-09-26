# -*- coding: utf-8 -*-
"""7. klase, 44. stunda: «Kā izskatās tarifa tabula un grafiks?»

Tieši proporcionāliem lielumiem attiecība ir nemainīga: divreiz vairāk
kilovatstundu - divreiz lielāks rēķins. Tabulā to redz pēc dalījuma,
grafikā - pēc taisnes caur koordinātu sākumpunktu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, plakne, restis)

TEMA = "Kā izskatās tarifa tabula un grafiks?"

MERKIS = ("Apkoposim lielumu vērtības tabulā, attēlosim tās grafiski un "
          "salīdzināsim abus veidus.")

_KWH = plakne(grafiki=[(0.2, 0, "y = 0,2x")],
              punkti=[(10, 2), (20, 4), (30, 6), (40, 8)],
              no_x=0, lidz_x=50, no_y=0, lidz_y=10, solis=10, solis_y=2,
              x_nos="kWh", y_nos="€")

SATURS = [
    Sakums("Elektrības rēķins: 0,20 € par kWh",
           zimejums=_KWH,
           paraksts="Punkti atrodas uz taisnes, kas iet caur 0.",
           fakti=["Mājsaimniecība mēnesī patērē ap 150-250 kWh.",
                  "Rēķins = cena · patēriņš.",
                  "Grafikā uzreiz redz, cik maksās jebkurš patēriņš."]),

    Doma("Tieši proporcionāli lielumi",
         "Lielumi x un y ir tieši proporcionāli, ja y = kx, kur k ir "
         "nemainīgs skaitlis. Tabulā dalījums y : x vienmēr ir k, grafiks "
         "ir taisne caur koordinātu sākumpunktu.",
         soli=[
             "Tabulā izdali y ar x katrā kolonnā.",
             "Ja visur tas pats k - lielumi ir tieši proporcionāli.",
             "Atzīmē punktus (x; y) koordinātu plaknē.",
             "Tie atrodas uz taisnes caur (0; 0).",
         ],
         pieze="Tabula dod precīzas vērtības; grafiks - pārskatu un iespēju "
               "nolasīt starpvērtības."),

    Zimejums("Tarifa tabula",
             restis([["kWh", "10", "20", "30", "40"],
                     ["€", "2", "4", "6", "8"],
                     ["€ : kWh", "0,2", "0,2", "0,2", "0,2"]]),
             paskaidro="Dalījums visur 0,2 - tas ir k."),

    Paraugs("Pārbaudi proporcionalitāti",
            uzd="Tabula: x = 2; 5; 8, y = 7; 17,5; 28. Vai y ir tieši "
                "proporcionāls x? Uzraksti formulu.",
            soli=[
                ("7 : 2 = 3,5", "Pirmā kolonna."),
                ("17,5 : 5 = 3,5; 28 : 8 = 3,5", "Pārējās."),
                ("k = 3,5 visur", "Tieši proporcionāli."),
                ("y = 3,5x", "Formula."),
            ],
            atbilde="Jā, y = 3,5x"),

    Varianti("Tieši proporcionāli?", [
        {"jaut": "x = 1; 2; 3, y = 4; 8; 12",
         "opcijas": ["Jā, k = 4", "Nē", "Jā, k = 1", "Nevar zināt"],
         "pareizi": 0,
         "padoms": "4 : 1 = 8 : 2 = 12 : 3."},
        {"jaut": "x = 1; 2; 3, y = 3; 5; 7",
         "opcijas": ["Nē", "Jā, k = 3", "Jā, k = 2", "Jā, k = 5"],
         "pareizi": 0,
         "padoms": "3 : 1 ≠ 5 : 2."},
        {"jaut": "Taksometrs: 2 € + 0,8 € par km. Summa ir tieši "
                 "proporcionāla km?",
         "opcijas": ["Nē - grafiks neiet caur 0",
                     "Jā - jo cena aug", "Jā, k = 0,8", "Jā, k = 2"],
         "pareizi": 0,
         "padoms": "0 km maksā 2 €, nevis 0."},
        {"jaut": "Kuras priekšrocības ir grafikam salīdzinot ar tabulu?",
         "opcijas": ["Redz visas starpvērtības un tendenci",
                     "Ir precīzāks", "Aizņem mazāk vietas vienmēr",
                     "Nav priekšrocību"],
         "pareizi": 0,
         "padoms": "Tabula - precizitāte, grafiks - pārskats."},
    ], pamats=4),

    Ievadi("Nolasi un aprēķini", [
        {"jaut": "0,20 € par kWh. Cik € par 25 kWh?",
         "atb": ["5"], "padoms": "0,2 · 25."},
        {"jaut": "Cik kWh var patērēt par 9 €?",
         "atb": ["45"], "padoms": "9 : 0,2."},
        {"jaut": "y = 3,5x. Cik ir y, ja x = 12?",
         "atb": ["42"], "padoms": "3,5 · 12."},
        {"jaut": "y tieši proporcionāls x; x = 4, y = 10. Cik ir k?",
         "atb": ["2,5"], "padoms": "10 : 4."},
    ]),

    Pasaule("Mēneša elektrības rēķins",
            Ievadi("", [
                {"jaut": "Ģimene patērēja 180 kWh pa 0,20 €. Cik € ir "
                         "rēķins?",
                 "atb": ["36"], "padoms": "0,2 · 180."},
                {"jaut": "Veļasmašīna vienā reizē patērē 0,9 kWh. Cik € "
                         "maksā 20 mazgāšanas reizes?",
                 "atb": ["3,6"], "padoms": "18 kWh · 0,2."},
                {"jaut": "Ja cena pieaug līdz 0,25 €, par cik € pieaugs "
                         "180 kWh rēķins?",
                 "atb": ["9"], "padoms": "180 · 0,05."},
            ]),
            pavediens="maja",
            konteksts="Elektrības rēķins ir tieši proporcionāls patēriņam - "
                      "ja nav fiksētas maksas.",
            kapec="Ar formulu var aprēķināt ietaupījumu."),

    Kopsavilkums([
        "Atpazīstu tieši proporcionālus lielumus pēc dalījuma.",
        "Pierakstu formulu y = kx.",
        "Attēloju tabulu grafikā.",
        "Zinu tabulas un grafika priekšrocības.",
    ]),

    Majas([
        "Atrodi mājās elektrības rēķinu un aprēķini cenu par kWh.",
        "Izveido tabulu un grafiku sava tarifa izmaksām.",
        "Izdomā tarifu, kas nav tieši proporcionāls.",
    ]),
]
