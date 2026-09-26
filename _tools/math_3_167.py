# -*- coding: utf-8 -*-
"""3. klase, 167. stunda: «Kuras skaldnes būs blakus?»

Temata pēdējā mācību stunda: prognoze un pārbaude. Uz izklājuma skolēns
paredz, kuras skaldnes salokot saskarsies, un tikai tad saloka. Tas ir tas
pats spriešanas veids, kas 162. stundā, tikai grūtāks.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         izklajums, restis)

TEMA = "Kuras skaldnes būs blakus?"

MERKIS = ("Prognozēsim, kuras krāsainā izklājuma skaldnes saskarsies, un "
          "pārbaudīsim pieņēmumu.")

SATURS = [
    Sakums("Kuras skaldnes salokot nonāks pretī viena otrai?",
           zimejums=izklajums(2, 2, 2),
           paraksts="Katrai skaldnei ir tieši viena pretējā un četras "
                    "blakus.",
           fakti=["Kubam katrai skaldnei ir viena pretējā un četras blakus.",
                  "Pretējās skaldnes izklājumā nekad nav blakus."]),

    Doma("Katrai skaldnei viena pretējā un četras blakus",
         "Izklājumā pretējās skaldnes vienmēr ir atdalītas ar vienu skaldni - "
         "tieši tāpēc tās salokot nonāk pretī.",
         soli=[
             "Izvēlies vienu skaldni un iedomājies to par apakšu.",
             "Atrodi to skaldni, kas krusta rindā ir caur vienu - tā būs "
             "augša.",
             "Pārējās četras kļūs par sāniem.",
             "Saloc un pārbaudi savu pieņēmumu.",
         ],
         pieze="Krusta formas izklājumā pretējās ir tās, kas atrodas vienā "
               "rindā ar vienu skaldni starp tām."),

    Petijums("Iekrāso un pārbaudi",
             vajag="kuba izklājums uz papīra, krāsainie zīmuļi un līmlente",
             soli=[
                 "Iekrāso izklājuma skaldnes sešās dažādās krāsās.",
                 "Pieraksti, kuras krāsas, tavuprāt, nonāks pretī.",
                 "Saloc kubu un pārbaudi.",
                 "Atzīmē, kuras prognozes izrādījās pareizas.",
             ],
             secinajums="Pretējās skaldnes vienmēr ir tās, kas izklājumā ir "
                        "atdalītas ar vienu skaldni."),

    Paraugs("Kuras skaldnes būs pretī?",
            uzd="Krusta formas izklājumā vidējā rindā pēc kārtas ir "
                "skaldnes A, B, C un D. Kura būs pretī skaldnei A?",
            soli=[
                ("A un B ir blakus",
                 "Salokot tās saskaras pa šķautni."),
                ("A un C atdala viena skaldne",
                 "Tātad tās nonāk pretī."),
                ("Pretī A ir C",
                 "B un D kļūs par sāniem."),
            ],
            atbilde="skaldne C"),

    Ievadi("Skaldņu attiecības", [
        {"jaut": "Cik skaldņu ir pretī vienai kuba skaldnei?", "atb": ["1"],
         "padoms": "Tikai viena."},
        {"jaut": "Cik skaldņu ir blakus vienai kuba skaldnei?", "atb": ["4"],
         "padoms": "6 − 1 − 1."},
        {"jaut": "Cik pretējo skaldņu pāru ir kubam?", "atb": ["3"],
         "padoms": "6 : 2."},
        {"jaut": "Cik skaldņu ir kubam?", "atb": ["6"],
         "padoms": "Augša, apakša, četri sāni."},
        {"jaut": "Kubam uz pretējām skaldnēm uzraksta 1 un 6, 2 un 5, 3 un 4. "
                 "Cik ir katra pāra summa?",
         "atb": ["7"], "padoms": "1 + 6."},
        {"jaut": "Cik ir visu sešu skaitļu summa?", "atb": ["21"],
         "padoms": "3 · 7."},
    ], pamats=4),

    Zimejums("Pretējo skaldņu pāri",
             restis([["pāris", "summa"],
                     ["1 un 6", 7],
                     ["2 un 5", 7],
                     ["3 un 4", 7]],
                    "spēļu kauliņš"),
             paskaidro="Uz spēļu kauliņa pretējo skaldņu summa vienmēr ir 7 - "
                       "tāpēc, nezinot augšu, var pateikt apakšu.",
             ievads="Tā šo prasmi lieto spēlēs."),

    Varianti("Kuras skaldnes saskarsies?", [
        {"jaut": "Cik skaldnes ir blakus vienai kuba skaldnei?",
         "opcijas": ["4", "2", "5", "6"],
         "pareizi": 0, "padoms": "Visas, izņemot sevi un pretējo."},
        {"jaut": "Uz spēļu kauliņa augšā ir 2. Kas ir apakšā?",
         "opcijas": ["5", "4", "6", "1"],
         "pareizi": 0, "padoms": "Summa ir 7."},
        {"jaut": "Cik pretējo skaldņu pāru ir kubam?",
         "opcijas": ["3", "6", "2", "4"],
         "pareizi": 0, "padoms": "6 : 2."},
        {"jaut": "Kuras skaldnes izklājumā ir pretējās?",
         "opcijas": ["Tās, ko atdala viena skaldne", "Blakus esošās",
                     "Visas", "Nevienas"],
         "pareizi": 0, "padoms": "Salokot tās nonāk pretī."},
    ], pamats=4),

    Pasaule("Kā uzdrukā uz iepakojuma?",
            Ievadi("", [
                {"jaut": "Kastītei 6 skaldnes. Cik no tām var uzdrukāt "
                         "vienu un to pašu attēlu, ja tas jāredz no "
                         "pretējām pusēm?",
                 "atb": ["2"], "padoms": "Viens pretējo pāris."},
                {"jaut": "Cik pretējo pāru ir kastītei?", "atb": ["3"],
                 "padoms": "6 : 2."},
                {"jaut": "Uz katras skaldnes drukā 2 attēlus. Cik attēlu ir "
                         "vienai kastītei?",
                 "atb": ["12"], "padoms": "6 · 2."},
                {"jaut": "Cik attēlu vajag 20 kastītēm?", "atb": ["240"],
                 "padoms": "20 · 12."},
            ]),
            pavediens="veikals",
            konteksts="Uz iepakojuma svarīgākais attēls parasti ir uz divām "
                      "pretējām skaldnēm - lai to redzētu no abām pusēm.",
            kapec="Bez izklājuma nevar pateikt, kura druka nonāks kur."),

    Kopsavilkums([
        "Prognozēju, kuras izklājuma skaldnes saskarsies.",
        "Zinu, ka katrai skaldnei ir viena pretējā un četras blakus.",
        "Pārbaudu pieņēmumu, salokot modeli.",
        "Lietoju šo prasmi spēļu kauliņam.",
    ]),

    Majas([
        "Iekrāso kuba izklājumu un pārbaudi savu prognozi.",
        "Paņem spēļu kauliņu un pārbaudi, vai pretējo skaldņu summa ir 7.",
        "Pārlasi tematu un atzīmē, kas vēl jāatkārto pirms pārbaudes darba.",
    ], ievads="Šī ir pēdējā stunda pirms pārbaudes darba."),
]
