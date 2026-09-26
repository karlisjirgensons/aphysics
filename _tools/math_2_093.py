# -*- coding: utf-8 -*-
"""2. klase, 93. stunda: «Kā pierakstīt savu algoritmu?»

Skolēns pats pieraksta algoritmu - ar skaidriem, secīgiem soļiem - un
pārbauda to, ļaujot klasesbiedram izpildīt burtiski. Ja izpildītājs
kļūdās, parasti vainīgs ir neskaidrs solis.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Pasaule, Petijums,
                         Sakums, Varianti, algoritms, celjs)

TEMA = "Kā pierakstīt savu algoritmu?"

MERKIS = ("Šodien pierakstīsim savu algoritmu uzdevuma izpildei un "
          "pārbaudīsim to ar klasesbiedru.")

SATURS = [
    Sakums("Kā robotam izskaidrot ceļu līdz ābolam?",
           zimejums=celjs(5, 4, (0, 3), (4, 0), "→→→→↑↑↑"),
           paraksts="4 soļi pa labi, 3 uz augšu.",
           fakti=["Robots nesaprot «tur, pie loga».",
                  "Tam vajag precīzus soļus.",
                  "Katram solim - viena darbība."]),

    Doma("Labs algoritms",
         "Katrs solis ir skaidrs, īss un izpildāms tikai vienā veidā.",
         soli=[
             "Sadali uzdevumu mazos soļos.",
             "Katru soli uzraksti ar darbības vārdu: paņem, pieskaiti, ej.",
             "Sakārto soļus pareizā secībā.",
             "Pārbaudi - lai kāds izpilda burtiski.",
         ]),

    Varianti("Vai solis ir skaidrs?", [
        {"jaut": "«Ej mazliet pa labi.»",
         "opcijas": ["Nē - cik ir «mazliet»?", "Jā"], "jaukt": False,
         "pareizi": 0, "padoms": "Vajag skaitli."},
        {"jaut": "«Ej 3 rūtiņas pa labi.»", "opcijas": ["Jā", "Nē"],
         "jaukt": False, "pareizi": 0, "padoms": "Skaidrs."},
        {"jaut": "«Pieskaiti kaut ko.»",
         "opcijas": ["Nē - ko pieskaitīt?", "Jā"], "jaukt": False,
         "pareizi": 0, "padoms": "Vajag skaitli."},
        {"jaut": "«Pieskaiti 12.»", "opcijas": ["Jā", "Nē"],
         "jaukt": False, "pareizi": 0, "padoms": "Skaidrs."},
    ]),

    Varianti("Kurš algoritms ved pie ābola?", [
        {"jaut": "Sākums apakšā kreisajā stūrī, ābols augšā labajā. Kurš "
                 "ceļš der?",
         "zim": celjs(5, 4, (0, 3), (4, 0)),
         "opcijas": ["4 pa labi, 3 uz augšu", "3 pa labi, 4 uz augšu",
                     "4 uz augšu, 4 pa labi"], "pareizi": 0,
         "padoms": "Saskaiti rūtiņas."},
        {"jaut": "Kurš vēl der?", "zim": celjs(5, 4, (0, 3), (4, 0)),
         "opcijas": ["3 uz augšu, 4 pa labi", "4 uz augšu, 3 pa labi",
                     "7 pa labi"], "pareizi": 0,
         "padoms": "Secību var mainīt, soļu skaitu - ne."},
    ]),

    Petijums("Mans algoritms", [
        "Izvēlies: ceļš rūtiņās vai skaitļu mašīna.",
        "Uzraksti 3-5 soļus shēmā ar kastītēm.",
        "Iedod klasesbiedram izpildīt burtiski.",
        "Ja kaut kas nesanāca - uzlabo soli.",
    ], vajag="rūtiņu lapa, zīmulis"),

    Pasaule("Skaitļu mašīna",
            Varianti("", [
                {"jaut": "Mašīna katru skaitli padara par 10 lielāku, tad "
                         "atņem 3. Kura shēma der?",
                 "zim": algoritms(["Paņem skaitli", "Pieskaiti 10",
                                   "Atņem 3"]),
                 "opcijas": ["šī shēma der", "vajag «Atņem 10»"],
                 "jaukt": False, "pareizi": 0,
                 "padoms": "+ 10, tad − 3."},
            ]),
            pavediens="tehnika",
            konteksts="Programmētāji raksta algoritmus datoriem.",
            kapec="Dators izpilda tieši to, kas uzrakstīts."),

    Kopsavilkums([
        "Pierakstu algoritmu ar skaidriem soļiem.",
        "Pārbaudu to ar klasesbiedru.",
        "Uzlaboju neskaidrus soļus.",
    ]),

    Majas([
        "Uzraksti algoritmu sviestmaizes pagatavošanai.",
        "Lai mājinieks izpilda burtiski.",
        "Kurš solis bija jāuzlabo?",
    ]),
]
