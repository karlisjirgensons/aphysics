# -*- coding: utf-8 -*-
"""IQ testu zīmējumi: figūras, matricas, kubu kaudzes, tīkli un svari.

Šis modulis tikai zīmē (SRP) - ko zīmēt un kāda ir pareizā atbilde, zina
iq_miklas.py. Visi zīmējumi ir SVG vai vienkāršs HTML ar klasēm, kuru stils
dzīvo iq_bloks.py, tāpēc tie izskatās vienādi telefonā un uz tāfeles un
nekad nav atkarīgi no emocijzīmju fonta.

Figūru apraksta ar vārdnīcu (tā ir arī mīklas «pazīmju vektors»):

    {"forma": "trijsturis", "skaits": 2, "krasa": "violets",
     "pild": "pilns", "rot": 0}

Tā pati vārdnīca der gan zīmēšanai, gan salīdzināšanai, gan paskaidrojumam
(DRY) - forma un krāsa ir arī latviskie vārdi, ko liek teikumā.
"""

import math

# --------------------------------------------------------------- vārdnīca
# Vārda formas teikumiem: nominatīvs, daudzskaitlis, datīvs («pretī
# zvaigznei»), akuzatīvs daudzskaitlī («atzīmē visus apļus») un ģenitīvs
# daudzskaitlī («cik apļu?»).
NOM, DSK, DAT, AKK, GEN = range(5)
FORMAS = {
    "aplis": ("aplis", "apļi", "aplim", "apļus", "apļu"),
    "kvadrats": ("kvadrāts", "kvadrāti", "kvadrātam", "kvadrātus",
                 "kvadrātu"),
    "trijsturis": ("trijstūris", "trijstūri", "trijstūrim", "trijstūrus",
                   "trijstūru"),
    "piecsturis": ("piecstūris", "piecstūri", "piecstūrim", "piecstūrus",
                   "piecstūru"),
    "sessturis": ("sešstūris", "sešstūri", "sešstūrim", "sešstūrus",
                  "sešstūru"),
    "zvaigzne": ("zvaigzne", "zvaigznes", "zvaigznei", "zvaigznes",
                 "zvaigžņu"),
    "rombs": ("rombs", "rombi", "rombam", "rombus", "rombu"),
    "krusts": ("krusts", "krusti", "krustam", "krustus", "krustu"),
    "bulta": ("bulta", "bultas", "bultai", "bultas", "bultu"),
}
SIEVIESU = {"zvaigzne", "bulta"}

# krāsa: CSS krāsa un vārds - «krāsa ir violeta», «visus violetos /
# visas violetās», «cik violetu».
KRASAS = {
    "violets": ("#7C3AED", "violeta", "violetos", "violetās", "violetu"),
    "oranzs": ("#F59E0B", "oranža", "oranžos", "oranžās", "oranžu"),
    "zils": ("#0EA5E9", "zila", "zilos", "zilās", "zilu"),
    "zals": ("#10B981", "zaļa", "zaļos", "zaļās", "zaļu"),
    "roza": ("#EC4899", "rozā", "rozā", "rozā", "rozā"),
}

PILDIJUMI = {"pilns": "aizkrāsota", "tukss": "tukša", "gaiss": "gaiša"}


def vards(forma, kas=NOM):
    return FORMAS[forma][kas]


def krasa(krasa_, kas="nom", forma=None):
    """Krāsas vārds: «nom» - violeta, «akk» - violetos/violetās, «gen»."""
    k = KRASAS[krasa_]
    if kas == "akk":
        return k[3] if forma in SIEVIESU else k[2]
    return k[4] if kas == "gen" else k[1]


def ko_akk(forma, krasa_=None):
    """«visus zilos apļus» / «visas zvaigznes»."""
    visi = "visas" if forma in SIEVIESU else "visus"
    if krasa_:
        return "%s %s %s" % (visi, krasa(krasa_, "akk", forma),
                             vards(forma, AKK))
    return "%s %s" % (visi, vards(forma, AKK))


def ko_gen(forma, krasa_=None):
    """«zilu apļu» / «zvaigžņu»."""
    if krasa_:
        return "%s %s" % (krasa(krasa_, "gen"), vards(forma, GEN))
    return vards(forma, GEN)


def _cip(x):
    return ("%.2f" % x).rstrip("0").rstrip(".")


def _punkti(pts):
    return " ".join("%s,%s" % (_cip(x), _cip(y)) for x, y in pts)


def _daudzsturis(n, cx, cy, r, rot, sakums=-90):
    return [(cx + r * math.cos(math.radians(sakums + rot + 360.0 * i / n)),
             cy + r * math.sin(math.radians(sakums + rot + 360.0 * i / n)))
            for i in range(n)]


