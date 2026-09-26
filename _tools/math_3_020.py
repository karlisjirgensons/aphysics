# -*- coding: utf-8 -*-
"""3. klase, 20. stunda: «Cik vienādās daļās var sadalīt figūru?»

Dalīšana pārceļas no priekšmetiem uz figūru. Rūtiņās sadalīts taisnstūris ir
tas modelis, kas 3.4. tematā kļūs par daļskaitli: te vēl skaita rūtiņas, bet
jau runā par «vienu daļu no astoņām».
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Cik vienādās daļās var sadalīt figūru?"

MERKIS = ("Sadalīsim rūtiņās sadalītu taisnstūri 2-10 vienādās daļās un "
          "noteiksim vienas daļas lielumu.")

SATURS = [
    Sakums("Kā sadalīt šokolādi, lai nevienam nebūtu mazāk?",
           zimejums=restis([["", "", "", "", "", ""],
                            ["", "", "", "", "", ""],
                            ["", "", "", "", "", ""],
                            ["", "", "", "", "", ""]],
                           "24 rūtiņas"),
           paraksts="24 rūtiņas var sadalīt daudzos vienādos veidos.",
           fakti=["Vienādās daļās nozīmē: katrā daļā vienāds rūtiņu skaits.",
                  "24 var sadalīt 2, 3, 4, 6, 8 un 12 vienādās daļās."]),

    Doma("Sadalīt vienādās daļās var tikai tad, ja skaitlis dalās",
         "Vienas daļas lielums ir rūtiņu skaits, izdalīts ar daļu skaitu.",
         soli=[
             "Saskaiti, cik rūtiņu ir visā figūrā.",
             "Izvēlies, cik vienādās daļās to dalīsi.",
             "Izdali rūtiņu skaitu ar daļu skaitu.",
             "Ja dalījums nav vesels skaitlis, tik daļās sadalīt nevar.",
         ],
         pieze="Daļas forma var būt dažāda - rinda, kvadrāts vai «L» burts. "
               "Svarīgs ir tikai rūtiņu *skaits*."),

    Paraugs("Cik rūtiņu ir vienā daļā?",
            uzd="Taisnstūri ar 24 rūtiņām sadala 6 vienādās daļās. Cik "
                "rūtiņu ir vienā daļā?",
            soli=[
                ("24 rūtiņas kopā",
                 "Vispirms saskaita visas rūtiņas: 4 rindas pa 6."),
                ("24 : 6 = 4",
                 "Kopskaitu izdala ar daļu skaitu."),
                ("4 rūtiņas vienā daļā",
                 "Pārbaude: 6 · 4 = 24 - neviena rūtiņa nepaliek pāri."),
            ],
            atbilde="4 rūtiņas"),

    Ievadi("Cik rūtiņu vienā daļā?", [
        {"jaut": "36 rūtiņas sadala 6 vienādās daļās. Cik rūtiņu ir vienā?",
         "atb": ["6"], "padoms": "36 : 6."},
        {"jaut": "40 rūtiņas sadala 8 vienādās daļās. Cik rūtiņu ir vienā?",
         "atb": ["5"], "padoms": "40 : 8."},
        {"jaut": "42 rūtiņas sadala 7 vienādās daļās. Cik rūtiņu ir vienā?",
         "atb": ["6"], "padoms": "42 : 7."},
        {"jaut": "30 rūtiņas sadala 5 vienādās daļās. Cik rūtiņu ir vienā?",
         "atb": ["6"], "padoms": "30 : 5."},
        {"jaut": "Cik vienādās daļās pa 9 rūtiņām var sadalīt 54 rūtiņas?",
         "atb": ["6"], "padoms": "54 : 9."},
        {"jaut": "Cik rūtiņu ir figūrā, ja tajā ir 8 daļas pa 7 rūtiņām?",
         "atb": ["56"], "padoms": "8 · 7."},
    ], pamats=4),

    Petijums("Sadali savu taisnstūri",
             vajag="rūtiņu lapa, zīmulis un krāsainie zīmuļi",
             soli=[
                 "Uzzīmē taisnstūri 6 rūtiņas platu un 4 augstu.",
                 "Sadali to 4 vienādās daļās un iekrāso katru citā krāsā.",
                 "Uzzīmē otru tādu pašu taisnstūri un sadali to 8 daļās.",
                 "Pieraksti, cik rūtiņu ir vienā daļā abos gadījumos.",
             ],
             secinajums="Jo vairāk daļu, jo mazāka katra daļa - bet kopā "
                        "vienmēr sanāk viss taisnstūris."),

    Zimejums("Vienas daļas lielums sarūk",
             restis([["daļu skaits", 2, 3, 4, 6],
                     ["rūtiņas daļā", 12, 8, 6, 4]],
                    "24 rūtiņas"),
             paskaidro="Reizinājums vienmēr ir 24: 2 · 12, 3 · 8, 4 · 6, "
                       "6 · 4.",
             ievads="Skaties, kā otrā rinda samazinās."),

    Varianti("Vai tā sadalīt var?", [
        {"jaut": "Vai 20 rūtiņas var sadalīt 3 vienādās daļās?",
         "opcijas": ["Nē, 20 nedalās ar 3", "Jā, katrā 6",
                     "Jā, katrā 7", "Jā, katrā 6 un viena pāri"],
         "pareizi": 0, "padoms": "20 : 3 nav vesels skaitlis."},
        {"jaut": "Cik vienādās daļās var sadalīt 18 rūtiņas?",
         "opcijas": ["2, 3, 6 vai 9", "Tikai 2", "Tikai 3 un 6",
                     "Jebkurā skaitā"],
         "pareizi": 0, "padoms": "Meklē visus 18 dalītājus."},
        {"jaut": "35 rūtiņas sadala 5 daļās. Cik rūtiņu ir vienā?",
         "opcijas": ["7", "6", "8", "5"],
         "pareizi": 0, "padoms": "35 : 5."},
        {"jaut": "Kas nemainās, mainot daļas formu?",
         "opcijas": ["Rūtiņu skaits", "Krāsa", "Malu skaits", "Nekas"],
         "pareizi": 0, "padoms": "Vienāda daļa nozīmē vienādu skaitu."},
    ], pamats=4),

    Pasaule("Kā sagriezt cepumu plāksni?",
            Ievadi("", [
                {"jaut": "Cepumu plāksnē ir 48 rūtiņas. To dala 8 bērniem. "
                         "Cik rūtiņu saņem katrs?",
                 "atb": ["6"], "padoms": "48 : 8."},
                {"jaut": "Cik rūtiņu saņemtu katrs, ja bērnu būtu 6?",
                 "atb": ["8"], "padoms": "48 : 6."},
                {"jaut": "Otrā plāksne ir 7 rūtiņas plata un 6 augsta. Cik "
                         "rūtiņu tajā ir?",
                 "atb": ["42"], "padoms": "7 · 6."},
                {"jaut": "Cik bērniem pietiks otrās plāksnes, ja katrs saņem "
                         "7 rūtiņas?",
                 "atb": ["6"], "padoms": "42 : 7."},
            ]),
            pavediens="virtuve",
            konteksts="Cepumu un šokolādes plāksnes vienmēr ir sadalītas "
                      "rūtiņās - tāpēc tās var dalīt taisnīgi.",
            kapec="Rūtiņas ļauj pārbaudīt, vai visiem tiešām sanāca "
                  "vienādi."),

    Kopsavilkums([
        "Sadalu rūtiņās sadalītu figūru 2-10 vienādās daļās.",
        "Nosaku vienas daļas lielumu ar dalīšanu.",
        "Zinu, ka daļas forma var būt dažāda, bet skaits - viens.",
        "Pārbaudu, vai neviena rūtiņa nav palikusi pāri.",
    ]),

    Majas([
        "Uzzīmē 6 x 6 rūtiņu kvadrātu un sadali to 4 vienādās daļās.",
        "Atrodi to pašu sadalījumu citā formā.",
        "Pamēģini sadalīt 25 rūtiņas 4 vienādās daļās un paskaidro, kāpēc "
        "neizdodas.",
    ]),
]
