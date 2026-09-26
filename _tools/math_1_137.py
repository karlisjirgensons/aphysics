# -*- coding: utf-8 -*-
"""1. klase, 137. stunda: «Cik rādīs pēc 15 minūtēm?»

Laiku pēc noteikta sprīža atrod, pagriežot garo rādītāju: 15 min - 3
cipari uz priekšu. Ja pāri 12 - nāk nākamā stunda.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, pulkstenis)

TEMA = "Cik rādīs pēc 15 minūtēm?"

MERKIS = ("Šodien noteiksim, cik rādīs pulkstenis pēc noteikta laika "
          "sprīža.")

SATURS = [
    Sakums("Tagad 3:10. Cik rādīs pēc 15 minūtēm?",
           zimejums=pulkstenis(3, 25),
           paraksts="10 + 15 = 25 minūtes: 3:25.",
           fakti=["Pieskaiti minūtes.",
                  "Garais iet uz priekšu.",
                  "Pāri 60 - nākamā stunda."]),

    Slidnis("Pagriežam garo", [
        {"v": "3:10", "teksts": "Tagad", "zim": pulkstenis(3, 10)},
        {"v": "3:25", "teksts": "Pēc 15 min", "zim": pulkstenis(3, 25)},
        {"v": "3:40", "teksts": "Pēc vēl 15 min", "zim": pulkstenis(3, 40)},
    ]),

    Doma("Laiks pēc",
         "Pieskaiti minūtes; ja sanāk 60, tā ir jauna stunda.",
         soli=[
             "Nolasi tagadējo laiku.",
             "Pieskaiti minūtes (skaiti pa 5).",
             "60 minūtes = 1 stunda.",
         ]),

    Ievadi("Cik rādīs? (kā 3:25)", [
        {"jaut": "Tagad 5:00. Pēc 15 min?", "atb": ["5:15", "5,15"],
         "tastatura": "text", "padoms": "0 + 15."},
        {"jaut": "Tagad 2:30. Pēc 15 min?", "atb": ["2:45", "2,45"],
         "tastatura": "text", "padoms": "30 + 15."},
        {"jaut": "Tagad 6:45. Pēc 15 min?", "atb": ["7:00", "7"],
         "tastatura": "text", "padoms": "45 + 15 = 60 - jauna stunda."},
        {"jaut": "Tagad 9:00. Pēc 1 stundas?", "atb": ["10:00", "10"],
         "tastatura": "text", "padoms": "9 + 1."},
    ]),

    Pasaule("Pankūkas",
            Ievadi("", [
                {"jaut": "Pankūkas cep 15 min. Sāka 4:30. Kad gatavas?",
                 "atb": ["4:45", "4,45"], "tastatura": "text",
                 "padoms": "30 + 15."},
            ]),
            pavediens="virtuve",
            konteksts="Recepte saka, cik minūšu cept.",
            kapec="Zinot laiku, pankūkas nepiedeg."),

    Kopsavilkums([
        "Nosaku laiku pēc noteiktām minūtēm.",
        "Zinu: 60 min = 1 stunda.",
        "Pagriežu garo rādītāju.",
    ]),

    Majas([
        "Kad sāksi mājasdarbu, pieraksti laiku.",
        "Cik rādīs pēc 15 min? Pārbaudi!",
        "Uzvāri olu - cik rādīja, kad gatava?",
    ]),
]
