# -*- coding: utf-8 -*-
"""3. klase, 30. stunda: «Pērku divreiz vairāk - cik maksā?»

Pirmā sakarība starp diviem lielumiem: ja cena nemainās, tad summa aug tieši
tikpat reižu, cik preču skaits. Tā ir tiešā proporcionalitāte, vēl bez
nosaukuma, un tieši uz tās vēlāk balstās gan mērogs, gan procenti.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Pērku divreiz vairāk - cik maksā?"

MERKIS = ("Formulēsim sakarību starp preču daudzumu un pirkuma summu, ja "
          "cena nemainās.")

SATURS = [
    Sakums("Vai divreiz vairāk preču maksā divreiz vairāk?",
           zimejums=restis([["gab.", 1, 2, 4, 8],
                            ["ct", 7, 14, 28, 56]],
                           "cena 7 ct par gabalu"),
           paraksts="Kad preču skaits divkāršojas, summa arī divkāršojas.",
           fakti=["Ja cena nemainās, summa aug tikpat reižu, cik daudzums.",
                  "Tāpēc summu var iegūt arī bez reizināšanas - dubultojot."]),

    Doma("Cik reižu vairāk preču, tik reižu lielāka summa",
         "Ja cena paliek tā pati, tad preču skaits un summa mainās vienādi.",
         soli=[
             "Noskaidro vienas preces cenu.",
             "Paskaties, cik reižu preču skaits ir lielāks.",
             "Reizini summu ar to pašu skaitu reižu.",
             "Pārbaudi ar reizināšanu: skaits reiz cena.",
         ],
         pieze="Tas strādā arī uz otru pusi: ja preču ir trīs reizes mazāk, "
               "summa ir trīs reizes mazāka."),

    Paraugs("Cik maksā 6 gabali, ja 2 maksā 18 ct?",
            uzd="Divas preces maksā 18 ct. Cik maksā sešas tādas preces?",
            soli=[
                ("6 : 2 = 3",
                 "Preču ir trīs reizes vairāk."),
                ("18 · 3 = 54",
                 "Tātad arī summa ir trīs reizes lielāka."),
                ("18 : 2 = 9; 6 · 9 = 54",
                 "Pārbaude caur vienas preces cenu - tā pati atbilde."),
            ],
            atbilde="54 ct"),

    Ievadi("Cik maksās?", [
        {"jaut": "1 prece maksā 8 ct. Cik maksā 4 preces?",
         "atb": ["32"], "padoms": "4 · 8."},
        {"jaut": "3 preces maksā 24 ct. Cik maksā 6 preces?",
         "atb": ["48"], "padoms": "Preču divreiz vairāk."},
        {"jaut": "4 preces maksā 36 ct. Cik maksā 1 prece?",
         "atb": ["9"], "padoms": "36 : 4."},
        {"jaut": "5 preces maksā 45 ct. Cik maksā 10 preces?",
         "atb": ["90"], "padoms": "Divreiz vairāk."},
        {"jaut": "8 preces maksā 56 ct. Cik maksā 2 preces?",
         "atb": ["14"], "padoms": "Četras reizes mazāk."},
        {"jaut": "6 preces maksā 42 ct. Cik maksā 3 preces?",
         "atb": ["21"], "padoms": "Divreiz mazāk."},
    ], pamats=4),

    Petijums("Uztaisi savu cenu tabulu",
             vajag="lapa, zīmulis un lineāls",
             soli=[
                 "Izvēlies preci un tās cenu - vienciparu vai divciparu.",
                 "Uzzīmē tabulu ar rindām «gabali» un «cena».",
                 "Aizpildi to skaitļiem no 1 līdz 10.",
                 "Apvelc pārus, kuros otrais skaits ir divreiz lielāks par "
                 "pirmo, un salīdzini cenas.",
             ],
             secinajums="Katrā apvilktajā pārī arī cena ir tieši divreiz "
                        "lielāka - tā strādā sakarība."),

    Zimejums("Cenu tabula",
             restis([["gab.", 1, 2, 3, 4, 5],
                     ["ct", 9, 18, 27, 36, 45]],
                    "cena 9 ct par gabalu"),
             paskaidro="Apakšējā rinda ir deviņnieku rinda - tāpēc reizinājumu "
                       "tabula noder arī veikalā.",
             ievads="Katrs nākamais gabals pieliek vēl 9 ct."),

    Varianti("Vai sakarība der?", [
        {"jaut": "2 preces maksā 14 ct. Cik maksā 4 preces?",
         "opcijas": ["28 ct", "16 ct", "21 ct", "56 ct"],
         "pareizi": 0, "padoms": "Preču divreiz vairāk."},
        {"jaut": "Kas notiek ar summu, ja preču ir trīs reizes mazāk?",
         "opcijas": ["Tā ir trīs reizes mazāka", "Tā nemainās",
                     "Tā ir par 3 mazāka", "Tā ir trīs reizes lielāka"],
         "pareizi": 0, "padoms": "Abi lielumi mainās vienādi."},
        {"jaut": "Kad šī sakarība *nestrādā*?",
         "opcijas": ["Ja lielākam daudzumam ir atlaide",
                     "Ja preču ir daudz", "Ja cena ir divciparu",
                     "Ja pērk vienu preci"],
         "pareizi": 0, "padoms": "Sakarība prasa, lai cena nemainās."},
        {"jaut": "10 preces maksā 60 ct. Cik maksā 5 preces?",
         "opcijas": ["30 ct", "12 ct", "55 ct", "120 ct"],
         "pareizi": 0, "padoms": "Preču divreiz mazāk."},
    ], pamats=4),

    Pasaule("Ko izdevīgāk pirkt?",
            Ievadi("", [
                {"jaut": "Paciņa ar 4 sulām maksā 48 ct. Cik maksā viena "
                         "sula?",
                 "atb": ["12"], "padoms": "48 : 4."},
                {"jaut": "Lielā paciņa ar 8 sulām maksā 88 ct. Cik maksā "
                         "viena sula tajā?",
                 "atb": ["11"], "padoms": "88 : 8."},
                {"jaut": "Par cik centiem lētāka ir viena sula lielajā "
                         "paciņā?",
                 "atb": ["1"], "padoms": "12 − 11."},
                {"jaut": "Cik maksātu 8 sulas, pērkot divas mazās paciņas?",
                 "atb": ["96"], "padoms": "2 · 48."},
            ]),
            pavediens="veikals",
            konteksts="Lielāks iepakojums bieži ir lētāks par gabalu - bet ne "
                      "vienmēr, un to var pārbaudīt tikai ar rēķinu.",
            kapec="Salīdzināt var tikai vienas preces cenu, ne paciņas cenu."),

    Kopsavilkums([
        "Formulēju sakarību starp preču daudzumu un summu.",
        "Aprēķinu summu, zinot vienas preces cenu.",
        "Atrodu vienas preces cenu no komplekta cenas.",
        "Zinu, ka sakarība der tikai tad, ja cena nemainās.",
    ]),

    Majas([
        "Atrodi mājās divus dažāda lieluma iepakojumus un salīdzini vienas "
        "vienības cenu.",
        "Uzzīmē cenu tabulu precei, kas maksā 6 ct.",
        "Pastāsti mājiniekiem, kad lielākais iepakojums nav izdevīgāks.",
    ]),
]
