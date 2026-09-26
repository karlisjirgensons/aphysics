# -*- coding: utf-8 -*-
"""9. klase, 38. stunda: «Kur tādas formas sastopamas?»

Temata noslēgums ar vienu lielu praktisku projektu: betona bruģakmens
apmale, pagalma dambis vai jumta daļa - viss ir trapeces prizmas. Skolēns
apvieno laukumu, Pitagoru, virsmu un tilpumu vienā aprēķinā un izmaksās.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, trapeces_prizma)

TEMA = "Kur tādas formas sastopamas?"

MERKIS = ("Risināsim praktisku uzdevumu par konstrukciju ar trapeces "
          "formu.")

SATURS = [
    Sakums("Trapeces prizmas ap mums",
           zimejums=trapeces_prizma(9, 5, 3, 8),
           paraksts="Ceļa uzbērums, grāvis, apmales akmens, jumts.",
           fakti=["Ceļa uzbērums šķērsgriezumā ir trapece.",
                  "Betona apmale - trapeces prizma ar nošķeltu augšu.",
                  "Būvniecībā tilpums nosaka materiālu un cenu."]),

    Doma("No zīmējuma līdz tāmei",
         "Praktisks uzdevums = ģeometrija + mērvienības + izmaksas.",
         soli=[
             "Atrodi, kura skaldne ir trapece (pamats).",
             "Aprēķini trūkstošos garumus (Pitagors).",
             "Tilpums - materiālam, virsma - krāsai vai apdarei.",
             "Pārvērš mērvienības un reizini ar cenu.",
         ]),

    Pasaule("Ceļa uzbērums",
            Ievadi("", [
                {"jaut": "Uzbēruma šķērsgriezums: apakšā 14 m, augšā 8 m, "
                         "augstums 2 m. Laukums (m²)?", "atb": ["22"],
                 "padoms": "11 · 2."},
                {"jaut": "Uzbērums 500 m garš. Cik m³ grunts?",
                 "atb": ["11000", "11 000"], "padoms": "22 · 500."},
                {"jaut": "Kravas auto ved 10 m³. Cik reisu?",
                 "atb": ["1100", "1 100"], "padoms": "11 000 : 10."},
                {"jaut": "Slīpā nogāze: katetes 3 m un 2 m. Nogāzes platums "
                         "līdz desmitdaļām (m)?", "atb": ["3,6"],
                 "padoms": "√13 ≈ 3,61."},
            ]),
            pavediens="celojums",
            konteksts="Jaunu ceļu būvē uz uzbēruma, lai pavasarī to neapplūdina.",
            kapec="Viena formula - un zināms, cik mašīnu grunts vajag."),

    Pasaule("Betona apmale",
            Ievadi("", [
                {"jaut": "Apmales šķērsgriezums: apakšā 15 cm, augšā 10 cm, "
                         "augstums 30 cm. Laukums (cm²)?", "atb": ["375"],
                 "padoms": "12,5 · 30."},
                {"jaut": "Apmale 1 m gara. Tilpums (dm³)?", "atb": ["37,5"],
                 "padoms": "375 cm² · 100 cm = 37 500 cm³."},
                {"jaut": "Betona blīvums 2,4 kg/dm³. Masa (kg)?",
                 "atb": ["90"], "padoms": "37,5 · 2,4."},
            ]),
            pavediens="tehnika",
            konteksts="Ietves apmale ir 1 m gari betona gabali ar trapeces "
                      "šķērsgriezumu.",
            kapec="Masa pasaka, vai to var pacelt divi strādnieki."),

    Petijums("Tavs projekts", [
        "Izvēlies objektu: grāvis, dobe, plaukts, rampa vai jumts.",
        "Uzzīmē šķērsgriezumu un izmēri (vai novērtē) izmērus.",
        "Aprēķini tilpumu un virsmu.",
        "Atrodi materiāla cenu internetā un sastādi tāmi.",
    ], vajag="mērlente, kalkulators",
       secinajums="Tāmē redzams, kuri izmēri visvairāk ietekmē cenu."),

    Varianti("Ko aprēķināt?", [
        {"jaut": "Cik krāsas vajag siles krāsošanai?",
         "opcijas": ["Virsmas laukumu", "Tilpumu", "Perimetru",
                     "Augstumu"],
         "pareizi": 0, "padoms": "Krāsa klāj virsmu."},
        {"jaut": "Cik betona vajag apmalei?",
         "opcijas": ["Tilpumu", "Virsmu", "Viduslīniju", "Diagonāli"],
         "pareizi": 0, "padoms": "Betons aizpilda telpu."},
        {"jaut": "Cik m apmales lentes vajag ap dobes trapeci?",
         "opcijas": ["Perimetru", "Laukumu", "Tilpumu", "Augstumu"],
         "pareizi": 0, "padoms": "Gar malām."},
    ]),

    Ievadi("Mērvienības", [
        {"jaut": "2,5 m³ = ? l", "atb": ["2500"], "padoms": "· 1000."},
        {"jaut": "4500 cm³ = ? dm³", "atb": ["4,5"], "padoms": ": 1000."},
        {"jaut": "0,3 m² = ? cm²", "atb": ["3000"], "padoms": "· 10 000."},
    ]),

    Kopsavilkums([
        "Saskatu trapeces prizmu būvēs un priekšmetos.",
        "Izvēlos: tilpums, virsma vai perimetrs.",
        "Sastādu vienkāršu tāmi.",
    ]),

    Majas([
        "Pabeidz projekta tāmi un noformē to vienā lapā.",
        "Atkārto 9.2. tematu - nākamajā stundā pārbaudes darbs.",
        "Izveido kopsavilkuma tabulu ar visām trapeces formulām.",
    ], ievads="Pārbaudes darbā būs: leņķi, viduslīnija, laukums, prizma."),
]
