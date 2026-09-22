# -*- coding: utf-8 -*-
"""5. klase, 161. stunda: «Ko stāsta grafika slīpums?»

Divas līnijas vienā plaknē, un jautājums ir tikai viens: kura ir stāvāka.
Skolēnam tas ir pirmais gadījums, kad no grafika izskata var izdarīt
secinājumu, neko nenolasot un nerēķinot. Tāpēc stunda beidzas ar teikumu,
ne ar skaitli.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, plakne)

TEMA = "Ko stāsta grafika slīpums?"

MERKIS = ("Mācīsimies salīdzināt divas kustības vienā koordinātu plaknē un "
          "secināt, kurš pārvietojas ātrāk.")

SATURS = [
    Sakums("Divas līnijas, divi ātrumi",
           zimejums=plakne(lauzta=[(0, 0), (1, 60), (2, 120), (3, 180)],
                           punkti=[(3, 90, "B")], no_x=0, lidz_x=4, no_y=0,
                           lidz_y=200, solis=50,
                           virsraksts="Auto un velosipēds"),
           paraksts="Stāvākā līnija ir ātrākajam braucējam.",
           fakti=["Abas kustības sākas punktā (0; 0).",
                  "Pēc trim stundām viens ir 180 km, otrs 90 km.",
                  "Ātrākajam līnija ceļas stāvāk."]),

    Doma("Stāvāka līnija - lielāks ātrums",
         "Ja divas vienmērīgas kustības attēlotas vienā plaknē, ātrāk "
         "pārvietojas tas, kura līnija ir stāvāka.",
         soli=[
             "Pārliecinies, ka abām līnijām ir vienas un tās pašas asis.",
             "Izvēlies vienu laika brīdi uz x ass.",
             "Salīdzini, cik augstu tajā brīdī ir katra līnija.",
             "Augstāk esošā ir nobraukusi vairāk.",
             "Formulē secinājumu vārdiem.",
         ],
         pieze="Salīdzināt drīkst tikai tad, ja abas līnijas ir vienā "
               "plaknē ar vienādām asu vienībām. Uz diviem atsevišķiem "
               "zīmējumiem stāvāka līnija var nozīmēt mazāku ātrumu."),

    Paraugs("Kurš brauc ātrāk?",
            uzd="Pēc 3 stundām viens ir nobraucis 180 km, otrs 90 km. Kurš "
                "brauc ātrāk?",
            soli=[
                ("Pirmais: 180 : 3 = 60 (km stundā)",
                 "Pirmā ātrums."),
                ("Otrais: 90 : 3 = 30 (km stundā)",
                 "Otrā ātrums."),
                ("60 > 30",
                 "Pirmais brauc ātrāk."),
                ("Grafikā pirmā līnija ir stāvāka",
                 "To var redzēt bez rēķina."),
            ],
            atbilde="Ātrāk brauc pirmais - 60 km stundā"),

    Ievadi("Salīdzini ātrumus", [
        {"jaut": "3 stundās nobraukti 180 km. Cik kilometru stundā?",
         "atb": ["60"], "padoms": "180 : 3."},
        {"jaut": "3 stundās nobraukti 90 km. Cik kilometru stundā?",
         "atb": ["30"], "padoms": "90 : 3."},
        {"jaut": "Kurš ātrums ir lielāks - 60 vai 30 km stundā? Ieraksti "
                 "skaitli.",
         "atb": ["60"], "padoms": "Lielāks skaitlis."},
        {"jaut": "2 stundās nobraukti 100 km. Cik kilometru stundā?",
         "atb": ["50"], "padoms": "100 : 2."},
        {"jaut": "4 stundās nobraukti 100 km. Cik kilometru stundā?",
         "atb": ["25"], "padoms": "100 : 4."},
        {"jaut": "Kurš nobrauca vairāk 2 stundās - ar 50 vai ar 25 km "
                 "stundā? Ieraksti kilometrus.",
         "atb": ["100"], "padoms": "50 · 2."},
        {"jaut": "5 stundās nobraukti 400 km. Cik kilometru stundā?",
         "atb": ["80"], "padoms": "400 : 5."},
        {"jaut": "Kura līnija ir stāvāka - ar ātrumu 80 vai 60? Ieraksti "
                 "skaitli.",
         "atb": ["80"], "padoms": "Lielāks ātrums."},
    ], pamats=4,
        ievads="Ātrumu iegūst, ceļu dalot ar laiku."),

    Zimejums("Lēnākā kustība",
             plakne(lauzta=[(0, 0), (1, 30), (2, 60), (3, 90)], no_x=0,
                    lidz_x=4, no_y=0, lidz_y=200, solis=50,
                    virsraksts="30 km stundā"),
             paskaidro="Šī līnija ceļas daudz lēnāk nekā stundas sākuma "
                       "līnija - tāpēc arī ātrums ir divreiz mazāks.",
             ievads="Tā pati plakne, cita kustība."),

    Varianti("Kura līnija ir ātrākā?", [
        {"jaut": "Kura līnija rāda lielāku ātrumu?",
         "opcijas": ["Stāvākā", "Lēzenākā", "Garākā", "Īsākā"],
         "pareizi": 0,
         "padoms": "Vairāk ceļa tajā pašā laikā."},
        {"jaut": "3 stundās 180 km. Cik kilometru stundā?",
         "opcijas": ["60", "180", "540", "3"],
         "pareizi": 0,
         "padoms": "180 : 3."},
        {"jaut": "Kad divas līnijas var salīdzināt?",
         "opcijas": ["Ja tās ir vienā plaknē ar vienādām asīm", "Vienmēr",
                     "Ja tās ir vienādi garas", "Nekad"],
         "pareizi": 0,
         "padoms": "Vienāds mērogs."},
        {"jaut": "Abas līnijas sākas punktā (0; 0). Ko tas nozīmē?",
         "opcijas": ["Abi sāka vienlaikus no vienas vietas",
                     "Abi brauc vienādi ātri",
                     "Grafiks ir nepareizs",
                     "Neko"],
         "pareizi": 0,
         "padoms": "Sākumā ceļš ir nulle."},
        {"jaut": "Viena līnija pēc 2 stundām ir 100 km, otra 60 km. Kura ir "
                 "stāvāka?",
         "opcijas": ["Pirmā", "Otrā", "Vienādas", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Vairāk ceļa tajā pašā laikā."},
        {"jaut": "Ar ko beidzas salīdzinājums?",
         "opcijas": ["Ar teikumu, kurš brauc ātrāk", "Ar skaitli",
                     "Ar grafiku", "Ar tabulu"],
         "pareizi": 0,
         "padoms": "Secinājums vārdiem."},
    ], pamats=4),

    Pasaule("Kurš būs galā pirmais?",
            Ievadi("", [
                {"jaut": "Auto brauc 80 km stundā, autobuss 60 km stundā. "
                         "Cik kilometru auto nobrauc 3 stundās?",
                 "atb": ["240"], "padoms": "80 · 3."},
                {"jaut": "Cik kilometru autobuss nobrauc 3 stundās?",
                 "atb": ["180"], "padoms": "60 · 3."},
                {"jaut": "Kurš nobrauca vairāk? Ieraksti kilometrus.",
                 "atb": ["240"], "padoms": "240 > 180."},
                {"jaut": "Ceļš ir 240 km. Cik stundas brauks autobuss? "
                         "Ieraksti skaitli.",
                 "atb": ["4"], "padoms": "240 : 60."},
            ]),
            pavediens="celojums",
            konteksts="Divu transporta veidu grafiki vienā plaknē uzreiz "
                      "parāda, kurš būs galā pirmais.",
            kapec="Slīpums pasaka ātrumu, arī neko nerēķinot."),

    Kopsavilkums([
        "Salīdzinu divas kustības vienā koordinātu plaknē.",
        "Secinu, kurš pārvietojas ātrāk, pēc līnijas slīpuma.",
        "Aprēķinu ātrumu, ceļu dalot ar laiku.",
        "Formulēju secinājumu pilnā teikumā.",
    ]),

    Majas([
        "Uzzīmē vienā plaknē divas kustības: 40 km stundā un 20 km stundā.",
        "Pieraksti, kura līnija ir stāvāka un kāpēc.",
        "Nolasi, cik kilometru katrs nobrauc 3 stundās.",
    ]),
]
