# -*- coding: utf-8 -*-
"""
Slaidos rakstīto aprēķinu izrēķināšana.

Uzdevuma solis latviešu pierakstā izskatās šādi:

    "3)  F_y = 200 · sin 60° = 200 · 0,87 = 173 N"

Šis modulis prot no tādas rindas izvilkt skaitliskās izteiksmes un tās
izrēķināt (SRP: te ir tikai rēķināšana; ko ar rezultātu darīt, izlemj
check_math.py). Tas vajadzīgs, lai pārbaudītu latviešu standarta prasību:
ja solī kaut kas noapaļots, rakstāms "≈", nevis "=".

Pieraksta īpatnības, ko saprot:
    12 345,6        atstarpe tūkstošos, komats aiz komata
    3,0·10⁻¹¹       pakāpes ar augšrakstiem
    a : b           dalījums ar kolu
    √(a + b), √25   kvadrātsakne
    sin 60°, tg α   trigonometrija grādos (α un citi burti - nezināmie)
    |a − b|         modulis
"""

import math
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import mathfmt as MF          # noqa: E402

_SUPER = "⁰¹²³⁴⁵⁶⁷⁸⁹"
_SUPER_MAP = {c: str(i) for i, c in enumerate(_SUPER)}
_SUPER_MAP["⁻"] = "-"
_SUPER_MAP["⁺"] = "+"

_FUNCS = {"sin": math.sin, "cos": math.cos, "tg": math.tan}

# rindas dalītāji: pēc tiem izteiksmes salīdzina savā starpā
# (atstarpes paliek gabalā, lai rindu var salikt atpakaļ nemainītu)
REL = re.compile(r"(\s*[=≈]\s*)")

# soļa numurs rindas sākumā ("3)  ") pie izteiksmes nepieder
_STEP_NO = re.compile(r"^\s*\d+\)\s*")
# mērvienība vai komentārs aiz skaitļa ("173 N", "2,4 s (bremzējot)")
_TAIL = re.compile(r"[\sA-Za-zĀ-žµΩ°%/·()⁰-⁹²³·,.]*$")


def _thousands(s):
    """Atstarpe tūkstošos: "12 345" -> "12345" (bet "2 · 3" nemainās)."""
    prev = None
    while prev != s:
        prev = s
        s = re.sub(r"(\d) (\d{3})(?!\d)", r"\1\2", s)
    return s


def _powers(s):
    """Augšraksti: "10⁻¹¹" -> "10**(-11)"."""
    def rep(m):
        return "**(%s)" % "".join(_SUPER_MAP[c] for c in m.group(0))
    return re.sub("[%s⁻⁺]+" % _SUPER, rep, s)


def _roots(s):
    """√(a + b) un √25 -> sqrt(...)."""
    out, i = [], 0
    while i < len(s):
        if s[i] != "√":
            out.append(s[i])
            i += 1
            continue
        j = i + 1
        while j < len(s) and s[j] == " ":
            j += 1
        if j < len(s) and s[j] == "(":
            depth, k = 0, j
            while k < len(s):
                if s[k] == "(":
                    depth += 1
                elif s[k] == ")":
                    depth -= 1
                    if depth == 0:
                        break
                k += 1
            out.append("sqrt" + s[j:k + 1])
            i = k + 1
        else:
            k = j
            while k < len(s) and (s[k].isdigit() or s[k] in ",.*()-+"):
                k += 1
            out.append("sqrt(%s)" % s[j:k])
            i = k
    return "".join(out)


def _abs_bars(s):
    """|a − b| -> abs(a - b); nepāra svītru gadījumā atstāj kā ir."""
    if s.count("|") % 2:
        return s
    parts = s.split("|")
    out = parts[0]
    for i in range(1, len(parts), 2):
        out += "abs(%s)" % parts[i] + (parts[i + 1]
                                       if i + 1 < len(parts) else "")
    return out


def _trig(s):
    """sin 60° -> sin(radians(60)); bez grādu zīmes izteiksmi noraida."""
    def rep(m):
        return "%s(radians(%s))" % (m.group(1), m.group(2))
    return re.sub(r"\b(sin|cos|tg)\s*([0-9.,]+)\s*°", rep, s)


def _colon_div(s):
    """"a · b : c" -> "(a · b)/(c)".

    Kols dala reizinājumu, kas tam priekšā - tāpat kā to lasa mathfmt,
    pārvēršot kolu vertikālā daļā (viens noteikums abiem, DRY). Bez
    iekavām Python "3,0·10⁸ : 9,0·10⁷" izrēķinātu kā (3·10⁸/9)·10⁷.
    """
    s = _inner_colons(s)
    depth = 0
    for i, ch in enumerate(s):
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        elif ch == ":" and depth == 0:
            a = MF.term_start(s, i)
            b = _den_end(s, i + 1)
            return (s[:a] + "(%s)/(%s)" % (s[a:i].strip(), s[i + 1:b].strip())
                    + _colon_div(s[b:]))
    return s


def _inner_colons(s):
    """Vispirms izlabo kolus iekavās: "√(1,80 : 9,8)"."""
    if ":" not in s:
        return s
    out, i, n = [], 0, len(s)
    while i < n:
        if s[i] != "(":
            out.append(s[i])
            i += 1
            continue
        depth, j = 0, i
        while j < n:
            if s[j] == "(":
                depth += 1
            elif s[j] == ")":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        if j >= n:                      # neaizvērta iekava - atstāj kā ir
            out.append(s[i:])
            break
        out.append("(" + _colon_div(s[i + 1:j]) + ")")
        i = j + 1
    return "".join(out)


