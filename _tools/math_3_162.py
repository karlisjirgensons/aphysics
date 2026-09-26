# -*- coding: utf-8 -*-
"""3. klase, 162. stunda: «Vai no šī izklājuma sanāks kubs?»

Ne katrs sešu kvadrātu salikums ir kuba izklājums. Atbildi var uzminēt, bet
droši pateikt - tikai salokot. Tāpēc stunda ir praktiska: hipotēze vispirms,
pārbaude pēc tam.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         izklajums, restis)

TEMA = "Vai no šī izklājuma sanāks kubs?"

MERKIS = ("Atlasīsim izklājumus, no kuriem var salocīt kubu vai piramīdu, un "
          "pārbaudīsim praktiski.")

SATURS = [
    Sakums("Vai no jebkuriem sešiem kvadrātiem sanāk kubs?",
           zimejums=izklajums(2, 2, 2),
           paraksts="Šis izklājums der - bet ne visi seši kvadrāti der.",
           fakti=["Kuba izklājumā vienmēr ir 6 kvadrāti.",
                  "Bet ne katrs sešu kvadrātu salikums ir izklājums."]),

    Doma("Vispirms pieņēmums, tad pārbaude",
         "Paskaties, vai skaldnes nepārklājas, un tikai tad saloc - tā "
         "iemācīsies paredzēt rezultātu.",
         soli=[
             "Saskaiti kvadrātus - to jābūt sešiem.",
             "Iedomājies, kura kļūs par apakšu.",
             "Pārbaudi, vai pārējās apliecas ap to, nepārklājoties.",
             "Saloc modeli un pārbaudi pieņēmumu.",
         ],
         pieze="Ja divas skaldnes salokot uzkrīt viena uz otras, izklājums "
               "neder - kaut kvadrātu skaits ir pareizs."),

    Petijums("Pārbaudi trīs salikumus",
             vajag="rūtiņu papīrs, šķēres un līmlente",
             soli=[
                 "Izgriez trīs dažādus sešu kvadrātu salikumus.",
                 "Pirms locīšanas pieraksti savu pieņēmumu par katru.",
                 "Saloc visus trīs.",
                 "Salīdzini rezultātu ar saviem pieņēmumiem.",
             ],
             secinajums="Kuba izklājumu ir vienpadsmit dažādu - bet sešu "
                        "kvadrātu salikumu ir daudz vairāk."),

    Paraugs("Vai šis izklājums der?",
            uzd="Salikumā ir 6 kvadrāti, bet divi no tiem ir blakus vienā "
                "rindā ar vēl četriem. Vai no tā sanāks kubs?",
            soli=[
                ("Kvadrātu ir seši",
                 "Skaits ir pareizs."),
                ("Sešas rindā salokot, divas uzkrīt viena uz otras",
                 "Rinda apliecas ap sevi."),
                ("Izklājums neder",
                 "Skaits vien nepietiek."),
            ],
            atbilde="neder"),

    Ievadi("Izklājumu skaitļi", [
        {"jaut": "Cik kvadrātu ir kuba izklājumā?", "atb": ["6"],
         "padoms": "Tik, cik skaldņu."},
        {"jaut": "Cik trīsstūru ir četrstūra piramīdas izklājumā?",
         "atb": ["4"], "padoms": "Četras sānu skaldnes."},
        {"jaut": "Cik figūru kopā ir piramīdas izklājumā?", "atb": ["5"],
         "padoms": "Pamats un četri trīsstūri."},
        {"jaut": "Kuba mala 4 cm. Cik kvadrātcentimetru ir viena skaldne?",
         "atb": ["16"], "padoms": "4 · 4."},
        {"jaut": "Cik kvadrātcentimetru ir viss izklājums?", "atb": ["96"],
         "padoms": "6 · 16."},
        {"jaut": "Kuba mala 5 cm. Cik kvadrātcentimetru ir izklājums?",
         "atb": ["150"], "padoms": "6 · 25."},
    ], pamats=4),

    Zimejums("Piramīdas izklājums skaitļos",
             restis([["daļa", "skaits", "forma"],
                     ["pamats", 1, "kvadrāts"],
                     ["sāni", 4, "trīsstūri"]],
                    "četrstūra piramīda"),
             paskaidro="Piramīdas izklājumā ir piecas figūras - viena "
                       "mazāk nekā kubam.",
             ievads="Otrs izklājuma veids."),

    Varianti("Vai izklājums der?", [
        {"jaut": "Cik kvadrātu jābūt kuba izklājumā?",
         "opcijas": ["6", "4", "8", "12"],
         "pareizi": 0, "padoms": "Tik, cik skaldņu."},
        {"jaut": "Vai seši kvadrāti vienā rindā ir kuba izklājums?",
         "opcijas": ["Nē, tie pārklājas", "Jā", "Tikai maziem kubiem",
                     "To nevar pateikt"],
         "pareizi": 0, "padoms": "Rinda apliecas ap sevi."},
        {"jaut": "Kā droši pārbaudīt izklājumu?",
         "opcijas": ["Salokot", "Saskaitot kvadrātus", "Mērot",
                     "Nekā"],
         "pareizi": 0, "padoms": "Tikai locīšana dod drošu atbildi."},
        {"jaut": "Cik figūru ir četrstūra piramīdas izklājumā?",
         "opcijas": ["5", "4", "6", "8"],
         "pareizi": 0, "padoms": "Pamats un četri sāni."},
    ], pamats=4),

    Pasaule("Cik kartona aiziet iepakojumam?",
            Ievadi("", [
                {"jaut": "Kubs ar malu 4 cm. Cik kvadrātcentimetru ir "
                         "izklājums?",
                 "atb": ["96"], "padoms": "6 · 16."},
                {"jaut": "Cik kvadrātcentimetru vajag 10 tādām kastītēm?",
                 "atb": ["960"], "padoms": "10 · 96."},
                {"jaut": "Kartona loksne ir 1000 cm². Cik kastīšu no tās "
                         "sanāks?",
                 "atb": ["10"], "padoms": "1000 : 96 ar atlikumu."},
                {"jaut": "Cik kvadrātcentimetru paliks pāri?", "atb": ["40"],
                 "padoms": "1000 − 960."},
            ]),
            pavediens="veikals",
            konteksts="Ražotājs uz vienas loksnes izvieto pēc iespējas vairāk "
                      "izklājumu - lai atgriezumu paliktu mazāk.",
            kapec="Katrs nederīgs izklājums ir izniekots kartons."),

    Kopsavilkums([
        "Zinu, ka kuba izklājumā ir 6 kvadrāti.",
        "Zinu, ka ne katrs sešu kvadrātu salikums ir izklājums.",
        "Izsaku pieņēmumu un pārbaudu to, salokot.",
        "Aprēķinu izklājuma laukumu.",
    ]),

    Majas([
        "Izgriez divus dažādus sešu kvadrātu salikumus un pārbaudi tos.",
        "Atrodi vismaz trīs derīgus kuba izklājumus.",
        "Izrēķini kuba ar malu 6 cm izklājuma laukumu.",
    ]),
]
