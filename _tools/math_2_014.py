# -*- coding: utf-8 -*-
"""2. klase, 14. stunda: «Kā izgatavot savu mērlenti?»

Praktiska stunda: no papīra sloksnēm salīmē metru garu lenti ar decimetru
un centimetru iedaļām. Gatavojot to, skolēns ar rokām pārbauda, ka 10 dm ir
tieši 1 m un 10 cm - tieši 1 dm.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, lineals, vienibas)

TEMA = "Kā izgatavot savu mērlenti?"

MERKIS = ("Šodien izgatavosim mērlenti ar m, dm un cm iedaļām un "
          "pārbaudīsim, vai tā mēra pareizi.")

SATURS = [
    Sakums("Kā izmērīt garumu, ja lineāla nav pie rokas?",
           zimejums=vienibas(10),
           paraksts="Metrs, sadalīts 10 decimetros.",
           fakti=["Pirmos metrus cilvēki gatavoja paši.",
                  "Pietiek ar papīru, lineālu un precizitāti."]),

    Doma("Lente no decimetriem",
         "Metrs ir 10 decimetri, un katrs decimetrs ir 10 centimetri.",
         soli=[
             "Sagriez 10 sloksnes, katru tieši 10 cm garu.",
             "Uz katras atzīmē 10 centimetru iedaļas.",
             "Salīmē sloksnes vienu pēc otras.",
             "Pie katras salīmējuma vietas uzraksti: 1 dm, 2 dm ... 10 dm.",
         ],
         pieze="Ja katra sloksne būs kaut par 1 mm par garu, visā lentē "
               "sakrāsies 1 cm kļūda."),

    Petijums("Izgatavo mērlenti", [
        "Ar lineālu atmēri un sagriez 10 sloksnes pa 10 cm.",
        "Katrā sloksnē atzīmē centimetrus.",
        "Salīmē sloksnes garā lentē.",
        "Salīdzini savu lenti ar skolotāja mērlenti. Vai 1 m sakrīt?",
    ], vajag="papīrs, lineāls, šķēres, līme, flomāsteris",
             secinajums="10 sloksnes pa 10 cm ir 100 cm jeb 1 m."),

    Ievadi("Lasi savu lenti", [
        {"jaut": "Pie kuras atzīmes lentē ir 30 cm? Raksti, cik dm.",
         "atb": ["3"], "padoms": "Katrs dm - 10 cm."},
        {"jaut": "Cik cm ir līdz atzīmei 6 dm?", "atb": ["60"],
         "padoms": "Seši decimetri pa 10 cm."},
        {"jaut": "Galds sniedzas līdz 7 dm un vēl 4 cm. Cik tas ir cm?",
         "atb": ["74"], "padoms": "70 + 4."},
        {"jaut": "Cik sloksnes vajag pusmetram?", "atb": ["5"],
         "padoms": "Puse no 10."},
        {"jaut": "Cik cm ir līdz atzīmei 9 dm?", "atb": ["90"],
         "padoms": "9 decimetri."},
        {"jaut": "Cik cm pietrūkst no 8 dm līdz 1 m?", "atb": ["20"],
         "padoms": "80 cm līdz 100 cm."},
    ], pamats=4),

    Varianti("Pārbaudi lenti", [
        {"jaut": "Viena sloksne iznāca 11 cm. Kas notiks ar lenti?",
         "opcijas": ["Tā būs par 1 cm par garu", "Nekas nemainīsies",
                     "Tā būs par 1 cm par īsu"], "pareizi": 0,
         "padoms": "Vienā vietā ir 1 cm par daudz."},
        {"jaut": "Kurš lineāls rāda to pašu, ko pirmā sloksne?",
         "zim": lineals(10), "opcijas": ["viss šis lineāls - 1 dm",
                                         "tikai 1 cm", "1 m"],
         "pareizi": 0, "padoms": "Lineālā ir 10 cm."},
    ]),

    Pasaule("Cik garš esi?",
            Ievadi("", [
                {"jaut": "Anna ir 1 m un 25 cm gara. Cik cm virs 1 m?",
                 "atb": ["25"], "padoms": "Nolasi atlikumu."},
                {"jaut": "Brālis ir 1 m 30 cm. Par cik cm viņš garāks "
                         "nekā Anna?", "atb": ["5"], "padoms": "30 − 25."},
            ]),
            pavediens="maja",
            konteksts="Mērlenti var pielīmēt pie durvju stenderes un "
                      "atzīmēt, kā aug ģimene.",
            kapec="Pašu lente rāda tos pašus centimetrus, ko veikalā "
                  "pirktā."),

    Kopsavilkums([
        "Izgatavoju mērlenti ar m, dm un cm iedaļām.",
        "Zinu, ka 10 dm = 1 m un 10 cm = 1 dm.",
        "Pārbaudu savu instrumentu ar īstu mērlenti.",
    ]),

    Majas([
        "Pielīmē savu lenti pie durvju stenderes.",
        "Izmēri visus mājiniekus.",
        "Pieraksti, par cik centimetriem katrs ir garāks nekā 1 m.",
    ]),
]
