# -*- coding: utf-8 -*-
"""5. klase, 123. stunda: «Kā raksturot cita uzzīmēto figūru?»

Stunda pāriem. Raksturot svešu figūru ir grūtāk nekā savu: nevar atsaukties
uz to, ko biji domājis, jāizmanto tikai tas, ko var izmērīt un saskaitīt.
Tāpēc stundas rezultāts ir saraksts ar pazīmēm, kas der jebkurai figūrai -
malu skaits, leņķu veidi, vienādas malas, izliektība.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         figura)

TEMA = "Kā raksturot cita uzzīmēto figūru?"

MERKIS = ("Mācīsimies pārī raksturot klasesbiedra uzzīmēta daudzstūra "
          "īpašības.")

SATURS = [
    Sakums("Kā aprakstīt figūru, ko nezīmēji pats?",
           zimejums=figura([(0, 0), (6, 0), (6, 2), (2, 2), (2, 5), (0, 5)],
                           virsraksts="Sešstūris rūtiņu lapā"),
           paraksts="Sešas malas, seši leņķi, viens no tiem atvērts.",
           fakti=["Par figūru var pateikt tikai to, ko redz vai izmēra.",
                  "Pazīmes ir vienmēr tās pašas.",
                  "Tāpēc apraksts sākas ar sarakstu, nevis ar sajūtu."]),

    Doma("Vienmēr tās pašas pazīmes",
         "Daudzstūri raksturo pēc malu skaita, malu garumiem, leņķu veidiem, "
         "vienādām malām un tā, vai figūra ir izliekta vai ieliekta.",
         soli=[
             "Saskaiti malas un virsotnes.",
             "Izmēri malas un atrodi vienādās.",
             "Nosaki leņķu veidus: šauri, taisni, plati, atvērti.",
             "Pārbaudi, vai figūra ir izliekta.",
             "Pieraksti secinājumu pilnos teikumos.",
         ],
         pieze="Apraksts ir labs tad, ja pēc tā otrs cilvēks var uzzīmēt ļoti "
               "līdzīgu figūru. Tas arī ir veids, kā pārbaudīt savu darbu."),

    Petijums("Apmainieties ar zīmējumiem",
             soli=["Uzzīmē rūtiņu lapā daudzstūri ar 5 vai 6 malām.",
                   "Apmainies zīmējumiem ar solabiedru.",
                   "Saskaiti saņemtās figūras malas, virsotnes un leņķus.",
                   "Pieraksti piecas pazīmes pilnos teikumos.",
                   "Salīdziniet aprakstus: vai abi pamanīja vienu un to "
                   "pašu?"],
             vajag="rūtiņu lapa, lineāls, zīmulis",
             secinajums="Divi cilvēki vienu figūru apraksta ar vieniem un "
                        "tiem pašiem vārdiem, ja lieto pazīmju sarakstu."),

    Paraugs("Sešstūra apraksts",
            uzd="Raksturo figūru ar sešām malām, kurai viens leņķis ir "
                "atvērts.",
            soli=[
                ("Tas ir sešstūris",
                 "Sešas malas un sešas virsotnes."),
                ("Četri leņķi ir taisni",
                 "Malas iet pa rūtiņu līnijām."),
                ("Viens leņķis ir atvērts",
                 "Lielāks par 180°."),
                ("Figūra ir ieliekta",
                 "Tāpēc, ka ir atvērts leņķis."),
                ("Divas malas ir vienāda garuma",
                 "Pēdējā pazīme."),
            ],
            atbilde="Ieliekts sešstūris ar četriem taisniem leņķiem"),

    Ievadi("Saskaiti pazīmes", [
        {"jaut": "Cik malu ir sešstūrim?",
         "atb": ["6"], "padoms": "Nosaukums to pasaka."},
        {"jaut": "Cik virsotņu ir sešstūrim?",
         "atb": ["6"], "padoms": "Tikpat, cik malu."},
        {"jaut": "Cik leņķu ir piecstūrim?",
         "atb": ["5"], "padoms": "Tikpat, cik virsotņu."},
        {"jaut": "Figūrai ir viens atvērts leņķis. Vai tā ir ieliekta? "
                 "Raksti «jā» vai «nē».",
         "atb": ["jā", "ja"], "padoms": "Atvērts leņķis padara ieliektu."},
        {"jaut": "Figūrai visi leņķi ir taisni un malu ir 4. Kā to sauc?",
         "atb": ["taisnstūris"], "padoms": "Četri taisni leņķi."},
        {"jaut": "Taisnstūrim ar vienādām malām ir savs nosaukums. Kāds?",
         "atb": ["kvadrāts", "kvadrats"], "padoms": "Visas četras malas "
                                                    "vienādas."},
        {"jaut": "Cik taisnu leņķu ir kvadrātam?",
         "atb": ["4"], "padoms": "Visi leņķi taisni."},
        {"jaut": "Figūras malas ir 3, 4, 5 un 6 rūtiņas. Cik rūtiņu ir "
                 "perimetrs?",
         "atb": ["18"], "padoms": "3 + 4 + 5 + 6."},
    ], pamats=4,
        ievads="Vispirms saskaiti, tikai tad apraksti."),

    Zimejums("Viena figūra, piecas pazīmes",
             figura([(0, 0), (5, 0), (5, 4), (2, 4), (2, 2), (0, 2)],
                    virsraksts="Sešstūris ar taisniem leņķiem"),
             paskaidro="Sešas malas, seši leņķi, pieci no tiem taisni, viens "
                       "atvērts; divas malas ir 2 rūtiņas garas.",
             ievads="Tādu figūru var aprakstīt ar piecām pazīmēm."),

    Varianti("Ko var pateikt par figūru?", [
        {"jaut": "Ar ko sāk figūras aprakstu?",
         "opcijas": ["Ar malu un virsotņu skaitu", "Ar krāsu",
                     "Ar laukumu", "Ar sajūtu"],
         "pareizi": 0,
         "padoms": "Vispirms saskaita."},
        {"jaut": "Kura pazīme nav matemātiska?",
         "opcijas": ["Figūra ir skaista", "Malu skaits",
                     "Leņķu veidi", "Vienādas malas"],
         "pareizi": 0,
         "padoms": "To nevar izmērīt."},
        {"jaut": "Kā pārbaudīt, vai apraksts ir labs?",
         "opcijas": ["Pēc tā uzzīmēt figūru no jauna",
                     "Saskaitīt vārdus",
                     "Salīdzināt krāsas",
                     "Pārbaudīt nevar"],
         "pareizi": 0,
         "padoms": "Apraksts aizstāj zīmējumu."},
        {"jaut": "Figūrai ir 5 malas. Cik tai ir virsotņu?",
         "opcijas": ["5", "4", "6", "10"],
         "pareizi": 0,
         "padoms": "Tikpat, cik malu."},
        {"jaut": "Kas padara figūru ieliektu?",
         "opcijas": ["Atvērts iekšējais leņķis", "Gara mala",
                     "Daudz malu", "Vienādas malas"],
         "pareizi": 0,
         "padoms": "Vairāk par 180°."},
        {"jaut": "Cik pazīmes pietiek labam aprakstam?",
         "opcijas": ["Apmēram piecas", "Viena", "Divdesmit", "Nevienas"],
         "pareizi": 0,
         "padoms": "Tik, lai figūru varētu atjaunot."},
    ], pamats=4),

    Pasaule("Apraksti klases plānu",
            Ievadi("", [
                {"jaut": "Klases telpa ir taisnstūris 8 m x 6 m. Cik metru ir "
                         "perimetrs?",
                 "atb": ["28"], "padoms": "(8 + 6) · 2."},
                {"jaut": "Cik kvadrātmetru ir tās laukums?",
                 "atb": ["48"], "padoms": "8 · 6."},
                {"jaut": "Citai telpai malas ir 5 m, 4 m, 5 m un 4 m. Cik "
                         "metru ir perimetrs?",
                 "atb": ["18"], "padoms": "5 + 4 + 5 + 4."},
                {"jaut": "Cik taisnu leņķu ir taisnstūrveida telpai?",
                 "atb": ["4"], "padoms": "Visi stūri taisni."},
            ]),
            pavediens="skola",
            konteksts="Skolas plānā katra telpa ir daudzstūris, un to "
                      "apraksta ar tām pašām pazīmēm.",
            kapec="Pēc laba apraksta telpu var atrast, to neredzot."),

    Kopsavilkums([
        "Raksturoju svešu daudzstūri pēc malu un virsotņu skaita.",
        "Nosaku leņķu veidus un vienādās malas.",
        "Pārbaudu, vai figūra ir izliekta vai ieliekta.",
        "Pierakstu aprakstu pilnos teikumos.",
    ]),

    Majas([
        "Uzzīmē daudzstūri un uzraksti par to piecas pazīmes.",
        "Iedod aprakstu mājiniekam un palūdz uzzīmēt figūru no jauna.",
        "Salīdzini abus zīmējumus.",
    ]),
]
