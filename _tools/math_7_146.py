# -*- coding: utf-8 -*-
"""7. klase, 146. stunda: «Kādi ir modelēšanas soļi?»

Matemātiskā modelēšana ir cikls: situācija → modelis (vienādojums) →
matemātiskais atrisinājums → interpretācija situācijā → pārbaude. Stunda
iziet visu ciklu un parāda, kur rodas kļūdas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kādi ir modelēšanas soļi?"

MERKIS = ("Nosauksim un lietosim matemātiskās modelēšanas soļus problēmas "
          "risināšanā.")

SATURS = [
    Sakums("Pieci soļi no problēmas līdz atbildei",
           zimejums=restis([["1", "Saprast situāciju"],
                            ["2", "Izveidot modeli (x, vienādojums)"],
                            ["3", "Atrisināt matemātiski"],
                            ["4", "Interpretēt: ko nozīmē x?"],
                            ["5", "Pārbaudīt situācijā"]]),
           fakti=["Inženieri, ekonomisti un ārsti strādā pēc šiem soļiem.",
                  "Visbiežāk kļūdās 1. un 4. solī - ne rēķinā."]),

    Doma("Modelēšanas cikls",
         "Matemātiskā modelēšana: 1) saprot situāciju un datus; 2) izveido "
         "modeli - apzīmējumus un vienādojumu; 3) atrisina; 4) interpretē "
         "atbildi situācijas valodā; 5) pārbauda, vai tā ir reāla. Ja nav - "
         "modeli labo.",
         soli=[
             "Kas zināms? Kas jāatrod? Kādas mērvienības?",
             "Kas ir x? Kāda vienādība?",
             "Atrisini.",
             "Atbilde vārdiem ar mērvienību.",
             "Vai skaitlis ir iespējams (vesels, pozitīvs, reāls)?",
         ]),

    Paraugs("Autobusu noma",
            uzd="Skolai jāved 130 skolēni; autobusā 45 vietas. Cik autobusu "
                "vajag?",
            soli=[
                ("Modelis: 45x = 130", "Vienādojums."),
                ("x = 2,88...", "Matemātiskā atbilde."),
                ("Interpretācija: 2 autobusi - par maz", "88 skolēni."),
                ("Vajag 3 autobusus", "Noapaļo uz augšu."),
            ],
            atbilde="3 autobusi."),

    Ievadi("Iziet visu ciklu", [
        {"jaut": "Lifts 8 cilvēki, rindā 50. Cik braucienu?",
         "atb": ["7"], "padoms": "50 : 8 = 6,25 - uz augšu."},
        {"jaut": "Krāsas bundža 2,5 l, vajag 11 l. Cik bundžu pirkt?",
         "atb": ["5"], "padoms": "11 : 2,5 = 4,4."},
        {"jaut": "Ar 20 € var nopirkt burtnīcas pa 1,5 €. Cik burtnīcu?",
         "atb": ["13"], "padoms": "13,33 - uz leju."},
        {"jaut": "Maratons 42 km, skrien 12 km/h. Cik min?",
         "atb": ["210"], "padoms": "3,5 h."},
    ]),

    Varianti("Kurš solis?", [
        {"jaut": "«x = 2,88 - tātad 3 autobusi.» Kurš solis?",
         "opcijas": ["Interpretācija", "Modelis", "Atrisināšana",
                     "Situācijas izpratne"],
         "pareizi": 0, "padoms": "Atbilde situācijai."},
        {"jaut": "«Apzīmēsim autobusu skaitu ar x.» Kurš solis?",
         "opcijas": ["Modelis", "Interpretācija", "Pārbaude",
                     "Atrisināšana"],
         "pareizi": 0, "padoms": "Apzīmējumi."},
        {"jaut": "Aprēķināts: klasē −3 skolēni. Kas jādara?",
         "opcijas": ["Jāpārbauda modelis - atbilde nav reāla",
                     "Jāatbild −3", "Jānoapaļo uz 0", "Jāatbild 3"],
         "pareizi": 0, "padoms": "5. solis."},
    ]),

    Pasaule("Dārza laistīšana",
            Ievadi("", [
                {"jaut": "Dārzam vajag 450 l ūdens nedēļā, lietus mucā 200 l. "
                         "Lejkanna 12 l. Cik lejkannu no krāna?",
                 "atb": ["21"], "padoms": "250 : 12 ≈ 20,8."},
                {"jaut": "Ja lietus nav un muca tukša, cik lejkannu?",
                 "atb": ["38"], "padoms": "450 : 12 = 37,5."},
                {"jaut": "Cik litru ietaupa muca (l)?",
                 "atb": ["200"], "padoms": "Mucas tilpums."},
            ]),
            pavediens="planeta",
            konteksts="Lietus ūdens krāšana ietaupa dzeramo ūdeni - "
                      "modelis parāda cik.",
            kapec="Modelis - no problēmas līdz lēmumam."),

    Kopsavilkums([
        "Nosaucu 5 modelēšanas soļus.",
        "Izveidoju modeli ar x un vienādojumu.",
        "Interpretēju atbildi situācijā (noapaļoju pareizi).",
        "Pārbaudu, vai atbilde ir reāla.",
    ]),

    Majas([
        "Modelē: cik pakas ūdens pudeļu vajag klases ekskursijai?",
        "Pieraksti visus 5 soļus.",
        "Atrodi situāciju, kur jānoapaļo uz leju.",
    ]),
]
