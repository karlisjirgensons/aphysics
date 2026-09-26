# -*- coding: utf-8 -*-
"""8. klase, 23. stunda: «Kāda ir pakāpes vērtība ar kāpinātāju 0?»

a^0 nevar izskaidrot kā «a reizināts nulle reizes». To atklāj no virknes:
katru reizi, kad kāpinātājs samazinās par 1, vērtība dalās ar bāzi. Tā
virkne pati noved līdz 2^0 = 1, un dalīšanas īpašība to apstiprina.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, restis)

TEMA = "Kāda ir pakāpes vērtība ar kāpinātāju 0?"

MERKIS = ("Izpētīsim pakāpju virkni un formulēsim, kam vienāda pakāpe ar "
          "kāpinātāju 0.")


def _virkne(n):
    """2^4 ... līdz 2^n tabulā: kāpinātājs augšā, vērtība apakšā."""
    rinda = list(range(4, n - 1, -1))
    virs = ["2⁴", "2³", "2²", "2¹", "2⁰"]
    return restis([virs[:len(rinda)],
                   [str(2 ** k) for k in rinda]])


SATURS = [
    Sakums("Ko nozīmē 2⁰?",
           zimejums=_virkne(1),
           paraksts="Katrs solis pa labi - vērtība dalās ar 2.",
           fakti=["16 : 2 = 8, 8 : 2 = 4, 4 : 2 = 2.",
                  "Nākamais solis: 2 : 2 = 1.",
                  "Tātad 2⁰ = 1."]),

    Slidnis("Turpini virkni", [
        {"v": "2^4 = 16", "teksts": "Sākums", "zim": _virkne(4)},
        {"v": "2^3 = 8", "teksts": ": 2", "zim": _virkne(3)},
        {"v": "2^2 = 4", "teksts": ": 2", "zim": _virkne(2)},
        {"v": "2^1 = 2", "teksts": ": 2", "zim": _virkne(1)},
        {"v": "2^0 = 1", "teksts": ": 2 - un vēl dalīt var!",
         "zim": _virkne(0)},
    ], ievads="Kāpinātājs samazinās par 1 - vērtību dala ar bāzi."),

    Doma("Pakāpe ar kāpinātāju 0",
         "Jebkuram skaitlim a ≠ 0: a^0 = 1. Tas saskan ar dalīšanas "
         "īpašību: {a^n|a^n} = a^{n − n} = a^0, bet skaitlis, dalīts pats ar "
         "sevi, ir 1.",
         soli=[
             "a^0 = 1, ja a ≠ 0.",
             "Bāze var būt jebkura: 7^0 = 1, (−3)^0 = 1, ({1|2})^0 = 1.",
             "0^0 skolā nedefinē - dalīt ar 0 nedrīkst.",
             "Uzmanies: −5^0 = −1, jo kāpina tikai 5.",
         ],
         pieze="Tā nav vienošanās «no gaisa» - tā ir vienīgā vērtība, pie "
               "kuras visas pakāpju īpašības paliek spēkā."),

    Paraugs("Pārbaudi ar īpašībām",
            uzd="Aprēķini 5^3 · 5^0 un {x^4|x^4}.",
            soli=[
                ("5^3 · 5^0 = 5^{3 + 0} = 5^3", "Reizināšanas īpašība."),
                ("5^3 · 1 = 5^3", "Tas pats ar 5^0 = 1."),
                ("{x^4|x^4} = x^0 = 1", "Dalīšana; x ≠ 0."),
            ],
            atbilde="125; 1"),

    Ievadi("Aprēķini", [
        {"jaut": "9^0", "atb": ["1"], "padoms": "Jebkurš a^0 = 1."},
        {"jaut": "(−12)^0", "atb": ["1"], "padoms": "Bāze −12."},
        {"jaut": "−12^0", "atb": ["−1", "-1"], "padoms": "−(12^0)."},
        {"jaut": "3^0 + 3^1 + 3^2", "atb": ["13"], "padoms": "1 + 3 + 9."},
        {"jaut": "(2x)^0 · 7, ja x ≠ 0", "atb": ["7"], "padoms": "1 · 7."},
        {"jaut": "{a^6 · a^0|a^6}, ja a ≠ 0", "atb": ["1"],
         "padoms": "a^0."},
    ], pamats=4),

    Varianti("Kurš ir pareizi?", [
        {"jaut": "100^0 =",
         "opcijas": ["1", "0", "100", "10"],
         "pareizi": 0, "padoms": "Jebkura pakāpe ar 0."},
        {"jaut": "Kāpēc 0^0 nedefinē?",
         "opcijas": ["Tas nozīmētu {0|0} - ar 0 dalīt nedrīkst",
                     "Tas ir 0", "Tas ir 1", "Tā ir kļūda"],
         "pareizi": 0, "padoms": "a^0 = {a^n|a^n}."},
        {"jaut": "Kurš virknes turpinājums ir pareizs: 10^2 = 100, "
                 "10^1 = 10, 10^0 = ?",
         "opcijas": ["1", "0", "10", "−10"],
         "pareizi": 0, "padoms": "10 : 10."},
    ]),

    Pasaule("Skaitļi dažādās sistēmās",
            Ievadi("", [
                {"jaut": "Decimālskaitlī 352 = 3 · 10^2 + 5 · 10^1 + 2 · 10^0. "
                         "Cik ir 2 · 10^0?",
                 "atb": ["2"], "padoms": "10^0 = 1."},
                {"jaut": "Binārajā 101 = 1 · 2^2 + 0 · 2^1 + 1 · 2^0. Kāds tas "
                         "ir decimālskaitlis?",
                 "atb": ["5"], "padoms": "4 + 0 + 1."},
                {"jaut": "Binārajā 1101 = ? (vietas 2^3, 2^2, 2^1, 2^0)",
                 "atb": ["13"], "padoms": "8 + 4 + 0 + 1."},
            ]),
            pavediens="kodi",
            konteksts="Vienu vieta katrā skaitīšanas sistēmā ir bāze nultajā "
                      "pakāpē - tāpēc tā vienmēr ir 1.",
            kapec="Bez a^0 = 1 skaitļu pieraksts nestrādātu."),

    Kopsavilkums([
        "Zinu, ka a^0 = 1, ja a ≠ 0.",
        "Pamatoju to ar virkni un dalīšanas īpašību.",
        "Atšķiru (−a)^0 no −a^0.",
    ]),

    Majas([
        "Uzraksti virkni 3^4, 3^3, ..., 3^0 ar vērtībām.",
        "Aprēķini 5^0 + 5^1 + 5^2.",
        "Pieraksti savu dzimšanas gadu kā 10 pakāpju summu.",
    ]),
]
