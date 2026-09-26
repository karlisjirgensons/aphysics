# -*- coding: utf-8 -*-
"""3. klase, 18. stunda: «Vienādās daļās vai pa vienādi?»

Vienam rēķinam 24 : 4 ir divas pilnīgi dažādas dzīves nozīmes: sadalīt četrās
daļās vai izdalīt pa četriem. Skaitlis abos gadījumos ir 6, bet atbilde uz
jautājumu «kas ir 6?» - dažāda. Šo atšķirību bez piemēra nesaprot.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         restis)

TEMA = "Vienādās daļās vai pa vienādi?"

MERKIS = ("Skaidrosim abas dalīšanas nozīmes ar praktisku piemēru un "
          "pateiksim, ko nozīmē iegūtais skaitlis.")

SATURS = [
    Sakums("Kas ir tie 6 - šķīvji vai plāceņi?",
           zimejums=restis([["24 : 4", "= 6"],
                            ["4 šķīvji", "6 katrā"],
                            ["pa 4 katrā", "6 šķīvji"]],
                           "viens rēķins, divas nozīmes"),
           paraksts="Skaitlis ir tas pats, bet stāsts - cits.",
           fakti=["Dalīt var divējādi: vienādās daļās vai pa vienādi.",
                  "Rēķins abos gadījumos izskatās vienāds."]),

    Doma("Dalīšanai ir divas nozīmes",
         "Vai zināms *daļu skaits*, vai zināms *daļas lielums* - un atbilde "
         "nozīmē to otro.",
         soli=[
             "Izlasi uzdevumu un atrodi, kas ir zināms.",
             "Ja zināms, cik ir daļu, atbilde būs vienas daļas lielums.",
             "Ja zināms, cik liela ir viena daļa, atbilde būs daļu skaits.",
             "Pieraksti atbildi kopā ar vārdu: «6 plāceņi» vai «6 šķīvji».",
         ],
         pieze="Tieši tāpēc atbildē vienmēr raksta arī vārdu. Skaitlis bez "
               "vārda neatbild uz uzdevuma jautājumu."),

    Slidnis("Viens rēķins, divi stāsti",
            soli=[
                {"v": "24 plāceņi", "teksts": "Tik daudz ir jāsadala.",
                 "josla": 25},
                {"v": "4 šķīvji", "teksts": "Zināms daļu skaits. "
                                            "Meklē, cik katrā.",
                 "josla": 50},
                {"v": "24 : 4 = 6", "teksts": "Katrā šķīvī 6 plāceņi.",
                 "josla": 75},
                {"v": "pa 4 katrā", "teksts": "Tagad zināms daļas lielums. "
                                              "Meklē šķīvju skaitu.",
                 "josla": 90},
                {"v": "24 : 4 = 6", "teksts": "Vajag 6 šķīvjus.",
                 "josla": 100},
            ],
            ievads="Spied soļus un seko, kas katrā stāstā ir zināms."),

    Paraugs("Ko nozīmē atbilde?",
            uzd="30 ābolus salika 5 grozos pa vienādi. Cik ābolu ir vienā "
                "grozā?",
            soli=[
                ("Zināms daļu skaits: 5 grozi",
                 "Tātad meklējam vienas daļas lielumu."),
                ("30 : 5 = 6",
                 "Izdala kopskaitu ar grozu skaitu."),
                ("6 āboli vienā grozā",
                 "Atbildē raksta arī vārdu - citādi nav skaidrs, kas ir 6."),
            ],
            atbilde="6 āboli katrā grozā"),

    Ievadi("Ko meklē uzdevums?", [
        {"jaut": "36 konfektes sadala 6 bērniem. Cik konfekšu saņem katrs?",
         "atb": ["6"], "padoms": "36 : 6 - zināms bērnu skaits."},
        {"jaut": "36 konfektes liek maisiņos pa 6. Cik maisiņu vajag?",
         "atb": ["6"], "padoms": "36 : 6 - zināms maisiņa lielums."},
        {"jaut": "42 kūkas liek uz 7 paplātēm. Cik kūku ir uz vienas?",
         "atb": ["6"], "padoms": "42 : 7."},
        {"jaut": "42 kūkas liek uz paplātēm pa 7. Cik paplāšu vajag?",
         "atb": ["6"], "padoms": "42 : 7."},
        {"jaut": "56 olas liek kastēs pa 8. Cik kastu vajag?",
         "atb": ["7"], "padoms": "56 : 8."},
        {"jaut": "56 olas sadala 8 receptēm. Cik olu vajag vienai receptei?",
         "atb": ["7"], "padoms": "56 : 8."},
    ], pamats=4,
        ievads="Skaitlis mēdz sakrist - svarīgi ir saprast, *ko* tas nozīmē."),

    Zimejums("Divi sadalījumi ar to pašu rēķinu",
             restis([["●●●●●●", "●●●●●●", "●●●●●●", "●●●●●●"],
                     ["4 grupas pa 6", "", "", ""]],
                    "24 : 4 = 6"),
             paskaidro="Ja četras grupas ir zināmas, 6 ir grupas lielums; ja "
                       "zināms, ka grupā ir 4, tad 6 būtu grupu skaits.",
             ievads="Vieni un tie paši punktiņi der abiem stāstiem."),

    Varianti("Ko nozīmē skaitlis atbildē?", [
        {"jaut": "«45 lapas sadala 9 bērniem» - ko nozīmē 45 : 9 = 5?",
         "opcijas": ["Katrs saņem 5 lapas", "Ir 5 bērni",
                     "Ir 5 kaudzītes pa 9", "Paliek pāri 5 lapas"],
         "pareizi": 0, "padoms": "Zināms bērnu skaits, meklē daļas lielumu."},
        {"jaut": "«45 lapas saliek kaudzītēs pa 9» - ko nozīmē 45 : 9 = 5?",
         "opcijas": ["Sanāk 5 kaudzītes", "Katrā kaudzītē 5 lapas",
                     "Ir 5 bērni", "Paliek pāri 5 lapas"],
         "pareizi": 0, "padoms": "Zināms kaudzītes lielums, meklē skaitu."},
        {"jaut": "Kurš jautājums *nav* dalīšanas uzdevums?",
         "opcijas": ["Cik kopā ir 6 grupās pa 4?",
                     "Cik grupu sanāks pa 4?",
                     "Cik ir katrā no 4 grupām?",
                     "Cik reižu 4 ietilpst 24?"],
         "pareizi": 0, "padoms": "Tur meklē kopskaitu, nevis daļu."},
        {"jaut": "Kāpēc atbildē raksta arī vārdu?",
         "opcijas": ["Citādi nav skaidrs, ko skaitlis nozīmē",
                     "Tā ir tradīcija", "Lai atbilde būtu garāka",
                     "Lai pārbaudītu pareizrakstību"],
         "pareizi": 0, "padoms": "Viens skaitlis der abiem stāstiem."},
    ], pamats=4),

    Pasaule("Kā sadalīt ēdienu uz galda?",
            Ievadi("", [
                {"jaut": "Uz galda ir 36 kotletes un 6 cilvēki. Cik kotlešu "
                         "saņem katrs?",
                 "atb": ["6"], "padoms": "36 : 6."},
                {"jaut": "Pavārs liek kotletes uz šķīvjiem pa 4. Cik šķīvju "
                         "vajag 36 kotletēm?",
                 "atb": ["9"], "padoms": "36 : 4."},
                {"jaut": "Zupu lej 8 bļodās pa vienādi, kopā 48 karotes. Cik "
                         "karošu ir vienā bļodā?",
                 "atb": ["6"], "padoms": "48 : 8."},
                {"jaut": "Ja katram vajag 6 karotes, cik cilvēkiem pietiks ar "
                         "48 karotēm zupas?",
                 "atb": ["8"], "padoms": "48 : 6."},
            ]),
            pavediens="virtuve",
            konteksts="Virtuvē vienmēr jāzina abi jautājumi: cik cilvēku un "
                      "cik liela ir viena porcija.",
            kapec="Viens no tiem skaitļiem vienmēr ir zināms - otru izrēķina."),

    Kopsavilkums([
        "Zinu abas dalīšanas nozīmes un atšķiru tās uzdevumā.",
        "Pateicu, ko nozīmē iegūtais skaitlis.",
        "Rakstu atbildē arī vārdu, ne tikai skaitli.",
        "Modelēju abus sadalījumus ar priekšmetiem vai zīmējumu.",
    ]),

    Majas([
        "Sadali 20 lietas mājās vispirms 4 vienādās daļās, tad pa 4.",
        "Uzraksti divus uzdevumus ar vienu un to pašu rēķinu 30 : 5.",
        "Pastāsti mājiniekiem, kāpēc atbildē vajadzīgs vārds.",
    ]),
]
