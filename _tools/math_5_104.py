# -*- coding: utf-8 -*-
"""5. klase, 104. stunda: «Kurš atņemšanas paņēmiens ērtāks?»

Atņemot jauktus skaitļus, ir divi ceļi: rēķināt pa daļām ar aizņemšanos vai
pārvērst abus skaitļus neīstās daļās. Abi ir pareizi, bet ne abi ir vienlīdz
ērti - tas atkarīgs no skaitļiem. Tāpēc stunda neizvēlas skolēna vietā, bet
māca pašam pamatot izvēli.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kurš atņemšanas paņēmiens ērtāks?"

MERKIS = ("Mācīsimies atņemt jauktus skaitļus ar dažādiem saucējiem, "
          "izvēloties sev piemērotu paņēmienu.")

SATURS = [
    Sakums("Divi ceļi uz vienu atbildi",
           zimejums=restis([["3 1/4", "13/4"],
                            ["1 1/2", "6/4"]],
                           virsraksts="Pa kreisi jaukti, pa labi neīstas"),
           paraksts="3{1|4} - 1{1|2} var rēķināt abos veidos - atbilde ir "
                    "1{3|4}.",
           fakti=["Pirmais ceļš: aizņemties veselo un rēķināt pa daļām.",
                  "Otrais ceļš: pārvērst abus neīstās daļās.",
                  "Izvēli nosaka skaitļu lielums."]),

    Doma("Izvēlies pēc skaitļiem",
         "Jauktus skaitļus atņem vai nu pa daļām ar aizņemšanos, vai "
         "pārvēršot abus neīstās daļās; abi paņēmieni dod vienu atbildi.",
         soli=[
             "Pārraksti daļas ar kopsaucēju.",
             "Salīdzini mazināmā un atņēmēja daļas.",
             "Ja mazināmā daļa ir lielāka - rēķini pa daļām.",
             "Ja mazāka - vai nu aizņemies veselo, vai pārej uz neīstām "
             "daļām.",
             "Pamato, kāpēc izvēlējies šo ceļu.",
         ],
         pieze="Ar maziem veselajiem neīstās daļas ir ērtas: 3{1|4} = "
               "{13|4}. Ar lieliem veselajiem tās kļūst neērtas: 27{1|4} = "
               "{109|4}, un tur labāk aizņemties veselo."),

    Paraugs("3{1|4} - 1{1|2} abos veidos",
            uzd="Izrēķini starpību divos veidos un salīdzini tos.",
            soli=[
                ("Kopsaucējs 4: 3{1|4} - 1{2|4}",
                 "Vispirms vienādo saucējus."),
                ("Pa daļām: 3{1|4} = 2{5|4}",
                 "Aizņemas veselo."),
                ("2{5|4} - 1{2|4} = 1{3|4}",
                 "Pirmais ceļš."),
                ("Neīstās daļās: {13|4} - {6|4} = {7|4}",
                 "Otrais ceļš."),
                ("{7|4} = 1{3|4}",
                 "Tā pati atbilde."),
            ],
            atbilde="3{1|4} - 1{1|2} = 1{3|4}"),

    Ievadi("Atņem jauktus skaitļus", [
        {"jaut": "3{1|4} - 1{1|2} = ? Atbildi raksti kā a b/c.",
         "atb": ["1 3/4"], "padoms": "Kopsaucējs 4."},
        {"jaut": "4{1|3} - 1{1|2} = ? Atbildi raksti kā a b/c.",
         "atb": ["2 5/6"], "padoms": "Kopsaucējs 6: 4{2|6} - 1{3|6}."},
        {"jaut": "5{1|2} - 2{1|4} = ? Atbildi raksti kā a b/c.",
         "atb": ["3 1/4"], "padoms": "{2|4} - {1|4}."},
        {"jaut": "3{2|3} - 1{1|6} = ? Atbildi raksti kā a b/c.",
         "atb": ["2 1/2", "2 3/6"], "padoms": "{4|6} - {1|6} = {3|6}."},
        {"jaut": "2{1|5} - 1{1|2} = ? Atbildi raksti kā a b/c.",
         "atb": ["7/10"], "padoms": "Kopsaucējs 10: 2{2|10} - 1{5|10}."},
        {"jaut": "4{1|6} - 2{1|3} = ? Atbildi raksti kā a b/c.",
         "atb": ["1 5/6"], "padoms": "4{1|6} - 2{2|6}."},
        {"jaut": "{13|4} - {6|4} = ? Atbildi raksti kā a/b.",
         "atb": ["7/4", "1 3/4"], "padoms": "Atņem skaitītājus."},
        {"jaut": "3{1|2} - 1{3|4} = ? Atbildi raksti kā a b/c.",
         "atb": ["1 3/4"], "padoms": "3{2|4} = 2{6|4}."},
    ], pamats=4,
        ievads="Vispirms kopsaucējs, tad izvēlies ceļu."),

    Zimejums("Abu ceļu galapunkts ir viens",
             restis([["2 5/4", "1 2/4", "1 3/4"],
                     ["13/4", "6/4", "7/4"]],
                    virsraksts="Augšā pa daļām, apakšā neīstās daļās"),
             paskaidro="Augšējā rindā veselais aizņemts, apakšējā skaitļi "
                       "pārvērsti neīstās daļās. Abu rindu atbilde ir viens "
                       "skaitlis.",
             ievads="Ceļi ir divi, atbilde - viena."),

    Varianti("Kuru ceļu izvēlēties?", [
        {"jaut": "Kad ērtāk pārvērst neīstās daļās?",
         "opcijas": ["Kad veselās daļas ir mazas", "Vienmēr",
                     "Kad veselās daļas ir lielas", "Nekad"],
         "pareizi": 0,
         "padoms": "Citādi skaitītāji kļūst milzīgi."},
        {"jaut": "Kad ērtāk aizņemties veselo?",
         "opcijas": ["Kad veselās daļas ir lielas", "Vienmēr",
                     "Kad saucēji ir vienādi", "Nekad"],
         "pareizi": 0,
         "padoms": "27{1|4} neīstā daļā ir neērts."},
        {"jaut": "Vai abi paņēmieni dod vienu atbildi?",
         "opcijas": ["Jā, vienmēr", "Nē", "Tikai ar vienādiem saucējiem",
                     "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Skaitlis ir tas pats, mainās pieraksts."},
        {"jaut": "Kas jāizdara pirms abiem paņēmieniem?",
         "opcijas": ["Jāvienādo saucēji", "Jāsaīsina", "Jāatņem veselie",
                     "Nekas"],
         "pareizi": 0,
         "padoms": "Bez kopsaucēja neviens ceļš nestrādā."},
        {"jaut": "Cik ir 3{1|2} - 1{3|4}?",
         "opcijas": ["1{3|4}", "2{1|4}", "1{1|4}", "2{3|4}"],
         "pareizi": 0,
         "padoms": "3{2|4} = 2{6|4}."},
        {"jaut": "27{1|4} - 2{1|2}: kurš ceļš ērtāks?",
         "opcijas": ["Aizņemties veselo", "Pārvērst neīstās daļās",
                     "Abi vienlīdz", "Neviens"],
         "pareizi": 0,
         "padoms": "{109|4} ir neērts skaitlis."},
    ], pamats=4),

    Pasaule("Cik distances palicis?",
            Ievadi("", [
                {"jaut": "Distance 3{1|4} km, noskrieti 1{1|2} km. Cik "
                         "palicis? Atbildi raksti kā a b/c.",
                 "atb": ["1 3/4"], "padoms": "3{1|4} = 2{5|4}."},
                {"jaut": "Distance 4{1|3} km, noskrieti 1{1|2} km. Cik "
                         "palicis? Atbildi raksti kā a b/c.",
                 "atb": ["2 5/6"], "padoms": "Kopsaucējs 6."},
                {"jaut": "Distance 5{1|2} km, noskrieti 2{1|4} km. Cik "
                         "palicis? Atbildi raksti kā a b/c.",
                 "atb": ["3 1/4"], "padoms": "{2|4} - {1|4}."},
                {"jaut": "Distance 2{1|5} km, noskrieti 1{1|2} km. Cik "
                         "palicis? Atbildi raksti kā a/b.",
                 "atb": ["7/10"], "padoms": "2{2|10} - 1{5|10}."},
            ]),
            pavediens="sports",
            konteksts="Skrējiena laikā atlikumu rēķina galvā, tāpēc ērtākais "
                      "paņēmiens ir tas, kas prasa mazāk soļu.",
            kapec="Izvēle starp diviem ceļiem ir arī matemātikas prasme."),

    Kopsavilkums([
        "Atņemu jauktus skaitļus ar dažādiem saucējiem.",
        "Izmantoju aizņemšanos vai pāreju uz neīstām daļām.",
        "Izvēlos paņēmienu pēc skaitļu lieluma.",
        "Pamatoju savu izvēli.",
    ]),

    Majas([
        "Izrēķini 5{1|6} - 2{3|4} abos veidos.",
        "Atrodi piemēru, kurā neīstās daļas ir neērtas.",
        "Uzraksti, kuru ceļu tu izvēlies biežāk un kāpēc.",
    ]),
]
