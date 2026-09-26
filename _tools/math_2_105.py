# -*- coding: utf-8 -*-
"""2. klase, 105. stunda: «Kas ir kopīgā daļa?»

Divas figūras var pārklāties; kopīgā daļa ir tā vieta, kas pieder abām -
tāpat kā Venna diagrammas vidus. Ar caurspīdīgiem modeļiem to redz un var
aprakstīt: kāda forma, cik rūtiņu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, restis)

TEMA = "Kas ir kopīgā daļa?"

MERKIS = ("Šodien pētīsim figūru pārklāšanos ar caurspīdīgiem modeļiem un "
          "aprakstīsim kopīgo daļu.")

# Divi taisnstūri rūtiņu tīklā: «A» - tikai pirmajā, «B» - tikai otrajā,
# «AB» - kopīgā daļa. Tā kopīgo daļu var saskaitīt pa rūtiņām.
_PARKLAJUMS = restis([["A", "A", "A", "A", "", ""],
                      ["A", "A", "AB", "AB", "B", "B"],
                      ["A", "A", "AB", "AB", "B", "B"],
                      ["", "", "B", "B", "B", "B"]])

SATURS = [
    Sakums("Kur saulesbrilles abas stikla daļas pārklājas?",
           zimejums=_PARKLAJUMS,
           paraksts="AB - vieta, kas pieder abiem taisnstūriem.",
           fakti=["Pārklājoties rodas kopīgā daļa.",
                  "Tā pieder abām figūrām.",
                  "Tāpat kā Venna diagrammas vidus."]),

    Doma("Kopīgā daļa",
         "Kopīgā daļa ir tā, kas ir gan pirmajā, gan otrajā figūrā.",
         soli=[
             "Uzliec vienu caurspīdīgu figūru uz otras.",
             "Atrodi vietu, kur redzamas abas.",
             "Apvelc to un nosauc formu.",
             "Saskaiti tās rūtiņas.",
         ]),

    Ievadi("Saskaiti rūtiņas", [
        {"jaut": "Cik rūtiņu ir kopīgajā daļā AB?", "zim": _PARKLAJUMS,
         "atb": ["4"], "padoms": "Skaiti «AB»."},
        {"jaut": "Cik rūtiņu ir visā taisnstūrī A (ar kopīgo daļu)?",
         "zim": _PARKLAJUMS, "atb": ["12"], "padoms": "«A» un «AB»."},
        {"jaut": "Cik rūtiņu ir visā taisnstūrī B?", "zim": _PARKLAJUMS,
         "atb": ["12"], "padoms": "«B» un «AB»."},
        {"jaut": "Cik rūtiņu aizņem abi kopā?", "zim": _PARKLAJUMS,
         "atb": ["20"], "padoms": "12 + 12 − 4."},
    ]),

    Varianti("Kāda ir kopīgā daļa?", [
        {"jaut": "Kādas formas ir kopīgā daļa AB?", "zim": _PARKLAJUMS,
         "opcijas": ["kvadrāts", "trijstūris", "aplis"], "pareizi": 0,
         "padoms": "2 rūtiņas plata, 2 augsta."},
        {"jaut": "Divi apļi pārklājas. Kāda forma ir kopīgā daļa?",
         "opcijas": ["kā citrona šķēle", "kvadrāts", "trijstūris"],
         "pareizi": 0, "padoms": "Divas izliektas malas."},
        {"jaut": "Vai divām figūrām kopīgās daļas var nebūt?",
         "opcijas": ["Jā, ja tās nepieskaras", "Nē, vienmēr ir"],
         "jaukt": False, "pareizi": 0, "padoms": "Tās var būt atsevišķi."},
    ]),

    Petijums("Caurspīdīgi modeļi", [
        "Uz caurspīdīgas plēves uzzīmē taisnstūri, uz otras - apli.",
        "Uzliec vienu uz otras dažādos veidos.",
        "Katru reizi apvelc kopīgo daļu.",
        "Kādas formas kopīgās daļas izdevās?",
    ], vajag="caurspīdīgas plēves, flomāsteri"),

    Pasaule("Divu lukturu gaisma",
            Varianti("", [
                {"jaut": "Divi lukturi apgaismo apļus uz ceļa. Kur ir "
                         "visgaišāk?",
                 "opcijas": ["kopīgajā daļā", "ārpus apļiem",
                             "tikai viena apļa vidū"], "pareizi": 0,
                 "padoms": "Tur spīd abi."},
            ]),
            pavediens="tehnika",
            konteksts="Ielu lukturu gaismas apļi pārklājas.",
            kapec="Kopīgā daļa saņem gaismu no abiem."),

    Kopsavilkums([
        "Atrodu divu figūru kopīgo daļu.",
        "Aprakstu tās formu.",
        "Saskaitu tās rūtiņas.",
    ]),

    Majas([
        "Uzliec vienu uz otras divas krūzes paliktņus vai monētas.",
        "Apvelc kopīgo daļu uz papīra.",
        "Kāda ir tās forma?",
    ]),
]
