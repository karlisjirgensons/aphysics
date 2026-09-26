# -*- coding: utf-8 -*-
"""9. klase, 96. stunda: «Kā grafiks palīdz saprast uzdevumu?»

Grafika skice atbild uz jautājumiem, pirms tie aprēķināti: kad augstums
ir 15 m (divreiz - augšup un lejup), kad bumba ir augstākajā punktā, kad
nokrīt. Un tā pārbauda, vai aprēķins ir ticams.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, parabola, saknes)

TEMA = "Kā grafiks palīdz saprast uzdevumu?"

MERKIS = ("Lietosim grafika skici, lai raksturotu situāciju vai "
          "pārbaudītu atrisinājumu.")

_T = "text"


def _bumba(punkti=(), citi=()):
    """h = −5t^2 + 20t: bumba uzmesta ar 20 m/s."""
    return parabola(-5, 20, 0, 0, 5, 0, 25, punkti=punkti, uzraksts="h(t)",
                    asis=("t", "h"),
                    solis_y=5, citi=citi)


SATURS = [
    Sakums("Bumba uzmesta ar 20 m/s. Kad tā ir 15 m augstumā?",
           zimejums=_bumba(punkti=[(1, 15, "1 s"), (3, 15, "3 s")],
                           citi=[(0, 15, "h = 15")]),
           paraksts="Divas atbildes: augšupceļā un lejupceļā.",
           fakti=["h = −5t^2 + 20t (m, s).",
                  "−5t^2 + 20t = 15 ⇒ t = 1 vai t = 3.",
                  "Grafiks uzreiz rāda: divi brīži, abi der."]),

    Slidnis("Grafiks atbild uz jautājumiem", [
        {"v": "Max", "teksts": "Augstākais punkts: t = 2 s, h = 20 m",
         "zim": _bumba(punkti=[(2, 20, "(2; 20)")])},
        {"v": "15 m", "teksts": "Divi krustpunkti ar h = 15: t = 1 un t = 3",
         "zim": _bumba(punkti=[(1, 15, "1"), (3, 15, "3")],
                       citi=[(0, 15, "")])},
        {"v": "Zemē", "teksts": "h = 0: t = 0 (metiens) un t = 4 (nokrīt)",
         "zim": _bumba(punkti=[(0, 0, "0"), (4, 0, "4")])},
        {"v": "25 m?", "teksts": "Taisne h = 25 grafiku nekrusto - tik augstu "
                                 "bumba netiek",
         "zim": _bumba(citi=[(0, 25, "h = 25")])},
    ]),

    Doma("Grafiks kā pārbaude",
         "Skice parāda, cik atbilžu gaidīt un kurš ir ticams intervāls.",
         soli=[
             "Uzskicē parabolu pēc virsotnes un nullēm.",
             "Uzzīmē horizontāli jautājuma augstumā.",
             "Krustpunktu skaits = atbilžu skaits.",
             "Salīdzini aprēķinu ar skici.",
         ]),

    Ievadi("Bumbas uzdevums (h = −5t^2 + 20t)", [
        {"jaut": "Kad h = 15 m?", "atb": saknes("1", "3"), "tastatura": _T,
         "vieta": "t₁; t₂", "padoms": "t^2 − 4t + 3 = 0."},
        {"jaut": "Cik s bumba ir augstāk par 15 m?", "atb": ["2"],
         "padoms": "No 1 līdz 3."},
        {"jaut": "Kad bumba nokrīt (t > 0)?", "atb": ["4"],
         "padoms": "−5t(t − 4) = 0."},
        {"jaut": "h pie t = 2,5 s?", "atb": ["18,75"],
         "padoms": "−31,25 + 50."},
    ]),

    Varianti("Vai aprēķins ticams?", [
        {"jaut": "Skolēns ieguva: bumba 25 m augstumā pēc 2,5 s.",
         "opcijas": ["Nē - max ir 20 m", "Jā", "Jā, lejupceļā",
                     "Nevar pārbaudīt"],
         "pareizi": 0, "padoms": "Virsotne 20 m."},
        {"jaut": "Skolēns: h = 10 m tikai vienreiz, t = 0,6 s.",
         "opcijas": ["Aizmirsta otrā sakne t ≈ 3,4 s", "Pareizi",
                     "Nav tāda brīža", "Jābūt t = 2"],
         "pareizi": 0, "padoms": "Horizontāle krusto divreiz."},
    ]),

    Pasaule("Ūdensbumba",
            Ievadi("", [
                {"jaut": "No 1 m augstuma ūdensbumbu met: h = −5t^2 + 10t + 1. "
                         "Lielākais augstums (m)?", "atb": ["6"],
                 "padoms": "t = 1: −5 + 10 + 1."},
                {"jaut": "Kad tā ir 1 m augstumā vēlreiz (s)?", "atb": ["2"],
                 "padoms": "−5t^2 + 10t = 0."},
            ]),
            pavediens="sports",
            konteksts="Vasaras spēlē ūdensbumbu met draugam, kurš stāv tikpat "
                      "augstu kā metējs.",
            kapec="Skice uzreiz rāda simetrisko brīdi.",
            zimejums=parabola(-5, 10, 1, 0, 3, -1, 7, uzraksts="h(t)",
                              asis=("t", "h"))),

    Kopsavilkums([
        "Uzskicēju grafiku pirms rēķināšanas.",
        "Nosaku atbilžu skaitu ar horizontāli.",
        "Pārbaudu aprēķina ticamību pēc grafika.",
    ]),

    Majas([
        "Bumba: h = −5t^2 + 15t. Uzskicē un atrodi max un lidojuma laiku.",
        "Kad h = 10 m? Cik atbilžu?",
        "Nofilmē metienu un pārbaudi, vai trajektorija līdzīga parabolai.",
    ]),
]
