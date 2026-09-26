# -*- coding: utf-8 -*-
"""4. klase, 56. stunda: «Kā mainās leņķa lielums?»

Leņķa modelis no divām sloksnītēm: viena mala nekustīga, otra griežas. Jo
tālāk griež, jo leņķis lielāks - neatkarīgi no malu garuma. Slīdnis ekrānā
dara to pašu, ko sloksnītes rokās.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, lenkis)

TEMA = "Kā mainās leņķa lielums?"

MERKIS = ("Ar leņķa modeli parādīsim leņķa palielināšanu un samazināšanu un "
          "saskatīsim nekustīgo un kustīgo malu.")

SATURS = [
    Sakums("Kā atveras klēpjdators?",
           zimejums=lenkis([(0, "klaviatūra"), (110, "ekrāns")],
                           loki=[(0, 110, "")]),
           paraksts="Ekrāns griežas, klaviatūra paliek uz galda.",
           fakti=["Viena mala nekustīga, otra griežas - leņķis mainās.",
                  "Klēpjdators parasti atveras līdz apmēram 135°."]),

    Doma("Leņķis aug, kad kustīgā mala griežas prom",
         "Leņķa lielums ir tas, cik tālu kustīgā mala pagriezusies no "
         "nekustīgās.",
         soli=[
             "Nekustīgā mala paliek vietā.",
             "Kustīgā mala griežas ap virsotni.",
             "Griežot prom - leņķis lielāks, griežot atpakaļ - mazāks.",
             "Malu garums leņķi nemaina.",
         ],
         pieze="Ja malas sakrīt, leņķis ir 0; ja veido taisni - izstiepts "
               "leņķis."),

    Slidnis("Griez kustīgo malu",
            soli=[
                {"v": "mazs leņķis", "teksts": "Mala tikko atvērusies.",
                 "zim": lenkis([(0, ""), (20, "")], loki=[(0, 20, "")])},
                {"v": "lielāks", "teksts": "Pagriezta tālāk.",
                 "zim": lenkis([(0, ""), (60, "")], loki=[(0, 60, "")])},
                {"v": "taisns leņķis", "teksts": "Malas perpendikulāras.",
                 "zim": lenkis([(0, ""), (90, "")], loki=[(0, 90, "")])},
                {"v": "plats leņķis", "teksts": "Vēl tālāk par taisnu.",
                 "zim": lenkis([(0, ""), (140, "")], loki=[(0, 140, "")])},
                {"v": "izstiepts leņķis", "teksts": "Malas vienā taisnē.",
                 "zim": lenkis([(0, ""), (180, "")], loki=[(0, 180, "")])},
            ],
            ievads="Spied soļus un skaties, kā aug leņķis."),

    Varianti("Lielāks vai mazāks?", [
        {"jaut": "Kustīgo malu pagriež tuvāk nekustīgajai. Leņķis...",
         "opcijas": ["samazinās", "palielinās", "nemainās"], "pareizi": 0,
         "padoms": "Malas tuvojas."},
        {"jaut": "Abas malas pagarina divreiz. Leņķis...",
         "opcijas": ["nemainās", "palielinās divreiz", "samazinās"],
         "pareizi": 0, "padoms": "Garums leņķi nemaina."},
        {"jaut": "Šķēres atver platāk. Leņķis starp asmeņiem...",
         "opcijas": ["palielinās", "samazinās", "nemainās"], "pareizi": 0,
         "padoms": "Asmeņi attālinās."},
        {"jaut": "Kurš leņķis ir lielāks - pulksteņa rādītāji plkst. 3 vai "
                 "plkst. 1?",
         "opcijas": ["plkst. 3", "plkst. 1", "vienādi"], "pareizi": 0,
         "padoms": "Plkst. 3 rādītāji ir tālāk viens no otra."},
    ], pamats=4),

    Ievadi("Pulksteņa leņķi", [
        {"jaut": "Minūšu rādītājs 60 minūtēs apiet visu apli. Cik minūtes "
                 "vajag ceturtdaļai apļa?", "atb": ["15"],
         "padoms": "60 : 4."},
        {"jaut": "Cik minūšu vajag pusei apļa?", "atb": ["30"],
         "padoms": "60 : 2."},
        {"jaut": "Ciparnīcā 12 skaitļi. Cik «stundu atstarpju» ir starp 12 un "
                 "3?", "atb": ["3"], "padoms": "12 → 1 → 2 → 3."},
        {"jaut": "Cik «stundu atstarpju» starp 12 un 6?", "atb": ["6"],
         "padoms": "Puse ciparnīcas."},
    ]),

    Pasaule("Paceļamais tilts",
            Varianti("", [
                {"jaut": "Paceļamā tilta puse griežas uz augšu. Kura mala "
                         "nekustīga?",
                 "opcijas": ["upes krasts (ceļš)", "tilta puse",
                             "abas kustas"], "pareizi": 0,
                 "padoms": "Krasts nekur neiet."},
                {"jaut": "Kuģim vajag lielāku atvērumu. Tilta leņķis "
                         "jā...",
                 "opcijas": ["palielina", "samazina", "nemaina"],
                 "pareizi": 0, "padoms": "Tilts jāpaceļ augstāk."},
                {"jaut": "Tilts pacēlies līdz vertikālai pozīcijai. Kāds "
                         "leņķis?",
                 "opcijas": ["taisns", "šaurs", "izstiepts"], "pareizi": 0,
                 "padoms": "Perpendikulāri ceļam."},
            ]),
            pavediens="tehnika",
            konteksts="Londonas Tauera tilts paceļas, lai zem tā izbrauktu "
                      "lieli kuģi.",
            kapec="Leņķa lielums nosaka, vai kuģis tiks cauri."),

    Petijums("Sloksnīšu modelis",
             soli=[
                 "Izgriez divas kartona sloksnītes.",
                 "Savieno galus ar spraudīti - tā ir virsotne.",
                 "Vienu sloksnīti turi, otru griez - vēro, kā leņķis mainās.",
                 "Pagarini vienu sloksnīti ar citu: vai leņķis mainījās?",
             ],
             vajag="kartons, šķēres, spraudīte",
             secinajums="Leņķis mainās tikai griežot, nevis pagarinot."),

    Kopsavilkums([
        "Parādu leņķa palielināšanu un samazināšanu.",
        "Nosaucu nekustīgo un kustīgo malu.",
        "Zinu, ka malu garums leņķi nemaina.",
    ]),

    Majas([
        "Pavēro durvis: kā mainās leņķis, tās atverot?",
        "Uztaisi sloksnīšu modeli mājās un parādi mājiniekiem.",
        "Atrodi pulkstenī laiku, kad rādītāji veido izstieptu leņķi.",
    ]),
]
