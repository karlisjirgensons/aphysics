# -*- coding: utf-8 -*-
"""Fizika I tematu, PD un LD plāni - visiem stundu sarakstiem.

Saturs abām klasēm ir viens un tas pats (fiz_plan_10.py, fiz_plan_11.py);
atšķiras tikai grafiks, tāpēc no viena plāna sanāk vairāki dokumenti ar
saviem datumiem (fiz_plani.Grafiks).

    Ādaži     - trešdienās dubultstunda un piektdienās viena stunda;
    Carnikava - visas trīs stundas ceturtdienā.

Palaiž:  .venv/Scripts/python.exe _tools/gen_fiz_plani.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import fiz_plan_10                                       # noqa: E402
import fiz_plan_11                                       # noqa: E402
import fiz_plani as F                                    # noqa: E402
from fiz_plani import FIZIKA                             # noqa: E402

# (modulis, klases nosaukums, grafiks, faila vārds)
DOKUMENTI = [
    (fiz_plan_10, "10. klase", F.ADAZI,
     "Fizika I 10. klase - tematu, PD un LD plans_tt.docx"),
    (fiz_plan_11, "11. klase", F.ADAZI,
     "Fizika I 11. klase - tematu, PD un LD plans_tt.docx"),
    (fiz_plan_10, "10. klase (Carnikava)", F.CARNIKAVA,
     "10kl_Carnikava.docx"),
    (fiz_plan_11, "11. klase (Carnikava)", F.CARNIKAVA,
     "11kl_Carnikava.docx"),
]


def main():
    for modulis, klase, grafiks, vards in DOKUMENTI:
        cels = os.path.join(FIZIKA, vards)
        p = modulis.build(cels, grafiks, klase)
        print("%-22s %3d stundas, %2d vertejumi -> %s"
              % (klase, p.n, len(p.vertejumi), vards))
        for m in p.mainas:
            print("      UZMANIBU: %s" % m)
        for kods, tema, svars, datums, _ in p.vertejumi:
            print("      %-5s %-44s %2d %%  %s"
                  % (kods, tema[:44], svars, datums))
        print("")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
