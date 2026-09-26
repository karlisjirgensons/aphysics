# -*- coding: utf-8 -*-
"""9. klase, 171. stunda: «Kā risinu ģeometrijas uzdevumus?»

Eksāmena ģeometrijas daļa (2025. gada 14.-24. uzdevuma formāts): leņķi,
trijstūri, Pitagora teorēma, līdzība, trigonometrija, trapece, riņķa
līnija. Izvērstajā uzdevumā katram apgalvojumam - pamatojums.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, geometrija)

TEMA = "Kā risinu ģeometrijas uzdevumus?"

MERKIS = ("Risināsim eksāmena formāta ģeometrijas uzdevumus un noformēsim "
          "pamatojumu.")

_KAPNES = geometrija([("C", 0, 0, -135), ("A", 1.4, 0, -45),
                      ("B", 0, 4.8, 135)],
                     nogriezni=["CA", "AB", "BC"], taisni=["ACB"],
                     malas=[("AB", "5 m"), ("CA", "1,4 m"), ("BC", "?")])

_LENKIS = geometrija([("A", -5, 0, 180), ("O", 0, 0, -90), ("K", 5, 0, 0),
                      ("B", 3.21, 3.83, 50)],
                     nogriezni=["AK"], stari=["OB"],
                     lenki=[("AOB", "130°"), ("BOK", "?")])

SATURS = [
    Sakums("Eksāmena ģeometrija - no leņķa līdz riņķa līnijai",
           zimejums=_LENKIS,
           paraksts="Stars OB dala izstieptu leņķi: ∠BOK = 180° − 130°.",
           fakti=["Zīmējumā atzīmē visu doto.",
                  "Katram solim - pamatojums: «jo ...».",
                  "Formulu lapā ir Pitagors, sin, cos, tg un laukumi."]),

    Doma("Ģeometrijas uzdevuma kārtība",
         "Vispirms zīmējums un dotais, tad sakarība ar pamatojumu, tad "
         "aprēķins.",
         soli=[
             "Pārzīmē vai papildini zīmējumu, atzīmē dotos lielumus.",
             "Atrodi figūru, kurā sakarība der: taisnleņķa, līdzīgi, "
             "ievilkts.",
             "Uzraksti sakarību un pamatojumu.",
             "Aprēķini un pārbaudi, vai atbilde ir saprātīga.",
         ]),

    Paraugs("Pamatojums (2 punkti)",
            uzd="△ABC ir vienādsānu, AB = BC, ∠A = 40°. Aprēķini ∠B.",
            soli=[
                ("∠C = ∠A = 40°", "Jo vienādsānu trijstūrī leņķi pie "
                                  "pamata ir vienādi."),
                ("∠B = 180° − 40° − 40°", "Jo trijstūra leņķu summa ir 180°."),
                ("∠B = 100°", "Aprēķins."),
            ],
            atbilde="∠B = 100°"),

    Ievadi("Aprēķini", [
        {"jaut": "∠AOB = 130° (zīmējumā). ∠BOK = ?°", "atb": ["50"],
         "padoms": "Blakusleņķi."},
        {"jaut": "Katetes 5 un 12. Hipotenūza?", "atb": ["13"],
         "padoms": "√(25 + 144)."},
        {"jaut": "Trapeces pamati 6 un 10. Viduslīnija?", "atb": ["8"],
         "padoms": "(6 + 10) : 2."},
        {"jaut": "Hipotenūza 10, leņķis 30°. Pretējā katete?", "atb": ["5"],
         "padoms": "10 · sin 30°."},
        {"jaut": "Līdzīgi trijstūri, k = 3. Mazākā perimetrs 12. Lielākā?",
         "atb": ["36"], "padoms": "12 · 3."},
        {"jaut": "Ievilktais leņķis 35°. Centra leņķis uz tā paša loka?",
         "atb": ["70"], "padoms": "Divreiz."},
    ]),

    Varianti("Kura sakarība der?", [
        {"jaut": "Zināma katete un pretējais leņķis, jāatrod hipotenūza.",
         "opcijas": ["sin α", "cos α", "tg α", "Pitagors"],
         "pareizi": 0, "padoms": "sin = pretējā : hipotenūza."},
        {"jaut": "Zināmas divas malas taisnleņķa trijstūrī, jāatrod trešā.",
         "opcijas": ["Pitagors", "sin α", "līdzība", "viduslīnija"],
         "pareizi": 0, "padoms": "Leņķis nav vajadzīgs."},
        {"jaut": "Ēna un augstums diviem priekšmetiem saulainā dienā.",
         "opcijas": ["līdzība", "Pitagors", "ievilktais leņķis", "tg 45°"],
         "pareizi": 0, "padoms": "Vienādi leņķi - līdzīgi trijstūri."},
    ]),

    Pasaule("Kāpnes pie sienas",
            Ievadi("", [
                {"jaut": "Kāpnes 5 m, apakšgals 1,4 m no sienas. Cik augstu "
                         "(m) kāpnes sniedzas?", "atb": ["4,8"],
                 "padoms": "√(25 − 1,96)."},
                {"jaut": "Kāpņu leņķis ar zemi: cos α = ? (decimāldaļa)",
                 "atb": ["0,28"], "padoms": "1,4 : 5."},
            ]),
            pavediens="maja",
            konteksts="Siena un zeme veido taisnu leņķi; kāpnes - "
                      "hipotenūza.",
            kapec="Tipisks 2. daļas uzdevums: dzīves situācija, taisnleņķa "
                  "trijstūris un pamatojums.",
            zimejums=_KAPNES),

    Pasaule("Koka augstums pēc ēnas",
            Ievadi("", [
                {"jaut": "2 m stabs met 3 m ēnu, koks - 18 m ēnu. Koka "
                         "augstums (m)?", "atb": ["12"],
                 "padoms": "{2|3} = {h|18}."},
            ]),
            pavediens="daba",
            konteksts="Tajā pašā brīdī saules stari krīt vienā leņķī uz abiem "
                      "priekšmetiem.",
            kapec="Līdzīgi trijstūri - viena proporcija."),

    Kopsavilkums([
        "Atzīmēju doto zīmējumā un izvēlos sakarību.",
        "Katram solim rakstu pamatojumu.",
        "Risinu eksāmena formāta ģeometrijas uzdevumus.",
    ]),

    Majas([
        "Atrisini iepriekšējā gada eksāmena ģeometrijas uzdevumus.",
        "Uzraksti pamatojumu vienam uzdevumam katrā tematā: trijstūris, "
        "trapece, riņķa līnija.",
        "Izmēri ēnas un aprēķini kāda augsta priekšmeta augstumu.",
    ]),
]
