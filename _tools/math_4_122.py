# -*- coding: utf-8 -*-
"""4. klase, 122. stunda: «Kāda daļa no 10 centimetriem?»

Lineāla modelis: 10 cm = 100 mm, un daļas no tā ir redzamas milimetros.
{1|2} no 10 cm = 5 cm, {1|5} = 2 cm, {1|4} = 25 mm. Skolēns mēra un
apkopo rezultātus - arī tad, ja atbilde nav vesels centimetru skaits.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, restis, taisne)

TEMA = "Kāda daļa no 10 centimetriem?"

MERKIS = ("Ar lineālu noteiksim dažādu daļu vērtību no 10 cm un apkoposim "
          "rezultātus.")

SATURS = [
    Sakums("Kā sadalīt 10 cm četrās daļās?",
           zimejums=taisne(0, 10, 1, [(2.5, "1/4")], sikas=2),
           paraksts="{1|4} no 10 cm = 2 cm 5 mm = 25 mm.",
           fakti=["10 cm nedalās ar 4 veselos centimetros.",
                  "Bet 100 mm dalās: 100 : 4 = 25 mm."]),

    Doma("Pārvērt milimetros, ja centimetri nedalās",
         "Daļu no garuma atrod, dalot ar saucēju; ja centimetros nesanāk "
         "vesels skaitlis, pārvērš milimetros.",
         soli=[
             "{1|2} no 10 cm = 10 : 2 = 5 cm.",
             "{1|5} no 10 cm = 2 cm.",
             "{1|4} no 10 cm: 100 mm : 4 = 25 mm.",
             "{3|4} no 10 cm = 3 · 25 = 75 mm = 7 cm 5 mm.",
         ],
         pieze="Ar lineālu to var pārbaudīt: 25 mm ir 2 cm un vēl puse "
               "centimetra."),

    Paraugs("{3|5} no 10 cm",
            uzd="Cik ir {3|5} no 10 cm?",
            soli=[
                ("{1|5} no 10 cm = 2 cm", None),
                ("{3|5} = 3 · 2 = 6 cm", None),
            ],
            atbilde="6 cm"),

    Petijums("Mēri ar lineālu",
             soli=[
                 "Uzzīmē nogriezni 10 cm.",
                 "Atzīmē {1|2}, {1|5}, {1|4} un {1|10} no tā.",
                 "Izmēri katru daļu milimetros.",
                 "Pieraksti tabulā un pārbaudi ar dalīšanu.",
             ],
             vajag="lineāls ar milimetriem, zīmulis",
             secinajums="Milimetros visas šīs daļas ir veseli skaitļi."),

    Ievadi("Daļas no 10 cm", [
        {"jaut": "{1|2} no 10 cm = ? cm", "atb": ["5"], "padoms": "10 : 2."},
        {"jaut": "{1|10} no 10 cm = ? cm", "atb": ["1"], "padoms": "10 : 10."},
        {"jaut": "{1|4} no 10 cm = ? mm", "atb": ["25"],
         "padoms": "100 mm : 4."},
        {"jaut": "{3|4} no 10 cm = ? mm", "atb": ["75"], "padoms": "3 · 25."},
        {"jaut": "{2|5} no 10 cm = ? cm", "atb": ["4"], "padoms": "2 · 2."},
        {"jaut": "{1|20} no 10 cm = ? mm", "atb": ["5"],
         "padoms": "100 : 20."},
    ], pamats=4),

    Varianti("Mērījums un daļa", [
        {"jaut": "7 cm no 10 cm ir ...",
         "opcijas": ["{7|10}", "{3|10}", "{1|7}", "{10|7}"], "pareizi": 0,
         "padoms": "7 no 10."},
        {"jaut": "5 mm no 10 cm ir ...",
         "opcijas": ["{5|100}", "{5|10}", "{1|5}", "{1|2}"], "pareizi": 0,
         "padoms": "10 cm = 100 mm."},
        {"jaut": "Kurš garums ir {1|2} no 10 cm?",
         "opcijas": ["50 mm", "5 mm", "20 mm", "500 mm"], "pareizi": 0,
         "padoms": "5 cm = 50 mm."},
    ]),

    Pasaule("Mazie objekti dabā",
            Ievadi("", [
                {"jaut": "Tauriņa spārnu plētums 10 cm, viens spārns ir "
                         "{1|2}. Cik cm?",
                 "atb": ["5"], "padoms": "10 : 2."},
                {"jaut": "Kāpurs ir {1|4} no 10 cm. Cik mm?", "atb": ["25"],
                 "padoms": "100 : 4."},
                {"jaut": "Skudra ir {1|20} no 10 cm. Cik mm?", "atb": ["5"],
                 "padoms": "100 : 20."},
                {"jaut": "Gliemezis ir {3|10} no 10 cm. Cik cm?",
                 "atb": ["3"], "padoms": "3 · 1."},
            ]),
            pavediens="daba",
            konteksts="Biologi mazus dzīvniekus mēra milimetros - jo "
                      "centimetri tiem ir par lieliem.",
            kapec="Milimetri ļauj precīzi izteikt mazas daļas."),

    Kopsavilkums([
        "Aprēķinu daļu no 10 cm.",
        "Pārvēršu milimetros, ja centimetros nesanāk vesels.",
        "Pārbaudu ar lineālu.",
    ]),

    Majas([
        "Izmēri 3 mazus priekšmetus un izsaki tos kā daļu no 10 cm.",
        "Uzzīmē 10 cm nogriezni un atzīmē {3|10}, {1|2} un {4|5}.",
        "Paskaidro, kāpēc {1|4} no 10 cm ērtāk rēķināt milimetros.",
    ]),
]
