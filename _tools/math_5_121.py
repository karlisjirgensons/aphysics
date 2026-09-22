# -*- coding: utf-8 -*-
"""5. klase, 121. stunda: «Vai diagonāles vienmēr krustojas?»

Pētnieciska stunda. Atbilde skolēniem šķiet acīmredzama - protams, ka
krustojas -, līdz parādās ieliekts četrstūris, kurā viena diagonāle iziet
ārpus figūras. Tāpēc stundas vērtība ir nevis atbildē, bet atklājumā, ka
«vienmēr» ir apgalvojums, kas jāpārbauda.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         figura)

TEMA = "Vai diagonāles vienmēr krustojas?"

MERKIS = ("Pētīsim, vai nogriežņi, kas savieno četrstūra pretējās virsotnes, "
          "vienmēr krustojas.")

SATURS = [
    Sakums("Divas diagonāles četrstūrī",
           zimejums=figura([(0, 0), (5, 0), (5, 3), (0, 3)],
                           virsraksts="Parasts taisnstūris"),
           paraksts="Šeit abas diagonāles krustojas figūras iekšpusē.",
           fakti=["Diagonāle savieno divas pretējās virsotnes.",
                  "Četrstūrim ir tieši divas diagonāles.",
                  "Bet vai tās krustojas vienmēr?"]),

    Doma("Pārbauda ar zīmējumu, nevis ar sajūtu",
         "Četrstūra diagonāles krustojas figūras iekšpusē tad, ja četrstūris "
         "ir izliekts; ieliektā četrstūrī viena diagonāle iziet ārpus "
         "figūras.",
         soli=[
             "Uzzīmē četrstūri un atzīmē virsotnes.",
             "Savieno pirmo virsotni ar trešo.",
             "Savieno otro virsotni ar ceturto.",
             "Paskaties, kur nogriežņi krustojas.",
             "Pamēģini uzzīmēt četrstūri, kurā tā nenotiek.",
         ],
         pieze="Izliektā figūrā jebkurš nogrieznis starp diviem tās punktiem "
               "paliek figūras iekšpusē. Ieliektā tā vairs nav - un tieši "
               "tas izšķir, kur nonāk diagonāle."),

    Petijums("Pārbaudi četras figūras",
             soli=["Uzzīmē kvadrātu un novelc abas diagonāles.",
                   "Uzzīmē garenu taisnstūri un novelc diagonāles.",
                   "Uzzīmē četrstūri, kuram viens stūris iespiests uz iekšu.",
                   "Novelc arī tam abas diagonāles.",
                   "Pieraksti, kurās figūrās diagonāles krustojas iekšpusē."],
             vajag="rūtiņu lapa, lineāls, zīmulis",
             secinajums="Pirmajās trijās figūrās diagonāles krustojas "
                        "iekšpusē, ieliektajā - viena iziet ārā."),

    Paraugs("Ieliekts četrstūris",
            uzd="Uzzīmē četrstūri ABCD, kuram virsotne C ir iespiesta uz "
                "iekšu. Kur nonāk diagonāles?",
            soli=[
                ("Virsotnes: A, B, C un D",
                 "C ir iespiesta uz iekšu."),
                ("Diagonāle AC paliek iekšpusē",
                 "Tā iet uz iespiesto virsotni."),
                ("Diagonāle BD iziet ārpus figūras",
                 "Tā šķērso ieliekto vietu."),
                ("Krustpunkts ir ārpus četrstūra",
                 "Apgalvojums «vienmēr» ir nepatiess."),
            ],
            atbilde="Ieliektā četrstūrī diagonāles krustojas ārpus figūras"),

    Ievadi("Diagonāles un virsotnes", [
        {"jaut": "Cik diagonāļu ir četrstūrim?",
         "atb": ["2"], "padoms": "Divi pretējo virsotņu pāri."},
        {"jaut": "Cik virsotņu savieno viena diagonāle?",
         "atb": ["2"], "padoms": "Tas ir nogrieznis."},
        {"jaut": "Cik diagonāļu ir piecstūrim?",
         "atb": ["5"], "padoms": "No katras virsotnes divas."},
        {"jaut": "Cik diagonāļu ir trijstūrim?",
         "atb": ["0"], "padoms": "Pretējo virsotņu nav."},
        {"jaut": "Taisnstūra diagonāles krustojas iekšpusē. Raksti «jā» vai "
                 "«nē».",
         "atb": ["jā", "ja"], "padoms": "Taisnstūris ir izliekts."},
        {"jaut": "Ieliekta četrstūra abas diagonāles ir iekšpusē?",
         "atb": ["nē", "ne"], "padoms": "Viena iziet ārā."},
        {"jaut": "Cik virsotņu ir četrstūrim?",
         "atb": ["4"], "padoms": "Tikpat, cik malu."},
        {"jaut": "Kvadrāta diagonāles ir vienāda garuma. Raksti «jā» vai "
                 "«nē».",
         "atb": ["jā", "ja"], "padoms": "Visas malas vienādas."},
    ], pamats=4,
        ievads="Vispirms saskaiti virsotnes, tad diagonāles."),

    Zimejums("Ieliekts četrstūris",
             figura([(0, 0), (6, 0), (3, 2), (6, 5)],
                    virsraksts="Viena virsotne iespiesta uz iekšu"),
             paskaidro="Šādā figūrā nogrieznis starp divām virsotnēm var "
                       "iziet ārpus figūras - tieši tāpēc diagonāles vairs "
                       "nekrustojas iekšpusē.",
             ievads="Tā izskatās ieliekts četrstūris."),

    Varianti("Kad diagonāles krustojas?", [
        {"jaut": "Kādā četrstūrī diagonāles krustojas iekšpusē?",
         "opcijas": ["Izliektā", "Ieliektā", "Jebkurā", "Nevienā"],
         "pareizi": 0,
         "padoms": "Izliektā nogriežņi paliek iekšpusē."},
        {"jaut": "Cik diagonāļu ir četrstūrim?",
         "opcijas": ["2", "4", "1", "6"],
         "pareizi": 0,
         "padoms": "Divi pretējo virsotņu pāri."},
        {"jaut": "Vai apgalvojums «diagonāles vienmēr krustojas» ir patiess?",
         "opcijas": ["Nav, ieliektā četrstūrī ne", "Ir",
                     "Ir tikai kvadrātam", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Pietiek ar vienu pretpiemēru."},
        {"jaut": "Kas ir izliekta figūra?",
         "opcijas": ["Katrs nogrieznis starp tās punktiem paliek iekšpusē",
                     "Figūra ar taisniem leņķiem",
                     "Figūra ar vienādām malām",
                     "Figūra bez diagonālēm"],
         "pareizi": 0,
         "padoms": "Tā ir izliektības definīcija."},
        {"jaut": "Cik diagonāļu ir trijstūrim?",
         "opcijas": ["Nevienas", "Viena", "Trīs", "Divas"],
         "pareizi": 0,
         "padoms": "Nav pretējo virsotņu."},
        {"jaut": "Kā pārbauda šādu apgalvojumu?",
         "opcijas": ["Zīmējot dažādas figūras", "Mērot malas",
                     "Skaitot leņķus", "Pārbaudīt nevar"],
         "pareizi": 0,
         "padoms": "Meklē pretpiemēru."},
    ], pamats=4),

    Pasaule("Kā nostiept virves pāri laukumam?",
            Ievadi("", [
                {"jaut": "Taisnstūra laukuma stūros iesistas 4 mietiņas. Cik "
                         "virvju vajag, lai savienotu pretējos stūrus?",
                 "atb": ["2"], "padoms": "Divas diagonāles."},
                {"jaut": "Cik reižu šīs virves krustojas?",
                 "atb": ["1"], "padoms": "Vienā punktā."},
                {"jaut": "Laukumam ir 5 stūri. Cik virvju vajag, lai "
                         "savienotu visus stūrus, kas nav blakus?",
                 "atb": ["5"], "padoms": "Piecstūrim ir 5 diagonāles."},
                {"jaut": "Cik virvju vajag laukumam ar 3 stūriem?",
                 "atb": ["0"], "padoms": "Trijstūrim diagonāļu nav."},
            ]),
            pavediens="skola",
            konteksts="Skolas sporta laukumā virves stiepj no stūra uz "
                      "stūri, un krustpunktā liek atzīmi.",
            kapec="Krustpunkts ir tikai tad, ja laukums ir izliekts."),

    Kopsavilkums([
        "Zīmēju četrstūra diagonāles.",
        "Pārbaudu, vai tās krustojas figūras iekšpusē.",
        "Atrodu pretpiemēru apgalvojumam ar vārdu «vienmēr».",
        "Atšķiru izliektu figūru no ieliektas.",
    ]),

    Majas([
        "Uzzīmē trīs dažādus četrstūrus un novelc visām diagonāles.",
        "Atrodi vienu, kurā diagonāles nekrustojas iekšpusē.",
        "Saskaiti, cik diagonāļu ir sešstūrim.",
    ]),
]
