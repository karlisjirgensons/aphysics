# -*- coding: utf-8 -*-
"""4. klase, 130. stunda: «Cik daudz laika veltu mācībām?»

Mikrotemata noslēgums - praktisks pētījums: skolēns pieraksta savu
diennakti, izsaka katru nodarbi kā daļu no 24 stundām un salīdzina ar
klasesbiedriem. Dati, daļas un diagramma vienā projektā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, kolonnas)

TEMA = "Cik daudz laika veltu mācībām?"

MERKIS = ("Veiksim praktisku pētījumu par diennakts sadalījumu un apkoposim "
          "datus ar daļām.")

SATURS = [
    Sakums("Kur paliek tava diennakts?",
           zimejums=kolonnas([("miegs", 9), ("skola", 6), ("mājasd.", 2),
                              ("ēšana", 2), ("brīvais", 5)], " h"),
           paraksts="Kopā 24 stundas.",
           fakti=["Miegs ir lielākā daļa - {9|24} diennakts.",
                  "Skola - {6|24} jeb {1|4} diennakts."]),

    Doma("Stundas no 24 - diennakts daļa",
         "Katras nodarbes laiks stundās ir skaitītājs, 24 - saucējs; visu "
         "daļu summa ir {24|24} = 1.",
         soli=[
             "Pieraksti katras nodarbes stundas.",
             "Pārbaudi: summa 24.",
             "Katru izsaki daļā: {9|24}, {6|24}, ...",
             "Salīdzini: kura daļa lielākā, kura mazākā?",
         ],
         pieze="Ja summa nav 24, kaut kas aizmirsts - ceļš, sports, "
               "spēles."),

    Petijums("Mana diennakts",
             soli=[
                 "Vienu darbdienu pieraksti, cik stundu katrai nodarbei.",
                 "Pārbaudi, vai kopā 24 h.",
                 "Uzraksti katru kā daļu no 24.",
                 "Uzzīmē stabiņu diagrammu un salīdzini ar klasesbiedru.",
             ],
             vajag="burtnīca, pulkstenis",
             secinajums="Diagramma un daļas parāda, kur tiešām aiziet laiks."),

    Ievadi("Diennakts daļas", [
        {"jaut": "Miegs 9 h. Kāda daļa diennakts? (saucējs 24)",
         "atb": ["9/24"], "vieta": "piem., 1/2", "padoms": "9 no 24."},
        {"jaut": "Skola 6 h. Kāda pamatdaļa diennakts?", "atb": ["1/4"],
         "vieta": "piem., 1/2", "padoms": "24 : 6 = 4."},
        {"jaut": "Mājasdarbi 2 h. Kāda pamatdaļa diennakts?",
         "atb": ["1/12"], "vieta": "piem., 1/2", "padoms": "24 : 2."},
        {"jaut": "Cik stundu ir {1|3} diennakts?", "atb": ["8"],
         "padoms": "24 : 3."},
    ]),

    Varianti("Ko rāda dati?", [
        {"jaut": "Kura daļa lielākā: miegs {9|24} vai skola {6|24}?",
         "opcijas": ["miegs", "skola", "vienādi"], "pareizi": 0,
         "padoms": "9 > 6."},
        {"jaut": "Vai {1|3} diennakts gulēt ir pietiekami 10 gadus vecam?",
         "opcijas": ["mazāk nekā ieteikts (9-11 h)", "par daudz",
                     "tieši tik"], "pareizi": 0,
         "padoms": "{1|3} = 8 h."},
        {"jaut": "Visu nodarbju daļu summa ir...",
         "opcijas": ["1", "24", "{1|24}", "atkarīgs no dienas"],
         "pareizi": 0, "padoms": "{24|24}."},
    ]),

    Pasaule("Ekrāna laiks",
            Ievadi("", [
                {"jaut": "Ekrānu lieto 3 h dienā. Kāda daļa diennakts? "
                         "(pamatdaļa)",
                 "atb": ["1/8"], "vieta": "piem., 1/2", "padoms": "24 : 3."},
                {"jaut": "Cik stundu nedēļā (7 dienas)?", "atb": ["21"],
                 "padoms": "3 · 7."},
                {"jaut": "Ja samazina par {1|3}, cik stundu dienā?",
                 "atb": ["2"], "padoms": "3 − 1."},
                {"jaut": "Cik stundu nedēļā ietaupās?", "atb": ["7"],
                 "padoms": "1 · 7."},
            ]),
            pavediens="dati",
            konteksts="Telefoni rāda ekrāna laiku - un to var izteikt kā daļu "
                      "no diennakts.",
            kapec="Daļa palīdz saprast, cik liels ir ieradums."),

    Kopsavilkums([
        "Veicu pētījumu par savu diennakti.",
        "Izsaku nodarbes kā daļas no 24 stundām.",
        "Salīdzinu un attēloju datus.",
    ]),

    Majas([
        "Nedēļas nogalē atkārto pētījumu - kas mainās?",
        "Pārrunā ar ģimeni, kāda daļa diennakts ir kopā pavadīta.",
        "Izveido diagrammu brīvdienai un darbdienai blakus.",
    ]),
]
