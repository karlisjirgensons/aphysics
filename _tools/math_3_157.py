# -*- coding: utf-8 -*-
"""3. klase, 157. stunda: «Kā sauc šo ķermeni?»

Pēdējā temata sākums: telpiskas figūras un to nosaukumi. Atšķirību starp
kubu un kvadrātu skolēni jauc bieži, tāpēc stunda sāk ar to, kas ķermeni
atšķir no plaknes figūras - tam ir tilpums.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, kermenis)

TEMA = "Kā sauc šo ķermeni?"

MERKIS = ("Atradīsim un nosauksim taisnstūru skaldni, kubu, piramīdu, "
          "cilindru un konusu.")

SATURS = [
    Sakums("Ar ko kubs atšķiras no kvadrāta?",
           zimejums=kermenis("kubs", virsraksts="kubs"),
           paraksts="Kubam ir tilpums, kvadrātam - tikai laukums.",
           fakti=["Plaknes figūru var uzzīmēt uz lapas, ķermeni - ne.",
                  "Ķermenim ir tilpums; tas aizņem vietu telpā."]),

    Doma("Ķermenis aizņem vietu telpā",
         "Kvadrāts ir plaknes figūra, kubs - telpiska; kubam katra skaldne "
         "ir kvadrāts.",
         soli=[
             "Paskaties, vai figūra ir plakana vai telpiska.",
             "Ja telpiska, apskati tās skaldnes.",
             "Ja visas skaldnes ir kvadrāti, tas ir kubs.",
             "Ja taisnstūri, tas ir taisnstūru skaldnis jeb kvadrs.",
         ],
         pieze="Cilindram un konusam nav skaldņu ar malām - to sāni ir "
               "izliekti, tāpēc tos no kociņiem uzbūvēt nevar."),

    Paraugs("Kurš ķermenis tas ir?",
            uzd="Ķermenim ir 6 skaldnes, un visas ir taisnstūri, bet ne "
                "kvadrāti. Kurš ķermenis tas ir?",
            soli=[
                ("6 skaldnes",
                 "Tik ir gan kubam, gan kvadram."),
                ("Skaldnes ir taisnstūri",
                 "Kubam tās būtu kvadrāti."),
                ("Tas ir taisnstūru skaldnis",
                 "To sauc arī par kvadru."),
            ],
            atbilde="taisnstūru skaldnis"),

    Ievadi("Ķermeņu nosaukumi", [
        {"jaut": "Cik skaldņu ir kubam?", "atb": ["6"],
         "padoms": "Augša, apakša un četri sāni."},
        {"jaut": "Cik skaldņu ir taisnstūru skaldnim?", "atb": ["6"],
         "padoms": "Tikpat, cik kubam."},
        {"jaut": "Cik plakanu skaldņu ir cilindram?", "atb": ["2"],
         "padoms": "Augšējais un apakšējais riņķis."},
        {"jaut": "Cik plakanu skaldņu ir konusam?", "atb": ["1"],
         "padoms": "Tikai pamats."},
        {"jaut": "Cik virsotņu ir kubam?", "atb": ["8"],
         "padoms": "Četras augšā, četras apakšā."},
        {"jaut": "Cik šķautņu ir kubam?", "atb": ["12"],
         "padoms": "Trīs grupas pa četrām."},
    ], pamats=4),

    Zimejums("Cilindrs un konuss",
             kermenis("konuss", virsraksts="konuss"),
             paskaidro="Konusam ir viena plakana skaldne - pamats - un viena "
                       "virsotne.",
             ievads="Ķermenis ar izliektu virsmu."),

    Varianti("Kurš ķermenis tas ir?", [
        {"jaut": "Ķermenim visas 6 skaldnes ir kvadrāti. Kurš tas ir?",
         "opcijas": ["Kubs", "Kvadrs", "Piramīda", "Cilindrs"],
         "pareizi": 0, "padoms": "Visas malas vienādas."},
        {"jaut": "Kuram ķermenim nav nevienas šķautnes?",
         "opcijas": ["Lodei", "Kubam", "Piramīdai", "Kvadram"],
         "pareizi": 0, "padoms": "Visa virsma ir izliekta."},
        {"jaut": "Ar ko kubs atšķiras no kvadrāta?",
         "opcijas": ["Kubam ir tilpums", "Kubs ir lielāks",
                     "Kubam ir vairāk malu", "Nekā"],
         "pareizi": 0, "padoms": "Viens ir telpisks, otrs plakans."},
        {"jaut": "Cik virsotņu ir konusam?",
         "opcijas": ["1", "0", "4", "8"],
         "pareizi": 0, "padoms": "Smaile augšā."},
    ], pamats=4),

    Pasaule("Kādas formas ir detaļas?",
            Ievadi("", [
                {"jaut": "Kastē 8 kubveida detaļas. Cik skaldņu tām kopā?",
                 "atb": ["48"], "padoms": "8 · 6."},
                {"jaut": "Cik šķautņu ir 8 kubiem?", "atb": ["96"],
                 "padoms": "8 · 12."},
                {"jaut": "Cik virsotņu ir 8 kubiem?", "atb": ["64"],
                 "padoms": "8 · 8."},
                {"jaut": "Kubs ar malu 3 cm. Cik kubikcentimetru ir tilpums?",
                 "atb": ["27"], "padoms": "3 · 3 · 3."},
            ]),
            pavediens="tehnika",
            konteksts="Ražošanā detaļu formas sauc precīzos vārdos - citādi "
                      "pasūtījumu nevar izpildīt.",
            kapec="«Kaste» var nozīmēt daudz ko; «kubs ar malu 3 cm» - tikai "
                  "vienu lietu."),

    Kopsavilkums([
        "Atpazīstu un nosaucu telpiskus ķermeņus.",
        "Zinu, ar ko kubs atšķiras no kvadrāta.",
        "Zinu, kuriem ķermeņiem ir izliekta virsma.",
        "Saskaitu skaldnes, šķautnes un virsotnes.",
    ]),

    Majas([
        "Atrodi mājās pa vienam katra ķermeņa piemēram.",
        "Nosauc tos pareizajos vārdos.",
        "Uzzīmē kubu un kvadrātu blakus un pastāsti atšķirību.",
    ]),
]
