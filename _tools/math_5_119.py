# -*- coding: utf-8 -*-
"""5. klase, 119. stunda: «Kādu rakstu var uzzīmēt ar cirkuli?»

Mikrotemata noslēgums, un vienīgā stunda, kurā rezultāts ir zīmējums, nevis
skaitlis. Raksts te nav rotaļa: lai tas sanāktu simetrisks, riņķis jāsadala
vienādās daļās, un tas ir tieši 112. stundas rēķins ar grādiem. Skaistums
šeit ir precizitātes pārbaude.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         lenkis, rinkis)

TEMA = "Kādu rakstu var uzzīmēt ar cirkuli?"

MERKIS = ("Mācīsimies veidot simetrisku zīmējumu, lietojot riņķa līnijas ar "
          "kopīgu centru un riņķa dalīšanu vienādās daļās.")

SATURS = [
    Sakums("Seši ziedlapiņu loki",
           zimejums=lenkis([(0, ""), (60, ""), (120, ""), (180, ""),
                            (240, ""), (300, "")],
                           loki=[(0, 60, "60°")],
                           virsraksts="Riņķis sadalīts sešās daļās"),
           paraksts="360 : 6 = 60 - tāpēc seši stari sadala riņķi vienādi.",
           fakti=["Rakstam vajag vienādas daļas.",
                  "Vienādas daļas iegūst, dalot 360° ar daļu skaitu.",
                  "Ar rādiusu riņķa līniju var sadalīt sešās daļās bez "
                  "rēķina."]),

    Doma("Simetrija sākas ar vienādām daļām",
         "Simetrisku rakstu zīmē, riņķi sadalot vienādās daļās un katrā daļā "
         "atkārtojot vienu un to pašu elementu.",
         soli=[
             "Uzzīmē riņķa līniju ar izvēlētu rādiusu.",
             "Aprēķini, cik grādu ir viena daļa: 360 dalīts ar daļu skaitu.",
             "Atzīmē uz līnijas vienādi attālus punktus.",
             "No katra punkta zīmē vienu un to pašu elementu.",
             "Pārbaudi, vai visas daļas izskatās vienādi.",
         ],
         pieze="Rādiuss riņķa līnijā ietilpst tieši sešas reizes, tāpēc "
               "sešas daļas var atzīmēt ar cirkuli vien - neizmainot "
               "atvērumu, ejot pa līniju no punkta uz punktu."),

    Petijums("Uzzīmē ziedu ar cirkuli",
             soli=["Uzzīmē riņķa līniju ar rādiusu 4 cm.",
                   "Neizmainot atvērumu, noliec adatu uz līnijas un atzīmē "
                   "nākamo punktu.",
                   "Atkārto, līdz uz līnijas ir seši punkti.",
                   "No katra punkta uzzīmē loku ar to pašu rādiusu.",
                   "Iekrāso iegūtās ziedlapiņas."],
             vajag="cirkulis, zīmulis, krāsainie zīmuļi",
             secinajums="Seši loki ar vienādu rādiusu veido simetrisku ziedu "
                        "ar sešām ziedlapiņām."),

    Paraugs("Cik grādu ir viena daļa?",
            uzd="Riņķi jāsadala 8 vienādās daļās. Cik grādu ir katra?",
            soli=[
                ("Pilns leņķis ir 360°",
                 "Veselais."),
                ("360 : 8 = 45",
                 "Viena daļa."),
                ("Katrs nākamais stars par 45° tālāk",
                 "Punkti uz līnijas."),
                ("Astoņi vienādi sektori",
                 "Raksts būs simetrisks."),
            ],
            atbilde="Katra daļa ir 45°"),

    Ievadi("Sadali riņķi vienādās daļās", [
        {"jaut": "Riņķi sadala 6 daļās. Cik grādu ir katra?",
         "atb": ["60"], "padoms": "360 : 6."},
        {"jaut": "Riņķi sadala 8 daļās. Cik grādu ir katra?",
         "atb": ["45"], "padoms": "360 : 8."},
        {"jaut": "Riņķi sadala 12 daļās. Cik grādu ir katra?",
         "atb": ["30"], "padoms": "360 : 12."},
        {"jaut": "Riņķi sadala 5 daļās. Cik grādu ir katra?",
         "atb": ["72"], "padoms": "360 : 5."},
        {"jaut": "Katra daļa ir 40°. Cik daļu sanāk?",
         "atb": ["9"], "padoms": "360 : 40."},
        {"jaut": "Katra daļa ir 90°. Cik daļu sanāk?",
         "atb": ["4"], "padoms": "360 : 90."},
        {"jaut": "Cik reižu rādiuss ietilpst riņķa līnijā, ja to atliek ar "
                 "cirkuli?",
         "atb": ["6"], "padoms": "Seši vienādi loki."},
        {"jaut": "Riņķi sadala 10 daļās. Cik grādu ir katra?",
         "atb": ["36"], "padoms": "360 : 10."},
    ], pamats=4,
        ievads="Viena daļa vienmēr ir 360°, dalīts ar daļu skaitu."),

    Zimejums("Riņķi ar kopīgu centru",
             rinkis(radiuss="r", virsraksts="Viens centrs, vairāki rādiusi"),
             paskaidro="Ja no viena centra zīmē vairākas riņķa līnijas ar "
                       "dažādiem rādiusiem, iznāk mērķa raksts.",
             ievads="Kopīgs centrs ir vienkāršākais simetriskais raksts."),

    Varianti("Kā sanāk simetrisks raksts?", [
        {"jaut": "Ko dara vispirms, zīmējot simetrisku rakstu?",
         "opcijas": ["Sadala riņķi vienādās daļās", "Iekrāso",
                     "Zīmē ziedlapiņas", "Mēra ar lineālu"],
         "pareizi": 0,
         "padoms": "Vienādas daļas ir pamats."},
        {"jaut": "Cik grādu ir viena daļa, ja riņķi dala 6 daļās?",
         "opcijas": ["60°", "36°", "72°", "90°"],
         "pareizi": 0,
         "padoms": "360 : 6."},
        {"jaut": "Cik reižu rādiuss ietilpst riņķa līnijā?",
         "opcijas": ["6", "4", "8", "3"],
         "pareizi": 0,
         "padoms": "Tāpēc sešas daļas var atzīmēt bez rēķina."},
        {"jaut": "Kas ir riņķa līnijas ar kopīgu centru?",
         "opcijas": ["Līnijas ar vienu centru un dažādiem rādiusiem",
                     "Līnijas ar vienu rādiusu",
                     "Divi riņķi blakus",
                     "Divi diametri"],
         "pareizi": 0,
         "padoms": "Mērķa raksts."},
        {"jaut": "Kāpēc raksts sanāk simetrisks?",
         "opcijas": ["Visas daļas ir vienādas", "Tas ir skaists",
                     "Cirkulis ir precīzs", "Tas nav simetrisks"],
         "pareizi": 0,
         "padoms": "Vienāds elements katrā daļā."},
        {"jaut": "Riņķi sadala 4 daļās. Cik grādu ir katra?",
         "opcijas": ["90°", "45°", "60°", "120°"],
         "pareizi": 0,
         "padoms": "360 : 4."},
    ], pamats=4),

    Pasaule("Raksts uz šķīvja",
            Ievadi("", [
                {"jaut": "Šķīvja malā jāizvieto 12 vienādi zīmējumi. Cik "
                         "grādu ir starp tiem?",
                 "atb": ["30"], "padoms": "360 : 12."},
                {"jaut": "Uz cita šķīvja 9 zīmējumi. Cik grādu ir starp "
                         "tiem?",
                 "atb": ["40"], "padoms": "360 : 9."},
                {"jaut": "Starp zīmējumiem ir 60°. Cik zīmējumu ir uz "
                         "šķīvja?",
                 "atb": ["6"], "padoms": "360 : 60."},
                {"jaut": "Starp zīmējumiem ir 24°. Cik zīmējumu ir?",
                 "atb": ["15"], "padoms": "360 : 24."},
            ]),
            pavediens="maja",
            konteksts="Keramikas un audumu rakstos elementi vienmēr ir "
                      "izvietoti vienādos leņķos.",
            kapec="Skaistumu te nodrošina dalīšana, nevis acumērs."),

    Kopsavilkums([
        "Sadalu riņķi vienādās daļās, dalot 360° ar daļu skaitu.",
        "Zinu, ka rādiuss riņķa līnijā ietilpst sešas reizes.",
        "Zīmēju riņķa līnijas ar kopīgu centru.",
        "Veidoju simetrisku rakstu, katrā daļā atkārtojot vienu elementu.",
    ]),

    Majas([
        "Uzzīmē ziedu ar sešām ziedlapiņām, lietojot vienu cirkuļa atvērumu.",
        "Uzzīmē mērķa rakstu no trim riņķa līnijām ar kopīgu centru.",
        "Aprēķini, cik grādu būtu starp 18 vienādiem rakstiem.",
    ]),
]
