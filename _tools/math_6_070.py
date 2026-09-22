# -*- coding: utf-8 -*-
"""6. klase, 70. stunda: «Cik kubu ietilpst ķermenī?»

Jauns mikrotemats. Tilpums te vēl nav formula - tas ir skaits. Skolēns
saskaita kubus slānī, tad slāņus, un no šīs skaitīšanas nākamajā stundā pati
no sevis izaug formula.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         kermenis, restis)

TEMA = "Cik kubu ietilpst ķermenī?"

MERKIS = ("Noteiksim ķermeņa tilpumu kā vienības kubu skaitu un veidosim "
          "izteiksmi.")

SATURS = [
    Sakums("Tilpums ir skaits, ne formula",
           zimejums=restis([["", "", "", ""],
                            ["", "", "", ""],
                            ["", "", "", ""]],
                           "viens slānis: 4 · 3 = 12 kubi"),
           paraksts="Ja tādu slāņu ir divi, kubu kopā ir 24.",
           fakti=["Vienības kubs ir kubs ar šķautni 1 - tas ir mērs.",
                  "Tilpums ir tas, cik tādu kubu ietilpst ķermenī.",
                  "Ērtāk skaitīt pa slāņiem, nevis pa vienam."]),

    Doma("Slānis, tad slāņu skaits",
         "Kvadra tilpumu atrod, saskaitot kubus vienā slānī un reizinot ar "
         "slāņu skaitu.",
         soli=[
             "Saskaiti kubus vienā rindā - tas ir garums.",
             "Saskaiti rindas slānī - tas ir platums.",
             "Reizini: tik kubu ir vienā slānī.",
             "Saskaiti slāņus - tas ir augstums.",
             "Reizini slāņa kubu skaitu ar slāņu skaitu.",
         ],
         pieze="Izteiksmi raksta tieši tādā kārtībā, kā skaitīja: "
               "(4 · 3) · 2. Iekavas parāda, ka vispirms bija slānis, tikai "
               "tad - slāņu skaits."),

    Paraugs("Saskaiti kubus kastē",
            uzd="Kastē kubi salikti 4 rindās pa 3, un tādu slāņu ir 2. Cik "
                "kubu ir kopā?",
            soli=[
                ("Vienā rindā 4 kubi",
                 "Tas ir garums."),
                ("Rindu slānī ir 3",
                 "Tas ir platums."),
                ("4 · 3 = 12 kubi slānī",
                 "Viens slānis."),
                ("Slāņu ir 2",
                 "Tas ir augstums."),
                ("12 · 2 = 24 kubi",
                 "Tilpums vienības kubos."),
            ],
            atbilde="24 vienības kubi"),

    Ievadi("Saskaiti kubus", [
        {"jaut": "Slānī 5 rindas pa 4 kubiem. Cik kubu ir slānī?",
         "atb": ["20"], "padoms": "5 · 4."},
        {"jaut": "Tādu slāņu ir 3. Cik kubu ir kopā?",
         "atb": ["60"], "padoms": "20 · 3."},
        {"jaut": "Kastē 6 x 2 x 4 kubi. Cik kubu ir kopā?",
         "atb": ["48"], "padoms": "12 · 4."},
        {"jaut": "Kubā 3 x 3 x 3. Cik vienības kubu ir kopā?",
         "atb": ["27"], "padoms": "9 · 3."},
        {"jaut": "Kastē ir 36 kubi, slānī 12. Cik slāņu ir kastē?",
         "atb": ["3"], "padoms": "36 : 12."},
        {"jaut": "Kastē ir 40 kubi, slāņu ir 5. Cik kubu ir vienā slānī?",
         "atb": ["8"], "padoms": "40 : 5."},
    ], pamats=4),

    Petijums("Saliec kasti no kubiem",
             vajag="kubiņi vai cukurgraudi un maza kastīte",
             soli=[
                 "Izliec kastītes apakšu ar kubiem vienā slānī.",
                 "Saskaiti, cik kubu bija vajadzīgi.",
                 "Skaiti, cik tādu slāņu ietilpst kastītē.",
                 "Reizini un pieraksti tilpumu.",
                 "Pārbaudi, izmērot kastītes izmērus ar lineālu.",
             ],
             secinajums="Kubu skaits sakrīt ar trīs izmēru reizinājumu - "
                        "tieši no tā nākamajā stundā izaugs formula."),

    Varianti("Kā skaitīt ātrāk?", [
        {"jaut": "Kā ātrāk saskaitīt kubus kastē?",
         "opcijas": ["Pa slāņiem", "Pa vienam",
                     "Pa diagonālēm", "Nav iespējams"],
         "pareizi": 0,
         "padoms": "Slānis ir reizinājums."},
        {"jaut": "Kubā 4 x 4 x 4 ir cik vienības kubu?",
         "opcijas": ["64", "16", "12", "48"],
         "pareizi": 0,
         "padoms": "16 · 4."},
        {"jaut": "Ko nozīmē «vienības kubs»?",
         "opcijas": ["Kubu ar šķautni 1", "Jebkuru kubu",
                     "Kubu ar tilpumu 10", "Kastes apakšu"],
         "pareizi": 0,
         "padoms": "Tas ir tilpuma mērs."},
        {"jaut": "Kastē 3 x 5 x 2. Kura izteiksme atbilst skaitīšanai pa "
                 "slāņiem?",
         "opcijas": ["(3 · 5) · 2", "3 + 5 + 2", "3 · (5 + 2)", "30 : 2"],
         "pareizi": 0,
         "padoms": "Vispirms slānis."},
    ], pamats=4),

    Pasaule("Cik kastu ietilpst noliktavā?",
            Ievadi("", [
                {"jaut": "Plauktā 8 kastes rindā un 4 rindas. Cik kastu ir "
                         "vienā slānī?",
                 "atb": ["32"], "padoms": "8 · 4."},
                {"jaut": "Plauktu ir 3. Cik kastu ietilpst kopā?",
                 "atb": ["96"], "padoms": "32 · 3."},
                {"jaut": "Noliktavā ir 5 tādi plaukti. Cik kastu ietilpst?",
                 "atb": ["480"], "padoms": "96 · 5."},
                {"jaut": "Cik kastu paliktu, ja viens plaukts būtu tukšs?",
                 "atb": ["384"], "padoms": "480 − 96."},
            ]),
            pavediens="tehnika",
            konteksts="Noliktavā ietilpību rēķina tieši tā: kastes slānī "
                      "reiz slāņu skaits.",
            kapec="Tilpums ir skaits - tāpēc to var pārbaudīt, saskaitot."),

    Zimejums("Kaste kā kubu kaudze",
             kermenis("kvadrs"),
             paskaidro="Ja katra šķautne ir sadalīta vienību daļās, kaste "
                       "sadalās tieši tik kubiņos, cik ir izmēru "
                       "reizinājums.",
             ievads="Tas pats kvadrs, ko zīmējām iepriekš."),

    Kopsavilkums([
        "Nosaku tilpumu kā vienības kubu skaitu.",
        "Skaitu pa slāņiem: vispirms slānis, tad slāņu skaits.",
        "Veidoju izteiksmi tādā kārtībā, kā skaitīju.",
        "Atrodu trūkstošo skaitli, ja tilpums ir zināms.",
    ]),

    Majas([
        "Saskaiti, cik kubiņu ietilptu tavā pildspalvu kārbiņā.",
        "Uzzīmē kasti 5 x 3 x 2 un saskaiti tās tilpumu.",
        "Pieraksti izteiksmi ar iekavām, kas parāda skaitīšanas kārtību.",
    ]),
]
