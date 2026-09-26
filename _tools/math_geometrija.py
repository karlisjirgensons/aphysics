# -*- coding: utf-8 -*-
"""Ģeometrijas zīmējumi: punkti, nogriežņi, taisnes, leņķi un to atzīmes.

7. klases ģeometrija runā par figūrām, kas nav rūtiņās: trijstūris ar
vienādām malām, divas paralēlas taisnes un krustotāja, leņķis ar bisektrisi.
Te ir viena funkcija, kas tās visas zīmē pēc vārdiem - kur ir punkti un kas
starp tiem jāsavelk -, tāpēc stundas failā nav ne SVG, ne mērogošanas (SRP):

    geometrija([("A", 0, 0), ("B", 6, 0), ("C", 2, 4)],
               nogriezni=["AB", "BC", "CA"],
               lenki=[("CAB", "α")], svitras=[("AC", 1), ("BC", 1)])

Koordinātes ir brīvi izvēlētās vienībās, y aug uz augšu (kā plaknē). Zīmējums
pats izvēlas mērogu, lai figūra aizpildītu platumu, bet nepārsniegtu augstumu
- tā viens un tas pats trijstūris der gan telefonā, gan uz tāfeles.
Uzrakstu mēri, SVG ietvars un daļas uzraksts nāk no math_zimejumi (DRY).
"""

import math

from math_zimejumi import (PLATUMS, _svg, _teksta_plat, _teksts,
                           _virs_atkape, _virs_linija)

MALA = 8.0              # tukša josla ap figūru - tajā stāv virsotņu burti
MAKS_AUG = 58.0         # figūras augstākais augstums zīmējuma vienībās
LOKS = 5.0              # leņķa loka rādiuss


def _pari(nosaukums):
    """«AB» -> ("A", "B"); garākiem vārdiem padod pāri pašu: ("A1", "B")."""
    if isinstance(nosaukums, (list, tuple)):
        return tuple(nosaukums)
    if len(nosaukums) != 2:
        raise ValueError("nogriezni «%s» raksta kā pāri, piemēram, "
                         "(\"A1\", \"B\")" % nosaukums)
    return nosaukums[0], nosaukums[1]


def _trijnieks(nosaukums):
    """«BAC» -> ("B", "A", "C"): vidējais burts ir virsotne."""
    if isinstance(nosaukums, (list, tuple)):
        return tuple(nosaukums)
    if len(nosaukums) != 3:
        raise ValueError("leņķi «%s» raksta ar trim burtiem" % nosaukums)
    return nosaukums[0], nosaukums[1], nosaukums[2]


def _pagarina(p, q, cik):
    """Punkts aiz q uz stara pq - taisnes un stara turpinājums."""
    dx, dy = q[0] - p[0], q[1] - p[1]
    gar = math.hypot(dx, dy) or 1.0
    return (q[0] + dx / gar * cik, q[1] + dy / gar * cik)


