# -*- coding: utf-8 -*-
"""2. klase, 86. stunda: «Kā izlasīt pierakstu ar vārdiem?»

Zīmes pārvērš vārdos un otrādi: «=» - tikpat, «<» - mazāk nekā, īsāks nekā,
«>» - vairāk nekā, garāks nekā. Latviski salīdzina ar «nekā».
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, restis)

TEMA = "Kā izlasīt pierakstu ar vārdiem?"

MERKIS = ("Šodien lasīsim vienādības un nevienādības ar vārdiem: tikpat "
          "garš, īsāks nekā, garāks nekā.")

SATURS = [
    Sakums("Kā pateikt «AB < CD» vārdiem?",
           zimejums=restis([["zīme", "vārdiem"],
                            ["=", "tikpat, vienāds ar"],
                            ["<", "mazāks nekā, īsāks nekā"],
                            [">", "lielāks nekā, garāks nekā"]]),
           fakti=["AB < CD: nogrieznis AB ir īsāks nekā CD.",
                  "Latviski salīdzina ar vārdu «nekā»."]),

    Doma("Zīme - vārdi",
         "Katrai zīmei ir savi vārdi atkarībā no tā, ko salīdzina.",
         soli=[
             "Garumi: īsāks nekā, garāks nekā, tikpat garš.",
             "Skaitļi: mazāks nekā, lielāks nekā, vienāds ar.",
             "Nauda: lētāks nekā, dārgāks nekā.",
             "Vecums: jaunāks nekā, vecāks nekā.",
         ]),

    Varianti("Izlasi vārdiem", [
        {"jaut": "Lente A = 40 cm, lente B = 40 cm. A = B.",
         "opcijas": ["A ir tikpat gara kā B", "A ir garāka nekā B",
                     "A ir īsāka nekā B"], "pareizi": 0,
         "padoms": "«=» - tikpat."},
        {"jaut": "Grāmata 12 € < spēle 25 €.",
         "opcijas": ["Grāmata ir lētāka nekā spēle",
                     "Grāmata ir dārgāka nekā spēle", "Tās maksā tikpat"],
         "pareizi": 0, "padoms": "«<» - mazāk."},
        {"jaut": "Anna 8 gadi > Toms 7 gadi.",
         "opcijas": ["Anna ir vecāka nekā Toms",
                     "Anna ir jaunāka nekā Toms", "Viņi ir vienaudži"],
         "pareizi": 0, "padoms": "«>» - vairāk gadu."},
        {"jaut": "Mārtiņš 25 kg < tētis 80 kg.",
         "opcijas": ["Mārtiņš ir vieglāks nekā tētis",
                     "Mārtiņš ir smagāks nekā tētis", "Viņi sver tikpat"],
         "pareizi": 0, "padoms": "«<» - mazāk kilogramu."},
    ]),

    Varianti("Uzraksti ar zīmi", [
        {"jaut": "«Suns ir smagāks nekā kaķis.» (suns 20 kg, kaķis 5 kg)",
         "opcijas": ["20 kg > 5 kg", "20 kg < 5 kg", "20 kg = 5 kg"],
         "pareizi": 0, "padoms": "Smagāks - vairāk."},
        {"jaut": "«Zīmulis ir īsāks nekā lineāls.» (15 cm un 30 cm)",
         "opcijas": ["15 cm < 30 cm", "15 cm > 30 cm", "15 cm = 30 cm"],
         "pareizi": 0, "padoms": "Īsāks - mazāk."},
    ]),

    Pasaule("Rekordu grāmata",
            Varianti("", [
                {"jaut": "Žirafe 5 m, zilonis 3 m. Kā izlasīt «5 m > 3 m»?",
                 "opcijas": ["Žirafe ir garāka nekā zilonis",
                             "Zilonis ir garāks nekā žirafe",
                             "Tie ir tikpat gari"], "pareizi": 0,
                 "padoms": "«>» - vairāk."},
            ]),
            pavediens="daba",
            konteksts="Dzīvnieku rekordu grāmatā skaitļus salīdzina.",
            kapec="Zīme un teikums pasaka to pašu."),

    Kopsavilkums([
        "Lasu <, > un = ar vārdiem.",
        "Izvēlos pareizos vārdus: īsāks, garāks, tikpat.",
        "Pierakstu teikumu ar zīmi.",
    ]),

    Majas([
        "Salīdzini ģimenes augumus.",
        "Uzraksti 3 teikumus ar «garāks nekā» vai «tikpat garš».",
        "Pārraksti tos ar zīmēm.",
    ]),
]
