# -*- coding: utf-8 -*-
"""7. klase, 100. stunda: «Kādi ir trijstūru veidi pēc leņķiem?»

Pēc leņķiem trijstūri ir šaurleņķa (visi leņķi šauri), taisnleņķa (viens
taisns) un platleņķa (viens plats). No leņķu summas izriet, ka platu vai
taisnu leņķi trijstūrim var būt tikai viens.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, geometrija)

TEMA = "Kādi ir trijstūru veidi pēc leņķiem?"

MERKIS = ("Klasificēsim trijstūrus pēc leņķiem un pamatosim klasifikāciju.")


def _tr(cx, cy, uzr):
    return geometrija([("A", 0, 0), ("B", 6, 0), ("C", cx, cy)],
                      nogriezni=["AB", "BC", "CA"],
                      lenki=[("ACB", uzr)] if uzr != "90°" else [],
                      taisni=["ACB"] if uzr == "90°" else [])


SATURS = [
    Sakums("Šaurs, taisns vai plats - lielākais leņķis izšķir",
           zimejums=_tr(1.5, 1, "> 90°"),
           paraksts="Platleņķa trijstūris: ∠C > 90°.",
           fakti=["Pietiek paskatīties uz lielāko leņķi.",
                  "Divi leņķi vienmēr ir šauri.",
                  "Trešais nosaka veidu."]),

    Slidnis("Virsotne C pārvietojas", [
        {"v": "Šaurleņķa", "teksts": "Visi leņķi < 90°",
         "zim": _tr(3, 4, "")},
        {"v": "Taisnleņķa", "teksts": "∠C = 90°", "zim": _tr(3, 3, "90°")},
        {"v": "Platleņķa", "teksts": "∠C > 90°", "zim": _tr(3, 1.2, "")},
    ], ievads="Jo zemāk C, jo lielāks leņķis pie C."),

    Doma("Klasifikācija pēc leņķiem",
         "Trijstūri sauc par šaurleņķa, ja visi tā leņķi ir šauri; par "
         "taisnleņķa, ja viens leņķis ir taisns; par platleņķa, ja viens "
         "leņķis ir plats.",
         soli=[
             "Atrodi lielāko leņķi.",
             "< 90° - šaurleņķa.",
             "= 90° - taisnleņķa.",
             "> 90° - platleņķa.",
         ],
         pieze="Divu platu vai taisnu leņķu trijstūrim nav: to summa jau "
               "būtu vismaz 180°, un trešajam nepaliktu nekas."),

    Paraugs("Nosaki veidu",
            uzd="Trijstūrī ∠A = 35°, ∠B = 48°. Kāds tas ir pēc leņķiem?",
            soli=[
                ("∠C = 180° − 35° − 48° = 97°", "(leņķu summa)"),
                ("97° > 90°", "Plats leņķis."),
                ("Platleņķa trijstūris", "Secinājums."),
            ],
            atbilde="Platleņķa"),

    Varianti("Kāds trijstūris?", [
        {"jaut": "Leņķi 30°, 60°, 90°",
         "opcijas": ["Taisnleņķa", "Šaurleņķa", "Platleņķa"],
         "pareizi": 0, "jaukt": False, "padoms": "Ir 90°."},
        {"jaut": "Leņķi 50°, 60°, 70°",
         "opcijas": ["Taisnleņķa", "Šaurleņķa", "Platleņķa"],
         "pareizi": 1, "jaukt": False, "padoms": "Visi < 90°."},
        {"jaut": "∠A = 20°, ∠B = 40°",
         "opcijas": ["Taisnleņķa", "Šaurleņķa", "Platleņķa"],
         "pareizi": 2, "jaukt": False, "padoms": "∠C = 120°."},
        {"jaut": "∠A = 45°, ∠B = 45°",
         "opcijas": ["Taisnleņķa", "Šaurleņķa", "Platleņķa"],
         "pareizi": 0, "jaukt": False, "padoms": "∠C = 90°."},
    ], pamats=4),

    Ievadi("Aprēķini", [
        {"jaut": "Taisnleņķa trijstūrī viens šaurais leņķis 28°. Otrs (°)?",
         "atb": ["62"], "padoms": "90 − 28."},
        {"jaut": "Šaurleņķa trijstūrī ∠A = 50°. Lielākais iespējamais "
                 "vesels ∠B (°)?",
         "atb": ["89"], "padoms": "Arī ∠C jābūt < 90°: ∠B > 40°, ∠B < 90°."},
        {"jaut": "Vai trijstūris ar ∠A = 91° var būt vienādsānu? Raksti «jā» "
                 "vai «nē».",
         "atb": ["jā", "ja"], "padoms": "Ja ∠A virsotnē: 91 + 44,5 + 44,5."},
    ]),

    Pasaule("Kurš ir stabilākais?",
            Varianti("", [
                {"jaut": "Telts priekšpuse ir trijstūris ar leņķi augšā "
                         "120°. Kāds tas ir?",
                 "opcijas": ["Platleņķa", "Šaurleņķa", "Taisnleņķa"],
                 "pareizi": 0, "jaukt": False, "padoms": "> 90°."},
                {"jaut": "Kurā teltī vairāk vietas augšā?",
                 "opcijas": ["Ar šaurāku leņķi augšā (augstāka)",
                             "Ar platāku leņķi", "Vienādi", "Nav atšķirības"],
                 "pareizi": 0, "padoms": "Šaurāks leņķis - augstāka telts."},
                {"jaut": "Mājas stūra atbalsts veido ar sienu un grīdu "
                         "trijstūri. Kāds leņķis pie stūra?",
                 "opcijas": ["90° - taisnleņķa", "120°", "45°", "180°"],
                 "pareizi": 0, "padoms": "Siena ⊥ grīda."},
            ]),
            pavediens="celojums",
            konteksts="Telšu ražotāji izvēlas leņķi starp vietu iekšā un "
                      "vēja noturību.",
            kapec="Leņķis nosaka formu un īpašības."),

    Kopsavilkums([
        "Klasificēju trijstūrus pēc leņķiem.",
        "Nosaku veidu pēc lielākā leņķa.",
        "Pamatoju, kāpēc plats leņķis var būt tikai viens.",
        "Aprēķinu otru šauro leņķi taisnleņķa trijstūrī.",
    ]),

    Majas([
        "Uzzīmē visu trīs veidu trijstūrus.",
        "Atrodi dzīvē visu trīs veidu trijstūrus.",
        "Vai var būt taisnleņķa vienādsānu trijstūris? Uzzīmē.",
    ]),
]
