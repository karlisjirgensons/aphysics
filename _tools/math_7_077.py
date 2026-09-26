# -*- coding: utf-8 -*-
"""7. klase, 77. stunda: «Cik elementu jāzina, lai trijstūri būtu vienādi?»

Trijstūrim ir seši elementi, bet, lai to uzzīmētu viennozīmīgi, pietiek ar
trim pareizi izvēlētiem. Divi elementi nepietiek: ar divām malām var
uzzīmēt daudz dažādu trijstūru. Stunda to atklāj ar pretpiemēriem.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, Zimejums, geometrija)

TEMA = "Cik elementu jāzina, lai trijstūri būtu vienādi?"

MERKIS = ("Zīmēsim trijstūrus pēc diviem dotiem elementiem un secināsim, ka "
          "ar tiem nepietiek.")

SATURS = [
    Sakums("Divas malas - daudz trijstūru",
           zimejums=geometrija([("A", 0, 0), ("B", 5, 0), ("C", 1, 2.8),
                                ("_D", 2.12, 2.12)],
                               nogriezni=["AB", "AC", "BC"],
                               izcelti=[("A", "_D"), ("_D", "B")],
                               malas=[("AB", "5 cm")]),
           paraksts="AB = 5 cm, otra mala 3 cm - bet leņķis dažāds.",
           fakti=["Divas malas ir zināmas, leņķis starp tām - nē.",
                  "Pagriežot vienu malu, rodas cits trijstūris.",
                  "Tātad divi elementi nenosaka trijstūri."]),

    Doma("Vajag trīs elementus - un pareizos",
         "Divi elementi trijstūri nenosaka. Trīs elementi to nosaka, ja tie "
         "ir: divas malas un leņķis starp tām (mlm), trīs malas (mmm) vai "
         "mala un abi tās pieleņķi (lml).",
         soli=[
             "Mēģini uzzīmēt trijstūri pēc dotajiem elementiem.",
             "Pārbaudi: vai var uzzīmēt vēl vienu, citu?",
             "Ja var - ar šiem elementiem nepietiek.",
             "Ja trijstūris sanāk tikai viens - elementi to nosaka.",
         ],
         pieze="Trīs leņķi arī nepietiek: trijstūri ar leņķiem 60°, 60°, "
               "60° var būt jebkura izmēra."),

    Zimejums("Trīs leņķi - dažādi izmēri",
             geometrija([("A", 0, 0), ("B", 2, 0), ("C", 1, 1.73),
                         ("K", 3, 0), ("L", 7, 0), ("M", 5, 3.46)],
                        nogriezni=["AB", "BC", "CA", "KL", "LM", "MK"]),
             paskaidro="Abiem visi leņķi 60°, bet trijstūri nav vienādi."),

    Paraugs("Pretpiemērs",
            uzd="Pierādi, ka ar malu 4 cm un leņķi 50° nepietiek, lai "
                "trijstūris būtu noteikts.",
            soli=[
                ("Uzzīmē AB = 4 cm un ∠A = 50°", "Divi elementi."),
                ("Uz leņķa otras malas izvēlies C₁ 2 cm no A",
                 "Viens trijstūris."),
                ("Izvēlies C₂ 5 cm no A", "Otrs trijstūris."),
                ("△ABC₁ ≠ △ABC₂", "Pretpiemērs atrasts."),
            ],
            atbilde="Nepietiek - ir vismaz divi dažādi trijstūri."),

    Varianti("Pietiek vai nepietiek?", [
        {"jaut": "Divas malas 5 cm un 7 cm",
         "opcijas": ["Nepietiek", "Pietiek"], "pareizi": 0,
         "jaukt": False, "padoms": "Leņķis var mainīties."},
        {"jaut": "Trīs malas 5, 6 un 7 cm",
         "opcijas": ["Nepietiek", "Pietiek"], "pareizi": 1,
         "jaukt": False, "padoms": "mmm."},
        {"jaut": "Trīs leņķi 30°, 60°, 90°",
         "opcijas": ["Nepietiek", "Pietiek"], "pareizi": 0,
         "jaukt": False, "padoms": "Izmērs nav zināms."},
        {"jaut": "Malas 5 un 6 cm un leņķis starp tām 40°",
         "opcijas": ["Nepietiek", "Pietiek"], "pareizi": 1,
         "jaukt": False, "padoms": "mlm."},
    ], pamats=4),

    Pasaule("Tālvadības drona navigācija",
            Varianti("", [
                {"jaut": "Drons zina attālumu līdz 2 torņiem, bet ne "
                         "virzienu. Cik vietās tas var būt?",
                 "opcijas": ["Divās (simetriski)", "Vienā", "Bezgalīgi",
                             "Nevienā"],
                 "pareizi": 0,
                 "padoms": "Divi apļi krustojas 2 punktos."},
                {"jaut": "Kas vēl vajadzīgs precīzai vietai?",
                 "opcijas": ["Attālums līdz trešajam tornim",
                             "Drona krāsa", "Augstums virs jūras",
                             "Nekas"],
                 "pareizi": 0,
                 "padoms": "Tā strādā GPS."},
                {"jaut": "Kāpēc GPS vajag vismaz 3-4 satelītus?",
                 "opcijas": ["Ar mazāk attālumiem vieta nav viennozīmīga",
                             "Satelīti ir lēti", "Tā ir tradīcija",
                             "Viens salūzt"],
                 "pareizi": 0,
                 "padoms": "Kā trijstūrim - vajag pietiekami datu."},
            ]),
            pavediens="kosmoss",
            konteksts="GPS nosaka vietu no attālumiem līdz satelītiem - tas "
                      "ir «trijstūra noteikšanas» uzdevums.",
            kapec="Par maz datu - vairākas atbildes."),

    Kopsavilkums([
        "Zinu, ka divi elementi trijstūri nenosaka.",
        "Atrodu pretpiemēru ar diviem dažādiem trijstūriem.",
        "Zinu, ka trīs leņķi arī nepietiek.",
        "Zinu trīs gadījumus, kad trīs elementi pietiek.",
    ]),

    Majas([
        "Uzzīmē 3 dažādus trijstūrus ar malām 4 cm un 6 cm.",
        "Uzzīmē 2 dažādus trijstūrus ar leņķiem 40°, 60°, 80°.",
        "Paskaidro, kāpēc trīs leņķi nepietiek.",
    ]),
]
