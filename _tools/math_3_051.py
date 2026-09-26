# -*- coding: utf-8 -*-
"""3. klase, 51. stunda: «Kā pastāstīt savu risinājumu?»

Mikrotemata noslēgums. Izstāstīt risinājumu ir grūtāk, nekā to izrēķināt, un
tieši stāstījums parāda, vai skolēns saprot, *kāpēc* darīja katru soli.
Stundā ir gatava struktūra, pēc kuras stāstīt - trīs teikumi un zīmējums.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kā pastāstīt savu risinājumu?"

MERKIS = ("Uzskatāmi attēlosim un pamatosim savu risinājumu klasesbiedriem.")

SATURS = [
    Sakums("Kā pateikt risinājumu trijos teikumos?",
           zimejums=restis([["1.", "Ko zinu"],
                            ["2.", "Ko rēķinu un kāpēc"],
                            ["3.", "Kāda ir atbilde"]],
                           "stāstījuma trīs daļas"),
           paraksts="Trīs teikumi - un klausītājs saprot visu.",
           fakti=["Labs stāstījums sākas ar to, kas ir zināms.",
                  "Katrs solis jāpamato ar vārdu «jo» vai «tāpēc»."]),

    Doma("Stāsti pa soļiem, ne pa skaitļiem",
         "Katram solim pasaki, *ko* tu rēķini un *kāpēc* tieši to.",
         soli=[
             "Pasaki, kas uzdevumā ir zināms.",
             "Pasaki pirmo darbību un kāpēc tā ir pirmā.",
             "Pasaki, ko ieguvi - tā ir starpatbilde.",
             "Pasaki otro darbību un galīgo atbildi.",
             "Parādi zīmējumu vai tāmi, kamēr stāsti.",
         ],
         pieze="Ja klausītājs jautā «kāpēc?», tas nav slikti - tas nozīmē, ka "
               "viens «tāpēc» stāstījumā vēl pietrūka."),

    Paraugs("Kā izstāstīt šo risinājumu?",
            uzd="Kabatā 90 ct, nopirka 4 zīmuļus pa 15 ct. Cik palika? "
                "Izstāsti risinājumu.",
            soli=[
                ("«Zinu, ka kabatā bija 90 ct un zīmulis maksā 15 ct.»",
                 "Pirmais teikums - kas ir zināms."),
                ("«Vispirms rēķinu 4 · 15 = 60, jo jāzina pirkuma summa.»",
                 "Otrais teikums - darbība un pamatojums."),
                ("«Tad 90 − 60 = 30, tātad palika 30 ct.»",
                 "Trešais teikums - otrā darbība un atbilde."),
            ],
            atbilde="30 ct"),

    Petijums("Izstāsti risinājumu pārī",
             vajag="uzdevums, lapa un zīmulis",
             soli=[
                 "Atrisini uzdevumu un uzzīmē tam shēmu.",
                 "Izstāsti risinājumu klasesbiedram trijos teikumos.",
                 "Palūdz, lai viņš pajautā vienu «kāpēc?».",
                 "Papildini stāstījumu ar atbildi uz šo jautājumu.",
             ],
             secinajums="Stāstījums ir pilnīgs tad, kad klausītājam vairs nav "
                        "ko jautāt."),

    Ievadi("Atrisini un sagatavo stāstījumu", [
        {"jaut": "Kabatā 90 ct, 4 zīmuļi pa 15 ct. Cik palika?",
         "atb": ["30"], "padoms": "90 − 60."},
        {"jaut": "6 kastes pa 9 olām, 4 saplīsa. Cik palika?",
         "atb": ["50"], "padoms": "54 − 4."},
        {"jaut": "48 lapas sadalīja 8 bērniem, katrs izlietoja 3. Cik katram "
                 "palika?",
         "atb": ["3"], "padoms": "48 : 8 = 6; 6 − 3."},
        {"jaut": "Klasē 24 bērni, katram 2 burtnīcas pa 20 ct. Cik maksā "
                 "visas?",
         "atb": ["960"], "padoms": "24 · 2 = 48; 48 · 20."},
        {"jaut": "100 ct, nopirka 3 preces pa 18 ct. Cik palika?",
         "atb": ["46"], "padoms": "3 · 18 = 54."},
        {"jaut": "7 grupas pa 4 bērniem, vēl 5 bērni klāt. Cik kopā?",
         "atb": ["33"], "padoms": "28 + 5."},
    ], pamats=4),

    Zimejums("Stāstījuma paraugs",
             restis([["Zinu", "90 ct un cena 15 ct"],
                     ["Rēķinu", "4 · 15 = 60, jo vajag summu"],
                     ["Atbilde", "90 − 60 = 30 ct"]],
                    "trīs rindas"),
             paskaidro="Pēc šīs tabulas var izstāstīt jebkuru divu darbību "
                       "risinājumu.",
             ievads="Šo tabulu vērts paturēt burtnīcā."),

    Varianti("Kas stāstījumā pietrūkst?", [
        {"jaut": "«60, tad 30.» Kas pietrūkst?",
         "opcijas": ["Kas ir zināms un kāpēc tā rēķina",
                     "Atbilde", "Skaitļi", "Nekas"],
         "pareizi": 0, "padoms": "Tikai skaitļi vēl nav stāstījums."},
        {"jaut": "Ar ko labāk sākt stāstījumu?",
         "opcijas": ["Ar to, kas ir zināms", "Ar atbildi",
                     "Ar otro darbību", "Ar pārbaudi"],
         "pareizi": 0, "padoms": "Klausītājam vispirms vajag datus."},
        {"jaut": "Kāds vārds palīdz pamatot soli?",
         "opcijas": ["jo", "un", "tad", "arī"],
         "pareizi": 0, "padoms": "Pamatojums sākas ar «jo» vai «tāpēc»."},
        {"jaut": "Ko nozīmē klausītāja jautājums «kāpēc?»",
         "opcijas": ["Kāds pamatojums vēl pietrūka", "Stāstījums ir slikts",
                     "Atbilde ir nepareiza", "Neko"],
         "pareizi": 0, "padoms": "Tā ir norāde, ko papildināt."},
    ], pamats=4),

    Pasaule("Pastāsti, kā saplānoji pirkumu",
            Ievadi("", [
                {"jaut": "Klases kasē 400 ct. Nopirka 5 sulas pa 60 ct. Cik "
                         "maksāja sulas?",
                 "atb": ["300"], "padoms": "5 · 60."},
                {"jaut": "Cik palika kasē?",
                 "atb": ["100"], "padoms": "400 − 300."},
                {"jaut": "Cik cepumu paciņu pa 25 ct vēl var nopirkt?",
                 "atb": ["4"], "padoms": "100 : 25."},
                {"jaut": "Cik naudas paliks pēc cepumiem?",
                 "atb": ["0"], "padoms": "100 − 100."},
            ]),
            pavediens="veikals",
            konteksts="Klases naudu tērē kopā - tāpēc katram jāprot "
                      "izstāstīt, kur nauda aizgāja.",
            kapec="Stāstījums ir tas, kas pārliecina pārējos, ka rēķins ir "
                  "pareizs."),

    Kopsavilkums([
        "Izstāstu savu risinājumu trijos teikumos.",
        "Pamatoju katru soli ar «jo» vai «tāpēc».",
        "Attēloju risinājumu ar shēmu vai tāmi.",
        "Papildinu stāstījumu, ja klausītājam rodas jautājums.",
    ]),

    Majas([
        "Izstāsti mājiniekiem vienu šodienas uzdevuma risinājumu.",
        "Uzzīmē tam shēmu un parādi to, kamēr stāsti.",
        "Palūdz, lai viņi pajautā vienu «kāpēc?».",
    ]),
]