def geometrija(punkti, nogriezni=(), taisnes=(), stari=(), lenki=(),
               taisni=(), svitras=(), malas=(), izcelti=(), iekrasot=(),
               uzraksti=(), rinki=(), slepti=(), virsraksts=None,
               aug=MAKS_AUG):
    """Ģeometriska figūra no nosauktiem punktiem.

    punkti:    [(vārds, x, y), ...] vai (vārds, x, y, virziens_grādos) - kur
               likt burtu; bez virziena burts stāv prom no figūras centra.
               Vārds, kas sākas ar «_», ir palīgpunkts bez burta.
    nogriezni: ["AB", ...]                  - nogriežņi;
    taisnes:   ["AB", ...]                  - taisne caur A un B (abos galos
               turpinās); stari: ["AB", ...] - stars no A caur B;
    lenki:     [("BAC", uzraksts[, loki]), ...] - loks virsotnē A starp
               stariem AB un AC (vienmēr mazākais leņķis); loki = 2 vai 3
               atzīmē vienādus leņķus;
    taisni:    ["ADB", ...]                 - taisnā leņķa kvadrātiņš pie D;
    svitras:   [("AB", n), ...]             - n svītriņas: vienādi nogriežņi;
    malas:     [("AB", uzraksts), ...]      - garums pie malas, ārpusē;
    izcelti:   ["AB", ...]                  - nogrieznis otrā krāsā;
    iekrasot:  [("ABC", 0 vai 1), ...]       - iekrāsots daudzstūris (0 -
               violets, 1 - dzintara; tā redz divus pārklātus trijstūrus);
    uzraksti:  [(x, y, teksts), ...]        - brīvs uzraksts tajās pašās
               koordinātēs;
    rinki:     [("O", r), ...] vai ("O", r, 1) - riņķa līnija ar centru
               punktā O un rādiusu r tajās pašās vienībās (1 - otrā krāsā).
               Tā 9. klases zīmējumā ievilkts trijstūris, pieskare un horda
               stāv uz īstas riņķa līnijas, nevis uz aptuvena apļa;
    slepti:    ["AB", ...]                  - neredzama šķautne (punktēta),
               kā telpiska ķermeņa skicē.
    """
    vieta, virzieni = {}, {}
    for p in punkti:
        vieta[p[0]] = (float(p[1]), float(p[2]))
        if len(p) > 3:
            virzieni[p[0]] = float(p[3])

    # Taisnes un stari iziet ārpus punktiem - arī tiem vajag vietu zīmējumā.
    gar = max(max(abs(a[0] - b[0]), abs(a[1] - b[1]))
              for a in vieta.values() for b in vieta.values()) or 1.0
    turpinajums = gar * 0.18
    linijas = [(vieta[a], vieta[b], "") for a, b in map(_pari, nogriezni)]
    linijas += [(vieta[a], vieta[b], " otra") for a, b in map(_pari, izcelti)]
    linijas += [(vieta[a], vieta[b], " slepts") for a, b in map(_pari, slepti)]
    for a, b in map(_pari, taisnes):
        linijas.append((_pagarina(vieta[b], vieta[a], turpinajums),
                        _pagarina(vieta[a], vieta[b], turpinajums), ""))
    for a, b in map(_pari, stari):
        linijas.append((vieta[a], _pagarina(vieta[a], vieta[b], turpinajums),
                        " stars"))

    visi = list(vieta.values()) + [p for l in linijas for p in l[:2]]
    visi += [(float(x), float(y)) for x, y, _ in uzraksti]
    for c, r, *_ in rinki:
        cx, cy = vieta[c]
        visi += [(cx - r, cy - r), (cx + r, cy + r)]
    x_min, x_max = min(p[0] for p in visi), max(p[0] for p in visi)
    y_min, y_max = min(p[1] for p in visi), max(p[1] for p in visi)
    merogs = min((PLATUMS - 2 * MALA) / ((x_max - x_min) or 1.0),
                 aug / ((y_max - y_min) or 1.0))
    y0 = MALA + (6.0 + _virs_atkape(virsraksts) if virsraksts else 0.0)
    x0 = (PLATUMS - (x_max - x_min) * merogs) / 2.0
    augstums = y0 + (y_max - y_min) * merogs + MALA

    def P(p):
        return (x0 + (p[0] - x_min) * merogs, y0 + (y_max - p[1]) * merogs)

    # Uzrakstus liek prom no figūras centra; ja visi punkti ir palīgpunkti
    # (laukuma modelis), centru dod tie paši.
    nosauktie = ([P(v) for k, v in vieta.items() if not k.startswith("_")]
                 or [P(v) for v in vieta.values()])
    centrs = (sum(p[0] for p in nosauktie) / max(len(nosauktie), 1),
              sum(p[1] for p in nosauktie) / max(len(nosauktie), 1))

    dalas = []
    if virsraksts:
        dalas.append(_teksts(PLATUMS / 2, 4.4 + _virs_linija(virsraksts),
                             virsraksts, "z-virs"))
    for virs, krasa in iekrasot:
        dalas.append('<polygon class="z-figura%s" points="%s"/>'
                     % (" otra" if krasa else "",
                        " ".join("%.2f,%.2f" % P(vieta[v]) for v in virs)))
    for c, r, *krasa in rinki:
        cx, cy = P(vieta[c])
        dalas.append('<circle class="z-lin%s" cx="%.2f" cy="%.2f" r="%.2f"/>'
                     % (" otra" if krasa and krasa[0] else "", cx, cy,
                        r * merogs))
    for a, b, klase in linijas:
        (x1, y1), (x2, y2) = P(a), P(b)
        dalas.append('<line class="z-lin%s" x1="%.2f" y1="%.2f" x2="%.2f" '
                     'y2="%.2f"/>' % (klase.replace(" stars", ""),
                                      x1, y1, x2, y2))
        if klase == " stars":
            dalas.append(_bultgals(x1, y1, x2, y2))
    for trij, *pars in lenki:
        dalas.extend(_lenkis(P, vieta, _trijnieks(trij), *pars))
    for trij in taisni:
        dalas.append(_taisns(P, vieta, _trijnieks(trij)))
    for nog, n in svitras:
        a, b = _pari(nog)
        dalas.extend(_svitras(P(vieta[a]), P(vieta[b]), n))
    for nog, uzraksts in malas:
        a, b = _pari(nog)
        dalas.append(_malas_uzraksts(P(vieta[a]), P(vieta[b]), centrs,
                                     uzraksts))
    for x, y, t in uzraksti:
        px, py = P((float(x), float(y)))
        dalas.append(_teksts(px, py, t, "z-atzime"))
    for vards, v in vieta.items():
        if vards.startswith("_"):
            continue
        px, py = P(v)
        dalas.append('<circle class="z-punkts" cx="%.2f" cy="%.2f" r="0.9"/>'
                     % (px, py))
        if vards in virzieni:
            a = math.radians(virzieni[vards])
            dx, dy = math.cos(a), -math.sin(a)
        else:
            dx, dy = px - centrs[0], py - centrs[1]
            g = math.hypot(dx, dy)
            dx, dy = (dx / g, dy / g) if g > 1e-6 else (0.6, -0.8)
        dalas.append(_teksts(px + 4.2 * dx, py + 4.2 * dy + 1.3, vards,
                             "z-virs"))
    return _svg(augstums, "".join(dalas))


