# -*- coding: utf-8 -*-
"""1. klase, 120. stunda: «Vai atbilde ir ticama?»

Atbildi pārbauda pēc jēgas: vai tā var būt? Ja «palika» vairāk nekā bija,
vai bērnu skaits sanāk 3 un puse - kaut kas nav kārtībā. Pēc tam pārbauda
ar pretējo darbību.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti)

TEMA = "Vai atbilde ir ticama?"

MERKIS = ("Šodien pārbaudīsim atbildi pēc situācijas jēgas un "
          "paskaidrosim, kāpēc tā ir ticama.")

SATURS = [
    Sakums("Bija 12 konfektes, apēda 5, palika 17. Vai ticams?",
           fakti=["Apēdot konfektes nevar kļūt vairāk!",
                  "Pareizi: 12 − 5 = 7.",
                  "Vienmēr pajautā: vai tā var būt?"]),

    Doma("Jēgas pārbaude",
         "Pirms rēķini pārbaudi ar darbību, pārbaudi ar prātu.",
         soli=[
             "Vai jābūt vairāk vai mazāk nekā sākumā?",
             "Vai skaitlis ir ticams (nav par lielu, nav negatīvs)?",
             "Tad pārbaudi ar pretējo darbību.",
         ]),

    Varianti("Ticama vai nē?", [
        {"jaut": "Klasē 18 bērni, 7 aizgāja mājās. Palika 25.",
         "opcijas": ["neticama", "ticama"], "jaukt": False, "pareizi": 0,
         "padoms": "Aizejot jāpaliek mazāk."},
        {"jaut": "Plauktā 9 grāmatas, ielika 6. Tagad 15.",
         "opcijas": ["ticama", "neticama"], "jaukt": False, "pareizi": 0,
         "padoms": "9 + 6 = 15."},
        {"jaut": "Zēns ir 7 gadus vecs, tētis par 25 vecāks - 8 gadi.",
         "opcijas": ["neticama", "ticama"], "jaukt": False, "pareizi": 0,
         "padoms": "Tētis nevar būt 8 gadus vecs."},
        {"jaut": "Tev 20 €, nopirki par 13 €. Palika 7 €.",
         "opcijas": ["ticama", "neticama"], "jaukt": False, "pareizi": 0,
         "padoms": "7 + 13 = 20."},
    ]),

    Varianti("Kāpēc neticama?", [
        {"jaut": "«Apēda 5 no 12, palika 17.» Kas nav kārtībā?",
         "opcijas": ["saskaitīja, nevis atņēma", "viss kārtībā",
                     "jāreizina"], "pareizi": 0,
         "padoms": "12 + 5 = 17."},
    ]),

    Pasaule("Vecmāmiņas gadi",
            Varianti("", [
                {"jaut": "Vecmāmiņai 67 gadi. Kurš no šiem nevar būt viņas "
                         "mazdēla vecums?",
                 "opcijas": ["70 gadi", "7 gadi", "12 gadi"], "pareizi": 0,
                 "padoms": "Mazdēls nevar būt vecāks."},
            ]),
            pavediens="maja",
            konteksts="Ģimenē visi ir dažādos vecumos.",
            kapec="Ticamība - pirmā pārbaude."),

    Kopsavilkums([
        "Pārbaudu atbildi pēc jēgas.",
        "Pamanu neticamu atbildi.",
        "Izskaidroju, kāpēc tā ir vai nav ticama.",
    ]),

    Majas([
        "Izdomā uzdevumu ar neticamu atbildi mājiniekam.",
        "Vai viņš pamanīja?",
        "Pārbaudi savu mājasdarbu pēc jēgas.",
    ]),
]
