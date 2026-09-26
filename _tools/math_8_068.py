# -*- coding: utf-8 -*-
"""8. klase, 68. stunda: «Kā sadalīt sarežģītu figūru?»

Divi paņēmieni: sadalīt figūru pazīstamās daļās vai ievietot to taisnstūrī
un atņemt liekos trijstūrus. Slīdnis papildina četrstūri ABCD līdz
taisnstūrim 7 × 5: 35 − 12,5 = 22,5 (pārbaudīts ar koordinātu formulu).
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, figura, geometrija)

TEMA = "Kā sadalīt sarežģītu figūru?"

MERKIS = ("Sadalīsim figūru trijstūros un taisnstūros un aprēķināsim tās "
          "laukumu.")

_PUNKTI = [("A", 0, 0), ("B", 7, 1), ("C", 5, 5), ("D", 1, 4),
           ("P", 7, 0, 315), ("Q", 7, 5, 45), ("R", 0, 5, 135)]


def _papild(taisnst, lieki):
    nogr = ["AB", "BC", "CD", "DA"]
    if taisnst:
        nogr += ["AP", "PQ", "QR", "RA"]
    krasa = [("ABCD", 0)]
    if lieki:
        krasa += [("ABP", 1), ("BQC", 1), ("CRD", 1), ("DAR", 1)]
    return geometrija(_PUNKTI if taisnst else _PUNKTI[:4], nogriezni=nogr,
                      iekrasot=krasa)


SATURS = [
    Sakums("Kā aprēķināt mājas sienas laukumu?",
           zimejums=figura([(0, 0), (8, 0), (8, 4), (4, 7), (0, 4)]),
           paraksts="Rūtiņa - 1 m. Siena = taisnstūris 8 × 4 + trijstūris.",
           fakti=["Sarežģītu figūru sadala taisnstūros un trijstūros.",
                  "Laukumus saskaita - vai atņem no lielāka taisnstūra.",
                  "Rūtiņu lapā augstumus nolasa pa rūtiņām."]),

    Doma("Sadali vai papildini",
         "Figūras laukums ir tās daļu laukumu summa.",
         soli=[
             "Sadali figūru daļās, kuru laukumus proti aprēķināt.",
             "Vai arī ievieto figūru taisnstūrī un atņem liekos trijstūrus.",
             "Pārbaudi, vai daļas nepārklājas un nekas nav izlaists.",
         ]),

    Paraugs("Mājas siena",
            uzd="Aprēķini sākuma zīmējuma mājas sienas laukumu.",
            soli=[
                ("8 · 4 = 32 m²", "Taisnstūris."),
                ("{8 · 3|2} = 12 m²", "Jumta trijstūris: pamats 8, "
                                      "augstums 7 − 4 = 3."),
                ("32 + 12 = 44 m²", "Saskaita."),
            ],
            atbilde="44 m²"),

    Slidnis("Papildini līdz taisnstūrim", [
        {"v": "ABCD", "teksts": "Nevienas malas gar rūtiņām",
         "zim": _papild(False, False)},
        {"v": "7 · 5 = 35", "teksts": "Taisnstūris APQR ap figūru",
         "zim": _papild(True, False)},
        {"v": "3,5 + 4 + 2,5 + 2,5 = 12,5", "teksts": "Četri lieki "
                                                      "taisnleņķa trijstūri",
         "zim": _papild(True, True)},
        {"v": "35 − 12,5 = 22,5", "teksts": "Figūras ABCD laukums",
         "zim": _papild(True, True)},
    ]),

    Ievadi("Aprēķini laukumu", [
        {"jaut": "L veida figūra: taisnstūris 6 × 4 bez stūra kvadrāta 2 × 2. "
                 "S?", "atb": ["20"], "padoms": "24 − 4."},
        {"jaut": "Taisnstūris 10 × 6 ar trijstūra izgriezumu (pamats 4, "
                 "augstums 3). S?", "atb": ["54"], "padoms": "60 − 6."},
        {"jaut": "Taisnstūris 5 × 4 un pie tā taisnleņķa trijstūris ar "
                 "katetēm 3 un 4. S?", "atb": ["26"], "padoms": "20 + 6."},
        {"jaut": "Slīdnī: cik liels ir trijstūris ABP?", "atb": ["3,5"],
         "padoms": "Katetes 7 un 1."},
    ]),

    Varianti("Spried", [
        {"jaut": "Taisnstūris 8 × 3 un virs tā trijstūris ar pamatu 8 un "
                 "augstumu 2. S = ?",
         "opcijas": ["32", "40", "28", "26"],
         "pareizi": 0, "padoms": "24 + 8."},
        {"jaut": "Vai laukums mainās, ja figūru sadala citādi?",
         "opcijas": ["Nē", "Jā", "Atkarīgs no daļu skaita",
                     "Tikai trijstūriem"],
         "pareizi": 0, "padoms": "Figūra ir tā pati."},
        {"jaut": "Kad ērtāk papildināt līdz taisnstūrim?",
         "opcijas": ["Ja malas ir slīpas", "Ja figūra ir taisnstūris",
                     "Ja figūra ir kvadrāts", "Nekad"],
         "pareizi": 0, "padoms": "Lieki ir taisnleņķa trijstūri."},
    ]),

    Pasaule("Grīdas remonts",
            Ievadi("", [
                {"jaut": "Istaba ir taisnstūris 5 m × 4 m ar nišu 2 m × 1,5 m. "
                         "Grīdas laukums (m²)?",
                 "atb": ["23"], "padoms": "20 + 3."},
                {"jaut": "Lamināta paka sedz 2,2 m². Cik paku jāpērk?",
                 "atb": ["11"], "padoms": "23 : 2,2 ≈ 10,5 - uz augšu."},
                {"jaut": "Paka maksā 18 €. Cik € kopā?", "atb": ["198"],
                 "padoms": "11 · 18."},
            ]),
            pavediens="maja",
            konteksts="Istabas reti ir tīri taisnstūri: nišas un erkeri "
                      "prasa sadalīt plānu daļās.",
            kapec="Materiālu pērk pēc laukuma, un pakas - noapaļojot uz "
                  "augšu."),

    Kopsavilkums([
        "Sadalu figūru taisnstūros un trijstūros.",
        "Papildinu figūru līdz taisnstūrim un atņemu liekās daļas.",
        "Pārbaudu, vai daļas nepārklājas.",
    ]),

    Majas([
        "Uzzīmē savas istabas plānu un aprēķini grīdas laukumu.",
        "Rūtiņu lapā uzzīmē četrstūri ar slīpām malām un aprēķini laukumu "
        "divos veidos.",
        "Aprēķini mājas gala sienas laukumu pēc foto vai mēriem.",
    ]),
]
