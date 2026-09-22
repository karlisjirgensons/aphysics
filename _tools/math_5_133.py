# -*- coding: utf-8 -*-
"""5. klase, 133. stunda: «Ko nozīmē paplašināt decimāldaļu?»

Daļas pamatīpašība te atgriežas jaunā izskatā: 0,7 = 0,70 ir tā pati
{7|10} = {70|100}. Skolēnam tas šķiet dīvaini - skaitlis it kā kļuva garāks,
bet vērtība nemainījās. Tieši šī nulle beigās vēlāk ļaus salīdzināt un atņemt
skaitļus ar dažādu ciparu skaitu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala, restis)

TEMA = "Ko nozīmē paplašināt decimāldaļu?"

MERKIS = ("Mācīsimies skaidrot decimāldaļas paplašināšanu un lietot to "
          "salīdzināšanai.")

SATURS = [
    Sakums("Nulle beigās neko nemaina",
           zimejums=dala(10, 7, "7/10 = 70/100"),
           paraksts="0,7 = 0,70 - tas pats daudzums, cits pieraksts.",
           fakti=["Veikalā cenu raksta 0,70 €, nevis 0,7 €.",
                  "Abi skaitļi ir vienādi.",
                  "Nulle beigās maina tikai šķiru skaitu."]),

    Doma("Nulli beigās drīkst pierakstīt",
         "Decimāldaļas beigās drīkst pierakstīt vai noņemt nulles - skaitļa "
         "vērtība nemainās, jo tā ir daļas paplašināšana.",
         soli=[
             "Paskaties, cik ciparu ir aiz komata katram skaitlim.",
             "Pieraksti nulles tam, kuram ciparu ir mazāk.",
             "Tagad abiem skaitļiem aiz komata ir vienāds ciparu skaits.",
             "Salīdzini vai rēķini kā ar veseliem skaitļiem.",
             "Atbildē nulles beigās drīkst noņemt.",
         ],
         pieze="Nulli drīkst pierakstīt tikai beigās: 0,7 = 0,70, bet 0,7 "
               "nav 0,07. Pirmajā gadījumā nulle nāk klāt pēdējā šķirā, "
               "otrajā - izspiež ciparu uz sīkāku šķiru."),

    Paraugs("Salīdzini 0,7 un 0,68",
            uzd="Kurš skaitlis ir lielāks?",
            soli=[
                ("0,7 ir viens cipars aiz komata",
                 "0,68 ir divi."),
                ("0,7 = 0,70",
                 "Paplašina līdz simtdaļām."),
                ("70 simtdaļas pret 68 simtdaļām",
                 "Tagad salīdzināt var."),
                ("0,70 > 0,68",
                 "Tātad 0,7 > 0,68."),
            ],
            atbilde="0,7 ir lielāks"),

    Ievadi("Paplašini un salīdzini", [
        {"jaut": "0,7 ar diviem cipariem aiz komata. Ieraksti skaitli.",
         "atb": ["0,70"], "padoms": "Pieraksti nulli beigās."},
        {"jaut": "0,5 ar trim cipariem aiz komata. Ieraksti skaitli.",
         "atb": ["0,500"], "padoms": "Divas nulles beigās."},
        {"jaut": "0,7 vai 0,68 - kurš lielāks? Ieraksti skaitli.",
         "atb": ["0,7", "0,70"], "padoms": "0,70 pret 0,68."},
        {"jaut": "0,4 vai 0,39 - kurš lielāks? Ieraksti skaitli.",
         "atb": ["0,4", "0,40"], "padoms": "0,40 pret 0,39."},
        {"jaut": "0,25 vai 0,3 - kurš lielāks? Ieraksti skaitli.",
         "atb": ["0,3", "0,30"], "padoms": "0,30 pret 0,25."},
        {"jaut": "1,5 vai 1,49 - kurš lielāks? Ieraksti skaitli.",
         "atb": ["1,5", "1,50"], "padoms": "1,50 pret 1,49."},
        {"jaut": "Vai 0,8 un 0,80 ir vienādi? Raksti «jā» vai «nē».",
         "atb": ["jā", "ja"], "padoms": "Nulle beigās."},
        {"jaut": "Vai 0,8 un 0,08 ir vienādi? Raksti «jā» vai «nē».",
         "atb": ["nē", "ne"], "padoms": "Nulle priekšā maina šķiru."},
    ], pamats=4,
        ievads="Vispirms izlīdzini ciparu skaitu, tikai tad salīdzini."),

    Zimejums("Viens skaitlis, divi pieraksti",
             restis([["0,7", "0,70"],
                     ["0,5", "0,500"]],
                    virsraksts="Nulles beigās neko nemaina"),
             paskaidro="Abās rindās kreisais un labais skaitlis ir vienāds. "
                       "Nulle beigās tikai pasaka, ka sīkāku šķiru nav.",
             ievads="Paplašināšana decimāldaļām izskatās tieši šādi."),

    Varianti("Vai nulle ko maina?", [
        {"jaut": "Vai 0,7 un 0,70 ir vienādi?",
         "opcijas": ["Jā", "Nē, 0,70 ir lielāks", "Nē, 0,7 ir lielāks",
                     "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Nulle beigās."},
        {"jaut": "Vai 0,7 un 0,07 ir vienādi?",
         "opcijas": ["Nē, 0,7 ir desmitreiz lielāks", "Jā",
                     "Nē, 0,07 ir lielāks", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Nulle priekšā maina šķiru."},
        {"jaut": "Kurš skaitlis ir lielāks: 0,4 vai 0,39?",
         "opcijas": ["0,4", "0,39", "Vienādi", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "0,40 pret 0,39."},
        {"jaut": "Ko dara pirms salīdzināšanas?",
         "opcijas": ["Izlīdzina ciparu skaitu aiz komata",
                     "Noņem komatu",
                     "Saskaita ciparus",
                     "Neko"],
         "pareizi": 0,
         "padoms": "Vienādas šķiras."},
        {"jaut": "0,5 ar trim cipariem aiz komata ir...",
         "opcijas": ["0,500", "0,005", "5,000", "0,05"],
         "pareizi": 0,
         "padoms": "Nulles pieraksta beigās."},
        {"jaut": "Kāpēc veikalā raksta 0,70 €?",
         "opcijas": ["Centi vienmēr ir divi cipari", "Tā ir lielāka cena",
                     "Tā ir kļūda", "Tā ir īsāk"],
         "pareizi": 0,
         "padoms": "Simtdaļas ir centi."},
    ], pamats=4),

    Pasaule("Kura cena ir zemāka?",
            Ievadi("", [
                {"jaut": "Viena prece maksā 0,7 €, otra 0,68 €. Kura ir "
                         "lētāka? Ieraksti cenu.",
                 "atb": ["0,68"], "padoms": "0,70 pret 0,68."},
                {"jaut": "Viena prece 1,5 €, otra 1,45 €. Kura ir lētāka? "
                         "Ieraksti cenu.",
                 "atb": ["1,45"], "padoms": "1,50 pret 1,45."},
                {"jaut": "Viena prece 2,4 €, otra 2,39 €. Kura ir lētāka? "
                         "Ieraksti cenu.",
                 "atb": ["2,39"], "padoms": "2,40 pret 2,39."},
                {"jaut": "Cik centu ir cena 0,7 €?",
                 "atb": ["70"], "padoms": "0,7 = 0,70."},
            ]),
            pavediens="veikals",
            konteksts="Cenu zīmēs vienmēr ir divi cipari aiz komata, bet "
                      "reklāmā tos reizēm raksta īsāk.",
            kapec="Salīdzināt var tikai tad, kad ciparu skaits ir vienāds."),

    Kopsavilkums([
        "Skaidroju, ka nulle decimāldaļas beigās vērtību nemaina.",
        "Paplašinu decimāldaļu līdz vajadzīgajam ciparu skaitam.",
        "Salīdzinu decimāldaļas, iepriekš izlīdzinot ciparu skaitu.",
        "Atšķiru nulli beigās no nulles pirms cipariem.",
    ]),

    Majas([
        "Pieraksti ar trim cipariem aiz komata 0,4, 1,25 un 0,7.",
        "Salīdzini 0,6 un 0,59; 0,8 un 0,801.",
        "Atrodi veikalā divas cenas, kuras atšķiras par vienu centu.",
    ]),
]
