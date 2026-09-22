# -*- coding: utf-8 -*-
"""5. klase, 166. stunda: «Kā attēlot savus datus?»

Pirmo reizi visā tematā dati nav doti - tie jāiegūst pašam. Tieši tur
parādās visas iepriekšējās stundas kopā: jāizvēlas, ko mērīt, jāsastāda
tabula, jāizvēlas asu vienības un jāizlemj, vai zīmēt punktus vai līniju.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         plakne, restis)

TEMA = "Kā attēlot savus datus?"

MERKIS = ("Mācīsimies iegūt datus par diviem lielumiem un attēlot tos "
          "koordinātu plaknē.")

SATURS = [
    Sakums("No mērījuma uz grafiku",
           zimejums=restis([["1", "2", "3", "4"],
                            ["12", "18", "25", "21"]],
                           virsraksts="Diena un skolēnu skaits"),
           paraksts="Katrs tabulas stabiņš kļūs par vienu punktu plaknē.",
           fakti=["Vispirms izvēlas, ko mērīt.",
                  "Tad datus pieraksta tabulā.",
                  "Tikai pēc tam zīmē grafiku."]),

    Doma("Tabula vispirms, grafiks pēc tam",
         "Savus datus attēlo pa soļiem: izvēlas divus lielumus, savāc datus "
         "tabulā, izvēlas asu vienības un atliek punktus plaknē.",
         soli=[
             "Izvēlies divus lielumus, kas saistīti savā starpā.",
             "Savāc datus un ieraksti tos tabulā.",
             "Atrodi lielāko vērtību katram lielumam.",
             "Izvēlies asu vienības tā, lai viss ietilptu.",
             "Atliec punktus un izlem, vai tos savienot.",
         ],
         pieze="Datus vispirms pieraksta tabulā, nevis uzreiz plaknē: tabulā "
               "tos var pārbaudīt un labot, bet no grafika kļūdaino punktu "
               "vairs neatšķirsi."),

    Petijums("Savāc un attēlo savus datus",
             soli=["Izvēlies, ko mērīsi: piemēram, mājasdarbu laiku katru "
                   "dienu.",
                   "Mēri piecas dienas un ieraksti datus tabulā.",
                   "Atrodi lielāko vērtību un izvēlies asu vienības.",
                   "Atliec punktus koordinātu plaknē.",
                   "Izlem, vai punktus savienot, un pamato izvēli."],
             vajag="rūtiņu lapa, lineāls, pulkstenis",
             secinajums="No pašu savāktiem datiem iznāk tāds pats grafiks kā "
                        "mācību grāmatā."),

    Paraugs("Piecu dienu dati",
            uzd="Kā attēlot mājasdarbu laiku piecās dienās?",
            soli=[
                ("Lielumi: diena un minūtes",
                 "Divi saistīti lielumi."),
                ("Tabula: 20, 35, 25, 40, 30",
                 "Dati par piecām dienām."),
                ("Lielākā vērtība ir 40",
                 "Pēc tās izvēlas vienību."),
                ("Uz y ass iedaļa 10 minūtes",
                 "40 : 10 = 4 iedaļas."),
                ("Punkti, nevis līnija",
                 "Starp dienām mērījumu nav."),
            ],
            atbilde="Pieci punkti ar iedaļu 10 minūtes"),

    Ievadi("Sagatavo savu grafiku", [
        {"jaut": "Dati: 20, 35, 25, 40, 30. Kāda ir lielākā vērtība?",
         "atb": ["40"], "padoms": "Lielākais skaitlis."},
        {"jaut": "Kāda ir mazākā vērtība?",
         "atb": ["20"], "padoms": "Mazākais skaitlis."},
        {"jaut": "Lielākā vērtība 40, iedaļu 4. Cik liela ir viena iedaļa?",
         "atb": ["10"], "padoms": "40 : 4."},
        {"jaut": "Cik punktu būs grafikā?",
         "atb": ["5"], "padoms": "Tik, cik datu."},
        {"jaut": "Kāds ir šo datu vidējais?",
         "atb": ["30"], "padoms": "150 : 5."},
        {"jaut": "Par cik minūtēm lielākā vērtība pārsniedz mazāko?",
         "atb": ["20"], "padoms": "40 - 20."},
        {"jaut": "Dati par dienām. Punkti vai līnija? Raksti vienu vārdu.",
         "atb": ["punkti"], "padoms": "Starp dienām mērījumu nav."},
        {"jaut": "Cik iedaļu vajag, ja lielākā vērtība ir 50 un iedaļa "
                 "ir 10?",
         "atb": ["5"], "padoms": "50 : 10."},
    ], pamats=4,
        ievads="Vispirms tabula un vienības, tikai tad punkti."),

    Zimejums("Pieci punkti no savas tabulas",
             plakne(punkti=[(1, 20, ""), (2, 35, ""), (3, 25, ""),
                            (4, 40, ""), (5, 30, "")],
                    no_x=0, lidz_x=6, no_y=0, lidz_y=50, solis=10,
                    virsraksts="Dienas un minūtes"),
             paskaidro="Punkti nav uz vienas taisnes, jo katru dienu laiks "
                       "bija citāds. Tie nav savienoti, jo starp dienām "
                       "mērījumu nav.",
             ievads="Tā izskatās savākto datu grafiks."),

    Varianti("Kā attēlo savus datus?", [
        {"jaut": "Ko dara vispirms?",
         "opcijas": ["Savāc datus tabulā", "Zīmē asis", "Izvēlas krāsas",
                     "Savieno punktus"],
         "pareizi": 0,
         "padoms": "Datus var pārbaudīt tikai tabulā."},
        {"jaut": "Pēc kā izvēlas asu vienību?",
         "opcijas": ["Pēc lielākās vērtības", "Pēc datu skaita",
                     "Pēc lapas izmēra", "Nejauši"],
         "pareizi": 0,
         "padoms": "Lai viss ietilptu."},
        {"jaut": "Dati par piecām dienām. Cik punktu būs grafikā?",
         "opcijas": ["5", "4", "10", "1"],
         "pareizi": 0,
         "padoms": "Viens punkts katrai dienai."},
        {"jaut": "Vai dienas datus savieno ar līniju?",
         "opcijas": ["Nē, starp dienām mērījumu nav", "Jā, vienmēr",
                     "Jā, ja punktu ir daudz", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "158. stundas kārtula."},
        {"jaut": "Kāpēc datus vispirms raksta tabulā?",
         "opcijas": ["Tur tos var pārbaudīt un labot", "Tā ir tradīcija",
                     "Tā ir ātrāk", "Tas nav vajadzīgs"],
         "pareizi": 0,
         "padoms": "Grafikā kļūdu neatšķirsi."},
        {"jaut": "Dati 20, 35, 25, 40, 30. Kāds ir vidējais?",
         "opcijas": ["30", "25", "40", "150"],
         "pareizi": 0,
         "padoms": "150 : 5."},
    ], pamats=4),

    Pasaule("Mana nedēļa skaitļos",
            Ievadi("", [
                {"jaut": "Mājasdarbiem veltītās minūtes: 20, 35, 25, 40, 30. "
                         "Cik minūšu kopā?",
                 "atb": ["150"], "padoms": "Saskaiti visus."},
                {"jaut": "Kāds ir vidējais laiks dienā?",
                 "atb": ["30"], "padoms": "150 : 5."},
                {"jaut": "Cik minūšu ir starpība starp garāko un īsāko "
                         "dienu?",
                 "atb": ["20"], "padoms": "40 - 20."},
                {"jaut": "Cik dienās laiks bija lielāks par vidējo?",
                 "atb": ["2"], "padoms": "35 un 40."},
            ]),
            pavediens="skola",
            konteksts="Pašu savākti dati par savu nedēļu ir tikpat īsti kā "
                      "tie, kas mācību grāmatā.",
            kapec="Grafiks parāda to, ko tabulā pamanīt ir grūtāk."),

    Kopsavilkums([
        "Izvēlos divus saistītus lielumus un savācu datus.",
        "Pierakstu datus tabulā, pirms zīmēju grafiku.",
        "Izvēlos asu vienības pēc lielākās vērtības.",
        "Izlemju, vai punktus savienot, un pamatoju izvēli.",
    ]),

    Majas([
        "Savāc datus par piecām dienām un ieraksti tos tabulā.",
        "Uzzīmē grafiku ar piemērotām asu vienībām.",
        "Pieraksti divus secinājumus no sava grafika.",
    ]),
]
