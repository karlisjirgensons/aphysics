# -*- coding: utf-8 -*-
"""7. klase, 166. stunda: «Kā apvienot vienādojumu un nevienādību?»

Daudzas problēmas prasa abus: vienādojums atrod konkrēto vērtību, bet
nevienādība - robežu. Piemēram, krāšanas plānā vienādojums saka, kad mērķis
sasniegts, nevienādība - cik ilgi vēl nepietiek.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā apvienot vienādojumu un nevienādību?"

MERKIS = ("Risināsim problēmu, kurā vajadzīgs gan vienādojums, gan "
          "nevienādība.")

SATURS = [
    Sakums("Kad tieši, un kad vismaz?",
           fakti=["«Pēc cik nedēļām būs tieši 200 €?» - vienādojums.",
                  "«No kuras nedēļas būs vismaz 200 €?» - nevienādība.",
                  "Bieži vajag abus vienā uzdevumā."]),

    Doma("Vienādojums - punkts, nevienādība - robeža",
         "Problēmā nosaka, kurš jautājums prasa konkrētu vērtību "
         "(vienādojums) un kurš - vērtību kopu (nevienādība). Bieži "
         "vienādojuma sakne ir nevienādības robeža.",
         soli=[
             "Izlasi visus jautājumus.",
             "«Tieši», «vienāds», «kad sasniedz» - vienādojums.",
             "«Vismaz», «ne vairāk», «kad pārsniedz» - nevienādība.",
             "Izmanto vienādojuma sakni kā robežu.",
         ]),

    Paraugs("Divi tarifi",
            uzd="Sporta zāle A: 25 € mēnesī; B: 3 € par reizi. Kad maksā "
                "vienādi? Kad A izdevīgāks?",
            soli=[
                ("3n = 25 ⇒ n ≈ 8,33", "Vienādojums: vienādi."),
                ("3n > 25 ⇒ n > 8,33", "Nevienādība: A lētāks."),
                ("n ≥ 9", "Veseli apmeklējumi."),
            ],
            atbilde="Vienādi pie ~8,3 reizēm; A izdevīgāks no 9 reizēm."),

    Ievadi("Atrisini abus", [
        {"jaut": "Krājumā 60 €, +15 € nedēļā. Pēc cik nedēļām tieši 150 €?",
         "atb": ["6"], "padoms": "15n = 90."},
        {"jaut": "No kuras nedēļas būs vairāk par 150 €?",
         "atb": ["7"], "padoms": "n > 6."},
        {"jaut": "Taisnstūra garums 2x, platums x, P = 36. x = ?",
         "atb": ["6"], "padoms": "6x = 36."},
        {"jaut": "Ja P ≤ 48, lielākais vesels x?",
         "atb": ["8"], "padoms": "6x ≤ 48."},
    ]),

    Varianti("Vienādojums vai nevienādība?", [
        {"jaut": "«Cik jāpārdod, lai nopelnītu tieši 500 €?»",
         "opcijas": ["Vienādojums", "Nevienādība"],
         "pareizi": 0, "jaukt": False, "padoms": "Tieši."},
        {"jaut": "«Cik jāpārdod, lai nebūtu zaudējumu?»",
         "opcijas": ["Vienādojums", "Nevienādība"],
         "pareizi": 1, "jaukt": False, "padoms": "Peļņa ≥ 0."},
        {"jaut": "«Kad abi vilcieni būs vienā vietā?»",
         "opcijas": ["Vienādojums", "Nevienādība"],
         "pareizi": 0, "jaukt": False, "padoms": "Konkrēts brīdis."},
    ]),

    Pasaule("Limonādes stends",
            Ievadi("", [
                {"jaut": "Izejvielas 12 €, glāze pārdod par 1,5 €. Pēc cik "
                         "glāzēm peļņa = 0?",
                 "atb": ["8"], "padoms": "1,5n = 12."},
                {"jaut": "Cik glāzes jāpārdod, lai peļņa ≥ 30 €?",
                 "atb": ["28"], "padoms": "1,5n ≥ 42."},
                {"jaut": "Peļņa, pārdodot 40 glāzes (€)?",
                 "atb": ["48"], "padoms": "60 − 12."},
            ]),
            pavediens="veikals",
            konteksts="Jebkurš bizness jautā: kad atmaksāsies (vienādojums) "
                      "un cik jāpārdod mērķim (nevienādība).",
            kapec="Abi rīki - viena problēma."),

    Kopsavilkums([
        "Atšķiru jautājumus, kas prasa vienādojumu vai nevienādību.",
        "Lietoju vienādojuma sakni kā robežu.",
        "Atrisinu abus un saistu atbildes.",
        "Interpretēju rezultātu situācijā.",
    ]),

    Majas([
        "Plāno limonādes vai cepumu stendu: atmaksāšanās un mērķis.",
        "Salīdzini divus tarifus ar vienādojumu un nevienādību.",
        "Izdomā uzdevumu ar abiem jautājumiem.",
    ]),
]
