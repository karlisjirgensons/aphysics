# -*- coding: utf-8 -*-
"""9. klase, 17. stunda: «Kā plānot risinājumu?»

Garākā uzdevumā vispirms plāns, tad rēķini: skice, dotais un meklējamais,
kurš trijstūris ir līdzīgs kuram un kādā secībā atrast lielumus. Plāns
tiek sastādīts pirms pirmā skaitļa.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, geometrija)

TEMA = "Kā plānot risinājumu?"

MERKIS = ("Veidosim skici un plānosim risinājuma soļus uzdevumam ar "
          "līdzību.")

_ZIM = geometrija([("A", 0, 0), ("B", 9, 0), ("C", 3, 6), ("D", 3, 0),
                   ("E", 5, 4)],
                  nogriezni=["AB", "BC", "CA"], izcelti=["DE"],
                  iekrasot=[("ADEC", 1)],
                  malas=[("DB", "4"), ("AD", "2"), ("DE", "5"),
                         ("BE", "4,5")])

SATURS = [
    Sakums("Kur sākt, ja jautā četras lietas?",
           zimejums=_ZIM,
           paraksts="DE ∥ AC. Atrodi četrstūra ADEC perimetru.",
           fakti=["Perimetram vajag AD, DE, EC un CA.",
                  "Zināmi ir tikai AD un DE.",
                  "EC un CA dod līdzība - plāns ir gatavs."]),

    Doma("Plāns pirms rēķiniem",
         "Sāc no jautājuma un ej atpakaļ: kas vajadzīgs atbildei, un no kā to "
         "var iegūt?",
         soli=[
             "Skice: atzīmē doto un meklējamo.",
             "Pieraksti formulu atbildei (P = ...).",
             "Katram nezināmajam atrodi, no kā to iegūt.",
             "Tikai tad rēķini - soli pa solim.",
             "Pārbaudi ticamību un mērvienības.",
         ]),

    Slidnis("Plāns sakuma uzdevumam", [
        {"v": "Jautājums", "teksts": "P = AD + DE + EC + CA; nezināmi EC, CA",
         "zim": _ZIM},
        {"v": "Līdzība", "teksts": "△DBE ∼ △ABC: ∠B kopīgs, ∠BDE = ∠BAC",
         "zim": _ZIM},
        {"v": "CA", "teksts": "{CA|5} = {6|4} ⇒ CA = 7,5",
         "zim": _ZIM},
        {"v": "EC", "teksts": "{BC|4,5} = {6|4} ⇒ BC = 6,75; EC = 2,25",
         "zim": _ZIM},
        {"v": "Atbilde", "teksts": "P = 2 + 5 + 2,25 + 7,5 = 16,75",
         "zim": _ZIM},
    ]),

    Varianti("Sakārto plānu", [
        {"jaut": "Kurš solis ir pirmais?",
         "opcijas": ["Uzzīmēt skici un atzīmēt doto",
                     "Sastādīt proporciju", "Aprēķināt k",
                     "Uzrakstīt atbildi"],
         "pareizi": 0, "padoms": "Bez skices nav, ko plānot."},
        {"jaut": "Kas jādara pirms proporcijas?",
         "opcijas": ["Pamatot līdzību", "Noapaļot", "Aprēķināt laukumu",
                     "Neko"],
         "pareizi": 0, "padoms": "Proporcija ir līdzības sekas."},
        {"jaut": "Pēdējais solis ir...",
         "opcijas": ["pārbaude un atbilde ar mērvienību",
                     "skice", "līdzības pamatojums", "dotā pierakstīšana"],
         "pareizi": 0, "padoms": "Vai rezultāts ir ticams?"},
    ]),

    Ievadi("Izpildi plānu", [
        {"jaut": "DE ∥ AC, BD = 3, DA = 3, DE = 4. AC = ?", "atb": ["8"],
         "padoms": "k = 2."},
        {"jaut": "Tas pats; BE = 3,5. EC = ?", "atb": ["3,5"],
         "padoms": "BC = 7."},
        {"jaut": "Četrstūra ADEC perimetrs = ?", "atb": ["18,5"],
         "padoms": "3 + 4 + 3,5 + 8."},
        {"jaut": "Ja △DBE laukums ir 5, △ABC laukums = ?", "atb": ["20"],
         "padoms": "k^2 = 4."},
        {"jaut": "Četrstūra ADEC laukums = ?", "atb": ["15"],
         "padoms": "20 − 5."},
    ], pamats=3),

    Pasaule("Galda virsma no trijstūra",
            Ievadi("", [
                {"jaut": "No trijstūra finiera (pamats 1,2 m) nozāģē virsotni "
                         "pa līniju ∥ pamatam, pusē augstuma. Cik m gara ir "
                         "zāģējuma līnija?", "atb": ["0,6"],
                 "padoms": "Viduslīnija."},
                {"jaut": "Trijstūra laukums 0,48 m². Cik m² paliek galda "
                         "virsmai?", "atb": ["0,36"],
                 "padoms": "Nozāģēts ceturtdaļa."},
            ]),
            pavediens="maja",
            konteksts="Galdnieks plāno griezumu, pirms zāģē - tāpat kā "
                      "risinājumu plāno pirms rēķina.",
            kapec="Nogrieztais trijstūris ir līdzīgs visam ar k = 0,5."),

    Kopsavilkums([
        "Sāku ar skici un jautājumu.",
        "Sastādu plānu: ko un no kā iegūt.",
        "Rēķinu pa soļiem un pārbaudu.",
    ]),

    Majas([
        "Sastādi plānu (bez rēķiniem) uzdevumam: DE ∥ AC, zināmi BD, DA, BE, "
        "DE; atrast ADEC perimetru.",
        "Izpildi plānu ar BD = 6, DA = 2, BE = 9, DE = 3.",
        "Pārbaudi atbildi ar zīmējumu mērogā.",
    ]),
]
