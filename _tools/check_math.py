# -*- coding: utf-8 -*-
"""
Pārbauda uzdevumu risinājumu pierakstu pēc latviešu standarta.

Ko meklē:
  · noapaļots solis ar "=" - ja izteiksmes vērtība un pierakstītais
    rezultāts nesakrīt, starp tiem jābūt "≈";
  · nepelnīts "≈" - ja abas puses ir precīzi vienādas (arī tad, ja
    mainās mērvienība: "0,0375 m = 37,5 mm"), rakstāma vienādības zīme;
  · rupja kļūda - puses atšķiras vairāk nekā par 5 %.

Zīmes noteikumu zina risinajums.py; šis skripts tikai apstaigā stundu
moduļus un izdrukā atrasto (SRP), tāpat kā check_formulas.py dara ar
formulām. Labo ar fix_math.py, kas lieto to pašu noteikumu (DRY).

Palaiž:  .venv/Scripts/python.exe _tools/check_math.py
         .venv/Scripts/python.exe _tools/check_math.py fiz_t06a
"""

import glob
import importlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")

import risinajums as R          # noqa: E402

TOOLS = os.path.dirname(os.path.abspath(__file__))


def moduli(argv):
    if argv:
        return list(argv)
    return sorted(os.path.splitext(os.path.basename(f))[0]
                  for f in glob.glob(os.path.join(TOOLS,
                                                  "fiz_t[0-9][0-9]*.py")))


def main(argv):
    kopa = 0
    for name in moduli(argv):
        m = importlib.import_module(name)
        for st in m.STUNDAS:
            for u in st.get("uzdevumi", []):
                piez = R.parbaudit(u)
                if not piez:
                    continue
                print("\n%s  %s. %s  ·  %d. uzdevums"
                      % (name, st["nr"], st["virsraksts"], u["nr"]))
                for p in piez:
                    print("   [%s] %s" % (p.veids, p.apraksts))
                    kopa += 1
    print("\nKopā piezīmju: %d" % kopa)
    return kopa


if __name__ == "__main__":
    main(sys.argv[1:])
