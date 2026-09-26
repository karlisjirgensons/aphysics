# -*- coding: utf-8 -*-
"""2. klase, 121. stunda: «Vai vienmēr var samaksāt ar divām vienādām
monētām?»

Pētījums ar visiem gadījumiem: ar divām vienādām eiro monētām var samaksāt
tikai dubultus no monētu vērtībām - 2, 4, 10, 20, 40 c, 1 €, 2 €, 4 €.
Summa 30 c vai 3 € ar divām vienādām monētām neiznāk.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, monetas, restis)

TEMA = "Vai vienmēr var samaksāt ar divām vienādām monētām?"

MERKIS = ("Šodien pētīsim, kuras summas var samaksāt ar divām vienādām "
          "monētām, un apskatīsim visus gadījumus.")

_TABULA = restis([["monēta", "divas monētas"],
                  ["1 c", "2 c"], ["2 c", "4 c"], ["5 c", "10 c"],
                  ["10 c", "20 c"], ["20 c", "40 c"], ["50 c", "1 €"],
                  ["1 €", "2 €"], ["2 €", "4 €"]])

SATURS = [
    Sakums("Vai 30 c var samaksāt ar divām vienādām monētām?",
           zimejums=monetas(["20 c", "10 c"]),
           paraksts="20 c + 10 c - bet tās nav vienādas!",
           fakti=["Eiro monētas: 1, 2, 5, 10, 20, 50 c, 1 €, 2 €.",
                  "15 c monētas nav.",
                  "Tāpēc 30 c ar divām vienādām nesanāk."]),

    Doma("Visi gadījumi",
         "Katrai monētai atrodi divu tādu summu - vairāk iespēju nav.",
         soli=[
             "Uzraksti visas monētas pēc kārtas.",
             "Katrai: divreiz tā vērtība.",
             "Ieraksti tabulā.",
             "Tikai šīs summas var samaksāt ar divām vienādām.",
         ]),

    Ievadi("Divas vienādas monētas", [
        {"jaut": "Divas 10 c monētas - cik centu?", "zim": _TABULA,
         "atb": ["20"], "mers": "c", "padoms": "10 + 10."},
        {"jaut": "Divas 50 c monētas - cik centu?", "atb": ["100"],
         "mers": "c", "padoms": "50 + 50 = 1 €."},
        {"jaut": "Cik dažādu summu var samaksāt ar divām vienādām eiro "
                 "monētām?", "zim": _TABULA, "atb": ["8"],
         "padoms": "Tik, cik monētu veidu."},
        {"jaut": "Ar kādām divām vienādām monētām samaksāt 40 c? Raksti "
                 "vienas monētas vērtību centos.", "atb": ["20"],
         "mers": "c", "padoms": "20 + 20."},
    ]),

    Varianti("Var vai nevar?", [
        {"jaut": "10 c", "opcijas": ["var: 5 c + 5 c", "nevar"],
         "jaukt": False, "pareizi": 0, "padoms": "Ir 5 c monēta."},
        {"jaut": "30 c", "opcijas": ["var", "nevar"], "jaukt": False,
         "pareizi": 1, "padoms": "Vajadzētu 15 c monētu."},
        {"jaut": "4 €", "opcijas": ["var: 2 € + 2 €", "nevar"],
         "jaukt": False, "pareizi": 0, "padoms": "Ir 2 € monēta."},
        {"jaut": "6 c", "opcijas": ["var", "nevar"], "jaukt": False,
         "pareizi": 1, "padoms": "Vajadzētu 3 c monētu."},
    ]),

    Petijums("Pārbaudi ar monētām", [
        "Paņem pa divām katra veida monētām (vai modeļiem).",
        "Saliec katru pāri un pieraksti summu.",
        "Salīdzini ar tabulu.",
        "Izdomā summu, ko nevar samaksāt ar divām vienādām.",
    ], vajag="monētas vai to modeļi"),

    Pasaule("Maksājam kioskā",
            Varianti("", [
                {"jaut": "Tev ir tikai 20 c monētas. Kuru cenu vari samaksāt "
                         "precīzi ar divām?", "opcijas": ["40 c", "30 c",
                                                           "50 c"],
                 "pareizi": 0, "padoms": "20 + 20."},
            ]),
            pavediens="veikals",
            konteksts="Makā ir tikai vienādas monētas.",
            kapec="Zinot visus gadījumus, var ātri pateikt atbildi."),

    Kopsavilkums([
        "Zinu eiro monētu vērtības.",
        "Aprēķinu divu vienādu monētu summu.",
        "Apskatu visus gadījumus tabulā.",
    ]),

    Majas([
        "Atrodi mājās monētas un saliec pa divām vienādām.",
        "Pieraksti summas.",
        "Kuru summu ar divām vienādām nevar samaksāt: 8 c vai 10 c?",
    ]),
]
