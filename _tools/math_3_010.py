# -*- coding: utf-8 -*-
"""3. klase, 10. stunda: «Kāds triks palīdz reizināt ar 9?»

Deviņnieku rinda ir tā, kurā likumsakarība redzama ar aci: desmiti aug par
vienu, vieni krīt par vienu, un ciparu summa vienmēr ir 9. Stunda to vispirms
liek *pamanīt* tabulā un tikai tad pamato ar modeli 9 · a = 10 · a − a.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kāds triks palīdz reizināt ar 9?"

MERKIS = ("Atklāsim likumsakarību deviņnieku rindā un pārbaudīsim to ar "
          "modeli 9 · a = 10 · a − a.")

SATURS = [
    Sakums("Kāpēc deviņnieku rindā cipari ir kā kāpnes?",
           zimejums=restis([[9, 18, 27, 36, 45],
                            [54, 63, 72, 81, 90]],
                           "deviņnieku rinda"),
           paraksts="Pirmais cipars aug: 0, 1, 2, 3... Otrais krīt: 9, 8, "
                    "7, 6...",
           fakti=["Katrā deviņnieku rindas skaitlī abu ciparu summa ir 9.",
                  "9 · 7 = 63, un 6 + 3 = 9."]),

    Doma("Deviņas grupas ir desmit grupas bez vienas",
         "9 · a = 10 · a − a - tāpēc deviņnieku rindu var iegūt no "
         "desmitnieku rindas ar vienu atņemšanu.",
         soli=[
             "Izrēķini 10 · a - pieraksti skaitlim nulli galā.",
             "Atņem vienu grupu, tas ir, pašu skaitli a.",
             "Sanākusī atbilde ir 9 · a.",
             "Pārbaudi: abu ciparu summai jābūt 9.",
         ],
         pieze="Tāpēc kāpnes arī rodas: katru reizi pieliek vēl desmit un "
               "noņem vienu - desmiti aug par 1, vieni krīt par 1."),

    Paraugs("Cik ir 9 · 7?",
            uzd="Izrēķini 9 · 7, izmantojot desmitnieku rindu.",
            soli=[
                ("10 · 7 = 70",
                 "Desmit septiņnieku grupas."),
                ("70 − 7 = 63",
                 "Vienu grupu noņem - paliek deviņas."),
                ("6 + 3 = 9",
                 "Pārbaude ar ciparu summu: tā ir 9, tātad viss pareizi."),
            ],
            atbilde="63"),

    Ievadi("Deviņnieku rinda", [
        {"jaut": "9 · 4 = ?", "atb": ["36"], "padoms": "40 − 4."},
        {"jaut": "9 · 6 = ?", "atb": ["54"], "padoms": "60 − 6."},
        {"jaut": "9 · 8 = ?", "atb": ["72"], "padoms": "80 − 8."},
        {"jaut": "9 · 9 = ?", "atb": ["81"], "padoms": "90 − 9."},
        {"jaut": "9 · 3 = ?", "atb": ["27"], "padoms": "30 − 3."},
        {"jaut": "9 · 10 = ?", "atb": ["90"], "padoms": "100 − 10."},
    ], pamats=4),

    Petijums("Pārbaudi triku ar pirkstiem",
             vajag="abas rokas",
             soli=[
                 "Izpleti abas rokas priekšā - tie ir desmit pirksti.",
                 "Lai izrēķinātu 9 · 4, saloc ceturto pirkstu no kreisās.",
                 "Pirksti pa kreisi no salocītā ir desmiti: te 3.",
                 "Pirksti pa labi ir vieni: te 6. Sanāk 36.",
                 "Pārbaudi tāpat 9 · 7 un 9 · 8.",
             ],
             secinajums="Triks strādā tāpēc, ka pirkstu kopā ir 10, un viens "
                        "no tiem tiek noņemts - gluži kā 10 · a − a."),

    Zimejums("Kā aug desmiti un krīt vieni",
             restis([["9 · 1", "9 · 2", "9 · 3", "9 · 4", "9 · 5"],
                     ["0 un 9", "1 un 8", "2 un 7", "3 un 6", "4 un 5"]],
                    "desmiti aug, vieni krīt"),
             paskaidro="Abu ciparu summa katru reizi ir 9 - tāpēc atbildi "
                       "var pārbaudīt pat neskaitot.",
             ievads="Salīdzini augšējo un apakšējo rindu."),

    Varianti("Vai atbilde iztur pārbaudi?", [
        {"jaut": "Kurš skaitlis *nevar* būt deviņnieku rindā?",
         "opcijas": ["64", "63", "72", "81"],
         "pareizi": 0, "padoms": "6 + 4 = 10, nevis 9."},
        {"jaut": "Kā no 10 · 8 iegūt 9 · 8?",
         "opcijas": ["Atņem 8", "Atņem 10", "Atņem 1", "Dala ar 2"],
         "pareizi": 0, "padoms": "Noņem vienu astotnieku grupu."},
        {"jaut": "Cik ir 9 · 5?",
         "opcijas": ["45", "54", "40", "50"],
         "pareizi": 0, "padoms": "50 − 5."},
        {"jaut": "Cik deviņnieku grupu ir 54?",
         "opcijas": ["6", "5", "7", "9"],
         "pareizi": 0, "padoms": "54 : 9."},
    ], pamats=4),

    Pasaule("Cik daļu ir raķetes blokos?",
            Ievadi("", [
                {"jaut": "Raķetes pakāpē ir 9 dzinēji. Cik dzinēju ir 3 "
                         "pakāpēs?",
                 "atb": ["27"], "padoms": "30 − 3."},
                {"jaut": "Cik dzinēju ir 7 pakāpēs?",
                 "atb": ["63"], "padoms": "70 − 7."},
                {"jaut": "Rūpnīca saskaitīja 81 dzinēju. Cik pakāpju tas ir?",
                 "atb": ["9"], "padoms": "81 : 9."},
                {"jaut": "Vienā pārbaudē iedarbina 9 dzinējus, un pārbaužu "
                         "ir 8. Cik iedarbināšanu kopā?",
                 "atb": ["72"], "padoms": "80 − 8."},
            ]),
            pavediens="tehnika",
            konteksts="Lielām raķetēm pirmajā pakāpē mēdz būt deviņi vienādi "
                      "dzinēji, kas strādā reizē.",
            kapec="Kad detaļas ir vienādas, to skaitu pārbauda ar "
                  "reizināšanu, nevis skaitot pa vienai."),

    Kopsavilkums([
        "Zinu visu deviņnieku rindu no 9 līdz 90.",
        "Lietoju paņēmienu 9 · a = 10 · a − a.",
        "Pārbaudu atbildi ar ciparu summu, kurai jābūt 9.",
        "Paskaidroju, kāpēc pirkstu triks strādā.",
    ]),

    Majas([
        "Izrēķini ar pirkstiem 9 · 3, 9 · 6 un 9 · 9 un pārbaudi ar tabulu.",
        "Uzraksti deviņnieku rindu un pasvītro abu ciparu summu.",
        "Pastāsti mājiniekiem, kāpēc 9 · 8 var iegūt no 80.",
    ]),
]
