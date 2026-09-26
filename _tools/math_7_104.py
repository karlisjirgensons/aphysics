# -*- coding: utf-8 -*-
"""7. klase, 104. stunda: «Kas ir trijstūra ārējais leņķis?»

Ārējais leņķis ir blakusleņķis trijstūra iekšējam leņķim. Tas ir vienāds ar
abu pārējo (ar to nesaistīto) iekšējo leņķu summu - to pierāda ar leņķu
summu un blakusleņķiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, geometrija)

TEMA = "Kas ir trijstūra ārējais leņķis?"

MERKIS = ("Definēsim ārējo leņķi un formulēsim tā sakarību ar diviem "
          "iekšējiem leņķiem.")

_AR = geometrija([("A", 0, 0), ("B", 6, 0), ("C", 2, 3.5), ("_D", 9, 0)],
                 nogriezni=["AB", "BC", "CA"], stari=[("B", "_D")],
                 lenki=[("BAC", "∠A"), ("ACB", "∠C"),
                        (("_D", "B", "C"), "ārējais", 2)])

SATURS = [
    Sakums("Pagarini malu - rodas ārējais leņķis",
           zimejums=_AR,
           paraksts="Ārējais leņķis pie B = ∠A + ∠C.",
           fakti=["Ārējais leņķis ir blakusleņķis iekšējam ∠B.",
                  "Tas ir vienāds ar divu citu leņķu summu.",
                  "Ātrs veids aprēķināt, neaprēķinot ∠B."]),

    Doma("Ārējais = pārējo divu iekšējo summa",
         "Trijstūra ārējais leņķis ir leņķis, kas ir blakusleņķis kādam "
         "trijstūra iekšējam leņķim. Ārējais leņķis ir vienāds ar abu "
         "pārējo iekšējo leņķu summu.",
         soli=[
             "Ārējais + ∠B = 180° (blakusleņķi).",
             "∠A + ∠C + ∠B = 180° (leņķu summa).",
             "Salīdzina: ārējais = ∠A + ∠C.",
         ],
         pieze="Tāpēc ārējais leņķis vienmēr ir lielāks par katru no abiem "
               "ar to nesaistītajiem iekšējiem leņķiem."),

    Paraugs("Pierādījums",
            uzd="Pierādi, ka ārējais leņķis pie B ir vienāds ar ∠A + ∠C.",
            soli=[
                ("ārējais + ∠B = 180°", "(blakusleņķi)"),
                ("∠A + ∠B + ∠C = 180°", "(leņķu summa)"),
                ("ārējais = 180° − ∠B = ∠A + ∠C", "(abas izsaka 180° − ∠B)"),
            ],
            atbilde="Pierādīts."),

    Ievadi("Aprēķini ārējo leņķi", [
        {"jaut": "∠A = 45°, ∠C = 70°. Ārējais leņķis pie B (°)?",
         "atb": ["115"], "padoms": "45 + 70."},
        {"jaut": "∠B = 80°. Ārējais leņķis pie B (°)?",
         "atb": ["100"], "padoms": "180 − 80."},
        {"jaut": "Ārējais pie C = 130°, ∠A = 60°. ∠B (°)?",
         "atb": ["70"], "padoms": "130 − 60."},
        {"jaut": "Vienādmalu trijstūra ārējais leņķis (°)?",
         "atb": ["120"], "padoms": "60 + 60."},
    ]),

    Varianti("Ārējais leņķis", [
        {"jaut": "Cik ārējo leņķu ir pie vienas virsotnes?",
         "opcijas": ["Divi (vienādi - krustleņķi)", "Viens", "Trīs",
                     "Neviens"],
         "pareizi": 0, "padoms": "Var pagarināt jebkuru no divām malām."},
        {"jaut": "Ārējais leņķis ir plats. Kāds ir iekšējais pie tās "
                 "pašas virsotnes?",
         "opcijas": ["Šaurs", "Plats", "Taisns", "Nevar zināt"],
         "pareizi": 0, "padoms": "Summa 180°."},
        {"jaut": "Vai ārējais leņķis var būt mazāks par iekšējo leņķi, kas "
                 "nav tam blakus?",
         "opcijas": ["Nē", "Jā", "Tikai platleņķa trijstūrī"],
         "pareizi": 0, "jaukt": False,
         "padoms": "Tas ir divu summa."},
    ]),

    Pasaule("Robota pagrieziens",
            Ievadi("", [
                {"jaut": "Robots brauc pa trijstūri. Iekšējais leņķis "
                         "virsotnē 70°. Par cik grādiem tam jāpagriežas "
                         "(ārējais leņķis)?",
                 "atb": ["110"], "padoms": "180 − 70."},
                {"jaut": "Trijstūra leņķi 70°, 60°, 50°. Pagriezieni: 110°, "
                         "120° un cik?",
                 "atb": ["130"], "padoms": "180 − 50."},
                {"jaut": "Visu trīs pagriezienu summa (°)?",
                 "atb": ["360"], "padoms": "Viens pilns apgrieziens."},
            ]),
            pavediens="tehnika",
            konteksts="Programmējot robotu, pagrieziena leņķis ir ārējais "
                      "leņķis, nevis iekšējais.",
            kapec="Ārējo leņķu summa - pilns apgrieziens 360°."),

    Zimejums("Visi trīs ārējie leņķi",
             geometrija([("A", 0, 0), ("B", 6, 0), ("C", 2, 3.5),
                         ("_x", 8, 0), ("_y", 3, 5.25), ("_z", -1, -1.75)],
                        nogriezni=["AB", "BC", "CA"],
                        stari=[("B", "_x"), ("C", "_y"), ("A", "_z")],
                        lenki=[(("_x", "B", "C"), ""),
                               (("_y", "C", "A"), "", 2),
                               (("_z", "A", "B"), "", 3)]),
             paskaidro="Pa vienam katrā virsotnē: summa 360°."),

    Kopsavilkums([
        "Definēju trijstūra ārējo leņķi.",
        "Zinu: ārējais = abu nesaistīto iekšējo summa.",
        "Pierādu to ar leņķu summu.",
        "Zinu, ka ārējo leņķu summa ir 360°.",
    ]),

    Majas([
        "Uzzīmē trijstūri, pagarini malas un izmēri ārējos leņķus.",
        "Pārbaudi, ka to summa ir 360°.",
        "Pierādi, ka ārējo leņķu summa ir 360°.",
    ]),
]
