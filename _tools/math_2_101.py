# -*- coding: utf-8 -*-
"""2. klase, 101. stunda: «Vai figūras ir vienādas?»

Divas figūras ir vienādas, ja, uzliekot vienu virsū otrai, tās pilnīgi
sakrīt - arī tad, ja viena ir pagriezta. Rūtiņu lapā vienādu figūru zīmē,
skaitot rūtiņas katrai malai.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, figura)

TEMA = "Vai figūras ir vienādas?"

MERKIS = ("Šodien pārbaudīsim figūru vienādību, tās savietojot, un "
          "zīmēsim vienādu figūru rūtiņu lapā.")

_L1 = figura([(0, 0), (4, 0), (4, 1), (1, 1), (1, 3), (0, 3)])
_L2 = figura([(0, 0), (3, 0), (3, 4), (2, 4), (2, 1), (0, 1)])
_L3 = figura([(0, 0), (4, 0), (4, 1), (1, 1), (1, 4), (0, 4)])

SATURS = [
    Sakums("Vai šīs divas «L» figūras ir vienādas?",
           zimejums=_L1,
           paraksts="Pagriez to - vai sakrīt ar otru?",
           fakti=["Vienādas figūras savietojot pilnīgi sakrīt.",
                  "Figūru drīkst pagriezt vai apgriezt.",
                  "Rūtiņu lapā vienādību pārbauda, skaitot rūtiņas."]),

    Doma("Vienādas figūras",
         "Figūras ir vienādas, ja tās var novietot vienu uz otras tā, ka "
         "tās sakrīt.",
         soli=[
             "Izgriez vienu figūru un uzliec uz otras.",
             "Ja nesakrīt - pagriez vai apgriez.",
             "Rūtiņās: salīdzini katras malas garumu rūtiņās.",
             "Vienādām figūrām ir vienāds rūtiņu skaits.",
         ]),

    Varianti("Vienādas vai nē?", [
        {"jaut": "Vai šī figūra ir vienāda ar sākuma «L»?", "zim": _L2,
         "opcijas": ["Jā - tā ir pagriezta", "Nē"], "jaukt": False,
         "pareizi": 0, "padoms": "Garā mala 4, īsā 3, platums 1."},
        {"jaut": "Vai šī figūra ir vienāda ar sākuma «L»?", "zim": _L3,
         "opcijas": ["Jā", "Nē - tā ir augstāka"], "jaukt": False,
         "pareizi": 1, "padoms": "Saskaiti rūtiņas augšup: 4, nevis 3."},
        {"jaut": "Divi kvadrāti ar malu 3 rūtiņas. Vienādi?",
         "opcijas": ["Jā", "Nē"], "jaukt": False, "pareizi": 0,
         "padoms": "Vienādas malas - sakrīt."},
        {"jaut": "Kvadrāts ar malu 3 rūtiņas un taisnstūris 1 rūtiņu plats, 9 garš. Vienādi?",
         "opcijas": ["Nē, lai gan rūtiņu skaits vienāds", "Jā"],
         "jaukt": False, "pareizi": 0, "padoms": "Forma atšķiras."},
    ]),

    Ievadi("Saskaiti rūtiņas", [
        {"jaut": "Cik rūtiņu ir šajā figūrā?", "zim": _L1, "atb": ["6"],
         "padoms": "4 apakšā un 2 augšup."},
        {"jaut": "Cik rūtiņu šajā?", "zim": _L2, "atb": ["6"],
         "padoms": "3 apakšā un 3 augšup."},
        {"jaut": "Cik rūtiņu šajā?", "zim": _L3, "atb": ["7"],
         "padoms": "4 apakšā un 3 augšup."},
        {"jaut": "Par cik rūtiņām pēdējā figūra lielāka?", "atb": ["1"],
         "padoms": "7 − 6."},
    ]),

    Petijums("Uzzīmē vienādu", [
        "Rūtiņu lapā uzzīmē jebkuru figūru no 5 rūtiņām.",
        "Blakus uzzīmē tai vienādu, bet pagrieztu.",
        "Izgriez abas un pārbaudi, uzliekot vienu uz otras.",
    ], vajag="rūtiņu lapa, šķēres"),

    Pasaule("Puzles gabaliņi",
            Varianti("", [
                {"jaut": "Grīdas flīzes jāliek bez spraugām. Kādām tām jābūt?",
                 "opcijas": ["vienādām", "dažādām", "apaļām"],
                 "pareizi": 0, "padoms": "Lai katra sakristu ar nākamo."},
            ]),
            pavediens="maja",
            konteksts="Flīzes un parketu gatavo vienādos gabalos.",
            kapec="Vienādas figūras var salikt ciešā rakstā."),

    Kopsavilkums([
        "Pārbaudu vienādību, savietojot figūras.",
        "Zinu, ka figūru drīkst pagriezt.",
        "Zīmēju vienādu figūru rūtiņu lapā.",
    ]),

    Majas([
        "Atrodi mājās divus vienādus priekšmetus - flīzes, šķīvjus.",
        "Kā pārbaudīt, ka tie vienādi?",
        "Uzzīmē rūtiņās divas vienādas figūras.",
    ]),
]
