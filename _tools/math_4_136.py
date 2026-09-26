# -*- coding: utf-8 -*-
"""4. klase, 136. stunda: «Kā izskatās figūru virkne ar daļām?»

4.6. temata pēdējā stunda pirms PD. Figūru virknē katrā nākamajā figūrā
iekrāsots par vienu gabalu vairāk: {1|6}, {2|6}, {3|6}, ... Skolēns to
pieraksta kā skaitļu virkni un nosaka, kurā solī figūra būs pilna.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Sakums, Slidnis, Varianti, dala)

TEMA = "Kā izskatās figūru virkne ar daļām?"

MERKIS = ("Saskatīsim likumsakarību figūru virknē ar daļām un pierakstīsim "
          "to kā skaitļu virkni.")

SATURS = [
    Sakums("Kāda būs nākamā figūra?",
           zimejums=dala(6, 1, "1/6") + dala(6, 2, "2/6")
           + dala(6, 3, "3/6"),
           paraksts="Katrā nākamajā - vēl viens gabals.",
           fakti=["Figūras veido virkni: {1|6}, {2|6}, {3|6}.",
                  "Nākamā būs {4|6}."]),

    Doma("Figūras → daļas → virkne",
         "Katru figūru pieraksta kā daļu, un daļu virknē meklē soli.",
         soli=[
             "Saskaiti gabalus figūrā - saucējs.",
             "Saskaiti iekrāsotos - skaitītājs.",
             "Salīdzini blakus figūras - kāds ir solis?",
             "Pajautā: kurā solī figūra būs pilna ({n|n})?",
         ],
         pieze="Ja solis ir 2 gabali, figūra ar 6 gabaliem piepildās 3 "
               "soļos."),

    Slidnis("Figūra piepildās",
            soli=[
                {"v": "{1|6}", "zim": dala(6, 1), "teksts": "1. figūra."},
                {"v": "{2|6}", "zim": dala(6, 2), "teksts": "2. figūra."},
                {"v": "{3|6}", "zim": dala(6, 3), "teksts": "3. figūra."},
                {"v": "{4|6}", "zim": dala(6, 4), "teksts": "4. figūra."},
                {"v": "{5|6}", "zim": dala(6, 5), "teksts": "5. figūra."},
                {"v": "{6|6} = 1", "zim": dala(6, 6),
                 "teksts": "6. figūra - pilna."},
            ]),

    Ievadi("Turpini virkni", [
        {"jaut": "{1|6}, {2|6}, {3|6}, ?", "atb": ["4/6"],
         "vieta": "piem., 1/2", "padoms": "+ {1|6}."},
        {"jaut": "Kurā figūrā būs {6|6}?", "atb": ["6"],
         "padoms": "Skaitītājs = numurs."},
        {"jaut": "{2|10}, {4|10}, {6|10}, ?", "atb": ["8/10"],
         "vieta": "piem., 1/2", "padoms": "+ {2|10}."},
        {"jaut": "Kurā figūrā virknē {2|10}, {4|10}, ... būs pilna?",
         "atb": ["5"], "padoms": "10 : 2."},
    ]),

    Varianti("Kāds solis?", [
        {"jaut": "{1|8}, {3|8}, {5|8}, ...",
         "opcijas": ["+ {2|8}", "+ {1|8}", "· 2", "+ {3|8}"], "pareizi": 0,
         "padoms": "3 − 1 = 2."},
        {"jaut": "Vai virknē {1|8}, {3|8}, {5|8}, ... kāda figūra būs tieši "
                 "pilna?",
         "opcijas": ["nē - skaitītāji nepāra, 8 nesanāks", "jā, 4.",
                     "jā, 8."], "pareizi": 0,
         "padoms": "1, 3, 5, 7, 9 - 8 izlaists."},
        {"jaut": "{9|9}, {7|9}, {5|9}, ... - kas notiek?",
         "opcijas": ["figūra iztukšojas", "piepildās", "nemainās"],
         "pareizi": 0, "padoms": "Skaitītājs samazinās."},
    ]),

    Pasaule("Uzlādes josla",
            Ievadi("", [
                {"jaut": "Telefona josla 10 iedaļās, ik 5 min +1 iedaļa. Sāk "
                         "ar {3|10}. Kāda daļa pēc 20 min?",
                 "atb": ["7/10"], "vieta": "piem., 1/2",
                 "padoms": "20 : 5 = 4 iedaļas."},
                {"jaut": "Pēc cik minūtēm no {3|10} būs pilns?", "atb": ["35"],
                 "padoms": "7 iedaļas · 5 min."},
                {"jaut": "Ja uzlāde ik 5 min +{2|10}, pēc cik minūtēm no "
                         "{2|10} būs pilns?",
                 "atb": ["20"], "padoms": "8 : 2 = 4 soļi · 5 min."},
                {"jaut": "Lejupielāde: {1|8}, {2|8}, ... ik minūti. Cik "
                         "minūtes kopā līdz pilnai (no 0)?",
                 "atb": ["8"], "padoms": "8 soļi."},
            ]),
            pavediens="dati",
            konteksts="Uzlādes un lejupielādes joslas ir figūru virkne ar "
                      "daļām - tās aug vienādos soļos.",
            kapec="Virkne pasaka, cik ilgi vēl jāgaida."),

    Kopsavilkums([
        "Pierakstu figūru virkni kā daļu virkni.",
        "Atrodu soli un turpinu virkni.",
        "Nosaku, kurā solī figūra būs pilna.",
        "Esmu gatavs 4.6. temata pārbaudes darbam.",
    ]),

    Majas([
        "Uzzīmē figūru virkni ar saucēju 5, kas piepildās.",
        "Pavēro uzlādes joslu un pieraksti virkni.",
        "Atkārto: daļa no skaitļa, veselais pēc daļas.",
    ], ievads="Nākamajā stundā - pārbaudes darbs par 4.6. tematu."),
]
