# -*- coding: utf-8 -*-
"""7. klase, 34. stunda: «Kā uzbūvēt divu soļu pamatojumu?»

Pirmais īstais pierādījums: divi spriedumi, kur otrais lieto pirmā
rezultātu. Klasiskais piemērs - ja AB = CD un visi punkti ir uz vienas
taisnes, tad AC = BD, jo no vienādiem nogriežņiem atņem vai pieskaita
kopīgo daļu.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, Zimejums, geometrija)

TEMA = "Kā uzbūvēt divu soļu pamatojumu?"

MERKIS = ("Veidosim pamatojumu no diviem saistītiem spriedumiem par "
          "nogriežņu vienādību.")

_ABCD = geometrija([("A", 0, 0), ("B", 3, 0), ("C", 7, 0), ("D", 10, 0)],
                   nogriezni=["AD"], svitras=[("AB", 1), ("CD", 1)])

SATURS = [
    Sakums("Vienādi gali - vienādi nogriežņi",
           zimejums=_ABCD,
           paraksts="AB = CD. Vai AC = BD?",
           fakti=["Abiem nogriežņiem AC un BD ir kopīga daļa BC.",
                  "Katram pievienots vēl viens vienāds gals.",
                  "Tātad tie ir vienādi - to var pierādīt divos soļos."]),

    Doma("Pirmais solis sagatavo otro",
         "Divu soļu pamatojumā pirmais spriedums iegūst jaunu faktu no dotā, "
         "bet otrais lieto šo faktu, lai nonāktu pie secinājuma.",
         soli=[
             "Uzraksti doto un jāpierādāmo.",
             "Jautā: kas man jāzina, lai pierādītu secinājumu?",
             "1. solis: iegūsti to no dotā (ar pamatojumu).",
             "2. solis: no 1. soļa secini jāpierādāmo.",
         ],
         pieze="Spriešana no beigām («kas man vajadzīgs?») palīdz atrast "
               "pirmo soli."),

    Paraugs("Pierādi, ka AC = BD",
            uzd="Punkti A, B, C, D atrodas uz taisnes šādā secībā. AB = CD. "
                "Pierādi, ka AC = BD.",
            soli=[
                ("Dots: A, B, C, D uz taisnes; AB = CD. Jāpierāda: AC = BD",
                 "Sākums."),
                ("AC = AB + BC", "(B ∈ AC)"),
                ("BD = BC + CD", "(C ∈ BD)"),
                ("AB + BC = CD + BC", "(AB = CD - dots)"),
                ("AC = BD", "(abu labās puses vienādas)"),
            ],
            atbilde="AC = BD - pierādīts."),

    Zimejums("Otrādi: no vienādiem atņem kopīgo",
             geometrija([("A", 0, 0), ("B", 3, 0), ("C", 7, 0),
                         ("D", 10, 0)],
                        nogriezni=["AD"], izcelti=["BC"]),
             paskaidro="Ja AC = BD, tad AB = AC − BC = BD − BC = CD."),

    Varianti("Sakārto pierādījumu", [
        {"jaut": "Dots: M - AB viduspunkts, N - CD viduspunkts, AB = CD. "
                 "Jāpierāda: AM = CN. Kāds ir pirmais solis?",
         "opcijas": ["AM = {1|2}AB (M - viduspunkts)",
                     "AM = CN (jo jāpierāda)",
                     "AB = CD (dots), tātad AM = CN uzreiz",
                     "CN = CD"],
         "pareizi": 0,
         "padoms": "Vispirms izsaki AM ar AB."},
        {"jaut": "Kāds ir otrais solis?",
         "opcijas": ["CN = {1|2}CD, un {1|2}AB = {1|2}CD, jo AB = CD",
                     "CN = CD",
                     "AM = MB",
                     "Pierādīts bez otra soļa"],
         "pareizi": 0,
         "padoms": "Pusītes no vienādiem ir vienādas."},
        {"jaut": "Kurš no šiem nav derīgs pamatojums?",
         "opcijas": ["(no zīmējuma izskatās vienādi)",
                     "(B ∈ AC)", "(M - viduspunkts)", "(dots)"],
         "pareizi": 0,
         "padoms": "Zīmējums var maldināt."},
    ]),

    Pasaule("Plaukta montāža",
            Varianti("", [
                {"jaut": "Dēlis 120 cm. No abiem galiem vienādā attālumā "
                         "ieskrūvē kronšteinus. Kāpēc attālumi no "
                         "kronšteiniem līdz pretējiem galiem ir vienādi?",
                 "opcijas": ["Jo katrs ir 120 cm mīnus vienāds gabals",
                             "Jo dēlis ir taisns", "Jo skrūves vienādas",
                             "Nav vienādi"],
                 "pareizi": 0,
                 "padoms": "Tā pati AC = BD teorēma."},
                {"jaut": "Kronšteini 20 cm no galiem. Cik cm no kreisā "
                         "kronšteina līdz labajam galam?",
                 "opcijas": ["100 cm", "80 cm", "120 cm", "20 cm"],
                 "pareizi": 0,
                 "padoms": "120 − 20."},
                {"jaut": "Cik cm ir starp kronšteiniem?",
                 "opcijas": ["80 cm", "100 cm", "40 cm", "60 cm"],
                 "pareizi": 0,
                 "padoms": "120 − 20 − 20."},
            ]),
            pavediens="maja",
            konteksts="Galdnieks liek kronšteinus simetriski - un matemātika "
                      "garantē vienādus attālumus.",
            kapec="Divi soļi: atņem vienādu no vienāda."),

    Kopsavilkums([
        "Veidoju divu soļu pamatojumu.",
        "Atrodu pirmo soli, spriežot no beigām.",
        "Pamatoju katru soli ar definīciju vai doto.",
        "Zinu, ka «izskatās» nav pamatojums.",
    ]),

    Majas([
        "Pierādi: ja AC = BD (A, B, C, D uz taisnes), tad AB = CD.",
        "Uzraksti savu divu soļu uzdevumu ar viduspunktiem.",
        "Paskaidro pierādījumu kādam mājās.",
    ]),
]