def _virziens(P, no, uz):
    (x1, y1), (x2, y2) = P(no), P(uz)
    return math.atan2(y2 - y1, x2 - x1)


def _lenkis(P, vieta, trij, uzraksts="", loki=1):
    """Leņķa loks (vai vairāki - vienādiem leņķiem) un uzraksts pie tā."""
    b, a, c = trij
    vx, vy = P(vieta[a])
    a1 = _virziens(P, vieta[a], vieta[b])
    a2 = _virziens(P, vieta[a], vieta[c])
    d = (a2 - a1 + math.pi) % (2 * math.pi) - math.pi
    out = []
    for i in range(int(loki)):
        r = LOKS + 1.1 * i
        out.append('<path class="z-lin" d="M%.2f %.2f A%.2f %.2f 0 0 %d '
                   '%.2f %.2f"/>'
                   % (vx + r * math.cos(a1), vy + r * math.sin(a1), r, r,
                      1 if d > 0 else 0,
                      vx + r * math.cos(a1 + d), vy + r * math.sin(a1 + d)))
    if uzraksts:
        vid = a1 + d / 2.0
        # Šauram leņķim uzrakstu liek tālāk, lai tas neuzkristu stariem.
        r = LOKS + 1.1 * (int(loki) - 1) + (4.2 if abs(d) > 0.9 else 6.4)
        out.append(_teksts(vx + r * math.cos(vid),
                           vy + r * math.sin(vid) + 1.2, uzraksts,
                           "z-atzime"))
    return out


