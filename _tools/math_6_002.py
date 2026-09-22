# -*- coding: utf-8 -*-
"""6. klase, 2. stunda: «Kā attiecību uzzīmēt?»

Attiecību no teksta pārceļ uz zīmējumu. Divi stabiņi vai josla, sadalīta
daļās, ir tas pats modelis, kas 5. klasē kalpoja summai un starpībai - un
tieši tas nākamajā mikrotematā ļaus sadalīt kopumu, neko neminot.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, kolonnas,
                         restis)

TEMA = "Kā attiecību uzzīmēt?"

MERKIS = ("Iemācīsimies attēlot divu lielumu attiecību shematiskā zīmējumā "
          "un izvēlēties sev piemērotāko veidu.")

SATURS = [
    Sakums("Divi stabiņi pasaka visu",
           zimejums=kolonnas([("krāsa", 2), ("ūdens", 3)]),
           paraksts="Attiecība 2 pret 3: krāsas stabiņā divas daļas, ūdens "
                    "stabiņā trīs.",
           fakti=["Zīmējumā nav ne litru, ne kilogramu - tikai daļas.",
                  "Visas daļas ir vienādas; tikai tad zīmējums nemelo."]),

    Doma("Viena daļa - viena rūtiņa",
         "Attiecību zīmē kā vienādas daļas: cik skaitlī, tik rūtiņu.",
         soli=[
             "Izvēlies, ko zīmēsi: divus stabiņus vai vienu joslu pa daļām.",
             "Uzzīmē tik vienādu daļu, cik pasaka katrs attiecības skaitlis.",
             "Pieraksti, ko katrs stabiņš nozīmē.",
             "Pārbaudi, vai daļas tiešām ir vienāda lieluma.",
         ],
         pieze="Divi stabiņi ir ērti, ja lielumus salīdzina. Viena josla, "
               "sadalīta daļās, ir ērtāka, ja zināms kopums - tad uzreiz "
               "redz, cik daļu tas satur."),

    Zimejums("Viena josla, sadalīta daļās",
             restis([["k", "k", "ū", "ū", "ū"]],
                    "kopā 5 vienādas daļas"),
             paskaidro="Tā pati attiecība 2 pret 3 vienā joslā: divas daļas "
                       "krāsas (k) un trīs daļas ūdens (ū).",
             ievads="Ja zināms kopums, ērtāk zīmēt vienu joslu."),

    Paraugs("No teksta uz zīmējumu",
            uzd="«Sulu un ūdeni maisa 1 pret 4.» Kā to uzzīmēt?",
            soli=[
                ("Sulai viena rūtiņa",
                 "Pirmais attiecības skaitlis ir 1."),
                ("Ūdenim četras tikpat lielas rūtiņas",
                 "Otrais skaitlis ir 4; rūtiņas nedrīkst būt lielākas."),
                ("Kopā joslā ir 5 rūtiņas",
                 "1 + 4 - tik daļu ir visā dzērienā."),
            ],
            atbilde="josla no 5 vienādām daļām: 1 sula un 4 ūdens"),

    Ievadi("Cik rūtiņu zīmēsi?", [
        {"jaut": "Attiecība 3 pret 5. Cik rūtiņu pirmajam stabiņam?",
         "atb": ["3"], "padoms": "Pirmais skaitlis."},
        {"jaut": "Tā pati attiecība. Cik rūtiņu ir kopā abos stabiņos?",
         "atb": ["8"], "padoms": "3 + 5."},
        {"jaut": "Attiecība 1 pret 4. Cik rūtiņu joslā pavisam?",
         "atb": ["5"], "padoms": "1 + 4."},
        {"jaut": "Attiecība 2 pret 2. Cik rūtiņu katram?",
         "atb": ["2"], "padoms": "Abiem vienādi."},
        {"jaut": "Attiecība 1 pret 2 pret 3. Cik rūtiņu joslā pavisam?",
         "atb": ["6"], "padoms": "1 + 2 + 3."},
        {"jaut": "Joslā ir 10 vienādas daļas, no tām 4 ir sula. Cik daļas "
                 "ir ūdens?",
         "atb": ["6"], "padoms": "10 − 4."},
    ], pamats=4,
        ievads="Skaitlis attiecībā pasaka, cik vienādu daļu uzzīmēt."),

    Varianti("Kurš zīmējums ir pareizs?", [
        {"jaut": "Skolēns attiecībai 2 pret 3 uzzīmēja divas lielas un trīs "
                 "mazas rūtiņas. Kas nav labi?",
         "opcijas": ["Daļām jābūt vienādām",
                     "Rūtiņu ir par maz",
                     "Rūtiņas jāzīmē blakus",
                     "Viss ir pareizi"],
         "pareizi": 0,
         "padoms": "Ar dažāda lieluma daļām zīmējums vairs neko nesalīdzina."},
        {"jaut": "Kad ērtāk zīmēt vienu joslu, nevis divus stabiņus?",
         "opcijas": ["Kad zināms kopums", "Kad skaitļi ir lieli",
                     "Kad lielumu ir divi", "Vienmēr"],
         "pareizi": 0,
         "padoms": "Joslā uzreiz redz, cik daļu ir visā kopumā."},
        {"jaut": "Joslā 7 daļas: 3 zilas un 4 sarkanas. Kāda ir zilo "
                 "attiecība pret sarkanajām?",
         "opcijas": ["3 pret 4", "4 pret 3", "3 pret 7", "7 pret 3"],
         "pareizi": 0,
         "padoms": "Vispirms nosauc to, par ko jautā."},
        {"jaut": "Ko zīmējums NEparāda?",
         "opcijas": ["Cik litru ir katrā daļā", "Cik daļu ir katram",
                     "Kurš lielums ir lielāks", "Cik daļu ir kopā"],
         "pareizi": 0,
         "padoms": "Daļas lielumu izvēlas tikai tad, kad zināms daudzums."},
    ], pamats=4),

    Pasaule("Kā uzzīmēt istabas plānu?",
            Ievadi("", [
                {"jaut": "Grīdas segums: paklājs un koks 1 pret 3. Cik "
                         "vienādu daļu ir visā grīdā?",
                 "atb": ["4"], "padoms": "1 + 3."},
                {"jaut": "Sienu krāso divās krāsās attiecībā 2 pret 5. Cik "
                         "daļu ir kopā?",
                 "atb": ["7"], "padoms": "2 + 5."},
                {"jaut": "Joslā 12 vienādas daļas, 5 no tām ir logi. Cik "
                         "daļu ir siena?",
                 "atb": ["7"], "padoms": "12 − 5."},
                {"jaut": "Dārzu dala dobēs un celiņos 4 pret 1. Cik daļu ir "
                         "kopā?",
                 "atb": ["5"], "padoms": "4 + 1."},
            ]),
            pavediens="maja",
            konteksts="Pirms kaut ko pērk vai krāso, attiecību uzzīmē - "
                      "zīmējumā kļūdu pamana ātrāk nekā rēķinā.",
            kapec="Vienādas daļas zīmējumā ir tas pats, kas vienādas daļas "
                  "dzīvē."),

    Kopsavilkums([
        "Attēloju attiecību ar diviem stabiņiem vai vienu joslu.",
        "Zīmēju tikai vienāda lieluma daļas.",
        "Izvēlos veidu pēc tā, vai kopums ir zināms.",
        "No zīmējuma nolasu, cik daļu ir katram un cik kopā.",
    ]),

    Majas([
        "Uzzīmē attiecību 3 pret 4 abos veidos un izlem, kurš tev patīk "
        "labāk.",
        "Atrodi mājās divus priekšmetus, kuru garumi ir aptuveni 1 pret 2, "
        "un uzzīmē tos.",
        "Uzzīmē attiecību 1 pret 2 pret 3 vienā joslā.",
    ]),
]
