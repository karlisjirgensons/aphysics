# -*- coding: utf-8 -*-
"""3. klase, 32. stunda: «Kāds uzdevums sanāk tev?»

Temata pēdējā mācību stunda pirms pārbaudes darba. Skolēns pats veido
uzdevumu un izvērtē klasesbiedra darbu - tieši uzdevuma *veidošana* parāda,
vai darbības jēga ir saprasta, un vērtēšanas kritēriji sagatavo PD.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kāds uzdevums sanāk tev?"

MERKIS = ("Veidosim savu uzdevumu ar reizināšanu vai dalīšanu un izvērtēsim "
          "klasesbiedra uzdevumu pēc skaidriem kritērijiem.")

SATURS = [
    Sakums("Kas padara uzdevumu par labu uzdevumu?",
           zimejums=restis([["skaidrs stāsts", "visi skaitļi"],
                            ["viens jautājums", "atbilde sanāk"]],
                           "četri kritēriji"),
           paraksts="Ja kāda no četrām rūtiņām pietrūkst, uzdevums nestrādā.",
           fakti=["Uzdevumā jābūt visiem skaitļiem, kas vajadzīgi.",
                  "Jautājumam jābūt tikai vienam un skaidram."]),

    Doma("Uzdevumu pārbauda, to atrisinot",
         "Uzrakstīji uzdevumu - atrisini to pats, un uzreiz redzēsi, kas "
         "pietrūkst.",
         soli=[
             "Izvēlies darbību un skaitļus.",
             "Izdomā situāciju, kurā šie skaitļi ir dabiski.",
             "Uzraksti vienu skaidru jautājumu.",
             "Atrisini savu uzdevumu un pārbaudi, vai atbilde ir saprātīga.",
             "Iedod to klasesbiedram un salīdzini atbildes.",
         ],
         pieze="Ja atbilde sanāk 2,5 cilvēki vai 0,5 kastes, uzdevuma "
               "skaitļi nav izvēlēti veiksmīgi - dzīvē tādu daudzumu nav."),

    Paraugs("Kā uzlabot nepilnīgu uzdevumu?",
            uzd="«Veikalā ir 6 kastes. Cik maksā visas?» Kas te nav kārtībā?",
            soli=[
                ("Nav zināma vienas kastes cena",
                 "Uzdevumā trūkst viena skaitļa."),
                ("«Katra kaste maksā 12 ct.»",
                 "Pieliek trūkstošo skaitli."),
                ("6 · 12 = 72",
                 "Tagad uzdevums ir atrisināms, un atbilde ir 72 ct."),
            ],
            atbilde="72 ct, kad pieliek kastes cenu"),

    Petijums("Uzraksti un apmaini uzdevumu",
             vajag="lapa un zīmulis",
             soli=[
                 "Izvēlies vienu darbību: reizināšanu vai dalīšanu.",
                 "Uzraksti uzdevumu ar divciparu skaitli.",
                 "Atrisini to pats un apsedz risinājumu.",
                 "Apmainies ar klasesbiedru un atrisini viņa uzdevumu.",
                 "Salīdziniet atbildes un pārrunājiet atšķirības.",
             ],
             secinajums="Ja atbildes nesakrīt, gandrīz vienmēr vainīgs nav "
                        "rēķins, bet uzdevuma teksts."),

    Ievadi("Atrisini klasesbiedru uzdevumus", [
        {"jaut": "«7 plaukti pa 14 grāmatām. Cik grāmatu kopā?»",
         "atb": ["98"], "padoms": "70 + 28."},
        {"jaut": "«84 grāmatas 6 plauktos pa vienādi. Cik vienā plauktā?»",
         "atb": ["14"], "padoms": "60 : 6 un 24 : 6."},
        {"jaut": "«5 kastes pa 16 āboliem. Cik ābolu kopā?»",
         "atb": ["80"], "padoms": "50 + 30."},
        {"jaut": "«96 zīmuļi 8 kastēs. Cik zīmuļu vienā kastē?»",
         "atb": ["12"], "padoms": "80 : 8 un 16 : 8."},
        {"jaut": "«Kabatā 90 ct, nopirka 3 preces pa 25 ct. Cik palika?»",
         "atb": ["15"], "padoms": "3 · 25 = 75; 90 − 75."},
        {"jaut": "«4 somas pa 13 burtnīcām. Cik burtnīcu kopā?»",
         "atb": ["52"], "padoms": "40 + 12."},
    ], pamats=4),

    Zimejums("Kā vērtēt uzdevumu",
             restis([["kritērijs", "jā vai nē"],
                     ["Vai skaidrs, par ko ir stāsts?", ""],
                     ["Vai ir visi skaitļi?", ""],
                     ["Vai jautājums ir viens?", ""],
                     ["Vai atbilde ir saprātīga?", ""]],
                    "vērtēšanas lapa"),
             paskaidro="Pēc šīs tabulas var izvērtēt gan savu, gan "
                       "klasesbiedra uzdevumu.",
             ievads="Četri jautājumi, uz kuriem jāatbild ar «jā»."),

    Varianti("Vai uzdevums ir gatavs?", [
        {"jaut": "«Klasē ir 24 skolēni. Cik grupu sanāks?» Kas pietrūkst?",
         "opcijas": ["Cik skolēnu ir vienā grupā", "Cik ir klašu",
                     "Kāds ir skolēnu vecums", "Nekas nepietrūkst"],
         "pareizi": 0, "padoms": "Nav zināms grupas lielums."},
        {"jaut": "«7 kastes pa 9 olām. Cik olu kopā un cik maksā?» Kas nav "
                 "kārtībā?",
         "opcijas": ["Jautājumi ir divi", "Skaitļi ir par lieliem",
                     "Nav zināms kastu skaits", "Viss ir kārtībā"],
         "pareizi": 0, "padoms": "Vienā uzdevumā - viens jautājums."},
        {"jaut": "Kura atbilde parāda, ka skaitļi izvēlēti slikti?",
         "opcijas": ["3 bērni un puse", "12 bērni", "8 kastes", "45 ct"],
         "pareizi": 0, "padoms": "Cilvēku skaits ir vesels skaitlis."},
        {"jaut": "Kā visātrāk pārbaudīt savu uzdevumu?",
         "opcijas": ["Atrisināt to pašam", "Pārrakstīt to skaisti",
                     "Uzrakstīt vēl vienu", "Pajautāt skolotājam"],
         "pareizi": 0, "padoms": "Risinot uzreiz redz, kas pietrūkst."},
    ], pamats=4),

    Pasaule("Uzraksti uzdevumu par klases veikaliņu",
            Ievadi("", [
                {"jaut": "«Klases veikaliņā 8 paciņas pa 15 cepumiem. Cik "
                         "cepumu kopā?»",
                 "atb": ["120"], "padoms": "80 + 40."},
                {"jaut": "«120 cepumus sadala 6 klasēm. Cik katrai?»",
                 "atb": ["20"], "padoms": "120 : 6."},
                {"jaut": "«Viena paciņa maksā 45 ct. Cik maksā 2 paciņas?»",
                 "atb": ["90"], "padoms": "2 · 45."},
                {"jaut": "«Ieņēma 90 ct, izdeva 60 ct. Cik palika?»",
                 "atb": ["30"], "padoms": "90 − 60."},
            ]),
            pavediens="skola",
            konteksts="Klases pasākumam vienmēr vajag saskaitīt gan preces, "
                      "gan naudu - tie ir īsti uzdevumi.",
            kapec="Uzdevums, kas nāk no dzīves, pats pasaka, vai atbilde ir "
                  "saprātīga."),

    Kopsavilkums([
        "Veidoju savu uzdevumu ar reizināšanu vai dalīšanu.",
        "Pārbaudu, vai uzdevumā ir visi skaitļi un viens jautājums.",
        "Atrisinu savu uzdevumu un vērtēju, vai atbilde ir saprātīga.",
        "Izvērtēju klasesbiedra uzdevumu pēc kritērijiem.",
    ]),

    Majas([
        "Uzraksti divus uzdevumus: vienu vienkāršu, otru ar divām darbībām.",
        "Iedod tos mājiniekiem un salīdzini atbildes.",
        "Pārlasi visu tematu un atzīmē, kas vēl jāatkārto pirms pārbaudes "
        "darba.",
    ], ievads="Šī ir pēdējā stunda pirms pārbaudes darba - atkārto to, kas "
              "vēl nav drošs."),
]