def _zvaigzne(cx, cy, r, rot):
    pts = []
    for i in range(10):
        rr = r if i % 2 == 0 else r * 0.45
        a = math.radians(-90 + rot + 36 * i)
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return pts


def _pagriez(pts, cx, cy, rot):
    a = math.radians(rot)
    c, s = math.cos(a), math.sin(a)
    return [(cx + (x - cx) * c - (y - cy) * s,
             cy + (x - cx) * s + (y - cy) * c) for x, y in pts]


def _krusts(cx, cy, r, rot):
    w = r * 0.36
    pts = [(-w, -r), (w, -r), (w, -w), (r, -w), (r, w), (w, w), (w, r),
           (-w, r), (-w, w), (-r, w), (-r, -w), (-w, -w)]
    return _pagriez([(cx + x, cy + y) for x, y in pts], cx, cy, rot)


def _bulta(cx, cy, r, rot):
    """Bulta uz augšu - pagriezta tā, lai virziens ir pazīme."""
    w = r * 0.32
    pts = [(0, -r), (r * 0.8, -r * 0.1), (w, -r * 0.1), (w, r), (-w, r),
           (-w, -r * 0.1), (-r * 0.8, -r * 0.1)]
    return _pagriez([(cx + x, cy + y) for x, y in pts], cx, cy, rot)


def _stils(krasa, pild):
    k = KRASAS[krasa][0]
    if pild == "tukss":
        return 'fill="#fff" stroke="%s" stroke-width="4"' % k
    if pild == "gaiss":
        return ('fill="%s" fill-opacity=".3" stroke="%s" stroke-width="4"'
                % (k, k))
    return 'fill="%s" stroke="%s" stroke-width="2"' % (k, k)


def figura(forma, cx, cy, r, krasa="violets", pild="pilns", rot=0):
    """Viena figūra SVG elementā; r - apvilktā riņķa rādiuss."""
    st = _stils(krasa, pild)
    if forma == "aplis":
        return '<circle cx="%s" cy="%s" r="%s" %s/>' % (
            _cip(cx), _cip(cy), _cip(r * 0.9), st)
    if forma == "zvaigzne":
        pts = _zvaigzne(cx, cy, r, rot)
    elif forma == "krusts":
        pts = _krusts(cx, cy, r * 0.9, rot)
    elif forma == "bulta":
        pts = _bulta(cx, cy, r, rot)
    else:
        n, pamats = {"kvadrats": (4, 45), "trijsturis": (3, 0),
                     "piecsturis": (5, 0), "sessturis": (6, 30),
                     "rombs": (4, 0)}[forma]
        rr = r * (0.95 if forma == "kvadrats" else 1.0)
        pts = _daudzsturis(n, cx, cy * 1.0 + (r * 0.12 if n == 3 else 0),
                           rr, pamats + rot)
        if forma == "rombs":
            pts = [(cx + (x - cx) * 0.72, y) for x, y in pts]
    return '<polygon points="%s" stroke-linejoin="round" %s/>' % (
        _punkti(pts), st)


# Kur rūtiņā stāv 1-6 figūras (100 × 100) un cik lielas tās ir.
_IZKARTOJUMI = {
    1: ([(50, 50)], 30),
    2: ([(28, 50), (72, 50)], 19),
    3: ([(50, 27), (27, 70), (73, 70)], 17),
    4: ([(29, 29), (71, 29), (29, 71), (71, 71)], 16),
    5: ([(25, 25), (75, 25), (50, 50), (25, 75), (75, 75)], 13),
    6: ([(27, 22), (73, 22), (27, 50), (73, 50), (27, 78), (73, 78)], 12),
}


def _svg(saturs, vb="0 0 100 100", klase="iq-f"):
    return ('<svg class="%s" viewBox="%s" aria-hidden="true">%s</svg>'
            % (klase, vb, saturs))


def suna(spec):
    """Rūtiņa ar vienu vai vairākām vienādām figūrām."""
    vietas, r = _IZKARTOJUMI[spec.get("skaits", 1)]
    if spec.get("izm"):
        r = r * spec["izm"]
    return _svg("".join(
        figura(spec["forma"], x, y, r, spec.get("krasa", "violets"),
               spec.get("pild", "pilns"), spec.get("rot", 0))
        for x, y in vietas))


def matrica(sunas, n):
    """n × n režģis; None ir tukšā rūtiņa ar jautājuma zīmi."""
    rutinas = []
    for s in sunas:
        if s is None:
            rutinas.append('<div class="iq-q">?</div>')
        else:
            rutinas.append("<div>%s</div>" % suna(s))
    return ('<div class="iq-mat" style="%s">%s</div>'
            % (_rezga_stils(n, len(rutinas)), "".join(rutinas)))


