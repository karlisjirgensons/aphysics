# -*- coding: utf-8 -*-
"""3. klase, 117. stunda: «Kā izmērīt lapas laukumu?»

Neregulāra figūra - pirmais gadījums, kad atbilde ir *aptuvena*. Rūtiņu
režģis dod divas robežas: pilno rūtiņu skaits ir par maz, visu aizskarto
rūtiņu skaits ir par daudz, un patiesā vērtība ir kaut kur pa vidu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         kolonnas)

TEMA = "Kā izmērīt lapas laukumu?"

MERKIS = ("Ar caurspīdīgu rūtiņu režģi noteiksim neregulāras figūras "
          "aptuveno laukumu.")

SATURS = [
    Sakums("Cik liela ir koka lapa?",
           zimejums=kolonnas([("pilnas", 18), ("aptuveni", 24),
                              ("aizskartas", 30)], " rūtiņas"),
           paraksts="Patiesais laukums ir kaut kur starp 18 un 30.",
           fakti=["Neregulārai figūrai laukums ir aptuvens.",
                  "Pilnās rūtiņas dod apakšējo robežu.",
                  "Visas aizskartās rūtiņas dod augšējo robežu."]),

    Doma("Skaiti pilnās un pusaizņemtās rūtiņas",
         "Pilnās skaita kā veselas, pusaizņemtās - kā pusi; summa ir aptuvenais "
         "laukums.",
         soli=[
             "Uzliec figūrai rūtiņu režģi.",
             "Saskaiti pilnās rūtiņas.",
             "Saskaiti daļēji aizņemtās un dalī to skaitu ar 2.",
             "Saskaiti abus skaitļus kopā.",
         ],
         pieze="Jo smalkāks režģis, jo precīzāka atbilde - bet rūtiņu "
               "jāskaita vairāk. Tā vienmēr ir izvēle starp ātrumu un "
               "precizitāti."),

    Petijums("Izmēri koka lapas laukumu",
             vajag="koka lapa, rūtiņu papīrs un zīmulis",
             soli=[
                 "Uzliec lapu uz rūtiņu papīra un apvelc to.",
                 "Saskaiti pilnās rūtiņas kontūrā.",
                 "Saskaiti rūtiņas, kuras kontūra šķērso.",
                 "Pieskaiti pusi no tām pilno rūtiņu skaitam.",
             ],
             secinajums="Iegūtais skaitlis ir aptuvens laukums - un divi "
                        "cilvēki var dabūt nedaudz dažādas atbildes."),

    Paraugs("Cik liels ir lapas laukums?",
            uzd="Kontūrā ir 18 pilnas rūtiņas un 12 daļēji aizņemtas. Cik "
                "liels ir aptuvenais laukums?",
            soli=[
                ("18 pilnas rūtiņas",
                 "Tās skaita kā veselas."),
                ("12 : 2 = 6",
                 "Daļēji aizņemtās skaita kā puses."),
                ("18 + 6 = 24",
                 "Aptuvenais laukums ir 24 rūtiņas."),
            ],
            atbilde="apmēram 24 rūtiņas"),

    Ievadi("Aptuvenais laukums", [
        {"jaut": "18 pilnas un 12 daļējas rūtiņas. Cik ir aptuvenais "
                 "laukums?",
         "atb": ["24"], "padoms": "18 + 6."},
        {"jaut": "20 pilnas un 10 daļējas. Cik ir aptuvenais laukums?",
         "atb": ["25"], "padoms": "20 + 5."},
        {"jaut": "14 pilnas un 8 daļējas. Cik ir aptuvenais laukums?",
         "atb": ["18"], "padoms": "14 + 4."},
        {"jaut": "Kāda ir apakšējā robeža, ja pilnas ir 18 rūtiņas?",
         "atb": ["18"], "padoms": "Tikai pilnās."},
        {"jaut": "Kāda ir augšējā robeža, ja pilnas 18 un daļējas 12?",
         "atb": ["30"], "padoms": "18 + 12."},
        {"jaut": "30 pilnas un 20 daļējas. Cik ir aptuvenais laukums?",
         "atb": ["40"], "padoms": "30 + 10."},
    ], pamats=4),

    Zimejums("Trīs skaitļi vienai lapai",
             kolonnas([("pilnas", 20), ("aptuveni", 25),
                       ("aizskartas", 30)], " rūtiņas"),
             paskaidro="Aptuvenā vērtība vienmēr atrodas starp abām robežām.",
             ievads="Tā izskatās mērījums ar režģi."),

    Varianti("Cik precīzs ir mērījums?", [
        {"jaut": "Kāpēc neregulāras figūras laukums ir aptuvens?",
         "opcijas": ["Kontūra šķērso rūtiņas", "Rūtiņas ir par lielām",
                     "Figūra ir par mazu", "Tas nav aptuvens"],
         "pareizi": 0, "padoms": "Daļēji aizņemtās rūtiņas."},
        {"jaut": "Kā iegūt precīzāku atbildi?",
         "opcijas": ["Ņemt smalkāku režģi", "Skaitīt ātrāk",
                     "Ņemt lielākas rūtiņas", "Mērīt ar lineālu"],
         "pareizi": 0, "padoms": "Mazākas rūtiņas - mazāka kļūda."},
        {"jaut": "16 pilnas un 8 daļējas. Cik ir aptuvenais laukums?",
         "opcijas": ["20", "24", "16", "8"],
         "pareizi": 0, "padoms": "16 + 4."},
        {"jaut": "Vai divi cilvēki var iegūt nedaudz dažādas atbildes?",
         "opcijas": ["Jā, mērījums ir aptuvens", "Nē, nekad",
                     "Tikai ja kļūdās", "Tikai lielām figūrām"],
         "pareizi": 0, "padoms": "Daļējās rūtiņas var skaitīt dažādi."},
    ], pamats=4),

    Pasaule("Cik liels ir zemes gabals?",
            Ievadi("", [
                {"jaut": "Plānā gabals aizņem 40 pilnas rūtiņas un 20 "
                         "daļējas. Cik ir aptuvenais laukums rūtiņās?",
                 "atb": ["50"], "padoms": "40 + 10."},
                {"jaut": "Viena rūtiņa ir 1 m². Cik kvadrātmetru tas ir?",
                 "atb": ["50"], "padoms": "Tas pats skaitlis."},
                {"jaut": "Cik kvadrātmetru ir puse no šī gabala?",
                 "atb": ["25"], "padoms": "50 : 2."},
                {"jaut": "Cik kvadrātmetru ir {1|5} no gabala?",
                 "atb": ["10"], "padoms": "50 : 5."},
            ]),
            pavediens="maja",
            konteksts="Zemes gabalu robežas reti ir taisnas - tāpēc laukumu "
                      "mēra tieši ar režģi uz kartes.",
            kapec="Aptuvens laukums pietiek, lai zinātu, cik sēklu vajag."),

    Kopsavilkums([
        "Nosaku neregulāras figūras aptuveno laukumu ar rūtiņu režģi.",
        "Skaitu pilnās rūtiņas un pusi no daļēji aizņemtajām.",
        "Zinu apakšējo un augšējo robežu.",
        "Zinu, ka smalkāks režģis dod precīzāku atbildi.",
    ]),

    Majas([
        "Apvelc savu plaukstu uz rūtiņu papīra un izmēri tās laukumu.",
        "Izmēri koka lapas laukumu.",
        "Salīdzini abus laukumus.",
    ]),
]
