# -*- coding: utf-8 -*-
"""
Fizika I pārbaudes darbu (PD) veidotājs.

Izmanto to pašu dzinēju, kas dabaszinību darbiem (pd_common.py) - mainās
tikai priekšmeta nosaukums galvenē un saknes mape.

Satura shēma ir tā pati, kas pd_XX_saturs.py failos; papildus ir atslēga
"klase" ("10. klase" vai "11. klase").

Palaiž:  .venv/Scripts/python.exe _tools/gen_fiz_pd.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pd_common as C                                   # noqa: E402

SAKNE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIZIKA = os.path.join(SAKNE, "Fizika_1")


def lidzsvarot(pd):
    """Izlīdzina pareizo atbilžu izkliedi pa burtiem A-D.

    pd_common.parbaudi() prasa, lai neviens burts neatkārtotos vairāk par
    pusi jautājumu. Šeit to panāk, pārkārtojot atbilžu variantus tajos
    jautājumos, kur pārstāvētais burts sastopams pārāk bieži - jautājuma
    saturs nemainās, mainās tikai atbilžu secība.
    """
    for v in pd["varianti"]:
        tests = v["tests"]
        limits = len(tests) // 2
        while True:
            skaits = [0, 0, 0, 0]
            for _, _, pareizais in tests:
                skaits[pareizais] += 1
            biezakais = max(range(4), key=lambda i: skaits[i])
            if skaits[biezakais] <= limits:
                break
            retakais = min(range(4), key=lambda i: skaits[i])
            for i, (jaut, varianti, pareizais) in enumerate(tests):
                if pareizais != biezakais:
                    continue
                jauns = list(varianti)
                jauns.insert(retakais, jauns.pop(pareizais))
                tests[i] = (jaut, jauns, retakais)
                break
    return pd


def build(pd):
    """Uzbūvē darba lapu un atbilžu lapu Fizika_1 temata mapē."""
    lidzsvarot(pd)
    vecais_pr, veca_mape = C.PRIEKSMETS, C.SAKNES_MAPE
    C.PRIEKSMETS = "Fizika I  |  %s" % pd["klase"]
    C.SAKNES_MAPE = FIZIKA
    try:
        return C.build(pd)
    finally:
        C.PRIEKSMETS, C.SAKNES_MAPE = vecais_pr, veca_mape
