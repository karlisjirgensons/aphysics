# -*- coding: utf-8 -*-
"""3. klase, 71. stunda: «Vai plāns ir labs?»

Praktiskā darba noslēgums. Vērtēšanas kritēriji ir zināmi iepriekš un ir
pārbaudāmi ar mērījumu, nevis ar gaumi: vai proporcijas sakrīt, vai
samazinājums pierakstīts, vai objekti atrodami. Tas ir arī gatavošanās PD.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Vai plāns ir labs?"

MERKIS = ("Prezentēsim plānu, salīdzināsim to ar citu grupu plāniem un "
          "izvērtēsim pēc kritērijiem.")

SATURS = [
    Sakums("Pēc kā pateikt, ka plāns ir labs?",
           zimejums=restis([["kritērijs", "jā/nē"],
                            ["Vai samazinājums pierakstīts?", ""],
                            ["Vai proporcijas sakrīt?", ""],
                            ["Vai durvis un logi atzīmēti?", ""],
                            ["Vai objektus var atrast?", ""]],
                           "četri kritēriji"),
           paraksts="Katru no tiem var pārbaudīt ar lineālu, ne ar gaumi.",
           fakti=["Labs plāns nav skaists - tas ir lietojams.",
                  "Katrs kritērijs ir pārbaudāms ar mērījumu."]),

    Doma("Plānu pārbauda ar mērījumu",
         "Izmēri plānā, reizini ar samazinājumu un salīdzini ar īsto izmēru - "
         "ja sakrīt, plāns strādā.",
         soli=[
             "Izmēri plānā kādu objektu.",
             "Reizini mērījumu ar samazinājumu.",
             "Salīdzini ar īsto izmēru mērījumu tabulā.",
             "Atkārto vēl diviem objektiem.",
         ],
         pieze="Neliela atšķirība ir normāla - zīmuļa svītra arī ir gandrīz "
               "milimetru plata. Bet divkārša atšķirība nozīmē kļūdu."),

    Paraugs("Vai plāns iztur pārbaudi?",
            uzd="Plānā galds ir 2,4 cm. Samazinājums 50. Vai tas atbilst "
                "120 cm garam galdam?",
            soli=[
                ("2,4 · 50 = 120",
                 "Plāna mērījumu reizina ar samazinājumu."),
                ("120 cm = 120 cm",
                 "Sakrīt ar mērījumu tabulu."),
                ("Plāns šajā vietā ir pareizs",
                 "To pašu pārbauda vēl diviem objektiem."),
            ],
            atbilde="atbilst"),

    Petijums("Novērtē citas grupas plānu",
             vajag="cits plāns, lineāls un kritēriju lapa",
             soli=[
                 "Apmainieties plāniem ar citu grupu.",
                 "Pārbaudiet katru kritēriju un atzīmējiet «jā» vai «nē».",
                 "Izmēriet divus objektus un pārbaudiet aprēķinu.",
                 "Uzrakstiet vienu ieteikumu, kā plānu uzlabot.",
             ],
             secinajums="Vērtējums ir noderīgs tikai tad, kad tam pievienots "
                        "konkrēts ieteikums."),

    Ievadi("Pārbaudi plānu", [
        {"jaut": "Plānā 4 cm, samazinājums 50. Cik centimetru telpā?",
         "atb": ["200"], "padoms": "4 · 50."},
        {"jaut": "Plānā 2 cm, samazinājums 50. Cik centimetru telpā?",
         "atb": ["100"], "padoms": "2 · 50."},
        {"jaut": "Plānā 16 cm, samazinājums 50. Cik centimetru telpā?",
         "atb": ["800"], "padoms": "16 · 50."},
        {"jaut": "Cik metru tas ir?", "atb": ["8"],
         "padoms": "800 : 100."},
        {"jaut": "Plānā 12 cm, samazinājums 50. Cik metru telpā?",
         "atb": ["6"], "padoms": "600 cm."},
        {"jaut": "Plānā 1,8 cm, samazinājums 50. Cik centimetru telpā?",
         "atb": ["90"], "padoms": "1,8 · 50."},
    ], pamats=4),

    Zimejums("Vērtēšanas lapa",
             restis([["kritērijs", "1. grupa", "2. grupa"],
                     ["samazinājums", "jā", "nē"],
                     ["proporcijas", "jā", "jā"],
                     ["durvis un logi", "jā", "jā"],
                     ["objekti atrodami", "nē", "jā"]],
                    "divu plānu salīdzinājums"),
             paskaidro="Abiem plāniem ir pa vienai vājai vietai - un abas var "
                       "izlabot dažās minūtēs.",
             ievads="Tā izskatās aizpildīta vērtēšanas lapa."),

    Varianti("Kas plānam pietrūkst?", [
        {"jaut": "Plānā nav pierakstīts samazinājums. Kāpēc tas ir slikti?",
         "opcijas": ["Nevar atjaunot īstos izmērus", "Plāns izskatās tukšs",
                     "Nevar saprast, kur ir durvis", "Tas nav slikti"],
         "pareizi": 0, "padoms": "Bez samazinājuma plāns ir tikai zīmējums."},
        {"jaut": "Plānā telpa ir kvadrātiska, bet īstā ir divreiz garāka "
                 "nekā plata. Kas nav kārtībā?",
         "opcijas": ["Proporcijas nesakrīt", "Samazinājums ir par lielu",
                     "Trūkst durvju", "Viss ir kārtībā"],
         "pareizi": 0, "padoms": "Abas malas nav samazinātas vienādi."},
        {"jaut": "Kā pārbaudīt plāna pareizību?",
         "opcijas": ["Izmērīt un reizināt ar samazinājumu",
                     "Paskatīties uz to", "Pajautāt zīmētājam",
                     "Salīdzināt krāsas"],
         "pareizi": 0, "padoms": "Pārbaude ir mērījums."},
        {"jaut": "Kas jāpievieno vērtējumam?",
         "opcijas": ["Konkrēts ieteikums", "Atzīme", "Paraksts",
                     "Krāsains vāks"],
         "pareizi": 0, "padoms": "Vērtējums bez ieteikuma neko nemaina."},
    ], pamats=4),

    Pasaule("Kā plānu izmanto skolā?",
            Ievadi("", [
                {"jaut": "Plānā klase ir 16 cm un 12 cm, samazinājums 50. "
                         "Cik centimetru ir īstais garums?",
                 "atb": ["800"], "padoms": "16 · 50."},
                {"jaut": "Cik centimetru ir īstais platums?",
                 "atb": ["600"], "padoms": "12 · 50."},
                {"jaut": "Cik metru ir klases perimetrs?",
                 "atb": ["28"], "padoms": "2 · (8 + 6)."},
                {"jaut": "Cik metru grīdlīstes vajag, ja durvis aizņem 1 m?",
                 "atb": ["27"], "padoms": "28 − 1."},
            ]),
            pavediens="skola",
            konteksts="Gatavu plānu izmanto remontam, mēbeļu pārkārtošanai "
                      "un evakuācijas ceļiem.",
            kapec="Plāns ir noderīgs tieši tik ilgi, kamēr tam var uzticēties."),

    Kopsavilkums([
        "Prezentēju savu plānu un paskaidroju samazinājumu.",
        "Pārbaudu plānu ar mērījumu un reizināšanu.",
        "Izvērtēju plānu pēc četriem kritērijiem.",
        "Sniedzu konkrētu ieteikumu, kā plānu uzlabot.",
    ]),

    Majas([
        "Parādi savu plānu mājiniekiem un palūdz atrast pēc tā kādu lietu.",
        "Pārbaudi divus objektus ar lineālu un reizināšanu.",
        "Pārlasi tematu un atzīmē, kas vēl jāatkārto pirms pārbaudes darba.",
    ], ievads="Šī ir pēdējā stunda pirms pārbaudes darba."),
]
