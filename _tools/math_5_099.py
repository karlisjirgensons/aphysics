# -*- coding: utf-8 -*-
"""5. klase, 99. stunda: «Ko darīt, ja daļa ir par mazu?»

Mikrotemata grūtākā stunda. Atņemot jauktus skaitļus, mazināmā daļa reizēm
ir mazāka par atņēmēja daļu, un tad atņemt «pa daļām» vairs nevar. Risinājums
ir iepriekšējās stundas solis: aizņemties vienu veselo. Tāpēc stundā svarīgs
ir pieraksts - tieši tur redzams, kur veselais pazuda.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Ko darīt, ja daļa ir par mazu?"

MERKIS = ("Iemācīsimies atņemt jauktus skaitļus, pārveidojot mazināmā veselo "
          "par daļu, un skaidrot pierakstu.")

SATURS = [
    Sakums("{1|4} mīnus {3|4} - tā nevar",
           zimejums=restis([["3 1/4", "2 5/4"]],
                           virsraksts="Viens un tas pats skaitlis"),
           paraksts="3{1|4} = 2{5|4} - tagad {3|4} atņemt var.",
           fakti=["Mazināmā daļa {1|4} ir mazāka par atņēmēja {3|4}.",
                  "Tāpēc no veselās daļas aizņemas vienu vienību.",
                  "Tā daļa kļūst neīsta, un atņemšana kļūst iespējama."]),

    Doma("Aizņemies vienu veselo un turpini",
         "Ja mazināmā daļa ir mazāka par atņēmēja daļu, no mazināmā veselās "
         "daļas aizņemas vienu vienību un pieskaita to daļai.",
         soli=[
             "Salīdzini abas daļas.",
             "Ja mazināmā daļa ir mazāka, samazini veselo par 1.",
             "Aizņemto vienību pieraksti kā daļu ar to pašu saucēju.",
             "Pieskaiti to esošajai daļai.",
             "Atņem veselos un daļas atsevišķi.",
         ],
         pieze="3{1|4} = 2 + 1 + {1|4} = 2 + {4|4} + {1|4} = 2{5|4}. Veselo "
               "daļu samazina par vienu, bet skaitītājam pieskaita saucēju - "
               "tas ir viss pārveidojums."),

    Paraugs("3{1|4} - 1{3|4}",
            uzd="Izrēķini starpību un parādi, kur aizņēmās veselo.",
            soli=[
                ("{1|4} < {3|4}",
                 "Atņemt pa daļām nevar."),
                ("3{1|4} = 2{5|4}",
                 "Aizņemas vienu veselo: 1 + 4 = 5 ceturtdaļas."),
                ("2 - 1 = 1",
                 "Veselās daļas."),
                ("{5|4} - {3|4} = {2|4}",
                 "Daļas."),
                ("1{2|4} = 1{1|2}",
                 "Saīsina rezultātu."),
            ],
            atbilde="3{1|4} - 1{3|4} = 1{1|2}"),

    Ievadi("Atņem ar aizņemšanos", [
        {"jaut": "3{1|4} - 1{3|4} = ? Atbildi raksti kā a b/c.",
         "atb": ["1 1/2", "1 2/4"], "padoms": "3{1|4} = 2{5|4}."},
        {"jaut": "4{1|3} - 1{2|3} = ? Atbildi raksti kā a b/c.",
         "atb": ["2 2/3"], "padoms": "4{1|3} = 3{4|3}."},
        {"jaut": "5{1|5} - 2{3|5} = ? Atbildi raksti kā a b/c.",
         "atb": ["2 3/5"], "padoms": "5{1|5} = 4{6|5}."},
        {"jaut": "3{2|6} - 1{5|6} = ? Atbildi raksti kā a b/c.",
         "atb": ["1 1/2", "1 3/6"], "padoms": "3{2|6} = 2{8|6}."},
        {"jaut": "Cik ceturtdaļu ir skaitlī 3{1|4}, ja aizņemas vienu "
                 "veselo? Ieraksti jauno skaitītāju.",
         "atb": ["5"], "padoms": "1 + 4."},
        {"jaut": "Cik trešdaļu ir skaitlī 4{1|3}, ja aizņemas vienu veselo? "
                 "Ieraksti jauno skaitītāju.",
         "atb": ["4"], "padoms": "1 + 3."},
        {"jaut": "4{3|8} - 2{1|8} = ? Atbildi raksti kā a b/c.",
         "atb": ["2 1/4", "2 2/8"], "padoms": "Aizņemties nevajag."},
        {"jaut": "6{1|2} - 3{1|2} = ? Ieraksti skaitli.",
         "atb": ["3"], "padoms": "Daļas vienādas."},
    ], pamats=4,
        ievads="Vispirms salīdzini daļas - tikai tad izlem, vai jāaizņemas."),

    Zimejums("Pirms un pēc aizņemšanās",
             restis([["3 1/4", "2 5/4"],
                     ["4 1/3", "3 4/3"]],
                    virsraksts="Kreisā un labā puse ir vienādas"),
             paskaidro="Veselā daļa samazinās par vienu, bet skaitītājam "
                       "pieskaita saucēju. Pati skaitļa vērtība nemainās.",
             ievads="Aizņemšanās maina pierakstu, nevis skaitli."),

    Varianti("Kad jāaizņemas?", [
        {"jaut": "Kad jāaizņemas viens veselais?",
         "opcijas": ["Kad mazināmā daļa ir mazāka par atņēmēja daļu",
                     "Vienmēr",
                     "Kad saucēji atšķiras",
                     "Nekad"],
         "pareizi": 0,
         "padoms": "Citādi daļas atņemt nevar."},
        {"jaut": "3{1|4} pēc aizņemšanās ir...",
         "opcijas": ["2{5|4}", "2{1|4}", "3{5|4}", "4{5|4}"],
         "pareizi": 0,
         "padoms": "1 + 4 = 5 ceturtdaļas."},
        {"jaut": "Kas notiek ar skaitītāju, aizņemoties?",
         "opcijas": ["Tam pieskaita saucēju", "Tas divkāršojas",
                     "Tas pazūd", "Tas dalās ar 2"],
         "pareizi": 0,
         "padoms": "Viena vienība ir {n|n}."},
        {"jaut": "Cik ir 4{1|3} - 1{2|3}?",
         "opcijas": ["2{2|3}", "3{1|3}", "2{1|3}", "3{2|3}"],
         "pareizi": 0,
         "padoms": "4{1|3} = 3{4|3}."},
        {"jaut": "Vai aizņemšanās maina skaitļa vērtību?",
         "opcijas": ["Nē, tikai pierakstu", "Jā, tas kļūst mazāks",
                     "Jā, tas kļūst lielāks", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "2{5|4} = 3{1|4}."},
        {"jaut": "4{3|8} - 2{1|8}: vai jāaizņemas?",
         "opcijas": ["Nav, {3|8} > {1|8}", "Ir", "Tikai veselajiem",
                     "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Mazināmā daļa ir lielāka."},
    ], pamats=4),

    Pasaule("Cik paliek no krāsas?",
            Ievadi("", [
                {"jaut": "Bija 3{1|4} l krāsas, izlietoti 1{3|4} l. Cik litru "
                         "palika? Atbildi raksti kā a b/c.",
                 "atb": ["1 1/2", "1 2/4"], "padoms": "3{1|4} = 2{5|4}."},
                {"jaut": "Bija 4{1|3} m līstes, nogriezti 1{2|3} m. Cik metru "
                         "palika? Atbildi raksti kā a b/c.",
                 "atb": ["2 2/3"], "padoms": "4{1|3} = 3{4|3}."},
                {"jaut": "Bija 5{1|5} kg javas, izlietoti 2{3|5} kg. Cik "
                         "kilogramu palika? Atbildi raksti kā a b/c.",
                 "atb": ["2 3/5"], "padoms": "5{1|5} = 4{6|5}."},
                {"jaut": "Bija 6{1|2} m tapešu, izlietoti 3{1|2} m. Cik metru "
                         "palika? Ieraksti skaitli.",
                 "atb": ["3"], "padoms": "Daļas vienādas."},
            ]),
            pavediens="maja",
            konteksts="Remontā gandrīz vienmēr atņem mazāku daļu no lielāka "
                      "skaitļa, bet daļas pašas nesakrīt.",
            kapec="Aizņemšanās ir vienīgais solis, kas šo atrisina."),

    Kopsavilkums([
        "Salīdzinu daļas, pirms sāku atņemt jauktus skaitļus.",
        "Aizņemos vienu veselo, ja mazināmā daļa ir par mazu.",
        "Pierakstu pārveidojumu tā, lai redzams, kur veselais pazuda.",
        "Atņemu veselos un daļas atsevišķi un saīsinu rezultātu.",
    ]),

    Majas([
        "Izrēķini 5{1|6} - 2{5|6} un pieraksti visus soļus.",
        "Uzraksti divus atņemšanas piemērus: vienu ar aizņemšanos, otru bez.",
        "Paskaidro, kāpēc 3{1|4} un 2{5|4} ir viens un tas pats skaitlis.",
    ]),
]
