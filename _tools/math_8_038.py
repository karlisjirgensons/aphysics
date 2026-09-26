# -*- coding: utf-8 -*-
"""8. klase, 38. stunda: «Kāpēc mērījums nav precīzs?»

Temata sākums. Katrs mērījums ir tuvinājums: mērinstrumenta skalai ir
mazākā iedaļa, un starp iedaļām acs tikai min. Stundā nosaka iedaļas
vērtību dažādām skalām - tā ir pirmā lieta, ko nolasa no jebkura instrumenta.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, Zimejums, taisne)

TEMA = "Kāpēc mērījums nav precīzs?"

MERKIS = ("Sapratīsim, ka mērījumā iegūst tuvinājumu, un noteiksim "
          "mērinstrumenta iedaļas vērtību.")

SATURS = [
    Sakums("Cik garš ir zīmulis?",
           zimejums=taisne(0, 20, 1, [(17.4, "?")], sikas=2),
           paraksts="Zīmuļa gals ir starp 17 un 17,5 cm.",
           fakti=["Viens saka 17,3 cm, otrs - 17,4 cm.",
                  "Abi mēra pareizi - lineāls neļauj precīzāk.",
                  "Katrs mērījums ir tuvinājums."]),

    Doma("Iedaļas vērtība",
         "Iedaļas vērtība c ir, cik mērvienību atbilst vienam mazākajam "
         "skalas solim. Tā nosaka, cik precīzi var nomērīt.",
         soli=[
             "Izvēlies divas blakus iedaļas ar skaitļiem, piemēram, 10 un 20.",
             "Atņem: 20 − 10 = 10.",
             "Saskaiti mazos intervālus starp tām, piemēram, 5.",
             "Iedaļas vērtība c = 10 : 5 = 2 mērvienības.",
         ],
         pieze="Tāpat kā dabaszinībās, mērījuma kļūdu šajā kursā ņem vienādu "
               "ar iedaļas vērtību: Δx = c."),

    Paraugs("Termometra iedaļa",
            uzd="Starp atzīmēm 20 °C un 30 °C ir 5 intervāli. Kāda ir "
                "iedaļas vērtība?",
            soli=[
                ("30 − 20 = 10 °C", "Starp atzīmēm."),
                ("c = {10 °C|5} = 2 °C", "Dala ar intervālu skaitu."),
            ],
            atbilde="c = 2 °C"),

    Zimejums("Nolasi skalu",
             taisne(0, 50, 10, [(34, "•")], sikas=5),
             paskaidro="Starp 0 un 10 ir 5 intervāli - c = 2. Punkts rāda 34."),

    Ievadi("Nosaki iedaļas vērtību", [
        {"jaut": "Starp 0 un 10 ir 10 intervāli. c = ?",
         "atb": ["1"], "padoms": "10 : 10."},
        {"jaut": "Starp 100 g un 200 g - 4 intervāli. c = ? (g)",
         "atb": ["25"], "padoms": "100 : 4."},
        {"jaut": "Starp 0,5 A un 1 A - 5 intervāli. c = ? (A)",
         "atb": ["0,1", "0.1"], "padoms": "0,5 : 5."},
        {"jaut": "Mērglāzē starp 50 ml un 100 ml - 10 intervāli. c = ? (ml)",
         "atb": ["5"], "padoms": "50 : 10."},
        {"jaut": "Zīmējumā punkts rāda...",
         "atb": ["34"], "padoms": "30 + 2 · 2."},
        {"jaut": "Lineāla c = 1 mm. Cik cm tas ir?",
         "atb": ["0,1", "0.1"], "padoms": "1 cm = 10 mm."},
    ], pamats=4),

    Varianti("Kurš mērījums precīzāks?", [
        {"jaut": "Garumu mēra ar lineālu (c = 1 mm) vai mērlenti (c = 1 cm).",
         "opcijas": ["Ar lineālu", "Ar mērlenti", "Vienādi",
                     "Nevar noteikt"],
         "pareizi": 0, "padoms": "Mazāka iedaļa."},
        {"jaut": "Kāpēc elektroniskie svari rāda 152,4 g, bet ne 152,43 g?",
         "opcijas": ["To iedaļas vērtība ir 0,1 g", "Tie ir bojāti",
                     "Grams ir par mazu", "Tā ir nejaušība"],
         "pareizi": 0, "padoms": "Pēdējais cipars."},
    ]),

    Pasaule("Virtuves svari un mērkrūze",
            Ievadi("", [
                {"jaut": "Mērkrūzē starp 200 ml un 300 ml ir 4 intervāli. "
                         "Kāda ir iedaļas vērtība (ml)?",
                 "atb": ["25"], "padoms": "100 : 4."},
                {"jaut": "Receptei vajag 330 ml piena. Cik tuvu var "
                         "nomērīt? Ieraksti tuvāko iedaļu virs 330 ml.",
                 "atb": ["350"], "padoms": "300; 325; 350..."},
                {"jaut": "Svari rāda 0,245 kg. Kāda ir iedaļas vērtība "
                         "gramos?",
                 "atb": ["1"], "padoms": "Pēdējais cipars - grami."},
            ]),
            pavediens="virtuve",
            konteksts="Cepšanā 25 ml atšķirība var sabojāt mīklu - tāpēc "
                      "precīzām receptēm lieto svarus, nevis krūzes.",
            kapec="Instrumenta iedaļa pasaka, cik precīzi var sekot receptei."),

    Kopsavilkums([
        "Zinu, ka mērījumā iegūst tuvinājumu.",
        "Nosaku iedaļas vērtību jebkurai skalai.",
        "Izvēlos precīzāko instrumentu.",
    ]),

    Majas([
        "Atrodi mājās 3 mērinstrumentus un nosaki to iedaļas vērtību.",
        "Nomēri galda garumu ar lineālu un mērlenti; salīdzini.",
        "Uzraksti, kāpēc rezultāti atšķiras.",
    ]),
]
