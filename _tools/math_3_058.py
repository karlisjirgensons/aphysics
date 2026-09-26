# -*- coding: utf-8 -*-
"""3. klase, 58. stunda: «Ko var ieraudzīt evakuācijas plānā?»

Praktiskā temata sākums. Plāns ir kaut kas, ko bērns redz katru dienu skolas
gaitenī, bet nekad nav lasījis kā matemātiku. Stunda parāda, kas plānā ir
saglabāts (forma un novietojums) un kas mainīts (izmērs).
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         figura)

TEMA = "Ko var ieraudzīt evakuācijas plānā?"

MERKIS = ("Aplūkosim dažādus telpu plānus un pastāstīsim, kā tie veidoti.")

SATURS = [
    Sakums("Kāpēc uz A4 lapas ietilpst visa skola?",
           zimejums=figura([(0, 0), (10, 0), (10, 6), (0, 6)],
                           [(5, -0.6, "klase"), (2, 3, "galdi"),
                            (8, 3, "logi")],
                           "klases plāns"),
           paraksts="Plānā telpu redz no augšas, un viss ir samazināts "
                    "vienādi.",
           fakti=["Evakuācijas plāns ir katrā skolas gaitenī.",
                  "Tajā telpa ir samazināta, bet forma - tā pati."]),

    Doma("Plāns ir skats no augšas, samazināts vienādi",
         "Plānā saglabājas forma un novietojums; mainās tikai izmērs - un "
         "visam vienādi.",
         soli=[
             "Iedomājies, ka skaties uz telpu no griestiem.",
             "Uzzīmē sienas kā taisnas līnijas.",
             "Atzīmē durvis, logus un lielākās lietas.",
             "Samazini visus izmērus vienādu skaitu reižu.",
         ],
         pieze="Ja vienu sienu samazinātu 10 reizes, bet otru 5 reizes, "
               "telpa plānā izskatītos pavisam citāda - tāpēc samazinājumam "
               "jābūt vienādam."),

    Paraugs("Ko plānā nozīmē 5 cm?",
            uzd="Klases siena ir 10 m gara, plānā tā ir 10 cm. Cik gara "
                "plānā būs 5 m siena?",
            soli=[
                ("10 m → 10 cm",
                 "Visi izmēri samazināti vienādu skaitu reižu."),
                ("5 m ir puse no 10 m",
                 "Tātad arī plānā tas būs puse."),
                ("5 cm",
                 "Otrā siena plānā ir 5 cm gara."),
            ],
            atbilde="5 cm"),

    Petijums("Izlasi savas skolas plānu",
             vajag="evakuācijas plāns gaitenī",
             soli=[
                 "Atrodi gaitenī evakuācijas plānu.",
                 "Atrodi tajā savu klasi.",
                 "Seko līdzi ceļam līdz tuvākajai izejai.",
                 "Pieraksti, cik durvju ir šajā ceļā.",
             ],
             secinajums="Plāns ir noderīgs tieši tāpēc, ka forma un "
                        "novietojums tajā ir pareizi."),

    Ievadi("Nolasi plānu", [
        {"jaut": "1 m telpā ir 1 cm plānā. Cik centimetru plānā ir 8 m "
                 "siena?",
         "atb": ["8"], "padoms": "Katram metram viens centimetrs."},
        {"jaut": "Cik metru telpā ir 12 cm plānā?", "atb": ["12"],
         "padoms": "Katram centimetram viens metrs."},
        {"jaut": "Klase ir 9 m un 6 m. Cik centimetru ir plāna garākā mala?",
         "atb": ["9"], "padoms": "9 m → 9 cm."},
        {"jaut": "Cik centimetru ir šī plāna perimetrs?", "atb": ["30"],
         "padoms": "2 · (9 + 6)."},
        {"jaut": "Cik metru ir klases perimetrs?", "atb": ["30"],
         "padoms": "Tas pats skaitlis, tikai metros."},
        {"jaut": "Plānā durvis ir 1 cm platas. Cik centimetru ir durvis "
                 "telpā? Raksti metros.",
         "atb": ["1"], "padoms": "1 cm plānā ir 1 m telpā."},
    ], pamats=4),

    Zimejums("Tā pati telpa, cits izmērs",
             figura([(0, 0), (5, 0), (5, 3), (0, 3)],
                    [(2.5, -0.6, "9 m"), (5.8, 1.5, "6 m")],
                    "klase plānā"),
             paskaidro="Forma ir tā pati, kas telpai; mainījies ir tikai "
                       "izmērs uz lapas.",
             ievads="Šis taisnstūris ir visa klase."),

    Varianti("Kas plānā saglabājas?", [
        {"jaut": "Kas plānā paliek tāds pats kā telpā?",
         "opcijas": ["Forma un novietojums", "Izmērs", "Krāsa", "Nekas"],
         "pareizi": 0, "padoms": "Mainās tikai izmērs."},
        {"jaut": "Kāpēc visi izmēri jāsamazina vienādi?",
         "opcijas": ["Citādi forma sagrozītos", "Tā ir tradīcija",
                     "Lai plāns būtu skaistāks", "Lai ietilptu lapā"],
         "pareizi": 0, "padoms": "Telpa izskatītos citāda."},
        {"jaut": "No kuras puses plānā skatās uz telpu?",
         "opcijas": ["No augšas", "No priekšas", "No sāna", "No apakšas"],
         "pareizi": 0, "padoms": "Plāns ir skats no griestiem."},
        {"jaut": "Ko evakuācijas plānā atzīmē vissvarīgāk?",
         "opcijas": ["Ceļu uz izeju", "Galdu krāsu", "Logu skaitu",
                     "Griestu augstumu"],
         "pareizi": 0, "padoms": "Plāns ir domāts izejai."},
    ], pamats=4),

    Pasaule("Kā atrast ceļu skolā?",
            Ievadi("", [
                {"jaut": "No klases līdz izejai jāiet 30 m un tad vēl 20 m. "
                         "Cik metru kopā?",
                 "atb": ["50"], "padoms": "30 + 20."},
                {"jaut": "Plānā 1 m ir 1 cm. Cik centimetru ir šis ceļš "
                         "plānā?",
                 "atb": ["50"], "padoms": "Tas pats skaitlis centimetros."},
                {"jaut": "Otrs ceļš ir 35 m. Par cik metriem tas ir īsāks?",
                 "atb": ["15"], "padoms": "50 − 35."},
                {"jaut": "Ja vienā minūtē var noiet 70 m, cik metru noies "
                         "3 minūtēs?",
                 "atb": ["210"], "padoms": "3 · 70."},
            ]),
            pavediens="skola",
            konteksts="Evakuācijas plāns rāda īsāko ceļu uz izeju - tāpēc to "
                      "der izlasīt pirms, nevis pēc trauksmes.",
            kapec="Plāns pārvērš telpu skaitļos, ko var salīdzināt."),

    Kopsavilkums([
        "Zinu, ka plāns ir skats uz telpu no augšas.",
        "Zinu, ka plānā visi izmēri samazināti vienādu skaitu reižu.",
        "Atrodu plānā telpu un ceļu uz izeju.",
        "Nolasu no plāna attālumus.",
    ]),

    Majas([
        "Atrodi mājās vai veikalā kādu plānu un apskati to.",
        "Uzzīmē savas istabas plānu no galvas.",
        "Saskaiti, cik durvju ir ceļā no tavas istabas līdz ārdurvīm.",
    ]),
]
