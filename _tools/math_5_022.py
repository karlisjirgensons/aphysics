# -*- coding: utf-8 -*-
"""5. klase, 22. stunda: «Kā mainās summa un starpība?»

Mikrotemata un visa 5.1. temata pēdējā stunda pirms pārbaudes darba. Te
nerēķina jaunus uzdevumus, bet formulē vispārinājumus: kas notiek ar summu
un starpību, ja vienu locekli maina. Vispārinājums ir tas, ko pārbaudes
darbā vairs nevar izdarīt ar kalkulatoru.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā mainās summa un starpība?"

MERKIS = ("Mācīsimies formulēt vispārinājumus par summas un starpības "
          "izmaiņām, mainot darbību locekļus.")

SATURS = [
    Sakums("Vai atbilde jārēķina no jauna?",
           fakti=["Zināms, ka 47 + 28 = 75.",
                  "Cik ir 47 + 29? Un cik ir 48 + 29?",
                  "Otrreiz rēķināt nevajag - pietiek redzēt, kas mainījās."]),

    Doma("Summa seko līdzi katram saskaitāmajam",
         "Ja saskaitāmo palielina par dažiem, tieši par tik palielinās arī "
         "summa.",
         soli=[
             "Salīdzini jauno izteiksmi ar veco: kurš loceklis mainījās?",
             "Nosaki, par cik tas mainījās un uz kuru pusi.",
             "Summai izmaiņu pieskaita: abi saskaitāmie to velk uz vienu "
             "pusi.",
             "Starpībā mazināmais velk uz to pašu pusi, mazinātājs - uz "
             "pretējo.",
         ],
         pieze="Tāpēc starpība nemainās, ja abus - gan mazināmo, gan "
               "mazinātāju - palielina par vienu un to pašu skaitli: "
               "75 − 28 un 77 − 30 ir vienādi."),

    Paraugs("Trīs izteiksmes, viens rēķins",
            uzd="Zināms, ka 47 + 28 = 75. Cik ir 47 + 29, 48 + 29 un "
                "47 + 26?",
            soli=[
                ("47 + 29 = 76",
                 "Otrs saskaitāmais par 1 lielāks, tāpēc summa par 1 "
                 "lielāka."),
                ("48 + 29 = 77",
                 "Tagad abi saskaitāmie par 1 lielāki - summa par 2 "
                 "lielāka."),
                ("47 + 26 = 73",
                 "Otrs saskaitāmais par 2 mazāks, tāpēc summa par 2 mazāka."),
            ],
            atbilde="76, 77 un 73 - nevienu no tiem nevajadzēja rēķināt no "
                    "gala"),

    Ievadi("Zināms, ka 47 + 28 = 75 un 80 − 35 = 45", [
        {"jaut": "Cik ir 47 + 30?", "atb": ["77"],
         "padoms": "Saskaitāmais par 2 lielāks."},
        {"jaut": "Cik ir 50 + 28?", "atb": ["78"],
         "padoms": "Saskaitāmais par 3 lielāks."},
        {"jaut": "Cik ir 45 + 28?", "atb": ["73"],
         "padoms": "Saskaitāmais par 2 mazāks."},
        {"jaut": "Cik ir 85 − 35?", "atb": ["50"],
         "padoms": "Mazināmais par 5 lielāks - starpība arī."},
        {"jaut": "Cik ir 80 − 30?", "atb": ["50"],
         "padoms": "Mazinātājs par 5 mazāks - starpība par 5 lielāka."},
        {"jaut": "Cik ir 85 − 40?", "atb": ["45"],
         "padoms": "Abi par 5 lielāki - starpība nemainās."},
        {"jaut": "Cik ir 47 + 28 + 10?", "atb": ["85"],
         "padoms": "Summai pieskaita 10."},
        {"jaut": "Cik ir 78 − 35?", "atb": ["43"],
         "padoms": "Mazināmais par 2 mazāks."},
    ], pamats=4,
        ievads="Nerēķini no gala - paskaties, kas mainījās."),

    Varianti("Formulē vispārinājumu", [
        {"jaut": "Vienu saskaitāmo palielina par 6. Kas notiek ar summu?",
         "opcijas": ["Palielinās par 6", "Nemainās", "Samazinās par 6",
                     "Palielinās par 12"],
         "pareizi": 0,
         "padoms": "Pārbaudi ar 10 + 5 un 16 + 5."},
        {"jaut": "Mazinātāju palielina par 4. Kas notiek ar starpību?",
         "opcijas": ["Samazinās par 4", "Palielinās par 4", "Nemainās",
                     "Samazinās par 8"],
         "pareizi": 0,
         "padoms": "Atņem vairāk - paliek mazāk."},
        {"jaut": "Gan mazināmo, gan mazinātāju palielina par 10. Kas notiek "
                 "ar starpību?",
         "opcijas": ["Nemainās", "Palielinās par 10", "Palielinās par 20",
                     "Samazinās par 10"],
         "pareizi": 0,
         "padoms": "Abi punkti uz skaitļu taisnes pavirzījās vienādi."},
        {"jaut": "Vienu saskaitāmo palielina par 5, otru samazina par 5. Kas "
                 "notiek ar summu?",
         "opcijas": ["Nemainās", "Palielinās par 5", "Samazinās par 5",
                     "Palielinās par 10"],
         "pareizi": 0,
         "padoms": "Viena izmaiņa atsver otru."},
        {"jaut": "Mazināmo samazina par 3. Kas notiek ar starpību?",
         "opcijas": ["Samazinās par 3", "Palielinās par 3", "Nemainās",
                     "Samazinās par 6"],
         "pareizi": 0,
         "padoms": "Mazināmais velk starpību uz to pašu pusi."},
        {"jaut": "Kāpēc 302 − 198 ērtāk rēķināt kā 304 − 200?",
         "opcijas": ["Starpība nemainās, bet skaitļi kļūst apaļi",
                     "Starpība kļūst lielāka",
                     "Tā ir cita darbība",
                     "Tā drīkst tikai ar simtiem"],
         "pareizi": 0,
         "padoms": "Abi palielināti par 2."},
    ], pamats=4),

    Pasaule("Kas mainās skolas skaitļos?",
            Ievadi("", [
                {"jaut": "Klasē bija 24 skolēni, kopā ar paralēlklasi 47. "
                         "Atnāca vēl 2 skolēni. Cik tagad kopā?",
                 "atb": ["49"], "padoms": "Summai pieskaita 2."},
                {"jaut": "Ēdnīcā no 260 porcijām palika 15. Nākamdien "
                         "pagatavoja par 20 vairāk, izsniedza tikpat. Cik "
                         "palika?",
                 "atb": ["35"], "padoms": "Mazināmais par 20 lielāks."},
                {"jaut": "Bibliotēkā no 500 grāmatām izsniegtas 180. "
                         "Nākamnedēļ izsniedza par 30 vairāk. Cik palika "
                         "plauktā?",
                 "atb": ["290"], "padoms": "Palika 320, tagad par 30 "
                                           "mazāk."},
                {"jaut": "Skolā 460 skolēni, 148 sākumskolā. Ja sākumskolā "
                         "atnāks vēl 10, par cik mainīsies pārējo skaits?",
                 "atb": ["0"], "padoms": "Abi skaitļi aug par 10 - starpība "
                                         "nemainās."},
            ]),
            pavediens="skola",
            konteksts="Skolas skaitļi mainās katru dienu, bet reti no gala - "
                      "parasti par dažiem uz vienu vai otru pusi.",
            kapec="Ja zini veco atbildi, jauno var pateikt bez rēķināšanas."),

    Kopsavilkums([
        "Formulēju, kā mainās summa, mainot vienu vai abus saskaitāmos.",
        "Formulēju, kā mainās starpība, mainot mazināmo vai mazinātāju.",
        "Zinu, ka starpība nemainās, ja abus locekļus maina vienādi.",
        "Lietoju šo, lai rēķinātu ērtāk: 302 − 198 kā 304 − 200.",
    ]),

    Majas([
        "Uzraksti vienu summu un piecas tai tuvas summas, kuras var pateikt "
        "bez rēķināšanas.",
        "Pārbaudi ar kalkulatoru, vai tavi vispārinājumi turas.",
        "Atrodi atņemšanu, kuru var padarīt vieglāku, abus locekļus "
        "palielinot.",
    ]),
]
