# -*- coding: utf-8 -*-
"""2. klase, 115. stunda: «Cik liels ir lapas laukums?»

Neregulāras figūras (koka lapa, peļķe) laukumu nosaka aptuveni: uzliek
caurspīdīgu rūtiņu tīklu, saskaita pilnās rūtiņas un pieskaita pusi no
nepilnajām. Tēmas noslēgums.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, restis)

TEMA = "Cik liels ir lapas laukums?"

MERKIS = ("Šodien ar caurspīdīgu rūtiņu tīklu noteiksim aptuvenu "
          "neregulāras figūras laukumu.")

# Lapa rūtiņu tīklā: «P» - pilna rūtiņa, «d» - daļēja, tukša - ārpusē.
_LAPA = restis([["", "d", "d", ""],
                ["d", "P", "P", "d"],
                ["d", "P", "P", "d"],
                ["", "d", "d", ""]])

SATURS = [
    Sakums("Kā noteikt koka lapas laukumu, ja tai nav taisnu malu?",
           zimejums=_LAPA,
           paraksts="P - pilnas rūtiņas, d - daļējas.",
           fakti=["Pilnās rūtiņas saskaita.",
                  "Daļējās: apmēram divas daļējas = viena pilna.",
                  "4 pilnas + 8 daļējas ≈ 4 + 4 = 8 rūtiņas."]),

    Doma("Aptuvenais laukums",
         "Pilnās rūtiņas + puse no daļējām.",
         soli=[
             "Uzliec caurspīdīgu rūtiņu tīklu uz figūras.",
             "Saskaiti pilnās rūtiņas.",
             "Saskaiti daļējās un paņem pusi.",
             "Saskaiti: tas ir aptuvenais laukums.",
         ]),

    Ievadi("Saskaiti", [
        {"jaut": "Cik pilno rūtiņu?", "zim": _LAPA, "atb": ["4"],
         "padoms": "Skaiti P."},
        {"jaut": "Cik daļējo rūtiņu?", "zim": _LAPA, "atb": ["8"],
         "padoms": "Skaiti d."},
        {"jaut": "Aptuvenais laukums rūtiņās?", "zim": _LAPA, "atb": ["8"],
         "padoms": "4 + puse no 8."},
        {"jaut": "Citai lapai: 10 pilnas, 6 daļējas. Aptuveni?",
         "atb": ["13"], "padoms": "10 + 3."},
    ]),

    Varianti("Kā mērīt?", [
        {"jaut": "Kāpēc nevar izmērīt tikai ar lineālu?",
         "opcijas": ["Lapai nav taisnu malu", "Lapa par mazu",
                     "Lineāls par īsu"], "pareizi": 0,
         "padoms": "Malas izliektas."},
        {"jaut": "Kā iegūt precīzāku rezultātu?",
         "opcijas": ["ņemt mazākas rūtiņas", "ņemt lielākas rūtiņas",
                     "neskaitīt daļējās"], "pareizi": 0,
         "padoms": "Jo sīkāk, jo precīzāk."},
    ]),

    Petijums("Kuras lapas laukums lielāks?", [
        "Atnes 2 dažādu koku lapas (kļava, bērzs).",
        "Novelc tās uz rūtiņu lapas.",
        "Saskaiti pilnās un daļējās rūtiņas.",
        "Aprēķini aptuveno laukumu. Kura lapa lielāka?",
    ], vajag="koku lapas, rūtiņu lapa, zīmulis"),

    Pasaule("Peļķe uz ceļa",
            Ievadi("", [
                {"jaut": "Peļķe kartē aizņem 12 pilnas un 10 daļējas rūtiņas. "
                         "Aptuvenais laukums?", "atb": ["17"],
                 "padoms": "12 + 5."},
            ]),
            pavediens="planeta",
            konteksts="Ezeru un mežu laukumu kartēs nosaka ar rūtiņām.",
            kapec="Tā kartogrāfi mēra ezeru un salu laukumus."),

    Kopsavilkums([
        "Nosaku neregulāras figūras aptuveno laukumu.",
        "Saskaitu pilnās un pusi no daļējām rūtiņām.",
        "Zinu, ka mazākas rūtiņas dod precīzāku rezultātu.",
    ]),

    Majas([
        "Novelc savu plaukstu uz rūtiņu lapas.",
        "Aprēķini aptuveno laukumu.",
        "Salīdzini ar mājinieka plaukstu.",
    ]),
]
