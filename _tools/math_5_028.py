# -*- coding: utf-8 -*-
"""5. klase, 28. stunda: «Kā pierakstīt nezināmo reizinājumā?»

21. stundas turpinājums: tur nezināmais stāvēja summā un starpībā, te tas
nonāk reizinājumā un dalījumā. Jaunas domas nav - ir tikai trīs jaunas
kārtulas, un katru no tām var atvasināt no pārbaudes, nevis iekalt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā pierakstīt nezināmo reizinājumā?"

MERKIS = ("Iemācīsimies aprēķināt nezināmo skaitli reizinājuma vai dalījuma "
          "vienādībā, apzīmējot to ar burtu.")

SATURS = [
    Sakums("Cik paciņās salika konfektes?",
           fakti=["Konfektes salika vienādās paciņās - kopā 91 konfekte.",
                  "Katrā paciņā ir 7 konfektes.",
                  "x · 7 = 91. Cik paciņu sanāca?"]),

    Doma("Nezināmo atrod ar pretējo darbību",
         "Reizināšanu atsauc dalīšana, dalīšanu - reizināšana.",
         soli=[
             "Apzīmē nezināmo ar burtu un pasaki, ko tas nozīmē.",
             "Uzraksti vienādību pēc teksta.",
             "Nosaki, kurš loceklis ir nezināms.",
             "Nezināmo reizinātāju atrod: reizinājumu dala ar otru "
             "reizinātāju.",
             "Nezināmo dalāmo atrod: dalījumu reizina ar dalītāju.",
             "Nezināmo dalītāju atrod: dalāmo dala ar dalījumu.",
         ],
         pieze="Trīs kārtulas iekalt nevajag - pietiek ar pārbaudi. Ja "
               "x · 7 = 91 un tu domā, ka x = 13, sareizini: 13 · 7 = 91. "
               "Sakrīt, tātad pareizi."),

    Paraugs("No teksta uz vienādību",
            uzd="91 konfekti salika paciņās pa 7. Cik paciņu sanāca?",
            soli=[
                ("x - paciņu skaits",
                 "Vispirms pasaka, ko burts nozīmē."),
                ("x · 7 = 91",
                 "Katrā paciņā 7, paciņu x, kopā 91."),
                ("x = 91 : 7 = 13",
                 "Nezināms ir reizinātājs, tāpēc dala."),
                ("Pārbaude: 13 · 7 = 91",
                 "Sakrīt ar doto."),
            ],
            atbilde="sanāca 13 paciņas"),

    Ievadi("Atrodi x", [
        {"jaut": "x · 7 = 91. Cik ir x?", "atb": ["13"],
         "padoms": "91 : 7."},
        {"jaut": "6 · x = 144. Cik ir x?", "atb": ["24"],
         "padoms": "144 : 6."},
        {"jaut": "x : 8 = 12. Cik ir x?", "atb": ["96"],
         "padoms": "Nezināms ir dalāmais: 12 · 8."},
        {"jaut": "96 : x = 12. Cik ir x?", "atb": ["8"],
         "padoms": "Nezināms ir dalītājs: 96 : 12."},
        {"jaut": "x · 25 = 500. Cik ir x?", "atb": ["20"],
         "padoms": "500 : 25."},
        {"jaut": "x : 15 = 4. Cik ir x?", "atb": ["60"],
         "padoms": "4 · 15."},
        {"jaut": "120 : x = 5. Cik ir x?", "atb": ["24"],
         "padoms": "120 : 5."},
        {"jaut": "x · x = 49. Cik ir x?", "atb": ["7"],
         "padoms": "Divi vienādi reizinātāji."},
    ], pamats=4,
        ievads="Vispirms nosaki, kurš loceklis ir nezināms."),

    Varianti("Kurš loceklis ir nezināms?", [
        {"jaut": "Vienādībā 6 · x = 144 nezināms ir...",
         "opcijas": ["reizinātājs", "reizinājums", "dalāmais", "dalītājs"],
         "pareizi": 0,
         "padoms": "x ir viens no diviem, ko reizina."},
        {"jaut": "Vienādībā 96 : x = 12 nezināms ir...",
         "opcijas": ["dalītājs", "dalāmais", "dalījums", "reizinātājs"],
         "pareizi": 0,
         "padoms": "x ir tas, ar ko dala."},
        {"jaut": "Kā atrod nezināmo dalāmo?",
         "opcijas": ["Dalījumu reizina ar dalītāju",
                     "Dalījumu dala ar dalītāju",
                     "Dalītāju dala ar dalījumu",
                     "Saskaita dalījumu un dalītāju"],
         "pareizi": 0,
         "padoms": "Pārbaudi ar x : 8 = 12."},
        {"jaut": "«Domāju skaitli, reizināju ar 9 un sanāca 108.» Kura "
                 "vienādība atbilst?",
         "opcijas": ["x · 9 = 108", "x : 9 = 108", "9 : x = 108",
                     "x + 9 = 108"],
         "pareizi": 0,
         "padoms": "Nezināmo skaitli reizina ar 9."},
        {"jaut": "Kā pārbaudīt atrasto x?",
         "opcijas": ["Ierakstīt to vienādībā un izrēķināt",
                     "Pārrakstīt vienādību no jauna",
                     "Salīdzināt ar kaimiņa atbildi",
                     "Nekā - atbilde ir gatava"],
         "pareizi": 0,
         "padoms": "Vienādībai jāpaliek patiesai."},
        {"jaut": "Ja x · 7 = 91, cik ir 91 : 13?",
         "opcijas": ["7", "13", "91", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Viens reizinājums dod divus dalījumus."},
    ], pamats=4),

    Pasaule("Cik paciņās salika preci?",
            Ievadi("", [
                {"jaut": "91 konfekti salika paciņās pa 7. Cik paciņu?",
                 "atb": ["13"], "padoms": "91 : 7."},
                {"jaut": "Kastē 144 olas, kārbās pa 6. Cik kārbu?",
                 "atb": ["24"], "padoms": "144 : 6."},
                {"jaut": "Cena 25 eiro par kasti, čekā 500 eiro. Cik kastu "
                         "nopirka?",
                 "atb": ["20"], "padoms": "500 : 25."},
                {"jaut": "Maisu sadalīja 8 vienādās paciņās pa 12 kg. Cik "
                         "kilogramu bija maisā?",
                 "atb": ["96"], "padoms": "12 · 8."},
            ]),
            pavediens="veikals",
            konteksts="Veikalā bieži zināms kopskaits un cena, bet ne "
                      "gabalu skaits - tieši to apzīmē ar burtu.",
            kapec="Pretējā darbība atsauc to, kas ar nezināmo izdarīts."),

    Kopsavilkums([
        "Apzīmēju nezināmo ar burtu un uzrakstu vienādību pēc teksta.",
        "Atrodu nezināmo reizinātāju, dalot reizinājumu.",
        "Atrodu nezināmo dalāmo un dalītāju ar pretējo darbību.",
        "Pārbaudu atbildi, ierakstot to atpakaļ vienādībā.",
    ]),

    Majas([
        "Izdomā uzdevumu, kurā nezināmais ir paciņu skaits, un uzraksti "
        "vienādību.",
        "Atrisini to un pārbaudi ar reizināšanu.",
        "Uzraksti trīs vienādības ar vieniem un tiem pašiem trim skaitļiem: "
        "vienu reizinājumu un divus dalījumus.",
    ]),
]
