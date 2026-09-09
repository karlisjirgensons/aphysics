# -*- coding: utf-8 -*-
"""
Daļskaitļu (dalījumu) noformēšana pēc rules_lessons.txt:

    "When writing a fraction formatted as a/b, display it in standard
     vertical fraction notation (numerator a on top, denominator b below),
     rather than inline text."

Latviešu standartā mērvienības (m/s, kg/m³, N/m², W/(m·K)) NEPĀRVEIDO
vertikālā daļā - tās raksta rindā. Tāpēc šeit ir izšķiršana starp
"formulas dalījumu" un "mērvienību".

Galvenā funkcija:

    parse_math("σ = F / S        [σ] = Pa = N/m²")
      -> [('t', 'σ = '), ('f', 'F', 'S'), ('t', '        [σ] = Pa = N/m²')]

Atomu veidi:
    ("t", teksts)            - parasts teksts
    ("f", skaitītājs, saucējs) - vertikāla daļa

Papildus - precīzs teksta platuma mērījums ar īsto Calibri fontu
(vajadzīgs, lai daļas un teksts prezentācijā saliktos bez pārklāšanās).
"""

import os
import re

# ------------------------------------------------------------------ mērvienības
_SUPER = "⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺"
_SUB = "₀₁₂₃₄₅₆₇₈₉"
_DIGITS = "0123456789" + _SUPER

# atdala vairākas formulas vienā rindā (2+ atstarpes)
_CHUNK = re.compile(r"(\s{2,})")
# atdala formulas daļas pie vienādības/bultas zīmēm
_REL = re.compile(r"(\s*(?:=|≈|→|<|>|≤|≥)\s*)")


_UNITS = set("""
m s kg g mg t N J W Pa K A V C mol h min km cm mm dm nm L l Hz T Bq Sv Gy
eV rad lx lm cd MPa GPa kPa hPa kW MW mW kJ MJ kWh mA kA mV kV kΩ MΩ Ω
µm µs ms µA ns Wb mSv mGy kN MN
m² m³ cm² cm³ mm² mm³ dm³ km² s² s³ °C °F ° % ppm dB
""".split())

_BASES = set("""m s g N J W Pa K A V C mol L l Hz T Bq Sv Gy eV cd lm lx Wb
F H rad h min t bar Wh Ah B EUR Ohm""".split())
_PREFIX = ("da", "k", "M", "G", "T", "P", "m", "µ", "μ", "n", "p",
           "c", "d", "h", "E")


def _base_unit(p):
    """Vai marķieris ir mērvienība arī ar SI priedēkli: µSv, kWh, MPa."""
    p = p.rstrip("²³")
    if p in _UNITS or p in _BASES:
        return True
    for pre in _PREFIX:
        if p.startswith(pre) and p[len(pre):] in _BASES:
            return True
    return False


def _has_bracket_unit(chunk):
    """[p] = Pa = N/m²  -> mērvienību pieraksts, nevis formula."""
    return "[" in chunk and "]" in chunk


def _split_slash(part):
    """Atrod pirmo dalījuma slīpsvītru ārpus iekavām."""
    depth = 0
    for i, ch in enumerate(part):
        if ch in "([":
            depth += 1
        elif ch in ")]":
            depth = max(0, depth - 1)
        elif ch == "/" and depth == 0:
            return i
    return -1


_NUM_PAREN = re.compile(r"^\(\s*[0-9,.\s±+\-−]*[0-9][0-9,.\s±+\-−]*\)$")


def _numeric_paren(part, close):
    """Vai part beidzas ar skaitlisku iekavu, piem. "(3,0 ± 0,2)"?"""
    depth = 0
    for i in range(close, -1, -1):
        if part[i] == ")":
            depth += 1
        elif part[i] == "(":
            depth -= 1
            if depth == 0:
                return bool(_NUM_PAREN.match(part[i:close + 1]))
    return False


