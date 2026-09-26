# -*- coding: utf-8 -*-
"""8. klase, 120. stunda: «Kā to parādīt ģeometriski?»

Taisnstūris ar malām (a + b) un (c + d) sadalās četrās daļās: ac, bc, ad,
bd - tas ir tieši katrs ar katru. Slīdnis to pašu parāda (x + 2)(x + 3).
(a + b)^2 ≠ a^2 + b^2, jo trūkst divu taisnstūru ab.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, geometrija)

TEMA = "Kā to parādīt ģeometriski?"

MERKIS = "Modelēsim divu binomu reizinājumu ar taisnstūra laukumu."


def _zim(malas, dalas, krasas=(0, 1, 1, 0)):
    """Taisnstūris 6 × 4,5, sadalīts četrās daļās."""
    punkti = [("A", 0, 0), ("E", 4, 0), ("B", 6, 0), ("H", 6, 3),
              ("C", 6, 4.5), ("F", 4, 4.5), ("D", 0, 4.5), ("G", 0, 3)]
    return geometrija(
        [(n, x, y) for n, x, y in punkti],
        nogriezni=["AB", "BC", "CD", "DA", "EF", "GH"],
        iekrasot=[(["A", "E", "_k", "G"], krasas[0])] if False else
        [(("A", "E", "_k", "G"), krasas[0])] if False else [],
        malas=list(zip(["AE", "EB", "AG", "GD"], malas)),
        uzraksti=list(zip([2, 5, 2, 5], [1.5, 1.5, 3.75, 3.75], dalas)))


SATURS = []
