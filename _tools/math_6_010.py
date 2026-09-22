# -*- coding: utf-8 -*-
"""6. klase, 10. stunda: «Cik katram pienākas?»

Mikrotemata pēdējā stunda. Visi iepriekšējie uzdevumi sākās ar kopumu; te
nezināmais var būt jebkurā vietā - kopums, viena daļa vai pat pati
attiecība. Tas prasa nevis jaunu darbību, bet plānu: ko zinu, ko meklēju.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Cik katram pienākas?"

MERKIS = ("Iemācīsimies sadalīt kopumu dotā attiecībā arī tad, ja nezināmais "
          "ir starpība, viena daļa vai kopums.")

SATURS = [
    Sakums("Kā sadalīt godīgi, ja ieguldījums nav vienāds?",
           fakti=["Trīs draugi nopelnīja 240 € un strādāja 2, 3 un 5 dienas.",
                  "Vienādi dalīt būtu vienkārši, bet negodīgi.",
                  "Attiecība 2 : 3 : 5 pasaka, cik pienākas katram."]),

    Doma("Vispirms pieraksti, kas ir zināms",
         "Uzdevumu atrisina viena daļa - tāpēc vienmēr meklē to vispirms, "
         "lai kurā vietā nezināmais būtu.",
         soli=[
             "Pieraksti attiecību un saskaiti daļu skaitu.",
             "Atrodi, kurš skaitlis uzdevumā ir zināms: kopums, viena daļa "
             "vai starpība.",
             "Izrēķini vienu daļu: kopumu dala ar daļu skaitu, starpību - "
             "ar daļu *starpību*.",
             "Reizini vienu daļu ar katru attiecības skaitli.",
             "Pārbaudi visus nosacījumus, ne tikai vienu.",
         ],
         pieze="Ja zināma starpība, dala ar daļu starpību: «par 9 vairāk» "
               "attiecībā 2 : 5 nozīmē, ka 3 daļas ir 9, tātad viena daļa "
               "ir 3."),

    Paraugs("Zināma starpība, ne kopums",
            uzd="Divi brāļi savāca ogas attiecībā 2 : 5. Otrs savāca par "
                "9 kg vairāk. Cik savāca katrs?",
            soli=[
                ("5 − 2 = 3 daļas",
                 "Tik daļu ir starpībā."),
                ("9 : 3 = 3 kg",
                 "Tik sver viena daļa."),
                ("Pirmais 2 · 3 = 6 kg",
                 "Reizina vienu daļu ar pirmo skaitli."),
                ("Otrais 5 · 3 = 15 kg",
                 "Tāpat otrajam."),
                ("15 − 6 = 9 kg",
                 "Pārbaude: starpība sakrīt ar doto."),
            ],
            atbilde="6 kg un 15 kg"),

    Ievadi("Kurš skaitlis ir zināms?", [
        {"jaut": "Attiecība 2 : 3 : 5, kopā 240 €. Cik eiro ir viena daļa?",
         "atb": ["24"], "padoms": "10 daļas; 240 : 10."},
        {"jaut": "Tā pati situācija. Cik eiro saņem tas, kurš strādāja "
                 "5 dienas?",
         "atb": ["120"], "padoms": "5 · 24."},
        {"jaut": "Attiecība 1 : 4. Otrajam ir par 12 vairāk. Cik ir viena "
                 "daļa?",
         "atb": ["4"], "padoms": "Starpība ir 3 daļas; 12 : 3."},
        {"jaut": "Tā pati attiecība. Cik ir abiem kopā?",
         "atb": ["20"], "padoms": "5 daļas pa 4."},
        {"jaut": "Attiecība 3 : 7. Pirmajam ir 21. Cik ir otrajam?",
         "atb": ["49"], "padoms": "21 : 3 = 7; 7 · 7."},
        {"jaut": "Attiecība 4 : 5. Kopā 180 kg. Par cik kilogramiem otrā "
                 "daļa ir lielāka?",
         "atb": ["20"], "padoms": "9 daļas pa 20 kg; starpība ir 1 daļa."},
    ], pamats=4,
        ievads="Viena daļa vienmēr ir pirmais solis - mainās tikai tas, ar "
               "ko to dala."),

    Varianti("Kura darbība te der?", [
        {"jaut": "Zināms kopums. Ar ko dala, lai atrastu vienu daļu?",
         "opcijas": ["Ar daļu skaitu", "Ar daļu starpību",
                     "Ar lielāko skaitli", "Ar 2"],
         "pareizi": 0,
         "padoms": "Kopumā ietilpst visas daļas."},
        {"jaut": "Zināma starpība. Ar ko dala?",
         "opcijas": ["Ar daļu starpību", "Ar daļu skaitu",
                     "Ar mazāko skaitli", "Ar summu"],
         "pareizi": 0,
         "padoms": "Starpībā ietilpst tikai liekās daļas."},
        {"jaut": "Attiecība 1 : 1, kopums 50. Kas te ir īpašs?",
         "opcijas": ["Abām daļām ir vienāds daudzums",
                     "Viena daļa ir 50", "Sadalīt nevar",
                     "Starpība ir 50"],
         "pareizi": 0,
         "padoms": "Vienādas daļas - vienāds sadalījums."},
        {"jaut": "Attiecība 2 : 3, viena daļa ir 7. Kāds ir kopums?",
         "opcijas": ["35", "14", "21", "7"],
         "pareizi": 0,
         "padoms": "5 daļas pa 7."},
    ], pamats=4),

    Pasaule("Cik tālu aizbrauc katra komanda?",
            Kustiba("", [
                {"jaut": "Divas komandas veica ceļu attiecībā 3 : 5, kopā "
                         "80 km. Cik km veica otrā komanda?",
                 "atb": 50, "beigas": 80, "iedala": 10, "mers": "kilometri",
                 "merkis": "2. komanda", "objekts": "Ekipāža",
                 "padoms": "8 daļas; viena daļa 10 km; 5 · 10."},
                {"jaut": "Tā pati diena. Cik km veica pirmā komanda?",
                 "atb": 30, "beigas": 80, "iedala": 10, "mers": "kilometri",
                 "merkis": "1. komanda", "objekts": "Ekipāža",
                 "padoms": "3 · 10."},
                {"jaut": "Nākamajā dienā attiecība 1 : 3, un otrā veica par "
                         "30 km vairāk. Cik km veica otrā?",
                 "atb": 45, "beigas": 60, "iedala": 10, "mers": "kilometri",
                 "merkis": "2. komanda", "objekts": "Ekipāža",
                 "padoms": "Starpība ir 2 daļas; 30 : 2 = 15; 3 · 15."},
                {"jaut": "Tā pati diena. Cik km bija abām kopā?",
                 "atb": 60, "beigas": 60, "iedala": 10, "mers": "kilometri",
                 "merkis": "kopā", "objekts": "Ekipāža",
                 "padoms": "4 daļas pa 15 km."},
            ]),
            pavediens="celojums",
            konteksts="Divas ekipāžas brauc pa vienu maršrutu, bet nevienādi "
                      "ātri - kur tās apstāsies?",
            kapec="Viens un tas pats ceļš, sadalīts attiecībā, pasaka abu "
                  "vietu."),

    Kopsavilkums([
        "Pierakstu attiecību un saskaitu, cik daļu ir kopā.",
        "Atrodu vienu daļu arī tad, ja zināma tikai starpība.",
        "Aprēķinu katra daļu un pārbaudu visus nosacījumus.",
        "Saprotu, ka nezināmais var būt jebkurā uzdevuma vietā.",
    ]),

    Majas([
        "Izdomā uzdevumu, kurā zināma starpība, un atrisini to.",
        "Sadali 100 € attiecībā 1 : 4 un pieraksti starpību.",
        "Pajautā mājās, kā tiek dalīti kādi darbi, un pieraksti to kā "
        "attiecību.",
    ]),
]
