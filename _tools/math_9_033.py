# -*- coding: utf-8 -*-
"""9. klase, 33. stunda: «Kā līdzība palīdz trapecē?»

Trapecē līdzība parādās divās vietās: diagonāles veido «tauriņu»
(△AOB ∼ △COD ar k = {a|b}), bet pagarinātās sānu malas - trijstūri, no
kura trapece ir nogriezta. Šādu pierādījumu prasīja 2025. gada eksāmena
2. daļa.
"""

from math_saturs import (TRAPECES_MALAS, Doma, Ievadi, Kopsavilkums, Majas,
                         Paraugs, Pasaule, Sakums, Slidnis, Varianti,
                         geometrija, trapece)

TEMA = "Kā līdzība palīdz trapecē?"

MERKIS = ("Lietosim trijstūru līdzību, lai aprēķinātu trapeces nezināmos "
          "lielumus.")

# Pamati 9 un 3, augstums 4; diagonāļu krustpunkts O dala augstumu 3 : 1.
_T = trapece(9, 3, 4, nobide=3)
_TAURINS = geometrija(_T + [("O", 4.5, 3, -90)],
                      nogriezni=TRAPECES_MALAS + ["AC", "BD"],
                      iekrasot=[("AOB", 0), ("COD", 1)])
# Sānu malu turpinājumi krustojas punktā P augstumā 6.
_VIRSOTNE = geometrija(_T + [("P", 4.5, 6)],
                       nogriezni=TRAPECES_MALAS + ["DP", "CP"],
                       iekrasot=[("DCP", 1)])

SATURS = [
    Sakums("Kur trapecē slēpjas līdzīgi trijstūri?",
           zimejums=_TAURINS,
           paraksts="Pamati 9 un 3: △AOB ir 3 reizes lielāks par △COD.",
           fakti=["Diagonāles veido «tauriņu»: △AOB ∼ △COD.",
                  "k = {AB|CD} = {9|3} = 3.",
                  "Tātad AO = 3 · OC un BO = 3 · OD."]),

    Slidnis("Divi līdzības zīmējumi", [
        {"v": "Tauriņš", "teksts": "∠AOB = ∠COD (krustleņķi), ∠OAB = ∠OCD "
                                   "(šķērsleņķi pie AB ∥ DC)",
         "zim": _TAURINS},
        {"v": "Virsotne", "teksts": "Sānu malas pagarina līdz P: △DPC ∼ △APB "
                                    "(∠P kopīgs, DC ∥ AB)",
         "zim": _VIRSOTNE},
    ]),

    Doma("Līdzība trapecē",
         "△AOB ∼ △COD un △DPC ∼ △APB; abos gadījumos k = {a|b} - pamatu "
         "attiecība.",
         soli=[
             "Diagonāļu nogriežņi: {AO|OC} = {BO|OD} = {a|b}.",
             "Augstumi trijstūros arī ir attiecībā a : b.",
             "Pagarinātās sānu malas: {PD|PA} = {b|a}.",
         ]),

    Paraugs("Diagonāles daļas",
            uzd="Trapecē AB = 12, DC = 4, diagonāle AC = 10. Atrodi AO un OC.",
            soli=[
                ("△AOB ∼ △COD, k = {12|4} = 3", "Tauriņš."),
                ("AO = 3 · OC; AO + OC = 10", "Daļas."),
                ("4 · OC = 10 ⇒ OC = 2,5; AO = 7,5", "Aprēķins."),
            ],
            atbilde="AO = 7,5; OC = 2,5"),

    Ievadi("Aprēķini", [
        {"jaut": "AB = 10, DC = 5, BO = 6. OD = ?", "atb": ["3"],
         "padoms": "k = 2."},
        {"jaut": "AB = 8, DC = 6, AC = 14. AO = ?", "atb": ["8"],
         "padoms": "AO : OC = 4 : 3."},
        {"jaut": "Trapeces augstums 8, pamati 12 un 4. △COD augstums?",
         "atb": ["2"], "padoms": "8 sadalās 3 : 1."},
        {"jaut": "Pamati 9 un 3, augstums 4. Augstums no P līdz DC?",
         "atb": ["2"], "padoms": "{x|x + 4} = {3|9}."},
    ]),

    Varianti("Pamato", [
        {"jaut": "∠OAB = ∠OCD, jo...",
         "opcijas": ["iekšējie šķērsleņķi pie AB ∥ DC, krustotāja AC",
                     "krustleņķi", "trapece vienādsānu", "kāpšļu leņķi"],
         "pareizi": 0, "padoms": "AC krusto abus pamatus."},
        {"jaut": "Tauriņa trijstūri trapecē ir līdzīgi...",
         "opcijas": ["jebkurā trapecē", "tikai vienādsānu",
                     "tikai taisnleņķa", "tikai ja a = 2b"],
         "pareizi": 0, "padoms": "Vajag tikai paralēlos pamatus."},
    ]),

    Pasaule("Lampas abažūrs",
            Ievadi("", [
                {"jaut": "Abažūra sāns - trapece: apakšā 30 cm, augšā 12 cm, "
                         "augstums 18 cm. Pagarinot sānus, iegūst trijstūri. "
                         "Tā augstums virs augšējās malas (cm)?",
                 "atb": ["12"], "padoms": "{x|x + 18} = {12|30}."},
                {"jaut": "Visa trijstūra augstums (cm)?", "atb": ["30"],
                 "padoms": "12 + 18."},
            ]),
            pavediens="maja",
            konteksts="Abažūra piegrieztni iegūst, nogriežot virsotni lielam "
                      "trijstūrim.",
            kapec="Līdzība dod trūkstošo virsotnes augstumu."),

    Kopsavilkums([
        "Saskatu tauriņu ar diagonālēm trapecē.",
        "Pagarinu sānu malas un saskatu līdzīgus trijstūrus.",
        "Aprēķinu nogriežņus ar k = a : b.",
    ]),

    Majas([
        "Trapecē AB = 15, DC = 10, BD = 20. Atrodi BO un OD.",
        "Pierādi, ka △AOB ∼ △COD (pieraksti iemeslus).",
        "Pagarini sānu malas uzzīmētā trapecē un pārbaudi attiecību.",
    ]),
]
