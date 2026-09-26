# -*- coding: utf-8 -*-
"""3. klase, 8. stunda: «Cik veikli jau rēķini?»

Mikrotemata noslēgums. Vērtējuma te nav - ir pašpārbaude: skolēns izrēķina
sešnieku un septiņnieku reizinājumus un pats pasaka, ar kuru paņēmienu viņš
tos atcerējās. Tieši šis otrais solis atšķir treniņu no minēšanas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Cik veikli jau rēķini?"

MERKIS = ("Pārbaudīsim, cik droši zinām reizinājumus ar 6 un 7, un "
          "paskaidrosim savu atcerēšanās paņēmienu.")

SATURS = [
    Sakums("Vai vari nosaukt atbildi ātrāk, nekā paspēj saskaitīt?",
           zimejums=restis([["6 · 6", "6 · 7", "6 · 8", "6 · 9"],
                            ["7 · 6", "7 · 7", "7 · 8", "7 · 9"]],
                           "astoņi reizinājumi - cik ātri?"),
           paraksts="Šos astoņus tu šonedēļ esi trenējis visvairāk.",
           fakti=["Veikli nozīmē: atbilde nāk ātrāk nekā skaitīšana.",
                  "Ja atbilde nenāk, vienmēr ir paņēmiens, kā to iegūt."]),

    Doma("Zināt un izrēķināt ir divas dažādas lietas",
         "Labākais rēķinātājs zina lielāko daļu no galvas un pārējo prot "
         "ātri iegūt.",
         soli=[
             "Vispirms mēģini atcerēties.",
             "Ja neatceries, ej no tuvākā zināmā: 6 · 8 ir 5 · 8 un vēl 8.",
             "Pārbaudi atbildi ar rindu: vai tā dalās ar 6 vai 7?",
             "Pieraksti, kuri reizinājumi vēl jātrenē.",
         ],
         pieze="Kļūda nav slikta ziņa - tā ir norāde, kuru kartīti rīt "
               "vajag paņemt pirmo."),

    Paraugs("Kā rīkoties, ja atbilde neatnāk?",
            uzd="Cik ir 7 · 9, ja šo reizinājumu neatceries?",
            soli=[
                ("10 · 9 = 90",
                 "Desmitnieku rinda ir tā, kuru zina vienmēr."),
                ("90 − 9 · 3 = 90 − 27 = 63",
                 "No desmit grupām noņem trīs deviņnieku grupas."),
                ("7 · 9 = 63",
                 "Pārbaude: 63 : 7 = 9 - sakrīt."),
            ],
            atbilde="63"),

    Ievadi("Astoņi galvenie reizinājumi", [
        {"jaut": "6 · 6 = ?", "atb": ["36"], "padoms": "30 + 6."},
        {"jaut": "7 · 7 = ?", "atb": ["49"], "padoms": "42 + 7."},
        {"jaut": "6 · 8 = ?", "atb": ["48"], "padoms": "40 + 8."},
        {"jaut": "7 · 8 = ?", "atb": ["56"], "padoms": "49 + 7."},
        {"jaut": "6 · 9 = ?", "atb": ["54"], "padoms": "60 − 6."},
        {"jaut": "7 · 9 = ?", "atb": ["63"], "padoms": "70 − 7."},
        {"jaut": "42 : 6 = ?", "atb": ["7"], "padoms": "Kurš skaitlis reiz "
                                                       "6 dod 42?"},
        {"jaut": "56 : 7 = ?", "atb": ["8"], "padoms": "Kurš skaitlis reiz "
                                                       "7 dod 56?"},
    ], pamats=4),

    Zimejums("Kur šie skaitļi ir rindā",
             restis([[6, 12, 18, 24, 30, 36, 42, 48, 54, 60],
                     [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]],
                    "augšā sešnieki, apakšā septiņnieki"),
             paskaidro="Viens skaitlis ir abās rindās - 42. Tas ir 6 · 7.",
             ievads="Atrodi savas atbildes šajās rindās."),

    Varianti("Kurš paņēmiens der?", [
        {"jaut": "Kā visātrāk iegūt 6 · 9, ja neatceries?",
         "opcijas": ["No 60 atņemt 6", "No 60 atņemt 9", "Pie 50 pieskaitīt 9",
                     "Reizināt 6 ar 10"],
         "pareizi": 0, "padoms": "10 · 6 = 60, noņem vienu sešnieku grupu."},
        {"jaut": "Kura atbilde nevar būt pareiza reizinājumam ar 7?",
         "opcijas": ["52", "49", "56", "63"],
         "pareizi": 0, "padoms": "Septiņnieku rindā 52 nav."},
        {"jaut": "6 · 7 un 7 · 6 - kāda ir atšķirība?",
         "opcijas": ["Atbilde ir viena un tā pati", "Pirmā ir lielāka",
                     "Otrā ir lielāka", "Tos nevar salīdzināt"],
         "pareizi": 0, "padoms": "Maiņas īpašība."},
        {"jaut": "Ko darīt ar reizinājumu, kas šodien nepadevās?",
         "opcijas": ["Atkārtot to rīt vēlreiz", "Aizmirst to",
                     "Pārrakstīt desmit reizes tūlīt", "Neko"],
         "pareizi": 0, "padoms": "Īss atkārtojums nākamajā dienā."},
    ], pamats=4),

    Pasaule("Cik dzīvnieku ir mežā?",
            Ievadi("", [
                {"jaut": "Mežā atrada 7 skudru pūžņus, katrā 6 lielas "
                         "ejas. Cik eju kopā?",
                 "atb": ["42"], "padoms": "7 · 6."},
                {"jaut": "Putnu būrīšu rindā ir 8 būrīši, katrā 7 olas. Cik "
                         "olu kopā?",
                 "atb": ["56"], "padoms": "8 · 7."},
                {"jaut": "Mežsargs saskaitīja 54 stādus 6 vienādās rindās. "
                         "Cik stādu ir vienā rindā?",
                 "atb": ["9"], "padoms": "54 : 6."},
                {"jaut": "63 ogas salika 7 vienādos groziņos. Cik ogu ir "
                         "vienā groziņā?",
                 "atb": ["9"], "padoms": "63 : 7."},
            ]),
            pavediens="daba",
            konteksts="Dabā bieži skaita rindās un grupās - tieši tāpēc "
                      "tabula noder arī ārpus klases.",
            kapec="Ar tabulu lielus skaitus var pateikt dažās sekundēs."),

    Kopsavilkums([
        "Veikli nosaucu reizinājumus ar 6 un 7.",
        "Atrodu dalījumu, domājot par reizinājumu.",
        "Paskaidroju, ar kuru paņēmienu ieguvu atbildi.",
        "Zinu, kuri reizinājumi man vēl jātrenē.",
    ]),

    Majas([
        "Palūdz, lai kāds tev pajautā visus astoņus galvenos reizinājumus.",
        "Pieraksti trīs, kas padevās visgrūtāk, un atkārto tos rīt.",
        "Izdomā uzdevumu par mežu, kurā jāizmanto 7 · 8.",
    ]),
]
