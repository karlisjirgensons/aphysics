# -*- coding: utf-8 -*-
"""2. klase, 122. stunda: «Kā uzzīmēt divreiz garāku?»

Divreiz garāks nogrieznis - divi dotie nogriežņi viens aiz otra. Divreiz
lielāks taisnstūris rūtiņās - divas dotās figūras blakus: tā laukums arī
divreiz lielāks.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, lineals, rutinas)

TEMA = "Kā uzzīmēt divreiz garāku?"

MERKIS = ("Šodien zīmēsim nogriezni un taisnstūri, kas ir divreiz garāks vai "
          "lielāks nekā dotais.")

SATURS = [
    Sakums("Kā uzzīmēt līniju divreiz garāku nekā 4 cm?",
           zimejums=lineals(10, [(0, 4, "4 cm"), (0, 8, "8 cm")]),
           paraksts="4 cm + 4 cm = 8 cm.",
           fakti=["Divreiz garāks - divi dotie viens aiz otra.",
                  "Garumu dubulto.",
                  "Taisnstūri dubulto, noliekot divus blakus."]),

    Doma("Dubultot zīmējumā",
         "Divreiz garāks = dotais + dotais.",
         soli=[
             "Izmēri doto nogriezni.",
             "Dubulto garumu: 4 + 4 = 8.",
             "Uzzīmē jauno nogriezni.",
             "Taisnstūrim: uzzīmē tādu pašu blakus - laukums dubultojas.",
         ]),

    Ievadi("Divreiz garāks", [
        {"jaut": "Dotais 3 cm. Divreiz garāks?", "atb": ["6"], "mers": "cm",
         "padoms": "3 + 3."},
        {"jaut": "Dotais 7 cm. Divreiz garāks?", "atb": ["14"], "mers": "cm",
         "padoms": "7 + 7."},
        {"jaut": "Dotais 4 cm 5 mm (45 mm). Divreiz garāks, mm?",
         "atb": ["90"], "mers": "mm", "padoms": "45 + 45."},
        {"jaut": "Divreiz garāks ir 16 cm. Cik garš dotais?", "atb": ["8"],
         "mers": "cm", "padoms": "Puse no 16."},
    ]),

    Varianti("Divreiz lielāks taisnstūris", [
        {"jaut": "Dotais taisnstūris - 6 rūtiņas. Cik rūtiņu divreiz "
                 "lielākajā?", "zim": rutinas(3, 2),
         "opcijas": ["12", "8", "6"], "pareizi": 0, "padoms": "6 + 6."},
        {"jaut": "Kā to uzzīmēt?", "zim": rutinas(6, 2),
         "opcijas": ["divus dotos blakus", "vienu rūtiņu vairāk",
                     "par 2 rūtiņām garāku"], "pareizi": 0,
         "padoms": "Tikpat un vēl tikpat."},
    ]),

    Petijums("Zīmē rūtiņu lapā", [
        "Uzzīmē nogriezni 5 cm.",
        "Zem tā - divreiz garāku.",
        "Uzzīmē taisnstūri 3 rūtiņas garu un 2 augstu.",
        "Blakus - divreiz lielāku. Saskaiti rūtiņas abos.",
    ], vajag="rūtiņu lapa, lineāls"),

    Pasaule("Galdauts lielākam galdam",
            Ievadi("", [
                {"jaut": "Galds ir 60 cm garš. Pieliekot otru tādu pašu, cik "
                         "garš kopā?", "atb": ["120"], "mers": "cm",
                 "padoms": "60 + 60."},
                {"jaut": "Vienam galdam vajag 4 krēslus. Cik krēslu diviem "
                         "galdiem?", "atb": ["8"], "padoms": "4 + 4."},
            ]),
            pavediens="maja",
            konteksts="Svētkos saliek divus vienādus galdus kopā.",
            kapec="Divreiz garāks galds - divreiz vairāk vietas."),

    Kopsavilkums([
        "Zīmēju divreiz garāku nogriezni.",
        "Zīmēju divreiz lielāku taisnstūri.",
        "Aprēķinu dubultoto garumu un rūtiņu skaitu.",
    ]),

    Majas([
        "Atrodi mājās divus priekšmetus, kur viens divreiz garāks.",
        "Izmēri un pārbaudi.",
        "Uzzīmē tos burtnīcā.",
    ]),
]
