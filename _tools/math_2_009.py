# -*- coding: utf-8 -*-
"""2. klase, 9. stunda: «Ko par klasi stāsta mūsu dati?»

Tēmas noslēgums: grupēšana kļūst par pētījumu. Aptaujas atbildes sagrupē,
saskaita ar svītriņām tabulā un attēlo stabiņos - no tā var nolasīt, kuras
grupas ir vairāk, un par cik.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Petijums,
                         Sakums, Varianti, Zimejums, kolonnas, restis)

TEMA = "Ko par klasi stāsta mūsu dati?"

MERKIS = ("Šodien veiksim nelielu aptauju, sagrupēsim atbildes un attēlosim "
          "tās tabulā un stabiņos.")

_AUGLI = kolonnas([("ābols", 8), ("banāns", 5), ("bumbieris", 3),
                   ("ķirsis", 6)])

SATURS = [
    Sakums("Kādu augli klase ēd visvairāk?",
           zimejums=_AUGLI,
           paraksts="22 bērni - 4 grupas.",
           fakti=["Dati ir atbildes, ko savāc aptaujā.",
                  "Sagrupēti dati parāda to, ko nevar redzēt sarakstā."]),

    Doma("No atbildēm līdz diagrammai",
         "Atbildes sagrupē, saskaita un parāda ar stabiņiem.",
         soli=[
             "Uzdod visiem vienu jautājumu.",
             "Katrai atbildei tabulā ievelc svītriņu savā rindā.",
             "Saskaiti svītriņas katrā rindā.",
             "Uzzīmē stabiņu: jo vairāk, jo augstāks.",
         ]),

    Zimejums("Svītriņu tabula",
             restis([["auglis", "svītriņas", "skaits"],
                     ["ābols", "|||| |||", 8],
                     ["banāns", "||||", 5],
                     ["bumbieris", "|||", 3],
                     ["ķirsis", "|||| |", 6]]),
             paskaidro="Svītriņas liek pa piecām - tā tās ātrāk saskaitīt.",
             ievads="Tā izskatījās tabula aptaujas laikā."),

    Ievadi("Nolasi diagrammu", [
        {"jaut": "Cik bērni izvēlējās ābolu?", "zim": _AUGLI, "atb": ["8"],
         "padoms": "Skaitlis virs stabiņa."},
        {"jaut": "Par cik vairāk bērnu izvēlējās ābolu nekā banānu?",
         "zim": _AUGLI, "atb": ["3"], "padoms": "8 − 5."},
        {"jaut": "Cik bērni izvēlējās ķiršus vai bumbierus?",
         "zim": _AUGLI, "atb": ["9"], "padoms": "6 + 3."},
        {"jaut": "Cik bērnu piedalījās aptaujā?", "zim": _AUGLI,
         "atb": ["22"], "padoms": "8 + 5 + 3 + 6."},
    ]),

    Varianti("Ko dati stāsta?", [
        {"jaut": "Kurš auglis ir vismazāk iecienīts?", "zim": _AUGLI,
         "opcijas": ["bumbieris", "banāns", "ķirsis"], "pareizi": 0,
         "padoms": "Zemākais stabiņš."},
        {"jaut": "Kurš apgalvojums ir patiess?", "zim": _AUGLI,
         "opcijas": ["Ābolu izvēlējās vairāk nekā ķiršus",
                     "Banānu izvēlējās visvairāk",
                     "Bumbieri un banānu izvēlējās vienādi"],
         "pareizi": 0, "padoms": "Salīdzini stabiņus."},
    ]),

    Petijums("Mūsu klases aptauja", [
        "Izvēlieties jautājumu: mīļākais gadalaiks, mājdzīvnieks vai sports.",
        "Uzrakstiet uz tāfeles 3-4 atbilžu grupas.",
        "Katrs ievelk savu svītriņu.",
        "Saskaitiet un uzzīmējiet stabiņus.",
        "Kurā grupā ir visvairāk bērnu? Par cik vairāk nekā mazākajā?",
    ], vajag="tāfele vai liela lapa, flomāsteri",
             secinajums="Diagramma vienā skatienā pasaka, kas klasei "
                        "patīk visvairāk."),

    Pasaule("Ko pasūtīt ēdnīcai?",
            Ievadi("", [
                {"jaut": "Aptaujā par zupām: biešu zupu grib 9 bērni, "
                         "zirņu - 4, tomātu - 7. Cik bērnu atbildēja?",
                 "atb": ["20"], "padoms": "9 + 4 + 7."},
                {"jaut": "Par cik vairāk bērnu grib biešu zupu nekā zirņu?",
                 "atb": ["5"], "padoms": "9 − 4."},
            ]),
            pavediens="skola",
            konteksts="Ēdnīca jautā klasēm, kādu zupu gatavot piektdienās.",
            kapec="Pēc datiem pavārs zina, ko gatavot vairāk."),

    Kopsavilkums([
        "Veicu nelielu aptauju.",
        "Sagrupēju atbildes svītriņu tabulā.",
        "Nolasu stabiņu diagrammu un salīdzinu grupas.",
    ]),

    Majas([
        "Pajautā 6 cilvēkiem, kāds ir viņu mīļākais gadalaiks.",
        "Sagrupē atbildes svītriņu tabulā.",
        "Kurš gadalaiks uzvarēja?",
    ]),
]
