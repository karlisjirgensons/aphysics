# -*- coding: utf-8 -*-
"""8. klase, 49. stunda: «Kā izskatās reālo skaitļu kopa?»

Bloka noslēgums: racionālie un iracionālie kopā ir reālie skaitļi, un
katram punktam uz skaitļu taisnes atbilst tieši viens reāls skaitlis.
Pārskata tabula un taisne sakārto visu, kas par skaitļiem mācīts 1.-8. klasē.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, Zimejums, restis, taisne)

TEMA = "Kā izskatās reālo skaitļu kopa?"

MERKIS = ("Izveidosim pārskatu par skaitļu kopām un to savstarpējo saistību.")

SATURS = [
    Sakums("Katram punktam - savs skaitlis",
           zimejums=taisne(-3, 4, 1, [(-2.5, "−2,5"), (0, "0"),
                                      (1.414, "√2"), (3.14, "π")]),
           paraksts="Uz taisnes ir gan racionāli, gan iracionāli skaitļi.",
           fakti=["Racionālie un iracionālie kopā - reālie skaitļi R.",
                  "Katram punktam uz taisnes - tieši viens reāls skaitlis.",
                  "Taisnē «caurumu» nav."]),

    Doma("Skaitļu kopu pārskats",
         "Katra jauna kopa radās, kad iepriekšējā nevarēja atrisināt kādu "
         "uzdevumu.",
         soli=[
             "N: skaitīšana. 5 − 8 nav naturāls - vajag Z.",
             "Z: veselie. 3 : 4 nav vesels - vajag Q.",
             "Q: daļas. Kvadrāta diagonāle nav daļa - vajag I.",
             "I: iracionālie (√2, π).",
             "R = Q un I kopā: N ⊂ Z ⊂ Q ⊂ R.",
         ]),

    Zimejums("Pārskata tabula",
             restis([["skaitlis", "N", "Z", "Q", "R"],
                     ["7", "✓", "✓", "✓", "✓"],
                     ["−4", "", "✓", "✓", "✓"],
                     ["0,75", "", "", "✓", "✓"],
                     ["√3", "", "", "", "✓"]]),
             paskaidro="Skaitlis, kas pieder mazākai kopai, pieder arī "
                       "visām lielākajām."),

    Varianti("Kurš apgalvojums pareizs?", [
        {"jaut": "Katrs vesels skaitlis ir racionāls.",
         "opcijas": ["Patiess", "Aplams"],
         "pareizi": 0, "padoms": "a = {a|1}.", "jaukt": False},
        {"jaut": "Katrs reāls skaitlis ir racionāls.",
         "opcijas": ["Patiess", "Aplams"],
         "pareizi": 1, "padoms": "√2.", "jaukt": False},
        {"jaut": "Divu iracionālu skaitļu summa vienmēr ir iracionāla.",
         "opcijas": ["Patiess", "Aplams"],
         "pareizi": 1, "padoms": "√2 + (−√2) = 0.", "jaukt": False},
        {"jaut": "Starp jebkuriem diviem racionāliem skaitļiem ir vēl "
                 "racionāls.",
         "opcijas": ["Patiess", "Aplams"],
         "pareizi": 0, "padoms": "Viduspunkts {a + b|2}.", "jaukt": False},
    ]),

    Ievadi("Sakārto un atrodi", [
        {"jaut": "Kurš lielāks: π vai 3,15? (ieraksti lielāko)",
         "atb": ["3,15", "3.15"], "padoms": "π = 3,1415..."},
        {"jaut": "Kurš lielāks: √2 vai 1,4? Ieraksti lielāko līdz simtdaļām.",
         "atb": ["1,41", "1.41"], "padoms": "√2 = 1,414... > 1,4."},
        {"jaut": "Atrodi racionālu skaitli starp 1,41 un 1,42 ar 3 cipariem "
                 "aiz komata, kas beidzas ar 5.",
         "atb": ["1,415", "1.415"], "padoms": "Vidū."},
        {"jaut": "Cik naturālu skaitļu ir starp −2,5 un π?",
         "atb": ["3"], "padoms": "1; 2; 3."},
    ]),

    Pasaule("Mērījumi un skaitļi",
            Ievadi("", [
                {"jaut": "Kvadrātveida dārza laukums 50 m². Mala ir √50 m. "
                         "Starp kuriem veseliem metriem? Ieraksti mazāko.",
                 "atb": ["7"], "padoms": "49 < 50 < 64."},
                {"jaut": "Mala līdz desmitdaļām (m)?",
                 "atb": ["7,1", "7.1"], "padoms": "7,07..."},
                {"jaut": "Cik metru žoga vajag (perimetrs līdz veseliem, uz "
                         "augšu)?",
                 "atb": ["29"], "padoms": "4 · 7,07 = 28,28."},
            ]),
            pavediens="maja",
            konteksts="Precīzā mala ir iracionāla (√50), bet žogu pērk "
                      "metros - tāpēc vajag tuvinājumu.",
            kapec="Iracionāls skaitlis dzīvē vienmēr kļūst par tuvinājumu."),

    Kopsavilkums([
        "Zinu kopas N ⊂ Z ⊂ Q ⊂ R un iracionālos I.",
        "Nosaku, kurām kopām skaitlis pieder.",
        "Salīdzinu racionālus un iracionālus skaitļus.",
    ]),

    Majas([
        "Uzzīmē skaitļu kopu shēmu ar apļiem un katrā ieraksti 2 piemērus.",
        "Sakārto: √5, 2,2, {9|4}, 2,(2).",
        "Pamato, kāpēc starp 1 un 2 ir bezgalīgi daudz skaitļu.",
    ]),
]
