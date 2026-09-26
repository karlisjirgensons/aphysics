# -*- coding: utf-8 -*-
"""8. klase, 1. stunda: «Kā iegūt ticamus datus?»

Gada pirmā stunda sākas ar jautājumu, ko uzdod katra ziņu virsraksta
priekšā: kam jautāja? Tie paši skaitļi no citas izlases stāsta citu stāstu,
tāpēc pirms jebkura vidējā vai diagrammas jāizvērtē, no kurienes dati nāk.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, Zimejums, kolonnas)

TEMA = "Kā iegūt ticamus datus?"

MERKIS = ("Mācīsimies plānot datu ieguvi un spriest, kā datu avots ietekmē "
          "secinājumus.")

SATURS = [
    Sakums("«90 % skolēnu mīl sportu!»",
           zimejums=kolonnas([("sporta zālē", 90), ("visā skolā", 55)], " %"),
           paraksts="Viens jautājums - divas aptaujas, divas atbildes.",
           fakti=["Pirmo aptauju veica sporta zālē pēc treniņa.",
                  "Otro - pie ieejas, katram desmitajam skolēnam.",
                  "Ticamāka ir tā, kurā katram ir vienāda iespēja tikt."]),

    Doma("Kopa un izlase",
         "Visus, par kuriem gribam uzzināt, sauc par *kopu* (populāciju). "
         "Ja visiem pajautāt nevar, izvēlas daļu - *izlasi*. Secinājums par "
         "visu kopu ir tik labs, cik laba ir izlase.",
         soli=[
             "Nosaki, par ko gribi spriest - tā ir kopa.",
             "Izlasē katram kopas pārstāvim jābūt vienādai iespējai tikt.",
             "Izlasei jābūt pietiekami lielai - 5 cilvēki nav «skola».",
             "Jautājums nedrīkst mudināt uz noteiktu atbildi.",
             "Pieraksti, kur, kad un kā dati iegūti.",
         ],
         pieze="Tieši tā strādā vēlēšanu aptaujas: Latvijā aptaujā ap 1000 "
               "cilvēku, bet izvēlas viņus no visiem novadiem un vecumiem."),

    Varianti("Vai izlase ir laba?", [
        {"jaut": "Grib uzzināt, cik skolēnu brauc uz skolu ar velosipēdu. "
                 "Kuru izlasi izvēlēties?",
         "opcijas": ["Katru piekto no skolēnu saraksta",
                     "Tos, kas stāv pie velosipēdu statīva",
                     "Tikai savas klases draugus",
                     "Tos, kas atnāk pirmie"],
         "pareizi": 0, "padoms": "Katram jābūt vienādai iespējai."},
        {"jaut": "Kurš jautājums ir godīgs?",
         "opcijas": ["Cik stundas nedēļā tu lasi grāmatas?",
                     "Vai tu, tāpat kā visi gudrie, lasi grāmatas?",
                     "Vai tev nepatīk garlaicīgas grāmatas?",
                     "Tu taču lasi daudz, vai ne?"],
         "pareizi": 0, "padoms": "Jautājums nedrīkst ieteikt atbildi."},
        {"jaut": "Veikals jautāja 10 pircējiem, vai cenas ir labas. 9 teica "
                 "«jā». Kas ir galvenā problēma?",
         "opcijas": ["Izlase ir par mazu", "Jautājums par garu",
                     "Pircēji ir kopa", "Problēmu nav"],
         "pareizi": 0, "padoms": "10 cilvēku ir maz."},
        {"jaut": "Tiešsaistes aptaujā par interneta lietošanu atbildēja "
                 "5000 cilvēku. Kas slikti?",
         "opcijas": ["Tā nesasniedz tos, kas internetu nelieto",
                     "5000 ir par maz", "Nekas", "Tā ir par dārgu"],
         "pareizi": 0, "padoms": "Kurš aptauju neredz?"},
    ]),

    Paraugs("No izlases uz visu skolu",
            uzd="Skolā mācās 480 skolēnu. Izlasē (katrs 8. no saraksta) 60 "
                "skolēnu; 21 no viņiem ēd skolas brokastis. Cik aptuveni "
                "ēd visā skolā?",
            soli=[
                ("{21|60} = 0,35 = 35 %", "Daļa izlasē."),
                ("480 · 0,35 = 168", "Tā pati daļa visā kopā."),
                ("Izlase bija nejauša un pietiekami liela",
                 "Tāpēc drīkst vispārināt."),
            ],
            atbilde="apmēram 168 skolēni"),

    Ievadi("Rēķini no izlases", [
        {"jaut": "Izlasē 50 skolēnu, 20 no viņiem ir mājdzīvnieks. Cik "
                 "procentu tas ir?",
         "atb": ["40", "40 %", "40%"], "padoms": "20 : 50 = 0,4."},
        {"jaut": "Skolā ir 600 skolēnu. Cik aptuveni skolēnu ir "
                 "mājdzīvnieks?",
         "atb": ["240"], "padoms": "40 % no 600."},
        {"jaut": "No 1000 aptaujātajiem 380 atbalsta jauno parku. Cik "
                 "procentu tas ir?",
         "atb": ["38", "38 %", "38%"], "padoms": "380 : 1000."},
        {"jaut": "Pilsētā 45 000 iedzīvotāju. Cik aptuveni atbalsta parku?",
         "atb": ["17100", "17 100"], "padoms": "0,38 · 45 000."},
    ]),

    Zimejums("Divas izlases - divi stāsti",
             kolonnas([("izlase A", 72), ("izlase B", 31), ("visi", 34)],
                      " %"),
             paskaidro="«Vai tev patīk basketbols?» A - basketbola spēlē, B - "
                       "nejaušā izlasē. Visas skolas rezultāts ir tuvāks B."),

    Pasaule("Skolas ēdnīcas aptauja",
            Ievadi("", [
                {"jaut": "Skolā ir 720 skolēnu. Aptaujā katru 12. no saraksta. "
                         "Cik skolēnu būs izlasē?",
                 "atb": ["60"], "padoms": "720 : 12."},
                {"jaut": "42 no izlases grib zupu katru dienu. Cik procentu "
                         "tas ir?",
                 "atb": ["70", "70 %", "70%"], "padoms": "42 : 60."},
                {"jaut": "Cik porciju zupas aptuveni jāvāra dienā visai "
                         "skolai?",
                 "atb": ["504"], "padoms": "70 % no 720."},
            ]),
            pavediens="skola",
            konteksts="Ēdnīca plāno porcijas pēc aptaujas - ja izlase ir "
                      "slikta, zupa paliek pāri vai pietrūkst.",
            kapec="Laba izlase ļauj pajautāt 60, bet spriest par 720."),

    Kopsavilkums([
        "Atšķiru kopu un izlasi.",
        "Izvērtēju, vai izlase ir nejauša un pietiekami liela.",
        "Pamanu jautājumu, kas mudina uz noteiktu atbildi.",
        "Vispārinu izlases rezultātu uz visu kopu.",
    ]),

    Majas([
        "Atrodi ziņās vienu aptaujas rezultātu un noskaidro, kam jautāja.",
        "Izdomā godīgu jautājumu aptaujai savā klasē.",
        "Uzraksti, kā izvēlētos izlasi no visas skolas.",
    ]),
]
