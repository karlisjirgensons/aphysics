# -*- coding: utf-8 -*-
"""5. klase, 40. stunda: «Kad autobusi atkal satiksies?»

Mazākais kopīgais dalāmais dzīvē. Grūtākais te nav rēķins, bet atpazīšana:
uzdevumā par pieturu, dežūrām vai gaismas signāliem nekur nav rakstīts vārds
«dalāmais» - skolēnam pašam jāsaprot, ka runa ir par atkārtošanos.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kad autobusi atkal satiksies?"

MERKIS = ("Mācīsimies lietot mazāko kopīgo dalāmo sadzīves uzdevumos par "
          "ciklisku darbību sakritību.")

SATURS = [
    Sakums("Abi aizbrauc vienlaikus - kad tas atkārtosies?",
           fakti=["Pirmais autobuss no pieturas iet ik pēc 15 minūtēm.",
                  "Otrais - ik pēc 20 minūtēm.",
                  "Plkst. 8.00 abi aizbrauca kopā. Kad atkal?"]),

    Doma("Sakritība notiek mazākajā kopīgajā dalāmajā",
         "Ja divas lietas atkārtojas ik pēc sava laika, tās sakrīt ik pēc to "
         "mazākā kopīgā dalāmā.",
         soli=[
             "Izraksti abus atkārtošanās intervālus.",
             "Pārliecinies, ka tie ir vienā mērvienībā.",
             "Atrodi to mazāko kopīgo dalāmo.",
             "Pieskaiti to sākuma laikam.",
             "Pārbaudi: vai abi tiešām sanāk vienā brīdī?",
         ],
         pieze="Uzdevumā nekad nav rakstīts «atrodi mazāko kopīgo dalāmo». "
               "Pazīmes ir citas: «ik pēc», «katru trešo», «atkal kopā» - "
               "tur, kur kaut kas atkārtojas, tas arī slēpjas."),

    Paraugs("Kad autobusi satiksies?",
            uzd="Viens autobuss iet ik pēc 15 minūtēm, otrs ik pēc 20. "
                "Plkst. 8.00 abi aizbrauca kopā. Kad tas notiks nākamreiz?",
            soli=[
                ("15 = 3 · 5 un 20 = 2 · 2 · 5",
                 "Sadalām pirmreizinātājos."),
                ("Ņemam 2 · 2 · 3 · 5 = 60",
                 "Katru pirmskaitli tik reižu, cik vairāk."),
                ("Pēc 60 minūtēm, tas ir, pēc vienas stundas",
                 "Mazākais kopīgais dalāmais ir 60."),
                ("8.00 + 1 h = 9.00",
                 "Pieskaitām sākuma laikam."),
            ],
            atbilde="plkst. 9.00"),

    Ievadi("Pēc cik laika sakritīs?", [
        {"jaut": "Ik pēc 15 un ik pēc 20 minūtēm. Pēc cik minūtēm sakritīs?",
         "atb": ["60"], "padoms": "2 · 2 · 3 · 5."},
        {"jaut": "Ik pēc 4 un ik pēc 6 stundām. Pēc cik stundām?",
         "atb": ["12"], "padoms": "2 · 2 · 3."},
        {"jaut": "Ik pēc 10 un ik pēc 12 minūtēm. Pēc cik minūtēm?",
         "atb": ["60"], "padoms": "2 · 2 · 3 · 5."},
        {"jaut": "Divi draugi dežurē ik pēc 3 un ik pēc 4 dienām. Pēc cik "
                 "dienām abi dežurēs kopā?",
         "atb": ["12"], "padoms": "3 · 4, jo kopīgu dalītāju nav."},
        {"jaut": "Bākas uzliesmo ik pēc 6 un ik pēc 8 sekundēm. Pēc cik "
                 "sekundēm abas uzliesmos reizē?",
         "atb": ["24"], "padoms": "2 · 2 · 2 · 3."},
        {"jaut": "Ik pēc 5 un ik pēc 7 dienām. Pēc cik dienām?",
         "atb": ["35"], "padoms": "5 · 7."},
        {"jaut": "Ik pēc 9 un ik pēc 6 mēnešiem. Pēc cik mēnešiem?",
         "atb": ["18"], "padoms": "2 · 3 · 3."},
        {"jaut": "Trīs autobusi: ik pēc 4, 6 un 8 minūtēm. Pēc cik minūtēm "
                 "visi trīs sakritīs?",
         "atb": ["24"], "padoms": "2 · 2 · 2 · 3."},
    ], pamats=4,
        ievads="Vispirms atrodi intervālu mazāko kopīgo dalāmo."),

    Varianti("Kā atpazīt uzdevumu?", [
        {"jaut": "Kura frāze norāda uz mazāko kopīgo dalāmo?",
         "opcijas": ["«ik pēc ... un atkal kopā»",
                     "«par cik vairāk»",
                     "«cik kopā»",
                     "«cik reižu lielāks»"],
         "pareizi": 0,
         "padoms": "Meklē atkārtošanos."},
        {"jaut": "Autobusi iet ik pēc 15 un 20 minūtēm. Kāpēc atbilde nav "
                 "300?",
         "opcijas": ["300 ir kopīgais dalāmais, bet ne mazākais",
                     "300 nedalās ar 15",
                     "300 nedalās ar 20",
                     "Atbilde ir 300"],
         "pareizi": 0,
         "padoms": "15 · 20 = 300, bet jau 60 derēja."},
        {"jaut": "Viens autobuss iet ik pēc 10, otrs ik pēc 30 minūtēm. Pēc "
                 "cik minūtēm tie sakritīs?",
         "opcijas": ["30", "300", "40", "10"],
         "pareizi": 0,
         "padoms": "30 jau dalās ar 10."},
        {"jaut": "Ja abi intervāli doti dažādās mērvienībās, ko dara "
                 "vispirms?",
         "opcijas": ["Pārveido vienā mērvienībā", "Saskaita tos",
                     "Izvēlas lielāko", "Rēķina tāpat"],
         "pareizi": 0,
         "padoms": "1 stunda un 20 minūtes nav salīdzināmas tieši."},
    ], pamats=4),

    Pasaule("Kad izdevīgi doties ceļā?",
            Ievadi("", [
                {"jaut": "Vilciens iet ik pēc 40 minūtēm, autobuss ik pēc 60. "
                         "Pēc cik minūtēm abi būs stacijā kopā?",
                 "atb": ["120"], "padoms": "2 · 2 · 2 · 3 · 5."},
                {"jaut": "Cik tas ir stundās?", "atb": ["2"],
                 "padoms": "120 : 60."},
                {"jaut": "Prāmis iet ik pēc 3 stundām, vilciens ik pēc "
                         "4 stundām. Pēc cik stundām sakritīs?",
                 "atb": ["12"], "padoms": "3 · 4."},
                {"jaut": "Ja pirmais reiss ir plkst. 6.00, cikos notiks "
                         "nākamā sakritība? Raksti stundu skaitli.",
                 "atb": ["18"], "padoms": "6 + 12."},
            ]),
            pavediens="celojums",
            konteksts="Pārsēšanās plāno tieši tā: kad abi saraksti nākamreiz "
                      "satiekas vienā brīdī.",
            kapec="Sakritība atkārtojas ik pēc mazākā kopīgā dalāmā."),

    Kopsavilkums([
        "Atpazīstu uzdevumu, kurā jāmeklē mazākais kopīgais dalāmais.",
        "Atrodu to un pieskaitu sākuma laikam.",
        "Pārveidoju intervālus vienā mērvienībā, pirms rēķinu.",
        "Pārbaudu atbildi, skaitot abas virknes.",
    ]),

    Majas([
        "Uzraksti uzdevumu par divām lietām, kas atkārtojas, un atrisini to.",
        "Noskaidro, ik pēc cik minūtēm iet divi autobusi tavā pieturā, un "
        "aprēķini sakritību.",
        "Padomā, kāpēc divi reisi, kas reiz izgājuši kopā, kādreiz "
        "noteikti sakrīt atkal.",
    ]),
]
