# -*- coding: utf-8 -*-
"""3. klase, 87. stunda: «Kāds ir tavs piemērs?»

Skolēns pats rada piemēru ar daļām un parāda to ar modeli. Tas ir tas pats
apgrieztais virziens, kas 23. un 32. stundā: kas prot izdomāt piemēru, tas
ir sapratis jēgu - un modelis neļauj piemēram būt tikai vārdiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         dala)

TEMA = "Kāds ir tavs piemērs?"

MERKIS = ("Radīsim savu piemēru ar daļām un parādīsim to ar modeli.")

SATURS = [
    Sakums("Kur tu esi redzējis daļas ārpus matemātikas stundas?",
           zimejums=dala(4, 3, "3/4", "trīs ceturtdaļas"),
           paraksts="Trīs ceturtdaļas ir arī pulkstenis, kūka un distance.",
           fakti=["Daļas ir pulkstenī, receptēs, sportā un veikalā.",
                  "Labā piemērā redzams gan veselais, gan daļa."]),

    Doma("Labā piemērā redzams veselais",
         "Vispirms pasaki, kas ir veselais, tikai tad - kāda daļa no tā "
         "tiek ņemta.",
         soli=[
             "Izvēlies veselo: kūku, distanci, stundu vai naudu.",
             "Pasaki, cik vienādās daļās tas sadalīts - tas ir saucējs.",
             "Pasaki, cik daļu tiek ņemts - tas ir skaitītājs.",
             "Uzzīmē modeli un pieraksti daļu.",
         ],
         pieze="Ja veselais nav nosaukts, daļa neko nenozīmē: «trīs "
               "ceturtdaļas» - no kā?"),

    Paraugs("Kā uzrakstīt savu piemēru?",
            uzd="Izveido piemēru ar daļu {3|4}.",
            soli=[
                ("Veselais - stunda, 60 minūtes",
                 "Vispirms izvēlas veselo."),
                ("Saucējs 4: 60 : 4 = 15 minūtes",
                 "Viena ceturtdaļa."),
                ("Skaitītājs 3: 3 · 15 = 45 minūtes",
                 "Trīs ceturtdaļas stundas ir 45 minūtes."),
            ],
            atbilde="{3|4} stundas ir 45 minūtes"),

    Petijums("Uzraksti savu piemēru",
             vajag="lapa, zīmulis un krāsainie zīmuļi",
             soli=[
                 "Izvēlies daļu, piemēram {2|5} vai {5|6}.",
                 "Izdomā veselo no savas dzīves.",
                 "Uzzīmē modeli un iekrāso daļu.",
                 "Iedod piemēru klasesbiedram un lūdz nosaukt daļu.",
             ],
             secinajums="Ja klasesbiedrs nosauca to pašu daļu, modelis ir "
                        "skaidrs."),

    Ievadi("Atrisini klasesbiedru piemērus", [
        {"jaut": "{1|4} no 60 minūtēm. Cik minūšu?", "atb": ["15"],
         "padoms": "60 : 4."},
        {"jaut": "{3|4} no 60 minūtēm. Cik minūšu?", "atb": ["45"],
         "padoms": "3 · 15."},
        {"jaut": "{2|5} no 100 cm. Cik centimetru?", "atb": ["40"],
         "padoms": "100 : 5 = 20; 2 · 20."},
        {"jaut": "{5|6} no 30 eiro. Cik eiro?", "atb": ["25"],
         "padoms": "30 : 6 = 5; 5 · 5."},
        {"jaut": "{3|8} no 400 m. Cik metru?", "atb": ["150"],
         "padoms": "400 : 8 = 50; 3 · 50."},
        {"jaut": "{2|3} no 900 g. Cik gramu?", "atb": ["600"],
         "padoms": "900 : 3 = 300; 2 · 300."},
    ], pamats=4),

    Zimejums("Modelis piemēram",
             dala(5, 2, "2/5 no 100 cm = 40 cm", "pieci posmi pa 20 cm"),
             paskaidro="Modelī redzams gan veselais (100 cm), gan viena daļa "
                       "(20 cm), gan ņemtās daļas.",
             ievads="Tā izskatās labs piemēra modelis."),

    Varianti("Vai piemērs ir labs?", [
        {"jaut": "«Es apēdu trīs ceturtdaļas.» Kas pietrūkst?",
         "opcijas": ["Nav pateikts, no kā", "Nav pateikts, cik daļu",
                     "Nav pateikts, kad", "Nekas nepietrūkst"],
         "pareizi": 0, "padoms": "Daļa vienmēr ir daļa no kaut kā."},
        {"jaut": "Kurš piemērs ir pilnīgs?",
         "opcijas": ["{1|4} no 60 minūtēm ir 15 minūtes",
                     "{1|4} ir 15", "Ceturtdaļa ir maza",
                     "{1|4} no visa"],
         "pareizi": 0, "padoms": "Nosaukts veselais un rezultāts."},
        {"jaut": "Cik ir {1|2} no 80?",
         "opcijas": ["40", "20", "60", "160"],
         "pareizi": 0, "padoms": "80 : 2."},
        {"jaut": "Kā pārbaudīt savu piemēru?",
         "opcijas": ["Iedot to klasesbiedram", "Pārrakstīt skaistāk",
                     "Izrēķināt vēlreiz tāpat", "Nekā"],
         "pareizi": 0, "padoms": "Cits pamanīs to, ko tu neredzi."},
    ], pamats=4),

    Pasaule("Uzraksti piemēru par sportu",
            Ievadi("", [
                {"jaut": "Spēle ilgst 60 minūtes. Cik minūšu ir {1|2} spēles?",
                 "atb": ["30"], "padoms": "60 : 2."},
                {"jaut": "Cik minūšu ir {1|4} spēles?", "atb": ["15"],
                 "padoms": "60 : 4."},
                {"jaut": "Distance 1200 m. Cik metru ir {1|3}?",
                 "atb": ["400"], "padoms": "1200 : 3."},
                {"jaut": "Cik metru ir {2|3}?", "atb": ["800"],
                 "padoms": "2 · 400."},
            ]),
            pavediens="sports",
            konteksts="Sporta pārraidēs daļas saka visu laiku: «puse spēles», "
                      "«pēdējā ceturtdaļa».",
            kapec="Katrā no tiem ir gan veselais, gan daļa - tāpēc tos "
                  "saprot uzreiz."),

    Kopsavilkums([
        "Radu savu piemēru ar daļām.",
        "Nosaucu veselo un daļu.",
        "Parādu piemēru ar modeli.",
        "Izvērtēju klasesbiedra piemēru.",
    ]),

    Majas([
        "Uzraksti divus piemērus ar daļām no savas dzīves.",
        "Uzzīmē modeli vienam no tiem.",
        "Pastāsti abus mājiniekiem un pārbaudi, vai viņi saprot.",
    ]),
]
