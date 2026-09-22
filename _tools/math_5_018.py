# -*- coding: utf-8 -*-
"""5. klase, 18. stunda: «Kā aizpildīt maģisko kvadrātu?»

Maģiskais kvadrāts te nav mīkla atpūtai, bet pirmais uzdevums, kurā skaitli
meklē pēc nosacījuma, nevis pēc darbības. Tieši šī doma - «summa jau ir
zināma, trūkst viena saskaitāmā» - 21. stundā kļūst par nezināmā burtu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā aizpildīt maģisko kvadrātu?"

MERKIS = ("Mācīsimies aizpildīt skaitļu sakārtojumus - maģisko kvadrātu un "
          "skaitļu trijstūri - pēc dotiem nosacījumiem.")

SATURS = [
    Sakums("Kāpēc šo kvadrātu sauc par maģisko?",
           zimejums=restis([[8, 1, 6], [3, 5, 7], [4, 9, 2]]),
           paraksts="Saskaiti jebkuru rindu, kolonnu vai diagonāli - vienmēr "
                    "sanāk 15.",
           fakti=["Katrs skaitlis no 1 līdz 9 lietots tieši vienu reizi.",
                  "Rindu ir trīs, kolonnu trīs un diagonāļu divas.",
                  "Astoņas dažādas summas, un visas ir vienādas."]),

    Doma("Sāc no rindas, kurā trūkst tikai viena skaitļa",
         "Ja summa ir zināma un trūkst viena saskaitāmā, to atrod ar "
         "atņemšanu.",
         soli=[
             "Noskaidro, kādai jābūt vienas rindas summai.",
             "Atrodi rindu, kolonnu vai diagonāli ar diviem zināmiem "
             "skaitļiem.",
             "Atņem abus no summas - sanāk trūkstošais skaitlis.",
             "Ieraksti to un meklē nākamo rindu, kurā tagad trūkst viena.",
         ],
         pieze="Ja kvadrātā ir skaitļi no 1 līdz 9, to summa ir 45. Trīs "
               "rindas ar vienādu summu nozīmē 45 : 3 = 15 - tāpēc rindas "
               "summu var zināt jau pirms rēķināšanas."),

    Zimejums("Aizpildi trūkstošo",
             restis([[None, 1, 6], [3, 5, None], [4, None, 2]],
                    "summa vienmēr 15"),
             paskaidro="Pirmajā rindā zināmi 1 un 6, tāpēc sāc tieši no tās: "
                       "15 − 1 − 6 = 8.",
             ievads="Trīs rūtiņas tukšas, bet nevienu nevajag minēt."),

    Paraugs("Atrodi visus trūkstošos skaitļus",
            uzd="Kvadrātā jāizmanto skaitļi no 1 līdz 9, katras rindas summa "
                "ir 15. Zināms: 1. rindā _, 1, 6; 2. rindā 3, 5, _; 3. rindā "
                "4, _, 2.",
            soli=[
                ("1. rinda: 15 − 1 − 6 = 8",
                 "Rinda, kurā zināmi divi skaitļi."),
                ("2. rinda: 15 − 3 − 5 = 7",
                 "Tagad tas pats otrajā rindā."),
                ("3. rinda: 15 − 4 − 2 = 9",
                 "Un trešajā."),
                ("Pārbaude: 8 + 3 + 4 = 15",
                 "Pirmā kolonna arī dod 15 - kvadrāts ir pareizs."),
            ],
            atbilde="trūkstošie skaitļi ir 8, 7 un 9"),

    Ievadi("Kas trūkst?", [
        {"jaut": "Rindas summa ir 15. Rindā ir 8, 1 un ?. Kas trūkst?",
         "atb": ["6"], "padoms": "15 − 8 − 1."},
        {"jaut": "Rindas summa ir 15. Rindā ir 4, 9 un ?.",
         "atb": ["2"], "padoms": "15 − 4 − 9."},
        {"jaut": "Kolonnas summa ir 15. Kolonnā ir 8, 3 un ?.",
         "atb": ["4"], "padoms": "15 − 8 − 3."},
        {"jaut": "Diagonāles summa ir 15. Diagonālē ir 8, 5 un ?.",
         "atb": ["2"], "padoms": "15 − 8 − 5."},
        {"jaut": "Cik ir visu skaitļu no 1 līdz 9 summa?",
         "atb": ["45"], "padoms": "1 + 2 + ... + 9; saliec pa pāriem: "
                                  "1 + 9, 2 + 8, 3 + 7, 4 + 6 un vēl 5."},
        {"jaut": "Trīs rindas, katra ar vienādu summu. Cik ir vienas rindas "
                 "summa?",
         "atb": ["15"], "padoms": "45 : 3."},
        {"jaut": "Kvadrātā lieto skaitļus no 2 līdz 10. Cik ir to summa?",
         "atb": ["54"], "padoms": "Katrs par 1 lielāks nekā iepriekš: "
                                  "45 + 9."},
        {"jaut": "Tad cik ir vienas rindas summa kvadrātā no 2 līdz 10?",
         "atb": ["18"], "padoms": "54 : 3."},
    ], pamats=4,
        ievads="Trūkstošo saskaitāmo atrod, atņemot no summas."),

    Varianti("Kā domā, aizpildot kvadrātu?", [
        {"jaut": "Ar kuru rindu sākt?",
         "opcijas": ["Ar to, kurā zināmi divi skaitļi",
                     "Ar pirmo no augšas",
                     "Ar to, kurā ir lielākais skaitlis",
                     "Vienalga ar kuru"],
         "pareizi": 0,
         "padoms": "Tikai tad trūkst viena skaitļa, un to var izrēķināt."},
        {"jaut": "Kā uzzināt rindas summu, ja kvadrāts vēl tukšs, bet zināms, "
                 "ka lietoti skaitļi no 1 līdz 9?",
         "opcijas": ["45 : 3", "45 : 9", "9 · 3", "15 · 3"],
         "pareizi": 0,
         "padoms": "Visu skaitļu summu sadala pa trim rindām."},
        {"jaut": "Ja katram kvadrāta skaitlim pieskaita 1, kas notiek ar "
                 "rindas summu?",
         "opcijas": ["Palielinās par 3", "Palielinās par 1",
                     "Nemainās", "Palielinās par 9"],
         "pareizi": 0,
         "padoms": "Rindā ir trīs skaitļi, katram pa 1."},
        {"jaut": "Skolēns aizpildīja kvadrātu, un viena kolonna dod 16. Ko "
                 "tas nozīmē?",
         "opcijas": ["Kaut kur ir kļūda", "Kvadrāts ir pareizs",
                     "Jāmaina summa uz 16", "Diagonāles nav jāpārbauda"],
         "pareizi": 0,
         "padoms": "Maģiskajā kvadrātā visas astoņas summas ir vienādas."},
    ], pamats=4),

    Pasaule("Kā sadalīt dežūras?",
            Ievadi("", [
                {"jaut": "Dežūru plānā katrā rindā jāsanāk 18 stundām. Rindā "
                         "ir 9, 2 un ?. Cik?",
                 "atb": ["7"], "padoms": "18 − 9 − 2."},
                {"jaut": "Kolonnā ir 9, 4 un ?. Cik?",
                 "atb": ["5"], "padoms": "18 − 9 − 4."},
                {"jaut": "Diagonālē ir 9, 6 un ?. Cik?",
                 "atb": ["3"], "padoms": "18 − 9 − 6."},
                {"jaut": "Trīs rindas pa 18 stundām. Cik stundu pavisam?",
                 "atb": ["54"], "padoms": "18 · 3."},
            ]),
            pavediens="skola",
            konteksts="Dežūras sadala tā, lai nevienai klasei nesanāktu "
                      "vairāk nekā citām - tas ir tas pats nosacījums.",
            kapec="Ja summa zināma, trūkstošo daļu vienmēr atrod ar "
                  "atņemšanu."),

    Kopsavilkums([
        "Aizpildu maģisko kvadrātu, sākot no rindas ar diviem zināmiem "
        "skaitļiem.",
        "Atrodu trūkstošo saskaitāmo, atņemot zināmos no summas.",
        "Izrēķinu rindas summu jau iepriekš, zinot, kuri skaitļi lietoti.",
        "Pārbaudu darbu: visām rindām, kolonnām un diagonālēm viena summa.",
    ]),

    Majas([
        "Uzzīmē savu 3x3 kvadrātu ar skaitļiem no 1 līdz 9 un pārbaudi visas "
        "astoņas summas.",
        "Aizsedz trīs skaitļus un iedod kvadrātu draugam aizpildīt.",
        "Pamēģini uzzīmēt skaitļu trijstūri, kurā katras malas summa ir "
        "vienāda.",
    ]),
]
