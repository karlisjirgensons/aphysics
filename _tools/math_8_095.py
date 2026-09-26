# -*- coding: utf-8 -*-
"""8. klase, 95. stunda: «Kā definē paralelogramu?»

Paralelograms - četrstūris, kura pretējās malas ir pa pāriem paralēlas.
Rūtiņās un koordinātu plaknē paralelitāti redz pēc vienāda «soļa»: ja AB
iet 4 pa labi un 1 uz augšu, tad arī DC. Tā atrod ceturto virsotni.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, Zimejums, geometrija, plakne)

TEMA = "Kā definē paralelogramu?"

MERKIS = "Definēsim paralelogramu un atpazīsim to starp četrstūriem."

SATURS = [
    Sakums("Kas kopīgs šiem četrstūriem?",
           zimejums=geometrija([("A", 0, 0), ("B", 5, 0), ("C", 6.5, 3),
                                ("D", 1.5, 3)],
                               nogriezni=["AB", "BC", "CD", "DA"],
                               iekrasot=[("ABCD", 0)]),
           paraksts="AB ∥ CD un AD ∥ BC.",
           fakti=["Paralelograms - četrstūris ar diviem paralēlu malu "
                  "pāriem.",
                  "Taisnstūris, rombs un kvadrāts ir paralelogrami.",
                  "Trapece nav paralelograms - tai ir tikai viens pāris."]),

    Doma("Kā pārbaudīt",
         "Jāpārbauda abi pretējo malu pāri.",
         soli=[
             "Rūtiņās paralēlām malām ir vienāds «solis»: tikpat pa labi un "
             "tikpat uz augšu.",
             "Koordinātu plaknē: no A uz B un no D uz C jāiet vienādi.",
             "Ja paralēls tikai viens pāris - tā ir trapece.",
             "Ceturto virsotni atrod, atkārtojot soli: D = A + (C − B).",
         ]),

    Zimejums("Paralelograms koordinātu plaknē",
             plakne(lauzta=[(0, 0), (4, 1), (5, 4), (1, 3), (0, 0)],
                    punkti=[(0, 0, "A"), (4, 1, "B"), (5, 4, "C"),
                            (1, 3, "D")],
                    no_x=-1, lidz_x=6, no_y=-1, lidz_y=5, aizpildi=True),
             paskaidro="No A uz B: 4 pa labi, 1 uz augšu - tāpat no D uz C."),

    Ievadi("Atrodi ceturto virsotni", [
        {"jaut": "Paralelogramam ABCD A(1; 1), B(6; 2), C(7; 5). D "
                 "x koordināte?", "atb": ["2"],
         "padoms": "No B uz C: 1 pa labi, 3 uz augšu; tāpat no A."},
        {"jaut": "D y koordināte?", "atb": ["4"], "padoms": "1 + 3."},
        {"jaut": "Cik paralēlu malu pāru ir paralelogramam?", "atb": ["2"],
         "padoms": "Definīcija."},
    ]),

    Varianti("Atpazīsti", [
        {"jaut": "Četrstūris ar vienu paralēlu malu pāri ir...",
         "opcijas": ["trapece", "paralelograms", "rombs", "kvadrāts"],
         "pareizi": 0, "padoms": "Viens pāris."},
        {"jaut": "Vai kvadrāts ir paralelograms?",
         "opcijas": ["Jā", "Nē", "Tikai liels", "Tikai pagriezts"],
         "pareizi": 0, "padoms": "Abi pretējo malu pāri paralēli."},
        {"jaut": "Rūtiņās AB iet 5 pa labi, DC arī 5 pa labi; AD iet 2 pa "
                 "labi un 3 uz augšu, BC - tāpat. Tas ir...",
         "opcijas": ["paralelograms", "trapece", "nevar noteikt",
                     "ieliekts četrstūris"],
         "pareizi": 0, "padoms": "Abi pāri ar vienādu soli."},
    ]),

    Pasaule("Lampas svira",
            Ievadi("", [
                {"jaut": "Galda lampas svira ir paralelograms ar malām 30 cm "
                         "un 10 cm. Perimetrs (cm)?",
                 "atb": ["80"], "padoms": "2 · (30 + 10)."},
                {"jaut": "Pagriežot sviru, vai pretējās malas paliek "
                         "paralēlas? (1 - jā, 0 - nē)",
                 "atb": ["1"], "padoms": "Malu garumi nemainās."},
                {"jaut": "Cik malu pāru paliek paralēli?", "atb": ["2"],
                 "padoms": "Abi."},
            ]),
            pavediens="tehnika",
            konteksts="Lampu sviras veido paralelogramu - lampa kustas, bet "
                      "paliek tajā pašā virzienā.",
            kapec="Paralelograma pretējās malas paliek paralēlas jebkurā "
                  "stāvoklī."),

    Kopsavilkums([
        "Definēju paralelogramu.",
        "Atpazīstu paralelogramu rūtiņās un koordinātu plaknē.",
        "Atrodu paralelograma ceturto virsotni.",
    ]),

    Majas([
        "Rūtiņās uzzīmē trīs dažādus paralelogramus.",
        "Atrodi paralelogramus apkārtnē: logi, flīzes, žogi.",
        "Dotas A(1; 1), B(6; 1), C(8; 4) - atrodi D.",
    ]),
]
