# -*- coding: utf-8 -*-
"""9. klase, 35. stunda: «Kā izskatās prizma ar trapeces pamatu?»

Taisna prizma ar trapeces pamatu: divi vienādi trapeces pamati un četras
taisnstūra sānu skaldnes. Stunda sākas ar lietus noteku un sili -
ķermeņiem, ko skolēns ir redzējis katru dienu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, trapeces_prizma)

TEMA = "Kā izskatās prizma ar trapeces pamatu?"

MERKIS = ("Zīmēsim taisnu prizmu, kuras pamats ir trapece, un raksturosim "
          "to.")

_PRIZMA = trapeces_prizma(8, 4, 3, 5)

SATURS = [
    Sakums("Kāda forma ir lietus notekai un silei?",
           zimejums=_PRIZMA,
           paraksts="Priekšā un aizmugurē - trapeces, sānos - taisnstūri.",
           fakti=["Prizmai ir divi vienādi, paralēli pamati.",
                  "Taisnai prizmai sānu skaldnes ir taisnstūri.",
                  "Trapeces prizmai ir 6 skaldnes, 8 virsotnes, 12 šķautnes."]),

    Doma("Taisna prizma ar trapeces pamatu",
         "Pamati - divas vienādas trapeces; sānu skaldnes - četri taisnstūri; "
         "sānu šķautnes ⊥ pamatiem un ir prizmas augstums.",
         soli=[
             "Uzzīmē priekšējo trapeci.",
             "No katras virsotnes velc vienādas, paralēlas šķautnes slīpi.",
             "Savieno galus - aizmugurējā trapece.",
             "Neredzamās šķautnes zīmē ar punktētu līniju.",
         ]),

    Slidnis("Skaldnes pa vienai", [
        {"v": "Pamati", "teksts": "ABCD un A_1B_1C_1D_1 - vienādas trapeces",
         "zim": _PRIZMA},
        {"v": "Apakša", "teksts": "ABB_1A_1 - taisnstūris ar malu AB",
         "zim": _PRIZMA},
        {"v": "Augša", "teksts": "DCC_1D_1 - taisnstūris ar malu DC",
         "zim": _PRIZMA},
        {"v": "Sāni", "teksts": "ADD_1A_1 un BCC_1B_1 - taisnstūri ar sānu "
                                "malām", "zim": _PRIZMA},
    ], ievads="Atrodi katru skaldni zīmējumā."),

    Varianti("Prizmas elementi", [
        {"jaut": "Cik skaldņu ir trapeces prizmai?",
         "opcijas": ["6", "5", "8", "4"],
         "pareizi": 0, "padoms": "2 pamati + 4 sāni."},
        {"jaut": "Cik šķautņu?",
         "opcijas": ["12", "8", "10", "6"],
         "pareizi": 0, "padoms": "4 + 4 + 4."},
        {"jaut": "Kāda figūra ir sānu skaldne taisnai prizmai?",
         "opcijas": ["Taisnstūris", "Trapece", "Trijstūris", "Rombs"],
         "pareizi": 0, "padoms": "Sānu šķautnes ⊥ pamatam."},
        {"jaut": "Vai divas sānu skaldnes var būt vienādas?",
         "opcijas": ["Jā - vienādsānu trapeces prizmai",
                     "Nē, nekad", "Tikai kubam", "Tikai pamati"],
         "pareizi": 0, "padoms": "Vienādas sānu malas."},
    ]),

    Ievadi("Skaiti un mēri", [
        {"jaut": "Prizmas pamats - trapece ar pamatiem 8 un 4, sānu malām "
                 "5 un 5; prizmas augstums 10. Visu šķautņu garumu summa?",
         "atb": ["84"], "padoms": "2 · 22 + 4 · 10."},
        {"jaut": "Cik virsotņu ir prizmai ar n-stūra pamatu, ja n = 4?",
         "atb": ["8"], "padoms": "2n."},
        {"jaut": "Tās pašas prizmas lielākās sānu skaldnes laukums "
                 "(pamati 8 un 4, augstums 10)?", "atb": ["80"],
         "padoms": "8 · 10."},
    ]),

    Petijums("Uztaisi modeli", [
        "Uz kartona uzzīmē trapeci: pamati 8 cm un 4 cm, sānu malas 5 cm.",
        "Izgriez divas vienādas trapeces.",
        "Izgriez četrus taisnstūrus ar garumu 10 cm un platumu pēc trapeces "
        "malām.",
        "Salīmē prizmu un saskaiti skaldnes, šķautnes, virsotnes.",
    ], vajag="kartons, lineāls, šķēres, līme"),

    Pasaule("Lietus notekas",
            Ievadi("", [
                {"jaut": "Notekas šķērsgriezums - trapece (augšā 12 cm, apakšā "
                         "8 cm). Noteka 6 m gara. Cik m garas ir sānu "
                         "šķautnes?", "atb": ["6"],
                 "padoms": "Prizmas augstums = garums."},
                {"jaut": "Cik skaldņu notekai būtu, ja tai nebūtu augšējās "
                         "(vaļējas)?", "atb": ["5"], "padoms": "6 − 1."},
            ]),
            pavediens="maja",
            konteksts="Jumta notekas bieži ir trapeces prizmas bez augšējās "
                      "skaldnes.",
            kapec="Prizmas pamats nosaka, cik ūdens tā var aizvadīt."),

    Kopsavilkums([
        "Zīmēju prizmu ar trapeces pamatu.",
        "Nosaucu pamatus, sānu skaldnes, šķautnes.",
        "Skaitu skaldnes, šķautnes un virsotnes.",
    ]),

    Majas([
        "Atrodi mājās trapeces prizmu (kaste, sile, dēlis ar nošķeltām "
        "malām).",
        "Uzzīmē to un atzīmē neredzamās šķautnes.",
        "Izmēri tās šķautnes un pieraksti.",
    ]),
]
