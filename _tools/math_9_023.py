# -*- coding: utf-8 -*-
"""9. klase, 23. stunda: «Kā konstruēt trapeci?»

Konstrukcijas atslēga: ja no trapeces «izgriež» paralelogramu, paliek
trijstūris ar malām c, d un a − b. Trijstūri konstruēt prot jau 7. klasē,
paralelogramu pieliek ar paralēli.
"""

from math_saturs import (TRAPECES_MALAS, Doma, Ievadi, Kopsavilkums, Majas,
                         Pasaule, Petijums, Sakums, Slidnis, Varianti,
                         geometrija)

TEMA = "Kā konstruēt trapeci?"

MERKIS = ("Konstruēsim trapeci pēc dotiem elementiem ar cirkuli un lineālu.")

# Pamati a = 9, b = 4, sānu malas AD = 4, BC = 3 (trijstūris 4, 3, 5 -
# taisnleņķa pie D', tāpēc koordinātes ir veselas).
_P = {"A": (0, 0), "E": (5, 0), "B": (9, 0), "D": (3.2, 2.4),
      "C": (7.2, 2.4)}


def _solis(n):
    vardi = {1: "AE", 2: "AED", 3: "AEDB", 4: "AEDBC"}[n]
    punkti = [(v,) + _P[v] for v in vardi]
    nogr = [("A", "E")]
    izc = []
    if n >= 2:
        nogr += ["AD", "DE"]
    if n >= 3:
        nogr.append("EB")
    if n >= 4:
        izc += ["DC", "CB"]
    return geometrija(punkti, nogriezni=nogr, izcelti=izc)


SATURS = [
    Sakums("Dots: pamati 9 un 4, sānu malas 4 un 3",
           zimejums=geometrija([(v,) + _P[v] for v in "ABCDE"],
                               nogriezni=TRAPECES_MALAS, izcelti=["DE"],
                               iekrasot=[("AED", 1)]),
           paraksts="DE ∥ CB - no trapeces izgriezts trijstūris AED.",
           fakti=["Trijstūra AED malas: 4, 3 un 9 − 4 = 5.",
                  "Trijstūri konstruē pēc trim malām.",
                  "Pēc tam pieliek paralelogramu EBCD."]),

    Slidnis("Konstrukcija pa soļiem", [
        {"v": "1", "teksts": "Atliek AE = a − b = 5.", "zim": _solis(1)},
        {"v": "2", "teksts": "Ar cirkuli: AD = 4 no A, ED = 3 no E. "
                             "Trijstūris AED.", "zim": _solis(2)},
        {"v": "3", "teksts": "Pagarina AE par EB = b = 4.", "zim": _solis(3)},
        {"v": "4", "teksts": "Caur D velk paralēli AB, atliek DC = 4; "
                             "savieno C ar B.", "zim": _solis(4)},
    ]),

    Doma("Konstrukcijas plāns",
         "Trapeci konstruē, sākot ar trijstūri, kura malas ir sānu malas un "
         "pamatu starpība.",
         soli=[
             "Skicē gatavu trapeci un atzīmē doto.",
             "Atrodi trijstūri, ko var konstruēt uzreiz.",
             "Konstruē to, tad pabeidz trapeci ar paralēli.",
             "Pārbaudi: vai iegūtajai figūrai ir visi dotie elementi?",
         ],
         pieze="Ja c + d ≤ a − b, trijstūris neveidojas - tādas trapeces nav."),

    Petijums("Konstruē pats", [
        "Dots: pamati 10 cm un 4 cm, sānu malas 5 cm un 7 cm.",
        "Aprēķini a − b un konstruē trijstūri.",
        "Pabeidz trapeci ar paralēli.",
        "Izmēri leņķus un pārbaudi ∠A + ∠D = 180°.",
    ], vajag="cirkulis, lineāls, trijstūris, transportieris"),

    Varianti("Vai trapeci var konstruēt?", [
        {"jaut": "Pamati 8 un 3, sānu malas 2 un 2.",
         "opcijas": ["Nē: 2 + 2 < 5", "Jā", "Tikai vienādsānu",
                     "Jā, taisnleņķa"],
         "pareizi": 0, "padoms": "Trijstūrim 2, 2, 5."},
        {"jaut": "Pamati 7 un 3, sānu malas 3 un 5.",
         "opcijas": ["Jā - trijstūris 3, 5, 4", "Nē", "Tikai paralelograms",
                     "Nevar zināt"],
         "pareizi": 0, "padoms": "3 + 4 > 5."},
        {"jaut": "Kurš elements vajadzīgs vienādsānu trapecei (pamati "
                 "zināmi)?",
         "opcijas": ["Viena sānu mala", "Abas diagonāles", "Nekas",
                     "Perimetrs un laukums"],
         "pareizi": 0, "padoms": "Otra ir tāda pati."},
    ]),

    Ievadi("Palīgtrijstūris", [
        {"jaut": "Pamati 12 un 5. Palīgtrijstūra trešā mala?", "atb": ["7"],
         "padoms": "12 − 5."},
        {"jaut": "Vienādsānu trapece, pamati 10 un 4, sānu mala 5. "
                 "Palīgtrijstūra perimetrs?", "atb": ["16"],
         "padoms": "5 + 5 + 6."},
        {"jaut": "Pamati 9 un 3, sānu malas 3 un x. Mazākais vesels x?",
         "atb": ["4"], "padoms": "3 + x > 6."},
    ]),

    Pasaule("Puķu dobes veidne",
            Ievadi("", [
                {"jaut": "Dobe - trapece ar pamatiem 3 m un 1,6 m, sānu "
                         "malas 1,2 m un 1 m. Palīgtrijstūra garākā mala (m)?",
                 "atb": ["1,4"], "padoms": "3 − 1,6."},
                {"jaut": "Cik m apmales vajag visai dobei?", "atb": ["6,8"],
                 "padoms": "3 + 1,6 + 1,2 + 1."},
            ]),
            pavediens="maja",
            konteksts="Dārznieks ar auklu un mietiņiem uz zemes konstruē tieši "
                      "tāpat kā ar cirkuli uz papīra.",
            kapec="Aukla ir cirkulis, taisns dēlis - lineāls."),

    Kopsavilkums([
        "Plānoju konstrukciju ar palīgtrijstūri.",
        "Konstruēju trapeci ar cirkuli un lineālu.",
        "Pārbaudu, vai konstrukcija iespējama.",
    ]),

    Majas([
        "Konstruē vienādsānu trapeci: pamati 8 cm un 4 cm, sānu mala 3 cm.",
        "Konstruē taisnleņķa trapeci: pamati 6 cm un 3 cm, augstums 4 cm.",
        "Izdomā datus, ar kuriem trapeci konstruēt nevar.",
    ]),
]
