# -*- coding: utf-8 -*-
"""4. klase, 33. stunda: «Ko darīt, ja nesanāk gludi?»

Dalīšana ar atlikumu: 29 : 4 = 7 (atl. 1). Atlikums vienmēr ir mazāks par
dalītāju - citādi varētu iedot vēl pa vienam. Šis noteikums ir pati
svarīgākā pārbaude, un to stunda atkārto vairākkārt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, restis)

TEMA = "Ko darīt, ja nesanāk gludi?"

MERKIS = ("Dalīsim ar atlikumu, nosauksim un pierakstīsim dalījumu un "
          "atlikumu.")

SATURS = [
    Sakums("29 kūciņas uz 4 šķīvjiem - cik paliks pāri?",
           zimejums=restis([["1. šķīvis", 7],
                            ["2. šķīvis", 7],
                            ["3. šķīvis", 7],
                            ["4. šķīvis", 7],
                            ["pāri", 1]],
                           "29 = 4 · 7 + 1"),
           paraksts="Katram 7, un viena paliek pāri.",
           fakti=["Ne katrs skaitlis dalās bez atlikuma.",
                  "Atlikums vienmēr ir mazāks par dalītāju."]),

    Doma("Dalījums un atlikums",
         "Atrodi lielāko reizinājumu, kas nepārsniedz dalāmo; tas dod "
         "dalījumu, un starpība ir atlikums.",
         soli=[
             "29 : 4 - kurš reizinājums ar 4 ir tuvākais, bet nepārsniedz 29?",
             "4 · 7 = 28 (4 · 8 = 32 jau par daudz).",
             "Atlikums: 29 − 28 = 1.",
             "Pieraksts: 29 : 4 = 7 (atl. 1). Pārbaudi: 1 < 4.",
         ],
         pieze="Ja atlikums sanāk lielāks vai vienāds ar dalītāju, dalījumu "
               "var palielināt - tātad kļūda."),

    Paraugs("47 : 6",
            uzd="Izdali 47 ar 6 ar atlikumu.",
            soli=[
                ("6 · 7 = 42", "Tuvākais, kas nepārsniedz 47."),
                ("47 − 42 = 5", "Atlikums."),
                ("5 < 6", "Atlikums mazāks par dalītāju - labi."),
            ],
            atbilde="47 : 6 = 7 (atl. 5)"),

    Slidnis("Kā mainās atlikums",
            soli=[
                {"v": "20 : 4 = 5 (atl. 0)", "teksts": "Dalās gludi."},
                {"v": "21 : 4 = 5 (atl. 1)", "teksts": "Paliek viens."},
                {"v": "22 : 4 = 5 (atl. 2)", "teksts": "Paliek divi."},
                {"v": "23 : 4 = 5 (atl. 3)", "teksts": "Paliek trīs."},
                {"v": "24 : 4 = 6 (atl. 0)", "teksts": "Atkal gludi - "
                 "atlikums nekad nesasniedz 4."},
            ],
            ievads="Dalītājs 4 - atlikums var būt tikai 0, 1, 2 vai 3."),

    Ievadi("Atrodi atlikumu", [
        {"jaut": "29 : 4 = 7 (atl. ?)", "atb": ["1"], "padoms": "29 − 28."},
        {"jaut": "38 : 5 = 7 (atl. ?)", "atb": ["3"], "padoms": "38 − 35."},
        {"jaut": "50 : 8 = 6 (atl. ?)", "atb": ["2"], "padoms": "50 − 48."},
        {"jaut": "Cik ir dalījums 61 : 9 (bez atlikuma daļas)?",
         "atb": ["6"], "padoms": "9 · 6 = 54, 9 · 7 = 63."},
        {"jaut": "Kāds atlikums 61 : 9?", "atb": ["7"],
         "padoms": "61 − 54."},
        {"jaut": "Kāds atlikums 45 : 7?", "atb": ["3"],
         "padoms": "7 · 6 = 42."},
    ], pamats=4),

    Varianti("Vai atlikums iespējams?", [
        {"jaut": "Dalot ar 5, kurš atlikums *nav* iespējams?",
         "opcijas": ["5", "4", "0", "3"], "pareizi": 0,
         "padoms": "Atlikums < dalītājs."},
        {"jaut": "Anna: 33 : 4 = 7 (atl. 5). Kas nepareizi?",
         "opcijas": ["atlikums lielāks par dalītāju", "viss pareizi",
                     "dalījums par lielu"], "pareizi": 0,
         "padoms": "Pareizi 8 (atl. 1)."},
        {"jaut": "Kāds ir lielākais iespējamais atlikums, dalot ar 9?",
         "opcijas": ["8", "9", "10", "1"], "pareizi": 0,
         "padoms": "Viens mazāk par dalītāju."},
        {"jaut": "Kurš skaitlis dalās ar 6 bez atlikuma?",
         "opcijas": ["42", "40", "44", "45"], "pareizi": 0,
         "padoms": "6 · 7 = 42."},
    ], pamats=4),

    Pasaule("Kas paliek virtuvē?",
            Ievadi("", [
                {"jaut": "53 olas sakrauj kastītēs pa 6. Cik pilnu kastīšu?",
                 "atb": ["8"], "padoms": "6 · 8 = 48."},
                {"jaut": "Cik olu paliek ārpus kastītēm?",
                 "atb": ["5"], "padoms": "53 − 48."},
                {"jaut": "35 pankūkas uz 4 šķīvjiem vienādi. Cik uz katra?",
                 "atb": ["8"], "padoms": "4 · 8 = 32."},
                {"jaut": "Cik pankūku paliek pāri?",
                 "atb": ["3"], "padoms": "35 − 32."},
            ]),
            pavediens="virtuve",
            konteksts="Virtuvē reti viss sadalās gludi - kaut kas vienmēr "
                      "paliek pāri.",
            kapec="Atlikums pasaka, cik paliks nesadalīts."),

    Kopsavilkums([
        "Dalu ar atlikumu.",
        "Pierakstu: dalāmais : dalītājs = dalījums (atl. ...).",
        "Zinu, ka atlikums vienmēr ir mazāks par dalītāju.",
    ]),

    Majas([
        "Sadali savas mantas (zīmuļus, kartiņas) 3 kaudzītēs. Kāds atlikums?",
        "Izrēķini, cik nedēļu un dienu ir 45 dienās.",
        "Atrodi skaitli, kas, dalot ar 4, dod atlikumu 3.",
    ]),
]
