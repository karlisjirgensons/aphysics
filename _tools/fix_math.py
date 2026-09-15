# -*- coding: utf-8 -*-
"""
Izlabo zīmi uzdevumu soļos: "=" <-> "≈".

check_math.py atrod vietas, kur zīme starp soļa pusēm nav godīga -
noapaļots solis ar vienādības zīmi vai nepelnīts "≈" tur, kur puses ir
precīzi vienādas. Lēmumu abos virzienos pieņem risinajums.py (viens
noteikumu īpašnieks, DRY); šis rīks to pašu laboto rindu tikai ieraksta
avota failā - nomaina zīmes un pārējo rindu atstāj burtu burtā tādu pašu.

Palaiž:  .venv/Scripts/python.exe _tools/fix_math.py --dry
         .venv/Scripts/python.exe _tools/fix_math.py
         .venv/Scripts/python.exe _tools/fix_math.py fiz_t06a
"""

import ast
import importlib
import io
import os
import sys
import tokenize

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")

import check_math as C          # noqa: E402
import risinajums as R          # noqa: E402

TOOLS = os.path.dirname(os.path.abspath(__file__))

# ------------------------------------------------- rinda avota failā
# Gara soļa rinda avotā bieži ir sadalīta vairākās virknēs:
#     "3)  M = 9,8 · 4,10·10¹³ : "
#     "6,67·10⁻¹¹ = 6,02·10²⁴ kg"
# Tāpēc rindu avotā meklē nevis pēc teksta, bet pēc blakus esošām
# virknēm - tad zīme nomainās tieši tur, kur vajag, un pārējais fails
# paliek burtu burtā tāds pats.


def _offsets(src):
    """Rindas sākuma pozīcija failā (tokenize dod rindu un kolonnu)."""
    poz, n = [0], 0
    for rinda in src.splitlines(True):
        n += len(rinda)
        poz.append(n)
    return poz


def string_groups(src):
    """[(vērtība, [(sākums, beigas, literālis), ...]), ...]."""
    poz = _offsets(src)
    grupas, kārtējā = [], []
    for t in tokenize.generate_tokens(io.StringIO(src).readline):
        if t.type == tokenize.STRING:
            kārtējā.append((poz[t.start[0] - 1] + t.start[1],
                            poz[t.end[0] - 1] + t.end[1], t.string))
        elif t.type in (tokenize.NL, tokenize.NEWLINE, tokenize.COMMENT,
                        tokenize.INDENT, tokenize.DEDENT):
            continue
        elif kārtējā:
            grupas.append(("".join(ast.literal_eval(x[2]) for x in kārtējā),
                           kārtējā))
            kārtējā = []
    if kārtējā:
        grupas.append(("".join(ast.literal_eval(x[2]) for x in kārtējā),
                       kārtējā))
    return grupas


def _parrakstit(lit, teksts, jauns):
    """Virknes literālis ar jaunu saturu; None, ja to nedrīkst aiztikt."""
    if "\\" in lit or lit[0] not in "\"'":
        return None
    return lit[0] + jauns + lit[0]


def replace_string(src, vecais, jaunais):
    """Nomaina zīmes vienā virknē; None, ja rindu neizdodas atrast.

    Labojums vienmēr ir viena rakstzīme pret vienu ("=" pret "≈"), tāpēc
    garums nemainās, gabalu robežas paliek tur pat un pārējais teksts -
    neskarts. Gabalus aizvieto no beigām uz sākumu, lai nenobīdītos vēl
    neaizvietoto gabalu pozīcijas failā.
    """
    if len(vecais) != len(jaunais):
        return None
    if vecais == jaunais:
        return src
    for vērtība, gabali in string_groups(src):
        if vērtība != vecais:
            continue
        jaunie, sākts = [], 0
        for a, b, lit in gabali:
            teksts = ast.literal_eval(lit)
            gals = sākts + len(teksts)
            jauns = _parrakstit(lit, teksts, jaunais[sākts:gals])
            if jauns is None:
                return None
            jaunie.append((a, b, jauns))
            sākts = gals
        for a, b, jauns in reversed(jaunie):
            src = src[:a] + jauns + src[b:]
        return src
    return None


def fix_task(u):
    """[(vecā rinda, labotā rinda), ...] vienam uzdevumam."""
    labojumi = []
    for p in R.parbaudit(u):
        if p.labota != p.rinda and (p.rinda, p.labota) not in labojumi:
            labojumi.append((p.rinda, p.labota))
    return labojumi


def main(argv):
    dry = "--dry" in argv
    names = C.moduli([a for a in argv if not a.startswith("-")])
    kopa = 0
    for name in names:
        path = os.path.join(TOOLS, name + ".py")
        src = io.open(path, encoding="utf-8").read()
        m = importlib.import_module(name)
        changed = 0
        for st in m.STUNDAS:
            for u in st.get("uzdevumi", []):
                for veca, labota in fix_task(u):
                    jauns = replace_string(src, veca, labota)
                    if jauns is None:
                        print("  ! nevar atrast avotā: %s" % veca)
                        continue
                    src = jauns
                    changed += 1
                    print("  %s -> %s" % (veca, labota))
        if changed and not dry:
            io.open(path, "w", encoding="utf-8").write(src)
        kopa += changed
        if changed:
            print("%s: %d rindas%s" % (name, changed,
                                       " (izmēģinājums)" if dry else ""))
    print("\nLabotas %d rindas." % kopa)
    return kopa


if __name__ == "__main__":
    main(sys.argv[1:])
