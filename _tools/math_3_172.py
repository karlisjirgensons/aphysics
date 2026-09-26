# -*- coding: utf-8 -*-
"""3. klase, 172. stunda: «Ko gribu iemācīties 4. klasē?»

Gada pēdējā stunda. Skolēns apkopo, ko iemācījies, un ieskatās nākamajā
gadā: 4. klasē nāk skaitļi līdz miljonam, rakstiskā reizināšana un dalīšana
un daļu saskaitīšana. Tas nav pārbaudījums, bet karte uz priekšu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Ko gribu iemācīties 4. klasē?"

MERKIS = ("Apkoposim gadā apgūto un iepazīsimies ar 4. klases tematiem.")

SATURS = [
    Sakums("Kas gaida nākamajā gadā?",
           zimejums=restis([["3. klasē", "4. klasē"],
                            ["skaitļi līdz 1000", "līdz miljonam"],
                            ["reizina galvā", "reizina stabiņā"],
                            ["daļas pazīst", "daļas saskaita"]],
                           "no šī gada uz nākamo"),
           paraksts="Katra nākamā prasme aug no tās, kas jau ir.",
           fakti=["4. klasē skaitļi kļūst lielāki, bet paņēmieni paliek tie "
                  "paši.",
                  "Reizināšanas tabula būs vajadzīga katru dienu."]),

    Doma("Nākamā gada prasmes aug no šī gada",
         "Reizināšana stabiņā ir tā pati reizināšana pa daļām; daļu "
         "saskaitīšana - tā pati, tikai ar dažādiem saucējiem.",
         soli=[
             "Pieraksti trīs lietas, kuras šogad iemācījies vislabāk.",
             "Pieraksti vienu, kas vēl nav droša.",
             "Paskaties, ko no tā prasīs 4. klase.",
             "Uzraksti vienu mērķi nākamajam gadam.",
         ],
         pieze="Vienīgā prasme, bez kuras 4. klasē būs patiešām grūti, ir "
               "reizināšanas tabula - tāpēc tai vasarā ir vērts dažas "
               "minūtes nedēļā."),

    Petijums("Uzraksti savu gada karti",
             vajag="lapa un zīmulis",
             soli=[
                 "Uzzīmē divas kolonnas: «protu» un «vēl mācos».",
                 "Ieraksti tajās šī gada tēmas.",
                 "Apvelc vienu, ko gribi uzlabot vispirms.",
                 "Uzraksti, ko darīsi vasarā, lai to sasniegtu.",
             ],
             secinajums="Karte ar vienu apvilktu mērķi strādā labāk nekā "
                        "saraksts ar desmit."),

    Paraugs("Kā no šī gada aug nākamais?",
            uzd="Šogad mācījāmies 24 · 3 rēķināt pa daļām. Kā tas palīdzēs "
                "4. klasē?",
            soli=[
                ("24 · 3 = 20 · 3 + 4 · 3",
                 "Šī gada paņēmiens."),
                ("Stabiņā dara to pašu",
                 "Tikai pieraksta īsāk, pa kolonnām."),
                ("Jauns ir tikai pieraksts",
                 "Doma paliek tā pati."),
            ],
            atbilde="stabiņš ir tas pats rēķins, tikai īsāks"),

    Ievadi("Viss gads vienā vietā", [
        {"jaut": "7 · 8 = ?", "atb": ["56"], "padoms": "49 + 7."},
        {"jaut": "96 : 4 = ?", "atb": ["24"], "padoms": "80 : 4 un 16 : 4."},
        {"jaut": "268 + 154 = ?", "atb": ["422"], "padoms": "Divi pārnesumi."},
        {"jaut": "703 − 258 = ?", "atb": ["445"], "padoms": "Caur nulli."},
        {"jaut": "Cik ir {3|4} no 60?", "atb": ["45"], "padoms": "3 · 15."},
        {"jaut": "Taisnstūris 8 cm un 5 cm. Cik ir laukums?", "atb": ["40"],
         "padoms": "8 · 5."},
        {"jaut": "Cik ir tā paša taisnstūra perimetrs?", "atb": ["26"],
         "padoms": "2 · 13."},
        {"jaut": "Kubs 3 x 3 x 3. Cik ir tilpums kubos?", "atb": ["27"],
         "padoms": "9 · 3."},
    ], pamats=6),

    Zimejums("Gada tēmas",
             restis([["temats", "galvenā prasme"],
                     ["reizināšana", "tabula līdz 10"],
                     ["izteiksmes", "darbību secība"],
                     ["daļas", "daļa no skaita"],
                     ["ģeometrija", "laukums un tilpums"]],
                    "3. klases karte"),
             paskaidro="Katra rinda ir viens gada temats un viena prasme, kas "
                       "no tā paliek.",
             ievads="Viss gads vienā tabulā."),

    Varianti("Kas gaida 4. klasē?", [
        {"jaut": "Kura prasme 4. klasē būs vajadzīga katru dienu?",
         "opcijas": ["Reizināšanas tabula", "Cirkuļa lietošana",
                     "Izklājumu locīšana", "Diagrammu zīmēšana"],
         "pareizi": 0, "padoms": "Bez tās nevar ne reizināt, ne dalīt."},
        {"jaut": "Kas ir reizināšana stabiņā?",
         "opcijas": ["Tā pati reizināšana pa daļām, īsāk pierakstīta",
                     "Pavisam jauna darbība", "Dalīšana otrādi",
                     "Saskaitīšana"],
         "pareizi": 0, "padoms": "Doma paliek tā pati."},
        {"jaut": "Līdz kādiem skaitļiem rēķina 4. klasē?",
         "opcijas": ["Līdz miljonam", "Līdz tūkstotim", "Līdz simtam",
                     "Līdz miljardam"],
         "pareizi": 0, "padoms": "Tūkstoškārt vairāk nekā šogad."},
        {"jaut": "Ko vērts darīt vasarā?",
         "opcijas": ["Dažas minūtes nedēļā atkārtot tabulu",
                     "Neko", "Izlasīt visu mācību grāmatu",
                     "Rēķināt katru dienu stundu"],
         "pareizi": 0, "padoms": "Mazs, bet regulārs darbs."},
    ], pamats=4),

    Pasaule("Ko izrēķināsi vasarā?",
            Ievadi("", [
                {"jaut": "Brīvlaiks 90 dienas. Cik nedēļu tas ir? Ieraksti "
                         "pilnu nedēļu skaitu.",
                 "atb": ["12"], "padoms": "12 · 7 = 84."},
                {"jaut": "Cik dienu paliek pāri?", "atb": ["6"],
                 "padoms": "90 − 84."},
                {"jaut": "Ja katru nedēļu atkārto 5 reizinājumus, cik to "
                         "sanāks 12 nedēļās?",
                 "atb": ["60"], "padoms": "12 · 5."},
                {"jaut": "Cik minūšu tas ir, ja katrai reizei vajag 5 "
                         "minūtes?",
                 "atb": ["60"], "padoms": "12 · 5."},
            ]),
            pavediens="skola",
            konteksts="Visa vasaras tabulas treniņa laiks ir viena stunda - "
                      "sadalīta pa piecām minūtēm nedēļā.",
            kapec="Viena stunda vasarā ietaupa daudzas stundas septembrī."),

    Kopsavilkums([
        "Apkopoju, ko šogad iemācījos.",
        "Zinu, kura prasme man vēl nav droša.",
        "Zinu, kas mani gaida 4. klasē.",
        "Esmu uzrakstījis sev vienu mērķi.",
    ]),

    Majas([
        "Uzraksti savu gada karti ar divām kolonnām.",
        "Apvelc vienu mērķi vasarai.",
        "Paglabā karti un paskaties uz to septembrī.",
    ], ievads="Šī ir pēdējā šī gada stunda. Uz tikšanos 4. klasē!"),
]
