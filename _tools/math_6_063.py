# -*- coding: utf-8 -*-
"""6. klase, 63. stunda: «Kā uzbūvēt cilindru?»

Programmas praktiskā daļa. Cilindru nevar salikt no kubiem, tāpēc te jāsāk
ar plānu: cik gara sanāks sānu virsma un kāpēc tieši tik gara. Apkārtmērs
kļūst par darba rīku, ne par formulu burtnīcā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         kermenis)

TEMA = "Kā uzbūvēt cilindru?"

MERKIS = ("Plānosim un praktiski izveidosim cilindra modeli pēc dotiem "
          "izmēriem.")

SATURS = [
    Sakums("Konservu bundža ir sarullēts taisnstūris",
           zimejums=kermenis("cilindrs"),
           paraksts="Sānu virsma ir taisnstūris; tā platums ir pamata "
                    "apkārtmērs, augstums - cilindra augstums.",
           fakti=["Cilindra pamati ir divi vienādi apļi.",
                  "Sānu virsma, izklāta uz galda, ir taisnstūris.",
                  "Apkārtmērs ir apmēram 3,14 reizes diametrs."]),

    Doma("Sānu virsmas platums ir apkārtmērs",
         "Lai uzbūvētu cilindru, vajag divus vienādus apļus un taisnstūri, "
         "kura platums ir pamata apkārtmērs.",
         soli=[
             "Izvēlies pamata diametru un cilindra augstumu.",
             "Aprēķini apkārtmēru: diametru reizini ar 3,14.",
             "Izgriez taisnstūri ar šo platumu un izvēlēto augstumu.",
             "Sarullē to un salīmē malas.",
             "Pieliec divus apļus ar izvēlēto diametru.",
         ],
         pieze="Apkārtmēru var arī izmērīt: aptin diegu ap apli un izmēri "
               "diega garumu. Rezultāts vienmēr sanāk mazliet vairāk nekā "
               "trīs diametri."),

    Paraugs("Saplāno cilindru",
            uzd="Cilindra pamata diametrs ir 6 cm, augstums 10 cm. Cik liels "
                "taisnstūris jāizgriež?",
            soli=[
                ("Apkārtmērs: 6 · 3,14 = 18,84 cm",
                 "Diametru reizina ar 3,14."),
                ("Noapaļo: apmēram 18,8 cm",
                 "Ar lineālu precīzāk nevar."),
                ("Taisnstūris 18,8 cm x 10 cm",
                 "Platums ir apkārtmērs, augstums - cilindra augstums."),
                ("Divi apļi ar diametru 6 cm",
                 "Pamati."),
            ],
            atbilde="taisnstūris 18,8 cm x 10 cm un divi apļi"),

    Ievadi("Aprēķini cilindra daļas", [
        {"jaut": "Diametrs ir 10 cm. Cik cm ir apkārtmērs? Rēķini ar 3,14.",
         "atb": ["31,4", "31.4"], "padoms": "10 · 3,14."},
        {"jaut": "Diametrs ir 5 cm. Cik cm ir apkārtmērs?",
         "atb": ["15,7", "15.7"], "padoms": "5 · 3,14."},
        {"jaut": "Apkārtmērs ir 31,4 cm, augstums 8 cm. Cik cm² ir sānu "
                 "virsmas laukums?",
         "atb": ["251,2", "251.2"], "padoms": "31,4 · 8."},
        {"jaut": "Diametrs ir 6 cm. Cik cm ir rādiuss?",
         "atb": ["3"], "padoms": "Puse no diametra."},
        {"jaut": "Apkārtmērs ir 18,84 cm. Cik cm ir diametrs?",
         "atb": ["6"], "padoms": "18,84 : 3,14."},
        {"jaut": "Cik apļu vajag viena cilindra pamatiem?",
         "atb": ["2"], "padoms": "Apakšā un augšā."},
    ], pamats=4),

    Petijums("Uzbūvē cilindru",
             vajag="papīrs, lineāls, šķēres, līme, diegs",
             soli=[
                 "Izvēlieties diametru 6 cm un augstumu 10 cm.",
                 "Aprēķiniet apkārtmēru un izgrieziet taisnstūri.",
                 "Sarullējiet to un salīmējiet.",
                 "Uzzīmējiet un izgrieziet divus apļus, pielīmējiet tos.",
                 "Pārbaudiet ar diegu, vai apkārtmērs sakrīt ar aprēķinu.",
             ],
             secinajums="Ja taisnstūris bija par īsu, malas nesatiekas; ja "
                        "par garu, tās pārklājas - apkārtmērs jārēķina "
                        "precīzi."),

    Varianti("Kas ar ko sakrīt?", [
        {"jaut": "Ar ko sakrīt sānu virsmas platums?",
         "opcijas": ["Ar pamata apkārtmēru", "Ar diametru",
                     "Ar rādiusu", "Ar augstumu"],
         "pareizi": 0,
         "padoms": "Sarullējot mala aptinas ap apli."},
        {"jaut": "Ar ko sakrīt sānu virsmas augstums?",
         "opcijas": ["Ar cilindra augstumu", "Ar apkārtmēru",
                     "Ar diametru", "Ar rādiusu"],
         "pareizi": 0,
         "padoms": "Tas nemainās, rullējot."},
        {"jaut": "Apkārtmērs ir apmēram...",
         "opcijas": ["3,14 diametri", "2 diametri", "3,14 rādiusi",
                     "10 diametri"],
         "pareizi": 0,
         "padoms": "Mazliet vairāk par trim diametriem."},
        {"jaut": "Ja taisnstūris sanāk par platu, kas notiks?",
         "opcijas": ["Malas pārklāsies", "Malas nesatiksies",
                     "Cilindrs būs augstāks", "Nekas nemainīsies"],
         "pareizi": 0,
         "padoms": "Papīra būs par daudz."},
    ], pamats=4),

    Pasaule("Cik etiķešu papīra vajag?",
            Ievadi("", [
                {"jaut": "Bundžas diametrs ir 8 cm. Cik cm gara ir etiķete? "
                         "Rēķini ar 3,14.",
                 "atb": ["25,12", "25.12"], "padoms": "8 · 3,14."},
                {"jaut": "Etiķetes augstums ir 10 cm. Cik cm² ir tās "
                         "laukums?",
                 "atb": ["251,2", "251.2"], "padoms": "25,12 · 10."},
                {"jaut": "Cik cm gara ir etiķete bundžai ar diametru 6 cm?",
                 "atb": ["18,84", "18.84"], "padoms": "6 · 3,14."},
                {"jaut": "Cik etiķešu var izgriezt no 100 cm garas sloksnes, "
                         "ja katra ir 25 cm?",
                 "atb": ["4"], "padoms": "100 : 25."},
            ]),
            pavediens="tehnika",
            konteksts="Etiķete ir tieši tas pats taisnstūris, kas sānu "
                      "virsma - tāpēc tās garumu rēķina pēc apkārtmēra.",
            kapec="Viens aprēķins pasaka, cik papīra vajag visai partijai."),

    Zimejums("Konuss - tā paša ģimene",
             kermenis("konuss"),
             paskaidro="Arī konusam pamats ir aplis, bet sānu virsma nav "
                       "taisnstūris - tā ir apļa izgriezums.",
             ievads="Nākamajā stundā salīdzināsim konusu ar piramīdu."),

    Kopsavilkums([
        "Plānoju cilindra modeli pēc dotiem izmēriem.",
        "Aprēķinu pamata apkārtmēru, reizinot diametru ar 3,14.",
        "Zinu, ka sānu virsma izklāta ir taisnstūris.",
        "Praktiski izveidoju cilindru un pārbaudu savus aprēķinus.",
    ]),

    Majas([
        "Atrodi mājās cilindra formas trauku un izmēri tā diametru.",
        "Aprēķini tā apkārtmēru un pārbaudi ar diegu.",
        "Uzzīmē, kā izskatītos tā etiķete, ja to nogrieztu un izklātu.",
    ]),
]
