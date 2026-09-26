# -*- coding: utf-8 -*-
"""8. klase, 67. stunda: «Kā atrast nezināmo augstumu?»

Formula S = {a · h|2} ir vienādojums: ja zināmi divi lielumi, trešo atrod.
h = {2S|a} un a = {2S|h}. Ja laukums nemainās, garāka mala nozīmē
īsāku augstumu - apgriezta proporcionalitāte, kas atgriezīsies 8.7.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, geometrija)

TEMA = "Kā atrast nezināmo augstumu?"

MERKIS = "Aprēķināsim trijstūra malu vai augstumu, ja zināms laukums."

SATURS = [
    Sakums("Laukums zināms - cik augsts ir trijstūris?",
           zimejums=geometrija([("A", 0, 0), ("B", 8, 0), ("C", 5, 6),
                                ("H", 5, 0, 270)],
                               nogriezni=["AB", "BC", "CA", "CH"],
                               taisni=["CHB"], iekrasot=[("ABC", 0)],
                               malas=[("AB", "8 cm")],
                               uzraksti=[(5.9, 3, "h")]),
           paraksts="S = 24 cm², tātad h = 2 · 24 : 8 = 6 cm.",
           fakti=["No S = {a · h|2} izriet h = {2S|a}.",
                  "Tāpat atrod malu: a = {2S|h}.",
                  "Pārbaude: ievieto atpakaļ formulā."]),

    Doma("Formula kā vienādojums",
         "Ja zināmi divi no trim lielumiem S, a, h, trešo atrod no formulas.",
         soli=[
             "Pieraksti formulu S = {a · h|2}.",
             "Ievieto zināmos lielumus.",
             "Reizini abas puses ar 2 un dali ar zināmo lielumu.",
             "Pārbaudi ar laukumu.",
         ]),

    Paraugs("Atrodi malu",
            uzd="Trijstūra laukums ir 45 cm², augstums - 9 cm. Atrodi malu, "
                "pret kuru novilkts augstums.",
            soli=[
                ("45 = {a · 9|2}", "Ievieto."),
                ("90 = 9a", "Reizina ar 2."),
                ("a = 10 cm", "Dala ar 9."),
                ("{10 · 9|2} = 45", "Pārbaude."),
            ],
            atbilde="10 cm"),

    Ievadi("Atrodi nezināmo", [
        {"jaut": "S = 30 cm², a = 12 cm. h (cm)?", "atb": ["5"],
         "padoms": "{60|12}."},
        {"jaut": "S = 18 cm², h = 4 cm. a (cm)?", "atb": ["9"],
         "padoms": "{36|4}."},
        {"jaut": "S = 7,5 m², a = 5 m. h (m)?", "atb": ["3"],
         "padoms": "{15|5}."},
        {"jaut": "S = 1 m², h = 0,5 m. a (m)?", "atb": ["4"],
         "padoms": "{2|0,5}."},
        {"jaut": "Taisnleņķa trijstūrim S = 35 cm², viena katete 7 cm. Otra "
                 "katete (cm)?", "atb": ["10"], "padoms": "{70|7}."},
    ]),

    Varianti("Spried", [
        {"jaut": "Laukums nemainās, bet mala kļūst 2 reizes garāka. "
                 "Augstums...",
         "opcijas": ["kļūst 2 reizes īsāks", "kļūst 2 reizes garāks",
                     "nemainās", "kļūst 4 reizes īsāks"],
         "pareizi": 0, "padoms": "a · h = 2S nemainās."},
        {"jaut": "Kā izteikt h no S = {a · h|2}?",
         "opcijas": ["h = {2S|a}", "h = {S|2a}", "h = 2Sa", "h = {a|2S}"],
         "pareizi": 0, "padoms": "Reizina ar 2, dala ar a."},
        {"jaut": "S = 20, a = 5. h = ?",
         "opcijas": ["8", "4", "2", "50"],
         "pareizi": 0, "padoms": "{40|5}."},
    ]),

    Pasaule("Līdzjutēju vimpelis",
            Ievadi("", [
                {"jaut": "Trijstūrveida vimpeļa laukums ir 600 cm², mala pie "
                         "kāta - 30 cm. Cik cm garš ir vimpelis (augstums)?",
                 "atb": ["40"], "padoms": "{1200|30}."},
                {"jaut": "Malu pie kāta samazina līdz 20 cm, laukums tas "
                         "pats. Garums (cm)?",
                 "atb": ["60"], "padoms": "{1200|20}."},
                {"jaut": "Vimpeli izgriež no taisnstūra 30 cm × "
                         "40 cm. Cik cm² paliek pāri?",
                 "atb": ["600"], "padoms": "1200 − 600."},
            ]),
            pavediens="sports",
            konteksts="Vimpeļa izmērus izvēlas pēc laukuma - tik daudz vietas "
                      "vajag komandas zīmei.",
            kapec="No laukuma un malas augstumu atrod ar h = {2S|a}."),

    Kopsavilkums([
        "Izsaku augstumu un malu no laukuma formulas.",
        "Aprēķinu nezināmo lielumu un pārbaudu to.",
        "Spriežu, kā mainās augstums, ja laukums nemainās.",
    ]),

    Majas([
        "Uzzīmē trijstūri ar laukumu 15 cm² un malu 6 cm.",
        "Cik garš jābūt augstumam, lai trijstūra ar malu 4 m laukums būtu "
        "10 m²?",
        "Izdomā uzdevumu, kurā jāatrod mala no laukuma.",
    ]),
]
