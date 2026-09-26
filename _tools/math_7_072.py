# -*- coding: utf-8 -*-
"""7. klase, 72. stunda: «Cik garš var būt trešais nogrieznis?»

Ja divas malas ir a un b, trešā mala c ir starp to starpību un summu:
|a − b| < c < a + b. Stunda to iegūst no trijstūra nevienādības un parāda
ar skici, kā trijstūris «atveras» un «saplok».
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         geometrija, taisne)

TEMA = "Cik garš var būt trešais nogrieznis?"

MERKIS = ("Noteiksim trešās malas iespējamo garumu, ja divas malas ir "
          "zināmas; lietosim skici.")


def _atvere(grads):
    """Malas 5 un 3 no virsotnes A; leņķis starp tām mainās."""
    import math
    a = math.radians(grads)
    return geometrija([("A", 0, 0), ("B", 5, 0),
                       ("C", 3 * math.cos(a), 3 * math.sin(a))],
                      nogriezni=["AB", "AC"], izcelti=["BC"],
                      malas=[("AB", "5"), ("AC", "3")])


SATURS = [
    Sakums("Malas 5 cm un 3 cm - kāda var būt trešā?",
           zimejums=_atvere(60),
           paraksts="Atverot leņķi, trešā mala aug.",
           fakti=["Leņķis gandrīz 0° - trešā mala gandrīz 5 − 3 = 2 cm.",
                  "Leņķis gandrīz 180° - gandrīz 5 + 3 = 8 cm.",
                  "Tātad 2 < c < 8."]),

    Slidnis("Atver leņķi", [
        {"v": "gandrīz 0°", "teksts": "c ≈ 2 cm", "zim": _atvere(8)},
        {"v": "60°", "teksts": "c ≈ 4,4 cm", "zim": _atvere(60)},
        {"v": "120°", "teksts": "c = 7 cm", "zim": _atvere(120)},
        {"v": "gandrīz 180°", "teksts": "c ≈ 8 cm", "zim": _atvere(172)},
    ]),

    Doma("Starp starpību un summu",
         "Ja trijstūra divas malas ir a un b (a ≥ b), trešā mala c atbilst "
         "nevienādībai a − b < c < a + b.",
         soli=[
             "Aprēķini summu a + b - augšējā robeža.",
             "Aprēķini starpību a − b - apakšējā robeža.",
             "Robežas neieskaita - tad trijstūris saplok.",
             "Uzraksti: a − b < c < a + b.",
         ]),

    Paraugs("Atrodi robežas",
            uzd="Trijstūra malas ir 7 cm un 12 cm. Kāda var būt trešā mala? "
                "Cik veselu centimetru garumu iespējams?",
            soli=[
                ("12 − 7 < c < 12 + 7", "Nevienādība."),
                ("5 < c < 19", "Robežas."),
                ("Veseli: 6; 7; ...; 18", "Neieskaitot 5 un 19."),
                ("18 − 6 + 1 = 13", "Saskaita."),
            ],
            atbilde="5 cm < c < 19 cm; 13 veselu garumu"),

    Zimejums("5 < c < 19",
             taisne(0, 20, 5, intervali=[(5, 19, False, False)], sikas=5),
             paskaidro="Tukši aplīši - robežas neieskaita."),

    Ievadi("Aprēķini", [
        {"jaut": "Malas 4 cm un 9 cm. Mazākā robeža c (cm)?",
         "atb": ["5"], "padoms": "9 − 4."},
        {"jaut": "Malas 4 cm un 9 cm. Lielākā robeža c (cm)?",
         "atb": ["13"], "padoms": "9 + 4."},
        {"jaut": "Malas 4 cm un 9 cm. Cik veselu c vērtību?",
         "atb": ["7"], "padoms": "6; 7; ...; 12."},
        {"jaut": "Vienādsānu trijstūrim sānu malas 5 cm. Lielākais vesels "
                 "pamats (cm)?",
         "atb": ["9"], "padoms": "Mazāk par 10."},
    ]),

    Varianti("Spried", [
        {"jaut": "Malas 10 un 10. Kura trešā mala nav iespējama?",
         "opcijas": ["20", "1", "19,9", "10"],
         "pareizi": 0,
         "padoms": "Jābūt mazāk par 20."},
        {"jaut": "Malas 6 un 2. Kura trešā mala ir iespējama?",
         "opcijas": ["5", "3", "4", "8"],
         "pareizi": 0,
         "padoms": "4 < c < 8."},
    ]),

    Pasaule("Wi-Fi tīkla attālums",
            Ievadi("", [
                {"jaut": "No rūtera līdz tev 12 m, līdz drauga telefonam - "
                         "5 m. Lielākais iespējamais attālums starp jums "
                         "(m)?",
                 "atb": ["17"], "padoms": "Ja esat pretējās pusēs."},
                {"jaut": "Mazākais iespējamais attālums (m)?",
                 "atb": ["7"], "padoms": "Ja esat vienā virzienā."},
                {"jaut": "Bluetooth darbojas līdz 10 m. Vai jūs noteikti "
                         "varat savienoties? Raksti «jā» vai «nē».",
                 "atb": ["nē", "ne"], "padoms": "Attālums var būt līdz 17 m."},
            ]),
            pavediens="dati",
            konteksts="Tīkla plānotāji novērtē attālumus starp ierīcēm ar "
                      "trijstūra nevienādību.",
            kapec="Robežas - pat nezinot precīzu vietu."),

    Kopsavilkums([
        "Aprēķinu trešās malas robežas: a − b < c < a + b.",
        "Nosaku iespējamo veselo garumu skaitu.",
        "Attēloju robežas uz skaitļu taisnes.",
        "Zinu, ka robežas neieskaita.",
    ]),

    Majas([
        "Malas 6 cm un 15 cm: kāda var būt trešā?",
        "Uzzīmē trīs trijstūrus ar malām 5 un 3 un dažādām trešajām.",
        "Izdomā uzdevumu par attālumu starp trim pilsētām.",
    ]),
]