def _taisns(P, vieta, trij):
    """Taisnā leņķa kvadrātiņš virsotnē (vidējais burts)."""
    b, a, c = trij
    vx, vy = P(vieta[a])
    a1 = _virziens(P, vieta[a], vieta[b])
    a2 = _virziens(P, vieta[a], vieta[c])
    s = 3.2
    p1 = (vx + s * math.cos(a1), vy + s * math.sin(a1))
    p2 = (vx + s * math.cos(a2), vy + s * math.sin(a2))
    p3 = (p1[0] + p2[0] - vx, p1[1] + p2[1] - vy)
    return ('<path class="z-lin" d="M%.2f %.2f L%.2f %.2f L%.2f %.2f"/>'
            % (p1[0], p1[1], p3[0], p3[1], p2[0], p2[1]))


def _svitras(p, q, n):
    """n īsas svītriņas pāri nogriežņa vidum - vienādu nogriežņu zīme."""
    mx, my = (p[0] + q[0]) / 2.0, (p[1] + q[1]) / 2.0
    a = math.atan2(q[1] - p[1], q[0] - p[0])
    ux, uy = math.cos(a), math.sin(a)
    nx, ny = -uy, ux
    out = []
    for i in range(int(n)):
        t = (i - (n - 1) / 2.0) * 1.3
        cx, cy = mx + ux * t, my + uy * t
        out.append('<line class="z-lin" x1="%.2f" y1="%.2f" x2="%.2f" '
                   'y2="%.2f"/>' % (cx - nx * 1.8, cy - ny * 1.8,
                                    cx + nx * 1.8, cy + ny * 1.8))
    return out


def _malas_uzraksts(p, q, centrs, uzraksts):
    """Garums pie malas vidus - ārpus figūras, lai neuzkristu iekšpusei."""
    mx, my = (p[0] + q[0]) / 2.0, (p[1] + q[1]) / 2.0
    a = math.atan2(q[1] - p[1], q[0] - p[0])
    nx, ny = -math.sin(a), math.cos(a)
    if (mx - centrs[0]) * nx + (my - centrs[1]) * ny < 0:
        nx, ny = -nx, -ny
    # Pie stāvas malas uzraksts stāv sānis, tāpēc atkāpei jāpieskaita puse
    # no tā platuma - citādi «1,6 m» uzkrīt vertikālai līnijai.
    atk = 4.0 + abs(nx) * _teksta_plat(str(uzraksts), 3.6) / 2.0
    return _teksts(mx + nx * atk, my + ny * atk + 1.2, uzraksts, "z-atzime")


def _bultgals(x1, y1, x2, y2):
    a = math.atan2(y2 - y1, x2 - x1)
    gali = [(x2 - 2.6 * math.cos(a + d), y2 - 2.6 * math.sin(a + d))
            for d in (0.45, -0.45)]
    return ('<path class="z-bultgals" d="M%.2f %.2f L%.2f %.2f L%.2f %.2f Z"/>'
            % (x2, y2, gali[0][0], gali[0][1], gali[1][0], gali[1][1]))


