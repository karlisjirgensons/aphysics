# -*- coding: utf-8 -*-
"""4. klase, 16. stunda: «Kurš darbības loceklis pazudis?»

Nezināmo locekli atrod, ja zina, ko nozīmē summa un starpība: summa ir
viss, saskaitāmie ir daļas. Stunda to rāda ar joslu - vesels un divi
gabali - un tā pati josla vēlāk strādās daļām un vienādojumiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kurš darbības loceklis pazudis?"

MERKIS = ("Aprēķināsim nezināmo saskaitāmo, mazināmo un atņēmēju, lietojot "
          "jēdzienus summa un starpība.")

SATURS = [
    Sakums("Cik lappušu vēl jāizlasa?",
           zimejums=restis([["visa grāmata", "1200 lpp."],
                            ["izlasītas", "750 lpp."],
                            ["atlikušas", None]],
                           "viss un daļas"),
           paraksts="Ja zina visu un vienu daļu, otru atrod ar atņemšanu.",
           fakti=["Summa ir viss, saskaitāmie - tā daļas.",
                  "Trūkstošo daļu atrod: viss mīnus zināmā daļa."]),

    Doma("Viss = daļa + daļa",
         "Ja nezināms ir saskaitāmais, no summas atņem otru saskaitāmo; ja "
         "nezināms ir mazināmais, starpībai pieskaita atņēmēju.",
         soli=[
             "☐ + 750 = 1200 → ☐ = 1200 − 750.",
             "☐ − 450 = 2300 → ☐ = 2300 + 450 (mazināmais ir viss).",
             "5000 − ☐ = 3200 → ☐ = 5000 − 3200.",
             "Pārbaudi: ieliec atrasto skaitli sākotnējā vienādībā.",
         ],
         pieze="Nezināmo bieži apzīmē ar burtu: x + 750 = 1200."),

    Paraugs("x − 1850 = 4300",
            uzd="Atrodi mazināmo: x − 1850 = 4300.",
            soli=[
                ("x ir viss", "No tā atņēma 1850 un palika 4300."),
                ("x = 4300 + 1850", "Viss = palikušais + atņemtais."),
                ("x = 6150", None),
                ("6150 − 1850 = 4300", "Pārbaude sakrīt."),
            ],
            atbilde="x = 6150"),

    Zimejums("Josla palīdz",
             restis([["viss (mazināmais)", "x"],
                     ["atņemtais", "1850"],
                     ["palikušais", "4300"]],
                    "x − 1850 = 4300"),
             paskaidro="Viss ir atņemtais kopā ar palikušo: "
                       "x = 1850 + 4300.",
             ievads="Uzzīmē joslu, un darbība kļūst redzama."),

    Ievadi("Atrodi x", [
        {"jaut": "x + 2500 = 7000", "atb": ["4500"],
         "padoms": "7000 − 2500."},
        {"jaut": "3400 + x = 5100", "atb": ["1700"],
         "padoms": "5100 − 3400."},
        {"jaut": "x − 1200 = 3600", "atb": ["4800"],
         "padoms": "3600 + 1200."},
        {"jaut": "8000 − x = 2750", "atb": ["5250"],
         "padoms": "8000 − 2750."},
        {"jaut": "x + 999 = 10 000", "atb": ["9001"],
         "padoms": "10 000 − 999."},
        {"jaut": "6420 − x = 6420", "atb": ["0"],
         "padoms": "Neko neatņēma."},
    ], pamats=4,
        ievads="Ieraksti tikai x vērtību."),

    Varianti("Kura darbība?", [
        {"jaut": "x + 450 = 900. Kā atrast x?",
         "opcijas": ["900 − 450", "900 + 450", "450 − 900", "900 · 450"],
         "pareizi": 0, "padoms": "Nezināms saskaitāmais."},
        {"jaut": "x − 300 = 700. Kā atrast x?",
         "opcijas": ["700 + 300", "700 − 300", "300 − 700", "700 : 300"],
         "pareizi": 0, "padoms": "Nezināms mazināmais - viss."},
        {"jaut": "1000 − x = 400. Kā atrast x?",
         "opcijas": ["1000 − 400", "1000 + 400", "400 − 1000",
                     "400 + 400"], "pareizi": 0,
         "padoms": "Nezināms atņēmējs."},
        {"jaut": "Kas ir summa vienādībā 350 + 650 = 1000?",
         "opcijas": ["1000", "350", "650", "350 un 650"], "pareizi": 0,
         "padoms": "Summa ir rezultāts - viss."},
    ], pamats=4),

    Pasaule("Kosmosa misija",
            Ievadi("", [
                {"jaut": "Raķetei jāpaceļas 9000 m augstumā. Tā jau ir "
                         "6250 m. Cik vēl jākāpj?",
                 "atb": ["2750"], "padoms": "6250 + x = 9000."},
                {"jaut": "Pēc 3200 m nolaišanās raķete bija 4800 m. Kādā "
                         "augstumā tā bija pirms tam?",
                 "atb": ["8000"], "padoms": "x − 3200 = 4800."},
                {"jaut": "Degvielas tvertnē bija 7000 l, palika 1850 l. Cik "
                         "sadedzināja?",
                 "atb": ["5150"], "padoms": "7000 − x = 1850."},
                {"jaut": "Divās pakāpēs kopā 8600 kg degvielas; pirmajā "
                         "5900 kg. Cik otrajā?",
                 "atb": ["2700"], "padoms": "8600 − 5900."},
            ]),
            pavediens="kosmoss",
            konteksts="Misijas vadība visu laiku rēķina «cik vēl trūkst» - "
                      "tas ir nezināmais saskaitāmais.",
            kapec="Katrs «cik vēl» jautājums ir vienādība ar nezināmo."),

    Kopsavilkums([
        "Atrodu nezināmo saskaitāmo ar atņemšanu.",
        "Atrodu nezināmo mazināmo ar saskaitīšanu.",
        "Atrodu nezināmo atņēmēju ar atņemšanu.",
        "Pārbaudu, ieliekot atbildi vienādībā.",
    ]),

    Majas([
        "Izdomā «cik vēl trūkst» uzdevumu par savu krājkasīti un pieraksti "
        "to ar x.",
        "Uzzīmē joslu vienādībai x − 250 = 750 un atrisini.",
        "Pajautā mājiniekiem, cik lappušu vēl jāizlasa grāmatā, ko viņi lasa.",
    ]),
]
