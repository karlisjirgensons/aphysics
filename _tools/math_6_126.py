# -*- coding: utf-8 -*-
"""6. klase, 126. stunda: «Kā saskaitīšanu parādīt ar bultiņām?»

Modelis, kas izskaidro visu turpmāko. Vērsts nogrieznis rāda gan skaitļa
lielumu, gan zīmi, un divu bultiņu salikšana ir tieši saskaitīšana. Pēc šīs
stundas likumu par summas zīmi vairs nav jāiegaumē.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kā saskaitīšanu parādīt ar bultiņām?"

MERKIS = ("Modelēsim saskaitīšanu uz skaitļu taisnes ar vērstiem "
          "nogriežņiem.")

SATURS = [
    Sakums("Bultiņa rāda gan cik, gan uz kurieni",
           zimejums=taisne(-8, 6, 2, [(0, "sākums"), (-2, "rezultāts")],
                           bultas=[(0, 4, "+4"), (4, -2, "−6")]),
           paraksts="No nulles četri soļi pa labi, tad seši pa kreisi: "
                    "4 + (−6) = −2.",
           fakti=["Bultiņas garums ir skaitļa modulis.",
                  "Bultiņas virziens ir skaitļa zīme.",
                  "Saskaitīt nozīmē likt bultiņas vienu aiz otras."]),

    Doma("Liec bultiņas vienu aiz otras",
         "Saskaitīšanu modelē, sākot no nulles un liekot bultiņas citu aiz "
         "citas; kur beidzas pēdējā, tur ir summa.",
         soli=[
             "Sāc no nulles.",
             "Pirmajam saskaitāmajam uzzīmē bultiņu: garums - modulis, "
             "virziens - zīme.",
             "No tās gala zīmē otro bultiņu.",
             "Nolasi, kur beidzas pēdējā bultiņa.",
             "Pieraksti summu.",
         ],
         pieze="Ja abas bultiņas ir vienā virzienā, tās saskaitās un summa "
               "ir garāka par abām. Ja pretējos - tās daļēji izlīdzinās, un "
               "summa ir īsāka."),

    Paraugs("Divas bultiņas",
            uzd="Parādi ar bultiņām 4 + (−6).",
            soli=[
                ("No nulles četri soļi pa labi",
                 "Pirmā bultiņa - uz 4."),
                ("No 4 seši soļi pa kreisi",
                 "Otrā bultiņa ir garāka."),
                ("Beidzas pie −2",
                 "Tur ir summa."),
                ("4 + (−6) = −2",
                 "Otrā bultiņa bija garāka, tāpēc summa ir negatīva."),
            ],
            atbilde="−2"),

    Ievadi("Nolasi no bultiņām", [
        {"jaut": "Cik ir 4 + (−6)?",
         "atb": ["-2", "−2"], "padoms": "Otrā bultiņa garāka."},
        {"jaut": "Cik ir −3 + 5?",
         "atb": ["2"], "padoms": "Pieci soļi pa labi no −3."},
        {"jaut": "Cik ir −2 + (−5)?",
         "atb": ["-7", "−7"], "padoms": "Abas bultiņas pa kreisi."},
        {"jaut": "Cik ir 7 + (−7)?",
         "atb": ["0"], "padoms": "Bultiņas izlīdzinās."},
        {"jaut": "Cik ir −8 + 3?",
         "atb": ["-5", "−5"], "padoms": "Trīs soļi pa labi."},
        {"jaut": "Cik ir −1 + (−9)?",
         "atb": ["-10", "−10"], "padoms": "Abas pa kreisi."},
    ], pamats=4),

    Varianti("Ko rāda bultiņas?", [
        {"jaut": "Bultiņas garums rāda...",
         "opcijas": ["skaitļa moduli", "skaitļa zīmi",
                     "summu", "darbību"],
         "pareizi": 0,
         "padoms": "Cik soļu."},
        {"jaut": "Bultiņas virziens rāda...",
         "opcijas": ["skaitļa zīmi", "skaitļa moduli",
                     "summu", "iekavas"],
         "pareizi": 0,
         "padoms": "Pa labi vai pa kreisi."},
        {"jaut": "Ja abas bultiņas ir vērstas pa kreisi, summa ir...",
         "opcijas": ["negatīva", "pozitīva", "nulle", "nevar zināt"],
         "pareizi": 0,
         "padoms": "Abi soļi vienā virzienā."},
        {"jaut": "Ja bultiņas ir pretējos virzienos un vienāda garuma, summa "
                 "ir...",
         "opcijas": ["nulle", "negatīva", "pozitīva", "dubulta"],
         "pareizi": 0,
         "padoms": "Tās izlīdzinās."},
    ], pamats=4),

    Pasaule("Kā kustas lifts?",
            Ievadi("", [
                {"jaut": "Lifts no 0 paceļas par 4 stāviem, tad nolaižas par "
                         "6. Kurā stāvā tas ir?",
                 "atb": ["-2", "−2"], "padoms": "4 + (−6)."},
                {"jaut": "No −2 tas paceļas par 5 stāviem. Kurā stāvā?",
                 "atb": ["3"], "padoms": "−2 + 5."},
                {"jaut": "No 3 tas nolaižas par 3 stāviem. Kurā stāvā?",
                 "atb": ["0"], "padoms": "Pretēji skaitļi."},
                {"jaut": "Cik stāvu lifts kopā nobraucis, skaitot visus "
                         "posmus (4 + 6 + 5 + 3)?",
                 "atb": ["18"], "padoms": "Moduļu summa, ne rezultāts."},
            ]),
            pavediens="maja",
            konteksts="Lifts nobrauc garu ceļu, bet var atgriezties tur, kur "
                      "sācis - ceļš un rezultāts nav viens un tas pats.",
            kapec="Bultiņu garumu summa ir ceļš, bultiņu gals - rezultāts."),

    Zimejums("Abas bultiņas vienā virzienā",
             taisne(-10, 2, 2, [(0, "sākums"), (-7, "rezultāts")],
                    bultas=[(0, -2, "−2"), (-2, -7, "−5")]),
             paskaidro="−2 + (−5) = −7. Abas bultiņas ir pa kreisi, tāpēc "
                       "summa ir garāka par abām.",
             ievads="Otrs gadījums: abi saskaitāmie negatīvi."),

    Kopsavilkums([
        "Modelēju saskaitīšanu ar vērstiem nogriežņiem.",
        "Zinu, ka bultiņas garums ir modulis, virziens - zīme.",
        "Nolasu summu no bultiņu gala.",
        "Paskaidroju, kad summa ir garāka un kad īsāka par saskaitāmajiem.",
    ]),

    Majas([
        "Uzzīmē bultiņas izteiksmei −6 + 4.",
        "Uzzīmē bultiņas izteiksmei −6 + (−4).",
        "Pieraksti, ar ko abi zīmējumi atšķiras.",
    ]),
]
