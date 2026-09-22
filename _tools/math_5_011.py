# -*- coding: utf-8 -*-
"""5. klase, 11. stunda: «Kā lasīt svešu šifru?»

Mikrotemata pēdējā stunda. Ēģiptiešu pieraksts te ir nevis jauna viela, bet
uzdevums: sistēmu neviens neizstāsta, to jāizdomā pašam pēc dotajiem
piemēriem. Prasme, ko vērtē, ir spriedums - «es redzu likumsakarību, tāpēc
domāju, ka...».
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā lasīt svešu šifru?"

MERKIS = ("Mācīsimies izdomāt nezināmas pieraksta sistēmas likumu pēc "
          "dotajiem piemēriem un pamatot savu spriedumu.")

SATURS = [
    Sakums("Ko nozīmē šīs zīmes?",
           fakti=["∩∩▮▮ un ∩∩∩▮ - abi ir skaitļi.",
                  "Pirmais ir 22, otrais ir 31.",
                  "Ar ko tie atšķiras? No tā arī var izdomāt likumu."]),

    Doma("Likumu meklē, salīdzinot piemērus",
         "Ja divi pieraksti atšķiras ar vienu zīmi, tad tā zīme arī "
         "izskaidro starpību.",
         soli=[
             "Salīdzini divus piemērus, kuriem zināma vērtība.",
             "Atrodi, ar ko tie atšķiras.",
             "Izdari pieņēmumu par vienas zīmes vērtību.",
             "Pārbaudi pieņēmumu uz trešā piemēra.",
         ],
         pieze="Ēģiptē katrai zīmei bija sava vērtība, un zīmes vienkārši "
               "saskaitīja - kā romiešiem, tikai bez atņemšanas likuma."),

    Paraugs("Atšifrē sistēmu",
            uzd="Zināms: ▮ = 1 un ∩ = 10. Ko nozīmē ∩∩▮▮▮?",
            soli=[
                ("∩∩ = 10 + 10 = 20",
                 "Divas desmitu zīmes."),
                ("▮▮▮ = 1 + 1 + 1 = 3",
                 "Trīs vienu zīmes."),
                ("20 + 3 = 23",
                 "Zīmes vienkārši saskaita - vietas nozīmes šeit nav."),
            ],
            atbilde="∩∩▮▮▮ ir 23"),

    Ievadi("Izlasi ēģiptiešu skaitli", [
        {"jaut": "▮ = 1, ∩ = 10. Cik ir ∩▮▮?", "atb": ["12"],
         "padoms": "10 + 1 + 1."},
        {"jaut": "Cik ir ∩∩∩?", "atb": ["30"], "padoms": "Trīs desmiti."},
        {"jaut": "Cik ir ∩∩∩∩▮?", "atb": ["41"], "padoms": "40 + 1."},
        {"jaut": "Ja ⟌ = 100, cik ir ⟌∩∩▮?", "atb": ["121"],
         "padoms": "100 + 20 + 1."},
        {"jaut": "Cik zīmju vajag, lai uzrakstītu 33?", "atb": ["6"],
         "padoms": "Trīs desmiti un trīs vieni."},
        {"jaut": "Cik zīmju vajag, lai uzrakstītu 99?", "atb": ["18"],
         "padoms": "Deviņi desmiti un deviņi vieni."},
    ], pamats=4,
        ievads="Zīmes vienkārši saskaita."),

    Varianti("Ko var secināt?", [
        {"jaut": "Ēģiptiešu pierakstā zīmju secība nemaina vērtību. Ko tas "
                 "nozīmē?",
         "opcijas": ["Vietas nozīmes nav", "Sistēmā ir nulle",
                     "Zīmes jāraksta no labās", "Zīmes var atņemt"],
         "pareizi": 0,
         "padoms": "Salīdzini ar mūsu pierakstu, kur 12 un 21 ir dažādi."},
        {"jaut": "Kāpēc šādā sistēmā lielus skaitļus rakstīt ir neērti?",
         "opcijas": ["Vajag ļoti daudz zīmju",
                     "Nav pietiekami daudz ciparu",
                     "Nevar uzrakstīt pāra skaitļus",
                     "Zīmes nevar atkārtot"],
         "pareizi": 0,
         "padoms": "Padomā, cik zīmju vajag skaitlim 99."},
        {"jaut": "Kura sistēma ēģiptiešu pierakstam ir vislīdzīgākā?",
         "opcijas": ["Romiešu", "Binārā", "Decimālā", "Neviena"],
         "pareizi": 0,
         "padoms": "Abās zīmēm ir sava vērtība un tās saskaita."},
        {"jaut": "Ja sistēmā parādītos zīme, kas nozīmē 1000, kas kļūtu "
                 "vieglāk?",
         "opcijas": ["Rakstīt lielus skaitļus", "Rakstīt mazus skaitļus",
                     "Saskaitīt", "Nekas nemainītos"],
         "pareizi": 0,
         "padoms": "Mazāk zīmju vienam skaitlim."},
    ], pamats=4),

    Pasaule("Kā atšifrēt failu?",
            Ievadi("", [
                {"jaut": "Zīme A = 5, zīme B = 20. Cik ir BBA?",
                 "atb": ["45"], "padoms": "20 + 20 + 5."},
                {"jaut": "Cik ir AAA?", "atb": ["15"], "padoms": "5 + 5 + 5."},
                {"jaut": "Cik zīmju vajag skaitlim 50?", "atb": ["4"],
                 "padoms": "Divas B un divas A: 20 + 20 + 5 + 5."},
                {"jaut": "Ja pievieno zīmi C = 100, cik ir CBA?",
                 "atb": ["125"], "padoms": "100 + 20 + 5."},
            ]),
            pavediens="dati",
            konteksts="Datu atšifrēšana sākas tāpat: salīdzina piemērus, kuru "
                      "nozīme jau zināma.",
            kapec="Likumu atrod, salīdzinot: ar ko divi pieraksti atšķiras."),

    Kopsavilkums([
        "Izdomāju nezināmas pieraksta sistēmas likumu pēc dotajiem piemēriem.",
        "Pārbaudu savu pieņēmumu uz vēl viena piemēra.",
        "Pamatoju spriedumu: kāpēc domāju, ka zīme nozīmē tieši to.",
    ]),

    Majas([
        "Izdomā savu skaitļu pieraksta sistēmu ar trim zīmēm un uzraksti tajā "
        "savu vecumu.",
        "Iedod to draugam ar trim piemēriem un paskaties, vai viņš atmin "
        "likumu.",
        "Padomā, kura no visām redzētajām sistēmām ir ērtākā un kāpēc.",
    ]),
]
