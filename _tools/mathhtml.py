# -*- coding: utf-8 -*-
"""Matemātiskais pieraksts HTML: vertikālas daļas, saknes, indeksi, vektori.

Viena vieta visam, kas lapā izskatās pēc matemātikas (SRP). To lieto gan
prezentācijas (html_deck.py), gan matemātikas stundas (math_bloki.py), tāpēc
daļa un saknes zīme abās vietās izskatās vienādi (DRY). Zīmējumu izmēri nāk no
mathfmt.py - tie paši, pēc kuriem zīmē .pptx, tāpēc ekrāns un slaids sakrīt.

Divi ceļi teksta pārvēršanai, jo latviešu standartā mērvienības (m/s, kg/m³)
rindā paliek, bet dalījumi kļūst vertikāli:

    proza("3/4 no klases")   - piesardzīgā atpazīšana parastam tekstam;
                               mērvienības un vārdu pāri paliek rindā;
    mat("{2|5} + {1|3}")     - autora marķējums (rules_pd.txt): kas iekavās
                               ar «|», tas ir daļa, un neviens minējums nav
                               vajadzīgs.

Formulu tekstu stundās raksta ar mat(): «2/5 + 1/3» pati par sevi ir
divdomīga, un uzdevumā nedrīkst iznākt «+ 1» virs «3».

Marķējums (tas pats, ko lieto darba lapas - fd_math.py):
    {a|b}        vertikāla daļa - a virs b;
    √(a + b)     kvadrātsakne; zem vinkula paliek visa izteiksme;
    √25          kvadrātsakne vienam loceklim;
    *7*          izcelts gabals - ar to uzdevumā parāda, par kuru ciparu
                 vai vārdu ir runa (HTML birkas saturā rakstīt nedrīkst,
                 tās nonāktu lapā kā teksts);
    a^{m + n}    kāpinātājs - viss iekavās kāpinātājā;
    10^−3, a^n   kāpinātājs - skaitlis vai viens burts, tāpēc x^3y ir x³y
                 un daļā raksta {a^10|a^2}, jo iekavas daļā neder.
                 Skaitļu kāpinātājiem der arī ² un ³ - tie ir fontā.
"""

import html
import re

import mathfmt as MF
import mathfmt_prose as MP


# ------------------------------------------------------------------ teksts
def esc(s):
    """Tikai HTML rakstzīmju aizsegšana - bez formulu noformējuma."""
    return html.escape(s, quote=False)


_RUN_HTML = {"v": '<span class="vv">%s</span>',   # bultiņu zīmē CSS
             "s": "<sub>%s</sub>"}                # F_y -> indekss


def txt_html(s, iekavas=True):
    """Teksts HTML: aizsegts, ar uzzīmētām bultiņām un īstiem indeksiem.

    Viss teksts iet caur šo funkciju (DRY) - tāpēc vektora un indeksa
    pieraksts izskatās vienādi virsrakstos, kartītēs, tabulās un formulās.
    iekavas=False - matemātikā «P(A)» un «f(a)» nav indeksi (MF.split_runs).
    """
    if not MF.has_markup(s):
        return esc(s)
    return "".join(_RUN_HTML.get(k, "%s") % esc(v)
                   for k, v in MF.split_runs(s, iekavas))


def _sp(s, iekavas=True):
    """Atstarpes HTML nesaspiež - tās notur formulu atstatumus.

    Rindas sākuma un beigu atstarpi pārlūks izmet pavisam, tāpēc centrēts
    gabals ("√2500" un " = 50 N") saslīdētu kopā; te tās paliek kā &nbsp;.
    """
    lead = len(s) - len(s.lstrip(" "))
    trail = len(s) - len(s.rstrip(" ")) if s.strip() else 0
    core = s[lead:len(s) - trail] if trail else s[lead:]
    body = txt_html(core, iekavas).replace("  ", "&nbsp;&nbsp;")
    return "&nbsp;" * lead + body + "&nbsp;" * trail


# -------------------------------------------------------- daļa un sakne
# Saknes zīmes augstums fonta izmēra daļās nāk no mathfmt - tie paši mēri,
# pēc kuriem zīmi uzzīmē arī .pptx, tāpēc abi skati sakrīt.
ROOT_EM = MF.root_em([("t", "")])
ROOT_EM_TALL = MF.root_em([("f", "", "")])


def root_svg(h=ROOT_EM):
    """Saknes zīme kā SVG - tā pati forma, ko zīmē slaidā (MF.root_pts)."""
    return MF.root_svg(h)


def root_html(inner, tall=False):
    """√-izteiksme: vinkuls (svītra) pāri VISAI izteiksmei, ne tikai iekavai.

    Saknes zīmi zīmē pati lapa (MF.ROOT_PTS), tāpēc tā izstiepjas līdz
    satura augstumam - arī tad, ja zem vinkula ir vertikāla daļa - un
    vinkuls turpinās no tās augšmalas. `inner` jau ir gatavs HTML.
    """
    h = ROOT_EM_TALL if tall else ROOT_EM
    w, _ = MF.root_pts(h)
    return ('<span class="rt" style="--rw:%.3fem">%s'
            '<span class="rv">%s</span></span>'
            % (w, root_svg(h), inner))


