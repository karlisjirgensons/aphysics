# -*- coding: utf-8 -*-
"""8. klase, 48. stunda: «Kādi skaitļi nav racionāli?»

Kvadrāta ar malu 1 diagonāles kvadrāts ir 2, bet neviena daļa kvadrātā nedod
2. Tā ir pirmā iracionālā skaitļa atklāšana. Stundā - arī bezgalīgas
neperiodiskas decimāldaļas kā iracionālu skaitļu pazīme.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, geometrija, restis)

TEMA = "Kādi skaitļi nav racionāli?"

MERKIS = ("Minēsim iracionālu skaitļu piemērus un pamatosim, ka tos nevar "
          "pierakstīt kā daļu.")

SATURS = [
    Sakums("Kvadrāta diagonāle",
           zimejums=geometrija([("A", 0, 0), ("B", 4, 0), ("C", 4, 4),
                                ("D", 0, 4)],
                               nogriezni=["AB", "BC", "CD", "DA", "AC"],
                               malas=[("AB", "1"), ("BC", "1"), ("AC", "?")],
                               taisni=["ABC"]),
           paraksts="Diagonāles kvadrāts ir 2 - kāds skaitlis kvadrātā dod 2?",
           fakti=["1,4² = 1,96 - par maz.",
                  "1,5² = 2,25 - par daudz.",
                  "Neviena daļa kvadrātā nedod tieši 2."]),

    Slidnis("Tuvojas √2", [
        {"v": "1,4^2 = 1,96", "teksts": "Mazāk par 2"},
        {"v": "1,41^2 = 1,9881", "teksts": "Tuvāk"},
        {"v": "1,414^2 = 1,999396", "teksts": "Vēl tuvāk"},
        {"v": "1,4142^2 = 1,99996164", "teksts": "Nekad tieši 2"},
        {"v": "√2 = 1,41421356...", "teksts": "Cipari nebeidzas un "
                                              "neatkārtojas"},
    ]),

    Doma("Iracionāli skaitļi",
         "Iracionāls skaitlis ir skaitlis, ko nevar pierakstīt kā daļu {m|n}. "
         "Decimāldaļā tas ir bezgalīgs un neperiodisks.",
         soli=[
             "√2, √3, √5 - kvadrātsaknes no skaitļiem, kas nav kvadrāti.",
             "π = 3,14159... - riņķa līnija un diametrs.",
             "0,1010010001... - cipari neveido periodu.",
             "Iracionālu skaitli pieraksta precīzi ar simbolu (√2, π) vai "
             "aptuveni ar decimāldaļu.",
         ],
         pieze="Senajā Grieķijā pitagorieši bija pārliecināti, ka visi "
               "skaitļi ir daļas. √2 atklāšana viņus šokēja."),

    Varianti("Racionāls vai iracionāls?", [
        {"jaut": "√9",
         "opcijas": ["Racionāls", "Iracionāls"],
         "pareizi": 0, "padoms": "√9 = 3.", "jaukt": False},
        {"jaut": "√7",
         "opcijas": ["Racionāls", "Iracionāls"],
         "pareizi": 1, "padoms": "7 nav kvadrāts.", "jaukt": False},
        {"jaut": "0,(142857)",
         "opcijas": ["Racionāls", "Iracionāls"],
         "pareizi": 0, "padoms": "Periodisks = {1|7}.", "jaukt": False},
        {"jaut": "0,12112111211112...",
         "opcijas": ["Racionāls", "Iracionāls"],
         "pareizi": 1, "padoms": "Perioda nav.", "jaukt": False},
        {"jaut": "{π|π}",
         "opcijas": ["Racionāls", "Iracionāls"],
         "pareizi": 0, "padoms": "= 1.", "jaukt": False},
        {"jaut": "2π",
         "opcijas": ["Racionāls", "Iracionāls"],
         "pareizi": 1, "padoms": "Divkāršs π.", "jaukt": False},
    ], pamats=4),

    Ievadi("Novērtē", [
        {"jaut": "Starp kuriem diviem veseliem skaitļiem ir √10? Ieraksti "
                 "mazāko.",
         "atb": ["3"], "padoms": "9 < 10 < 16."},
        {"jaut": "√2 līdz simtdaļām", "atb": ["1,41", "1.41"],
         "padoms": "1,414..."},
        {"jaut": "Kvadrāta ar malu 5 cm diagonāles kvadrāts (cm²)?",
         "atb": ["50"], "padoms": "Divi kvadrāti 25 + 25."},
        {"jaut": "Cik veselu skaitļu ir starp √5 un √30?",
         "atb": ["3"], "padoms": "3; 4; 5."},
    ]),

    Pasaule("Papīra formāts A4",
            Ievadi("", [
                {"jaut": "A4 lapa ir 210 × 297 mm. Aprēķini 297 : 210 līdz "
                         "simtdaļām.",
                 "atb": ["1,41", "1.41"], "padoms": "1,414..."},
                {"jaut": "Pārlokot A4 uz pusēm, iegūst A5: 148,5 × 210 mm. "
                         "Aprēķini 210 : 148,5 līdz simtdaļām.",
                 "atb": ["1,41", "1.41"], "padoms": "Tā pati attiecība."},
                {"jaut": "A3 ir divas A4 blakus. Tās garākā mala (mm)?",
                 "atb": ["420"], "padoms": "2 · 210."},
            ]),
            pavediens="tehnika",
            konteksts="A formātu malu attiecība ir √2 - tāpēc, pārlokot lapu, "
                      "forma paliek tā pati.",
            kapec="Iracionāls skaitlis ir katrā skolas burtnīcā."),

    Kopsavilkums([
        "Zinu, ka iracionālu skaitli nevar pierakstīt kā daļu.",
        "Min piemērus: √2, √3, π.",
        "Nošķiru racionālu un iracionālu skaitli pēc decimāldaļas.",
        "Novērtēju kvadrātsakni starp veseliem skaitļiem.",
    ]),

    Majas([
        "Ar kalkulatoru atrodi √3 un pārbaudi 1,73^2.",
        "Uzraksti 3 racionālus un 3 iracionālus skaitļus starp 1 un 2.",
        "Nomēri burtnīcas malas un aprēķini to attiecību.",
    ]),
]
