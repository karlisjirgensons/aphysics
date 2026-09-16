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


def _preceded_by_number(part, i, spaced_units=False):
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
            # Zem saknes zīmes "2h" ir divi reizinātāji, nevis 2 stundas;
            # īstā mērvienība no skaitļa vienmēr atdalīta ar atstarpi.
            if spaced_units and m == k:
                return False
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


def _decimal_comma(part, i):
    """Vai komats ir skaitļa decimāldaļa (9,8), nevis atdalītājs?"""
    return (0 < i < len(part) - 1
            and part[i - 1].isdigit() and part[i + 1].isdigit())


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
            if ch == "," and _decimal_comma(part, i):
                continue                     # "9,8" ir viens skaitlis
            return i
    return len(part)


# saskaitīšanas zīmes, kas beidz skaitītāju: "13,9 + 193/13,7" nozīmē
# 13,9 plus daļa, nevis (13,9 + 193) dalīts ar 13,7
_ADD = "+−-"


def term_start(part, i):
    """Kur sākas reizinājums, kas beidzas pozīcijā i.

    Dalījums saista ciešāk par saskaitīšanu, tāpēc skaitītājs ir tikai
    pēdējais loceklis. Zīme izteiksmes sākumā ("−625/(−10)") ir skaitļa
    zīme, nevis atņemšana, tāpēc pie tās neapstājas.
    """
    depth = 0
    for k in range(i - 1, -1, -1):
        ch = part[k]
        if ch in ")]":
            depth += 1
        elif ch in "([":
            depth = max(0, depth - 1)
        elif depth == 0 and ch in _ADD and part[:k].strip():
            k += 1
            while k < i and part[k] == " ":
                k += 1
            return k
    return 0


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


def _atoms_from_part(part, spaced_units=False):
    i = _split_slash(part)
    if i < 0 or _preceded_by_number(part, i, spaced_units):
        return [("t", part)]
    end = _den_end(part, i + 1)
    start = term_start(part, i)
    num = part[start:i].strip()
    den = part[i + 1:end].strip()
    tail = part[end:]
    trail = ""
    while den and den[-1] in _DEN_TRAIL:        # punkts paliek tekstā
        trail = den[-1] + trail
        den = den[:-1].rstrip()
    tail = trail + tail
    if not num or not den:
        return [("t", part)]
    # viss, kas bija pirms skaitītāja ("13,9 + "), paliek tekstā
    lead = part[:start]
    out = []
    if lead:
        out.append(("t", lead))
    out.append(("f", _strip_outer(num), _strip_outer(den)))
    if tail:
        if not tail[:1].isspace() and tail[:1] not in _DEN_TRAIL:
            tail = " " + tail
        out.extend(_atoms_from_part(tail, spaced_units))
    return out


# --------------------------------------------------------- dalījums ar kolu
# Latviešu skolas pierakstā dalījumu bieži raksta ar kolu: "60 : 30 = 2,0".
# rules_lessons.txt prasa to rādīt kā vertikālu daļu, tāpēc pirms atomu
# meklēšanas kolu pārraksta par slīpsvītru - bet TIKAI tur, kur tas tiešām
# ir dalījums. Attiecība ("attiecas kā 1 : 3 : 5", "attiecība 4 : 1") paliek
# rindā: tur nekas netiek dalīts.

_RATIO_CHARS = set("0123456789 ,.·×" + _SUPER + _SUB)
_RATIO_REL = "=≈<>≤≥"


def _depth_at(text, i):
    """Iekavu dziļums pozīcijā i.

    Iekavas skaita, nevis salīdzina to skaitu - soļa numurs "1)" ir
    nepāra iekava, kas citādi visu rindu padarītu par "iekavās esošu".
    """
    depth = 0
    for ch in text[:i]:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
    return depth


def _group_left(text, j):
    """Ja pirms j ir aizverošā iekava, atgriež visas grupas sākumu."""
    depth = 0
    for k in range(j - 1, -1, -1):
        if text[k] == ")":
            depth += 1
        elif text[k] == "(":
            depth -= 1
            if depth == 0:
                return k
    return None


