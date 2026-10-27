# -*- coding: utf-8 -*-
"""Dienas izaicinājuma (calcubo.lv/play) būvētājs - angliski un latviski.

    python gen_play.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import play_vietne                                  # noqa: E402
from courses import SITE_ROOT                       # noqa: E402


def main():
    for path in play_vietne.build():
        print("Play:  %s" % os.path.relpath(path, SITE_ROOT))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
