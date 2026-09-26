# -*- coding: utf-8 -*-
"""3. klase, 92. stunda: «Vai puse vienmēr ir vienāda?»

Daļa bez veselā neko nenozīmē. Puse no lielas pizzas ir vairāk par pusi no
mazas, un tieši tāpēc divas daļas var salīdzināt tikai tad, kad veselais ir
viens un tas pats. Šī ir viena no svarīgākajām stundām visā tematā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         kolonnas)

TEMA = "Vai puse vienmēr ir vienāda?"

MERKIS = ("Pētīsim, ka daļa ir atkarīga no veselā lieluma, un minēsim "
          "piemērus.")

SATURS = [
    Sakums("Kura puse ir lielāka?",
           zimejums=kolonnas([("puse no 20", 10), ("puse no 100", 50)]),
           paraksts="Abas ir puses, bet viena ir piecas reizes lielāka.",
           fakti=["Daļa vienmēr ir daļa *no kaut kā*.",
                  "Divas daļas var salīdzināt tikai pie viena veselā."]),

    Doma("Daļa ir atkarīga no veselā",
         "{1|2} no 20 ir 10, bet {1|2} no 100 ir 50 - abas ir puses, bet "
         "pavisam dažādas.",
         soli=[
             "Vispirms noskaidro, kas ir veselais.",
             "Izrēķini daļu no tā.",
             "Ja veselie atšķiras, daļas salīdzināt nevar.",
             "Salīdzināt drīkst tikai iegūtos skaitļus.",
         ],
         pieze="Tāpēc uzdevumā vienmēr raksta «puse no 20», nevis vienkārši "
               "«puse». Bez veselā daļa ir tikai zīmes uz papīra."),

    Paraugs("Kura puse ir lielāka?",
            uzd="Salīdzini {1|2} no 20 un {1|2} no 100.",
            soli=[
                ("20 : 2 = 10",
                 "Puse no divdesmit."),
                ("100 : 2 = 50",
                 "Puse no simta."),
                ("10 < 50",
                 "Otrā puse ir lielāka, kaut abas ir puses."),
            ],
            atbilde="puse no 100 ir lielāka"),

    Petijums("Divas dažādas puses",
             vajag="divas dažāda garuma papīra sloksnes",
             soli=[
                 "Izmēri abas sloksnes un pieraksti garumus.",
                 "Saloc katru uz pusēm.",
                 "Izmēri abas puses.",
                 "Salīdzini un uzraksti, ko pamanīji.",
             ],
             secinajums="Abas ir puses, bet to garumi atšķiras - jo atšķiras "
                        "veselie."),

    Ievadi("Daļa no dažādiem veselajiem", [
        {"jaut": "Cik ir {1|2} no 20?", "atb": ["10"], "padoms": "20 : 2."},
        {"jaut": "Cik ir {1|2} no 100?", "atb": ["50"], "padoms": "100 : 2."},
        {"jaut": "Cik ir {1|4} no 40?", "atb": ["10"], "padoms": "40 : 4."},
        {"jaut": "Cik ir {1|4} no 80?", "atb": ["20"], "padoms": "80 : 4."},
        {"jaut": "Cik ir {1|3} no 60?", "atb": ["20"], "padoms": "60 : 3."},
        {"jaut": "Kurš skaitlis ir lielāks: {1|2} no 20 vai {1|4} no 80? "
                 "Ieraksti lielāko.",
         "atb": ["20"], "padoms": "10 un 20."},
    ], pamats=4),

    Zimejums("Ceturtdaļa no diviem dažādiem veselajiem",
             kolonnas([("1/4 no 40", 10), ("1/4 no 80", 20)]),
             paskaidro="Abas ir ceturtdaļas, bet otrā ir divreiz lielāka - jo "
                       "veselais ir divreiz lielāks.",
             ievads="Tā pati daļa, divi dažādi veselie."),

    Varianti("Vai daļas var salīdzināt?", [
        {"jaut": "Vai {1|2} vienmēr ir viens un tas pats skaitlis?",
         "opcijas": ["Nē, tas atkarīgs no veselā", "Jā, vienmēr",
                     "Jā, ja veselais ir liels", "To nevar pateikt"],
         "pareizi": 0, "padoms": "Puse no 20 un no 100 ir dažādas."},
        {"jaut": "Kurš skaitlis ir lielāks: {1|2} no 30 vai {1|3} no 60?",
         "opcijas": ["{1|3} no 60", "{1|2} no 30", "Abi vienādi",
                     "To nevar pateikt"],
         "pareizi": 0, "padoms": "15 un 20."},
        {"jaut": "Kad divas daļas var salīdzināt tieši?",
         "opcijas": ["Kad veselais ir viens un tas pats",
                     "Vienmēr", "Kad saucēji vienādi", "Nekad"],
         "pareizi": 0, "padoms": "Citādi jāizrēķina skaitļi."},
        {"jaut": "Cik ir {1|5} no 50?",
         "opcijas": ["10", "5", "25", "45"],
         "pareizi": 0, "padoms": "50 : 5."},
    ], pamats=4),

    Pasaule("Kurš dzīvnieks apēd vairāk?",
            Ievadi("", [
                {"jaut": "Lācis apēd {1|2} no 40 kg barības. Cik kilogramu?",
                 "atb": ["20"], "padoms": "40 : 2."},
                {"jaut": "Vāvere apēd {1|2} no 2 kg. Cik kilogramu?",
                 "atb": ["1"], "padoms": "2 : 2."},
                {"jaut": "Par cik kilogramiem lācis apēd vairāk?",
                 "atb": ["19"], "padoms": "20 − 1."},
                {"jaut": "Cik kilogramu ir {1|4} no 40 kg?",
                 "atb": ["10"], "padoms": "40 : 4."},
            ]),
            pavediens="daba",
            konteksts="Abi apēd pusi no savas barības, bet lāča puse ir "
                      "divdesmit reižu lielāka.",
            kapec="Bez veselā daļa nepasaka, cik tas ir daudz."),

    Kopsavilkums([
        "Zinu, ka daļa ir atkarīga no veselā lieluma.",
        "Izrēķinu daļu no dažādiem veselajiem un salīdzinu skaitļus.",
        "Zinu, ka daļas salīdzināt var tikai pie viena veselā.",
        "Minu piemērus no dzīves.",
    ]),

    Majas([
        "Izrēķini {1|2} no 50 un {1|2} no 500.",
        "Atrodi mājās divas dažāda lieluma lietas un sadali abas uz pusēm.",
        "Pastāsti mājiniekiem, kāpēc «puse» bez veselā neko nenozīmē.",
    ]),
]
