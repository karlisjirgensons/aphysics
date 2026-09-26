# -*- coding: utf-8 -*-
"""3. klase, 59. stunda: «Ko nozīmē samazināt vienādu skaitu reižu?»

Mēroga jēdziens bez vārda «mērogs». Galvenais te ir vārds *vienādu*: ja vienu
malu samazina 10, bet otru 5 reizes, figūra sagrozās. Stunda to parāda ar
diviem zīmējumiem, no kuriem otrais ir acīmredzami nepareizs.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         figura)

TEMA = "Ko nozīmē samazināt vienādu skaitu reižu?"

MERKIS = ("Skaidrosim, ka plānā visi lielumi samazināti vienādu skaitu "
          "reižu, un pārbaudīsim to aprēķinos.")

SATURS = [
    Sakums("Kāpēc šis plāns izskatās greizs?",
           zimejums=figura([(0, 0), (10, 0), (10, 2), (0, 2)],
                           [(5, -0.6, "10"), (10.8, 1, "2")],
                           "garums : 1, platums : 3"),
           paraksts="Šeit garums samazināts 1 reizi, bet platums 3 reizes.",
           fakti=["Plānā visi izmēri jāsamazina vienādu skaitu reižu.",
                  "Ja nav vienādi, telpas forma sagrozās."]),

    Doma("Samazinājumam jābūt vienam visiem izmēriem",
         "Ja katru garumu dala ar vienu un to pašu skaitli, forma saglabājas.",
         soli=[
             "Izvēlies samazinājumu - piemēram, 100 reizes.",
             "Izdali ar to katru izmēru.",
             "Pārbaudi, vai proporcijas saglabājas.",
             "Uzraksti pie plāna, cik reižu samazināji.",
         ],
         pieze="Ja telpa ir 8 m un 4 m, tad plānā tai jāpaliek divreiz "
               "garākai nekā platai - lai kādu samazinājumu izvēlētos."),

    Slidnis("Viena telpa, trīs samazinājumi",
            soli=[
                {"v": "800 cm x 400 cm",
                 "teksts": "Īstie izmēri - telpa 8 m x 4 m.", "josla": 100},
                {"v": "80 cm x 40 cm",
                 "teksts": "Samazināts 10 reizes - vēl par lielu lapai.",
                 "josla": 60},
                {"v": "16 cm x 8 cm",
                 "teksts": "Samazināts 50 reizes - der A4 lapai.",
                 "josla": 25},
                {"v": "8 cm x 4 cm",
                 "teksts": "Samazināts 100 reizes - der burtnīcai.",
                 "josla": 12},
            ],
            ievads="Katrā solī abi izmēri samazināti vienādi, tāpēc forma "
                   "nemainās."),

    Paraugs("Cik liela telpa ir plānā?",
            uzd="Telpa ir 600 cm un 300 cm. Samazini to 100 reizes.",
            soli=[
                ("600 : 100 = 6",
                 "Garums plānā ir 6 cm."),
                ("300 : 100 = 3",
                 "Platums plānā ir 3 cm."),
                ("6 cm un 3 cm",
                 "Pārbaude: telpa bija divreiz garāka nekā plata - plānā arī."),
            ],
            atbilde="6 cm un 3 cm"),

    Ievadi("Samazini 100 reizes", [
        {"jaut": "800 cm samazina 100 reizes. Cik centimetru?",
         "atb": ["8"], "padoms": "Noņem divas nulles."},
        {"jaut": "450 cm samazina 100 reizes. Cik centimetru?",
         "atb": ["4,5", "4.5"], "padoms": "450 : 100."},
        {"jaut": "1200 cm samazina 100 reizes. Cik centimetru?",
         "atb": ["12"], "padoms": "Noņem divas nulles."},
        {"jaut": "700 cm samazina 10 reizes. Cik centimetru?",
         "atb": ["70"], "padoms": "Noņem vienu nulli."},
        {"jaut": "Plānā 5 cm, samazinājums 100 reizes. Cik centimetru ir "
                 "telpā?",
         "atb": ["500"], "padoms": "5 · 100."},
        {"jaut": "Plānā 9 cm, samazinājums 50 reizes. Cik centimetru ir "
                 "telpā?",
         "atb": ["450"], "padoms": "9 · 50."},
    ], pamats=4),

    Zimejums("Pareizs samazinājums",
             figura([(0, 0), (8, 0), (8, 4), (0, 4)],
                    [(4, -0.6, "8 cm"), (8.8, 2, "4 cm")],
                    "telpa 8 m x 4 m, samazināta 100 reizes"),
             paskaidro="Telpa bija divreiz garāka nekā plata, un plānā tā ir "
                       "tāda pati.",
             ievads="Salīdzini šo ar stundas sākuma zīmējumu."),

    Varianti("Kurš plāns ir pareizs?", [
        {"jaut": "Telpa 10 m x 5 m. Kurš plāns ir pareizs?",
         "opcijas": ["10 cm x 5 cm", "10 cm x 2 cm", "5 cm x 5 cm",
                     "10 cm x 10 cm"],
         "pareizi": 0, "padoms": "Abi izmēri samazināti 100 reizes."},
        {"jaut": "Kas notiek, ja malas samazina dažādi?",
         "opcijas": ["Forma sagrozās", "Nekas", "Plāns kļūst precīzāks",
                     "Plāns kļūst lielāks"],
         "pareizi": 0, "padoms": "Proporcijas vairs nesakrīt."},
        {"jaut": "Telpa 12 m gara. Plānā tā ir 6 cm. Cik reižu samazināts?",
         "opcijas": ["200", "100", "50", "2"],
         "pareizi": 0, "padoms": "1200 cm : 6 cm."},
        {"jaut": "Kāpēc pie plāna raksta samazinājumu?",
         "opcijas": ["Lai varētu izrēķināt īstos izmērus",
                     "Lai plāns izskatītos nopietnāks",
                     "Lai atcerētos, kurš zīmēja", "Nav vajadzīgs"],
         "pareizi": 0, "padoms": "Bez tā plāns nepasaka izmērus."},
    ], pamats=4),

    Pasaule("Cik liela ir sporta zāle plānā?",
            Ievadi("", [
                {"jaut": "Sporta zāle ir 2400 cm gara. Cik centimetru tā ir "
                         "plānā, ja samazina 100 reizes?",
                 "atb": ["24"], "padoms": "2400 : 100."},
                {"jaut": "Zāle ir 1200 cm plata. Cik centimetru plānā?",
                 "atb": ["12"], "padoms": "1200 : 100."},
                {"jaut": "Cik centimetru ir plāna perimetrs?",
                 "atb": ["72"], "padoms": "2 · (24 + 12)."},
                {"jaut": "Cik metru ir zāles perimetrs?",
                 "atb": ["72"], "padoms": "Tas pats skaitlis metros."},
            ]),
            pavediens="skola",
            konteksts="Skolas plānā sporta zāle ir lielākā telpa - un tieši "
                      "tā nosaka, cik reižu jāsamazina viss pārējais.",
            kapec="Samazinājumu izvēlas pēc lielākā objekta, kas jāietilpina "
                  "lapā."),

    Kopsavilkums([
        "Zinu, ka plānā visi izmēri samazināti vienādu skaitu reižu.",
        "Izrēķinu plāna izmērus, dalot īstos izmērus ar samazinājumu.",
        "Atrodu īstos izmērus, reizinot plāna izmērus ar samazinājumu.",
        "Pamanu plānu, kurā proporcijas ir sagrozītas.",
    ]),

    Majas([
        "Izmēri savu istabu un izrēķini tās izmērus, samazinot 100 reizes.",
        "Uzzīmē šo taisnstūri burtnīcā.",
        "Pārbaudi, vai plānā istaba ir tikpat reižu garāka nekā plata.",
    ]),
]
