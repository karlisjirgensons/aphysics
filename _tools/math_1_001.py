# -*- coding: utf-8 -*-
"""1. klase, 1. stunda: «Cik logu ir mūsu klasē?»

Pirmā matemātikas stunda gadā. Skolēns jau prot skaitīt vārdus pēc kārtas,
tāpēc te mācās to, kas ir zem skaitīšanas: katrai lietai - viens skaitļa
vārds, un pēdējais pateiktais vārds ir atbilde uz jautājumu «cik?». Otrā
stundas puse to pārceļ uz modeli - tik ripiņu, cik lietu -, jo no šī modeļa
aug viss tālākais darbs ar skaitļiem.

Šajā failā ir tikai saturs; kā tas izskatās lapā, zina math_bloki.py un
math_lapa.py (SRP).
"""

from math_saturs import (Doma, Izvele, Josla, Kopsavilkums, Majas, Modelis,
                         Pasaule, Sakums)

TEMA = "Cik logu ir mūsu klasē?"

MERKIS = ("Šodien iemācīsimies saskaitīt lietas ap sevi un parādīt ar "
          "ripiņām, cik to ir.")

SATURS = [
    Sakums("Vai visiem pietiks krēslu?",
           fakti=["Rīt klasē nāks ciemiņi.",
                  "Lai to zinātu, jāatbild uz vienu vārdu: cik?"]),

    Doma("Skaitīt nozīmē: katrai lietai savs vārds",
         "Pēdējais skaitlis, ko pateici, pasaka, cik ir kopā.",
         soli=[
             "Pieskaries vienai lietai un saki: viens.",
             "Pieskaries nākamajai un saki: divi.",
             "Nevienu neizlaid un nevienu neskaiti divreiz.",
             "Pēdējais pateiktais skaitlis ir atbilde uz jautājumu «cik?».",
         ],
         pieze="Ja sāksi skaitīt no otra gala, atbilde būs tā pati - lietu "
               "skaits no skaitīšanas kārtības nemainās."),

    Josla("Skaitļu josla no 0 līdz 10", lidz=10,
          ievads="Pieskaries skaitlim un paskaties, cik daudz tas ir. Jo "
                 "tālāk pa joslu, jo vairāk ripiņu."),

    Doma("Viena ripiņa - viena lieta",
         "Paņem tik ripiņu, cik ir lietu; tad ripiņas stāsta to pašu skaitli.",
         soli=[
             "Par katru lietu ieliec paplātē vienu ripiņu.",
             "Kad lietas beidzas, beidz likt arī ripiņas.",
             "Tagad ripiņu ir tikpat, cik lietu.",
         ],
         pieze="Tā dara matemātiķi: lielo un smago aizstāj ar mazu modeli. "
               "Logu nevar paņemt rokā, ripiņu var."),

    # Pirmās četras izdara visi; pārējās lapa piedāvā pa divām tiem, kas
    # tiek galā ātrāk.
    Modelis("Noliec tikpat ripiņu", [
        {"ikona": "zimulis", "skaits": 4,
         "jaut": "Noliec tik ripiņu, cik ir zīmuļu."},
        {"ikona": "gramata", "skaits": 3,
         "jaut": "Noliec tik ripiņu, cik ir grāmatu."},
        {"ikona": "abols", "skaits": 7,
         "jaut": "Noliec tik ripiņu, cik ir ābolu."},
        {"ikona": "bumba", "skaits": 9,
         "jaut": "Noliec tik ripiņu, cik ir bumbu."},
        {"ikona": "soma", "skaits": 6,
         "jaut": "Noliec tik ripiņu, cik ir somu."},
        {"ikona": "puke", "skaits": 5,
         "jaut": "Noliec tik ripiņu, cik ir puķu."},
        {"ikona": "karote", "skaits": 8,
         "jaut": "Noliec tik ripiņu, cik ir karošu."},
        {"ikona": "logs", "skaits": 10,
         "jaut": "Noliec tik ripiņu, cik ir logu."},
    ], pamats=4,
        ievads="Vispirms saskaiti lietas. Tad spied «Noliec ripiņu», līdz "
               "paplātē to ir tikpat, un pārbaudi."),

    Izvele("Cik ir?", [
        {"ikona": "abols", "skaits": 6, "jaut": "Cik ābolu ir grozā?"},
        {"ikona": "bumba", "skaits": 4, "jaut": "Cik bumbu ir sporta zālē?"},
        {"ikona": "karote", "skaits": 9, "jaut": "Cik karošu ir uz galda?"},
        {"ikona": "zimulis", "skaits": 7, "jaut": "Cik zīmuļu ir penālī?"},
        {"ikona": "logs", "skaits": 10, "jaut": "Cik logu ir gaitenī?"},
        {"ikona": "kresls", "skaits": 5, "jaut": "Cik krēslu ir ap galdu?"},
        {"ikona": "gramata", "skaits": 2, "jaut": "Cik grāmatu ir somā?"},
        {"ikona": "puke", "skaits": 8, "jaut": "Cik puķu ir dobē?"},
    ], pamats=4, lidz=10,
        ievads="Saskaiti un pieskaries pareizajam skaitlim."),

    Pasaule("Cik krēslu vajag ciemiņiem?",
            Izvele("", [
                {"ikona": "kresls", "skaits": 5,
                 "jaut": "Cik krēslu ir sagatavots?"},
                {"ikona": "karote", "skaits": 7,
                 "jaut": "Cik karošu ir uz galda?"},
                {"ikona": "soma", "skaits": 4,
                 "jaut": "Cik somu atnesa ciemiņi?"},
                {"ikona": "abols", "skaits": 8,
                 "jaut": "Cik ābolu ir groziņā?"},
            ], lidz=10),
            pavediens="skola",
            konteksts="Rīt klasē nāks ciemiņi, un viss jāsagatavo pa vienam.",
            kapec="Kad zini, cik ir, vari pateikt, vai visiem pietiks."),

    Kopsavilkums([
        "Saskaitu lietas līdz 10 un nevienu neizlaižu.",
        "Zinu, ka pēdējais pateiktais skaitlis pasaka, cik ir kopā.",
        "Protu nolikt tikpat ripiņu, cik ir lietu.",
    ]),

    Majas([
        "Saskaiti, cik durvju ir jūsu mājoklī.",
        "Saskaiti, cik krēslu ir ap virtuves galdu.",
        "Noliec tik karošu, cik cilvēku sēdīsies pie galda. Vai sanāca "
        "tikpat?",
        "Atrodi mājās kaut ko, kā ir tieši 10.",
    ], ievads="Rādi ar pirkstu un skaiti skaļi - tāpat kā stundā."),
]
