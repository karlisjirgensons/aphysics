# -*- coding: utf-8 -*-
"""6. klase, 136. stunda: «Kā pierakstīt izteiksmi citādi?»

Jauns mikrotemats. Vienu izteiksmi var uzrakstīt daudzos veidos, un dažs no
tiem ir daudz ērtāks rēķināšanai. Tā ir prasme, kas 7. klasē kļūs par
izteiksmju pārveidošanu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā pierakstīt izteiksmi citādi?"

MERKIS = ("Pierakstīsim vienu izteiksmi vairākos veidos, nemainot tās "
          "vērtību.")

SATURS = [
    Sakums("Viena vērtība, daudzi pieraksti",
           zimejums=restis([["7 − 3", "7 + (−3)", "−3 + 7", "4"]]),
           paraksts="Visi četri pieraksti apzīmē vienu un to pašu skaitli.",
           fakti=["Atņemšanu var pierakstīt kā saskaitīšanu.",
                  "Saskaitāmos drīkst mainīt vietām.",
                  "Iekavas var pievienot vai noņemt, ja vērtība nemainās."]),

    Doma("Pārveido tā, lai būtu ērtāk",
         "Izteiksmi pārraksta, lietojot trīs atļautas darbības: atņemšanu "
         "aizstāj ar saskaitīšanu, saskaitāmos maina vietām, sagrupē tos ar "
         "iekavām.",
         soli=[
             "Pārraksti visas atņemšanas kā saskaitīšanas.",
             "Ja vajag, maini saskaitāmos vietām.",
             "Sagrupē ar iekavām tos, kurus ērti saskaitīt kopā.",
             "Pārbaudi, vai vērtība nav mainījusies.",
             "Izvēlies to pierakstu, kurā rēķināt visērtāk.",
         ],
         pieze="Pārveidošanas mērķis nav skaistums, bet ērtums: "
               "−7 + 15 + 7 ērtāk ir kā (−7 + 7) + 15, jo pirmā iekava dod "
               "nulli."),

    Paraugs("Pārraksti ērtāk",
            uzd="Pārraksti ērtāk un izrēķini −7 + 15 + 7.",
            soli=[
                ("Saskaitāmie: −7; 15; 7",
                 "Visi ar zīmēm."),
                ("Maina vietām: −7 + 7 + 15",
                 "Pretējie blakus."),
                ("Sagrupē: (−7 + 7) + 15",
                 "Iekava dod nulli."),
                ("0 + 15 = 15",
                 "Viena darbība."),
            ],
            atbilde="15"),

    Ievadi("Pārraksti un izrēķini", [
        {"jaut": "Cik ir −7 + 15 + 7?",
         "atb": ["15"], "padoms": "Pretēju skaitļu pāris."},
        {"jaut": "Cik ir 12 − 9 + (−12)?",
         "atb": ["-9", "−9"], "padoms": "12 un −12."},
        {"jaut": "Cik ir −5 + 8 + 5 + (−8)?",
         "atb": ["0"], "padoms": "Divi pāri."},
        {"jaut": "Cik ir 20 − 7 − 13?",
         "atb": ["0"], "padoms": "7 + 13 = 20."},
        {"jaut": "Cik ir −3 + 11 − (−3)?",
         "atb": ["11"], "padoms": "−3 un 3."},
        {"jaut": "Cik ir 6 − 14 + 14?",
         "atb": ["6"], "padoms": "−14 un 14."},
    ], pamats=4,
        ievads="Vispirms meklē, ko var pārveidot - tikai tad rēķini."),

    Varianti("Vai pieraksts ir tas pats?", [
        {"jaut": "7 − 3 ir tas pats, kas...",
         "opcijas": ["−3 + 7", "3 − 7", "−7 + 3", "−7 − 3"],
         "pareizi": 0,
         "padoms": "Saskaitāmos drīkst mainīt vietām."},
        {"jaut": "−5 + 9 ir tas pats, kas...",
         "opcijas": ["9 − 5", "5 − 9", "−9 + 5", "−9 − 5"],
         "pareizi": 0,
         "padoms": "Pārraksti kā atņemšanu."},
        {"jaut": "Kurš pārveidojums *nav* atļauts?",
         "opcijas": ["Mainīt mazināmo un mazinātāju vietām",
                     "Mainīt saskaitāmos vietām",
                     "Aizstāt atņemšanu ar saskaitīšanu",
                     "Sagrupēt saskaitāmos"],
         "pareizi": 0,
         "padoms": "7 − 3 nav 3 − 7."},
        {"jaut": "Izteiksmi −8 + 12 + 8 ērtāk rēķināt kā...",
         "opcijas": ["(−8 + 8) + 12", "−8 + (12 + 8)",
                     "(−8 + 12) + 8", "no kreisās uz labo"],
         "pareizi": 0,
         "padoms": "Pirmā iekava dod nulli."},
    ], pamats=4),

    Pasaule("Kā ātrāk saskaitīt čeku?",
            Ievadi("", [
                {"jaut": "Čekā: +18; −25; −18; +40 €. Cik eiro ir kopā?",
                 "atb": ["15"], "padoms": "18 un −18 izsvītrojas."},
                {"jaut": "Čekā: −30; +12; +30 €. Cik eiro ir kopā?",
                 "atb": ["12"], "padoms": "−30 un 30."},
                {"jaut": "Čekā: +50; −14; −36 €. Cik eiro ir kopā?",
                 "atb": ["0"], "padoms": "14 + 36 = 50."},
                {"jaut": "Čekā: −9; +25; +9; −25 €. Cik eiro ir kopā?",
                 "atb": ["0"], "padoms": "Divi pāri."},
            ]),
            pavediens="veikals",
            konteksts="Garā čekā bieži ir atgriezti maksājumi - tos var "
                      "izsvītrot, pirms sāc saskaitīt.",
            kapec="Pārveidošana ietaupa laiku un samazina kļūdu iespēju."),

    Zimejums("Trīs pieraksti, viena vērtība",
             restis([["−7 + 15 + 7", "(−7 + 7) + 15", "15"]]),
             paskaidro="Visi trīs pieraksti ir viens un tas pats skaitlis. "
                       "Otrais ir visērtākais.",
             ievads="Pārveidošana nemaina vērtību."),

    Kopsavilkums([
        "Pierakstu vienu izteiksmi vairākos veidos.",
        "Aizstāju atņemšanu ar saskaitīšanu.",
        "Mainu saskaitāmos vietām un grupēju tos.",
        "Izvēlos pierakstu, kurā rēķināt visērtāk.",
    ]),

    Majas([
        "Pārraksti trīs veidos izteiksmi 9 − 4 + (−9).",
        "Izrēķini to visērtākajā veidā.",
        "Atrodi čekā vai pierakstos divus skaitļus, kurus var izsvītrot.",
    ]),
]
