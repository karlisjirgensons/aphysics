# -*- coding: utf-8 -*-
"""3. klase, 19. stunda: «Ko dara ar 1 un 0?»

Īpašie gadījumi, kurus tabula neietver. Trīs no tiem ir vienkārši, ceturtais -
dalīšana ar nulli - ir tas, ko nedrīkst; un skolēnam to neiemāca ar aizliegumu,
bet ar jautājumu, uz kuru nav atbildes.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Ko dara ar 1 un 0?"

MERKIS = ("Secināsim un lietosim sakarības 1 · a = a, a : 1 = a un "
          "0 · a = 0, un noskaidrosim, kāpēc ar 0 dalīt nevar.")

SATURS = [
    Sakums("Kāpēc kalkulators uz 5 : 0 atbild ar kļūdu?",
           zimejums=restis([["1 · a = a", "a : 1 = a"],
                            ["0 · a = 0", "a : 0 = ?"]],
                           "trīs sakarības un viens jautājums"),
           paraksts="Trīs no šiem četriem ir viegli. Ceturtais nav iespējams.",
           fakti=["Reizinot ar 1, skaitlis nemainās.",
                  "Reizinot ar 0, vienmēr iznāk 0.",
                  "Dalīt ar 0 nevar - tādas atbildes nav."]),

    Doma("Viens neko nemaina, nulle visu nonulle",
         "1 · a = a, a : 1 = a, a : a = 1, 0 · a = 0 - un ar 0 dalīt nevar.",
         soli=[
             "Viena grupa pa a - tas ir tas pats a.",
             "Sadalīt vienā daļā nozīmē neko nedalīt: a : 1 = a.",
             "Nevienas grupas - tātad nekā: 0 · a = 0.",
             "Bet «cik nullīšu grupu ir 5?» - uz šo atbildes nav.",
         ],
         pieze="Dalīšana ir jautājums «cik reižu?». Ja katrā grupā ir 0, tad "
               "no tām nekad nesanāks 5 - lai cik daudz grupu ņemtu."),

    Paraugs("Kāpēc 5 : 0 nav atbildes?",
            uzd="Paskaidro, kāpēc 5 : 0 aprēķināt nevar.",
            soli=[
                ("5 : 0 = ? nozīmē ? · 0 = 5",
                 "Dalījumu pārraksta kā reizinājumu ar trūkstošu skaitli."),
                ("Jebkurš skaitlis reiz 0 dod 0",
                 "0, 10, 100 - visi reiz nulli dod nulli."),
                ("Neviens skaitlis nedod 5",
                 "Tātad trūkstošā skaitļa nav; dalīt ar 0 nevar."),
            ],
            atbilde="atbildes nav - dalīt ar nulli nevar"),

    Ievadi("Īpašie gadījumi", [
        {"jaut": "1 · 47 = ?", "atb": ["47"], "padoms": "Viens neko nemaina."},
        {"jaut": "63 : 1 = ?", "atb": ["63"], "padoms": "Viena daļa - viss."},
        {"jaut": "0 · 9 = ?", "atb": ["0"], "padoms": "Nevienas grupas."},
        {"jaut": "0 : 8 = ?", "atb": ["0"], "padoms": "Nekā sadalīt astoņās "
                                                      "daļās - katrā 0."},
        {"jaut": "35 : 35 = ?", "atb": ["1"], "padoms": "Viena grupa."},
        {"jaut": "1 · 0 = ?", "atb": ["0"], "padoms": "Viena tukša grupa."},
    ], pamats=4),

    Zimejums("Kas notiek ar skaitli",
             restis([["skaitlis", "reiz 1", "reiz 0"],
                     [8, 8, 0],
                     [25, 25, 0]],
                    "reizināšana ar 1 un 0"),
             paskaidro="Reizinot ar 1, skaitlis paliek tas pats; reizinot ar "
                       "0, no tā nekas nepaliek.",
             ievads="Salīdzini otro un trešo kolonnu."),

    Varianti("Kurš apgalvojums ir patiess?", [
        {"jaut": "Cik ir 0 : 7?",
         "opcijas": ["0", "7", "1", "Atbildes nav"],
         "pareizi": 0, "padoms": "Nekas, sadalīts septiņās daļās, ir nekas."},
        {"jaut": "Cik ir 7 : 0?",
         "opcijas": ["Atbildes nav", "0", "7", "1"],
         "pareizi": 0, "padoms": "Neviens skaitlis reiz 0 nedod 7."},
        {"jaut": "Kurš rēķins dod to pašu skaitli, kas bija sākumā?",
         "opcijas": ["a : 1", "a · 0", "a : a", "a − a"],
         "pareizi": 0, "padoms": "Dalīšana ar 1 neko nemaina."},
        {"jaut": "Cik ir 19 : 19?",
         "opcijas": ["1", "0", "19", "Atbildes nav"],
         "pareizi": 0, "padoms": "Viena grupa pa 19."},
    ], pamats=4),

    Pasaule("Ko darīt, ja trauku nav?",
            Ievadi("", [
                {"jaut": "12 plāceņus liek vienā šķīvī. Cik plāceņu ir "
                         "šķīvī?",
                 "atb": ["12"], "padoms": "12 : 1."},
                {"jaut": "Katram no 12 viesiem dod pa 1 plācenim. Cik "
                         "plāceņu vajag?",
                 "atb": ["12"], "padoms": "12 · 1."},
                {"jaut": "Pavārs izcepa 0 kūkas un liek tās 6 kastēs. Cik "
                         "kūku ir vienā kastē?",
                 "atb": ["0"], "padoms": "0 : 6."},
                {"jaut": "Uz galda ir 8 tukši šķīvji, katrā 0 plāceņi. Cik "
                         "plāceņu ir kopā?",
                 "atb": ["0"], "padoms": "8 · 0."},
            ]),
            pavediens="virtuve",
            konteksts="Virtuvē mēdz gadīties arī tukšs šķīvis un viens "
                      "vienīgs trauks - arī tie ir rēķini.",
            kapec="Ja saproti īpašos gadījumus, neviens uzdevums vairs "
                  "nepārsteidz."),

    Kopsavilkums([
        "Zinu un lietoju sakarības 1 · a = a un a : 1 = a.",
        "Zinu, ka 0 · a = 0 un 0 : a = 0.",
        "Zinu, ka a : a = 1.",
        "Paskaidroju, kāpēc ar nulli dalīt nevar.",
    ]),

    Majas([
        "Pamēģini kalkulatorā 8 : 0 un pastāsti, ko tas parādīja.",
        "Uzraksti trīs rēķinus, kuros rezultāts ir 0.",
        "Paskaidro mājiniekiem, kāpēc 6 : 6 = 1.",
    ]),
]
