# -*- coding: utf-8 -*-
"""5. klase, 51. stunda: «Kas notiek, ja skaitītāju un saucēju reizina?»

Mikrotemata svarīgākā stunda: līdz šim vienādas daļas atrada ar modeli, te
tās sāk iegūt ar rēķinu. Daļas pamatīpašība ir viena no tām kārtulām, ko
viegli iemācīties nepareizi - tāpēc te blakus stāv arī abas biežākās kļūdas:
reizināt tikai vienu locekli un reizināt ar nulli.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums, dala)

TEMA = "Kas notiek, ja skaitītāju un saucēju reizina?"

MERKIS = ("Iemācīsimies daļas pamatīpašību: reizinot skaitītāju un saucēju "
          "ar vienu un to pašu skaitli, daļas vērtība nemainās.")

SATURS = [
    Sakums("Katru gabalu pārgriež uz pusēm",
           zimejums=dala(3, 1, "1/3"),
           paraksts="Ja katru trešdaļu pārgriež uz pusēm, iznāk {2|6} - tikpat "
                    "daudz.",
           fakti=["Gabalu skaits kļūst divreiz lielāks.",
                  "Arī paņemto gabalu skaits kļūst divreiz lielāks.",
                  "Pats daudzums nemainās ne par drusku."]),

    Doma("Daļas pamatīpašība",
         "Ja daļas skaitītāju un saucēju reizina ar vienu un to pašu skaitli "
         "(tikai ne ar nulli), daļas vērtība nemainās.",
         soli=[
             "Izvēlies skaitli, ar kuru reizināt.",
             "Reizini ar to skaitītāju.",
             "Reizini ar to pašu skaitli arī saucēju.",
             "Pieraksti jauno daļu un liec vienādības zīmi.",
             "Pārbaudi ar modeli: gabali kļuva sīkāki, bet daudzums tas pats.",
         ],
         pieze="Saucējs pasaka, cik sīki sagriež, skaitītājs - cik gabalu "
               "paņem. Ja sagriež divreiz sīkāk, tad arī paņem divreiz "
               "vairāk gabalu, un rokā paliek tikpat."),

    Paraugs("Pieraksti {2|3} ar saucēju 12",
            uzd="Uzraksti daļu {2|3} tā, lai saucējs būtu 12.",
            soli=[
                ("12 : 3 = 4",
                 "Ar cik jāreizina saucējs, lai iznāktu 12."),
                ("{2 · 4|3 · 4}",
                 "Ar to pašu skaitli reizina abus locekļus."),
                ("{2 · 4|3 · 4} = {8|12}",
                 "Skaitītājs 8, saucējs 12."),
                ("{2|3} = {8|12}",
                 "Daudzums nemainījās, mainījās tikai pieraksts."),
            ],
            atbilde="{2|3} = {8|12}"),

    Slidnis("Viens un tas pats daudzums",
            [{"v": "{1|3}", "teksts": "sākuma daļa", "josla": 33,
              "zim": dala(3, 1)},
             {"v": "{2|6}", "teksts": "abus reizina ar 2", "josla": 33,
              "zim": dala(6, 2)},
             {"v": "{3|9}", "teksts": "abus reizina ar 3", "josla": 33,
              "zim": dala(9, 3)},
             {"v": "{4|12}", "teksts": "abus reizina ar 4", "josla": 33,
              "zim": dala(12, 4)}],
            ievads="Spied soli pa solim: skaitļi aug, josla stāv uz vietas."),

    Ievadi("Reizini abus locekļus", [
        {"jaut": "{1|2} = {?|6}. Ar cik reizināja abus locekļus?",
         "atb": ["3"], "padoms": "6 : 2."},
        {"jaut": "{1|2} pieraksti ar saucēju 6. Kāds ir skaitītājs?",
         "atb": ["3"], "padoms": "1 · 3."},
        {"jaut": "{3|5} pieraksti ar saucēju 20. Kāds ir skaitītājs?",
         "atb": ["12"], "padoms": "20 : 5 = 4; 3 · 4."},
        {"jaut": "{2|7} pieraksti ar saucēju 21. Kāds ir skaitītājs?",
         "atb": ["6"], "padoms": "21 : 7 = 3; 2 · 3."},
        {"jaut": "{4|9} pieraksti ar saucēju 27. Kāds ir skaitītājs?",
         "atb": ["12"], "padoms": "27 : 9 = 3; 4 · 3."},
        {"jaut": "{5|6} pieraksti ar saucēju 24. Kāds ir skaitītājs?",
         "atb": ["20"], "padoms": "24 : 6 = 4; 5 · 4."},
        {"jaut": "{3|4} pieraksti ar skaitītāju 15. Kāds ir saucējs?",
         "atb": ["20"], "padoms": "15 : 3 = 5; 4 · 5."},
        {"jaut": "{2|5} pieraksti ar skaitītāju 14. Kāds ir saucējs?",
         "atb": ["35"], "padoms": "14 : 2 = 7; 5 · 7."},
    ], pamats=4,
        ievads="Vispirms noskaidro, ar cik reizināja, tad reizini otru "
               "locekli ar to pašu skaitli."),

    Zimejums("Deviņas devītdaļas, paņemtas trīs",
             dala(9, 3, "3/9"),
             paskaidro="Tā ir tā pati trešdaļa: katrs no trim gabaliem "
                       "sagriezts trijos, tāpēc gan skaitītājs, gan saucējs "
                       "kļuva trīs reizes lielāks.",
             ievads="Modelis pierāda to, ko pasaka pamatīpašība."),

    Varianti("Kur kārtula darbojas un kur nē?", [
        {"jaut": "Skaitītāju un saucēju reizina ar 5. Kas notiek ar daļas "
                 "vērtību?",
         "opcijas": ["Nemainās", "Kļūst 5 reizes lielāka",
                     "Kļūst 5 reizes mazāka", "Kļūst par 5 lielāka"],
         "pareizi": 0,
         "padoms": "Sīkāki gabali, bet tikpat daudz."},
        {"jaut": "Skolēns {2|3} pārraksta kā {6|3}. Kas nav labi?",
         "opcijas": ["Saucējs nav reizināts", "Skaitītājs nav reizināts",
                     "Reizināts ar nepareizu skaitli", "Viss ir labi"],
         "pareizi": 0,
         "padoms": "Reizināt jāsāk un jābeidz abiem locekļiem."},
        {"jaut": "Kāpēc abus locekļus nedrīkst reizināt ar nulli?",
         "opcijas": ["Saucējs kļūtu 0, bet ar nulli dalīt nedrīkst",
                     "Skaitītājs kļūtu par liels",
                     "Nulle nav naturāls skaitlis",
                     "Drīkst gan"],
         "pareizi": 0,
         "padoms": "Daļa ir dalījums, un saucējs nedrīkst būt nulle."},
        {"jaut": "Kura daļa ir vienāda ar {3|7}?",
         "opcijas": ["{9|21}", "{9|7}", "{3|21}", "{6|7}"],
         "pareizi": 0,
         "padoms": "Abi locekļi reizināti ar 3."},
        {"jaut": "{4|5} un {8|10} - ko var teikt?",
         "opcijas": ["Tās ir vienādas", "{8|10} ir divreiz lielāka",
                     "{4|5} ir lielāka", "Tās nav salīdzināmas"],
         "pareizi": 0,
         "padoms": "Abi locekļi reizināti ar 2."},
        {"jaut": "Ar kuru skaitli reizināti abi {2|9} locekļi, ja iznāca "
                 "{10|45}?",
         "opcijas": ["5", "2", "4", "9"],
         "pareizi": 0,
         "padoms": "45 : 9."},
    ], pamats=4),

    Pasaule("Recepte lielākai pannai",
            Ievadi("", [
                {"jaut": "Receptē ir {1|4} glāzes cukura. Cik tas ir "
                         "astotdaļu?",
                 "atb": ["2"], "padoms": "Abus locekļus reizina ar 2."},
                {"jaut": "Receptē ir {2|3} glāzes miltu. Cik tas ir "
                         "devītdaļu?",
                 "atb": ["6"], "padoms": "Abus locekļus reizina ar 3."},
                {"jaut": "Receptē ir {3|5} glāzes ūdens. Cik tas ir "
                         "desmitdaļu?",
                 "atb": ["6"], "padoms": "Abus locekļus reizina ar 2."},
                {"jaut": "Receptē ir {1|2} glāzes eļļas, bet mērglāzei ir "
                         "12 iedaļas. Cik iedaļas ieliet?",
                 "atb": ["6"], "padoms": "12 : 2 = 6; 1 · 6."},
            ]),
            pavediens="virtuve",
            konteksts="Katram mērtraukam ir savas iedaļas, tāpēc recepte "
                      "jāpārraksta ar to saucēju, kāds ir uz trauka.",
            kapec="Pamatīpašība ļauj to izdarīt, neko nepārmērot."),

    Kopsavilkums([
        "Formulēju daļas pamatīpašību saviem vārdiem.",
        "Pamatoju to ar joslas modeli.",
        "Pierakstu doto daļu ar citu, lielāku saucēju.",
        "Zinu, ka reizināt drīkst ar jebkuru skaitli, tikai ne ar nulli.",
    ]),

    Majas([
        "Uzraksti {3|4} ar saucējiem 8, 12 un 20.",
        "Uzzīmē modeli, kas parāda, ka {2|5} = {6|15}.",
        "Padomā, vai pamatīpašība der arī tad, ja abus locekļus dala.",
    ]),
]
