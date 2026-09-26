# -*- coding: utf-8 -*-
"""IQ sadaļas būvētājs - IQ testi un vietnes sākumlapa ar IQ pogu.

    python gen_iq.py

Pilnu matemātikas sadaļu (plāni, stundas, IQ) būvē gen_math.py; šis ir
ātrais ceļš, kad mainīts tikai IQ saturs (iq_testi.py, iq_miklas.py).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import iq_vietne                                    # noqa: E402
import math_plani                                   # noqa: E402
import site_index                                   # noqa: E402


def main():
    for path in iq_vietne.build():
        print("IQ:    %s" % os.path.relpath(path, math_plani.SAKNE))
    print("Lapa:  %s" % site_index.build_home())


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