def paralelas(radit=(1, 2, 3, 4, 5, 6, 7, 8), uzraksti=None, loki=None,
              slipums=60, paralelas=True, virsraksts=None):
    """Divas taisnes a (apakšā) un b (augšā), kuras krusto taisne c.

    Leņķus numurē vienādi visās stundās: pie augšējā krustpunkta 1-4,
    pie apakšējā 5-8, katrā - pretēji pulksteņa rādītājam, sākot no
    labās puses augšas (1 un 5 ir kāpšļu leņķi, 3 un 5 - iekšējie
    šķērsleņķi, 4 un 5 - iekšējie vienpusleņķi).

    radit    - kurus leņķus atzīmēt;
    uzraksti - {numurs: teksts}, piemēram, {1: "70°"}; citādi numurs;
    loki     - {numurs: loku skaits} - vienādi leņķi ar vienādiem lokiem;
    paralelas=False - taisne b ir nedaudz sasvērta (pazīmes stundām).
    """
    uzraksti = uzraksti or {}
    loki = loki or {}
    a = math.radians(slipums)
    dx, dy = math.cos(a), math.sin(a)
    h = 4.5                                   # attālums starp a un b
    m = (3.0, 0.0)
    n = (m[0] + h * dx / dy, h)
    b_sv = 0.0 if paralelas else 0.35
    punkti = [("_a1", -1, 0), ("_a2", 9, 0),
              ("_b1", -1, h - b_sv), ("_b2", 9, h + b_sv),
              ("_tu", n[0] + 1.6 * dx, n[1] + 1.6 * dy),
              ("_td", m[0] - 1.6 * dx, m[1] - 1.6 * dy),
              ("_M", m[0], m[1]), ("_N", n[0], n[1])]
    stari = {1: ("_b2", "_N", "_tu"), 2: ("_tu", "_N", "_b1"),
             3: ("_b1", "_N", "_M"), 4: ("_M", "_N", "_b2"),
             5: ("_a2", "_M", "_N"), 6: ("_N", "_M", "_a1"),
             7: ("_a1", "_M", "_td"), 8: ("_td", "_M", "_a2")}
    lenki = [(stari[i], uzraksti.get(i, str(i)), loki.get(i, 1))
             for i in radit]
    return geometrija(punkti,
                      taisnes=[("_a1", "_a2"), ("_b1", "_b2"),
                               ("_td", "_tu")],
                      lenki=lenki, virsraksts=virsraksts,
                      uzraksti=[(9.6, 0.3, "a"), (9.6, h + 0.3 + b_sv, "b"),
                                (n[0] + 2.2 * dx + 0.4, n[1] + 2.2 * dy,
                                 "c")])


def prizmas_izklajums(a, b, c, h, uzraksti=None):
    """Trijstūra prizmas virsmas izklājums: trīs sānu taisnstūri rindā un
    divi pamati pie vidējā.

    a, b, c - pamata malas, h - prizmas augstums (skaitļi zīmējuma
    proporcijām). Pamata trijstūris piestiprināts pie malas b tā, ka tā mala
    a salocoties sakrīt ar pirmā taisnstūra malu, bet c - ar trešā, tāpēc
    izklājums tiešām saliekas prizmā. uzraksti - (a, b, c, h) teksti; None -
    paši skaitļi.
    """
    a, b, c, h = float(a), float(b), float(c), float(h)
    x = (a * a - c * c + b * b) / (2.0 * b)
    y = math.sqrt(max(a * a - x * x, 0.0))
    p = {"_1": (0, 0), "_2": (a, 0), "_3": (a + b, 0), "_4": (a + b + c, 0),
         "_5": (a + b + c, h), "_6": (a + b, h), "_7": (a, h), "_8": (0, h),
         "_9": (a + x, h + y), "_0": (a + x, -y)}
    punkti = [(k, v[0], v[1]) for k, v in p.items()]
    nogr = [("_1", "_4"), ("_4", "_5"), ("_5", "_8"), ("_8", "_1"),
            ("_2", "_7"), ("_3", "_6"), ("_7", "_9"), ("_9", "_6"),
            ("_2", "_0"), ("_0", "_3")]
    krasas = [(["_1", "_2", "_7", "_8"], 0), (["_2", "_3", "_6", "_7"], 0),
              (["_3", "_4", "_5", "_6"], 0), (["_7", "_6", "_9"], 1),
              (["_2", "_3", "_0"], 1)]
    ua, ub, uc, uh = uzraksti or tuple(
        ("%g" % v).replace(".", ",") for v in (a, b, c, h))
    teksti = [(a / 2, h / 2, ua), (a + b / 2, h / 2, ub),
              (a + b + c / 2, h / 2, uc), (a + b + c + 0.9, h / 2, uh)]
    return geometrija(punkti, nogriezni=nogr, iekrasot=krasas,
                      uzraksti=teksti)


