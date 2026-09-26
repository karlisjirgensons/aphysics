# -*- coding: utf-8 -*-
"""9. klase, 128. stunda: «Kā virkni attēlot grafiski?»

Virknes grafiks - punkti (n; a_n). No tā redz augšanas veidu: vienmērīgi
(punkti uz taisnes), paātrināti (līkne augšup) vai tuvojoties vērtībai.
Salīdzina divus krājumu plānus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, plakne, restis)

TEMA = "Kā virkni attēlot grafiski?"

MERKIS = ("Attēlosim virkni koordinātu plaknē un raksturosim tās "
          "uzvedību.")

_A = [(n, 10 + 10 * n, "") for n in range(1, 7)]
_B = [(n, 5 * 2 ** (n - 1), "") for n in range(1, 7)]

SATURS = [
    Sakums("Divi krāšanas plāni - kurš uzvar?",
           zimejums=plakne(punkti=_A + _B, no_x=0, lidz_x=7, no_y=0,
                           lidz_y=180, solis_y=20, x_nos="n", y_nos="€"),
           paraksts="A: +10 € mēnesī. B: katru mēnesi divreiz vairāk.",
           fakti=["A punkti guļ uz taisnes - vienmērīga augšana.",
                  "B punkti izliecas augšup - paātrināta augšana.",
                  "Pēc 5. mēneša B apsteidz A."]),

    Doma("Virknes grafiks",
         "Katram loceklim - punkts (n; a_n); punktus NEsavieno ar līniju.",
         soli=[
             "Tabula: n un a_n.",
             "Uz horizontālās ass - numurs n, uz vertikālās - a_n.",
             "Atliec punktus.",
             "Raksturo: augoša/dilstoša, vienmērīgi/paātrināti.",
         ]),

    Slidnis("Divi plāni pa mēnešiem", [
        {"v": "A", "teksts": "20, 30, 40, 50, 60, 70 - vienmērīgi",
         "zim": plakne(punkti=_A, no_x=0, lidz_x=7, no_y=0, lidz_y=180,
                       solis_y=20, x_nos="n", y_nos="€")},
        {"v": "B", "teksts": "5, 10, 20, 40, 80, 160 - paātrināti",
         "zim": plakne(punkti=_B, no_x=0, lidz_x=7, no_y=0, lidz_y=180,
                       solis_y=20, x_nos="n", y_nos="€")},
    ]),

    Ievadi("Nolasi un aprēķini", [
        {"jaut": "Plāns A: cik € 6. mēnesī?", "atb": ["70"],
         "padoms": "10 + 60."},
        {"jaut": "Plāns B: cik € 6. mēnesī?", "atb": ["160"],
         "padoms": "5 · 2^5."},
        {"jaut": "Kurā mēnesī B pirmo reizi pārsniedz A?", "atb": ["5"],
         "padoms": "80 > 60."},
    ]),

    Varianti("Kā izskatās grafiks?", [
        {"jaut": "a_n = 3n − 1",
         "opcijas": ["Punkti uz taisnes", "Punkti uz parabolas",
                     "Nepārtraukta līnija", "Viens punkts"],
         "pareizi": 0, "padoms": "Lineāra formula."},
        {"jaut": "a_n = {12|n}",
         "opcijas": ["Punkti dilst, tuvojas 0", "Punkti aug",
                     "Punkti uz taisnes", "Visi vienādi"],
         "pareizi": 0, "padoms": "12, 6, 4, 3, ..."},
    ]),

    Pasaule("Viedtālruņa akumulators",
            Ievadi("", [
                {"jaut": "Pilns akumulators 100 %, ik stundu zūd 8 % (no "
                         "sākuma). a_n = 100 − 8n. Cik % pēc 5 h?",
                 "atb": ["60"], "padoms": "100 − 40."},
                {"jaut": "Pēc cik pilnām stundām paliks mazāk par 20 %?",
                 "atb": ["11"], "padoms": "100 − 88 = 12 < 20."},
            ]),
            pavediens="dati",
            konteksts="Telefona uzlādes grafiks ir punkti katru stundu.",
            kapec="Punkti uz taisnes - vienmērīga izlāde.",
            zimejums=restis([["h", "0", "5", "10"], ["%", "100", "60", "20"]])),

    Kopsavilkums([
        "Attēloju virkni ar punktiem plaknē.",
        "Raksturoju augšanas veidu pēc grafika.",
        "Salīdzinu divas virknes.",
    ]),

    Majas([
        "Uzzīmē a_n = 2^n un a_n = 10n pirmos 6 punktus vienā plaknē.",
        "Kurā n 2^n pārsniedz 10n?",
        "Atrodi savu «krāšanas plānu» un uzzīmē to.",
    ]),
]
