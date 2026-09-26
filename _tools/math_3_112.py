# -*- coding: utf-8 -*-
"""3. klase, 112. stunda: «Kā uzzīmēt riņķi?»

Mikrotemata noslēgums. Riņķa līnija ir vienīgā figūra, ko nosaka viens
skaitlis - rādiuss. Cirkulis to arī parāda: attālums no centra ir tas, kas
paliek nemainīgs, kamēr zīmulis iet apkārt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         rinkis)

TEMA = "Kā uzzīmēt riņķi?"

MERKIS = ("Zīmēsim riņķi ar cirkuli un skaidrosim, ka riņķa lielumu nosaka "
          "rādiuss.")

SATURS = [
    Sakums("Kāpēc ritenis ir apaļš?",
           zimejums=rinkis(radiuss="r", virsraksts="riņķa līnija",
                           paraksts="r - rādiuss"),
           fakti=["Visi riņķa līnijas punkti ir vienādā attālumā no centra.",
                  "Šo attālumu sauc par rādiusu.",
                  "Riņķa lielumu nosaka tikai rādiuss."]),

    Doma("Rādiuss nosaka riņķi",
         "Riņķa līnija ir visi punkti, kas atrodas vienādā attālumā no "
         "centra; šis attālums ir rādiuss.",
         soli=[
             "Atzīmē centru.",
             "Ieregulē cirkulī vajadzīgo rādiusu pēc lineāla.",
             "Iedur cirkuļa adatu centrā.",
             "Apgriez cirkuli vienu apli, adatu nekustinot.",
         ],
         pieze="Ja cirkuļa atvērums mainās zīmēšanas laikā, līnija vairs nav "
               "riņķis - tāpēc adatu tur cieši."),

    Petijums("Uzzīmē trīs riņķus",
             vajag="cirkulis, lineāls un lapa",
             soli=[
                 "Atzīmē lapas vidū punktu - centru.",
                 "Uzzīmē riņķi ar rādiusu 2 cm.",
                 "Ap to pašu centru uzzīmē riņķi ar rādiusu 4 cm.",
                 "Un vēl vienu ar rādiusu 6 cm.",
             ],
             secinajums="Visiem trim centrs ir viens, bet lielums dažāds - "
                        "to nosaka tikai rādiuss."),

    Paraugs("Cik garš ir diametrs?",
            uzd="Riņķa rādiuss ir 4 cm. Cik garš ir diametrs?",
            soli=[
                ("Diametrs iet caur centru",
                 "Tas savieno divus pretējus riņķa līnijas punktus."),
                ("Diametrs ir divi rādiusi",
                 "No centra uz vienu pusi un uz otru."),
                ("2 · 4 = 8",
                 "Diametrs ir 8 cm."),
            ],
            atbilde="8 cm"),

    Ievadi("Rādiuss un diametrs", [
        {"jaut": "Rādiuss ir 4 cm. Cik centimetru ir diametrs?",
         "atb": ["8"], "padoms": "2 · 4."},
        {"jaut": "Diametrs ir 10 cm. Cik centimetru ir rādiuss?",
         "atb": ["5"], "padoms": "10 : 2."},
        {"jaut": "Rādiuss ir 7 cm. Cik centimetru ir diametrs?",
         "atb": ["14"], "padoms": "2 · 7."},
        {"jaut": "Diametrs ir 18 cm. Cik centimetru ir rādiuss?",
         "atb": ["9"], "padoms": "18 : 2."},
        {"jaut": "Rādiuss ir 12 cm. Cik centimetru ir diametrs?",
         "atb": ["24"], "padoms": "2 · 12."},
        {"jaut": "Riteņa diametrs 60 cm. Cik centimetru ir rādiuss?",
         "atb": ["30"], "padoms": "60 : 2."},
    ], pamats=4),

    Zimejums("Diametrs",
             rinkis(diametrs="d", virsraksts="diametrs",
                    paraksts="d = 2 · r"),
             paskaidro="Diametrs iet caur centru un ir divreiz garāks par "
                       "rādiusu.",
             ievads="Otra riņķa mērījums."),

    Varianti("Kas nosaka riņķi?", [
        {"jaut": "Kas nosaka riņķa lielumu?",
         "opcijas": ["Rādiuss", "Centra vieta", "Krāsa", "Lapas izmērs"],
         "pareizi": 0, "padoms": "Attālums no centra."},
        {"jaut": "Cik reižu diametrs ir garāks par rādiusu?",
         "opcijas": ["2", "3", "4", "Tikpat"],
         "pareizi": 0, "padoms": "Divi rādiusi."},
        {"jaut": "Kur atrodas riņķa līnijas punkti?",
         "opcijas": ["Vienādā attālumā no centra", "Tuvu centram",
                     "Tālu no centra", "Dažādos attālumos"],
         "pareizi": 0, "padoms": "Tā ir riņķa definīcija."},
        {"jaut": "Riteņa rādiuss ir 35 cm. Cik centimetru ir diametrs?",
         "opcijas": ["70", "17", "35", "140"],
         "pareizi": 0, "padoms": "2 · 35."},
    ], pamats=4),

    Pasaule("Cik lieli ir riteņi?",
            Ievadi("", [
                {"jaut": "Velosipēda riteņa rādiuss ir 30 cm. Cik "
                         "centimetru ir diametrs?",
                 "atb": ["60"], "padoms": "2 · 30."},
                {"jaut": "Auto riteņa diametrs ir 70 cm. Cik centimetru ir "
                         "rādiuss?",
                 "atb": ["35"], "padoms": "70 : 2."},
                {"jaut": "Par cik centimetriem auto ritenis ir platāks par "
                         "velosipēda riteni?",
                 "atb": ["10"], "padoms": "70 − 60."},
                {"jaut": "Cik riteņu ir 8 velosipēdiem?", "atb": ["16"],
                 "padoms": "8 · 2."},
            ]),
            pavediens="tehnika",
            konteksts="Riteņa izmēru vienmēr saka kā diametru - tāpēc, "
                      "pērkot riepu, jāzina tieši tas skaitlis.",
            kapec="Ritenis rit vienmērīgi tikai tāpēc, ka visi tā punkti ir "
                  "vienādā attālumā no ass."),

    Kopsavilkums([
        "Zīmēju riņķi ar cirkuli.",
        "Zinu, ka riņķa lielumu nosaka rādiuss.",
        "Zinu, ka diametrs ir divi rādiusi.",
        "Aprēķinu rādiusu no diametra un otrādi.",
    ]),

    Majas([
        "Uzzīmē trīs riņķus ar vienu centru un dažādiem rādiusiem.",
        "Izmēri kāda mājas priekšmeta diametru un izrēķini rādiusu.",
        "Atrodi mājās piecus apaļus priekšmetus.",
    ]),
]
