# -*- coding: utf-8 -*-
"""Viss, no kā saliek stundu - viena vieta, ko stundas failam importēt.

Bloku veidi dzīvo trijos moduļos pēc atbildības: math_bloki.py - stundas
pamats (teksts, spēļu dzinējs, 1.-2. klases skaitīšanas spēles),
math_uzdevumi.py - uzdevumi, kuros atbildi raksta vai izvēlas,
math_interakcija.py - kustīgs objekts, slīdnis, pētījums un nejaušs
eksperiments. Zīmējumi: math_zimejumi.py, math_geometrija.py (figūras
ar leņķiem) un math_koks.py (iespēju koks). Stundas saturam
šis dalījums nav svarīgs, tāpēc te tie ir salikti kopā:

    from math_saturs import Stasts, Doma, Paraugs, Ievadi, Varianti

Tā stundas fails nemainās, ja bloks vēlāk pārceļas uz citu moduli (DRY).
"""

from math_bildes import (algoritms, bildes, celjs, desmiti, kaulini, kubi, lineals,
                         majina, monetas, pulkstenis, ramis, simta_kvadrats,
                         rutinas, sloksnes, stabins, vienibas)
from math_bloki import (Bloks, Doma, Izvele, Josla, Kopsavilkums, Majas,
                        Modelis, Sakums, Skaiti, Spele)
from math_geometrija import (TRAPECES_MALAS, binoma_kvadrats, geometrija,
                             lidzigi, paralelas, prizmas_izklajums,
                             regulars, taisnlenka, trapece, trapeces_prizma,
                             uz_rinka)
from math_interakcija import Kustiba, Petijums, Simulacija, Slidnis
from math_koks import koks
from math_uzdevumi import (Ievadi, Paraugs, Pasaule, Varianti, laiks,
                            paris, saknes)
from math_zimejumi import (Zimejums, biti, cilindra_izklajums, dala,
                           figura, gredzens, izklajums, kermenis, kolonnas,
                           kvadrats, laika_ass, lenkis, likne, linijas,
                           parabola, plakne, restis, rinka_sektori, rinkis,
                           sektori, taisne, venna)

__all__ = ["TRAPECES_MALAS", "algoritms", "bildes", "celjs", "desmiti", "kaulini", "kubi", "lineals",
           "majina", "monetas", "pulkstenis", "ramis", "simta_kvadrats",
           "rutinas", "sloksnes", "stabins", "vienibas", "Bloks", "Doma", "Ievadi", "Izvele", "Josla",
           "Kopsavilkums", "Kustiba", "laiks", "Majas", "Modelis", "Paraugs", "Pasaule", "Petijums",
           "Sakums", "Simulacija", "Skaiti", "Slidnis", "Spele", "Varianti",
           "Zimejums", "binoma_kvadrats", "biti", "cilindra_izklajums", "dala", "figura",
           "geometrija", "gredzens", "izklajums", "lidzigi",
           "kermenis", "kolonnas", "koks", "kvadrats", "laika_ass", "lenkis",
           "likne", "linijas", "parabola", "paralelas", "paris", "plakne",
           "prizmas_izklajums", "regulars", "restis", "rinka_sektori", "rinkis",
           "saknes", "sektori", "taisne", "taisnlenka", "trapece",
           "trapeces_prizma", "uz_rinka", "venna"]
