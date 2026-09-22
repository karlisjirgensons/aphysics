# -*- coding: utf-8 -*-
"""5. klase, 157. stunda: «Kā izvēlēties vienību uz ass?»

Punktu atlikt skolēns jau prot; te parādās jautājums, ko parasti neviens
neuzdod: cik liela ir viena rūtiņa. Ja cena ir 250 €, bet uz ass viena
rūtiņa ir viens eiro, zīmējums neietilpst lapā. Tāpēc vienību izvēlas pēc
skaitļiem, nevis otrādi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, plakne)

TEMA = "Kā izvēlēties vienību uz ass?"

MERKIS = ("Mācīsimies izvēlēties asu vienības atbilstoši lielumu "
          "skaitliskajām vērtībām.")

SATURS = [
    Sakums("Viena rūtiņa - cik eiro?",
           zimejums=plakne(punkti=[(2, 4, ""), (4, 8, "")], no_x=0,
                           lidz_x=6, no_y=0, lidz_y=10, solis=2,
                           virsraksts="Uz y ass viena iedaļa ir 2 €"),
           paraksts="Ja iedaļa būtu 1 €, zīmējums būtu divreiz garāks.",
           fakti=["Uz abām asīm vienība var būt dažāda.",
                  "To izvēlas pēc lielākā skaitļa.",
                  "Bet uz vienas ass tā visur ir viena un tā pati."]),

    Doma("Vienību izvēlas pēc lielākā skaitļa",
         "Asu vienību izvēlas tā, lai lielākais lielums ietilptu zīmējumā un "
         "lai skaitļi iekristu uz iedaļām.",
         soli=[
             "Atrodi lielāko skaitli, kas jāattēlo.",
             "Izlem, cik iedaļu tev ir vietas.",
             "Dali lielāko skaitli ar iedaļu skaitu.",
             "Noapaļo iegūto līdz ērtam skaitlim: 1, 2, 5, 10, 50 vai 100.",
             "Uz vienas ass visas iedaļas ir vienādas.",
         ],
         pieze="Abām asīm nav jābūt vienādām vienībām: uz x ass var būt "
               "kilogrami, uz y ass - eiro. Bet vienas ass ietvaros iedaļa "
               "nedrīkst mainīties."),

    Paraugs("Cenas līdz 10 eiro",
            uzd="Uz y ass jāattēlo cenas līdz 10 €. Vietas ir 5 iedaļas. "
                "Cik liela ir viena iedaļa?",
            soli=[
                ("Lielākā cena ir 10 €",
                 "Augstākais punkts."),
                ("Iedaļu ir 5",
                 "Tik ir vietas."),
                ("10 : 5 = 2",
                 "Viena iedaļa ir 2 €."),
                ("Iedaļas: 2, 4, 6, 8 un 10",
                 "Visi skaitļi iekrīt uz iedaļām."),
            ],
            atbilde="Viena iedaļa ir 2 €"),

    Ievadi("Izvēlies vienību", [
        {"jaut": "Lielākais skaitlis 10, iedaļu 5. Cik liela ir viena "
                 "iedaļa?",
         "atb": ["2"], "padoms": "10 : 5."},
        {"jaut": "Lielākais skaitlis 50, iedaļu 5. Cik liela ir viena "
                 "iedaļa?",
         "atb": ["10"], "padoms": "50 : 5."},
        {"jaut": "Lielākais skaitlis 100, iedaļu 10. Cik liela ir viena "
                 "iedaļa?",
         "atb": ["10"], "padoms": "100 : 10."},
        {"jaut": "Lielākais skaitlis 250, iedaļu 5. Cik liela ir viena "
                 "iedaļa?",
         "atb": ["50"], "padoms": "250 : 5."},
        {"jaut": "Iedaļa ir 2 €. Cik eiro ir 4 iedaļas?",
         "atb": ["8"], "padoms": "2 · 4."},
        {"jaut": "Iedaļa ir 10 km. Cik kilometru ir 7 iedaļas?",
         "atb": ["70"], "padoms": "10 · 7."},
        {"jaut": "Punkts ir 3 iedaļas augstu, iedaļa ir 5 €. Cik eiro?",
         "atb": ["15"], "padoms": "5 · 3."},
        {"jaut": "Punkts ir 25 €, iedaļa ir 5 €. Cik iedaļas augstu tas ir?",
         "atb": ["5"], "padoms": "25 : 5."},
    ], pamats=4,
        ievads="Dali lielāko skaitli ar iedaļu skaitu un noapaļo līdz ērtam."),

    Zimejums("Viena ass, vienādas iedaļas",
             plakne(punkti=[(1, 2, ""), (2, 4, ""), (3, 6, "")], no_x=0,
                    lidz_x=5, no_y=0, lidz_y=8, solis=2,
                    virsraksts="Katra iedaļa uz y ass ir 2"),
             paskaidro="Visas iedaļas uz vienas ass ir vienādas - tikai tad "
                       "punktus var salīdzināt savā starpā.",
             ievads="Vienādas iedaļas ir galvenais noteikums."),

    Varianti("Kāda vienība te der?", [
        {"jaut": "Kā izvēlas asu vienību?",
         "opcijas": ["Pēc lielākā attēlojamā skaitļa", "Vienmēr 1",
                     "Pēc lapas platuma", "Kā sanāk"],
         "pareizi": 0,
         "padoms": "Lai viss ietilptu."},
        {"jaut": "Lielākais skaitlis 250, iedaļu 5. Cik liela ir iedaļa?",
         "opcijas": ["50", "25", "5", "100"],
         "pareizi": 0,
         "padoms": "250 : 5."},
        {"jaut": "Vai abām asīm jābūt vienādām vienībām?",
         "opcijas": ["Nav, tās var atšķirties", "Jā, vienmēr",
                     "Tikai kartēm", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Kilogrami un eiro."},
        {"jaut": "Vai vienas ass iedaļa drīkst mainīties?",
         "opcijas": ["Nedrīkst", "Drīkst", "Drīkst beigās",
                     "Drīkst, ja skaitļi ir lieli"],
         "pareizi": 0,
         "padoms": "Citādi punktus salīdzināt nevar."},
        {"jaut": "Punkts ir 3 iedaļas augstu, iedaļa ir 5 €. Cik eiro?",
         "opcijas": ["15 €", "8 €", "5 €", "3 €"],
         "pareizi": 0,
         "padoms": "5 · 3."},
        {"jaut": "Kāpēc iedaļu noapaļo līdz 1, 2, 5 vai 10?",
         "opcijas": ["Tā vieglāk nolasīt", "Tā zīmējums ir mazāks",
                     "Tā prasa likums", "Tas nav vajadzīgs"],
         "pareizi": 0,
         "padoms": "Skaitļi iekrīt uz iedaļām."},
    ], pamats=4),

    Pasaule("Kā attēlot klases rezultātus?",
            Ievadi("", [
                {"jaut": "Lielākais rezultāts ir 20 punkti, iedaļu 5. Cik "
                         "liela ir iedaļa?",
                 "atb": ["4"], "padoms": "20 : 5."},
                {"jaut": "Skolēns ieguva 12 punktus. Cik iedaļas augstu tas "
                         "ir?",
                 "atb": ["3"], "padoms": "12 : 4."},
                {"jaut": "Lielākais rezultāts 100 punkti, iedaļu 10. Cik "
                         "liela ir iedaļa?",
                 "atb": ["10"], "padoms": "100 : 10."},
                {"jaut": "Skolēns ieguva 70 punktus. Cik iedaļas augstu?",
                 "atb": ["7"], "padoms": "70 : 10."},
            ]),
            pavediens="skola",
            konteksts="Klases rezultātu grafiks jāsaliek vienā lapā, tāpēc "
                      "iedaļu izvēlas pēc labākā rezultāta.",
            kapec="Pareizi izvēlēta vienība padara grafiku salasāmu."),

    Kopsavilkums([
        "Izvēlos asu vienību pēc lielākā attēlojamā skaitļa.",
        "Noapaļoju iedaļu līdz ērtam skaitlim.",
        "Zinu, ka uz vienas ass visas iedaļas ir vienādas.",
        "Zinu, ka abām asīm vienības var atšķirties.",
    ]),

    Majas([
        "Izvēlies iedaļu, ja lielākais skaitlis ir 60 un iedaļu ir 6.",
        "Uzzīmē asi ar šo iedaļu un atzīmē uz tās 24.",
        "Padomā, kāda iedaļa derētu skaitļiem līdz 1000.",
    ]),
]
