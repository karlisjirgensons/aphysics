# -*- coding: utf-8 -*-
"""5. klase, 49. stunda: «Vai divas dažādi pierakstītas daļas var būt vienādas?»

Jauna temata pirmā stunda. Skaitļiem līdz šim bija viens pieraksts: 12 ir 12.
Daļām tā nav - viens un tas pats daudzums izskatās pēc diviem dažādiem
skaitļu pāriem. Tāpēc šī stunda neko nerēķina, bet tikai skatās: divas joslas
blakus un jautājums, vai iekrāsots ir vienādi daudz.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums, dala)

TEMA = "Vai divas dažādi pierakstītas daļas var būt vienādas?"

MERKIS = ("Mācīsimies ar modeli parādīt, ka dažādi pierakstītas daļas var "
          "apzīmēt vienu un to pašu daudzumu.")

SATURS = [
    Sakums("Viena pica, divi griezumi",
           zimejums=dala(8, 4, "4/8 picas"),
           paraksts="Iekrāsota tieši puse picas - lai gan pierakstā nav "
                    "neviena divnieka.",
           fakti=["Vienā picērijā picu griež 8 gabalos, otrā - 4 gabalos.",
                  "Tu apēdi 4 gabalus pirmās un 2 gabalus otrās picas.",
                  "Vai apēdi vienādi daudz?"]),

    Doma("Daļa pasaka, cik daudz, nevis kādi skaitļi",
         "Divas daļas ir vienādas tad, ja tās apzīmē vienu un to pašu "
         "daudzumu - kaut arī skaitītājs un saucējs ir citi.",
         soli=[
             "Uzzīmē abas daļas vienāda garuma joslās.",
             "Sadali katru joslu tik gabalos, cik rāda saucējs.",
             "Iekrāso tik gabalu, cik rāda skaitītājs.",
             "Salīdzini iekrāsoto garumu, nevis skaitļus.",
             "Ja iekrāsots vienādi - daļas ir vienādas.",
         ],
         pieze="Svarīgi, lai abas joslas būtu vienāda garuma: {1|2} no "
               "picas un {1|2} no kūkas nav viens daudzums, bet {1|2} un "
               "{4|8} no *vienas un tās pašas* picas ir."),

    Slidnis("Puse paliek puse",
            [{"v": "{1|2}", "teksts": "1 gabals no 2", "josla": 50,
              "zim": dala(2, 1)},
             {"v": "{2|4}", "teksts": "2 gabali no 4", "josla": 50,
              "zim": dala(4, 2)},
             {"v": "{3|6}", "teksts": "3 gabali no 6", "josla": 50,
              "zim": dala(6, 3)},
             {"v": "{4|8}", "teksts": "4 gabali no 8", "josla": 50,
              "zim": dala(8, 4)},
             {"v": "{5|10}", "teksts": "5 gabali no 10", "josla": 50,
              "zim": dala(10, 5)}],
            ievads="Spied soli pa solim: gabalu kļūst arvien vairāk, bet "
                   "iekrāsotā josla nekustas no vietas."),

    Paraugs("Vai {2|3} un {4|6} ir viens un tas pats?",
            uzd="Divas vienāda garuma joslas: pirmo sadala 3 gabalos un "
                "iekrāso 2, otro sadala 6 gabalos un iekrāso 4. Vai "
                "iekrāsots ir vienādi daudz?",
            soli=[
                ("Pirmā josla: 3 gabali, iekrāsoti 2",
                 "Katrs gabals ir trešdaļa."),
                ("Otrā josla: 6 gabali, iekrāsoti 4",
                 "Katrs gabals ir sestdaļa - divreiz mazāks."),
                ("Viena trešdaļa ir divas sestdaļas",
                 "Gabals divreiz mazāks, tāpēc to vajag divreiz vairāk."),
                ("2 trešdaļas ir 4 sestdaļas",
                 "Abās joslās iekrāsots vienāds garums."),
            ],
            atbilde="Jā, {2|3} un {4|6} ir viens un tas pats daudzums"),

    Ievadi("Cik smalkāku gabalu vajag?", [
        {"jaut": "Cik ceturtdaļu ir tikpat, cik {1|2}?",
         "atb": ["2"], "padoms": "Ceturtdaļa ir divreiz mazāka par pusi."},
        {"jaut": "Cik astotdaļu ir tikpat, cik {1|2}?",
         "atb": ["4"], "padoms": "Astoņi gabali, puse no tiem."},
        {"jaut": "Cik sestdaļu ir tikpat, cik {1|3}?",
         "atb": ["2"], "padoms": "Sestdaļa ir divreiz mazāka par trešdaļu."},
        {"jaut": "Cik devītdaļu ir tikpat, cik {1|3}?",
         "atb": ["3"], "padoms": "Trešdaļu sadala vēl trijos gabalos."},
        {"jaut": "Cik desmitdaļu ir tikpat, cik {1|5}?",
         "atb": ["2"], "padoms": "Piektdaļu sadala uz pusēm."},
        {"jaut": "Cik astotdaļu ir tikpat, cik {3|4}?",
         "atb": ["6"], "padoms": "Katra ceturtdaļa ir divas astotdaļas."},
        {"jaut": "Cik divpadsmitdaļu ir tikpat, cik {2|3}?",
         "atb": ["8"], "padoms": "Katra trešdaļa ir četras divpadsmitdaļas."},
        {"jaut": "Cik sestdaļu ir tikpat, cik {1|2}?",
         "atb": ["3"], "padoms": "Puse no sešiem gabaliem."},
    ], pamats=4,
        ievads="Jo smalkāki gabali, jo vairāk to vajag - daudzums paliek "
               "tas pats."),

    Zimejums("Četras sestdaļas",
             dala(6, 4, "4/6"),
             paskaidro="Tikpat garu joslu iekrāso arī divas trešdaļas: "
                       "sestdaļa ir tieši puse no trešdaļas, tāpēc to vajag "
                       "divreiz vairāk.",
             ievads="Tas pats daudzums, tikai sīkākos gabalos."),

    Varianti("Vienāds vai nav?", [
        {"jaut": "Vai {1|2} un {3|6} ir vienādas daļas?",
         "opcijas": ["Jā, abas ir puse", "Nē, skaitļi ir dažādi",
                     "Nē, {3|6} ir lielāka", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Trīs gabali no sešiem ir puse."},
        {"jaut": "Vai {1|3} un {1|6} ir vienādas daļas?",
         "opcijas": ["Nē, {1|6} ir divreiz mazāka", "Jā, skaitītājs ir viens",
                     "Jā, abas ir mazas", "Nē, {1|6} ir lielāka"],
         "pareizi": 0,
         "padoms": "Lielāks saucējs - sīkāki gabali."},
        {"jaut": "Ko nozīmē, ka divas daļas ir vienādas?",
         "opcijas": ["Tās apzīmē vienu un to pašu daudzumu",
                     "Tām sakrīt skaitītāji",
                     "Tām sakrīt saucēji",
                     "Tās ir pierakstītas vienādi"],
         "pareizi": 0,
         "padoms": "Skaitļi var atšķirties, daudzums - nē."},
        {"jaut": "Pica sagriezta 8 gabalos, tu apēdi 2. Cik gabalu tas būtu, "
                 "ja pica būtu sagriezta 4 gabalos?",
         "opcijas": ["1", "2", "4", "8"],
         "pareizi": 0,
         "padoms": "{2|8} ir ceturtdaļa."},
        {"jaut": "Kura daļa ir vienāda ar {2|5}?",
         "opcijas": ["{4|10}", "{2|10}", "{5|2}", "{4|5}"],
         "pareizi": 0,
         "padoms": "Gabali divreiz sīkāki, tāpēc to vajag divreiz vairāk."},
        {"jaut": "Kāpēc joslām jābūt vienāda garuma?",
         "opcijas": ["Citādi salīdzina daļas no dažādiem veselajiem",
                     "Citādi tās nesanāk skaistas",
                     "Citādi gabali ir par maziem",
                     "Garums nav svarīgs"],
         "pareizi": 0,
         "padoms": "Puse no maza kliņģera nav puse no liela."},
    ], pamats=4),

    Pasaule("Kurš gabals ir lielāks?",
            Ievadi("", [
                {"jaut": "Kūku sagrieza 12 gabalos. Cik gabalu ir {1|3} "
                         "kūkas?",
                 "atb": ["4"], "padoms": "12 : 3."},
                {"jaut": "Tā pati kūka. Cik gabalu ir {1|4} kūkas?",
                 "atb": ["3"], "padoms": "12 : 4."},
                {"jaut": "Anna apēda 6 gabalus no 12. Cik astotdaļu tas būtu, "
                         "ja kūka būtu sagriezta 8 gabalos?",
                 "atb": ["4"], "padoms": "Viņa apēda pusi."},
                {"jaut": "Divas vienādas picas: no otrās apēsti 5 gabali no "
                         "10. Cik gabalu no 6 būtu tikpat?",
                 "atb": ["3"], "padoms": "Abas reizes apēsta puse."},
            ]),
            pavediens="virtuve",
            konteksts="Virtuvē vienu un to pašu picu griež dažādi, tāpēc "
                      "gabalu skaits vien neko nepasaka.",
            kapec="Lai zinātu, kurš dabūja vairāk, jāskatās daļa, nevis "
                  "gabalu skaits."),

    Kopsavilkums([
        "Zinu, ka viens daudzums var būt pierakstīts ar dažādām daļām.",
        "Parādu ar joslu modeli, ka divas daļas ir vienādas.",
        "Skaidroju, kāpēc sīkāku gabalu vajag vairāk.",
        "Salīdzinu daļas tikai tad, ja veselais ir viens un tas pats.",
    ]),

    Majas([
        "Uzzīmē divas vienāda garuma joslas un parādi, ka {3|4} = {6|8}.",
        "Atrodi virtuvē lietu, ko var sagriezt divējādi, un uzraksti abas "
        "daļas.",
        "Padomā, cik gabalu no 100 būtu tikpat, cik {1|4}.",
    ]),
]
