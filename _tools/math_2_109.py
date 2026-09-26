# -*- coding: utf-8 -*-
"""2. klase, 109. stunda: «Ko noderīgu var izgatavot?»

Mikrotemata noslēgums: grupa izgatavo noderīgu lietu no daudzstūriem -
grāmatzīmi, kastīti, virtenes karodziņus - un apraksta, kādas figūras un
cik daudz izmantoja.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, bildes)

TEMA = "Ko noderīgu var izgatavot?"

MERKIS = ("Šodien grupā izgatavosim noderīgu lietu no daudzstūriem un "
          "aprakstīsim izmantotās figūras.")

_VIRTENE = bildes([["trijsturis", "trijsturis*", "trijsturis",
                    "trijsturis*", "trijsturis", "trijsturis*",
                    "trijsturis", "trijsturis*"]])

SATURS = [
    Sakums("No kādām figūrām sastāv svētku karodziņu virtene?",
           zimejums=_VIRTENE,
           paraksts="Trijstūri divās krāsās pārmaiņus.",
           fakti=["Noderīgas lietas bieži ir no daudzstūriem.",
                  "Kaste - no taisnstūriem, virtene - no trijstūriem.",
                  "Plānojot jāzina, cik figūru vajag."]),

    Doma("No idejas līdz lietai",
         "Izvēlies lietu, saplāno figūras, saskaiti un izgatavo.",
         soli=[
             "Izvēlies, ko gatavosi.",
             "Uzzīmē, no kādām figūrām tā sastāv.",
             "Saskaiti, cik katras figūras vajag.",
             "Izgriez, salīmē un apraksti.",
         ]),

    Ievadi("Saplāno", [
        {"jaut": "Virtenē 8 karodziņi. Cik ir violetu?", "zim": _VIRTENE,
         "atb": ["4"], "padoms": "Pārmaiņus."},
        {"jaut": "Garākai virtenei vajag 20 karodziņu. Cik dzeltenu?",
         "atb": ["10"], "padoms": "Puse."},
        {"jaut": "Kastītei vajag 6 taisnstūru skaldnes. Cik skaldņu "
                 "vajag 3 kastītēm?", "atb": ["18"],
         "padoms": "6 + 6 + 6."},
        {"jaut": "Cik virsotņu ir 8 trijstūriem kopā?", "atb": ["24"],
         "padoms": "3 katram: 3 + 3 + ... (8 reizes)."},
    ]),

    Varianti("Kādas figūras?", [
        {"jaut": "Grāmatzīme ir garš...", "opcijas": ["taisnstūris",
                                                    "aplis", "trijstūris"],
         "pareizi": 0, "padoms": "Šaura un gara."},
        {"jaut": "Kastītes vāks ir...", "opcijas": ["taisnstūris vai "
                                                  "kvadrāts", "aplis",
                                                  "trijstūris"],
         "pareizi": 0, "padoms": "Kā kastes skaldne."},
    ]),

    Petijums("Grupas darbs", [
        "Grupā izvēlieties: virtene, grāmatzīme vai kastīte.",
        "Uzzīmējiet plānu un saskaitiet figūras.",
        "Izgrieziet un salīmējiet.",
        "Pastāstiet klasei: kādas figūras un cik daudz izmantojāt.",
    ], vajag="krāsains papīrs, šķēres, līme, aukla",
             secinajums="Plānojot figūras iepriekš, papīrs netiek "
                        "izšķērdēts."),

    Pasaule("Klases svētku dekorācijas",
            Ievadi("", [
                {"jaut": "Klasei vajag 3 virtenes pa 10 karodziņiem. Cik "
                         "karodziņu kopā?", "atb": ["30"],
                 "padoms": "10 + 10 + 10."},
                {"jaut": "No vienas lapas iznāk 6 karodziņi. Vai 5 lapas "
                         "pietiks?", "atb": ["jā", "ja"],
                 "tastatura": "text", "padoms": "6 + 6 + 6 + 6 + 6 = 30."},
            ]),
            pavediens="skola",
            konteksts="Klase gatavo dekorācijas Ziemassvētkiem.",
            kapec="Aprēķins pasaka, cik papīra nopirkt."),

    Kopsavilkums([
        "Plānoju lietu no daudzstūriem.",
        "Saskaitu, cik figūru vajag.",
        "Aprakstu izmantotās figūras.",
    ]),

    Majas([
        "Izgatavo grāmatzīmi no taisnstūra un trijstūriem.",
        "Pastāsti, kādas figūras izmantoji.",
        "Uzdāvini to kādam!",
    ]),
]
