# -*- coding: utf-8 -*-
"""3. klase, 45. stunda: «Vai visas izteiksmes ir atrastas?»

Turpinājums iepriekšējai stundai, bet jautājums ir cits: ne «cik atradi», bet
«kā zini, ka vairāk nav». Šis ir pirmais pamatojums pilnībai - prasme, kas
ģeometrijā un kombinatorikā vēlāk atgriezīsies katru gadu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Vai visas izteiksmes ir atrastas?"

MERKIS = ("Spriedīsim, vai izveidoti visi gadījumi, un atlasīsim tās "
          "izteiksmes, kurām var aprēķināt vērtību.")

SATURS = [
    Sakums("Kā pierādīt, ka vairāk variantu nav?",
           zimejums=restis([["1. zīme", "+", "+", "·", "·"],
                            ["2. zīme", "+", "·", "+", "·"]],
                           "visas zīmju kombinācijas"),
           paraksts="Divas vietas, katrā divas izvēles - kopā tieši četri "
                    "varianti.",
           fakti=["Pilnību pierāda ar tabulu, ne ar cerību.",
                  "Ja katrai vietai ir divas izvēles, divām vietām ir 4 "
                  "varianti."]),

    Doma("Saskaiti izvēles, nevis atradumus",
         "Ja katrā vietā ir zināms izvēļu skaits, tad visu variantu skaitu "
         "var izrēķināt iepriekš.",
         soli=[
             "Saskaiti, cik vietās jāizvēlas.",
             "Saskaiti, cik izvēļu ir katrā vietā.",
             "Reizini šos skaitļus - tas ir visu variantu skaits.",
             "Salīdzini ar to, cik variantu esi atradis.",
         ],
         pieze="Ja atradi mazāk, kāds variants vēl trūkst; ja vairāk - daži "
               "atkārtojas."),

    Paraugs("Cik variantu ir ar trim zīmēm?",
            uzd="Divās vietās jāizvēlas zīme no trim: +, − un ·. Cik variantu "
                "ir kopā?",
            soli=[
                ("Pirmā vieta: 3 izvēles",
                 "Tur var likt +, − vai ·."),
                ("Otrā vieta: 3 izvēles",
                 "Tās pašas trīs zīmes."),
                ("3 · 3 = 9",
                 "Tik variantu ir kopā."),
            ],
            atbilde="9 varianti"),

    Petijums("Pārbaudi savu sarakstu",
             vajag="iepriekšējās stundas saraksts",
             soli=[
                 "Saskaiti, cik izteiksmju tu atradi.",
                 "Izrēķini, cik to vajadzētu būt.",
                 "Ja skaitļi nesakrīt, atrodi trūkstošo vai lieko.",
                 "Pasvītro tās izteiksmes, kurām vērtību aprēķināt nevar.",
             ],
             secinajums="Saraksts ir pilns tad, kad atrasto skaits sakrīt ar "
                        "izrēķināto."),

    Ievadi("Cik variantu ir kopā?", [
        {"jaut": "Divās vietās, katrā 2 izvēles. Cik variantu?",
         "atb": ["4"], "padoms": "2 · 2."},
        {"jaut": "Divās vietās, katrā 3 izvēles. Cik variantu?",
         "atb": ["9"], "padoms": "3 · 3."},
        {"jaut": "Trīs vietās, katrā 2 izvēles. Cik variantu?",
         "atb": ["8"], "padoms": "2 · 2 · 2."},
        {"jaut": "Divās vietās: pirmajā 4, otrajā 3 izvēles. Cik variantu?",
         "atb": ["12"], "padoms": "4 · 3."},
        {"jaut": "Trīs vietās, katrā 3 izvēles. Cik variantu?",
         "atb": ["27"], "padoms": "3 · 3 · 3."},
        {"jaut": "Divās vietās, katrā 5 izvēles. Cik variantu?",
         "atb": ["25"], "padoms": "5 · 5."},
    ], pamats=4),

    Zimejums("Kad vērtību aprēķināt nevar",
             restis([["izteiksme", "vērtība"],
                     ["12 : 4 + 2", "5"],
                     ["12 : (4 − 4)", "nav"],
                     ["4 − 12", "nav 3. klasē"]],
                    "ne katrai izteiksmei ir vērtība"),
             paskaidro="Ar nulli dalīt nevar, un negatīvus skaitļus mācīsimies "
                       "vēlāk - tādas izteiksmes tagad atlasa ārā.",
             ievads="Pārbaudi katru izteiksmi, pirms to rēķini."),

    Varianti("Vai saraksts ir pilns?", [
        {"jaut": "Divās vietās var likt + vai ·. Cik variantu ir kopā?",
         "opcijas": ["4", "2", "3", "8"],
         "pareizi": 0, "padoms": "2 · 2."},
        {"jaut": "Skolēns atrada 3 variantus no 4. Ko tas nozīmē?",
         "opcijas": ["Viens variants vēl trūkst", "Saraksts ir pilns",
                     "Viens variants ir lieks", "Aprēķins bija nepareizs"],
         "pareizi": 0, "padoms": "Atrasto ir mazāk nekā izrēķināto."},
        {"jaut": "Kurai izteiksmei vērtību aprēķināt nevar?",
         "opcijas": ["8 : (5 − 5)", "8 : (5 − 4)", "8 − 5 + 5", "8 · 5 − 5"],
         "pareizi": 0, "padoms": "Saucējā sanāk nulle."},
        {"jaut": "Kā pierāda, ka visi varianti atrasti?",
         "opcijas": ["Saskaita izvēles un salīdzina", "Pameklē vēl reizi",
                     "Pajautā draugam", "To pierādīt nevar"],
         "pareizi": 0, "padoms": "Izvēļu skaitu var izrēķināt."},
    ], pamats=4),

    Pasaule("Cik dažādu lietotājvārdu var izveidot?",
            Ievadi("", [
                {"jaut": "Lietotājvārdā divas vietas, katrā viens no 4 "
                         "burtiem. Cik variantu?",
                 "atb": ["16"], "padoms": "4 · 4."},
                {"jaut": "Ja vietas ir trīs, cik variantu?",
                 "atb": ["64"], "padoms": "4 · 4 · 4."},
                {"jaut": "Pirmajā vietā 5 burti, otrajā 6 cipari. Cik "
                         "variantu?",
                 "atb": ["30"], "padoms": "5 · 6."},
                {"jaut": "Cik variantu ir, ja vietas ir divas un katrā var "
                         "likt 10 ciparus?",
                 "atb": ["100"], "padoms": "10 · 10."},
            ]),
            pavediens="dati",
            konteksts="Datorsistēma pārbauda, vai vārds jau aizņemts - tāpēc "
                      "tai jāzina, cik variantu vispār ir.",
            kapec="Katra papildu vieta variantu skaitu reizina, nevis "
                  "palielina par vienu."),

    Kopsavilkums([
        "Izrēķinu, cik variantu ir kopā, reizinot izvēļu skaitu.",
        "Salīdzinu atrasto variantu skaitu ar izrēķināto.",
        "Pamatoju, ka saraksts ir pilns.",
        "Atlasu izteiksmes, kurām vērtību aprēķināt nevar.",
    ]),

    Majas([
        "Izrēķini, cik dažādu divciparu skaitļu var izveidot no cipariem "
        "1, 2 un 3.",
        "Pieraksti tos visus un pārbaudi, vai skaits sakrīt.",
        "Atrodi izteiksmi, kurai vērtību aprēķināt nevar.",
    ]),
]
