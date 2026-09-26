# -*- coding: utf-8 -*-
"""8. klase, 112. stunda: «Kā dala monomus?»

Bloka noslēgums: koeficientus dala, kāpinātājus atņem (a^m : a^n =
a^{m − n}). Dalījums ir monoms tikai tad, ja katrs burts dalāmajā ir
vismaz tādā pašā pakāpē kā dalītājā - citādi burts paliek saucējā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, restis)

TEMA = "Kā dala monomus?"

MERKIS = "Dalīsim monomus un paskaidrosim, kad dalījums ir monoms."

_T = "text"

SATURS = [
    Sakums("12a⁵b : 3a² = ?",
           zimejums=restis([["12 : 3", "a⁵ : a²", "b"],
                            ["4", "a³", "b"]]),
           paraksts="Rezultāts: 4a^3b.",
           fakti=["Koeficientus dala.",
                  "Vienādiem burtiem kāpinātājus atņem.",
                  "Ja burts paliek saucējā, dalījums nav monoms."]),

    Doma("Monomu dalīšana",
         "Dalīšana ir apgriezta reizināšanai.",
         soli=[
             "Izdali koeficientus.",
             "Katram burtam atņem kāpinātājus: a^m : a^n = a^{m − n}.",
             "Ja kāpinātāji vienādi, burts pazūd (a^0 = 1).",
             "Pārbaudi: dalījums · dalītājs = dalāmais.",
         ],
         pieze="6x^2 : 3x^5 = {2|x^3} - tas nav monoms."),

    Paraugs("Izdali",
            uzd="Aprēķini −15x^4y^2 : 5x^3y un pārbaudi.",
            soli=[
                ("−15 : 5 = −3", "Koeficients."),
                ("x^{4 − 3} = x; y^{2 − 1} = y", "Burti."),
                ("−3xy", "Dalījums."),
                ("−3xy · 5x^3y = −15x^4y^2", "Pārbaude."),
            ],
            atbilde="−3xy"),

    Ievadi("Izdali (normālformā)", [
        {"jaut": "12a^5 : 3a^2", "atb": ["4a^3"], "tastatura": _T,
         "padoms": "12 : 3; 5 − 2."},
        {"jaut": "8a^3b : 2a^3", "atb": ["4b"], "tastatura": _T,
         "padoms": "a pazūd."},
        {"jaut": "6x^2 : 6x^2", "atb": ["1"], "padoms": "Viss saīsinās."},
        {"jaut": "20a^4b^3 : (−4ab^3)", "atb": ["−5a^3", "-5a^3"],
         "tastatura": _T, "padoms": "20 : (−4); 4 − 1."},
        {"jaut": "−9x^6 : (−3x^2)", "atb": ["3x^4"], "tastatura": _T,
         "padoms": "Mīnuss dalīts ar mīnusu."},
        {"jaut": "x^7y^2 : x^2y^2", "atb": ["x^5"], "tastatura": _T,
         "padoms": "y pazūd."},
    ], pamats=4),

    Varianti("Spried", [
        {"jaut": "Vai 6x^2 : 3x^5 ir monoms?",
         "opcijas": ["Nē - x paliek saucējā", "Jā", "Tikai ja x = 1",
                     "Jā, 2x^3"],
         "pareizi": 0, "padoms": "2 − 5 < 0."},
        {"jaut": "a^8 : a^2 = ?",
         "opcijas": ["a^6", "a^4", "a^10", "a^16"],
         "pareizi": 0, "padoms": "Atņem."},
        {"jaut": "Kā pārbaudīt dalījumu?",
         "opcijas": ["Sareizināt ar dalītāju", "Saskaitīt ar dalītāju",
                     "Kāpināt kvadrātā", "Nevar pārbaudīt"],
         "pareizi": 0, "padoms": "Dalījums · dalītājs = dalāmais."},
    ]),

    Pasaule("Otra mala",
            Ievadi("", [
                {"jaut": "Taisnstūra laukums 24x^3, viena mala 6x. Otra mala "
                         "= ?x^2",
                 "atb": ["4"], "padoms": "24x^3 : 6x."},
                {"jaut": "Kvadrāta laukums 49a^2. Mala = ?a",
                 "atb": ["7"], "padoms": "7a · 7a."},
                {"jaut": "Kuba tilpums 64x^3. Šķautne = ?x",
                 "atb": ["4"], "padoms": "4^3 = 64."},
            ]),
            pavediens="maja",
            konteksts="Zinot laukumu un vienu malu, otru atrod, dalot "
                      "monomus.",
            kapec="Dalīšana ir apgriezta reizināšanai."),

    Kopsavilkums([
        "Dalu monomus.",
        "Lietoju a^m : a^n = a^{m − n}.",
        "Paskaidroju, kad dalījums nav monoms.",
    ]),

    Majas([
        "Izdali: 18x^5 : 6x^2; −10a^3b : 5ab.",
        "Pārbaudi katru dalījumu ar reizināšanu.",
        "Izdomā dalījumu, kas nav monoms.",
    ]),
]
