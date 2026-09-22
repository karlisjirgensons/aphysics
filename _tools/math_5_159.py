# -*- coding: utf-8 -*-
"""5. klase, 159. stunda: «Kā no grafika nolasīt samaksu?»

Mikrotemata noslēgums, un pirmā reize, kad grafiks tiek lasīts, nevis zīmēts.
Uzdevums ir vienkāršs tikai no izskata: no vienas līnijas var nolasīt gan
cenu par vienu vienību, gan samaksu par jebkuru daudzumu, gan to, cik daudz
var nopirkt par doto naudu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, plakne)

TEMA = "Kā no grafika nolasīt samaksu?"

MERKIS = ("Mācīsimies nolasīt no grafiskā attēla visu iespējamo informāciju "
          "par diviem lielumiem.")

SATURS = [
    Sakums("Viena līnija, trīs atbildes",
           zimejums=plakne(lauzta=[(0, 0), (1, 2), (2, 4), (3, 6), (4, 8)],
                           no_x=0, lidz_x=5, no_y=0, lidz_y=10, solis=2,
                           virsraksts="Kilogrami un eiro"),
           paraksts="No šīs līnijas var nolasīt cenu, samaksu un daudzumu.",
           fakti=["Uz x ass ir kilogrami, uz y ass - eiro.",
                  "Viens kilograms maksā 2 €.",
                  "Par 8 € var nopirkt 4 kg."]),

    Doma("Ej no ass uz līniju un atpakaļ",
         "Lai no grafika nolasītu vērtību, no zināmā lieluma ass iet līdz "
         "līnijai un no tās - uz otro asi.",
         soli=[
             "Atrodi zināmo vērtību uz vienas ass.",
             "Ej taisni līdz līnijai.",
             "No līnijas ej uz otro asi.",
             "Nolasi vērtību.",
             "Pārbaudi ar rēķinu, ja skaitļi ir apaļi.",
         ],
         pieze="Vienas vienības cenu nolasa vienkāršāk: skaties, kur līnija "
               "ir virs skaitļa 1 uz x ass. Tālāk visu pārējo var arī "
               "izrēķināt."),

    Paraugs("Cik maksā 3 kg?",
            uzd="No grafika nolasi samaksu par 3 kg.",
            soli=[
                ("Atrodi 3 uz x ass",
                 "Zināmais lielums."),
                ("Ej uz augšu līdz līnijai",
                 "Līdz krustpunktam."),
                ("No turienes ej pa kreisi uz y asi",
                 "Nolasi vērtību."),
                ("Iznāk 6 €",
                 "Samaksa par 3 kg."),
                ("Pārbaude: 2 · 3 = 6",
                 "Cena par kilogramu ir 2 €."),
            ],
            atbilde="3 kg maksā 6 €"),

    Ievadi("Nolasi no grafika", [
        {"jaut": "1 kg maksā 2 €. Cik eiro maksā 3 kg?",
         "atb": ["6"], "padoms": "2 · 3."},
        {"jaut": "Cik eiro maksā 4 kg?",
         "atb": ["8"], "padoms": "2 · 4."},
        {"jaut": "Cik kilogramu var nopirkt par 8 €?",
         "atb": ["4"], "padoms": "8 : 2."},
        {"jaut": "Cik kilogramu var nopirkt par 10 €?",
         "atb": ["5"], "padoms": "10 : 2."},
        {"jaut": "Cik eiro maksā 1 kg?",
         "atb": ["2"], "padoms": "Līnija virs skaitļa 1."},
        {"jaut": "Cik eiro maksā 2 kg?",
         "atb": ["4"], "padoms": "2 · 2."},
        {"jaut": "Cik eiro maksā puskilograms?",
         "atb": ["1"], "padoms": "2 : 2."},
        {"jaut": "Cik kilogramu var nopirkt par 12 €?",
         "atb": ["6"], "padoms": "12 : 2."},
    ], pamats=4,
        ievads="No ass uz līniju, no līnijas uz otro asi."),

    Zimejums("Divi ceļi pa grafiku",
             plakne(lauzta=[(0, 0), (1, 2), (2, 4), (3, 6), (4, 8)],
                    punkti=[(3, 6, "")], no_x=0, lidz_x=5, no_y=0,
                    lidz_y=10, solis=2, virsraksts="3 kg maksā 6 €"),
             paskaidro="No 3 uz x ass uz augšu līdz līnijai, tad pa kreisi "
                       "uz y asi. Pretējā virzienā nolasa, cik var nopirkt "
                       "par doto naudu.",
             ievads="Viens punkts atbild uz diviem jautājumiem."),

    Varianti("Ko var nolasīt no grafika?", [
        {"jaut": "Kā nolasa samaksu par zināmu daudzumu?",
         "opcijas": ["No x ass uz līniju, tad uz y asi",
                     "No y ass uz līniju",
                     "Tikai rēķinot",
                     "Nolasīt nevar"],
         "pareizi": 0,
         "padoms": "Zināmais ir uz x ass."},
        {"jaut": "1 kg maksā 2 €. Cik maksā 4 kg?",
         "opcijas": ["8 €", "6 €", "4 €", "2 €"],
         "pareizi": 0,
         "padoms": "2 · 4."},
        {"jaut": "Cik kilogramu var nopirkt par 10 €?",
         "opcijas": ["5", "10", "20", "2"],
         "pareizi": 0,
         "padoms": "10 : 2."},
        {"jaut": "Kur grafikā redz viena kilograma cenu?",
         "opcijas": ["Virs skaitļa 1 uz x ass", "Līnijas galā",
                     "Krustpunktā", "Nekur"],
         "pareizi": 0,
         "padoms": "Viena vienība."},
        {"jaut": "Ko nozīmē punkts (3; 6)?",
         "opcijas": ["3 kg maksā 6 €", "6 kg maksā 3 €", "3 € par 6 kg",
                     "Neko"],
         "pareizi": 0,
         "padoms": "Pirmais skaitlis - kilogrami."},
        {"jaut": "Kā pārbauda nolasīto vērtību?",
         "opcijas": ["Ar rēķinu", "Ar lineālu", "Ar citu grafiku",
                     "Pārbaudīt nevar"],
         "pareizi": 0,
         "padoms": "Cena reiz daudzums."},
    ], pamats=4),

    Pasaule("Cik maksās pusdienas?",
            Ievadi("", [
                {"jaut": "Vienas pusdienas maksā 2 €. Cik eiro maksā "
                         "5 pusdienas?",
                 "atb": ["10"], "padoms": "2 · 5."},
                {"jaut": "Cik pusdienas var nopirkt par 20 €?",
                 "atb": ["10"], "padoms": "20 : 2."},
                {"jaut": "Cik eiro maksā pusdienas visu nedēļu - 5 dienas?",
                 "atb": ["10"], "padoms": "2 · 5."},
                {"jaut": "Cik eiro vajag mēnesim - 20 dienām?",
                 "atb": ["40"], "padoms": "2 · 20."},
            ]),
            pavediens="skola",
            konteksts="Ēdnīcas cenu grafiks pie sienas ļauj uzreiz redzēt, "
                      "cik maksās nedēļa vai mēnesis.",
            kapec="Nolasīt no grafika ir ātrāk nekā rēķināt katru reizi."),

    Kopsavilkums([
        "Nolasu no grafika samaksu par zināmu daudzumu.",
        "Nolasu, cik var nopirkt par zināmu naudu.",
        "Atrodu grafikā vienas vienības cenu.",
        "Pārbaudu nolasīto vērtību ar rēķinu.",
    ]),

    Majas([
        "Uzzīmē grafiku, kurā viena prece maksā 3 €.",
        "Nolasi no tā, cik maksā 4 preces un cik var nopirkt par 15 €.",
        "Pārbaudi abas atbildes ar rēķinu.",
    ]),
]
