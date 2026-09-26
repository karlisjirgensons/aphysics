# -*- coding: utf-8 -*-
"""1. klase, 12. stunda: «Ko var salikt no trim figūrām?»

Figūras savieno ar malām un iegūst jaunas: divi trijstūri - kvadrāts vai
lielāks trijstūris, trīs - trapecei līdzīga figūra. Zīmējumā katra daļa
redzama savā krāsā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, geometrija)

TEMA = "Ko var salikt no trim figūrām?"

MERKIS = ("Šodien saliksim jaunas figūras no trijstūriem un kvadrātiem.")


def _saliktas(punkti, dalas):
    """Figūra no daļām: katra daļa iekrāsota pamīšus divās krāsās."""
    return geometrija([("_%s" % k, x, y) for k, (x, y) in punkti.items()],
                      nogriezni=[(("_" + d[i]), ("_" + d[(i + 1) % len(d)]))
                                 for d in dalas for i in range(len(d))],
                      iekrasot=[(["_" + c for c in d], i % 2)
                                for i, d in enumerate(dalas)])


_P = {"A": (0, 0), "B": (4, 0), "C": (4, 4), "D": (0, 4), "E": (8, 0),
      "F": (8, 4), "G": (2, 4), "H": (6, 4)}

_KVADRATS = _saliktas(_P, ["ABC", "ACD"])
_LIELS = _saliktas(_P, ["ABG", "BEH", "BHG"])
_TAISNST = _saliktas(_P, ["ABCD", "BEFC"])

SATURS = [
    Sakums("Divi trijstūri - kas iznāk?",
           zimejums=_KVADRATS,
           paraksts="Divi trijstūri, salikti ar garo malu, - kvadrāts.",
           fakti=["Figūras savieno ar malām.",
                  "No daļām rodas jauna figūra.",
                  "To pašu var salikt dažādi."]),

    Doma("Saliec ar malām",
         "Pieliec figūras vienu otrai tā, lai malas sakrīt, - rodas jauna "
         "figūra.",
         soli=[
             "Izvēlies divas vai trīs figūras.",
             "Pieliec tās ar vienādām malām.",
             "Saskaiti jaunās figūras stūrus un nosauc to.",
         ]),

    Varianti("Kas iznāca?", [
        {"jaut": "No kā salikta šī figūra?", "zim": _KVADRATS,
         "opcijas": ["no 2 trijstūriem", "no 2 kvadrātiem",
                     "no 3 trijstūriem"],
         "pareizi": 0, "padoms": "Saskaiti krāsainās daļas."},
        {"jaut": "No kā salikta šī figūra?", "zim": _TAISNST,
         "opcijas": ["no 2 kvadrātiem", "no 2 trijstūriem",
                     "no 4 kvadrātiem"],
         "pareizi": 0, "padoms": "Divas daļas ar 4 stūriem."},
        {"jaut": "Kā sauc visu lielo figūru?", "zim": _LIELS,
         "opcijas": ["četrstūris", "trijstūris", "piecstūris"],
         "pareizi": 0, "padoms": "Saskaiti lielās figūras stūrus."},
    ]),

    Ievadi("Saskaiti daļas", [
        {"jaut": "Cik trijstūru šajā figūrā?", "zim": _LIELS, "atb": ["3"],
         "padoms": "Skaiti krāsainās daļas."},
        {"jaut": "Cik stūru ir lielajai figūrai?", "zim": _TAISNST,
         "atb": ["4"], "padoms": "Tikai ārējie stūri."},
    ]),

    Petijums("Saliec pats", [
        "Izgriez no papīra 2 kvadrātus un pārgriez tos pa diagonāli.",
        "Saliec no 2 trijstūriem kvadrātu.",
        "Saliec no 2 trijstūriem lielu trijstūri.",
        "Saliec no 3 trijstūriem kaut ko jaunu un nosauc to.",
    ], vajag="papīrs, šķēres (vai tangrams)"),

    Pasaule("Flīzes",
            Ievadi("", [
                {"jaut": "Katru kvadrātflīzi saliek no 2 trijstūriem. Cik "
                         "trijstūru vajag 3 kvadrātiem?", "atb": ["6"],
                 "padoms": "2, 4, 6."},
                {"jaut": "Cik trijstūru vajag 5 kvadrātiem?", "atb": ["10"],
                 "padoms": "Katram kvadrātam 2."},
            ]),
            pavediens="maja",
            konteksts="Meistars liek grīdu no trijstūra flīzēm.",
            kapec="Zinot, no kā figūra salikta, var saskaitīt vajadzīgās "
                  "daļas."),

    Kopsavilkums([
        "Saliku jaunas figūras no dotajām.",
        "Nosaucu, no kā figūra salikta.",
        "Nosaucu jauno figūru pēc stūru skaita.",
    ]),

    Majas([
        "Saliec no grāmatām vai kastītēm lielāku taisnstūri.",
        "Salokot salveti, uztaisi no kvadrāta trijstūri.",
        "Uzzīmē figūru no 3 trijstūriem.",
    ]),
]
