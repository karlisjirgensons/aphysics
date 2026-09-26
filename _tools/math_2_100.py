# -*- coding: utf-8 -*-
"""2. klase, 100. stunda: «Kā uzzīmēt figūru datorā?»

Zīmēšanas programmā figūras veido ar rīkiem: taisnstūris, elipse, līnija.
Kvadrātu iegūst, velkot taisnstūri ar vienādām malām (bieži - turot Shift).
Svarīgi zināt figūru īpašības, lai izvēlētos pareizo rīku.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Pasaule, Petijums,
                         Sakums, Varianti, figura)

TEMA = "Kā uzzīmēt figūru datorā?"

MERKIS = ("Šodien veidosim figūru zīmējumus ar zīmēšanas rīkiem un "
          "saglabāsim rezultātu.")

_MAJA = figura([(0, 0), (6, 0), (6, 4), (3, 7), (0, 4)])

SATURS = [
    Sakums("Kā datorā uzzīmēt māju no figūrām?",
           zimejums=_MAJA,
           paraksts="Kvadrāts un trijstūris - māja.",
           fakti=["Programmā ir rīki: taisnstūris, elipse, līnija.",
                  "Sarežģītu zīmējumu saliek no vienkāršām figūrām.",
                  "Darbu saglabā, lai to neiznīcinātu."]),

    Doma("Rīks katrai figūrai",
         "Izvēlies rīku pēc figūras īpašībām.",
         soli=[
             "Taisnstūra rīks - taisnstūris vai kvadrāts.",
             "Elipses rīks - aplis (turot Shift - tieši apaļš).",
             "Līnijas rīks - trijstūris un citi daudzstūri.",
             "Saglabā: «Fails» → «Saglabāt».",
         ]),

    Varianti("Kuru rīku ņemt?", [
        {"jaut": "Logs mājai - kvadrāts.",
         "opcijas": ["taisnstūra rīks", "elipses rīks", "dzēšgumija"],
         "pareizi": 0, "padoms": "Kvadrāts ir taisnstūris."},
        {"jaut": "Saule - aplis.",
         "opcijas": ["elipses rīks", "līnijas rīks", "taisnstūra rīks"],
         "pareizi": 0, "padoms": "Apaļa figūra."},
        {"jaut": "Jumts - trijstūris.",
         "opcijas": ["līnijas rīks - 3 līnijas", "elipses rīks",
                     "taisnstūra rīks"], "pareizi": 0,
         "padoms": "Trijstūrim ir 3 malas."},
        {"jaut": "Cik figūru vajag šai mājai?", "zim": _MAJA,
         "opcijas": ["2: kvadrāts un trijstūris", "1", "5"],
         "pareizi": 0, "padoms": "Siena un jumts."},
    ]),

    Petijums("Datora zīmējums", [
        "Atver zīmēšanas programmu (piemēram, Paint).",
        "Uzzīmē māju no kvadrāta un trijstūra.",
        "Pievieno logu, durvis un sauli.",
        "Saglabā darbu ar savu vārdu.",
        "Saskaiti: cik figūru izmantoji?",
    ], vajag="dators vai planšete",
             secinajums="Katrs zīmējums sastāv no vienkāršām figūrām."),

    Pasaule("Spēļu dizainers",
            Varianti("", [
                {"jaut": "Datorspēles varonis ir salikts no 4 kvadrātiem un "
                         "2 apļiem. Cik figūru jāuzzīmē?",
                 "opcijas": ["6", "4", "2"], "pareizi": 0,
                 "padoms": "4 + 2."},
                {"jaut": "Kāpēc spēļu dizaineri zīmē no figūrām?",
                 "opcijas": ["Datoram vieglāk zīmēt vienkāršas figūras",
                             "Tā ir smukāk", "Nav citu rīku"],
                 "pareizi": 0, "padoms": "Dators strādā ar figūrām."},
            ]),
            pavediens="tehnika",
            konteksts="Arī datorspēļu pasaules sastāv no figūrām.",
            kapec="Ģeometrija ir katra datora zīmējuma pamatā."),

    Kopsavilkums([
        "Izvēlos zīmēšanas rīku pēc figūras.",
        "Salieku zīmējumu no vienkāršām figūrām.",
        "Saglabāju savu darbu.",
    ]),

    Majas([
        "Datorā vai uz papīra uzzīmē robotu no figūrām.",
        "Saskaiti, cik katras figūras izmantoji.",
        "Parādi mājiniekam.",
    ]),
]
