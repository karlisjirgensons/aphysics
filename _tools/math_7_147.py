# -*- coding: utf-8 -*-
"""7. klase, 147. stunda: «Vai atrisinājums der situācijai?»

Vienādojumam var būt sakne, kas situācijai neder: negatīvs skaits,
daļskaitlis cilvēkiem, laiks pēc procesa beigām. Stunda trenē pārbaudi
situācijā un noapaļošanu pareizajā virzienā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Vai atrisinājums der situācijai?"

MERKIS = ("Noteiksim matemātiskā atrisinājuma atbilstību reālajai "
          "situācijai.")

SATURS = [
    Sakums("x = −4 bērni? x = 2,5 autobusi?",
           fakti=["Matemātika atrisina vienādojumu - ne situāciju.",
                  "Pēc atrisināšanas jājautā: vai tas ir iespējams?",
                  "Ja nē - jānoapaļo vai jāatzīst, ka atbildes nav."]),

    Doma("Pārbaudi situācijā",
         "Atrisinājums der situācijai, ja tas atbilst lieluma dabai "
         "(vesels, nenegatīvs) un situācijas robežām. Citādi to noapaļo "
         "pareizajā virzienā vai secina, ka situācija nav iespējama.",
         soli=[
             "Vai lielums var būt daļskaitlis?",
             "Vai tas var būt negatīvs?",
             "Vai tas ietilpst robežās (laiks, tilpums, vecums)?",
             "Noapaļo: vietas un iepakojumi - uz augšu; iespējamie pirkumi - "
             "uz leju.",
         ]),

    Paraugs("Neiespējama situācija",
            uzd="Tēvs 40 gadus vecs, dēls 10. Pēc cik gadiem tēvs būs "
                "3 reizes vecāks par dēlu? Pēc cik - 5 reizes vecāks?",
            soli=[
                ("40 + x = 3(10 + x) ⇒ x = 5", "Pēc 5 gadiem: 45 un 15."),
                ("40 + x = 5(10 + x) ⇒ x = −2,5", "Negatīvs."),
                ("−2,5 - pirms 2,5 gadiem", "Pagātnē: 37,5 un 7,5."),
            ],
            atbilde="3 reizes - pēc 5 gadiem; 5 reizes - bija pirms 2,5 gadiem."),

    Varianti("Der vai neder?", [
        {"jaut": "Skolēnu skaits x = 23,5",
         "opcijas": ["Neder - jābūt veselam", "Der",
                     "Der, noapaļo uz 24"],
         "pareizi": 0, "jaukt": False,
         "padoms": "Iespējams, datos ir kļūda."},
        {"jaut": "Laiks līdz vilciena atiešanai x = −10 min",
         "opcijas": ["Vilciens jau atgājis", "Der",
                     "Tas ir 10 min"],
         "pareizi": 0, "jaukt": False, "padoms": "Negatīvs laiks - pagātne."},
        {"jaut": "Ar 50 € var nopirkt x = 6,25 spēles",
         "opcijas": ["6 spēles", "7 spēles", "6,25 spēles"],
         "pareizi": 0, "jaukt": False, "padoms": "Uz leju."},
        {"jaut": "Vajag x = 6,25 kastes",
         "opcijas": ["7 kastes", "6 kastes", "6,25 kastes"],
         "pareizi": 0, "jaukt": False, "padoms": "Uz augšu - lai pietiktu."},
    ], pamats=4),

    Ievadi("Atrisini un interpretē", [
        {"jaut": "Laivā drīkst 4 cilvēki. Cik braucienu 18 cilvēkiem?",
         "atb": ["5"], "padoms": "4,5 - uz augšu."},
        {"jaut": "Biļete 7 €, ir 30 €. Cik biļetes?",
         "atb": ["4"], "padoms": "4,28 - uz leju."},
        {"jaut": "Tvertnē 100 l, tecē 8 l/min. Pēc cik pilnām min būs "
                 "mazāk par 10 l?",
         "atb": ["12"], "padoms": "100 − 8t < 10 ⇒ t > 11,25."},
    ]),

    Pasaule("Tūristu nometne",
            Ievadi("", [
                {"jaut": "Teltī 3 cilvēki, nometnē 47. Cik telšu?",
                 "atb": ["16"], "padoms": "15,67 - uz augšu."},
                {"jaut": "Telts maksā 12 € naktī, budžets 150 € naktī. Cik "
                         "telšu var atļauties?",
                 "atb": ["12"], "padoms": "12,5 - uz leju."},
                {"jaut": "Vai budžets pietiek visiem? Raksti «jā» vai «nē».",
                 "atb": ["nē", "ne"], "padoms": "Vajag 16, var 12."},
            ]),
            pavediens="celojums",
            konteksts="Nometnes plānotājs noapaļo telšu skaitu uz augšu, bet "
                      "budžetu - uz leju.",
            kapec="Viens aprēķins, divi noapaļošanas virzieni."),

    Kopsavilkums([
        "Pārbaudu, vai sakne der situācijai.",
        "Noapaļoju pareizajā virzienā.",
        "Interpretēju negatīvu atbildi (pagātne, zaudējums).",
        "Secinu, ja situācija nav iespējama.",
    ]),

    Majas([
        "Izdomā uzdevumu, kur sakne ir negatīva, un interpretē to.",
        "Aprēķini, cik transportlīdzekļu vajag ģimenes ceļojumam.",
        "Atrodi uzdevumu, kur jānoapaļo uz leju.",
    ]),
]
