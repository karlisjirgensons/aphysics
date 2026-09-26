# -*- coding: utf-8 -*-
"""4. klase, 54. stunda: «Kas ir stars un kas - leņķis?»

Stars ir taisnes daļa ar sākumpunktu - kā lukturīša gaisma. Divi stari ar
kopīgu sākumpunktu veido leņķi. Skolēns vispirms apraksta savos vārdos un
salīdzina ar citu aprakstiem, tikai tad nonāk pie vienotas definīcijas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, Zimejums, lenkis,
                         linijas)

TEMA = "Kas ir stars un kas - leņķis?"

MERKIS = ("Aprakstīsim staru un leņķi savos vārdos un salīdzināsim savu "
          "aprakstu ar citu aprakstiem.")

SATURS = [
    Sakums("Kur beidzas lāzera stars?",
           zimejums=linijas([(1, 2, 11, 2, "stars")],
                            uzraksti=[(1, 2.6, "O")],
                            punkti=[(1, 2)], platums=12, augstums=3),
           paraksts="Stars sākas punktā O un turpinās bez gala.",
           fakti=["Lāzera staru no Zemes raida līdz Mēness atstarotājiem.",
                  "Matemātikā stars ir līnija ar sākumu, bet bez beigām."]),

    Doma("Divi stari ar kopīgu sākumu veido leņķi",
         "Stars ir taisnes daļa, kurai ir sākumpunkts; leņķis ir figūra no "
         "diviem stariem ar kopīgu sākumpunktu.",
         soli=[
             "Nogrieznim ir divi gali, staram - viens, taisnei - neviena.",
             "Leņķa stari ir tā malas.",
             "Kopīgais sākumpunkts ir leņķa virsotne.",
             "Leņķa lielumu nosaka tas, cik tālu malas ir «atvērtas».",
         ],
         pieze="Pulksteņa rādītāji ir leņķa malas, un ass centrā - virsotne."),

    Zimejums("Leņķa daļas",
             lenkis([(0, "mala"), (60, "mala")], loki=[(0, 60, "leņķis")]),
             paskaidro="Punkts, kurā satiekas malas, ir virsotne.",
             ievads="Divi stari no viena punkta."),

    Varianti("Nogrieznis, stars vai taisne?", [
        {"jaut": "Lukturīša gaisma tumsā",
         "opcijas": ["stars", "nogrieznis", "taisne"], "pareizi": 0,
         "padoms": "Sākas lukturī un iet tālu."},
        {"jaut": "Zīmuļa mala",
         "opcijas": ["nogrieznis", "stars", "taisne"], "pareizi": 0,
         "padoms": "Tai ir divi gali."},
        {"jaut": "Līnija bez sākuma un beigām",
         "opcijas": ["taisne", "stars", "nogrieznis"], "pareizi": 0,
         "padoms": "Turpinās uz abām pusēm."},
        {"jaut": "Kas ir leņķa virsotne?",
         "opcijas": ["kopīgais staru sākumpunkts", "staru gals",
                     "vidējais punkts uz malas", "loks"], "pareizi": 0,
         "padoms": "Tur abi stari sākas."},
        {"jaut": "Cik malu ir leņķim?",
         "opcijas": ["2", "1", "3", "4"], "pareizi": 0,
         "padoms": "Divi stari."},
        {"jaut": "Cik galu ir staram?",
         "opcijas": ["1", "0", "2", "bezgalīgi"], "pareizi": 0,
         "padoms": "Tikai sākumpunkts."},
    ], pamats=4),

    Ievadi("Saskaiti", [
        {"jaut": "No viena punkta iziet 2 stari. Cik leņķu (mazāku par "
                 "izstieptu) tie veido?", "atb": ["1"],
         "padoms": "Viens leņķis starp tiem."},
        {"jaut": "Cik virsotņu ir trijstūrim?", "atb": ["3"],
         "padoms": "Trīs stūri."},
        {"jaut": "Cik leņķu ir kvadrātam?", "atb": ["4"],
         "padoms": "Četri stūri."},
        {"jaut": "Cik galu ir 3 nogriežņiem kopā?", "atb": ["6"],
         "padoms": "3 · 2."},
    ]),

    Pasaule("Bākas gaisma",
            Varianti("", [
                {"jaut": "Bāka griežas un raida gaismas staru. Kur ir stara "
                         "sākumpunkts?",
                 "opcijas": ["bākas lampā", "uz kuģa", "jūrā"],
                 "pareizi": 0, "padoms": "No turienes gaisma nāk."},
                {"jaut": "Divi prožektori no viena punkta. Ko veido to "
                         "stari?",
                 "opcijas": ["leņķi", "taisni", "nogriezni"], "pareizi": 0,
                 "padoms": "Divi stari ar kopīgu sākumu."},
                {"jaut": "Ja prožektorus pagriež tālāk vienu no otra, leņķis...",
                 "opcijas": ["palielinās", "samazinās", "nemainās"],
                 "pareizi": 0, "padoms": "Malas atveras."},
            ]),
            pavediens="tehnika",
            konteksts="Bākas un prožektori ir īsti stari - gaisma sākas "
                      "vienā punktā un iet tālu.",
            kapec="Staru un leņķi var redzēt katru vakaru, ja paskatās."),

    Petijums("Mans leņķa apraksts",
             soli=[
                 "Uzraksti savos vārdos: kas ir leņķis?",
                 "Izlasi divu klasesbiedru aprakstus.",
                 "Kas visos aprakstos ir kopīgs? Kas trūkst?",
                 "Uzraksti kopīgu, precīzu aprakstu.",
             ],
             secinajums="Labā aprakstā ir divi stari un kopīgs sākumpunkts."),

    Kopsavilkums([
        "Atšķiru nogriezni, staru un taisni.",
        "Zinu, ka leņķi veido divi stari ar kopīgu sākumpunktu.",
        "Nosaucu leņķa virsotni un malas.",
    ]),

    Majas([
        "Atrodi mājās 5 leņķus (šķēres, grāmata, durvis) un parādi virsotni.",
        "Uzzīmē staru, nogriezni un taisni un paskaidro atšķirību.",
        "Pavēro pulksteni: kādu leņķi rādītāji veido plkst. 3?",
    ]),
]
