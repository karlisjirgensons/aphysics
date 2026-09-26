# -*- coding: utf-8 -*-
"""4. klase, 67. stunda: «Kāds četrstūris sanāks?»

Nosacījumi par malām un leņķiem nosaka četrstūra veidu: 4 taisni leņķi -
taisnstūris, arī vienādas malas - kvadrāts, viens paralēlu malu pāris -
trapece, divi pāri - paralelograms. Skolēns zīmē rūtiņās pēc nosacījumiem
un nosauc, kas sanāca.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, figura, restis)

TEMA = "Kāds četrstūris sanāks?"

MERKIS = ("Zīmēsim daudzstūri, ievērojot nosacījumus par malu novietojumu "
          "un leņķu veidiem.")

SATURS = [
    Sakums("Kas kopīgs pūķim, durvīm un galda virsmai?",
           zimejums=restis([["četrstūris", "paralēli pāri", "taisni leņķi"],
                            ["kvadrāts", "2", "4"],
                            ["taisnstūris", "2", "4"],
                            ["paralelograms", "2", "0"],
                            ["trapece", "1", "0, 1 vai 2"]],
                           "četrstūru ģimene"),
           fakti=["Visi ir četrstūri - bet ar dažādām īpašībām.",
                  "Nosacījumi par malām un leņķiem pasaka, kurš tas ir."]),

    Doma("Nosacījumi nosaka veidu",
         "Četrstūra veidu nosaka, cik tam ir paralēlu malu pāru un kādi ir "
         "leņķi.",
         soli=[
             "Divi paralēlu malu pāri - paralelograms.",
             "Paralelograms ar 4 taisniem leņķiem - taisnstūris.",
             "Taisnstūris ar vienādām malām - kvadrāts.",
             "Tikai viens paralēlu malu pāris - trapece.",
         ],
         pieze="Katrs kvadrāts ir taisnstūris, katrs taisnstūris - "
               "paralelograms, bet ne otrādi."),

    Zimejums("Paralelograms rūtiņās",
             figura([(1, 1), (8, 1), (10, 5), (3, 5)],
                    uzraksti=[(4.5, 0.4, "7"), (6.5, 5.6, "7")],
                    platums=11, augstums=6),
             paskaidro="Pretējās malas paralēlas un vienādas, bet leņķi nav "
                       "taisni.",
             ievads="Divi paralēlu malu pāri, nav taisnu leņķu."),

    Paraugs("Zīmē pēc nosacījumiem",
            uzd="Uzzīmē četrstūri ar diviem taisniem leņķiem un tieši vienu "
                "paralēlu malu pāri.",
            soli=[
                ("apakšā 6 rūtiņas, kreisā mala uz augšu 4", "Divi taisni "
                 "leņķi apakšā kreisajā un augšā kreisajā."),
                ("augšējā mala 3 rūtiņas, paralēla apakšējai", None),
                ("labā mala slīpa", "Tātad tikai viens paralēlu pāris."),
            ],
            atbilde="taisnleņķa trapece"),

    Varianti("Kas tas ir?", [
        {"jaut": "4 taisni leņķi, visas malas 5 cm",
         "opcijas": ["kvadrāts", "trapece", "paralelograms bez taisniem "
                     "leņķiem"], "pareizi": 0,
         "padoms": "Taisni leņķi un vienādas malas."},
        {"jaut": "4 taisni leņķi, malas 5 cm un 3 cm",
         "opcijas": ["taisnstūris", "kvadrāts", "trapece"], "pareizi": 0,
         "padoms": "Malas dažādas."},
        {"jaut": "Tikai viens paralēlu malu pāris",
         "opcijas": ["trapece", "taisnstūris", "kvadrāts"], "pareizi": 0,
         "padoms": "Trapeces pazīme."},
        {"jaut": "Divi paralēlu malu pāri, nav taisnu leņķu",
         "opcijas": ["paralelograms", "kvadrāts", "trapece"], "pareizi": 0,
         "padoms": "«Šķības kastes» forma."},
        {"jaut": "Vai četrstūrim var būt tieši 3 taisni leņķi?",
         "opcijas": ["nē", "jā"], "pareizi": 0,
         "padoms": "Ja 3 ir taisni, arī ceturtais sanāk taisns."},
    ], pamats=3),

    Ievadi("Malu garumi un perimetri", [
        {"jaut": "Paralelograma malas 7 un 4. Perimetrs?", "atb": ["22"],
         "padoms": "7 + 4 + 7 + 4."},
        {"jaut": "Kvadrāta perimetrs 36. Mala?", "atb": ["9"],
         "padoms": "36 : 4."},
        {"jaut": "Trapeces malas 6, 3, 4, 5. Perimetrs?", "atb": ["18"],
         "padoms": "Saskaiti visas."},
        {"jaut": "Taisnstūra perimetrs 24, mala 8. Otra mala?", "atb": ["4"],
         "padoms": "24 : 2 = 12; 12 − 8."},
    ]),

    Pasaule("Parka celiņu plānošana",
            Varianti("", [
                {"jaut": "Dārzniekam vajag dobi ar 4 taisniem stūriem un "
                         "vienādām malām. Kāda forma?",
                 "opcijas": ["kvadrāts", "trapece", "paralelograms"],
                 "pareizi": 0, "padoms": "Abi nosacījumi kopā."},
                {"jaut": "Celiņš starp divām paralēlām ielām, bet viens gals "
                         "slīps. Kāda forma?",
                 "opcijas": ["trapece", "kvadrāts", "taisnstūris"],
                 "pareizi": 0, "padoms": "Viens paralēlu pāris."},
                {"jaut": "Stāvvietas vieta ar slīpām līnijām, abas malu "
                         "pāri paralēli. Kāda forma?",
                 "opcijas": ["paralelograms", "trapece", "kvadrāts"],
                 "pareizi": 0, "padoms": "Slīpa, bet divi pāri."},
            ]),
            pavediens="maja",
            konteksts="Ainavu arhitekti izvēlas četrstūrus pēc vajadzības: "
                      "slīpas stāvvietas, taisnas dobes.",
            kapec="Pareizais nosaukums ātri pasaka visas īpašības."),

    Kopsavilkums([
        "Zīmēju četrstūri pēc nosacījumiem par malām un leņķiem.",
        "Nosaucu: kvadrāts, taisnstūris, paralelograms, trapece.",
        "Zinu, ka kvadrāts ir arī taisnstūris un paralelograms.",
    ]),

    Majas([
        "Uzzīmē rūtiņās visus četrus četrstūru veidus.",
        "Atrodi mājās vismaz 2 četrstūru veidus.",
        "Izdomā nosacījumu, pēc kura sanāk tikai kvadrāts.",
    ]),
]
