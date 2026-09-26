# -*- coding: utf-8 -*-
"""3. klase, 109. stunda: «Šaurs, taisns vai plats?»

Leņķu klasifikācija ar uzstūri kā mēru. Grādi šajā klasē vēl nav vajadzīgi:
pietiek salīdzināt ar taisnu leņķi - mazāks, tieši tāds vai lielāks. Acumērs
te ir pirmais solis, uzstūris - pārbaude.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         lenkis)

TEMA = "Šaurs, taisns vai plats?"

MERKIS = ("Pēc acumēra noteiksim leņķa veidu un pārbaudīsim to ar uzstūri.")

SATURS = [
    Sakums("Kā pateikt leņķa veidu, to nemērot?",
           zimejums=lenkis([(0, ""), (90, "")], [(0, 90, "taisns")],
                           "taisns leņķis"),
           paraksts="Taisns leņķis ir tas, kas ir istabas stūrī un uz lapas "
                    "malas.",
           fakti=["Šaurs leņķis ir mazāks par taisnu.",
                  "Plats leņķis ir lielāks par taisnu.",
                  "Taisnu leņķi pārbauda ar uzstūri vai lapas stūri."]),

    Doma("Salīdzini ar taisnu leņķi",
         "Taisns leņķis ir mērs: viss, kas mazāks, ir šaurs, viss, kas "
         "lielāks, - plats.",
         soli=[
             "Pieliec uzstūri vai lapas stūri pie leņķa virsotnes.",
             "Salīdzini leņķa staru ar uzstūra malu.",
             "Ja stars ir iekšpusē - leņķis ir šaurs.",
             "Ja stars ir ārpusē - leņķis ir plats.",
         ],
         pieze="Papīra lapas stūris vienmēr ir taisns leņķis - tāpēc uzstūri "
               "var aizstāt ar jebkuru lapu."),

    Petijums("Atrodi visus trīs veidus",
             vajag="papīra lapa un zīmulis",
             soli=[
                 "Atrodi klasē piecus dažādus leņķus.",
                 "Pieliec pie katra lapas stūri.",
                 "Pieraksti, kurš ir šaurs, kurš taisns, kurš plats.",
                 "Uzzīmē pa vienam katra veida leņķim.",
             ],
             secinajums="Gandrīz visi telpas leņķi ir taisni - tieši tāpēc "
                        "tos ir viegli atpazīt."),

    Paraugs("Kāds ir šis leņķis?",
            uzd="Leņķa stars ir iekšpus uzstūra malai. Kāds ir leņķa veids?",
            soli=[
                ("Pieliek uzstūri pie virsotnes",
                 "Uzstūra mala rāda taisnu leņķi."),
                ("Stars ir iekšpusē",
                 "Tātad leņķis ir mazāks par taisnu."),
                ("Leņķis ir šaurs",
                 "Šauru leņķi sauc arī par asu leņķi."),
            ],
            atbilde="šaurs leņķis"),

    Ievadi("Leņķu veidi", [
        {"jaut": "Cik taisnu leņķu ir taisnstūrim?", "atb": ["4"],
         "padoms": "Visi četri."},
        {"jaut": "Cik taisnu leņķu ir vienā pilnā apgriezienā?",
         "atb": ["4"], "padoms": "Četri pagriezieni."},
        {"jaut": "Cik taisnu leņķu ir izstieptā leņķī?", "atb": ["2"],
         "padoms": "Puse apgrieziena."},
        {"jaut": "Cik taisnu leņķu ir kvadrātam?", "atb": ["4"],
         "padoms": "Tāpat kā taisnstūrim."},
        {"jaut": "Cik šauru leņķu vismaz ir trīsstūrim?", "atb": ["2"],
         "padoms": "Vismaz divi vienmēr ir šauri."},
        {"jaut": "Cik leņķu ir sešstūrim?", "atb": ["6"],
         "padoms": "Tik, cik virsotņu."},
    ], pamats=4),

    Zimejums("Šaurs un plats leņķis",
             lenkis([(0, ""), (40, ""), (140, "")],
                    [(0, 40, "šaurs"), (40, 140, "plats")],
                    "salīdzini abus"),
             paskaidro="Šaurais leņķis ir mazāks par taisnu, platais - "
                       "lielāks.",
             ievads="Divi leņķi ar vienu virsotni."),

    Varianti("Kāds leņķis tas ir?", [
        {"jaut": "Leņķis ir mazāks par taisnu. Kāds tas ir?",
         "opcijas": ["Šaurs", "Plats", "Taisns", "Izstiepts"],
         "pareizi": 0, "padoms": "Mazāks par taisnu."},
        {"jaut": "Ar ko pārbauda taisnu leņķi?",
         "opcijas": ["Ar uzstūri vai lapas stūri", "Ar lineālu",
                     "Ar cirkuli", "Ar aci"],
         "pareizi": 0, "padoms": "Uzstūrim ir taisns leņķis."},
        {"jaut": "Kāds leņķis ir istabas stūrī?",
         "opcijas": ["Taisns", "Šaurs", "Plats", "Izstiepts"],
         "pareizi": 0, "padoms": "Sienas ir perpendikulāras."},
        {"jaut": "Kāds leņķis ir starp pulksteņa rādītājiem pulksten 3?",
         "opcijas": ["Taisns", "Šaurs", "Plats", "Izstiepts"],
         "pareizi": 0, "padoms": "Ceturtdaļa apgrieziena."},
    ], pamats=4),

    Pasaule("Kādā leņķī stāv saules panelis?",
            Ievadi("", [
                {"jaut": "Panelis stāv tā, ka leņķis ar zemi ir mazāks par "
                         "taisnu. Kāds tas ir? Raksti «šaurs» vai «plats».",
                 "atb": ["šaurs", "saurs"], "padoms": "Mazāks par taisnu.",
                 "tastatura": "text"},
                {"jaut": "Cik taisnu leņķu ir paneļa taisnstūrveida rāmim?",
                 "atb": ["4"], "padoms": "Visi četri."},
                {"jaut": "Rāmis ir 200 cm un 100 cm. Cik ir perimetrs "
                         "centimetros?",
                 "atb": ["600"], "padoms": "2 · 300."},
                {"jaut": "Cik metru tas ir?", "atb": ["6"],
                 "padoms": "600 : 100."},
            ]),
            pavediens="tehnika",
            konteksts="Saules paneli noliec šaurā leņķī pret zemi, lai saules "
                      "stari krīt taisnāk.",
            kapec="No leņķa atkarīgs, cik daudz enerģijas panelis saņem."),

    Kopsavilkums([
        "Nosaku leņķa veidu pēc acumēra.",
        "Pārbaudu to ar uzstūri vai lapas stūri.",
        "Zinu, kas ir šaurs, taisns un plats leņķis.",
        "Atrodu leņķus apkārtnē.",
    ]),

    Majas([
        "Atrodi mājās vienu šauru, vienu taisnu un vienu platu leņķi.",
        "Pārbaudi tos ar papīra lapas stūri.",
        "Uzzīmē visus trīs veidus burtnīcā.",
    ]),
]
