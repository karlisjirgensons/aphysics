# -*- coding: utf-8 -*-
"""7. klase, 28. stunda: «Vai figūru var sadalīt vienādās daļās?»

Sadalīt figūru vienādās daļās ir mīkla ar ģeometrijas noteikumiem: katrai
daļai jābūt vienādai ar citām, un kopā tām jāaizpilda viss. Pirmais solis
vienmēr ir laukums: katras daļas laukums ir viss laukums, dalīts ar daļu
skaitu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, figura)

TEMA = "Vai figūru var sadalīt vienādās daļās?"

MERKIS = ("Spriedīsim, vai figūru var sadalīt noteiktā skaitā vienādu "
          "daļu, un pamatosim atbildi.")

_L = figura([(0, 0), (4, 0), (4, 2), (2, 2), (2, 4), (0, 4)],
            platums=5, augstums=5)

SATURS = [
    Sakums("Sadali L formu 4 vienādās daļās",
           zimejums=_L,
           paraksts="Laukums ir 12 rūtiņas - katrai daļai 3.",
           fakti=["Sena mīkla, ko joprojām uzdod olimpiādēs.",
                  "Atbilde: 4 mazas L formas pa 3 rūtiņām.",
                  "Laukums pasaka, cik lielai jābūt katrai daļai."]),

    Doma("Vispirms laukums, tad forma",
         "Ja figūru sadala n vienādās daļās, katras daļas laukums ir {1|n} "
         "no visas figūras laukuma. Ja laukums nedalās, sadalīt rūtiņās nav "
         "iespējams.",
         soli=[
             "Saskaiti figūras laukumu (rūtiņas).",
             "Izdali ar daļu skaitu - katras daļas laukums.",
             "Meklē formu, kas atkārtojas: sāc no stūra.",
             "Pārbaudi, vai visas daļas ir vienādas (sakrīt uzliekot).",
         ],
         pieze="Ja laukums nedalās ar n, rūtiņu figūru nevar sadalīt n "
               "vienādās rūtiņu daļās - tas ir pamatojums «nevar»."),

    Paraugs("Vai var sadalīt?",
            uzd="Figūrai ir 14 rūtiņas. Vai to var sadalīt 3 vienādās "
                "daļās pa rūtiņu līnijām?",
            soli=[
                ("14 : 3 = 4 (atl. 2)", "Laukums nedalās."),
                ("Katrai daļai būtu jābūt {14|3} rūtiņas",
                 "Tas nav vesels skaitlis."),
                ("Pa rūtiņu līnijām - nevar", "Pamatojums."),
            ],
            atbilde="Nevar, jo 14 nedalās ar 3."),

    Zimejums("L forma no 4 mazām L formām",
             figura([(0, 0), (2, 0), (2, 1), (1, 1), (1, 2), (0, 2)],
                    platums=3, augstums=3),
             paskaidro="Viena daļa - 3 rūtiņas. Četras tādas, pagrieztas, "
                       "aizpilda lielo L."),

    Ievadi("Laukuma pārbaude", [
        {"jaut": "Taisnstūris 4 × 6 rūtiņas jāsadala 8 vienādās daļās. "
                 "Cik rūtiņu katrai?",
         "atb": ["3"], "padoms": "24 : 8."},
        {"jaut": "Kvadrāts 5 × 5 - cik vienādās daļās pa 5 rūtiņām?",
         "atb": ["5"], "padoms": "25 : 5."},
        {"jaut": "Figūra no 18 rūtiņām - lielākais daļu skaits, ja katrā "
                 "jābūt vismaz 4 rūtiņām un daļas vienādas?",
         "atb": ["3"], "padoms": "18 dalītāji: 6 rūtiņas - 3 daļas."},
        {"jaut": "Kvadrātu sadala ar abām diagonālēm. Cik vienādu "
                 "trijstūru?",
         "atb": ["4"], "padoms": "Diagonāles krustojas centrā."},
    ]),

    Varianti("Spried", [
        {"jaut": "Vai jebkuru trijstūri var sadalīt 2 vienādos trijstūros?",
         "opcijas": ["Nē - tikai dažus (piemēram, vienādsānu)",
                     "Jā - ar jebkuru nogriezni",
                     "Jā - ar mediānu vienmēr",
                     "Nē - nevienu"],
         "pareizi": 0,
         "padoms": "Mediāna dala laukumu uz pusēm, bet trijstūri var nebūt "
                   "vienādi."},
        {"jaut": "Vai taisnstūri var sadalīt 2 vienādos trijstūros?",
         "opcijas": ["Jā - ar diagonāli", "Nē", "Tikai kvadrātu",
                     "Tikai 3 daļās"],
         "pareizi": 0,
         "padoms": "Diagonāle."},
        {"jaut": "Kāpēc 3 × 3 kvadrātu nevar sadalīt 2 vienādās daļās pa "
                 "rūtiņu līnijām?",
         "opcijas": ["9 nedalās ar 2", "Kvadrātu nevar dalīt",
                     "Tas ir par mazu", "Var"],
         "pareizi": 0,
         "padoms": "Laukuma pārbaude."},
    ]),

    Pasaule("Dārza dobes brāļiem",
            Ievadi("", [
                {"jaut": "Dārzs ir taisnstūris 6 m × 4 m. Trīs brāļi grib "
                         "vienādas dobes. Cik m² katram?",
                 "atb": ["8"], "padoms": "24 : 3."},
                {"jaut": "Dobes ir taisnstūri ar garumu 4 m. Cik m plata "
                         "katra dobe?",
                 "atb": ["2"], "padoms": "8 : 4."},
                {"jaut": "Ja brāļu būtu 5, cik m² būtu katram?",
                 "atb": ["4,8"], "padoms": "24 : 5."},
            ]),
            pavediens="maja",
            konteksts="Zemes gabalus dala tā, lai katram būtu vienāda "
                      "platība un forma.",
            kapec="Laukums ir pirmā pārbaude; forma - otrā."),

    Kopsavilkums([
        "Vispirms aprēķinu katras daļas laukumu.",
        "Pamatoju «nevar» ar laukuma nedalāmību.",
        "Meklēju atkārtojamu formu no stūra.",
        "Pārbaudu, vai daļas sakrīt, tās uzliekot.",
    ]),

    Majas([
        "Sadali taisnstūri 3 × 4 četrās vienādās daļās trīs dažādos veidos.",
        "Uzzīmē figūru no 10 rūtiņām, ko var sadalīt 2 vienādās daļās.",
        "Pamato, kāpēc 7 rūtiņu figūru nevar sadalīt 2 vienādās daļās.",
    ]),
]
