# -*- coding: utf-8 -*-
"""6. klase, 115. stunda: «Kā izpētīt ledus kušanu?»

Programmas mājas eksperiments. Skolēns pats plāno mērījumus, apkopo tos
tabulā un attēlo grafikā - un tieši šis grafiks parāda to, ko nevar
izlasīt: kušanas laikā temperatūra kādu brīdi nemainās.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         plakne)

TEMA = "Kā izpētīt ledus kušanu?"

MERKIS = ("Plānosim mājas eksperimentu, apkoposim datus tabulā un attēlosim "
          "tos grafiski.")

SATURS = [
    Sakums("Kūstot temperatūra apstājas",
           zimejums=plakne(lauzta=[(0, -6), (2, -3), (4, 0), (6, 0),
                                   (8, 0), (10, 4)],
                           no_x=0, lidz_x=10, no_y=-8, lidz_y=6, solis=2,
                           x_nos="min", y_nos="°C"),
           paraksts="Kamēr ledus kūst, temperatūra turas pie nulles - "
                    "grafikā tā ir horizontāla līnija.",
           fakti=["Eksperimentā mērījumus veic vienādos laika intervālos.",
                  "Datus vispirms pieraksta tabulā, tikai tad zīmē.",
                  "Horizontāla grafika daļa nozīmē, ka lielums nemainās."]),

    Doma("Plāno, mēri, pieraksti, zīmē",
         "Eksperimentu plāno pirms tā sākuma: jāzina, ko mērīs, cik bieži un "
         "cik ilgi; tikai tad dati būs salīdzināmi.",
         soli=[
             "Pieraksti, ko mērīsi un kādā mērvienībā.",
             "Izvēlies mērījumu intervālu un kopējo laiku.",
             "Sagatavo tabulu ar divām rindām.",
             "Veic mērījumus un pieraksti tos uzreiz.",
             "Attēlo datus plaknē un izstāsti grafiku.",
         ],
         pieze="Mērījumu intervālam jābūt vienādam - citādi grafiks melo. Ja "
               "viens mērījums izlaists, to atzīmē kā iztrūkstošu, nevis "
               "aizpilda ar minējumu."),

    Paraugs("Saplāno eksperimentu",
            uzd="Kā izpētīt, kā silst ledus gabaliņš glāzē?",
            soli=[
                ("Mērīsim temperatūru grādos",
                 "Lielums un mērvienība."),
                ("Ik pēc 2 minūtēm, 10 minūtes",
                 "Sanāks 6 mērījumi."),
                ("Tabula: augšā minūtes, apakšā grādi",
                 "Sagatavo pirms sākuma."),
                ("Mērījumi: −6; −3; 0; 0; 0; 4",
                 "Vidū temperatūra nemainās."),
                ("Grafikā tā ir horizontāla daļa",
                 "Tieši tur ledus kūst."),
            ],
            atbilde="6 mērījumi ik pēc 2 minūtēm"),

    Ievadi("Nolasi eksperimenta datus", [
        {"jaut": "Mērījumi: 0 min → −6 °C. Cik grādu bija sākumā?",
         "atb": ["-6", "−6"], "padoms": "Pirmais mērījums.",
         "zim": plakne(lauzta=[(0, -6), (2, -3), (4, 0), (6, 0), (8, 0),
                               (10, 4)],
                       no_x=0, lidz_x=10, no_y=-8, lidz_y=6, solis=2,
                       x_nos="min", y_nos="°C")},
        {"jaut": "Pie kuras minūtes temperatūra sasniedza 0 °C?",
         "atb": ["4"], "padoms": "Grafiks šķērso asi."},
        {"jaut": "Cik minūtes temperatūra turējās pie nulles?",
         "atb": ["4"], "padoms": "No 4 līdz 8 minūtei."},
        {"jaut": "Cik grādu bija pie 10 minūtes?",
         "atb": ["4"], "padoms": "Pēdējais mērījums."},
        {"jaut": "Par cik grādiem temperatūra pieauga pirmajās 4 minūtēs?",
         "atb": ["6"], "padoms": "No −6 līdz 0."},
        {"jaut": "Cik mērījumu ir kopā, ja mēra ik pēc 2 minūtēm 10 minūtes, "
                 "ieskaitot sākumu?",
         "atb": ["6"], "padoms": "0; 2; 4; 6; 8; 10."},
    ], pamats=4),

    Petijums("Izpēti ledus kušanu mājās",
             vajag="ledus gabaliņi, glāze, termometrs, pulkstenis",
             soli=[
                 "Ieliec glāzē ledus gabaliņus un iemērc termometru.",
                 "Pieraksti temperatūru ik pēc 2 minūtēm 10 minūtes.",
                 "Apkopo datus tabulā ar divām rindām.",
                 "Uzzīmē grafiku, ietverot arī negatīvās vērtības.",
                 "Pieraksti, cik ilgi temperatūra turējās pie nulles.",
             ],
             secinajums="Kamēr glāzē ir ledus, temperatūra pie nulles "
                        "nemainās - enerģija aiziet kušanai, ne sildīšanai."),

    Varianti("Ko rāda grafika forma?", [
        {"jaut": "Horizontāla grafika daļa nozīmē...",
         "opcijas": ["lielums nemainās", "lielums aug",
                     "mērījumu trūkst", "kļūdu"],
         "pareizi": 0,
         "padoms": "Vērtība paliek tā pati."},
        {"jaut": "Kāpēc mērījumu intervālam jābūt vienādam?",
         "opcijas": ["Lai grafiks rādītu īsto izmaiņas ātrumu",
                     "Lai būtu vieglāk skaitīt",
                     "Lai tabula būtu skaista", "Nav iemesla"],
         "pareizi": 0,
         "padoms": "Nevienādi intervāli izkropļo līniju."},
        {"jaut": "Ko darīt, ja viens mērījums izlaists?",
         "opcijas": ["Atzīmēt kā iztrūkstošu", "Aizpildīt ar minējumu",
                     "Izmest visus datus", "Atkārtot iepriekšējo"],
         "pareizi": 0,
         "padoms": "Minējums nav mērījums."},
        {"jaut": "Kurā grafika daļā ledus kūst?",
         "opcijas": ["Tur, kur līnija ir horizontāla pie nulles",
                     "Sākumā", "Beigās", "Nevar noteikt"],
         "pareizi": 0,
         "padoms": "Temperatūra nemainās."},
    ], pamats=4),

    Pasaule("Cik ilgi kūst sniegs?",
            Ievadi("", [
                {"jaut": "No rīta −6 °C, temperatūra aug par 2 grādiem "
                         "stundā. Pēc cik stundām būs 0 °C?",
                 "atb": ["3"], "padoms": "6 : 2."},
                {"jaut": "Cik grādu būs pēc 5 stundām?",
                 "atb": ["4"], "padoms": "−6 + 10."},
                {"jaut": "Ja temperatūra 2 stundas turas pie nulles, pēc cik "
                         "stundām no rīta tā sāk celties virs nulles?",
                 "atb": ["5"], "padoms": "3 + 2."},
                {"jaut": "Cik stundu kopā bija zem nulles?",
                 "atb": ["3"], "padoms": "Līdz nullei."},
            ]),
            pavediens="planeta",
            konteksts="Pavasarī sniegs kūst tieši tāpat: temperatūra kādu "
                      "laiku turas pie nulles, un tikai tad ceļas.",
            kapec="Grafika horizontālā daļa ir kušanas laiks."),

    Zimejums("Kušanas grafiks",
             plakne(lauzta=[(0, -6), (2, -3), (4, 0), (6, 0), (8, 0),
                            (10, 4)],
                    no_x=0, lidz_x=10, no_y=-8, lidz_y=6, solis=2,
                    x_nos="min", y_nos="°C"),
             paskaidro="Trīs daļas: sildīšanās zem nulles, kušana pie nulles "
                       "un sildīšanās virs nulles.",
             ievads="Vienā grafikā redz visu eksperimentu."),

    Kopsavilkums([
        "Plānoju eksperimentu: ko, cik bieži un cik ilgi mērīšu.",
        "Apkopoju mērījumus tabulā.",
        "Attēloju datus koordinātu plaknē.",
        "Paskaidroju, ko nozīmē horizontālā grafika daļa.",
    ]),

    Majas([
        "Veic ledus kušanas eksperimentu un pieraksti sešus mērījumus.",
        "Uzzīmē grafiku un atzīmē kušanas laiku.",
        "Pieraksti, cik ilgi temperatūra turējās pie nulles.",
    ]),
]
