# -*- coding: utf-8 -*-
"""8. klase, 42. stunda: «Kā kļūda ietekmē rezultātu?»

Ja malas mēra ar kļūdu, arī laukums ir ar kļūdu. Mazāko un lielāko
iespējamo laukumu atrod, reizinot robežas. Kvadrāts, kura mala ir nedaudz
garāka vai īsāka, parāda, ka laukuma kļūda ir lielāka par malas kļūdu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, restis)

TEMA = "Kā kļūda ietekmē rezultātu?"

MERKIS = ("Spriedīsim, kā mērījuma kļūda ietekmē aprēķina rezultātu.")

SATURS = [
    Sakums("Galds (4,0 ± 0,1) m × (3,0 ± 0,1) m",
           zimejums=restis([["", "mazākais", "nolasītais", "lielākais"],
                            ["garums", "3,9", "4,0", "4,1"],
                            ["platums", "2,9", "3,0", "3,1"],
                            ["laukums", "11,31", "12", "12,71"]]),
           paraksts="Laukums var būt no 11,31 līdz 12,71 m².",
           fakti=["Malas kļūda - apmēram 3 %.",
                  "Laukuma kļūda - apmēram 6 %.",
                  "Reizinot relatīvās kļūdas saskaitās."]),

    Doma("Rezultāta robežas",
         "Ja lielumi doti ar kļūdu, rezultāta mazāko un lielāko vērtību atrod, "
         "rēķinot ar robežām.",
         soli=[
             "Pieraksti katra lieluma mazāko un lielāko vērtību.",
             "Summa un reizinājums: mazāko rezultātu dod mazākās vērtības.",
             "Starpība un dalījums: uzmanīgi - mazākais rezultāts rodas, "
             "atņemot vai dalot ar lielāko.",
             "Rezultātu noapaļo tā, lai kļūdas cipars būtu jēgpilns.",
         ]),

    Slidnis("Kvadrāta mala (10 ± 1) cm", [
        {"v": "a = 9 cm", "teksts": "S = 81 cm²", "josla": 67},
        {"v": "a = 10 cm", "teksts": "S = 100 cm²", "josla": 83},
        {"v": "a = 11 cm", "teksts": "S = 121 cm²", "josla": 100},
    ], ievads="Mala mainās par 10 %, laukums - par apmēram 20 %."),

    Paraugs("Starpības robežas",
            uzd="a = (20 ± 1) cm, b = (8 ± 1) cm. Kādās robežās ir a − b?",
            soli=[
                ("Mazākā: 19 − 9 = 10 cm", "Mazākais a mīnus lielākais b."),
                ("Lielākā: 21 − 7 = 14 cm", "Lielākais a mīnus mazākais b."),
                ("a − b = (12 ± 2) cm", "Kļūdas saskaitās."),
            ],
            atbilde="no 10 līdz 14 cm"),

    Ievadi("Atrodi robežas", [
        {"jaut": "Taisnstūris (5 ± 1) × (3 ± 1) cm. Mazākais laukums (cm²)?",
         "atb": ["8"], "padoms": "4 · 2."},
        {"jaut": "Tam pašam - lielākais laukums?",
         "atb": ["24"], "padoms": "6 · 4."},
        {"jaut": "Perimetrs taisnstūrim (5 ± 1) × (3 ± 1). Lielākais?",
         "atb": ["20"], "padoms": "2 · (6 + 4)."},
        {"jaut": "Ceļš (100 ± 2) m, laiks (20 ± 1) s. Lielākais ātrums (m/s)? "
                 "Noapaļo līdz desmitdaļām.",
         "atb": ["5,4", "5.4"], "padoms": "102 : 19."},
    ]),

    Varianti("Kā kļūda mainās?", [
        {"jaut": "Kuba mala ar kļūdu 1 %. Tilpuma kļūda ir apmēram...",
         "opcijas": ["3 %", "1 %", "0,3 %", "9 %"],
         "pareizi": 0, "padoms": "Trīs reizinātāji."},
        {"jaut": "Divu garumu summa: kļūdas...",
         "opcijas": ["saskaitās", "atņemas", "sareizinās", "pazūd"],
         "pareizi": 0, "padoms": "(a ± 1) + (b ± 1)."},
    ]),

    Pasaule("Istabas krāsošana",
            Ievadi("", [
                {"jaut": "Siena (4,0 ± 0,1) m × (2,5 ± 0,1) m. Lielākais "
                         "laukums (m²)? Noapaļo līdz desmitdaļām.",
                 "atb": ["10,7", "10.7"], "padoms": "4,1 · 2,6 = 10,66."},
                {"jaut": "Krāsa: 1 l uz 8 m². Cik litru vajag lielākajam "
                         "laukumam 2 kārtās? (līdz desmitdaļām)",
                 "atb": ["2,7", "2.7"], "padoms": "2 · 10,66 : 8 ≈ 2,67."},
                {"jaut": "Krāsa ir kannās pa 1 l. Cik kannu jāpērk?",
                 "atb": ["3"], "padoms": "Uz augšu."},
            ]),
            pavediens="maja",
            konteksts="Plānojot remontu, rēķina ar lielāko iespējamo laukumu, "
                      "lai pietiktu materiāla.",
            kapec="Mērījuma kļūda pārvēršas par papildu kannu krāsas."),

    Kopsavilkums([
        "Atrodu rezultāta mazāko un lielāko vērtību.",
        "Zinu, ka reizinot relatīvā kļūda pieaug.",
        "Starpībai izvēlos robežas pretējos virzienos.",
    ]),

    Majas([
        "Nomēri galda malas ar kļūdu un atrodi laukuma robežas.",
        "Aprēķini relatīvo kļūdu malai un laukumam.",
        "Paskaidro, kāpēc laukuma kļūda ir lielāka.",
    ]),
]
