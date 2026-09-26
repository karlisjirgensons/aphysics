# -*- coding: utf-8 -*-
"""9. klase, 15. stunda: «Kur kļūdās pierādījums?»

Eksāmenā punktus zaudē ne tikai par nepareizu atbildi, bet par pamatojumu,
kurā trūkst soļa vai iemesla. Šajā stundā skolēns ir vērtētājs: lasa
svešu pierādījumu, atrod kļūdaino soli un pasaka, kāpēc tas neder.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, geometrija)

TEMA = "Kur kļūdās pierādījums?"

MERKIS = "Lasīsim pierādījumu, atradīsim un paskaidrosim kļūdu tajā."

_ZIM = geometrija([("A", 0, 0), ("B", 9, 0), ("C", 3, 6), ("D", 3, 0),
                   ("E", 5, 4)],
                  nogriezni=["AB", "BC", "CA"], izcelti=["DE"],
                  lenki=[("BAC", "", 1), ("BDE", "", 1)])

SATURS = [
    Sakums("Atbilde pareiza, bet 0 punktu?",
           zimejums=_ZIM,
           paraksts="«Trijstūri ir līdzīgi, jo tā izskatās» - tas nav "
                    "pamatojums.",
           fakti=["Katram apgalvojumam vajag iemeslu.",
                  "Pazīmei vajag tieši to, ko tā prasa - ne mazāk.",
                  "Virsotņu secība pierakstā ir svarīga."]),

    Doma("Biežākās kļūdas",
         "Pārbaudi katru soli: vai iemesls ir pateikts un vai tas tiešām "
         "der?",
         soli=[
             "Līdzība «no zīmējuma» bez pazīmes.",
             "Tikai viens vienāds leņķis vai divas malas bez leņķa starp tām.",
             "Nepareiza virsotņu secība - nepareiza proporcija.",
             "«Līdzīgi» sajaukts ar «vienādi»: malas proporcionālas, nevis "
             "vienādas.",
         ]),

    Slidnis("Lasi pierādījumu", [
        {"v": "Dots", "teksts": "DE ∥ AC. Pierādīt: △DBE ∼ △ABC.",
         "zim": _ZIM},
        {"v": "1. solis", "teksts": "∠B ir kopīgs. ✔ Pareizi.",
         "zim": _ZIM},
        {"v": "2. solis", "teksts": "∠BDE = ∠BAC, jo tie ir krustleņķi. ✘ "
                                    "Tie ir kāpšļu leņķi pie DE ∥ AC.",
         "zim": _ZIM},
        {"v": "3. solis", "teksts": "Tātad DE = AC. ✘ Līdzībā malas ir "
                                    "proporcionālas, nevis vienādas.",
         "zim": _ZIM},
    ], ievads="Katru soli novērtē: ✔ vai ✘ un kāpēc."),

    Varianti("Kur kļūda?", [
        {"jaut": "«∠A = ∠K, tātad △ABC ∼ △KLM.»",
         "opcijas": ["Vajag vēl vienu vienādu leņķi",
                     "Nav kļūdas", "Jāraksta △KML", "Vajag trīs malas"],
         "pareizi": 0, "padoms": "Pazīmei vajag divus leņķus."},
        {"jaut": "«AB = 4, BC = 6, ∠C = 30°; KL = 8, LM = 12, ∠M = 30°. "
                 "Līdzīgi pēc 2. pazīmes.»",
         "opcijas": ["Leņķis nav starp dotajām malām",
                     "Malas nav proporcionālas", "Nav kļūdas",
                     "Jābūt 3. pazīmei"],
         "pareizi": 0, "padoms": "Starp AB un BC ir ∠B."},
        {"jaut": "«△ABC ∼ △KLM, tāpēc {AB|KM} = {BC|KL}.»",
         "opcijas": ["Nepareizas atbilstošās malas",
                     "Nav kļūdas", "Jāraksta ar reizinājumu",
                     "Trijstūri nav līdzīgi"],
         "pareizi": 0, "padoms": "AB atbilst KL, BC - LM."},
        {"jaut": "«Malas 3, 4, 5 un 6, 8, 11. {6|3} = {8|4} = 2, līdzīgi.»",
         "opcijas": ["Nepārbaudīja trešo malu: {11|5} ≠ 2",
                     "Nav kļūdas", "Jādala otrādi", "Vajag leņķus"],
         "pareizi": 0, "padoms": "Visas trīs attiecības."},
    ]),

    Ievadi("Salabo aprēķinu", [
        {"jaut": "△ABC ∼ △KLM, AB = 6, KL = 9, LM = 12. Skolēns ieguva "
                 "BC = 18. Pareizi BC = ?", "atb": ["8"],
         "padoms": "k = 1,5, BC = 12 : 1,5."},
        {"jaut": "Līdzīgu trijstūru laukumi 4 un 36. Skolēns: k = 9. "
                 "Pareizi k = ?", "atb": ["3"], "padoms": "k = √9."},
        {"jaut": "DE ∥ AC, BD = 2, DA = 3, DE = 4. Skolēns: AC = 6. "
                 "Pareizi AC = ?", "atb": ["10"], "padoms": "BA = 5."},
    ]),

    Pasaule("Klasesbiedra mājasdarbs",
            Varianti("", [
                {"jaut": "Draugs raksta: «Trijstūri līdzīgi, jo abiem ir "
                         "taisns leņķis.» Ko ieteiksi?",
                 "opcijas": ["Atrast vēl vienu vienādu leņķi",
                             "Viss pareizi", "Izmērīt visas malas ar lineālu",
                             "Pārzīmēt"],
                 "pareizi": 0, "padoms": "Viens leņķis nepietiek."},
                {"jaut": "Draugs līdzību pierakstīja △ABC ∼ △MLK, bet "
                         "atbilstošās ir A-K, B-L, C-M. Kā labot?",
                 "opcijas": ["△ABC ∼ △KLM", "Neko", "△ABC ∼ △LKM",
                             "△ACB ∼ △KLM"],
                 "pareizi": 0, "padoms": "Virsotnes pa pāriem."},
            ]),
            pavediens="skola",
            konteksts="Labākais veids iemācīties pierādīt - pārbaudīt citu "
                      "pierādījumu kā skolotājs.",
            kapec="Kļūdu atrast svešā darbā ir vieglāk nekā savā."),

    Kopsavilkums([
        "Pārbaudu, vai katram solim ir pareizs iemesls.",
        "Pamanu nepilnīgi izmantotu pazīmi.",
        "Pamanu nepareizu virsotņu atbilstību.",
    ]),

    Majas([
        "Uzraksti pierādījumu ar vienu apzinātu kļūdu un iedod to draugam.",
        "Pārbaudi savus iepriekšējos risinājumus: vai katram solim ir iemesls?",
        "Pieraksti trīs frāzes, ar kurām pamato vienādus leņķus.",
    ]),
]
