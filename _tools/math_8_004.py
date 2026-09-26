# -*- coding: utf-8 -*-
"""8. klase, 4. stunda: «Kura diagramma der šiem datiem?»

Trīs diagrammas - trīs jautājumi: stabiņi salīdzina, sektori rāda daļas
no veseluma, līnija rāda izmaiņas laikā. Slīdnis parāda tos pašus datus
visās trijās, lai redz, kura atbild uz jautājumu un kura tikai izskatās.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, Zimejums, kolonnas, plakne,
                         sektori)

TEMA = "Kura diagramma der šiem datiem?"

MERKIS = ("Izvēlēsimies piemērotu diagrammas veidu un pamatosim izvēli.")

_TRANSPORTS = [("kājām", 12), ("autobuss", 9), ("velo", 6), ("auto", 3)]

# Rīgas vidējā gaisa temperatūra pa mēnešiem, °C (noapaļota).
_RIGA = [(1, -3), (2, -3), (3, 1), (4, 7), (5, 12), (6, 16), (7, 19),
         (8, 18), (9, 13), (10, 7), (11, 2), (12, -1)]

SATURS = [
    Sakums("Kā klase nokļūst skolā?",
           zimejums=sektori(_TRANSPORTS),
           paraksts="30 skolēni - katrs sektors ir viena atbilde.",
           fakti=["Sektoru diagramma rāda daļas no visiem.",
                  "Stabiņu diagramma salīdzina skaitus.",
                  "Līniju diagramma rāda, kā lielums mainās laikā."]),

    Doma("Jautājums izvēlas diagrammu",
         "Pirms zīmē, pajautā: ko lasītājam jāredz? Katrai diagrammai ir "
         "savs darbs.",
         soli=[
             "Salīdzināt lielumus - stabiņu diagramma.",
             "Parādīt daļas no veseluma (kopā 100 %) - sektoru diagramma.",
             "Parādīt izmaiņas laikā - līniju diagramma.",
             "Diagrammai vajag virsrakstu, asu nosaukumus un mērvienības.",
         ],
         pieze="Sektoru diagramma der tikai tad, ja daļas kopā veido veselu - "
               "piemēram, katrs skolēns atbildēja tieši vienu reizi."),

    Slidnis("Tie paši dati - trīs diagrammas", [
        {"v": "Stabiņi", "teksts": "Uzreiz redz: kājām iet visvairāk",
         "zim": kolonnas(_TRANSPORTS)},
        {"v": "Sektori", "teksts": "Uzreiz redz: kājām iet 40 % klases",
         "zim": sektori(_TRANSPORTS)},
        {"v": "Līnija?",
         "teksts": "Neder: starp «kājām» un «autobusu» nav laika",
         "zim": plakne(lauzta=[(1, 12), (2, 9), (3, 6), (4, 3)], no_x=0,
                       lidz_x=5, no_y=0, lidz_y=14, solis=1, solis_y=2,
                       x_nos="?", y_nos="skaits")},
    ], ievads="Kurš attēls atbild uz jautājumu, un kurš maldina?"),

    Varianti("Izvēlies diagrammu", [
        {"jaut": "Temperatūra katru stundu no rīta līdz vakaram.",
         "opcijas": ["Līniju", "Sektoru", "Stabiņu", "Nekāda"],
         "pareizi": 0, "padoms": "Izmaiņas laikā."},
        {"jaut": "Kā ģimenes budžets sadalās: pārtika, īre, transports, cits.",
         "opcijas": ["Sektoru", "Līniju", "Neviena neder", "Punktu"],
         "pareizi": 0, "padoms": "Daļas no visas summas."},
        {"jaut": "Iedzīvotāju skaits piecās Latvijas pilsētās.",
         "opcijas": ["Stabiņu", "Līniju", "Sektoru", "Neviena neder"],
         "pareizi": 0, "padoms": "Salīdzina lielumus."},
        {"jaut": "Aptaujā katrs drīkstēja izvēlēties vairākus hobijus. "
                 "Kura neder?",
         "opcijas": ["Sektoru", "Stabiņu", "Abas der", "Neviena neder"],
         "pareizi": 0, "padoms": "Summa pārsniedz visu skolēnu skaitu."},
    ]),

    Ievadi("Lasi sektoru diagrammu", [
        {"jaut": "Klasē 30 skolēnu, kājām iet 40 %. Cik skolēnu?",
         "atb": ["12"], "padoms": "0,4 · 30."},
        {"jaut": "Ar velosipēdu brauc 6 no 30. Cik procentu?",
         "atb": ["20", "20 %", "20%"], "padoms": "6 : 30."},
        {"jaut": "Cik grādu ir sektoram «velo» (20 %)?",
         "atb": ["72", "72°"], "padoms": "20 % no 360°."},
        {"jaut": "Sektors ir 90°. Kāda daļa no visiem tas ir procentos?",
         "atb": ["25", "25 %", "25%"], "padoms": "90 : 360."},
    ]),

    Pasaule("Kā mainās laiks Rīgā?",
            Ievadi("", [
                {"jaut": "Grafikā: kura mēneša numurā vidēji ir vissiltāk?",
                 "atb": ["7"], "padoms": "Augstākais punkts."},
                {"jaut": "Cik grādu ir starpība starp siltāko un aukstāko "
                         "mēnesi?",
                 "atb": ["22", "22°"], "padoms": "19 − (−3)."},
                {"jaut": "Cik mēnešos vidējā temperatūra ir zem 0 °C?",
                 "atb": ["3"], "padoms": "1., 2. un 12. mēnesis."},
            ]),
            pavediens="planeta",
            konteksts="Klimatu raksturo vidējā temperatūra katrā mēnesī - "
                      "tā mainās laikā, tāpēc der līniju diagramma.",
            kapec="Līnija parāda arī to, kad kļūst siltāks un kad vēsāks.",
            zimejums=plakne(lauzta=_RIGA, punkti=_RIGA, no_x=0, lidz_x=12,
                            no_y=-5, lidz_y=20, solis=1, solis_y=5,
                            x_nos="mēn.", y_nos="°C")),

    Kopsavilkums([
        "Stabiņu diagrammu lietoju salīdzināšanai.",
        "Sektoru diagrammu - daļām no veseluma.",
        "Līniju diagrammu - izmaiņām laikā.",
        "Pamatoju, kāpēc cita diagramma neder.",
    ]),

    Majas([
        "Atrodi ziņās divas diagrammas un nosaki to veidu.",
        "Katrai uzraksti, vai veids izvēlēts pareizi.",
        "Uzzīmē sektoru diagrammu savai dienai: miegs, skola, brīvais laiks.",
    ]),
]
