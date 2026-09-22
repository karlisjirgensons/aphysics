# -*- coding: utf-8 -*-
"""5. klase, 50. stunda: «Kā to pierakstīt kā vienādību?»

Iepriekšējā stunda redzēja, ka divas daļas ir vienādas; šī to pieraksta.
Vienādības zīme starp divām daļām skolēnam nav pašsaprotama - līdz šim tā
stāvēja starp rēķinu un rezultātu, tagad starp diviem pierakstiem, no kuriem
neviens nav «atbilde». Tieši to šī stunda arī māca izlasīt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala)

TEMA = "Kā to pierakstīt kā vienādību?"

MERKIS = ("Mācīsimies secinājumu par divām vienādām daļām pierakstīt kā "
          "vienādību un to izlasīt.")

SATURS = [
    Sakums("Zīmējums pasaka, pieraksts pierāda",
           zimejums=dala(4, 2, "2/4"),
           paraksts="Redzētais vienā rindā: {1|2} = {2|4}.",
           fakti=["Zīmējumu grāmatā neieliks - vienādību ieliks.",
                  "Vienādības zīme te nesaka «atbilde ir», bet «tikpat».",
                  "Abās pusēs stāv viens daudzums, divos pierakstos."]),

    Doma("Vienādības zīme starp daļām nozīmē «tikpat daudz»",
         "Ja abas daļas apzīmē vienu un to pašu daudzumu, starp tām raksta "
         "vienādības zīmi.",
         soli=[
             "Pārliecinies ar modeli, ka daudzums ir viens un tas pats.",
             "Uzraksti vienu daļu pa kreisi, otru pa labi.",
             "Starp tām liec vienādības zīmi.",
             "Izlasi to skaļi: «puse ir tikpat, cik divas ceturtdaļas».",
             "Pārbaudi, vai abas daļas ir no viena un tā paša veselā.",
         ],
         pieze="Vienādību var lasīt uz abām pusēm: {1|2} = {2|4} un "
               "{2|4} = {1|2} ir viens un tas pats teikums. Tāpēc nav "
               "«pareizās» un «nepareizās» puses - abas ir vienlīdz labas."),

    Paraugs("No zīmējuma uz vienādību",
            uzd="Josla sadalīta 6 vienādos gabalos, iekrāsoti 3. Otra tikpat "
                "gara josla sadalīta 2 gabalos, iekrāsots 1. Pieraksti "
                "secinājumu kā vienādību.",
            soli=[
                ("Pirmā josla: {3|6}",
                 "Saucējs 6, skaitītājs 3."),
                ("Otrā josla: {1|2}",
                 "Saucējs 2, skaitītājs 1."),
                ("Iekrāsots vienāds garums",
                 "Abās joslās iekrāsota tieši puse."),
                ("{3|6} = {1|2}",
                 "Vienādības zīme starp abiem pierakstiem."),
            ],
            atbilde="{3|6} = {1|2}"),

    Ievadi("Aizpildi vienādību", [
        {"jaut": "{1|2} = {?|6}. Kāds skaitlis ir skaitītājā?",
         "atb": ["3"], "padoms": "Puse no sešiem gabaliem."},
        {"jaut": "{1|3} = {?|9}. Kāds skaitlis ir skaitītājā?",
         "atb": ["3"], "padoms": "Trešdaļa no deviņiem gabaliem."},
        {"jaut": "{2|5} = {4|?}. Kāds skaitlis ir saucējā?",
         "atb": ["10"], "padoms": "Gabalu divreiz vairāk, tie divreiz "
                                  "sīkāki."},
        {"jaut": "{3|4} = {?|8}. Kāds skaitlis ir skaitītājā?",
         "atb": ["6"], "padoms": "Katra ceturtdaļa ir divas astotdaļas."},
        {"jaut": "{1|4} = {3|?}. Kāds skaitlis ir saucējā?",
         "atb": ["12"], "padoms": "Skaitītājs pieauga trīs reizes."},
        {"jaut": "{2|3} = {?|12}. Kāds skaitlis ir skaitītājā?",
         "atb": ["8"], "padoms": "Katra trešdaļa ir četras divpadsmitdaļas."},
        {"jaut": "{5|10} = {1|?}. Kāds skaitlis ir saucējā?",
         "atb": ["2"], "padoms": "Piecas desmitdaļas ir puse."},
        {"jaut": "{3|5} = {6|?}. Kāds skaitlis ir saucējā?",
         "atb": ["10"], "padoms": "Skaitītājs pieauga divas reizes."},
    ], pamats=4,
        ievads="Abās vienādības pusēs jābūt vienam daudzumam - meklē "
               "trūkstošo skaitli."),

    Zimejums("Trīs sestdaļas",
             dala(6, 3, "3/6"),
             paskaidro="To pašu joslu iekrāso arī viena puse, tāpēc "
                       "pieraksts {3|6} = {1|2} ir patiess.",
             ievads="Zīmējums - tikai pierādījums; grāmatā paliek vienādība."),

    Varianti("Vai vienādība ir patiesa?", [
        {"jaut": "Vai {2|6} = {1|3} ir patiesa vienādība?",
         "opcijas": ["Jā", "Nē, {2|6} ir lielāka", "Nē, {1|3} ir lielāka",
                     "To nevar pateikt"],
         "pareizi": 0,
         "padoms": "Divas sestdaļas ir tieši viena trešdaļa."},
        {"jaut": "Vai {3|4} = {3|8} ir patiesa vienādība?",
         "opcijas": ["Nē, {3|8} ir mazāka", "Jā, skaitītāji sakrīt",
                     "Jā, abas ir mazākas par vienu", "Nē, {3|8} ir lielāka"],
         "pareizi": 0,
         "padoms": "Vienāds skaitītājs, sīkāki gabali - mazāks daudzums."},
        {"jaut": "Ko nozīmē vienādības zīme pierakstā {1|2} = {4|8}?",
         "opcijas": ["Abās pusēs ir viens daudzums",
                     "Pa labi ir atbilde",
                     "Pa kreisi ir vienkāršāks skaitlis",
                     "Daļas jāsaskaita"],
         "pareizi": 0,
         "padoms": "Tā nav darbība, bet apgalvojums."},
        {"jaut": "Kurš pieraksts ir vienādība?",
         "opcijas": ["{2|4} = {1|2}", "{2|4} + {1|2}", "{2|4} < {1|2}",
                     "{2|4} un {1|2}"],
         "pareizi": 0,
         "padoms": "Vienādībā ir zīme «=»."},
        {"jaut": "Vienādību {1|2} = {3|6} pārraksta otrādi. Vai tā paliek "
                 "patiesa?",
         "opcijas": ["Jā, puses var mainīt vietām", "Nē, secība ir svarīga",
                     "Tikai ar veseliem skaitļiem", "Nē, zīme mainās"],
         "pareizi": 0,
         "padoms": "«Tikpat» darbojas uz abām pusēm."},
        {"jaut": "Kura vienādība *nav* patiesa?",
         "opcijas": ["{1|3} = {2|9}", "{1|3} = {2|6}", "{1|3} = {3|9}",
                     "{1|3} = {4|12}"],
         "pareizi": 0,
         "padoms": "Trešdaļa ir trīs devītdaļas, nevis divas."},
    ], pamats=4),

    Pasaule("Recepte diviem pierakstiem",
            Ievadi("", [
                {"jaut": "Receptē vajag {1|2} glāzes piena. Mērglāze "
                         "sadalīta 4 daļās. Cik daļas jāielej?",
                 "atb": ["2"], "padoms": "{1|2} = {2|4}."},
                {"jaut": "Tā pati recepte, bet mērglāze sadalīta 8 daļās. "
                         "Cik daļas jāielej?",
                 "atb": ["4"], "padoms": "{1|2} = {4|8}."},
                {"jaut": "Receptē vajag {3|4} glāzes miltu, mērglāze "
                         "sadalīta 8 daļās. Cik daļas jāieber?",
                 "atb": ["6"], "padoms": "{3|4} = {6|8}."},
                {"jaut": "Receptē vajag {2|3} glāzes ūdens, mērglāze "
                         "sadalīta 9 daļās. Cik daļas jāielej?",
                 "atb": ["6"], "padoms": "{2|3} = {6|9}."},
            ]),
            pavediens="virtuve",
            konteksts="Receptē raksta vienu daļu, bet uz mērglāzes ir "
                      "pavisam citas iedaļas.",
            kapec="Vienādība pasaka, cik iedaļu ielej - bez tās jāmin."),

    Kopsavilkums([
        "Pierakstu secinājumu par divām vienādām daļām kā vienādību.",
        "Izlasu vienādību starp daļām kā «tikpat daudz».",
        "Atrodu vienādībā trūkstošo skaitītāju vai saucēju.",
        "Zinu, ka vienādības puses drīkst samainīt vietām.",
    ]),

    Majas([
        "Uzzīmē joslu modeli un pieraksti trīs patiesas vienādības.",
        "Uzraksti vienu nepatiesu vienādību un paskaidro, kur tā kļūdās.",
        "Atrodi mājās mērtrauku un pieraksti, cik tā iedaļu ir {1|2}.",
    ]),
]