def lidzigi(virsotnes, k, burti=("A", "B", "C"), burti2=("A_1", "B_1", "C_1"),
            malas=(), malas2=(), lenki=(), atstarpe=None):
    """Divi līdzīgi trijstūri blakus: otrais ir pirmais, reizināts ar k.

    9. klases līdzības stundās šis zīmējums atkārtojas visu laiku, tāpēc to
    salikt no punktiem katrā stundā nevajag (DRY):

        lidzigi([(0, 0), (4, 0), (1, 3)], 1.5,
                malas=[(0, 1, "4")], malas2=[(0, 1, "6")],
                lenki=[(0, "α", 1), (1, "β", 2)])

    virsotnes - pirmā trijstūra virsotnes [(x, y)] * 3;
    malas, malas2 - [(i, j, uzraksts)] - mala starp i. un j. virsotni katram
    trijstūrim; lenki - [(i, uzraksts, loki)] - vienādi leņķi atzīmēti abos
    trijstūros ar tikpat lokiem. Uzraksts "" - tikai loks.
    atstarpe - brīva vieta starp trijstūriem; pēc noklusējuma tik liela, lai
    blakus stāvošie virsotņu burti (B un A_1) nesaskartos.
    """
    x_max = max(x for x, _ in virsotnes)
    x_min = min(x for x, _ in virsotnes)
    if atstarpe is None:
        atstarpe = 0.45 * (x_max - x_min)
    nobide = x_max + atstarpe - k * x_min
    otrs = [(nobide + k * x, k * y) for x, y in virsotnes]
    platums = nobide + k * x_max - x_min
    # Burtus un garumus liek prom no SAVA trijstūra centra: kopīgais centrs
    # stāv starp abiem trijstūriem un sūtītu uzrakstus tiem iekšā.
    punkti, nogriezni, uzraksti, ln = [], [], [], []
    for b, v, uz in ((burti, virsotnes, malas), (burti2, otrs, malas2)):
        cx, cy = sum(p[0] for p in v) / 3.0, sum(p[1] for p in v) / 3.0
        for burts, (x, y) in zip(b, v):
            punkti.append((burts, x, y,
                           math.degrees(math.atan2(y - cy, x - cx))))
        nogriezni += [(b[i], b[(i + 1) % 3]) for i in range(3)]
        for i, j, t in uz:
            mx, my = (v[i][0] + v[j][0]) / 2.0, (v[i][1] + v[j][1]) / 2.0
            dx, dy = mx - cx, my - cy
            g = math.hypot(dx, dy) or 1.0
            atk = 0.06 * platums
            uzraksti.append((mx + dx / g * atk, my + dy / g * atk, t))
        for i, t, loki in lenki:
            ln.append(((b[(i + 1) % 3], b[i], b[(i + 2) % 3]), t, loki))
    return geometrija(punkti, nogriezni=nogriezni, uzraksti=uzraksti,
                      lenki=ln)


TRAPECES_MALAS = ["AB", "BC", "CD", "DA"]


