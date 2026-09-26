# -*- coding: utf-8 -*-
"""8. klase, 87. stunda: «Kā konstruēt paralēlu taisni?»

Konstrukcija ar cirkuli un lineālu: caur punktu P novelk krustotāju un
nokopē kāpšļu leņķi. Vienādi kāpšļu leņķi pēc pazīmes dod paralēlu
taisni. Caur punktu ārpus taisnes iet tikai viena paralēla taisne.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, geometrija)

TEMA = "Kā konstruēt paralēlu taisni?"

MERKIS = "Ar cirkuli un lineālu konstruēsim taisni, kas paralēla dotajai."

SATURS = [
    Sakums("Kā caur punktu P novilkt paralēlu taisni?",
           zimejums=geometrija(
               [("Q", 0, 0, 270), ("_r", 6, 0), ("_l", -1, 0), ("P", 2, 3, 150),
                ("_t", 7, 3), ("_u", 3, 4.5)],
               taisnes=[("_l", "_r"), ("Q", "P"), ("P", "_t")],
               lenki=[(("_r", "Q", "P"), "α"), (("_t", "P", "_u"), "α")],
               uzraksti=[(6.6, -0.5, "a")]),
           paraksts="Leņķi α pie Q nokopē pie P - taisnes ir paralēlas.",
           fakti=["Paralēlu taisni konstruē, nokopējot leņķi.",
                  "Vienādi kāpšļu leņķi nodrošina paralelitāti.",
                  "Caur punktu ārpus taisnes iet tikai viena paralēla taisne."]),

    Doma("Konstrukcijas soļi",
         "Paralēla taisne = nokopēts kāpšļu leņķis.",
         soli=[
             "Caur P novelc jebkuru taisni, kas krusto a punktā Q.",
             "Ap Q uzzīmē loku, kas krusto abas taisnes.",
             "Ar to pašu rādiusu uzzīmē loku ap P.",
             "Ar cirkuli pārnes attālumu starp pirmā loka krustpunktiem.",
             "Caur P un iegūto punktu novelc taisni - tā ir paralēla a.",
         ],
         pieze="Cits veids: uzbūvē rombu ar virsotni P - tā pretējās malas "
               "ir paralēlas."),

    Varianti("Spried", [
        {"jaut": "Kāpēc konstruētā taisne ir paralēla a?",
         "opcijas": ["Kāpšļu leņķi ir vienādi", "Tā izskatās paralēla",
                     "Tā ir perpendikulāra", "Cirkulis to garantē"],
         "pareizi": 0, "padoms": "Paralelitātes pazīme."},
        {"jaut": "Cik paralēlu taišņu var novilkt caur punktu ārpus "
                 "taisnes?",
         "opcijas": ["Vienu", "Divas", "Bezgalīgi daudz", "Nevienu"],
         "pareizi": 0, "padoms": "Paralēlo taišņu aksioma."},
        {"jaut": "Ko pārnes ar cirkuli trešajā solī?",
         "opcijas": ["Attālumu starp loka krustpunktiem",
                     "Taisnes garumu", "Punkta P augstumu",
                     "Leņķi grādos"],
         "pareizi": 0, "padoms": "Tā nokopē leņķa atvērumu."},
        {"jaut": "Kāpēc der arī romba konstrukcija?",
         "opcijas": ["Romba pretējās malas ir paralēlas",
                     "Rombam visi leņķi taisni", "Rombs ir kvadrāts",
                     "Diagonāles vienādas"],
         "pareizi": 0, "padoms": "Rombs ir paralelograms."},
    ]),

    Ievadi("Leņķi konstrukcijā", [
        {"jaut": "Krustotājs QP ar a veido 63°. Kādu leņķi nokopē pie P "
                 "(kāpšļu vietā)?", "atb": ["63"], "padoms": "Vienāds."},
        {"jaut": "Ja nokopē iekšējo šķērsleņķi, cik grādu tas ir?",
         "atb": ["63"], "padoms": "Arī vienāds."},
        {"jaut": "Ja lieto vienpusleņķi, cik grādu tas ir?",
         "atb": ["117"], "padoms": "180° − 63°."},
    ]),

    Pasaule("Stāvvietas līnijas",
            Ievadi("", [
                {"jaut": "Stāvvietas līnijas krāso slīpi - 60° pret ceļa malu. "
                         "Kāds leņķis ir otrajai līnijai?",
                 "atb": ["60"], "padoms": "Paralēlas līnijas."},
                {"jaut": "Kāds ir blakusleņķis pie ceļa malas?",
                 "atb": ["120"], "padoms": "180° − 60°."},
                {"jaut": "Līnijas gar ceļa malu ik pēc 2,5 m, pirmā pie 0 m. "
                         "Cik līniju 25 m garumā?",
                 "atb": ["11"], "padoms": "25 : 2,5 + 1."},
            ]),
            pavediens="celojums",
            konteksts="Stāvvietu līnijas krāso ar šablonu, kas nokopē vienu "
                      "leņķi.",
            kapec="Vienādi kāpšļu leņķi nozīmē paralēlas līnijas."),

    Kopsavilkums([
        "Konstruēju paralēlu taisni, nokopējot leņķi.",
        "Pamatoju konstrukciju ar paralelitātes pazīmi.",
        "Zinu, ka caur punktu iet tikai viena paralēla taisne.",
    ]),

    Majas([
        "Ar cirkuli un lineālu konstruē paralēlu taisni caur punktu 4 cm "
        "attālumā.",
        "Pārbaudi ar stūreni, vai attālums visur vienāds.",
        "Konstruē paralēlu taisni ar romba paņēmienu.",
    ]),
]
