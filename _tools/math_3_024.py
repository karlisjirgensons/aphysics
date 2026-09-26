# -*- coding: utf-8 -*-
"""3. klase, 24. stunda: «Cik veikli dali?»

Dalīšanas mikrotemata noslēgums: dalījumi bez atlikuma un ar atlikumu, abas
dalīšanas nozīmes un pārbaude - viss vienā patstāvīgā darbā. Vērtējuma nav;
ir saraksts, ko vēl atkārtot pirms pārbaudes darba.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Cik veikli dali?"

MERKIS = ("Patstāvīgi dalīsim tabulas apjomā, pārbaudīsim rezultātus un "
          "atzīmēsim, kas vēl jātrenē.")

SATURS = [
    Sakums("Vai dalīšana jau nāk tikpat ātri kā reizināšana?",
           zimejums=restis([[48, ":", 6, "=", "?"],
                            [56, ":", 7, "=", "?"],
                            [72, ":", 8, "=", "?"],
                            [81, ":", 9, "=", "?"]],
                           "četri dalījumi"),
           paraksts="Katram no tiem atbilst viens reizinājums, ko tu zini.",
           fakti=["Dalīšanu vienmēr var atrast reizināšanas tabulā.",
                  "Pārbaude ar reizināšanu aizņem vienu rindu."]),

    Doma("Dalīt veikli nozīmē - zināt reizinājumu",
         "Ja reizinājums ir atmiņā, dalījums atnāk pats; ja nav, dalīšana "
         "kļūst par meklēšanu.",
         soli=[
             "Izlasi dalījumu kā jautājumu par trūkstošo reizinātāju.",
             "Atceries reizinājumu no tabulas.",
             "Pieraksti atbildi un pārbaudi to ar reizināšanu.",
             "Ja atlikums ir, pārbaudē to pieskaiti.",
         ],
         pieze="Ja dalījums nesanāk, tā nav dalīšanas problēma - tā ir "
               "norāde, kuru reizinājumu vēl vajag trenēt."),

    Paraugs("Cik pilnu grupu un cik paliek pāri?",
            uzd="Izdali 59 ar 8 un pasaki, cik paliek pāri.",
            soli=[
                ("8, 16, 24, 32, 40, 48, 56",
                 "Astotnieku rinda līdz 59."),
                ("56 ≤ 59, bet 64 > 59",
                 "Septiņas pilnas grupas ietilpst, astotā vairs ne."),
                ("59 − 56 = 3",
                 "Atlikums; pārbaude: 7 · 8 + 3 = 59."),
            ],
            atbilde="7 grupas, atlikums 3"),

    Ievadi("Patstāvīgais darbs", [
        {"jaut": "48 : 6 = ?", "atb": ["8"], "padoms": "6 · 8 = 48."},
        {"jaut": "56 : 7 = ?", "atb": ["8"], "padoms": "7 · 8 = 56."},
        {"jaut": "72 : 8 = ?", "atb": ["9"], "padoms": "8 · 9 = 72."},
        {"jaut": "81 : 9 = ?", "atb": ["9"], "padoms": "9 · 9 = 81."},
        {"jaut": "Cik paliek pāri, dalot 50 ar 6?", "atb": ["2"],
         "padoms": "48 + 2 = 50."},
        {"jaut": "Cik pilnu grupu sanāk, dalot 50 ar 6?", "atb": ["8"],
         "padoms": "6 · 8 = 48."},
        {"jaut": "63 : 7 = ?", "atb": ["9"], "padoms": "7 · 9 = 63."},
        {"jaut": "0 : 9 = ?", "atb": ["0"], "padoms": "Nekas, sadalīts "
                                                      "deviņās daļās."},
    ], pamats=6),

    Zimejums("Dalījumi bez atlikuma",
             restis([[36, 42, 48, 54],
                     [":6 = 6", ":6 = 7", ":6 = 8", ":6 = 9"]],
                    "sešnieku rinda otrādi"),
             paskaidro="Katra reizināšanas rinda ir arī dalīšanas rinda - "
                       "tikai lasīta no otras puses.",
             ievads="Pārbaudi sevi, aizsedzot apakšējo rindu."),

    Varianti("Vai atbilde ir ticama?", [
        {"jaut": "Kurš dalījums *nav* vesels skaitlis?",
         "opcijas": ["50 : 7", "49 : 7", "56 : 7", "63 : 7"],
         "pareizi": 0, "padoms": "50 nav septiņnieku rindā."},
        {"jaut": "Cik ir 64 : 8?",
         "opcijas": ["8", "7", "9", "6"],
         "pareizi": 0, "padoms": "8 · 8 = 64."},
        {"jaut": "Dalot ar 9, kāds atlikums nevar būt?",
         "opcijas": ["9", "8", "5", "0"],
         "pareizi": 0, "padoms": "Atlikums ir mazāks par dalītāju."},
        {"jaut": "Ar ko pārbaudīt 45 : 5 = 9 ar atlikumu 0?",
         "opcijas": ["9 · 5 = 45", "45 · 5", "9 : 5", "45 + 5"],
         "pareizi": 0, "padoms": "Atbildi reizina ar dalītāju."},
    ], pamats=4),

    Pasaule("Cik porciju sanāks svētkiem?",
            Ievadi("", [
                {"jaut": "72 sausiņus liek maisiņos pa 8. Cik maisiņu "
                         "sanāks?",
                 "atb": ["9"], "padoms": "72 : 8."},
                {"jaut": "50 sausiņus liek maisiņos pa 6. Cik pilnu maisiņu?",
                 "atb": ["8"], "padoms": "48 ≤ 50."},
                {"jaut": "Cik sausiņu paliks pāri?",
                 "atb": ["2"], "padoms": "50 − 48."},
                {"jaut": "Cik sausiņu vajag, lai pietiktu 9 pilniem maisiņiem "
                         "pa 6?",
                 "atb": ["54"], "padoms": "9 · 6."},
            ]),
            pavediens="virtuve",
            konteksts="Svētku galdam ēdienu vienmēr dala porcijās - un "
                      "atlikums parāda, vai pietiek visiem.",
            kapec="Ar dalīšanu var saplānot galdu, pirms kaut kas ir "
                  "sagatavots."),

    Kopsavilkums([
        "Patstāvīgi dalu reizināšanas tabulas apjomā.",
        "Dalu ar atlikumu un zinu, ko atlikums nozīmē.",
        "Pārbaudu katru rezultātu ar reizināšanu.",
        "Zinu, kurus reizinājumus man vēl vajag trenēt.",
    ]),

    Majas([
        "Izrēķini desmit dalījumus un pārbaudi katru.",
        "Atrodi trīs dalījumus, kuros rodas atlikums.",
        "Pieraksti, kuri reizinājumi tev vēl nepadodas.",
    ]),
]
