# -*- coding: utf-8 -*-
"""6. klase, 9. stunda: «Kā sadalīt figūru?»

Attiecība pārceļas no garuma uz laukumu. Rūtiņa ir ērtākā daļa, kāda vien
var būt: to var saskaitīt, un sadalījumu var pārbaudīt ar aci. Tieši tāpēc
šī stunda ir starp nogriezni un «īsto» sadzīves uzdevumu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kā sadalīt figūru?"

MERKIS = ("Mācīsimies rūtiņu lapā sadalīt figūru daļās, ja dota to laukumu "
          "attiecība.")

SATURS = [
    Sakums("Kā sadalīt dārzu, nemērot ne metru?",
           zimejums=restis([["A", "A", "B", "B", "B", "B"],
                            ["A", "A", "B", "B", "B", "B"]],
                           "12 rūtiņas, attiecība 1 : 2"),
           paraksts="A aizņem 4 rūtiņas, B - 8. Attiecība 4 : 8 = 1 : 2.",
           fakti=["Dārznieks neskaita metrus - viņš skaita vienādas dobes.",
                  "Ja rūtiņas ir vienādas, laukumu attiecība ir rūtiņu "
                  "attiecība."]),

    Doma("Skaiti rūtiņas, nevis metrus",
         "Vienādu rūtiņu skaits ir laukums - tāpēc figūru sadalīt attiecībā "
         "nozīmē sadalīt rūtiņas.",
         soli=[
             "Saskaiti, cik rūtiņu ir visā figūrā.",
             "Saskaiti attiecības skaitļus - cik daļu ir kopā.",
             "Izdali rūtiņu skaitu ar daļu skaitu - tā ir viena daļa.",
             "Katrai daļai atdali tik rūtiņu, cik pasaka tās skaitlis.",
             "Pārbaudi, vai neviena rūtiņa nav palikusi pāri.",
         ],
         pieze="Sadalījums nav viens vienīgais: 4 rūtiņas var būt rinda, "
               "kvadrāts vai «L» burts. Svarīgs ir *skaits*, ne forma."),

    Paraugs("Sadali 12 rūtiņas attiecībā 1 : 2",
            uzd="Taisnstūris ir 6 rūtiņas plats un 2 augsts. Sadali to "
                "attiecībā 1 : 2.",
            soli=[
                ("6 · 2 = 12 rūtiņas",
                 "Vispirms - cik rūtiņu ir pavisam."),
                ("1 + 2 = 3 daļas",
                 "Attiecība pasaka, cik vienādu daļu vajag."),
                ("12 : 3 = 4 rūtiņas",
                 "Tik liela ir viena daļa."),
                ("A: 1 · 4 = 4; B: 2 · 4 = 8",
                 "Katrai daļai reizina vienu daļu ar tās skaitli."),
                ("4 + 8 = 12",
                 "Pārbaude: rūtiņas ir sadalītas visas."),
            ],
            atbilde="viena daļa 4 rūtiņas, otra 8 rūtiņas"),

    Ievadi("Cik rūtiņu katrai daļai?", [
        {"jaut": "Figūrā 20 rūtiņu, attiecība 1 : 3. Cik rūtiņu ir mazākajai "
                 "daļai?",
         "atb": ["5"], "padoms": "4 daļas; 20 : 4."},
        {"jaut": "Tā pati figūra. Cik rūtiņu ir lielākajai daļai?",
         "atb": ["15"], "padoms": "3 · 5."},
        {"jaut": "Taisnstūris 5 x 6 rūtiņas. Cik rūtiņu tajā ir?",
         "atb": ["30"], "padoms": "5 · 6.",
         "zim": restis([[""] * 6] * 5, "5 rindas pa 6 rūtiņām")},
        {"jaut": "To pašu figūru dala 2 : 3. Cik rūtiņu ir pirmajai daļai?",
         "atb": ["12"], "padoms": "5 daļas; 30 : 5 = 6; 2 · 6."},
        {"jaut": "Figūrā 24 rūtiņas, attiecība 1 : 2 : 3. Cik rūtiņu ir "
                 "vidējai daļai?",
         "atb": ["8"], "padoms": "6 daļas; viena daļa 4 rūtiņas; 2 · 4."},
        {"jaut": "Figūrā 18 rūtiņas, attiecība 1 : 1 : 1. Cik rūtiņu katrai?",
         "atb": ["6"], "padoms": "18 : 3."},
    ], pamats=4),

    Zimejums("Viena un tā pati attiecība - divi sadalījumi",
             restis([["A", "B", "B", "A", "B", "B"],
                     ["A", "B", "B", "A", "B", "B"]],
                    "arī šis ir 1 : 2"),
             paskaidro="A atkal ir 4 rūtiņas, B - 8. Forma cita, attiecība "
                       "tā pati.",
             ievads="Pārbaudi pats: saskaiti A un B rūtiņas."),

    Varianti("Vai sadalījums der?", [
        {"jaut": "Figūrā 10 rūtiņu. Vai to var sadalīt attiecībā 1 : 3?",
         "opcijas": ["Nē, 10 nedalās ar 4", "Jā, katrai pa 2 un 8",
                     "Jā, katrai pa 1 un 3", "Nē, jo rūtiņu ir par maz"],
         "pareizi": 0,
         "padoms": "Viena daļa būtu 2,5 rūtiņas - rūtiņas nedala."},
        {"jaut": "Divas daļas sanāca 6 un 9 rūtiņas. Kāda ir attiecība?",
         "opcijas": ["2 : 3", "6 : 9 nav attiecība", "3 : 2", "1 : 2"],
         "pareizi": 0,
         "padoms": "Abus dala ar 3."},
        {"jaut": "Kas ir svarīgākais, sadalot figūru attiecībā?",
         "opcijas": ["Rūtiņu skaits katrā daļā", "Daļu forma",
                     "Krāsa", "Kur sākas zīmējums"],
         "pareizi": 0,
         "padoms": "Laukumu nosaka skaits, ne izskats."},
        {"jaut": "Kvadrāts 4 x 4 jāsadala 1 : 3. Cik rūtiņu ir mazākajā "
                 "daļā?",
         "opcijas": ["4", "3", "1", "12"],
         "pareizi": 0,
         "padoms": "16 rūtiņas, 4 daļas."},
    ], pamats=4),

    Pasaule("Kā iekārtot skolas dārzu?",
            Ievadi("", [
                {"jaut": "Dārzā 36 rūtiņas. Dobes un celiņi ir 5 : 1. Cik "
                         "rūtiņu ir celiņiem?",
                 "atb": ["6"], "padoms": "6 daļas; 36 : 6."},
                {"jaut": "Cik rūtiņu paliek dobēm?",
                 "atb": ["30"], "padoms": "36 − 6 vai 5 · 6."},
                {"jaut": "Dobes dala trim klasēm attiecībā 1 : 2 : 2. Cik "
                         "rūtiņu ir pirmajai klasei?",
                 "atb": ["6"], "padoms": "5 daļas; 30 : 5."},
                {"jaut": "Viena rūtiņa dabā ir 1 m². Cik kvadrātmetru ir "
                         "vienas klases lielākā dobe?",
                 "atb": ["12"], "padoms": "2 · 6 rūtiņas, katra 1 m²."},
            ]),
            pavediens="skola",
            konteksts="Skolas dārzā vispirms uzzīmē plānu rūtiņās un tikai "
                      "tad iet ārā ar lāpstu.",
            kapec="Rūtiņa ir mērvienība: uz papīra tā ir rūtiņa, dabā - "
                  "kvadrātmetrs."),

    Petijums("Sadali savu rūtiņu lapu",
             vajag="rūtiņu lapa un zīmulis",
             soli=[
                 "Uzzīmē taisnstūri 6 rūtiņas platu un 4 augstu.",
                 "Saskaiti, cik rūtiņu tajā ir.",
                 "Sadali to attiecībā 1 : 1 : 2 un iekrāso trīs daļas.",
                 "Pārbaudi, vai iekrāsoto rūtiņu skaits sakrīt ar aprēķinu.",
             ],
             secinajums="Ja rūtiņas saskaitītas pareizi, sadalījumu var "
                        "pārbaudīt bez lineāla."),

    Kopsavilkums([
        "Nosaku figūras laukumu, saskaitot vienādas rūtiņas.",
        "Sadalu rūtiņas dotā attiecībā, izmantojot vienu daļu.",
        "Zinu, ka daļas forma var būt dažāda, bet skaits - tikai viens.",
        "Pārbaudu, vai visas rūtiņas ir sadalītas.",
    ]),

    Majas([
        "Uzzīmē 4 x 5 rūtiņu taisnstūri un sadali to attiecībā 1 : 4.",
        "Izdomā figūru, ko attiecībā 1 : 2 sadalīt nevar, un paskaidro, "
        "kāpēc.",
        "Uzzīmē divus dažādus sadalījumus vienai un tai pašai attiecībai.",
    ]),
]