def _group_right(text, j):
    """Ja text[j] ir atverošā iekava, atgriež grupas beigas."""
    depth = 0
    for k in range(j, len(text)):
        if text[k] == "(":
            depth += 1
        elif text[k] == ")":
            depth -= 1
            if depth == 0:
                return k + 1
    return None


def _ratio_left(text, i):
    """Skaitītājs pa kreisi no kola; (sākums, beigas) vai None."""
    j = i
    while j > 0 and text[j - 1] == " ":
        j -= 1
    if j > 0 and text[j - 1] == ")":
        k = _group_left(text, j)
        return (k, j) if k is not None else None
    k = j
    while k > 0 and text[k - 1] in _RATIO_CHARS:
        k -= 1
    while k < j and text[k] == " ":
        k += 1
    return (k, j) if k < j and any(c.isdigit() for c in text[k:j]) else None


def _sci_factor(text, i):
    """Vai reizinājuma zīme pozīcijā i ir daļa no standartformas?

    "6,0 · 10⁻⁴" ir VIENS skaitlis, tāpēc saucējā tas paliek veselums.
    "25,0 · 100 %" turpretī ir reizinājums AIZ dalījuma - tas saucējā
    neietilpst, citādi 0,1 : 25,0 · 100 % pārtaptu par 0,1/(25,0 · 100).
    """
    k = i + 1
    while k < len(text) and text[k] == " ":
        k += 1
    return (text[k:k + 2] == "10" and k + 2 < len(text)
            and text[k + 2] in _SUPER)


def _ratio_right(text, i):
    """Saucējs pa labi no kola; (sākums, beigas) vai None."""
    j = i + 1
    while j < len(text) and text[j] == " ":
        j += 1
    if j < len(text) and text[j] == "(":
        k = _group_right(text, j)
        return (j, k) if k is not None else None
    k = j
    while k < len(text) and text[k] in _RATIO_CHARS:
        if text[k] in "·×" and not _sci_factor(text, k):
            break
        k += 1
    while k > j and text[k - 1] == " ":
        k -= 1
    return (j, k) if k > j and any(c.isdigit() for c in text[j:k]) else None


def _is_division(text, lo, hi, num, den):
    """Vai "a : b" ir dalījums (nevis attiecība)?

    Dalījumu pazīst pēc tā, ka tas ir vienādojumā: vai nu tūlīt aiz
    vienādības zīmes ("N = 1440 : 118"), vai aiz kola seko rezultāts
    ("9 : 24 = 0,375"), vai abi lielumi ir iekavās ("(1,67 kg) : (9,1 kg)")
    - attiecību tā neraksta.
    """
    after = text[hi:]
    if after.lstrip().startswith(":"):          # ķēde 1 : 3 : 5 - attiecība
        return False
    if num.startswith("(") and den.startswith("("):
        return True
    return (text[:lo].rstrip().endswith("=")
            or any(c in _RATIO_REL for c in after))


def ratio_slash(text):
    """Dalījuma kolus pārraksta par slīpsvītrām; attiecības neaiztiek."""
    if " : " not in text:
        return text
    out, pos, i = [], 0, 0
    while True:
        i = text.find(" : ", i)
        if i < 0:
            break
        i += 1                                   # kols
        if i < pos or _depth_at(text, i):
            i += 1
            continue
        left, right = _ratio_left(text, i), _ratio_right(text, i)
        if not left or not right:
            i += 1
            continue
        num, den = text[left[0]:left[1]], text[right[0]:right[1]]
        if not _is_division(text, left[0], right[1], num, den):
            i += 1
            continue
        if not den.startswith("(") and any(c in den for c in "·×"):
            den = "(%s)" % den               # saucējs reizinājums: 6,0·10⁻⁴
        out.append(text[pos:left[0]])
        out.append("%s/%s" % (num, den))
        pos = i = right[1]
    out.append(text[pos:])
    return "".join(out)


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


