# -*- coding: utf-8 -*-
"""7. klase, 33. stunda: «Kas ir teorēma un pierādījums?»

Teorēma ir apgalvojums, ko pierāda. Tai ir divas daļas: nosacījums
(«ja ...») un secinājums («tad ...»). Stunda iemāca no teksta izdalīt, kas
dots un kas jāpierāda - pirms jebkura pierādījuma pirmais solis.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, Zimejums, geometrija, restis)

TEMA = "Kas ir teorēma un pierādījums?"

MERKIS = ("Iemācīsimies atšķirt teorēmas nosacījumu no secinājuma un "
          "pierakstīt, kas dots un kas jāpierāda.")

SATURS = [
    Sakums("«Ja līst, tad ielas ir slapjas»",
           fakti=["«Ja līst» - nosacījums.",
                  "«Tad ielas ir slapjas» - secinājums.",
                  "Otrādi nav noteikti: ielas var būt slapjas no laistīšanas."]),

    Doma("Teorēma: ja (dots), tad (jāpierāda)",
         "Teorēma ir apgalvojums, kura patiesumu pamato ar pierādījumu. "
         "Teorēmā ir nosacījums (dots) un secinājums (jāpierāda). "
         "Pierādījums ir spriedumu virkne no dotā līdz secinājumam.",
         soli=[
             "Pārraksti teorēmu formā «ja ..., tad ...».",
             "Daļa aiz «ja» ir «dots».",
             "Daļa aiz «tad» ir «jāpierāda».",
             "Uzzīmē zīmējumu un atzīmē doto.",
         ],
         pieze="Apgrieztā teorēma samaina nosacījumu un secinājumu vietām. "
               "Tā var būt patiesa, bet var būt arī aplama."),

    Paraugs("Izdali doto un jāpierāda",
            uzd="Teorēma: «Ja punkts M ir nogriežņa AB viduspunkts un "
                "AB = 10 cm, tad AM = 5 cm.»",
            soli=[
                ("Dots: M - AB viduspunkts; AB = 10 cm", "Aiz «ja»."),
                ("Jāpierāda: AM = 5 cm", "Aiz «tad»."),
                ("AM = MB un AM + MB = AB", "(viduspunkta definīcija)"),
                ("2AM = 10, AM = 5 (cm)", "Secinājums pierādīts."),
            ],
            atbilde="Pierādīts."),

    Zimejums("Teorēma un apgrieztā teorēma",
             restis([["teorēma", "ja kvadrāts, tad taisnstūris"],
                     ["apgrieztā", "ja taisnstūris, tad kvadrāts"],
                     ["patiesa?", "pirmā - jā, otrā - nē"]]),
             paskaidro="Apgrieztā teorēma jāpārbauda atsevišķi."),

    Varianti("Nosacījums vai secinājums?", [
        {"jaut": "«Ja divi leņķi ir krustleņķi, tad tie ir vienādi.» Kas "
                 "ir dots?",
         "opcijas": ["Leņķi ir krustleņķi", "Leņķi ir vienādi",
                     "Abi", "Nekas"],
         "pareizi": 0,
         "padoms": "Aiz «ja»."},
        {"jaut": "«Vienādmalu trijstūrim visi leņķi ir vienādi.» Kā to "
                 "pārrakstīt ar «ja ..., tad ...»?",
         "opcijas": ["Ja trijstūris ir vienādmalu, tad tā leņķi ir vienādi",
                     "Ja leņķi ir vienādi, tad trijstūris ir vienādmalu",
                     "Ja trijstūris, tad vienādmalu",
                     "Ja leņķi, tad trijstūris"],
         "pareizi": 0,
         "padoms": "Par ko runā - tas ir nosacījums."},
        {"jaut": "Kura apgrieztā teorēma ir aplama?",
         "opcijas": ["«Ja skaitlis dalās ar 2, tad tas dalās ar 4»",
                     "«Ja skaitlis dalās ar 10, tad tas beidzas ar 0»",
                     "«Ja trijstūrim ir vienādas malas, tad vienādi leņķi»",
                     "«Ja M ∈ AB un AM = MB, tad M - viduspunkts»"],
         "pareizi": 0,
         "padoms": "6 dalās ar 2, bet ne ar 4."},
    ]),

    Pasaule("Viedā mājas automātika",
            Varianti("", [
                {"jaut": "Noteikums: «Ja temperatūra ir zem 19 °C, tad "
                         "ieslēdz apkuri.» Kas ir nosacījums?",
                 "opcijas": ["Temperatūra zem 19 °C", "Ieslēdz apkuri",
                             "19 °C", "Apkure"],
                 "pareizi": 0,
                 "padoms": "Aiz «ja»."},
                {"jaut": "Apkure ir ieslēgta. Vai noteikti ir zem 19 °C?",
                 "opcijas": ["Nē - to varēja ieslēgt ar roku",
                             "Jā, vienmēr", "Jā, ja ir ziema",
                             "Nē, tad ir 19 °C"],
                 "pareizi": 0,
                 "padoms": "Apgrieztais apgalvojums nav garantēts."},
                {"jaut": "Ir 17 °C. Ko secina automātika?",
                 "opcijas": ["Ieslēdz apkuri", "Izslēdz apkuri",
                             "Neko", "Atver logu"],
                 "pareizi": 0,
                 "padoms": "Nosacījums izpildās."},
            ]),
            pavediens="maja",
            konteksts="Viedās mājas lietotnēs noteikumus raksta tieši kā "
                      "teorēmas: «ja ..., tad ...».",
            kapec="Nosacījums un secinājums ir loģikas pamats."),

    Kopsavilkums([
        "Zinu, ka teorēma ir apgalvojums, kuru pierāda.",
        "Pārrakstu teorēmu «ja ..., tad ...» formā.",
        "Izdalu doto un jāpierādāmo.",
        "Zinu, ka apgrieztā teorēma var būt aplama.",
    ]),

    Majas([
        "Uzraksti 3 apgalvojumus «ja ..., tad ...» no ikdienas.",
        "Katram uzraksti apgriezto un pārbaudi, vai tas ir patiess.",
        "Izdali doto un jāpierāda teorēmā: «Ja B ∈ AC, tad AC > AB».",
    ]),
]
