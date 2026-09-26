# -*- coding: utf-8 -*-
"""9. klase, 172. stunda: «Ko darīt ar laiku eksāmenā?»

Gada pēdējā stunda. Laika stratēģija: trīs gājieni (vispirms viegli, tad
izvērstie, beigās pārbaude), laika budžets uz uzdevumu, iestrēgšanas
noteikums. Pēc tam jaukts miniatūrs darbs no visām jomām un kļūdu analīze.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, kolonnas)

TEMA = "Ko darīt ar laiku eksāmenā?"

MERKIS = ("Risināsim darbu laika kontrolē un analizēsim savas kļūdas.")

_LAIKS = kolonnas([("1. gājiens", 60), ("2. gājiens", 30),
                   ("Pārbaude", 15)], " min")

SATURS = [
    Sakums("105 minūtes 26 uzdevumiem - kā tās sadalīt?",
           zimejums=_LAIKS,
           paraksts="1. daļas laika plāns trīs gājienos.",
           fakti=["1. gājiens: visi uzdevumi, ko proti uzreiz.",
                  "2. gājiens: izlaistie un izvērstie uzdevumi.",
                  "Beigās: pārbaudi atbildes un pārnesumus."]),

    Doma("Trīs gājienu stratēģija",
         "Punkts par vieglu uzdevumu ir tikpat vērtīgs kā par grūtu - "
         "vispirms savāc drošos punktus.",
         soli=[
             "Iestrēdzi ilgāk par 3-4 min? Atzīmē un ej tālāk.",
             "Izvēles uzdevumā izslēdz nepareizās atbildes.",
             "Izvērstajā uzdevumā uzraksti vismaz formulu - tā dod punktu.",
             "Neatstāj tukšu: daļējs risinājums var dot punktus.",
         ]),

    Ievadi("Laika budžets", [
        {"jaut": "105 min, 15 min atstāj pārbaudei. Cik min vidēji uz vienu "
                 "no 26 uzdevumiem? Noapaļo līdz desmitdaļām.",
         "atb": ["3,5"], "padoms": "90 : 26 ≈ 3,46."},
        {"jaut": "2. daļā 75 min, 5 uzdevumi, 10 min pārbaudei. Min uz "
                 "uzdevumu?", "atb": ["13"], "padoms": "65 : 5."},
        {"jaut": "1 punkta uzdevumam iztērēji 12 min, vidēji paredzētas 3. "
                 "Cik reižu ilgāk?", "atb": ["4"], "padoms": "12 : 3."},
    ]),

    Varianti("Ko darīt?", [
        {"jaut": "Pēc 5 minūtēm uzdevums joprojām nepadodas.",
         "opcijas": ["atzīmē un ej tālāk", "turpini līdz sanāk"],
         "jaukt": False, "pareizi": 0, "padoms": "Atgriezīsies 2. gājienā."},
        {"jaut": "Palikušas 2 min, izvēles uzdevums neatrisināts.",
         "opcijas": ["izslēdz aplamās un izvēlies", "atstāj tukšu"],
         "jaukt": False, "pareizi": 0, "padoms": "Tukšs - noteikti 0."},
        {"jaut": "Atbilde sanāca −3 m garums.",
         "opcijas": ["meklē kļūdu", "raksti atbildi"], "jaukt": False,
         "pareizi": 0, "padoms": "Garums nevar būt negatīvs."},
    ]),

    Ievadi("Mini darbs: 10 minūtes", [
        {"jaut": "2^{−3} (decimāldaļa)", "atb": ["0,125"],
         "padoms": "{1|8}."},
        {"jaut": "(x − 3)^2 = x^2 − kx + 9. k = ?", "atb": ["6"],
         "padoms": "2 · 3."},
        {"jaut": "x^2 = 49, x > 0", "atb": ["7"], "padoms": "√49."},
        {"jaut": "a_1 = 5, d = −2. a_6 = ?", "atb": ["−5"],
         "padoms": "5 + 5 · (−2)."},
        {"jaut": "Regulāra sešstūra leņķis (°)", "atb": ["120"],
         "padoms": "4 · 180 : 6."},
        {"jaut": "R = 5, attālums līdz hordai 4. Horda?", "atb": ["6"],
         "padoms": "2 · √(25 − 16)."},
    ]),

    Petijums("Kļūdu analīze", [
        "Katru mini darba kļūdu pieraksti: kur un kāpēc.",
        "Kāda tā bija: nezināju, pārrakstījos, pietrūka laika?",
        "«Nezināju» - temats uz atkārtošanas sarakstu.",
        "«Pārrakstījos» - ieplāno pārbaudes gājienu.",
    ], vajag="mini darba rezultāti, 167. stundas saraksts",
       secinajums="Katrai kļūdai ir cēlonis, un katram cēlonim - "
                  "savs līdzeklis."),

    Pasaule("Kā skrējienā",
            Ievadi("", [
                {"jaut": "5 km jānoskrien 25 min. Cik min uz 1 km?",
                 "atb": ["5"], "padoms": "25 : 5."},
                {"jaut": "Pēc 3 km pagājušas 16 min. Cik min uz 1 km "
                         "atlikušajiem 2 km?", "atb": ["4,5"],
                 "padoms": "(25 − 16) : 2."},
            ]),
            pavediens="sports",
            konteksts="Skrējējs seko tempam katrā kilometrā, nevis tikai "
                      "finišā - tāpat eksāmenā seko laikam.",
            kapec="Ja pusceļā redzi, ka atpaliec, vēl var paātrināties - "
                  "tāpēc skaties pulkstenī ik pēc 5 uzdevumiem."),

    Kopsavilkums([
        "Zinu trīs gājienu stratēģiju un iestrēgšanas noteikumu.",
        "Aprēķinu savu laika budžetu uz uzdevumu.",
        "Analizēju kļūdas pēc cēloņa.",
    ]),

    Majas([
        "Izpildi pilnu iepriekšējā gada eksāmenu ar taimeri.",
        "Pieraksti, cik minūšu aizņēma katrs uzdevums.",
        "Izveido savu laika plānu un paņem to līdzi atmiņā uz eksāmenu.",
    ]),
]