_TENS = re.compile(r"[·×]\s*10\*\*")


def _den_end(s, start):
    """Kur beidzas saucējs: pie pirmās reizināšanas/saskaitīšanas zīmes.

    "·10**(6)" ir paša skaitļa daļa (standartforma), nevis jauns
    reizinātājs - citādi "4,0·10¹⁴ : 7,0·10⁶" dalītu tikai ar 7,0.
    """
    depth, i = 0, start
    while i < len(s):
        ch = s[i]
        m = _TENS.match(s, i) if depth == 0 else None
        if m:
            i = m.end()
            continue
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        elif depth == 0 and ch in "·×*+-:":
            return i
        i += 1
    return len(s)


def _clean(expr):
    """Latviešu pierakstu pārraksta par Python izteiksmi."""
    s = expr.strip()
    s = _STEP_NO.sub("", s)
    s = _thousands(s)
    s = s.replace("−", "-").replace("–", "-")
    s = _trig(s)
    s = _powers(s)
    s = _roots(s)
    s = _abs_bars(s)
    s = _colon_div(s)
    s = s.replace("·", "*").replace("×", "*")
    s = re.sub(r"(?<=\d),(?=\d)", ".", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


_ALLOWED = re.compile(r"^[0-9\s.+\-*/()]*$")
_NS = {"sqrt": math.sqrt, "abs": abs, "radians": math.radians,
       "sin": math.sin, "cos": math.cos, "tg": math.tan, "tan": math.tan}


def value(expr):
    """Izteiksmes skaitliskā vērtība vai None, ja tā nav tīrs aprēķins.

    Mērvienību un paskaidrojumu aiz skaitļa atmet ("173 N" -> 173), bet
    izteiksmi ar nezināmiem burtiem ("v = at") atgriež kā None.
    """
    s = _clean(expr)
    if not s:
        return None
    # Nogriež mērvienību vai komentāru aiz pēdējā skaitļa ("173 N",
    # "2,4 s (bremzējot)"). Atstarpe ir obligāta: "3t" ir reizinājums ar
    # nezināmo, nevis skaitlis ar mērvienību.
    m = re.match(r"^(.*?[0-9)])(?:\s+([A-Za-zĀ-žµΩ][^=≈]*))?$", s)
    if m:
        # Ja aiz mērvienības ir vēl viens skaitlis, tā vairs nav mērvienība,
        # bet salikts pieraksts ("1 h 17 min") - tādu neizrēķina, jo otrais
        # skaitlis pazustu. Pakāpes ("m/s²" -> "m/s**(2)") nav skaitļi.
        aste = re.sub(r"\*\*\(-?\d+\)", "", m.group(2) or "")
        if re.search(r"\d", aste):
            return None
        s = m.group(1)
    for fn in _FUNCS:
        s = s.replace(fn + "(radians(", "@%s@(radians(" % fn)
    if not _ALLOWED.match(re.sub(r"sqrt|abs|radians|@sin@|@cos@|@tg@", "", s)):
        return None
    if re.search(r"[0-9)]\s*\(", s.replace("**(", "")):
        return None                     # "210 (245)" - skaitlis un piebilde
    s = s.replace("@", "")
    try:
        v = eval(s, {"__builtins__": {}}, _NS)          # noqa: S307
    except Exception:
        return None
    return float(v) if isinstance(v, (int, float)) else None


_UNIT = re.compile("[0-9)" + _SUPER + "⁻⁺]"
                   r"\s*([A-Za-zĀ-žµΩ°%]+(?:/[A-Za-zĀ-žµΩ]+[²³]?)?[²³]?)\s*$")


def unit(expr):
    """Mērvienība aiz pēdējā skaitļa ("20 ms" -> "ms") vai ""."""
    m = _UNIT.search(expr.strip().rstrip(".,;"))
    return m.group(1) if m else ""


# Vienā solī mēdz būt divi patstāvīgi apgalvojumi ("F₁² = 1600 N² ;
# F₂² = 900 N²"), secinājums aiz bultas vai pretstats ("I ≈ 5,5 mA, nevis
# 5,5 A") - tos salīdzināt savā starpā nedrīkst.
STATEMENT = re.compile(r"(\s*[;→]\s*|,\s+nevis\s+)")


def statements(line):
    """Rindu sadala patstāvīgos apgalvojumos."""
    return [p for p in STATEMENT.split(line)[::2] if p.strip()]


def split_keep(line, pattern=REL):
    """Rinda gabalos, saglabājot atdalītājus ar atstarpēm.

    Dala tikai ārpus iekavām: piebilde "(mazāka par mg = 245 N)" ir
    komentārs, nevis vēl viens vienādojuma posms. Atdalītāji paliek
    sarakstā, lai labotājs (fix_math.py) varētu nomainīt vienu zīmi un
    pārējo rindu atstāt burtu burtā tādu pašu.
    """
    out, prev, depth = [], 0, 0
    for i, ch in enumerate(line):
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        elif depth == 0:
            m = pattern.match(line, i)
            if m and m.start() >= prev:
                out.append(line[prev:m.start()])
                out.append(m.group(0))
                prev = m.end()
    out.append(line[prev:])
    return out


def segments(line):
    """Rindu sadala pa "=" / "≈": [(zīme_pirms, izteiksme), ...]."""
    parts = split_keep(line)
    out = [("", parts[0])]
    for i in range(1, len(parts) - 1, 2):
        out.append((parts[i].strip(), parts[i + 1]))
    return out
