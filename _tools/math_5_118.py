# -*- coding: utf-8 -*-
"""5. klase, 118. stunda: «Kā ar cirkuli atlikt vienādus nogriežņus?»

Cirkulis te pirmo reizi tiek lietots nevis riņķa zīmēšanai, bet mērīšanai.
Tā ir konstruēšana: nogriezni pārceļ, nezinot tā garumu centimetros, un
tieši tāpēc rezultāts iznāk precīzāks nekā ar lineālu. Šis paņēmiens
nākamajā stundā kļūs par raksta pamatu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         taisne)

TEMA = "Kā ar cirkuli atlikt vienādus nogriežņus?"

MERKIS = ("Iemācīsimies ar cirkuli konstruēt nogriezni, kas vienāds ar doto "
          "vai vairākas reizes garāks.")

SATURS = [
    Sakums("Cirkulis mēra, nevis zīmē",
           zimejums=taisne(0, 4, 1, [(1, "A"), (2, "B"), (3, "C")],
                           virsraksts="Trīs vienādi nogriežņi pēc kārtas"),
           paraksts="Katrs nākamais nogrieznis atlikts ar to pašu cirkuļa "
                    "atvērumu.",
           fakti=["Cirkuļa atvērums ir nogriežņa garums.",
                  "To var pārcelt, neizmērot centimetros.",
                  "Tā nogriezni var atlikt cik reižu vien vajag."]),

    Doma("Atvērumu nemaina",
         "Lai atliktu nogriezni, kas vienāds ar doto, cirkuļa kājas noliek uz "
         "dotā nogriežņa galiem un, atvērumu nemainot, atzīmē to citā vietā.",
         soli=[
             "Noliec cirkuļa adatu uz nogriežņa viena gala.",
             "Zīmuļa galu noliec uz otra gala.",
             "Neizmaini atvērumu.",
             "Uz jaunas taisnes atzīmē sākumpunktu un ar cirkuli otru galu.",
             "Vairākiem nogriežņiem atkārto soli pēc kārtas.",
         ],
         pieze="Ar cirkuli var atlikt arī nogriezni, kas ir trīs reizes "
               "garāks: atvērumu neizmaina un atzīmē trīs punktus pēc kārtas. "
               "Lineāls to izdarītu ar trim mērījumiem un trim kļūdām."),

    Petijums("Atliec nogriezni trīs reizes",
             soli=["Uzzīmē nogriezni AB, kas ir 3 cm garš.",
                   "Uzzīmē garu taisni un atzīmē uz tās punktu C.",
                   "Ar cirkuli pārcel AB garumu no C uz labo pusi.",
                   "Atkārto vēl divas reizes, neizmainot atvērumu.",
                   "Izmēri iegūto nogriezni ar lineālu."],
             vajag="cirkulis, lineāls, zīmulis",
             secinajums="Iegūtais nogrieznis ir 9 cm garš - tieši trīs reizes "
                        "garāks par doto."),

    Paraugs("Nogrieznis, trīs reizes garāks",
            uzd="Dots nogrieznis AB = 3 cm. Konstruē nogriezni, kas trīs "
                "reizes garāks.",
            soli=[
                ("Cirkuļa atvērums ir AB",
                 "Nogriežņa garums."),
                ("No punkta C atliec pirmo nogriezni",
                 "Iegūst punktu D."),
                ("No D atliec otro",
                 "Iegūst punktu E."),
                ("No E atliec trešo",
                 "Iegūst punktu F."),
                ("CF = 3 · AB = 9 cm",
                 "Trīs vienādi nogriežņi pēc kārtas."),
            ],
            atbilde="CF = 9 cm"),

    Ievadi("Cik garš iznāk nogrieznis?", [
        {"jaut": "AB = 3 cm, atliek 3 reizes. Cik centimetru ir iegūtais "
                 "nogrieznis?",
         "atb": ["9"], "padoms": "3 · 3."},
        {"jaut": "AB = 4 cm, atliek 2 reizes. Cik centimetru?",
         "atb": ["8"], "padoms": "4 · 2."},
        {"jaut": "AB = 5 cm, atliek 4 reizes. Cik centimetru?",
         "atb": ["20"], "padoms": "5 · 4."},
        {"jaut": "AB = 2{1|2} cm, atliek 2 reizes. Cik centimetru?",
         "atb": ["5"], "padoms": "2{1|2} · 2."},
        {"jaut": "Iegūtais nogrieznis ir 12 cm, atlika 4 reizes. Cik "
                 "centimetru ir AB?",
         "atb": ["3"], "padoms": "12 : 4."},
        {"jaut": "Iegūtais nogrieznis ir 15 cm, AB = 5 cm. Cik reižu atlika?",
         "atb": ["3"], "padoms": "15 : 5."},
        {"jaut": "AB = 6 cm, atliek 3 reizes. Cik centimetru?",
         "atb": ["18"], "padoms": "6 · 3."},
        {"jaut": "Cik reižu jāatliek 4 cm nogrieznis, lai iegūtu 24 cm?",
         "atb": ["6"], "padoms": "24 : 4."},
    ], pamats=4,
        ievads="Atlikts nogrieznis ir reizinājums: garums reiz reižu skaits."),

    Zimejums("Četri vienādi nogriežņi",
             taisne(0, 5, 1, [(1, "A"), (2, "B"), (3, "C"), (4, "D")],
                    virsraksts="Viens atvērums, četri punkti"),
             paskaidro="Visi attālumi starp blakus punktiem ir vienādi, jo "
                       "cirkuļa atvērums netika mainīts.",
             ievads="Tā izskatās nogriežņa atlikšana pa soļiem."),

    Varianti("Kāpēc ar cirkuli?", [
        {"jaut": "Kas ir cirkuļa atvērums?",
         "opcijas": ["Nogriežņa garums", "Riņķa laukums", "Leņķis",
                     "Diametrs"],
         "pareizi": 0,
         "padoms": "Attālums starp kājām."},
        {"jaut": "Kāpēc cirkulis ir precīzāks par lineālu?",
         "opcijas": ["Garums nav jāizlasa un jāpārliek",
                     "Cirkulis ir garāks",
                     "Lineāls ir salīcis",
                     "Tas nav precīzāks"],
         "pareizi": 0,
         "padoms": "Katrs nolasījums ir jauna kļūda."},
        {"jaut": "AB = 4 cm, atliek 5 reizes. Cik garš ir iegūtais?",
         "opcijas": ["20 cm", "9 cm", "16 cm", "45 cm"],
         "pareizi": 0,
         "padoms": "4 · 5."},
        {"jaut": "Ko nedrīkst darīt, atliekot nogriežņus?",
         "opcijas": ["Mainīt cirkuļa atvērumu", "Zīmēt taisni",
                     "Atzīmēt punktus", "Lietot zīmuli"],
         "pareizi": 0,
         "padoms": "Atvērums ir mērs."},
        {"jaut": "Kā iegūt nogriezni, kas ir puse no dotā?",
         "opcijas": ["Jāsadala tas uz pusēm", "Jāatliek divas reizes",
                     "Jāpalielina atvērums", "Tā nevar"],
         "pareizi": 0,
         "padoms": "Puse ir mazāka par doto."},
        {"jaut": "Iegūtais nogrieznis ir 18 cm, atlika 3 reizes. Cik garš "
                 "bija dotais?",
         "opcijas": ["6 cm", "9 cm", "15 cm", "54 cm"],
         "pareizi": 0,
         "padoms": "18 : 3."},
    ], pamats=4),

    Pasaule("Kā iezīmēt vienādus attālumus?",
            Ievadi("", [
                {"jaut": "Plauktā jāizurbj 5 caurumi ar 8 cm atstarpi. Cik "
                         "centimetru ir no pirmā līdz pēdējam?",
                 "atb": ["32"], "padoms": "Četras atstarpes pa 8 cm."},
                {"jaut": "Žogā stabi ik pa 2 m, pavisam 6 stabi. Cik metru "
                         "ir no pirmā līdz pēdējam?",
                 "atb": ["10"], "padoms": "Piecas atstarpes."},
                {"jaut": "Plaukts ir 24 cm garš, caurumi ik pa 6 cm. Cik "
                         "atstarpju sanāk?",
                 "atb": ["4"], "padoms": "24 : 6."},
                {"jaut": "Cik caurumu sanāk, ja atstarpju ir 4?",
                 "atb": ["5"], "padoms": "Par vienu vairāk nekā atstarpju."},
            ]),
            pavediens="maja",
            konteksts="Vienādas atstarpes iezīmē ar vienu mēru, ko pārceļ, "
                      "nevis mēra no jauna katrai vietai.",
            kapec="Tā kļūda neuzkrājas no viena cauruma uz nākamo."),

    Kopsavilkums([
        "Ar cirkuli pārceļu nogriezni, neizmērot to centimetros.",
        "Konstruēju nogriezni, kas vairākas reizes garāks par doto.",
        "Zinu, ka atvērumu atlikšanas laikā nedrīkst mainīt.",
        "Aprēķinu iegūtā nogriežņa garumu ar reizināšanu.",
    ]),

    Majas([
        "Uzzīmē 2 cm nogriezni un atliec to piecas reizes.",
        "Izmēri iegūto nogriezni un salīdzini ar aprēķinu.",
        "Padomā, kā ar cirkuli pārbaudīt, vai divi nogriežņi ir vienādi.",
    ]),
]