def trapece(apaksa, augsa, augstums, nobide=None, pedas=False,
            viduspunkti=False):
    """Trapeces ABCD punkti zīmējumam geometrija(): AB - apakšējais pamats,
    DC - augšējais, D ir virs apakšējā pamata punkta ar x = nobide.

    9.2. tematā trapeci zīmē gandrīz katrā stundā; te tā ir vienreiz (DRY):

        geometrija(trapece(10, 4, 4), nogriezni=TRAPECES_MALAS)

    nobide=None - vienādsānu trapece; 0 - taisnleņķa (AD ⊥ AB).
    pedas - augstumu pēdas H (zem D) un K (zem C);
    viduspunkti - sānu malu viduspunkti M (uz AD) un N (uz BC).
    """
    if nobide is None:
        nobide = (apaksa - augsa) / 2.0
    punkti = [("A", 0, 0), ("B", apaksa, 0),
              ("C", nobide + augsa, augstums), ("D", nobide, augstums)]
    if pedas:
        punkti += [("H", nobide, 0, -90), ("K", nobide + augsa, 0, -90)]
    if viduspunkti:
        punkti += [("M", nobide / 2.0, augstums / 2.0, 180),
                   ("N", (apaksa + nobide + augsa) / 2.0, augstums / 2.0, 0)]
    return punkti


def trapeces_prizma(apaksa, augsa, augstums, dzilums, nobide=None,
                    malas=()):
    """Taisna prizma, kuras pamats ir trapece ABCD (priekšā), aizmugurējā
    skaldne A_1B_1C_1D_1 nobīdīta slīpi augšup pa labi.

    Redzamas priekšējā skaldne, augšējā un labā sānu skaldne; šķautnes, kas
    iet no aizmugurējās kreisās apakšējās virsotnes A_1, ir punktētas - tā
    zīmē ķermeņus mācību grāmatā. malas - [(("A", "B"), uzraksts), ...].
    """
    dx, dy = 0.45 * dzilums, 0.33 * dzilums
    # Burtu virzieni ir noteikti: katrai virsotnei tur, kur no tās neiziet
    # neviena šķautne (C - uz augšu, jo pa labi augšā iet CC_1).
    virzieni = {"A": 225, "B": -90, "C": 100, "D": 180,
                "A_1": 160, "B_1": 0, "C_1": 45, "D_1": 110}
    priekša = [(p[0], p[1], p[2], virzieni[p[0]])
               for p in trapece(apaksa, augsa, augstums, nobide)]
    aizmugure = [(p[0] + "_1", p[1] + dx, p[2] + dy, virzieni[p[0] + "_1"])
                 for p in priekša]
    return geometrija(
        priekša + aizmugure,
        nogriezni=TRAPECES_MALAS + [("B", "B_1"), ("C", "C_1"),
                                    ("D", "D_1"), ("B_1", "C_1"),
                                    ("C_1", "D_1")],
        slepti=[("A", "A_1"), ("A_1", "B_1"), ("A_1", "D_1")],
        iekrasot=[("ABCD", 0)], malas=list(malas))


def taisnlenka(b, a, malas=("a", "b", "c"), lenkis="α", izcelti=(),
               burti=("A", "B", "C"), otrs=None):
    """Taisnleņķa trijstūris ABC ar ∠C = 90°, kā to zīmē latviešu mācību
    grāmatās: A kreisajā apakšā, C labajā apakšā, B virs C.

    b = AC (apakšējā katete), a = BC (vertikālā katete) - skaitļi zīmējuma
    proporcijām. malas - uzraksti (pie BC, pie AC, pie AB); None - bez
    uzraksta. lenkis - šaurā leņķa A uzraksts ("α", "30°", "" - tikai loks,
    None - bez loka); otrs - leņkim B tāpat. 9.3. tematā šis trijstūris ir
    gandrīz katrā stundā, tāpēc tas ir uzrakstīts vienreiz (DRY).
    """
    A, B, C = burti
    punkti = [(A, 0, 0, 225), (C, b, 0, -45), (B, b, a, 45)]
    uzr = [((B, C), malas[0]), ((A, C), malas[1]), ((A, B), malas[2])]
    lenki = []
    if lenkis is not None:
        lenki.append(((C, A, B), lenkis))
    if otrs is not None:
        lenki.append(((A, B, C), otrs, 2))
    return geometrija(punkti, nogriezni=[(A, C), (C, B), (B, A)],
                      taisni=[(A, C, B)], lenki=lenki,
                      malas=[(m, t) for m, t in uzr if t],
                      izcelti=list(izcelti))


