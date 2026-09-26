# -*- coding: utf-8 -*-
"""2. klase, 103. stunda: «Kā pierakstīt savu rakstu?»

Otrādi: rakstu (virkni figūru vai līniju) apraksta ar ciklisku algoritmu -
atrod daļu, kas atkārtojas, un pieraksta, cik reizes. Tā pati domāšana kā
1. klases virknēs, tikai ar pierakstu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, bildes)

TEMA = "Kā pierakstīt savu rakstu?"

MERKIS = ("Šodien pierakstīsim ciklisku algoritmu savas figūru virknes "
          "veidošanai.")

_RAKSTS = bildes([["aplis", "trijsturis", "trijsturis", "aplis",
                   "trijsturis", "trijsturis", "aplis", "trijsturis",
                   "trijsturis"]])

SATURS = [
    Sakums("Kā pierakstīt tautisko jostu rakstu?",
           zimejums=_RAKSTS,
           paraksts="Aplis, trijstūris, trijstūris - un atkal.",
           fakti=["Lielvārdes jostā raksti atkārtojas.",
                  "Atrodi daļu, kas atkārtojas.",
                  "Pieraksti: «Atkārto 3 reizes: aplis, 2 trijstūri»."]),

    Doma("Raksta algoritms",
         "Atrodi mazāko daļu, kas atkārtojas, un saskaiti, cik reižu.",
         soli=[
             "Sāc no sākuma un meklē, kur viss sākas no jauna.",
             "Tā ir atkārtojamā daļa.",
             "Saskaiti, cik reižu tā ir rakstā.",
             "Pieraksti: «Atkārto N reizes: ...».",
         ]),

    Ievadi("Atrodi atkārtojumu", [
        {"jaut": "Cik figūru ir atkārtojamā daļā?", "zim": _RAKSTS,
         "atb": ["3"], "padoms": "Aplis, trijstūris, trijstūris."},
        {"jaut": "Cik reizes daļa atkārtojas?", "zim": _RAKSTS,
         "atb": ["3"], "padoms": "Saskaiti apļus."},
        {"jaut": "Cik trijstūru būs, ja atkārto 5 reizes?", "atb": ["10"],
         "padoms": "2 katrā reizē."},
        {"jaut": "Cik figūru kopā, ja atkārto 5 reizes?", "atb": ["15"],
         "padoms": "3 katrā reizē."},
    ]),

    Varianti("Kurš pieraksts der?", [
        {"jaut": "Kurš pieraksts apraksta šo rakstu?",
         "zim": bildes([["kvadrats", "kvadrats*", "kvadrats", "kvadrats*",
                         "kvadrats", "kvadrats*"]]),
         "opcijas": ["Atkārto 3 reizes: violets, dzeltens",
                     "Atkārto 6 reizes: violets",
                     "Atkārto 2 reizes: violets, dzeltens"],
         "pareizi": 0, "padoms": "Divas krāsas pārmaiņus."},
        {"jaut": "Kāds būs nākamais?",
         "zim": bildes([["zvaigzne", "sirds", "sirds", "zvaigzne", "sirds",
                         None]]),
         "opcijas": ["sirds", "zvaigzne"], "jaukt": False, "pareizi": 0,
         "padoms": "Zvaigzne, 2 sirdis."},
    ]),

    Petijums("Mans raksts", [
        "Izdomā atkārtojamu daļu no 2-4 figūrām.",
        "Uzraksti algoritmu: «Atkārto ... reizes: ...».",
        "Iedod algoritmu klasesbiedram - lai uzzīmē.",
        "Vai raksts sanāca tāds, kā gribēji?",
    ], vajag="rūtiņu lapa, krāsainie zīmuļi"),

    Pasaule("Pērļu aproce",
            Ievadi("", [
                {"jaut": "Aprocei: atkārto 8 reizes: 2 sarkanas, 1 balta "
                         "pērle. Cik balto pērļu vajag?", "atb": ["8"],
                 "padoms": "Viena katrā reizē."},
                {"jaut": "Cik sarkano?", "atb": ["16"],
                 "padoms": "2 katrā reizē: 8 + 8."},
            ]),
            pavediens="maja",
            konteksts="Pērļu aproces raksts atkārtojas.",
            kapec="Algoritms pasaka, cik pērļu pirkt."),

    Kopsavilkums([
        "Atrodu rakstā daļu, kas atkārtojas.",
        "Pierakstu ciklisku algoritmu.",
        "Aprēķinu, cik figūru vajag.",
    ]),

    Majas([
        "Atrodi mājās rakstu, kas atkārtojas: tapetēs, audumā, flīzēs.",
        "Uzraksti tā algoritmu.",
        "Uzzīmē savu jostas rakstu.",
    ]),
]
