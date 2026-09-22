# -*- coding: utf-8 -*-
"""5. klase, 69. stunda: «Kur šeit var kļūdīties?»

Stunda bez jauna paņēmiena: te skolēns ir tas, kas labo. Kļūdas daļu
saskaitīšanā ir tikai dažas un vienmēr tās pašas, tāpēc tās ir vērts
nosaukt vārdā - tad nākamajā reizē tās pamana pats. Katrs uzdevums te rāda
gatavu risinājumu, un jautājums ir viens: kurā rindā tas sabruka.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kur šeit var kļūdīties?"

MERKIS = ("Mācīsimies atpazīt tipiskas kļūdas daļu saskaitīšanā un formulēt, "
          "kā no tām izvairīties.")

SATURS = [
    Sakums("Trīs atbildes, viena pareiza",
           zimejums=restis([["2/5", "5/6", "2/6"]],
                           virsraksts="Trīs atbildes uzdevumam 1/2 + 1/3"),
           paraksts="Pareiza ir tikai vidējā; abas pārējās kļūdas ir tik "
                    "biežas, ka tām ir savs vārds.",
           fakti=["Pirmajā atbildē saskaitīti arī saucēji.",
                  "Trešajā atbildē skaitītāji nav paplašināti.",
                  "Pareizā atbilde ir tikai viena."]),

    Doma("Katrai kļūdai ir sava pazīme",
         "Daļu saskaitīšanā kļūdas ir dažas un atkārtojas: saskaitīti "
         "saucēji, nepaplašināts skaitītājs, nesaīsināta atbilde.",
         soli=[
             "Pārbaudi, vai saucējs atbildē ir tas pats, kas kopsaucējs.",
             "Pārbaudi, vai abi skaitītāji tika paplašināti.",
             "Pārbaudi, vai atbilde ir saīsināta līdz galam.",
             "Novērtē atbildi: vai tā vispār var būt tik liela vai maza.",
         ],
         pieze="Ātrākā pārbaude ir novērtējums. {1|2} + {1|3} noteikti ir "
               "vairāk nekā {1|2}, tāpēc atbilde {2|5} ir nepareiza vēl "
               "pirms rēķina pārbaudes."),

    Paraugs("Atrodi kļūdu pierakstā",
            uzd="Skolēns rēķina: {1|2} + {1|4} = {1 + 1|2 + 4} = {2|6} = "
                "{1|3}. Kur ir kļūda?",
            soli=[
                ("Kopsaucējs netika meklēts",
                 "Pirmais solis izlaists."),
                ("Saskaitīti arī saucēji",
                 "Saucējs pasaka gabala lielumu - to nesaskaita."),
                ("Pareizi: {1|2} = {2|4}",
                 "Pusi pārraksta kā divas ceturtdaļas."),
                ("{2|4} + {1|4} = {3|4}",
                 "Saskaita tikai skaitītājus."),
                ("{3|4} > {1|2}",
                 "Novērtējums apstiprina: summa ir lielāka par saskaitāmo."),
            ],
            atbilde="Pareizā atbilde ir {3|4}"),

    Ievadi("Izlabo kļūdaino atbildi", [
        {"jaut": "{1|2} + {1|4} = ? Atbildi raksti kā a/b.",
         "atb": ["3/4"], "padoms": "{2|4} + {1|4}."},
        {"jaut": "{1|3} + {1|4} = ? Atbildi raksti kā a/b.",
         "atb": ["7/12"], "padoms": "{4|12} + {3|12}."},
        {"jaut": "{2|5} + {1|5} = ? Atbildi raksti kā a/b.",
         "atb": ["3/5"], "padoms": "Saucēji jau vienādi."},
        {"jaut": "{1|6} + {1|3} = ? Atbildi raksti kā a/b.",
         "atb": ["1/2", "3/6"], "padoms": "{1|6} + {2|6} = {3|6}."},
        {"jaut": "{3|8} + {1|8} = ? Atbildi raksti kā a/b.",
         "atb": ["1/2", "4/8"], "padoms": "{4|8} saīsināts."},
        {"jaut": "{2|3} - {1|2} = ? Atbildi raksti kā a/b.",
         "atb": ["1/6"], "padoms": "{4|6} - {3|6}."},
        {"jaut": "{5|6} - {1|2} = ? Atbildi raksti kā a/b.",
         "atb": ["1/3", "2/6"], "padoms": "{5|6} - {3|6} = {2|6}."},
        {"jaut": "{1|4} + {1|4} + {1|4} = ? Atbildi raksti kā a/b.",
         "atb": ["3/4"], "padoms": "Trīs vienādi gabali."},
    ], pamats=4,
        ievads="Pēc katras atbildes uzdod sev jautājumu: vai tā izskatās "
               "ticama?"),

    Zimejums("Kļūdas ar vārdu",
             restis([["2/5", "2/6", "2/4"],
                     ["5/6", "5/6", "1/2"]],
                    virsraksts="Augšā kļūda, apakšā pareizi"),
             paskaidro="Pirmajā ailē saskaitīti saucēji, otrajā nav "
                       "paplašināti skaitītāji, trešajā atbilde palikusi "
                       "nesaīsināta. Visas trīs pamana ar vienu pārbaudi.",
             ievads="Ja kļūdai ir vārds, to vieglāk pamanīt."),

    Varianti("Kura kļūda pieļauta?", [
        {"jaut": "{1|2} + {1|3} = {2|5}. Kāda kļūda?",
         "opcijas": ["Saskaitīti saucēji", "Nav saīsināts",
                     "Nepareizs kopsaucējs", "Kļūdas nav"],
         "pareizi": 0,
         "padoms": "Saucēju nekad nesaskaita."},
        {"jaut": "{1|2} + {1|3} = {2|6}. Kāda kļūda?",
         "opcijas": ["Skaitītāji nav paplašināti",
                     "Saskaitīti saucēji",
                     "Atbilde nav saīsināta",
                     "Kļūdas nav"],
         "pareizi": 0,
         "padoms": "Kopsaucējs pareizs, bet skaitītāji palika vecie."},
        {"jaut": "{1|4} + {1|4} = {2|4}. Kāda kļūda?",
         "opcijas": ["Atbilde nav saīsināta", "Saskaitīti saucēji",
                     "Nepareizs kopsaucējs", "Kļūdas nav"],
         "pareizi": 0,
         "padoms": "{2|4} = {1|2}."},
        {"jaut": "Kā ātri pārbaudīt summu, nerēķinot?",
         "opcijas": ["Summai jābūt lielākai par katru saskaitāmo",
                     "Summai jābūt mazākai par 1",
                     "Saucējam jābūt lielākam",
                     "Pārbaudīt nevar"],
         "pareizi": 0,
         "padoms": "Pieliekot kļūst vairāk."},
        {"jaut": "{3|4} - {1|2} = {2|2}. Kāda kļūda?",
         "opcijas": ["Atņemti saucēji", "Nav saīsināts",
                     "Nepareizs kopsaucējs", "Kļūdas nav"],
         "pareizi": 0,
         "padoms": "Saucēju neatņem."},
        {"jaut": "Kurš solis pasargā no lielākās daļas kļūdu?",
         "opcijas": ["Pierakstīt paplašināšanu ar abiem locekļiem",
                     "Rēķināt galvā",
                     "Uzreiz saīsināt",
                     "Sākt ar atbildi"],
         "pareizi": 0,
         "padoms": "58. stundas pieraksts."},
    ], pamats=4),

    Pasaule("Pārbaudi klasesbiedra darbu",
            Ievadi("", [
                {"jaut": "Klasesbiedrs raksta: {1|2} + {1|6} = {2|8}. Kāda "
                         "ir pareizā atbilde? Raksti kā a/b.",
                 "atb": ["2/3", "4/6"], "padoms": "{3|6} + {1|6} = {4|6}."},
                {"jaut": "Viņš raksta: {2|3} + {1|6} = {3|9}. Kāda ir "
                         "pareizā atbilde? Raksti kā a/b.",
                 "atb": ["5/6"], "padoms": "{4|6} + {1|6}."},
                {"jaut": "Viņš raksta: {3|4} - {1|4} = {2|4}. Kā atbildi "
                         "pabeigt? Raksti kā a/b.",
                 "atb": ["1/2"], "padoms": "Saīsina."},
                {"jaut": "Viņš raksta: {1|3} + {1|3} = {2|6}. Kāda ir "
                         "pareizā atbilde? Raksti kā a/b.",
                 "atb": ["2/3"], "padoms": "Saucēji jau bija vienādi."},
            ]),
            pavediens="skola",
            konteksts="Klasē darbus bieži pārbauda savā starpā, un atrast "
                      "svešu kļūdu ir vieglāk nekā savu.",
            kapec="Kas pamana kļūdu cita darbā, to pamana arī savējā."),

    Kopsavilkums([
        "Atpazīstu kļūdu, kurā saskaitīti saucēji.",
        "Atpazīstu kļūdu, kurā skaitītājs nav paplašināts.",
        "Atpazīstu nepabeigtu atbildi, kas nav saīsināta.",
        "Novērtēju atbildi, pirms sāku to pārbaudīt ar rēķinu.",
    ]),

    Majas([
        "Uzraksti trīs kļūdainus rēķinus un iedod tos draugam labot.",
        "Pārbaudi savus vecos darbus - vai tur ir kāda no šīm kļūdām.",
        "Uzraksti vienā teikumā, kā pārbaudīt summu bez rēķināšanas.",
    ]),
]
