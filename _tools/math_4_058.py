# -*- coding: utf-8 -*-
"""4. klase, 58. stunda: «Kā mēra ar transportieri?»

Transportieris ir lineāls leņķiem. Trīs noteikumi: centrs virsotnē, nulles
līnija uz vienas malas, skaitli nolasa tajā skalā, kas sākas ar 0 uz šīs
malas. Visbiežākā kļūda - nolasīt otru skalu (130° vietā 50°); to
palīdz pamanīt spriedums «šaurs vai plats?».
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas,
                         Paraugs, Pasaule, Petijums, Sakums, Varianti,
                         lenkis)

TEMA = "Kā mēra ar transportieri?"

MERKIS = ("Ar transportieri izmērīsim leņķa lielumu un pierakstīsim "
          "rezultātu.")

SATURS = [
    Sakums("Kā izmērīt leņķi, ja lineāls neder?",
           zimejums=lenkis([(0, "0°"), (30, "30°"), (60, "60°"), (90, "90°"),
                            (120, "120°"), (150, "150°"), (180, "180°")]),
           paraksts="Transportieris - pusaplis ar grādu skalu.",
           fakti=["Transportierim parasti ir divas skalas - ārējā un "
                  "iekšējā.",
                  "Tās iet pretējos virzienos: 0 kreisajā un 0 labajā pusē."]),

    Doma("Centrs virsotnē, nulle uz malas",
         "Transportiera centru liek leņķa virsotnē, nulles līniju - uz "
         "vienas malas, un nolasa skalā, kas uz šīs malas sākas ar 0.",
         soli=[
             "Transportiera centra punktu novieto leņķa virsotnē.",
             "Nulles līniju savieto ar vienu leņķa malu.",
             "Atrodi skalu, kurā uz šīs malas ir 0.",
             "Nolasi skaitli, kur otrā mala krusto šo skalu.",
         ],
         pieze="Pārbaudi ar aci: ja leņķis ir šaurs, atbildei jābūt mazākai "
               "par 90°."),

    Paraugs("Kuru skalu lasīt?",
            uzd="Leņķa mala iet caur skalu, kur ārējā skalā ir 50, iekšējā - "
                "130. Leņķis ir šaurs. Cik tas ir?",
            soli=[
                ("šaurs → mazāks par 90°", "Spriedums pirms nolasīšanas."),
                ("50° < 90°, 130° > 90°", "Der tikai 50°."),
            ],
            atbilde="50°"),

    Kustiba("Aizgriez rādītāju", [
        {"jaut": "Leņķis ir 70°. Aizved rādītāju līdz tam uz skalas.",
         "atb": 70, "beigas": 180, "iedala": 10, "mers": "grādi",
         "merkis": "70°", "objekts": "Rādītājs",
         "stasts": "Te transportiera loks ir iztaisnots skalā no 0° līdz "
                   "180°.",
         "padoms": "7 iedaļas pa 10°."},
        {"jaut": "Taisns leņķis. Kur jāapstājas?",
         "atb": 90, "beigas": 180, "iedala": 10, "mers": "grādi",
         "merkis": "taisns", "objekts": "Rādītājs",
         "padoms": "90°."},
        {"jaut": "Ārējā skalā 40, iekšējā 140. Leņķis ir plats. Kur?",
         "atb": 140, "beigas": 180, "iedala": 10, "mers": "grādi",
         "merkis": "plats", "objekts": "Rādītājs",
         "padoms": "Plats - lielāks par 90."},
        {"jaut": "Leņķis ir par 25° mazāks nekā taisns. Kur?",
         "atb": 65, "beigas": 180, "iedala": 10, "mers": "grādi",
         "merkis": "?", "objekts": "Rādītājs",
         "padoms": "90 − 25."},
    ], pamats=2,
        ievads="Ieraksti grādus un palaid rādītāju."),

    Varianti("Transportiera kļūdas", [
        {"jaut": "Kur jāliek transportiera centrs?",
         "opcijas": ["leņķa virsotnē", "uz malas galā", "jebkur",
                     "lapas vidū"], "pareizi": 0,
         "padoms": "Virsotnē satiekas malas."},
        {"jaut": "Plata leņķa mērījums sanāca 60°. Kas noticis?",
         "opcijas": ["nolasīja nepareizo skalu", "viss pareizi",
                     "leņķis ir šaurs"], "pareizi": 0,
         "padoms": "Platam jābūt > 90°; pareizi 120°."},
        {"jaut": "Mērījums: ārējā 35, iekšējā 145. Leņķis ir šaurs.",
         "opcijas": ["35°", "145°", "90°", "180°"], "pareizi": 0,
         "padoms": "Šaurs < 90°."},
        {"jaut": "Kā pierakstīt: leņķis ABC ir 75 grādi?",
         "opcijas": ["∠ABC = 75°", "ABC = 75", "∠75 = ABC",
                     "∠ABC = 75 cm"], "pareizi": 0,
         "padoms": "Leņķa zīme, virsotne vidū, grādi."},
    ], pamats=4),

    Ievadi("Nolasi pareizo skalu", [
        {"jaut": "Ārējā 20, iekšējā 160; leņķis plats. Cik grādu?",
         "atb": ["160"], "padoms": "Plats > 90."},
        {"jaut": "Ārējā 110, iekšējā 70; leņķis šaurs. Cik grādu?",
         "atb": ["70"], "padoms": "Šaurs < 90."},
        {"jaut": "Mala iet caur 90 abās skalās. Cik grādu?",
         "atb": ["90"], "padoms": "Taisns."},
        {"jaut": "Ārējā 15, iekšējā 165; leņķis šaurs. Cik grādu?",
         "atb": ["15"], "padoms": "Šaurs."},
    ]),

    Pasaule("Kalna nogāzes slīpums",
            Ievadi("", [
                {"jaut": "Slēpošanas trase «zilā» ir ap 15° slīpa, «sarkanā» "
                         "- 25°. Par cik grādiem sarkanā stāvāka?",
                 "atb": ["10"], "padoms": "25 − 15."},
                {"jaut": "«Melnā» trase ir divreiz stāvāka nekā zilā. Cik "
                         "grādu?",
                 "atb": ["30"], "padoms": "15 · 2."},
                {"jaut": "Cik grādu trūkst melnajai trasei līdz taisnam "
                         "leņķim?",
                 "atb": ["60"], "padoms": "90 − 30."},
                {"jaut": "Pret sienu atbalstītas kāpnes ar zemi veido 75°. "
                         "Kāds leņķa veids? Raksti vārdu.",
                 "atb": ["šaurs", "saurs"], "tastatura": "text",
                 "padoms": "75 < 90."},
            ]),
            pavediens="sports",
            konteksts="Slēpošanas trases slīpumu mēra grādos - jo lielāks "
                      "leņķis, jo ātrāks brauciens.",
            kapec="Transportieris pārvērš «stāvs» un «lēzens» skaitļos."),

    Petijums("Mēri klasē",
             soli=[
                 "Uzzīmē 4 dažādus leņķus.",
                 "Katram vispirms uzmini, cik grādu tas ir.",
                 "Izmēri ar transportieri.",
                 "Salīdzini minējumu ar mērījumu.",
             ],
             vajag="transportieris, zīmulis, lapa",
             secinajums="Jo vairāk mēri, jo precīzāk vari novērtēt ar aci."),

    Kopsavilkums([
        "Mēru leņķi ar transportieri.",
        "Izvēlos pareizo skalu.",
        "Pārbaudu mērījumu ar spriedumu «šaurs vai plats».",
        "Pierakstu: ∠ABC = 75°.",
    ]),

    Majas([
        "Izmēri 3 leņķus mājās (grāmatas atvērums, šķēres, durvis).",
        "Uzmini un izmēri leņķi starp pulksteņa rādītājiem plkst. 2.",
        "Iemāci mājiniekam, kā lietot transportieri.",
    ]),
]
