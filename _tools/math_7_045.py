# -*- coding: utf-8 -*-
"""7. klase, 45. stunda: «Punkti vai nepārtraukta līnija?»

Grafiku savieno ar līniju tikai tad, ja mainīgais var pieņemt arī
starpvērtības. Biļešu skaits ir vesels - grafiks ir atsevišķi punkti;
benzīna litri var būt jebkuri - grafiks ir līnija.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, Zimejums, plakne)

TEMA = "Punkti vai nepārtraukta līnija?"

MERKIS = ("Iemācīsimies pamatot, vai sakarības grafiks ir līnija vai "
          "atsevišķi punkti.")

SATURS = [
    Sakums("Biļetes un benzīns",
           zimejums=plakne(punkti=[(1, 3), (2, 6), (3, 9), (4, 12)],
                           no_x=0, lidz_x=5, no_y=0, lidz_y=15, solis=1,
                           solis_y=3, x_nos="n", y_nos="€"),
           paraksts="Biļetes pa 3 € - tikai atsevišķi punkti.",
           fakti=["Nevar nopirkt 2,5 biļetes - starp punktiem nekā nav.",
                  "Benzīnu var iepildīt 2,5 l - tur grafiks ir līnija."]),

    Doma("Līnija tikai tad, ja der starpvērtības",
         "Ja neatkarīgais mainīgais var pieņemt jebkuras vērtības kādā "
         "intervālā, grafiks ir nepārtraukta līnija. Ja tikai atsevišķas "
         "(veselas) vērtības - grafiks ir atsevišķi punkti.",
         soli=[
             "Nosaki neatkarīgo mainīgo.",
             "Jautā: vai der vērtība pa vidu, piemēram, 2,5?",
             "Ja der - savieno punktus ar līniju.",
             "Ja neder - atstāj tikai punktus.",
         ],
         pieze="Punktus reizēm savieno ar raustītu līniju, lai redzētu "
               "tendenci, - bet tad jāzina, ka starpvērtības nav jēgpilnas."),

    Zimejums("Benzīns: līnija",
             plakne(grafiki=[(1.6, 0, "")],
                    no_x=0, lidz_x=10, no_y=0, lidz_y=16, solis=1,
                    solis_y=2, x_nos="l", y_nos="€"),
             paskaidro="1,60 € par litru: arī 2,5 l ir jēgpilni - 4 €."),

    Paraugs("Pamato izvēli",
            uzd="Vai grafikam «ūdens daudzums vannā atkarībā no laika» jābūt "
                "līnijai vai punktiem?",
            soli=[
                ("Neatkarīgais - laiks t", "Tas rit nepārtraukti."),
                ("t = 2,5 min ir jēgpilna vērtība", "Arī 2,51 un 2,512."),
                ("Tātad grafiks ir nepārtraukta līnija", "Secinājums."),
            ],
            atbilde="Līnija, jo laiks mainās nepārtraukti."),

    Varianti("Līnija vai punkti?", [
        {"jaut": "Mācību grāmatu skaits un to masa",
         "opcijas": ["Punkti", "Līnija"],
         "pareizi": 0, "jaukt": False,
         "padoms": "Grāmatas skaita veselās."},
        {"jaut": "Brauciena laiks un nobrauktais ceļš",
         "opcijas": ["Punkti", "Līnija"],
         "pareizi": 1, "jaukt": False,
         "padoms": "Laiks nepārtraukts."},
        {"jaut": "Pirkto ābolu masa (kg) un cena",
         "opcijas": ["Punkti", "Līnija"],
         "pareizi": 1, "jaukt": False,
         "padoms": "Var nosvērt 1,35 kg."},
        {"jaut": "Koncerta biļešu skaits un kopējā summa",
         "opcijas": ["Punkti", "Līnija"],
         "pareizi": 0, "jaukt": False,
         "padoms": "Biļetes veselas."},
    ], pamats=4),

    Varianti("Nolasi no grafika", [
        {"jaut": "Benzīna grafikā: cik € maksā 5 l?",
         "opcijas": ["8 €", "5 €", "10 €", "6 €"],
         "pareizi": 0,
         "padoms": "1,6 · 5."},
        {"jaut": "Biļešu grafikā: cik biļetes par 12 €?",
         "opcijas": ["4", "3", "12", "36"],
         "pareizi": 0,
         "padoms": "Punkts (4; 12)."},
    ]),

    Pasaule("Mobilais internets",
            Varianti("", [
                {"jaut": "Maksā 1 € par katru iesāktu GB. Vai grafiks "
                         "«patērētie GB - maksa» ir taisne caur 0?",
                 "opcijas": ["Nē - tas ir «pakāpienu» grafiks",
                             "Jā", "Tikai punkti uz taisnes",
                             "Tā ir horizontāla taisne"],
                 "pareizi": 0,
                 "padoms": "1,1 GB maksā tikpat, cik 2 GB."},
                {"jaut": "Cik € par 2,3 GB?",
                 "opcijas": ["3 €", "2,3 €", "2 €", "23 €"],
                 "pareizi": 0,
                 "padoms": "Iesākti 3 GB."},
                {"jaut": "Cik € par 0,1 GB?",
                 "opcijas": ["1 €", "0,1 €", "0 €", "10 €"],
                 "pareizi": 0,
                 "padoms": "Iesākts viens GB."},
            ]),
            pavediens="dati",
            konteksts="Daži tarifi rēķina par «iesāktu vienību» - un tad "
                      "grafiks ir kā kāpnes.",
            kapec="Ne katra sakarība ir taisne - jāskatās situācija."),

    Kopsavilkums([
        "Pamatoju, vai grafiks ir līnija vai punkti.",
        "Pārbaudu, vai starpvērtības ir jēgpilnas.",
        "Nolasu vērtības no abu veidu grafikiem.",
        "Zinu, ka ir arī «pakāpienu» grafiki.",
    ]),

    Majas([
        "Uzzīmē grafiku «saldējuma porciju skaits - cena».",
        "Uzzīmē grafiku «laiks - nostaigātais ceļš».",
        "Paskaidro, kāpēc viens ir punkti, bet otrs - līnija.",
    ]),
]
