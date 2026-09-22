# -*- coding: utf-8 -*-
"""5. klase, 19. stunda: «Kādi ir abi skaitļi?»

Pirmais uzdevumu veids, kuru bez zīmējuma atrisināt ir grūti: zināma divu
skaitļu summa un starpība. Shematiskais zīmējums te nav ilustrācija - tas ir
pats risinājums, jo tikai uz tā redzams, kāpēc starpību atņem, pirms dala uz
pusēm.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, kolonnas)

TEMA = "Kādi ir abi skaitļi?"

MERKIS = ("Iemācīsimies atrast abus skaitļus, ja zināma to summa un "
          "starpība, veidojot shematisku zīmējumu.")

SATURS = [
    Sakums("Divi skaitļi slēpjas aiz diviem faktiem",
           fakti=["Abu skaitļu summa ir 100.",
                  "Viens no tiem ir par 20 lielāks nekā otrs.",
                  "Ar vienu faktu skaitļu ir bezgalīgi daudz, ar abiem - "
                  "tikai viens pāris."]),

    Doma("Nogriez starpību - paliek divi vienādi gabali",
         "Ja abus skaitļus uzzīmē kā stabiņus, tie atšķiras tieši par "
         "starpību.",
         soli=[
             "Uzzīmē divus stabiņus: otrs garāks tieši par starpību.",
             "Atņem starpību no summas - abi gabali kļūst vienādi.",
             "Izdali atlikumu ar 2 - tas ir mazākais skaitlis.",
             "Mazākajam pieskaiti starpību - tas ir lielākais skaitlis.",
             "Pārbaudi: vai summa un starpība sanāk tādas, kā dotas?",
         ],
         pieze="Ja summa un starpība ir dažādas - viena pāra, otra "
               "nepāra -, veselu skaitļu pāra nav: 20 − 5 = 15 uz pusēm "
               "nedalās."),

    Zimejums("Tā izskatās atbilde",
             kolonnas([("mazākais", 40), ("lielākais", 60)]),
             paskaidro="Abi stabiņi kopā ir 100, un otrs ir par 20 garāks. "
                       "Nogriežot 20, paliktu divi stabiņi pa 40.",
             ievads="Summa 100, starpība 20."),

    Paraugs("Cik skolēnu katrā klasē?",
            uzd="Divās klasēs kopā ir 53 skolēni, un vienā no tām ir par 5 "
                "skolēniem vairāk. Cik skolēnu katrā klasē?",
            soli=[
                ("53 − 5 = 48",
                 "Nogriežam starpību - paliek divi vienādi gabali."),
                ("48 : 2 = 24",
                 "Mazākajā klasē ir 24 skolēni."),
                ("24 + 5 = 29",
                 "Lielākajā klasē ir 29 skolēni."),
                ("Pārbaude: 24 + 29 = 53 un 29 − 24 = 5",
                 "Abi dotie fakti sakrīt."),
            ],
            atbilde="24 un 29 skolēni"),

    Ievadi("Atrodi abus skaitļus", [
        {"jaut": "Summa 100, starpība 20. Kāds ir mazākais skaitlis?",
         "atb": ["40"], "padoms": "(100 − 20) : 2."},
        {"jaut": "Summa 100, starpība 20. Kāds ir lielākais skaitlis?",
         "atb": ["60"], "padoms": "40 + 20."},
        {"jaut": "Summa 30, starpība 6. Kāds ir mazākais skaitlis?",
         "atb": ["12"], "padoms": "(30 − 6) : 2."},
        {"jaut": "Summa 30, starpība 6. Kāds ir lielākais skaitlis?",
         "atb": ["18"], "padoms": "12 + 6."},
        {"jaut": "Summa 84, starpība 10. Kāds ir mazākais skaitlis?",
         "atb": ["37"], "padoms": "(84 − 10) : 2."},
        {"jaut": "Summa 250, starpība 50. Kāds ir lielākais skaitlis?",
         "atb": ["150"], "padoms": "(250 − 50) : 2 = 100; 100 + 50."},
        {"jaut": "Summa 1 000, starpība 200. Kāds ir mazākais skaitlis?",
         "atb": ["400"], "padoms": "(1 000 − 200) : 2."},
        {"jaut": "Summa 45, starpība 45. Kāds ir mazākais skaitlis?",
         "atb": ["0"], "padoms": "(45 − 45) : 2."},
    ], pamats=4,
        ievads="Vispirms nogriez starpību, tikai tad dali uz pusēm."),

    Varianti("Kāpēc tā drīkst?", [
        {"jaut": "Kāpēc no summas vispirms atņem starpību?",
         "opcijas": ["Lai paliktu divi vienādi gabali",
                     "Lai skaitlis kļūtu mazāks",
                     "Lai summa dalītos ar 2",
                     "Tā ir kārtula bez iemesla"],
         "pareizi": 0,
         "padoms": "Paskaties uz stabiņiem: ko nogriež?"},
        {"jaut": "Vai var atrast divus veselus skaitļus, kuru summa ir 20 un "
                 "starpība 5?",
         "opcijas": ["Nē, 20 − 5 nedalās ar 2",
                     "Jā, tie ir 12 un 7",
                     "Jā, tie ir 15 un 5",
                     "Jā, bet tikai viens no tiem ir vesels"],
         "pareizi": 0,
         "padoms": "Izrēķini (20 − 5) : 2."},
        {"jaut": "Ko pārbauda pēc atbildes iegūšanas?",
         "opcijas": ["Vai summa un starpība sakrīt ar dotajām",
                     "Vai skaitļi ir pāra",
                     "Vai skaitļi ir apaļi",
                     "Neko, atbilde ir gatava"],
         "pareizi": 0,
         "padoms": "Abi dotie fakti jāapmierina vienlaikus."},
        {"jaut": "Ja starpība ir 0, kādi ir abi skaitļi?",
         "opcijas": ["Vienādi", "Blakus skaitļi", "Nulles", "Tādu nav"],
         "pareizi": 0,
         "padoms": "Neviens nav lielāks par otru."},
    ], pamats=4),

    Pasaule("Cik grāmatu katrā plauktā?",
            Ievadi("", [
                {"jaut": "Divos plauktos kopā 96 grāmatas, augšējā par 12 "
                         "vairāk. Cik ir apakšējā?",
                 "atb": ["42"], "padoms": "(96 − 12) : 2."},
                {"jaut": "Cik grāmatu ir augšējā plauktā?",
                 "atb": ["54"], "padoms": "42 + 12."},
                {"jaut": "Divās klasēs kopā 47 skolēni, vienā par 3 vairāk. "
                         "Cik ir mazākajā?",
                 "atb": ["22"], "padoms": "(47 − 3) : 2."},
                {"jaut": "Ēdnīcā izsniedza 130 porcijas divās maiņās, otrajā "
                         "par 10 mazāk. Cik porciju bija otrajā maiņā?",
                 "atb": ["60"], "padoms": "(130 − 10) : 2."},
            ]),
            pavediens="skola",
            konteksts="Skolā bieži zina kopskaitu un to, par cik viens ir "
                      "lielāks - bet ne pašus skaitļus.",
            kapec="Nogriez starpību, izdali uz pusēm, pieliec atpakaļ."),

    Kopsavilkums([
        "Veidoju shematisku zīmējumu situācijai ar summu un starpību.",
        "Atrodu mazāko skaitli: no summas atņemu starpību un dalu ar 2.",
        "Atrodu lielāko, pieskaitot starpību mazākajam.",
        "Pārbaudu abus dotos faktus, pirms rakstu atbildi.",
    ]),

    Majas([
        "Izdomā divus skaitļus, pasaki kādam tikai to summu un starpību un "
        "paskaties, vai viņš tos atmin.",
        "Uzzīmē stabiņus uzdevumam, kurā summa ir 60 un starpība 10.",
        "Atrodi summas un starpības pāri, kuram veselu skaitļu atrisinājuma "
        "nav.",
    ]),
]
