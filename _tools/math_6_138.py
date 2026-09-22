# -*- coding: utf-8 -*-
"""6. klase, 138. stunda: «Kāda izteiksme atbilst aprakstam?»

No vārdiem uz izteiksmi. Apraksts te ir vispārīgs - «divu negatīvu skaitļu
summa, kas lielāka par −10» -, un atbilžu ir daudz. Tieši tāpēc šis uzdevums
prasa saprast, nevis atcerēties.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti)

TEMA = "Kāda izteiksme atbilst aprakstam?"

MERKIS = ("Veidosim izteiksmi pēc vispārīga apraksta par saskaitāmo zīmēm "
          "un summu.")

SATURS = [
    Sakums("Apraksts ir nosacījums, ne recepte",
           fakti=["«Divu negatīvu skaitļu summa» - abi ar mīnusu.",
                  "«Summa ir pozitīva» - lielākajam modulim jābūt pozitīvam.",
                  "Aprakstam parasti atbilst daudz izteiksmju."]),

    Doma("Vispirms zīmes, tad moduļi",
         "Izteiksmi pēc apraksta veido divos soļos: vispirms izvēlas "
         "saskaitāmo zīmes, tad moduļus tā, lai summa atbilstu nosacījumam.",
         soli=[
             "Izlasi aprakstu un pasvītro katru nosacījumu.",
             "Nosaki, kādas zīmes jābūt saskaitāmajiem.",
             "Izvēlies moduļus, lai summa iznāktu vajadzīgā.",
             "Pieraksti izteiksmi un izrēķini to.",
             "Pārbaudi visus nosacījumus.",
         ],
         pieze="Ja nosacījumi ir pretrunīgi, izteiksmes nav: «divu negatīvu "
               "skaitļu summa ir pozitīva» nav iespējama, jo divas bultiņas "
               "pa kreisi nekad neatgriežas pa labi."),

    Paraugs("Veido izteiksmi",
            uzd="Uzraksti divu skaitļu summu, kurā viens ir negatīvs, otrs "
                "pozitīvs, bet summa ir negatīva.",
            soli=[
                ("Zīmes: viens mīnuss, viens pluss",
                 "Tas ir dots."),
                ("Summa negatīva nozīmē: negatīvajam lielāks modulis",
                 "Garākā bultiņa nosaka virzienu."),
                ("Piemēram, −9 un 4",
                 "Moduļi 9 un 4."),
                ("−9 + 4 = −5",
                 "Nosacījumi izpildīti."),
            ],
            atbilde="piemēram, −9 + 4 = −5"),

    Ievadi("Pārbaudi nosacījumus", [
        {"jaut": "−9 + 4. Vai summa ir negatīva? Raksti «jā» vai «nē».",
         "atb": ["jā", "ja"], "padoms": "9 ir lielāks par 4."},
        {"jaut": "Cik ir −9 + 4?",
         "atb": ["-5", "−5"], "padoms": "9 − 4, zīme mīnus."},
        {"jaut": "−3 + 7. Vai summa ir pozitīva? Raksti «jā» vai «nē».",
         "atb": ["jā", "ja"], "padoms": "7 ir lielāks par 3."},
        {"jaut": "Vai divu negatīvu skaitļu summa var būt pozitīva? Raksti "
                 "«jā» vai «nē».",
         "atb": ["nē", "ne"], "padoms": "Abas bultiņas pa kreisi."},
        {"jaut": "Uzraksti negatīvu skaitli, kura summa ar 6 ir 0.",
         "atb": ["-6", "−6"], "padoms": "Pretējais skaitlis."},
        {"jaut": "Divu negatīvu skaitļu summa ir −10, viens no tiem ir −4. "
                 "Kāds ir otrs?",
         "atb": ["-6", "−6"], "padoms": "−10 − (−4)."},
    ], pamats=4),

    Varianti("Vai tāda izteiksme ir?", [
        {"jaut": "Divu negatīvu skaitļu summa var būt...",
         "opcijas": ["tikai negatīva", "pozitīva",
                     "nulle", "jebkāda"],
         "pareizi": 0,
         "padoms": "Abas bultiņas vienā virzienā."},
        {"jaut": "Lai summa būtu pozitīva, kad zīmes atšķiras, vajag...",
         "opcijas": ["pozitīvajam lielāku moduli",
                     "negatīvajam lielāku moduli",
                     "vienādus moduļus", "abus pozitīvus"],
         "pareizi": 0,
         "padoms": "Garākā bultiņa nosaka virzienu."},
        {"jaut": "Divu skaitļu summa ir nulle. Tie ir...",
         "opcijas": ["pretēji skaitļi", "abi nulles",
                     "abi pozitīvi", "abi negatīvi"],
         "pareizi": 0,
         "padoms": "Vienādi moduļi, dažādas zīmes."},
        {"jaut": "Kura izteiksme atbilst aprakstam «negatīvs plus pozitīvs, "
                 "summa negatīva»?",
         "opcijas": ["−8 + 3", "−3 + 8", "8 + 3", "−8 + (−3)"],
         "pareizi": 0,
         "padoms": "Negatīvajam lielāks modulis."},
    ], pamats=4),

    Petijums("Izdomā izteiksmes trim aprakstiem",
             vajag="burtnīca",
             soli=[
                 "Uzraksti izteiksmi, kuras summa ir negatīva, bet viens "
                 "saskaitāmais - pozitīvs.",
                 "Uzraksti izteiksmi ar trim saskaitāmajiem, kuras summa ir "
                 "nulle.",
                 "Uzraksti izteiksmi, kurai nav risinājuma, un paskaidro, "
                 "kāpēc.",
                 "Iedod visas trīs soļabiedram pārbaudei.",
             ],
             secinajums="Trešajam aprakstam izteiksmes nav - un to arī jāmāk "
                        "pamatot, nevis tikai pateikt."),

    Pasaule("Kāds bijis mēnesis?",
            Ievadi("", [
                {"jaut": "Mēneša rezultāts ir −50 €, ienākumi 200 €. Cik "
                         "eiro bija izdevumi?",
                 "atb": ["250"], "padoms": "200 + 50."},
                {"jaut": "Cits mēnesis: rezultāts 30 €, izdevumi 170 €. Cik "
                         "eiro bija ienākumi?",
                 "atb": ["200"], "padoms": "170 + 30."},
                {"jaut": "Vai rezultāts var būt pozitīvs, ja ir tikai "
                         "izdevumi? Raksti «jā» vai «nē».",
                 "atb": ["nē", "ne"], "padoms": "Visi saskaitāmie negatīvi."},
                {"jaut": "Ienākumi 150 €, izdevumi 150 €. Kāds ir rezultāts "
                         "eiro?",
                 "atb": ["0"], "padoms": "Pretēji skaitļi."},
            ]),
            pavediens="veikals",
            konteksts="Mēneša pārskatu var aprakstīt vārdos - un no tā "
                      "atjaunot skaitļus.",
            kapec="Apraksts par zīmēm pasaka, kāds rezultāts vispār "
                  "iespējams."),

    Kopsavilkums([
        "Veidoju izteiksmi pēc vispārīga apraksta.",
        "Vispirms izvēlos zīmes, tad moduļus.",
        "Pārbaudu visus nosacījumus.",
        "Pamatoju, kad aprakstam neatbilst neviena izteiksme.",
    ]),

    Majas([
        "Uzraksti izteiksmi, kuras summa ir −12 un viens saskaitāmais ir "
        "pozitīvs.",
        "Uzraksti trīs saskaitāmo summu, kas vienāda ar nulli.",
        "Izdomā aprakstu, kuram neatbilst neviena izteiksme.",
    ]),
]
