# -*- coding: utf-8 -*-
"""7. klase, 114. stunda: «Ko nozīmē 4a?»

4a nozīmē 4 · a = a + a + a + a. Ģeometriski - četri vienādi nogriežņi
pēc kārtas vai kvadrāta perimetrs. Stunda modelē reizinājumu ar
mainīgo ar nogriežņiem un taisnstūriem un iemāca pierakstu a · b = ab.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         geometrija)

TEMA = "Ko nozīmē 4a?"

MERKIS = ("Paskaidrosim reizinājuma pierakstu ar mainīgo un modelēsim to "
          "ģeometriski.")


def _nog(n, a=2.0):
    p = [("_%d" % i, i * a, 0) for i in range(n + 1)]
    return geometrija(p, nogriezni=[("_0", "_%d" % n)],
                      svitras=[(("_%d" % i, "_%d" % (i + 1)), 1)
                               for i in range(n)],
                      malas=[(("_%d" % i, "_%d" % (i + 1)), "a")
                             for i in range(n)])


SATURS = [
    Sakums("Kvadrāta perimetrs: a + a + a + a = 4a",
           zimejums=geometrija([("A", 0, 0), ("B", 3, 0), ("C", 3, 3),
                                ("D", 0, 3)],
                               nogriezni=["AB", "BC", "CD", "DA"],
                               malas=[("AB", "a"), ("BC", "a"), ("CD", "a"),
                                      ("DA", "a")]),
           paraksts="Četras vienādas malas - 4a.",
           fakti=["4a ir īsāk nekā a + a + a + a.",
                  "Skaitli pie burta sauc par koeficientu.",
                  "Ja a = 5 cm, 4a = 20 cm."]),

    Doma("4a = a + a + a + a",
         "Pieraksts 4a nozīmē 4 · a - četrus saskaitāmos, katrs a. Skaitli 4 "
         "sauc par koeficientu. Reizinājumu ab ģeometriski attēlo kā "
         "taisnstūra laukumu ar malām a un b.",
         soli=[
             "4a - četri nogriežņi a pēc kārtas.",
             "a · 4 raksta kā 4a - skaitli priekšā.",
             "1 · a = a (vieninieku neraksta).",
             "ab - taisnstūra laukums; a · a = a².",
         ],
         pieze="Nejauc: 4a nav «4 un a blakus» kā skaitlī 45. Ja a = 5, "
               "4a = 20, nevis 45."),

    Slidnis("Nogriežņi pēc kārtas", [
        {"v": "a", "teksts": "Viens nogrieznis", "zim": _nog(1)},
        {"v": "2a", "teksts": "a + a", "zim": _nog(2)},
        {"v": "3a", "teksts": "a + a + a", "zim": _nog(3)},
        {"v": "4a", "teksts": "a + a + a + a", "zim": _nog(4)},
    ]),

    Paraugs("Laukums ar burtiem",
            uzd="Taisnstūra malas ir 3 cm un a cm. Uzraksti laukumu un "
                "perimetru.",
            soli=[
                ("S = 3 · a = 3a (cm²)", "Laukums."),
                ("P = 2 · (3 + a) = 2(a + 3) (cm)", "Perimetrs."),
                ("a = 5: S = 15 cm², P = 16 cm", "Pārbaude."),
            ],
            atbilde="S = 3a, P = 2(a + 3)"),

    Varianti("Nozīme", [
        {"jaut": "Ko nozīmē 5x, ja x = 3?",
         "opcijas": ["15", "53", "8", "35"],
         "pareizi": 0, "padoms": "5 · 3."},
        {"jaut": "Kā īsāk uzrakstīt y + y + y?",
         "opcijas": ["3y", "y³", "y + 3", "yyy"],
         "pareizi": 0, "padoms": "Trīs saskaitāmie."},
        {"jaut": "Kurš ir koeficients izteiksmē −7m?",
         "opcijas": ["−7", "7", "m", "−7m"],
         "pareizi": 0, "padoms": "Skaitlis ar zīmi."},
        {"jaut": "Kā pierakstīt b · 6 · a?",
         "opcijas": ["6ab", "b6a", "6 + ab", "ab6"],
         "pareizi": 0, "padoms": "Skaitlis priekšā, burti alfabētiski."},
    ], pamats=4),

    Ievadi("Aprēķini", [
        {"jaut": "4a, ja a = 2,5",
         "atb": ["10"], "padoms": "4 · 2,5."},
        {"jaut": "3ab, ja a = 2, b = 5",
         "atb": ["30"], "padoms": "3 · 2 · 5."},
        {"jaut": "Kāds koeficients izteiksmē x?",
         "atb": ["1"], "padoms": "x = 1 · x."},
        {"jaut": "a², ja a = 7",
         "atb": ["49"], "padoms": "7 · 7."},
    ]),

    Pasaule("Žogs dārzam",
            Ievadi("", [
                {"jaut": "Kvadrātveida dārza mala a m. Žoga garums 4a. "
                         "Cik m, ja a = 12,5?",
                 "atb": ["50"], "padoms": "4 · 12,5."},
                {"jaut": "Žoga metrs maksā 8 €. Cik € par žogu (32a), ja "
                         "a = 12,5?",
                 "atb": ["400"], "padoms": "32 · 12,5."},
                {"jaut": "Dārza laukums a² - cik m²?",
                 "atb": ["156,25"], "padoms": "12,5 · 12,5."},
            ]),
            pavediens="maja",
            konteksts="Būvmateriālu kalkulatori internetā rēķina tieši šādas "
                      "izteiksmes.",
            kapec="4a un a² - perimetrs un laukums."),

    Kopsavilkums([
        "Zinu, ka 4a = a + a + a + a = 4 · a.",
        "Atšķiru koeficientu no mainīgā.",
        "Modelēju ab kā taisnstūra laukumu.",
        "Aprēķinu izteiksmju vērtības.",
    ]),

    Majas([
        "Izmēri galda malu a un uzraksti perimetru ar a.",
        "Uzzīmē modeli izteiksmei 3a + 2b.",
        "Paskaidro, kāpēc 4a ≠ 4 un a blakus.",
    ]),
]
