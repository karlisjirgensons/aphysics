# -*- coding: utf-8 -*-
"""7. klase, 169. stunda: «Cik droši rīkojos ar izteiksmēm?»

Gada noslēguma bloka pirmā stunda - atskats uz algebru: iekavu atvēršana,
līdzīgo locekļu savilkšana, kopīgā reizinātāja iznešana un lineārs
vienādojums. Nekā jauna - tikai tas, kas jāprot droši pirms 8. klases.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, restis)

TEMA = "Cik droši rīkojos ar izteiksmēm?"

MERKIS = ("Atkārtosim izteiksmju pārveidojumus un vienādojumu risināšanu un "
          "novērtēsim, cik droši tos protam.")

SATURS = [
    Sakums("Gada algebra četrās darbībās",
           zimejums=restis([["darbība", "piemērs"],
                            ["atver iekavas", "3(x + 4) = 3x + 12"],
                            ["savelk", "2a + 4a = 6a"],
                            ["iznes", "6x + 9 = 3(2x + 3)"],
                            ["risina", "2x = 10, x = 5"]]),
           paraksts="Katrs vienādojums šogad bija šo četru darbību virkne.",
           fakti=["Mīnuss pirms iekavām maina visas zīmes.",
                  "Savelk tikai līdzīgos locekļus.",
                  "Atbildi pārbauda, ievietojot."]),

    Doma("Viens plāns visām izteiksmēm",
         "Garāka izteiksme nav grūtāka - tajā ir vairāk vienkāršu soļu. "
         "Kļūdas rodas nevis sarežģītajā vietā, bet zīmēs.",
         soli=[
             "Atver iekavas, katram loceklim līdzi paņemot zīmi.",
             "Savelc līdzīgos locekļus.",
             "Vienādojumā - locekļus ar x uz vienu pusi, skaitļus uz otru.",
             "Dala ar koeficientu pie x.",
             "Pārbaudi, ievietojot atbildi sākuma vienādojumā.",
         ],
         pieze="Astotajā klasē izteiksmes kļūs garākas (polinomi), bet soļi "
               "paliks tie paši."),

    Slidnis("Vienādojums pa soļiem", [
        {"v": "5 − 2(x − 3) = 3x + 1", "teksts": "Sākums"},
        {"v": "5 − 2x + 6 = 3x + 1",
         "teksts": "Atver iekavas: (−2) · (−3) = +6"},
        {"v": "11 − 2x = 3x + 1", "teksts": "Savelk: 5 + 6 = 11"},
        {"v": "10 = 5x", "teksts": "x pa labi, skaitļi pa kreisi"},
        {"v": "x = 2", "teksts": "Dala ar 5"},
        {"v": "7 = 7",
         "teksts": "Pārbaude: 5 − 2 · (−1) = 7 un 3 · 2 + 1 = 7"},
    ], ievads="Spied bultiņu un skaties, kura darbība notiek katrā solī."),

    Ievadi("Vienkāršo izteiksmi", [
        {"jaut": "3(x + 4) − 2x",
         "atb": ["x + 12", "x+12", "12+x"], "padoms": "3x + 12 − 2x.",
         "tastatura": "text"},
        {"jaut": "2a − 5 + 4a + 1",
         "atb": ["6a − 4", "6a-4", "-4+6a"], "padoms": "2a + 4a un −5 + 1.",
         "tastatura": "text"},
        {"jaut": "−2(3 − y)",
         "atb": ["2y − 6", "2y-6", "-6+2y"], "padoms": "−6 + 2y.",
         "tastatura": "text"},
        {"jaut": "6x + 9 = 3(...). Kas ir iekavās?",
         "atb": ["2x + 3", "2x+3", "3+2x"], "padoms": "6x : 3 un 9 : 3.",
         "tastatura": "text"},
        {"jaut": "Izteiksmes 2x² − 3x vērtība, ja x = −2",
         "atb": ["14"], "padoms": "2 · 4 + 6."},
    ], pamats=3),

    Ievadi("Atrisini vienādojumu", [
        {"jaut": "4x − 7 = 2x + 5",
         "atb": ["6"], "padoms": "2x = 12."},
        {"jaut": "3(x − 1) = 2(x + 4)",
         "atb": ["11"], "padoms": "3x − 3 = 2x + 8."},
        {"jaut": "{x|2} − {x|5} = 3",
         "atb": ["10"], "padoms": "· 10: 5x − 2x = 30."},
        {"jaut": "0,5x + 1,2 = 3,7",
         "atb": ["5"], "padoms": "0,5x = 2,5."},
    ], pamats=2),

    Varianti("Atrodi kļūdu", [
        {"jaut": "−(x − 4) = −x − 4",
         "opcijas": ["Kļūda: jābūt −x + 4", "Pareizi",
                     "Kļūda: jābūt x − 4", "Kļūda: jābūt x + 4"],
         "pareizi": 0, "padoms": "Mīnuss maina abas zīmes."},
        {"jaut": "3x + 2x = 5x²",
         "opcijas": ["Kļūda: jābūt 5x", "Pareizi", "Kļūda: jābūt 6x",
                     "Kļūda: jābūt 6x²"],
         "pareizi": 0, "padoms": "Saskaita koeficientus, x paliek."},
        {"jaut": "2x = 8 ⇒ x = 6",
         "opcijas": ["Kļūda: jādala, x = 4", "Pareizi",
                     "Kļūda: x = 16", "Kļūda: x = 10"],
         "pareizi": 0, "padoms": "2x nozīmē 2 · x."},
        {"jaut": "2(a + 3) = 2a + 3",
         "opcijas": ["Kļūda: jābūt 2a + 6", "Pareizi",
                     "Kļūda: jābūt a + 6", "Kļūda: jābūt 2a + 5"],
         "pareizi": 0, "padoms": "Reizina abus locekļus."},
    ]),

    Pasaule("Kurš mobilā tarifs ir lētāks?",
            Ievadi("", [
                {"jaut": "Tarifs A: 8 € mēnesī un 0,05 € par minūti. Cik "
                         "eiro maksā 100 minūtes?",
                 "atb": ["13"], "padoms": "8 + 0,05 · 100."},
                {"jaut": "Tarifs B: 3 € mēnesī un 0,15 € par minūti. Cik "
                         "eiro maksā 100 minūtes?",
                 "atb": ["18"], "padoms": "3 + 0,15 · 100."},
                {"jaut": "8 + 0,05m = 3 + 0,15m. Pie cik minūtēm abi "
                         "tarifi maksā vienādi?",
                 "atb": ["50"], "padoms": "5 = 0,1m."},
                {"jaut": "Cik eiro tad maksā katrs tarifs?",
                 "atb": ["10,5", "10.5", "10,50"],
                 "padoms": "8 + 0,05 · 50."},
            ]),
            pavediens="dati",
            konteksts="Tarifa cena ir izteiksme ar mainīgo m - minūšu "
                      "skaitu. Vienādojums parāda, kur izdevīgums mainās.",
            kapec="Ja runā mazāk par 50 minūtēm, lētāks ir B, ja vairāk - "
                  "A."),

    Kopsavilkums([
        "Atveru iekavas, arī ar mīnusu priekšā.",
        "Savelku līdzīgos locekļus un iznesu kopīgo reizinātāju.",
        "Atrisinu lineāru vienādojumu un pārbaudu atbildi.",
        "Atpazīstu biežākās zīmju kļūdas.",
    ]),

    Majas([
        "Vienkāršo trīs izteiksmes ar mīnusu pirms iekavām.",
        "Atrisini divus vienādojumus un pieraksti pārbaudi.",
        "Salīdzini divus reālus tarifus (telefons, internets) ar "
        "vienādojumu.",
    ]),
]
