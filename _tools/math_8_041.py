# -*- coding: utf-8 -*-
"""8. klase, 41. stunda: «Kad vajag precīzo vērtību?»

Ne katrā situācijā vajag vienādu precizitāti: zāļu devai - līdz miligramam,
ceļa garumam - līdz kilometram. Stunda māca izvēlēties precizitāti pēc
situācijas un atšķirt precīzu vērtību ({1|3}, π) no tās tuvinājuma.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, restis)

TEMA = "Kad vajag precīzo vērtību?"

MERKIS = ("Izvērtēsim, kad situācijā vajadzīga precīza un kad - aptuvena "
          "vērtība.")

SATURS = [
    Sakums("Cik tālu ir Liepāja?",
           zimejums=restis([["jautājums", "atbilde"],
                            ["Cik ilgi brauksim?", "≈ 220 km"],
                            ["Cik zāļu dot bērnam?", "2,5 ml"],
                            ["Cik maksā?", "12,49 €"]]),
           paraksts="Katram jautājumam - sava precizitāte.",
           fakti=["Braucienam pietiek ar desmitiem kilometru.",
                  "Zālēm vajag precīzi - kļūda ir bīstama.",
                  "Naudai - līdz centam."]),

    Doma("Precīza un aptuvena vērtība",
         "Precīza vērtība ir tieši skaitlis, piemēram, {1|3} vai π. Tuvinājums "
         "ir tai tuvs skaitlis ar galīgu ciparu skaitu, piemēram, 0,33 vai "
         "3,14.",
         soli=[
             "Starprēķinos glabā precīzo vērtību ({1|3}, π, √2).",
             "Noapaļo tikai beigās - citādi kļūdas sakrājas.",
             "Precizitāti izvēlas pēc situācijas un mērījumu precizitātes.",
             "Eksāmenā: ja nav norādīts, dod precīzu vērtību (piem., 25π).",
         ],
         pieze="Ar kalkulatoru rēķinot, var izmantot atmiņu vai visu "
               "izteiksmi ievadīt uzreiz - tad nekas netiek noapaļots pa "
               "vidu."),

    Varianti("Kāda precizitāte vajadzīga?", [
        {"jaut": "Cik cilvēku bija koncertā (ziņām)?",
         "opcijas": ["Līdz tūkstošiem", "Līdz vienam cilvēkam",
                     "Līdz miljoniem", "Nav jāzina"],
         "pareizi": 0, "padoms": "«Ap 12 000»."},
        {"jaut": "Cik miligramu zāļu tabletē?",
         "opcijas": ["Precīzi, līdz mg", "Līdz 100 mg", "Aptuveni",
                     "Līdz gramiem"],
         "pareizi": 0, "padoms": "Dozai jābūt precīzai."},
        {"jaut": "Cik laika līdz vilciena atiešanai?",
         "opcijas": ["Līdz minūtei", "Līdz sekundei", "Līdz stundai",
                     "Līdz dienai"],
         "pareizi": 0, "padoms": "Sarakstā - minūtes."},
        {"jaut": "Kurš ir precīzs skaitlis, nevis tuvinājums?",
         "opcijas": ["{2|3}", "0,67", "0,667", "0,6667"],
         "pareizi": 0, "padoms": "Decimāldaļa ir bezgalīga."},
    ]),

    Ievadi("Starprezultāts: noapaļot vai ne?", [
        {"jaut": "Aprēķini ({1|3} · 3) precīzi.",
         "atb": ["1"], "padoms": "{3|3}."},
        {"jaut": "Tagad ar tuvinājumu: 0,33 · 3 = ?",
         "atb": ["0,99", "0.99"], "padoms": "Kļūda 0,01."},
        {"jaut": "0,33 · 300 = ? (salīdzini ar {1|3} · 300 = 100)",
         "atb": ["99"], "padoms": "Kļūda pieaug 100 reizes."},
        {"jaut": "Pica sadalīta 3 daļās, katra 0,33 no picas. Cik procentu "
                 "picas «pazuda»?",
         "atb": ["1", "1 %", "1%"], "padoms": "100 − 99."},
    ]),

    Pasaule("Būvmateriāli",
            Ievadi("", [
                {"jaut": "Grīda 4,35 m × 3,2 m. Laukums (m²) līdz "
                         "desmitdaļām?",
                 "atb": ["13,9", "13.9"], "padoms": "13,92."},
                {"jaut": "Lamināta paka sedz 2,2 m². Cik paku jāpērk "
                         "(veselas)?",
                 "atb": ["7"], "padoms": "13,92 : 2,2 ≈ 6,3 - noapaļo uz "
                                         "augšu."},
                {"jaut": "Cik m² paliek pāri?",
                 "atb": ["1,48", "1.48"], "padoms": "7 · 2,2 − 13,92."},
            ]),
            pavediens="maja",
            konteksts="Pērkot materiālus, noapaļo uz augšu - 6,3 pakas nevar "
                      "nopirkt, un 6 pakām pietrūks.",
            kapec="Situācija nosaka ne tikai precizitāti, bet arī virzienu."),

    Kopsavilkums([
        "Atšķiru precīzu vērtību no tuvinājuma.",
        "Noapaļoju tikai rezultātu, ne starprezultātus.",
        "Izvēlos precizitāti un noapaļošanas virzienu pēc situācijas.",
    ]),

    Majas([
        "Atrodi 3 situācijas, kurās noapaļo uz augšu.",
        "Aprēķini {1|7} · 700 precīzi un ar 0,14.",
        "Pieraksti, kurās situācijās tavā dienā vajag precizitāti līdz "
        "minūtei.",
    ]),
]
