# -*- coding: utf-8 -*-
"""7. klase, 81. stunda: «Kā pierādīt divu trijstūru vienādību?»

Pierādījums pēc zīmējuma: atrod trīs vienādu elementu pārus, pārbauda,
kurai pazīmei tie atbilst, un pieraksta strukturēti. Stunda iemāca
«pierādījuma tabulu»: katrā rindā - vienādība un tās pamatojums.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, Zimejums, geometrija, restis)

TEMA = "Kā pierādīt divu trijstūru vienādību?"

MERKIS = ("Pierādīsim trijstūru vienādību pēc dota zīmējuma un veidosim "
          "strukturētu pierakstu.")

_PUKIS = geometrija([("A", 0, 0), ("B", 3, -2), ("C", 8, 0), ("D", 3, 2)],
                    nogriezni=["AB", "BC", "CD", "DA"], izcelti=["AC"],
                    svitras=[("AB", 1), ("AD", 1), ("CB", 2), ("CD", 2)])

SATURS = [
    Sakums("Pūķa (deltveida) konstrukcija",
           zimejums=_PUKIS,
           paraksts="AB = AD, CB = CD. Vai △ABC un △ADC ir vienādi?",
           fakti=["Pierādījums nav «izskatās vienādi».",
                  "Vajag trīs vienādu elementu pārus un pazīmi.",
                  "Katrai rindai - pamatojums."]),

    Doma("Trīs pāri un pazīme",
         "Lai pierādītu trijstūru vienādību, atrod trīs atbilstošu elementu "
         "pārus, kas ir vienādi, un pārbauda, vai tie atbilst kādai pazīmei - "
         "mlm, lml vai mmm.",
         soli=[
             "Uzraksti: dots, jāpierāda.",
             "Atzīmē zīmējumā vienādos elementus (svītriņas, loki).",
             "Meklē «bezmaksas» vienādības: kopīga mala, krustleņķi.",
             "Pārbaudi pazīmi un uzraksti secinājumu ar tās nosaukumu.",
         ],
         pieze="Katru vienādību pamato: (dots), (kopīga mala), "
               "(krustleņķi), (viduspunkts)."),

    Paraugs("Pierādījums tabulā",
            uzd="Četrstūrī ABCD: AB = AD un CB = CD. Pierādi, ka "
                "△ABC = △ADC.",
            soli=[
                ("AB = AD", "(dots)"),
                ("CB = CD", "(dots)"),
                ("AC = AC", "(kopīga mala)"),
                ("△ABC = △ADC", "(mmm)"),
            ],
            atbilde="Pierādīts."),

    Zimejums("Pierādījuma shēma",
             restis([["vienādība", "pamatojums"],
                     ["AB = AD", "dots"],
                     ["CB = CD", "dots"],
                     ["AC = AC", "kopīga mala"],
                     ["△ABC = △ADC", "mmm"]]),
             paskaidro="Divas kolonnas: ko apgalvo un kāpēc."),

    Varianti("Kura pazīme?", [
        {"jaut": "Dots AO = OC, BO = OD (AC un BD krustojas O). "
                 "△AOB = △COD pēc...",
         "opcijas": ["mlm (ar krustleņķiem)", "mmm", "lml", "Nevar pierādīt"],
         "pareizi": 0, "padoms": "Divas malas un krustleņķi starp tām."},
        {"jaut": "Dots ∠1 = ∠2, ∠3 = ∠4 un kopīga mala starp tiem.",
         "opcijas": ["lml", "mlm", "mmm", "Nevar pierādīt"],
         "pareizi": 0, "padoms": "Mala un pieleņķi."},
        {"jaut": "Dotas tikai divas vienādas malas un kopīga mala.",
         "opcijas": ["mmm", "mlm", "lml", "Nevar pierādīt"],
         "pareizi": 0, "padoms": "Trīs malas."},
        {"jaut": "Dots tikai AB = KL un ∠A = ∠K.",
         "opcijas": ["Nevar pierādīt - par maz", "mlm", "lml", "mmm"],
         "pareizi": 0, "padoms": "Vajag trīs pārus."},
    ], pamats=4),

    Pasaule("Simetrisks jumts",
            Varianti("", [
                {"jaut": "Jumta kopnē AC = BC (slīpās malas), CM - "
                         "vertikāls balsts, M - pamata viduspunkts. Kā "
                         "pierādīt △AMC = △BMC?",
                 "opcijas": ["mmm: AC = BC, AM = BM, CM kopīga",
                             "lml: tikai leņķi",
                             "Nevar", "Pēc laukuma"],
                 "pareizi": 0, "padoms": "Trīs malas."},
                {"jaut": "Ko no tā secina par balsta leņķi pie M?",
                 "opcijas": ["∠AMC = ∠BMC, tātad abi 90°",
                             "Tie ir 45°", "Nekas", "∠AMC = 180°"],
                 "pareizi": 0, "padoms": "Vienādi blakusleņķi."},
                {"jaut": "Kāpēc tas svarīgi būvniekam?",
                 "opcijas": ["Balsts ir vertikāls un slodze sadalās vienādi",
                             "Jumts ir skaistāks", "Dakstiņi ir lētāki",
                             "Nav svarīgi"],
                 "pareizi": 0, "padoms": "Simetrija."},
            ]),
            pavediens="maja",
            konteksts="Būvinženieris pierāda, ka simetriskais jumts nes "
                      "slodzi vienādi.",
            kapec="Pierādījums garantē, nevis cer."),

    Kopsavilkums([
        "Atrodu trīs vienādu elementu pārus.",
        "Izmantoju kopīgu malu un krustleņķus.",
        "Nosaku pazīmi un to pierakstu.",
        "Veidoju pierādījumu divās kolonnās.",
    ]),

    Majas([
        "Pierādi: taisnstūrī ABCD △ABD = △CDB.",
        "Uzzīmē krustojošus nogriežņus ar vienādām pusēm un pierādi "
        "trijstūru vienādību.",
        "Uzraksti pierādījumu tabulā.",
    ]),
]
