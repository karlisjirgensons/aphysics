# -*- coding: utf-8 -*-
"""Viss, no kā saliek stundu - viena vieta, ko stundas failam importēt.

Bloku veidi dzīvo trijos moduļos pēc atbildības: math_bloki.py - stundas
pamats (teksts, spēļu dzinējs, 1.-2. klases skaitīšanas spēles),
math_uzdevumi.py - uzdevumi, kuros atbildi raksta vai izvēlas,
math_interakcija.py - kustīgs objekts, slīdnis un pētījums. Stundas saturam
šis dalījums nav svarīgs, tāpēc te tie ir salikti kopā:

    from math_saturs import Stasts, Doma, Paraugs, Ievadi, Varianti

Tā stundas fails nemainās, ja bloks vēlāk pārceļas uz citu moduli (DRY).
"""

from math_bloki import (Bloks, Doma, Izvele, Josla, Kopsavilkums, Majas,
                        Modelis, Sakums, Skaiti, Spele)
from math_interakcija import Kustiba, Petijums, Slidnis
from math_uzdevumi import Ievadi, Paraugs, Pasaule, Varianti
from math_zimejumi import (Zimejums, biti, dala, figura, izklajums,
                           kermenis, kolonnas, kvadrats, laika_ass,
                           lenkis, plakne, restis, rinkis, taisne, venna)

__all__ = ["Bloks", "Doma", "Ievadi", "Izvele", "Josla", "Kopsavilkums",
           "Kustiba", "Majas", "Modelis", "Paraugs", "Pasaule", "Petijums",
           "Sakums", "Skaiti", "Slidnis", "Spele", "Varianti", "Zimejums",
           "biti", "dala", "figura", "izklajums", "kermenis", "kolonnas",
           "kvadrats",
           "laika_ass", "lenkis", "plakne", "restis", "rinkis", "taisne",
           "venna"]
