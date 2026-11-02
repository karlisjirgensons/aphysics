# -*- coding: utf-8 -*-
"""Lapas vecākiem, angliski un latviski:

    calcubo.lv/parent   vecāku aptauja (vecaki_vietne)
    calcubo.lv/smart    cik labi zini bērna matemātiku (smart_vietne)

    python gen_vecaki.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import smart_vietne                                 # noqa: E402
import vecaki_vietne                                # noqa: E402
from courses import SITE_ROOT                       # noqa: E402


def main():
    for vietne in (vecaki_vietne, smart_vietne):
        for path in vietne.build():
            print("Vecākiem:  %s" % os.path.relpath(path, SITE_ROOT))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
