# -*- coding: utf-8 -*-
"""2. klase, 65. stunda: «Kā uzzīmēt stabiņu diagrammu?»

Diagrammu zīmē pēc noteikumiem: visi stabiņi vienā platumā, uz vienas
pamatlīnijas, augstums atbilst skaitlim, katram stabiņam nosaukums, un
diagrammai virsraksts. Ja kāds noteikums pārkāpts, diagramma melo.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, kolonnas, restis)

TEMA = "Kā uzzīmēt stabiņu diagrammu?"

MERKIS = ("Šodien veidosim vienkāršu stabiņu diagrammu par saviem datiem un "
          "pastāstīsim, kas jāievēro.")

_DATI = [("rudens", 6), ("ziema", 9), ("pavasaris", 4), ("vasara", 8)]

SATURS = [
    Sakums("Kā vienā attēlā parādīt, kurš gadalaiks klasei patīk visvairāk?",
           zimejums=kolonnas(_DATI),
           paraksts="Mīļākais gadalaiks - 27 bērni.",
           fakti=["Stabiņa augstums - cik bērnu to izvēlējās.",
                  "Visaugstākais stabiņš - ziema.",
                  "Diagramma jāzīmē godīgi."]),

    Doma("Pieci noteikumi",
         "Diagramma ir godīga, ja augstums atbilst skaitlim.",
         soli=[
             "Uzzīmē pamatlīniju un vertikālo asi ar skaitļiem.",
             "Visi stabiņi vienādi plati, ar atstarpēm.",
             "Stabiņa augstums - tieši tik rūtiņu, cik skaitlis.",
             "Zem stabiņa - nosaukums, virs visa - virsraksts.",
         ]),

    Petijums("Uzzīmē rūtiņu lapā", [
        "Pārzīmē tabulu: rudens 6, ziema 9, pavasaris 4, vasara 8.",
        "Kreisajā malā uzraksti skaitļus no 0 līdz 10.",
        "Katram gadalaikam uzzīmē stabiņu 2 rūtiņas platu.",
        "Iekrāso un uzraksti virsrakstu.",
    ], vajag="rūtiņu lapa, zīmulis, krāsainie zīmuļi"),

    Ievadi("Pēc diagrammas", [
        {"jaut": "Cik rūtiņu augsts būs stabiņš «ziema»?",
         "zim": restis([["rudens", 6], ["ziema", 9], ["pavasaris", 4],
                        ["vasara", 8]]), "atb": ["9"],
         "padoms": "Tik, cik bērnu."},
        {"jaut": "Par cik rūtiņām «vasara» augstāka nekā «pavasaris»?",
         "zim": kolonnas(_DATI), "atb": ["4"], "padoms": "8 − 4."},
        {"jaut": "Cik bērnu atbildēja?", "zim": kolonnas(_DATI),
         "atb": ["27"], "padoms": "6 + 9 + 4 + 8."},
        {"jaut": "Cik bērnu neizvēlējās ziemu?", "zim": kolonnas(_DATI),
         "atb": ["18"], "padoms": "27 − 9."},
    ]),

    Varianti("Kas nav kārtībā?", [
        {"jaut": "Vienam stabiņam ir 5 bērni, bet tas uzzīmēts augstāks "
                 "nekā stabiņš ar 7. Kas nepareizi?",
         "opcijas": ["Augstums neatbilst skaitlim", "Nav virsraksta",
                     "Viss kārtībā"], "pareizi": 0,
         "padoms": "5 ir mazāk nekā 7."},
        {"jaut": "Stabiņi bez nosaukumiem. Kas trūkst?",
         "opcijas": ["Nevar zināt, kas ir katrs stabiņš",
                     "Nekas netrūkst", "Krāsas"], "pareizi": 0,
         "padoms": "Kam pieder stabiņš?"},
    ]),

    Pasaule("Ziemas sporta aptauja",
            Ievadi("", [
                {"jaut": "Slēpošana 7, slidošana 12, kalniņi 8. Cik augsts "
                         "būs augstākais stabiņš (rūtiņās)?", "atb": ["12"],
                 "padoms": "Lielākais skaitlis."},
                {"jaut": "Par cik rūtiņām tas augstāks nekā zemākais?",
                 "atb": ["5"], "padoms": "12 − 7."},
            ]),
            pavediens="sports",
            konteksts="Klase izvēlas, ko darīt ziemas sporta dienā.",
            kapec="Diagramma parāda izvēli visiem vienā skatienā."),

    Kopsavilkums([
        "Zīmēju stabiņu diagrammu rūtiņu lapā.",
        "Ievēroju: vienāds platums, pareizs augstums, nosaukumi.",
        "Pamanu, ja diagramma uzzīmēta negodīgi.",
    ]),

    Majas([
        "Pajautā 8 cilvēkiem viņu mīļāko krāsu.",
        "Uzzīmē stabiņu diagrammu rūtiņu lapā.",
        "Parādi to klasei.",
    ]),
]
