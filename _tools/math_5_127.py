# -*- coding: utf-8 -*-
"""5. klase, 127. stunda: «Kā atrast nezināmo malu?»

Reālos rasējumos nav atzīmēti visi izmēri - daži ir jāizrēķina. Kombinētā
figūrā tas ir vienkārši: pretējo malu summas sakrīt, tāpēc trūkstošo garumu
iegūst, saskaitot vai atņemot zināmos. Tieši šis solis parasti ir pirmais,
pirms vispār var ķerties pie laukuma.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, figura)

TEMA = "Kā atrast nezināmo malu?"

MERKIS = ("Iemācīsimies aprēķināt kombinētas figūras nezināmo malu garumus, "
          "saskaitot vai atņemot zināmos.")

SATURS = [
    Sakums("Rasējumā trūkst divu izmēru",
           zimejums=figura([(0, 0), (6, 0), (6, 2), (3, 2), (3, 5), (0, 5)],
                           uzraksti=[(3, -0.4, "6"), (6.6, 1, "2"),
                                     (-0.6, 2.5, "5")],
                           virsraksts="Trīs malas dotas, trīs nav"),
           paraksts="Trūkstošās malas var izrēķināt no dotajām.",
           fakti=["Rasējumā atzīmē tikai daļu izmēru.",
                  "Pārējos var atrast ar saskaitīšanu vai atņemšanu.",
                  "Pretējo malu summas kombinētā figūrā sakrīt."]),

    Doma("Pretējo malu summas sakrīt",
         "Kombinētā figūrā ar taisniem leņķiem visu vienā virzienā vērsto "
         "malu summa ir vienāda ar pretējā virzienā vērsto malu summu.",
         soli=[
             "Sagrupē malas pēc virziena: horizontālās un vertikālās.",
             "Saskaiti zināmās malas katrā virzienā.",
             "Pielīdzini abas summas.",
             "Atrodi trūkstošo malu ar atņemšanu.",
             "Pārbaudi: abas summas sakrīt.",
         ],
         pieze="Apakšējā mala vienmēr ir vienāda ar visu augšējo malu summu, "
               "un kreisā - ar visu labo malu summu. Tieši tā arī izriet "
               "trūkstošais garums."),

    Paraugs("Atrodi trūkstošās malas",
            uzd="Apakšējā mala ir 6, labā 2, kreisā 5. Cik garas ir pārējās?",
            soli=[
                ("Vertikālās malas: kreisā 5, labā 2 un x",
                 "Trūkst vienas."),
                ("5 = 2 + x",
                 "Kreisā ir vienāda ar abu labo summu."),
                ("x = 5 - 2 = 3",
                 "Vidējā vertikālā mala."),
                ("Horizontālās: apakšējā 6, augšējās y un 3",
                 "Arī trūkst vienas."),
                ("y = 6 - 3 = 3",
                 "Augšējā mala."),
            ],
            atbilde="Trūkstošās malas ir 3 un 3"),

    Ievadi("Aprēķini trūkstošo malu", [
        {"jaut": "Kreisā mala 5, labā 2. Cik gara ir vidējā vertikālā mala?",
         "atb": ["3"], "padoms": "5 - 2."},
        {"jaut": "Apakšējā mala 6, augšējā daļa 3. Cik gara ir otra "
                 "horizontālā mala?",
         "atb": ["3"], "padoms": "6 - 3."},
        {"jaut": "Kreisā mala 8, labā 3. Cik gara ir trūkstošā vertikālā?",
         "atb": ["5"], "padoms": "8 - 3."},
        {"jaut": "Apakšējā mala 10, augšējās 4 un x. Cik ir x?",
         "atb": ["6"], "padoms": "10 - 4."},
        {"jaut": "Augšējās malas 3 un 4. Cik gara ir apakšējā?",
         "atb": ["7"], "padoms": "3 + 4."},
        {"jaut": "Labās malas 2 un 3. Cik gara ir kreisā?",
         "atb": ["5"], "padoms": "2 + 3."},
        {"jaut": "Apakšējā mala 12, augšējās 5 un x. Cik ir x?",
         "atb": ["7"], "padoms": "12 - 5."},
        {"jaut": "Kreisā mala 9, labās 4 un x. Cik ir x?",
         "atb": ["5"], "padoms": "9 - 4."},
    ], pamats=4,
        ievads="Sagrupē malas pēc virziena un pielīdzini summas."),

    Zimejums("Visas malas atzīmētas",
             figura([(0, 0), (6, 0), (6, 2), (3, 2), (3, 5), (0, 5)],
                    uzraksti=[(3, -0.4, "6"), (6.6, 1, "2"), (4.5, 1.7, "3"),
                              (3.6, 3.5, "3"), (1.5, 5.4, "3"),
                              (-0.6, 2.5, "5")],
                    virsraksts="Sešas malas, seši skaitļi"),
             paskaidro="Augšējā 3 plus vidējā 3 ir 6 - tikpat, cik apakšējā. "
                       "Labā 2 plus vidējā 3 ir 5 - tikpat, cik kreisā.",
             ievads="Kad visi izmēri zināmi, var rēķināt laukumu."),

    Varianti("Kā atrod trūkstošo?", [
        {"jaut": "Ar ko ir vienāda apakšējā mala?",
         "opcijas": ["Ar visu augšējo malu summu", "Ar kreiso malu",
                     "Ar labo malu", "Ar laukumu"],
         "pareizi": 0,
         "padoms": "Vienā virzienā vērstās malas."},
        {"jaut": "Kreisā mala ir 7, labās 3 un x. Cik ir x?",
         "opcijas": ["4", "10", "3", "7"],
         "pareizi": 0,
         "padoms": "7 - 3."},
        {"jaut": "Ko dara vispirms?",
         "opcijas": ["Sagrupē malas pēc virziena", "Rēķina laukumu",
                     "Mēra ar lineālu", "Zīmē diagonāli"],
         "pareizi": 0,
         "padoms": "Horizontālās atsevišķi no vertikālajām."},
        {"jaut": "Augšējās malas ir 2 un 5. Cik gara ir apakšējā?",
         "opcijas": ["7", "3", "10", "5"],
         "pareizi": 0,
         "padoms": "2 + 5."},
        {"jaut": "Kā pārbauda atrasto garumu?",
         "opcijas": ["Salīdzina abu virzienu summas",
                     "Izmēra ar lineālu",
                     "Saskaita visas malas",
                     "Pārbaudīt nevar"],
         "pareizi": 0,
         "padoms": "Summām jāsakrīt."},
        {"jaut": "Kāpēc rasējumā neatzīmē visus izmērus?",
         "opcijas": ["Pārējos var izrēķināt", "Trūkst vietas",
                     "Tos nezina", "Tā ir kļūda"],
         "pareizi": 0,
         "padoms": "Lieks skaitlis tikai traucē."},
    ], pamats=4),

    Pasaule("Cik gara ir istabas siena?",
            Ievadi("", [
                {"jaut": "Istabas garā siena ir 6 m, izcilnis 2 m. Cik metru "
                         "ir atlikusī daļa?",
                 "atb": ["4"], "padoms": "6 - 2."},
                {"jaut": "Kreisā siena 5 m, labā 2 m. Cik metru ir vidējā "
                         "siena?",
                 "atb": ["3"], "padoms": "5 - 2."},
                {"jaut": "Divas augšējās sienas ir 3 m un 4 m. Cik metru ir "
                         "apakšējā?",
                 "atb": ["7"], "padoms": "3 + 4."},
                {"jaut": "Cik metru ir visas istabas perimetrs, ja malas ir "
                         "6, 2, 3, 3, 3 un 5?",
                 "atb": ["22"], "padoms": "Saskaiti visas malas."},
            ]),
            pavediens="maja",
            konteksts="Plānā mēra tikai dažas sienas, pārējās aprēķina - "
                      "citādi mērīšana ilgtu visu dienu.",
            kapec="Pretējo malu summas vienmēr sakrīt, tāpēc rēķins ir "
                  "drošs."),

    Kopsavilkums([
        "Sagrupēju malas pēc virziena.",
        "Aprēķinu trūkstošo malu, saskaitot vai atņemot zināmās.",
        "Pārbaudu, vai abu virzienu summas sakrīt.",
        "Zinu, ka rasējumā daļa izmēru ir jāizrēķina pašam.",
    ]),

    Majas([
        "Uzzīmē kombinētu figūru un atzīmē tikai pusi izmēru.",
        "Iedod to draugam un palūdz atrast pārējos.",
        "Aprēķini savas figūras perimetru.",
    ]),
]
