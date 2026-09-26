# -*- coding: utf-8 -*-
"""4. klase, 60. stunda: «Vai malu pagarināšana maina leņķi?»

Bieža nepareizā priekšstata atspēkošana: «lielāks zīmējums - lielāks
leņķis». Divi leņķi ar vienādu atvērumu, bet dažāda garuma malām, ir
vienādi. Skolēns to pārbauda ar transportieri un pamato: leņķis ir
pagrieziens, nevis attālums.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, lenkis)

TEMA = "Vai malu pagarināšana maina leņķi?"

MERKIS = ("Secināsim, ka leņķa lielums nemainās, pagarinot tā malas, un "
          "pamatosim to.")

SATURS = [
    Sakums("Kurš leņķis lielāks?",
           zimejums=lenkis([(0, ""), (40, "40°")], loki=[(0, 40, "")],
                           r=34),
           paraksts="Mazais un lielais zīmējums - abi 40°.",
           fakti=["Daudzi domā, ka garākas malas nozīmē lielāku leņķi.",
                  "Transportieris abos gadījumos rāda 40°."]),

    Doma("Leņķis ir pagrieziens, nevis attālums",
         "Pagarinot malas, virziens nemainās - tāpēc leņķa lielums paliek "
         "tas pats.",
         soli=[
             "Izmēri leņķi ar transportieri.",
             "Pagarini abas malas ar lineālu.",
             "Izmēri vēlreiz - skaitlis tas pats.",
             "Secinājums: leņķi nosaka malu virziens, nevis garums.",
         ],
         pieze="Tāpat palielināmais stikls palielina figūru, bet ne tās "
               "leņķus."),

    Slidnis("Malas aug, leņķis ne",
            soli=[
                {"v": "40°", "teksts": "Īsas malas.",
                 "zim": lenkis([(0, ""), (40, "")], loki=[(0, 40, "40°")],
                               r=14)},
                {"v": "40°", "teksts": "Garākas malas.",
                 "zim": lenkis([(0, ""), (40, "")], loki=[(0, 40, "40°")],
                               r=24)},
                {"v": "40°", "teksts": "Vēl garākas - leņķis tas pats.",
                 "zim": lenkis([(0, ""), (40, "")], loki=[(0, 40, "40°")],
                               r=34)},
            ],
            ievads="Skaties uz skaitli - vai tas mainās?"),

    Varianti("Vai leņķis mainās?", [
        {"jaut": "Leņķa malas pagarina 3 reizes. Leņķis...",
         "opcijas": ["nemainās", "3 reizes lielāks", "3 reizes mazāks"],
         "pareizi": 0, "padoms": "Virziens tas pats."},
        {"jaut": "Fotogrāfiju palielina. Mājas jumta leņķis attēlā...",
         "opcijas": ["nemainās", "palielinās", "samazinās"], "pareizi": 0,
         "padoms": "Palielina tikai garumus."},
        {"jaut": "Kas notiek ar nogriezni, ja to pagarina?",
         "opcijas": ["garums palielinās", "nemainās", "samazinās"],
         "pareizi": 0, "padoms": "Nogrieznim - mainās."},
        {"jaut": "Kurš apgalvojums pareizs?",
         "opcijas": ["Leņķa lielums nav atkarīgs no malu garuma",
                     "Lielākam zīmējumam - lielāks leņķis",
                     "Īsām malām leņķis vienmēr šaurs"], "pareizi": 0,
         "padoms": "Atceries eksperimentu."},
    ], pamats=4),

    Ievadi("Izmēri un secini", [
        {"jaut": "Leņķis ar 3 cm malām ir 55°. Cik grādu, ja malas 9 cm?",
         "atb": ["55"], "padoms": "Nemainās."},
        {"jaut": "Trijstūra leņķis 60°. Trijstūri palielina divreiz. Cik "
                 "grādu tagad?", "atb": ["60"], "padoms": "Leņķi nemainās."},
        {"jaut": "Kvadrāta leņķi ir 90°. Cik grādu ir lielā kvadrāta leņķi?",
         "atb": ["90"], "padoms": "Visi kvadrāti - 90°."},
        {"jaut": "Palielinātā kartē nogrieznis bija 2 cm, tagad 3 reizes "
                 "garāks. Cik cm?", "atb": ["6"], "padoms": "2 · 3."},
    ]),

    Pasaule("Kartes un planšetes tālummaiņa",
            Varianti("", [
                {"jaut": "Karti telefonā tuvina. Ielu krustojuma leņķis...",
                 "opcijas": ["paliek tāds pats", "kļūst lielāks",
                             "kļūst mazāks"], "pareizi": 0,
                 "padoms": "Mainās mērogs, ne virziens."},
                {"jaut": "Attālums līdz veikalam kartē pēc tuvināšanas...",
                 "opcijas": ["izskatās garāks", "paliek tāds pats",
                             "izskatās īsāks"], "pareizi": 0,
                 "padoms": "Garumi palielinās."},
                {"jaut": "Kāpēc tuvināta karte joprojām «pareiza»?",
                 "opcijas": ["leņķi nemainās, garumi aug vienādi",
                             "nekas nemainās", "mainās tikai krāsas"],
                 "pareizi": 0, "padoms": "Forma saglabājas."},
            ]),
            pavediens="celojums",
            konteksts="Tuvinot karti, ielas kļūst garākas, bet krustojumu "
                      "leņķi paliek tādi paši.",
            kapec="Tāpēc karti var tuvināt un nenomaldīties."),

    Petijums("Pagarini un izmēri",
             soli=[
                 "Uzzīmē leņķi ar 3 cm garām malām.",
                 "Izmēri to ar transportieri.",
                 "Pagarini abas malas līdz 10 cm.",
                 "Izmēri vēlreiz un salīdzini.",
             ],
             vajag="lineāls, transportieris",
             secinajums="Leņķa lielums pēc pagarināšanas nemainījās."),

    Kopsavilkums([
        "Zinu, ka leņķa lielums nav atkarīgs no malu garuma.",
        "Pamatoju to ar eksperimentu.",
        "Atšķiru, kas mainās garumam un kas - leņķim.",
    ]),

    Majas([
        "Nofotografē durvju stūri tuvu un tālu: vai leņķis mainās?",
        "Uzzīmē mazu un lielu kvadrātu un izmēri to leņķus.",
        "Pastāsti kādam, kāpēc leņķis nemainās, pagarinot malas.",
    ]),
]
