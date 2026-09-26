# -*- coding: utf-8 -*-
"""3. klase, 2. stunda: «Kāpēc pietiek iemācīties pusi tabulas?»

Reizināšanas maiņas īpašība te nav teorija, bet darba taupīšana: ja 6 · 7 un
7 · 6 ir viens un tas pats, tad no 100 reizinājumiem jāiegaumē tikai puse.
Modelis ir taisnstūris, ko pagriež - tas pats rūtiņu skaits, cits izskats.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kāpēc pietiek iemācīties pusi tabulas?"

MERKIS = ("Iemācīsimies izmantot īpašību a · b = b · a, lai iegaumējamo "
          "reizinājumu skaits kļūtu divreiz mazāks.")

SATURS = [
    Sakums("Vai 3 rindas pa 6 ir tas pats, kas 6 rindas pa 3?",
           zimejums=restis([["", "", "", "", "", ""],
                            ["", "", "", "", "", ""],
                            ["", "", "", "", "", ""]],
                           "3 rindas pa 6 rūtiņām"),
           paraksts="Pagriez šo taisnstūri sānis - rūtiņu skaits nemainās.",
           fakti=["Tabulā ir 100 reizinājumu, bet dažādu atbilžu daudz mazāk.",
                  "Pagriežot taisnstūri, rūtiņu skaits paliek tas pats."]),

    Doma("Reizinātājus drīkst samainīt vietām",
         "a · b = b · a - tāpēc katrs reizinājums tabulā ir divreiz, un "
         "iemācīties vajag tikai vienu no tiem.",
         soli=[
             "Uzzīmē taisnstūri: rindu skaits reizināts ar rūtiņām rindā.",
             "Pagriez lapu par ceturtdaļu apgriezienu.",
             "Tagad rindu ir tikpat, cik agrāk bija rūtiņu rindā.",
             "Rūtiņas neviena nepazuda, tātad reizinājums ir tas pats.",
         ],
         pieze="Tas neder dalīšanai: 12 : 4 un 4 : 12 nav viens un tas pats. "
               "Vietām drīkst mainīt tikai *reizinātājus*."),

    Paraugs("Kāpēc 7 · 4 nav jāmācās atsevišķi?",
            uzd="Tu jau proti 4 · 7 = 28. Cik ir 7 · 4?",
            soli=[
                ("4 · 7 = 28",
                 "Šo reizinājumu proti no četrinieku rindas."),
                ("7 · 4 = 4 · 7",
                 "Reizinātājus drīkst samainīt vietām."),
                ("7 · 4 = 28",
                 "Atbilde ir tā pati - jaunu neko mācīties nevajag."),
            ],
            atbilde="28"),

    Ievadi("Izmanto to, ko jau zini", [
        {"jaut": "5 · 8 = 40. Cik ir 8 · 5?", "atb": ["40"],
         "padoms": "Reizinātājus samaini vietām."},
        {"jaut": "3 · 9 = 27. Cik ir 9 · 3?", "atb": ["27"],
         "padoms": "Tas pats reizinājums no otras puses."},
        {"jaut": "2 · 7 = 14. Cik ir 7 · 2?", "atb": ["14"],
         "padoms": "Septiņi pāri jeb divas septiņnieku grupas."},
        {"jaut": "4 · 6 = 24. Cik ir 6 · 4?", "atb": ["24"],
         "padoms": "Pagriez taisnstūri."},
        {"jaut": "5 · 9 = 45. Cik ir 9 · 5?", "atb": ["45"],
         "padoms": "Deviņas piecnieku grupas."},
        {"jaut": "3 · 7 = 21. Cik ir 7 · 3?", "atb": ["21"],
         "padoms": "Atbilde nemainās."},
    ], pamats=4,
        ievads="Katrā rindā viens reizinājums jau ir izrēķināts. Otru "
               "izrēķināt nevajag - to var *nolasīt*."),

    Zimejums("Tas pats taisnstūris, pagriezts",
             restis([["", "", ""], ["", "", ""], ["", "", ""],
                     ["", "", ""], ["", "", ""], ["", "", ""]],
                    "6 rindas pa 3 rūtiņām"),
             paskaidro="Te ir 6 · 3 = 18 rūtiņas - tikpat, cik iepriekšējā "
                       "zīmējumā bija 3 · 6.",
             ievads="Salīdzini ar stundas sākuma zīmējumu: forma cita, "
                    "skaits tas pats."),

    Varianti("Kur maiņa der un kur ne?", [
        {"jaut": "Vai 8 · 6 = 6 · 8?",
         "opcijas": ["Jā, reizinātājus drīkst mainīt vietām",
                     "Nē, pirmais skaitlis ir svarīgāks",
                     "Tikai tad, ja abi ir pāra skaitļi",
                     "Nē, jo atbildes ir dažādas"],
         "pareizi": 0,
         "padoms": "Taisnstūri var pagriezt."},
        {"jaut": "Vai 12 : 3 = 3 : 12?",
         "opcijas": ["Nē, dalīšanā vietas nedrīkst mainīt",
                     "Jā, tāpat kā reizināšanā",
                     "Jā, abas reizes iznāk 4",
                     "Tikai tad, ja skaitļi ir lieli"],
         "pareizi": 0,
         "padoms": "12 : 3 = 4, bet 3 : 12 nav vesels skaitlis."},
        {"jaut": "Cik bieži katrs reizinājums ar dažādiem skaitļiem ir "
                 "tabulā?",
         "opcijas": ["Divas reizes", "Vienu reizi", "Trīs reizes",
                     "Desmit reizes"],
         "pareizi": 0,
         "padoms": "Katram a · b tabulā ir arī b · a."},
        {"jaut": "Kurš reizinājums ir tabulā tikai *vienu* reizi?",
         "opcijas": ["7 · 7", "7 · 8", "6 · 9", "4 · 5"],
         "pareizi": 0,
         "padoms": "Ja abi reizinātāji ir vienādi, samainīt nav ko."},
    ], pamats=4),

    Pasaule("Cik šūnu ir bišu kāres gabalā?",
            Ievadi("", [
                {"jaut": "Kārē ir 4 rindas pa 7 šūnām. Cik šūnu ir kopā?",
                 "atb": ["28"], "padoms": "4 · 7."},
                {"jaut": "Bitenieks to pašu gabalu skatās no sāna: 7 rindas "
                         "pa 4 šūnām. Cik šūnu tagad?",
                 "atb": ["28"],
                 "padoms": "Tas pats gabals - tas pats skaits."},
                {"jaut": "Otrā kārē ir 5 rindas pa 6 šūnām. Cik šūnu ir?",
                 "atb": ["30"], "padoms": "5 · 6."},
                {"jaut": "Cik šūnu ir abos gabalos kopā?",
                 "atb": ["58"], "padoms": "28 + 30."},
            ]),
            pavediens="daba",
            konteksts="Bišu kāre ir gluži kā rūtiņu lapa: vienādas šūnas "
                      "stāv taisnās rindās.",
            kapec="No kuras puses skatās, tas neko nemaina - šūnu skaits "
                  "paliek viens."),

    Kopsavilkums([
        "Zinu un lietoju īpašību a · b = b · a.",
        "Pamatoju to ar taisnstūri, kuru pagriež.",
        "No viena zināma reizinājuma nolasu arī otru.",
        "Zinu, ka dalīšanā vietas mainīt nedrīkst.",
    ]),

    Majas([
        "Saliec 12 pogas taisnstūrī divos dažādos veidos un pieraksti abus "
        "reizinājumus.",
        "Atrodi mājās kaut ko, kas salikts rindās, un pieraksti to divējādi.",
        "Pastāsti kādam mājiniekam, kāpēc pietiek iemācīties pusi tabulas.",
    ]),
]
