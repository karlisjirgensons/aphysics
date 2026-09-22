# -*- coding: utf-8 -*-
"""5. klase, 5. stunda: «Kur skaitlis stāv uz skaitļu taisnes?»

Skaitļu taisne pirmo reizi tiek zīmēta pašam: jāizvēlas sākuma punkts un
vienība. Tieši šī izvēle vēlāk ļaus uz vienas ass atlikt gan gadsimtus
(6. stunda), gan daļas (5.3. temats), gan decimāldaļas (5.7. temats).
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kur skaitlis stāv uz skaitļu taisnes?"

MERKIS = ("Iemācīsimies izvēlēties vienību un atlikt skaitļus uz skaitļu "
          "taisnes tā, lai tie ietilpst un ir salasāmi.")

SATURS = [
    Sakums("Kāpēc visi punkti saspiedās vienā vietā?",
           zimejums=taisne(0, 1000, 200, [(980, ""), (1000, "")]),
           paraksts="Uz šīs ass 980 un 1 000 gandrīz sakrīt - iedaļa ir par "
                    "lielu.",
           fakti=["Lineālam, termometram un degvielas rādītājam ass ir viena "
                  "un tā pati.",
                  "Vispirms izvēlas iedaļu, tikai tad liek punktus."]),

    Doma("Vienību izvēlas pēc tā, ko gribi parādīt",
         "Vispirms izlemj, cik liela ir viena iedaļa - tikai tad liek "
         "punktus.",
         soli=[
             "Paskaties, kurš ir mazākais un kurš lielākais skaitlis.",
             "Izvēlies sākuma punktu - bieži 0, bet ne vienmēr.",
             "Izvēlies iedaļas vērtību tā, lai viss ietilptu.",
             "Atzīmē punktus un pieraksti tiem skaitļus.",
         ],
         pieze="Ja jāatliek 980, 1 000 un 1 020, sākt no nulles nav vērts - "
               "visi trīs punkti saplūstu. Labāk sākt no 960 ar iedaļu 20."),

    Zimejums("Viena un tā pati taisne, divas vienības",
             taisne(0, 100, 10, [(30, "30"), (75, "75")]),
             paskaidro="Viena iedaļa ir 10. Punkti 30 un 75 ir labi "
                       "saskatāmi.",
             ievads="Vispirms plaša aina no 0 līdz 100."),

    Zimejums("Tuvāks skats",
             taisne(70, 80, 1, [(75, "75"), (78, "78")]),
             paskaidro="Tagad viena iedaļa ir 1, un starp 75 un 78 redzam "
                       "katru soli."),

    Paraugs("Kā atlikt 1 250?",
            uzd="Uz taisnes jāatliek 1 100, 1 250 un 1 400. Kādu asi zīmēt?",
            soli=[
                ("Mazākais 1 100, lielākais 1 400",
                 "Vispirms noskaidro, cik plata aina vajadzīga."),
                ("Sākums 1 100, iedaļa 50",
                 "No 1 100 līdz 1 400 ir 300; ar iedaļu 50 sanāk seši soļi - "
                 "tik uz lapas ietilpst."),
                ("1 250 ir tieši vidū starp 1 100 un 1 400",
                 "Trīs iedaļas no sākuma."),
            ],
            atbilde="ass no 1 100 līdz 1 400 ar iedaļu 50; 1 250 ir trešajā "
                    "iedaļā"),

    Ievadi("Ko rāda iedaļa?", [
        {"jaut": "Ass no 0 līdz 50 sadalīta 10 vienādās daļās. Cik liela ir "
                 "viena iedaļa?", "atb": ["5"],
         "padoms": "50 : 10."},
        {"jaut": "Ass no 200 līdz 300 ar iedaļu 20. Cik iedaļu ir kopā?",
         "atb": ["5"], "padoms": "100 : 20."},
        {"jaut": "Ass sākas ar 0, iedaļa ir 25. Kāds skaitlis ir ceturtajā "
                 "iedaļā?", "atb": ["100"], "padoms": "25 · 4."},
        {"jaut": "Ass no 60 līdz 90 ar iedaļu 5. Cik liels skaitlis ir divas "
                 "iedaļas aiz 70?", "atb": ["80"], "padoms": "70 + 5 + 5."},
        {"jaut": "Ass no 1 000 līdz 2 000 ar iedaļu 250. Cik iedaļu?",
         "atb": ["4"], "padoms": "1 000 : 250."},
        {"jaut": "Punkts ir tieši vidū starp 340 un 360. Kāds tas skaitlis?",
         "atb": ["350"], "padoms": "Vidus ir pusceļš starp abiem."},
    ], pamats=4),

    Varianti("Kura ass der?", [
        {"jaut": "Jāatliek 7, 9 un 12. Kura ass ir ērtākā?",
         "opcijas": ["No 0 līdz 15 ar iedaļu 1", "No 0 līdz 1 000 ar iedaļu "
                     "100", "No 0 līdz 100 ar iedaļu 50",
                     "No 100 līdz 200 ar iedaļu 10"],
         "pareizi": 0,
         "padoms": "Punktiem jābūt atsevišķi saskatāmiem."},
        {"jaut": "Jāatliek 2 000, 2 005 un 2 010. Kur sākt asi?",
         "opcijas": ["No 2 000", "No 0", "No 1 000", "No 2 500"],
         "pareizi": 0,
         "padoms": "Sākot no nulles, visi trīs punkti saplūstu kopā."},
        {"jaut": "Uz ass ar iedaļu 10 punkts ir starp 40 un 50. Kurš skaitlis "
                 "tas nevar būt?",
         "opcijas": ["52", "41", "45", "49"],
         "pareizi": 0,
         "padoms": "52 jau ir aiz 50."},
        {"jaut": "Ass no 0 līdz 20 ar iedaļu 2. Cik iedaļu ir no 0 līdz 14?",
         "opcijas": ["7", "14", "6", "12"],
         "pareizi": 0,
         "padoms": "14 : 2."},
    ], pamats=4),

    Pasaule("Kur uz ass likt planētas?",
            Ievadi("", [
                {"jaut": "Ass no 0 līdz 1 500 miljoniem km ar iedaļu 300. "
                         "Cik iedaļu kopā?",
                 "atb": ["5"], "padoms": "1 500 : 300."},
                {"jaut": "Zeme ir 150 miljonu km attālumā. Cik tas ir pusēs "
                         "no 300?",
                 "atb": ["0,5", "0.5"], "padoms": "150 ir puse no 300."},
                {"jaut": "Ass iedaļa ir 50. Kāds skaitlis ir sestajā iedaļā?",
                 "atb": ["300"], "padoms": "50 · 6."},
                {"jaut": "Punkts ir tieši vidū starp 200 un 400. Kāds "
                         "skaitlis?",
                 "atb": ["300"], "padoms": "Vidus starp abiem."},
            ]),
            pavediens="kosmoss",
            konteksts="Marss ir ap 228 miljoniem km no Saules, Jupiters - ap "
                      "778 miljoniem km.",
            kapec="Ja iedaļa ir par lielu, tuvākās planētas uz ass saplūst "
                  "vienā punktā."),

    Kopsavilkums([
        "Izvēlos skaitļu taisnes sākuma punktu un iedaļas vērtību.",
        "Atlieku skaitļus uz taisnes tā, lai tie visi ietilpst.",
        "Nolasu, kāds skaitlis atbilst punktam starp iedaļām.",
    ]),

    Majas([
        "Uzzīmē asi savam augumam: no 100 cm līdz 200 cm. Kādu iedaļu "
        "izvēlēsies?",
        "Atzīmē uz vienas ass visu ģimenes locekļu dzimšanas gadus.",
        "Paskaties uz lineālu: cik liela ir viena mazā iedaļa?",
    ]),
]
