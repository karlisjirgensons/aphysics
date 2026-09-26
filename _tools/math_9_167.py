# -*- coding: utf-8 -*-
"""9. klase, 167. stunda: «Kas man vēl jāatkārto?»

Diagnosticējoša pārbaude: pa diviem īsiem uzdevumiem no katras lielās
eksāmena jomas (skaitļi, izteiksmes, vienādojumi, funkcijas, ģeometrija).
Kļūda vai trešais mēģinājums nozīmē - temats iet sarakstā. Saraksts un
procenti pa jomām ir nākamās stundas plāna pamats.
"""

from math_saturs import (Ievadi, Kopsavilkums, Majas, Pasaule, Petijums,
                         Sakums, Varianti, kolonnas, saknes)

TEMA = "Kas man vēl jāatkārto?"

MERKIS = ("Veiksim diagnosticējošu pārbaudi un izveidosim savu atkārtojamo "
          "tematu sarakstu.")

_PIEMERS = kolonnas([("Skaitļi", 90), ("Izteiksmes", 60),
                     ("Vienādojumi", 75), ("Funkcijas", 40),
                     ("Ģeometrija", 55)], "%")

SATURS = [
    Sakums("Kur es zaudēšu punktus?",
           zimejums=_PIEMERS,
           paraksts="Piemērs: kāda skolēna pārbaudes rezultāts pa jomām.",
           fakti=["Atkārto vispirms to, kur rezultāts zemākais.",
                  "Pieraksti katru kļūdu - tā ir atkārtojamais temats.",
                  "Neskaties padomu, pirms neesi mēģinājis pats."]),

    Ievadi("1. Skaitļi", [
        {"jaut": "5^3 = ?", "atb": ["125"], "padoms": "5 · 5 · 5."},
        {"jaut": "(0,3)^2 = ?", "atb": ["0,09"], "padoms": "0,3 · 0,3."},
        {"jaut": "Cik ir 15 % no 240?", "atb": ["36"], "padoms": "0,15 · 240."},
    ]),

    Ievadi("2. Izteiksmes", [
        {"jaut": "x^8 · x^2 = x^n. n = ?", "atb": ["10"],
         "padoms": "Kāpinātājus saskaita."},
        {"jaut": "(4 + b)^2 = 16 + kb + b^2. k = ?", "atb": ["8"],
         "padoms": "2 · 4 · b."},
        {"jaut": "√64 + √36 = ?", "atb": ["14"], "padoms": "8 + 6."},
    ]),

    Ievadi("3. Vienādojumi un progresija", [
        {"jaut": "3x − 7 = 11. x = ?", "atb": ["6"], "padoms": "3x = 18."},
        {"jaut": "x^2 − 5x + 6 = 0. Saknes?", "atb": saknes("2", "3"),
         "tastatura": "text", "vieta": "piem. 1; 4",
         "padoms": "Vjeta: summa 5, reizinājums 6."},
        {"jaut": "a_1 = 3, d = 2. a_4 = ?", "atb": ["9"],
         "padoms": "3 + 3 · 2."},
    ]),

    Varianti("4. Funkcijas", [
        {"jaut": "Kur grafiks y = −3x + 5 krusto y asi?",
         "opcijas": ["(0; 5)", "(5; 0)", "(0; −3)", "(−3; 0)"],
         "pareizi": 0, "padoms": "x = 0."},
        {"jaut": "Parabolas y = x^2 + 2x virsotnes abscisa x_v = ?",
         "opcijas": ["−1", "1", "2", "−2"],
         "pareizi": 0, "padoms": "x_v = −{b|2a}."},
    ]),

    Ievadi("5. Ģeometrija", [
        {"jaut": "Izstiepts leņķis sadalīts; viens leņķis 130°. Otrs (°)?",
         "atb": ["50"], "padoms": "180 − 130."},
        {"jaut": "Katetes 6 un 8. Hipotenūza?", "atb": ["10"],
         "padoms": "Pitagors."},
        {"jaut": "Centra leņķis 80°. Ievilktais leņķis uz tā paša loka (°)?",
         "atb": ["40"], "padoms": "Puse."},
    ]),

    Petijums("Mans atkārtojamo tematu saraksts", [
        "Katrai jomai saskaiti, cik uzdevumu izdevās ar pirmo mēģinājumu.",
        "Aprēķini procentus katrai jomai.",
        "Uzzīmē savu stabiņu diagrammu kā sākumā.",
        "Pieraksti 3 zemākās jomas un konkrētus tematus tajās.",
    ], vajag="burtnīca, šīs stundas rezultāti",
       secinajums="Šis saraksts ir nākamās stundas plāna izejas punkts."),

    Pasaule("Rezultāts pa jomām",
            Ievadi("", [
                {"jaut": "Algebrā ieguvi 18 punktus no 24. Cik procentu?",
                 "atb": ["75"], "padoms": "18 : 24."},
                {"jaut": "Ģeometrijā 11 no 20. Cik procentu?", "atb": ["55"],
                 "padoms": "11 : 20."},
                {"jaut": "Par cik procentpunktiem ģeometrija atpaliek?",
                 "atb": ["20"], "padoms": "75 − 55."},
            ]),
            pavediens="skola",
            konteksts="Skolotāja izdala diagnosticējošā darba rezultātus pa "
                      "jomām.",
            kapec="Procenti ļauj salīdzināt jomas ar dažādu punktu skaitu."),

    Kopsavilkums([
        "Veicu diagnosticējošu pārbaudi visās jomās.",
        "Aprēķinu rezultātu procentos pa jomām.",
        "Izveidoju savu atkārtojamo tematu sarakstu.",
    ]),

    Majas([
        "Papildini sarakstu ar tematiem no saviem kontroldarbiem.",
        "Katram tematam atrodi vienu stundu šajā vietnē.",
        "Parādi sarakstu vecākiem vai skolotājam.",
    ]),
]
