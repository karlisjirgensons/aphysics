# -*- coding: utf-8 -*-
"""2. klase, 68. stunda: «Kā saplānot pasākumu?»

Tēmas noslēgums: pasākuma laika plāns. Katram posmam ir ilgums, un
nākamais sākas, kad iepriekšējais beidzas. Visu posmu summai jāietilpst
pieejamajā laikā - to pārbauda, saskaitot.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, laiks, restis)

TEMA = "Kā saplānot pasākumu?"

MERKIS = ("Šodien sastādīsim vienkāršu pasākuma laika plānu un "
          "pārbaudīsim, vai laiks pietiek.")

_BALLITE = restis([["posms", "ilgums", "sākums"],
                   ["apsveikšana", "15 min", "14:00"],
                   ["spēles", "40 min", "14:15"],
                   ["torte", "20 min", "?"],
                   ["dejas", "30 min", "?"]])

SATURS = [
    Sakums("Klases ballītei ir 2 stundas. Vai viss paspēsies?",
           zimejums=_BALLITE,
           paraksts="Nākamais posms sākas, kad iepriekšējais beidzas.",
           fakti=["Pasākums sastāv no posmiem.",
                  "Katram posmam ir ilgums.",
                  "Visiem kopā jāietilpst pieejamajā laikā."]),

    Doma("Laika plāns",
         "Nākamā posma sākums = iepriekšējā sākums + ilgums.",
         soli=[
             "Uzraksti posmus pēc kārtas.",
             "Katram ieraksti ilgumu.",
             "Aprēķini katra sākumu.",
             "Saskaiti ilgumus un salīdzini ar pieejamo laiku.",
         ]),

    Ievadi("Aizpildi plānu", [
        {"jaut": "Cikos sākas torte?", "zim": _BALLITE,
         "atb": laiks(14, 55), "padoms": "14:15 + 40 min."},
        {"jaut": "Cikos sākas dejas?", "zim": _BALLITE,
         "atb": laiks(15, 15), "padoms": "14:55 + 20 min."},
        {"jaut": "Cikos beidzas dejas?", "zim": _BALLITE,
         "atb": laiks(15, 45), "padoms": "15:15 + 30 min."},
        {"jaut": "Cik minūšu ilgst viss pasākums?", "zim": _BALLITE,
         "atb": ["105"], "mers": "min", "padoms": "15 + 40 + 20 + 30."},
    ]),

    Varianti("Vai pietiek laika?", [
        {"jaut": "Ballītei ir 2 h (120 min). Plāns aizņem 105 min. Vai "
                 "pietiek?", "opcijas": ["Jā, paliek 15 min", "Nē"],
         "jaukt": False, "pareizi": 0, "padoms": "120 − 105."},
        {"jaut": "Ko var pievienot atlikušajām 15 min?",
         "opcijas": ["mīklu minēšanu 10 min", "filmu 45 min",
                     "ekskursiju 1 h"], "pareizi": 0,
         "padoms": "Jāietilpst 15 minūtēs."},
    ]),

    Petijums("Mūsu pasākuma plāns", [
        "Grupā izvēlieties pasākumu: ballīte, sporta diena, izstāde.",
        "Uzrakstiet 4-5 posmus un to ilgumus.",
        "Aprēķiniet katra posma sākumu.",
        "Pārbaudiet, vai viss ietilpst 1 h 30 min.",
    ], vajag="lapa tabulai, pulkstenis"),

    Pasaule("Dzimšanas dienas svinības",
            Ievadi("", [
                {"jaut": "Ciemiņi nāk 12:00. Pusdienas 45 min, spēles "
                         "50 min. Cikos beigsies spēles?",
                 "atb": laiks(13, 35), "padoms": "12:00 + 45 + 50."},
                {"jaut": "Ciemiņiem jābrauc mājās 14:00. Cik minūšu "
                         "paliek tortei?", "atb": ["25"], "mers": "min",
                 "padoms": "No 13:35 līdz 14:00."},
            ]),
            pavediens="maja",
            konteksts="Plānojot svinības, saskaita posmu ilgumus.",
            kapec="Labs plāns - viss paspēts un neviens nesteidzas."),

    Kopsavilkums([
        "Sastādu pasākuma laika plānu.",
        "Aprēķinu katra posma sākumu.",
        "Pārbaudu, vai laiks pietiek.",
    ]),

    Majas([
        "Kopā ar ģimeni saplāno sestdienas rītu.",
        "Pieraksti posmus un ilgumus.",
        "Vai viss ietilpa līdz pusdienām?",
    ]),
]
