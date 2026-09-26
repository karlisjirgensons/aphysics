# -*- coding: utf-8 -*-
"""7. klase, 111. stunda: «Kur ģeometrija noder dzīvē?»

Tematu noslēdz praktiski uzdevumi: jumta slīpums, ielu krustojumi, saules
paneļi un kāpnes. Katrā - leņķu summa, paralēlas taisnes vai vienādsānu
trijstūris, tikai ar īstiem skaitļiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         geometrija)

TEMA = "Kur ģeometrija noder dzīvē?"

MERKIS = ("Lietosim leņķu sakarības praktiskās situācijās: jumts, "
          "maršruts, konstrukcija.")

_JUMTS = geometrija([("A", 0, 0), ("B", 8, 0), ("C", 4, 3)],
                    nogriezni=["AB", "BC", "CA"],
                    svitras=[("AC", 1), ("BC", 1)],
                    lenki=[("CAB", "37°"), ("ACB", "?")],
                    malas=[("AB", "8 m")])

SATURS = [
    Sakums("Jumts, ceļš un tilts - visur leņķi",
           zimejums=_JUMTS,
           paraksts="Frontons: slīpums 37°, kores leņķis ?",
           fakti=["Jumta kores leņķis = 180° − 2 · 37° = 106°.",
                  "Būvnieki leņķus aprēķina, pirms zāģē.",
                  "Viena kļūda - jumts nesaskan kopā."]),

    Doma("Modelē ar ģeometriju",
         "Praktiskā uzdevumā vispirms atrod ģeometrisko modeli - trijstūri, "
         "paralēlas taisnes, leņķi - tad lieto zināmās īpašības un "
         "rezultātu pārbauda ar veselo saprātu.",
         soli=[
             "Uzzīmē situācijas skici ar ģeometriskām figūrām.",
             "Atpazīsti: vienādsānu? paralēlas? taisns leņķis?",
             "Aprēķini ar īpašībām.",
             "Pārbaudi: vai atbilde ir reāla?",
         ]),

    Paraugs("Rampa ratiņkrēslam",
            uzd="Noteikumi: rampas slīpums ne vairāk kā 5°. Rampa sākas pie "
                "ēkas, kur siena ir vertikāla. Kādu leņķi rampa veido ar "
                "sienu?",
            soli=[
                ("Siena ⊥ zeme: 90°", "Taisns leņķis."),
                ("Rampa, siena un zeme - taisnleņķa trijstūris",
                 "Modelis."),
                ("Leņķis pie sienas: 90° − 5° = 85°",
                 "(šaurie leņķi kopā 90°)"),
            ],
            atbilde="85° (vai vairāk, ja slīpums mazāks)"),

    Ievadi("Praktiski aprēķini", [
        {"jaut": "Frontona slīpums 45° abās pusēs. Kores leņķis (°)?",
         "atb": ["90"], "padoms": "180 − 90."},
        {"jaut": "Saules panelis pret zemi 40°, balsts ⊥ panelim. Balsta "
                 "leņķis pret zemi (°)?",
         "atb": ["50"], "padoms": "Taisnleņķa trijstūris."},
        {"jaut": "Divas paralēlas ielas krusto aleja 65° leņķī. Šķērsleņķis "
                 "pie otras ielas (°)?",
         "atb": ["65"], "padoms": "Šķērsleņķi."},
        {"jaut": "Karuselim 12 vienādi sektori. Leņķis starp blakus "
                 "sēdekļiem no centra (°)?",
         "atb": ["30"], "padoms": "360 : 12."},
    ]),

    Petijums("Izmēri jumtu",
             ["Nofotografē mājas frontonu tieši no priekšas.",
              "Izdrukā vai uzzīmē kontūru.",
              "Izmēri abus leņķus pie pamata.",
              "Aprēķini kores leņķi un pārbaudi ar transportieri."],
             vajag="telefons, transportieris, lineāls",
             secinajums="Latvijā jumtu slīpums parasti 30°-45° - lai sniegs "
                         "noslīdētu."),

    Varianti("Kurš modelis?", [
        {"jaut": "Kāpnes pie sienas",
         "opcijas": ["Taisnleņķa trijstūris", "Paralēlas taisnes",
                     "Vienādmalu trijstūris", "Aplis"],
         "pareizi": 0, "padoms": "Siena ⊥ zeme."},
        {"jaut": "Dzelzceļa sliedes un pārbrauktuve",
         "opcijas": ["Paralēlas taisnes un krustotājs",
                     "Taisnleņķa trijstūris", "Aplis",
                     "Vienādsānu trijstūris"],
         "pareizi": 0, "padoms": "Sliedes paralēlas."},
        {"jaut": "Simetrisks jumts",
         "opcijas": ["Vienādsānu trijstūris", "Paralēlas taisnes",
                     "Kvadrāts", "Aplis"],
         "pareizi": 0, "padoms": "Vienādas slīpās malas."},
    ]),

    Pasaule("Lidostas skrejceļi",
            Ievadi("", [
                {"jaut": "Skrejceļš vērsts 180° (uz dienvidiem). Vējš pūš "
                         "no 150°. Leņķis starp skrejceļu un vēju (°)?",
                 "atb": ["30"], "padoms": "180 − 150."},
                {"jaut": "Skrejceļu numurē ar virzienu : 10. Kāds numurs "
                         "virzienam 180°?",
                 "atb": ["18"], "padoms": "180 : 10."},
                {"jaut": "Pretējais virziens tam pašam skrejceļam ir "
                         "180° + 180° = 360°. Kāds tā numurs?",
                 "atb": ["36"], "padoms": "360 : 10."},
            ]),
            pavediens="celojums",
            konteksts="Rīgas lidostas skrejceļš ir 18/36 - pēc virziena "
                      "grādiem, dalītiem ar 10.",
            kapec="Leņķi ir aviācijas valoda."),

    Zimejums("Kāpnes: taisnleņķa trijstūris",
             geometrija([("A", 0, 0), ("B", 5, 0), ("C", 5, 3.64)],
                        nogriezni=["AB", "BC", "CA"], taisni=["ABC"],
                        lenki=[("BAC", "36°"), ("ACB", "54°")]),
             paskaidro="Kāpņu slīpums 36° - ērts solis."),

    Kopsavilkums([
        "Atrodu ģeometrisko modeli praktiskā situācijā.",
        "Lietoju leņķu summu, paralēlas taisnes un vienādsānu trijstūri.",
        "Pārbaudu atbildes reālumu.",
        "Redzu ģeometriju būvniecībā, satiksmē un tehnikā.",
    ]),

    Majas([
        "Nofotografē 3 ģeometriskus objektus pilsētā un aprēķini leņķus.",
        "Izmēri kāpņu slīpumu savās mājās.",
        "Uzraksti vienu praktisku uzdevumu ar leņķiem.",
    ]),
]
