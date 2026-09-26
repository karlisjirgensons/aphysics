# -*- coding: utf-8 -*-
"""2. klase, 106. stunda: «Kā sadalīt taisnstūri vienādos kvadrātos?»

Rūtiņu tīklā taisnstūri var sadalīt vienāda lieluma daļās: 12 rūtiņas - 2
daļās pa 6, 3 pa 4, 4 pa 3, 6 pa 2. Kvadrātos - tikai tad, ja malas to
atļauj. Te sagatavo dalīšanu, kas nāks 2.7. tematā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, restis)

TEMA = "Kā sadalīt taisnstūri vienādos kvadrātos?"

MERKIS = ("Šodien sadalīsim taisnstūri rūtiņu tīklā vienāda lieluma daļās "
          "vairākos veidos.")


def _rezgis(burti):
    """Taisnstūris rūtiņās; katrā rūtiņā - tās daļas burts."""
    return restis([list(r) for r in burti])


SATURS = [
    Sakums("Kā sadalīt vafeles plāksni 4 bērniem godīgi?",
           zimejums=_rezgis(["ABCD", "ABCD", "ABCD"]),
           paraksts="12 rūtiņas - katrā daļā vienāds skaits.",
           fakti=["Vienādas daļas - vienāds rūtiņu skaits.",
                  "Daļu forma var būt dažāda.",
                  "Kvadrātos var sadalīt ne vienmēr."]),

    Doma("Vienādas daļas",
         "Katrā daļā ir tikpat rūtiņu; visas rūtiņas izlietotas.",
         soli=[
             "Saskaiti visas rūtiņas.",
             "Izvēlies daļu skaitu.",
             "Atrodi, cik rūtiņu katrā daļā.",
             "Iekrāso katru daļu citā krāsā un pārbaudi.",
         ]),

    Slidnis("Taisnstūris ar 8 rūtiņām", [
        {"v": "2 daļas", "teksts": "Pa 4 rūtiņām: 2 kvadrāti.",
         "zim": _rezgis(["AABB", "AABB"])},
        {"v": "4 daļas", "teksts": "Pa 2 rūtiņām: 4 stabiņi.",
         "zim": _rezgis(["ABCD", "ABCD"])},
        {"v": "8 daļas", "teksts": "Pa 1 rūtiņai: 8 mazi kvadrāti.",
         "zim": _rezgis(["ABCD", "EFGH"])},
    ]),

    Ievadi("Cik rūtiņu daļā?", [
        {"jaut": "12 rūtiņas sadala 2 vienādās daļās. Cik katrā?",
         "atb": ["6"], "padoms": "6 + 6."},
        {"jaut": "12 rūtiņas sadala 3 vienādās daļās. Cik katrā?",
         "atb": ["4"], "padoms": "4 + 4 + 4."},
        {"jaut": "12 rūtiņas sadala 4 vienādās daļās. Cik katrā?",
         "atb": ["3"], "padoms": "3 + 3 + 3 + 3."},
        {"jaut": "8 rūtiņas - cik vienādās daļās pa 2?", "atb": ["4"],
         "padoms": "2 + 2 + 2 + 2."},
        {"jaut": "Kvadrāts 4 rūtiņas garš un 4 plats. Cik kvadrātos ar "
                 "malu 2 rūtiņas to var sadalīt?", "atb": ["4"], "padoms": "Katrā kvadrātā 4 "
                                                      "rūtiņas, kopā 16."},
        {"jaut": "Taisnstūris ar 10 rūtiņām - cik daļās pa 5?", "atb": ["2"],
         "padoms": "5 + 5."},
    ], pamats=4),

    Varianti("Vai var sadalīt?", [
        {"jaut": "Vai 9 rūtiņas var sadalīt 2 vienādās daļās?",
         "opcijas": ["Nē", "Jā"], "jaukt": False, "pareizi": 0,
         "padoms": "4 + 4 = 8, 5 + 5 = 10."},
        {"jaut": "Vai taisnstūri 3 rūtiņas garu un 2 platu var sadalīt "
                 "kvadrātos ar malu 2 rūtiņas?",
         "opcijas": ["Nē", "Jā"], "jaukt": False, "pareizi": 0,
         "padoms": "Malā 3 rūtiņas - 2 ietilpst tikai vienreiz."},
    ]),

    Petijums("Sadali pats", [
        "Uzzīmē taisnstūri 6 rūtiņas garu un 2 augstu.",
        "Sadali to 2, 3, 4 un 6 vienādās daļās - katrā zīmējumā savādāk.",
        "Iekrāso daļas.",
        "Kurā gadījumā daļas bija kvadrāti?",
    ], vajag="rūtiņu lapa, krāsainie zīmuļi"),

    Pasaule("Dārza dobes",
            Ievadi("", [
                {"jaut": "Dārzs ir 6 rūtiņas garš un 4 plats - 24 rūtiņas. "
                         "4 bērni saņem vienādas dobes. Cik rūtiņu katram?",
                 "atb": ["6"], "padoms": "6 + 6 + 6 + 6 = 24."},
            ]),
            pavediens="daba",
            konteksts="Skolas dārzā katrai grupai sava dobe.",
            kapec="Vienādas dobes - godīgs darbs visiem."),

    Kopsavilkums([
        "Sadalu taisnstūri vienāda lieluma daļās.",
        "Atrodu vairākus sadalījuma veidus.",
        "Zinu, kad var sadalīt kvadrātos.",
    ]),

    Majas([
        "Sagriez papīra taisnstūri 8 vienādās daļās.",
        "Atrodi divus dažādus veidus.",
        "Kurā veidā daļas bija kvadrāti?",
    ]),
]
