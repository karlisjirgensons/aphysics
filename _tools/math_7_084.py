# -*- coding: utf-8 -*-
"""7. klase, 84. stunda: «Kā plānot garāku pierādījumu?»

Garākā pierādījumā vienu trijstūru vienādību lieto, lai iegūtu elementu
otrai. Plānu atrod, spriežot no beigām: kas man vajadzīgs? Kādi trijstūri
to dos? Kas vajadzīgs tiem? Stunda iemāca šo «atpakaļgaitas» plānu.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, Zimejums, geometrija, restis)

TEMA = "Kā plānot garāku pierādījumu?"

MERKIS = ("Plānosim pierādījuma gaitu, lietojot spriešanu no beigām.")

SATURS = [
    Sakums("Labirints no izejas puses",
           fakti=["Labirintu vieglāk atrisināt no izejas.",
                  "Pierādījumu - no tā, kas jāpierāda.",
                  "Jautā: «Kas man vajadzīgs, lai to iegūtu?»"]),

    Doma("Spried no beigām, raksti no sākuma",
         "Plānojot pierādījumu, sāk ar jāpierādāmo un jautā, no kā tas "
         "izrietētu. Tā iegūst ķēdi līdz dotajam. Pierādījumu pieraksta "
         "otrādi - no dotā.",
         soli=[
             "Jāpierāda: X = Y. Kuros trijstūros ir X un Y?",
             "Kas vajadzīgs šo trijstūru vienādībai? Kuri elementi trūkst?",
             "Kā iegūt trūkstošo? Varbūt no citiem vienādiem trijstūriem.",
             "Kad ķēde sasniedz doto - raksti pierādījumu no sākuma.",
         ],
         pieze="Plānu var uzzīmēt kā shēmu ar bultām no dotā līdz "
               "jāpierādāmajam."),

    Zimejums("Pierādījuma plāns",
             restis([["jāpierāda", "∠BAD = ∠BCD"],
                     ["vajag", "△BAD = △BCD"],
                     ["tam vajag", "AB = CB, AD = CD, BD kopīga"],
                     ["tas ir", "dots - pierādīts (mmm)"]]),
             paskaidro="Lasa no augšas uz leju - tā plāno; pieraksta no "
                       "apakšas uz augšu."),

    Paraugs("Plāns no beigām",
            uzd="Uz taisnes secīgi atzīmēti B, C, E, D, punkts A ir ārpus "
                "tās. AB = AD, BC = DE, ∠B = ∠D. Pierādi, ka AC = AE.",
            soli=[
                ("Plāns: AC un AE ir △ABC un △ADE malas", "No beigām."),
                ("Vajag △ABC = △ADE: AB = AD, BC = DE, ∠B = ∠D",
                 "Viss dots - mlm."),
                ("AB = AD, BC = DE, ∠B = ∠D", "(dots)"),
                ("△ABC = △ADE", "(mlm)"),
                ("AC = AE", "(atbilstošās malas)"),
            ],
            atbilde="AC = AE - pierādīts."),

    Zimejums("Zīmējums uzdevumam",
             geometrija([("A", 3, 5), ("B", 0, 0), ("C", 2, 0),
                         ("E", 4, 0), ("D", 6, 0)],
                        nogriezni=["BD", "AB", "AC", "AE", "AD"],
                        svitras=[("AB", 1), ("AD", 1), ("BC", 2),
                                 ("ED", 2)],
                        lenki=[("CBA", ""), ("ADE", "")]),
             paskaidro="△ABC un △ADE - spoguļattēli."),

    Varianti("Plāno", [
        {"jaut": "Jāpierāda, ka ∠1 = ∠2. Pirmais jautājums?",
         "opcijas": ["Kuros trijstūros ir ∠1 un ∠2?",
                     "Cik grādu ir ∠1?", "Vai ∠1 ir ass?",
                     "Kāda ir trijstūra krāsa?"],
         "pareizi": 0, "padoms": "Meklē trijstūrus."},
        {"jaut": "Trijstūru vienādībai trūkst viena leņķa. Ko dara?",
         "opcijas": ["Meklē citus vienādus trijstūrus vai krustleņķus",
                     "Pieņem, ka tas ir vienāds",
                     "Izmēra ar transportieri",
                     "Izmet uzdevumu"],
         "pareizi": 0, "padoms": "Vēl viens solis ķēdē."},
        {"jaut": "Kādā secībā pieraksta pierādījumu?",
         "opcijas": ["No dotā uz jāpierādāmo",
                     "No jāpierādāmā uz doto",
                     "Jebkurā", "Tikai zīmējumu"],
         "pareizi": 0, "padoms": "Plāno otrādi."},
    ]),

    Pasaule("Detektīvs",
            Varianti("", [
                {"jaut": "Detektīvs zina: zaglis atstāja pēdas pie loga. "
                         "Kā viņš domā?",
                 "opcijas": ["No sekām atpakaļ uz cēloni",
                             "Uzmin", "No sākuma uz beigām",
                             "Gaida atzīšanos"],
                 "pareizi": 0, "padoms": "Spriešana no beigām."},
                {"jaut": "Kas pierādījumā atbilst «pierādījumiem tiesā»?",
                 "opcijas": ["Pamatojumi (dots, pazīme, īpašība)",
                             "Zīmējuma krāsa", "Skolotāja viedoklis",
                             "Mērījumi"],
                 "pareizi": 0, "padoms": "Katrs solis pamatots."},
                {"jaut": "Ja vienam solim nav pamatojuma?",
                 "opcijas": ["Pierādījums nav pilnīgs",
                             "Tas nav svarīgi", "Pietiek ar atbildi",
                             "Pieliek «acīmredzami»"],
                 "pareizi": 0, "padoms": "Ķēde pārtrūkst."},
            ]),
            pavediens="skola",
            konteksts="Detektīvi, ārsti un inženieri spriež no sekām uz "
                      "cēloņiem - tāpat kā pierādījumā.",
            kapec="Spriešana no beigām ir universāla metode."),

    Kopsavilkums([
        "Plānoju pierādījumu no jāpierādāmā.",
        "Atrodu, kuri trijstūri un elementi vajadzīgi.",
        "Pierakstu pierādījumu no dotā.",
        "Katram solim dodu pamatojumu.",
    ]),

    Majas([
        "Uzzīmē plāna shēmu kādam iepriekšējās stundas pierādījumam.",
        "Pierādi: rombā diagonāle dala leņķi uz pusēm.",
        "Izdomā situāciju no dzīves, kur spried no beigām.",
    ]),
]
