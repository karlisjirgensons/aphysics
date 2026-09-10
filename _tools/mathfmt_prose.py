# -*- coding: utf-8 -*-
"""
Piesardzīgā daļu atpazīšana PARASTĀ TEKSTĀ (paneļi, kopsavilkumi, uzdevumu
teksti).

mathfmt.parse_math() ir domāts laukiem, kur visa rinda ir formula. Parastā
tekstā tā nederētu: tur "km/h" ir mērvienība, "garums/augstums" ir divi vārdi,
bet "1/16", "F/S" un "1/r²" tomēr ir īstas daļas. Šeit pārveido tikai tos
gadījumus, kur kļūda praktiski nav iespējama.

Noraida:
  · mērvienības             m/s, kg/m³, N/m², W/(m·K), MJ/kg, km/h
  · vārdus                  garums/augstums, drošinātājs/automātslēdzis
  · lielumu ar mērvienību   15°/h, 1,8 °C/min
  · nepārprotamu grupējumu  "24 + 37/60" (pirms skaitītāja ir + vai −)

Pieņem:
  1/16, 4/3, F/S, c/f, Δs/λ, 1/r², A(lied)/A(patēr), (m₁+m₂)/(V₁+V₂),
  ρ = m/V (aiz vienādības zīmes mērvienību aizliegums nedarbojas).
"""

from mathfmt import (_SUB, _SUPER, _strip_outer, split_roots,
                     _UNITS, _BASES, _PREFIX, _base_unit)

# mērvienību simboli (bez tiem, ko lieto arī kā lielumu apzīmējumus tekstā)
_LET = ("abcdefghijklmnopqrstuvwxyzāčēģīķļņšūž"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZĀČĒĢĪĶĻŅŠŪŽ"
        "αβγδεζηθικλμνξοπρστυφχψωΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ")
_ASCII_DIGITS = "0123456789"

# no marķiera galiem noņem tikai pieturzīmes - iekavas ir daļa no izteiksmes
_TRIM = " \t.,;:!?—–…\"'«»“”„"
# mērvienību pārbaudē iekavas tomēr jānoņem: W/(m·K)
_UTRIM = _TRIM + "()[]"
# zīmes, kas nozīmē, ka skaitītājs ir tikai daļa no lielākas izteiksmes
_BREAK = "+−-·×*"


def _is_unit(tok):
    t = tok.strip(_UTRIM)
    if not t:
        return False
    for piece in t.replace("×", "·").replace("/", "·").split("·"):
        piece = piece.strip(_UTRIM)
        if piece and not _base_unit(piece):
            return False
    return True


def _max_letter_run(tok):
    """Garākā burtu virkne ārpus iekavām - iekavās ir indeksi: A(lied)."""
    best = run = depth = 0
    for ch in tok:
        if ch == "(":
            depth += 1
            run = 0
            continue
        if ch == ")":
            depth = max(0, depth - 1)
            run = 0
            continue
        if depth:
            continue
        run = run + 1 if ch in _LET else 0
        best = max(best, run)
    return best


def _ident_start(part, k):
    """Pirms iekavas paņem arī apzīmējumu: A(lied) -> sākas pie 'A'."""
    while k > 0 and (part[k - 1] in _LET or part[k - 1] in _SUB
                     or part[k - 1] in _SUPER):
        k -= 1
    return k


def _paren_left(part, i):
    j = i - 1
    while j >= 0 and part[j] == " ":
        j -= 1
    if j < 0 or part[j] != ")":
        return None
    depth = 0
    for k in range(j, -1, -1):
        if part[k] == ")":
            depth += 1
        elif part[k] == "(":
            depth -= 1
            if depth == 0:
                return _ident_start(part, k), j + 1
    return None


def _paren_right(part, i):
    j = i + 1
    while j < len(part) and part[j] == " ":
        j += 1
    if j >= len(part) or part[j] != "(":
        return None
    depth = 0
    for k in range(j, len(part)):
        if part[k] == "(":
            depth += 1
        elif part[k] == ")":
            depth -= 1
            if depth == 0:
                return j, k + 1
    return None


def _tok_left(part, i):
    grp = _paren_left(part, i)
    if grp:
        return grp
    j = i
    while j > 0 and part[j - 1] == " ":
        j -= 1
    k = j
    while k > 0 and part[k - 1] != " ":
        k -= 1
    return (k, j) if k < j else None


def _tok_right(part, i):
    grp = _paren_right(part, i)
    if grp:
        return grp
    j = i + 1
    while j < len(part) and part[j] == " ":
        j += 1
    k = j
    while k < len(part) and part[k] != " ":
        k += 1
    return (j, k) if k > j else None


def _lhs_token(text, k):
    """Marķieris pa kreisi no "=": 'kg : m³ = kg/m³' -> 'm³'."""
    j = k - 1
    while j >= 0 and text[j] in " =":
        j -= 1
    e = j + 1
    while j >= 0 and text[j] != " ":
        j -= 1
    return text[j + 1:e]


