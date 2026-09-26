# -*- coding: utf-8 -*-
"""8. klase, 89. stunda: «Kā perpendikulitāte dod paralelitāti?»

Bloka noslēgums: a ⊥ c un b ⊥ c ⇒ a ∥ b, jo kāpšļu leņķi abi ir 90°.
Otrādi: ja a ∥ b un c ⊥ a, tad c ⊥ b. Tā zīmē paralēlas taisnes ar
stūreni un lineālu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, geometrija)

TEMA = "Kā perpendikulitāte dod paralelitāti?"

MERKIS = ("Pamatosim, ka divas taisnes, kas perpendikulāras trešajai, ir "
          "paralēlas.")

SATURS = [
    Sakums("Abas taisnes ir perpendikulāras c. Kas tad?",
           zimejums=geometrija(
               [("M", 0, 0, 225), ("N", 0, 3, 135), ("_c1", 0, -1.5),
                ("_c2", 0, 4.5), ("_a1", -3, 0), ("_a2", 4, 0),
                ("_b1", -3, 3), ("_b2", 4, 3)],
               taisnes=[("_c1", "_c2"), ("_a1", "_a2"), ("_b1", "_b2")],
               taisni=[("_a2", "M", "N"), ("_b2", "N", "_c2")],
               uzraksti=[(4.4, 0.35, "a"), (4.4, 3.35, "b"),
                         (0.4, 4.7, "c")]),
           paraksts="a ⊥ c un b ⊥ c, tātad a ∥ b.",
           fakti=["Divas taisnes, kas perpendikulāras trešajai, ir "
                  "paralēlas.",
                  "Pamatojums: kāpšļu leņķi abi ir 90°.",
                  "Tā zīmē paralēlas taisnes ar stūreni un lineālu."]),

    Doma("No perpendikulitātes uz paralelitāti",
         "Perpendikulāras taisnes veido taisnus kāpšļu leņķus.",
         soli=[
             "a ⊥ c, tātad leņķis pie M ir 90°.",
             "b ⊥ c, tātad kāpšļu leņķis pie N arī ir 90°.",
             "Kāpšļu leņķi vienādi - pēc pazīmes a ∥ b.",
             "Otrādi: ja a ∥ b un c ⊥ a, tad arī c ⊥ b.",
         ]),

    Paraugs("Pierādījums",
            uzd="Dots: a ⊥ c, b ⊥ c. Pierādi, ka a ∥ b.",
            soli=[
                ("Leņķis starp a un c ir 90°", "Dots a ⊥ c."),
                ("Leņķis starp b un c ir 90°", "Dots b ⊥ c."),
                ("Kāpšļu leņķi ir vienādi", "Abi 90°."),
                ("a ∥ b", "Pēc kāpšļu leņķu pazīmes."),
            ],
            atbilde="a ∥ b"),

    Varianti("Spried", [
        {"jaut": "Rūtiņu lapā vertikālās līnijas ir paralēlas, jo...",
         "opcijas": ["tās visas ir ⊥ horizontālajām",
                     "tās ir vienāda garuma", "tās ir vienā krāsā",
                     "tās nekrustojas uz lapas"],
         "pareizi": 0, "padoms": "Perpendikulāras vienai taisnei."},
        {"jaut": "a ∥ b un c ⊥ a. Tad c un b ir...",
         "opcijas": ["perpendikulāras", "paralēlas", "viena taisne",
                     "nevar noteikt"],
         "pareizi": 0, "padoms": "Kāpšļu leņķi vienādi - 90°."},
        {"jaut": "Kāds ir abu kāpšļu leņķu lielums?",
         "opcijas": ["90°", "45°", "180°", "60°"],
         "pareizi": 0, "padoms": "Perpendikulāras taisnes."},
    ]),

    Ievadi("Aprēķini", [
        {"jaut": "Taisnstūrī ABCD malas AD un BC abas ir ⊥ AB. Cik ir "
                 "paralēlu malu pāru?", "atb": ["2"],
         "padoms": "AD ∥ BC un AB ∥ CD."},
        {"jaut": "a ∥ b, c ⊥ a. Leņķis starp c un b (°)?", "atb": ["90"],
         "padoms": "Kāpšļu leņķi."},
        {"jaut": "Kāpnēm 12 pakāpieni, visi ⊥ vertikālajai sijai. Cik ir "
                 "paralēlu pakāpienu pāru?", "atb": ["66"],
         "padoms": "{12 · 11|2}."},
    ]),

    Pasaule("Plauktu statne",
            Ievadi("", [
                {"jaut": "Plaukti piestiprināti ⊥ vertikālai statnei. Vai tie "
                         "ir paralēli? (1 - jā, 0 - nē)",
                 "atb": ["1"], "padoms": "Divas ⊥ trešajai."},
                {"jaut": "Statne ir sasvērta, bet plaukti vienalga ⊥ tai. Vai "
                         "plaukti paralēli? (1/0)",
                 "atb": ["1"], "padoms": "Pazīme nav atkarīga no slīpuma."},
                {"jaut": "Statne sasvērta par 5°. Par cik grādiem plaukti "
                         "slīpi pret horizontāli?",
                 "atb": ["5"], "padoms": "Plaukts pagriežas kopā ar statni."},
            ]),
            pavediens="maja",
            konteksts="Plauktu sistēmās plauktus stiprina perpendikulāri "
                      "statnei.",
            kapec="Divas taisnes, kas perpendikulāras trešajai, ir "
                  "paralēlas."),

    Kopsavilkums([
        "Pamatoju, ka divas taisnes, kas ⊥ trešajai, ir paralēlas.",
        "Lietoju apgriezto apgalvojumu: c ⊥ a un a ∥ b ⇒ c ⊥ b.",
        "Zīmēju paralēlas taisnes ar stūreni.",
    ]),

    Majas([
        "Ar stūreni un lineālu uzzīmē trīs paralēlas taisnes.",
        "Atrodi mājās piemēru, kur paralēlas līnijas ir ⊥ vienai.",
        "Pieraksti pierādījumu ar saviem vārdiem.",
    ]),
]
