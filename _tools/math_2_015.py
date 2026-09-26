# -*- coding: utf-8 -*-
"""2. klase, 15. stunda: «Kā mērīja senāk?»

Senās mērvienības ņēma no cilvēka ķermeņa: olekts, sprīdis, pēda, solis.
Tās bija ērtas, bet katram cilvēkam dažādas - tieši tāpēc vienojās par
metru, kas visur ir vienāds.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, restis)

TEMA = "Kā mērīja senāk?"

MERKIS = ("Šodien iepazīsim senās mērvienības, salīdzināsim tās ar metru un "
          "sapratīsim, kāpēc vajadzīga vienota mērvienība.")

_SENAS = restis([["mērvienība", "no kā", "apmēram"],
                 ["sprīdis", "īkšķis - mazais pirksts", "20 cm"],
                 ["pēda", "pēdas garums", "30 cm"],
                 ["olekts", "elkonis - pirkstu gals", "50 cm"],
                 ["solis", "viens solis", "70 cm"]])

SATURS = [
    Sakums("Kāpēc audums, nopirkts vienā tirgū, bija garāks nekā otrā?",
           zimejums=_SENAS,
           paraksts="Senās mērvienības nāca no cilvēka ķermeņa.",
           fakti=["Audumu mērīja olektīs - no elkoņa līdz pirkstu galam.",
                  "Garam tirgotājam olekts bija garāka!",
                  "Tāpēc pirms vairāk nekā 200 gadiem izdomāja metru."]),

    Doma("Vienota mērvienība",
         "Metrs visur ir vienāds, tāpēc visi mērījumi sakrīt.",
         soli=[
             "Senās vienības bija ērtas - tās vienmēr ir līdzi.",
             "Bet katram cilvēkam tās ir citādas.",
             "Metrs visā pasaulē ir tieši tik garš.",
             "Tāpēc mūsdienās mēra metros un centimetros.",
         ]),

    Petijums("Tava olekts un sprīdis", [
        "Izmēri savu sprīdi centimetros.",
        "Izmēri savu olekti.",
        "Salīdzini ar klasesbiedru un ar skolotāju.",
        "Izmēri galdu savos sprīžos. Vai visiem sanāk vienādi?",
    ], vajag="mērlente vai lineāls",
             secinajums="Sprīži ir dažādi, tāpēc galds sanāk dažāds - "
                        "centimetros visiem vienāds."),

    Ievadi("Rēķini senās vienībās", [
        {"jaut": "Sprīdis ir apmēram 20 cm. Cik cm ir 2 sprīži?",
         "zim": _SENAS, "atb": ["40"], "padoms": "20 + 20."},
        {"jaut": "Olekts ir apmēram 50 cm. Cik olektis ir 1 metrā?",
         "zim": _SENAS, "atb": ["2"], "padoms": "50 + 50 = 100."},
        {"jaut": "Cik sprīžu ir apmēram 1 metrā?", "zim": _SENAS,
         "atb": ["5"], "padoms": "Skaiti pa 20 līdz 100."},
        {"jaut": "Par cik cm pēda ir garāka nekā sprīdis?", "zim": _SENAS,
         "atb": ["10"], "padoms": "30 − 20."},
    ]),

    Varianti("Kāpēc metrs?", [
        {"jaut": "Kāpēc mūsdienās nemēra olektīs?",
         "opcijas": ["Katram cilvēkam olekts ir cita",
                     "Olekts ir par garu", "Olekts ir par īsu"],
         "pareizi": 0, "padoms": "Salīdzini savu un skolotāja olekti."},
        {"jaut": "Kur mūsdienās vēl lieto pēdas?",
         "opcijas": ["Lidmašīnu lidojuma augstumā",
                     "Latvijas ceļa zīmēs", "Skolas lineālā"],
         "pareizi": 0,
         "padoms": "Piloti augstumu mēra pēdās."},
    ]),

    Pasaule("Cik soļu līdz skolai?",
            Varianti("", [
                {"jaut": "Tētis līdz vārtiem aiziet 10 soļos, tu - 14 "
                         "soļos. Kura solis ir īsāks?",
                 "opcijas": ["mans solis", "tēta solis", "vienādi"],
                 "pareizi": 0, "padoms": "Kurš sper vairāk soļu?"},
                {"jaut": "Tēta solis ir apmēram 70 cm. Cik ir 2 tēta soļi?",
                 "opcijas": ["140 cm", "72 cm", "70 cm"], "pareizi": 0,
                 "padoms": "70 + 70."},
            ]),
            pavediens="celojums",
            konteksts="Ar soļiem joprojām ātri novērtē attālumu.",
            kapec="Soļi der aptuvenam mērījumam, metri - precīzam."),

    Kopsavilkums([
        "Zinu senās mērvienības: sprīdis, pēda, olekts, solis.",
        "Salīdzinu tās ar centimetriem.",
        "Paskaidroju, kāpēc vajag vienotu mērvienību.",
    ]),

    Majas([
        "Izmēri gultu savos sprīžos un mājinieka sprīžos.",
        "Kāpēc sanāk dažādi skaitļi?",
        "Izmēri gultu centimetros.",
    ]),
]
