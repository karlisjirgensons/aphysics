# -*- coding: utf-8 -*-
"""9. klase, 18. stunda: «Kā to risinātu eksāmenā?»

Temata noslēgums eksāmena formātā (Math/mat_ex.pdf): 1. daļas īsie
uzdevumi ar atbilžu izvēli un «Atbilde:», izvērstais uzdevums ar laukumu
attiecību un pierādījums, kurā jāaizpilda iemesli - tieši tā, kā tas ir
eksāmena darba lapā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, geometrija, restis)

TEMA = "Kā to risinātu eksāmenā?"

MERKIS = ("Risināsim eksāmena formāta uzdevumus par līdzību un noformēsim "
          "risinājumu.")

# 2025. gada eksāmena 20. uzdevuma zīmējums: KL ∥ PS, △KRL ∼ △PRS.
_ZIM = geometrija([("R", 3, 8), ("K", 2.25, 6), ("L", 4.5, 6), ("P", 0, 0),
                   ("S", 9, 0)],
                  nogriezni=["RP", "RS", "PS"], izcelti=["KL"],
                  malas=[("KL", "2 cm"), ("PS", "8 cm")])

SATURS = [
    Sakums("Eksāmena uzdevums par 2 punktiem",
           zimejums=_ZIM,
           paraksts="△PRS ∼ △KRL, S_{KRL} = 3 cm². Atrodi S_{PRS}.",
           fakti=["Par pareizu atbildi bez risinājuma - 1 punkts no 2.",
                  "Otro punktu dod pamatojums: k un k^2.",
                  "Formulu lapā līdzības nav - to jāzina pašam."]),

    Doma("Kā noformē",
         "Risinājumā redzama doma: kas līdzīgs kam, kāds ir k, kāda formula, "
         "atbilde ar mērvienību.",
         soli=[
             "Pieraksti līdzību un pazīmi (ja nav dota).",
             "Aprēķini k no zināmajām atbilstošajām malām.",
             "Garumiem reizini ar k, laukumiem - ar k^2.",
             "Atbilde: skaitlis ar mērvienību.",
         ]),

    Paraugs("Eksāmena risinājums",
            uzd="△PRS ∼ △KRL, KL = 2 cm, PS = 8 cm, S_{KRL} = 3 cm². "
                "Aprēķini S_{PRS}.",
            soli=[
                ("k = {PS|KL} = {8|2} = 4", "Līdzības koeficients."),
                ("S_{PRS} : S_{KRL} = k^2 = 16", "Laukumu attiecība."),
                ("S_{PRS} = 16 · 3 = 48 (cm²)", "Aprēķins."),
            ],
            atbilde="48 cm²"),

    Varianti("1. daļas stilā", [
        {"jaut": "Trijstūri ar malām 3, 5, 7 un 6, 10, x ir līdzīgi. x = ?",
         "opcijas": ["14", "10", "12", "21"],
         "pareizi": 0, "padoms": "k = 2."},
        {"jaut": "Līdzīgu trijstūru perimetri 12 cm un 18 cm. Laukumu "
                 "attiecība ir",
         "opcijas": ["4 : 9", "2 : 3", "12 : 18", "16 : 81"],
         "pareizi": 0, "padoms": "k = {2|3}, k^2 = {4|9}."},
        {"jaut": "Trijstūra viduslīnija 6 cm. Paralēlā mala ir",
         "opcijas": ["12 cm", "3 cm", "6 cm", "18 cm"],
         "pareizi": 0, "padoms": "Divreiz."},
        {"jaut": "Kura NAV līdzības pazīme?",
         "opcijas": ["Divas malas un leņķis pretī vienai no tām",
                     "Divi leņķi", "Trīs malas proporcionālas",
                     "Divas malas un leņķis starp tām"],
         "pareizi": 0, "padoms": "Leņķim jābūt starp malām."},
    ]),

    Ievadi("Atbilde:", [
        {"jaut": "△ABC ∼ △MNK, AB = 5, MN = 15, BC = 7. NK = ?",
         "atb": ["21"], "padoms": "k = 3."},
        {"jaut": "Karte 1 : 20 000. 7 cm kartē = ? km dabā", "atb": ["1,4"],
         "padoms": "140 000 cm."},
        {"jaut": "Taisnleņķa △ABC, CH - augstums, AH = 4, HB = 16. CH = ?",
         "atb": ["8"], "padoms": "√64."},
        {"jaut": "Mietiņš 1,5 m met 2 m ēnu, koks - 12 m. Koks (m)?",
         "atb": ["9"], "padoms": "{h|12} = {1,5|2}."},
    ]),

    Varianti("Aizpildi pierādījumu", [
        {"jaut": "AB ∥ CD, AD ∩ BC = O. 1) ∠AOB = ∠DOC, jo...",
         "opcijas": ["krustleņķi", "kāpšļu leņķi", "blakusleņķi",
                     "dots"],
         "pareizi": 0, "padoms": "Divas krustojošas taisnes."},
        {"jaut": "2) ∠OAB = ∠ODC, jo...",
         "opcijas": ["iekšējie šķērsleņķi pie AB ∥ CD", "krustleņķi",
                     "vienādsānu trijstūris", "blakusleņķi"],
         "pareizi": 0, "padoms": "Krustotāja AD."},
        {"jaut": "Tātad △AOB ∼ △DOC pēc pazīmes...",
         "opcijas": ["divi leņķi", "trīs malas", "divas malas un leņķis",
                     "viena mala"],
         "pareizi": 0, "padoms": "Divi vienādi leņķi."},
    ]),

    Pasaule("Zemes gabala plāns",
            Ievadi("", [
                {"jaut": "Plānā mērogā 1 : 500 trijstūra gabala laukums ir "
                         "40 cm². Cik m² tas ir dabā?", "atb": ["1000"],
                 "padoms": "1 cm² → 25 m²."},
                {"jaut": "Gabala mala plānā 12 cm. Cik m dabā?", "atb": ["60"],
                 "padoms": "12 · 5 m."},
            ]),
            pavediens="maja",
            konteksts="Zemesgrāmatas plāns ir līdzīga figūra: garumi mērogā "
                      "k, laukums - k^2.",
            kapec="Tā pati laukumu kļūda, ko pieļauj eksāmenā.",
            zimejums=restis([["plānā", "dabā"], ["1 cm", "5 m"],
                             ["1 cm²", "25 m²"]])),

    Kopsavilkums([
        "Noformēju līdzības uzdevumu ar k un k².",
        "Aizpildu pierādījuma iemeslus.",
        "Zinu, par ko eksāmenā dod punktus.",
    ]),

    Majas([
        "Atkārto 9.1. tematu: viduslīnija, pazīmes, k un k².",
        "Atrisini: līdzīgu trijstūru laukumi 12 cm² un 27 cm², mazākā "
        "perimetrs 10 cm. Atrodi lielākā perimetru.",
        "Uzraksti sev atgādni ar trīs pazīmēm un zīmējumiem.",
    ]),
]
