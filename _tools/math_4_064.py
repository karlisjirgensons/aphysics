# -*- coding: utf-8 -*-
"""4. klase, 64. stunda: «Kā pagriezt staru par leņķi?»

Pagrieziens ap punktu - leņķis kustībā. Pulksteņa minūšu rādītājs ik
minūti pagriežas par 6°, tāpēc 15 minūtēs - par 90°. Stunda sasaista leņķi
ar laiku un virzienu (pulksteņa rādītāja virzienā vai pretēji).
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas,
                         Paraugs, Pasaule, Sakums, Slidnis, Varianti, lenkis)

TEMA = "Kā pagriezt staru par leņķi?"

MERKIS = ("Pagriezīsim staru ap punktu par doto leņķi un veidosim "
          "zīmējumu.")

SATURS = [
    Sakums("Par cik grādiem pagriežas minūšu rādītājs?",
           zimejums=lenkis([(90, "12"), (0, "3")], loki=[(0, 90, "90°")]),
           paraksts="No 12 līdz 3 - ceturtdaļa apļa, 90°.",
           fakti=["Stundā minūšu rādītājs apiet 360°.",
                  "Vienā minūtē - 360 : 60 = 6°."]),

    Doma("Pagrieziens: centrs, virziens, leņķis",
         "Lai pagrieztu staru, jāzina centrs (ap ko griež), virziens (kā "
         "pulksteņa rādītājs vai pretēji) un leņķis.",
         soli=[
             "Stara sākumpunkts - pagrieziena centrs.",
             "Transportiera nulli liec uz sākotnējā stara.",
             "Atzīmē vajadzīgos grādus izvēlētajā virzienā.",
             "Novelc jauno staru - tas ir pagrieztais.",
         ],
         pieze="Pagriežot par 360°, stars atgriežas sākumā."),

    Paraugs("Rādītājs 20 minūtēs",
            uzd="Par cik grādiem pagriežas minūšu rādītājs 20 minūtēs?",
            soli=[
                ("1 min → 6°", "360 : 60."),
                ("20 · 6 = 120", None),
            ],
            atbilde="120°"),

    Slidnis("Rādītājs griežas",
            soli=[
                {"v": "0 min → 0°", "teksts": "Sākums pie 12.",
                 "zim": lenkis([(90, "12")])},
                {"v": "5 min → 30°", "teksts": "Pie 1.",
                 "zim": lenkis([(90, "12"), (60, "1")], loki=[(60, 90, "")])},
                {"v": "15 min → 90°", "teksts": "Pie 3.",
                 "zim": lenkis([(90, "12"), (0, "3")], loki=[(0, 90, "")])},
                {"v": "30 min → 180°", "teksts": "Pie 6.",
                 "zim": lenkis([(90, "12"), (270, "6")],
                               loki=[(270, 450, "")])},
            ],
            ievads="Rādītājs griežas pulksteņa virzienā."),

    Kustiba("Aizgriez rādītāju", [
        {"jaut": "Par cik grādiem pagriežas minūšu rādītājs 10 minūtēs?",
         "atb": 60, "beigas": 360, "iedala": 30, "mers": "grādi",
         "merkis": "10 min", "objekts": "Rādītājs",
         "padoms": "10 · 6.",
         "stasts": "Skala ir pulksteņa aplis, iztaisnots līnijā."},
        {"jaut": "Un 45 minūtēs?",
         "atb": 270, "beigas": 360, "iedala": 30, "mers": "grādi",
         "merkis": "45 min", "objekts": "Rādītājs",
         "padoms": "45 · 6."},
        {"jaut": "Stundas rādītājs stundā pagriežas par 30°. Cik 4 stundās?",
         "atb": 120, "beigas": 360, "iedala": 30, "mers": "grādi",
         "merkis": "4 h", "objekts": "Rādītājs",
         "padoms": "4 · 30."},
        {"jaut": "Minūšu rādītājs 50 minūtēs?",
         "atb": 300, "beigas": 360, "iedala": 30, "mers": "grādi",
         "merkis": "50 min", "objekts": "Rādītājs",
         "padoms": "50 · 6."},
    ], pamats=2,
        ievads="Izrēķini grādus un palaid."),

    Varianti("Kurp būs vērsts?", [
        {"jaut": "Rādītājs pie 12 pagriežas par 90° pulksteņa virzienā. Kur "
                 "tas rāda?",
         "opcijas": ["uz 3", "uz 9", "uz 6", "uz 12"], "pareizi": 0,
         "padoms": "Ceturtdaļa apļa pa labi."},
        {"jaut": "Rādītājs pie 12 pagriežas par 90° pretēji pulksteņa "
                 "virzienam.",
         "opcijas": ["uz 9", "uz 3", "uz 6", "uz 12"], "pareizi": 0,
         "padoms": "Pa kreisi."},
        {"jaut": "Pagrieziens par 360° - kur rāda stars?",
         "opcijas": ["tur pat, kur sākumā", "pretēji", "perpendikulāri"],
         "pareizi": 0, "padoms": "Pilns aplis."},
        {"jaut": "Pagrieziens par 180° no 12:",
         "opcijas": ["uz 6", "uz 3", "uz 9", "uz 12"], "pareizi": 0,
         "padoms": "Pretējā puse."},
    ], pamats=4),

    Ievadi("Grādi un minūtes", [
        {"jaut": "Cik minūtēs minūšu rādītājs pagriežas par 90°?",
         "atb": ["15"], "padoms": "90 : 6."},
        {"jaut": "Cik minūtēs par 180°?", "atb": ["30"],
         "padoms": "180 : 6."},
        {"jaut": "Par cik grādiem pagriežas stundas rādītājs no 12 līdz 3?",
         "atb": ["90"], "padoms": "3 · 30."},
        {"jaut": "Kāds leņķis starp rādītājiem plkst. 2.00?",
         "atb": ["60"], "padoms": "2 · 30."},
    ]),

    Pasaule("Vēja turbīnas lāpstiņas",
            Ievadi("", [
                {"jaut": "Turbīnai 3 lāpstiņas vienādi. Cik grādu starp "
                         "blakus lāpstiņām?",
                 "atb": ["120"], "padoms": "360 : 3."},
                {"jaut": "Turbīna minūtē apgriežas 15 reizes. Cik grādu tā "
                         "pagriežas minūtē?",
                 "atb": ["5400"], "padoms": "15 · 360."},
                {"jaut": "Par cik grādiem jāpagriež lāpstiņa, lai tā nonāktu "
                         "nākamās lāpstiņas vietā?",
                 "atb": ["120"], "padoms": "Leņķis starp lāpstiņām."},
                {"jaut": "Cik reižu jāpagriež par 120°, lai būtu pilns aplis?",
                 "atb": ["3"], "padoms": "360 : 120."},
            ]),
            pavediens="planeta",
            konteksts="Vēja turbīnu lāpstiņas stāv 120° cita no citas - tā "
                      "turbīna griežas vienmērīgi.",
            kapec="Pagriezienu leņķi ir vēja enerģijas pamatā."),

    Kopsavilkums([
        "Pagriežu staru ap punktu par doto leņķi.",
        "Zinu, ka minūšu rādītājs minūtē pagriežas par 6°.",
        "Nošķiru pagriezienu pulksteņa virzienā un pretēji.",
    ]),

    Majas([
        "Pavēro pulksteni 15 minūtes un pārbaudi, vai rādītājs pagriezās "
        "par 90°.",
        "Uzzīmē staru un pagriez to par 45°, 90° un 180°.",
        "Izrēķini leņķi starp rādītājiem plkst. 4.00.",
    ]),
]
