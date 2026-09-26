# -*- coding: utf-8 -*-
"""7. klase, 88. stunda: «Kas ir bisektrise, mediāna un augstums?»

Trīs svarīgas trijstūra līnijas, kas iziet no virsotnes: mediāna iet uz
pretējās malas viduspunktu, bisektrise dala leņķi uz pusēm, augstums ir
perpendikuls pret pretējo malu. Parastā trijstūrī tās ir trīs dažādas līnijas.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, geometrija)

TEMA = "Kas ir bisektrise, mediāna un augstums?"

MERKIS = ("Definēsim trijstūra bisektrisi, mediānu un augstumu un "
          "zīmēsim tās.")

_P = [("A", 0, 0), ("C", 8, 0), ("B", 2, 4)]


def _l(kura):
    """Viena no trim līnijām no virsotnes B."""
    if kura == "mediāna":
        p = _P + [("M", 4, 0, -90)]
        return geometrija(p, nogriezni=["AB", "BC", "CA"], izcelti=["BM"],
                          svitras=[("AM", 1), ("MC", 1)])
    if kura == "bisektrise":
        # Bisektrise dala pretējo malu attiecībā AL : LC = BA : BC.
        ba = (2 ** 2 + 4 ** 2) ** 0.5
        bc = (6 ** 2 + 4 ** 2) ** 0.5
        p = _P + [("L", 8 * ba / (ba + bc), 0, -90)]
        return geometrija(p, nogriezni=["AB", "BC", "CA"], izcelti=["BL"],
                          lenki=[("ABL", ""), ("LBC", "")])
    p = _P + [("H", 2, 0, -90)]
    return geometrija(p, nogriezni=["AB", "BC", "CA"], izcelti=["BH"],
                      taisni=["BHC"])


SATURS = [
    Sakums("Trīs ceļi no vienas virsotnes",
           zimejums=_l("mediāna"),
           paraksts="Mediāna BM - uz malas AC vidu.",
           fakti=["Mediāna dala malu uz pusēm.",
                  "Bisektrise dala leņķi uz pusēm.",
                  "Augstums krīt taisnā leņķī."]),

    Slidnis("Trīs līnijas", [
        {"v": "Mediāna", "teksts": "BM: AM = MC.", "zim": _l("mediāna")},
        {"v": "Bisektrise", "teksts": "BL: ∠ABL = ∠LBC.",
         "zim": _l("bisektrise")},
        {"v": "Augstums", "teksts": "BH ⊥ AC.", "zim": _l("augstums")},
    ], ievads="Viens un tas pats trijstūris - trīs dažādas līnijas."),

    Doma("Definīcijas",
         "Trijstūra mediāna ir nogrieznis, kas savieno virsotni ar pretējās "
         "malas viduspunktu. Bisektrise ir nogrieznis, kas dala trijstūra "
         "leņķi uz pusēm un iet līdz pretējai malai. Augstums ir perpendikuls, "
         "kas novilkts no virsotnes pret pretējo malu (vai tās pagarinājumu).",
         soli=[
             "Mediāna: atrodi malas viduspunktu un savieno ar virsotni.",
             "Bisektrise: sadali leņķi uz pusēm.",
             "Augstums: novelc perpendikulu pret malu.",
             "Katram trijstūrim ir 3 mediānas, 3 bisektrises, 3 augstumi.",
         ],
         pieze="Platleņķa trijstūrī divi augstumi krīt ārpus trijstūra - uz "
               "malu pagarinājumiem."),

    Paraugs("Nosaki līniju",
            uzd="△ABC: D ∈ AC, AD = DC. E ∈ AC, ∠ABE = ∠EBC. F ∈ AC, "
                "BF ⊥ AC. Nosauc BD, BE, BF.",
            soli=[
                ("BD: D - AC viduspunkts", "Mediāna."),
                ("BE: dala ∠B uz pusēm", "Bisektrise."),
                ("BF: perpendikuls pret AC", "Augstums."),
            ],
            atbilde="BD - mediāna, BE - bisektrise, BF - augstums."),

    Varianti("Kura līnija?", [
        {"jaut": "Nogrieznis no virsotnes līdz pretējās malas vidum",
         "opcijas": ["Mediāna", "Bisektrise", "Augstums", "Diagonāle"],
         "pareizi": 0, "padoms": "«Medius» - vidējais."},
        {"jaut": "Dala leņķi divos vienādos",
         "opcijas": ["Bisektrise", "Mediāna", "Augstums", "Viduslīnija"],
         "pareizi": 0, "padoms": "«Bi-» - divi."},
        {"jaut": "Veido 90° ar pretējo malu",
         "opcijas": ["Augstums", "Mediāna", "Bisektrise", "Mala"],
         "pareizi": 0, "padoms": "Perpendikuls."},
        {"jaut": "Mediāna BM, AC = 18 cm. Cik cm ir MC?",
         "opcijas": ["9", "18", "6", "36"],
         "pareizi": 0, "padoms": "Puse."},
    ], pamats=4),

    Pasaule("Līdzsvara punkts",
            Varianti("", [
                {"jaut": "Kartona trijstūri var noturēt uz zīmuļa gala "
                         "punktā, kur krustojas...",
                 "opcijas": ["mediānas", "augstumi", "bisektrises",
                             "malas"],
                 "pareizi": 0, "padoms": "Smaguma centrs."},
                {"jaut": "Kāpēc mediāna sadala trijstūri divos vienāda "
                         "laukuma trijstūros?",
                 "opcijas": ["Vienādi pamati un kopīgs augstums",
                             "Tie ir vienādi trijstūri",
                             "Tā ir bisektrise", "Nesadala"],
                 "pareizi": 0, "padoms": "Laukums = pamats · augstums : 2."},
                {"jaut": "Ja trijstūri piekar aiz virsotnes, mediāna no tās "
                         "virsotnes būs...",
                 "opcijas": ["vertikāla", "horizontāla", "slīpa 45°",
                             "neredzama"],
                 "pareizi": 0, "padoms": "Iet caur smaguma centru."},
            ]),
            pavediens="tehnika",
            konteksts="Inženieri smaguma centru meklē mediānu krustpunktā - "
                      "tā balansē dronus un tiltus.",
            kapec="Mediāna nav tikai līnija - tā dala masu."),

    Kopsavilkums([
        "Definēju mediānu, bisektrisi un augstumu.",
        "Zīmēju tās jebkurā trijstūrī.",
        "Atšķiru tās pēc definīcijas.",
        "Zinu, ka platleņķa trijstūrī augstums var krist ārpusē.",
    ]),

    Majas([
        "Uzzīmē trijstūri un visas 3 mediānas - vai tās krustojas vienā "
        "punktā?",
        "Izgriez trijstūri un atrodi līdzsvara punktu.",
        "Uzzīmē platleņķa trijstūri un visus 3 augstumus.",
    ]),
]