def _frac(num, den):
    """Vertikāla daļa no jau gatava HTML."""
    return ('<span class="f"><span class="n">%s</span>'
            '<span class="d">%s</span></span>' % (num, den))


def frac_span(num, den, iekavas=True):
    """Vertikāla daļa: skaitītājs virs saucēja; `num`/`den` ir teksts."""
    return _frac(txt_html(num, iekavas), txt_html(den, iekavas))


def atoms_html(atoms):
    """Atomu virkne uz HTML - viena vieta abiem parsētājiem (DRY)."""
    out = []
    for a in atoms:
        if a[0] == "t":
            out.append(_sp(a[1]))
        elif a[0] == "r":
            out.append(root_html(atoms_html(a[1]),
                                 tall=any(x[0] == "f" for x in a[1])))
        else:
            out.append(frac_span(a[1], a[2]))
    return "".join(out)


def proza(text):
    """Parasta teksta dalījumi HTML - vertikāla daļa kā <span class=f>.

    Lieto piesardzīgo atpazīšanu: mērvienības (m/s, kg/m³) un vārdu pāri
    (garums/augstums) paliek rindā, bet 1/16, F/S, 1/r² kļūst vertikāli.
    """
    return atoms_html(MP.parse_prose(text))


# --------------------------------------------------- autora marķējums
_DALA = re.compile(r"\{([^{}|]*)\|([^{}|]*)\}")
# Izcēlumā nav atstarpes pie malām, tāpēc «3 * 4» paliek, kā bija.
_IZCEL = re.compile(r"\*(\S|\S[^*]*?\S)\*")
# Kāpinātājs: ^{...} - viss iekavās; ^−3, ^n - viens loceklis ar zīmi.
_PAKAPE = re.compile(r"\^(?:\{([^{}]*)\}|([−-]?(?:\d+|[A-Za-z])))")


def _teksts(s):
    """Stundas teksta gabals: aizsegts, ar atstarpēm, izcēlumiem un
    kāpinātājiem.

    Izcēlumu un kāpinātāju liek tikai šeit, nevis _sp(), jo to pašu _sp()
    lieto prezentācijas, un tur zvaigznīte tekstā nozīmē zvaigznīti.
    """
    s = _IZCEL.sub(lambda m: '<b class="izcel">%s</b>' % m.group(1),
                   _sp(s, iekavas=False))
    return _PAKAPE.sub(lambda m: '<sup class="pk">%s</sup>'
                       % (m.group(1) if m.group(1) is not None
                          else m.group(2)).replace("-", "−"), s)


def mat(text):
    """Autora marķējums -> HTML: {a|b} ir daļa, √(...) ir sakne.

    Neko nemin: kas nav marķēts, paliek teksts, tāpēc «12 m/s» un
    «1. variants» netiek pārveidoti (rules_lessons.txt). Sakne un daļa var
    būt viena otrā: √{9|16} ir sakne no daļas (vinkuls pāri visai daļai),
    {√2|2} - daļa ar sakni skaitītājā.
    """
    out, i = [], 0
    while True:
        j = _saknes_vieta(text, i)
        if j < 0:
            out.append(_bez_saknes(text[i:]))
            return "".join(out)
        out.append(_bez_saknes(text[i:j]))
        iekss, i = _zem_saknes(text, j)
        out.append(root_html(mat(iekss), tall=bool(_DALA.search(iekss))))


def _saknes_vieta(text, no):
    """Pirmā √ ārpus daļas iekavām - saknes daļā apstrādā pati daļa."""
    dzilums = 0
    for k in range(no, len(text)):
        if text[k] == "{":
            dzilums += 1
        elif text[k] == "}":
            dzilums -= 1
        elif text[k] == MF.ROOT_SIGN and dzilums == 0:
            return k
    return -1


def _zem_saknes(text, j):
    """(zemsaknes teksts, kur sakne beidzas) saknei pozīcijā j.

    √{a|b} - zem vinkula visa daļa; citādi robežu nosaka mathfmt - tas pats
    noteikums, pēc kura sakni zīmē prezentācijās un darba lapās (DRY).
    """
    k = j + 1
    while k < len(text) and text[k] == " ":
        k += 1
    if k < len(text) and text[k] == "{":
        beigas = text.find("}", k) + 1 or len(text)
        return text[k:beigas], beigas
    sakums, beigas = MF._root_span(text, j)
    iekss = text[sakums:beigas]
    if iekss.startswith("(") and iekss.endswith(")"):
        iekss = iekss[1:-1]
    return iekss, beigas


def _bez_saknes(text):
    """Teksts bez saknēm ārpus daļām: daļas vertikāli, pārējais teksts."""
    out, i = [], 0
    for m in _DALA.finditer(text):
        out.append(_teksts(text[i:m.start()]))
        out.append(_frac(mat(m.group(1)), mat(m.group(2))))
        i = m.end()
    out.append(_teksts(text[i:]))
    return "".join(out)


def ir_mat(text):
    """Vai tekstā vispār ir marķējums - lai lieki nesauc parsētāju."""
    return (bool(_DALA.search(text)) or MF.ROOT_SIGN in text
            or bool(_PAKAPE.search(text)))
