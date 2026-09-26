# -*- coding: utf-8 -*-
"""1. klase, 172. stunda: «Ko gribu iemācīties 2. klasē?»

Gada pēdējā stunda: skolēns novērtē, kas padodas viegli un kas vēl
jāatkārto, un iepazīstas ar 2. klases tematiem - skaitļi līdz 100 un
tālāk, reizināšana, garums metros, laiks minūtēs.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Pasaule, Petijums,
                         Sakums, Varianti, bildes)

TEMA = "Ko gribu iemācīties 2. klasē?"

MERKIS = ("Šodien pateiksim, kas padodas viegli un kas vēl jāatkārto, un "
          "uzzināsim, kas gaida 2. klasē.")

SATURS = [
    Sakums("Ko tu jau proti? Ko vēl gribi iemācīties?",
           zimejums=bildes([[("zvaigzne", 5)]]),
           paraksts="Novērtē sevi zvaigznītēs.",
           fakti=["Kas man padodas viegli?",
                  "Kas vēl jāatkārto?",
                  "Kas mani gaida 2. klasē?"]),

    Doma("Novērtē sevi",
         "Godīgs novērtējums palīdz zināt, ko vasarā trenēt.",
         soli=[
             "Izvēlies 3 lietas, kas padodas labi.",
             "Izvēlies 1-2 lietas, kas vēl jātrenē.",
             "Izdomā, kā tās trenēsi.",
         ]),

    Varianti("2. klasē gaida...", [
        {"jaut": "Kura darbība būs jauna 2. klasē?",
         "opcijas": ["reizināšana", "saskaitīšana", "skaitīšana"],
         "pareizi": 0, "padoms": "Saskaitīt jau proti."},
        {"jaut": "Līdz kuram skaitlim skaitīsim un rēķināsim?",
         "opcijas": ["līdz 100 un tālāk", "tikai līdz 10",
                     "tikai līdz 20"], "pareizi": 0,
         "padoms": "Arvien lielāki skaitļi."},
    ]),

    Petijums("Mana vēstule sev", [
        "Uzraksti vai uzzīmē: ko es protu labi.",
        "Ko gribu iemācīties 2. klasē.",
        "Kā vasarā trenēšos.",
        "Ieliec vēstuli aploksnē - atvērsi septembrī!",
    ], vajag="papīrs, aploksne, krāsas"),

    Pasaule("Vasaras plāns",
            Varianti("", [
                {"jaut": "Kā vasarā labi trenēt matemātiku?",
                 "opcijas": ["spēlēt kauliņu un veikala spēles",
                             "neko nedarīt", "tikai skatīties TV"],
                 "pareizi": 0, "padoms": "Spēlējot mācās."},
            ]),
            pavediens="speles",
            konteksts="Vasarā skolas nav, bet matemātika ir visur.",
            kapec="Spēles palīdz neaizmirst."),

    Kopsavilkums([
        "Zinu, kas man padodas.",
        "Zinu, ko vēl jātrenē.",
        "Zinu, kas gaida 2. klasē.",
    ]),

    Majas([
        "Vasarā spēlē veikalu, kauliņus un mērīšanu.",
        "Saskaiti pa 10 līdz 100 un atpakaļ.",
        "Priecīgu vasaru!",
    ]),
]
