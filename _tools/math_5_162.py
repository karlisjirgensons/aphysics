# -*- coding: utf-8 -*-
"""5. klase, 162. stunda: «Kā salīdzināt divas cenas?»

Tas pats slīpums, tikai tagad uz asīm ir kilogrami un eiro. Ja divu veikalu
cenas attēlo vienā plaknē, lētākā prece ir tā, kuras līnija ir zemāk - un
tas ir redzams uzreiz, bez rēķina par katru kilogramu atsevišķi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, plakne)

TEMA = "Kā salīdzināt divas cenas?"

MERKIS = ("Mācīsimies salīdzināt divus pirkuma notikumus pēc to grafiskā "
          "attēla.")

SATURS = [
    Sakums("Divas līnijas, divi veikali",
           zimejums=plakne(lauzta=[(0, 0), (1, 3), (2, 6), (3, 9)], no_x=0,
                           lidz_x=4, no_y=0, lidz_y=12, solis=3,
                           virsraksts="Pirmais veikals: 3 € par kg"),
           paraksts="Otrā veikala līnija ar 2 € par kg būtu zemāk.",
           fakti=["Uz x ass ir kilogrami, uz y ass - eiro.",
                  "Stāvāka līnija nozīmē dārgāku preci.",
                  "Zemāk esošā līnija ir lētākais veikals."]),

    Doma("Zemāka līnija - lētāka prece",
         "Ja divu veikalu cenas attēlotas vienā plaknē, lētāks ir tas, kura "
         "līnija tajā pašā daudzumā atrodas zemāk.",
         soli=[
             "Pārbaudi, vai abām līnijām ir vienādas asis.",
             "Izvēlies vienu daudzumu uz x ass.",
             "Salīdzini, cik augstu tajā vietā ir katra līnija.",
             "Zemākā līnija ir lētākā prece.",
             "Aprēķini starpību, ja vajag precīzu atbildi.",
         ],
         pieze="Abas līnijas sākas punktā (0; 0): ja nepērk neko, nemaksā "
               "neko. Tieši tāpēc cenu grafiki vienmēr iziet no "
               "sākumpunkta."),

    Paraugs("3 € vai 2 € par kilogramu?",
            uzd="Cik maksā 4 kg katrā veikalā un kur ir lētāk?",
            soli=[
                ("Pirmais: 3 · 4 = 12 (€)",
                 "Dārgākais veikals."),
                ("Otrais: 2 · 4 = 8 (€)",
                 "Lētākais veikals."),
                ("12 - 8 = 4 (€)",
                 "Ietaupījums."),
                ("Otrā veikala līnija ir zemāk",
                 "To redz bez rēķina."),
            ],
            atbilde="Otrajā veikalā ir lētāk - ietaupījums 4 €"),

    Ievadi("Salīdzini cenas", [
        {"jaut": "1 kg maksā 3 €. Cik maksā 4 kg?",
         "atb": ["12"], "padoms": "3 · 4."},
        {"jaut": "Citā veikalā 1 kg maksā 2 €. Cik maksā 4 kg?",
         "atb": ["8"], "padoms": "2 · 4."},
        {"jaut": "Cik eiro ir starpība?",
         "atb": ["4"], "padoms": "12 - 8."},
        {"jaut": "Cik maksā 6 kg pirmajā veikalā?",
         "atb": ["18"], "padoms": "3 · 6."},
        {"jaut": "Cik maksā 6 kg otrajā veikalā?",
         "atb": ["12"], "padoms": "2 · 6."},
        {"jaut": "Cik kilogramu var nopirkt par 12 € otrajā veikalā?",
         "atb": ["6"], "padoms": "12 : 2."},
        {"jaut": "Cik kilogramu var nopirkt par 12 € pirmajā veikalā?",
         "atb": ["4"], "padoms": "12 : 3."},
        {"jaut": "Kurā veikalā par 12 € dabū vairāk? Ieraksti kilogramus.",
         "atb": ["6"], "padoms": "6 kg pret 4 kg."},
    ], pamats=4,
        ievads="Salīdzini abus veikalus vienā un tajā pašā daudzumā."),

    Zimejums("Lētākā veikala līnija",
             plakne(lauzta=[(0, 0), (1, 2), (2, 4), (3, 6), (4, 8)], no_x=0,
                    lidz_x=5, no_y=0, lidz_y=12, solis=3,
                    virsraksts="Otrais veikals: 2 € par kg"),
             paskaidro="Šī līnija ceļas lēnāk nekā pirmā, tāpēc jebkurā "
                       "daudzumā tā atrodas zemāk - un prece ir lētāka.",
             ievads="Tā pati plakne, otrs veikals."),

    Varianti("Kur ir lētāk?", [
        {"jaut": "Kura līnija rāda lētāku preci?",
         "opcijas": ["Zemākā", "Stāvākā", "Garākā", "Īsākā"],
         "pareizi": 0,
         "padoms": "Mazāka samaksa par to pašu daudzumu."},
        {"jaut": "1 kg maksā 3 €. Cik maksā 4 kg?",
         "opcijas": ["12 €", "7 €", "9 €", "34 €"],
         "pareizi": 0,
         "padoms": "3 · 4."},
        {"jaut": "Kāpēc abas līnijas sākas punktā (0; 0)?",
         "opcijas": ["Ja nepērk neko, nemaksā neko", "Tā ir tradīcija",
                     "Tā ir kļūda", "Lai būtu skaisti"],
         "pareizi": 0,
         "padoms": "Nulle kilogramu - nulle eiro."},
        {"jaut": "Par 12 € pirmajā veikalā dabū 4 kg, otrajā 6 kg. Kurš ir "
                 "izdevīgāks?",
         "opcijas": ["Otrais", "Pirmais", "Vienādi", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Vairāk par to pašu naudu."},
        {"jaut": "Kad divas cenu līnijas var salīdzināt?",
         "opcijas": ["Ja tās ir vienā plaknē ar vienādām asīm", "Vienmēr",
                     "Ja cenas ir apaļas", "Nekad"],
         "pareizi": 0,
         "padoms": "Vienāds mērogs."},
        {"jaut": "Stāvāka cenu līnija nozīmē...",
         "opcijas": ["Dārgāku preci", "Lētāku preci", "Lielāku daudzumu",
                     "Neko"],
         "pareizi": 0,
         "padoms": "Straujāk aug samaksa."},
    ], pamats=4),

    Pasaule("Kurā veikalā pirkt?",
            Ievadi("", [
                {"jaut": "Pirmajā veikalā 1 kg maksā 3 €. Cik maksā 5 kg?",
                 "atb": ["15"], "padoms": "3 · 5."},
                {"jaut": "Otrajā veikalā 1 kg maksā 2 €. Cik maksā 5 kg?",
                 "atb": ["10"], "padoms": "2 · 5."},
                {"jaut": "Cik eiro ietaupa, pērkot otrajā?",
                 "atb": ["5"], "padoms": "15 - 10."},
                {"jaut": "Cik kilogramu var nopirkt par 30 € otrajā veikalā?",
                 "atb": ["15"], "padoms": "30 : 2."},
            ]),
            pavediens="veikals",
            konteksts="Divu veikalu cenu grafiki vienā plaknē parāda ne "
                      "tikai to, kur ir lētāk, bet arī cik daudz lētāk.",
            kapec="Ietaupījums aug līdz ar pirkuma daudzumu."),

    Kopsavilkums([
        "Salīdzinu divus pirkumus pēc to grafiskā attēla.",
        "Zinu, ka zemāka līnija nozīmē lētāku preci.",
        "Aprēķinu ietaupījumu konkrētam daudzumam.",
        "Zinu, kāpēc cenu grafiks sākas punktā (0; 0).",
    ]),

    Majas([
        "Uzzīmē vienā plaknē divas cenas: 4 € un 2 € par kilogramu.",
        "Nolasi, cik maksā 3 kg katrā gadījumā.",
        "Aprēķini ietaupījumu, pērkot 5 kg.",
    ]),
]
