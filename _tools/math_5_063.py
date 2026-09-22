# -*- coding: utf-8 -*-
"""5. klase, 63. stunda: «Kā sakārtot vairākas daļas?»

Trīs paņēmieni jau ir rokā, te tos liek kopā. Ar divām daļām pietiek ar vienu
triku, bet ar četrām tas vairs nestrādā - vajadzīgs viens kopīgs mērogs.
Tāpēc šī stunda ir arī atbilde uz 59. stundas jautājumu: tieši te
starprezultātu nesaīsina.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis, taisne)

TEMA = "Kā sakārtot vairākas daļas?"

MERKIS = ("Iemācīsimies sakārtot trīs vai četras daļas augošā un dilstošā "
          "secībā.")

SATURS = [
    Sakums("Četri rezultāti vienā tabulā",
           zimejums=restis([["1/2", "2/3", "3/4", "5/6"],
                            ["6/12", "8/12", "9/12", "10/12"]],
                           virsraksts="Augšā dotās daļas, apakšā - ar vienu "
                                      "saucēju"),
           paraksts="Apakšējā rindā secība ir redzama bez rēķina.",
           fakti=["Četras daļas ar dažādiem saucējiem nesakārtosi ar aci.",
                  "Viens kopīgs saucējs padara tās salīdzināmas.",
                  "Tad atliek sakārtot skaitītājus."]),

    Doma("Viens saucējs visām",
         "Lai sakārtotu vairākas daļas, tās visas pārraksta ar vienu kopīgu "
         "saucēju un sakārto pēc skaitītājiem.",
         soli=[
             "Izraksti visus saucējus.",
             "Atrodi skaitli, kas dalās ar tiem visiem.",
             "Paplašini katru daļu līdz šim saucējam.",
             "Sakārto skaitītājus augošā vai dilstošā secībā.",
             "Atbildē raksti sākotnējās daļas tajā pašā secībā.",
         ],
         pieze="Starprezultātus te nesaīsina: kopīgais saucējs ir tieši tas, "
               "kas ļauj secību ieraudzīt. Saīsina tikai tad, ja atbildē "
               "prasa nesaīsināmas daļas."),

    Paraugs("Sakārto {1|2}, {2|3}, {3|4} un {5|6}",
            uzd="Sakārto četras daļas augošā secībā.",
            soli=[
                ("Saucēji: 2, 3, 4 un 6",
                 "Vispirms izraksta visus."),
                ("Kopīgais saucējs ir 12",
                 "12 dalās ar 2, 3, 4 un 6."),
                ("{6|12}, {8|12}, {9|12}, {10|12}",
                 "Katru daļu paplašina līdz saucējam 12."),
                ("6 < 8 < 9 < 10",
                 "Sakārto skaitītājus."),
                ("{1|2} < {2|3} < {3|4} < {5|6}",
                 "Atbildē - sākotnējās daļas."),
            ],
            atbilde="{1|2} < {2|3} < {3|4} < {5|6}"),

    Ievadi("Ar kopīgu saucēju", [
        {"jaut": "Daļām {1|3}, {1|4} un {1|6} kāds ir mazākais kopīgais "
                 "saucējs?",
         "atb": ["12"], "padoms": "12 dalās ar 3, 4 un 6."},
        {"jaut": "Ar saucēju 12: kāds skaitītājs ir daļai {1|3}?",
         "atb": ["4"], "padoms": "12 : 3."},
        {"jaut": "Ar saucēju 12: kāds skaitītājs ir daļai {1|4}?",
         "atb": ["3"], "padoms": "12 : 4."},
        {"jaut": "Kura no trim daļām {1|3}, {1|4}, {1|6} ir vislielākā? "
                 "Ieraksti kā a/b.",
         "atb": ["1/3"], "padoms": "{4|12} ir lielākā."},
        {"jaut": "Daļām {2|5}, {1|2} un {3|10} kāds ir mazākais kopīgais "
                 "saucējs?",
         "atb": ["10"], "padoms": "10 dalās ar 5, 2 un 10."},
        {"jaut": "Kura no tām ir vismazākā? Ieraksti kā a/b.",
         "atb": ["3/10"], "padoms": "{4|10}, {5|10} un {3|10}."},
        {"jaut": "Daļām {3|4} un {5|8} kāds ir mazākais kopīgais saucējs?",
         "atb": ["8"], "padoms": "8 dalās ar 4 un 8."},
        {"jaut": "Kura no tām ir lielākā? Ieraksti kā a/b.",
         "atb": ["3/4"], "padoms": "{6|8} pret {5|8}."},
    ], pamats=4,
        ievads="Kopīgais saucējs vispirms, secība pēc tam."),

    Zimejums("Visas četras uz vienas taisnes",
             taisne(0, 1, 1, [(1 / 2.0, "1/2"), (2 / 3.0, "2/3"),
                              (5 / 6.0, "5/6")],
                    virsraksts="Augošā secībā no kreisās uz labo"),
             paskaidro="Uz taisnes secība ir pati par sevi saprotama: kas "
                       "pa labi, tas lielāks.",
             ievads="Sakārtota rinda izskatās tieši tā."),

    Varianti("Kā sakārto daļas?", [
        {"jaut": "Ar ko sāk, kārtojot vairākas daļas?",
         "opcijas": ["Ar kopīgā saucēja meklēšanu",
                     "Ar saīsināšanu",
                     "Ar skaitītāju salīdzināšanu",
                     "Ar saucēju sakārtošanu"],
         "pareizi": 0,
         "padoms": "Salīdzināt var tikai vienādus gabalus."},
        {"jaut": "Vai starprezultātus šeit saīsina?",
         "opcijas": ["Nē, kopīgais saucējs vēl vajadzīgs",
                     "Jā, vienmēr",
                     "Jā, lai skaitļi ir mazāki",
                     "Tikai pēdējo"],
         "pareizi": 0,
         "padoms": "59. stundas kārtula."},
        {"jaut": "Daļas ar vienu saucēju sakārto pēc...",
         "opcijas": ["Skaitītājiem", "Saucējiem", "Garuma", "Secības tabulā"],
         "pareizi": 0,
         "padoms": "Gabali ir vienādi, skaits atšķiras."},
        {"jaut": "Kāds ir mazākais kopīgais saucējs daļām {1|2}, {1|3} un "
                 "{1|5}?",
         "opcijas": ["30", "10", "15", "60"],
         "pareizi": 0,
         "padoms": "2 · 3 · 5."},
        {"jaut": "Dilstošā secībā nozīmē...",
         "opcijas": ["No lielākās uz mazāko", "No mazākās uz lielāko",
                     "Pēc saucējiem", "Pēc skaitītājiem"],
         "pareizi": 0,
         "padoms": "Dilst - kļūst mazāks."},
        {"jaut": "Kurā secībā ir {1|4}, {1|3}, {1|2}?",
         "opcijas": ["Augošā", "Dilstošā", "Nesakārtotā", "Pēc saucējiem "
                                                          "augošā"],
         "pareizi": 0,
         "padoms": "Katra nākamā ir lielāka."},
    ], pamats=4),

    Pasaule("Rezultātu tabula pēc precizitātes",
            Ievadi("", [
                {"jaut": "Anna trāpīja {3|4}, Roberts {5|8}, Elza {7|8} "
                         "metienu. Ar saucēju 8 - kāds skaitītājs ir Annai?",
                 "atb": ["6"], "padoms": "{3|4} = {6|8}."},
                {"jaut": "Kurš ir pirmais tabulā? Ieraksti vārdu.",
                 "atb": ["Elza", "elza"], "padoms": "{7|8} ir lielākā."},
                {"jaut": "Kurš ir pēdējais? Ieraksti vārdu.",
                 "atb": ["Roberts", "roberts"], "padoms": "{5|8} ir "
                                                          "mazākā."},
                {"jaut": "Marks trāpīja {2|3}. Cik divdesmitčetrdaļu tas ir?",
                 "atb": ["16"], "padoms": "{2|3} = {16|24}."},
            ]),
            pavediens="sports",
            konteksts="Rezultātu tabulu sakārto pēc precizitātes, nevis pēc "
                      "metienu skaita.",
            kapec="Sakārtot var tikai tad, kad visiem ir viens saucējs."),

    Kopsavilkums([
        "Atrodu vairākām daļām kopīgu saucēju.",
        "Paplašinu visas daļas līdz šim saucējam.",
        "Sakārtoju daļas augošā un dilstošā secībā.",
        "Atbildē rakstu sākotnējās daļas, nevis starprezultātus.",
    ]),

    Majas([
        "Sakārto augošā secībā {2|3}, {3|5} un {7|10}.",
        "Sakārto dilstošā secībā {1|2}, {5|8} un {3|4}.",
        "Atrodi sporta tabulu un sakārto trīs rezultātus pēc precizitātes.",
    ]),
]
