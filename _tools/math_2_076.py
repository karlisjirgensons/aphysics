# -*- coding: utf-8 -*-
"""2. klase, 76. stunda: «Kā uzrakstīt savu uzdevumu?»

Mikrotemata noslēgums: skolēns pats izdomā situāciju, uzraksta jautājumu
un izteiksmi, tad apmainās ar klasesbiedru. Lai uzdevums būtu labs, tajā
jābūt visiem vajadzīgajiem skaitļiem un skaidram jautājumam.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti)

TEMA = "Kā uzrakstīt savu uzdevumu?"

MERKIS = ("Šodien izdomāsim situāciju un pierakstīsim to ar divu darbību "
          "izteiksmi.")

SATURS = [
    Sakums("Kas vajadzīgs labam matemātikas uzdevumam?",
           fakti=["Situācija ar skaitļiem.",
                  "Skaidrs jautājums: cik? par cik?",
                  "Pietiek datu, lai atbildētu."]),

    Doma("Labs uzdevums",
         "Uzdevumā ir situācija, visi vajadzīgie skaitļi un jautājums.",
         soli=[
             "Izvēlies tēmu: veikals, sports, dzīvnieki.",
             "Uzraksti, kas bija sākumā.",
             "Pievieno divus notikumus.",
             "Uzdod jautājumu un uzraksti izteiksmi.",
         ]),

    Varianti("Vai uzdevums ir labs?", [
        {"jaut": "«Mežā bija zaķi. 5 aizbēga. Cik palika?»",
         "opcijas": ["Trūkst skaitļa - cik bija sākumā", "Labs",
                     "Trūkst jautājuma"], "pareizi": 0,
         "padoms": "Cik zaķu bija?"},
        {"jaut": "«Grozā 20 āboli, pielika 8, apēda 5.»",
         "opcijas": ["Trūkst jautājuma", "Labs", "Trūkst skaitļa"],
         "pareizi": 0, "padoms": "Ko jautā?"},
        {"jaut": "«Plauktā 30 grāmatas, 7 paņēma, 4 atnesa. Cik tagad?»",
         "opcijas": ["Labs", "Trūkst jautājuma", "Trūkst skaitļa"],
         "pareizi": 0, "padoms": "Viss ir."},
        {"jaut": "«Anna nopirka konfektes par 3 € un sulu. Cik samaksāja?»",
         "opcijas": ["Trūkst sulas cenas", "Labs", "Trūkst jautājuma"],
         "pareizi": 0, "padoms": "Cik maksāja sula?"},
    ]),

    Petijums("Mans uzdevums", [
        "Izdomā situāciju ar trim skaitļiem līdz 100.",
        "Uzraksti to 2-3 teikumos ar jautājumu.",
        "Atsevišķi uzraksti izteiksmi un atbildi.",
        "Apmainies ar klasesbiedru un atrisiniet viens otra uzdevumu.",
    ], vajag="burtnīca", secinajums="Ja abi ieguvāt to pašu atbildi, "
                                    "uzdevums ir skaidrs."),

    Ievadi("Atrisini klasesbiedra uzdevumu", [
        {"jaut": "«Akvārijā 24 zivtiņas. Nopirka vēl 9, 3 iedeva draugam. "
                 "Cik tagad?»", "atb": ["30"], "padoms": "24 + 9 − 3."},
        {"jaut": "«Krājkasītē 55 €. Nopirka spēli par 30 € un grāmatu par "
                 "12 €. Cik palika?»", "atb": ["13"], "mers": "€",
         "padoms": "55 − (30 + 12)."},
    ]),

    Pasaule("Uzdevums avīzei",
            Varianti("", [
                {"jaut": "Skolas avīzei jāuzraksta uzdevums izteiksmei "
                         "70 − 25 + 10. Kurš der?",
                 "opcijas": ["Parkā 70 koki, 25 nocirta, 10 iestādīja. Cik "
                             "tagad?",
                             "Parkā 70 koki, 25 iestādīja, 10 nocirta. Cik "
                             "tagad?",
                             "Parkā 70 koki un 25 krūmi."], "pareizi": 0,
                 "padoms": "Vispirms mīnus, tad plus."},
            ]),
            pavediens="skola",
            konteksts="Skolas avīzē ir sadaļa «Atrisini!».",
            kapec="Labs uzdevums ir skaidrs katram lasītājam."),

    Kopsavilkums([
        "Izdomāju situāciju ar divām darbībām.",
        "Uzrakstu skaidru jautājumu.",
        "Pierakstu izteiksmi un atbildi.",
    ]),

    Majas([
        "Izdomā uzdevumu par savu ģimeni.",
        "Lai mājinieks to atrisina.",
        "Vai viņš ieguva tavu atbildi?",
    ]),
]
