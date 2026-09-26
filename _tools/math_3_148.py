# -*- coding: utf-8 -*-
"""3. klase, 148. stunda: «Cik veikli rēķini?»

Mikrotemata noslēgums: saskaitīšana un atņemšana 1000 apjomā sajauktā
secībā, ar pārnesumiem, aizņēmumiem un obligātu pārbaudi. Vērtējuma nav -
ir saraksts, ko atkārtot.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Cik veikli rēķini?"

MERKIS = ("Patstāvīgi saskaitīsim un atņemsim 1000 apjomā, pārbaudot "
          "atbildes.")

SATURS = [
    Sakums("Vai visi paņēmieni jau ir rokā?",
           zimejums=restis([["+", "bez pārejas", "ar pāreju"],
                            ["−", "bez aizņēmuma", "ar aizņēmumu"]],
                           "četri gadījumi"),
           paraksts="Katrs no četriem gadījumiem prasa savu uzmanību.",
           fakti=["Grūtākie gadījumi ir pāreja un aizņēmums.",
                  "Katru atbildi pārbauda ar pretējo darbību."]),

    Doma("Rēķini, tad pārbaudi - katru reizi",
         "Pārbaude nav papildus darbs; tā ir rēķina otrā puse.",
         soli=[
             "Uzraksti piemēru stabiņā.",
             "Izrēķini, sākot no vieniem.",
             "Pārbaudi ar pretējo darbību.",
             "Ja pārbaude nesakrīt, meklē kļūdu kolonnās.",
         ],
         pieze="Ja pēc pārbaudes atbilde ir pareiza, pie šī piemēra vairs "
               "nav jāatgriežas - tas ir pabeigts."),

    Paraugs("Kā strādāt ar sajauktu sarakstu?",
            uzd="Izrēķini 703 − 258 un pārbaudi atbildi.",
            soli=[
                ("Vieni: 3 − 8 nesanāk",
                 "Desmitu vietā ir 0, aizņemas caur to."),
                ("13 − 8 = 5; 9 − 5 = 4; 6 − 2 = 4",
                 "Atbilde ir 445."),
                ("445 + 258 = 703",
                 "Pārbaude sakrīt."),
            ],
            atbilde="445"),

    Ievadi("Patstāvīgais darbs", [
        {"jaut": "268 + 154 = ?", "atb": ["422"], "padoms": "Divi pārnesumi."},
        {"jaut": "703 − 258 = ?", "atb": ["445"], "padoms": "Caur nulli."},
        {"jaut": "456 + 327 = ?", "atb": ["783"], "padoms": "Viens pārnesums."},
        {"jaut": "900 − 345 = ?", "atb": ["555"], "padoms": "Divi aizņēmumi."},
        {"jaut": "548 + 276 = ?", "atb": ["824"], "padoms": "Divi pārnesumi."},
        {"jaut": "612 − 389 = ?", "atb": ["223"], "padoms": "Divi aizņēmumi."},
        {"jaut": "Cik pietrūkst 445 līdz 1000?", "atb": ["555"],
         "padoms": "5 + 50 + 500."},
        {"jaut": "375 + 625 = ?", "atb": ["1000"], "padoms": "Apaļa summa."},
    ], pamats=6),

    Zimejums("Četri gadījumi",
             restis([["268 + 154", "ar pāreju"],
                     ["342 + 215", "bez pārejas"],
                     ["703 − 258", "ar aizņēmumu"],
                     ["568 − 234", "bez aizņēmuma"]],
                    "atpazīsti gadījumu pirms rēķina"),
             paskaidro="Ja jau iepriekš zini, kurš gadījums tas ir, kļūdu "
                       "iespēja kļūst daudz mazāka.",
             ievads="Četri piemēri, četri gadījumi."),

    Varianti("Vai atbilde ir ticama?", [
        {"jaut": "Cik apmēram ir 268 + 154?",
         "opcijas": ["400", "300", "500", "1000"],
         "pareizi": 0, "padoms": "300 + 200."},
        {"jaut": "Kurā piemērā būs aizņēmums?",
         "opcijas": ["703 − 258", "568 − 234", "342 + 215", "268 + 154"],
         "pareizi": 0, "padoms": "3 − 8 nesanāk."},
        {"jaut": "Cik ir 1000 − 555?",
         "opcijas": ["445", "455", "545", "555"],
         "pareizi": 0, "padoms": "Pārbaude: 445 + 555."},
        {"jaut": "Ar ko pārbauda starpību?",
         "opcijas": ["Ar saskaitīšanu", "Ar atņemšanu vēlreiz",
                     "Ar reizināšanu", "Nekā"],
         "pareizi": 0, "padoms": "Pretējā darbība."},
    ], pamats=4),

    Pasaule("Cik punktu ir sezonas beigās?",
            Ievadi("", [
                {"jaut": "Pirmajā pusē 268 punkti, otrajā 154. Cik kopā?",
                 "atb": ["422"], "padoms": "268 + 154."},
                {"jaut": "Pretiniekiem 703 punkti, zaudēja 258. Cik tiem "
                         "palika?",
                 "atb": ["445"], "padoms": "703 − 258."},
                {"jaut": "Par cik punktiem pretinieki ir priekšā?",
                 "atb": ["23"], "padoms": "445 − 422."},
                {"jaut": "Cik punktu abām komandām kopā?", "atb": ["867"],
                 "padoms": "422 + 445."},
            ]),
            pavediens="sports",
            konteksts="Sezonas beigās visus rezultātus saskaita un pārbauda "
                      "divas reizes.",
            kapec="23 punktu starpība izšķir, kura komanda ir čempions."),

    Kopsavilkums([
        "Patstāvīgi saskaitu un atņemu 1000 apjomā.",
        "Atpazīstu, vai būs pāreja vai aizņēmums.",
        "Pārbaudu katru atbildi ar pretējo darbību.",
        "Zinu, kuri gadījumi man vēl jātrenē.",
    ]),

    Majas([
        "Izrēķini astoņus piemērus un pārbaudi katru.",
        "Pieraksti, kuri gadījumi tev nepadevās.",
        "Atkārto tos rīt.",
    ]),
]
