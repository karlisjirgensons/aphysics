# -*- coding: utf-8 -*-
"""3. klase, 80. stunda: «Cik dažādi var sadalīt taisnstūri?»

Mikrotemata noslēgums. Viens un tas pats taisnstūris sadalās daļās daudzos
veidos, un daļas forma var būt pavisam cita - svarīgs ir tikai laukums. Tas
ir tas pats atklājums, kas 20. stundā, tikai tagad ar daļu vārdiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Cik dažādi var sadalīt taisnstūri?"

MERKIS = ("Dalīsim vienādu taisnstūri vienādās daļās dažādos veidos un "
          "salīdzināsim rezultātus.")

SATURS = [
    Sakums("Vai ceturtdaļai vienmēr jāizskatās vienādi?",
           zimejums=restis([["A", "A", "B", "B"],
                            ["C", "C", "D", "D"]],
                           "kvadrāts četrās ceturtdaļās"),
           paraksts="Katrā burtā ir 2 rūtiņas no 8 - tātad katra ir "
                    "ceturtdaļa.",
           fakti=["Ceturtdaļa nozīmē vienādu laukumu, ne vienādu formu.",
                  "Vienu taisnstūri ceturtdaļās var sadalīt daudzos veidos."]),

    Doma("Daļu nosaka laukums, nevis forma",
         "Ja divās daļās ir vienāds rūtiņu skaits, tās ir vienādas daļas - lai "
         "kā tās izskatītos.",
         soli=[
             "Saskaiti visas rūtiņas taisnstūrī.",
             "Izdali tās ar daļu skaitu.",
             "Atdali katrai daļai tik rūtiņu.",
             "Pārbaudi: vai neviena rūtiņa nav palikusi pāri?",
         ],
         pieze="Tāpēc «L» formas gabals var būt tieši tāda pati ceturtdaļa kā "
               "taisna josla - abās ir vienāds rūtiņu skaits."),

    Paraugs("Cik rūtiņu ir vienā ceturtdaļā?",
            uzd="Taisnstūrī ir 8 rūtiņas. Cik rūtiņu ir vienā ceturtdaļā?",
            soli=[
                ("8 rūtiņas pavisam",
                 "Vispirms saskaita visu taisnstūri."),
                ("8 : 4 = 2",
                 "Vienā ceturtdaļā ir divas rūtiņas."),
                ("4 · 2 = 8",
                 "Pārbaude: četras ceturtdaļas dod visu taisnstūri."),
            ],
            atbilde="2 rūtiņas"),

    Petijums("Sadali kvadrātu ceturtdaļās trijos veidos",
             vajag="trīs rūtiņu kvadrāti 4 x 4 un krāsainie zīmuļi",
             soli=[
                 "Pirmo kvadrātu sadali četrās vertikālās joslās.",
                 "Otro sadali četros mazos kvadrātos.",
                 "Trešo sadali četrās «L» formas daļās.",
                 "Saskaiti rūtiņas katrā daļā un salīdzini.",
             ],
             secinajums="Visos trijos veidos katrā daļā ir 4 rūtiņas - tātad "
                        "visas ir ceturtdaļas."),

    Ievadi("Cik rūtiņu ir daļā?", [
        {"jaut": "Taisnstūrī 16 rūtiņas. Cik rūtiņu ir {1|4}?",
         "atb": ["4"], "padoms": "16 : 4."},
        {"jaut": "Taisnstūrī 16 rūtiņas. Cik rūtiņu ir {1|2}?",
         "atb": ["8"], "padoms": "16 : 2."},
        {"jaut": "Taisnstūrī 24 rūtiņas. Cik rūtiņu ir {1|3}?",
         "atb": ["8"], "padoms": "24 : 3."},
        {"jaut": "Taisnstūrī 24 rūtiņas. Cik rūtiņu ir {3|4}?",
         "atb": ["18"], "padoms": "24 : 4 = 6; 3 · 6."},
        {"jaut": "Taisnstūrī 20 rūtiņas. Cik rūtiņu ir {2|5}?",
         "atb": ["8"], "padoms": "20 : 5 = 4; 2 · 4."},
        {"jaut": "Taisnstūrī 18 rūtiņas. Cik rūtiņu ir {1|6}?",
         "atb": ["3"], "padoms": "18 : 6."},
    ], pamats=4),

    Zimejums("Trīs ceturtdaļas, viena forma katrai",
             restis([["A", "B", "C", "D"],
                     ["A", "B", "C", "D"],
                     ["A", "B", "C", "D"],
                     ["A", "B", "C", "D"]],
                    "cits sadalījums ceturtdaļās"),
             paskaidro="Arī te katrā burtā ir 4 rūtiņas no 16 - tātad katra "
                       "ir ceturtdaļa.",
             ievads="Salīdzini ar stundas sākuma zīmējumu."),

    Varianti("Vai tā ir daļa?", [
        {"jaut": "Divās daļās ir 6 un 6 rūtiņas, bet formas atšķiras. Vai "
                 "tās ir vienādas daļas?",
         "opcijas": ["Jā, laukums ir vienāds", "Nē, formas atšķiras",
                     "Tikai ja tās ir taisnstūri", "To nevar pateikt"],
         "pareizi": 0, "padoms": "Daļu nosaka laukums."},
        {"jaut": "Taisnstūrī 20 rūtiņas. Vai to var sadalīt 3 vienādās "
                 "daļās?",
         "opcijas": ["Nē, 20 nedalās ar 3", "Jā, katrā 6",
                     "Jā, katrā 7", "Jā, katrā 6 un viena pāri"],
         "pareizi": 0, "padoms": "20 : 3 nav vesels skaitlis."},
        {"jaut": "Cik rūtiņu ir {1|8} no 32 rūtiņām?",
         "opcijas": ["4", "8", "6", "3"],
         "pareizi": 0, "padoms": "32 : 8."},
        {"jaut": "Kas nemainās, mainot daļas formu?",
         "opcijas": ["Rūtiņu skaits", "Malu skaits", "Krāsa", "Nekas"],
         "pareizi": 0, "padoms": "Daļu nosaka laukums."},
    ], pamats=4),

    Pasaule("Kā sadalīt cepumu plāksni?",
            Ievadi("", [
                {"jaut": "Plāksnē 24 rūtiņas. Cik rūtiņu ir {1|4}?",
                 "atb": ["6"], "padoms": "24 : 4."},
                {"jaut": "Cik rūtiņu ir {1|6}?", "atb": ["4"],
                 "padoms": "24 : 6."},
                {"jaut": "Cik rūtiņu ir {2|3}?", "atb": ["16"],
                 "padoms": "24 : 3 = 8; 2 · 8."},
                {"jaut": "Cik rūtiņu paliks, ja apēd {3|4}?",
                 "atb": ["6"], "padoms": "24 − 18."},
            ]),
            pavediens="virtuve",
            konteksts="Cepumu plāksni var sagriezt joslās vai kvadrātos - "
                      "svarīgi tikai, lai rūtiņu skaits katrā būtu vienāds.",
            kapec="Tieši tāpēc dalīšana ar aci nestrādā, bet skaitīšana - jā."),

    Kopsavilkums([
        "Sadalu taisnstūri vienādās daļās dažādos veidos.",
        "Zinu, ka daļu nosaka laukums, ne forma.",
        "Aprēķinu, cik rūtiņu ir dotajā daļā.",
        "Pārbaudu, vai neviena rūtiņa nav palikusi pāri.",
    ]),

    Majas([
        "Uzzīmē 4 x 4 kvadrātu un sadali to ceturtdaļās trijos veidos.",
        "Pārbaudi, vai katrā daļā ir vienāds rūtiņu skaits.",
        "Atrodi sadalījumu, kurā daļas nav taisnstūri.",
    ]),
]
