# -*- coding: utf-8 -*-
"""3. klase, 34. stunda: «Ko es jau protu un ko vēl ne?»

Jauna temata pirmā stunda sākas ar inventarizāciju: skolēns pats izmēģina
katru no četrām darbībām un atzīmē, kura vieta klibo. No šī saraksta 36.
stundā izaugs treniņu plāns, tāpēc te svarīgs ir godīgums, ne rezultāts.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Ko es jau protu un ko vēl ne?"

MERKIS = ("Novērtēsim savas rēķināšanas prasmes ar piemēriem un formulēsim "
          "mērķi to pilnveidei.")

SATURS = [
    Sakums("Kurā vietā tavs rēķins apstājas?",
           zimejums=restis([["+", "−", "·", ":"],
                            ["", "", "", ""]],
                           "četras darbības - kura ir grūtākā?"),
           paraksts="Katram ir sava vājākā aile. Svarīgi to zināt.",
           fakti=["Sportists zina savu vājāko vietu - tāpēc viņš aug.",
                  "Rēķinot arī: vispirms atrod, kur apstājas."]),

    Doma("Vispirms izmēri, tad trenē",
         "Prasmi nevar uzlabot, kamēr nezini, kura tieši prasme klibo.",
         soli=[
             "Izrēķini pa vienam piemēram no katras darbības.",
             "Atzīmē, kurš prasīja visilgāk.",
             "Atzīmē, kurā kļūdījies.",
             "Uzraksti vienu teikumu: ko tieši gribi uzlabot.",
         ],
         pieze="Mērķis «gribu rēķināt labāk» nestrādā. Strādā mērķis «gribu "
               "bez kļūdām atņemt ar pāreju pāri desmitam»."),

    Paraugs("Kā formulēt savu mērķi?",
            uzd="Skolēns kļūdījās uzdevumos 62 − 28 un 71 − 34. Kāds ir viņa "
                "mērķis?",
            soli=[
                ("Abos ir atņemšana ar pāreju",
                 "Vispirms meklē, kas abām kļūdām ir kopīgs."),
                ("Reizināšanā un saskaitīšanā kļūdu nav",
                 "Tātad problēma nav visā rēķināšanā."),
                ("«Iemācīšos atņemt ar pāreju bez kļūdām»",
                 "Mērķis ir konkrēts, tāpēc to var arī sasniegt."),
            ],
            atbilde="atņemšana ar pāreju pāri desmitam"),

    Ievadi("Pašpārbaude: visas četras darbības", [
        {"jaut": "47 + 35 = ?", "atb": ["82"], "padoms": "40 + 30 un 7 + 5."},
        {"jaut": "62 − 28 = ?", "atb": ["34"], "padoms": "62 − 30 + 2."},
        {"jaut": "8 · 7 = ?", "atb": ["56"], "padoms": "49 + 7."},
        {"jaut": "72 : 8 = ?", "atb": ["9"], "padoms": "8 · 9 = 72."},
        {"jaut": "56 + 27 = ?", "atb": ["83"], "padoms": "56 + 30 − 3."},
        {"jaut": "91 − 45 = ?", "atb": ["46"], "padoms": "91 − 50 + 5."},
        {"jaut": "6 · 9 = ?", "atb": ["54"], "padoms": "60 − 6."},
        {"jaut": "63 : 7 = ?", "atb": ["9"], "padoms": "7 · 9 = 63."},
    ], pamats=8,
        ievads="Izdari visus astoņus un atzīmē, kuri prasīja visilgāk."),

    Petijums("Uzraksti savu prasmju karti",
             vajag="burtnīca un zīmulis",
             soli=[
                 "Uzzīmē tabulu ar četrām ailēm: +, −, · un :.",
                 "Katrā ailē ieraksti, cik uzdevumu izdarīji pareizi.",
                 "Apvelc aili ar vismazāko skaitli.",
                 "Uzraksti vienu teikumu par to, ko gribi uzlabot.",
             ],
             secinajums="Šī karte ir sākums - pēc divām nedēļām to "
                        "aizpildīsi vēlreiz un salīdzināsi."),

    Zimejums("Prasmju karte",
             restis([["+", "−", "·", ":"],
                     [2, 1, 2, 2]],
                    "pareizi no diviem"),
             paskaidro="Šim skolēnam vājākā aile ir atņemšana - tātad "
                       "treniņš sākas tur.",
             ievads="Tā izskatās aizpildīta karte."),

    Varianti("Kurš mērķis ir labs?", [
        {"jaut": "Kurš mērķis ir vislabāk formulēts?",
         "opcijas": ["Iemācīšos atņemt ar pāreju",
                     "Būšu labāks matemātikā", "Centīšos vairāk",
                     "Nekļūdīšos nekad"],
         "pareizi": 0, "padoms": "Labs mērķis ir konkrēts un pārbaudāms."},
        {"jaut": "Ko darīt vispirms, ja divas kļūdas ir vienā darbībā?",
         "opcijas": ["Trenēt tieši šo darbību", "Trenēt visas darbības",
                     "Trenēt reizināšanas tabulu", "Neko"],
         "pareizi": 0, "padoms": "Kļūdas norāda uz vietu."},
        {"jaut": "Kāpēc pašpārbaudei nav atzīmes?",
         "opcijas": ["Tā rāda, ko trenēt, nevis vērtē",
                     "Tā ir par vieglu", "Tā nav svarīga",
                     "Atzīmi liek vēlāk"],
         "pareizi": 0, "padoms": "Šī ir karte, ne vērtējums."},
        {"jaut": "Kā pārbaudīt, vai mērķis sasniegts?",
         "opcijas": ["Aizpildīt karti vēlreiz pēc divām nedēļām",
                     "Pajautāt draugam", "Izlasīt grāmatu",
                     "Nekā nevar pārbaudīt"],
         "pareizi": 0, "padoms": "To pašu mēru lieto divas reizes."},
    ], pamats=4),

    Pasaule("Kā treneris atrod vājo vietu?",
            Ievadi("", [
                {"jaut": "Skrējējs noskrēja 4 apļus pa 400 m. Cik metru?",
                 "atb": ["1600"], "padoms": "4 · 400."},
                {"jaut": "Viņa mērķis ir 2000 m. Cik metru vēl trūkst?",
                 "atb": ["400"], "padoms": "2000 − 1600."},
                {"jaut": "Otrs skrējējs noskrēja 7 apļus. Cik metru?",
                 "atb": ["2800"], "padoms": "7 · 400."},
                {"jaut": "Par cik metriem vairāk noskrēja otrais?",
                 "atb": ["1200"], "padoms": "2800 − 1600."},
            ]),
            pavediens="sports",
            konteksts="Treneris vispirms nomēra rezultātu un tikai tad "
                      "izdomā, ko trenēt - gluži kā ar prasmju karti.",
            kapec="Bez mērījuma nevar pateikt, vai treniņš palīdzēja."),

    Kopsavilkums([
        "Novērtēju savas prasmes visās četrās darbībās.",
        "Atrodu, kura darbība man padodas vissliktāk.",
        "Formulēju konkrētu un pārbaudāmu mērķi.",
        "Zinu, ka to pašu mēru izmantošu arī pēc treniņa.",
    ]),

    Majas([
        "Aizpildi savu prasmju karti un parādi to mājiniekiem.",
        "Uzraksti savu mērķi vienā teikumā un pielīmē to pie burtnīcas.",
        "Izdomā piecus uzdevumus tajā darbībā, kas tev padodas vissliktāk.",
    ]),
]
