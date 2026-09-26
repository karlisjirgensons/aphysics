# -*- coding: utf-8 -*-
"""2. klase, 84. stunda: «Vai pieraksts ir patiess?»

Vienādība (45 + 5 = 50) un nevienādība (38 < 40) var būt patiesa vai
aplama. To noskaidro, aprēķinot abas puses vai spriežot. Tā ir pirmā
saskarsme ar apgalvojumu, ko var pārbaudīt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti)

TEMA = "Vai pieraksts ir patiess?"

MERKIS = ("Šodien noteiksim, vai vienādība vai nevienādība ir patiesa, "
          "izmantojot dažādus paņēmienus.")

_PA = ["patiesa", "aplama"]

SATURS = [
    Sakums("Vai 30 + 25 = 60 ir taisnība?",
           fakti=["Kreisā puse: 30 + 25 = 55.",
                  "Labā puse: 60.",
                  "55 nav 60 - vienādība ir aplama."]),

    Doma("Patiess vai aplams",
         "Pieraksts ir patiess, ja abas puses tiešām ir tādas, kā saka zīme.",
         soli=[
             "«=» - abām pusēm jābūt vienādām.",
             "«<» - kreisajai jābūt mazākai, «>» - lielākai.",
             "Aprēķini katru pusi vai spried.",
             "Salīdzini un izlem: patiesa vai aplama.",
         ]),

    Varianti("Patiesa vai aplama?", [
        {"jaut": "45 + 5 = 50", "opcijas": _PA, "jaukt": False,
         "pareizi": 0, "padoms": "45 + 5 = 50."},
        {"jaut": "63 − 20 = 33", "opcijas": _PA, "jaukt": False,
         "pareizi": 1, "padoms": "63 − 20 = 43."},
        {"jaut": "38 + 12 < 49", "opcijas": _PA, "jaukt": False,
         "pareizi": 1, "padoms": "50 nav mazāks par 49."},
        {"jaut": "70 − 25 > 40", "opcijas": _PA, "jaukt": False,
         "pareizi": 0, "padoms": "45 > 40."},
        {"jaut": "27 + 18 = 18 + 27", "opcijas": _PA, "jaukt": False,
         "pareizi": 0, "padoms": "Saskaitāmos var samainīt."},
        {"jaut": "50 − 20 = 20 − 50", "opcijas": _PA, "jaukt": False,
         "pareizi": 1, "padoms": "Atņemot samainīt nevar."},
    ], pamats=4),

    Ievadi("Izlabo, lai būtu patiesa", [
        {"jaut": "30 + 25 = ?", "atb": ["55"], "padoms": "Aprēķini."},
        {"jaut": "63 − 20 = ?", "atb": ["43"], "padoms": "6 − 2 desmiti."},
        {"jaut": "? + 15 = 40", "atb": ["25"], "padoms": "40 − 15."},
        {"jaut": "80 − ? = 55", "atb": ["25"], "padoms": "80 − 55."},
    ]),

    Pasaule("Vai reklāma saka taisnību?",
            Varianti("", [
                {"jaut": "Reklāma: «Bumba 12 € + tīkls 8 € = tikai 18 €!» "
                         "Vai tā ir patiesība?",
                 "opcijas": ["Nē, 12 + 8 = 20", "Jā"], "jaukt": False,
                 "pareizi": 0, "padoms": "Saskaiti."},
                {"jaut": "«Komplekts lētāks nekā 25 €», ja komplekts maksā "
                         "12 € + 8 €. Patiess?",
                 "opcijas": ["Jā, 20 < 25", "Nē"], "jaukt": False,
                 "pareizi": 0, "padoms": "20 un 25."},
            ]),
            pavediens="veikals",
            konteksts="Reklāmās skaitļi ne vienmēr ir pareizi.",
            kapec="Pārbaudīt var ikviens, kurš prot rēķināt."),

    Kopsavilkums([
        "Nosaku, vai vienādība ir patiesa.",
        "Nosaku, vai nevienādība ir patiesa.",
        "Izlaboju aplamu pierakstu.",
    ]),

    Majas([
        "Uzraksti 3 patiesas un 2 aplamas vienādības.",
        "Lai mājinieks atrod aplamās.",
        "Izlabo tās.",
    ]),
]
