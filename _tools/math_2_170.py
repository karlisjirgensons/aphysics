# -*- coding: utf-8 -*-
"""2. klase, 170. stunda: «Kurus reizinājumus zinu no galvas?»

Gada noslēgums, 2. stunda: pārbaude par reizinājumiem ar 2, 3, 4 un 5 un
atbilstošajiem dalījumiem. Skolēns aizpilda savu «zinu / trenēt» tabulu un
izvēlas vasaras treniņam konkrētus reizinājumus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, restis)

TEMA = "Kurus reizinājumus zinu no galvas?"

MERKIS = ("Šodien pārbaudīsim reizinājumus ar 2, 3, 4 un 5 un izvēlēsimies "
          "trenējamos.")

_KOPA = restis([["·", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                [2, None, 4, None, 8, None, 12, None, 16, None, 20],
                [3, 3, None, 9, None, 15, None, 21, None, 27, None],
                [4, None, 8, None, 16, None, 24, None, 32, None, 40],
                [5, 5, None, 15, None, 25, None, 35, None, 45, None]])

SATURS = [
    Sakums("Vai vari aizpildīt tabulas tukšās rūtiņas no galvas?",
           zimejums=_KOPA,
           paraksts="«?» - reizinājumi, kas jāatceras.",
           fakti=["Šogad iemācījies 4 tabulas.",
                  "Triki: dubultot, puse no 10, vietas maiņa.",
                  "Šodien noskaidrosim, kuri jau galvā."]),

    Doma("Mani palīgi",
         "Ja reizinājumu neatceries, atrodi to no zināmā.",
         soli=[
             "· 2: dubulto.",
             "· 4: dubulto divreiz.",
             "· 5: puse no · 10.",
             "· 3: · 2 un vēl vienreiz.",
         ]),

    Ievadi("Aizpildi tabulu", [
        {"jaut": "2 · 7 = ?", "zim": _KOPA, "atb": ["14"],
         "padoms": "7 + 7."},
        {"jaut": "3 · 8 = ?", "zim": _KOPA, "atb": ["24"],
         "padoms": "16 + 8."},
        {"jaut": "4 · 9 = ?", "zim": _KOPA, "atb": ["36"],
         "padoms": "18, 36."},
        {"jaut": "5 · 6 = ?", "zim": _KOPA, "atb": ["30"],
         "padoms": "Puse no 60."},
        {"jaut": "4 · 5 = ?", "zim": _KOPA, "atb": ["20"],
         "padoms": "10, 20."},
        {"jaut": "3 · 4 = ?", "zim": _KOPA, "atb": ["12"],
         "padoms": "8 + 4."},
    ], pamats=4),

    Ievadi("Dalījumi", [
        {"jaut": "28 : 4 = ?", "atb": ["7"], "padoms": "4 · 7."},
        {"jaut": "45 : 5 = ?", "atb": ["9"], "padoms": "5 · 9."},
        {"jaut": "18 : 3 = ?", "atb": ["6"], "padoms": "3 · 6."},
        {"jaut": "16 : 2 = ?", "atb": ["8"], "padoms": "2 · 8."},
    ]),

    Petijums("Mana tabula", [
        "Uzzīmē tabulu ar 4 rindām: · 2, · 3, · 4, · 5.",
        "Atzīmē ar ✓ reizinājumus, ko zini uzreiz.",
        "Apvelc tos, kas vēl grūti.",
        "Izveido kartītes tieši šiem - vasaras treniņam.",
    ], vajag="lapa, krāsainie zīmuļi"),

    Pasaule("Saldējuma kiosks vasarā",
            Ievadi("", [
                {"jaut": "Bumbiņa maksā 2 €. Ģimene nopērk 7 bumbiņas. Cik "
                         "maksā?", "atb": ["14"], "mers": "€",
                 "padoms": "7 · 2."},
                {"jaut": "Ar 20 € - cik bumbiņu pa 4 € var nopirkt?",
                 "atb": ["5"], "padoms": "20 : 4."},
            ]),
            pavediens="veikals",
            konteksts="Vasarā saldējuma kioskā cenas ir apaļos eiro.",
            kapec="Reizinājumi no galvas - un rēķins ir gatavs."),

    Kopsavilkums([
        "Pārbaudīju reizinājumus ar 2, 3, 4 un 5.",
        "Zinu, kurus vēl jātrenē.",
        "Izmantoju trikus reizinājumu atrašanai.",
    ]),

    Majas([
        "Vasarā trenējies ar kartītēm 2 reizes nedēļā.",
        "Katru reizi 5 minūtes.",
        "Rudenī pārbaudi sevi vēlreiz!",
    ]),
]
