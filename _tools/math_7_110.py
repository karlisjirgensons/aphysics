# -*- coding: utf-8 -*-
"""7. klase, 110. stunda: «Kā izmantot skici?»

Sarežģītākā uzdevumā skice ir domāšanas rīks: tajā atzīmē visu doto un
aprēķināto, un plāns redzams uzreiz. Stunda risina kombinētu leņķu
uzdevumu, katrā solī papildinot skici.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, geometrija)

TEMA = "Kā izmantot skici?"

MERKIS = ("Veidosim skici sarežģītākai situācijai un plānosim risinājuma "
          "soļus.")


def _sk(n):
    """Trijstūris ABC ar bisektrisi AD; leņķi parādās pa soļiem."""
    lenki = [("CAB", "80°" if n >= 1 else "")]
    if n >= 2:
        lenki = [("DAB", "40°"), ("CAD", "40°", 2)]
    if n >= 3:
        lenki += [("ABC", "60°")]
    if n >= 4:
        lenki += [("ADB", "80°", 3)]
    # C izvēlēts tā, ka ∠A = 80° un ∠B = 60°; D - bisektrises pamats.
    return geometrija([("A", 0, 0), ("B", 7, 0), ("C", 1.64, 9.29),
                       ("D", 4.72, 3.96, 20)],
                      nogriezni=["AB", "BC", "CA"], izcelti=["AD"],
                      lenki=lenki)


SATURS = [
    Sakums("Skice domā tavā vietā",
           zimejums=_sk(4),
           paraksts="Katrs aprēķinātais leņķis - uzreiz skicē.",
           fakti=["Galvā nevar paturēt 6 leņķus.",
                  "Skicē tie visi redzami.",
                  "Nākamais solis bieži «pats parādās»."]),

    Doma("Atzīmē visu, ko zini",
         "Risinot uzdevumu, skicē atzīmē ne tikai doto, bet arī katru "
         "aprēķināto lielumu. Tā redz, kurš trijstūris ir «gandrīz "
         "zināms» un kur ir nākamais solis.",
         soli=[
             "Uzzīmē skici ar visiem punktiem no teksta.",
             "Atzīmē doto (leņķus, vienādas malas).",
             "Atrodi trijstūri, kurā zināmi divi leņķi - aprēķini trešo.",
             "Ieraksti to skicē un atkārto.",
         ]),

    Slidnis("Risinājums skicē", [
        {"v": "1. solis", "teksts": "Dots: ∠A = 80°, ∠B = 60°, AD - "
                                    "bisektrise.", "zim": _sk(1)},
        {"v": "2. solis", "teksts": "Bisektrise: ∠DAB = ∠CAD = 40°.",
         "zim": _sk(2)},
        {"v": "3. solis", "teksts": "Atzīmē ∠B = 60°.", "zim": _sk(3)},
        {"v": "4. solis",
         "teksts": "△ABD: ∠ADB = 180° − 40° − 60° = 80°.", "zim": _sk(4)},
    ]),

    Paraugs("Pieraksts",
            uzd="Trijstūrī ABC ∠A = 80°, ∠B = 60°, AD - bisektrise (D ∈ BC). "
                "Atrodi ∠ADB un ∠ADC.",
            soli=[
                ("∠DAB = 80° : 2 = 40°", "(AD - bisektrise)"),
                ("∠ADB = 180° − 40° − 60° = 80°", "(leņķu summa △ABD)"),
                ("∠ADC = 180° − 80° = 100°", "(blakusleņķi)"),
                ("Pārbaude △ADC: 40° + 100° + ∠C = 180°, ∠C = 40°",
                 "Un ∠C = 180° − 80° − 60° = 40° ✓"),
            ],
            atbilde="∠ADB = 80°, ∠ADC = 100°"),

    Ievadi("Aprēķini ar skici", [
        {"jaut": "△ABC: ∠A = 70°, ∠B = 50°, CD - bisektrise. ∠ACD (°)?",
         "atb": ["30"], "padoms": "∠C = 60°, puse."},
        {"jaut": "Tajā pašā - ∠ADC (°)?",
         "atb": ["80"], "padoms": "180 − 70 − 30."},
        {"jaut": "△ABC: ∠A = 90°, ∠B = 40°, AH - augstums. ∠BAH (°)?",
         "atb": ["50"], "padoms": "△ABH: 180 − 90 − 40."},
        {"jaut": "Tajā pašā - ∠HAC (°)?",
         "atb": ["40"], "padoms": "90 − 50."},
    ]),

    Pasaule("Futbola sitiens",
            Ievadi("", [
                {"jaut": "Spēlētājs redz vārtu stabus leņķī 20°. Līnija uz "
                         "kreiso stabu veido ar vārtu līniju 70°. Kādu leņķi "
                         "ar vārtu līniju veido līnija uz labo stabu (iekšējo, "
                         "trijstūrī)?",
                 "atb": ["90"], "padoms": "180 − 70 − 20."},
                {"jaut": "Ja spēlētājs pieiet tuvāk, vārtu leņķis kļūst "
                         "lielāks vai mazāks? Raksti «lielāks» vai «mazāks».",
                 "atb": ["lielāks", "lielaks"],
                 "padoms": "Vārti «aizņem» vairāk redzes lauka.",
                 "tastatura": "text"},
            ]),
            pavediens="sports",
            konteksts="Sporta analītiķi skicē sitiena leņķi - jo lielāks "
                      "vārtu leņķis, jo vieglāk trāpīt.",
            kapec="Skice pārvērš laukumu trijstūros."),

    Kopsavilkums([
        "Veidoju skici un atzīmēju visu doto.",
        "Katru aprēķināto lielumu ierakstu skicē.",
        "Meklēju trijstūri ar diviem zināmiem leņķiem.",
        "Pārbaudu rezultātu citā trijstūrī.",
    ]),

    Majas([
        "△ABC: ∠A = 50°, ∠C = 70°, BD - bisektrise. Atrodi ∠BDC.",
        "Uzraksti risinājumu ar skici pa soļiem.",
        "Izdomā uzdevumu, kur skice ir obligāta.",
    ]),
]