def _num_extend(text, a, b):
    """Pievieno skaitli skaitītāja priekšā: '1,00 m' / D(S)."""
    j = a
    while j > 0 and text[j - 1] == " ":
        j -= 1
    if j == a or j == 0 or text[j - 1] not in "0123456789":
        return a, b
    k = j
    while k > 0 and text[k - 1] != " ":
        k -= 1
    return k, b


def _den_cut(text, a, b):
    """Bez iekavām saucējs beidzas pie pirmās reizināšanas zīmes: 4/3·π·R³."""
    for k in range(a, b):
        if text[k] in "·×*":
            return a, k
    return a, b


def _prev_visible(part, k):
    j = k - 1
    while j >= 0 and part[j] == " ":
        j -= 1
    return part[j] if j >= 0 else ""


def _quantity(tok):
    """'15°', '90 %' - skaitlis ar mērvienību, nevis mainīgais.

    Ar nolūku šauri: "2h" (2 reiz augstums) NAV lielums ar mērvienību,
    tāpēc √(2h/g) paliek daļa.
    """
    t = tok.strip()
    return (any(c in _ASCII_DIGITS for c in t)
            and t.endswith(("°", "%")))


def _scope(text, i):
    """Iekšējās iekavas, kurās atrodas slīpsvītra: '(4/3)·π' -> '4/3'."""
    lo, stack = 0, []
    for k, ch in enumerate(text):
        if ch == "(":
            stack.append(k)
        elif ch == ")" and stack:
            o = stack.pop()
            if o < i < k:
                lo = max(lo, o + 1)
                return lo, k
    return 0, len(text)


def _balanced(s):
    d = 0
    for ch in s:
        if ch == "(":
            d += 1
        elif ch == ")":
            d -= 1
            if d < 0:
                return False
    return d == 0


def parse_prose(text):
    """Atgriež tādus pašus atomus kā mathfmt.parse_math().

    Vispirms atdala saknes: zem vinkula esošu slīpsvītru ("√(l/g)") lasa
    saknes atomu būvētājs, nevis šī piesardzīgā daļu meklēšana - citādi
    daļa tiktu izrauta ārā no saknes.
    """
    out = []
    for a in split_roots([("t", text)]):
        if a[0] == "t":
            out.extend(_prose_fractions(a[1]))
        else:
            out.append(a)
    merged = []
    for a in out:
        if a[0] == "t" and merged and merged[-1][0] == "t":
            merged[-1] = ("t", merged[-1][1] + a[1])
        else:
            merged.append(a)
    if not any(a[0] in ("f", "r") for a in merged):
        return [("t", text)]
    return merged


def _prose_fractions(text):
    """Daļu meklēšana tekstā bez saknēm; ja nav, atgriež vienu ("t", ...)."""
    out, pos, i, n = [], 0, 0, len(text)
    # "[p] = Pa = N/m²" - mērvienību pieraksts; tur nekas nav jāpārveido
    bracket = "[" in text and "]" in text
    while i < n:
        if text[i] != "/":
            i += 1
            continue
        lo, hi = _scope(text, i)
        seg = text[lo:hi]
        L = _tok_left(seg, i - lo)
        R = _tok_right(seg, i - lo)
        if not L or not R:
            i += 1
            continue
        L = (L[0] + lo, L[1] + lo)
        R = (R[0] + lo, R[1] + lo)
        if text[R[0]] != "(":
            R = _den_cut(text, R[0], R[1])
        num = text[L[0]:L[1]].strip(_TRIM)
        den = text[R[0]:R[1]].strip(_TRIM)
        prev = _prev_visible(text, L[0])
        # aiz "=" ir formula - ja vien pa kreisi no "=" nav mērvienība
        formula = (prev == "=" and not bracket
                   and not _is_unit(_lhs_token(text, L[0])))
        ok = (num and den
              and len(num) <= 16 and len(den) <= 16
              and any(c.isalnum() or c in _SUB or c in _SUPER for c in num)
              and any(c.isalnum() or c in _SUB or c in _SUPER for c in den)
              and _max_letter_run(num) <= 3 and _max_letter_run(den) <= 3
              and _balanced(num) and _balanced(den)
              and not (num.isalpha() and den.isalpha()
                       and len(num) >= 3 and len(den) >= 3)
              and not (prev and prev in _BREAK)
              and (formula or not (_is_unit(num) and _is_unit(den)))
              and not (_quantity(num) and _is_unit(den)))
        if not ok:
            i += 1
            continue
        L = _num_extend(text, L[0], L[1])
        num = text[L[0]:L[1]].strip(_TRIM)
        if pos < L[0]:
            out.append(("t", text[pos:L[0]]))
        out.append(("f", _strip_outer(num), _strip_outer(den)))
        pos = i = R[1]
    if pos < n:
        out.append(("t", text[pos:]))
    return out or [("t", text)]


def has_prose_fraction(text):
    return any(a[0] == "f" for a in parse_prose(text))


def has_prose_math(text):
    """Vai teksta rindā ir daļa vai sakne, kas jāzīmē vertikāli."""
    return any(a[0] in ("f", "r") for a in parse_prose(text))
