# -*- coding: utf-8 -*-
"""5. klase, 164. stunda: «Ko stāsta temperatūras grafiks?»

Jauns mikrotemats, un pirmā reize, kad grafiks nav taisns. Temperatūra ceļas
un krīt, tāpēc līnija ir lauzta, un tieši tur parādās jauna prasme: nolasīt
ne tikai vērtības, bet arī to, kurā brīdī lielums auga un kurā - sarūka.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, plakne)

TEMA = "Ko stāsta temperatūras grafiks?"

MERKIS = ("Mācīsimies raksturot nepazīstamu sakarību pēc tās grafiskā attēla "
          "un formulēt secinājumus.")

SATURS = [
    Sakums("Diena, kas silst un atdziest",
           zimejums=plakne(lauzta=[(0, 4), (1, 8), (2, 14), (3, 16),
                                   (4, 12), (5, 6)],
                           no_x=0, lidz_x=6, no_y=0, lidz_y=20, solis=4,
                           virsraksts="Temperatūra dienas laikā"),
           paraksts="Līnija ceļas līdz vidum un tad krīt.",
           fakti=["Temperatūra nav vienmērīga - tā mainās uz abām pusēm.",
                  "Grafiks tāpēc ir lauzta līnija.",
                  "Augstākais punkts rāda dienas siltāko brīdi."]),

    Doma("Skaties, kur līnija ceļas un kur krīt",
         "No grafika nolasa ne tikai atsevišķas vērtības, bet arī to, kurā "
         "posmā lielums aug, kurā sarūk un kur ir tā lielākā vērtība.",
         soli=[
             "Atrodi augstāko punktu - tā ir lielākā vērtība.",
             "Atrodi zemāko punktu - mazākā vērtība.",
             "Paskaties, kuros posmos līnija ceļas.",
             "Paskaties, kuros posmos tā krīt.",
             "Formulē secinājumus pilnos teikumos.",
         ],
         pieze="Stāvāks posms nozīmē straujāku izmaiņu. Ja līnija ceļas ļoti "
               "stāvi, temperatūra augusi ātri; ja tā ir gandrīz "
               "horizontāla, tā gandrīz nav mainījusies."),

    Paraugs("Ko var pateikt par dienu?",
            uzd="Temperatūra: 4°, 8°, 14°, 16°, 12°, 6°. Kādus secinājumus "
                "var izdarīt?",
            soli=[
                ("Augstākā temperatūra ir 16°",
                 "Grafika augstākais punkts."),
                ("Zemākā ir 4°",
                 "Rīta stundā."),
                ("Līdz ceturtajam mērījumam temperatūra auga",
                 "Līnija ceļas."),
                ("Pēc tam tā krita",
                 "Līnija iet uz leju."),
                ("Starpība ir 16 - 4 = 12 grādi",
                 "Dienas svārstība."),
            ],
            atbilde="Diena silusi līdz 16° un tad atdzisusi līdz 6°"),

    Ievadi("Nolasi no grafika", [
        {"jaut": "Temperatūras: 4, 8, 14, 16, 12, 6. Kāda ir augstākā?",
         "atb": ["16"], "padoms": "Lielākais skaitlis."},
        {"jaut": "Kāda ir zemākā temperatūra?",
         "atb": ["4"], "padoms": "Mazākais skaitlis."},
        {"jaut": "Cik grādu ir starpība starp augstāko un zemāko?",
         "atb": ["12"], "padoms": "16 - 4."},
        {"jaut": "Par cik grādiem temperatūra auga no 8 līdz 14?",
         "atb": ["6"], "padoms": "14 - 8."},
        {"jaut": "Par cik grādiem tā krita no 16 līdz 12?",
         "atb": ["4"], "padoms": "16 - 12."},
        {"jaut": "Cik mērījumu ir šajā grafikā?",
         "atb": ["6"], "padoms": "Saskaiti punktus."},
        {"jaut": "Kurā mērījumā bija siltākais brīdis? Ieraksti tā numuru.",
         "atb": ["4"], "padoms": "Ceturtais punkts ir 16°."},
        {"jaut": "Par cik grādiem temperatūra krita no 12 līdz 6?",
         "atb": ["6"], "padoms": "12 - 6."},
    ], pamats=4,
        ievads="Vispirms atrodi augstāko un zemāko punktu."),

    Zimejums("Kāpums un kritums",
             plakne(lauzta=[(0, 4), (1, 8), (2, 14), (3, 16), (4, 12),
                            (5, 6)],
                    punkti=[(3, 16, "")], no_x=0, lidz_x=6, no_y=0,
                    lidz_y=20, solis=4, virsraksts="Augstākais punkts"),
             paskaidro="Līdz atzīmētajam punktam līnija ceļas, pēc tā krīt. "
                       "Tieši tur diena bija vissiltākā.",
             ievads="Vienā grafikā ir gan kāpums, gan kritums."),

    Varianti("Ko rāda lauztā līnija?", [
        {"jaut": "Ko rāda grafika augstākais punkts?",
         "opcijas": ["Lielāko vērtību", "Vidējo vērtību", "Pirmo mērījumu",
                     "Neko"],
         "pareizi": 0,
         "padoms": "Visaugstāk pa y asi."},
        {"jaut": "Ko nozīmē, ka līnija krīt?",
         "opcijas": ["Lielums sarūk", "Lielums aug", "Lielums nemainās",
                     "Grafiks ir nepareizs"],
         "pareizi": 0,
         "padoms": "Iet uz leju."},
        {"jaut": "Ko nozīmē stāvāks posms?",
         "opcijas": ["Straujāku izmaiņu", "Lielāku vērtību",
                     "Garāku laiku", "Neko"],
         "pareizi": 0,
         "padoms": "Vairāk izmaiņu tajā pašā laikā."},
        {"jaut": "Temperatūras 4, 8, 14, 16, 12, 6. Cik grādu ir starpība "
                 "starp augstāko un zemāko?",
         "opcijas": ["12", "16", "4", "20"],
         "pareizi": 0,
         "padoms": "16 - 4."},
        {"jaut": "Kāpēc temperatūras grafiks nav taisne?",
         "opcijas": ["Temperatūra mainās nevienmērīgi",
                     "Tas ir zīmēts nepareizi",
                     "Punktu ir par maz",
                     "Asis ir dažādas"],
         "pareizi": 0,
         "padoms": "Reizēm aug, reizēm sarūk."},
        {"jaut": "Ko nozīmē gandrīz horizontāls posms?",
         "opcijas": ["Lielums gandrīz nemainās", "Lielums strauji aug",
                     "Mērījumu trūkst", "Neko"],
         "pareizi": 0,
         "padoms": "Nav ne kāpuma, ne krituma."},
    ], pamats=4),

    Pasaule("Kāda bija nedēļa?",
            Ievadi("", [
                {"jaut": "Temperatūras nedēļā: 5, 9, 12, 8, 6. Kāda ir "
                         "augstākā?",
                 "atb": ["12"], "padoms": "Lielākais skaitlis."},
                {"jaut": "Kāda ir zemākā?",
                 "atb": ["5"], "padoms": "Mazākais skaitlis."},
                {"jaut": "Cik grādu ir starpība?",
                 "atb": ["7"], "padoms": "12 - 5."},
                {"jaut": "Kāds ir vidējais no 5, 9, 12, 8 un 6?",
                 "atb": ["8"], "padoms": "40 : 5."},
            ]),
            pavediens="planeta",
            konteksts="Laika ziņās temperatūru vienmēr rāda kā grafiku - no "
                      "tā uzreiz redz, vai kļūs siltāks vai vēsāks.",
            kapec="Lauztā līnija pastāsta par visu nedēļu vienā skatienā."),

    Kopsavilkums([
        "Raksturoju sakarību pēc tās grafiskā attēla.",
        "Atrodu grafika augstāko un zemāko punktu.",
        "Nosaku, kuros posmos lielums aug un kuros sarūk.",
        "Formulēju secinājumus pilnos teikumos.",
    ]),

    Majas([
        "Atrodi laika ziņu grafiku un pieraksti trīs secinājumus.",
        "Nosaki augstāko un zemāko temperatūru.",
        "Aprēķini to starpību.",
    ]),
]
