# -*- coding: utf-8 -*-
"""5. klase, 94. stunda: «Kur uz skaitļu taisnes ir jaukts skaitlis?»

Trešā pārveidošanas stunda, bet ar zīmuli rokā. Jauktu skaitli atlikt ir
vieglāk nekā neīstu daļu: veselā daļa uzreiz pasaka, starp kuriem veseliem
skaitļiem meklēt. Otra stundas puse ir tas, ko skolēni parasti izlaiž -
taisni ar piemērotu iedaļu vajag uzzīmēt pašam.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         taisne)

TEMA = "Kur uz skaitļu taisnes ir jaukts skaitlis?"

MERKIS = ("Mācīsimies atlikt jauktus skaitļus uz skaitļu taisnes un uzzīmēt "
          "piemērotu taisni pašiem.")

SATURS = [
    Sakums("Starp diviem veseliem",
           zimejums=taisne(0, 3, 1, [(1.5, "1 1/2"), (2.25, "2 1/4")],
                           virsraksts="Divi jaukti skaitļi"),
           paraksts="1{1|2} ir starp 1 un 2, bet 2{1|4} - starp 2 un 3.",
           fakti=["Veselā daļa pasaka, starp kuriem veseliem meklēt.",
                  "Daļa pasaka, cik tālu no kreisā vesela.",
                  "Tāpēc jauktu skaitli atlikt ir ātrāk nekā neīstu daļu."]),

    Doma("Vispirms atrodi veselo, tad daļu",
         "Jauktu skaitli atliek divos soļos: atrod tā veselo daļu uz taisnes "
         "un no tās virzās pa labi par daļas lielumu.",
         soli=[
             "Atrodi uz taisnes jauktā skaitļa veselo daļu.",
             "Sadali nākamo vienību tik daļās, cik rāda saucējs.",
             "Skaiti pa labi tik daļas, cik rāda skaitītājs.",
             "Atzīmē punktu un pieraksti pie tā skaitli.",
             "Pārbaudi: punktam jābūt starp diviem veseliem.",
         ],
         pieze="Iedaļu izvēlas pēc saucēja. Ja jāatliek 1{1|2} un 2{1|4}, "
               "ērtāk ir sadalīt vienību ceturtdaļās: tad abi punkti "
               "iekrīt iedaļās."),

    Paraugs("Atliec 2{1|4} uz taisnes",
            uzd="Uzzīmē taisni no 0 līdz 3 un atzīmē uz tās 2{1|4}.",
            soli=[
                ("Veselā daļa ir 2",
                 "Punkts būs starp 2 un 3."),
                ("Saucējs ir 4",
                 "Vienību sadala četrās daļās."),
                ("No 2 skaita vienu ceturtdaļu pa labi",
                 "Skaitītājs ir 1."),
                ("Atzīmē punktu un pieraksti 2{1|4}",
                 "Punkts ir tuvu divniekam."),
            ],
            atbilde="2{1|4} atrodas starp 2 un 3, tuvu 2"),

    Petijums("Uzzīmē savu taisni",
             soli=["Uzzīmē 12 cm garu taisni un atzīmē uz tās 0, 1, 2 un 3.",
                   "Katru vienību sadali četrās vienādās daļās pa 1 cm.",
                   "Atzīmē 1{1|2}, 2{1|4} un 2{3|4}.",
                   "Pieraksti pie katra punkta skaitli.",
                   "Pārbaudi, vai katrs punkts ir starp pareizajiem "
                   "veseliem."],
             vajag="lineāls, zīmulis, rūtiņu lapa",
             secinajums="Ar 1 cm iedaļu visi trīs punkti iekrīt tieši uz "
                        "iedaļām."),

    Ievadi("Starp kuriem veseliem?", [
        {"jaut": "Starp kuriem veseliem ir 2{1|4}? Ieraksti mazāko.",
         "atb": ["2"], "padoms": "Veselā daļa."},
        {"jaut": "Starp kuriem veseliem ir 5{3|8}? Ieraksti mazāko.",
         "atb": ["5"], "padoms": "Veselā daļa."},
        {"jaut": "Starp kuriem veseliem ir {11|4}? Ieraksti mazāko.",
         "atb": ["2"], "padoms": "{11|4} = 2{3|4}."},
        {"jaut": "Starp kuriem veseliem ir {17|5}? Ieraksti mazāko.",
         "atb": ["3"], "padoms": "{17|5} = 3{2|5}."},
        {"jaut": "Cik daļās jāsadala vienība, lai atliktu 2{1|4}?",
         "atb": ["4"], "padoms": "Saucējs."},
        {"jaut": "Cik daļās jāsadala vienība, lai atliktu 1{2|3}?",
         "atb": ["3"], "padoms": "Saucējs."},
        {"jaut": "Cik daļās jāsadala vienība, lai uz vienas taisnes atliktu "
                 "1{1|2} un 2{1|4}?",
         "atb": ["4"], "padoms": "4 dalās ar 2 un 4."},
        {"jaut": "Kurš skaitlis ir tuvāk 3 - 2{3|4} vai 2{1|4}? Atbildi "
                 "raksti kā a b/c.",
         "atb": ["2 3/4"], "padoms": "Lielāka daļa - tuvāk nākamajam."},
    ], pamats=4,
        ievads="Veselā daļa pasaka vietu, saucējs - iedaļu."),

    Zimejums("Trīs punkti ar ceturtdaļu iedaļu",
             taisne(0, 3, 1, [(1.5, "1 1/2"), (2.25, "2 1/4"),
                              (2.75, "2 3/4")],
                    virsraksts="Visi trīs iekrīt uz iedaļām"),
             paskaidro="Ar ceturtdaļu iedaļu der arī 1{1|2}, jo puse ir "
                       "divas ceturtdaļas.",
             ievads="Viena iedaļa, kas der visiem trim skaitļiem."),

    Varianti("Kā atliek jauktu skaitli?", [
        {"jaut": "Ko atrod vispirms?",
         "opcijas": ["Veselo daļu uz taisnes", "Daļas skaitītāju",
                     "Taisnes garumu", "Kopsaucēju"],
         "pareizi": 0,
         "padoms": "Veselā daļa pasaka vietu."},
        {"jaut": "Kas nosaka iedaļas lielumu?",
         "opcijas": ["Saucējs", "Skaitītājs", "Veselā daļa", "Taisnes garums"],
         "pareizi": 0,
         "padoms": "Cik daļās sadala vienību."},
        {"jaut": "Kur atrodas 3{1|2}?",
         "opcijas": ["Starp 3 un 4", "Starp 2 un 3", "Starp 1 un 2",
                     "Aiz 4"],
         "pareizi": 0,
         "padoms": "Veselā daļa ir 3."},
        {"jaut": "Kurš punkts ir tuvāk veselajam skaitlim pa kreisi?",
         "opcijas": ["2{1|8}", "2{7|8}", "2{1|2}", "2{3|4}"],
         "pareizi": 0,
         "padoms": "Mazāka daļa - tuvāk kreisajam."},
        {"jaut": "Kāda iedaļa der gan {1|2}, gan {1|3}?",
         "opcijas": ["Sestdaļas", "Ceturtdaļas", "Piektdaļas", "Puses"],
         "pareizi": 0,
         "padoms": "6 dalās ar 2 un 3."},
        {"jaut": "{9|2} uz taisnes atrodas...",
         "opcijas": ["Starp 4 un 5", "Starp 2 un 3", "Starp 9 un 10",
                     "Pie 2"],
         "pareizi": 0,
         "padoms": "{9|2} = 4{1|2}."},
    ], pamats=4),

    Pasaule("Cik glāžu ir mērglāzē?",
            Ievadi("", [
                {"jaut": "Mērglāzē ielietas 1{1|2} glāzes. Starp kuriem "
                         "veseliem tas ir? Ieraksti mazāko.",
                 "atb": ["1"], "padoms": "Veselā daļa."},
                {"jaut": "Cik ceturtdaļglāžu tas ir?",
                 "atb": ["6"], "padoms": "1{1|2} = {6|4}."},
                {"jaut": "Otrā traukā ir 2{3|4} glāzes. Cik ceturtdaļglāžu "
                         "tas ir?",
                 "atb": ["11"], "padoms": "2 · 4 + 3."},
                {"jaut": "Kurā traukā ir vairāk? Ieraksti skaitli kā a b/c.",
                 "atb": ["2 3/4"], "padoms": "11 ceturtdaļas pret 6."},
            ]),
            pavediens="virtuve",
            konteksts="Mērglāzes iedaļas ir tieši tā pati skaitļu taisne, "
                      "tikai stāvus.",
            kapec="Ja zini, starp kurām iedaļām meklēt, mērīt ir ātrāk."),

    Kopsavilkums([
        "Atlieku jauktu skaitli uz skaitļu taisnes.",
        "Izvēlos iedaļu pēc daļas saucēja.",
        "Uzzīmēju taisni, kas der vairākiem skaitļiem uzreiz.",
        "Pārbaudu, vai punkts atrodas starp pareizajiem veseliem.",
    ]),

    Majas([
        "Uzzīmē taisni no 0 līdz 4 un atzīmē 1{1|4}, 2{1|2} un 3{3|4}.",
        "Atliec uz tās pašas taisnes {7|2} un pieraksti, kur tas nokļuva.",
        "Izvēlies iedaļu, kas derētu arī trešdaļām.",
    ]),
]
