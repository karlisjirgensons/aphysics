# -*- coding: utf-8 -*-
"""6. klase, 155. stunda: «Cik dažādi var pierakstīt vienu skaitli?»

Viens skaitlis - daudzi pieraksti. Tas nav triks, bet prasme: eksāmenā
atbildi bieži prasa konkrētā formā, un salīdzināt divus skaitļus var tikai
tad, ja tie ir vienā pierakstā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Cik dažādi var pierakstīt vienu skaitli?"

MERKIS = ("Pierakstīsim vienu racionālu skaitli dažādos veidos un "
          "izvēlēsimies piemērotāko.")

SATURS = [
    Sakums("Viens skaitlis, pieci pieraksti",
           zimejums=restis([["1/2", "2/4", "0,5", "50 %"]]),
           paraksts="Visi četri pieraksti apzīmē vienu un to pašu skaitli.",
           fakti=["Daļu var paplašināt un saīsināt - vērtība nemainās.",
                  "To pašu skaitli var rakstīt kā decimāldaļu vai "
                  "procentus.",
                  "Salīdzināt var tikai vienā pierakstā."]),

    Doma("Izvēlies pierakstu pēc uzdevuma",
         "Vienu racionālu skaitli var pierakstīt kā parasto daļu, "
         "decimāldaļu vai procentus; izvēli nosaka tas, ko ar skaitli darīs.",
         soli=[
             "Pieraksti skaitli kā parasto daļu un saīsini to.",
             "Pārveido to decimāldaļā.",
             "Pārveido decimāldaļu procentos.",
             "Pārbaudi, vai visi pieraksti dod vienu vērtību.",
             "Izvēlies to, kas der uzdevumam.",
         ],
         pieze="Reizināšanai un dalīšanai ērtākas ir parastās daļas, "
               "salīdzināšanai un saskaitīšanai - decimāldaļas, bet "
               "sadzīves uzdevumos - procenti."),

    Paraugs("Pieci pieraksti vienam skaitlim",
            uzd="Pieraksti skaitli {3|4} visos zināmajos veidos.",
            soli=[
                ("{3|4} - parastā daļa",
                 "Pamatforma."),
                ("{6|8} - paplašināta daļa",
                 "Tā pati vērtība."),
                ("0,75 - decimāldaļa",
                 "3 : 4."),
                ("75 % - procenti",
                 "0,75 · 100."),
            ],
            atbilde="{3|4} = {6|8} = 0,75 = 75 %"),

    Ievadi("Pārveido pierakstu", [
        {"jaut": "Cik ir {3|4} decimāldaļā?",
         "atb": ["0,75", "0.75"], "padoms": "3 : 4."},
        {"jaut": "Cik procentu ir {3|4}?",
         "atb": ["75"], "padoms": "{75|100}."},
        {"jaut": "Cik ir 0,5 parastajā daļā? Atbildi raksti kā a/b.",
         "atb": ["1/2", "5/10"], "padoms": "{5|10}."},
        {"jaut": "Cik procentu ir 0,2?",
         "atb": ["20"], "padoms": "20 simtdaļas."},
        {"jaut": "Cik ir 40 % decimāldaļā?",
         "atb": ["0,4", "0.4"], "padoms": "{40|100}."},
        {"jaut": "Cik ir {2|5} decimāldaļā?",
         "atb": ["0,4", "0.4"], "padoms": "{4|10}."},
    ], pamats=4),

    Varianti("Kurš pieraksts te der?", [
        {"jaut": "Skaitļu salīdzināšanai ērtāks pieraksts ir...",
         "opcijas": ["decimāldaļa", "parastā daļa",
                     "procenti", "jebkurš"],
         "pareizi": 0,
         "padoms": "Salīdzina pa vietas vērtībām."},
        {"jaut": "Reizināšanai ar {1|3} ērtāks pieraksts ir...",
         "opcijas": ["parastā daļa", "decimāldaļa",
                     "procenti", "jebkurš"],
         "pareizi": 0,
         "padoms": "{1|3} decimālpierakstā nav precīzs."},
        {"jaut": "Kurš skaitlis *nav* vienāds ar pārējiem?",
         "opcijas": ["0,45", "{1|2}", "0,5", "50 %"],
         "pareizi": 0,
         "padoms": "Trīs no tiem ir puse."},
        {"jaut": "{6|8} ir vienāds ar...",
         "opcijas": ["0,75", "0,68", "{3|8}", "0,6"],
         "pareizi": 0,
         "padoms": "Saīsina ar 2."},
    ], pamats=4),

    Pasaule("Kurš piedāvājums ir labāks?",
            Ievadi("", [
                {"jaut": "Atlaide {1|4} vai 20 %. Cik procentu ir {1|4}?",
                 "atb": ["25"], "padoms": "{25|100}."},
                {"jaut": "Kura atlaide ir lielāka? Ieraksti procentus.",
                 "atb": ["25"], "padoms": "25 ir vairāk par 20."},
                {"jaut": "Cena 80 €, atlaide {1|4}. Cik eiro ir atlaide?",
                 "atb": ["20"], "padoms": "80 : 4."},
                {"jaut": "Cena 80 €, atlaide 20 %. Cik eiro ir atlaide?",
                 "atb": ["16"], "padoms": "80 · 0,2."},
            ]),
            pavediens="veikals",
            konteksts="Divas atlaides dažādos pierakstos salīdzināt nevar - "
                      "vispirms abas jāpārveido vienā veidā.",
            kapec="Pareizs pieraksts padara salīdzināšanu acīmredzamu."),

    Zimejums("Viens skaitlis, četri pieraksti",
             restis([["3/4", "6/8", "0,75", "75 %"]]),
             paskaidro="Visi četri ir viens un tas pats skaitlis. Izvēle "
                       "atkarīga no tā, ko ar to darīsi.",
             ievads="Tā izskatās viens skaitlis četros veidos."),

    Kopsavilkums([
        "Pierakstu vienu skaitli kā daļu, decimāldaļu un procentus.",
        "Paplašinu un saīsinu daļas, nemainot vērtību.",
        "Izvēlos pierakstu pēc tā, ko ar skaitli darīšu.",
        "Salīdzinu skaitļus, tos vispirms pārveidojot vienā pierakstā.",
    ]),

    Majas([
        "Pieraksti {2|5} četros veidos.",
        "Salīdzini {3|8} un 0,4 - kurš ir lielāks?",
        "Atrodi veikalā divas atlaides dažādos pierakstos un salīdzini tās.",
    ]),
]
