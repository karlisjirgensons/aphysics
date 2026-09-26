# -*- coding: utf-8 -*-
"""9. klase, 150. stunda: «Kā to pierādīt?»

Ievilktā leņķa teorēmas pierādījums gadījumā, kad viena mala iet caur
centru: △OBC ir vienādsānu, ārējais leņķis ∠AOB = 2∠C. Pārējos gadījumus
iegūst, novelkot diametru un saskaitot vai atņemot.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Pasaule, Sakums, Slidnis,
                         Varianti, geometrija, uz_rinka)

TEMA = "Kā to pierādīt?"

MERKIS = ("Iepazīsim ievilktā leņķa īpašības pierādījumu un atstāstīsim to.")

_P = [("O", 0, 0, -90), uz_rinka("A", 0), uz_rinka("B", 100),
      uz_rinka("C", 180)]


def _zim(lenki=(), iekrasot=()):
    return geometrija(_P, nogriezni=["CA", "CB", "OB"],
                      lenki=list(lenki), iekrasot=list(iekrasot),
                      rinki=[("O", 5)])


SATURS = [
    Sakums("Kāpēc tieši puse?",
           zimejums=_zim(lenki=[("ACB", "α"), ("AOB", "2α")]),
           paraksts="CA iet caur centru O - vienkāršākais gadījums.",
           fakti=["OB = OC - rādiusi.",
                  "△OBC ir vienādsānu.",
                  "Ārējais leņķis = divu iekšējo summa."]),

    Slidnis("Pierādījums soli pa solim", [
        {"v": "Dots", "teksts": "∠ACB ievilktais, CA iet caur O. Pierādīt: "
                                "∠AOB = 2∠ACB.",
         "zim": _zim()},
        {"v": "1", "teksts": "OB = OC (rādiusi) ⇒ △OBC vienādsānu, "
                             "∠OBC = ∠OCB = α.",
         "zim": _zim(lenki=[("OCB", "α"), ("OBC", "α")],
                     iekrasot=[("OBC", 1)])},
        {"v": "2", "teksts": "∠AOB - △OBC ārējais leņķis pie O.",
         "zim": _zim(lenki=[("AOB", "?")], iekrasot=[("OBC", 1)])},
        {"v": "3", "teksts": "Ārējais = divu nesaistīto iekšējo summa: "
                             "∠AOB = α + α = 2α ∎",
         "zim": _zim(lenki=[("ACB", "α"), ("AOB", "2α")])},
    ]),

    Doma("Pierādījuma ideja",
         "Vienādsānu trijstūris ar rādiusiem un ārējā leņķa īpašība dod "
         "∠AOB = 2∠ACB.",
         soli=[
             "Gadījums 1: viena mala - diametrs (pierādīts augstāk).",
             "Gadījums 2: centrs leņķa iekšpusē - novelk diametru, divu "
             "gadījumu 1 summa.",
             "Gadījums 3: centrs ārpusē - divu gadījumu 1 starpība.",
         ]),

    Varianti("Pierādījuma soļi", [
        {"jaut": "Kāpēc △OBC ir vienādsānu?",
         "opcijas": ["OB un OC - rādiusi", "BC = OB", "∠C = 90°",
                     "Tā izskatās"],
         "pareizi": 0, "padoms": "Rādiusi vienādi."},
        {"jaut": "Ārējais leņķis trijstūrim ir...",
         "opcijas": ["divu nesaistīto iekšējo leņķu summa",
                     "vienāds ar blakus iekšējo", "90°",
                     "trīs leņķu summa"],
         "pareizi": 0, "padoms": "Teorēma par ārējo leņķi."},
        {"jaut": "Ja centrs ir ievilktā leņķa iekšpusē, pierādījumā...",
         "opcijas": ["novelk diametru un saskaita divus gadījumus",
                     "neko nevar pierādīt", "leņķis ir 90°",
                     "leņķi atņem"],
         "pareizi": 0, "padoms": "Gadījums 2."},
    ]),

    Pasaule("Atstāsti draugam",
            Varianti("", [
                {"jaut": "Draugs saka: «Ievilktais leņķis ir puse, jo tā "
                         "zīmējumā izskatās.» Kas trūkst?",
                 "opcijas": ["Pamatojums ar vienādsānu trijstūri un ārējo "
                             "leņķi", "Nekas", "Mērījums ar lineālu",
                             "Formula no interneta"],
                 "pareizi": 0, "padoms": "Pierādījums, ne izskats."},
            ]),
            pavediens="skola",
            konteksts="Pierādījuma atstāstīšana ir labākais veids, kā to "
                      "saprast pašam.",
            kapec="Eksāmenā pamatojumu vērtē atsevišķi."),

    Kopsavilkums([
        "Atstāstu pierādījumu, ja viena mala ir diametrs.",
        "Zinu, kā rīkoties pārējos gadījumos.",
        "Lietoju ārējā leņķa īpašību.",
    ]),

    Majas([
        "Pieraksti pierādījumu burtnīcā ar zīmējumu.",
        "Pierādi gadījumu, kad centrs ir leņķa iekšpusē.",
        "Atstāsti pierādījumu kādam mājās.",
    ]),
]
