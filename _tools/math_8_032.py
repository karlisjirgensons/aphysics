# -*- coding: utf-8 -*-
"""8. klase, 32. stunda: «Kāda likumsakarība ir pakāpju virknē?»

Pētnieciska stunda: pakāpju pēdējie cipari atkārtojas ciklā (2, 4, 8, 6).
No cikla var atrast 2^{2026} pēdējo ciparu, neaprēķinot skaitli ar 600
cipariem. Tā ir tā pati spriešana, ko prasa eksāmena 2. daļas virknes.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, restis)

TEMA = "Kāda likumsakarība ir pakāpju virknē?"

MERKIS = ("Izpētīsim likumsakarības pakāpju pēdējos ciparos un formulēsim "
          "vispārinājumu.")


def _cikls(baze, n):
    """Pakāpes baze^1 ... baze^n un to pēdējie cipari."""
    return restis([["n"] + [str(k) for k in range(1, n + 1)],
                   ["cip."] + [str(baze ** k % 10) for k in range(1, n + 1)]])


SATURS = [
    Sakums("Kāds ir 2²⁰²⁶ pēdējais cipars?",
           zimejums=_cikls(2, 8),
           paraksts="2ⁿ pēdējais cipars: 2, 4, 8, 6 - un no jauna.",
           fakti=["Cikla garums ir 4.",
                  "2026 : 4 = 506, atlikums 2.",
                  "Tātad tāpat kā 2² - pēdējais cipars 4."]),

    Doma("Kā atrast ciklu",
         "Pēdējais cipars atkarīgs tikai no iepriekšējā pēdējā cipara, tāpēc "
         "agrāk vai vēlāk tas sāk atkārtoties.",
         soli=[
             "Izraksti pirmo pakāpju pēdējos ciparus.",
             "Atrodi, kad cipari sāk atkārtoties - tas ir cikla garums.",
             "Dali kāpinātāju ar cikla garumu un atrodi atlikumu.",
             "Atlikums 0 nozīmē cikla pēdējo ciparu.",
         ],
         pieze="Reizinot ievēro tikai pēdējo ciparu: 8 · 2 = 16, tātad "
               "nākamais ir 6 - pārējie cipari neietekmē."),

    Slidnis("Dažādas bazes - dažādi cikli", [
        {"v": "2^n: 2, 4, 8, 6", "teksts": "Cikls 4", "zim": _cikls(2, 8)},
        {"v": "3^n: 3, 9, 7, 1", "teksts": "Cikls 4", "zim": _cikls(3, 8)},
        {"v": "4^n: 4, 6", "teksts": "Cikls 2", "zim": _cikls(4, 8)},
        {"v": "5^n: 5", "teksts": "Vienmēr 5", "zim": _cikls(5, 8)},
        {"v": "9^n: 9, 1", "teksts": "Cikls 2", "zim": _cikls(9, 8)},
    ]),

    Ievadi("Atrodi pēdējo ciparu", [
        {"jaut": "2^{10}", "atb": ["4"], "padoms": "10 : 4 - atlikums 2."},
        {"jaut": "3^{20}", "atb": ["1"], "padoms": "Atlikums 0 - 4. cipars."},
        {"jaut": "7^3", "atb": ["3"], "padoms": "343."},
        {"jaut": "4^{99}", "atb": ["4"], "padoms": "Nepāra kāpinātājs."},
        {"jaut": "2^{2026}", "atb": ["4"], "padoms": "Atlikums 2."},
        {"jaut": "3^{2027}", "atb": ["7"], "padoms": "2027 : 4 - atlikums 3."},
    ], pamats=4),

    Varianti("Vispārinājums", [
        {"jaut": "Kuras bazes pakāpēm pēdējais cipars vienmēr ir 6?",
         "opcijas": ["6", "4", "2", "8"],
         "pareizi": 0, "padoms": "6 · 6 = 36."},
        {"jaut": "Vai 7^n var beigties ar 5?",
         "opcijas": ["Nē - cikls ir 7, 9, 3, 1", "Jā", "Tikai pāra n",
                     "Tikai n = 5"],
         "pareizi": 0, "padoms": "Izraksti ciklu."},
    ]),

    Petijums("Pēti 7 un 8 pakāpes",
             vajag="burtnīca",
             soli=[
                 "Izraksti 7^1 ... 7^5 pēdējos ciparus.",
                 "Atrodi cikla garumu.",
                 "Tāpat ar 8^1 ... 8^5.",
                 "Uzraksti likumu: kā atrast 8^n pēdējo ciparu jebkuram n.",
             ],
             secinajums="7^n: 7, 9, 3, 1; 8^n: 8, 4, 2, 6. Abiem cikls ir 4."),

    Pasaule("Nedēļas dienas",
            Ievadi("", [
                {"jaut": "Dienas atkārtojas ciklā ar garumu 7. Šodien ir "
                         "pirmdiena. Kas būs pēc 100 dienām? (1 = pirmdiena, "
                         "2 = otrdiena...)",
                 "atb": ["3"], "padoms": "100 : 7 - atlikums 2."},
                {"jaut": "Luksofors: 30 s zaļš, 5 s dzeltens, 25 s sarkans. "
                         "Cikla garums sekundēs?",
                 "atb": ["60"], "padoms": "30 + 5 + 25."},
                {"jaut": "Pēc 1000 s no zaļā sākuma. Cik sekunžu jau pagājis "
                         "pašreizējā ciklā?",
                 "atb": ["40"], "padoms": "1000 : 60 - atlikums 40 (sarkans)."},
            ]),
            pavediens="kodi",
            konteksts="Cikliskas sistēmas - kalendārs, luksofori, šifri - "
                      "strādā ar atlikumu, tāpat kā pēdējie cipari.",
            kapec="Atlikums pasaka vietu ciklā bez skaitīšanas."),

    Kopsavilkums([
        "Atrodu pakāpju pēdējo ciparu ciklu.",
        "Lietoju atlikumu, lai atrastu vietu ciklā.",
        "Formulēju vispārinājumu jebkuram n.",
    ]),

    Majas([
        "Atrodi 7^{100} un 8^{2026} pēdējo ciparu.",
        "Pierādi, ka 5^n vienmēr beidzas ar 5.",
        "Kāda nedēļas diena būs tavā nākamajā dzimšanas dienā?",
    ]),
]