def _rezga_stils(kol, skaits):
    """Kolonnas un rindas - pēc tām CSS režģi ieliek pieejamajā vietā."""
    return "--n:%d;--rindas:%d" % (kol, -(-skaits // kol))


def rinda(sunas):
    """Figūru rinda - «lieks ārā» un virknes no figūrām."""
    return matrica(sunas, len(sunas))


# ------------------------------------------------------ skaitļu flīzes
def flizes(skaitli):
    """Skaitļu virkne; None ir flīze ar jautājuma zīmi."""
    gab = ['<span class="iq-q">?</span>' if s is None
           else "<span>%s</span>" % s for s in skaitli]
    return '<div class="iq-flizes">%s</div>' % "".join(gab)


def tabula(rindas):
    """Skaitļu režģis (maģiskais kvadrāts u.c.); None ir «?»."""
    n = len(rindas[0])
    sunas = []
    for r in rindas:
        for s in r:
            sunas.append('<span class="iq-q">?</span>' if s is None
                         else "<span>%s</span>" % ("" if s == "" else s))
    return ('<div class="iq-tab" style="%s">%s</div>'
            % (_rezga_stils(n, len(sunas)), "".join(sunas)))


def piramida(rindas):
    """Skaitļu piramīda: augšējā rinda pirmā; None ir «?»."""
    out = []
    for r in rindas:
        out.append('<div>%s</div>' % "".join(
            '<span class="iq-q">?</span>' if s is None
            else "<span>%s</span>" % s for s in r))
    return '<div class="iq-pir">%s</div>' % "".join(out)


# ----------------------------------------------------- simbolu vienādojumi
def simbols(forma, krasa):
    """Mazs figūras attēls teksta rindā."""
    return _svg(figura(forma, 50, 50, 42, krasa), klase="iq-s")


def vienadojumi(rindas):
    """Rindas no gabaliem: (forma, krāsa) ir simbols, teksts ir teksts."""
    out = []
    for r in rindas:
        gab = []
        for g in r:
            if isinstance(g, tuple):
                gab.append(simbols(*g))
            else:
                gab.append("<span>%s</span>" % g)
        out.append('<div class="iq-vien">%s</div>' % "".join(gab))
    return '<div class="iq-vienadojumi">%s</div>' % "".join(out)


# ------------------------------------------------------------------ svari
def svari(kreisa, laba):
    """Līdzsvarā esoši svari; katra puse - [(forma, krāsa), ...] vai «?»."""
    def puse(lietas, cx):
        if lietas == "?":
            return ('<text x="%d" y="41" text-anchor="middle" '
                    'class="iq-svq">?</text>' % cx)
        n = len(lietas)
        r = 7 if n <= 4 else 5.6
        solis = 2 * r + 1.5
        rindas = [lietas[i:i + 4] for i in range(0, n, 4)]
        out = []
        for ri, rinda_ in enumerate(rindas):
            x0 = cx - (len(rinda_) - 1) * solis / 2
            for i, (forma, krasa) in enumerate(rinda_):
                out.append(figura(forma, x0 + i * solis,
                                  46 - r - ri * (2 * r + 1), r, krasa))
        return "".join(out)
    k = ('<path d="M60 50 L60 88 M44 88 H76" class="iq-sv"/>'
         '<path d="M14 50 H106" class="iq-sv"/>'
         '<path d="M4 50 Q24 60 44 50 M76 50 Q96 60 116 50" class="iq-sv"/>'
         '<circle cx="60" cy="50" r="3" class="iq-svc"/>')
    return _svg(k + puse(kreisa, 24) + puse(laba, 96), "0 8 120 84",
                "iq-f iq-svari")


# ------------------------------------------------------------ kubu kaudze
_KUBA_KRASAS = ("#DDD6FE", "#A78BFA", "#7C3AED")   # augša, kreisā, labā


def kubi(augstumi):
    """Kubu stabiņi izometrijā; augstumi[i][j], i - no aizmugures uz priekšu.

    Zīmē no aizmugures uz priekšu un no apakšas uz augšu, tāpēc priekšējie
    kubi pareizi aizsedz aizmugurējos (gleznotāja kārtība).
    """
    a, b, c = 13.0, 7.5, 15.0

    def p(i, j, z):
        return ((j - i) * a, (j + i) * b - z * c)

    kubi_ = [(i, j, z) for i, r in enumerate(augstumi)
             for j, h in enumerate(r) for z in range(h)]
    kubi_.sort(key=lambda t: (t[0] + t[1], t[2]))
    dalas, visi = [], []
    for i, j, z in kubi_:
        virsa = [p(i, j, z + 1), p(i, j + 1, z + 1), p(i + 1, j + 1, z + 1),
                 p(i + 1, j, z + 1)]
        kreisa = [p(i + 1, j, z + 1), p(i + 1, j + 1, z + 1),
                  p(i + 1, j + 1, z), p(i + 1, j, z)]
        laba = [p(i, j + 1, z + 1), p(i + 1, j + 1, z + 1),
                p(i + 1, j + 1, z), p(i, j + 1, z)]
        for pts, krasa in ((virsa, _KUBA_KRASAS[0]), (kreisa, _KUBA_KRASAS[1]),
                           (laba, _KUBA_KRASAS[2])):
            dalas.append('<polygon points="%s" fill="%s" stroke="#312E81" '
                         'stroke-width=".8" stroke-linejoin="round"/>'
                         % (_punkti(pts), krasa))
            visi.extend(pts)
    xs, ys = [x for x, _ in visi], [y for _, y in visi]
    m = 3
    vb = "%s %s %s %s" % (_cip(min(xs) - m), _cip(min(ys) - m),
                          _cip(max(xs) - min(xs) + 2 * m),
                          _cip(max(ys) - min(ys) + 2 * m))
    return _svg("".join(dalas), vb, "iq-f iq-kubi")


# ------------------------------------------------------------ poliomino
def poliomino(sunas, krasa="violets", zime=None):
    """Figūra no rūtiņām; zime - (rinda, kolonna), kur ir punkts."""
    rs = [r for r, _ in sunas]
    cs = [c for _, c in sunas]
    h, w = max(rs) - min(rs) + 1, max(cs) - min(cs) + 1
    s = 80.0 / max(h, w, 3)
    x0 = 50 - w * s / 2 - min(cs) * s
    y0 = 50 - h * s / 2 - min(rs) * s
    k = KRASAS[krasa][0]
    out = ['<rect x="%s" y="%s" width="%s" height="%s" rx="1.5" fill="%s" '
           'stroke="#fff" stroke-width="2"/>'
           % (_cip(x0 + c * s), _cip(y0 + r * s), _cip(s), _cip(s), k)
           for r, c in sunas]
    if zime:
        r, c = zime
        out.append('<circle cx="%s" cy="%s" r="%s" fill="#fff"/>'
                   % (_cip(x0 + (c + .5) * s), _cip(y0 + (r + .5) * s),
                      _cip(s * .22)))
    return _svg("".join(out))


def ar_spoguli(zimejums):
    """Figūra un spoguļa līnija pa labi no tās."""
    return ('<div class="iq-spogulis">%s<span class="iq-sp-l"></span>'
            '<span class="iq-q">?</span></div>' % zimejums)


# ------------------------------------------------------------- kuba tīkls
def tikls(sunas, simboli):
    """Kuba izklājums: sunas - [(rinda, kolonna)], simboli - [(forma, krāsa)]."""
    rs = [r for r, _ in sunas]
    cs = [c for _, c in sunas]
    s = 20.0
    w, h = (max(cs) + 1) * s, (max(rs) + 1) * s
    out = []
    for (r, c), (forma, krasa) in zip(sunas, simboli):
        out.append('<rect x="%s" y="%s" width="%s" height="%s" fill="#fff" '
                   'stroke="#4F46E5" stroke-width="1"/>'
                   % (_cip(c * s), _cip(r * s), _cip(s), _cip(s)))
        out.append(figura(forma, c * s + s / 2, r * s + s / 2, s * .34,
                          krasa))
    return _svg("".join(out), "-1 -1 %s %s" % (_cip(w + 2), _cip(h + 2)),
                "iq-f iq-tikls")


# ---------------------------------------------------------- atmiņas režģis
def rezgis(kol, ieslegtas=(), saturs=None):
    """Rūtiņu režģis ar kol kolonnām; ieslēgtās ir iekrāsotas (atmiņas
    uzdevuma paraugs). Bez satura režģis ir kvadrāts kol × kol."""
    ieslegtas = set(ieslegtas)
    skaits = len(saturs) if saturs else kol * kol
    gab = []
    for i in range(skaits):
        iekss = saturs[i] if saturs else ""
        gab.append('<span class="%s">%s</span>'
                   % ("on" if i in ieslegtas else "", iekss))
    return ('<div class="iq-rez" style="%s">%s</div>'
            % (_rezga_stils(kol, skaits), "".join(gab)))


def cipari(teksts):
    """Lieli cipari, ko jāiegaumē."""
    return '<div class="iq-cipari">%s</div>' % "".join(
        "<span>%s</span>" % c for c in teksts)
