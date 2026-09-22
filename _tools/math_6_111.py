# -*- coding: utf-8 -*-
"""6. klase, 111. stunda: «Kas kopīgs visiem šiem grafikiem?»

Jauns mikrotemats sākas ar apskati, ne ar definīciju. Grafiki nāk no
dažādām jomām - laika ziņām, sportu, ekonomikas -, un skolēniem pašiem
jāpamana, kas tiem visiem ir vienāds: divas asis un punkti uz tām.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         plakne)

TEMA = "Kas kopīgs visiem šiem grafikiem?"

MERKIS = ("Aplūkosim dažādu jomu grafikus un noteiksim, kas tiem kopīgs.")

SATURS = [
    Sakums("Viens attēls, daudzas jomas",
           zimejums=plakne(lauzta=[(0, -3), (1, -1), (2, 2), (3, 4),
                                   (4, 3), (5, 0)],
                           no_x=0, lidz_x=5, no_y=-4, lidz_y=5, solis=1,
                           x_nos="h", y_nos="°C"),
           paraksts="Temperatūra dienas laikā: no rīta zem nulles, "
                    "pēcpusdienā virs tās, vakarā atkal nulle.",
           fakti=["Katram grafikam ir divas asis un to krustpunkts.",
                  "Uz asīm ir mērvienības - ne tikai skaitļi.",
                  "Punkts grafikā vienmēr apvieno divus lielumus."]),

    Doma("Divas asis, viens punkts - divi lielumi",
         "Jebkurš grafiks rāda, kā viens lielums mainās atkarībā no otra: "
         "horizontālā ass ir tas, ko izvēlas, vertikālā - tas, ko mēra.",
         soli=[
             "Atrodi abas asis un to krustpunktu.",
             "Izlasi, kādi lielumi ir uz katras ass.",
             "Nosaki mērvienības un iedaļas lielumu.",
             "Atrodi, kur grafiks šķērso nulli.",
             "Nolasi vienu punktu un pasaki, ko tas nozīmē.",
         ],
         pieze="Ja vertikālajā asī ir negatīvi skaitļi, grafiks var "
               "nolaisties zem horizontālās ass. Tieši tāpēc 6. klasē "
               "vajag visu plakni, ne tikai pirmo kvadrantu."),

    Paraugs("Izlasi grafiku",
            uzd="Grafiks rāda temperatūru dienas laikā. Ko var nolasīt?",
            soli=[
                ("Horizontālā ass - laiks stundās",
                 "Tas, ko izvēlas."),
                ("Vertikālā ass - temperatūra grādos",
                 "Tas, ko mēra."),
                ("Sākumā grafiks ir zem nulles",
                 "No rīta bija sals."),
                ("Pie 2 h grafiks šķērso nulli",
                 "Tur temperatūra kļuva pozitīva."),
                ("Augstākais punkts ir 4 °C pie 3 h",
                 "Dienas maksimums."),
            ],
            atbilde="no rīta sals, pēcpusdienā līdz 4 °C"),

    Ievadi("Nolasi no grafika", [
        {"jaut": "Cik asis ir katram grafikam?",
         "atb": ["2"], "padoms": "Horizontālā un vertikālā."},
        {"jaut": "Grafikā pie 3 h temperatūra ir 4 °C. Cik grādu tas ir?",
         "atb": ["4"], "padoms": "Vertikālā ass.",
         "zim": plakne(lauzta=[(0, -3), (1, -1), (2, 2), (3, 4), (4, 3),
                               (5, 0)],
                       no_x=0, lidz_x=5, no_y=-4, lidz_y=5, solis=1,
                       x_nos="h", y_nos="°C")},
        {"jaut": "Pie kuras stundas grafiks šķērso nulli?",
         "atb": ["2"], "padoms": "Tur temperatūra kļūst pozitīva."},
        {"jaut": "Cik grādu bija sākumā, pie 0 h?",
         "atb": ["-3", "−3"], "padoms": "Zem nulles."},
        {"jaut": "Par cik grādiem temperatūra pieauga no 0 h līdz 3 h?",
         "atb": ["7"], "padoms": "No −3 līdz 4."},
        {"jaut": "Cik grādu bija pie 5 h?",
         "atb": ["0"], "padoms": "Grafiks atgriežas pie ass."},
    ], pamats=4),

    Petijums("Salīdzini trīs grafikus",
             vajag="trīs grafiki no ziņām, mācību grāmatas vai interneta",
             soli=[
                 "Atrodi trīs grafikus no dažādām jomām.",
                 "Katram pieraksti, kas ir uz abām asīm.",
                 "Pieraksti, vai grafikā ir negatīvas vērtības.",
                 "Pieraksti, kas visiem trim ir kopīgs.",
             ],
             secinajums="Visiem grafikiem ir divas asis, mērvienības un "
                        "punkti - atšķiras tikai tas, ko tie mēra."),

    Varianti("Ko rāda ass?", [
        {"jaut": "Horizontālajā asī parasti ir...",
         "opcijas": ["tas, ko izvēlas, piemēram, laiks",
                     "tas, ko mēra", "vienmēr temperatūra",
                     "tikai pozitīvi skaitļi"],
         "pareizi": 0,
         "padoms": "Laiks iet uz priekšu neatkarīgi no mērījuma."},
        {"jaut": "Ko nozīmē punkts grafikā?",
         "opcijas": ["Divu lielumu pāri", "Vienu skaitli",
                     "Ass krustpunktu", "Grafika beigas"],
         "pareizi": 0,
         "padoms": "Katram punktam ir divas koordinātas."},
        {"jaut": "Kad grafiks iet zem horizontālās ass?",
         "opcijas": ["Kad mērītais lielums ir negatīvs",
                     "Kad laiks ir negatīvs",
                     "Kad grafiks ir nepareizs", "Nekad"],
         "pareizi": 0,
         "padoms": "Negatīvas vērtības."},
        {"jaut": "Kas ir kopīgs visiem grafikiem?",
         "opcijas": ["Divas asis un punkti", "Viena krāsa",
                     "Temperatūra", "Taisne"],
         "pareizi": 0,
         "padoms": "Jomas atšķiras, uzbūve - ne."},
    ], pamats=4),

    Pasaule("Ko rāda dienas grafiks?",
            Ievadi("", [
                {"jaut": "No rīta −3 °C, dienā 4 °C. Par cik grādiem "
                         "pieauga?",
                 "atb": ["7"], "padoms": "3 + 4."},
                {"jaut": "Vakarā atkal 0 °C. Par cik grādiem nokrita no "
                         "dienas maksimuma?",
                 "atb": ["4"], "padoms": "4 − 0."},
                {"jaut": "Cik stundas temperatūra bija zem nulles, ja tā "
                         "bija zem nulles no 0 h līdz 2 h?",
                 "atb": ["2"], "padoms": "Divas stundas."},
                {"jaut": "Kāda bija dienas temperatūru starpība starp "
                         "augstāko un zemāko?",
                 "atb": ["7"], "padoms": "No −3 līdz 4."},
            ]),
            pavediens="planeta",
            konteksts="Laika ziņu grafikā svarīgākais ir tas, kur līnija "
                      "šķērso nulli - tur sākas atkusnis.",
            kapec="Grafiks pasaka visu dienu vienā attēlā."),

    Zimejums("Grafiks ar negatīvām vērtībām",
             plakne(lauzta=[(0, 2), (1, 0), (2, -2), (3, -3), (4, -1)],
                    no_x=0, lidz_x=4, no_y=-4, lidz_y=3, solis=1,
                    x_nos="h", y_nos="°C"),
             paskaidro="Šeit temperatūra krīt zem nulles un tad atkal aug. "
                       "Grafiks iet gan virs, gan zem ass.",
             ievads="Otrs grafiks, cita diena."),

    Kopsavilkums([
        "Atrodu grafikā abas asis un to krustpunktu.",
        "Izlasu, kādi lielumi un mērvienības ir uz asīm.",
        "Nolasu atsevišķu punktu un paskaidroju, ko tas nozīmē.",
        "Zinu, ko nozīmē grafika daļa zem horizontālās ass.",
    ]),

    Majas([
        "Atrodi ziņās grafiku un pieraksti, kas ir uz abām asīm.",
        "Pieraksti, vai tajā ir negatīvas vērtības.",
        "Nolasi no tā vienu punktu un uzraksti, ko tas nozīmē.",
    ]),
]
