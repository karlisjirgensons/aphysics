# -*- coding: utf-8 -*-
"""7. klase, 140. stunda: «Kas ir proporcija?»

Proporcija ir divu attiecību vienādība: a : b = c : d jeb {a|b} = {c|d}.
Galvenā īpašība: ārējo locekļu reizinājums ir vienāds ar vidējo locekļu
reizinājumu (ad = bc). Ar to pārbauda, vai proporcija ir patiesa.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kas ir proporcija?"

MERKIS = ("Paskaidrosim proporciju kā divu attiecību vienādību un "
          "lasīsim tās pierakstu.")

SATURS = [
    Sakums("Ekrāns 16 : 9",
           zimejums=restis([["ekrāns", "platums : augstums"],
                            ["telefons horizontāli", "16 : 9"],
                            ["televizors", "160 cm : 90 cm"],
                            ["monitors", "48 cm : 27 cm"]]),
           paraksts="Visām trim - viena un tā pati attiecība.",
           fakti=["16 : 9 = 160 : 90 - tā ir proporcija.",
                  "Tāpēc filma izskatās vienādi uz visiem ekrāniem.",
                  "Pārbaude: 16 · 90 = 9 · 160."]),

    Doma("Proporcija un tās pamatīpašība",
         "Proporcija ir divu attiecību vienādība: a : b = c : d. Skaitļus a "
         "un d sauc par ārējiem locekļiem, b un c - par vidējiem. Pareizā "
         "proporcijā ārējo locekļu reizinājums ir vienāds ar vidējo "
         "locekļu reizinājumu: ad = bc.",
         soli=[
             "Nosauc ārējos (pirmo un pēdējo) un vidējos locekļus.",
             "Sareizini ārējos.",
             "Sareizini vidējos.",
             "Vienādi - proporcija pareiza.",
         ],
         pieze="Daļu pierakstā {a|b} = {c|d} tas ir «krustiskais» "
               "reizinājums: a · d = b · c."),

    Paraugs("Pārbaudi proporciju",
            uzd="Vai 12 : 18 = 10 : 15 ir pareiza proporcija?",
            soli=[
                ("Ārējie: 12 · 15 = 180", "Pirmais un pēdējais."),
                ("Vidējie: 18 · 10 = 180", "Vidējie."),
                ("180 = 180", "Pareiza."),
                ("Abas attiecības = 2 : 3", "Saīsināti."),
            ],
            atbilde="Pareiza."),

    Varianti("Pareiza proporcija?", [
        {"jaut": "3 : 4 = 9 : 12",
         "opcijas": ["Jā", "Nē"], "pareizi": 0, "jaukt": False,
         "padoms": "36 = 36."},
        {"jaut": "{2|5} = {5|2}",
         "opcijas": ["Jā", "Nē"], "pareizi": 1, "jaukt": False,
         "padoms": "4 ≠ 25."},
        {"jaut": "0,5 : 2 = 3 : 12",
         "opcijas": ["Jā", "Nē"], "pareizi": 0, "jaukt": False,
         "padoms": "6 = 6."},
        {"jaut": "Proporcijā 7 : x = 14 : 10 vidējie locekļi ir...",
         "opcijas": ["x un 14", "7 un 10", "7 un 14", "x un 10"],
         "pareizi": 0, "padoms": "Vidū."},
    ], pamats=4),

    Ievadi("Ārējie un vidējie", [
        {"jaut": "5 : 8 = 15 : 24. Ārējo locekļu reizinājums?",
         "atb": ["120"], "padoms": "5 · 24."},
        {"jaut": "Vidējo locekļu reizinājums?",
         "atb": ["120"], "padoms": "8 · 15."},
        {"jaut": "Kurš skaitlis padara proporciju pareizu: 2 : 3 = 6 : ?",
         "atb": ["9"], "padoms": "Trīsreiz lielāki."},
    ]),

    Pasaule("Fotogrāfijas izmērs",
            Ievadi("", [
                {"jaut": "Foto 3 : 2. Drukā 15 cm platu. Cik cm augstu, lai "
                         "attiecība saglabātos?",
                 "atb": ["10"], "padoms": "3 : 2 = 15 : x."},
                {"jaut": "Plakāts 60 cm plats. Augstums (cm)?",
                 "atb": ["40"], "padoms": "3 : 2 = 60 : x."},
                {"jaut": "Vai 45 × 25 cm drukā foto bez apgriešanas? Raksti "
                         "«jā» vai «nē».",
                 "atb": ["nē", "ne"], "padoms": "45 : 25 = 9 : 5 ≠ 3 : 2."},
            ]),
            pavediens="dati",
            konteksts="Fotoattēlu attiecība (3 : 2, 4 : 3, 16 : 9) saka, "
                      "vai attēls ietilps bez apgriešanas.",
            kapec="Proporcija saglabā formu."),

    Kopsavilkums([
        "Zinu, ka proporcija ir divu attiecību vienādība.",
        "Nosaucu ārējos un vidējos locekļus.",
        "Pārbaudu proporciju ar ad = bc.",
        "Atpazīstu proporcijas ekrānos un attēlos.",
    ]),

    Majas([
        "Izmēri 3 ekrānus un aprēķini attiecību.",
        "Uzraksti 3 pareizas proporcijas ar 4 : 5.",
        "Pārbaudi, vai A4 lapa (21 × 29,7) ir 1 : 1,41.",
    ]),
]
