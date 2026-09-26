# -*- coding: utf-8 -*-
"""9. klase, 12. stunda: «Kā mainās perimetrs un laukums?»

Perimetrs aug k reizes, laukums - k² reizes. Slīdnis to parāda bez
formulām: trijstūris ar divreiz garākām malām sastāv no 4 mazajiem, ar
trīsreiz garākām - no 9.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, geometrija)

TEMA = "Kā mainās perimetrs un laukums?"

MERKIS = ("Noteiksim līdzīgu trijstūru perimetru un laukumu attiecību.")

_H = 1.732                              # vienādmalu trijstūra augstums


def _rezgis(k):
    """Vienādmalu trijstūris ar malu k, sadalīts k² trijstūros ar malu 1."""
    punkti = [("_A", 0, 0), ("_B", 2.0 * k, 0), ("_C", float(k), _H * k)]
    nogr = [("_A", "_B"), ("_B", "_C"), ("_C", "_A")]
    for i in range(1, k):
        y = _H * i
        # Līnija ∥ pamatam augstumā i un līnijas ∥ sānu malām no pamata.
        punkti += [("_l%d" % i, float(i), y), ("_r%d" % i, 2.0 * k - i, y),
                   ("_p%d" % i, 2.0 * i, 0)]
        nogr.append(("_l%d" % i, "_r%d" % i))
    for i in range(1, k):
        # No pamata punkta 2i uz augšu pa labi līdz labajai malai un pa
        # kreisi līdz kreisajai malai.
        punkti += [("_rt%d" % i, float(k + i), _H * (k - i)),
                   ("_lt%d" % i, float(i), _H * i)]
        nogr += [("_p%d" % i, "_rt%d" % i), ("_p%d" % i, "_lt%d" % i)]
    return geometrija(punkti, nogriezni=nogr,
                      iekrasot=[(("_A", "_B", "_C"), 0)])


SATURS = [
    Sakums("Divreiz garākas malas - cik reižu vairāk krāsas?",
           zimejums=_rezgis(2),
           paraksts="Malas 2 reizes garākas - iekšā 4 mazie trijstūri.",
           fakti=["Perimetrs pieaug k reizes.",
                  "Laukums pieaug k² reizes.",
                  "Krāsa maksā pēc laukuma, rāmis - pēc perimetra."]),

    Slidnis("Palielini malas", [
        {"v": "k = 1", "teksts": "1 trijstūris", "zim": _rezgis(1)},
        {"v": "k = 2", "teksts": "Perimetrs × 2, laukums × 4",
         "zim": _rezgis(2)},
        {"v": "k = 3", "teksts": "Perimetrs × 3, laukums × 9",
         "zim": _rezgis(3)},
        {"v": "k = 4", "teksts": "Perimetrs × 4, laukums × 16",
         "zim": _rezgis(4)},
    ], ievads="Saskaiti mazos trijstūrus katrā solī."),

    Doma("Perimetri un laukumi",
         "Ja △A_1B_1C_1 ∼ △ABC ar koeficientu k, tad {P_1|P} = k un "
         "{S_1|S} = k^2.",
         soli=[
             "Visas malas reizinās ar k - arī to summa.",
             "Laukumā reizinās divi garumi (mala un augstums) - tātad k · k.",
             "No laukumu attiecības k = √({S_1|S}).",
         ]),

    Paraugs("No laukuma uz malu",
            uzd="Līdzīgu trijstūru laukumi ir 12 cm² un 75 cm². Mazākā "
                "trijstūra mala ir 4 cm. Atrodi atbilstošo lielākā malu.",
            soli=[
                ("k^2 = {75|12} = {25|4}", "Laukumu attiecība."),
                ("k = √{25|4} = {5|2} = 2,5", "Kvadrātsakne."),
                ("4 · 2,5 = 10", "Mala reizināta ar k."),
            ],
            atbilde="10 cm"),

    Ievadi("Aprēķini", [
        {"jaut": "k = 3, P = 12 cm. P_1 = ? cm", "atb": ["36"],
         "padoms": "12 · 3."},
        {"jaut": "k = 3, S = 5 cm². S_1 = ? cm²", "atb": ["45"],
         "padoms": "5 · 9."},
        {"jaut": "k = 0,5, S = 40 cm². S_1 = ? cm²", "atb": ["10"],
         "padoms": "40 · 0,25."},
        {"jaut": "{S_1|S} = 49. k = ?", "atb": ["7"], "padoms": "√49."},
        {"jaut": "Perimetri 10 un 25. Laukumu attiecība {S_1|S} = ?",
         "atb": ["6,25", "{25|4}", "25/4"], "padoms": "k = 2,5; k^2."},
        {"jaut": "Laukumi 18 un 8. Perimetru attiecība {P_1|P} = ?",
         "atb": ["1,5", "{3|2}", "3/2"], "padoms": "√({18|8}) = √{9|4}."},
    ], pamats=4),

    Varianti("Kļūdu slazds", [
        {"jaut": "Malas palielina 2 reizes. Laukums pieaug...",
         "opcijas": ["4 reizes", "2 reizes", "8 reizes", "nemainās"],
         "pareizi": 0, "padoms": "k^2."},
        {"jaut": "Laukums pieauga 9 reizes. Perimetrs pieauga...",
         "opcijas": ["3 reizes", "9 reizes", "81 reizi", "4,5 reizes"],
         "pareizi": 0, "padoms": "k = √9."},
        {"jaut": "Karte 1 : 1000. Laukums 1 cm² kartē = ? dabā",
         "opcijas": ["100 m²", "10 m²", "1000 cm²", "1 km²"],
         "pareizi": 0, "padoms": "1 cm → 10 m; 1 cm² → 100 m²."},
    ]),

    Pasaule("Buru krāsošana",
            Ievadi("", [
                {"jaut": "Modeļa trijstūra bura 0,3 m², īstās laivas bura "
                         "ir līdzīga ar k = 10. Laukums (m²)?",
                 "atb": ["30"], "padoms": "0,3 · 100."},
                {"jaut": "Modeļa buras mala 1,2 m apmales lente. Cik m lentes "
                         "vajag īstajai? (k = 10)", "atb": ["12"],
                 "padoms": "Garums × k."},
                {"jaut": "Audums 8 € par m². Cik € maksā īstā bura?",
                 "atb": ["240"], "padoms": "30 · 8."},
            ]),
            pavediens="tehnika",
            konteksts="Jahtu būvētāji buru vispirms pārbauda uz modeļa, "
                      "tad palielina.",
            kapec="Audumu rēķina ar k², lenti - ar k."),

    Kopsavilkums([
        "Zinu, ka perimetru attiecība ir k.",
        "Zinu, ka laukumu attiecība ir k².",
        "No laukumu attiecības atrodu k un malu.",
    ]),

    Majas([
        "Uzzīmē rūtiņās trijstūri un tam līdzīgu ar k = 3. Saskaiti rūtiņas.",
        "Kāpēc 32 cm pica ir vairāk nekā divas 20 cm picas? Pārbaudi.",
        "Laukumi 20 cm² un 45 cm². Atrodi perimetru attiecību.",
    ]),
]
