# -*- coding: utf-8 -*-
"""3. klase, 164. stunda: «Kāds konuss sanāks?»

No vienāda lieluma riņķiem var izveidot pavisam dažādus konusus: jo lielāku
sektoru izgriež, jo šaurāks un augstāks konuss sanāk. Tas ir pētījums ar
skaidru likumsakarību, kuru skolēns atrod pats.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         kermenis, rinkis)

TEMA = "Kāds konuss sanāks?"

MERKIS = ("No vienāda lieluma riņķiem veidosim dažādus konusus un "
          "salīdzināsim tos.")

SATURS = [
    Sakums("Kāpēc no vienādiem riņķiem sanāk dažādi konusi?",
           zimejums=rinkis(sektors=270, virsraksts="riņķis ar izgriezumu",
                           paraksts="palikušo daļu satin konusā"),
           fakti=["Konusu veido, satinot riņķa daļu.",
                  "Jo mazāka daļa palikusi, jo šaurāks konuss sanāk."]),

    Doma("Jo mazāka riņķa daļa, jo šaurāks konuss",
         "No vesela riņķa konusu nesatīsi; jo lielāku sektoru izgriež, jo "
         "šaurāks un augstāks konuss sanāk.",
         soli=[
             "Izgriez riņķi un atzīmē tā centru.",
             "Izgriez no tā sektoru - ceturtdaļu vai pusi.",
             "Satin palikušo daļu tā, lai malas saskartos.",
             "Salīdzini iegūtos konusus.",
         ],
         pieze="Riņķa rādiuss kļūst par konusa slīpo malu, tāpēc no vienāda "
               "riņķa visiem konusiem šī mala ir vienāda."),

    Petijums("Uztaisi trīs konusus",
             vajag="trīs vienādi papīra riņķi, šķēres un līmlente",
             soli=[
                 "No pirmā riņķa izgriez ceturtdaļu.",
                 "No otrā - pusi.",
                 "No trešā - trīs ceturtdaļas.",
                 "Satin visus trīs un salīdzini to augstumu un platumu.",
             ],
             secinajums="Jo vairāk izgriezts, jo šaurāks un augstāks konuss - "
                        "kaut visiem slīpā mala ir vienāda."),

    Paraugs("Cik liela riņķa daļa paliek?",
            uzd="No riņķa izgriež ceturtdaļu. Kāda daļa paliek konusam?",
            soli=[
                ("Viss riņķis ir {4|4}",
                 "Četras ceturtdaļas."),
                ("Izgriež {1|4}",
                 "Vienu ceturtdaļu."),
                ("{4|4} − {1|4} = {3|4}",
                 "Konusam paliek trīs ceturtdaļas."),
            ],
            atbilde="{3|4} riņķa"),

    Ievadi("Riņķa daļas konusam", [
        {"jaut": "No riņķa izgriež {1|4}. Cik ceturtdaļu paliek?",
         "atb": ["3"], "padoms": "4 − 1."},
        {"jaut": "No riņķa izgriež {1|2}. Cik ceturtdaļu paliek?",
         "atb": ["2"], "padoms": "4 − 2."},
        {"jaut": "No riņķa izgriež {3|4}. Cik ceturtdaļu paliek?",
         "atb": ["1"], "padoms": "4 − 3."},
        {"jaut": "Cik grādu ir visā riņķī?", "atb": ["360"],
         "padoms": "Pilns apgrieziens."},
        {"jaut": "Cik grādu ir riņķa ceturtdaļā?", "atb": ["90"],
         "padoms": "360 : 4."},
        {"jaut": "Cik grādu paliek, izgriežot ceturtdaļu?", "atb": ["270"],
         "padoms": "360 − 90."},
    ], pamats=4),

    Zimejums("Gatavs konuss",
             kermenis("konuss", virsraksts="konuss"),
             paskaidro="Konusam ir viena plakana skaldne - pamats - un viena "
                       "virsotne.",
             ievads="Tā izskatās satīts riņķa gabals."),

    Varianti("Kāds konuss sanāks?", [
        {"jaut": "Kas notiek, ja izgriež lielāku sektoru?",
         "opcijas": ["Konuss kļūst šaurāks", "Konuss kļūst platāks",
                     "Nekas nemainās", "Konuss kļūst zemāks"],
         "pareizi": 0, "padoms": "Paliek mazāka riņķa daļa."},
        {"jaut": "Vai no vesela riņķa var satīt konusu?",
         "opcijas": ["Nē", "Jā", "Tikai no liela", "Tikai no maza"],
         "pareizi": 0, "padoms": "Malām jāsaskaras, bet tās jau ir kopā."},
        {"jaut": "Par ko kļūst riņķa rādiuss?",
         "opcijas": ["Par konusa slīpo malu", "Par augstumu",
                     "Par pamata rādiusu", "Par neko"],
         "pareizi": 0, "padoms": "Tā ir mala no virsotnes līdz pamatam."},
        {"jaut": "Cik grādu paliek, izgriežot pusi riņķa?",
         "opcijas": ["180", "90", "270", "360"],
         "pareizi": 0, "padoms": "360 : 2."},
    ], pamats=4),

    Pasaule("Cik papīra vajag cepurītei?",
            Ievadi("", [
                {"jaut": "No riņķa izgriež {1|4}. Cik grādu paliek "
                         "cepurītei?",
                 "atb": ["270"], "padoms": "360 − 90."},
                {"jaut": "Cik cepurīšu var izgriezt no 4 riņķiem?",
                 "atb": ["4"], "padoms": "Katram riņķim viena."},
                {"jaut": "Cik cepurīšu vajag 24 bērniem?", "atb": ["24"],
                 "padoms": "Katram viena."},
                {"jaut": "Cik riņķu vajag, ja no vienas lapas sanāk 2 riņķi?",
                 "atb": ["12"], "padoms": "24 : 2."},
            ]),
            pavediens="veikals",
            konteksts="Svētku cepurītes ražo tieši tā: no riņķa izgriež "
                      "sektoru un satin pārējo konusā.",
            kapec="Jo vairāk izgriež, jo smailāka cepurīte sanāk."),

    Kopsavilkums([
        "Veidoju konusu no riņķa daļas.",
        "Zinu, ka lielāks izgriezums dod šaurāku konusu.",
        "Aprēķinu, kāda riņķa daļa paliek.",
        "Salīdzinu vairākus konusus savā starpā.",
    ]),

    Majas([
        "Izgriez divus vienādus riņķus un uztaisi no tiem divus dažādus "
        "konusus.",
        "Salīdzini to augstumu.",
        "Pasaki, kurš izgriezums bija lielāks.",
    ]),
]
