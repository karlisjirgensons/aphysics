# -*- coding: utf-8 -*-
"""7. klase, 68. stunda: «Kā izpētīt sveces degšanu?»

Pētījums: sveces augstumu mēra ik pēc 10 minūtēm, datus attēlo grafikā un
novelk taisni, kas vislabāk atbilst punktiem. No taisnes nolasa, cik ātri
svece deg un kad tā izdegs - tas ir lineārs modelis.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Zimejums, plakne, restis)

TEMA = "Kā izpētīt sveces degšanu?"

MERKIS = ("Iegūsim datus par reālu procesu, attēlosim tos grafiski un "
          "raksturosim lineāru modeli.")

_DATI = [(0, 12.0), (10, 11.1), (20, 10.3), (30, 9.3), (40, 8.5),
         (50, 7.4)]

SATURS = [
    Sakums("Cik ilgi degs svece?",
           zimejums=plakne(grafiki=[(-0.09, 12, "")], punkti=_DATI,
                           no_x=0, lidz_x=60, no_y=0, lidz_y=12, solis=10,
                           solis_y=2, x_nos="min", y_nos="cm"),
           paraksts="Mērījumu punkti un taisne, kas tiem atbilst vislabāk.",
           fakti=["Svece 12 cm; mēra ik pēc 10 min.",
                  "Punkti gandrīz uz taisnes - process ir aptuveni lineārs.",
                  "No taisnes var prognozēt, kad svece izdegs."]),

    Doma("Lineārs modelis no mērījumiem",
         "Ja mērījumu punkti izvietojas gandrīz uz taisnes, procesu var "
         "aprakstīt ar lineāru funkciju. Taisni novelk tā, lai punkti būtu "
         "abās pusēs un pēc iespējas tuvāk.",
         soli=[
             "Mēri lielumu vienādos laika intervālos un pieraksti tabulā.",
             "Atzīmē punktus koordinātu plaknē.",
             "Novelc taisni, kas vislabāk atbilst punktiem.",
             "Nolasi k (ātrumu) un b (sākuma vērtību), uzraksti formulu.",
             "Izmanto formulu prognozei.",
         ],
         pieze="Modelis ir vienkāršojums: īsta svece deg nevienmērīgi, bet "
               "vidēji - gandrīz vienmērīgi."),

    Zimejums("Mērījumu tabula",
             restis([["t, min", "0", "10", "20", "30", "40", "50"],
                     ["h, cm", "12", "11,1", "10,3", "9,3", "8,5", "7,4"]]),
             paskaidro="Katrās 10 min svece kļūst īsāka par ~0,9 cm."),

    Paraugs("Izveido modeli",
            uzd="No tabulas atrodi lineāro modeli h = kt + b un prognozē, "
                "kad svece izdegs.",
            soli=[
                ("b = 12 (cm)", "Sākuma augstums."),
                ("50 min laikā: 12 − 7,4 = 4,6 (cm)", "Kopējā izmaiņa."),
                ("k ≈ −4,6 : 50 ≈ −0,09 (cm/min)", "Vidējais ātrums."),
                ("h = −0,09t + 12", "Modelis."),
                ("0 = −0,09t + 12, t ≈ 133 (min)", "Prognoze."),
            ],
            atbilde="h ≈ −0,09t + 12; svece izdegs pēc ~133 min (~2 h 13 min)"),

    Petijums("Tavs sveces eksperiments",
             ["Nomēri tējas sveces vai garas sveces augstumu (pieaugušā "
              "klātbūtnē!).",
              "Aizdedz un ik pēc 10 min mēri augstumu. Pieraksti tabulā.",
              "Pēc 6 mērījumiem atzīmē punktus grafikā.",
              "Novelc taisni un uzraksti modeli h = kt + b.",
              "Prognozē, kad svece izdegs, un salīdzini ar realitāti."],
             vajag="svece, lineāls, pulkstenis, ugunsdroša pamatne",
             secinajums="Punkti nav ideāli uz taisnes, bet modelis ļauj "
                         "prognozēt ar dažu minūšu precizitāti."),

    Ievadi("Lieto modeli", [
        {"jaut": "h = −0,09t + 12. Cik cm pēc 60 min?",
         "atb": ["6,6"], "padoms": "12 − 5,4."},
        {"jaut": "Cik cm pēc 100 min?",
         "atb": ["3"], "padoms": "12 − 9."},
        {"jaut": "Cik cm svece sadeg stundā?",
         "atb": ["5,4"], "padoms": "0,09 · 60."},
        {"jaut": "Cita svece: h = −0,05t + 15. Pēc cik min tā izdegs?",
         "atb": ["300"], "padoms": "15 : 0,05."},
    ]),

    Pasaule("Kūstošais ledājs",
            Ievadi("", [
                {"jaut": "Ledāja mala atkāpjas vidēji 25 m gadā. 2020. gadā "
                         "līdz ezeram bija 900 m. Cik m būs 2030. gadā?",
                 "atb": ["650"], "padoms": "900 − 250."},
                {"jaut": "Kurā gadā mala sasniegs ezeru (0 m), ja tempi "
                         "nemainīsies?",
                 "atb": ["2056"], "padoms": "900 : 25 = 36 gadi."},
                {"jaut": "Kāds ir modeļa k (m gadā)?",
                 "atb": ["−25", "-25"], "padoms": "Attālums samazinās."},
            ]),
            pavediens="planeta",
            konteksts="Zinātnieki ledāju kušanu mēra katru gadu un "
                      "prognozē ar lineāriem modeļiem.",
            kapec="Tas pats kā svece - tikai gadu desmitos."),

    Kopsavilkums([
        "Iegūstu datus ar mērījumiem vienādos intervālos.",
        "Novelku taisni, kas vislabāk atbilst punktiem.",
        "Uzrakstu lineāru modeli un nolasu k un b.",
        "Izmantoju modeli prognozei.",
    ]),

    Majas([
        "Izdari sveces vai ledus kubiņa kušanas eksperimentu.",
        "Izveido grafiku un modeli.",
        "Salīdzini prognozi ar īsto rezultātu.",
    ]),
]
