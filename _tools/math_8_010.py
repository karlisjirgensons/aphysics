# -*- coding: utf-8 -*-
"""8. klase, 10. stunda: «Kā salīdzināt divas datu kopas?»

Bloka noslēgums: divas kopas salīdzina ar visiem četriem rādītājiem. Vidējais
un mediāna pasaka, kura ir «lielāka», amplitūda - kura ir stabilāka. Abas
kopas uz vienas skaitļu taisnes parāda to, ko skaitļi pasaka vārdos.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, Zimejums, restis, taisne)

TEMA = "Kā salīdzināt divas datu kopas?"

MERKIS = ("Salīdzināsim divas datu kopas, lietojot vairākus statistiskos "
          "rādītājus.")

_TABULA = restis([["", "Anna", "Beāte"],
                  ["vidējais", "8", "8"],
                  ["mediāna", "8", "8"],
                  ["amplitūda", "2", "8"]])

SATURS = [
    Sakums("Kuru šāvēju sūtīt uz sacensībām?",
           zimejums=_TABULA,
           paraksts="Annas punkti: 7, 8, 8, 8, 9. Beātes: 3, 8, 8, 10, 11.",
           fakti=["Vidējais un mediāna vienādi.",
                  "Annas rezultāti ir stabilāki - amplitūda 2.",
                  "Beāte var uzvarēt - vai izkrist."]),

    Doma("Salīdzināšanas plāns",
         "Vienu rādītāju var sagadīšanās dēļ sakrist, tāpēc kopas salīdzina ar "
         "vairākiem: ko rāda centrs un ko - izkliede.",
         soli=[
             "Sakārto abas kopas.",
             "Centrs: aritmētiskais vidējais un mediāna.",
             "Izkliede: amplitūda - mazāka nozīmē stabilāk.",
             "Novirzes: vai kāda vērtība neizkropļo vidējo?",
             "Secinājums: pilns teikums ar skaitļiem.",
         ],
         pieze="Labs secinājums: «Annas vidējais un mediāna ir tādi paši kā "
               "Beātei, bet amplitūda 4 reizes mazāka, tāpēc Anna ir "
               "stabilāka.»"),

    Zimejums("Abas kopas uz vienas taisnes",
             taisne(2, 12, 1, [(3, "B"), (7, "A"), (8, "A B"), (9, "A"),
                               (10, "B"), (11, "B")]),
             paskaidro="A - Anna, B - Beāte (8 punktos abām ir vairākas "
                       "vērtības). Annas punkti ir blīvi, Beātes - izkliedēti."),

    Paraugs("Divas klases",
            uzd="Kontroldarbā 8.a punkti: 12, 15, 15, 18, 20. 8.b: 10, 14, 17, "
                "17, 22. Salīdzini.",
            soli=[
                ("8.a: vidējais 16, mediāna 15, amplitūda 8", "80 : 5."),
                ("8.b: vidējais 16, mediāna 17, amplitūda 12", "80 : 5."),
                ("Vidējie vienādi; 8.b mediāna lielāka", "Puse 8.b ≥ 17."),
                ("8.a rezultāti stabilāki", "Amplitūda mazāka."),
            ],
            atbilde="Vidēji vienādi; 8.b - vairāk augstu rezultātu, 8.a - "
                    "vienmērīgāk"),

    Ievadi("Aprēķini un salīdzini", [
        {"jaut": "Veikals X: 30, 35, 40 pircēju. Veikals Y: 20, 38, 47. "
                 "X vidējais?",
         "atb": ["35"], "padoms": "105 : 3."},
        {"jaut": "Y vidējais?",
         "atb": ["35"], "padoms": "105 : 3."},
        {"jaut": "X amplitūda?",
         "atb": ["10"], "padoms": "40 − 30."},
        {"jaut": "Y amplitūda?",
         "atb": ["27"], "padoms": "47 − 20."},
    ]),

    Varianti("Kurš secinājums pareizs?", [
        {"jaut": "Tas pats piemērs: X un Y vidēji vienādi, bet...",
         "opcijas": ["X pircēju skaits ir stabilāks",
                     "Y pircēju skaits ir stabilāks",
                     "Y ir labāks veikals",
                     "Abi pilnīgi vienādi"],
         "pareizi": 0, "padoms": "Mazāka amplitūda."},
        {"jaut": "Grupa A: mediāna 70, grupa B: mediāna 60. Ko var teikt?",
         "opcijas": ["A pusei ir ne mazāk kā 70, B pusei - ne vairāk kā 60",
                     "Katrs A ir labāks par katru B",
                     "A vidējais noteikti lielāks",
                     "Nekā nevar teikt"],
         "pareizi": 0, "padoms": "Mediāna dala uz pusēm."},
    ]),

    Pasaule("Divu pilsētu laiks",
            Ievadi("", [
                {"jaut": "Nedēļas maksimālās temperatūras. Liepāja: 18, 19, "
                         "19, 20, 19, 18, 20. Mediāna?",
                 "atb": ["19"], "padoms": "Ceturtā sakārtotā."},
                {"jaut": "Daugavpils: 14, 22, 25, 17, 19, 24, 12. Mediāna?",
                 "atb": ["19"], "padoms": "12; 14; 17; 19; ..."},
                {"jaut": "Daugavpils amplitūda?",
                 "atb": ["13"], "padoms": "25 − 12."},
                {"jaut": "Liepājas amplitūda?",
                 "atb": ["2"], "padoms": "20 − 18."},
            ]),
            pavediens="planeta",
            konteksts="Jūras piekrastē laiks ir stabilāks nekā valsts "
                      "iekšienē - to parāda amplitūda, ne vidējais.",
            kapec="Mediānas vienādas, bet dzīvot šajās nedēļās būtu "
                  "pavisam citādi."),

    Kopsavilkums([
        "Salīdzinu kopas pēc vidējā un mediānas.",
        "Ar amplitūdu nosaku, kura kopa stabilāka.",
        "Uzrakstu secinājumu pilnā teikumā ar skaitļiem.",
    ]),

    Majas([
        "Salīdzini savas un drauga nedēļas soļu skaitu ar 3 rādītājiem.",
        "Uzraksti divu teikumu secinājumu.",
        "Izdomā divas kopas ar vienādu vidējo, bet dažādu amplitūdu.",
    ]),
]
