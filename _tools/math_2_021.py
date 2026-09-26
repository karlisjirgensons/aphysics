# -*- coding: utf-8 -*-
"""2. klase, 21. stunda: «Kā uzzīmēt 6 cm 5 mm?»

Apgrieztā mērīšana: garums ir dots, un nogrieznis jāuzzīmē. Punktu liek pie
nulles, otru - pie vajadzīgās iedaļas, un savieno pa lineāla malu.
"""

from math_saturs import (Doma, Kopsavilkums, Kustiba, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, lineals)

TEMA = "Kā uzzīmēt 6 cm 5 mm?"

MERKIS = ("Šodien zīmēsim dota garuma nogriežņus, ja garums dots "
          "centimetros un milimetros.")

SATURS = [
    Sakums("Kā uzzīmēt līniju tieši 6 cm 5 mm garu?",
           zimejums=lineals(8, [(0, 6.5, "6 cm 5 mm")], mm=True),
           paraksts="Sāk pie 0, beidz pie garās vidus iedaļas aiz 6.",
           fakti=["Lineāla nulle ir pirmā iedaļa, nevis lineāla mala.",
                  "Galus atzīmē ar punktiem, tad savieno."]),

    Doma("Nogrieznis pēc dota garuma",
         "Punkts pie 0, punkts pie vajadzīgās iedaļas, un līnija starp tiem.",
         soli=[
             "Noliec lineālu uz lapas un atzīmē punktu pie 0.",
             "Atrodi veselos centimetrus - 6.",
             "Aiz 6 noskaiti milimetrus - 5 sīkas iedaļas.",
             "Atzīmē otru punktu un savieno abus pa lineāla malu.",
         ]),

    Slidnis("Zīmējam soli pa solim", [
        {"v": "0", "teksts": "Pirmais punkts pie nulles.",
         "zim": lineals(8, [(0, 0.05, "")], mm=True)},
        {"v": "6 cm", "teksts": "Līdz sestajai lielajai iedaļai.",
         "zim": lineals(8, [(0, 6, "")], mm=True)},
        {"v": "6 cm 5 mm", "teksts": "Vēl 5 milimetri.",
         "zim": lineals(8, [(0, 6.5, "6 cm 5 mm")], mm=True)},
    ]),

    Kustiba("Aizved zīmuli līdz galam", [
        {"jaut": "Zīmē 4 cm 5 mm. Cik mm tas ir? Zīmulis apstāsies tur.",
         "atb": 45, "beigas": 80, "iedala": 10, "mers": "mm",
         "objekts": "zīmulis", "merkis": "4 cm 5 mm",
         "padoms": "40 + 5."},
        {"jaut": "Zīmē 7 cm 2 mm. Cik mm tas ir?", "atb": 72, "beigas": 80,
         "iedala": 10, "mers": "mm", "objekts": "zīmulis",
         "merkis": "7 cm 2 mm", "padoms": "70 + 2."},
        {"jaut": "Zīmē 3 cm 8 mm. Cik mm tas ir?", "atb": 38, "beigas": 80,
         "iedala": 10, "mers": "mm", "objekts": "zīmulis",
         "merkis": "3 cm 8 mm", "padoms": "30 + 8."},
        {"jaut": "Zīmē 6 cm. Cik mm tas ir?", "atb": 60, "beigas": 80,
         "iedala": 10, "mers": "mm", "objekts": "zīmulis",
         "merkis": "6 cm", "padoms": "6 desmiti."},
    ], ievads="Trase ir lineāls milimetros."),

    Varianti("Kur ir kļūda?", [
        {"jaut": "Ieva zīmēja 5 cm, bet sāka pie lineāla malas, nevis pie 0. "
                 "Kāda iznāca līnija?",
         "opcijas": ["mazliet par garu", "tieši 5 cm", "par īsu"],
         "pareizi": 0, "padoms": "Mala ir pirms nulles."},
        {"jaut": "Ivars zīmēja 3 cm 4 mm un apstājās pie 4 cm 3 mm. Ko "
                 "sajauca?",
         "opcijas": ["cm un mm vietām", "sāka nepareizi", "neko"],
         "pareizi": 0, "padoms": "3 cm 4 mm - vispirms 3 cm."},
    ]),

    Petijums("Zīmē pats", [
        "Burtnīcā uzzīmē nogriežņus: 2 cm 5 mm, 5 cm 3 mm, 8 cm 1 mm.",
        "Pie katra uzraksti garumu.",
        "Apmainies ar klasesbiedru un izmēri viņa nogriežņus.",
        "Vai visi garumi sakrīt?",
    ], vajag="burtnīca, lineāls, asināts zīmulis"),

    Pasaule("Kartiņa ar rāmi",
            Varianti("", [
                {"jaut": "Apsveikuma kartiņā jāuzvelk līnija 9 cm 5 mm. "
                         "Kur jābeidz?",
                 "opcijas": ["pie vidus iedaļas starp 9 un 10",
                             "pie 5", "pie 9"], "pareizi": 0,
                 "padoms": "9 cm un vēl 5 mm."},
            ]),
            pavediens="maja",
            konteksts="Kartiņai zīmē rāmi pa malām.",
            kapec="Precīza līnija - glīts rāmis."),

    Kopsavilkums([
        "Zīmēju nogriezni, sākot pie lineāla nulles.",
        "Atzīmēju garumu centimetros un milimetros.",
        "Pārbaudu zīmējumu, izmērot to vēlreiz.",
    ]),

    Majas([
        "Uzzīmē 3 nogriežņus pēc mājinieka dotiem garumiem.",
        "Lai mājinieks pārbauda ar lineālu.",
        "Uzzīmē kvadrātu ar malu 4 cm 5 mm.",
    ]),
]
