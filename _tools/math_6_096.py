# -*- coding: utf-8 -*-
"""6. klase, 96. stunda: «Kāds uzdevums sanāk tev?»

Temata pēdējā mācību stunda. Uzdevumu izdomāt ir grūtāk nekā atrisināt: tajā
jābūt pietiekami daudz datu, bet ne pārāk daudz, un atbildei jābūt
iespējamai. Tieši tāpēc šī stunda ir laba sagatavošanās pārbaudes darbam.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti)

TEMA = "Kāds uzdevums sanāk tev?"

MERKIS = ("Veidosim savu procentu uzdevumu par sev nozīmīgu situāciju un "
          "risināsim klasesbiedra uzdevumu.")

SATURS = [
    Sakums("Labs uzdevums ir tas, kuru var atrisināt",
           fakti=["Uzdevumā jābūt pietiekami daudz datu, bet ne pārāk daudz.",
                  "Atbildei jābūt iespējamai - veselai un reālai.",
                  "Autoram pašam jāzina atbilde, pirms viņš uzdevumu iedod."]),

    Doma("Vispirms atbilde, tad uzdevums",
         "Savu uzdevumu veido no gala: izvēlas situāciju un atbildi un tikai "
         "tad izdomā tekstu, kas uz to ved.",
         soli=[
             "Izvēlies situāciju no savas dzīves.",
             "Izvēlies skaitļus, ar kuriem atbilde sanāk vesela.",
             "Uzraksti tekstu ar jautājumu beigās.",
             "Atrisini savu uzdevumu un pieraksti atbildi atsevišķi.",
             "Pārbaudi, vai tekstā ir viss vajadzīgais un nekas lieks.",
         ],
         pieze="Ja gribi, lai atbilde sanāk vesela, sāc no kopuma, kas "
               "dalās ar 100 vai vismaz ar 20: tad 5 %, 15 % un 25 % visi "
               "dod veselus skaitļus."),

    Paraugs("Uzraksti uzdevumu no gala",
            uzd="Izdomā uzdevumu par velosipēda cenu, kura atbilde ir 240 €.",
            soli=[
                ("Atbilde būs 240 €",
                 "Sāku no gala."),
                ("Lai būtu 20 % atlaide, sākotnējā cena ir 300 €",
                 "240 ir 80 % no 300."),
                ("Teksts: «Velosipēds maksāja 300 €, atlaide 20 %...»",
                 "Jautājums: cik tas maksā tagad?"),
                ("Pārbaude: 300 · 0,8 = 240",
                 "Atbilde sanāk vesela."),
            ],
            atbilde="uzdevums ar atbildi 240 €"),

    Ievadi("Pārbaudi savu uzdevumu", [
        {"jaut": "Cena 300 €, atlaide 20 %. Cik maksā tagad?",
         "atb": ["240"], "padoms": "80 % no 300."},
        {"jaut": "Cena 300 €, atlaide 15 %. Cik maksā tagad?",
         "atb": ["255"], "padoms": "85 % no 300."},
        {"jaut": "Ar kādu kopumu 15 % vienmēr sanāk vesels skaitlis? "
                 "Ieraksti mazāko divciparu skaitli.",
         "atb": ["20"], "padoms": "15 % no 20 ir 3."},
        {"jaut": "Cena 80 €, atlaide 25 %. Cik maksā tagad?",
         "atb": ["60"], "padoms": "75 % no 80."},
        {"jaut": "Kopums 500, meklē 35 %. Cik tas ir?",
         "atb": ["175"], "padoms": "35 · 5."},
        {"jaut": "Kopums 60, meklē 45 %. Cik tas ir?",
         "atb": ["27"], "padoms": "45 · 0,6."},
    ], pamats=4),

    Petijums("Uzraksti un apmaini uzdevumu",
             vajag="burtnīca, soļabiedrs",
             soli=[
                 "Izvēlies situāciju: kabatas nauda, sports, spēle, pirkums.",
                 "Izdomā atbildi un no tās izveido uzdevumu.",
                 "Atrisini to pats un pieraksti atbildi atsevišķā lapā.",
                 "Apmainieties uzdevumiem un atrisiniet viens otra darbu.",
                 "Salīdziniet atbildes un pārrunājiet, kur bija grūtāk.",
             ],
             secinajums="Ja soļabiedra atbilde sakrīt ar tavējo, uzdevums ir "
                        "uzrakstīts skaidri; ja ne, visbiežāk trūkst viena "
                        "datu."),

    Varianti("Kas uzdevumā nav kārtībā?", [
        {"jaut": "«Prece maksāja 50 €. Cik tā maksā pēc atlaides?» Kas "
                 "trūkst?",
         "opcijas": ["Atlaides lielums", "Sākotnējā cena",
                     "Jautājums", "Nekas netrūkst"],
         "pareizi": 0,
         "padoms": "Bez procentiem rēķināt nevar."},
        {"jaut": "«Klasē 23 skolēni, 30 % sporto.» Kas nav kārtībā?",
         "opcijas": ["Atbilde nesanāk vesela", "Trūkst datu",
                     "Trūkst jautājuma", "Viss kārtībā"],
         "pareizi": 0,
         "padoms": "23 · 0,3 = 6,9."},
        {"jaut": "Kāds kopums der, lai 30 % sanāktu vesels?",
         "opcijas": ["20", "23", "25", "27"],
         "pareizi": 0,
         "padoms": "30 % no 20 ir 6."},
        {"jaut": "Kas uzdevumā ir obligāts?",
         "opcijas": ["Jautājums", "Liekie dati",
                     "Zīmējums", "Vairāki procenti"],
         "pareizi": 0,
         "padoms": "Bez jautājuma nav uzdevuma."},
    ], pamats=4),

    Pasaule("Uzdevums par savu nedēļu",
            Ievadi("", [
                {"jaut": "Nedēļā ir 168 stundas. Cik stundu ir 25 % no tām?",
                 "atb": ["42"], "padoms": "168 : 4."},
                {"jaut": "Miegam atvēl 8 h diennaktī. Cik stundu nedēļā?",
                 "atb": ["56"], "padoms": "8 · 7."},
                {"jaut": "Cik procenti no nedēļas tas ir? Noapaļo līdz "
                         "veselam.",
                 "atb": ["33"], "padoms": "{56|168} = {1|3}."},
                {"jaut": "Skolā pavada 30 h nedēļā. Cik procenti tas ir? "
                         "Noapaļo līdz veselam.",
                 "atb": ["18"], "padoms": "{30|168}."},
            ]),
            pavediens="skola",
            konteksts="Savas nedēļas sadalījums ir uzdevums, kura dati ir "
                      "pie rokas un atbilde ir noderīga.",
            kapec="Uzdevums par sevi ir vieglāk pārbaudāms nekā izdomāts."),

    Kopsavilkums([
        "Veidoju savu procentu uzdevumu no gala.",
        "Izvēlos skaitļus tā, lai atbilde sanāktu vesela.",
        "Pārbaudu, vai tekstā ir viss vajadzīgais.",
        "Risinu klasesbiedra uzdevumu un salīdzinu atbildes.",
    ]),

    Majas([
        "Uzraksti vienu procentu uzdevumu par savu ģimeni.",
        "Atrisini to un pieraksti atbildi atsevišķi.",
        "Iedod to kādam mājās un salīdziniet atbildes.",
    ]),
]
