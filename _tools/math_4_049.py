# -*- coding: utf-8 -*-
"""4. klase, 49. stunda: «Kā izvietotas rūtiņu lapas līnijas?»

4.3. temata sākums. Rūtiņu lapa ir gatavs paralēlu un perpendikulāru
līniju modelis: horizontālās līnijas nekad nekrustojas, bet horizontālā ar
vertikālo krustojas taisnā leņķī. No šīs lapas izaug viss temats - leņķi,
grādi un figūru zīmēšana.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, Zimejums, lenkis,
                         linijas)

TEMA = "Kā izvietotas rūtiņu lapas līnijas?"

MERKIS = ("Raksturosim paralēlas un perpendikulāras līnijas un atradīsim to "
          "piemērus apkārtnē.")

SATURS = [
    Sakums("Kāpēc sliedes nekad nesatiekas?",
           zimejums=linijas([(0, 3, 12, 3, "stars"),
                             (0, 1, 12, 1, "stars")],
                            uzraksti=[(6, 3.5, "a"), (6, 1.5, "b")],
                            platums=12, augstums=4),
           paraksts="a ∥ b - taisnes ir paralēlas.",
           fakti=["Sliežu attālums visā garumā ir vienāds.",
                  "Tāpēc tās nekrustojas, lai cik garas būtu.",
                  "Tādas līnijas sauc par paralēlām."]),

    Doma("Paralēlas nekrustojas, perpendikulāras krustojas taisnā leņķī",
         "Paralēlas taisnes (a ∥ b) plaknē nekad nekrustojas; "
         "perpendikulāras (a ⊥ c) krustojas, veidojot taisnu leņķi.",
         soli=[
             "Rūtiņu lapas horizontālās līnijas ir paralēlas.",
             "Vertikālās līnijas arī ir paralēlas cita citai.",
             "Horizontālā un vertikālā līnija ir perpendikulāras.",
             "Pieraksts: a ∥ b - «a ir paralēla b»; a ⊥ c - «a ir "
             "perpendikulāra c».",
         ],
         pieze="Taisnu leņķi zīmējumā atzīmē ar mazu kvadrātiņu virsotnē."),

    Zimejums("Perpendikulāras taisnes",
             lenkis([(0, "a"), (90, "c"), (180, ""), (270, "")],
                    loki=[(0, 90, "90°")], r=26),
             paskaidro="Četri leņķi pie krustpunkta - visi taisni.",
             ievads="a ⊥ c: krustojoties rodas četri vienādi leņķi."),

    Varianti("Paralēlas vai perpendikulāras?", [
        {"jaut": "Grāmatas plaukta divi plaukti viens virs otra",
         "opcijas": ["paralēli", "perpendikulāri", "ne viens, ne otrs"],
         "pareizi": 0, "padoms": "Tie nekrustojas."},
        {"jaut": "Grīda un siena",
         "opcijas": ["perpendikulāras", "paralēlas", "ne viens, ne otrs"],
         "pareizi": 0, "padoms": "Satiekas taisnā leņķī."},
        {"jaut": "Šķēru asmeņi, kad šķēres ir atvērtas",
         "opcijas": ["ne viens, ne otrs", "paralēli", "perpendikulāri"],
         "pareizi": 0, "padoms": "Krustojas, bet ne taisnā leņķī."},
        {"jaut": "Gājēju pārejas svītras",
         "opcijas": ["paralēlas", "perpendikulāras", "ne viens, ne otrs"],
         "pareizi": 0, "padoms": "Visas vienā virzienā."},
        {"jaut": "Ko nozīmē zīme ⊥?",
         "opcijas": ["perpendikulāras", "paralēlas", "vienādas",
                     "krustojas jebkādi"], "pareizi": 0,
         "padoms": "Apgriezts «T» - taisns leņķis."},
        {"jaut": "Ko nozīmē zīme ∥?",
         "opcijas": ["paralēlas", "perpendikulāras", "vienādi garas",
                     "krustojas"], "pareizi": 0,
         "padoms": "Divas vienādi vērstas svītriņas."},
    ], pamats=4),

    Ievadi("Saskaiti rūtiņu lapā", [
        {"jaut": "Lapā 5 horizontālas līnijas. Cik pāru paralēlu līniju "
                 "var izvēlēties no divām blakus esošām?",
         "atb": ["4"], "padoms": "1.-2., 2.-3., 3.-4., 4.-5."},
        {"jaut": "3 horizontālas un 4 vertikālas līnijas. Cik krustpunktu?",
         "atb": ["12"], "padoms": "3 · 4."},
        {"jaut": "Cik taisnu leņķu veidojas vienā krustpunktā?",
         "atb": ["4"], "padoms": "Paskaties uz zīmējumu."},
        {"jaut": "Cik taisnu leņķu pavisam pie 12 krustpunktiem?",
         "atb": ["48"], "padoms": "12 · 4."},
    ]),

    Pasaule("Pilsētas ielu tīkls",
            Varianti("", [
                {"jaut": "Ņujorkā Manhetenas ielas un avēnijas krustojas "
                         "taisnā leņķī. Kādas tās ir?",
                 "opcijas": ["perpendikulāras", "paralēlas",
                             "ne viens, ne otrs"], "pareizi": 0,
                 "padoms": "Taisns leņķis."},
                {"jaut": "Visas avēnijas savā starpā ir...",
                 "opcijas": ["paralēlas", "perpendikulāras",
                             "krustojas"], "pareizi": 0,
                 "padoms": "Tās iet vienā virzienā."},
                {"jaut": "Rīgas Vecrīgā ielas ir līkumainas. Vai tās ir "
                         "paralēlas?",
                 "opcijas": ["lielākoties nē", "visas jā",
                             "visas perpendikulāras"], "pareizi": 0,
                 "padoms": "Viduslaiku ielas neplānoja ar lineālu."},
            ]),
            pavediens="celojums",
            konteksts="Jaunajās pilsētās ielas plāno kā rūtiņu lapu - tāpēc "
                      "tajās ir viegli orientēties.",
            kapec="Paralēlas un perpendikulāras ielas padara karti "
                  "saprotamu."),

    Petijums("Līniju meklētāji",
             soli=[
                 "Atrodi klasē 3 paralēlu līniju pārus.",
                 "Atrodi 3 perpendikulāru līniju pārus.",
                 "Pārbaudi perpendikularitāti ar burtnīcas stūri.",
                 "Pieraksti ar zīmēm ∥ un ⊥.",
             ],
             vajag="burtnīca vai papīra lapa ar taisnu stūri",
             secinajums="Taisnie leņķi un paralēlās līnijas ir visur, kur "
                        "cilvēks kaut ko būvē."),

    Kopsavilkums([
        "Zinu, kas ir paralēlas un perpendikulāras līnijas.",
        "Lietoju zīmes ∥ un ⊥.",
        "Atrodu tās apkārtnē un rūtiņu lapā.",
    ]),

    Majas([
        "Atrodi mājās 5 paralēlu un 5 perpendikulāru līniju piemērus.",
        "Uzzīmē savas ielas vai pagalma plānu ar paralēlām līnijām.",
        "Paskaidro mājiniekiem zīmes ∥ un ⊥.",
    ]),
]