def root_atoms(expr):
    """Atomi zem saknes zīmes.

    Zem vinkula slīpsvītra vienmēr ir dalījums (mērvienības tur neraksta),
    tāpēc te der agresīvā atpazīšana - arī tad, ja pārējo rindu lasa
    piesardzīgi (mathfmt_prose).
    """
    return _atoms_from_part(_strip_outer(expr), spaced_units=True)


def has_root_fraction(atom):
    """Vai ("r", atomi) satur vertikālu daļu?"""
    return atom[0] == "r" and any(a[0] == "f" for a in atom[1])


def split_roots(atoms):
    """Teksta atomos atdala √-izteiksmes kā ("r", [apakšatomi])."""
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
            out.append(("r", root_atoms(s[b:e])))
            pos = e
        if pos < len(s):
            out.append(("t", s[pos:]))
    return out


def with_ratio(text, build):
    """Nolasa rindu, kolu dalījumu ("60 : 30") pieņemot par daļu.

    Ja pārrakstītā rinda tomēr nedod daļu, atgriež sākotnējo lasījumu -
    tā kols nekad nepaliek redzams kā slīpsvītra. Šo palīgu lieto abi
    parsētāji (DRY), tāpēc noteikums ir viens un tas pats.
    """
    alt = ratio_slash(text)
    if alt != text:
        atoms = build(alt)
        if any(a[0] == "f" for a in atoms):
            return atoms
    return build(text)


def parse_math(text):
    """Sadala tekstu atomos; ja daļu nav, atgriež vienu ("t", text)."""
    return with_ratio(text, _parse_math)


def _parse_math(text):
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


def _plain_w(s, size_pt, bold=False, italic=False):
    """Viena parasta teksta gabala platums punktos."""
    if not s:
        return 0.0
    f = _font(bold, italic)
    if f is None:                                  # rezerves novērtējums
        return len(s) * size_pt * 0.50
    return f.getlength(s) * size_pt / _REF


def text_w(s, size_pt, bold=False, italic=False):
    """Teksta platums punktos pie dotā fonta izmēra.

    Mēra pa gabaliem, jo indeksu (F_y) raksta mazākā fontā, bet vektora
    bultiņa ir kombinējošā zīme - tā stāv virs burta un platumu
    nepievieno; fontā tās parasti nav, tāpēc mērīšanai to izlaiž.
    """
    total = 0.0
    for kind, chunk in split_runs(s):
        k = SUB_SIZE if kind == "s" else 1.0
        total += _plain_w(chunk, size_pt * k, bold, italic)
    return total




# --------------------------------------------------------------------- vektori
# Vektoru apzīmē ar bultiņu virs simbola. Unikoda kombinējošā bultiņa
# (U+20D7) lielākajā daļā fontu vai nu iztrūkst pavisam (Calibri, Inter,
# Arial), vai nenostājas virs burta - tāpēc zīmētāji bultiņu zīmē paši.
# Šis modulis atbild tikai par atpazīšanu; kā to attēlot, izlemj zīmētājs.

VEC_MARK = "⃗"


def has_vector(text):
    return bool(text) and VEC_MARK in text


# --------------------------------------------------------------- indeksi
# Latviešu standartā indeksu raksta mazāku un zem pamatlīnijas: Rz, vvid,
# Fb. Unikodā apakšindeksa burtu "y" nav (ir tikai ₓ, ₐ, ₙ ...), tāpēc
# avotā indeksu raksta vienā no trim veidiem - visi nozīmē vienu un to
# pašu, un visi te tiek pārvērsti par īstu apakšindeksu:
#
#     F_y, N_A          viena zīme aiz pasvītrojuma
#     F_{max}           vairākas zīmes figūriekavās
#     R(Z), v(vid)      indekss iekavās aiz viena simbola
#
# Šis modulis ir vienīgā vieta, kas izšķir, kas ir indekss (SRP); slaidu,
# lapas un platuma mērītājs to visi uzzina caur split_runs() (DRY), tāpēc
# pieraksts izskatās vienādi virsrakstos, kartītēs, tabulās un formulās.

