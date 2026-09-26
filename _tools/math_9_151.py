# -*- coding: utf-8 -*-
"""9. klase, 151. stunda: «Kādi ir ievilktie leņķi uz viena loka?»

Ievilktie leņķi, kas balstās uz viena loka, ir vienādi (katrs - puse no
tā paša centra leņķa). Teātrī skatītāji uz vienas riņķa līnijas redz
skatuvi vienādā leņķī.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, geometrija, uz_rinka)

TEMA = "Kādi ir ievilktie leņķi uz viena loka?"

MERKIS = ("Lietosim īpašību, ka ievilktie leņķi uz viena loka ir vienādi.")

_ZIM = geometrija([("O", 0, 0, -90), uz_rinka("A", 210), uz_rinka("B", 330),
                   uz_rinka("C", 60), uz_rinka("D", 120)],
                  nogriezni=["CA", "CB", "DA", "DB"],
                  lenki=[("ACB", "α"), ("ADB", "α")], rinki=[("O", 5)])

SATURS = [
    Sakums("Divi skatītāji - viens leņķis",
           zimejums=_ZIM,
           paraksts="∠ACB = ∠ADB - abi balstās uz loka AB.",
           fakti=["Abi ir puse no ∠AOB.",
                  "Visi ievilktie leņķi uz viena loka ir vienādi.",
                  "Leņķi uz pretējiem lokiem kopā ir 180°."]),

    Doma("Leņķi uz viena loka",
         "Ievilktie leņķi, kas balstās uz viena un tā paša loka, ir vienādi.",
         soli=[
             "Atrodi loku (hordu), uz kura balstās leņķi.",
             "Pārliecinies, ka virsotnes ir vienā lokā pusē.",
             "Leņķi ir vienādi.",
             "Ja virsotnes ir pretējās pusēs - leņķu summa 180°.",
         ]),

    Ievadi("Aprēķini", [
        {"jaut": "∠ACB = 40°. ∠ADB (tā pati puse) = ?°", "atb": ["40"],
         "padoms": "Viens loks."},
        {"jaut": "Punkts E pretējā lokā. ∠AEB = ?°", "atb": ["140"],
         "padoms": "180 − 40."},
        {"jaut": "∠AOB = 96°. ∠ACB = ?°", "atb": ["48"], "padoms": "Puse."},
    ]),

    Varianti("Vienādi vai nē?", [
        {"jaut": "∠ACB un ∠ADB, C un D vienā pusē no AB.",
         "opcijas": ["Vienādi", "Kopā 180°", "Nevar zināt",
                     "Viens divreiz lielāks"],
         "pareizi": 0, "padoms": "Viens loks."},
        {"jaut": "Četrstūrī ACBD uz riņķa līnijas ∠C = 70°. ∠D (pretējais) = ?",
         "opcijas": ["110°", "70°", "140°", "35°"],
         "pareizi": 0, "padoms": "Pretējie leņķi kopā 180°."},
    ]),

    Pasaule("Teātra skatītāju zāle",
            Ievadi("", [
                {"jaut": "Skatuves platums redzams 30° leņķī no sēdvietas uz "
                         "riņķa līnijas caur skatuves malām. Cik grādu leņķī to "
                         "redz citā vietā uz tās pašas riņķa līnijas?",
                 "atb": ["30"], "padoms": "Viens loks."},
                {"jaut": "Centra leņķis (no apļa centra)?", "atb": ["60"],
                 "padoms": "Divreiz."},
            ]),
            pavediens="skola",
            konteksts="Senie amfiteātri sēdvietas izvietoja pa lokiem - "
                      "skatuve visiem redzama līdzīgā leņķī.",
            kapec="Ievilktie leņķi uz viena loka ir vienādi.",
            zimejums=_ZIM),

    Kopsavilkums([
        "Zinu: ievilktie leņķi uz viena loka ir vienādi.",
        "Lietoju: pretējās pusēs - summa 180°.",
        "Atrodu vienādus leņķus zīmējumā.",
    ]),

    Majas([
        "Uzzīmē loku un 3 ievilktos leņķus uz tā; izmēri.",
        "Pierādi: ievilktā četrstūra pretējo leņķu summa ir 180°.",
        "Atrodi zīmējumā visus vienādos leņķus četrstūrim uz riņķa līnijas.",
    ]),
]
