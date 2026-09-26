# -*- coding: utf-8 -*-
"""7. klase, 78. stunda: «Kāda ir pazīme mlm?»

Pirmā trijstūru vienādības pazīme: ja viena trijstūra divas malas un leņķis
starp tām ir attiecīgi vienādi ar otra trijstūra divām malām un leņķi starp
tām, tad trijstūri ir vienādi. Svarīgi - leņķis ir tieši starp malām.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, Zimejums, geometrija)

TEMA = "Kāda ir pazīme mlm?"

MERKIS = ("Formulēsim un lietosim pirmo trijstūru vienādības pazīmi "
          "(mlm).")

_MLM = geometrija([("A", 0, 0), ("B", 5, 0), ("C", 1.5, 3),
                   ("K", 7, 0), ("L", 12, 0), ("M", 8.5, 3)],
                  nogriezni=["AB", "BC", "CA", "KL", "LM", "MK"],
                  svitras=[("AB", 1), ("KL", 1), ("AC", 2), ("KM", 2)],
                  lenki=[("BAC", ""), ("LKM", "")])

SATURS = [
    Sakums("Mala - leņķis - mala",
           zimejums=_MLM,
           paraksts="AB = KL, AC = KM, ∠A = ∠K - trijstūri vienādi.",
           fakti=["Leņķis «saslēdz» abas malas savā vietā.",
                  "Trešā mala tad var būt tikai viena.",
                  "Tā ir kā šķēres: atvērums nosaka attālumu starp galiem."]),

    Doma("Pazīme mlm",
         "Ja viena trijstūra divas malas un leņķis starp tām ir attiecīgi "
         "vienādi ar otra trijstūra divām malām un leņķi starp tām, tad šie "
         "trijstūri ir vienādi.",
         soli=[
             "Atrodi divas vienādu malu pārus.",
             "Pārbaudi, vai vienādais leņķis ir STARP šīm malām.",
             "Uzraksti: △ABC = △KLM (mlm).",
             "Secini par pārējiem elementiem.",
         ],
         pieze="Ja vienādais leņķis nav starp malām, pazīme mlm neder - un "
               "trijstūri var nebūt vienādi."),

    Paraugs("Lieto pazīmi",
            uzd="Nogriežņi AB un CD krustojas punktā O, AO = OB, CO = OD. "
                "Pierādi, ka △AOC = △BOD.",
            soli=[
                ("AO = OB", "(dots)"),
                ("CO = OD", "(dots)"),
                ("∠AOC = ∠BOD", "(krustleņķi)"),
                ("△AOC = △BOD", "(mlm)"),
            ],
            atbilde="Pierādīts pēc pazīmes mlm."),

    Zimejums("Krustojošies nogriežņi",
             geometrija([("A", 0, 3), ("B", 6, -3), ("C", 0, -1.5),
                         ("D", 6, 1.5), ("O", 3, 0, 90)],
                        nogriezni=["AB", "CD", "AC", "BD"],
                        svitras=[("AO", 1), ("OB", 1), ("CO", 2),
                                 ("OD", 2)],
                        lenki=[("AOC", ""), ("BOD", "")]),
             paskaidro="Krustleņķi pie O ir vienādi - tie ir starp malām."),

    Varianti("Vai der mlm?", [
        {"jaut": "AB = KL, BC = LM, ∠B = ∠L.",
         "opcijas": ["Der - ∠B ir starp AB un BC", "Neder"],
         "pareizi": 0, "jaukt": False, "padoms": "Leņķis B ir starp."},
        {"jaut": "AB = KL, BC = LM, ∠A = ∠K.",
         "opcijas": ["Der", "Neder - ∠A nav starp AB un BC"],
         "pareizi": 1, "jaukt": False, "padoms": "Starp tām ir ∠B."},
        {"jaut": "AC = KM, AB = KL, ∠A = ∠K.",
         "opcijas": ["Der", "Neder"],
         "pareizi": 0, "jaukt": False, "padoms": "∠A starp AB un AC."},
        {"jaut": "Pēc mlm △ABC = △KLM. Kas vēl ir vienāds?",
         "opcijas": ["BC = LM, ∠B = ∠L, ∠C = ∠M",
                     "Tikai BC = LM", "Nekas", "Tikai leņķi"],
         "pareizi": 0, "padoms": "Visi atbilstošie elementi."},
    ], pamats=4),

    Pasaule("Saliekamā kāpne",
            Varianti("", [
                {"jaut": "Divām kāpnēm kājas ir 2 m garas un atvērtas 30° "
                         "leņķī. Vai attālums starp kāju galiem ir vienāds?",
                 "opcijas": ["Jā - trijstūri vienādi pēc mlm",
                             "Nē", "Tikai, ja kāpnes jaunas",
                             "Nevar zināt"],
                 "pareizi": 0,
                 "padoms": "Divas malas un leņķis starp tām."},
                {"jaut": "Kāpēc kāpnēm ir ķēdīte starp kājām?",
                 "opcijas": ["Tā fiksē leņķi - trijstūris kļūst noteikts",
                             "Rotājumam", "Lai būtu smagākas",
                             "Lai varētu pakārt"],
                 "pareizi": 0,
                 "padoms": "Ķēde fiksē trešo malu."},
                {"jaut": "Ja leņķi atver vairāk, attālums starp kājām...",
                 "opcijas": ["palielinās", "samazinās", "nemainās",
                             "kļūst 0"],
                 "pareizi": 0,
                 "padoms": "Šķēres."},
            ]),
            pavediens="maja",
            konteksts="Saliekamās kāpnes ir trijstūris ar divām fiksētām "
                      "malām un maināmu leņķi.",
            kapec="mlm: fiksē leņķi - fiksē visu."),

    Kopsavilkums([
        "Formulēju pazīmi mlm.",
        "Pārbaudu, vai leņķis ir starp malām.",
        "Lietoju krustleņķus kā vienādus leņķus pierādījumā.",
        "Pierakstu pierādījumu ar pamatojumiem.",
    ]),

    Majas([
        "Uzzīmē divus trijstūrus pēc mlm un pārbaudi, ka tie sakrīt.",
        "Uzzīmē pretpiemēru: divas malas un leņķis, kas nav starp tām.",
        "Uzraksti pierādījumu no atmiņas.",
    ]),
]
