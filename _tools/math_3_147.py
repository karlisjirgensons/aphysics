# -*- coding: utf-8 -*-
"""3. klase, 147. stunda: «Kur ir kļūda?»

Sveša risinājuma lasīšana - tas pats, kas 43. stundā, bet tagad ar
saskaitīšanu un atņemšanu 1000 apjomā. Trīs tipiskākās kļūdas ir aizmirsts
pārnesums, aizmirsts aizņēmums un sašķiebts pieraksts.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kur ir kļūda?"

MERKIS = ("Atradīsim kļūdu dotā risinājumā un izskaidrosim tās cēloni.")

SATURS = [
    Sakums("Trīs kļūdas, trīs cēloņi",
           zimejums=restis([["kļūda", "cēlonis"],
                            ["268 + 154 = 312", "aizmirsts pārnesums"],
                            ["425 − 183 = 362", "aizmirsts aizņēmums"],
                            ["342 + 21 = 552", "sašķiebts pieraksts"]],
                           "biežākās kļūdas"),
           paraksts="Katru kļūdu var atrast ar pārbaudi.",
           fakti=["Biežākā kļūda ir aizmirsts pārnesums vai aizņēmums.",
                  "Otra biežākā - cipari nav savās kolonnās."]),

    Doma("Atrodi kolonnu, kurā rezultāts nesakrīt",
         "Pārbaudi katru kolonnu atsevišķi - kļūda gandrīz vienmēr ir tieši "
         "vienā no tām.",
         soli=[
             "Izrēķini uzdevumu pats.",
             "Salīdzini atbildes pa ciparam.",
             "Atrodi pirmo kolonnu, kurā cipari atšķiras.",
             "Pasaki, kāpēc tur radās kļūda.",
         ],
         pieze="Ja atšķiras tikai desmitu cipars, kļūda gandrīz droši ir "
               "pārnesums vai aizņēmums - ne pati saskaitīšana."),

    Paraugs("Kur kļūdījās šis skolēns?",
            uzd="Skolēns uzrakstīja 268 + 154 = 312. Kur ir kļūda?",
            soli=[
                ("Vieni: 8 + 4 = 12, raksta 2 - pareizi",
                 "Pirmā kolonna ir kārtībā."),
                ("Desmiti: 6 + 5 = 11, bet pārnesums aizmirsts",
                 "Jābūt 6 + 5 + 1 = 12."),
                ("Pareizā atbilde ir 422",
                 "Kļūdas cēlonis - aizmirsts pārnesums."),
            ],
            atbilde="422; aizmirsts pārnesums"),

    Ievadi("Izlabo kļūdu", [
        {"jaut": "«268 + 154 = 312» - cik ir pareizi?", "atb": ["422"],
         "padoms": "Divi pārnesumi."},
        {"jaut": "«425 − 183 = 362» - cik ir pareizi?", "atb": ["242"],
         "padoms": "Desmitos jāaizņemas."},
        {"jaut": "«347 + 285 = 522» - cik ir pareizi?", "atb": ["632"],
         "padoms": "Pārnesums no desmitiem."},
        {"jaut": "«600 − 234 = 466» - cik ir pareizi?", "atb": ["366"],
         "padoms": "Aizņemas caur nulli."},
        {"jaut": "«175 + 236 = 301» - cik ir pareizi?", "atb": ["411"],
         "padoms": "Pārnesums no desmitiem."},
        {"jaut": "«802 − 347 = 545» - cik ir pareizi?", "atb": ["455"],
         "padoms": "Divi aizņēmumi."},
    ], pamats=4),

    Zimejums("Kā atrast kļūdaino kolonnu",
             restis([["", "S", "D", "V"],
                     ["skolēns", 3, 1, 2],
                     ["pareizi", 4, 2, 2]],
                    "268 + 154"),
             paskaidro="Vienu cipars sakrīt, desmitu un simtu - nē; tātad "
                       "kļūda sākās desmitu kolonnā.",
             ievads="Salīdzina pa kolonnām."),

    Varianti("Kāds ir kļūdas cēlonis?", [
        {"jaut": "«268 + 154 = 312» - kāda ir kļūda?",
         "opcijas": ["Aizmirsts pārnesums", "Nepareiza secība",
                     "Sašķiebts pieraksts", "Kļūdas nav"],
         "pareizi": 0, "padoms": "Desmitos pietrūkst 1."},
        {"jaut": "«425 − 183 = 362» - kāda ir kļūda?",
         "opcijas": ["Aizmirsts aizņēmums", "Aizmirsts pārnesums",
                     "Nepareiza secība", "Kļūdas nav"],
         "pareizi": 0, "padoms": "2 − 8 nesanāk bez aizņēmuma."},
        {"jaut": "«342 + 21 = 552» - kāda ir kļūda?",
         "opcijas": ["Cipari nav savās kolonnās", "Aizmirsts pārnesums",
                     "Aizmirsts aizņēmums", "Kļūdas nav"],
         "pareizi": 0, "padoms": "21 ierakstīts par vienu vietu pa kreisi."},
        {"jaut": "Kā atrast kļūdaino kolonnu?",
         "opcijas": ["Salīdzinot ciparus pa vienam",
                     "Pārrakstot atbildi", "Skaitot no gala", "Nekā"],
         "pareizi": 0, "padoms": "Pirmā kolonna, kurā cipari atšķiras."},
    ], pamats=4),

    Pasaule("Kur kļūdījās tablo?",
            Ievadi("", [
                {"jaut": "Tablo rādīja 268 + 154 = 312. Cik ir pareizi?",
                 "atb": ["422"], "padoms": "Divi pārnesumi."},
                {"jaut": "Par cik punktiem tablo kļūdījās?", "atb": ["110"],
                 "padoms": "422 − 312."},
                {"jaut": "Otrā spēlē: 425 − 183. Cik ir pareizi?",
                 "atb": ["242"], "padoms": "Ar aizņēmumu."},
                {"jaut": "Cik punktu abās spēlēs kopā?", "atb": ["664"],
                 "padoms": "422 + 242."},
            ]),
            pavediens="sports",
            konteksts="Arī tablo var kļūdīties - tāpēc tiesnesis rezultātu "
                      "vienmēr pārrēķina uz papīra.",
            kapec="Kļūda par 110 punktiem maina uzvarētāju."),

    Kopsavilkums([
        "Atrodu kļūdu dotā risinājumā.",
        "Nosaku kolonnu, kurā kļūda sākās.",
        "Nosaucu kļūdas cēloni.",
        "Izlaboju risinājumu.",
    ]),

    Majas([
        "Atrodi kļūdu rēķinā 356 + 279 = 525 un izlabo to.",
        "Uzraksti rēķinu ar aizmirstu aizņēmumu un iedod to mājiniekiem.",
        "Pieraksti savas trīs biežākās kļūdas.",
    ]),
]
