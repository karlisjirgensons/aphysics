# -*- coding: utf-8 -*-
"""5. klase, 158. stunda: «Punkti vai līnija?»

Jautājums, ko mācību grāmatas parasti apiet: kad punktus drīkst savienot ar
līniju? Ja starp diviem attēlotajiem stāvokļiem lielums tiešām mainās, līnija
ir pareiza; ja starpvērtību nav - piemēram, skolēnu skaits -, tad pareizi ir
tikai atsevišķi punkti.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, plakne)

TEMA = "Punkti vai līnija?"

MERKIS = ("Mācīsimies argumentēt, kad sakarības attēls ir atsevišķi punkti un "
          "kad - līnija.")

SATURS = [
    Sakums("Vai starp punktiem kaut kas ir?",
           zimejums=plakne(punkti=[(1, 2, ""), (2, 4, ""), (3, 6, "")],
                           no_x=0, lidz_x=5, no_y=0, lidz_y=8, solis=2,
                           virsraksts="Trīs punkti bez līnijas"),
           paraksts="Ja pērk 1, 2 vai 3 preces, starpvērtību nav.",
           fakti=["Preču skaits var būt tikai vesels.",
                  "Pusotras preces nopirkt nevar.",
                  "Tāpēc te zīmē punktus, nevis līniju."]),

    Doma("Līnija nozīmē, ka starpvērtības pastāv",
         "Punktus savieno ar līniju tad, ja lielums var pieņemt arī "
         "starpvērtības; ja tādu nav, attēlo tikai atsevišķus punktus.",
         soli=[
             "Padomā, vai starp diviem punktiem lielums var mainīties.",
             "Ja var - savieno punktus ar līniju.",
             "Ja nevar - atstāj atsevišķus punktus.",
             "Pārbaudi ar jautājumu: ko nozīmētu punkts starp tiem?",
             "Pamato savu izvēli vienā teikumā.",
         ],
         pieze="Laiks un attālums mainās nepārtraukti, tāpēc kustības "
               "grafiks ir līnija. Skolēnu skaits un preču skaits mainās pa "
               "vienam, tāpēc tur ir tikai punkti."),

    Paraugs("Preces un cena",
            uzd="Viena prece maksā 2 €. Vai grafiku zīmēt ar punktiem vai "
                "līniju?",
            soli=[
                ("1 prece - 2 €, 2 preces - 4 €",
                 "Divi punkti."),
                ("Vai var nopirkt pusotru preci?",
                 "Nevar."),
                ("Starpvērtību nav",
                 "Punkts starp tiem neko nenozīmētu."),
                ("Zīmē atsevišķus punktus",
                 "Bez savienojošās līnijas."),
            ],
            atbilde="Pareizi ir atsevišķi punkti"),

    Ievadi("Punkti vai līnija?", [
        {"jaut": "Preču skaits un cena. Punkti vai līnija? Raksti vienu "
                 "vārdu.",
         "atb": ["punkti"], "padoms": "Pusotru preci nenopirksi."},
        {"jaut": "Laiks un nobrauktais ceļš. Punkti vai līnija?",
         "atb": ["līnija", "linija"], "padoms": "Laiks mainās nepārtraukti."},
        {"jaut": "Skolēnu skaits klasēs. Punkti vai līnija?",
         "atb": ["punkti"], "padoms": "Puse skolēna nav."},
        {"jaut": "Temperatūra dienas laikā. Punkti vai līnija?",
         "atb": ["līnija", "linija"], "padoms": "Tā mainās pakāpeniski."},
        {"jaut": "Viena prece maksā 2 €. Cik maksā 3 preces?",
         "atb": ["6"], "padoms": "2 · 3."},
        {"jaut": "Cik maksā 5 preces?",
         "atb": ["10"], "padoms": "2 · 5."},
        {"jaut": "Auto brauc 60 km stundā. Cik kilometru tas nobrauc "
                 "2 stundās?",
         "atb": ["120"], "padoms": "60 · 2."},
        {"jaut": "Cik kilometru tas nobrauc pusstundā?",
         "atb": ["30"], "padoms": "60 : 2."},
    ], pamats=4,
        ievads="Jautā sev: ko nozīmētu punkts starp diviem attēlotajiem?"),

    Zimejums("Kustība ir nepārtraukta",
             plakne(lauzta=[(0, 0), (1, 2), (2, 4), (3, 6)], no_x=0,
                    lidz_x=5, no_y=0, lidz_y=8, solis=2,
                    virsraksts="Laiks un ceļš - ar līniju"),
             paskaidro="Starp katrām divām stundām auto turpina braukt, "
                       "tāpēc punkti ir savienoti - katrs līnijas punkts "
                       "kaut ko nozīmē.",
             ievads="Šeit līnija ir pareiza."),

    Varianti("Kad savieno punktus?", [
        {"jaut": "Kad punktus savieno ar līniju?",
         "opcijas": ["Kad pastāv starpvērtības", "Vienmēr", "Nekad",
                     "Kad punktu ir daudz"],
         "pareizi": 0,
         "padoms": "Līnijas punktam kaut kas jānozīmē."},
        {"jaut": "Preču skaits un cena - kā attēlo?",
         "opcijas": ["Ar punktiem", "Ar līniju", "Ar stabiņiem",
                     "Ar riņķi"],
         "pareizi": 0,
         "padoms": "Pusotra prece neeksistē."},
        {"jaut": "Laiks un nobrauktais ceļš - kā attēlo?",
         "opcijas": ["Ar līniju", "Ar punktiem", "Ar sektoriem",
                     "Nekā"],
         "pareizi": 0,
         "padoms": "Laiks mainās nepārtraukti."},
        {"jaut": "Ko nozīmē punkts starp diviem attēlotajiem?",
         "opcijas": ["Starpvērtību", "Kļūdu", "Neko", "Vidējo"],
         "pareizi": 0,
         "padoms": "Ja tāda pastāv."},
        {"jaut": "Skolēnu skaits - kā attēlo?",
         "opcijas": ["Ar punktiem", "Ar līniju", "Ar sektoriem", "Nekā"],
         "pareizi": 0,
         "padoms": "Skaits ir vesels."},
        {"jaut": "Kas jāpamato, izvēloties attēlu?",
         "opcijas": ["Vai starpvērtības pastāv", "Vai punktu ir daudz",
                     "Vai lapa ir liela", "Neko"],
         "pareizi": 0,
         "padoms": "Tas ir vienīgais jautājums."},
    ], pamats=4),

    Pasaule("Kā attēlot skolas datus?",
            Ievadi("", [
                {"jaut": "Skolēnu skaits piecās klasēs. Punkti vai līnija? "
                         "Raksti vienu vārdu.",
                 "atb": ["punkti"], "padoms": "Skaits ir vesels."},
                {"jaut": "Temperatūra klasē dienas laikā. Punkti vai līnija?",
                 "atb": ["līnija", "linija"], "padoms": "Mainās "
                                                        "nepārtraukti."},
                {"jaut": "Ēdnīcā pusdienas maksā 2 €. Cik maksā 4 pusdienas?",
                 "atb": ["8"], "padoms": "2 · 4."},
                {"jaut": "Pusdienu skaits un samaksa. Punkti vai līnija?",
                 "atb": ["punkti"], "padoms": "Pusdienu skaits ir vesels."},
            ]),
            pavediens="skola",
            konteksts="Skolas datos ir gan skaitāmas lietas, gan tādas, kas "
                      "mainās nepārtraukti.",
            kapec="Attēla veids pasaka, vai starpvērtībām ir jēga."),

    Kopsavilkums([
        "Izlemju, vai sakarību attēlot ar punktiem vai līniju.",
        "Pamatoju izvēli ar to, vai starpvērtības pastāv.",
        "Savienoju punktus tikai tad, kad līnijai ir jēga.",
        "Paskaidroju, ko nozīmē punkts starp diviem attēlotajiem.",
    ]),

    Majas([
        "Atrodi divus datu piemērus: vienu ar punktiem, otru ar līniju.",
        "Pamato katru izvēli vienā teikumā.",
        "Uzzīmē abus grafikus.",
    ]),
]
