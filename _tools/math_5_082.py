# -*- coding: utf-8 -*-
"""5. klase, 82. stunda: «Kā zīmējums palīdz?»

Kad uzdevumā ir trīs skaitļi un divas attiecības, teksts vairs neietilpst
galvā. Shematisks zīmējums ir tas, kas to notur: viena josla, sadalīta
vienādās daļās, un uzraksti pie gabaliem. Šī stunda nemāca jaunu rēķinu -
tā māca, ko zīmēt, pirms sāk rēķināt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Petijums, Varianti, Zimejums, dala)

TEMA = "Kā zīmējums palīdz?"

MERKIS = ("Mācīsimies veidot shematisku zīmējumu, lai attēlotu vienu skaitli "
          "kā otra skaitļa daļu.")

SATURS = [
    Sakums("Trīs skaitļi vienā teikumā",
           zimejums=dala(5, 2, "2/5 preču"),
           paraksts="No 20 precēm 8 ir atlaidē: divas piektdaļas joslas.",
           fakti=["Veikalā ir 20 preces, atlaidē 8.",
                  "Teksts ir garš, josla - īsa.",
                  "Zīmējumā uzreiz redz, cik liela daļa tā ir."]),

    Doma("Zīmē joslu, pirms sāc rēķināt",
         "Shematiskā zīmējumā visa josla ir veselais, tā sadalīta vienādās "
         "daļās, un pie katra gabala pieraksta, ko tas nozīmē.",
         soli=[
             "Nosaki, kas uzdevumā ir veselais - tā ir visa josla.",
             "Sadali joslu tik daļās, cik rāda saucējs.",
             "Iekrāso tik gabalu, cik rāda skaitītājs.",
             "Pieraksti pie joslas gan daļu, gan skaitļus.",
             "Tikai tad sāc rēķināt.",
         ],
         pieze="Zīmējums nav ilustrācija, bet darbarīks: kad josla ir "
               "uzzīmēta, uzdevums parasti atrisinās pats - redzams, kurš "
               "skaitlis pieder kuram gabalam."),

    Paraugs("No 20 precēm 8 ir atlaidē",
            uzd="Uzzīmē shēmu un nosaki, kāda daļa preču ir atlaidē.",
            soli=[
                ("Josla ir 20 preces",
                 "Veselais."),
                ("{8|20} = {2|5}",
                 "Saīsināta daļa."),
                ("Sadali joslu 5 daļās",
                 "Katrā daļā 4 preces."),
                ("Iekrāso 2 daļas",
                 "Tās ir 8 preces."),
                ("Pieraksti: 1 daļa = 4 preces",
                 "Tagad no shēmas var nolasīt jebkuru skaitli."),
            ],
            atbilde="Atlaidē ir {2|5} preču"),

    Petijums("Uzzīmē shēmu pats",
             soli=["Uzzīmē 10 cm garu joslu - tā ir visa nauda, 30 €.",
                   "Sadali to 3 vienādās daļās; katra daļa ir 10 €.",
                   "Iekrāso 2 daļas - tik iztērēts.",
                   "Pieraksti pie joslas: {2|3} un 20 €.",
                   "Pārbaudi ar rēķinu: 30 : 3 · 2."],
             vajag="lineāls, zīmulis, krāsainie zīmuļi",
             secinajums="Shēma un rēķins dod vienu un to pašu skaitli - "
                        "20 €."),

    Ievadi("Nolasi no shēmas", [
        {"jaut": "Josla ir 20 preces, sadalīta 5 daļās. Cik preču ir vienā "
                 "daļā?",
         "atb": ["4"], "padoms": "20 : 5."},
        {"jaut": "Iekrāsotas 2 daļas. Cik preču tas ir?",
         "atb": ["8"], "padoms": "4 · 2."},
        {"jaut": "Josla ir 30 €, sadalīta 3 daļās. Cik eiro ir vienā daļā?",
         "atb": ["10"], "padoms": "30 : 3."},
        {"jaut": "Josla ir 24 skolēni, sadalīta 4 daļās. Cik skolēnu ir "
                 "vienā daļā?",
         "atb": ["6"], "padoms": "24 : 4."},
        {"jaut": "Iekrāsotas 3 daļas no 4. Cik skolēnu tas ir?",
         "atb": ["18"], "padoms": "6 · 3."},
        {"jaut": "No 20 precēm 8 ir atlaidē. Kāda daļa? Atbildi raksti kā "
                 "a/b.",
         "atb": ["2/5", "8/20"], "padoms": "Abus dala ar 4."},
        {"jaut": "No 36 precēm 12 ir atlaidē. Kāda daļa? Atbildi raksti kā "
                 "a/b.",
         "atb": ["1/3", "12/36"], "padoms": "Abus dala ar 12."},
        {"jaut": "Josla ir 45 €, sadalīta 5 daļās. Cik eiro ir trīs daļas?",
         "atb": ["27"], "padoms": "45 : 5 · 3."},
    ], pamats=4,
        ievads="Vispirms viena daļa, tad tik daļu, cik vajag."),

    Zimejums("Divas daļas no piecām",
             dala(5, 2, "2/5"),
             paskaidro="Katra daļa ir 4 preces, tāpēc iekrāsotās divas ir "
                       "8 preces. Neiekrāsotās trīs ir 12 preces.",
             ievads="No vienas shēmas var nolasīt visus uzdevuma skaitļus."),

    Varianti("Ko zīmē vispirms?", [
        {"jaut": "Kas shēmā ir visa josla?",
         "opcijas": ["Veselais", "Gabals", "Daļa", "Atbilde"],
         "pareizi": 0,
         "padoms": "Josla ir tas, no kā ņem daļu."},
        {"jaut": "Cik daļās sadala joslu?",
         "opcijas": ["Tik, cik rāda saucējs", "Tik, cik rāda skaitītājs",
                     "Vienmēr desmit", "Cik vien gribas"],
         "pareizi": 0,
         "padoms": "Saucējs pasaka gabalu skaitu."},
        {"jaut": "Kāpēc pie joslas pieraksta arī skaitļus?",
         "opcijas": ["Lai zinātu, cik liela ir viena daļa",
                     "Lai zīmējums ir krāsains",
                     "Lai daļa kļūtu lielāka",
                     "Tas nav vajadzīgs"],
         "pareizi": 0,
         "padoms": "Viena daļa ir atslēga uz atbildi."},
        {"jaut": "Josla ir 20, sadalīta 5 daļās. Viena daļa ir...",
         "opcijas": ["4", "5", "20", "2"],
         "pareizi": 0,
         "padoms": "20 : 5."},
        {"jaut": "Kad zīmē shēmu?",
         "opcijas": ["Pirms rēķināšanas", "Pēc atbildes",
                     "Tikai pārbaudei", "Nekad"],
         "pareizi": 0,
         "padoms": "Shēma palīdz saprast uzdevumu."},
        {"jaut": "Kas shēmā ir neiekrāsotā daļa?",
         "opcijas": ["Atlikums", "Veselais", "Kļūda", "Nekas"],
         "pareizi": 0,
         "padoms": "Tas, kas nav uzskaitīts."},
    ], pamats=4),

    Pasaule("Cik preču ir atlaidē?",
            Ievadi("", [
                {"jaut": "Plauktā 40 preces, atlaidē 10. Kāda daļa? Atbildi "
                         "raksti kā a/b.",
                 "atb": ["1/4", "10/40"], "padoms": "{10|40}."},
                {"jaut": "Cik preču ir vienā ceturtdaļā?",
                 "atb": ["10"], "padoms": "40 : 4."},
                {"jaut": "Citā plauktā 60 preces, atlaidē 20. Kāda daļa? "
                         "Atbildi raksti kā a/b.",
                 "atb": ["1/3", "20/60"], "padoms": "{20|60}."},
                {"jaut": "Cik preču nav atlaidē otrajā plauktā?",
                 "atb": ["40"], "padoms": "60 - 20."},
            ]),
            pavediens="veikals",
            konteksts="Veikala plauktā skaitļi ir doti, bet daļa jāsaskata "
                      "pašam.",
            kapec="Uzzīmēta josla parāda gan daļu, gan atlikumu vienlaikus."),

    Kopsavilkums([
        "Uzzīmēju joslu, kurā visa josla ir veselais.",
        "Sadalu joslu tik daļās, cik rāda saucējs.",
        "Pierakstu pie shēmas gan daļu, gan skaitļus.",
        "Nolasu no shēmas gan daļas vērtību, gan atlikumu.",
    ]),

    Majas([
        "Uzzīmē shēmu uzdevumam: no 24 skolēniem 18 brauc ekskursijā.",
        "Nolasi no savas shēmas, cik skolēnu nebrauc.",
        "Uzraksti, ar ko shēma palīdzēja.",
    ]),
]