def _preceded_by_number(part, i):
    """Vai pirms slīpsvītras ir skaitļa mērvienība?

    "2700 kg/m³", "9,81 m/s²", "3 · 10⁸ m/s"        -> True (mērvienība)
    "1 kg · m/s²", "6,67·10⁻¹¹ N·m²/kg²"            -> True (salikta)
    "(3,0 ± 0,2) m/s"                               -> True (mērījums)
    "F / S", "m/V", "1/T", "2π/T", "(2k + 1)λ/2"    -> False (formulas daļa)

    Simbolu ķēdi (kg·m, N·m²) skenē atpakaļ pa punktiem. Par mērvienību to
    atzīst tikai tad, ja ķēdes priekšā ir skaitlis vai skaitliska iekava UN
    visi ķēdes simboli ir īstas mērvienības - citādi "2π/T" izskatītos pēc
    mērvienības, lai gan tā ir formulas daļa.
    """
    j = i
    while j > 0 and part[j - 1] == " ":
        j -= 1
    syms = []
    while True:
        k = j
        while k > 0 and (part[k - 1].isalpha() or part[k - 1] in _SUPER + _SUB):
            k -= 1
        if k == j:                      # pirms slīpsvītras nav burtu
            return False
        syms.append(part[k:j])
        m = k
        while m > 0 and part[m - 1] == " ":
            m -= 1
        if m == 0:
            return False
        if part[m - 1] in _DIGITS:                  # "9,81 m", "10⁻¹¹ N·m²"
            break
        if part[m - 1] == ")" and m < k and _numeric_paren(part, m - 1):
            break                                   # "(3,0 ± 0,2) m/s"
        if part[m - 1] in "·×":                     # salikta mērvienība
            j = m - 1
            while j > 0 and part[j - 1] == " ":
                j -= 1
            continue
        return False
    return all(_base_unit(s) for s in syms)


# reizinājuma/saskaitīšanas zīmes, kas beidz saucēju:  a / b · c  =  (a/b)·c
# ("-" arī beidz saucēju: "Ek = mv²/2 - skalārs" -> saucējs ir tikai "2")
_STOP = "·×*+−-:;,"
# teikuma pieturzīmes, kas nepieder saucējam: "f = 1/T." -> saucējs "T"
_DEN_TRAIL = ".,;:!?"


def _den_end(part, start):
    """Kur beidzas saucējs: pie pirmās reizināšanas/saskaitīšanas zīmes."""
    depth = 0
    for i in range(start, len(part)):
        ch = part[i]
        if ch in "([":
            depth += 1
        elif ch in ")]":
            depth = max(0, depth - 1)
        elif depth == 0 and ch in _STOP:
            return i
    return len(part)


def _strip_outer(s):
    """(v − v₀) -> v − v₀, ja iekavas aptver visu izteiksmi."""
    s = s.strip()
    while len(s) > 1 and s[0] == "(" and s[-1] == ")":
        depth = 0
        for i, ch in enumerate(s):
            if ch == "(":
                depth += 1
            elif ch == ")":
                depth -= 1
                if depth == 0 and i != len(s) - 1:
                    return s
        s = s[1:-1].strip()
    return s


def _atoms_from_part(part):
    i = _split_slash(part)
    if i < 0 or _preceded_by_number(part, i):
        return [("t", part)]
    end = _den_end(part, i + 1)
    num = part[:i].strip()
    den = part[i + 1:end].strip()
    tail = part[end:]
    trail = ""
    while den and den[-1] in _DEN_TRAIL:        # punkts paliek tekstā
        trail = den[-1] + trail
        den = den[:-1].rstrip()
    tail = trail + tail
    if not num or not den:
        return [("t", part)]
    # saglabā ievadošo atstarpi, lai teksts nesalīp
    lead = part[:len(part) - len(part.lstrip())]
    out = []
    if lead:
        out.append(("t", lead))
    out.append(("f", _strip_outer(num), _strip_outer(den)))
    if tail:
        if not tail[:1].isspace() and tail[:1] not in _DEN_TRAIL:
            tail = " " + tail
        out.extend(_atoms_from_part(tail))
    return out


