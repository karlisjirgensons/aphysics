# -*- coding: utf-8 -*-
"""2. klase, 73. stunda: «Vai vienu situāciju var pierakstīt dažādi?»

Viena situācija - vairākas pareizas izteiksmes: 50 − (12 + 8), 50 − 12 − 8
un 50 − 8 − 12 dod to pašu. Atņemt summu ir tas pats, kas atņemt katru
saskaitāmo pēc kārtas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti)

TEMA = "Vai vienu situāciju var pierakstīt dažādi?"

MERKIS = ("Šodien aplūkosim vairākas izteiksmes, ar kurām pieraksta vienu "
          "un to pašu situāciju.")

_JA_NE = ["Jā", "Nē"]

SATURS = [
    Sakums("Trīs bērni uzrakstīja trīs dažādas izteiksmes. Kurš kļūdījās?",
           fakti=["Anna: 50 − (12 + 8). Toms: 50 − 12 − 8.",
                  "Līva: 50 − 8 − 12.",
                  "Visas dod 30 - neviens nekļūdījās!"]),

    Doma("Dažādi ceļi uz to pašu",
         "Atņemt summu ir tas pats, kas atņemt katru daļu pēc kārtas.",
         soli=[
             "50 − (12 + 8): vispirms tēriņi kopā.",
             "50 − 12 − 8: vispirms grāmata, tad pildspalva.",
             "50 − 8 − 12: vispirms pildspalva, tad grāmata.",
             "Visas izteiksmes ir pareizas, jo vērtība sakrīt.",
         ]),

    Ievadi("Pārbaudi - aprēķini visas", [
        {"jaut": "60 − (15 + 5) = ?", "atb": ["40"], "padoms": "60 − 20."},
        {"jaut": "60 − 15 − 5 = ?", "atb": ["40"], "padoms": "45 − 5."},
        {"jaut": "60 − 5 − 15 = ?", "atb": ["40"], "padoms": "55 − 15."},
        {"jaut": "Vai 60 − 15 + 5 arī ir 40? Raksti tās vērtību.",
         "atb": ["50"], "padoms": "45 + 5 - cits skaitlis!"},
    ]),

    Varianti("Vai apraksta to pašu?", [
        {"jaut": "Situācija: 80 − (30 + 20). Vai der 80 − 30 − 20?",
         "opcijas": _JA_NE, "jaukt": False, "pareizi": 0,
         "padoms": "Abas ir 30."},
        {"jaut": "Situācija: 80 − (30 + 20). Vai der 80 − 30 + 20?",
         "opcijas": _JA_NE, "jaukt": False, "pareizi": 1,
         "padoms": "80 − 30 + 20 = 70."},
        {"jaut": "Situācija: 25 + 15 + 10. Vai der 25 + 10 + 15?",
         "opcijas": _JA_NE, "jaukt": False, "pareizi": 0,
         "padoms": "Saskaitāmos var samainīt."},
        {"jaut": "Situācija: 40 + 12 − 7. Vai der 40 − 7 + 12?",
         "opcijas": _JA_NE, "jaukt": False, "pareizi": 0,
         "padoms": "45 un 45."},
    ]),

    Varianti("Atrodi neiederīgo", [
        {"jaut": "Bija 90 zīmuļi, iedeva 2.a klasei 25, 2.b klasei 35. "
                 "Kura izteiksme neder?",
         "opcijas": ["90 − 25 + 35", "90 − (25 + 35)", "90 − 25 − 35"],
         "pareizi": 0, "padoms": "Abas klases zīmuļus paņēma."},
    ]),

    Pasaule("Kā saskaitīt pirkumus?",
            Varianti("", [
                {"jaut": "Grozā: maize 2 €, piens 1 €, siers 5 €. Kura "
                         "izteiksme nav kopējā cena?",
                 "opcijas": ["5 − 2 + 1", "2 + 1 + 5", "5 + 2 + 1"],
                 "pareizi": 0, "padoms": "Visu saskaita."},
                {"jaut": "Kurā secībā saskaitīt ērtāk: 17 + 8 + 3?",
                 "opcijas": ["17 + 3 + 8", "8 + 17 + 3", "tikai kā "
                             "uzrakstīts"], "pareizi": 0,
                 "padoms": "17 + 3 = 20."},
            ]),
            pavediens="veikals",
            konteksts="Kasē cenas var saskaitīt jebkurā secībā.",
            kapec="Izvēlies secību, kurā rēķināt ir vieglāk."),

    Kopsavilkums([
        "Pierakstu vienu situāciju ar dažādām izteiksmēm.",
        "Zinu, ka atņemt summu - tas pats, kas atņemt katru daļu.",
        "Pārbaudu, vai izteiksmēm vienāda vērtība.",
    ]),

    Majas([
        "Uzraksti trīs izteiksmes stāstam: 40 €, iztērēja 10 € un 15 €.",
        "Aprēķini katru.",
        "Uzraksti vienu, kas neder, un paskaidro, kāpēc.",
    ]),
]
