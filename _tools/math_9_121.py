# -*- coding: utf-8 -*-
"""9. klase, 121. stunda: «Vai atrisinājums der situācijai?»

Matemātiski pareiza atbilde var neatbilst dzīvei: 12,5 skolēni, negatīvs
ātrums, vairāk biļešu nekā vietu. Skolēns izvērtē atrisinājumu pēc
situācijas nosacījumiem un pamana nekorektus datus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti)

TEMA = "Vai atrisinājums der situācijai?"

MERKIS = ("Izvērtēsim atrisinājuma atbilstību reālajai situācijai.")

SATURS = [
    Sakums("Atbilde: 12,5 skolēni",
           fakti=["Sistēma atrisināta pareizi - bet skolēni ir veseli.",
                  "Tātad dati uzdevumā ir pretrunīgi vai nolasīti kļūdaini.",
                  "Matemātika pasaka, ka tāda situācija nav iespējama."]),

    Doma("Situācijas pārbaude",
         "Pēc atrisināšanas pārbaudi: vai vērtības ir iespējamas (veseli, "
         "pozitīvi, reāli lieli) un vai tās atbilst VISIEM nosacījumiem.",
         soli=[
             "Skaiti - naturāli skaitļi.",
             "Garumi, ātrumi, masas - pozitīvi.",
             "Vērtības reālās robežās (ātrums, vecums).",
             "Ja neder - pārbaudi aprēķinu, tad datus.",
         ]),

    Slidnis("Trīs aizdomīgas atbildes", [
        {"v": "Daļskaitlis", "teksts": "x = 7,5 automašīnas - neder, "
                                       "jāpārbauda dati"},
        {"v": "Negatīvs", "teksts": "Straumes ātrums −2 km/h - sajaukts "
                                    "«pa» un «pret» straumi"},
        {"v": "Nereāls", "teksts": "Vectēvam 180 gadi - kļūda vienādojumā"},
    ]),

    Varianti("Der vai neder?", [
        {"jaut": "Biļešu uzdevumā: x = 45 pilnās, y = −5 bērnu.",
         "opcijas": ["Neder - skaits nevar būt negatīvs", "Der",
                     "Der, ja noapaļo", "Der tikai x"],
         "pareizi": 0, "padoms": "y ≥ 0."},
        {"jaut": "Maisījumā: 150 g un 150 g, kopā vajadzēja 300 g.",
         "opcijas": ["Der", "Neder", "Der tikai vienam", "Nevar zināt"],
         "pareizi": 0, "padoms": "Pozitīvi, summa sakrīt."},
        {"jaut": "Laivas ātrums 3 km/h, straumes - 5 km/h. Laiva brauc pret "
                 "straumi.",
         "opcijas": ["Neder - pret straumi laiva neizkustētos",
                     "Der", "Der, ja vējš", "Nevar zināt"],
         "pareizi": 0, "padoms": "v − u < 0."},
    ]),

    Ievadi("Atrisini un izvērtē", [
        {"jaut": "Klasē 25 skolēni, meiteņu par 3 vairāk nekā zēnu. "
                 "Zēnu x = ? (ieraksti aprēķina rezultātu)", "atb": ["11"],
         "padoms": "2x + 3 = 25."},
        {"jaut": "Ja meiteņu būtu par 4 vairāk: 2x + 4 = 25, x = ?",
         "atb": ["10,5"], "padoms": "Nav vesels - tādu datu nevar būt."},
        {"jaut": "Laiva: v + u = 8, v − u = 12. Straumes ātrums u = ?",
         "atb": ["−2", "-2"], "padoms": "Negatīvs - dati sajaukti!"},
    ]),

    Pasaule("Aptaujas dati",
            Varianti("", [
                {"jaut": "Ziņu portāls: «Aptaujā 50 cilvēki; 60 % vīrieši, "
                         "sieviešu par 15 vairāk.» Vai tas ir iespējams?",
                 "opcijas": ["Nē - ja vīrieši 30, sievietes 20 (par 10 mazāk)",
                             "Jā", "Jā, ja noapaļo", "Nevar pārbaudīt"],
                 "pareizi": 0, "padoms": "x + y = 50, y − x = 15 ⇒ x = 17,5."},
            ]),
            pavediens="dati",
            konteksts="Ziņās skaitļi reizēm ir pretrunīgi; sistēma to atklāj.",
            kapec="Kritiska domāšana: pārbaudi, vai dati ir savstarpēji "
                  "saderīgi."),

    Kopsavilkums([
        "Izvērtēju, vai atrisinājums der situācijai.",
        "Pamanu pretrunīgus datus.",
        "Paskaidroju, kāpēc atbilde neder.",
    ]),

    Majas([
        "Izdomā uzdevumu, kura atbilde ir daļskaitlis, lai gan jābūt "
        "veselam. Kā to labot?",
        "Atrodi ziņās skaitļus un pārbaudi, vai tie saskan.",
        "Pārbaudi iepriekšējās stundas atbildes pēc situācijas.",
    ]),
]
