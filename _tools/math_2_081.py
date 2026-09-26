# -*- coding: utf-8 -*-
"""2. klase, 81. stunda: «Vai iekavas maina rezultātu?»

20 − (5 + 7) = 8, bet 20 − 5 + 7 = 22. Iekavas ap summu, ko atņem, maina
rezultātu; turpretī 20 + (5 + 7) = 20 + 5 + 7. Skolēns pēta, kad iekavas
ietekmē un kad ne.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, sloksnes)

TEMA = "Vai iekavas maina rezultātu?"

MERKIS = ("Šodien salīdzināsim 20 − (5 + 7) un 20 − 5 + 7 un paskaidrosim "
          "atšķirību.")

_MAINA = ["maina", "nemaina"]

SATURS = [
    Sakums("20 − (5 + 7) un 20 − 5 + 7 - tie paši skaitļi. Vai rezultāts "
           "tas pats?",
           zimejums=sloksnes([("20", 20, "20"), ("atņem", 12, "5 + 7")],
                             starpiba=True),
           paraksts="20 − (5 + 7): atņem visu 12 - paliek 8.",
           fakti=["20 − (5 + 7) = 20 − 12 = 8.",
                  "20 − 5 + 7 = 15 + 7 = 22.",
                  "Iekavas mainīja rezultātu par 14!"]),

    Doma("Kad iekavas ir svarīgas",
         "Ja pirms iekavām ir «−», iekavas parasti maina rezultātu.",
         soli=[
             "«+» pirms iekavām: 20 + (5 + 7) = 20 + 5 + 7.",
             "«−» pirms iekavām ar summu: atņem abus.",
             "20 − (5 + 7) = 20 − 5 − 7 - abi ar mīnusu.",
             "Pārbaudi, aprēķinot abus.",
         ]),

    Slidnis("Salīdzinām", [
        {"v": "20 + (5 + 7) = 32", "teksts": "Tas pats kā 20 + 5 + 7."},
        {"v": "20 − (5 + 7) = 8", "teksts": "Tas pats kā 20 − 5 − 7."},
        {"v": "20 − 5 + 7 = 22", "teksts": "Cits rezultāts."},
    ]),

    Varianti("Vai iekavas maina?", [
        {"jaut": "30 + (10 + 5) un 30 + 10 + 5", "opcijas": _MAINA,
         "jaukt": False, "pareizi": 1, "padoms": "Abas 45."},
        {"jaut": "30 − (10 + 5) un 30 − 10 + 5", "opcijas": _MAINA,
         "jaukt": False, "pareizi": 0, "padoms": "15 un 25."},
        {"jaut": "(30 − 10) + 5 un 30 − 10 + 5", "opcijas": _MAINA,
         "jaukt": False, "pareizi": 1, "padoms": "Iekavas jau pirmās."},
        {"jaut": "30 − (10 − 5) un 30 − 10 − 5", "opcijas": _MAINA,
         "jaukt": False, "pareizi": 0, "padoms": "25 un 15."},
    ]),

    Ievadi("Aprēķini abas", [
        {"jaut": "50 − (15 + 5) = ?", "atb": ["30"], "padoms": "50 − 20."},
        {"jaut": "50 − 15 + 5 = ?", "atb": ["40"], "padoms": "35 + 5."},
        {"jaut": "Par cik atšķiras rezultāti?", "atb": ["10"],
         "padoms": "40 − 30."},
        {"jaut": "Kur jāliek iekavas, lai 40 − 10 + 20 būtu 10? Raksti "
                 "vērtību iekavās.", "atb": ["30"], "padoms": "40 − (10 + 20)."},
    ]),

    Pasaule("Kā nesajaukt?",
            Varianti("", [
                {"jaut": "Bija 40 €. Nopirka bumbu 10 € un tīklu 20 €. Kura "
                         "izteiksme dod atlikumu?",
                 "opcijas": ["40 − (10 + 20) = 10", "40 − 10 + 20 = 50"],
                 "jaukt": False, "pareizi": 0,
                 "padoms": "Abi pirkumi jāatņem."},
            ]),
            pavediens="veikals",
            konteksts="Bez iekavām rēķins izskatītos pēc naudas pieauguma.",
            kapec="Iekavas apvieno visus tēriņus."),

    Kopsavilkums([
        "Salīdzinu izteiksmes ar iekavām un bez.",
        "Zinu, ka «−» pirms iekavām maina rezultātu.",
        "Ieliku iekavas, lai iegūtu vajadzīgo vērtību.",
    ]),

    Majas([
        "Aprēķini 60 − (20 + 10) un 60 − 20 + 10.",
        "Paskaidro atšķirību mājiniekam ar naudas piemēru.",
        "Izdomā izteiksmi, kur iekavas neko nemaina.",
    ]),
]
