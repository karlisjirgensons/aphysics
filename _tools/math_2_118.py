# -*- coding: utf-8 -*-
"""2. klase, 118. stunda: «Ko nozīmē «divreiz vairāk»?»

«Divreiz vairāk» nozīmē: tikpat un vēl tikpat. Modelis - divas vienādas
sloksnes blakus vai divreiz garāka sloksne. Tas atšķiras no «par 2 vairāk»,
un šo atšķirību vēl pētīs 133. stundā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, sloksnes)

TEMA = "Ko nozīmē «divreiz vairāk»?"

MERKIS = ("Šodien modelēsim doto daudzumu un divreiz lielāku daudzumu ar "
          "priekšmetiem vai sloksnēm.")

SATURS = [
    Sakums("Annai 4 konfektes, brālim divreiz vairāk. Cik brālim?",
           zimejums=sloksnes([("Anna", 4, "4"), ("brālis", 8, "?")]),
           paraksts="Brālim tikpat un vēl tikpat: 4 + 4 = 8.",
           fakti=["Divreiz vairāk - divas reizes tikpat.",
                  "4 divreiz ir 4 + 4 = 8.",
                  "Sloksne kļūst divreiz garāka."]),

    Doma("Divreiz vairāk",
         "Divreiz vairāk nozīmē saskaitīt skaitli pašu ar sevi.",
         soli=[
             "Paņem doto daudzumu.",
             "Noliec blakus vēl tikpat.",
             "Saskaiti: 4 + 4 = 8.",
             "Pārbaudi: garākā sloksne ir divas īsās.",
         ]),

    Slidnis("Divreiz garāk", [
        {"v": "3", "teksts": "Sloksne 3 rūtiņas.",
         "zim": sloksnes([("dotā", 3, "3")])},
        {"v": "3 + 3", "teksts": "Divreiz garāka: 6 rūtiņas.",
         "zim": sloksnes([("dotā", 3, "3"), ("divreiz", 6, "6")])},
        {"v": "5 + 5", "teksts": "No 5 - divreiz ir 10.",
         "zim": sloksnes([("dotā", 5, "5"), ("divreiz", 10, "10")])},
    ]),

    Ievadi("Divreiz vairāk", [
        {"jaut": "Divreiz vairāk nekā 6 ir?", "atb": ["12"],
         "padoms": "6 + 6."},
        {"jaut": "Divreiz vairāk nekā 9 ir?", "atb": ["18"],
         "padoms": "9 + 9."},
        {"jaut": "Divreiz vairāk nekā 10 ir?", "atb": ["20"],
         "padoms": "10 + 10."},
        {"jaut": "Divreiz vairāk nekā 25 ir?", "atb": ["50"],
         "padoms": "25 + 25."},
        {"jaut": "Divreiz vairāk nekā 40 ir?", "atb": ["80"],
         "padoms": "40 + 40."},
        {"jaut": "Divreiz vairāk nekā 15 ir?", "atb": ["30"],
         "padoms": "15 + 15."},
    ], pamats=4),

    Varianti("Kura sloksne divreiz garāka?", [
        {"jaut": "Dotā sloksne 4. Kura ir divreiz garāka?",
         "opcijas": ["8", "6", "4"], "pareizi": 0, "padoms": "4 + 4."},
        {"jaut": "Ja Toms ir divreiz vecāks nekā māsa, kurai 4 gadi?",
         "opcijas": ["8 gadi", "6 gadi", "2 gadi"], "pareizi": 0,
         "padoms": "4 + 4."},
    ]),

    Pasaule("Receptes dubultošana",
            Ievadi("", [
                {"jaut": "Pankūkām vajag 2 olas un 5 ēdamkarotes miltu. "
                         "Gatavo divreiz vairāk. Cik olu?", "atb": ["4"],
                 "padoms": "2 + 2."},
                {"jaut": "Cik ēdamkarotes miltu?", "atb": ["10"],
                 "padoms": "5 + 5."},
            ]),
            pavediens="virtuve",
            konteksts="Ciemiņu ir daudz, tāpēc receptē visu ņem divreiz.",
            kapec="Dubultojot jādubulto katra sastāvdaļa."),

    Kopsavilkums([
        "Zinu, ka «divreiz vairāk» - tikpat un vēl tikpat.",
        "Modelēju to ar sloksnēm.",
        "Aprēķinu divreiz lielāku daudzumu.",
    ]),

    Majas([
        "Noliec uz galda dažas karotes un blakus divreiz vairāk dakšiņu.",
        "Saskaiti abus.",
        "Kas vēl mājās ir divreiz vairāk nekā kaut kas cits?",
    ]),
]
