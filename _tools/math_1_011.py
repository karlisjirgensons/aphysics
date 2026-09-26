# -*- coding: utf-8 -*-
"""1. klase, 11. stunda: «Vai vari uzzīmēt taisnu līniju?»

Taisna līnija - ar lineālu vai pa rūtiņu malām. Lauzta līnija sastāv no
vairākiem taisniem gabaliem. No taisnām līnijām rūtiņu lapā zīmē
trijstūrus un četrstūrus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, figura, linijas)

TEMA = "Vai vari uzzīmēt taisnu līniju?"

MERKIS = ("Šodien zīmēsim taisnas līnijas ar lineālu un pa rūtiņām un no "
          "tām - figūras.")

_TAISNA = linijas([(1, 3, 11, 3)], platums=12, augstums=6)
_LAUZTA = linijas([(1, 1, 4, 5), (4, 5, 7, 1), (7, 1, 11, 4)],
                  platums=12, augstums=6)

SATURS = [
    Sakums("Kā uzzīmēt taisnu līniju bez lineāla?",
           zimejums=_TAISNA,
           paraksts="Rūtiņu lapā - pa rūtiņu malu.",
           fakti=["Ar lineālu līnija sanāk taisna.",
                  "Rūtiņu lapā var vilkt pa rūtiņu malu.",
                  "Lauzta līnija sastāv no taisniem gabaliem."]),

    Doma("Kā vilkt ar lineālu",
         "Lineālu tur ar vienu roku, zīmuli velc ar otru - gar lineāla "
         "malu.",
         soli=[
             "Noliec lineālu uz abiem punktiem.",
             "Turi to cieši ar pirkstiem vidū.",
             "Velc zīmuli gar malu no viena punkta līdz otram.",
         ]),

    Varianti("Kāda līnija?", [
        {"jaut": "Kāda ir šī līnija?", "zim": _TAISNA,
         "opcijas": ["taisna", "lauzta"], "jaukt": False, "pareizi": 0,
         "padoms": "Viens taisns gabals."},
        {"jaut": "Kāda ir šī līnija?", "zim": _LAUZTA,
         "opcijas": ["taisna", "lauzta"], "jaukt": False, "pareizi": 1,
         "padoms": "Vairāki gabali ar lūzumiem."},
    ]),

    Ievadi("Saskaiti gabalus", [
        {"jaut": "No cik taisniem gabaliem sastāv lauztā līnija?",
         "zim": _LAUZTA, "atb": ["3"], "padoms": "Skaiti starp lūzumiem."},
        {"jaut": "Cik taisnu līniju vajag trijstūrim?",
         "zim": figura([(0, 0), (5, 0), (0, 4)]), "atb": ["3"],
         "padoms": "Viena katrai malai."},
        {"jaut": "Cik taisnu līniju vajag četrstūrim?",
         "zim": figura([(0, 0), (5, 0), (5, 3), (0, 3)]), "atb": ["4"],
         "padoms": "Viena katrai malai."},
    ]),

    Petijums("Zīmē rūtiņu lapā", [
        "Novelc ar lineālu taisnu līniju 5 rūtiņas garu.",
        "Pa rūtiņu malām uzzīmē četrstūri.",
        "Uzzīmē trijstūri - savieno 3 punktus ar lineālu.",
        "Uzzīmē lauztu līniju no 4 gabaliem.",
    ], vajag="rūtiņu burtnīca, lineāls, zīmulis"),

    Pasaule("Grāmatplaukts",
            Ievadi("", [
                {"jaut": "Tētis zīmē plauktu - taisnstūri - un vēl 2 "
                         "plauktus iekšā. Cik taisnu līniju pavisam?",
                 "zim": linijas([(1, 0, 9, 0), (9, 0, 9, 6), (9, 6, 1, 6),
                                 (1, 6, 1, 0), (1, 2, 9, 2), (1, 4, 9, 4)],
                                platums=10, augstums=6),
                 "atb": ["6"], "padoms": "4 malas un 2 plaukti."},
            ]),
            pavediens="maja",
            konteksts="Pirms plaukta taisīšanas to uzzīmē ar lineālu.",
            kapec="Taisnas līnijas zīmējumā - taisni dēļi īstenībā."),

    Kopsavilkums([
        "Zīmēju taisnu līniju ar lineālu.",
        "Zīmēju pa rūtiņu malām.",
        "Atšķiru taisnu un lauztu līniju.",
    ]),

    Majas([
        "Atrodi mājās 3 taisnas līnijas.",
        "Uzzīmē rūtiņās māju tikai ar taisnām līnijām.",
        "Saskaiti, no cik taisniem gabaliem sastāv tavs zīmējums.",
    ]),
]
