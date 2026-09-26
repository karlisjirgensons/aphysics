# -*- coding: utf-8 -*-
"""3. klase, 68. stunda: «Kādu samazinājumu izvēlēties?»

Praktiskā darba pirmais lēmums. Samazinājumu neizvēlas pēc nejaušības: tas
jāizvēlas tā, lai lielākais izmērs ietilptu lapā un mazākais vēl būtu
saskatāms. Skolēns salīdzina divus variantus un pamato izvēli ar skaitļiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kādu samazinājumu izvēlēties?"

MERKIS = ("Salīdzināsim, kā izmēri izskatās, samazinot 10 un 20 reizes, un "
          "izvēlēsimies piemērotāko.")

SATURS = [
    Sakums("Kurš samazinājums ietilps lapā?",
           zimejums=restis([["telpa", ": 10", ": 20", ": 50"],
                            ["800 cm", "80 cm", "40 cm", "16 cm"],
                            ["600 cm", "60 cm", "30 cm", "12 cm"]],
                           "trīs varianti"),
           paraksts="A4 lapa ir apmēram 29 cm gara - ietilpst tikai pēdējais.",
           fakti=["A4 lapa ir 21 cm plata un 29 cm gara.",
                  "Samazinājumu izvēlas pēc lielākā izmēra."]),

    Doma("Samazinājumu izvēlas pēc lielākā izmēra",
         "Lielākajam izmēram jāietilpst lapā, un mazākajam vēl jābūt "
         "saskatāmam.",
         soli=[
             "Atrodi telpas lielāko izmēru.",
             "Izmēģini samazinājumu: izdali to ar 10, 20 vai 50.",
             "Salīdzini rezultātu ar lapas izmēru.",
             "Izvēlies mazāko samazinājumu, kas vēl ietilpst.",
         ],
         pieze="Jo mazāks samazinājums, jo lielāks plāns un jo vairāk "
               "sīkumu tajā redzams - tāpēc neņem lielāku, nekā vajag."),

    Paraugs("Kurš samazinājums der klasei?",
            uzd="Klase ir 800 cm un 600 cm. Kurš samazinājums der A4 lapai?",
            soli=[
                ("800 : 10 = 80 cm",
                 "Par lielu - lapa ir tikai 29 cm gara."),
                ("800 : 20 = 40 cm",
                 "Joprojām par lielu."),
                ("800 : 50 = 16 cm; 600 : 50 = 12 cm",
                 "Abi ietilpst lapā ar rezervi."),
            ],
            atbilde="samazinājums 50 reizes"),

    Petijums("Izvēlies samazinājumu savai klasei",
             vajag="klases mērījumi, A4 lapa un lineāls",
             soli=[
                 "Paņem savas klases izmērus no mērījumu tabulas.",
                 "Izdali tos ar 10, 20 un 50.",
                 "Salīdzini katru rezultātu ar lapas izmēriem.",
                 "Izvēlies piemērotāko un pieraksti to uz lapas.",
             ],
             secinajums="Samazinājumu vienmēr pieraksta pie plāna - citādi "
                        "plāns nepasaka īstos izmērus."),

    Ievadi("Izrēķini plāna izmērus", [
        {"jaut": "800 cm samazina 50 reizes. Cik centimetru?",
         "atb": ["16"], "padoms": "800 : 50."},
        {"jaut": "600 cm samazina 50 reizes. Cik centimetru?",
         "atb": ["12"], "padoms": "600 : 50."},
        {"jaut": "400 cm samazina 20 reizes. Cik centimetru?",
         "atb": ["20"], "padoms": "400 : 20."},
        {"jaut": "900 cm samazina 100 reizes. Cik centimetru?",
         "atb": ["9"], "padoms": "Noņem divas nulles."},
        {"jaut": "Plānā 15 cm, samazinājums 50 reizes. Cik centimetru telpā?",
         "atb": ["750"], "padoms": "15 · 50."},
        {"jaut": "Plānā 7 cm, samazinājums 100 reizes. Cik centimetru telpā?",
         "atb": ["700"], "padoms": "7 · 100."},
    ], pamats=4),

    Zimejums("Divi plāni vienai klasei",
             restis([["samazinājums", "garums", "platums", "der?"],
                     [20, "40 cm", "30 cm", "nē"],
                     [50, "16 cm", "12 cm", "jā"]],
                    "A4 lapa: 21 x 29 cm"),
             paskaidro="Pirmais plāns būtu skaistāks, bet lapā neietilptu.",
             ievads="Salīdzini abas rindas ar lapas izmēriem."),

    Varianti("Kurš samazinājums der?", [
        {"jaut": "Telpa 1000 cm gara. Kurš samazinājums der A4 lapai?",
         "opcijas": ["100 reizes", "10 reizes", "20 reizes", "2 reizes"],
         "pareizi": 0, "padoms": "1000 : 100 = 10 cm."},
        {"jaut": "Kas notiek, ja samazinājums ir par lielu?",
         "opcijas": ["Plāns kļūst sīks un nesalasāms",
                     "Plāns neietilpst lapā", "Forma sagrozās",
                     "Nekas"],
         "pareizi": 0, "padoms": "Sīkumus vairs nevar atzīmēt."},
        {"jaut": "Telpa 500 cm, plānā 10 cm. Cik reižu samazināts?",
         "opcijas": ["50", "10", "100", "5"],
         "pareizi": 0, "padoms": "500 : 10."},
        {"jaut": "Ko pieraksta pie gatava plāna?",
         "opcijas": ["Samazinājumu", "Datumu", "Krāsu", "Lapas izmēru"],
         "pareizi": 0, "padoms": "Bez tā plāns nepasaka izmērus."},
    ], pamats=4),

    Pasaule("Kāds mērogs ir kartei?",
            Ievadi("", [
                {"jaut": "Kartē 1 cm ir 1 km. Cik kilometru ir 8 cm?",
                 "atb": ["8"], "padoms": "Katram centimetram viens "
                                         "kilometrs."},
                {"jaut": "Cik centimetru kartē ir 25 km?",
                 "atb": ["25"], "padoms": "Tas pats skaitlis."},
                {"jaut": "Citā kartē 1 cm ir 10 km. Cik kilometru ir 7 cm?",
                 "atb": ["70"], "padoms": "7 · 10."},
                {"jaut": "Cik centimetru šajā kartē ir 300 km?",
                 "atb": ["30"], "padoms": "300 : 10."},
            ]),
            pavediens="celojums",
            konteksts="Kartes mērogs ir tas pats samazinājums - tikai "
                      "pierakstīts kilometros uz centimetru.",
            kapec="No mēroga atkarīgs, vai kartē redzama viena pilsēta vai "
                  "visa valsts."),

    Kopsavilkums([
        "Izvēlos samazinājumu pēc lielākā izmēra.",
        "Salīdzinu vairākus samazinājumus un pamatoju izvēli.",
        "Izrēķinu plāna izmērus un īstos izmērus.",
        "Zinu, ka samazinājumu vienmēr pieraksta pie plāna.",
    ]),

    Majas([
        "Izvēlies samazinājumu savai istabai un pamato izvēli.",
        "Izrēķini, cik liela istaba būs plānā.",
        "Atrodi kādā kartē tās mērogu.",
    ]),
]
