# -*- coding: utf-8 -*-
"""3. klase, 4. stunda: «Kā atcerēties reizinājumus ar 6?»

Stratēģija, nevis iekalšana: piecnieku rindu skolēns zina droši, tāpēc
sešnieku iegūst no tās ar vienu soli - 6 · 8 ir 5 · 8 un vēl astoņi. Tas ir
pirmais paņēmiens, kas rāda, ka tabulu var *izrēķināt*, nevis tikai atcerēties.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kā atcerēties reizinājumus ar 6?"

MERKIS = ("Izstrādāsim savu paņēmienu, kā no piecnieku rindas iegūt "
          "sešnieku rindu, un pārbaudīsim to.")

SATURS = [
    Sakums("Vai 6 · 8 var izrēķināt, to neatceroties?",
           zimejums=restis([["5 ·", "5 ·", "5 ·", "5 ·", "5 ·", "5 ·",
                             "5 ·", "5 ·"],
                            ["+1", "+1", "+1", "+1", "+1", "+1", "+1",
                             "+1"]],
                           "sešas reizes ir piecas reizes un vēl viena"),
           paraksts="Augšējā rinda ir 5 · 8, apakšējā pieliek vēl 8.",
           fakti=["Piecnieku rindu tu zini no galvas - tā ir atbalsts.",
                  "Sešas grupas ir piecas grupas un vēl viena."]),

    Doma("Sešas reizes ir piecas reizes un vēl viena",
         "6 · a = 5 · a + a - tāpēc katru sešnieku var iegūt no piecnieka ar "
         "vienu saskaitīšanu.",
         soli=[
             "Izrēķini 5 · a - piecnieku rinda beidzas ar 0 vai 5.",
             "Pieskaiti vēl vienu grupu, tas ir, pašu skaitli a.",
             "Sanākusī atbilde ir 6 · a.",
             "Pārbaudi to ar sešnieku rindu: 6, 12, 18, 24, 30, 36, ...",
         ],
         pieze="Tas pats paņēmiens der arī uz otru pusi: 4 · a ir 5 · a "
               "*mīnus* a. Viena zināma rinda palīdz abām kaimiņrindām."),

    Paraugs("Kā ātri iegūt 6 · 8?",
            uzd="Izrēķini 6 · 8, izmantojot piecnieku rindu.",
            soli=[
                ("5 · 8 = 40",
                 "Piecas astoņnieku grupas - šo proti no galvas."),
                ("40 + 8 = 48",
                 "Sestā grupa pieliek vēl astoņus."),
                ("6 · 8 = 48",
                 "Pārbaude sešnieku rindā: 42, 48 - sakrīt."),
            ],
            atbilde="48"),

    Ievadi("Rēķini pa soļiem", [
        {"jaut": "5 · 7 = 35. Cik ir 6 · 7?", "atb": ["42"],
         "padoms": "35 + 7."},
        {"jaut": "5 · 9 = 45. Cik ir 6 · 9?", "atb": ["54"],
         "padoms": "45 + 9."},
        {"jaut": "5 · 6 = 30. Cik ir 6 · 6?", "atb": ["36"],
         "padoms": "30 + 6."},
        {"jaut": "5 · 4 = 20. Cik ir 6 · 4?", "atb": ["24"],
         "padoms": "20 + 4."},
        {"jaut": "5 · 10 = 50. Cik ir 6 · 10?", "atb": ["60"],
         "padoms": "50 + 10."},
        {"jaut": "5 · 3 = 15. Cik ir 6 · 3?", "atb": ["18"],
         "padoms": "15 + 3."},
    ], pamats=4,
        ievads="Pirmais rēķins jau ir izdarīts - tev jāpieliek vēl viena "
               "grupa."),

    Zimejums("Piecnieku rinda un sešnieku rinda blakus",
             restis([[5, 10, 15, 20, 25, 30],
                     [6, 12, 18, 24, 30, 36]],
                    "augšā 5 ·, apakšā 6 ·"),
             paskaidro="Katrs apakšējais skaitlis ir par tik lielāks, cik "
                       "liela ir tā vieta rindā: 6 = 5 + 1, 12 = 10 + 2.",
             ievads="Salīdzini abas rindas pa pāriem."),

    Varianti("Kurš solis ir pareizais?", [
        {"jaut": "Kā no 5 · 7 iegūt 6 · 7?",
         "opcijas": ["Pieskaita 7", "Pieskaita 5", "Pieskaita 1",
                     "Reizina ar 2"],
         "pareizi": 0, "padoms": "Pieliek vēl vienu septiņnieku grupu."},
        {"jaut": "Kā no 5 · 9 iegūt 4 · 9?",
         "opcijas": ["Atņem 9", "Atņem 5", "Atņem 1", "Dala ar 2"],
         "pareizi": 0, "padoms": "Noņem vienu deviņnieku grupu."},
        {"jaut": "6 · 5 = ?",
         "opcijas": ["30", "35", "25", "11"],
         "pareizi": 0, "padoms": "5 · 5 = 25, pieskaiti vēl 5."},
        {"jaut": "Kurš rēķins *nav* vienāds ar 6 · 4?",
         "opcijas": ["5 · 4 + 5", "5 · 4 + 4", "4 · 6", "3 · 4 + 3 · 4"],
         "pareizi": 0, "padoms": "Pieliek vēl vienu četrinieku grupu, ne "
                                 "piecinieku."},
    ], pamats=4),

    Pasaule("Cik ola ir olu kastēs?",
            Ievadi("", [
                {"jaut": "Vienā kastē ir 6 olas. Cik olu ir 7 kastēs?",
                 "atb": ["42"], "padoms": "5 · 7 = 35, pieskaiti 7."},
                {"jaut": "Cik olu ir 9 kastēs?",
                 "atb": ["54"], "padoms": "45 + 9."},
                {"jaut": "Virtuvē saskaitīja 36 olas. Cik kastu tas ir?",
                 "atb": ["6"], "padoms": "36 : 6."},
                {"jaut": "Receptei vajag 8 olas. Cik olu paliks pāri no "
                         "divām kastēm?",
                 "atb": ["4"], "padoms": "2 · 6 = 12; 12 − 8."},
            ]),
            pavediens="virtuve",
            konteksts="Olas veikalā pārdod pa sešām - tāpēc virtuvē "
                      "sešnieku rinda ir vajadzīga gandrīz katru nedēļu.",
            kapec="Kad iepakojums ir vienāds, kopskaitu var izrēķināt, "
                  "neatverot nevienu kasti."),

    Petijums("Pārbaudi savu paņēmienu",
             vajag="lapa un zīmulis",
             soli=[
                 "Uzraksti vienā kolonnā piecnieku rindu no 5 līdz 50.",
                 "Blakus katram skaitlim pieraksti, cik jāpieskaita.",
                 "Izrēķini un pieraksti sešnieku rindu.",
                 "Pārbaudi to ar skaitīšanu pa 6: 6, 12, 18, ...",
             ],
             secinajums="Ja abas reizes iznāk tas pats, paņēmiens strādā - "
                        "un tam var uzticēties arī kontroldarbā."),

    Kopsavilkums([
        "Zinu paņēmienu 6 · a = 5 · a + a un lietoju to.",
        "No piecnieku rindas iegūstu gan sešnieku, gan četrinieku rindu.",
        "Pārbaudu savu rezultātu ar sešnieku rindu.",
        "Paskaidroju savu atcerēšanās paņēmienu citiem.",
    ]),

    Majas([
        "Izrēķini 6 · 7, 6 · 8 un 6 · 9, katru reizi sākot no piecnieka.",
        "Izdomā savu paņēmienu, kā atcerēties 6 · 6, un pastāsti to mājās.",
        "Saskaiti, cik olu ir mājās esošajās kastēs.",
    ]),
]
