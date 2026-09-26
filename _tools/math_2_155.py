# -*- coding: utf-8 -*-
"""2. klase, 155. stunda: «Kas ir trešdaļa, ceturtdaļa, piektdaļa?»

Figūru rūtiņu lapā sadala 3, 4 vai 5 vienādās daļās un nosauc vienu daļu:
trešdaļa, ceturtdaļa, piektdaļa. Daļskaitļa pierakstu ({1|3}) vēl nelieto -
to sāks 3. klasē; te vārds un zīmējums.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, dala)

TEMA = "Kas ir trešdaļa, ceturtdaļa, piektdaļa?"

MERKIS = ("Šodien sadalīsim figūru rūtiņu lapā vienādās daļās un "
          "nosauksim katru daļu.")

SATURS = [
    Sakums("Kā sadalīt picu 4 draugiem - kā sauc katra gabalu?",
           zimejums=dala(4, 1),
           paraksts="Viena no 4 vienādām daļām - ceturtdaļa.",
           fakti=["2 daļas - puse.",
                  "3 daļas - trešdaļa, 4 - ceturtdaļa.",
                  "5 daļas - piektdaļa."]),

    Doma("Daļas nosaukums",
         "Daļas nosaukums pasaka, cik vienādās daļās dalīts viss.",
         soli=[
             "Sadali figūru vienādās daļās.",
             "Saskaiti daļas.",
             "3 - trešdaļa, 4 - ceturtdaļa, 5 - piektdaļa.",
             "Jo vairāk daļu, jo mazāka katra.",
         ]),

    Slidnis("Josla dalās", [
        {"v": "puse", "teksts": "2 vienādas daļas.", "zim": dala(2, 1)},
        {"v": "trešdaļa", "teksts": "3 vienādas daļas.", "zim": dala(3, 1)},
        {"v": "ceturtdaļa", "teksts": "4 vienādas daļas.", "zim": dala(4, 1)},
        {"v": "piektdaļa", "teksts": "5 vienādas daļas.", "zim": dala(5, 1)},
    ]),

    Varianti("Kā sauc?", [
        {"jaut": "Iekrāsotā daļa ir...", "zim": dala(3, 1),
         "opcijas": ["trešdaļa", "puse", "ceturtdaļa"], "pareizi": 0,
         "padoms": "Saskaiti daļas."},
        {"jaut": "Iekrāsotā daļa ir...", "zim": dala(5, 1),
         "opcijas": ["piektdaļa", "trešdaļa", "ceturtdaļa"], "pareizi": 0,
         "padoms": "5 daļas."},
        {"jaut": "Kura daļa lielāka - trešdaļa vai piektdaļa?",
         "opcijas": ["trešdaļa", "piektdaļa"], "jaukt": False, "pareizi": 0,
         "padoms": "Mazāk daļu - lielāka katra."},
        {"jaut": "Cik ceturtdaļu ir veselajā?", "opcijas": ["4", "2", "3"],
         "pareizi": 0, "padoms": "Ceturtdaļa - viena no 4."},
    ]),

    Ievadi("Daļa no skaitļa", [
        {"jaut": "Trešdaļa no 12 āboliem?", "atb": ["4"],
         "padoms": "12 : 3."},
        {"jaut": "Ceturtdaļa no 20?", "atb": ["5"], "padoms": "20 : 4."},
        {"jaut": "Piektdaļa no 30?", "atb": ["6"], "padoms": "30 : 5."},
        {"jaut": "Trešdaļa no 27?", "atb": ["9"], "padoms": "27 : 3."},
    ]),

    Petijums("Loki un krāso", [
        "Sagriez 3 vienādas papīra sloksnes.",
        "Pirmo saloki 3 vienādās daļās, otru - 4, trešo - 5.",
        "Katrā iekrāso vienu daļu.",
        "Salīdzini: kura iekrāsotā daļa lielākā?",
    ], vajag="papīra sloksnes, krāsainie zīmuļi"),

    Pasaule("Pica ģimenei",
            Ievadi("", [
                {"jaut": "Picu sagrieza 4 vienādās daļās. Mamma apēda "
                         "ceturtdaļu. Cik daļu palika?", "atb": ["3"],
                 "padoms": "4 − 1."},
                {"jaut": "Picā 20 salami šķēlītes, vienmērīgi. Cik šķēlīšu "
                         "vienā ceturtdaļā?", "atb": ["5"],
                 "padoms": "20 : 4."},
            ]),
            pavediens="virtuve",
            konteksts="Svētdienā ģimene cep picu.",
            kapec="Daļas nosaukums pasaka, cik liels gabals."),

    Kopsavilkums([
        "Sadalu figūru 3, 4, 5 vienādās daļās.",
        "Nosaucu daļu: trešdaļa, ceturtdaļa, piektdaļa.",
        "Atrodu daļu no skaitļa ar dalīšanu.",
    ]),

    Majas([
        "Sagriez ābolu 4 vienādās daļās.",
        "Cik ir katra daļa? Kā to sauc?",
        "Uzzīmē apli, sadalītu trešdaļās.",
    ]),
]
