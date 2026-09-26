# -*- coding: utf-8 -*-
"""2. klase, 4. stunda: «Kā grupēšanu parādīt ar zīmējumu?»

Grupēšanai ir divi zīmējumi: Venna diagramma (divi apļi, kas pārklājas) un
tabula ar rindām un kolonnām. Svarīgākais ir pārklājums - tur ir tie, kuriem
ir abas pazīmes, un ārpus apļiem - tie, kuriem nav nevienas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, Zimejums, restis, venna)

TEMA = "Kā grupēšanu parādīt ar zīmējumu?"

MERKIS = ("Šodien attēlosim grupēšanu Venna diagrammā un tabulā un lasīsim, "
          "kas tajās parādīts.")

_DZIVNIEKI = venna(["bite", "vārna"], ["zivs", "valis"], ["pīle", "gulbis"],
                   ("lido", "peld"))

SATURS = [
    Sakums("Kur ielikt pīli - pie tiem, kas lido, vai pie tiem, kas peld?",
           zimejums=_DZIVNIEKI,
           paraksts="Pīle prot abus - tā ir apļu kopīgajā daļā.",
           fakti=["Venna diagrammā katrai pazīmei ir savs aplis.",
                  "Kopīgajā daļā ir tie, kam ir abas pazīmes."]),

    Doma("Divi apļi - četras vietas",
         "Katrs priekšmets atrod vietu tieši vienā no četrām daļām.",
         soli=[
             "Tikai kreisajā aplī - ir tikai pirmā pazīme.",
             "Tikai labajā aplī - ir tikai otrā pazīme.",
             "Kopīgajā daļā - ir abas pazīmes.",
             "Ārpus apļiem - nav nevienas no tām.",
         ]),

    Slidnis("Liekam dzīvniekus pa vietām", [
        {"v": "bite", "teksts": "Lido, bet nepeld - kreisajā aplī.",
         "zim": venna(["bite"], [], [], ("lido", "peld"))},
        {"v": "zivs", "teksts": "Peld, bet nelido - labajā aplī.",
         "zim": venna(["bite"], ["zivs"], [], ("lido", "peld"))},
        {"v": "pīle", "teksts": "Lido un peld - kopīgajā daļā.",
         "zim": venna(["bite"], ["zivs"], ["pīle"], ("lido", "peld"))},
        {"v": "kaķis", "teksts": "Ne lido, ne peld - ārpus apļiem.",
         "zim": venna(["bite"], ["zivs"], ["pīle"], ("lido", "peld"))},
    ], ievads="Spied nākamo soli un skaties, kur nonāk dzīvnieks."),

    Varianti("Kur ir vieta?", [
        {"jaut": "Kur Venna diagrammā «lido/peld» ir gulbis?",
         "zim": _DZIVNIEKI,
         "opcijas": ["kopīgajā daļā", "tikai «lido»", "tikai «peld»",
                     "ārpus apļiem"], "jaukt": False, "pareizi": 0,
         "padoms": "Gulbis lido un peld."},
        {"jaut": "Kur ir vārna?", "zim": _DZIVNIEKI,
         "opcijas": ["kopīgajā daļā", "tikai «lido»", "tikai «peld»",
                     "ārpus apļiem"], "jaukt": False, "pareizi": 1,
         "padoms": "Vārna lido, bet nepeld."},
        {"jaut": "Kur būtu suns?", "zim": _DZIVNIEKI,
         "opcijas": ["kopīgajā daļā", "tikai «lido»", "tikai «peld»",
                     "ārpus apļiem"], "jaukt": False, "pareizi": 3,
         "padoms": "Parasti suns nelido un nav ūdens dzīvnieks."},
        {"jaut": "Kur ir valis?", "zim": _DZIVNIEKI,
         "opcijas": ["kopīgajā daļā", "tikai «lido»", "tikai «peld»",
                     "ārpus apļiem"], "jaukt": False, "pareizi": 2,
         "padoms": "Valis peld, bet nelido."},
    ]),

    Zimejums("To pašu var ierakstīt tabulā",
             restis([["", "lido", "nelido"],
                     ["peld", "pīle", "zivs"],
                     ["nepeld", "bite", "kaķis"]]),
             paskaidro="Rinda pasaka vienu pazīmi, kolonna - otru. Pīle ir "
                       "rindā «peld» un kolonnā «lido».",
             ievads="Tabulā katram dzīvniekam ir sava rūtiņa."),

    Ievadi("Nolasi diagrammu", [
        {"jaut": "Cik dzīvnieku lido?", "zim": _DZIVNIEKI, "atb": ["4"],
         "padoms": "Viss kreisais aplis kopā ar kopīgo daļu."},
        {"jaut": "Cik dzīvnieku peld?", "zim": _DZIVNIEKI, "atb": ["4"],
         "padoms": "Viss labais aplis kopā ar kopīgo daļu."},
        {"jaut": "Cik dzīvnieku prot abus?", "zim": _DZIVNIEKI,
         "atb": ["2"], "padoms": "Skaiti kopīgajā daļā."},
        {"jaut": "Cik dzīvnieku ir diagrammā pavisam?", "zim": _DZIVNIEKI,
         "atb": ["6"], "padoms": "Katru skaiti tikai vienu reizi."},
    ]),

    Pasaule("Kurš ko ēd brokastīs?",
            Ievadi("", [
                {"jaut": "Cik bērni ēd putru?", "atb": ["7"],
                 "padoms": "4 tikai putru un 3 abus."},
                {"jaut": "Cik bērni ēd maizi?", "atb": ["8"],
                 "padoms": "5 tikai maizi un 3 abus."},
                {"jaut": "Cik bērnu bija aptaujā?", "atb": ["12"],
                 "padoms": "4 + 3 + 5."},
            ]),
            pavediens="skola",
            konteksts="Venna diagrammā: tikai putra - 4 bērni, abi - 3 "
                      "bērni, tikai maize - 5 bērni.",
            zimejums=venna([4], [5], [3], ("putra", "maize")),
            kapec="Diagramma rāda, ka tie 3 nav jāskaita divreiz."),

    Kopsavilkums([
        "Ievietoju priekšmetus Venna diagrammā pēc divām pazīmēm.",
        "Zinu, ka kopīgajā daļā ir tie, kam ir abas pazīmes.",
        "Nolasu diagrammu un tabulu.",
    ]),

    Majas([
        "Uzzīmē divus apļus: «sarkans» un «ēdams».",
        "Ievieto tajos 6 lietas no mājām.",
        "Kas nonāca kopīgajā daļā?",
    ]),
]
