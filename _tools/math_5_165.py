# -*- coding: utf-8 -*-
"""5. klase, 165. stunda: «Kādus jautājumus var uzdot?»

Stunda, kurā skolēns kļūst par uzdevumu autoru. Nolasīt grafiku viņš jau
prot; tagad jāsaprot, kādi jautājumi tam vispār der. Labs jautājums ir tāds,
uz kuru grafiks atbild - un tieši tāpēc tā uzrakstīšana pierāda, ka grafiks
ir saprasts.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         plakne)

TEMA = "Kādus jautājumus var uzdot?"

MERKIS = ("Mācīsimies formulēt jautājumus par lielumiem un sakarībām, "
          "izmantojot grafisko attēlu.")

SATURS = [
    Sakums("Viens grafiks, daudz jautājumu",
           zimejums=plakne(lauzta=[(0, 4), (1, 8), (2, 14), (3, 16),
                                   (4, 12)],
                           no_x=0, lidz_x=5, no_y=0, lidz_y=20, solis=4,
                           virsraksts="Temperatūra dienas laikā"),
           paraksts="Kāda bija augstākā temperatūra? Kad tā sāka krist?",
           fakti=["Uz dažiem jautājumiem grafiks atbild.",
                  "Uz citiem - nē, lai cik uzmanīgi skatītos.",
                  "Labs jautājums ir tāds, uz kuru atbilde ir grafikā."]),

    Doma("Jautā to, uz ko grafiks atbild",
         "No grafika var jautāt par vērtībām, par izmaiņām un par "
         "salīdzinājumu; jautājumi par to, kas grafikā nav attēlots, paliek "
         "bez atbildes.",
         soli=[
             "Jautājums par vērtību: cik liels lielums bija konkrētā brīdī?",
             "Jautājums par izmaiņu: par cik tas pieauga vai saruka?",
             "Jautājums par salīdzinājumu: kurā brīdī bija vislielākais?",
             "Pārbaudi, vai atbilde tiešām ir grafikā.",
             "Ja nav - jautājums neder šim grafikam.",
         ],
         pieze="«Kāpēc temperatūra krita?» ir labs jautājums, bet grafiks uz "
               "to neatbild - tas rāda, kas notika, nevis kāpēc. Matemātikā "
               "abus jautājumus tur atsevišķi."),

    Petijums("Uzraksti trīs jautājumus",
             soli=["Izvēlies grafiku no mācību grāmatas vai ziņām.",
                   "Uzraksti vienu jautājumu par vērtību.",
                   "Uzraksti vienu jautājumu par izmaiņu.",
                   "Uzraksti vienu jautājumu, uz kuru grafiks neatbild.",
                   "Apmainies ar solabiedru un atbildi uz viņa "
                   "jautājumiem."],
             vajag="grafiks, burtnīca",
             secinajums="Grafiks atbild uz jautājumiem par vērtībām un "
                        "izmaiņām, bet ne par cēloņiem."),

    Paraugs("Trīs jautājumi par vienu grafiku",
            uzd="Temperatūra: 4°, 8°, 14°, 16°, 12°. Kādus jautājumus var "
                "uzdot?",
            soli=[
                ("Cik grādu bija trešajā mērījumā?",
                 "Jautājums par vērtību - atbilde 14°."),
                ("Par cik grādiem temperatūra pieauga no pirmā līdz "
                 "trešajam?",
                 "Jautājums par izmaiņu - atbilde 10°."),
                ("Kurā brīdī bija vissiltāk?",
                 "Jautājums par salīdzinājumu - ceturtajā."),
                ("Kāpēc pēc tam kļuva vēsāks?",
                 "Uz šo grafiks neatbild."),
            ],
            atbilde="Pirmie trīs jautājumi der, ceturtais - nē"),

    Ievadi("Atbildi uz jautājumiem", [
        {"jaut": "Temperatūras 4, 8, 14, 16, 12. Cik grādu bija trešajā "
                 "mērījumā?",
         "atb": ["14"], "padoms": "Trešais skaitlis."},
        {"jaut": "Par cik grādiem temperatūra pieauga no pirmā līdz "
                 "trešajam?",
         "atb": ["10"], "padoms": "14 - 4."},
        {"jaut": "Kurā mērījumā bija vissiltāk? Ieraksti numuru.",
         "atb": ["4"], "padoms": "16 ir lielākais."},
        {"jaut": "Cik grādu bija pēdējā mērījumā?",
         "atb": ["12"], "padoms": "Pēdējais skaitlis."},
        {"jaut": "Par cik grādiem temperatūra saruka no ceturtā līdz "
                 "piektajam?",
         "atb": ["4"], "padoms": "16 - 12."},
        {"jaut": "Cik mērījumu ir grafikā?",
         "atb": ["5"], "padoms": "Saskaiti punktus."},
        {"jaut": "Kāda ir starpība starp augstāko un zemāko?",
         "atb": ["12"], "padoms": "16 - 4."},
        {"jaut": "Cik grādu bija otrajā mērījumā?",
         "atb": ["8"], "padoms": "Otrais skaitlis."},
    ], pamats=4,
        ievads="Katram jautājumam atbildei jābūt pašā grafikā."),

    Zimejums("Uz ko grafiks atbild",
             plakne(lauzta=[(0, 4), (1, 8), (2, 14), (3, 16), (4, 12)],
                    punkti=[(2, 14, "")], no_x=0, lidz_x=5, no_y=0,
                    lidz_y=20, solis=4, virsraksts="Trešais mērījums"),
             paskaidro="Atzīmētais punkts atbild uz jautājumu par vērtību; "
                       "attālums līdz blakus punktiem - uz jautājumu par "
                       "izmaiņu.",
             ievads="Viens punkts, divi jautājumu veidi."),

    Varianti("Vai grafiks atbild?", [
        {"jaut": "«Cik grādu bija pulksten 12?» Vai grafiks atbild?",
         "opcijas": ["Atbild, ja tas brīdis ir attēlots", "Nekad neatbild",
                     "Vienmēr atbild", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Jautājums par vērtību."},
        {"jaut": "«Kāpēc temperatūra krita?» Vai grafiks atbild?",
         "opcijas": ["Neatbild - tas rāda, kas notika, ne kāpēc", "Atbild",
                     "Atbild daļēji", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Cēloņi nav grafikā."},
        {"jaut": "Kāds ir jautājums par izmaiņu?",
         "opcijas": ["Par cik lielums pieauga", "Cik liels tas bija",
                     "Kāpēc tas mainījās", "Kas to mērīja"],
         "pareizi": 0,
         "padoms": "Starpība starp diviem punktiem."},
        {"jaut": "«Kurā brīdī bija vissiltāk?» Kāds tas ir jautājums?",
         "opcijas": ["Par salīdzinājumu", "Par vērtību", "Par cēloni",
                     "Par mērvienību"],
         "pareizi": 0,
         "padoms": "Meklē lielāko."},
        {"jaut": "Kā pārbauda, vai jautājums der?",
         "opcijas": ["Paskatās, vai atbilde ir grafikā", "Pajautā "
                                                         "skolotājam",
                     "Izrēķina", "Nekā"],
         "pareizi": 0,
         "padoms": "Atbildei jābūt attēlā."},
        {"jaut": "Temperatūras 4, 8, 14, 16, 12. Par cik pieauga no pirmā "
                 "līdz trešajam?",
         "opcijas": ["10", "14", "4", "18"],
         "pareizi": 0,
         "padoms": "14 - 4."},
    ], pamats=4),

    Pasaule("Jautājumi par skolas datiem",
            Ievadi("", [
                {"jaut": "Skolēnu skaits klasēs: 20, 22, 25, 21. Kurā klasē "
                         "ir visvairāk? Ieraksti skaitu.",
                 "atb": ["25"], "padoms": "Lielākais skaitlis."},
                {"jaut": "Cik skolēnu ir visās četrās klasēs kopā?",
                 "atb": ["88"], "padoms": "20 + 22 + 25 + 21."},
                {"jaut": "Kāds ir vidējais skolēnu skaits klasē?",
                 "atb": ["22"], "padoms": "88 : 4."},
                {"jaut": "Par cik skolēniem lielākā klase pārsniedz mazāko?",
                 "atb": ["5"], "padoms": "25 - 20."},
            ]),
            pavediens="skola",
            konteksts="Par skolas datiem var uzdot desmitiem jautājumu, bet "
                      "tikai daļa no tiem ir atbildami ar grafiku.",
            kapec="Labs jautājums ir tāds, uz kuru dati tiešām atbild."),

    Kopsavilkums([
        "Formulēju jautājumus par vērtībām un izmaiņām.",
        "Formulēju jautājumus par salīdzinājumu.",
        "Pārbaudu, vai atbilde ir grafikā.",
        "Atpazīstu jautājumus, uz kuriem grafiks neatbild.",
    ]),

    Majas([
        "Izvēlies grafiku un uzraksti tam trīs jautājumus ar atbildēm.",
        "Uzraksti vienu jautājumu, uz kuru grafiks neatbild.",
        "Iedod savus jautājumus draugam.",
    ]),
]
