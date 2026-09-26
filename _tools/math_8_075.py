# -*- coding: utf-8 -*-
"""8. klase, 75. stunda: «Kā telpisku ķermeni attēlo plaknē?»

Paralēlā projekcija: priekšējā skaldne īstajā formā, dziļums slīpi un
īsāk, paralēlas šķautnes paliek paralēlas, neredzamās - punktētas.
Slīdnis rāda pazīstamos ķermeņus tieši tā uzzīmētus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, kermenis)

TEMA = "Kā telpisku ķermeni attēlo plaknē?"

MERKIS = ("Paskaidrosim, kas saglabājas, attēlojot telpisku ķermeni plaknē, "
          "un zīmēsim prizmu.")

SATURS = [
    Sakums("Kā uz plakanas lapas parādīt kasti?",
           zimejums=kermenis("kvadrs"),
           paraksts="Priekšējā skaldne - īstajā formā, dziļums - slīpi un "
                    "īsāk.",
           fakti=["Paralēlas šķautnes zīmējumā paliek paralēlas.",
                  "Neredzamās šķautnes zīmē ar punktētu līniju.",
                  "Dziļumā garumi un leņķi mainās - tā ir skice, ne mērogs."]),

    Doma("Kas saglabājas, kas mainās",
         "Zīmējumā saglabājas paralēlums un priekšējās skaldnes forma.",
         soli=[
             "Uzzīmē priekšējo skaldni īstajā formā.",
             "No katras virsotnes velc paralēlas slīpas līnijas dziļumā - "
             "parasti 45° leņķī un uz pusi īsākas.",
             "Savieno galus - iegūst aizmugurējo skaldni.",
             "Neredzamās šķautnes pārvelc ar punktētu līniju.",
         ]),

    Slidnis("Pazīstami ķermeņi", [
        {"v": "Kubs", "teksts": "Sānu skaldne izskatās kā paralelograms",
         "zim": kermenis("kubs")},
        {"v": "Kvadrs", "teksts": "Trīs punktētas šķautnes aizmugurē",
         "zim": kermenis("kvadrs")},
        {"v": "Trijstūra prizma", "teksts": "Priekšā - trijstūris īstajā "
                                            "formā",
         "zim": kermenis("prizma")},
        {"v": "Cilindrs", "teksts": "Riņķi izskatās kā elipses",
         "zim": kermenis("cilindrs")},
    ]),

    Paraugs("Uzzīmē kvadru",
            uzd="Uzzīmē kvadru 4 cm × 3 cm × 2 cm.",
            soli=[
                ("Taisnstūris 4 cm × 3 cm", "Priekšējā skaldne."),
                ("Četras slīpas līnijas pa 1 cm 45° leņķī", "Dziļums 2 cm - "
                                                            "uz pusi īsāk."),
                ("Savieno galus", "Aizmugurējā skaldne."),
                ("Trīs šķautnes punktētas", "Tās, kas slēpjas aiz kastes."),
            ],
            atbilde="Kvadra skice ar redzamām un punktētām šķautnēm"),

    Ievadi("Saskaiti un aprēķini", [
        {"jaut": "Cik šķautņu ir trijstūra prizmai?", "atb": ["9"],
         "padoms": "3 + 3 + 3."},
        {"jaut": "Cik virsotņu ir trijstūra prizmai?", "atb": ["6"],
         "padoms": "Divi trijstūri."},
        {"jaut": "Cik skaldņu ir trijstūra prizmai?", "atb": ["5"],
         "padoms": "2 pamati + 3 sāni."},
        {"jaut": "Cik kvadra šķautņu zīmējumā ir punktētas?", "atb": ["3"],
         "padoms": "Tās satiekas aizmugurējā stūrī."},
    ]),

    Varianti("Spried", [
        {"jaut": "Kā zīmē neredzamās šķautnes?",
         "opcijas": ["Ar punktētu līniju", "Nezīmē vispār",
                     "Ar treknu līniju", "Ar citu krāsu"],
         "pareizi": 0, "padoms": "Tā redz, ka ķermenis ir telpisks."},
        {"jaut": "Kas saglabājas zīmējumā?",
         "opcijas": ["Šķautņu paralēlums", "Visi leņķi", "Visi garumi",
                     "Skaldņu laukumi"],
         "pareizi": 0, "padoms": "Dziļums sagriež leņķus."},
        {"jaut": "Kuba sānu skaldne zīmējumā izskatās kā...",
         "opcijas": ["paralelograms", "kvadrāts", "trijstūris", "riņķis"],
         "pareizi": 0, "padoms": "Slīpās šķautnes."},
    ]),

    Pasaule("Skapja skice",
            Ievadi("", [
                {"jaut": "Skapis 80 cm × 180 cm × 50 cm, mērogs 1 : 20. "
                         "Priekšpuses platums zīmējumā (cm)?",
                 "atb": ["4"], "padoms": "80 : 20."},
                {"jaut": "Priekšpuses augstums zīmējumā (cm)?", "atb": ["9"],
                 "padoms": "180 : 20."},
                {"jaut": "Dziļumu zīmē uz pusi īsāku. Cik cm?",
                 "atb": ["1,25"], "padoms": "50 : 20 : 2."},
            ]),
            pavediens="maja",
            konteksts="Mēbeļu skicēs priekšpuse ir īstā formā, bet dziļums "
                      "- slīpi un īsāk.",
            kapec="Skice parāda formu; precīzus izmērus raksta ar "
                  "skaitļiem."),

    Kopsavilkums([
        "Zinu, kas saglabājas, zīmējot ķermeni plaknē.",
        "Zīmēju kvadru un prizmu ar punktētām neredzamām šķautnēm.",
        "Saskaitu prizmas virsotnes, šķautnes un skaldnes.",
    ]),

    Majas([
        "Uzzīmē savu skolas somu vai kasti kā kvadru.",
        "Uzzīmē trijstūra prizmu ar punktētām šķautnēm.",
        "Uzzīmē vienu ķermeni divreiz: ar dziļumu pa kreisi un pa labi.",
    ]),
]
