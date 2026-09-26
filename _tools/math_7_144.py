# -*- coding: utf-8 -*-
"""7. klase, 144. stunda: «Vai proporcija šeit der?»

Proporciju drīkst lietot tikai tad, ja lielumi ir tieši (vai apgriezti)
proporcionāli. Daudzas situācijas izskatās proporcionālas, bet nav:
taksometrs ar iekāpšanas maksu, augšana, atlaide no noteiktas summas.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, Zimejums, restis)

TEMA = "Vai proporcija šeit der?"

MERKIS = ("Izvērtēsim, vai situācijā lielumi ir proporcionāli, un "
          "pamatosim izvēli.")

SATURS = [
    Sakums("Bērns 10 gados 140 cm. 20 gados - 280 cm?",
           zimejums=restis([["vecums", "augums"],
                            ["10 gadi", "140 cm"],
                            ["20 gadi", "? (ne 280!)"]]),
           paraksts="Proporcija dod absurdu atbildi.",
           fakti=["Augšana nav tieši proporcionāla vecumam.",
                  "Pirms proporcijas jāpārbauda, vai tā der.",
                  "Pārbaude: divreiz vairāk - divreiz vairāk?"]),

    Doma("Pārbaudi pirms lieto",
         "Tiešo proporciju drīkst lietot, ja, vienu lielumu palielinot n "
         "reizes, otrs arī palielinās n reizes (un 0 atbilst 0). Apgriezto - "
         "ja otrs samazinās n reizes.",
         soli=[
             "Jautā: ja pirmo divkāršo, vai otrs divkāršojas?",
             "Jautā: vai 0 atbilst 0 (nav fiksētas maksas)?",
             "Ja jā - tieša proporcionalitāte.",
             "Ja otrs samazinās divreiz - apgriezta; citādi - neder.",
         ],
         pieze="Apgrieztā: 2 strādnieki - 6 dienas, 4 strādnieki - 3 dienas. "
               "Proporcija tad ir «otrādi»: 2 · 6 = 4 · x."),

    Paraugs("Taksometrs",
            uzd="Taksometrs: 3 km - 5 €. Vai 6 km maksās 10 €, ja tarifs "
                "ir 2 € + 1 € par km?",
            soli=[
                ("3 km: 2 + 3 = 5 (€)", "Pārbauda."),
                ("6 km: 2 + 6 = 8 (€)", "Nevis 10."),
                ("Iekāpšanas maksa - nav proporcionāli", "0 km maksā 2 €."),
            ],
            atbilde="Nē - 8 €, proporcija neder."),

    Varianti("Der vai neder?", [
        {"jaut": "Benzīna litri un cena",
         "opcijas": ["Tieša proporcija", "Apgriezta proporcija", "Neder"],
         "pareizi": 0, "jaukt": False, "padoms": "Divreiz vairāk - divreiz "
                                                 "dārgāk."},
        {"jaut": "Ātrums un laiks noteiktam ceļam",
         "opcijas": ["Tieša proporcija", "Apgriezta proporcija", "Neder"],
         "pareizi": 1, "jaukt": False, "padoms": "vt = s."},
        {"jaut": "Telefona tarifs 5 € + 0,1 € par min",
         "opcijas": ["Tieša proporcija", "Apgriezta proporcija", "Neder"],
         "pareizi": 2, "jaukt": False, "padoms": "Fiksētā daļa."},
        {"jaut": "Skrējēja laiks 100 m un 1000 m",
         "opcijas": ["Tieša proporcija", "Apgriezta proporcija", "Neder"],
         "pareizi": 2, "jaukt": False, "padoms": "Garākā distancē nogurst."},
        {"jaut": "Strādnieku skaits un darba dienas",
         "opcijas": ["Tieša proporcija", "Apgriezta proporcija", "Neder"],
         "pareizi": 1, "jaukt": False, "padoms": "Vairāk cilvēku - ātrāk."},
        {"jaut": "Kvadrāta mala un laukums",
         "opcijas": ["Tieša proporcija", "Apgriezta proporcija", "Neder"],
         "pareizi": 2, "jaukt": False, "padoms": "Divreiz mala - 4 reiz "
                                                 "laukums."},
    ], pamats=4),

    Pasaule("Lielā pica pret mazo",
            Varianti("", [
                {"jaut": "Pica 30 cm maksā 9 €. Vai 60 cm picai jāmaksā 18 €?",
                 "opcijas": ["Nē - tā ir 4 reizes lielāka pēc laukuma",
                             "Jā", "Nē - jāmaksā 9 €", "Nevar zināt"],
                 "pareizi": 0, "padoms": "Laukums aug kā kvadrāts."},
                {"jaut": "Kas ir izdevīgāk: 2 picas 30 cm vai 1 pica 60 cm "
                         "par vienādu cenu?",
                 "opcijas": ["1 pica 60 cm - tajā divreiz vairāk",
                             "2 picas 30 cm", "Vienādi", "Nevar zināt"],
                 "pareizi": 0, "padoms": "4 : 2."},
            ]),
            pavediens="virtuve",
            konteksts="Picas cena pēc diametra ir klasisks slazds - laukums "
                      "nav proporcionāls diametram.",
            kapec="Proporcija der tikai proporcionāliem lielumiem."),

    Zimejums("Pārbaudes tabula",
             restis([["divkāršo pirmo", "otrs...", "secinājums"],
                     ["divkāršojas", "×2", "tieša"],
                     ["samazinās 2×", ":2", "apgriezta"],
                     ["cits", "?", "proporcija neder"]]),
             paskaidro="Viens jautājums izšķir metodi."),

    Kopsavilkums([
        "Pārbaudu, vai lielumi ir proporcionāli.",
        "Atšķiru tiešu un apgrieztu proporcionalitāti.",
        "Atpazīstu fiksētu maksu un nelineāras sakarības.",
        "Pamatoju, kāpēc proporcija der vai neder.",
    ]),

    Majas([
        "Atrodi 2 situācijas, kurās proporcija der, un 2, kurās neder.",
        "Salīdzini divu picu izmēru cenas picērijā.",
        "Atrisini ar apgriezto proporciju: 3 sūkņi - 8 h, 4 sūkņi - ?",
    ]),
]
