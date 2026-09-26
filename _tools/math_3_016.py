# -*- coding: utf-8 -*-
"""3. klase, 16. stunda: «Cik daudz tabulas zini no galvas?»

Mikrotemata noslēgums: viss, kas mācīts no 9. līdz 15. stundai, vienā
pašpārbaudē. Uzdevumi apzināti sajaukti pa rindām, jo tieši sajaukumā redz,
vai reizinājums ir atmiņā vai tikai rindas ritmā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Cik daudz tabulas zini no galvas?"

MERKIS = ("Formatīvi pārbaudīsim visu reizināšanas tabulu un izvēlēsimies, "
          "ko vēl trenēt.")

SATURS = [
    Sakums("Vai tabula ir atmiņā vai tikai rindas ritmā?",
           zimejums=restis([["9 · 6", "7 · 8", "8 · 8"],
                            ["6 · 7", "9 · 9", "8 · 9"]],
                           "sajaukti, ne pēc rindām"),
           paraksts="Kad rinda ir sajaukta, ritms vairs nepalīdz.",
           fakti=["Rindā skaitot, atbildi var uzminēt pēc ritma.",
                  "Sajauktā secībā redz, kas tiešām ir iemācīts."]),

    Doma("Zināt no galvas nozīmē - jebkurā secībā",
         "Ja atbilde nāk tikai tad, kad skaita rindu no sākuma, reizinājums "
         "vēl nav iemācīts.",
         soli=[
             "Izdari uzdevumus sajauktā secībā.",
             "Katram atceries atbildi, neskaitot rindu.",
             "Ja rinda tomēr bija jāskaita, atzīmē šo reizinājumu.",
             "Atzīmētos ieliec kartīšu kaudzītē «vēl mācos».",
         ],
         pieze="Šī nav atzīme. Šī ir karte, kas pasaka, kur rīt jāiet."),

    Paraugs("Kā pārbaudīt savu atbildi?",
            uzd="Uzrakstīji, ka 8 · 7 = 54. Kā pamanīt kļūdu?",
            soli=[
                ("54 : 7 = ?",
                 "Pārbaude ar dalīšanu: 7 · 7 = 49, 8 · 7 = 56 - 54 "
                 "starp tiem neiekrīt."),
                ("Septiņnieku rindā 54 nav",
                 "Rinda ir 49, 56, 63 - tātad atbilde nav no šīs rindas."),
                ("8 · 7 = 56",
                 "Pareizā atbilde; 54 ir 6 · 9."),
            ],
            atbilde="56"),

    Ievadi("Sajaukta tabula", [
        {"jaut": "9 · 6 = ?", "atb": ["54"], "padoms": "60 − 6."},
        {"jaut": "7 · 8 = ?", "atb": ["56"], "padoms": "49 + 7."},
        {"jaut": "8 · 8 = ?", "atb": ["64"], "padoms": "32 + 32."},
        {"jaut": "6 · 7 = ?", "atb": ["42"], "padoms": "35 + 7."},
        {"jaut": "9 · 9 = ?", "atb": ["81"], "padoms": "90 − 9."},
        {"jaut": "8 · 9 = ?", "atb": ["72"], "padoms": "80 − 8."},
        {"jaut": "72 : 8 = ?", "atb": ["9"], "padoms": "Kurš skaitlis reiz "
                                                       "8 dod 72?"},
        {"jaut": "63 : 9 = ?", "atb": ["7"], "padoms": "Kurš skaitlis reiz "
                                                       "9 dod 63?"},
    ], pamats=6),

    Zimejums("Astoņi grūtākie",
             restis([["6 · 6", "6 · 7", "6 · 8", "6 · 9"],
                     [36, 42, 48, 54],
                     ["7 · 7", "7 · 8", "8 · 8", "8 · 9"],
                     [49, 56, 64, 72]],
                    "tabulas smagākais stūris"),
             paskaidro="Ja šos astoņus zini droši, pārējā tabula nesagādā "
                       "grūtības.",
             ievads="Pārbaudi sevi: aizsedz apakšējo rindu."),

    Varianti("Vai atbilde ir ticama?", [
        {"jaut": "Kura atbilde 9 · 7 ir noteikti nepareiza?",
         "opcijas": ["65", "63", "70 − 7", "7 · 9"],
         "pareizi": 0, "padoms": "Ciparu summai jābūt 9."},
        {"jaut": "Kurš skaitlis ir gan sešnieku, gan astotnieku rindā?",
         "opcijas": ["48", "42", "56", "36"],
         "pareizi": 0, "padoms": "48 : 6 = 8 un 48 : 8 = 6."},
        {"jaut": "Kurš reizinājums dod vislielāko rezultātu?",
         "opcijas": ["9 · 9", "8 · 9", "7 · 9", "8 · 8"],
         "pareizi": 0, "padoms": "81, 72, 63 un 64."},
        {"jaut": "Ko darīt ar reizinājumu, kas prasīja rindas skaitīšanu?",
         "opcijas": ["Ielikt kaudzītē «vēl mācos»", "Aizmirst",
                     "Atzīmēt kā zināmu", "Pierakstīt divreiz"],
         "pareizi": 0, "padoms": "Tas vēl nav atmiņā."},
    ], pamats=4),

    Pasaule("Cik daļu ir lielā konstrukcijā?",
            Ievadi("", [
                {"jaut": "Tiltam ir 9 posmi, katrā 8 balsti. Cik balstu "
                         "kopā?",
                 "atb": ["72"], "padoms": "9 · 8."},
                {"jaut": "Katrā balstā ir 6 skrūves. Cik skrūvju ir vienā "
                         "posmā?",
                 "atb": ["48"], "padoms": "8 · 6."},
                {"jaut": "Cik skrūvju vajag 7 posmiem?",
                 "atb": ["336"], "padoms": "7 · 48 = 7 · 50 − 7 · 2."},
                {"jaut": "Noliktavā ir 64 balsti. Cik pilnu posmu no tiem "
                         "var salikt?",
                 "atb": ["8"], "padoms": "64 : 8."},
            ]),
            pavediens="tehnika",
            konteksts="Tiltu būvē no vienādiem posmiem - tāpēc visu materiālu "
                      "izrēķina ar reizināšanu.",
            kapec="Ja tabula ir atmiņā, materiālu var saskaitīt tieši "
                  "būvlaukumā."),

    Kopsavilkums([
        "Zinu reizināšanas tabulu arī sajauktā secībā.",
        "Atrodu dalījumu, domājot par reizinājumu.",
        "Pārbaudu savu atbildi ar rindu vai ar dalīšanu.",
        "Zinu, kurus reizinājumus man vēl jātrenē.",
    ]),

    Majas([
        "Palūdz, lai kāds tev pajautā desmit reizinājumus sajauktā secībā.",
        "Pieraksti tos, kuros kļūdījies, un atkārto tos trīs dienas pēc "
        "kārtas.",
        "Izdomā uzdevumu, kurā vajag 9 · 8.",
    ]),
]
