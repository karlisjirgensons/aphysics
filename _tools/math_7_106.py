# -*- coding: utf-8 -*-
"""7. klase, 106. stunda: «Vai apgalvojums ir patiess?»

Apgalvojumu par vienādsānu un vienādmalu trijstūriem pārbauda divējādi:
patiesu pamato ar teorēmu, aplamu - atspēko ar vienu pretpiemēru. Stunda
trenē tieši šo spriešanu - to prasa eksāmena «patiess / aplams» uzdevumi.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, Zimejums, geometrija)

TEMA = "Vai apgalvojums ir patiess?"

MERKIS = ("Izvērtēsim apgalvojumus par vienādsānu un vienādmalu trijstūri "
          "un pamatosim atbildi.")

SATURS = [
    Sakums("«Katrs vienādsānu trijstūris ir šaurleņķa.» Patiess?",
           zimejums=geometrija([("A", 0, 0), ("C", 8, 0), ("B", 4, 1.5)],
                               nogriezni=["AB", "BC", "CA"],
                               svitras=[("AB", 1), ("BC", 1)],
                               lenki=[("ABC", "> 90°")]),
           paraksts="Pretpiemērs: vienādsānu platleņķa trijstūris.",
           fakti=["Pietiek ar vienu pretpiemēru, lai atspēkotu.",
                  "Lai pierādītu «katrs», vajag teorēmu, nevis piemērus."]),

    Doma("Pamato vai atspēko",
         "Vispārīgu apgalvojumu («katrs», «vienmēr») pierāda ar teorēmām. "
         "Lai to atspēkotu, pietiek ar vienu pretpiemēru.",
         soli=[
             "Izlasi apgalvojumu: vai tas ir «katrs» vai «eksistē»?",
             "Mēģini atrast pretpiemēru - arī dīvainu gadījumu.",
             "Ja atrodi - apgalvojums aplams.",
             "Ja neatrodi - meklē teorēmu, kas to pierāda.",
         ],
         pieze="«Eksistē» apgalvojumu («ir vienādsānu taisnleņķa "
               "trijstūris») pierāda ar vienu piemēru."),

    Paraugs("Izvērtē",
            uzd="«Ja trijstūrim divi leņķi ir 60°, tas ir vienādmalu.»",
            soli=[
                ("Trešais leņķis: 180° − 120° = 60°", "(leņķu summa)"),
                ("Visi leņķi vienādi", "60°, 60°, 60°."),
                ("Pret vienādiem leņķiem - vienādas malas",
                 "(sakarība starp malām un leņķiem)"),
                ("Visas malas vienādas", "Vienādmalu."),
            ],
            atbilde="Patiess."),

    Varianti("Patiess vai aplams?", [
        {"jaut": "Vienādmalu trijstūra visi leņķi ir 60°.",
         "opcijas": ["Patiess", "Aplams"], "pareizi": 0, "jaukt": False,
         "padoms": "180 : 3."},
        {"jaut": "Vienādsānu trijstūris var būt taisnleņķa.",
         "opcijas": ["Patiess", "Aplams"], "pareizi": 0, "jaukt": False,
         "padoms": "45°, 45°, 90°."},
        {"jaut": "Vienādmalu trijstūris var būt taisnleņķa.",
         "opcijas": ["Patiess", "Aplams"], "pareizi": 1, "jaukt": False,
         "padoms": "Visi leņķi 60°."},
        {"jaut": "Katrs vienādsānu trijstūris ir vienādmalu.",
         "opcijas": ["Patiess", "Aplams"], "pareizi": 1, "jaukt": False,
         "padoms": "5, 5, 8."},
        {"jaut": "Katrs vienādmalu trijstūris ir vienādsānu.",
         "opcijas": ["Patiess", "Aplams"], "pareizi": 0, "jaukt": False,
         "padoms": "Divas malas vienādas - ir."},
        {"jaut": "Vienādsānu trijstūrī leņķis pie pamata var būt 90°.",
         "opcijas": ["Patiess", "Aplams"], "pareizi": 1, "jaukt": False,
         "padoms": "Divi 90° - summa 180°."},
    ], pamats=4),

    Zimejums("Vienādsānu taisnleņķa - piemērs, kas eksistē",
             geometrija([("A", 0, 0), ("C", 4, 0), ("B", 0, 4)],
                        nogriezni=["AB", "BC", "CA"],
                        svitras=[("AB", 1), ("AC", 1)], taisni=["BAC"]),
             paskaidro="Viens piemērs pierāda «eksistē»."),

    Pasaule("Ziņu pārbaude",
            Varianti("", [
                {"jaut": "Reklāma: «Visi mūsu klienti ir apmierināti.» "
                         "Kā to atspēkot?",
                 "opcijas": ["Atrast vienu neapmierinātu klientu",
                             "Atrast 10 apmierinātus",
                             "Nevar atspēkot", "Pajautāt reklāmistam"],
                 "pareizi": 0, "padoms": "Pretpiemērs."},
                {"jaut": "«Daži kaķi ir melni.» Kā pierādīt?",
                 "opcijas": ["Parādīt vienu melnu kaķi",
                             "Pārbaudīt visus kaķus", "Nevar",
                             "Atrast baltu kaķi"],
                 "pareizi": 0, "padoms": "Eksistence - ar piemēru."},
                {"jaut": "«Šī tablete palīdz visiem» - kāpēc zinātnieki "
                         "šaubās?",
                 "opcijas": ["Pietiek ar vienu gadījumu, kad nepalīdz",
                             "Tabletes ir dārgas",
                             "Zinātnieki nekad netic",
                             "Tas ir patiess"],
                 "pareizi": 0, "padoms": "«Visiem» - stingrs apgalvojums."},
            ]),
            pavediens="dati",
            konteksts="Kritiskā domāšana ziņās un reklāmās ir tā pati "
                      "loģika, ko lieto matemātikā.",
            kapec="Pretpiemērs ir spēcīgākais arguments."),

    Kopsavilkums([
        "Atšķiru «katrs» un «eksistē» apgalvojumus.",
        "Atspēkoju ar vienu pretpiemēru.",
        "Pamatoju patiesu apgalvojumu ar teorēmu.",
        "Lietoju šo loģiku arī ārpus matemātikas.",
    ]),

    Majas([
        "Uzraksti 3 patiesus un 3 aplamus apgalvojumus par trijstūriem.",
        "Katram aplamajam uzzīmē pretpiemēru.",
        "Atrodi reklāmu ar «visi» un izdomā pretpiemēru.",
    ]),
]
