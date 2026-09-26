# -*- coding: utf-8 -*-
"""3. klase, 7. stunda: «Kā trenēties ar kartītēm?»

Stunda par to, kā mācīties, nevis par jaunu rēķinu. Kartītes strādā tāpēc,
ka tās atdala zināmo no nezināmā: pareizi atbildēto liek malā, pārējo atkārto
biežāk. Tas pats princips vēlāk der jebkurai vielai, tāpēc to māca ar rokām.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         kolonnas)

TEMA = "Kā trenēties ar kartītēm?"

MERKIS = ("Izveidosim savu kartīšu komplektu un iemācīsimies trenēties tā, "
          "lai atkārtotu tieši to, kas vēl nepadodas.")

SATURS = [
    Sakums("Kā iemācīties 20 reizinājumus ātrāk nekā 100?",
           zimejums=kolonnas([("zinu", 17), ("vēl mācos", 3)]),
           paraksts="Trenēt vajag tikai to mazo kaudzīti labajā pusē.",
           fakti=["Atkārtot to, ko jau zini, atmiņai gandrīz neko nedod.",
                  "Kartītes palīdz atdalīt zināmo no vēl nezināmā."]),

    Doma("Trenē tikai to, kas vēl nepadodas",
         "Divas kaudzītes: «zinu» un «vēl mācos» - un otrā kaudzīte kļūst "
         "arvien mazāka.",
         soli=[
             "Uzraksti uz kartītes priekšpuses reizinājumu, otrā pusē - "
             "atbildi.",
             "Pasaki atbildi skaļi, tikai tad apgriez kartīti.",
             "Ja atbildēji pareizi un ātri, liec kartīti kaudzītē «zinu».",
             "Ja nē - liec atpakaļ kaudzītē «vēl mācos» un atkārto vēlāk.",
         ],
         pieze="Svarīgi ir *vispirms atcerēties* un tikai tad pārbaudīt. Ja "
               "vienmēr paskaties uz atbildi, atmiņa netrenējas."),

    Paraugs("Cik kartīšu vajag sešnieku un septiņnieku rindai?",
            uzd="Katrai rindai no 2 līdz 10 ir 9 reizinājumi. Cik kartīšu "
                "vajag divām rindām?",
            soli=[
                ("9 kartītes vienai rindai",
                 "No 2 · 6 līdz 10 · 6 - tie ir deviņi reizinājumi."),
                ("2 · 9 = 18",
                 "Divas rindas - divreiz vairāk kartīšu."),
                ("18 − 1 = 17",
                 "Reizinājums 6 · 7 ir abās rindās, tāpēc kartīte vajadzīga "
                 "tikai viena."),
            ],
            atbilde="17 kartītes"),

    Ievadi("Pārbaudi sevi bez kartītēm", [
        {"jaut": "6 · 7 = ?", "atb": ["42"], "padoms": "35 + 7."},
        {"jaut": "7 · 9 = ?", "atb": ["63"], "padoms": "70 − 7."},
        {"jaut": "6 · 9 = ?", "atb": ["54"], "padoms": "60 − 6."},
        {"jaut": "7 · 8 = ?", "atb": ["56"], "padoms": "49 + 7."},
        {"jaut": "6 · 8 = ?", "atb": ["48"], "padoms": "40 + 8."},
        {"jaut": "7 · 6 = ?", "atb": ["42"], "padoms": "Tas pats, kas 6 · 7."},
    ], pamats=4,
        ievads="Vispirms pasaki atbildi skaļi, tikai tad ieraksti to "
               "lodziņā."),

    Petijums("Uztaisi savu kartīšu komplektu",
             vajag="biezāka papīra lapa, šķēres un zīmulis",
             soli=[
                 "Sagriez lapu 17 vienādās kartītēs.",
                 "Uzraksti priekšpusē reizinājumu, otrā pusē - atbildi.",
                 "Sajauc kartītes un izej tām cauri vienu reizi.",
                 "Saskaiti, cik kartīšu nonāca kaudzītē «vēl mācos».",
                 "Rīt izej cauri tikai šai kaudzītei.",
             ],
             secinajums="Ja «vēl mācos» kaudzīte katru dienu kļūst mazāka, "
                        "treniņš strādā."),

    Zimejums("Kaudzīte «vēl mācos» sarūk",
             kolonnas([("1. diena", 9), ("2. diena", 6), ("3. diena", 3),
                       ("4. diena", 1)]),
             paskaidro="Tas nav burvju triks - tikai katru dienu atkārto "
                       "tieši to, kas vakar nepadevās.",
             ievads="Tā izskatās nedēļa ar kartītēm."),

    Varianti("Kā trenēties gudrāk?", [
        {"jaut": "Ko darīt ar kartīti, uz kuru atbildēji pareizi un ātri?",
         "opcijas": ["Likt kaudzītē «zinu»", "Atkārtot uzreiz vēlreiz",
                     "Izmest", "Uzrakstīt vēl vienu tādu pašu"],
         "pareizi": 0, "padoms": "Trenē to, kas vēl nepadodas."},
        {"jaut": "Kas jādara vispirms - jāatceras atbilde vai jāapgriež "
                 "kartīte?",
         "opcijas": ["Jāatceras atbilde", "Jāapgriež kartīte",
                     "Vienalga", "Jāpaskatās tabulā"],
         "pareizi": 0, "padoms": "Atmiņa trenējas tikai tad, kad to lieto."},
        {"jaut": "Cik ilgi vienā reizē ir vērts trenēties?",
         "opcijas": ["Īsi, bet katru dienu", "Vienu reizi ļoti ilgi",
                     "Tikai pirms pārbaudes darba", "Reizi mēnesī"],
         "pareizi": 0, "padoms": "Biežums atmiņai palīdz vairāk nekā "
                                 "garums."},
        {"jaut": "Kāpēc vienai kartītei pietiek ar 6 · 7, un 7 · 6 nav "
                 "vajadzīga?",
         "opcijas": ["Jo a · b = b · a", "Jo 7 ir lielāks",
                     "Jo kartīšu ir par maz", "Jo atbildes ir dažādas"],
         "pareizi": 0, "padoms": "Atceries maiņas īpašību."},
    ], pamats=4),

    Pasaule("Cik ilgi jātrenējas komandai?",
            Ievadi("", [
                {"jaut": "Treniņš notiek 3 reizes nedēļā pa 2 stundām. Cik "
                         "stundas tas ir nedēļā?",
                 "atb": ["6"], "padoms": "3 · 2."},
                {"jaut": "Cik stundu sanāk 7 nedēļās?",
                 "atb": ["42"], "padoms": "7 · 6."},
                {"jaut": "Komandā ir 6 spēlētāji, katrs met 7 metienus. Cik "
                         "metienu kopā?",
                 "atb": ["42"], "padoms": "6 · 7."},
                {"jaut": "Treneris saskaitīja 56 metienus, katrs spēlētājs "
                         "meta 7. Cik spēlētāju bija?",
                 "atb": ["8"], "padoms": "56 : 7."},
            ]),
            pavediens="sports",
            konteksts="Sportisti trenē tieši to kustību, kas vēl neizdodas - "
                      "gluži tāpat kā kartītes.",
            kapec="Treniņa plāns ir rēķins: reizes nedēļā reiz stundas."),

    Kopsavilkums([
        "Izveidoju savu kartīšu komplektu reizināšanas tabulai.",
        "Trenējos tā, ka vispirms atceros un tikai tad pārbaudu.",
        "Atdalu to, ko jau zinu, no tā, kas vēl jāmācās.",
        "Sekoju, kā mana «vēl mācos» kaudzīte kļūst mazāka.",
    ]),

    Majas([
        "Izej cauri savām kartītēm vienu reizi un saskaiti abas kaudzītes.",
        "Palūdz mājiniekam pajautāt tev piecus reizinājumus no galvas.",
        "Rīt atkārto tikai tās kartītes, kas šodien nepadevās.",
    ], ievads="Piecas minūtes katru dienu dod vairāk nekā stunda reizi "
              "nedēļā."),
]
