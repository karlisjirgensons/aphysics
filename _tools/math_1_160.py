# -*- coding: utf-8 -*-
"""1. klase, 160. stunda: «Kur dabā ir simetrija?»

Simetrija dabā: tauriņš, lapa, sniegpārsla, cilvēka seja, zieds.
Skolēns atrod attēlus un pamato: kur ir simetrijas līnija, kas abās pusēs
vienāds.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Pasaule, Petijums,
                         Sakums, Varianti, bildes)

TEMA = "Kur dabā ir simetrija?"

MERKIS = ("Šodien atradīsim simetriskus dabas objektus un pamatosim savu "
          "izvēli.")

SATURS = [
    Sakums("Kas kopīgs tauriņam, lapai un sniegpārslai?",
           zimejums=bildes([["puke", "sirds", "zvaigzne", "abols"]]),
           paraksts="Visiem ir simetrijas līnija.",
           fakti=["Dabā daudz simetrisku lietu.",
                  "Tauriņa spārni vienādi.",
                  "Sniegpārslai - daudz simetrijas līniju."]),

    Doma("Simetrija dabā",
         "Dabas objekts ir simetrisks, ja to var «pārlocīt» domās un puses "
         "sakrīt.",
         soli=[
             "Atrodi, kur varētu būt locījuma līnija.",
             "Salīdzini abas puses.",
             "Pamato: kas abās pusēs vienāds.",
         ],
         pieze="Dabā simetrija nav pilnīga - divas lapas puses ir gandrīz "
               "vienādas."),

    Varianti("Simetrisks?", [
        {"jaut": "Tauriņš", "opcijas": ["simetrisks", "nav"],
         "jaukt": False, "pareizi": 0, "padoms": "Spārni vienādi."},
        {"jaut": "Akmens no upes (nejaušas formas)",
         "opcijas": ["parasti nav", "vienmēr simetrisks"], "jaukt": False,
         "pareizi": 0, "padoms": "Forma nejauša."},
        {"jaut": "Cilvēka seja",
         "opcijas": ["gandrīz simetriska", "nav nemaz"], "jaukt": False,
         "pareizi": 0, "padoms": "Divas acis, divas ausis."},
        {"jaut": "Sniegpārsla",
         "opcijas": ["simetriska - daudz līniju", "nav"], "jaukt": False,
         "pareizi": 0, "padoms": "6 vienādi zari."},
    ]),

    Petijums("Simetrijas meklētāji", [
        "Pastaigā savāc 3 lapas.",
        "Atrodi katrai simetrijas līniju.",
        "Uzliec spoguli uz līnijas - vai redzi visu lapu?",
        "Uzzīmē simetriskāko.",
    ], vajag="lapas, neliels spogulis, zīmulis"),

    Pasaule("Kukaiņu vērošana",
            Varianti("", [
                {"jaut": "Kur mārītei simetrijas līnija?",
                 "opcijas": ["pa muguras vidu", "pāri galvai",
                             "tai nav"], "pareizi": 0,
                 "padoms": "Punktiņi abās pusēs vienādi."},
            ]),
            pavediens="daba",
            konteksts="Pļavā vērojam kukaiņus.",
            kapec="Simetrija palīdz dzīvniekiem kustēties līdzsvarā."),

    Kopsavilkums([
        "Atrodu simetriju dabā.",
        "Parādu simetrijas līniju.",
        "Pamatoju savu izvēli.",
    ]),

    Majas([
        "Atrodi dārzā vai parkā 3 simetriskas lietas.",
        "Nofotografē vai uzzīmē tās.",
        "Parādi klasē.",
    ]),
]
