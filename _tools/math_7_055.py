# -*- coding: utf-8 -*-
"""7. klase, 55. stunda: «Kuras sakarības nav funkcijas?»

Grafikā funkciju atpazīst ar vertikālās taisnes pārbaudi: ja kāda
vertikāla taisne krusto līniju vairāk nekā vienā punktā, tai x ir vairākas
vērtības - tā nav funkcija. Riņķa līnija un vertikāla taisne nav funkcijas.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, Zimejums, plakne, rinkis)

TEMA = "Kuras sakarības nav funkcijas?"

MERKIS = ("Minēsim piemērus sakarībām, kas nav funkcijas, un pamatosim "
          "izvēli.")

SATURS = [
    Sakums("Riņķa līnija nav funkcija",
           zimejums=rinkis(diametrs="d"),
           paraksts="Vertikāla taisne caur centru krusto to divos punktos.",
           fakti=["Vienam x - divi y: augšā un apakšā.",
                  "Tāpēc riņķa līnija nav funkcijas grafiks.",
                  "Pusriņķa līnija (tikai augšējā) - ir."]),

    Doma("Vertikālās taisnes pārbaude",
         "Līnija koordinātu plaknē ir funkcijas grafiks tad un tikai tad, ja "
         "katra vertikāla taisne to krusto ne vairāk kā vienā punktā.",
         soli=[
             "Iedomājies vertikālu taisni, kas slīd no kreisās uz labo.",
             "Katrā vietā saskaiti krustpunktus ar līniju.",
             "Ja kaut kur ir 2 vai vairāk - nav funkcija.",
             "Pretpiemērs: norādi to x un abus y.",
         ],
         pieze="Horizontāla taisne y = 3 ir funkcija (katram x viens y = 3). "
               "Vertikāla taisne x = 3 nav funkcija."),

    Zimejums("x = 3 - nav funkcija",
             plakne(grafiki=[([(3, -3), (3, 4)], "x = 3")],
                    punkti=[(3, 1), (3, -2)],
                    no_x=-2, lidz_x=5, no_y=-3, lidz_y=4, solis=1),
             paskaidro="Argumentam 3 atbilst visi y: 1, −2, ..."),

    Paraugs("Pamato ar pretpiemēru",
            uzd="Sakarība: y ir skaitlis, kura modulis ir x. Vai tā ir "
                "funkcija?",
            soli=[
                ("Paņem x = 5", "Kāds konkrēts arguments."),
                ("|5| = 5 un |−5| = 5", "Der y = 5 un y = −5."),
                ("Vienam x - divi y", "Pretpiemērs."),
            ],
            atbilde="Nav funkcija: x = 5 atbilst y = 5 un y = −5."),

    Varianti("Funkcija vai nē?", [
        {"jaut": "Horizontāla taisne y = −2",
         "opcijas": ["Funkcija", "Nav funkcija"],
         "pareizi": 0, "jaukt": False,
         "padoms": "Vertikāla taisne to krusto vienreiz."},
        {"jaut": "Vertikāla taisne x = −2",
         "opcijas": ["Funkcija", "Nav funkcija"],
         "pareizi": 1, "jaukt": False,
         "padoms": "Vienam x - visi y."},
        {"jaut": "Parabola y = x²",
         "opcijas": ["Funkcija", "Nav funkcija"],
         "pareizi": 0, "jaukt": False,
         "padoms": "Katram x viens kvadrāts."},
        {"jaut": "Burts «S», uzzīmēts koordinātu plaknē",
         "opcijas": ["Funkcija", "Nav funkcija"],
         "pareizi": 1, "jaukt": False,
         "padoms": "Vertikāla taisne to krusto trīs vietās."},
    ], pamats=4),

    Pasaule("Metro vilcienu kustības grafiks",
            Varianti("", [
                {"jaut": "Grafikā «laiks - vieta» vilciens pie stacijas "
                         "stāv 2 min (horizontāls posms). Vai tā ir "
                         "funkcija?",
                 "opcijas": ["Jā - katrā brīdī vilciens ir vienā vietā",
                             "Nē - vilciens stāv",
                             "Nē - horizontāla līnija nav funkcija",
                             "Nevar zināt"],
                 "pareizi": 0,
                 "padoms": "Katram laikam viena vieta."},
                {"jaut": "Grafikā «vieta - laiks» (otrādi) tas pats "
                         "vilciens. Vai tā ir funkcija?",
                 "opcijas": ["Nē - stacijas vietai atbilst vairāki laiki",
                             "Jā, vienmēr", "Jā, ja vilciens ātrs",
                             "Nevar zināt"],
                 "pareizi": 0,
                 "padoms": "Stāvot vilciens ir vienā vietā vairākus brīžus."},
                {"jaut": "Vai vilciens var būt divās vietās vienlaikus?",
                 "opcijas": ["Nē - tāpēc vieta ir laika funkcija",
                             "Jā", "Tikai metro", "Tikai naktī"],
                 "pareizi": 0,
                 "padoms": "Fizika to neļauj."},
            ]),
            pavediens="celojums",
            konteksts="Vilcienu dispečeri zīmē grafikus «laiks - vieta»; tie "
                      "vienmēr ir funkcijas.",
            kapec="Ne katra sakarība otrādi ir funkcija."),

    Kopsavilkums([
        "Lietoju vertikālās taisnes pārbaudi.",
        "Minu piemērus sakarībām, kas nav funkcijas.",
        "Pamatoju ar konkrētu pretpiemēru.",
        "Zinu, ka x = a nav funkcija, bet y = b ir.",
    ]),

    Majas([
        "Uzzīmē 3 līnijas: 2 funkcijas un 1, kas nav funkcija.",
        "Kuri lielie drukātie burti var būt funkcijas grafiks?",
        "Paskaidro, kāpēc riņķa līnija nav funkcija.",
    ]),
]
