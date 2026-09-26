# -*- coding: utf-8 -*-
"""3. klase, 36. stunda: «Kā izveidot savu treniņu plānu?»

34. stundā skolēns atrada savu vājo vietu, šeit viņš uzraksta, ko ar to darīs.
Plāns ir īss un pārbaudāms: ko, cik bieži, cik ilgi un kad pārbaudīsim. Tas
pats plāna veids vēlāk noder jebkuram darbam ar termiņu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         kolonnas)

TEMA = "Kā izveidot savu treniņu plānu?"

MERKIS = ("Sastādīsim rīcības plānu prasmju pilnveidei un vienosimies par "
          "pārbaudes laiku.")

SATURS = [
    Sakums("Kāpēc «trenēšos vairāk» nestrādā?",
           zimejums=kolonnas([("pirmdien", 5), ("otrdien", 5),
                              ("trešdien", 5), ("ceturtdien", 5),
                              ("piektdien", 5)], " min"),
           paraksts="Piecas reizes pa 5 minūtēm ir 25 minūtes nedēļā.",
           fakti=["Plānā jābūt skaitļiem: cik bieži un cik ilgi.",
                  "Plānā jābūt datumam, kad pārbaudīsim rezultātu."]),

    Doma("Plānā ir četras lietas",
         "Ko trenēšu, cik bieži, cik ilgi un kad pārbaudīšu - bez kāda no "
         "šiem plāns paliek vēlējums.",
         soli=[
             "Uzraksti, kuru prasmi trenēsi.",
             "Izvēlies dienas: labāk īsi un bieži nekā ilgi un reti.",
             "Nosaki laiku vienai reizei - 5 vai 10 minūtes.",
             "Pieraksti datumu, kad aizpildīsi prasmju karti vēlreiz.",
         ],
         pieze="Plāns, kuru nevar izpildīt, ir sliktāks par mazu plānu, "
               "kuru izpildīt var. Sāc ar to, kas noteikti sanāks."),

    Paraugs("Cik minūšu sanāks divās nedēļās?",
            uzd="Plāns: 5 minūtes dienā, 5 dienas nedēļā. Cik minūšu sanāks "
                "divās nedēļās?",
            soli=[
                ("5 · 5 = 25",
                 "Tik minūšu sanāk vienā nedēļā."),
                ("25 · 2 = 50",
                 "Divās nedēļās - divreiz vairāk."),
                ("50 minūtes",
                 "Gandrīz stunda, un katra reize bija tikai 5 minūtes."),
            ],
            atbilde="50 minūtes"),

    Petijums("Uzraksti savu plānu",
             vajag="burtnīca un kalendārs",
             soli=[
                 "Pārlasi savu mērķi no 34. stundas.",
                 "Uzraksti, kuras dienas trenēsies un cik ilgi.",
                 "Uzraksti, ko tieši darīsi - kartītes, piemēri vai lietotne.",
                 "Atzīmē kalendārā datumu, kad pārbaudīsi rezultātu.",
             ],
             secinajums="Plāns ir gatavs tad, kad tajā ir gan darbs, gan "
                        "diena, kurā pārbaudīsi, vai tas palīdzēja."),

    Ievadi("Izrēķini savu plānu", [
        {"jaut": "10 minūtes dienā, 5 dienas nedēļā. Cik minūšu nedēļā?",
         "atb": ["50"], "padoms": "5 · 10."},
        {"jaut": "Cik minūšu sanāks 4 nedēļās?", "atb": ["200"],
         "padoms": "4 · 50."},
        {"jaut": "8 minūtes dienā, 6 dienas nedēļā. Cik minūšu nedēļā?",
         "atb": ["48"], "padoms": "6 · 8."},
        {"jaut": "Plānā 12 uzdevumi dienā, 7 dienas. Cik uzdevumu?",
         "atb": ["84"], "padoms": "7 · 12."},
        {"jaut": "Nedēļā jāizdara 60 uzdevumi, 5 dienās. Cik dienā?",
         "atb": ["12"], "padoms": "60 : 5."},
        {"jaut": "Nedēļā 90 minūtes, 6 dienās. Cik minūšu dienā?",
         "atb": ["15"], "padoms": "90 : 6."},
    ], pamats=4),

    Zimejums("Divi plāni, viens laiks",
             kolonnas([("5 min x 5 d.", 25), ("25 min x 1 d.", 25)]),
             paskaidro="Minūšu skaits vienāds, bet pirmais plāns atmiņai dod "
                       "daudz vairāk - jo atkārtojums ir biežāks.",
             ievads="Kurš no šiem plāniem strādā labāk?"),

    Varianti("Kurš plāns ir labāks?", [
        {"jaut": "Kurš plāns atmiņai der vislabāk?",
         "opcijas": ["5 min katru dienu", "25 min reizi nedēļā",
                     "1 stunda mēnesī", "2 stundas pirms PD"],
         "pareizi": 0, "padoms": "Biežums palīdz vairāk nekā garums."},
        {"jaut": "Kas plānā nedrīkst iztrūkt?",
         "opcijas": ["Pārbaudes datums", "Skolotāja paraksts",
                     "Krāsains vāks", "Draugu saraksts"],
         "pareizi": 0, "padoms": "Bez datuma nevar pateikt, vai izdevās."},
        {"jaut": "Plānā 6 minūtes dienā 7 dienas. Cik minūšu nedēļā?",
         "opcijas": ["42", "36", "13", "76"],
         "pareizi": 0, "padoms": "7 · 6."},
        {"jaut": "Ko darīt, ja plāns nesanāk trīs dienas pēc kārtas?",
         "opcijas": ["Padarīt plānu mazāku", "Atmest plānu",
                     "Padarīt plānu lielāku", "Neko nemainīt"],
         "pareizi": 0, "padoms": "Labāk mazs plāns, ko var izpildīt."},
    ], pamats=4),

    Pasaule("Kā gatavojas sportists?",
            Ievadi("", [
                {"jaut": "Treniņš ilgst 45 minūtes, 4 reizes nedēļā. Cik "
                         "minūšu nedēļā?",
                 "atb": ["180"], "padoms": "4 · 45."},
                {"jaut": "Cik minūšu sanāk 3 nedēļās?",
                 "atb": ["540"], "padoms": "3 · 180."},
                {"jaut": "Sportists grib nedēļā 240 minūtes. Cik minūšu "
                         "vienā treniņā, ja to ir 4?",
                 "atb": ["60"], "padoms": "240 : 4."},
                {"jaut": "Par cik minūtēm garāks būtu katrs treniņš?",
                 "atb": ["15"], "padoms": "60 − 45."},
            ]),
            pavediens="sports",
            konteksts="Sportista plānā ir tie paši četri jautājumi: ko, cik "
                      "bieži, cik ilgi un kad mēra rezultātu.",
            kapec="Ar skaitļiem plānu var pārbaudīt; bez tiem - tikai cerēt."),

    Kopsavilkums([
        "Sastādu savu treniņu plānu ar četrām daļām.",
        "Izrēķinu, cik laika plāns prasīs nedēļā un mēnesī.",
        "Zinu, ka biežums palīdz vairāk nekā garums.",
        "Vienojos par datumu, kad pārbaudīšu rezultātu.",
    ]),

    Majas([
        "Uzraksti savu plānu un parādi to mājiniekiem.",
        "Izrēķini, cik minūšu tas prasīs mēnesī.",
        "Atzīmē kalendārā pārbaudes dienu.",
    ]),
]
