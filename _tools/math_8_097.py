# -*- coding: utf-8 -*-
"""8. klase, 97. stunda: «Ko dara diagonāles?»

Paralelograma diagonāles krustpunktā dalās uz pusēm: △ABO = △CDO pēc
pazīmes leņķis-mala-leņķis (AB = CD un šķērsleņķi). Krustpunkts ir
simetrijas centrs. Diagonāles parasti nav vienādas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, geometrija)

TEMA = "Ko dara diagonāles?"

MERKIS = ("Pierādīsim, ka paralelograma diagonāles krustpunktā dalās uz "
          "pusēm.")

SATURS = [
    Sakums("Kur krustojas diagonāles?",
           zimejums=geometrija([("A", 0, 0), ("B", 5, 0), ("C", 6.5, 3),
                                ("D", 1.5, 3), ("O", 3.25, 1.5, 270)],
                               nogriezni=["AB", "BC", "CD", "DA", "AC",
                                          "BD"],
                               svitras=[("AO", 1), ("OC", 1), ("BO", 2),
                                        ("OD", 2)],
                               iekrasot=[("ABO", 0), ("CDO", 0)]),
           paraksts="AO = OC un BO = OD.",
           fakti=["Diagonāles krustpunktā dalās uz pusēm.",
                  "Krustpunkts O ir simetrijas centrs.",
                  "Diagonāles parasti nav vienādas."]),

    Doma("Diagonāļu īpašība",
         "Krustpunkts O ir abu diagonāļu viduspunkts.",
         soli=[
             "△ABO un △CDO: AB = CD (pretējās malas).",
             "∠BAO = ∠DCO un ∠ABO = ∠CDO (šķērsleņķi, AB ∥ CD).",
             "Trijstūri vienādi pēc pazīmes leņķis-mala-leņķis.",
             "Tātad AO = OC un BO = OD.",
         ],
         pieze="Pagriežot paralelogramu par 180° ap O, tas pārklājas pats "
               "ar sevi."),

    Paraugs("Aprēķins",
            uzd="Paralelogramā AC = 14 cm, BD = 10 cm, AB = 8 cm. Atrodi "
                "trijstūra ABO perimetru.",
            soli=[
                ("AO = 14 : 2 = 7 cm", "Diagonāle dalās uz pusēm."),
                ("BO = 10 : 2 = 5 cm", "Tāpat."),
                ("P = 8 + 7 + 5 = 20 cm", "Trijstūra perimetrs."),
            ],
            atbilde="20 cm"),

    Ievadi("Aprēķini", [
        {"jaut": "AC = 12 cm. AO (cm)?", "atb": ["6"], "padoms": "Puse."},
        {"jaut": "BO = 5 cm. BD (cm)?", "atb": ["10"], "padoms": "Divreiz."},
        {"jaut": "AO = x + 2, OC = 7. x?", "atb": ["5"],
         "padoms": "x + 2 = 7."},
        {"jaut": "BD = 2x, OD = 9. x?", "atb": ["9"],
         "padoms": "BD = 18."},
    ]),

    Varianti("Spried", [
        {"jaut": "Krustpunkts O ir...",
         "opcijas": ["abu diagonāļu viduspunkts", "tikai AC viduspunkts",
                     "tuvāk garākajai malai", "virsotne"],
         "pareizi": 0, "padoms": "AO = OC un BO = OD."},
        {"jaut": "Vai paralelograma diagonāles vienmēr ir vienādas?",
         "opcijas": ["Nē", "Jā", "Tikai garam", "Tikai šauram"],
         "pareizi": 0, "padoms": "Zīmējumā AC ir garāka."},
        {"jaut": "Kāpēc △ABO = △CDO?",
         "opcijas": ["AB = CD un šķērsleņķi vienādi",
                     "Visi leņķi taisni", "Tie ir vienādsānu",
                     "Tie ir līdzīgi"],
         "pareizi": 0, "padoms": "Pazīme leņķis-mala-leņķis."},
    ]),

    Pasaule("Salokāmais krēsls",
            Ievadi("", [
                {"jaut": "Krēsla kājas ir 90 cm garas un krustojas tieši vidū. "
                         "Cik cm no krustpunkta līdz grīdai pa kāju?",
                 "atb": ["45"], "padoms": "90 : 2."},
                {"jaut": "Kājas 90 cm un 70 cm dalās uz pusēm. Īsākās kājas "
                         "puses garums (cm)?",
                 "atb": ["35"], "padoms": "70 : 2."},
                {"jaut": "Kāds četrstūris veidojas no kāju galiem? (ieraksti "
                         "vārdu)",
                 "atb": ["paralelograms"], "tastatura": "text",
                 "padoms": "Diagonāles dalās uz pusēm."},
            ]),
            pavediens="maja",
            konteksts="Ja divi stieņi krustojas savos viduspunktos, to gali "
                      "veido paralelogramu.",
            kapec="Tā ir paralelograma pazīme - nākamās stundas temats."),

    Kopsavilkums([
        "Pierādu, ka diagonāles krustpunktā dalās uz pusēm.",
        "Lietoju šo īpašību aprēķinos.",
        "Zinu, ka diagonāles parasti nav vienādas.",
    ]),

    Majas([
        "Uzzīmē paralelogramu, novelc diagonāles un izmēri to daļas.",
        "Pieraksti pierādījumu ar saviem vārdiem.",
        "Pārbaudi ar salokāmu krēslu vai statīvu.",
    ]),
]
