# -*- coding: utf-8 -*-
"""1. klase, 7. stunda: «Kā izveidot savu rakstu?»

Rakstu veido pats: izvēlas grupu (2-3 figūras) un atkārto to. Mācās
parādīt grupu un saskaitīt, cik figūru vajag, ja grupu atkārto vairākas
reizes.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, bildes)

TEMA = "Kā izveidot savu rakstu?"

MERKIS = ("Šodien veidosim savu rakstu un parādīsim grupu, kas "
          "atkārtojas.")

SATURS = [
    Sakums("No kā sastāv raksts?",
           zimejums=bildes([["zvaigzne", "sirds", "sirds"] * 3]),
           paraksts="Grupa: zvaigzne, sirds, sirds - atkārtota 3 reizes.",
           fakti=["Rakstam vajag grupu.",
                  "Grupu atkārto atkal un atkal.",
                  "Ja grupu maina, raksts izjūk."]),

    Doma("Grupa un atkārtojums",
         "Izvēlies grupu un atkārto to vienādi - tā rodas raksts.",
         soli=[
             "Izvēlies 2 vai 3 figūras - tā ir grupa.",
             "Noliec grupu.",
             "Noliec to pašu grupu vēlreiz un vēlreiz.",
         ]),

    Ievadi("Cik figūru?", [
        {"jaut": "Grupā ir 2 figūras. Grupu atkārto 3 reizes. Cik figūru "
                 "kopā?", "zim": bildes([["aplis", "kvadrats"] * 3]),
         "atb": ["6"], "padoms": "Saskaiti zīmējumā."},
        {"jaut": "Cik figūru ir grupā?",
         "zim": bildes([["trijsturis", "aplis", "aplis"] * 2]),
         "atb": ["3"], "padoms": "Trijstūris, aplis, aplis."},
        {"jaut": "Cik reizes grupa atkārtota?",
         "zim": bildes([["sirds", "zvaigzne"] * 4]), "atb": ["4"],
         "padoms": "Saskaiti sirdis."},
    ]),

    Varianti("Vai tas ir raksts?", [
        {"jaut": "Vai te ir raksts?",
         "zim": bildes([["aplis", "kvadrats", "aplis", "kvadrats", "aplis",
                         "kvadrats"]]),
         "opcijas": ["Jā", "Nē"], "jaukt": False, "pareizi": 0,
         "padoms": "Aplis, kvadrāts atkārtojas."},
        {"jaut": "Vai te ir raksts?",
         "zim": bildes([["aplis", "kvadrats", "kvadrats", "aplis",
                         "trijsturis", "aplis"]]),
         "opcijas": ["Jā", "Nē"], "jaukt": False, "pareizi": 1,
         "padoms": "Nav grupas, kas atkārtojas."},
        {"jaut": "Kurā vietā raksts izjūk?",
         "zim": bildes([["zvaigzne", "sirds", "zvaigzne", "sirds",
                         "sirds", "zvaigzne"]]),
         "opcijas": ["5. figūra", "2. figūra", "1. figūra"],
         "pareizi": 0, "padoms": "Pēc sirds jānāk zvaigznei."},
    ]),

    Petijums("Mans raksts", [
        "Izvēlies 2 vai 3 krāsainas figūras.",
        "Noliec tās rindā - tā ir tava grupa.",
        "Atkārto grupu vēl 3 reizes.",
        "Palūdz blakus sēdētājam parādīt tavu grupu.",
    ], vajag="krāsainas figūras vai krāsu zīmuļi"),

    Pasaule("Apmale burtnīcā",
            Ievadi("", [
                {"jaut": "Toms zīmē apmali: 1 zvaigzne un 2 sirdis, 4 reizes. "
                         "Cik siržu viņš uzzīmēs?", "atb": ["8"],
                 "padoms": "Katrā grupā 2 sirdis."},
                {"jaut": "Cik zvaigžņu?", "atb": ["4"],
                 "padoms": "Katrā grupā 1."},
            ]),
            pavediens="skola",
            konteksts="Burtnīcas lapas malā zīmē rakstu, kas atkārtojas.",
            kapec="Zinot grupu, var saskaitīt, cik katras figūras vajag."),

    Kopsavilkums([
        "Veidoju rakstu no grupas, kas atkārtojas.",
        "Parādu grupu citu rakstā.",
        "Pamanu, kur raksts izjūk.",
    ]),

    Majas([
        "Izveido rakstu no pogām vai makaroniem.",
        "Uzzīmē apmali ar savu rakstu.",
        "Paslēp vienu figūru un palūdz kādam atrast, kuras trūkst.",
    ]),
]
