# -*- coding: utf-8 -*-
"""9. klase, 14. stunda: «Kā izmērīt koka augstumu?»

Trīs lauka metodes ar līdzību: ēna, spogulis uz zemes un mietiņš, pār kuru
skatās uz galotni. Katrā ir divi taisnleņķa trijstūri ar vienu vienādu
šauro leņķi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, geometrija)

TEMA = "Kā izmērīt koka augstumu?"

MERKIS = ("Risināsim praktisku uzdevumu par augstumu vai attālumu, lietojot "
          "līdzību.")

# Spoguļa metode: acis E virs punkta P, spogulis M uz zemes, koks TK.
_SPOGULIS = geometrija([("P", 0, 0), ("E", 0, 3.2), ("M", 4, 0, -90),
                        ("K", 19, 0), ("T", 19, 12)],
                       nogriezni=["PK", "PE", "KT"],
                       izcelti=["EM", "MT"], taisni=["EPM", "MKT"],
                       lenki=[("PME", "", 1), ("KMT", "", 1)],
                       malas=[("PE", "1,6 m"), ("PM", "2 m"),
                              ("MK", "12 m")])

_ENA = geometrija([("A", 0, 0), ("B", 0, 8), ("C", 12, 0), ("D", 16, 0),
                   ("E", 16, 2), ("F", 19, 0)],
                  nogriezni=["AB", "BC", "AC", "DE", "EF", "DF"],
                  taisni=["BAC", "EDF"], lenki=[("ACB", "", 1),
                                                ("DFE", "", 1)],
                  malas=[("AB", "h"), ("AC", "12 m"), ("DE", "2 m"),
                         ("DF", "3 m")])

SATURS = [
    Sakums("Cik augsts ir skolas pagalma koks?",
           zimejums=_SPOGULIS,
           paraksts="Spogulis uz zemes: krišanas leņķis = atstarošanas leņķis.",
           fakti=["Kāpt kokā nevajag - pietiek ar mērlenti.",
                  "Divi taisnleņķa trijstūri ar vienādu šauro leņķi.",
                  "Tātad tie ir līdzīgi: {h|1,6} = {12|2}."]),

    Slidnis("Trīs metodes", [
        {"v": "Ēna", "teksts": "Saules stari paralēli: {h|12} = {2|3}, h = 8 m",
         "zim": _ENA},
        {"v": "Spogulis", "teksts": "{h|1,6} = {12|2}, h = 9,6 m",
         "zim": _SPOGULIS},
    ], ievads="Katrā metodē atrodi divus līdzīgus trijstūrus."),

    Doma("Mērījuma plāns",
         "Atrodi divus taisnleņķa trijstūrus ar vienādu šauro leņķi: vienā "
         "viss izmērāms, otrā - meklētais augstums.",
         soli=[
             "Uzzīmē skici un atzīmē taisnos leņķus.",
             "Pamato vienādo šauro leņķi (paralēli stari, spogulis).",
             "Izmēri trīs garumus.",
             "Sastādi proporciju un aprēķini; noapaļo saprātīgi.",
         ]),

    Petijums("Mēram pagalmā", [
        "Noliec spoguli uz zemes vairākus metrus no koka.",
        "Atkāpies, līdz spogulī redzi koka galotni.",
        "Izmēri: acu augstumu, attālumu līdz spogulim, spoguļa attālumu līdz "
        "kokam.",
        "Aprēķini augstumu. Atkārto ar ēnas metodi un salīdzini.",
    ], vajag="mērlente, neliels spogulis, saulaina diena",
       secinajums="Abas metodes dod tuvus rezultātus - kļūda ir mērījumos, "
                  "nevis līdzībā."),

    Ievadi("Aprēķini augstumu", [
        {"jaut": "Ēna: nūja 1 m met 1,5 m ēnu, masts - 18 m ēnu. Masts (m)?",
         "atb": ["12"], "padoms": "{h|18} = {1|1,5}."},
        {"jaut": "Spogulis: acis 1,5 m, līdz spogulim 2 m, spogulis līdz "
                 "kokam 10 m. Koks (m)?", "atb": ["7,5"],
         "padoms": "{h|1,5} = {10|2}."},
        {"jaut": "Cilvēks 1,7 m met 2 m ēnu. Laterna met 5 m ēnu. Laterna "
                 "(m)?", "atb": ["4,25"], "padoms": "{h|5} = {1,7|2}."},
        {"jaut": "Tornis 30 m met 45 m ēnu. Cik m ēnu tajā brīdī met 1,6 m "
                 "garš skolēns?", "atb": ["2,4"], "padoms": "k = 1,5."},
    ]),

    Varianti("Kas jāpamato?", [
        {"jaut": "Kāpēc ēnas metodē trijstūri ir līdzīgi?",
         "opcijas": ["Taisns leņķis un vienāds saules staru leņķis",
                     "Ēnas ir vienādas", "Koks un nūja ir paralēli",
                     "Tā vienmēr ir"],
         "pareizi": 0, "padoms": "Divi leņķi."},
        {"jaut": "Mākoņainā dienā derēs...",
         "opcijas": ["spoguļa metode", "ēnas metode", "neviena",
                     "tikai kāpšana kokā"],
         "pareizi": 0, "padoms": "Ēnas nav."},
    ]),

    Pasaule("Baznīcas tornis",
            Ievadi("", [
                {"jaut": "Torņa ēna 36 m, 2 m mietiņa ēna 1,5 m. Augstums (m)?",
                 "atb": ["48"], "padoms": "{h|36} = {2|1,5}."},
                {"jaut": "Pēc stundas mietiņa ēna ir 2 m. Torņa ēna (m)?",
                 "atb": ["48"], "padoms": "Ēna = augstums, k = 1."},
            ]),
            pavediens="celojums",
            konteksts="Senie ceļotāji torņu augstumu noteica pēc ēnas - "
                      "arī Taless Ēģiptē.",
            kapec="Līdzība ļauj izmērīt nesasniedzamo."),

    Kopsavilkums([
        "Izmēru augstumu ar ēnas un spoguļa metodi.",
        "Pamatoju trijstūru līdzību praktiskā situācijā.",
        "Novērtēju mērījuma precizitāti.",
    ]),

    Majas([
        "Izmēri savas mājas vai laternas augstumu ar vienu metodi.",
        "Uzzīmē skici un pieraksti proporciju.",
        "Padomā, kā izmērīt upes platumu ar līdzību.",
    ]),
]
