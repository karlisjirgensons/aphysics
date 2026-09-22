# -*- coding: utf-8 -*-
"""5. klase, 163. stunda: «Ātrāk rēķināt vai nolasīt?»

Mikrotemata noslēgums, un tas ir izvēles uzdevums. Grafiks ir ātrs, bet
neprecīzs; rēķins ir precīzs, bet lēnāks. Prasme izvēlēties starp tiem ir
tikpat svarīga kā abas atsevišķi, un to var pamatot ar vienu jautājumu: cik
precīza atbilde vajadzīga.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, plakne)

TEMA = "Ātrāk rēķināt vai nolasīt?"

MERKIS = ("Mācīsimies izvērtēt, kad nezināmo lielumu ātrāk noteikt no "
          "grafika un kad - aprēķinot.")

SATURS = [
    Sakums("Divi ceļi uz vienu atbildi",
           zimejums=plakne(lauzta=[(0, 0), (1, 2), (2, 4), (3, 6), (4, 8)],
                           no_x=0, lidz_x=5, no_y=0, lidz_y=10, solis=2,
                           virsraksts="2 € par kilogramu"),
           paraksts="3 kg var nolasīt no grafika vai izrēķināt: 2 · 3.",
           fakti=["Grafiks dod atbildi ātri, bet aptuveni.",
                  "Rēķins dod precīzu atbildi, bet lēnāk.",
                  "Izvēle atkarīga no tā, cik precīzi vajag."]),

    Doma("Izvēlies pēc vajadzīgās precizitātes",
         "No grafika nolasa tad, kad pietiek ar aptuvenu atbildi vai kad "
         "vērtība iekrīt uz iedaļas; rēķina tad, kad vajadzīga precizitāte.",
         soli=[
             "Paskaties, vai vajadzīgā vērtība iekrīt uz iedaļas.",
             "Ja iekrīt - nolasi no grafika.",
             "Ja nav starp iedaļām - labāk rēķini.",
             "Ja vajag tikai novērtējumu - pietiek ar grafiku.",
             "Pamato savu izvēli vienā teikumā.",
         ],
         pieze="Grafika precizitāte ir tik liela, cik smalkas ir iedaļas. "
               "Ja viena iedaļa ir 2 €, tad 7 € no tā nolasīt nevar - "
               "jārēķina."),

    Paraugs("Cik maksā 3 kg un cik 3,5 kg?",
            uzd="Kurā gadījumā ērtāk nolasīt, kurā rēķināt?",
            soli=[
                ("3 kg iekrīt uz iedaļas",
                 "Nolasa no grafika: 6 €."),
                ("3,5 kg ir starp iedaļām",
                 "Grafikā to precīzi nenolasīs."),
                ("2 · 3,5 = 7 (€)",
                 "Rēķins dod precīzu atbildi."),
                ("Izvēle atkarīga no skaitļa",
                 "Uz iedaļas - nolasa, starp tām - rēķina."),
            ],
            atbilde="3 kg nolasa, 3,5 kg rēķina"),

    Ievadi("Nolasīt vai rēķināt?", [
        {"jaut": "1 kg maksā 2 €. Cik maksā 3 kg?",
         "atb": ["6"], "padoms": "2 · 3."},
        {"jaut": "Cik maksā 3,5 kg?",
         "atb": ["7"], "padoms": "2 · 3,5."},
        {"jaut": "Cik maksā 10 kg?",
         "atb": ["20"], "padoms": "2 · 10."},
        {"jaut": "Grafikā redzami tikai 5 kg. Vai 10 kg var nolasīt? Raksti "
                 "«jā» vai «nē».",
         "atb": ["nē", "ne"], "padoms": "Tas ir ārpus zīmējuma."},
        {"jaut": "Iedaļa uz y ass ir 2 €. Vai 7 € var precīzi nolasīt?",
         "atb": ["nē", "ne"], "padoms": "Starp iedaļām."},
        {"jaut": "Vai 6 € var precīzi nolasīt, ja iedaļa ir 2 €?",
         "atb": ["jā", "ja"], "padoms": "6 iekrīt uz iedaļas."},
        {"jaut": "Cik kilogramu var nopirkt par 20 €?",
         "atb": ["10"], "padoms": "20 : 2."},
        {"jaut": "Cik maksā 7 kg?",
         "atb": ["14"], "padoms": "2 · 7."},
    ], pamats=4,
        ievads="Vispirms paskaties, vai skaitlis iekrīt uz iedaļas."),

    Zimejums("Kad grafiks nepietiek",
             plakne(lauzta=[(0, 0), (1, 2), (2, 4), (3, 6), (4, 8)],
                    punkti=[(3, 6, "")], no_x=0, lidz_x=5, no_y=0,
                    lidz_y=10, solis=2, virsraksts="Iedaļa ir 2 €"),
             paskaidro="Uz iedaļām esošās vērtības nolasa precīzi; starp "
                       "tām esošās var tikai novērtēt. Tur palīdz rēķins.",
             ievads="Grafika precizitāte ir tā iedaļu smalkums."),

    Varianti("Kurš ceļš te ātrāks?", [
        {"jaut": "Kad ērtāk nolasīt no grafika?",
         "opcijas": ["Kad vērtība iekrīt uz iedaļas", "Vienmēr",
                     "Kad skaitļi ir lieli", "Nekad"],
         "pareizi": 0,
         "padoms": "Tad atbilde ir precīza."},
        {"jaut": "Kad labāk rēķināt?",
         "opcijas": ["Kad vajadzīga precīza atbilde", "Vienmēr",
                     "Kad grafiks ir liels", "Nekad"],
         "pareizi": 0,
         "padoms": "Starp iedaļām."},
        {"jaut": "Iedaļa ir 2 €. Vai 7 € var precīzi nolasīt?",
         "opcijas": ["Nevar", "Var", "Var, ja uzmanīgi", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Starp 6 un 8."},
        {"jaut": "Grafikā redzami 5 kg. Cik maksā 10 kg?",
         "opcijas": ["Jāizrēķina: 20 €", "Jānolasa no grafika", "10 €",
                     "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Ārpus zīmējuma."},
        {"jaut": "No kā atkarīga grafika precizitāte?",
         "opcijas": ["No iedaļu smalkuma", "No līnijas garuma",
                     "No lapas krāsas", "Ne no kā"],
         "pareizi": 0,
         "padoms": "Sīkākas iedaļas - precīzāka nolasīšana."},
        {"jaut": "Kas jāpieraksta pie izvēles?",
         "opcijas": ["Pamatojums", "Tikai atbilde", "Grafiks", "Nekas"],
         "pareizi": 0,
         "padoms": "Kāpēc tieši šis ceļš."},
    ], pamats=4),

    Pasaule("Pie kases vai mājās?",
            Ievadi("", [
                {"jaut": "1 kg maksā 2 €. Cik maksā 4 kg?",
                 "atb": ["8"], "padoms": "2 · 4."},
                {"jaut": "Cik maksā 4,5 kg?",
                 "atb": ["9"], "padoms": "2 · 4,5."},
                {"jaut": "Cik kilogramu var nopirkt par 15 €? Ieraksti "
                         "skaitli.",
                 "atb": ["7,5"], "padoms": "15 : 2."},
                {"jaut": "Vai šo vērtību var precīzi nolasīt no grafika ar "
                         "iedaļu 1 kg? Raksti «jā» vai «nē».",
                 "atb": ["nē", "ne"], "padoms": "7,5 ir starp iedaļām."},
            ]),
            pavediens="veikals",
            konteksts="Veikalā ātrs novērtējums der izvēlei, bet kasē summa "
                      "jāzina precīzi.",
            kapec="Katram uzdevumam savs ceļš - grafiks vai rēķins."),

    Kopsavilkums([
        "Izvērtēju, kad vērtību ātrāk nolasīt no grafika.",
        "Izvērtēju, kad vajadzīgs precīzs rēķins.",
        "Zinu, ka grafika precizitāti nosaka iedaļu smalkums.",
        "Pamatoju savu izvēli vienā teikumā.",
    ]),

    Majas([
        "Uzzīmē grafiku ar cenu 3 € par kilogramu.",
        "Nolasi no tā 2 kg cenu un izrēķini 2,5 kg cenu.",
        "Pieraksti, kurā gadījumā grafiks bija ērtāks.",
    ]),
]
