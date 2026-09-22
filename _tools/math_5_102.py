# -*- coding: utf-8 -*-
"""5. klase, 102. stunda: «Kā plānot darbību izpildi?»

Jauns mikrotemats sākas nevis ar rēķinu, bet ar plānu. Kad saucēji atšķiras,
soļu ir daudz, un skolēns parasti sāk no vidus - pie kopsaucēja ķeras tikai
tad, kad jau ir iestrēdzis. Tāpēc šī stunda prasa vienu lietu: pirms rēķina
pateikt vārdiem, kas un kādā secībā tiks darīts.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā plānot darbību izpildi?"

MERKIS = ("Mācīsimies pirms aprēķina aprakstīt, ko un kādā secībā darīsim ar "
          "jauktiem skaitļiem.")

SATURS = [
    Sakums("Četri soļi, ne viens",
           zimejums=restis([["1/2", "1/3", "5/6"]],
                           virsraksts="Saucēji 2 un 3, kopsaucējs 6"),
           paraksts="Pirms saskaitīšanas vienmēr ir kopsaucēja meklēšana.",
           fakti=["Jaukti skaitļi ar dažādiem saucējiem prasa vairāk soļu.",
                  "Soļu secība vienmēr ir viena un tā pati.",
                  "Ja to pasaka iepriekš, rēķins vairs neapmulsina."]),

    Doma("Vispirms plāns, tad rēķins",
         "Ar jauktiem skaitļiem darbības plāno secībā: kopsaucējs, daļu "
         "pārrakstīšana, darbība ar veselajiem un daļām, rezultāta "
         "sakārtošana.",
         soli=[
             "Pasaki, kāda darbība jāizpilda.",
             "Atrodi daļu kopsaucēju.",
             "Pārraksti abas daļas ar kopsaucēju.",
             "Izpildi darbību ar veselajiem un daļām.",
             "Sakārto rezultātu: atdali veselo un saīsini.",
         ],
         pieze="Plāns ir noderīgs arī tāpēc, ka pasaka, kur varētu rasties "
               "grūtības: ja atņemot mazināmā daļa izrādīsies mazāka, būs "
               "jāaizņemas veselais - to var paredzēt jau plānojot."),

    Paraugs("Uzraksti plānu 2{1|2} + 1{1|3}",
            uzd="Pirms rēķina apraksti, ko darīsi.",
            soli=[
                ("1. Darbība ir saskaitīšana",
                 "Vispirms pasaka, kas jādara."),
                ("2. Kopsaucējs ir 6",
                 "6 dalās ar 2 un 3."),
                ("3. {1|2} = {3|6}, {1|3} = {2|6}",
                 "Pārraksta abas daļas."),
                ("4. 2 + 1 = 3 un {3|6} + {2|6} = {5|6}",
                 "Izpilda darbību."),
                ("5. 3{5|6} - daļa ir īsta un nesaīsināma",
                 "Rezultāts sakārtots."),
            ],
            atbilde="2{1|2} + 1{1|3} = 3{5|6}"),

    Ievadi("Kāds būs nākamais solis?", [
        {"jaut": "2{1|2} + 1{1|3}. Kāds ir kopsaucējs?",
         "atb": ["6"], "padoms": "6 dalās ar 2 un 3."},
        {"jaut": "Ar saucēju 6: kāds skaitītājs ir daļai {1|2}?",
         "atb": ["3"], "padoms": "6 : 2."},
        {"jaut": "Ar saucēju 6: kāds skaitītājs ir daļai {1|3}?",
         "atb": ["2"], "padoms": "6 : 3."},
        {"jaut": "Cik ir 2{1|2} + 1{1|3}? Atbildi raksti kā a b/c.",
         "atb": ["3 5/6"], "padoms": "Veselie 3, daļas {5|6}."},
        {"jaut": "3{1|4} + 2{1|6}. Kāds ir kopsaucējs?",
         "atb": ["12"], "padoms": "12 dalās ar 4 un 6."},
        {"jaut": "3{3|4} - 1{1|2}. Kāds ir kopsaucējs?",
         "atb": ["4"], "padoms": "4 jau dalās ar 2."},
        {"jaut": "Cik ir 3{3|4} - 1{1|2}? Atbildi raksti kā a b/c.",
         "atb": ["2 1/4"], "padoms": "{3|4} - {2|4}."},
        {"jaut": "2{1|3} - 1{1|2}. Vai būs jāaizņemas veselais? Raksti «jā» "
                 "vai «nē».",
         "atb": ["jā", "ja"], "padoms": "{2|6} < {3|6}."},
    ], pamats=4,
        ievads="Pirms katras atbildes pasaki sev, kurš solis tas ir."),

    Zimejums("Soļu secība",
             restis([["1/2", "3/6"],
                     ["1/3", "2/6"]],
                    virsraksts="Otrais solis: viens saucējs"),
             paskaidro="Kreisajā ailē ir dotās daļas, labajā - tās pašas ar "
                       "kopsaucēju. Tikai pēc tam sākas saskaitīšana.",
             ievads="Plāna otrais solis ir tas, ko visbiežāk izlaiž."),

    Varianti("Kurš solis ir pirmais?", [
        {"jaut": "Ko dara vispirms, saskaitot jauktus skaitļus ar dažādiem "
                 "saucējiem?",
         "opcijas": ["Meklē kopsaucēju", "Saskaita veselos",
                     "Saskaita daļas", "Saīsina"],
         "pareizi": 0,
         "padoms": "Vienādi gabali vispirms."},
        {"jaut": "Kurš solis ir pēdējais?",
         "opcijas": ["Rezultāta sakārtošana", "Kopsaucēja meklēšana",
                     "Daļu pārrakstīšana", "Veselo saskaitīšana"],
         "pareizi": 0,
         "padoms": "Atdala veselo un saīsina."},
        {"jaut": "Kāpēc plānu raksta pirms rēķina?",
         "opcijas": ["Lai neizlaistu nevienu soli",
                     "Lai rēķins būtu garāks",
                     "Lai atbilde būtu precīzāka",
                     "Tas nav vajadzīgs"],
         "pareizi": 0,
         "padoms": "Izlaists solis ir biežākā kļūda."},
        {"jaut": "2{1|3} - 1{1|2}. Ko plāns paredz papildus?",
         "opcijas": ["Aizņemties veselo", "Saīsināt saucēju",
                     "Reizināt", "Neko papildus"],
         "pareizi": 0,
         "padoms": "{2|6} < {3|6}."},
        {"jaut": "3{1|4} + 2{1|6}: kāds kopsaucējs ir ērtākais?",
         "opcijas": ["12", "24", "10", "6"],
         "pareizi": 0,
         "padoms": "Mazākais, kas dalās ar 4 un 6."},
        {"jaut": "Cik soļu ir plānā?",
         "opcijas": ["Pieci", "Divi", "Viens", "Desmit"],
         "pareizi": 0,
         "padoms": "Darbība, kopsaucējs, pārrakstīšana, rēķins, "
                   "sakārtošana."},
    ], pamats=4),

    Pasaule("Cik kilometru kopā?",
            Ievadi("", [
                {"jaut": "Skrējiens: 2{1|2} km un 1{1|3} km. Kāds ir "
                         "kopsaucējs?",
                 "atb": ["6"], "padoms": "6 dalās ar 2 un 3."},
                {"jaut": "Cik kilometru kopā? Atbildi raksti kā a b/c.",
                 "atb": ["3 5/6"], "padoms": "2 + 1 un {3|6} + {2|6}."},
                {"jaut": "Otrā dienā 3{1|4} km un 2{1|6} km. Kāds ir "
                         "kopsaucējs?",
                 "atb": ["12"], "padoms": "12 dalās ar 4 un 6."},
                {"jaut": "Cik kilometru kopā otrajā dienā? Atbildi raksti kā "
                         "a b/c.",
                 "atb": ["5 5/12"], "padoms": "{3|12} + {2|12}."},
            ]),
            pavediens="sports",
            konteksts="Treniņu attālumus pieraksta ar jauktiem skaitļiem, un "
                      "nedēļas kopsummu rēķina no tiem.",
            kapec="Plānots rēķins neaizmirst kopsaucēju."),

    Kopsavilkums([
        "Pirms aprēķina pasaku, kāda darbība jāizpilda.",
        "Nosaucu soļu secību: kopsaucējs, pārrakstīšana, darbība, "
        "sakārtošana.",
        "Paredzu, vai būs jāaizņemas veselais.",
        "Izpildu rēķinu pēc sava plāna.",
    ]),

    Majas([
        "Uzraksti plānu uzdevumam 4{1|3} - 1{3|4} un tad izrēķini to.",
        "Atrodi piemēru, kurā kopsaucējs ir lielākais no saucējiem.",
        "Pieraksti savu plānu piecos teikumos.",
    ]),
]
