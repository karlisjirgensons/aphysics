# -*- coding: utf-8 -*-
"""4. klase, 50. stunda: «Kā uzzīmēt paralēlas līnijas baltā lapā?»

Rūtiņu lapā paralēlas līnijas ir jau gatavas; baltā lapā tās jāuzbūvē.
Ar diviem lineāliem (vai lineālu un uzstūri): vienu tur nekustīgi, otru
bīda gar to. Pārbaude - attālums starp līnijām ir vienāds vairākās vietās.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, linijas)

TEMA = "Kā uzzīmēt paralēlas līnijas baltā lapā?"

MERKIS = ("Ar diviem lineāliem zīmēsim paralēlas taisnas līnijas un "
          "pārbaudīsim rezultātu.")

SATURS = [
    Sakums("Kā uzzīmēt sliedes bez rūtiņām?",
           zimejums=linijas([(0, 3, 12, 3), (2, 1, 10, 1)],
                            uzraksti=[(6, 3.5, "a"), (6, 1.5, "b")],
                            platums=12, augstums=4),
           paraksts="Attālums starp a un b visur ir vienāds.",
           fakti=["Baltajā lapā rūtiņu nav - palīdz divi lineāli.",
                  "Arhitekti tā zīmēja rasējumus pirms datoriem."]),

    Doma("Bīdi otro lineālu gar pirmo",
         "Ja zīmējot lineāls pārvietojas, bet nemaina virzienu, visas "
         "novilktās līnijas ir paralēlas.",
         soli=[
             "Novelc taisni a gar lineāla malu.",
             "Pieliec otru lineālu (vai uzstūri) pie pirmā malas.",
             "Turi otro lineālu nekustīgu un bīdi pirmo gar to.",
             "Novelc taisni b. Pārbaudi attālumu 2-3 vietās.",
         ],
         pieze="Ja attālumi atšķiras, līnijas nav paralēlas - kāds lineāls "
               "pagriezās."),

    Slidnis("Kā lineāls slīd",
            soli=[
                {"v": "1. solis", "teksts": "Novelk taisni a.",
                 "zim": linijas([(0, 3, 12, 3)], platums=12, augstums=4)},
                {"v": "2. solis", "teksts": "Lineālu pabīda par 2 rūtiņām "
                 "uz leju, nepagriežot.",
                 "zim": linijas([(0, 3, 12, 3), (0, 1, 12, 1)],
                                platums=12, augstums=4)},
                {"v": "3. solis", "teksts": "Pabīda vēlreiz - trīs paralēlas "
                 "taisnes.",
                 "zim": linijas([(0, 3, 12, 3), (0, 1, 12, 1),
                                 (0, 0, 12, 0)],
                                platums=12, augstums=4)},
            ],
            ievads="Lineāls pārvietojas, bet nepagriežas."),

    Varianti("Vai būs paralēlas?", [
        {"jaut": "Lineāls tika pabīdīts un nedaudz pagriezts. Līnijas būs...",
         "opcijas": ["nav paralēlas", "paralēlas", "perpendikulāras"],
         "pareizi": 0, "padoms": "Pagrieziens maina virzienu."},
        {"jaut": "Attālums starp līnijām: kreisajā galā 3 cm, labajā 3 cm, "
                 "vidū 3 cm.",
         "opcijas": ["paralēlas", "nav paralēlas", "nevar zināt"],
         "pareizi": 0, "padoms": "Visur vienāds."},
        {"jaut": "Attālums: kreisajā galā 2 cm, labajā 4 cm.",
         "opcijas": ["nav paralēlas", "paralēlas", "perpendikulāras"],
         "pareizi": 0, "padoms": "Attālums mainās - tās tuvojas."},
        {"jaut": "Cik vietās vismaz jāpārbauda attālums?",
         "opcijas": ["divās", "vienā", "nevienā"], "pareizi": 0,
         "padoms": "Vienā vietā nepietiek, lai redzētu virzienu."},
    ], pamats=4),

    Ievadi("Rēķini ar paralēlām", [
        {"jaut": "Starp paralēlām taisnēm 3 cm. Uzzīmē vēl vienu tikpat "
                 "tālu zem otrās. Cik cm starp pirmo un trešo?",
         "atb": ["6"], "padoms": "3 + 3."},
        {"jaut": "Burtnīcas lapā līnijas ik pēc 8 mm. Cik mm starp 1. un "
                 "6. līniju?",
         "atb": ["40"], "padoms": "5 atstarpes · 8 mm."},
        {"jaut": "Lapā 20 cm augstumā jānovelk paralēlas līnijas ik pēc "
                 "2 cm. Cik atstarpju sanāks?",
         "atb": ["10"], "padoms": "20 : 2."},
        {"jaut": "Gājēju pārejā 7 baltas svītras ar atstarpēm starp tām. "
                 "Cik atstarpju?",
         "atb": ["6"], "padoms": "Viena mazāk nekā svītru."},
    ]),

    Pasaule("Stāvvietas marķējums",
            Ievadi("", [
                {"jaut": "Stāvvietā paralēlas līnijas ik pēc 3 m. Cik "
                         "automašīnu ietilps starp 11 līnijām?",
                 "atb": ["10"], "padoms": "Starp 11 līnijām - 10 vietas."},
                {"jaut": "Cik metru garš būs visu 10 vietu posms?",
                 "atb": ["30"], "padoms": "10 · 3."},
                {"jaut": "Katra līnija ir 5 m gara. Cik metru krāsas līnijas "
                         "jānovelk 11 līnijām?",
                 "atb": ["55"], "padoms": "11 · 5."},
                {"jaut": "Ja līnijas vilktu ik pēc 2 m 50 cm = 250 cm, cik "
                         "vietu sanāktu 30 m = 3000 cm garumā?",
                 "atb": ["12"], "padoms": "3000 : 250."},
            ]),
            pavediens="maja",
            konteksts="Stāvvietas līnijas krāso ar īpašu ratiņu, kas "
                      "pārvietojas paralēli iepriekšējai līnijai.",
            kapec="Paralēlas līnijas nodrošina, ka katrai mašīnai ir "
                  "vienāda vieta."),

    Petijums("Divu lineālu metode",
             soli=[
                 "Baltā lapā novelc taisni a.",
                 "Ar diviem lineāliem uzzīmē 3 taisnes, paralēlas a.",
                 "Ar lineālu izmēri attālumu starp a un b trīs vietās.",
                 "Pieraksti mērījumus. Vai tie vienādi?",
             ],
             vajag="balta lapa, divi lineāli vai lineāls un uzstūris",
             secinajums="Ja attālumi sakrīt, līnijas ir paralēlas."),

    Kopsavilkums([
        "Zīmēju paralēlas līnijas ar diviem lineāliem.",
        "Pārbaudu paralelitāti, mērot attālumu vairākās vietās.",
        "Zinu, ka pagriežot lineālu, paralelitāte pazūd.",
    ]),

    Majas([
        "Baltā lapā uzzīmē 5 paralēlas līnijas un izkrāso starp tām "
        "karogu.",
        "Izmēri attālumu starp burtnīcas līnijām.",
        "Pastāsti mājiniekiem, kā darbojas divu lineālu metode.",
    ]),
]
