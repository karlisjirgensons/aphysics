# -*- coding: utf-8 -*-
"""2. klase, 7. stunda: «Pēc kā var sagrupēt figūras?»

Figūras grupē pēc dotas pazīmes (plakana vai telpiska, ir stūri vai nav,
stūru skaits) un pēc pašu izvēlētas. Viena un tā pati figūru kopa dod
dažādas grupas atkarībā no pazīmes - tieši to stunda liek ieraudzīt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, bildes, kermenis)

TEMA = "Pēc kā var sagrupēt figūras?"

MERKIS = ("Šodien grupēsim plaknes un telpiskas figūras pēc dotas un pašu "
          "izvēlētas pazīmes.")

_RINDA = ["trijsturis", "aplis", "kvadrats", "trijsturis*", "aplis*",
          "kvadrats*"]

SATURS = [
    Sakums("Kā vienas un tās pašas figūras sagrupēt trīs veidos?",
           zimejums=bildes([_RINDA]),
           paraksts="Pēc formas, pēc krāsas vai pēc stūriem.",
           fakti=["Grupējums ir atkarīgs no izvēlētās pazīmes.",
                  "Plakanu figūru var uzzīmēt uz lapas, telpisku - paņemt "
                  "rokā."]),

    Doma("Figūru pazīmes",
         "Figūras var grupēt pēc formas, krāsas, stūru skaita un tā, vai "
         "tās ir plakanas vai telpiskas.",
         soli=[
             "Izvēlies vienu pazīmi.",
             "Katrai figūrai pārbaudi šo pazīmi.",
             "Liec kopā tās, kam pazīme vienāda.",
             "Nosauc katru grupu.",
         ]),

    Slidnis("Viena kopa - trīs grupējumi", [
        {"v": "pēc formas", "teksts": "3 grupas: trijstūri, apļi, kvadrāti.",
         "zim": bildes([["trijsturis", "trijsturis*"],
                        ["aplis", "aplis*"], ["kvadrats", "kvadrats*"]])},
        {"v": "pēc krāsas", "teksts": "2 grupas: violetās un dzeltenās.",
         "zim": bildes([["trijsturis", "aplis", "kvadrats"],
                        ["trijsturis*", "aplis*", "kvadrats*"]])},
        {"v": "pēc stūriem", "teksts": "2 grupas: ar stūriem un bez.",
         "zim": bildes([["trijsturis", "kvadrats", "trijsturis*",
                         "kvadrats*"], ["aplis", "aplis*"]])},
    ]),

    Varianti("Plakana vai telpiska?", [
        {"jaut": "Kas tā ir par figūru?", "zim": kermenis("kubs"),
         "opcijas": ["telpiska", "plakana"], "jaukt": False, "pareizi": 0,
         "padoms": "Kubu var paņemt rokā."},
        {"jaut": "Kas tā ir par figūru?", "zim": bildes([["kvadrats"]]),
         "opcijas": ["telpiska", "plakana"], "jaukt": False, "pareizi": 1,
         "padoms": "Kvadrātu uzzīmē uz lapas."},
        {"jaut": "Kas tā ir par figūru?", "zim": kermenis("lode"),
         "opcijas": ["telpiska", "plakana"], "jaukt": False, "pareizi": 0,
         "padoms": "Lode ir kā bumba."},
        {"jaut": "Kas tā ir par figūru?", "zim": kermenis("cilindrs"),
         "opcijas": ["telpiska", "plakana"], "jaukt": False, "pareizi": 0,
         "padoms": "Cilindrs ir kā konservu bundža."},
    ]),

    Ievadi("Cik ir grupā?", [
        {"jaut": "Cik figūrām ir stūri?", "zim": bildes([_RINDA]),
         "atb": ["4"], "padoms": "Apļiem stūru nav."},
        {"jaut": "Cik grupas sanāk, grupējot pēc formas?",
         "zim": bildes([_RINDA]), "atb": ["3"],
         "padoms": "Trijstūri, apļi, kvadrāti."},
        {"jaut": "Cik stūru kopā ir trijstūrim un kvadrātam?",
         "atb": ["7"], "padoms": "3 + 4."},
        {"jaut": "Cik stūru kopā ir diviem kvadrātiem?", "atb": ["8"],
         "padoms": "4 + 4."},
    ]),

    Pasaule("Kā sakārtot rotaļlietu kasti?",
            Varianti("", [
                {"jaut": "Kastē: kubs, bumba, ripa, klucis, kauliņš. Kura "
                         "grupa ripo?",
                 "opcijas": ["bumba, ripa", "kubs, kauliņš",
                             "klucis, kubs"], "pareizi": 0,
                 "padoms": "Ripo apaļās."},
                {"jaut": "Kurus var sakraut tornī vienu uz otra?",
                 "opcijas": ["kubs, klucis, kauliņš", "bumba, ripa",
                             "tikai bumba"], "pareizi": 0,
                 "padoms": "Tiem ir plakanas skaldnes."},
            ]),
            pavediens="maja",
            konteksts="Rotaļlietas ātrāk atrast, ja tās sakārto pa "
                      "grupām.",
            kapec="Pazīme «ripo / neripo» pasaka, kuras var sakraut."),

    Kopsavilkums([
        "Grupēju figūras pēc formas, krāsas un stūriem.",
        "Atšķiru plakanas figūras no telpiskām.",
        "Zinu, ka viena kopa var dot dažādus grupējumus.",
    ]),

    Majas([
        "Atrodi mājās 3 telpiskas figūras, kas ripo, un 3, kas neripo.",
        "Uzzīmē 6 figūras un sagrupē tās divos veidos.",
        "Pastāsti, pēc kādām pazīmēm grupēji.",
    ]),
]
