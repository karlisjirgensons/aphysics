# -*- coding: utf-8 -*-
"""7. klase, 41. stunda: «Kurš mainīgais no kura atkarīgs?»

Divi mainīgie parasti nav vienlīdzīgi: vienu izvēlas (neatkarīgais), otrs
no tā izriet (atkarīgais). Iepērkoties izvēlas daudzumu, un cena no tā
atkarīga. Grafikā neatkarīgo liek uz horizontālās ass.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, plakne)

TEMA = "Kurš mainīgais no kura atkarīgs?"

MERKIS = ("Noteiksim neatkarīgo un atkarīgo mainīgo un paskaidrosim šo "
          "jēdzienu nozīmi.")

SATURS = [
    Sakums("Tu izvēlies kilogramus - kase izrēķina cenu",
           zimejums=plakne(grafiki=[([(0, 0), (5, 10)], "")],
                           punkti=[(1, 2), (2, 4), (3, 6), (4, 8)],
                           no_x=0, lidz_x=5, no_y=0, lidz_y=10, solis=1,
                           solis_y=2, x_nos="kg", y_nos="€"),
           paraksts="Āboli 2 € par kilogramu.",
           fakti=["Daudzumu izvēlas pircējs - tas ir neatkarīgais.",
                  "Cena izriet no daudzuma - tā ir atkarīgā.",
                  "Grafikā neatkarīgais ir uz horizontālās ass."]),

    Doma("Neatkarīgais izvēlas, atkarīgais seko",
         "Neatkarīgais mainīgais ir tas, kura vērtību izvēlas brīvi. "
         "Atkarīgais mainīgais ir tas, kura vērtība ir noteikta, kad "
         "neatkarīgā vērtība ir izvēlēta.",
         soli=[
             "Jautā: ko es izvēlos vai mainu? - neatkarīgais.",
             "Ko es pēc tam uzzinu vai izrēķinu? - atkarīgais.",
             "Neatkarīgo parasti apzīmē ar x vai t.",
             "Grafikā: neatkarīgais - pa labi (x), atkarīgais - uz augšu (y).",
         ],
         pieze="Laiks gandrīz vienmēr ir neatkarīgais: tas rit pats, un "
               "citi lielumi mainās līdz ar to."),

    Paraugs("Nosaki mainīgos",
            uzd="Skrējējs skrien ar ātrumu 3 m/s. Kurš mainīgais ir "
                "neatkarīgais, kurš - atkarīgais?",
            soli=[
                ("Mainīgie: laiks t (s) un ceļš s (m)", "Uzskaita."),
                ("Laiks rit pats - t ir neatkarīgais", "To neviens neizvēlas."),
                ("Ceļš atkarīgs no laika: s = 3t", "s ir atkarīgais."),
            ],
            atbilde="t - neatkarīgais, s - atkarīgais"),

    Varianti("Kurš ir atkarīgais?", [
        {"jaut": "Benzīna daudzums (l) un summa par benzīnu (€)",
         "opcijas": ["Summa", "Benzīna daudzums"],
         "pareizi": 0, "jaukt": False,
         "padoms": "Summa izriet no litriem."},
        {"jaut": "Gaisa temperatūra un saldējuma pārdošana",
         "opcijas": ["Saldējuma pārdošana", "Temperatūra"],
         "pareizi": 0, "jaukt": False,
         "padoms": "Karstumā pērk vairāk, ne otrādi."},
        {"jaut": "Kvadrāta mala un tā laukums",
         "opcijas": ["Laukums", "Mala"],
         "pareizi": 0, "jaukt": False,
         "padoms": "S = a · a."},
        {"jaut": "Mācīšanās laiks un testa rezultāts",
         "opcijas": ["Testa rezultāts", "Mācīšanās laiks"],
         "pareizi": 0, "jaukt": False,
         "padoms": "Rezultāts seko mācīšanās laikam."},
    ], pamats=4),

    Ievadi("Aprēķini atkarīgo", [
        {"jaut": "Āboli 2 € par kg. Cik € par 3,5 kg?",
         "atb": ["7"], "padoms": "2 · 3,5."},
        {"jaut": "Skrējējs 3 m/s. Cik m pēc 40 s?",
         "atb": ["120"], "padoms": "3 · 40."},
        {"jaut": "Kvadrāta mala 7 cm. Laukums (cm²)?",
         "atb": ["49"], "padoms": "7 · 7."},
        {"jaut": "Āboli 2 € par kg, samaksāja 9 €. Cik kg?",
         "atb": ["4,5"], "padoms": "9 : 2."},
    ]),

    Pasaule("Lejupielāde",
            Ievadi("", [
                {"jaut": "Internets lejupielādē 25 MB sekundē. Cik MB pēc "
                         "12 s?",
                 "atb": ["300"], "padoms": "25 · 12."},
                {"jaut": "Spēle aizņem 4000 MB. Pēc cik sekundēm tā būs "
                         "lejupielādēta?",
                 "atb": ["160"], "padoms": "4000 : 25."},
                {"jaut": "Kurš mainīgais te ir neatkarīgais - «laiks» vai "
                         "«MB»?",
                 "atb": ["laiks"], "padoms": "Laiks rit pats.",
                 "tastatura": "text"},
            ]),
            pavediens="dati",
            konteksts="Lejupielādes josla rāda, kā atkarīgais (MB) aug līdz "
                      "ar neatkarīgo (laiku).",
            kapec="Zinot sakarību, var prognozēt beigu laiku."),

    Kopsavilkums([
        "Nosaku neatkarīgo un atkarīgo mainīgo.",
        "Zinu, ka neatkarīgo izvēlas, atkarīgais no tā izriet.",
        "Grafikā neatkarīgo lieku uz horizontālās ass.",
        "Aprēķinu atkarīgā vērtību.",
    ]),

    Majas([
        "Atrodi 3 atkarīgu lielumu pārus savā dienā.",
        "Katram pārim nosaki, kurš ir neatkarīgais.",
        "Izdomā pāri, kurā grūti pateikt, kurš no kura atkarīgs.",
    ]),
]
