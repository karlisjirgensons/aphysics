# -*- coding: utf-8 -*-
"""2. klase, 151. stunda: «Kurus reizinājumus vēl jāiemācās?»

Mikrotemata noslēgums: pašpārbaude ar visām četrām tabulām (2, 3, 4, 5).
Skolēns atzīmē, kuri reizinājumi vēl nav galvā, un izvēlas, ko trenēt
mērķtiecīgi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, restis)

TEMA = "Kurus reizinājumus vēl jāiemācās?"

MERKIS = ("Šodien pārbaudīsim sevi ar kartītēm un izvēlēsimies, ko trenēt "
          "mērķtiecīgi.")

SATURS = [
    Sakums("Cik reizinājumu tev jau ir galvā?",
           zimejums=restis([["tabula", "zinu", "trenēt"],
                            ["· 2", "", ""], ["· 3", "", ""],
                            ["· 4", "", ""], ["· 5", "", ""]]),
           paraksts="Aizpildi savu tabulu.",
           fakti=["40 reizinājumi - 4 tabulas pa 10.",
                  "Daudzus jau zini.",
                  "Trenē tikai tos, kas vēl grūti."]),

    Doma("Mērķtiecīgi",
         "Treniņš ir efektīvs, ja trenē tieši to, ko vēl nezini.",
         soli=[
             "Pārbaudi sevi ar visām kartītēm.",
             "Zināmās liec malā.",
             "Pieraksti grūtās.",
             "Trenē grūtās katru dienu.",
         ],
         pieze="Palīgi: 4 = divreiz dubultot, 5 = puse no 10, vietas maiņa."),

    Ievadi("Pašpārbaude", [
        {"jaut": "7 · 4 = ?", "atb": ["28"], "padoms": "14, 28."},
        {"jaut": "8 · 5 = ?", "atb": ["40"], "padoms": "Puse no 80."},
        {"jaut": "6 · 3 = ?", "atb": ["18"], "padoms": "3 · 6."},
        {"jaut": "9 · 4 = ?", "atb": ["36"], "padoms": "18, 36."},
        {"jaut": "7 · 5 = ?", "atb": ["35"], "padoms": "Puse no 70."},
        {"jaut": "8 · 3 = ?", "atb": ["24"], "padoms": "7 · 3 + 3."},
        {"jaut": "6 · 4 = ?", "atb": ["24"], "padoms": "12, 24."},
        {"jaut": "9 · 2 = ?", "atb": ["18"], "padoms": "9 + 9."},
    ], pamats=6),

    Varianti("Kurš triks?", [
        {"jaut": "Kā atcerēties 8 · 4?",
         "opcijas": ["dubultot 8 divreiz: 16, 32", "puse no 80",
                     "8 + 4"], "pareizi": 0, "padoms": "Reizināt ar 4."},
        {"jaut": "Kā atcerēties 6 · 5?",
         "opcijas": ["puse no 60", "6 + 5", "dubultot 6"], "pareizi": 0,
         "padoms": "Reizināt ar 5."},
    ]),

    Pasaule("Tirgus diena",
            Ievadi("", [
                {"jaut": "Zemenes 4 € kastīte. Nopirka 6. Cik maksā?",
                 "atb": ["24"], "mers": "€", "padoms": "6 · 4."},
                {"jaut": "Gurķi 3 € kilogramā, nopirka 5 kg. Cik maksā?",
                 "atb": ["15"], "mers": "€", "padoms": "5 · 3."},
            ]),
            pavediens="veikals",
            konteksts="Sestdienas tirgū pārdod ogas un dārzeņus.",
            kapec="Kas zina reizinājumus, zina cenu uzreiz."),

    Kopsavilkums([
        "Pārbaudu sevi ar visām tabulām.",
        "Zinu, kuri reizinājumi vēl jātrenē.",
        "Izmantoju trikus, lai atcerētos.",
    ]),

    Majas([
        "Katru dienu trenē 5 grūtākās kartītes.",
        "Pēc nedēļas pārbaudi sevi vēlreiz.",
        "Pieraksti, cik reizinājumu zini tagad.",
    ]),
]