def binoma_kvadrats(a=4.0, b=1.8, burti=("a", "b"), izcelt=None):
    """Kvadrāts ar malu a + b, sadalīts četrās daļās: a², ab, ab, b².

    Saīsinātās reizināšanas formulu laukuma modelis (9.4. temats). burti -
    malu uzraksti; izcelt - "a2", "ab" vai "b2": kuru daļu iekrāsot otrā
    krāsā (pārējās - pirmajā).
    """
    s = a + b
    x, y = burti
    gabali = {"a2": ("_1", "_2", "_5", "_4"), "ab1": ("_2", "_3", "_6", "_5"),
             "ab2": ("_4", "_5", "_8", "_7"), "b2": ("_5", "_6", "_9", "_8")}
    punkti = [("_%d" % (1 + i + 3 * j), [0, a, s][i], [0, a, s][j])
              for j in range(3) for i in range(3)]
    iekr = [(v, 1 if izcelt and k.startswith(izcelt) else 0)
            for k, v in gabali.items()]
    # Reizinājumu raksta kā algebrā: ab, 3x (skaitlis priekšā), 5 · 1.
    if (x + y).isalpha():
        reiz = x + y
    elif x.isdigit() != y.isdigit():
        reiz = (x + y) if x.isdigit() else (y + x)
    else:
        reiz = "%s · %s" % (x, y)
    return geometrija(
        punkti,
        nogriezni=[("_1", "_3"), ("_3", "_9"), ("_9", "_7"), ("_7", "_1"),
                   ("_2", "_8"), ("_4", "_6")],
        iekrasot=iekr,
        malas=[(("_1", "_2"), x), (("_2", "_3"), y), (("_1", "_4"), x),
               (("_4", "_7"), y)],
        uzraksti=[(a / 2, a / 2, x + "²"), (a + b / 2, a / 2, reiz),
                  (a / 2, a + b / 2, reiz), (a + b / 2, a + b / 2, y + "²")])


def uz_rinka(vards, grads, r=5.0, centrs=(0.0, 0.0)):
    """Punkts uz riņķa līnijas zīmējumam geometrija(): (vārds, x, y, virz.).

    9.8. tematā ievilktie trijstūri, hordas un pieskares punkti stāv uz
    riņķa līnijas; burts vienmēr stāv ārpusē - radiusa virzienā (DRY):

        geometrija([("O", 0, 0), uz_rinka("A", 90), uz_rinka("B", 210)],
                   rinki=[("O", 5)], nogriezni=["OA", "OB"])
    """
    a = math.radians(grads)
    return (vards, centrs[0] + r * math.cos(a), centrs[1] + r * math.sin(a),
            grads)


def regulars(n, r=5.0, burti="ABCDEFGHIJKL"):
    """Regulāra n-stūra virsotnes uz riņķa līnijas ar centru (0; 0) un malas.

    Apakšējā mala ir horizontāla, burti iet pretēji pulksteņa rādītājam no
    apakšējā kreisā stūra. Atgriež (punkti, malas) - tāpat kā trapece(),
    lai zīmējumam varētu pielikt centru, rādiusus un riņķa līnijas:

        punkti, malas = regulars(6)
        geometrija(punkti + [("O", 0, 0)], nogriezni=malas,
                   rinki=[("O", 5)])
    """
    burti = list(burti[:n])
    punkti = [uz_rinka(b, -90.0 - 180.0 / n + 360.0 * i / n, r)
              for i, b in enumerate(burti)]
    malas = [(burti[i], burti[(i + 1) % n]) for i in range(n)]
    return punkti, malas
