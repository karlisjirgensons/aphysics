# -*- coding: utf-8 -*-
"""7. klase, 85. stunda: «Kad trijstūri pārklājas?»

Visgrūtākie zīmējumi ir tie, kuros trijstūri pārklājas: tiem ir kopīga
daļa, un tos grūti ieraudzīt. Stunda iemāca «izvilkt» trijstūrus atsevišķi -
iekrāsot vai pārzīmēt blakus - un atrast kopīgo leņķi vai malu.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, geometrija)

TEMA = "Kad trijstūri pārklājas?"

MERKIS = ("Pierādīsim vienādību situācijā, kurā trijstūri zīmējumā "
          "pārklājas.")

_P = [("A", 3, 5), ("B", 0, 0), ("C", 6, 0), ("K", 1.2, 2, 180),
      ("L", 4.8, 2, 0)]


def _p(kuri):
    krasas = {"ABL": [("ABL", 0)], "ACK": [("ACK", 1)],
              "abi": [("ABL", 0), ("ACK", 1)], "": []}[kuri]
    return geometrija(_P, nogriezni=["AB", "AC", "BC", "BL", "CK"],
                      svitras=[("AK", 1), ("AL", 1), ("KB", 2), ("LC", 2)],
                      iekrasot=krasas)


SATURS = [
    Sakums("Divi trijstūri vienā zīmējumā",
           zimejums=_p("abi"),
           paraksts="△ABL un △ACK pārklājas - kopīgs ∠A.",
           fakti=["Pārklājošie trijstūri ir grūti ieraugāmi.",
                  "Iekrāso katru savā krāsā.",
                  "Kopīgs leņķis vai mala - bezmaksas vienādība."]),

    Slidnis("Izvelc trijstūrus", [
        {"v": "Viss", "teksts": "Zīmējums, kā dots.", "zim": _p("")},
        {"v": "△ABL", "teksts": "Pirmais trijstūris.", "zim": _p("ABL")},
        {"v": "△ACK", "teksts": "Otrais trijstūris.", "zim": _p("ACK")},
        {"v": "Abi", "teksts": "Kopīgs - ∠A.", "zim": _p("abi")},
    ]),

    Doma("Iekrāso un salīdzini",
         "Ja trijstūri pārklājas, katru iekrāso vai pārzīmē atsevišķi. "
         "Kopīgs leņķis (vai mala) abiem trijstūriem ir vienāds - to var "
         "izmantot pazīmē.",
         soli=[
             "Nosauc abus trijstūrus ar trim burtiem.",
             "Iekrāso vai pārzīmē tos blakus.",
             "Atrodi kopīgo elementu.",
             "Pievieno dotos un pierādi.",
         ],
         pieze="Dažreiz vajadzīgo malu iegūst, saskaitot vai atņemot: "
               "AB = AK + KB, ja K ∈ AB."),

    Paraugs("Pierādi, ka BL = CK",
            uzd="Trijstūrī ABC uz malām AB un AC atzīmēti K un L: AK = AL, "
                "KB = LC. Pierādi, ka BL = CK.",
            soli=[
                ("AB = AK + KB = AL + LC = AC", "(K ∈ AB, L ∈ AC, dots)"),
                ("AL = AK", "(dots)"),
                ("∠A - kopīgs", "(kopīgs leņķis)"),
                ("△ABL = △ACK", "(mlm: AB = AC, ∠A, AL = AK)"),
                ("BL = CK", "(atbilstošās malas)"),
            ],
            atbilde="BL = CK - pierādīts."),

    Varianti("Pārklāšanās", [
        {"jaut": "Kāpēc AB = AC šajā uzdevumā?",
         "opcijas": ["Vienādu nogriežņu summas ir vienādas",
                     "Tā ir dots", "No zīmējuma",
                     "Trijstūris ir vienādmalu"],
         "pareizi": 0, "padoms": "AK + KB = AL + LC."},
        {"jaut": "Kurš elements ir kopīgs △ABL un △ACK?",
         "opcijas": ["∠A", "Mala BC", "Punkts K", "Mala BL"],
         "pareizi": 0, "padoms": "Abi iziet no A."},
        {"jaut": "Kas palīdz ieraudzīt pārklājošos trijstūrus?",
         "opcijas": ["Iekrāsošana dažādās krāsās",
                     "Lielāks zīmējums", "Mērīšana", "Nekas"],
         "pareizi": 0, "padoms": "Kā slīdnī."},
    ]),

    Pasaule("Logo dizains",
            Varianti("", [
                {"jaut": "Dizainers zīmē logo no diviem pārklājošiem "
                         "trijstūriem ar kopīgu virsotni. Kā pārbaudīt, ka "
                         "tie vienādi?",
                 "opcijas": ["Salīdzināt divas malas un kopīgo leņķi (mlm)",
                             "Salīdzināt krāsas",
                             "Salīdzināt tikai laukumu",
                             "Nav iespējams"],
                 "pareizi": 0, "padoms": "Kopīgs leņķis."},
                {"jaut": "Kāpēc logo ar vienādiem trijstūriem izskatās "
                         "līdzsvarots?",
                 "opcijas": ["Simetrija - acs to uztver kā kārtību",
                             "Tas ir lētāk", "Tā ir tradīcija",
                             "Nav nozīmes"],
                 "pareizi": 0, "padoms": "Simetrija."},
            ]),
            pavediens="tehnika",
            konteksts="Daudzu zīmolu logo ir pārklājošas figūras - un "
                      "dizaineri tās konstruē precīzi.",
            kapec="Pārklājumā vienādība nav redzama uzreiz."),

    Kopsavilkums([
        "Atrodu pārklājošos trijstūrus zīmējumā.",
        "Iekrāsoju vai pārzīmēju tos atsevišķi.",
        "Izmantoju kopīgu leņķi vai malu.",
        "Iegūstu malu kā nogriežņu summu.",
    ]),

    Majas([
        "Atrodi zīmējumu ar pārklājošiem trijstūriem (karogs, logo).",
        "Pierādi: vienādsānu trijstūrī mediānas pret sānu malām ir "
        "vienādas.",
        "Iekrāso trijstūrus trīs krāsās un pieraksti vienādības.",
    ]),
]
