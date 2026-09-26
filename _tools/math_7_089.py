# -*- coding: utf-8 -*-
"""7. klase, 89. stunda: «Kā konstruēt leņķa bisektrisi?»

Ar cirkuli un lineālu leņķi var sadalīt precīzi uz pusēm: loks no
virsotnes, divi vienādi loki no krustpunktiem - un stars caur to
krustpunktu ir bisektrise. Pamatojums - vienādi trijstūri pēc mmm.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, geometrija)

TEMA = "Kā konstruēt leņķa bisektrisi?"

MERKIS = ("Ar cirkuli un lineālu konstruēsim leņķa bisektrisi un "
          "pamatosim darbības.")


def _b(n):
    p = [("O", 0, 0), ("_A", 6, 0), ("_B", 4.2, 4.2)]
    izc, stari, lenki, nog = [], [("O", "_A"), ("O", "_B")], [], []
    if n >= 2:
        p += [("M", 3, 0, -90), ("N", 2.12, 2.12, 135)]
    if n >= 3:
        p += [("K", 4.6, 1.9, 0)]
        izc += [("M", "K"), ("N", "K")]
    if n >= 4:
        stari += [("O", "K")]
        lenki = [(("_A", "O", "K"), ""), (("K", "O", "_B"), "")]
        nog = []
    return geometrija(p, nogriezni=nog, stari=stari, izcelti=izc,
                      lenki=lenki)


SATURS = [
    Sakums("Precīzi uz pusēm - bez transportiera",
           zimejums=_b(4),
           paraksts="Stars OK dala leņķi divās vienādās daļās.",
           fakti=["Transportieris dod ±1° kļūdu.",
                  "Konstrukcija ir precīza teorētiski.",
                  "Tā balstās uz vienādiem trijstūriem."]),

    Doma("Konstrukcijas soļi",
         "Leņķa bisektrisi konstruē: 1) no virsotnes O novelk loku, kas "
         "krusto malas punktos M un N; 2) no M un N ar vienādu rādiusu "
         "novelk lokus, kas krustojas punktā K; 3) novelk staru OK.",
         soli=[
             "Loks no O: punkti M un N uz malām (OM = ON).",
             "No M un N - loki ar vienu rādiusu: krustpunkts K (MK = NK).",
             "Stars OK ir bisektrise.",
             "Pārbaudi ar transportieri.",
         ],
         pieze="Otrā soļa rādiusam jābūt lielākam par pusi no MN - citādi "
               "loki nekrustosies."),

    Slidnis("Soli pa solim", [
        {"v": "1. solis", "teksts": "Dots leņķis ar virsotni O.",
         "zim": _b(1)},
        {"v": "2. solis", "teksts": "Loks no O: M un N.", "zim": _b(2)},
        {"v": "3. solis", "teksts": "Loki no M un N: punkts K.",
         "zim": _b(3)},
        {"v": "4. solis", "teksts": "Stars OK - bisektrise.", "zim": _b(4)},
    ]),

    Paraugs("Pamatojums",
            uzd="Pamato, ka OK ir bisektrise.",
            soli=[
                ("OM = ON", "(viens loks no O)"),
                ("MK = NK", "(vienāds rādiuss)"),
                ("OK = OK", "(kopīga mala)"),
                ("△OMK = △ONK", "(mmm)"),
                ("∠MOK = ∠NOK", "(atbilstošie leņķi)"),
            ],
            atbilde="OK dala leņķi uz pusēm."),

    Varianti("Konstrukcija", [
        {"jaut": "Kāpēc OM = ON?",
         "opcijas": ["Tie ir viena loka rādiusi", "Tā gadās",
                     "Izmērīti ar lineālu", "Leņķis ir taisns"],
         "pareizi": 0, "padoms": "Viens cirkuļa atvērums."},
        {"jaut": "Kas notiek, ja loki no M un N ir ar dažādiem rādiusiem?",
         "opcijas": ["K nav uz bisektrises", "Nekas",
                     "Bisektrise būs precīzāka", "Loki sakritīs"],
         "pareizi": 0, "padoms": "Jābūt MK = NK."},
        {"jaut": "Kā konstruēt 45° leņķi?",
         "opcijas": ["Konstruēt taisna leņķa bisektrisi",
                     "Divreiz uzzīmēt 90°", "Ar lineālu", "Nevar"],
         "pareizi": 0, "padoms": "90 : 2."},
    ]),

    Petijums("Konstruē un pārbaudi",
             ["Uzzīmē jebkuru leņķi.",
              "Izpildi 3 konstrukcijas soļus.",
              "Izmēri abas daļas ar transportieri.",
              "Konstruē bisektrisi arī vienai no pusēm - kāda daļa no "
              "leņķa sanāk?"],
             vajag="cirkulis, lineāls, transportieris",
             secinajums="Divreiz konstruējot bisektrisi, iegūst ceturtdaļu "
                         "leņķa."),

    Pasaule("Galdnieka stūris",
            Varianti("", [
                {"jaut": "Bilžu rāmja stūri savieno 45° leņķī. Kā to "
                         "atrast bez transportiera?",
                 "opcijas": ["Taisnā leņķa bisektrise",
                             "Uz aci", "Mērīt ar lineālu", "Nevar"],
                 "pareizi": 0, "padoms": "90° uz pusēm."},
                {"jaut": "Ja divi 45° gabali savienojas, stūris ir...",
                 "opcijas": ["90°", "45°", "180°", "135°"],
                 "pareizi": 0, "padoms": "45 + 45."},
                {"jaut": "Sešstūra rāmja stūris ir 120°. Kādā leņķī "
                         "jāzāģē katra līste?",
                 "opcijas": ["60°", "120°", "30°", "45°"],
                 "pareizi": 0, "padoms": "Bisektrise: 120 : 2."},
            ]),
            pavediens="maja",
            konteksts="Līstes stūros zāģē pa leņķa bisektrisi - tad šuve "
                      "ir taisna.",
            kapec="Bisektrise ir galdnieka ikdiena."),

    Kopsavilkums([
        "Konstruēju leņķa bisektrisi ar cirkuli un lineālu.",
        "Pamatoju konstrukciju ar pazīmi mmm.",
        "Iegūstu 45°, 30° un citus leņķus.",
        "Zinu rādiusa nosacījumu.",
    ]),

    Majas([
        "Konstruē 90° leņķa bisektrisi un pārbaudi.",
        "Sadali leņķi 4 vienādās daļās.",
        "Uzraksti konstrukcijas soļus saviem vārdiem.",
    ]),
]
