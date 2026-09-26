# -*- coding: utf-8 -*-
"""2. klase, 169. stunda: «Cik veikli rēķinu 100 apjomā?»

Gada noslēgums, 1. stunda: formatīva pārbaude par saskaitīšanu un
atņemšanu 100 apjomā. Skolēns pats atzīmē, kas izdodas un kas vēl jātrenē
vasarā - pārbaude ir priekš viņa, nevis atzīmei.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Petijums,
                         Sakums, restis, stabins)

TEMA = "Cik veikli rēķinu 100 apjomā?"

MERKIS = ("Šodien pārbaudīsim saskaitīšanu un atņemšanu 100 apjomā un "
          "atzīmēsim, kas vēl jātrenē.")

SATURS = [
    Sakums("Ko esi iemācījies par skaitļiem līdz 100 šajā gadā?",
           zimejums=stabins(58, 27, virs="1"),
           fakti=["Saskaiti desmitus ar desmitiem, vienus ar vieniem.",
                  "Ja vienu vairāk nekā 10 - jauns desmits.",
                  "Atņemot, ja vajag, sadala desmitu."]),

    Doma("Mans pārbaudes plāns",
         "Katram piemēram: apmērs, aprēķins, pārbaude, atzīme.",
         soli=[
             "Novērtē apmēru.",
             "Izrēķini ar sev ērtāko paņēmienu.",
             "Pārbaudi ar pretējo darbību.",
             "Atzīmē: izdevās viegli / bija grūti.",
         ]),

    Ievadi("Saskaitīšana", [
        {"jaut": "36 + 43 = ?", "atb": ["79"], "padoms": "70 + 9."},
        {"jaut": "58 + 27 = ?", "atb": ["85"], "padoms": "70 + 15."},
        {"jaut": "49 + 49 = ?", "atb": ["98"], "padoms": "50 + 50 − 2."},
        {"jaut": "65 + 35 = ?", "atb": ["100"], "padoms": "5 + 5 = 10."},
    ]),

    Ievadi("Atņemšana", [
        {"jaut": "87 − 34 = ?", "atb": ["53"], "padoms": "Vieni pietiek."},
        {"jaut": "72 − 48 = ?", "atb": ["24"], "padoms": "12 − 8, 6 − 4."},
        {"jaut": "100 − 63 = ?", "atb": ["37"], "padoms": "7 + 30."},
        {"jaut": "? + 38 = 90", "atb": ["52"], "padoms": "90 − 38."},
    ]),

    Petijums("Kas man jātrenē?", [
        "Apskati savus piemērus: kuri izdevās uzreiz?",
        "Kuri bija ar jaunu desmitu vai desmita sadalīšanu?",
        "Kurā piemērā pārbaude parādīja kļūdu?",
        "Pieraksti 3 lietas, ko trenēsi vasarā.",
    ], vajag="burtnīca", secinajums="Kas zina savas grūtības, var tās "
                                    "mērķtiecīgi trenēt."),

    Pasaule("Vasaras ceļojuma budžets",
            Ievadi("", [
                {"jaut": "Ģimenei 100 € ekskursijai. Biļetes 46 €, "
                         "pusdienas 38 €. Cik paliks?", "atb": ["16"],
                 "mers": "€", "padoms": "100 − 84."},
            ]),
            zimejums=restis([["izdevumi", "€"], ["biļetes", 46],
                             ["pusdienas", 38]]),
            pavediens="celojums",
            konteksts="Vasarā ģimene plāno ekskursiju uz Cēsu pili.",
            kapec="Rēķini 100 apjomā vajadzīgi katru dienu."),

    Kopsavilkums([
        "Pārbaudīju saskaitīšanu un atņemšanu 100 apjomā.",
        "Zinu, kas man izdodas labi.",
        "Zinu, ko trenēt vasarā.",
    ]),

    Majas([
        "Uzraksti 5 piemērus, kas tev bija grūti.",
        "Trenē tos vasarā pa vienam katru nedēļu.",
        "Veikalā saskaiti cenas galvā.",
    ]),
]
