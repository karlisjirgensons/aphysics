# -*- coding: utf-8 -*-
"""2. klase, 91. stunda: «Kā izpildīt soļus pēc pieraksta?»

Algoritms ir soļu virkne, ko izpilda precīzi pēc kārtas. Shēmā katrs solis
ir kastīte, un bulta rāda, kurš nāk nākamais. Ja soli izlaiž vai samaina
secību, iznāk cits rezultāts - tieši tāpat kā izteiksmē.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, algoritms)

TEMA = "Kā izpildīt soļus pēc pieraksta?"

MERKIS = ("Šodien lasīsim un izpildīsim dotu algoritmu ar vairākiem "
          "soļiem.")

_A = algoritms(["Paņem skaitli", "Pieskaiti 15", "Atņem 5",
                "Pieraksti rezultātu"])

SATURS = [
    Sakums("Kā robots zina, ko darīt?",
           zimejums=_A,
           paraksts="Algoritms - soļi pēc kārtas.",
           fakti=["Robots izpilda katru soli precīzi.",
                  "Tas neizlaiž un nemaina secību.",
                  "Ja skaitlis ir 20: 20 + 15 = 35, 35 − 5 = 30."]),

    Doma("Algoritms",
         "Algoritms ir soļi, kas jāizpilda precīzi un pēc kārtas.",
         soli=[
             "Sāc ar pirmo kastīti.",
             "Izpildi to un ej pa bultu uz nākamo.",
             "Nākamais solis izmanto iepriekšējā rezultātu.",
             "Beigās ir rezultāts.",
         ]),

    Ievadi("Izpildi algoritmu", [
        {"jaut": "Skaitlis 20. Kāds rezultāts?", "zim": _A, "atb": ["30"],
         "padoms": "20 + 15 − 5."},
        {"jaut": "Skaitlis 45. Kāds rezultāts?", "zim": _A, "atb": ["55"],
         "padoms": "45 + 15 − 5."},
        {"jaut": "Skaitlis 8. Kāds rezultāts?", "zim": _A, "atb": ["18"],
         "padoms": "8 + 15 − 5."},
        {"jaut": "Skaitlis 70. Kāds rezultāts?", "zim": _A, "atb": ["80"],
         "padoms": "70 + 15 − 5."},
    ]),

    Varianti("Ko dara algoritms?", [
        {"jaut": "Ko šis algoritms dara ar jebkuru skaitli?", "zim": _A,
         "opcijas": ["pieskaita 10", "pieskaita 15", "atņem 5"],
         "pareizi": 0, "padoms": "+ 15 − 5 = + 10."},
        {"jaut": "Rezultāts bija 50. Kāds bija skaitlis?", "zim": _A,
         "opcijas": ["40", "50", "60"], "pareizi": 0,
         "padoms": "Atpakaļ: − 10."},
    ]),

    Ievadi("Cits algoritms", [
        {"jaut": "Paņem 30, atņem 12, pieskaiti 20. Rezultāts?",
         "zim": algoritms(["Paņem 30", "Atņem 12", "Pieskaiti 20"]),
         "atb": ["38"], "padoms": "18 + 20."},
        {"jaut": "Paņem 64, atņem 30, atņem 4. Rezultāts?",
         "zim": algoritms(["Paņem 64", "Atņem 30", "Atņem 4"]),
         "atb": ["30"], "padoms": "34 − 4."},
    ]),

    Pasaule("Recepte ir algoritms",
            Varianti("", [
                {"jaut": "Pankūku recepte: 1) iesit olas, 2) pielej pienu, "
                         "3) pieber miltus, 4) cep. Kas notiks, ja izlaidīs "
                         "3. soli?", "opcijas": ["mīkla būs šķidra, pankūkas "
                                                 "neizdosies", "nekas",
                                                 "būs garšīgākas"],
                 "pareizi": 0, "padoms": "Bez miltiem mīkla nesabiezē."},
            ]),
            pavediens="virtuve",
            konteksts="Recepte ir soļi, ko izpilda pēc kārtas.",
            kapec="Algoritmi ir visur - ne tikai datoros."),

    Kopsavilkums([
        "Lasu algoritma shēmu.",
        "Izpildu soļus precīzi un pēc kārtas.",
        "Nosaku rezultātu.",
    ]),

    Majas([
        "Uzraksti algoritmu zobu tīrīšanai.",
        "Lai mājinieks to izpilda precīzi, kā uzrakstīts.",
        "Vai kāds solis bija aizmirsts?",
    ]),
]
