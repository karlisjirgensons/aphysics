# -*- coding: utf-8 -*-
"""5. klase, 64. stunda: «Kāda daļa ir starp divām dotajām?»

Mikrotemata noslēgums un pirmā stunda, kurā paplašināšanu lieto nevis tāpēc,
ka saucēji atšķiras, bet tāpēc, ka vietas ir par maz. Ja starp diviem
skaitītājiem nav neviena vesela skaitļa, tos abus paplašina - un vieta
rodas. Tieši te skolēns pirmo reizi redz, ka starp divām daļām vienmēr ir
vēl viena.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kāda daļa ir starp divām dotajām?"

MERKIS = ("Mācīsimies nosaukt daļu, kas uz skaitļu taisnes atrodas starp "
          "divām dotajām daļām.")

SATURS = [
    Sakums("Vai starp tām vispār kas ir?",
           zimejums=taisne(0, 1, 1, [(1 / 4.0, "1/4"), (1 / 2.0, "1/2")],
                           virsraksts="Divas daļas un tukšums starp tām"),
           paraksts="Starp {1|4} un {1|2} ir bezgalīgi daudz daļu - viena no "
                    "tām ir {3|8}.",
           fakti=["Starp diviem blakus veseliem skaitļiem nav neviena vesela.",
                  "Starp divām daļām vienmēr ir vēl kāda daļa.",
                  "Lai to ieraudzītu, vienību sadala sīkāk."]),

    Doma("Ja vietas nav, sadali sīkāk",
         "Lai atrastu daļu starp divām dotajām, abas pārraksta ar kopīgu "
         "saucēju; ja starp skaitītājiem nav vietas, saucēju palielina vēl.",
         soli=[
             "Pārraksti abas daļas ar kopīgu saucēju.",
             "Paskaties, vai starp skaitītājiem ir vesels skaitlis.",
             "Ja ir - tas arī ir meklētā daļa.",
             "Ja nav - reizini abus locekļus vēl ar 2.",
             "Tagad starp skaitītājiem vieta ir vienmēr.",
         ],
         pieze="Starp {1|2} un {2|3} ar saucēju 6 ir {3|6} un {4|6} - vietas "
               "nav. Ar saucēju 12 tās kļūst {6|12} un {8|12}, un starp tām "
               "ir {7|12}."),

    Paraugs("Kas ir starp {1|4} un {1|2}?",
            uzd="Nosauc vienu daļu, kas atrodas starp {1|4} un {1|2}.",
            soli=[
                ("Kopīgais saucējs ir 4",
                 "{1|4} un {2|4}."),
                ("Starp 1 un 2 vesela skaitļa nav",
                 "Vieta par šauru - saucēju palielina."),
                ("{2|8} un {4|8}",
                 "Abus locekļus reizina ar 2."),
                ("Starp 2 un 4 ir 3",
                 "Tas ir meklētais skaitītājs."),
                ("{2|8} < {3|8} < {4|8}",
                 "Tātad {3|8} atrodas starp dotajām daļām."),
            ],
            atbilde="Piemēram, {3|8}"),

    Ievadi("Atrodi vidējo skaitītāju", [
        {"jaut": "Ar saucēju 8: {2|8} un {4|8}. Kāds skaitītājs ir starp "
                 "tiem?",
         "atb": ["3"], "padoms": "Starp 2 un 4."},
        {"jaut": "Ar saucēju 12: {6|12} un {8|12}. Kāds skaitītājs ir starp "
                 "tiem?",
         "atb": ["7"], "padoms": "Starp 6 un 8."},
        {"jaut": "Ar saucēju 10: {3|10} un {7|10}. Nosauc vienu skaitītāju "
                 "starp tiem.",
         "atb": ["4", "5", "6"], "padoms": "Der 4, 5 vai 6."},
        {"jaut": "{1|2} ar saucēju 12 - kāds ir skaitītājs?",
         "atb": ["6"], "padoms": "12 : 2."},
        {"jaut": "{2|3} ar saucēju 12 - kāds ir skaitītājs?",
         "atb": ["8"], "padoms": "12 : 3 = 4; 2 · 4."},
        {"jaut": "{1|3} ar saucēju 18 - kāds ir skaitītājs?",
         "atb": ["6"], "padoms": "18 : 3."},
        {"jaut": "{1|2} ar saucēju 18 - kāds ir skaitītājs?",
         "atb": ["9"], "padoms": "18 : 2."},
        {"jaut": "Nosauc vienu skaitītāju starp 6 un 9.",
         "atb": ["7", "8"], "padoms": "Der 7 vai 8."},
    ], pamats=4,
        ievads="Vispirms viens saucējs, tad meklē vietu starp skaitītājiem."),

    Zimejums("Trīs punkti vienā rindā",
             taisne(0, 1, 1, [(2 / 8.0, "2/8"), (3 / 8.0, "3/8"),
                              (4 / 8.0, "4/8")],
                    virsraksts="Ar saucēju 8 vieta ir"),
             paskaidro="{2|8} ir tā pati {1|4}, bet {4|8} - tā pati {1|2}. "
                       "Vidū iederas {3|8}.",
             ievads="Sīkāka iedaļa atklāj punktu, kas iepriekš nebija "
                    "redzams."),

    Varianti("Cik daļu ir starp divām daļām?", [
        {"jaut": "Cik daļu atrodas starp {1|4} un {1|2}?",
         "opcijas": ["Bezgalīgi daudz", "Viena", "Neviena", "Trīs"],
         "pareizi": 0,
         "padoms": "Saucēju var palielināt bezgalīgi."},
        {"jaut": "Ar saucēju 6 daļas ir {3|6} un {4|6}. Ko dara tālāk?",
         "opcijas": ["Reizina abus locekļus ar 2",
                     "Saīsina abas daļas",
                     "Saka, ka starp tām nekā nav",
                     "Salīdzina saucējus"],
         "pareizi": 0,
         "padoms": "Vajag vairāk vietas starp skaitītājiem."},
        {"jaut": "Kura daļa atrodas starp {1|3} un {1|2}?",
         "opcijas": ["{5|12}", "{1|4}", "{7|12}", "{2|3}"],
         "pareizi": 0,
         "padoms": "Ar saucēju 12: {4|12} un {6|12}."},
        {"jaut": "Kura daļa *nav* starp {2|5} un {4|5}?",
         "opcijas": ["{1|5}", "{3|5}", "{5|10}", "{7|10}"],
         "pareizi": 0,
         "padoms": "Tā ir pa kreisi no abām."},
        {"jaut": "Kāpēc saucēju palielina?",
         "opcijas": ["Lai starp skaitītājiem rastos vesels skaitlis",
                     "Lai daļa kļūtu lielāka",
                     "Lai to varētu saīsināt",
                     "Lai skaitļi būtu skaistāki"],
         "pareizi": 0,
         "padoms": "Sīkāka iedaļa - vairāk punktu."},
        {"jaut": "Starp {1|2} un {2|3} ar saucēju 12 ir...",
         "opcijas": ["{7|12}", "{5|12}", "{9|12}", "{12|12}"],
         "pareizi": 0,
         "padoms": "{6|12} un {8|12}."},
    ], pamats=4),

    Pasaule("Starp diviem rezultātiem",
            Ievadi("", [
                {"jaut": "Anna trāpīja {1|2}, Elza {2|3} metienu. Ar saucēju "
                         "12 - kāds skaitītājs ir Annai?",
                 "atb": ["6"], "padoms": "{1|2} = {6|12}."},
                {"jaut": "Kāds skaitītājs ar saucēju 12 ir Elzai?",
                 "atb": ["8"], "padoms": "{2|3} = {8|12}."},
                {"jaut": "Roberta rezultāts ir starp abiem. Kāds ir viņa "
                         "skaitītājs ar saucēju 12?",
                 "atb": ["7"], "padoms": "Starp 6 un 8."},
                {"jaut": "Marks trāpīja starp {1|4} un {1|2}. Kāds ir viņa "
                         "skaitītājs ar saucēju 8?",
                 "atb": ["3"], "padoms": "Starp {2|8} un {4|8}."},
            ]),
            pavediens="sports",
            konteksts="Tabulā starp diviem rezultātiem vienmēr var iespraust "
                      "vēl vienu spēlētāju.",
            kapec="Sīkāka iedaļa parāda atšķirību, ko rupjā tabula noklusē."),

    Kopsavilkums([
        "Pārrakstu divas daļas ar kopīgu saucēju.",
        "Nosaucu daļu, kas atrodas starp tām.",
        "Palielinu saucēju, ja starp skaitītājiem nav vietas.",
        "Zinu, ka starp divām daļām vienmēr ir vēl kāda daļa.",
    ]),

    Majas([
        "Nosauc divas daļas, kas atrodas starp {1|3} un {2|3}.",
        "Atrodi daļu starp {3|4} un {4|5} un pieraksti, kā to atradi.",
        "Padomā, vai starp {1|2} un {1|2} var atrast kādu daļu.",
    ]),
]
