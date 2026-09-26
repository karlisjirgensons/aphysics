# -*- coding: utf-8 -*-
"""7. klase, 80. stunda: «Kāda ir pazīme lml?»

Otrā pazīme: ja trijstūru viena mala un abi tās pieleņķi ir vienādi, tad
trijstūri ir vienādi. No malas galiem novilktie stari krustojas tikai vienā
punktā - tā ir trešā virsotne. Uz šīs pazīmes balstās attāluma mērīšana ar
«triangulāciju».
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Petijums, Sakums, Varianti, Zimejums, geometrija)

TEMA = "Kāda ir pazīme lml?"

MERKIS = ("Konstruēsim trijstūri pēc malas un tās pieleņķiem un "
          "formulēsim pazīmi lml.")

_LML = geometrija([("A", 0, 0), ("B", 6, 0), ("C", 2, 3)],
                  nogriezni=["AB", "BC", "CA"],
                  lenki=[("BAC", "56°"), ("ABC", "37°")],
                  malas=[("AB", "6 cm")])

SATURS = [
    Sakums("Kā izmērīt upes platumu, to nešķērsojot?",
           zimejums=_LML,
           paraksts="Zinot AB un leņķus pie A un B, C vieta ir noteikta.",
           fakti=["No diviem krasta punktiem skatās uz koku otrā krastā.",
                  "Izmēra divus leņķus un attālumu starp punktiem.",
                  "Trijstūris ir noteikts - pēc pazīmes lml."]),

    Doma("Pazīme lml",
         "Ja viena trijstūra mala un tās pieleņķi ir attiecīgi vienādi ar "
         "otra trijstūra malu un tās pieleņķiem, tad šie trijstūri ir "
         "vienādi.",
         soli=[
             "Konstrukcija: uzzīmē AB.",
             "Pie A atliec doto leņķi, pie B - otru.",
             "Stari krustojas punktā C - tas var būt tikai viens.",
             "Pierādījumā: mala un abi leņķi tās GALOS.",
         ],
         pieze="Leņķiem jābūt tieši pie šīs malas. Ja viens leņķis ir "
               "pretī malai - jālieto citas zināšanas."),

    Paraugs("Pierādi ar lml",
            uzd="Nogriežņi AB un CD krustojas punktā O. AO = OB un "
                "∠OAC = ∠OBD. Pierādi, ka △AOC = △BOD.",
            soli=[
                ("AO = OB", "(dots)"),
                ("∠OAC = ∠OBD", "(dots)"),
                ("∠AOC = ∠BOD", "(krustleņķi)"),
                ("△AOC = △BOD", "(lml: mala AO un tās pieleņķi)"),
            ],
            atbilde="Pierādīts pēc pazīmes lml."),

    Zimejums("Pieleņķi pie malas AO",
             geometrija([("A", 0, 3), ("B", 6, -3), ("C", 0, -1.5),
                         ("D", 6, 1.5), ("O", 3, 0, 90)],
                        nogriezni=["AB", "CD", "AC", "BD"],
                        svitras=[("AO", 1), ("OB", 1)],
                        lenki=[("OAC", "", 2), ("OBD", "", 2),
                               ("AOC", ""), ("BOD", "")]),
             paskaidro="Mala AO un abi tās galu leņķi - vienādi ar BO un "
                       "tās leņķiem."),

    Varianti("Vai der lml?", [
        {"jaut": "AB = KL, ∠A = ∠K, ∠B = ∠L.",
         "opcijas": ["Der", "Neder"], "pareizi": 0, "jaukt": False,
         "padoms": "Leņķi pie AB galiem."},
        {"jaut": "AB = KL, ∠A = ∠K, ∠C = ∠M.",
         "opcijas": ["Der tieši", "Neder tieši - ∠C nav pie AB"],
         "pareizi": 1, "jaukt": False,
         "padoms": "∠C ir pretī AB (vēlāk to atrisinās leņķu summa)."},
        {"jaut": "Kura pazīme: divas malas un leņķis starp tām?",
         "opcijas": ["mlm", "lml", "mmm", "lll"],
         "pareizi": 0, "padoms": "m-l-m."},
        {"jaut": "Kura pazīme: mala un abi pieleņķi?",
         "opcijas": ["lml", "mlm", "mmm", "lll"],
         "pareizi": 0, "padoms": "l-m-l."},
    ], pamats=4),

    Petijums("Upes platums pagalmā",
             ["Izvēlies «otra krasta» punktu C (koks, stabs).",
              "Uz sava krasta atzīmē A un B 10 m attālumā.",
              "Izmēri leņķus CAB un CBA (ar transportieri uz kartona).",
              "Uzzīmē trijstūri mērogā 1 cm : 1 m un izmēri attālumu līdz C."],
             vajag="mērlente, kartona transportieris, papīrs",
             secinajums="No viena malas garuma un diviem leņķiem trijstūris "
                         "ir noteikts, tāpēc attālumu var izmērīt, to "
                         "nešķērsojot."),

    Pasaule("Kuģa atrašanās vieta",
            Varianti("", [
                {"jaut": "Divas bākas 12 km viena no otras redz kuģi 50° un "
                         "70° leņķī pret krasta līniju. Vai kuģa vieta ir "
                         "noteikta?",
                 "opcijas": ["Jā - pēc lml",
                             "Nē, vajag trešo bāku",
                             "Nē, vajag kuģa ātrumu",
                             "Nevar zināt"],
                 "pareizi": 0,
                 "padoms": "Mala un abi pieleņķi."},
                {"jaut": "Ko sauc par šo metodi?",
                 "opcijas": ["Triangulācija", "Fotosintēze",
                             "Navigācija ar kompasu", "Eholote"],
                 "pareizi": 0,
                 "padoms": "No vārda «trijstūris»."},
                {"jaut": "Ja bākas būtu tālāk viena no otras, mērījums "
                         "būtu...",
                 "opcijas": ["precīzāks", "neprecīzāks", "neiespējams",
                             "tāds pats"],
                 "pareizi": 0,
                 "padoms": "Garāka bāze - lielāki leņķi, mazāka kļūda."},
            ]),
            pavediens="celojums",
            konteksts="Pirms GPS kuģus un kartes noteica ar triangulāciju - "
                      "leņķiem un vienu zināmu attālumu.",
            kapec="lml ir attāluma mērīšana no tālienes."),

    Kopsavilkums([
        "Konstruēju trijstūri pēc malas un pieleņķiem.",
        "Formulēju pazīmi lml.",
        "Atšķiru pieleņķus no pretleņķa.",
        "Zinu triangulācijas ideju.",
    ]),

    Majas([
        "Konstruē trijstūri: AB = 7 cm, ∠A = 40°, ∠B = 60°.",
        "Izmēri attālumu līdz kokam, izmantojot divus leņķus.",
        "Uzraksti visas trīs pazīmes un katrai zīmējumu.",
    ]),
]
