# -*- coding: utf-8 -*-
"""Matemātika, 2. klase. 2.4. Kā laika rēķini palīdz plānot?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 2. klase, 2.4. temats): laika mērvienības
(sekunde, minūte, stunda, diena, nedēļa, mēnesis, gads), pulksteņa laika
nolasīšana ar precizitāti līdz minūtei, notikuma ilguma, sākuma un beigu
laika aprēķini, kalendārs un saraksti, datu apkopošana tabulā un stabiņu
diagramma.
"""

PRIEKSMETS = "Matemātika  |  2. klase"
TEMATS = "2.4."
NOSAUKUMS = "Kā laika rēķini palīdz plānot?"

ATGADNE = [
    "1 minūte = 60 sekundes   ·   1 stunda = 60 minūtes   ·   "
    "1 diennakts = 24 stundas",
    "1 nedēļa = 7 dienas   ·   1 gads = 12 mēneši   ·   mēnesī ir 28–31 "
    "diena",
    "Ilgums = beigu laiks − sākuma laiks   ·   beigu laiks = sākums + "
    "ilgums",
]

FD = {
    "veids": "fd",
    "klase": 2,
    "temats": TEMATS,
    "nr": 4,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "4. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 2.4. temata beigās. Pārbauda laika "
                "mērvienības un to sakarības, pulksteņa laika nolasīšanu, "
                "notikuma ilguma, sākuma un beigu laika aprēķinus, "
                "kalendāra un saraksta lasīšanu un datu attēlošanu "
                "diagrammā.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Zina laika mērvienības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura no tām ir laika mērvienība?",
              ["sekunde", "centimetrs", "kilograms", "litrs"], 0),
             ("Kura laika mērvienība ir visīsākā?",
              ["sekunde", "minūte", "stunda", "diena"], 0),
             ("Kura laika mērvienība ir visgarākā?",
              ["minūte", "stunda", "diena", "gads"], 3),
         ]},
        {"sr": "Zina sakarības starp laika mērvienībām",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik sekunžu ir 1 minūtē?", ["10", "30", "60", "100"], 2),
             ("Cik minūšu ir 1 stundā?", ["24", "30", "60", "100"], 2),
             ("Cik stundu ir diennaktī?", ["12", "24", "60", "365"], 1),
         ]},
        {"sr": "Pārveido laika mērvienības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik minūšu ir 2 stundās?", ["60", "100", "120", "240"], 2),
             ("Cik dienu ir 3 nedēļās?", ["14", "21", "24", "30"], 1),
             ("Cik sekunžu ir 3 minūtēs?", ["30", "90", "180", "360"], 2),
         ]},
        {"sr": "Nolasa laiku ar precizitāti līdz minūtei",
         "stunda": TEMATS,
         "jautajumi": [
             ("Minūšu rādītājs ir uz 3. Cik minūtes ir pagājušas?",
              ["3", "15", "30", "45"], 1),
             ("Minūšu rādītājs ir uz 9. Cik minūtes ir pagājušas?",
              ["9", "30", "45", "54"], 2),
             ("Digitālais pulkstenis rāda 14:07. Cik minūtes pēc pilnas "
              "stundas?",
              ["7", "14", "17", "47"], 0),
         ]},
        {"sr": "Aprēķina notikuma ilgumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Nodarbība no 9:00 līdz 9:40. Cik ilga tā bija?",
              ["20 min", "30 min", "40 min", "60 min"], 2),
             ("Filma no 15:10 līdz 16:10. Cik ilga tā bija?",
              ["10 min", "50 min", "60 min", "70 min"], 2),
             ("Treniņš no 17:30 līdz 18:15. Cik ilgs tas bija?",
              ["30 min", "45 min", "50 min", "75 min"], 1),
         ]},
        {"sr": "Aprēķina notikuma beigu laiku",
         "stunda": TEMATS,
         "jautajumi": [
             ("Stunda sākas 8:00 un ilgst 40 minūtes. Kad tā beigsies?",
              ["8:30", "8:40", "9:00", "9:40"], 1),
             ("Pasākums sākas 12:20 un ilgst 30 minūtes. Kad tas beigsies?",
              ["12:40", "12:50", "13:20", "13:50"], 1),
             ("Brauciens sākas 10:45 un ilgst 15 minūtes. Kad tas beigsies?",
              ["10:50", "11:00", "11:15", "11:45"], 1),
         ]},
        {"sr": "Aprēķina notikuma sākuma laiku",
         "stunda": TEMATS,
         "jautajumi": [
             ("Nodarbība beidzas 11:00 un ilga 45 minūtes. Kad tā sākās?",
              ["10:15", "10:45", "11:45", "10:00"], 0),
             ("Filma beidzās 19:30 un ilga 1 stundu. Kad tā sākās?",
              ["18:00", "18:30", "19:00", "20:30"], 1),
             ("Treniņš beidzās 16:20 un ilga 20 minūtes. Kad tas sākās?",
              ["15:20", "16:00", "16:40", "17:20"], 1),
         ]},
        {"sr": "Lieto kalendāru",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik mēnešu ir gadā?", ["7", "10", "12", "24"], 2),
             ("Cik dienu ir janvārī?", ["28", "29", "30", "31"], 3),
             ("Šodien ir 5. maijs. Kāds datums būs pēc nedēļas?",
              ["10. maijs", "11. maijs", "12. maijs", "15. maijs"], 2),
         ]},
        {"sr": "Lasa informāciju sarakstā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Autobuss atiet 8:15 un brauc 25 minūtes. Kad tas pienāk?",
              ["8:30", "8:40", "8:45", "9:15"], 1),
             ("Afišā: izrāde sākas 17:00, ilgums 1 h 30 min. Kad tā "
              "beidzas?",
              ["18:00", "18:30", "19:00", "19:30"], 1),
             ("Sarakstā vilcieni 9:00, 9:30, 10:00. Cik bieži tie iet?",
              ["ik pēc 15 min", "ik pēc 30 min", "ik pēc 60 min",
               "nevar zināt"], 1),
         ]},
        {"sr": "Apkopo datus par laiku tabulā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Tabulā: pirmdien 30 min, otrdien 45 min lasīšanas. Cik kopā?",
              ["15 min", "60 min", "75 min", "80 min"], 2),
             ("Tabulā: treniņi 40, 40 un 50 minūtes. Cik kopā?",
              ["80 min", "90 min", "130 min", "140 min"], 2),
             ("Kāpēc datus par laiku pieraksta tabulā?",
              ["lai tos būtu viegli salīdzināt", "lai aizņemtu vietu",
               "lai nevajadzētu pulksteni", "lai būtu krāsaini"], 0),
         ]},
        {"sr": "Lasa un veido stabiņu diagrammu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Diagrammā garākais stabiņš rāda …",
              ["visilgāko laiku", "visīsāko laiku", "vidējo laiku",
               "nekādu laiku"], 0),
             ("Diagrammā pirmdien 20, otrdien 40 minūtes. Cik reižu vairāk "
              "otrdien?",
              ["2 reizes", "3 reizes", "4 reizes", "20 reizes"], 0),
             ("Ko liek diagrammas stabiņa augstumā?",
              ["datu vērtību", "datuma nosaukumu", "krāsu", "nosaukumu"], 0),
         ]},
        {"sr": "Plāno dienas darbības pēc laika",
         "stunda": TEMATS,
         "jautajumi": [
             ("Skola sākas 8:30. Ceļš aizņem 20 minūtes. Kad jāizbrauc?",
              ["8:00", "8:10", "8:20", "8:50"], 1),
             ("Jāpaspēj uz treniņu 17:00. Ceļš 30 min. Kad jāizbrauc?",
              ["16:00", "16:30", "17:30", "18:00"], 1),
             ("Kas palīdz plānot dienu?",
              ["pulkstenis un kalendārs", "lineāls", "svari",
               "mērtrauks"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 2,
    "temats": TEMATS,
    "nr": 4,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "4. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 2.4. temata noslēgumā. "
                "Pārbauda laika mērvienību sakarības un pārveidošanu, "
                "pulksteņa laika nolasīšanu, notikuma ilguma un sākuma "
                "laika aprēķinus, saraksta lasīšanu un datu attēlošanu "
                "diagrammā.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 punktus. "
              "Risinājumu raksti un zīmē tam atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Zina laika mērvienību sakarības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik sekunžu ir 1 minūtē?", ["10", "30", "60", "100"], 2),
             ("Cik minūšu ir 1 stundā?", ["24", "30", "60", "100"], 2),
             ("Cik dienu ir 1 nedēļā?", ["5", "7", "12", "30"], 1),
         ]},
        {"sr": "Pārveido laika mērvienības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik minūšu ir 3 stundās?", ["60", "120", "180", "360"], 2),
             ("Cik dienu ir 2 nedēļās?", ["7", "12", "14", "21"], 2),
             ("Cik sekunžu ir 2 minūtēs?", ["60", "100", "120", "200"], 2),
         ]},
        {"sr": "Nolasa pulksteņa laiku",
         "stunda": TEMATS,
         "jautajumi": [
             ("Minūšu rādītājs uz 6. Cik minūtes pagājušas?",
              ["6", "15", "30", "60"], 2),
             ("Digitālais pulkstenis rāda 09:25. Cik minūtes pēc pilnas "
              "stundas?",
              ["9", "25", "35", "52"], 1),
             ("Stundu rādītājs starp 4 un 5, minūšu uz 12. Cik ir "
              "pulkstenis?",
              ["4:00", "4:30", "5:00", "12:04"], 0),
         ]},
        {"sr": "Aprēķina notikuma ilgumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("No 10:00 līdz 10:35. Cik ilgi?",
              ["25 min", "35 min", "45 min", "60 min"], 1),
             ("No 13:20 līdz 14:00. Cik ilgi?",
              ["20 min", "40 min", "60 min", "80 min"], 1),
             ("No 18:15 līdz 19:15. Cik ilgi?",
              ["15 min", "45 min", "60 min", "75 min"], 2),
         ]},
        {"sr": "Aprēķina sākuma un beigu laiku",
         "stunda": TEMATS,
         "jautajumi": [
             ("Sākas 7:40, ilgst 20 min. Kad beidzas?",
              ["7:50", "8:00", "8:20", "8:40"], 1),
             ("Beidzas 12:00, ilga 45 min. Kad sākās?",
              ["11:15", "11:45", "12:45", "11:00"], 0),
             ("Sākas 16:50, ilgst 30 min. Kad beidzas?",
              ["17:00", "17:20", "17:30", "17:50"], 1),
         ]},
        {"sr": "Lasa kalendāru un sarakstu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik mēnešu ir gadā?", ["7", "10", "12", "24"], 2),
             ("Šodien ir 12. marts. Kāds datums būs pēc nedēļas?",
              ["17. marts", "18. marts", "19. marts", "20. marts"], 2),
             ("Vilcieni iet 8:00, 8:20, 8:40. Cik bieži?",
              ["ik pēc 10 min", "ik pēc 20 min", "ik pēc 30 min",
               "ik pēc 40 min"], 1),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Pārveido laika mērvienības",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Ieraksti trūkstošo skaitli",
              "note": "Ieraksti pareizo skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("1 stunda = …… minūtes", "60"),
                         ("2 minūtes = …… sekundes", "120"),
                         ("1 diennakts = …… stundas", "24"),
                         ("3 nedēļas = …… dienas", "21")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo skaitli",
              "note": "Ieraksti pareizo skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("1 minūte = …… sekundes", "60"),
                         ("2 stundas = …… minūtes", "120"),
                         ("1 gads = …… mēneši", "12"),
                         ("2 nedēļas = …… dienas", "14")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo skaitli",
              "note": "Ieraksti pareizo skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Pusstunda = …… minūtes", "30"),
                         ("3 minūtes = …… sekundes", "180"),
                         ("1 nedēļa = …… dienas", "7"),
                         ("4 stundas = …… minūtes", "240")]},
         ]},
        {"sr": "Aprēķina notikuma ilgumu un beigu laiku",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Ieraksti laiku",
              "note": "Ieraksti pareizo laiku vai ilgumu! Par katru pareizu "
                      "atbildi — 1 punkts.",
              "rindas": [("No 9:00 līdz 9:45 ir …… minūtes", "45"),
                         ("Sākas 10:30, ilgst 40 min, beidzas plkst. ……",
                          "11:10"),
                         ("Beidzas 14:00, ilga 30 min, sākās plkst. ……",
                          "13:30")]},
             {"tips": "parveide", "virs": "Ieraksti laiku",
              "note": "Ieraksti pareizo laiku vai ilgumu! Par katru pareizu "
                      "atbildi — 1 punkts.",
              "rindas": [("No 11:15 līdz 12:00 ir …… minūtes", "45"),
                         ("Sākas 8:50, ilgst 20 min, beidzas plkst. ……",
                          "9:10"),
                         ("Beidzas 17:00, ilga 45 min, sākās plkst. ……",
                          "16:15")]},
             {"tips": "parveide", "virs": "Ieraksti laiku",
              "note": "Ieraksti pareizo laiku vai ilgumu! Par katru pareizu "
                      "atbildi — 1 punkts.",
              "rindas": [("No 15:20 līdz 16:00 ir …… minūtes", "40"),
                         ("Sākas 12:45, ilgst 30 min, beidzas plkst. ……",
                          "13:15"),
                         ("Beidzas 19:30, ilga 1 stundu, sākās plkst. ……",
                          "18:30")]},
         ]},
        {"sr": "Plāno dienas darbības pēc saraksta",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Dienas plāns", "vieta": 6.0,
              "ievads": "Treniņš sākas 17:00 un ilgst 1 stundu 15 minūtes. "
                        "Ceļš uz treniņu aizņem 20 minūtes.",
              "jaut": [("Aprēķini, cikos treniņš beigsies!", 1),
                       ("Aprēķini, cikos jāizbrauc no mājām!", 1),
                       ("Aprēķini treniņa ilgumu minūtēs!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) 17:00 + 1 h 15 min = 18:15   (1 p.)",
                           "2) 17:00 − 20 min = 16:40   (1 p.)",
                           "3) 60 + 15 = 75 minūtes   (1 p.)",
                           "4) Atbilde: beigsies 18:15; izbraukt 16:40; "
                           "ilgums 75 minūtes.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Dienas plāns", "vieta": 6.0,
              "ievads": "Izrāde sākas 18:30 un ilgst 1 stundu 30 minūtes. "
                        "Ceļš uz teātri aizņem 25 minūtes.",
              "jaut": [("Aprēķini, cikos izrāde beigsies!", 1),
                       ("Aprēķini, cikos jāizbrauc no mājām!", 1),
                       ("Aprēķini izrādes ilgumu minūtēs!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) 18:30 + 1 h 30 min = 20:00   (1 p.)",
                           "2) 18:30 − 25 min = 18:05   (1 p.)",
                           "3) 60 + 30 = 90 minūtes   (1 p.)",
                           "4) Atbilde: beigsies 20:00; izbraukt 18:05; "
                           "ilgums 90 minūtes.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Dienas plāns", "vieta": 6.0,
              "ievads": "Nodarbība sākas 9:15 un ilgst 45 minūtes. Ceļš uz "
                        "skolu aizņem 15 minūtes.",
              "jaut": [("Aprēķini, cikos nodarbība beigsies!", 1),
                       ("Aprēķini, cikos jāizbrauc no mājām!", 1),
                       ("Aprēķini, cik minūšu pietrūkst līdz pilnai "
                        "stundai!", 1),
                       ("Uzraksti atbildi ar vārdiem!", 1)],
              "atbildes": ["1) 9:15 + 45 min = 10:00   (1 p.)",
                           "2) 9:15 − 15 min = 9:00   (1 p.)",
                           "3) 60 − 45 = 15 minūtes   (1 p.)",
                           "4) Atbilde: beigsies 10:00; izbraukt 9:00; "
                           "pietrūkst 15 minūtes.   (1 p.)"]},
         ]},
        {"sr": "Apkopo datus tabulā un veido stabiņu diagrammu",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Dati par lasīšanu", "vieta": 5.5,
              "ievads": "Pirmdien 20 min, otrdien 30 min, trešdien 40 min.",
              "jaut": [("Uzzīmē stabiņu diagrammu!", 1),
                       ("Aprēķini kopējo laiku!", 1),
                       ("Uzraksti, kurā dienā lasīts visilgāk!", 1)],
              "atbildes": ["1) Trīs stabiņi augstumā 20, 30 un 40.   (1 p.)",
                           "2) 20 + 30 + 40 = 90 minūtes   (1 p.)",
                           "3) Atbilde: trešdien (40 min).   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Dati par treniņiem", "vieta": 5.5,
              "ievads": "Pirmdien 45 min, trešdien 60 min, piektdien 30 min.",
              "jaut": [("Uzzīmē stabiņu diagrammu!", 1),
                       ("Aprēķini kopējo laiku!", 1),
                       ("Uzraksti, kurā dienā trenējies visīsāk!", 1)],
              "atbildes": ["1) Trīs stabiņi augstumā 45, 60 un 30.   (1 p.)",
                           "2) 45 + 60 + 30 = 135 minūtes   (1 p.)",
                           "3) Atbilde: piektdien (30 min).   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Dati par pastaigām", "vieta": 5.5,
              "ievads": "Sestdien 50 min, svētdien 70 min, pirmdien 20 min.",
              "jaut": [("Uzzīmē stabiņu diagrammu!", 1),
                       ("Aprēķini kopējo laiku!", 1),
                       ("Aprēķini, par cik svētdien ilgāk nekā pirmdien!",
                        1)],
              "atbildes": ["1) Trīs stabiņi augstumā 50, 70 un 20.   (1 p.)",
                           "2) 50 + 70 + 20 = 140 minūtes   (1 p.)",
                           "3) 70 − 20 = 50 minūtes   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
