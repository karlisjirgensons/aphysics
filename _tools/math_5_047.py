# -*- coding: utf-8 -*-
"""5. klase, 47. stunda: «Kā mainās reizinājums, mainot reizinātāju?»

Temata pēdējā stunda pirms pārbaudes darba, un tā ir 22. stundas pāriniece:
tur vispārinājumus veidoja summai un starpībai, te - reizinājumam un
dalījumam. Atšķirība ir būtiska: te locekli nevis palielina *par* kaut cik,
bet *tik reižu*.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā mainās reizinājums, mainot reizinātāju?"

MERKIS = ("Mācīsimies raksturot, kā mainās reizinājums un dalījums, mainot "
          "kādu darbības locekli.")

SATURS = [
    Sakums("Vai atbilde jārēķina no jauna?",
           fakti=["Zināms, ka 24 · 5 = 120.",
                  "Cik ir 48 · 5? Un cik ir 24 · 10?",
                  "Abas atbildes var pateikt, neko nerēķinot."]),

    Doma("Reizinātājs aug tik reižu - aug arī reizinājums",
         "Ja vienu reizinātāju palielina divas reizes, arī reizinājums kļūst "
         "divreiz lielāks.",
         soli=[
             "Salīdzini jauno izteiksmi ar veco: kurš loceklis mainījās?",
             "Nosaki, cik reižu tas mainījās.",
             "Reizinājumā: tikpat reižu mainās arī rezultāts.",
             "Dalījumā: dalāmais velk uz to pašu pusi, dalītājs - uz "
             "pretējo.",
         ],
         pieze="Ja abus reizinātājus palielina divas reizes, reizinājums aug "
               "nevis divas, bet četras reizes: 2 · 2 = 4. Tāpēc kvadrāta "
               "laukums aug četrkārt, ja malu palielina divkārt."),

    Paraugs("Trīs izteiksmes, viens rēķins",
            uzd="Zināms, ka 24 · 5 = 120. Cik ir 48 · 5, 24 · 10 un 12 · 5?",
            soli=[
                ("48 · 5 = 240",
                 "Pirmais reizinātājs divreiz lielāks - reizinājums arī."),
                ("24 · 10 = 240",
                 "Otrs reizinātājs divreiz lielāks - tas pats iznākums."),
                ("12 · 5 = 60",
                 "Pirmais reizinātājs divreiz mazāks - reizinājums arī."),
            ],
            atbilde="240, 240 un 60"),

    Ievadi("Zināms, ka 24 · 5 = 120 un 120 : 4 = 30", [
        {"jaut": "Cik ir 48 · 5?", "atb": ["240"],
         "padoms": "Reizinātājs divreiz lielāks."},
        {"jaut": "Cik ir 24 · 10?", "atb": ["240"],
         "padoms": "Otrs reizinātājs divreiz lielāks."},
        {"jaut": "Cik ir 12 · 5?", "atb": ["60"],
         "padoms": "Reizinātājs divreiz mazāks."},
        {"jaut": "Cik ir 48 · 10?", "atb": ["480"],
         "padoms": "Abi divreiz lielāki: 2 · 2 = 4 reizes."},
        {"jaut": "Cik ir 240 : 4?", "atb": ["60"],
         "padoms": "Dalāmais divreiz lielāks."},
        {"jaut": "Cik ir 120 : 8?", "atb": ["15"],
         "padoms": "Dalītājs divreiz lielāks - dalījums divreiz mazāks."},
        {"jaut": "Cik ir 120 : 2?", "atb": ["60"],
         "padoms": "Dalītājs divreiz mazāks."},
        {"jaut": "Cik ir 24 · 50?", "atb": ["1200"],
         "padoms": "Reizinātājs desmit reizes lielāks."},
    ], pamats=4,
        ievads="Nerēķini no gala - paskaties, kas mainījās un cik reižu."),

    Varianti("Formulē vispārinājumu", [
        {"jaut": "Vienu reizinātāju palielina 3 reizes. Kas notiek ar "
                 "reizinājumu?",
         "opcijas": ["Palielinās 3 reizes", "Palielinās par 3",
                     "Nemainās", "Palielinās 9 reizes"],
         "pareizi": 0,
         "padoms": "Pārbaudi ar 2 · 5 un 6 · 5."},
        {"jaut": "Dalītāju palielina 2 reizes. Kas notiek ar dalījumu?",
         "opcijas": ["Samazinās 2 reizes", "Palielinās 2 reizes",
                     "Nemainās", "Samazinās par 2"],
         "pareizi": 0,
         "padoms": "Vairāk cilvēku dala - mazāka daļa."},
        {"jaut": "Abus reizinātājus palielina 2 reizes. Cik reižu aug "
                 "reizinājums?",
         "opcijas": ["4 reizes", "2 reizes", "8 reizes", "Nemainās"],
         "pareizi": 0,
         "padoms": "2 · 2."},
        {"jaut": "Vienu reizinātāju palielina 2 reizes, otru samazina "
                 "2 reizes. Kas notiek?",
         "opcijas": ["Reizinājums nemainās", "Aug 2 reizes",
                     "Sarūk 2 reizes", "Aug 4 reizes"],
         "pareizi": 0,
         "padoms": "Viena izmaiņa atsver otru."},
        {"jaut": "Gan dalāmo, gan dalītāju palielina 3 reizes. Kas notiek ar "
                 "dalījumu?",
         "opcijas": ["Nemainās", "Aug 3 reizes", "Sarūk 3 reizes",
                     "Aug 9 reizes"],
         "pareizi": 0,
         "padoms": "120 : 4 un 360 : 12."},
        {"jaut": "Ar ko šī kārtula atšķiras no 22. stundas kārtulas par "
                 "summu?",
         "opcijas": ["Te locekli maina tik reižu, tur - par tik",
                     "Te nekas nemainās",
                     "Tur bija iekavas",
                     "Atšķirības nav"],
         "pareizi": 0,
         "padoms": "Summā pieskaita, reizinājumā reizina."},
    ], pamats=4),

    Pasaule("Cik vietas aizņems divreiz vairāk?",
            Ievadi("", [
                {"jaut": "24 faili pa 5 MB aizņem 120 MB. Cik aizņems "
                         "48 faili pa 5 MB?",
                 "atb": ["240"], "padoms": "Failu divreiz vairāk."},
                {"jaut": "Cik aizņems 24 faili pa 10 MB?",
                 "atb": ["240"], "padoms": "Katrs fails divreiz lielāks."},
                {"jaut": "120 MB sadala 4 mapēs - katrā 30 MB. Cik būs katrā, "
                         "ja mapju ir 8?",
                 "atb": ["15"], "padoms": "Dalītājs divreiz lielāks."},
                {"jaut": "Attēla mala aug 2 reizes. Cik reižu aug punktu "
                         "skaits?",
                 "atb": ["4"], "padoms": "Aug abas malas: 2 · 2."},
            ]),
            pavediens="dati",
            konteksts="Failu skaits un izmērs mainās nevis par dažiem, bet "
                      "reizēm - divreiz, desmitreiz.",
            kapec="Ja zini veco rezultātu, jauno var pateikt bez "
                  "rēķināšanas."),

    Kopsavilkums([
        "Raksturoju, kā mainās reizinājums, mainot reizinātāju.",
        "Raksturoju, kā mainās dalījums, mainot dalāmo vai dalītāju.",
        "Zinu, ka dalījums nemainās, ja abus locekļus maina vienādi.",
        "Atšķiru izmaiņu «par tik» no izmaiņas «tik reižu».",
    ]),

    Majas([
        "Uzraksti vienu reizinājumu un piecus tam tuvus, kurus vari pateikt "
        "bez rēķināšanas.",
        "Pārbaudi ar kalkulatoru, vai tavi vispārinājumi turas.",
        "Padomā, cik reižu aug kuba tilpums, ja malu palielina divreiz.",
    ]),
]
