# -*- coding: utf-8 -*-
"""6. klase, 14. stunda: «Kā nolasīt nezināmo no grafika?»

Grafiks no zīmējuma kļūst par rīku. Nolasīšana ir prasme, kuru prasa arī
eksāmens: atrast asī doto vērtību, uzkāpt līdz līnijai un nolasīt otru
skaitli. Te tā tiek vingrināta uz īstiem grafikiem, ne uz definīcijas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, plakne)

TEMA = "Kā nolasīt nezināmo no grafika?"

MERKIS = ("Iemācīsimies nolasīt lielumu vērtības no proporcionālu lielumu "
          "grafiskā attēla.")

SATURS = [
    Sakums("Grafiks atbild ātrāk nekā kalkulators",
           zimejums=plakne(lauzta=[(0, 0), (6, 30)], punkti=[(4, 20, "?")],
                           no_x=0, lidz_x=6, no_y=0, lidz_y=30, solis=1,
                           x_nos="h", y_nos="km"),
           paraksts="Ejot 5 km stundā: pēc 4 stundām - 20 km. Atbilde "
                    "nolasāma bez rēķināšanas.",
           fakti=["Uz grafika atbildi meklē ar divām kustībām: uz augšu un "
                  "uz sāniem.",
                  "Lasa vienmēr no tās ass, kurā skaitlis ir dots."]),

    Doma("Uzkāp līdz līnijai un pagriezies",
         "Lai nolasītu nezināmo, no dotās vērtības ej perpendikulāri līdz "
         "līnijai un tad - līdz otrai asij.",
         soli=[
             "Atrodi doto skaitli uz tās ass, kurā tas ir.",
             "Ej no tā taisni līdz līnijai.",
             "No līnijas ej taisni līdz otrai asij.",
             "Nolasi skaitli un pieraksti to ar mērvienību.",
             "Pārbaudi ar rēķinu: vai dalījums sakrīt ar pārējiem punktiem?",
         ],
         pieze="Ja vērtība iekrīt starp iedaļām, atbildi sniedz aptuveni - "
               "«apmēram 17 km». Tas nav slikti: grafiku lasa tieši tāpēc, "
               "ka vajag ātru novērtējumu."),

    Paraugs("Nolasi ceļu un laiku",
            uzd="Grafikā redzams: 6 stundās veikti 30 km. Cik km veikti "
                "4 stundās un cik stundās veikti 15 km?",
            soli=[
                ("30 : 6 = 5 km stundā",
                 "Viena vienība - tas pats grafika slīpums."),
                ("4 h → 4 · 5 = 20 km",
                 "No horizontālās ass uz augšu līdz līnijai."),
                ("15 : 5 = 3 h",
                 "No vertikālās ass uz sāniem līdz līnijai."),
                ("Pārbaude: punkti (4; 20) un (3; 15) ir uz tās pašas "
                 "taisnes",
                 "Abi dalījumi dod 5."),
            ],
            atbilde="20 km un 3 stundas"),

    Ievadi("Nolasi no grafika", [
        {"jaut": "Taisne iet caur (0; 0) un (6; 30). Cik ir y, ja x = 2?",
         "atb": ["10"], "padoms": "Viena vienība ir 5.",
         "zim": plakne(lauzta=[(0, 0), (6, 30)], no_x=0, lidz_x=6, no_y=0,
                       lidz_y=30, solis=1, x_nos="h", y_nos="km")},
        {"jaut": "Tā pati taisne. Cik ir x, ja y = 25?",
         "atb": ["5"], "padoms": "25 : 5."},
        {"jaut": "Taisne iet caur (0; 0) un (4; 12). Cik ir y, ja x = 7?",
         "atb": ["21"], "padoms": "Viena vienība ir 3."},
        {"jaut": "Tā pati taisne. Cik ir x, ja y = 9?",
         "atb": ["3"], "padoms": "9 : 3."},
        {"jaut": "Grafikā 8 kg maksā 24 €. Cik eiro maksā 5 kg?",
         "atb": ["15"], "padoms": "Viena vienība ir 3 €."},
        {"jaut": "Tas pats grafiks. Cik kilogramu var nopirkt par 36 €?",
         "atb": ["12"], "padoms": "36 : 3."},
    ], pamats=4,
        ievads="Vispirms atrodi vienas vienības vērtību - tā ir visa "
               "grafika atslēga."),

    Zimejums("Divi nolasījumi vienā zīmējumā",
             plakne(lauzta=[(0, 0), (8, 24)],
                    punkti=[(5, 15, "15 €"), (2, 6, "6 €")],
                    no_x=0, lidz_x=8, no_y=0, lidz_y=24, solis=2,
                    x_nos="kg", y_nos="€"),
             paskaidro="5 kg maksā 15 €, 2 kg maksā 6 €. Abi punkti ir uz "
                       "vienas taisnes, jo cena ir proporcionāla masai.",
             ievads="Vienā grafikā var nolasīt tik atbilžu, cik vajag."),

    Varianti("Kur meklēt atbildi?", [
        {"jaut": "Zināms laiks, meklē ceļu. No kuras ass sāk?",
         "opcijas": ["No horizontālās, kur atlikts laiks",
                     "No vertikālās", "No koordinātu sākumpunkta",
                     "No līnijas gala"],
         "pareizi": 0,
         "padoms": "Sāk vienmēr no tā, kas ir dots."},
        {"jaut": "Vērtība iekrīt starp divām iedaļām. Ko darīt?",
         "opcijas": ["Nolasīt aptuveni un tā arī pateikt",
                     "Noapaļot līdz tuvākajai iedaļai un klusēt",
                     "Uzskatīt, ka grafiks ir nepareizs",
                     "Meklēt citu grafiku"],
         "pareizi": 0,
         "padoms": "Grafiks dod novērtējumu, un to arī pierakstām."},
        {"jaut": "Taisne iet caur (3; 18). Kāda ir vienas vienības vērtība?",
         "opcijas": ["6", "3", "18", "15"],
         "pareizi": 0,
         "padoms": "18 : 3."},
        {"jaut": "Divas taisnes sākas nullē, viena ir stāvāka. Ko tas "
                 "nozīmē?",
         "opcijas": ["Stāvākajai lielāka vienas vienības vērtība",
                     "Stāvākā ir garāka",
                     "Stāvākā ir nepareiza",
                     "Abas ir vienādas"],
         "pareizi": 0,
         "padoms": "Slīpums ir tieši vienas vienības vērtība."},
    ], pamats=4),

    Pasaule("Cik tālu aiziet pārgājienā?",
            Ievadi("", [
                {"jaut": "Grupa iet 4 km stundā. Cik km tā noiet 3 stundās?",
                 "atb": ["12"], "padoms": "3 · 4.",
                 "zim": plakne(lauzta=[(0, 0), (5, 20)], no_x=0, lidz_x=5,
                               no_y=0, lidz_y=20, solis=1, x_nos="h",
                               y_nos="km")},
                {"jaut": "Cik stundas vajag 18 km?",
                 "atb": ["4,5", "4.5"], "padoms": "18 : 4."},
                {"jaut": "Pusdienas ir pēc 10 km. Cik stundas līdz tām?",
                 "atb": ["2,5", "2.5"], "padoms": "10 : 4."},
                {"jaut": "Maršruts ir 20 km. Cik stundas tas prasīs?",
                 "atb": ["5"], "padoms": "20 : 4."},
            ]),
            pavediens="celojums",
            konteksts="Pārgājiena plānā vispirms uzzīmē grafiku - tad redz, "
                      "vai grupa paspēs līdz tumsai.",
            kapec="Grafiks atbild uz abiem: cik tālu un cik ilgi."),

    Kopsavilkums([
        "Nolasu nezināmo vērtību no proporcionālu lielumu grafika.",
        "Zinu, ka sākt jālasa no tās ass, kurā skaitlis ir dots.",
        "Nosaku vienas vienības vērtību no jebkura grafika punkta.",
        "Pasaku, kad atbilde ir precīza un kad - aptuvena.",
    ]),

    Majas([
        "Uzzīmē grafiku savam gājiena ātrumam un nolasi, cik tālu tiktu "
        "2 stundās.",
        "Atrodi grafiku ziņās un nolasi no tā vienu vērtību.",
        "Pieraksti, kurā gadījumā grafiks ir noderīgāks nekā rēķins.",
    ]),
]