SUB_MARK = "_"
SUB_OPEN, SUB_CLOSE = "{", "}"
SUB_SIZE = 0.62                 # indeksa fonta izmērs (pamata daļās)
_ASCII_ALNUM = set("0123456789abcdefghijklmnopqrstuvwxyz"
                   "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

# Simbols, kam drīkst būt indekss: viens latīņu, grieķu vai latviešu burts.
_SYMBOL = re.compile(r"[^\W\d_]", re.UNICODE)
# Zīmes, kas stāv simbola priekšā, bet nav tā daļa: "ΣE(dienā)", "Δt(vid)".
_PREFIKSI = set("ΣΔ∑∆Π∏")
# Indeksa saturs: tikai burti un cipari, bez atstarpēm un darbības zīmēm,
# citādi par indeksu kļūtu arī "(R + h)" un "(3,0 ± 0,2)".
_SUB_BODY = re.compile(r"[^\W_]{1,12}\Z", re.UNICODE)

# Iekavās ne vienmēr ir indekss - fizikā tāpat pieraksta grafiku un
# raksturlīkņu funkcijas: "v(t) grafiks", "I(U) raksturlīkne". Tās uzskaita
# šeit, jo pēc formas tās no indeksa neatšķiras: x(m) ir amplitūda (indekss),
# x(t) ir koordināta atkarībā no laika (funkcija).
FUNKCIJAS = frozenset("""
x(t) v(t) a(t) s(t) T(t) x(l)
F(x) f(x) y(x) d(x)
I(U) U(I) m(V) p(V) V(p) p(T) V(T)
g(h) v(h) v(r) F(r) T(r)
""".split())


def _is_sub(text, i):
    """Vai text[i] ir indeksa pasvītrojums, nevis faila vārda daļa?

    Indekss ir viena zīme ("F_y", "N_A") vai figūriekavās ("F_{max}");
    "gen_fiz", "projekcijas_tt" - nav indekss.
    """
    if text[i] != SUB_MARK or i == 0 or text[i - 1] in " 	":
        return False
    if text[i + 1:i + 2] == SUB_OPEN:
        return _sub_brace_end(text, i) > 0
    nxt = text[i + 1] if i + 1 < len(text) else ""
    nxt2 = text[i + 2] if i + 2 < len(text) else ""
    return nxt in _ASCII_ALNUM and nxt2 not in _ASCII_ALNUM


def _sub_brace_end(text, i):
    """"F_{max}": aizverošās figūriekavas vieta vai 0, ja indeksa nav."""
    close = text.find(SUB_CLOSE, i + 2)
    if close < 0:
        return 0
    return close if _SUB_BODY.match(text[i + 2:close]) else 0


def _sub_paren_end(text, i):
    """"R(Z)": aizverošās iekavas vieta vai 0, ja tur nav indeksa.

    Indekss ir tikai aiz VIENA burta ("R(Z)", "v(vid)") - tā "cos(x)",
    "W/(m·K)" un "(3 · 10⁻⁵ m)" paliek neskarti. Skaitlis iekavās ir
    funkcijas vērtība ("x(3) = 1,0 m"), nevis indekss; ciparu indeksu
    raksta ar pasvītrojumu vai Unikodu: "V_1", "V₁".
    """
    if text[i] != "(" or i == 0 or not _SYMBOL.match(text[i - 1]):
        return 0
    if i > 1 and text[i - 2] not in _PREFIKSI and (
            _SYMBOL.match(text[i - 2]) or text[i - 2] in _ASCII_ALNUM):
        return 0
    close = text.find(")", i + 1)
    if close < 0:
        return 0
    body = text[i + 1:close]
    if not _SUB_BODY.match(body) or body.isdigit():
        return 0
    return 0 if text[i - 1] + "(" + body + ")" in FUNKCIJAS else close


def has_index(text):
    """Vai tekstā ir kāds indeksa pieraksts? (ātrais ceļš zīmētājiem)"""
    return bool(text) and (SUB_MARK in text or "(" in text)


def has_markup(text):
    """Vai tekstu drīkst rakstīt kā vienu gabalu, bez split_runs()?"""
    return has_vector(text) or has_index(text)


def split_runs(text):
    """Tekstu sadala gabalos, ko attēlo atšķirīgi.

        ("t", teksts)   - parasts teksts
        ("v", simbols)  - vektors (bultiņa virs simbola)
        ("s", zīme)     - apakšindekss

        "|Δv⃗| = 16"  ->  [('t','|Δ'), ('v','v'), ('t','| = 16')]
        "F_y = 12"    ->  [('t','F'), ('s','y'), ('t',' = 12')]
        "R(Z) = 6,4"  ->  [('t','R'), ('s','Z'), ('t',' = 6,4')]
    """
    out, buf = [], []

    def flush():
        if buf:
            out.append(("t", "".join(buf)))
            del buf[:]

    i, n = 0, len(text)
    while i < n:
        if i + 1 < n and text[i + 1] == VEC_MARK:
            flush()
            out.append(("v", text[i]))
            i += 2
            continue
        if _is_sub(text, i):
            flush()
            if text[i + 1] == SUB_OPEN:
                close = _sub_brace_end(text, i)
                out.append(("s", text[i + 2:close]))
                i = close + 1
            else:
                out.append(("s", text[i + 1]))
                i += 2
            continue
        close = _sub_paren_end(text, i)
        if close:
            flush()
            out.append(("s", text[i + 1:close]))
            i = close + 1
            continue
        if text[i] != VEC_MARK:             # bultiņa bez bāzes - izlaiž
            buf.append(text[i])
        i += 1
    flush()
    return out


def split_vectors(text):
    """Novecojis vārds - sk. split_runs()."""
    return split_runs(text)


# ------------------------------------------------------------- saknes zīme
# Saknes zīmi zīmē kā daudzstūri, nevis kā fonta glifu: fonta √ ir tikai
# vienas rindas augstumā, tāpēc pie kāpinātājiem (F₁² + F₂²) tā paliek par
# zemu un vinkuls no tās atraujas. Punkti ir kopīgi .pptx un HTML zīmētājam
# (DRY): x mērogs 0..ROOT_VB[0], y mērogs 0..ROOT_VB[1], y aug uz leju.

# ---------------------------------------------------- formulas izmēri
# Visi mēri ir fonta izmēra daļās ("em"), tāpēc der gan slaidam, gan lapai.
MATH_LH = 1.22            # rindas augstums
MATH_PAD = 0.30           # atstarpe ap daļas svītru
MATH_H = 2.0 * MATH_LH + MATH_PAD + 0.10      # daļas kopējais augstums
MATH_ROOT_LH = MATH_LH + 0.22                 # vieta vinkulam virs saknes
BASE_OFF = 0.34           # bāzes līnija zem rindas viduslīnijas
ROOT_ASC = 0.98           # vinkuls virs bāzes līnijas
ROOT_DESC = 0.10          # zīmes apakša zem bāzes līnijas
ROOT_TOP = 0.18           # vinkuls un elpa virs daļas zem saknes
ROOT_BAR = 0.055          # vinkula biezums
ROOT_LEAD = 0.30          # atstarpe pirms saknes zīmes
ROOT_INNER = 0.16         # atstarpe starp zīmi un izteiksmi
ROOT_SIDE = 0.42          # elpa aiz saknes


def root_extent(atoms):
    """Cik augstu virs un zem rindas viduslīnijas sniedzas saknes zīme.

    Vienkāršai izteiksmei tā ir viena rinda ar vinkulu; ja zem vinkula ir
    vertikāla daļa, zīme aptver visu daļu (rules_lessons.txt: zem saknes
    zīmes jābūt VISAI izteiksmei).
    """
    if any(a[0] == "f" for a in atoms):
        return MATH_H / 2.0 + ROOT_TOP, MATH_H / 2.0
    return ROOT_ASC - BASE_OFF, ROOT_DESC + BASE_OFF


def root_em(atoms):
    """Saknes zīmes augstums fonta izmēra daļās."""
    up, dn = root_extent(atoms)
    return up + dn


ROOT_T = 0.075               # zīmes līnijas biezums (fonta izmēra daļās)
ROOT_HOOK = 0.80             # āķīša augstums, kad zīme ir gara


def root_width(h):
    """Zīmes platums, ja tās augstums ir h (abi fonta izmēra daļās).

    Platums aug daudz lēnāk par augstumu: garai saknei (piem., zem vinkula
    ir vertikāla daļa) svītra kļūst stāvāka, nevis platāka - tāpat kā
    grāmatu salikumā.
    """
    return 0.44 + 0.20 * h


def _cross(a, b):
    """Divu taišņu krustpunkts (leņķa iekšmala)."""
    (x1, y1), (x2, y2) = a
    (x3, y3), (x4, y4) = b
    d = (x2 - x1) * (y4 - y3) - (y2 - y1) * (x4 - x3)
    if abs(d) < 1e-9:
        return x2, y2
    u = ((x3 - x1) * (y4 - y3) - (y3 - y1) * (x4 - x3)) / d
    return x1 + u * (x2 - x1), y1 + u * (y2 - y1)


def _offset(pts, d):
    """Lauztā līnija, atkāpta par d uz sāniem (ar leņķu krustpunktiem)."""
    segs = []
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        dx, dy = x2 - x1, y2 - y1
        ln = (dx * dx + dy * dy) ** 0.5 or 1e-9
        nx, ny = -dy / ln * d, dx / ln * d
        segs.append(((x1 + nx, y1 + ny), (x2 + nx, y2 + ny)))
    out = [segs[0][0]]
    for a, b in zip(segs, segs[1:]):
        out.append(_cross(a, b))
    out.append(segs[-1][1])
    return out


def root_pts(h):
    """Saknes zīmes kontūra fonta izmēra daļās; y aug uz leju.

    Līnijas biezums ir nemainīgs (ROOT_T) neatkarīgi no zīmes augstuma,
    tāpēc gara sakne nekļūst treknāka par vinkulu.
    """
    w = root_width(h)
    hook = min(0.46 * h, ROOT_HOOK)
    axis = [(0.0, 0.97 * h - hook + 0.12),
            (0.22 * w, 0.97 * h - hook),
            (0.52 * w, 0.97 * h),
            (w, 0.02 * h)]
    pts = _offset(axis, ROOT_T / 2.0) + _offset(axis, -ROOT_T / 2.0)[::-1]
    # kontūra pieliec malas mazliet ārpus asu kastes - ieliek to atpakaļ,
    # lai zīmes stūris precīzi sakristu ar vinkula sākumu
    xs = [q[0] for q in pts]
    ys = [q[1] for q in pts]
    kx = w / (max(xs) - min(xs))
    ky = h / (max(ys) - min(ys))
    pts = [((x - min(xs)) * kx, (y - min(ys)) * ky) for x, y in pts]
    return w, pts


def root_path_d(h):
    """Saknes zīmes kontūra kā SVG "d" virkne (koordinātas em vienībās)."""
    _, pts = root_pts(h)
    return "M%s Z" % " L".join("%.4f %.4f" % p for p in pts)


def root_svg(h=None, cls="rk"):
    """Saknes zīme kā SVG - to pašu kontūru zīmē arī .pptx (root_pts).

    Zīmi lieto divas vietas: prezentāciju lapa (html_deck.py) un pārbaudes
    darbu lapa (fd_stils.py), tāpēc markup ir šeit, nevis abās (DRY).
    """
    h = root_em([("t", "")]) if h is None else h
    w, _ = root_pts(h)
    return ('<svg class="%s" viewBox="0 0 %.4f %.4f" '
            'preserveAspectRatio="none" aria-hidden="true">'
            '<path d="%s"/></svg>' % (cls, w, h, root_path_d(h)))
