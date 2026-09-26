# -*- coding: utf-8 -*-
"""9. klase, 13. stunda: «Kā aprēķināt nezināmo malu?»

Viens algoritms visiem līdzības uzdevumiem: pamato līdzību, pieraksti
atbilstošās malas, sastādi proporciju, aprēķini. Uzdevumos nezināmais ir
gan mazajā, gan lielajā trijstūrī, un gan malā, gan tās daļā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, geometrija)

TEMA = "Kā aprēķināt nezināmo malu?"

MERKIS = ("Aprēķināsim nezināmus nogriežņus, lietojot līdzīgu trijstūru "
          "malu proporcionalitāti.")

# DE ∥ AC; BD = 4, DA = 2 (AB = 6), DE = 5, AC = ?
_ZIM = geometrija([("A", 0, 0), ("B", 9, 0), ("C", 3, 6), ("D", 3, 0),
                   ("E", 5, 4)],
                  nogriezni=["AB", "BC", "CA"], izcelti=["DE"],
                  malas=[("DB", "4"), ("AD", "2"), ("DE", "5"),
                         ("AC", "x")])

SATURS = [
    Sakums("Trūkst viena garuma",
           zimejums=_ZIM,
           paraksts="DE ∥ AC. Cik garš ir AC?",
           fakti=["Mazais △DBE ir līdzīgs lielajam △ABC.",
                  "Uzmanies: BA = 4 + 2 = 6, nevis 2.",
                  "Proporcijā liek veselas malas, nevis gabalus."]),

    Doma("Četri soļi",
         "Pamato līdzību → pieraksti atbilstošās malas → proporcija → "
         "aprēķins.",
         soli=[
             "Pieraksti △DBE ∼ △ABC un pazīmi.",
             "Salīdzini malas pēc virsotņu secības: {DB|AB} = {BE|BC} = "
             "{DE|AC}.",
             "Izvēlies attiecību, kurā ir divi zināmi un nezināmais.",
             "Aprēķini un pārbaudi: lielajā trijstūrī mala lielāka.",
         ]),

    Paraugs("Sakuma zīmējums",
            uzd="DE ∥ AC, BD = 4, DA = 2, DE = 5. Atrodi AC.",
            soli=[
                ("△DBE ∼ △ABC", "∠B kopīgs, ∠BDE = ∠BAC (kāpšļu leņķi)."),
                ("BA = 4 + 2 = 6", "Visa mala."),
                ("{DE|AC} = {BD|BA} ⇒ {5|AC} = {4|6}", "Proporcija."),
                ("AC = {5 · 6|4} = 7,5", "Aprēķins; 7,5 > 5 - ticami."),
            ],
            atbilde="AC = 7,5"),

    Ievadi("Aprēķini (DE ∥ AC)", [
        {"jaut": "BD = 3, DA = 6, DE = 2. AC = ?", "atb": ["6"],
         "padoms": "BA = 9; k = 3."},
        {"jaut": "BE = 5, EC = 3, AC = 16. DE = ?", "atb": ["10"],
         "padoms": "BC = 8; {DE|16} = {5|8}."},
        {"jaut": "DE = 4, AC = 10, BD = 6. DA = ?", "atb": ["9"],
         "padoms": "BA = 15, DA = 15 − 6."},
        {"jaut": "BD : DA = 2 : 3, AC = 20. DE = ?", "atb": ["8"],
         "padoms": "BD : BA = 2 : 5."},
        {"jaut": "BD = 2,4, BA = 6, BC = 7. BE = ?", "atb": ["2,8"],
         "padoms": "k = 0,4."},
        {"jaut": "DE = 3, AC = 7,5, EC = 6. BE = ?", "atb": ["4"],
         "padoms": "{BE|BE + 6} = {3|7,5}."},
    ], pamats=4),

    Varianti("Kur kļūda?", [
        {"jaut": "BD = 4, DA = 2, DE = 5. Skolēns raksta {5|AC} = {4|2}. "
                 "Kļūda?",
         "opcijas": ["Jāņem BA = 6, nevis DA", "Nav kļūdas",
                     "Jāraksta {AC|5}", "Jāņem BC"],
         "pareizi": 0, "padoms": "Proporcijā - visas malas."},
        {"jaut": "Lielā trijstūra mala iznāca mazāka par atbilstošo mazā "
                 "trijstūra malu. Ko tas nozīmē?",
         "opcijas": ["Proporcija sastādīta otrādi", "Viss kārtībā",
                     "Trijstūri nav līdzīgi", "Jānoapaļo"],
         "pareizi": 0, "padoms": "Pārbaudi atbilstību."},
    ]),

    Pasaule("Kāpņu margas",
            Ievadi("", [
                {"jaut": "Kāpnes paceļas 3 m uz 4 m horizontāli. Pēc 1 m "
                         "horizontāli cik m augstu ir pakāpiens?",
                 "atb": ["0,75"], "padoms": "{h|1} = {3|4}."},
                {"jaut": "Cik m augstu ir pēc 2,4 m horizontāli?",
                 "atb": ["1,8"], "padoms": "2,4 · 0,75."},
                {"jaut": "Margu balsts vajadzīgs ik pēc 0,8 m horizontāli. "
                         "Cik balstu uz 4 m (ieskaitot abus galus)?",
                 "atb": ["6"], "padoms": "4 : 0,8 = 5 posmi."},
            ]),
            pavediens="maja",
            konteksts="Kāpnes ar margām veido taisnleņķa trijstūri; katrs "
                      "vertikālais balsts nogriež mazāku līdzīgu trijstūri.",
            kapec="Katra balsta augstumu dod viena proporcija."),

    Kopsavilkums([
        "Sastādu proporciju no līdzīgu trijstūru malām.",
        "Proporcijā lieku visas malas, nevis to daļas.",
        "Pārbaudu, vai rezultāts ir ticams.",
    ]),

    Majas([
        "DE ∥ AC, BD = 5, DA = 3, DE = 4. Atrodi AC.",
        "Tauriņā AO = 4, OD = 10, AB = 3. Atrodi CD.",
        "Izdomā uzdevumu, kurā slazds ir «visa mala vai daļa».",
    ]),
]
