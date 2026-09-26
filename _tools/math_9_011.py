# -*- coding: utf-8 -*-
"""9. klase, 11. stunda: «Kā pamatot, ka trijstūri ir līdzīgi?»

Trīs zīmējumi, kas eksāmenā atkārtojas: paralēle trijstūrī, «tauriņš»
(divas paralēlas malas un krustojošas diagonāles) un taisnleņķa trijstūri
ar kopīgu leņķi. Katram - viens pamatojums ar pazīmi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, geometrija)

TEMA = "Kā pamatot, ka trijstūri ir līdzīgi?"

MERKIS = ("Saskatīsim līdzīgus trijstūrus zīmējumā un pamatosim līdzību ar "
          "pazīmi.")

# «Tauriņš»: AB ∥ CD, nogriežņi AD un BC krustojas punktā O.
_TAURINS = geometrija([("A", 0, 4), ("B", 3, 4), ("O", 3.333, 2.667, 200),
                       ("C", 4, 0), ("D", 10, 0)],
                      nogriezni=["AB", "CD", "AD", "BC"],
                      lenki=[("OAB", "", 1), ("ODC", "", 1),
                             ("AOB", "", 2), ("DOC", "", 2)])

_PARALELE = geometrija([("A", 0, 0), ("B", 9, 0), ("C", 3, 6),
                        ("D", 4, 0), ("E", 5.667, 3.333)],
                       nogriezni=["AB", "BC", "CA"], izcelti=["DE"],
                       lenki=[("BAC", "", 1), ("BDE", "", 1)])

_TAISNLENKA = geometrija([("A", 0, 0), ("B", 8, 0), ("C", 8, 6),
                          ("D", 4, 0), ("E", 4, 3)],
                         nogriezni=["AB", "BC", "CA"], izcelti=["DE"],
                         taisni=["ABC", "ADE"], lenki=[("BAC", "", 1)])

SATURS = [
    Sakums("Kur šeit ir līdzīgi trijstūri?",
           zimejums=_TAURINS,
           paraksts="AB ∥ CD - «tauriņš» ar diviem līdzīgiem spārniem.",
           fakti=["Krustleņķi pie O ir vienādi.",
                  "Šķērsleņķi pie paralēlām malām ir vienādi.",
                  "Tātad △AOB ∼ △DOC."]),

    Doma("Pamatojuma plāns",
         "Līdzību pamato ar pazīmi, un katram vienādajam leņķim vai "
         "attiecībai raksta iemeslu.",
         soli=[
             "Atrodi divus trijstūrus ar nezināmo un zināmajiem lielumiem.",
             "Meklē vienādus leņķus: kopīgs, krustleņķi, paralēles, 90°.",
             "Pieraksti: △… ∼ △… pēc … pazīmes.",
             "Virsotnes raksti atbilstošā secībā - tad proporcija ir gatava.",
         ]),

    Slidnis("Trīs biežākie zīmējumi", [
        {"v": "Paralēle", "teksts": "DE ∥ AC: ∠B kopīgs, ∠BDE = ∠BAC. "
                                    "△DBE ∼ △ABC.",
         "zim": _PARALELE},
        {"v": "Tauriņš", "teksts": "AB ∥ CD: ∠AOB = ∠DOC (krustleņķi), "
                                   "∠A = ∠D (šķērsleņķi). △AOB ∼ △DOC.",
         "zim": _TAURINS},
        {"v": "Taisnleņķa", "teksts": "∠A kopīgs, ∠ADE = ∠ABC = 90°. "
                                      "△ADE ∼ △ABC.",
         "zim": _TAISNLENKA},
    ]),

    Paraugs("Tauriņš",
            uzd="AB ∥ CD, AD ∩ BC = O. AB = 4, CD = 6, AO = 3. Atrodi OD.",
            soli=[
                ("△AOB ∼ △DOC", "∠AOB = ∠DOC (krustleņķi), ∠OAB = ∠ODC "
                                "(šķērsleņķi)."),
                ("{OD|AO} = {CD|AB} = {6|4} = 1,5", "Atbilstošās malas."),
                ("OD = 1,5 · 3 = 4,5", "Aprēķins."),
            ],
            atbilde="OD = 4,5"),

    Varianti("Kāds ir pamatojums?", [
        {"jaut": "Tauriņā ∠AOB = ∠DOC, jo tie ir...",
         "opcijas": ["krustleņķi", "kāpšļu leņķi", "blakusleņķi",
                     "vienpusleņķi"],
         "pareizi": 0, "padoms": "Divas taisnes krustojas punktā O."},
        {"jaut": "DE ∥ AC trijstūrī ABC. ∠BDE = ∠BAC, jo...",
         "opcijas": ["kāpšļu leņķi pie paralēlām taisnēm", "krustleņķi",
                     "trijstūris ir vienādsānu", "tie ir blakusleņķi"],
         "pareizi": 0, "padoms": "Krustotāja AB."},
        {"jaut": "Kurš pieraksts atbilst tauriņam?",
         "opcijas": ["△AOB ∼ △DOC", "△AOB ∼ △COD", "△ABO ∼ △CDO",
                     "△OAB ∼ △OCD"],
         "pareizi": 0, "padoms": "A atbilst D, B atbilst C."},
    ]),

    Ievadi("Aprēķini", [
        {"jaut": "Tauriņš: AB = 5, CD = 10, BO = 4. OC = ?", "atb": ["8"],
         "padoms": "k = 2."},
        {"jaut": "Tauriņš: AO = 6, OD = 9, CD = 12. AB = ?", "atb": ["8"],
         "padoms": "k = 1,5."},
        {"jaut": "Taisnleņķa: AD = 4, AB = 8, BC = 6. DE = ?", "atb": ["3"],
         "padoms": "{DE|BC} = {AD|AB}."},
        {"jaut": "Taisnleņķa: AD = 2, DE = 1,5, BC = 6. AB = ?", "atb": ["8"],
         "padoms": "k = 4."},
    ]),

    Pasaule("Upes platums",
            Ievadi("", [
                {"jaut": "Tauriņa shēmā: krasta posms AB = 12 m, pretējais "
                         "CD = 30 m (paralēli). AO = 8 m. Cik m ir OD?",
                 "atb": ["20"], "padoms": "k = 2,5."},
                {"jaut": "Upes platums ir AD. Cik m?", "atb": ["28"],
                 "padoms": "8 + 20."},
            ]),
            pavediens="celojums",
            konteksts="Tūristi upes platumu mēra ar mietiņiem: veido tauriņu "
                      "ar paralēlām līnijām abos krastos.",
            kapec="Pāri upei nav jābrien - to izdara līdzība."),

    Kopsavilkums([
        "Atpazīstu paralēles, tauriņa un taisnleņķa zīmējumu.",
        "Pamatoju vienādos leņķus.",
        "Pierakstu līdzību pareizā secībā un aprēķinu malu.",
    ]),

    Majas([
        "Uzzīmē visus trīs zīmējumus un pieraksti pamatojumus.",
        "Tauriņš: AB = 3, CD = 7,5, OC = 5. Atrodi OB.",
        "Atrodi līdzīgus trijstūrus logā, jumtā vai tiltā.",
    ]),
]
