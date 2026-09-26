# -*- coding: utf-8 -*-
"""1. klase, 162. stunda: «Kādu rotājumu izveidosi?»

Noslēdzošs darbs par simetriju: skolēns izvēlas tehniku (locīt un griezt,
zīmēt rūtiņās, kopēt ar krāsu) un izveido simetrisku rotājumu vai
kartīti. Pēc tam parāda simetrijas līnijas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, bildes)

TEMA = "Kādu rotājumu izveidosi?"

MERKIS = ("Šodien izveidosim simetrisku rotājumu vai kartīti izvēlētā "
          "tehnikā.")

SATURS = [
    Sakums("Simetrisks rotājums - trīs veidi",
           zimejums=bildes([["sirds", "zvaigzne", "puke"]]),
           paraksts="Sirds, zvaigzne, zieds - katrs simetrisks.",
           fakti=["Pārloki un izgriez.",
                  "Zīmē rūtiņās pa pusei.",
                  "Krāsas nospiedums uz pārlocītas lapas."]),

    Doma("Izvēlies tehniku",
         "Katrā tehnikā simetrija rodas no locījuma vai rūtiņām.",
         soli=[
             "Izgriešana: pārloki, zīmē pusi, izgriez.",
             "Rūtiņas: puse, tad otra pa rūtiņām.",
             "Nospiedums: krāsa vienā pusē, pārloki, atloki.",
         ]),

    Petijums("Mans rotājums", [
        "Izvēlies tehniku.",
        "Izveido rotājumu.",
        "Atrodi un uzvelc tā simetrijas līniju(-as).",
        "Pastāsti klasei, kā to izveidoji.",
    ], vajag="papīrs, šķēres, krāsas, rūtiņu lapa"),

    Varianti("Kura tehnika?", [
        {"jaut": "Sniegpārsla ar daudz zariem - kā ātrāk?",
         "opcijas": ["locīt vairākkārt un griezt", "zīmēt brīvi"],
         "jaukt": False, "pareizi": 0,
         "padoms": "Vairāki locījumi - vairākas līnijas."},
        {"jaut": "Tauriņš ar krāsainiem spārniem - kā?",
         "opcijas": ["krāsas nospiedums uz pārlocītas lapas",
                     "krāsot katru spārnu atsevišķi citādi"],
         "jaukt": False, "pareizi": 0, "padoms": "Nospiedums dod spoguli."},
    ]),

    Ievadi("Saskaiti", [
        {"jaut": "Papīru pārloka divreiz un izgriež. Cik vienādu daļu "
                 "rakstā?", "atb": ["4"], "padoms": "2 locījumi - 4 daļas."},
    ]),

    Pasaule("Svētku izstāde",
            Ievadi("", [
                {"jaut": "Klasē 20 bērnu, katrs izveido 2 rotājumus. Cik "
                         "rotājumu izstādē?", "atb": ["40"],
                 "padoms": "20 + 20."},
            ]),
            pavediens="skola",
            konteksts="Klase rīko rotājumu izstādi.",
            kapec="Matemātika var būt skaista."),

    Kopsavilkums([
        "Izveidoju simetrisku rotājumu.",
        "Parādu tā simetrijas līnijas.",
        "Pastāstu, kā to izveidoju.",
    ]),

    Majas([
        "Izveido simetrisku kartīti kādam no ģimenes.",
        "Parādi, kur ir simetrijas līnija.",
        "Pastāsti, kā to izveidoji.",
    ]),
]
