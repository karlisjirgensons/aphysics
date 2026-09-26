# -*- coding: utf-8 -*-
"""8. klase, 46. stunda: «Kādi skaitļi ir racionāli?»

Racionāls ir katrs skaitlis, ko var uzrakstīt kā {m|n} ar veseliem m un
n ≠ 0 - arī 5, −2 un 0,(3). Stunda sakārto līdz šim zināmās kopas N, Z, Q
vienu otrā un sagatavo jautājumu: vai ir skaitļi, kas nav daļas?
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, restis)

TEMA = "Kādi skaitļi ir racionāli?"

MERKIS = ("Sapratīsim, ka racionālu skaitli var pierakstīt kā daļu, un "
          "noteiksim skaitļu piederību kopām.")


def _kopas(n):
    rindas = [["N", "naturālie", "1; 2; 3; ..."],
              ["Z", "veselie", "...; −1; 0; 1; ..."],
              ["Q", "racionālie", "m/n"]]
    return restis(rindas[:n])


SATURS = [
    Sakums("Vai 0,25 ir daļa?",
           zimejums=restis([["5", "=", "5/1"], ["−2", "=", "−2/1"],
                            ["0,25", "=", "1/4"], ["0,(3)", "=", "1/3"]]),
           paraksts="Visus šos skaitļus var pierakstīt kā daļu.",
           fakti=["Veselu skaitli - ar saucēju 1.",
                  "Galīgu decimāldaļu - ar saucēju 10, 100...",
                  "Periodisku - kā iepriekšējā stundā."]),

    Doma("Racionāli skaitļi",
         "Racionāls skaitlis ir skaitlis, ko var pierakstīt kā {m|n}, kur m ir "
         "vesels, n - naturāls skaitlis. Racionālo skaitļu kopu apzīmē ar Q.",
         soli=[
             "N - naturālie: 1; 2; 3; ...",
             "Z - veselie: naturālie, 0 un pretējie tiem.",
             "Q - racionālie: visas daļas {m|n}.",
             "N ⊂ Z ⊂ Q - katra kopa ir nākamās apakškopa.",
             "Decimāldaļā racionāls skaitlis ir galīgs vai periodisks.",
         ]),

    Slidnis("Kopas viena otrā", [
        {"v": "N", "teksts": "Skaitīšanai: 1; 2; 3", "zim": _kopas(1)},
        {"v": "Z", "teksts": "Klāt 0 un negatīvie", "zim": _kopas(2)},
        {"v": "Q", "teksts": "Klāt daļas", "zim": _kopas(3)},
    ]),

    Varianti("Kurai mazākajai kopai pieder?", [
        {"jaut": "−7",
         "opcijas": ["Z", "N", "Q, bet ne Z", "Nevienai"],
         "pareizi": 0, "padoms": "Vesels, negatīvs."},
        {"jaut": "0",
         "opcijas": ["Z", "N", "Q, bet ne Z", "Nevienai"],
         "pareizi": 0, "padoms": "Latvijā 0 nav naturāls."},
        {"jaut": "{12|4}",
         "opcijas": ["N", "Z, bet ne N", "Q, bet ne Z", "Nevienai"],
         "pareizi": 0, "padoms": "{12|4} = 3."},
        {"jaut": "−0,(6)",
         "opcijas": ["Q, bet ne Z", "Z", "N", "Nevienai"],
         "pareizi": 0, "padoms": "−{2|3}."},
    ]),

    Ievadi("Pieraksti kā daļu", [
        {"jaut": "0,6 = {3|?}", "atb": ["5"], "padoms": "{6|10}."},
        {"jaut": "2,25 = {9|?}", "atb": ["4"], "padoms": "{225|100}."},
        {"jaut": "−1,5 = {?|2}", "atb": ["−3", "-3"], "padoms": "−{3|2}."},
        {"jaut": "0,(4) = {4|?}", "atb": ["9"], "padoms": "10x − x = 4."},
    ]),

    Pasaule("Sporta rezultāti",
            Ievadi("", [
                {"jaut": "Basketbolists iemeta 12 no 20 metieniem. Kāda daļa "
                         "(decimāldaļā)?",
                 "atb": ["0,6", "0.6"], "padoms": "{12|20}."},
                {"jaut": "Otrs - 5 no 9. Kāda daļa (0,(5) - ieraksti "
                         "periodu)?",
                 "atb": ["5"], "padoms": "{5|9} = 0,555..."},
                {"jaut": "Kurš metējs precīzāks? (1 vai 2)",
                 "atb": ["1"], "padoms": "0,6 > 0,555..."},
            ]),
            pavediens="sports",
            konteksts="Statistikā trāpījumu daļa vienmēr ir racionāls skaitlis "
                      "- trāpījumi dalīti ar metieniem.",
            kapec="Periodisku daļu salīdzina tāpat kā galīgu."),

    Kopsavilkums([
        "Zinu, ka racionālu skaitli var pierakstīt kā daļu.",
        "Nosaku skaitļa piederību kopām N, Z, Q.",
        "Pārveidoju galīgu un periodisku decimāldaļu par daļu.",
    ]),

    Majas([
        "Pieraksti kā daļu: 1,2; −0,05; 0,(8).",
        "Uzraksti pa diviem skaitļiem, kas pieder Z, bet ne N; Q, bet ne Z.",
        "Padomā: vai katra bezgalīga decimāldaļa ir periodiska?",
    ]),
]
