# -*- coding: utf-8 -*-
"""8. klase, 105. stunda: «Vai īpašība ir arī pazīme?»

Īpašība: «ja rombs, tad diagonāles perpendikulāras». Apgrieztais
apgalvojums («ja diagonāles perpendikulāras, tad rombs») ir aplams -
pretpiemērs ir deltoīds. Viens pretpiemērs pietiek, lai apgalvojumu
atspēkotu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, geometrija)

TEMA = "Vai īpašība ir arī pazīme?"

MERKIS = ("Izvērtēsim, kuras īpašības ir arī pazīmes, un pamatosim ar "
          "pretpiemēru.")

SATURS = [
    Sakums("Diagonāles perpendikulāras - vai tas ir rombs?",
           zimejums=geometrija([("A", 0, 0), ("B", 3, -2, 270), ("C", 8, 0),
                                ("D", 3, 2, 90), ("O", 3, 0, 300)],
                               nogriezni=["AB", "BC", "CD", "DA", "AC",
                                          "BD"],
                               taisni=["COD"], iekrasot=[("ABCD", 0)]),
           paraksts="Deltoīds: diagonāles perpendikulāras, bet tas nav rombs.",
           fakti=["Īpašība: «ja figūra ir X, tad ...».",
                  "Pazīme: «ja ..., tad figūra ir X».",
                  "Viens pretpiemērs atspēko apgalvojumu."]),

    Doma("Apgriezts apgalvojums",
         "Apgriežot apgalvojumu, tas var kļūt aplams.",
         soli=[
             "Pieraksti īpašību formā «ja ..., tad ...».",
             "Samaini vietām nosacījumu un secinājumu.",
             "Meklē pretpiemēru - figūru, kam nosacījums der, bet "
             "secinājums ne.",
             "Ja pretpiemēra nav un var pierādīt - tā ir pazīme.",
         ],
         pieze="Paralelogramam vienādas diagonāles ir pazīme, ka tas ir "
               "taisnstūris, bet jebkuram četrstūrim - nav."),

    Varianti("Pazīme vai nē?", [
        {"jaut": "«Ja četrstūra diagonāles ir perpendikulāras, tas ir "
                 "rombs.»",
         "opcijas": ["Aplams - pretpiemērs deltoīds", "Patiess",
                     "Patiess tikai kvadrātam", "Nevar pārbaudīt"],
         "pareizi": 0, "padoms": "Skaties sākuma zīmējumu."},
        {"jaut": "«Ja četrstūra diagonāles dalās uz pusēm, tas ir "
                 "paralelograms.»",
         "opcijas": ["Patiess - tā ir pazīme", "Aplams", "Tikai rombam",
                     "Tikai taisnstūrim"],
         "pareizi": 0, "padoms": "98. stundas pazīme."},
        {"jaut": "«Ja četrstūra diagonāles ir vienādas, tas ir "
                 "taisnstūris.»",
         "opcijas": ["Aplams - pretpiemērs vienādsānu trapece", "Patiess",
                     "Patiess tikai rombam", "Patiess kvadrātam"],
         "pareizi": 0, "padoms": "Vienādsānu trapecei diagonāles vienādas."},
        {"jaut": "«Ja paralelograma diagonāles ir vienādas, tas ir "
                 "taisnstūris.»",
         "opcijas": ["Patiess - tā ir pazīme", "Aplams", "Tikai rombam",
                     "Nevar zināt"],
         "pareizi": 0, "padoms": "103. stunda."},
    ]),

    Ievadi("Pretpiemēri skaitļos", [
        {"jaut": "Deltoīdam diagonāles 6 un 8, perpendikulāras. Laukums?",
         "atb": ["24"], "padoms": "{6 · 8|2} der arī deltoīdam."},
        {"jaut": "Cik malu pāru vienādas deltoīdam (blakus malas)?",
         "atb": ["2"], "padoms": "AB = AD, CB = CD."},
        {"jaut": "Vienādsānu trapecei diagonāles 7 un ?", "atb": ["7"],
         "padoms": "Vienādas."},
    ]),

    Pasaule("Reklāmas apgalvojums",
            Ievadi("", [
                {"jaut": "«Visi čempioni ēd musli.» Vai no tā izriet: «kas ēd "
                         "musli, ir čempions»? (1 - jā, 0 - nē)",
                 "atb": ["0"], "padoms": "Apgriezts apgalvojums."},
                {"jaut": "Cik pretpiemēru vajag, lai to atspēkotu?",
                 "atb": ["1"], "padoms": "Viens cilvēks, kas ēd musli, bet "
                                        "nav čempions."},
                {"jaut": "«Ja līst, iela ir slapja.» Vai «ja iela slapja, "
                         "tad līst» ir patiess? (1/0)",
                 "atb": ["0"], "padoms": "Iela var būt nomazgāta."},
            ]),
            pavediens="veikals",
            konteksts="Reklāmās un ziņās bieži apgriež apgalvojumus - tā "
                      "izskatās pārliecinoši.",
            kapec="Apgriezts apgalvojums nav automātiski patiess."),

    Kopsavilkums([
        "Pierakstu īpašību un tās apgriezto apgalvojumu.",
        "Atrodu pretpiemēru aplamai pazīmei.",
        "Nošķiru pazīmes no īpašībām četrstūriem.",
    ]),

    Majas([
        "Uzzīmē deltoīdu un pārbaudi, ka diagonāles perpendikulāras.",
        "Izdomā vēl vienu apgalvojumu, kura apgrieztais ir aplams.",
        "Uzraksti tabulu: īpašība - vai tā ir pazīme - pretpiemērs.",
    ]),
]