# ---------------------------------------------------------------------- saknes
# rules_lessons.txt: "√(a + b)" - zem saknes zīmes jābūt VISAI izteiksmei.
# Tāpēc sakni glabā atsevišķā atomā ("r", izteiksme); zīmētājs tai pāri velk
# vinkulu (horizontālu svītru), nevis paļaujas uz iekavām.

ROOT_SIGN = "√"


def _root_span(text, i):
    """Kur sākas un beidzas √-izteiksme, ja saknes zīme ir pozīcijā i."""
    j = i + 1
    while j < len(text) and text[j] == " ":
        j += 1
    if j < len(text) and text[j] == "(":            # √(a + b) - visa iekava
        depth = 0
        for k in range(j, len(text)):
            if text[k] == "(":
                depth += 1
            elif text[k] == ")":
                depth -= 1
                if depth == 0:
                    return j, k + 1
        return j, len(text)
    k = j                                            # √25, √2500, √h
    while k < len(text) and (text[k].isalnum()
                             or text[k] in _SUB + _SUPER
                             or text[k] in ",."):
        k += 1
    return j, k


def split_roots(atoms):
    """Teksta atomos atdala √-izteiksmes kā ("r", izteiksme)."""
    out = []
    for a in atoms:
        if a[0] != "t" or ROOT_SIGN not in a[1]:
            out.append(a)
            continue
        s, pos = a[1], 0
        while True:
            i = s.find(ROOT_SIGN, pos)
            if i < 0:
                break
            b, e = _root_span(s, i)
            if e <= b:                      # tukša sakne - atstāj tekstā
                pos = i + 1
                continue
            if i > pos:
                out.append(("t", s[pos:i]))
            out.append(("r", _strip_outer(s[b:e])))
            pos = e
        if pos < len(s):
            out.append(("t", s[pos:]))
    return out


def parse_math(text):
    """Sadala tekstu atomos; ja daļu nav, atgriež vienu ("t", text)."""
    atoms = []
    for chunk in _CHUNK.split(text):
        if not chunk:
            continue
        if chunk.isspace() or _has_bracket_unit(chunk):
            atoms.append(("t", chunk))
            continue
        for part in _REL.split(chunk):
            if not part:
                continue
            if re.fullmatch(r"\s*(?:=|≈|→|<|>|≤|≥)\s*", part):
                atoms.append(("t", part))
            else:
                atoms.extend(_atoms_from_part(part))
    # sapludina blakus esošos teksta atomus
    merged = []
    for a in atoms:
        if a[0] == "t" and merged and merged[-1][0] == "t":
            merged[-1] = ("t", merged[-1][1] + a[1])
        else:
            merged.append(a)
    return split_roots(merged)


def has_fraction(text):
    return any(a[0] == "f" for a in parse_math(text))


def has_math(text):
    """Vai rinda jāzīmē ar formulu dzinēju - ir daļa vai sakne."""
    return any(a[0] in ("f", "r") for a in parse_math(text))


# ------------------------------------------------------------ teksta mērīšana
_FONTS = {}
_REF = 200.0        # mēra pie 200 px un pārrēķina uz vajadzīgo izmēru


def _font(bold, italic):
    key = (bool(bold), bool(italic))
    if key in _FONTS:
        return _FONTS[key]
    name = {(False, False): "calibri.ttf", (True, False): "calibrib.ttf",
            (False, True): "calibrii.ttf", (True, True): "calibriz.ttf"}[key]
    f = None
    try:
        from PIL import ImageFont
        for base in (os.environ.get("WINDIR", "C:/Windows") + "/Fonts",
                     "C:/Windows/Fonts"):
            p = os.path.join(base, name)
            if os.path.exists(p):
                f = ImageFont.truetype(p, int(_REF))
                break
    except Exception:
        f = None
    _FONTS[key] = f
    return f


def text_w(s, size_pt, bold=False, italic=False):
    """Teksta platums punktos pie dotā fonta izmēra."""
    if not s:
        return 0.0
    f = _font(bold, italic)
    if f is None:                                  # rezerves novērtējums
        return len(s) * size_pt * 0.50
    return f.getlength(s) * size_pt / _REF


