# -*- coding: utf-8 -*-
"""6. klase, 153. stunda: «Kādi skaitļi mums ir?»

Jauns mikrotemats sākas ar atskatu. Sešu gadu laikā skaitļu klāsts ir audzis
pakāpeniski: naturālie, nulle, daļas, decimāldaļas, negatīvie. Šī stunda tos
saliek vienā attēlā, pirms nākamajā tos nosauc vārdā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kādi skaitļi mums ir?"

MERKIS = ("Sistematizēsim zināmos skaitļu veidus un to savstarpējo "
          "saistību.")

SATURS = [
    Sakums("Katrs gads pievienoja jaunus skaitļus",
           zimejums=taisne(-3, 3, 1, [(-2.5, "−2,5"), (-1, "−1"),
                                      (0.5, "1/2"), (2, "2")]),
           paraksts="Uz vienas taisnes satiekas visi skaitļu veidi, ko esam "
                    "iepazinuši.",
           fakti=["Naturālie skaitļi: 1; 2; 3 un tālāk.",
                  "Veselie: naturālie, nulle un negatīvie.",
                  "Daļskaitļi aizpilda vietas starp veselajiem."]),

    Doma("Katra jauna kopa ietver iepriekšējo",
         "Skaitļu veidi veido kāpnes: naturālie ietilpst veselajos, veselie - "
         "daļskaitļos; katrs jauns solis pievieno to, kā iepriekš trūka.",
         soli=[
             "Sāc ar naturālajiem skaitļiem - tie skaita priekšmetus.",
             "Pievieno nulli - tā apzīmē tukšumu.",
             "Pievieno negatīvos - tie apzīmē pretējo virzienu.",
             "Pievieno daļas - tās aizpilda vietas starp veselajiem.",
             "Pārbaudi: katrs iepriekšējais veids ietilpst nākamajā.",
         ],
         pieze="Skaitlis 3 ir gan naturāls, gan vesels, gan daļskaitlis - "
               "to var uzrakstīt kā {3|1} vai 3,0. Kopas nav savstarpēji "
               "izslēdzošas."),

    Paraugs("Kurai kopai pieder skaitlis?",
            uzd="Kādi ir skaitļi 5; −2; {1|2} un 0?",
            soli=[
                ("5 ir naturāls, vesels un daļskaitlis",
                 "Naturālie ietilpst visos pārējos."),
                ("−2 ir vesels un daļskaitlis, bet nav naturāls",
                 "Negatīvs."),
                ("{1|2} ir tikai daļskaitlis",
                 "Nav vesels."),
                ("0 ir vesels un daļskaitlis, bet nav naturāls",
                 "Nulle nav naturāls skaitlis."),
            ],
            atbilde="katrs pieder vairākām kopām"),

    Ievadi("Nosaki skaitļa veidu", [
        {"jaut": "Vai 5 ir naturāls skaitlis? Raksti «jā» vai «nē».",
         "atb": ["jā", "ja"], "padoms": "Skaita priekšmetus."},
        {"jaut": "Vai −2 ir naturāls skaitlis?",
         "atb": ["nē", "ne"], "padoms": "Naturālie ir pozitīvi."},
        {"jaut": "Vai −2 ir vesels skaitlis?",
         "atb": ["jā", "ja"], "padoms": "Veselie ietver negatīvos."},
        {"jaut": "Vai {1|2} ir vesels skaitlis?",
         "atb": ["nē", "ne"], "padoms": "Starp veselajiem."},
        {"jaut": "Vai 0 ir vesels skaitlis?",
         "atb": ["jā", "ja"], "padoms": "Nulle ir veselo vidū."},
        {"jaut": "Cik veselu skaitļu ir starp −2 un 2, ieskaitot galus?",
         "atb": ["5"], "padoms": "−2; −1; 0; 1; 2."},
    ], pamats=4),

    Varianti("Kurai kopai pieder?", [
        {"jaut": "Naturālie skaitļi ir...",
         "opcijas": ["1; 2; 3 un tālāk", "visi veselie",
                     "arī nulle", "arī negatīvie"],
         "pareizi": 0,
         "padoms": "Tie skaita priekšmetus."},
        {"jaut": "Veselie skaitļi ietver...",
         "opcijas": ["naturālos, nulli un negatīvos",
                     "tikai pozitīvos", "arī daļas",
                     "tikai negatīvos"],
         "pareizi": 0,
         "padoms": "Visi bez daļām."},
        {"jaut": "Skaitlis 3 ir...",
         "opcijas": ["gan naturāls, gan vesels", "tikai naturāls",
                     "tikai vesels", "tikai daļskaitlis"],
         "pareizi": 0,
         "padoms": "Kopas ietver viena otru."},
        {"jaut": "Kurš skaitlis nav vesels?",
         "opcijas": ["0,5", "−7", "0", "12"],
         "pareizi": 0,
         "padoms": "Starp veselajiem."},
    ], pamats=4),

    Pasaule("Kāds skaitlis te der?",
            Ievadi("", [
                {"jaut": "Skolēnu skaits klasē. Vai tas var būt daļskaitlis? "
                         "Raksti «jā» vai «nē».",
                 "atb": ["nē", "ne"], "padoms": "Cilvēkus skaita veselos."},
                {"jaut": "Temperatūra. Vai tā var būt negatīva?",
                 "atb": ["jā", "ja"], "padoms": "Zem nulles."},
                {"jaut": "Auguma garums metros. Vai tas var būt daļskaitlis?",
                 "atb": ["jā", "ja"], "padoms": "1,65 m."},
                {"jaut": "Stāvu numurs. Vai tas var būt negatīvs?",
                 "atb": ["jā", "ja"], "padoms": "Pagrabstāvi."},
            ]),
            pavediens="skola",
            konteksts="Katram lielumam der savs skaitļu veids - un izvēle "
                      "nav brīva, to nosaka pati situācija.",
            kapec="Skaitļa veids pasaka, kādas atbildes vispār ir "
                  "iespējamas."),

    Zimejums("Visi veidi uz vienas taisnes",
             taisne(-4, 4, 1, [(-3, "vesels"), (-1.5, "daļa"), (0, "nulle"),
                               (2, "naturāls")]),
             paskaidro="Uz skaitļu taisnes visi veidi stāv blakus - "
                       "atšķirība ir tikai tajā, kā tos pieraksta.",
             ievads="Viena taisne, četri skaitļu veidi."),

    Kopsavilkums([
        "Nosaucu zināmos skaitļu veidus.",
        "Zinu, ka naturālie ietilpst veselajos, veselie - daļskaitļos.",
        "Nosaku, kurai kopai pieder konkrēts skaitlis.",
        "Izvēlos skaitļa veidu, kas der konkrētajai situācijai.",
    ]),

    Majas([
        "Pieraksti pa trim naturāliem, veseliem un daļskaitļiem.",
        "Atrodi skaitli, kas pieder visām trim kopām.",
        "Pieraksti lielumu, kuram der tikai naturāli skaitļi.",
    ]),
]
