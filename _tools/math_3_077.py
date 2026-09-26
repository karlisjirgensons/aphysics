# -*- coding: utf-8 -*-
"""3. klase, 77. stunda: «Cik daļu ir iekrāsotas?»

Pirmā reize, kad daļu *nosauc* ar diviem skaitļiem: cik daļu ir pavisam un
cik no tām ir ņemtas. Pieraksts ar daļsvītru nāks 81. stundā; te vēl pietiek
ar vārdiem «divas no piecām» - bet skatīties jau jāmāk pareizi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         dala)

TEMA = "Cik daļu ir iekrāsotas?"

MERKIS = ("Iekrāsosim figūrā doto daļu skaitu un nosauksim iekrāsoto daļu.")

SATURS = [
    Sakums("Cik daļu ir nokrāsotas un cik palikušas?",
           zimejums=dala(8, 3, "3/8", "astoņas daļas, trīs iekrāsotas"),
           paraksts="Trīs no astoņām - tā nosauc iekrāsoto daļu.",
           fakti=["Daļu nosauc ar diviem skaitļiem: cik pavisam un cik ņemtas.",
                  "Ja iekrāsotas 3 no 8, tad neiekrāsotas ir 5 no 8."]),

    Doma("Daļu nosauc ar diviem skaitļiem",
         "Vispirms pasaki, cik daļu ir pavisam, tad - cik no tām ir ņemtas.",
         soli=[
             "Saskaiti visas vienādās daļas figūrā.",
             "Saskaiti iekrāsotās daļas.",
             "Nosauc: «trīs no astoņām».",
             "Pārbaudi: iekrāsotās un neiekrāsotās kopā dod visas daļas.",
         ],
         pieze="Skaitīt drīkst tikai *vienādas* daļas. Ja figūra sadalīta "
               "nevienādi, daļu nosaukt nevar."),

    Paraugs("Kāda daļa ir iekrāsota?",
            uzd="Figūra sadalīta 8 vienādās daļās, 3 no tām iekrāsotas. Kāda "
                "daļa ir iekrāsota un kāda - ne?",
            soli=[
                ("Pavisam 8 daļas",
                 "Vispirms saskaita visas daļas."),
                ("Iekrāsotas 3 daļas",
                 "Iekrāsotā daļa ir trīs no astoņām."),
                ("8 − 3 = 5",
                 "Neiekrāsotā daļa ir piecas no astoņām."),
            ],
            atbilde="iekrāsotas {3|8}, neiekrāsotas {5|8}"),

    Ievadi("Saskaiti daļas", [
        {"jaut": "Figūrā 8 daļas, iekrāsotas 3. Cik daļu nav iekrāsotas?",
         "atb": ["5"], "padoms": "8 − 3."},
        {"jaut": "Figūrā 6 daļas, iekrāsotas 2. Cik daļu nav iekrāsotas?",
         "atb": ["4"], "padoms": "6 − 2."},
        {"jaut": "Figūrā 10 daļas, iekrāsotas 7. Cik daļu nav iekrāsotas?",
         "atb": ["3"], "padoms": "10 − 7."},
        {"jaut": "Figūrā 5 daļas, neiekrāsotas 2. Cik daļu ir iekrāsotas?",
         "atb": ["3"], "padoms": "5 − 2."},
        {"jaut": "Figūrā 12 daļas, iekrāsota puse. Cik daļu ir iekrāsotas?",
         "atb": ["6"], "padoms": "12 : 2."},
        {"jaut": "Figūrā 9 daļas, iekrāsota trešdaļa. Cik daļu ir "
                 "iekrāsotas?",
         "atb": ["3"], "padoms": "9 : 3."},
    ], pamats=4),

    Petijums("Iekrāso savu figūru",
             vajag="rūtiņu lapa un krāsainie zīmuļi",
             soli=[
                 "Uzzīmē joslu no 10 vienādām rūtiņām.",
                 "Iekrāso 4 rūtiņas vienā krāsā.",
                 "Iekrāso 3 rūtiņas citā krāsā.",
                 "Pasaki, kāda daļa ir katrā krāsā un cik palicis balts.",
             ],
             secinajums="Visas trīs daļas kopā vienmēr dod veselo: 4, 3 un 3 "
                        "no desmit."),

    Zimejums("Iekrāsotā un neiekrāsotā daļa",
             dala(5, 2, "2/5 iekrāsotas, 3/5 baltas",
                  "piecas vienādas daļas"),
             paskaidro="Abas daļas kopā vienmēr dod veselo: divas un trīs "
                       "piektdaļas ir pieci no pieciem.",
             ievads="Vienā figūrā vienmēr ir divas daļas."),

    Varianti("Kāda daļa ir iekrāsota?", [
        {"jaut": "Figūrā 4 daļas, iekrāsota 1. Kāda daļa ir iekrāsota?",
         "opcijas": ["{1|4}", "{1|3}", "{3|4}", "{4|1}"],
         "pareizi": 0, "padoms": "Viena no četrām."},
        {"jaut": "Figūrā 10 daļas, iekrāsotas 7. Kāda daļa nav iekrāsota?",
         "opcijas": ["{3|10}", "{7|10}", "{10|3}", "{1|3}"],
         "pareizi": 0, "padoms": "10 − 7 = 3."},
        {"jaut": "Kad daļu nosaukt nevar?",
         "opcijas": ["Kad daļas nav vienādas", "Kad daļu ir daudz",
                     "Kad figūra ir riņķis", "Vienmēr var"],
         "pareizi": 0, "padoms": "Daļa nozīmē vienādu daļu."},
        {"jaut": "Figūrā 6 daļas, iekrāsotas 3. Kā vēl var nosaukt šo daļu?",
         "opcijas": ["Puse", "Trešdaļa", "Ceturtdaļa", "Sestdaļa"],
         "pareizi": 0, "padoms": "Trīs no sešām ir tieši puse."},
    ], pamats=4),

    Pasaule("Cik daudz kūkas ir apēsts?",
            Ievadi("", [
                {"jaut": "Kūka sadalīta 8 daļās, apēstas 3. Cik daļu "
                         "palika?",
                 "atb": ["5"], "padoms": "8 − 3."},
                {"jaut": "Kūka sadalīta 12 daļās, apēsta puse. Cik daļu "
                         "apēsts?",
                 "atb": ["6"], "padoms": "12 : 2."},
                {"jaut": "Cik daļu ir {1|4} no 12 daļām?",
                 "atb": ["3"], "padoms": "12 : 4."},
                {"jaut": "Cik daļu ir {3|4} no 12 daļām?",
                 "atb": ["9"], "padoms": "3 · 3."},
            ]),
            pavediens="virtuve",
            konteksts="Uz galda palikušos kūkas gabalus vienmēr nosauc pēc "
                      "tā, cik to bija sākumā.",
            kapec="«Trīs gabali» neko nepasaka, ja nezini, cik to bija "
                  "pavisam."),

    Kopsavilkums([
        "Saskaitu, cik vienādu daļu ir figūrā.",
        "Nosaucu iekrāsoto un neiekrāsoto daļu.",
        "Zinu, ka abas daļas kopā dod veselo.",
        "Zinu, ka daļu var nosaukt tikai vienādām daļām.",
    ]),

    Majas([
        "Uzzīmē joslu no 8 rūtiņām un iekrāso 5.",
        "Pasaki, kāda daļa ir iekrāsota un kāda - ne.",
        "Atrodi mājās kaut ko, kur daļa jau ir «apēsta», un nosauc to.",
    ]),
]
