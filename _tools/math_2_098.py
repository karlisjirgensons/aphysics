# -*- coding: utf-8 -*-
"""2. klase, 98. stunda: «Kā nosaukt figūru precīzi?»

Jēdzieni mala, virsotne, šķautne un daudzstūru nosaukumi (trijstūris,
četrstūris, piecstūris, sešstūris) - nosaukums nāk no stūru skaita.
Telpiskai figūrai šķautne ir tas, kas plaknes figūrai mala.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, figura, kermenis)

TEMA = "Kā nosaukt figūru precīzi?"

MERKIS = ("Šodien lietosim jēdzienus mala, virsotne, šķautne un nosauksim "
          "daudzstūrus un telpiskās figūras.")

_PIECSTURIS = figura([(1, 0), (5, 0), (6, 3), (3, 5), (0, 3)])
_SESSTURIS = figura([(2, 0), (5, 0), (7, 3), (5, 6), (2, 6), (0, 3)])
_TRIJSTURIS = figura([(0, 0), (6, 0), (2, 4)])

SATURS = [
    Sakums("Kāpēc ASV Aizsardzības ministrijas ēku sauc par «Pentagonu»?",
           zimejums=_PIECSTURIS,
           paraksts="Pentagons - grieķu valodā «piecstūris».",
           fakti=["Ēkai ir 5 malas un 5 stūri.",
                  "Figūras nosaukums bieži pasaka stūru skaitu.",
                  "Daudzstūrim malu ir tikpat, cik virsotņu."]),

    Doma("Figūras daļas",
         "Daudzstūrim ir malas un virsotnes; telpiskai figūrai - šķautnes, "
         "virsotnes un skaldnes.",
         soli=[
             "Mala - nogrieznis, kas veido daudzstūra robežu.",
             "Virsotne - punkts, kur satiekas divas malas.",
             "Šķautne - telpiskas figūras «mala».",
             "Skaldne - telpiskas figūras plakanā virsma.",
         ]),

    Ievadi("Saskaiti", [
        {"jaut": "Cik virsotņu?", "zim": _PIECSTURIS, "atb": ["5"],
         "padoms": "Saskaiti punktus."},
        {"jaut": "Cik malu?", "zim": _SESSTURIS, "atb": ["6"],
         "padoms": "Tikpat, cik virsotņu."},
        {"jaut": "Cik skaldņu kubam?", "zim": kermenis("kubs"),
         "atb": ["6"], "padoms": "Kā metamajam kauliņam."},
        {"jaut": "Cik virsotņu kubam?", "zim": kermenis("kubs"),
         "atb": ["8"], "padoms": "4 augšā, 4 apakšā."},
        {"jaut": "Cik šķautņu kubam?", "zim": kermenis("kubs"),
         "atb": ["12"], "padoms": "4 augšā, 4 apakšā, 4 sānos."},
        {"jaut": "Cik malu kopā trijstūrim un piecstūrim?", "atb": ["8"],
         "padoms": "3 + 5."},
    ], pamats=4),

    Varianti("Kā sauc?", [
        {"jaut": "Kā sauc šo figūru?", "zim": _SESSTURIS,
         "opcijas": ["sešstūris", "piecstūris", "četrstūris"],
         "pareizi": 0, "padoms": "Saskaiti stūrus."},
        {"jaut": "Kā sauc šo figūru?", "zim": _TRIJSTURIS,
         "opcijas": ["trijstūris", "četrstūris", "aplis"], "pareizi": 0,
         "padoms": "3 stūri."},
        {"jaut": "Kas ir virsotne?",
         "opcijas": ["punkts, kur satiekas malas", "figūras vidus",
                     "garākā mala"], "pareizi": 0,
         "padoms": "Stūra punkts."},
        {"jaut": "Kāda figūra ir kvadrāts?",
         "opcijas": ["četrstūris", "trijstūris", "piecstūris"],
         "pareizi": 0, "padoms": "4 stūri."},
    ]),

    Pasaule("Ceļa zīmes",
            Varianti("", [
                {"jaut": "Zīme «STOP» ir astoņstūris. Cik tai malu?",
                 "opcijas": ["8", "6", "5"], "pareizi": 0,
                 "padoms": "Astoņ- nozīmē 8."},
                {"jaut": "Brīdinājuma zīmes ir trijstūri. Cik tām virsotņu?",
                 "opcijas": ["3", "4", "0"], "pareizi": 0,
                 "padoms": "Trij- nozīmē 3."},
            ]),
            pavediens="celojums",
            konteksts="Ceļa zīmēm ir dažādas formas, lai tās pazītu uzreiz.",
            kapec="Forma pasaka nozīmi, pat ja uzrakstu neredz."),

    Kopsavilkums([
        "Lietoju vārdus mala, virsotne, šķautne, skaldne.",
        "Nosaucu daudzstūri pēc stūru skaita.",
        "Saskaitu kuba virsotnes, šķautnes un skaldnes.",
    ]),

    Majas([
        "Atrodi mājās 3 daudzstūrus un nosauc tos.",
        "Saskaiti malas un virsotnes.",
        "Atrodi kubu vai kasti un saskaiti šķautnes.",
    ]),
]
