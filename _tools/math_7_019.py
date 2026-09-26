# -*- coding: utf-8 -*-
"""7. klase, 19. stunda: «Kas ir ģeometriska figūra?»

Ģeometrijā figūra ir punktu kopa - tā pati kopa, ko mācījāmies pirmajā
tematā. Nogrieznis, riņķa līnija un trijstūris ir punktu kopas ar noteiktu
īpašību, un tāpēc par figūrām var runāt ar kopu valodu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, geometrija,
                         rinkis)

TEMA = "Kas ir ģeometriska figūra?"

MERKIS = ("Sapratīsim, ka ģeometriska figūra ir punktu kopa, un aprakstīsim "
          "figūras kā kopas.")

SATURS = [
    Sakums("Ekrāns zīmē figūras no punktiem",
           zimejums=rinkis(radiuss="r = 3 cm"),
           paraksts="Riņķa līnija - visi punkti 3 cm attālumā no centra.",
           fakti=["Telefona ekrānā ir miljoniem punktu - pikseļu.",
                  "Katrs attēls ir izgaismoto pikseļu kopa.",
                  "Ģeometrijā figūra arī ir punktu kopa - tikai bezgalīga."]),

    Doma("Figūra ir punktu kopa",
         "Jebkura punktu kopa plaknē ir ģeometriska figūra. Figūru nosaka "
         "tas, kuri punkti tai pieder un kuri - nepieder.",
         soli=[
             "Punkts ir vienkāršākā figūra - viena punkta kopa.",
             "Nogrieznis AB - punkti A, B un visi punkti starp tiem.",
             "Riņķa līnija - punkti, kas atrodas vienādā attālumā no centra.",
             "Ja punkts M pieder figūrai F, raksta M ∈ F.",
         ],
         pieze="Tāpat kā kopām, figūrām ir šķēlums: divu taišņu šķēlums ir "
               "to krustpunkts."),

    Zimejums("Punkti un figūra",
             geometrija([("A", 0, 0), ("B", 8, 0), ("M", 3, 0),
                          ("K", 5, 2, 90)],
                        nogriezni=["AB"]),
             paskaidro="M ∈ AB, bet K ∉ AB - punkts K ir ārpus nogriežņa."),

    Paraugs("Divu figūru šķēlums",
            uzd="Nogrieznis AB un nogrieznis CD krustojas punktā O. Kāds ir "
                "abu nogriežņu šķēlums? Kāds - taisnes un riņķa līnijas "
                "šķēlums, ja taisne iet caur centru?",
            soli=[
                ("AB ∩ CD = {O}", "Kopīgs ir tikai krustpunkts."),
                ("Taisne caur centru krusto riņķa līniju 2 punktos",
                 "Diametra galos."),
                ("Šķēlums - divu punktu kopa", "Figūru šķēlums ir figūra."),
            ],
            atbilde="{O}; divi punkti"),

    Varianti("Pieder vai nepieder?", [
        {"jaut": "Punkts atrodas nogriežņa AB vidū. Vai tas pieder AB?",
         "opcijas": ["Jā", "Nē", "Tikai, ja AB ir horizontāls",
                     "Nevar zināt"],
         "pareizi": 0,
         "padoms": "Nogrieznim pieder visi punkti starp galiem."},
        {"jaut": "Riņķa līnijas centrs...",
         "opcijas": ["nepieder riņķa līnijai", "pieder riņķa līnijai",
                     "ir tās viduspunkts, tātad pieder",
                     "pieder, ja r = 1"],
         "pareizi": 0,
         "padoms": "Centrs ir attālumā 0, nevis r."},
        {"jaut": "Kas ir divu paralēlu taišņu šķēlums?",
         "opcijas": ["∅", "Viens punkts", "Divi punkti", "Taisne"],
         "pareizi": 0,
         "padoms": "Tām nav kopīgu punktu."},
        {"jaut": "Kas ir nogriežņa un tā gala punkta šķēlums?",
         "opcijas": ["Gala punkts", "∅", "Viss nogrieznis",
                     "Nogriežņa viduspunkts"],
         "pareizi": 0,
         "padoms": "Gala punkts pieder nogrieznim."},
    ], pamats=4),

    Ievadi("Saskaiti kopīgos punktus", [
        {"jaut": "Cik kopīgu punktu var būt taisnei un riņķa līnijai "
                 "visvairāk?",
         "atb": ["2"], "padoms": "Iedomājies diametru."},
        {"jaut": "Cik kopīgu punktu ir divām taisnēm, kas krustojas?",
         "atb": ["1"], "padoms": "Krustpunkts."},
        {"jaut": "Cik kopīgu punktu var būt divām riņķa līnijām "
                 "visvairāk (ja tās nesakrīt)?",
         "atb": ["2"], "padoms": "Zīmē divus apļus, kas pārklājas."},
        {"jaut": "Cik punktu ir nogrieznim?",
         "atb": ["bezgalīgi daudz", "bezgalīgi", "∞"],
         "padoms": "Starp jebkuriem diviem punktiem ir vēl viens.",
         "tastatura": "text"},
    ]),

    Pasaule("Navigācijas zona",
            Varianti("", [
                {"jaut": "Dronam atļauts lidot 500 m attālumā no operatora "
                         "(ne tālāk). Kāda figūra ir atļautā zona uz zemes?",
                 "opcijas": ["Riņķis ar rādiusu 500 m",
                             "Riņķa līnija ar rādiusu 500 m",
                             "Kvadrāts ar malu 500 m",
                             "Nogrieznis 500 m"],
                 "pareizi": 0,
                 "padoms": "Visi punkti, kas nav tālāk par 500 m - arī "
                           "iekšpuse."},
                {"jaut": "Kurš punkts nepieder atļautajai zonai?",
                 "opcijas": ["620 m no operatora", "500 m no operatora",
                             "0 m no operatora", "250 m no operatora"],
                 "pareizi": 0,
                 "padoms": "620 > 500."},
                {"jaut": "Robeža, kur dronam jāapstājas, ir...",
                 "opcijas": ["riņķa līnija", "riņķis", "taisne", "punkts"],
                 "pareizi": 0,
                 "padoms": "Tieši 500 m attālumā."},
            ]),
            pavediens="tehnika",
            konteksts="Dronu lietotnes zīmē atļauto zonu kā punktu kopu ap "
                      "operatoru.",
            kapec="Figūra kā punktu kopa ir tieši tas, ko dators pārbauda."),

    Kopsavilkums([
        "Zinu, ka ģeometriska figūra ir punktu kopa.",
        "Lietoju ∈ un ∉ punktiem un figūrām.",
        "Atrodu divu figūru šķēlumu.",
        "Atšķiru riņķa līniju no riņķa.",
    ]),

    Majas([
        "Atrodi mājās 3 priekšmetus, kas atgādina figūras, un apraksti tās "
        "kā punktu kopas.",
        "Uzzīmē divus nogriežņus, kuru šķēlums ir nogrieznis.",
        "Kāds var būt taisnes un nogriežņa šķēlums? Uzzīmē visus gadījumus.",
    ]),
]
