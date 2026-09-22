# -*- coding: utf-8 -*-
"""6. klase, 85. stunda: «Kādas sakarības var izlasīt?»

Mikrotemata noslēgums. No viena fakta - «2 no 8 ir 25 %» - izriet vairāki
citi, un tos var pierakstīt, neko nerēķinot. Tā ir prasme lasīt uz abām
pusēm, un tieši tā vēlāk ļauj ātri pārbaudīt savu atbildi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala)

TEMA = "Kādas sakarības var izlasīt?"

MERKIS = ("Formulēsim dažādas sakarības starp lielumiem, ja zināma viena.")

SATURS = [
    Sakums("Viens fakts - četri apgalvojumi",
           zimejums=dala(4, 1, "2 no 8"),
           paraksts="Ja 2 no 8 ir 25 %, tad 25 % no 8 ir 2, bet 75 % no 8 "
                    "ir 6.",
           fakti=["No vienas sakarības izriet vairākas citas.",
                  "Otrs virziens: ja 25 % ir 2, tad kopums ir 8.",
                  "Atlikums vienmēr ir 100 % mīnus dotais procents."]),

    Doma("Lasi uz abām pusēm",
         "No apgalvojuma «a ir p procenti no b» izriet, ka p procenti no b "
         "ir a, ka kopums ir a, dalīts ar daļu, un ka atlikums ir "
         "100 % − p.",
         soli=[
             "Pieraksti doto sakarību ar skaitļiem.",
             "Pārraksti to otrādi: procenti no kopuma dod daļu.",
             "Aprēķini atlikumu: 100 % mīnus dotais.",
             "Pieraksti atlikuma skaitlisko vērtību.",
             "Pārbaudi: daļa un atlikums kopā dod kopumu.",
         ],
         pieze="Šīs sakarības der arī pārbaudei. Ja atbilde un atlikums kopā "
               "nedod kopumu, kaut kur ir kļūda - un to pamana uzreiz."),

    Paraugs("No viena fakta uz četriem",
            uzd="Zināms, ka 2 no 8 ir 25 %. Kādus apgalvojumus vēl var "
                "pierakstīt?",
            soli=[
                ("25 % no 8 ir 2",
                 "Tā pati sakarība otrā virzienā."),
                ("75 % no 8 ir 6",
                 "Atlikums: 8 − 2."),
                ("Ja 25 % ir 2, tad kopums ir 8",
                 "No daļas uz kopumu."),
                ("6 no 8 ir 75 %",
                 "Atlikums procentos."),
            ],
            atbilde="četri apgalvojumi par vienu un to pašu"),

    Ievadi("Turpini sakarību", [
        {"jaut": "2 no 8 ir 25 %. Cik ir 25 % no 8?",
         "atb": ["2"], "padoms": "Tā pati sakarība."},
        {"jaut": "Cik procenti no 8 ir 6?",
         "atb": ["75"], "padoms": "100 − 25."},
        {"jaut": "Ja 25 % ir 2, cik ir kopums?",
         "atb": ["8"], "padoms": "2 · 4."},
        {"jaut": "Ja 50 % ir 12, cik ir kopums?",
         "atb": ["24"], "padoms": "12 · 2."},
        {"jaut": "Ja 20 % ir 7, cik ir kopums?",
         "atb": ["35"], "padoms": "7 · 5."},
        {"jaut": "Ja 10 % ir 4,5, cik ir kopums?",
         "atb": ["45"], "padoms": "4,5 · 10."},
    ], pamats=4,
        ievads="Katrs fakts par procentiem der abos virzienos."),

    Varianti("Kurš apgalvojums izriet?", [
        {"jaut": "«5 no 20 ir 25 %.» Kurš apgalvojums izriet no tā?",
         "opcijas": ["15 no 20 ir 75 %", "20 no 5 ir 25 %",
                     "25 no 20 ir 5 %", "5 no 25 ir 20 %"],
         "pareizi": 0,
         "padoms": "Atlikums ir 100 % − 25 %."},
        {"jaut": "Ja 40 % no kopuma ir 12, cik ir kopums?",
         "opcijas": ["30", "48", "4,8", "120"],
         "pareizi": 0,
         "padoms": "1 % ir 0,3."},
        {"jaut": "Ja daļa ir 30 % no kopuma, cik procentu ir atlikums?",
         "opcijas": ["70", "30", "100", "170"],
         "pareizi": 0,
         "padoms": "100 − 30."},
        {"jaut": "Kā pārbaudīt savu atbildi?",
         "opcijas": ["Daļa un atlikums kopā dod kopumu",
                     "Atbildei jābūt veselai",
                     "Atbildei jābūt lielākai par kopumu",
                     "Pārbaudīt nevar"],
         "pareizi": 0,
         "padoms": "100 % ir viss."},
    ], pamats=4),

    Pasaule("Ko vēl var pateikt par datiem?",
            Ievadi("", [
                {"jaut": "Aptaujā 30 no 120 izvēlējās pirmo atbildi. Cik "
                         "procenti tas ir?",
                 "atb": ["25"], "padoms": "{30|120} = {1|4}."},
                {"jaut": "Cik procenti izvēlējās citas atbildes?",
                 "atb": ["75"], "padoms": "100 − 25."},
                {"jaut": "Cik cilvēku izvēlējās citas atbildes?",
                 "atb": ["90"], "padoms": "120 − 30."},
                {"jaut": "Ja 25 % ir 30 cilvēki, cik cilvēku ir 50 %?",
                 "atb": ["60"], "padoms": "Divreiz vairāk."},
            ]),
            pavediens="skola",
            konteksts="Aptaujas rezultātus publicē procentos, bet skolēnu "
                      "skaitu var atjaunot no tiem pašiem datiem.",
            kapec="Viens fakts par procentiem satur vairākus citus."),

    Zimejums("Daļa un atlikums vienā joslā",
             dala(4, 1, "25 % un 75 %"),
             paskaidro="Iekrāsotā daļa un pārējā daļa kopā vienmēr ir "
                       "100 % - tā ir vienkāršākā pārbaude.",
             ievads="Josla parāda abas sakarības reizē."),

    Kopsavilkums([
        "Formulēju vairākas sakarības no viena dotā fakta.",
        "Lasu sakarību abos virzienos.",
        "Aprēķinu atlikumu gan procentos, gan skaitļos.",
        "Pārbaudu atbildi: daļa un atlikums dod kopumu.",
    ]),

    Majas([
        "No fakta «10 no 40 ir 25 %» pieraksti četrus apgalvojumus.",
        "Atrodi ziņās procentu un pieraksti, kāds ir atlikums.",
        "Izdomā faktu par savu klasi un pieraksti no tā trīs sakarības.",
    ]),
]
