# -*- coding: utf-8 -*-
"""6. klase, 87. stunda: «Cik maksāja sākumā?»

Apgrieztais uzdevums: zināma daļa, meklē kopumu. Tas ir grūtāks nekā tiešais
un tieši tāpēc pārbaudes darbos parādās biežāk. Ceļš ir viens - vispirms
atrast, cik ir viens procents.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala)

TEMA = "Cik maksāja sākumā?"

MERKIS = ("Iemācīsimies aprēķināt veselo, ja zināma procentu skaitliskā "
          "vērtība.")

SATURS = [
    Sakums("Zināms gabals - meklē visu",
           zimejums=dala(5, 1, "20 % = 14 €"),
           paraksts="Ja viena piektdaļa ir 14 €, tad viss kopums ir "
                    "5 · 14 = 70 €.",
           fakti=["Vispirms atrod, cik ir viens procents.",
                  "Tad reizina ar simtu - tas ir viss kopums.",
                  "Pārbaude: no atrastā kopuma jāiznāk sākotnējais gabals."]),

    Doma("Viens procents ir atslēga",
         "Ja zināms, cik ir p procenti, tad viens procents ir šis skaitlis, "
         "dalīts ar p, un kopums - viens procents reiz 100.",
         soli=[
             "Pieraksti, cik procenti ir zināmi un kāda ir to vērtība.",
             "Izdali vērtību ar procentu skaitu - tas ir viens procents.",
             "Reizini ar 100 - tas ir kopums.",
             "Pārbaudi: aprēķini doto procentu no atrastā kopuma.",
             "Salīdzini ar sākotnējo skaitli.",
         ],
         pieze="Ja zināmi ir 50 %, 25 % vai 20 %, ceļš ir vēl īsāks: kopums "
               "ir divas, četras vai piecas reizes lielāks par doto skaitli."),

    Paraugs("Atrodi sākotnējo cenu",
            uzd="Atlaide 20 % ir 14 €. Cik maksāja prece sākumā?",
            soli=[
                ("20 % ir 14 €",
                 "Zināmā daļa."),
                ("1 % ir 14 : 20 = 0,7 €",
                 "Viens procents."),
                ("100 % ir 0,7 · 100 = 70 €",
                 "Viss kopums."),
                ("Pārbaude: 20 % no 70 ir 14",
                 "Sakrīt ar doto."),
            ],
            atbilde="70 €"),

    Ievadi("Atrodi kopumu", [
        {"jaut": "20 % ir 14. Cik ir viens procents?",
         "atb": ["0,7", "0.7"], "padoms": "14 : 20."},
        {"jaut": "Cik ir kopums?",
         "atb": ["70"], "padoms": "0,7 · 100."},
        {"jaut": "25 % ir 15. Cik ir kopums?",
         "atb": ["60"], "padoms": "15 · 4."},
        {"jaut": "50 % ir 32. Cik ir kopums?",
         "atb": ["64"], "padoms": "32 · 2."},
        {"jaut": "10 % ir 9. Cik ir kopums?",
         "atb": ["90"], "padoms": "9 · 10."},
        {"jaut": "40 % ir 24. Cik ir kopums?",
         "atb": ["60"], "padoms": "1 % ir 0,6."},
    ], pamats=4,
        ievads="Vispirms viens procents, tikai tad simts."),

    Varianti("Kurš ceļš ir īsāks?", [
        {"jaut": "Ja 25 % ir 15, kopumu iegūst, reizinot ar...",
         "opcijas": ["4", "25", "100", "0,25"],
         "pareizi": 0,
         "padoms": "25 % ir ceturtdaļa."},
        {"jaut": "Ja 50 % ir 32, kopumu iegūst, reizinot ar...",
         "opcijas": ["2", "50", "100", "0,5"],
         "pareizi": 0,
         "padoms": "Puse."},
        {"jaut": "Skolēns rēķina «20 % ir 14, tātad kopums ir 14 : 5 = 2,8». "
                 "Kas nav labi?",
         "opcijas": ["Jāreizina, nevis jādala", "Jādala ar 20",
                     "Jāreizina ar 20", "Viss ir pareizi"],
         "pareizi": 0,
         "padoms": "Kopums ir lielāks par daļu."},
        {"jaut": "Ja jaunā cena ir 80 % un tā ir 48 €, cik maksāja sākumā?",
         "opcijas": ["60 €", "38,4 €", "128 €", "80 €"],
         "pareizi": 0,
         "padoms": "1 % ir 0,6 €."},
    ], pamats=4),

    Pasaule("Cik maksāja pirms atlaides?",
            Ievadi("", [
                {"jaut": "Atlaide 25 % ir 20 €. Cik maksāja prece sākumā?",
                 "atb": ["80"], "padoms": "20 · 4."},
                {"jaut": "Cik eiro maksā prece pēc atlaides?",
                 "atb": ["60"], "padoms": "80 − 20."},
                {"jaut": "Cita prece pēc 40 % atlaides maksā 54 €. Cik tā "
                         "maksāja sākumā?",
                 "atb": ["90"], "padoms": "54 ir 60 %; 1 % ir 0,9."},
                {"jaut": "Cik eiro bija tās atlaide?",
                 "atb": ["36"], "padoms": "90 − 54."},
            ]),
            pavediens="veikals",
            konteksts="Reizēm cenu zīmē redzama tikai jaunā cena un atlaides "
                      "procenti - sākotnējā jāizrēķina pašam.",
            kapec="Viens procents savieno jebkuru daļu ar kopumu."),

    Zimejums("No daļas uz kopumu",
             dala(5, 1, "1 daļa = 20 %"),
             paskaidro="Ja viena daļa no piecām ir 14 €, tad visas piecas ir "
                       "70 €. Tas pats rēķins kā attiecību tematā.",
             ievads="Josla palīdz arī apgrieztajā uzdevumā."),

    Kopsavilkums([
        "Atrodu viena procenta vērtību no dotās daļas.",
        "Aprēķinu kopumu, reizinot viena procenta vērtību ar 100.",
        "Lietoju īsceļus zināmiem procentiem.",
        "Pārbaudu atbildi, rēķinot doto procentu no kopuma.",
    ]),

    Majas([
        "Atrodi kopumu, ja 15 % ir 45.",
        "Izdomā uzdevumu, kurā zināma jaunā cena un atlaide.",
        "Pieraksti, kāpēc kopums vienmēr ir lielāks par doto daļu.",
    ]),
]
