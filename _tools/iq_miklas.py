# -*- coding: utf-8 -*-
"""IQ mīklu ģeneratori - katrs mīklas veids ir viena funkcija.

Mīklas netiek rakstītas ar roku pa vienai: ģenerators izvēlas likumu, no tā
uzbūvē uzdevumu un pats izrēķina atbildi, tāpēc pareizā atbilde vienmēr
sakrīt ar zīmējumu, un paskaidrojums nāk no tā paša likuma (SRP). Nejaušība
ir ar sēklu, tāpēc katrs būvējums dod tās pašas lapas.

Katrs ģenerators: gen(rng, limenis) -> kārta (vārdnīca), kur limenis ir
1 (no 1. klases), 2 (no 4. klases) vai 3 (no 7. klases). Kārtas veidi:

    izvele - {jaut, zim, opcijas (HTML), pareizi, kol, skaidro}
    ievade - {jaut, zim, atb (pieņemamie pieraksti), skaidro}
    rezgis - {jaut, n, saturs (HTML rūtiņās vai None), atb (indeksi), skaidro}

Jebkurai kārtai var būt «radit» un «laiks»: to vispirms parāda uz dažām
sekundēm, tad paslēpj - tā top atmiņas uzdevumi bez atsevišķa dzinēja (DRY).

Kā kārta izskatās un kā to spēlē, zina iq_bloks.py; kā izskatās figūras -
iq_zimejumi.py.
"""

import itertools

import iq_zimejumi as Z
from math_bloki import esc
from valoda import en, t


def limenis(n):
    """Grūtības pakāpe testa lapas galvā."""
    return t({1: "no 1. klases", 2: "no 4. klases", 3: "no 7. klases"}[n],
             {1: "age 7+", 2: "age 10+", 3: "age 13+"}[n])


def teikuma(vards):
    """Vārds teikuma sākumā: latviski ar lielo burtu («Aplis sver...»);
    angliski priekšā ir «A»/«The», tāpēc vārds paliek mazs."""
    return vards if en() else vards.capitalize()


# ================================================================ palīgi
def sk(n):
    """Skaitlis latviešu pierakstā: mīnuss ir «−», nevis defise."""
    return str(n).replace("-", "−")


def txt(s):
    """Teksta atbilde pogā - aizsegta un ar matemātikas marķējumu."""
    return '<span class="iq-t">%s</span>' % esc(s)


def izvele(jaut, pareiza, citas, skaidro, zim=None, kol=None):
    """Izvēles kārta; pareizo liek pirmo, sajauc lapas būvētājs.

    Nepareizie drīkst būt vienādi savā starpā (lieks ārā - četras vienādas
    figūras), bet neviens nedrīkst sakrist ar pareizo.
    """
    if pareiza in citas:
        raise AssertionError("«%s»: nepareizs variants sakrīt ar pareizo"
                             % jaut)
    opcijas = [pareiza] + list(citas)
    k = {"veids": "izvele", "jaut": jaut, "opcijas": opcijas, "pareizi": 0,
         "skaidro": skaidro}
    if zim:
        k["zim"] = zim
    if kol:
        k["kol"] = kol
    return k


def ievade(jaut, atb, skaidro, zim=None, vieta="?"):
    atb = [a if isinstance(a, str) else sk(a)
           for a in (atb if isinstance(atb, (list, tuple)) else [atb])]
    k = {"veids": "ievade", "jaut": jaut, "atb": atb, "skaidro": skaidro,
         "vieta": vieta}
    if zim:
        k["zim"] = zim
    return k


def _atskir(rng, pareiza, kandidati, cik):
    """cik dažādi kandidāti, kas nav pareizā atbilde."""
    out = []
    kandidati = list(kandidati)
    rng.shuffle(kandidati)
    for k in kandidati:
        if k != pareiza and k not in out:
            out.append(k)
        if len(out) == cik:
            break
    if len(out) < cik:
        raise AssertionError("par maz atšķirīgu variantu")
    return out


# ======================================================= skaitļu virknes
def _v_plus(rng, lim):
    d = rng.randint(2, 5 if lim == 1 else 9)
    a = rng.randint(1, 12)
    v = [a + d * i for i in range(6)]
    return v, t("Katrs nākamais skaitlis ir par %d lielāks: %d + %d = %d.",
                "Each number is %d more than the one before: "
                "%d + %d = %d.") % (d, v[-2], d, v[-1])


def _v_minus(rng, lim):
    d = rng.randint(2, 5 if lim == 1 else 9)
    a = d * 6 + rng.randint(0, 10)
    v = [a - d * i for i in range(6)]
    return v, t("Katrs nākamais skaitlis ir par %d mazāks: %d − %d = %d.",
                "Each number is %d less than the one before: "
                "%d − %d = %d.") % (d, v[-2], d, v[-1])


def _v_divreiz(rng, lim):
    a = rng.randint(1, 3)
    v = [a * 2 ** i for i in range(6)]
    return v, t("Katrs nākamais skaitlis ir divreiz lielāks: %d · 2 = %d.",
                "Each number is twice the one before: %d · 2 = %d.") % (
        v[-2], v[-1])


def _v_augosi(rng, lim):
    a, d = rng.randint(1, 10), rng.randint(1, 2)
    v = [a]
    for i in range(1, 6):
        v.append(v[-1] + d * i)
    soli = ", ".join("+%d" % (d * i) for i in range(1, 6))
    return v, t("Soļi aug: %s. Tāpēc %d + %d = %d.",
                "The steps grow: %s. So %d + %d = %d.") % (
        soli, v[-2], d * 5, v[-1])


def _v_mainigi(rng, lim):
    a, b = rng.randint(4, 9), rng.randint(1, 3)
    v = [rng.randint(3, 15)]
    for i in range(7):
        v.append(v[-1] + (a if i % 2 == 0 else -b))
    return v, t("Pārmaiņus +%d un −%d. Pēdējais solis ir +%d: %d + %d = %d.",
                "Alternately +%d and −%d. The last step is +%d: "
                "%d + %d = %d.") % (a, b, a, v[-2], a, v[-1])


def _v_trisreiz(rng, lim):
    a = rng.randint(1, 2)
    v = [a * 3 ** i for i in range(6)]
    return v, t("Katrs nākamais skaitlis ir trīsreiz lielāks: %d · 3 = %d.",
                "Each number is three times the one before: "
                "%d · 3 = %d.") % (v[-2], v[-1])


def _v_kvadrati(rng, lim):
    n = rng.randint(1, 4)
    v = [(n + i) ** 2 for i in range(6)]
    return v, t("Tie ir kvadrāti: %d² = %d, ..., %d² = %d.",
                "They are squares: %d² = %d, ..., %d² = %d.") % (
        n, v[0], n + 5, v[-1])


def _v_divas(rng, lim):
    a, b = rng.randint(1, 5), rng.randint(20, 30)
    da, db = rng.randint(2, 4), -rng.randint(1, 3)
    v = []
    for i in range(4):
        v += [a + da * i, b + db * i]
    return v, (t("Tās ir divas virknes pamīšus: %s (+%d) un %s (−%d). "
                 "Trūkst otrās virknes skaitļa: %d.",
                 "Two sequences take turns: %s (+%d) and %s (−%d). "
                 "The missing number belongs to the second one: %d.") % (
                   ", ".join(sk(x) for x in v[0::2]), da,
                   ", ".join(sk(x) for x in v[1::2]), -db, v[-1]))


def _v_puse(rng, lim):
    a = rng.choice([3, 5, 7]) * 2 ** 5
    v = [a // 2 ** i for i in range(6)]
    return v, t("Katrs nākamais skaitlis ir divreiz mazāks: %d : 2 = %d.",
                "Each number is half the one before: %d : 2 = %d.") % (
        v[-2], v[-1])


def _v_fibonaci(rng, lim):
    v = [rng.randint(1, 4), rng.randint(1, 5)]
    while len(v) < 8:
        v.append(v[-1] + v[-2])
    return v, (t("Katrs skaitlis ir divu iepriekšējo summa: %d + %d = %d. "
                 "Tā aug Fibonači virkne - tā slēpjas arī saulespuķu "
                 "sēklās.",
                 "Each number is the sum of the two before it: "
                 "%d + %d = %d. That is how the Fibonacci sequence grows - "
                 "it hides in sunflower seeds too.") % (v[-3], v[-2], v[-1]))


def _v_kubi(rng, lim):
    n = rng.randint(1, 2)
    v = [(n + i) ** 3 for i in range(5)]
    return v, t("Tie ir kubi: %d³ = %d, ..., %d³ = %d.",
                "They are cubes: %d³ = %d, ..., %d³ = %d.") % (
        n, v[0], n + 4, v[-1])


_PIRM = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]


def _v_pirmskaitli(rng, lim):
    i = rng.randint(0, 6)
    v = _PIRM[i:i + 7]
    return v, (t("Tie ir pirmskaitļi - dalās tikai ar 1 un ar sevi. Pēc %d "
                 "nākamais pirmskaitlis ir %d.",
                 "They are primes - divisible only by 1 and themselves. "
                 "After %d the next prime is %d.") % (v[-2], v[-1]))


def _v_trijstura(rng, lim):
    v = [n * (n + 1) // 2 for n in range(1, 8)]
    return v, (t("Soļi aug par vienu: +2, +3, +4, ... Pēdējais solis ir "
                 "+7: %d + 7 = %d.",
                 "The steps grow by one: +2, +3, +4, ... The last step is "
                 "+7: %d + 7 = %d.") % (v[-2], v[-1]))


def _v_reizpluss(rng, lim):
    a = rng.randint(1, 3)
    p = rng.choice([1, -1]) if lim == 3 else 1
    if a == 1 and p == -1:
        a = 2
    v = [a]
    for _ in range(5):
        v.append(2 * v[-1] + p)
    zime = "+ 1" if p == 1 else "− 1"
    return v, t("Reizina ar 2 un %s: %d · 2 %s = %d.",
                "Multiply by 2 and %s: %d · 2 %s = %d.") % (
        t("pieskaita 1", "add 1") if p == 1 else t("atņem 1", "subtract 1"),
        v[-2], zime, v[-1])


def _v_dubultsoli(rng, lim):
    v = [rng.randint(1, 9)]
    for i in range(6):
        v.append(v[-1] + 2 ** i)
    return v, t("Soļi dubultojas: +1, +2, +4, +8, +16, +32. %d + 32 = %d.",
                "The steps double: +1, +2, +4, +8, +16, +32. "
                "%d + 32 = %d.") % (v[-2], v[-1])


def _v_negativi(rng, lim):
    d = rng.randint(3, 7)
    a = rng.randint(5, 12)
    v = [a - d * i for i in range(6)]
    return v, t("Katrs nākamais ir par %d mazāks - arī aiz nulles: "
                "%s − %d = %s.",
                "Each number is %d less - even past zero: "
                "%s − %d = %s.") % (d, sk(v[-2]), d, sk(v[-1]))


VIRKNES = {
    1: [_v_plus, _v_minus, _v_divreiz, _v_plus],
    2: [_v_augosi, _v_mainigi, _v_trisreiz, _v_kvadrati, _v_divas, _v_puse,
        _v_negativi],
    3: [_v_fibonaci, _v_kubi, _v_pirmskaitli, _v_trijstura, _v_reizpluss,
        _v_dubultsoli, _v_divas, _v_kvadrati],
}


# Likumi pēc nosaukuma - testu plānā (iq_testi.py) raksta vārdu.
VIRKNU_LIKUMI = {
    "plus": _v_plus, "minus": _v_minus, "divreiz": _v_divreiz,
    "augosi": _v_augosi, "mainigi": _v_mainigi, "trisreiz": _v_trisreiz,
    "kvadrati": _v_kvadrati, "divas": _v_divas, "puse": _v_puse,
    "fibonaci": _v_fibonaci, "kubi": _v_kubi, "pirmskaitli": _v_pirmskaitli,
    "trijstura": _v_trijstura, "reizpluss": _v_reizpluss,
    "dubultsoli": _v_dubultsoli, "negativi": _v_negativi,
}


def virkne(rng, lim, likums=None):
    """Skaitļu virkne - atrodi nākamo skaitli."""
    f = VIRKNU_LIKUMI[likums] if likums else rng.choice(VIRKNES[lim])
    v, skaidro = f(rng, lim)
    return ievade(t("Kurš skaitlis ir nākamais?",
                    "Which number comes next?"), v[-1], skaidro,
                  zim=Z.flizes([sk(x) for x in v[:-1]] + [None]))


# ========================================================= figūru matricas
_M_FORMAS = ["aplis", "kvadrats", "trijsturis", "zvaigzne", "sessturis",
             "rombs", "krusts"]
_M_KRASAS = ["violets", "oranzs", "zils", "zals", "roza"]
_M_PILD = ["pilns", "gaiss", "tukss"]

# pazīme: (vārds, visas vērtības kopā)
_PAZIMES = {"forma": ("figūra", "visas trīs figūras"),
            "krasa": ("krāsa", "visas trīs krāsas"),
            "skaits": ("figūru skaits", "visi trīs skaiti"),
            "pild": ("aizkrāsojums", "visi trīs aizkrāsojumi"),
            "rot": ("bultas virziens", "visi trīs virzieni")}
_PAZIMES_EN = {"forma": ("the shape", "all three shapes"),
               "krasa": ("the colour", "all three colours"),
               "skaits": ("the number of shapes", "all three counts"),
               "pild": ("the fill", "all three fills"),
               "rot": ("the arrow's direction", "all three directions")}


def vards_saraksts(v):
    v = list(v)
    return v[0] if len(v) == 1 else "%s %s %s" % (
        ", ".join(v[:-1]), t("un", "and"), v[-1])


def _vertibas_teksts(pazime, vert):
    f = {"forma": Z.vards, "krasa": Z.krasa, "skaits": str,
         "pild": Z.pildijums, "rot": lambda v: "%d°" % v}
    return vards_saraksts(f[pazime](v) for v in vert)


def _likums_teksts(pazime, likums, vert):
    nos, visas = (_PAZIMES_EN if en() else _PAZIMES)[pazime]
    vt = _vertibas_teksts(pazime, vert)
    if likums == "kolonna":
        return t("Pa labi mainās %s: %s.",
                 "Left to right, %s changes: %s.") % (nos, vt)
    if likums == "rinda":
        return t("Uz leju mainās %s: %s.",
                 "Top to bottom, %s changes: %s.") % (nos, vt)
    return t("Katrā rindā un kolonnā ir %s: %s.",
             "Every row and column has %s: %s.") % (visas, vt)


def _indekss(likums, r, c, n):
    return {"kolonna": c, "rinda": r, "latins": (r + c) % n,
            "latins2": (c - r) % n}[likums]


def matrica(rng, lim, n=None, bulta=None):
    """Figūru matrica: kas iet tukšajā rūtiņā?

    n - 2 (analoģija 2 × 2) vai 3; bulta - vai viena no pazīmēm ir bultas
    virziens (None - kā sanāk).
    """
    n = n or (2 if lim == 1 and rng.random() < 0.4 else 3)
    cik = {1: 1, 2: 2, 3: 3}[lim] if n == 3 else 2
    varbut = ["forma", "krasa", "skaits", "pild"]
    ar_bultu = bulta if bulta is not None else (lim >= 2
                                                and rng.random() < 0.3)
    if ar_bultu:
        varbut = ["rot", "krasa", "skaits", "pild"]
    mainas = rng.sample(varbut, cik)
    if ar_bultu and "rot" not in mainas:
        mainas[0] = "rot"
    if n == 2:
        likumi = {mainas[0]: "kolonna", mainas[1]: "rinda"}
    else:
        visi = ["kolonna", "rinda", "latins", "latins2"]
        likumi = {}
        for i, p in enumerate(mainas):
            likumi[p] = rng.choice(visi if lim > 1 else ["kolonna", "latins"])
        # divi latīņu kvadrāti ar vienādu likumu atkārto viens otru
        if list(likumi.values()).count("latins") > 1:
            for p in mainas[1:]:
                if likumi[p] == "latins":
                    likumi[p] = "latins2"
    domenes = {"forma": rng.sample(_M_FORMAS, n),
               "krasa": rng.sample(_M_KRASAS, n),
               "skaits": [1, 2, 3][:n] if lim < 3 else rng.choice(
                   [[1, 2, 3], [2, 3, 4], [1, 3, 5]])[:n],
               "pild": rng.sample(_M_PILD, n),
               "rot": rng.choice([[0, 90, 180], [0, 45, 90],
                                  [270, 0, 90]])[:n]}
    pamats = {"forma": "bulta" if ar_bultu else rng.choice(_M_FORMAS),
              "krasa": rng.choice(_M_KRASAS), "skaits": 1, "pild": "pilns",
              "rot": 0}

    def rutina(r, c):
        s = dict(pamats)
        for p, lk in likumi.items():
            s[p] = domenes[p][_indekss(lk, r, c, n)]
        return s

    sunas = [rutina(r, c) for r in range(n) for c in range(n)]
    pareiza = sunas[-1]
    # Kļūdainie varianti: pareizā rūtiņa ar vienu vai divām samainītām
    # pazīmēm - tā tie izskatās ticami, bet katrs lauž kādu likumu.
    kandidati = []
    for p in ["forma", "krasa", "skaits", "pild"] + (["rot"] if ar_bultu
                                                     else []):
        if p == "forma" and ar_bultu:
            continue
        dom = domenes[p] if p in likumi else domenes[p][:2] + [
            {"forma": "sessturis" if pamats["forma"] != "sessturis"
             else "aplis", "krasa": "roza" if pamats["krasa"] != "roza"
             else "zals", "skaits": 2, "pild": "tukss", "rot": 180}[p]]
        for v in dom:
            if v != pareiza[p]:
                s = dict(pareiza)
                s[p] = v
                kandidati.append(s)
    for a, b in itertools.combinations(list(likumi), 2):
        for va in domenes[a]:
            for vb in domenes[b]:
                s = dict(pareiza, **{a: va, b: vb})
                kandidati.append(s)
    kandidati = [k for k in kandidati if k != pareiza]
    unik = []
    for k in kandidati:
        if k not in unik:
            unik.append(k)
    citi = _atskir(rng, pareiza, unik, 3 if lim == 1 else 5)
    skaidro = " ".join(_likums_teksts(p, likumi[p], domenes[p])
                       for p in mainas)
    return izvele(t("Kura figūra iet tukšajā rūtiņā?",
                    "Which picture goes in the empty cell?"),
                  Z.suna(pareiza),
                  [Z.suna(c) for c in citi], skaidro,
                  zim=Z.matrica(sunas[:-1] + [None], n), kol=3)


# ============================================================ lieks ārā
def _lieks_figuras(rng, lim):
    veids = rng.choice({1: ["forma", "krasa"], 2: ["skaits", "pild", "forma"],
                        3: ["spogulis", "skaits"]}[lim])
    if veids == "spogulis":
        return _lieks_spogulis(rng)
    krasa, forma = rng.choice(_M_KRASAS), rng.choice(_M_FORMAS)
    formas = rng.sample(_M_FORMAS, 5)
    if veids == "forma":
        cita = rng.choice([f for f in _M_FORMAS if f != forma])
        if lim == 1:
            vienadas = [{"forma": forma, "krasa": krasa}] * 4
            lieka = {"forma": cita, "krasa": krasa}
        else:
            # Divas krāsas, katra vismaz divreiz: krāsa atbildi nenodod,
            # jāskatās forma.
            k1, k2 = rng.sample(_M_KRASAS, 2)
            vienadas = [{"forma": forma, "krasa": k}
                        for k in (k1, k1, k2, k2)]
            lieka = {"forma": cita, "krasa": rng.choice((k1, k2))}
        skaidro = t("Visas pārējās figūras ir %s, bet šī ir %s.",
                    "All the others are %s, but this one is a %s.") % (
            Z.vards(forma, Z.DSK), Z.vards(cita))
    elif veids == "krasa":
        cita = rng.choice([k for k in _M_KRASAS if k != krasa])
        vienadas = [{"forma": forma, "krasa": krasa}] * 4
        lieka = {"forma": forma, "krasa": cita}
        skaidro = t("Visām pārējām krāsa ir %s, bet šai - %s.",
                    "All the others are %s, but this one is %s.") % (
            Z.krasa(krasa), Z.krasa(cita))
    elif veids == "skaits":
        n, m = rng.choice([(3, 4), (4, 3), (2, 3), (4, 5)])
        vienadas = [{"forma": f, "krasa": krasa, "skaits": n}
                    for f in formas[:4]]
        lieka = {"forma": formas[4], "krasa": krasa, "skaits": m}
        skaidro = t("Forma te neko nenozīmē. Visās pārējās ir %d "
                    "figūras, bet šajā - %d.",
                    "The shape doesn't matter here. All the others have %d "
                    "shapes, but this one has %d.") % (n, m)
    else:
        p, cita = rng.sample(_M_PILD, 2)
        vienadas = [{"forma": f, "krasa": krasa, "pild": p}
                    for f in formas[:4]]
        lieka = {"forma": formas[4], "krasa": krasa, "pild": cita}
        skaidro = t("Formas visas ir dažādas - tās nav pavediens. Visas "
                    "pārējās ir %s, bet šī - %s.",
                    "The shapes are all different - they are not the clue. "
                    "All the others are %s, but this one is %s.") % (
                        Z.pildijums(p), Z.pildijums(cita))
    return izvele(_lieka(), Z.suna(lieka),
                  [Z.suna(v) for v in vienadas], skaidro, kol=5)


def _lieka():
    return t("Kura figūra ir lieka?", "Which picture is the odd one out?")


def _lieks_spogulis(rng):
    fig = _hirala(rng, 5)
    kr = rng.choice(_M_KRASAS)
    pagr = [_norm(_rot(fig, k)) for k in range(4)]
    lieka = _norm(_rot(_spog(fig), rng.randint(0, 3)))
    return izvele(_lieka(), Z.poliomino(lieka, kr),
                  [Z.poliomino(p, kr) for p in pagr],
                  t("Četras ir viena un tā pati figūra, tikai pagriezta. "
                    "Liekā ir tās spoguļattēls - to ar pagriešanu vien "
                    "nevar dabūt.",
                    "Four are the same shape, just turned. The odd one is "
                    "its mirror image - you can't get it by turning."),
                  kol=5)


def _lieks_skaitli(rng, lim):
    if lim == 1:
        para = rng.sample(range(2, 40, 2), 4)
        lieka = rng.choice(range(3, 40, 2))
        return para, lieka, t("Visi pārējie ir pāra skaitļi - dalās ar 2. "
                              "%d ir nepāra.",
                              "All the others are even - divisible by 2. "
                              "%d is odd.") % lieka
    if lim == 2:
        d = rng.choice([3, 4, 5, 9])
        visi = rng.sample(range(d * 2, d * 12, d), 4)
        lieka = rng.choice([x for x in range(d * 2 + 1, d * 12)
                            if x % d and x % 2 == visi[0] % 2])
        return visi, lieka, t("Visi pārējie dalās ar %d. %d ar %d nedalās.",
                              "All the others are divisible by %d. %d is "
                              "not divisible by %d.") % (d, lieka, d)
    if rng.random() < 0.5:
        pirm = rng.sample([p for p in _PIRM if p > 10], 4)
        lieka = rng.choice([51, 57, 87, 91, 49, 39])
        dal = next(x for x in range(3, lieka) if lieka % x == 0)
        return pirm, lieka, t("Visi pārējie ir pirmskaitļi. %d tikai "
                              "izskatās pēc pirmskaitļa: %d = %d · %d.",
                              "All the others are primes. %d only looks "
                              "like one: %d = %d · %d.") % (
                                  lieka, lieka, dal, lieka // dal)
    kv = rng.sample([n * n for n in range(4, 16)], 4)
    lieka = rng.choice([n * n + rng.choice([-1, 1]) for n in range(5, 15)])
    return kv, lieka, (t("Visi pārējie ir kvadrāti (%s). %d nav neviena "
                         "vesela skaitļa kvadrāts.",
                         "All the others are squares (%s). %d is not the "
                         "square of any whole number.") % (
                           ", ".join("%d = %d²" % (x, int(x ** .5))
                                     for x in kv), lieka))


def lieks(rng, lim, ko=None):
    """Lieks ārā: figūras vai skaitļi."""
    ko = ko or rng.choice(["figuras", "figuras", "skaitli"])
    if ko == "figuras":
        return _lieks_figuras(rng, lim)
    visi, lieka, skaidro = _lieks_skaitli(rng, lim)
    return izvele(t("Kurš skaitlis ir lieks?",
                    "Which number is the odd one out?"), txt(sk(lieka)),
                  [txt(sk(x)) for x in visi], skaidro, kol=5)


# ============================================================ poliomino
def _norm(sunas):
    rs = min(r for r, _ in sunas)
    cs = min(c for _, c in sunas)
    return tuple(sorted((r - rs, c - cs) for r, c in sunas))


def _rot(sunas, k=1):
    for _ in range(k % 4):
        sunas = [(c, -r) for r, c in sunas]
    return _norm(sunas)


def _spog(sunas):
    return _norm([(r, -c) for r, c in sunas])


def _hirala(rng, n):
    """Nejauša figūra no n rūtiņām, kuras spoguļattēlu nevar iegūt,
    to tikai pagriežot - citādi «pagriezta» un «spogulī» sakristu."""
    while True:
        sunas = {(0, 0)}
        while len(sunas) < n:
            r, c = rng.choice(sorted(sunas))
            dr, dc = rng.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
            sunas.add((r + dr, c + dc))
        fig = _norm(sunas)
        pagr = {_rot(fig, k) for k in range(4)}
        if _spog(fig) not in pagr and len(pagr) == 4:
            return fig


def rotacija(rng, lim):
    """Kura figūra ir tā pati, tikai pagriezta?"""
    fig = _hirala(rng, {1: 4, 2: 5, 3: 6}[lim])
    kr = rng.choice(_M_KRASAS)
    pareiza = _rot(fig, rng.randint(1, 3))
    spog = [_rot(_spog(fig), k) for k in range(4)]
    citi = _atskir(rng, pareiza, spog, 3)
    return izvele(t("Kura figūra ir šī pati, tikai pagriezta?",
                    "Which shape is this one, just turned?"),
                  Z.poliomino(pareiza, kr), [Z.poliomino(c, kr) for c in citi],
                  t("Pareizo var pagriezt atpakaļ un uzlikt virsū paraugam. "
                    "Pārējās ir apgrieztas otrādi - kā spogulī.",
                    "The right one can be turned back to fit exactly on the "
                    "original. The others are flipped - like in a mirror."),
                  zim='<div class="iq-viena">%s</div>' % Z.poliomino(fig, kr),
                  kol=4)


def spogulis(rng, lim):
    """Kā figūra izskatās spogulī?"""
    fig = _hirala(rng, {1: 4, 2: 5, 3: 6}[lim])
    kr = rng.choice(_M_KRASAS)
    pareiza = _spog(fig)
    visas = [_rot(fig, k) for k in range(4)] + [_rot(pareiza, k)
                                                for k in range(1, 4)]
    citi = _atskir(rng, pareiza, visas, 3)
    return izvele(t("Kā šī figūra izskatās spogulī?",
                    "What does this shape look like in the mirror?"),
                  Z.poliomino(pareiza, kr),
                  [Z.poliomino(c, kr) for c in citi],
                  t("Spogulī kreisā puse kļūst par labo, bet augša paliek "
                    "augšā - tāpat kā tavs atspulgs.",
                    "In a mirror left becomes right, but the top stays on "
                    "top - just like your reflection."),
                  zim=Z.ar_spoguli(Z.poliomino(fig, kr)), kol=4)


# ============================================================ kubu kaudze
def _kaudze(rng, rindas, kol, maks):
    """Augstumi, kas uz priekšu un pa labi nepieaug - tad katrs stabiņš ir
    redzams un kubus var saskaitīt bez minēšanas."""
    h = [[0] * kol for _ in range(rindas)]
    for i in range(rindas):
        for j in range(kol):
            aug = maks
            if i:
                aug = min(aug, h[i - 1][j])
            if j:
                aug = min(aug, h[i][j - 1])
            h[i][j] = rng.randint(1, max(1, aug))
    return h


def kubi(rng, lim):
    """Cik kubu kaudzē?"""
    rindas, kol, maks = {1: (2, 2, 2), 2: (2, 3, 3), 3: (3, 3, 3)}[lim]
    h = _kaudze(rng, rindas, kol, maks)
    kopa = sum(map(sum, h))
    stab = " + ".join(str(x) for r in h for x in r)
    if lim == 3 and rng.random() < 0.5:
        trukst = 27 - kopa
        return ievade(t("Cik kubu vēl vajag, lai sanāktu liels kubs "
                        "3 × 3 × 3?",
                        "How many more cubes make a big 3 × 3 × 3 cube?"),
                      trukst, t("Kaudzē ir %s = %d kubi. Lielajā kubā ir "
                                "3 · 3 · 3 = 27, tātad trūkst 27 − %d = %d.",
                                "The stack has %s = %d cubes. The big cube "
                                "has 3 · 3 · 3 = 27, so 27 − %d = %d are "
                                "missing.")
                      % (stab, kopa, kopa, trukst), zim=Z.kubi(h))
    return ievade(t("Cik kubu ir kaudzē? Neviens kubs nekarājas gaisā.",
                    "How many cubes are in the stack? No cube floats in "
                    "the air."), kopa,
                  t("Skaitām pa stabiņiem: %s = %d.",
                    "Count column by column: %s = %d.") % (stab, kopa),
                  zim=Z.kubi(h))


# ============================================================ kuba tīkls
# Visi 11 kuba izklājumi (rinda, kolonna).
TIKLI = [
    [(0, 1), (1, 0), (1, 1), (1, 2), (1, 3), (2, 1)],
    [(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0)],
    [(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 1)],
    [(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 2)],
    [(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 3)],
    [(0, 1), (1, 0), (1, 1), (1, 2), (1, 3), (2, 2)],
    [(0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (2, 3)],
    [(0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (2, 2)],
    [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 3)],
    [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3), (1, 4)],
    [(0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (2, 1)],
]

_RIPO = {  # kur nonāk skaldnes, kubam apveļoties uz to pusi
    (0, 1): lambda o: dict(o, apak=o["aust"], aust=o["augs"],
                           augs=o["rietu"], rietu=o["apak"]),
    (0, -1): lambda o: dict(o, apak=o["rietu"], rietu=o["augs"],
                            augs=o["aust"], aust=o["apak"]),
    (1, 0): lambda o: dict(o, apak=o["dienv"], dienv=o["augs"],
                           augs=o["zieme"], zieme=o["apak"]),
    (-1, 0): lambda o: dict(o, apak=o["zieme"], zieme=o["augs"],
                            augs=o["dienv"], dienv=o["apak"]),
}
_PRETI = [("apak", "augs"), ("aust", "rietu"), ("zieme", "dienv")]


def salocit(sunas):
    """Kuba skaldne katrai tīkla rūtiņai: kubu veļ pa tīklu, un rūtiņa
    kļūst par to skaldni, kas tobrīd ir apakšā."""
    sakums = {k: k for k in ("apak", "augs", "aust", "rietu", "zieme",
                             "dienv")}
    skaldne, redz = {}, set()

    def iet(suna, o):
        redz.add(suna)
        skaldne[suna] = o["apak"]
        for (dr, dc), f in _RIPO.items():
            cita = (suna[0] + dr, suna[1] + dc)
            if cita in sunas and cita not in redz:
                iet(cita, f(o))
    iet(sunas[0], sakums)
    if len(set(skaldne.values())) != 6:
        raise AssertionError("tīkls nesalokās kubā: %s" % (sunas,))
    return skaldne


def pretejas(sunas):
    """{rūtiņa: pretējā rūtiņa} salocītā kubā."""
    sk_ = salocit(sunas)
    pec = {v: k for k, v in sk_.items()}
    out = {}
    for a, b in _PRETI:
        out[pec[a]], out[pec[b]] = pec[b], pec[a]
    return out


_T_FORMAS = ["aplis", "kvadrats", "trijsturis", "zvaigzne", "krusts",
             "sessturis"]


def tikls(rng, lim):
    """Kura skaldne būs pretī?"""
    sunas = list(rng.choice(TIKLI[:2] if lim == 1 else
                            TIKLI[:6] if lim == 2 else TIKLI[5:]))
    formas = rng.sample(_T_FORMAS, 6)
    krasas = [rng.choice(_M_KRASAS) for _ in range(6)]
    simb = dict(zip(sunas, zip(formas, krasas)))
    pr = pretejas(sunas)
    jaut_suna = rng.choice(sunas)
    pret = pr[jaut_suna]
    f, k = simb[jaut_suna]
    citas = [s for s in sunas if s not in (jaut_suna, pret)]
    citas = rng.sample(citas, 3)
    pf = simb[pret]
    return izvele(t("Saloki kubu. Kas būs pretī %s?",
                    "Fold the cube. What will be opposite the %s?")
                  % Z.vards(f, Z.DAT),
                  Z.simbols(*pf), [Z.simbols(*simb[s]) for s in citas],
                  t("%s un %s nekad nesaskaras: salokot kubu, šīs skaldnes "
                    "nonāk pretējās pusēs. Tīklā starp pretējām skaldnēm "
                    "vienmēr ir vismaz viena cita.",
                    "The %s and the %s never touch: when the cube is folded, these "
                    "faces end up on opposite sides. In the net there is "
                    "always at least one face between opposite faces.") % (
                      teikuma(Z.vards(f)), Z.vards(pf[0])),
                  zim=Z.tikls(sunas, [simb[s] for s in sunas]), kol=4)


# ===================================================== simbolu vienādojumi
def simboli(rng, lim):
    """Figūras slēpj skaitļus - atšifrē!"""
    trio = list(zip(rng.sample(["aplis", "kvadrats", "trijsturis",
                                "zvaigzne", "sessturis"], 3),
                    rng.sample(_M_KRASAS, 3)))
    A, B, C = trio
    if lim == 1:
        a, b = rng.randint(2, 9), rng.randint(1, 9)
        rindas = [[A, "+", A, "=", sk(2 * a)], [A, "+", B, "=", sk(a + b)],
                  [B, "=", "?"]]
        return ievade(t("Kādu skaitli slēpj figūra?",
                        "Which number is hidden behind the shape?"), b,
                      t("No pirmās rindas %s = %d : 2 = %d. Tad %s = %d − %d "
                        "= %d.",
                        "From the first line %s = %d : 2 = %d. Then "
                        "%s = %d − %d = %d.")
                      % (Z.vards(A[0]), 2 * a, a, Z.vards(B[0]), a + b, a, b),
                      zim=Z.vienadojumi(rindas))
    if lim == 2:
        a, b, c = rng.randint(2, 7), rng.randint(2, 9), rng.randint(1, 9)
        rindas = [[A, "+", A, "+", A, "=", sk(3 * a)],
                  [A, "+", B, "=", sk(a + b)], [B, "+", C, "=", sk(b + c)],
                  [C, "+", A, "=", "?"]]
        return ievade(t("Kādu skaitli slēpj pēdējā rinda?",
                        "Which number is hidden in the last line?"), c + a,
                      t("%s = %d, %s = %d, %s = %d. Tātad %d + %d = %d.",
                        "%s = %d, %s = %d, %s = %d. So %d + %d = %d.")
                      % (Z.vards(A[0]).capitalize(), a, Z.vards(B[0]), b,
                         Z.vards(C[0]),
                         c, c, a, c + a), zim=Z.vienadojumi(rindas))
    a, b, c = rng.randint(2, 6), rng.randint(2, 6), rng.randint(2, 5)
    rindas = [[A, "·", A, "=", sk(a * a)], [A, "+", B, "=", sk(a + b)],
              [B, "·", C, "=", sk(b * c)], [A, "+", B, "·", C, "=", "?"]]
    return ievade(t("Kādu skaitli slēpj pēdējā rinda? Atceries darbību "
                    "secību!",
                    "Which number is hidden in the last line? Mind the "
                    "order of operations!"), a + b * c,
                  t("%s = %d, %s = %d, %s = %d. Reizināšana ir pirms "
                    "saskaitīšanas: %d + %d · %d = %d + %d = %d.",
                    "%s = %d, %s = %d, %s = %d. Multiplication comes before "
                    "addition: %d + %d · %d = %d + %d = %d.")
                  % (Z.vards(A[0]).capitalize(), a, Z.vards(B[0]), b,
                     Z.vards(C[0]), c, a, b, c, a, b * c, a + b * c),
                  zim=Z.vienadojumi(rindas))


# ================================================================== svari
def _svari_jaut():
    return t("Cik %s jāliek «?» vietā?",
             "How many %s replace the question mark?")


def svari(rng, lim):
    """Līdzsvara mīkla: cik figūru jāliek «?» vietā?"""
    trio = list(zip(rng.sample(["aplis", "kvadrats", "trijsturis",
                                "zvaigzne"], 3), rng.sample(_M_KRASAS, 3)))
    A, B, C = trio
    a_, b_ = Z.vards(A[0]), Z.vards(B[0])
    bd, cd = Z.vards(B[0], Z.DSK), Z.vards(C[0], Z.DSK)
    if lim == 1:
        m, k = rng.randint(2, 3), rng.randint(2, 3)
        zim = Z.svari([A], [B] * m) + Z.svari([A] * k, "?")
        return ievade(_svari_jaut() % Z.vards(B[0], Z.GEN),
                      m * k, t("%s sver tikpat, cik %d %s. Tātad %d %s sver "
                               "tikpat, cik %d · %d = %d %s.",
                               "A %s weighs as much as %d %s. So %d %s "
                               "weigh as much as %d · %d = %d %s.") % (
                          teikuma(a_), m, bd, k,
                          Z.vards(A[0], Z.DSK), k, m, m * k, bd), zim=zim)
    if lim == 2:
        m, n = rng.randint(2, 3), rng.randint(2, 3)
        zim = (Z.svari([A], [B] * m) + Z.svari([B], [C] * n)
               + Z.svari([A], "?"))
        return ievade(_svari_jaut() % Z.vards(C[0], Z.GEN),
                      m * n, t("%s = %d %s, un katrs %s = %d %s. Tātad "
                               "%d · %d = %d.",
                               "A %s = %d %s, and each %s = %d %s. So "
                               "%d · %d = %d.")
                      % (teikuma(a_), m, bd, b_, n, cd, m, n, m * n),
                      zim=zim)
    b, a = rng.randint(2, 3), rng.randint(2, 3)
    kopa = a + b
    zim = (Z.svari([B], [C] * b) + Z.svari([A, B], [C] * kopa)
           + Z.svari([A, A, B], "?"))
    return ievade(_svari_jaut() % Z.vards(C[0], Z.GEN),
                  2 * a + b, t("%s = %d %s. No otrajiem svariem %s = %d − %d "
                               "= %d %s. Tātad 2 · %d + %d = %d.",
                               "A %s = %d %s. From the second scale a "
                               "%s = %d − %d = %d %s. So 2 · %d + %d = %d.")
                  % (
                      teikuma(b_), b, cd, a_, kopa, b, a, cd, a, b,
                      2 * a + b), zim=zim)


# ===================================================== piramīda un kvadrāts
def piramida(rng, lim):
    """Katrs bloks ir abu zem tā esošo summa."""
    n = 3 if lim == 1 else 4
    apaksa = [rng.randint(1, 9 if lim == 1 else 12) for _ in range(n)]
    rindas = [apaksa]
    while len(rindas[-1]) > 1:
        r = rindas[-1]
        rindas.append([r[i] + r[i + 1] for i in range(len(r) - 1)])
    rindas.reverse()                               # augšējā rinda pirmā
    radit = [[sk(x) for x in r] for r in rindas]
    jaut = t("Katrs bloks ir abu zem tā esošo summa. ",
             "Each block is the sum of the two below it. ")
    apaksa_j = t("Kas slēpjas apakšā?", "What is hidden at the bottom?")
    if lim == 1:
        radit[0][0] = None
        return ievade(jaut + t("Kas ir virsotnē?", "What is at the top?"),
                      rindas[0][0],
                      "%d + %d = %d." % (rindas[1][0], rindas[1][1],
                                         rindas[0][0]),
                      zim=Z.piramida(radit))
    j = rng.randint(0, n - 1)
    radit[-1][j] = None
    if lim == 2:
        # Virs trūkstošā ir bloks, un blakus tam - kaimiņš: viena atņemšana.
        vecaks = rindas[-2][j - 1 if j else 0]
        kaimins = apaksa[j - 1] if j else apaksa[1]
        return ievade(jaut + apaksa_j, apaksa[j],
                      t("Bloks virs tā ir %d, blakus stāv %d: %d − %d = %d.",
                        "The block above it is %d, its neighbour is %d: "
                        "%d − %d = %d.")
                      % (vecaks, kaimins, vecaks, kaimins, apaksa[j]),
                      zim=Z.piramida(radit))
    # Redzama tikai virsotne un apakša - vidus jāizdomā pašam.
    for r in radit[1:-1]:
        for i in range(len(r)):
            r[i] = ""
    koef = [1, 3, 3, 1]
    zin = sum(koef[i] * apaksa[i] for i in range(n) if i != j)
    return ievade(jaut + apaksa_j, apaksa[j],
                  t("Virsotnē apakšējie skaitļi sanāk ar svariem 1, 3, 3, 1. "
                    "Zināmie dod %d, tātad trūkstošais ir (%d − %d) : %d = %d.",
                    "The bottom numbers reach the top with weights "
                    "1, 3, 3, 1. The known ones give %d, so the missing one "
                    "is (%d − %d) : %d = %d.")
                  % (zin, rindas[0][0], zin, koef[j], apaksa[j]),
                  zim=Z.piramida(radit))


_LO_SHU = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]


def magiskais(rng, lim):
    """Maģiskais kvadrāts: visas rindas, kolonnas un diagonāles vienādas."""
    kv = [r[:] for r in _LO_SHU]
    for _ in range(rng.randint(0, 3)):
        kv = [list(r) for r in zip(*kv[::-1])]
    if rng.random() < 0.5:
        kv = [r[::-1] for r in kv]
    m, k = rng.choice([1, 1, 2, 3]), rng.randint(0, 10)
    kv = [[m * x + k for x in r] for r in kv]
    summa = 3 * (5 * m + k)
    linijas = ([[(r, c) for c in range(3)] for r in range(3)]
               + [[(r, c) for r in range(3)] for c in range(3)]
               + [[(i, i) for i in range(3)], [(i, 2 - i) for i in range(3)]])
    while True:
        q = (rng.randint(0, 2), rng.randint(0, 2))
        tuksi = {q} | set(rng.sample([(r, c) for r in range(3)
                                      for c in range(3) if (r, c) != q],
                                     2 if lim == 2 else 3))
        vesela = [l for l in linijas if not tuksi & set(l)]
        caur_q = [l for l in linijas if q in l
                  and len(tuksi & set(l)) == 1]
        if vesela and caur_q:
            break
    radit = [["" if (r, c) in tuksi and (r, c) != q else
              None if (r, c) == q else sk(kv[r][c]) for c in range(3)]
             for r in range(3)]
    l = caur_q[0]
    citi = [kv[r][c] for r, c in l if (r, c) != q]
    return ievade(t("Maģiskajā kvadrātā katras rindas, kolonnas un "
                    "diagonāles summa ir vienāda. Kas ir «?» vietā?",
                    "In a magic square every row, column and diagonal has "
                    "the same sum. Which number replaces the question "
                    "mark?"),
                  kv[q[0]][q[1]],
                  t("Pilnā līnija dod summu %d. Tad %d − %d − %d = %d.",
                    "A full line gives the sum %d. Then "
                    "%d − %d − %d = %d.")
                  % (summa, summa, citi[0], citi[1], kv[q[0]][q[1]]),
                  zim=Z.tabula(radit))


# ============================================================== mīklas
# (līmenis, jautājums, pareizā, [nepareizās] vai None ievadei, paskaidrojums)
MIKLAS = [
    (1, "Anna ir garāka par Bertu, Berta ir garāka par Cēzaru. Kurš ir "
        "visīsākais?", "Cēzars", ["Anna", "Berta", "Nevar zināt"],
     "Sakārto: Anna > Berta > Cēzars. Īsākais ir pēdējais."),
    (1, "Pēc divām dienām būs piektdiena. Kāda diena bija vakar?",
     "otrdiena", ["trešdiena", "pirmdiena", "ceturtdiena"],
     "Ja pēc divām dienām piektdiena, šodien ir trešdiena, bet vakar - "
     "otrdiena."),
    (1, "Tēvam ir 5 meitas, un katrai meitai ir viens brālis. Cik bērnu "
        "ir ģimenē?", "6", None,
     "Brālis visām meitām ir viens un tas pats: 5 meitas + 1 dēls = 6."),
    (1, "Istabas katrā stūrī sēž kaķis, un katrs kaķis redz 3 kaķus. Cik "
        "kaķu ir istabā?", "4", None,
     "Istabā ir 4 stūri - katrs kaķis redz pārējos trīs."),
    (1, "Rindā Ieva ir 7. no priekšas un 5. no beigām. Cik cilvēku stāv "
        "rindā?", "11", None,
     "Pirms Ievas ir 6, aiz viņas - 4: 6 + 1 + 4 = 11."),
    (1, "Kurā mēnesī ir 28 dienas?", "Visos", ["Februārī", "Nevienā",
                                              "Garajos gados"],
     "Katrā mēnesī ir vismaz 28 dienas - arī janvārī un jūlijā."),
    (2, "Baļķi sazāģē 5 gabalos. Viens zāģējums ilgst 2 minūtes. Cik "
        "minūtēs to izdara?", "8", None,
     "5 gabaliem vajag 4 zāģējumus: 4 · 2 = 8 minūtes."),
    (2, "Gliemezis kāpj 10 m stabā: dienā uzrāpjas 3 m, naktī noslīd 2 m. "
        "Kurā dienā tas būs galā?", "8", None,
     "Pēc 7 diennaktīm tas ir 7 m augstumā, un 8. dienā uzrāpjas vēl 3 m."),
    (2, "5 kaķi 5 minūtēs noķer 5 peles. Cik kaķu 100 minūtēs noķers 100 "
        "peles?", "5", None,
     "Katrs kaķis vienu peli ķer 5 minūtes, tātad 100 minūtēs - 20 peles. "
     "5 kaķi · 20 = 100."),
    (2, "Atvilktnē tumsā ir 10 melnas un 10 baltas zeķes. Cik zeķes "
        "jāizņem, lai droši būtu pāris?", "3", None,
     "Divas var būt dažādas, bet trešā noteikti sakritīs ar kādu no tām."),
    (2, "Dīķī ūdensrožu lapu laukums katru dienu divkāršojas. 30. dienā dīķis "
        "ir pilns. Kurā dienā tas bija pusē?", "29", None,
     "Ja laukums dubultojas, dienu pirms pilna dīķa tas bija puse."),
    (2, "Ja 3 printeri 3 minūtēs izdrukā 3 lapas, cik lapu 6 printeri "
        "izdrukā 6 minūtēs?", "12", None,
     "Viens printeris - 1 lapa 3 minūtēs, tātad 6 minūtēs 2 lapas. "
     "6 · 2 = 12."),
    (3, "Bumba un nūja kopā maksā 1,10 €. Nūja ir par 1 € dārgāka nekā "
        "bumba. Cik eiro maksā bumba?", "0,05", None,
     "Ja bumba ir x, nūja ir x + 1. Tad 2x + 1 = 1,10, x = 0,05 €. "
     "Ātrā atbilde 0,10 ir slazds!"),
    (3, "Mamma ir 3 reizes vecāka par dēlu. Pēc 10 gadiem viņa būs 2 "
        "reizes vecāka. Cik gadu ir dēlam?", "10", None,
     "3x + 10 = 2(x + 10), tātad x = 10. Mammai ir 30."),
    (3, "Cik ciparu vajag, lai sanumurētu grāmatas lappuses no 1 līdz 100?",
     "192", None, "9 viencipara + 90 · 2 divciparu + 3 = 9 + 180 + 3 = 192."),
    (3, "Kāda ir summa 1 − 2 + 3 − 4 + ... + 99 − 100?", "−50", None,
     "Katrs pāris (1 − 2), (3 − 4), ... dod −1, un pāru ir 50."),
    (3, "Divi riteņbraucēji 30 km attālumā brauc viens otram pretī, katrs ar "
        "15 km/h. Muša lido starp tiem ar 30 km/h. Cik km muša nolidos līdz "
        "tikšanās brīdim?", "30", None,
     "Riteņbraucēji satiekas pēc 1 h (30 : 30), un muša visu šo stundu lido: "
     "30 km."),
    (3, "Kurš skaitlis ir par 7 lielāks nekā puse no sevis?", "14", None,
     "x = {x|2} + 7, tātad {x|2} = 7 un x = 14."),
]


# Tās pašas mīklas angliski - tādā pašā secībā, tāpēc tests ar sēklu dod
# to pašu mīklu abās valodās.
MIKLAS_EN = [
    (1, "Anna is taller than Beth, and Beth is taller than Carl. Who is the "
        "shortest?", "Carl", ["Anna", "Beth", "Can't tell"],
     "Put them in order: Anna > Beth > Carl. The shortest is the last one."),
    (1, "In two days it will be Friday. What day was yesterday?",
     "Tuesday", ["Wednesday", "Monday", "Thursday"],
     "If it's Friday in two days, today is Wednesday, so yesterday was "
     "Tuesday."),
    (1, "A father has 5 daughters, and each daughter has one brother. How "
        "many children are in the family?", "6", None,
     "All the daughters share the same brother: 5 daughters + 1 son = 6."),
    (1, "A cat sits in each corner of a room, and each cat sees 3 cats. How "
        "many cats are in the room?", "4", None,
     "A room has 4 corners - each cat sees the other three."),
    (1, "In a queue Eve is 7th from the front and 5th from the back. How "
        "many people are in the queue?", "11", None,
     "6 people are in front of Eve and 4 behind her: 6 + 1 + 4 = 11."),
    (1, "Which month has 28 days?", "All of them", ["February", "None",
                                                   "Only in leap years"],
     "Every month has at least 28 days - January and July too."),
    (2, "A log is sawn into 5 pieces. Each cut takes 2 minutes. How many "
        "minutes does it take?", "8", None,
     "5 pieces need 4 cuts: 4 · 2 = 8 minutes."),
    (2, "A snail climbs a 10 m pole: 3 m up by day, 2 m down by night. On "
        "which day does it reach the top?", "8", None,
     "After 7 days and nights it is 7 m up, and on day 8 it climbs the last "
     "3 m."),
    (2, "5 cats catch 5 mice in 5 minutes. How many cats will catch 100 "
        "mice in 100 minutes?", "5", None,
     "Each cat catches a mouse in 5 minutes, so 20 mice in 100 minutes. "
     "5 cats · 20 = 100."),
    (2, "A drawer in the dark has 10 black and 10 white socks. How many "
        "socks must you take out to be sure of a pair?", "3", None,
     "Two can be different, but the third will surely match one of them."),
    (2, "Water lilies on a pond double their area every day. On day 30 the "
        "pond is full. On which day was it half full?", "29", None,
     "If the area doubles, the pond was half full the day before it was "
     "full."),
    (2, "If 3 printers print 3 pages in 3 minutes, how many pages do 6 "
        "printers print in 6 minutes?", "12", None,
     "One printer - 1 page in 3 minutes, so 2 pages in 6 minutes. "
     "6 · 2 = 12."),
    (3, "A bat and a ball cost 1.10 € together. The bat costs 1 € more than "
        "the ball. How many euros does the ball cost?", "0.05", None,
     "If the ball is x, the bat is x + 1. Then 2x + 1 = 1.10, x = 0.05 €. "
     "The quick answer 0.10 is a trap!"),
    (3, "A mother is 3 times as old as her son. In 10 years she will be "
        "twice as old. How old is the son?", "10", None,
     "3x + 10 = 2(x + 10), so x = 10. The mother is 30."),
    (3, "How many digits are needed to number the pages of a book from 1 to "
        "100?", "192", None,
     "9 one-digit + 90 · 2 two-digit + 3 = 9 + 180 + 3 = 192."),
    (3, "What is 1 − 2 + 3 − 4 + ... + 99 − 100?", "−50", None,
     "Each pair (1 − 2), (3 − 4), ... gives −1, and there are 50 pairs."),
    (3, "Two cyclists 30 km apart ride towards each other, each at 15 km/h. "
        "A fly flies between them at 30 km/h. How many km does the fly cover "
        "before they meet?", "30", None,
     "The cyclists meet after 1 h (30 : 30), and the fly flies the whole "
     "hour: 30 km."),
    (3, "Which number is 7 more than half of itself?", "14", None,
     "x = {x|2} + 7, so {x|2} = 7 and x = 14."),
]


def mikla(rng, lim, nr=None):
    """Teksta mīkla no MIKLAS saraksta (nr - kura pēc kārtas šajā līmenī)."""
    visas = [m for m in (MIKLAS_EN if en() else MIKLAS) if m[0] == lim]
    _, jaut, pareiza, citas, skaidro = (visas[nr % len(visas)] if nr is not None
                                        else rng.choice(visas))
    if citas:
        return izvele(jaut, txt(pareiza), [txt(c) for c in citas], skaidro,
                      kol=2)
    return ievade(jaut, pareiza, skaidro, vieta="atbilde")


# ====================================================== atmiņa un uzmanība
def atmina_rezgis(rng, lim):
    """Iegaumē iekrāsotās rūtiņas un atzīmē tās pašas."""
    n, k = {1: (3, 3), 2: (4, 5), 3: (5, 7)}[lim]
    on = sorted(rng.sample(range(n * n), k))
    return {"veids": "rezgis", "n": n, "atb": on,
            "jaut": t("Atzīmē tās pašas %d rūtiņas!",
                      "Tap the same %d cells!") % k,
            "radit": Z.rezgis(n, on), "laiks": 2500 + 400 * k,
            "skaidro": t("Atmiņu var trenēt: iegaumē rūtiņas kā figūru vai "
                         "burtu, nevis katru atsevišķi.",
                         "Memory can be trained: remember the cells as "
                         "one shape or letter, not one by one.")}


def atmina_cipari(rng, lim):
    """Iegaumē ciparus."""
    n = {1: 4, 2: 6, 3: 7}[lim]
    cip = "".join(str(rng.randint(0, 9)) for _ in range(n))
    atpakal = lim == 3 and rng.random() < 0.5
    atb = cip[::-1] if atpakal else cip
    grupas, i = [], 0
    for g in {4: (2, 2), 6: (3, 3), 7: (3, 2, 2)}[n]:
        grupas.append(cip[i:i + g])
        i += g
    k = ievade(t("Ieraksti ciparus %s!", "Type the digits %s!") % (
                   t("pretējā secībā - no beigām uz sākumu",
                     "backwards - from last to first") if atpakal else
                   t("tādā pašā secībā", "in the same order")),
               [atb], t("Cipari bija %s%s. Iegaumēt palīdz grupas: %s.",
                        "The digits were %s%s. Groups help you remember: "
                        "%s.")
               % (cip, t(", no beigām - %s", ", backwards - %s") % atb
                  if atpakal else "", " ".join(grupas)),
               vieta=t("cipari", "digits"))
    k["radit"], k["laiks"] = Z.cipari(cip), 1500 + 600 * n
    return k


def atmina_figuras(rng, lim):
    """Iegaumē figūru rindu un pasaki, kura bija n-tā."""
    n = {1: 3, 2: 4, 3: 5}[lim]
    formas = rng.sample(_M_FORMAS, n)
    krasas = [rng.choice(_M_KRASAS) for _ in range(n)]
    sunas = [{"forma": f, "krasa": k} for f, k in zip(formas, krasas)]
    j = rng.randint(1, n - 1)
    nos = t(["pirmā", "otrā", "trešā", "ceturtā", "piektā"],
            ["first", "second", "third", "fourth", "fifth"])[j]
    citas = [s for i, s in enumerate(sunas) if i != j]
    citas += [{"forma": rng.choice([f for f in _M_FORMAS
                                    if f not in formas]),
               "krasa": krasas[j]}]
    k = izvele(t("Kura figūra bija %s?", "Which picture was %s?") % nos,
               Z.suna(sunas[j]), [Z.suna(c) for c in citas[:3]],
               t("Rindā bija: %s.", "The row was: %s.")
               % ", ".join(Z.vards(f) for f in formas),
               kol=4)
    k["radit"], k["laiks"] = Z.rinda(sunas), 1800 + 700 * n
    return k


def citads(rng, lim):
    """Atrodi vienu citādu starp daudzām vienādām."""
    n = {1: 9, 2: 16, 3: 16}[lim]
    kol = 3 if n == 9 else 4
    kr = rng.choice(_M_KRASAS)
    if lim == 1:
        f1, f2 = rng.choice([("aplis", "sessturis"), ("kvadrats", "rombs"),
                             ("zvaigzne", "krusts"), ("trijsturis", "rombs")])
        vien, cits = Z.suna({"forma": f1, "krasa": kr}), Z.suna(
            {"forma": f2, "krasa": kr})
        skaidro = t("Visi pārējie ir %s, bet šis ir %s.",
                    "All the others are %s, but this one is a %s.") % (
            Z.vards(f1, Z.DSK), Z.vards(f2))
    elif lim == 2:
        rot = rng.choice([0, 90, 180, 270])
        vien = Z.suna({"forma": "bulta", "krasa": kr, "rot": rot})
        cits = Z.suna({"forma": "bulta", "krasa": kr,
                       "rot": (rot + rng.choice([45, 90, 180])) % 360})
        skaidro = t("Visas pārējās bultas rāda vienā virzienā, bet šī - "
                    "citā.", "All the other arrows point the same way, but "
                    "this one doesn't.")
    else:
        fig = _hirala(rng, 5)
        vien, cits = Z.poliomino(fig, kr), Z.poliomino(_spog(fig), kr)
        skaidro = t("Šī figūra ir spoguļattēls - pārējās ir tieši "
                    "vienādas.", "This shape is a mirror image - the others "
                    "are exactly the same.")
    # Visas vienādās pogas ir vienāds HTML, tāpēc tās atšķir ar numuru.
    k = {"veids": "izvele", "jaut": t("Atrodi vienu citādu - ātri!",
                                       "Find the one that's different - "
                                       "fast!"),
         "opcijas": [cits] + [vien] * (n - 1), "pareizi": 0, "kol": kol,
         "skaidro": skaidro, "sikas": True}
    return k


def skaiti(rng, lim):
    """Cik ir noteiktu figūru? - uzmanības uzdevums."""
    n = {1: 12, 2: 16, 3: 20}[lim]
    formas = rng.sample(["aplis", "kvadrats", "trijsturis", "zvaigzne"],
                        2 if lim == 1 else 3)
    krasas = rng.sample(_M_KRASAS, 1 if lim == 1 else 2)
    merkis = {"forma": formas[0], "krasa": krasas[0]}
    atb = 0
    while atb < 2:
        sunas = [{"forma": rng.choice(formas), "krasa": rng.choice(krasas)}
                 for _ in range(n)]
        atb = sum(1 for s in sunas if s == merkis)
    ko = Z.ko_gen(formas[0], krasas[0] if lim > 1 else None)
    return ievade(t("Cik te ir %s?", "How many %s are there?") % ko, atb,
                  t("Skaitot palīdz iet pa rindām no kreisās uz labo. "
                    "Pareizi: %d.",
                    "It helps to count row by row, left to right. "
                    "Answer: %d.") % atb,
                  zim=Z.rezgis(4, (), [Z.suna(s) for s in sunas]))


def atzime(rng, lim):
    """Atzīmē visas figūras, kas atbilst nosacījumam."""
    n = {1: 3, 2: 4, 3: 4}[lim]
    formas = rng.sample(["aplis", "kvadrats", "trijsturis", "zvaigzne"], 3)
    krasas = rng.sample(_M_KRASAS, 2)
    pild = ["pilns", "tukss"] if lim == 3 else ["pilns"]
    while True:
        sunas = [{"forma": rng.choice(formas), "krasa": rng.choice(krasas),
                  "pild": rng.choice(pild)} for _ in range(n * n)]
        if lim == 1:
            der = [i for i, s in enumerate(sunas) if s["forma"] == formas[0]]
            ko = Z.ko_akk(formas[0])
        elif lim == 2:
            der = [i for i, s in enumerate(sunas)
                   if s["forma"] == formas[0] and s["krasa"] == krasas[0]]
            ko = Z.ko_akk(formas[0], krasas[0])
        else:
            der = [i for i, s in enumerate(sunas)
                   if s["forma"] == formas[0] or s["pild"] == "tukss"]
            ko = t("%s un visas tukšās figūras",
                   "%s and all empty shapes") % Z.ko_akk(formas[0])
        if 2 <= len(der) <= n * n // 2:
            break
    return {"veids": "rezgis", "n": n, "atb": der,
            "saturs": [Z.suna(s) for s in sunas],
            "jaut": t("Atzīmē %s!", "Tap %s!") % ko,
            "skaidro": t("Der %d rūtiņas. Ej pa rindām un katru pārbaudi "
                         "pret nosacījumu.",
                         "%d cells fit. Go row by row and check each one "
                         "against the rule.") % len(der)}


# ========================================================== mērķa laiki
# Cik sekundēs šādu mīklu atrisina, ja zina, kā (1., 2., 3. līmenis). Tas ir
# vērtējuma atskaites punkts (MSP.tempo), nevis sods - lēnāk nekā mērķis
# arī ir labi, tikai teikums mudina trenēties.
MERKA_LAIKS = {
    "virkne": (20, 30, 40), "matrica": (25, 40, 60), "lieks": (15, 25, 35),
    "rotacija": (15, 20, 30), "spogulis": (15, 20, 30), "kubi": (15, 25, 35),
    "tikls": (25, 35, 45), "simboli": (30, 45, 60), "svari": (25, 40, 60),
    "piramida": (20, 40, 60), "magiskais": (40, 50, 60),
    "mikla": (30, 45, 60), "atmina_rezgis": (10, 15, 20),
    "atmina_cipari": (10, 12, 15), "atmina_figuras": (8, 10, 12),
    "citads": (8, 10, 15), "skaiti": (15, 20, 25), "atzime": (15, 20, 30),
}


# ============================================================ reģistrs
# Ģeneratori pēc nosaukuma - testu plānā raksta vārdu, nevis funkciju.
GENERATORI = {
    "virkne": virkne, "matrica": matrica, "lieks": lieks,
    "rotacija": rotacija, "spogulis": spogulis, "kubi": kubi,
    "tikls": tikls, "simboli": simboli, "svari": svari,
    "piramida": piramida, "magiskais": magiskais, "mikla": mikla,
    "atmina_rezgis": atmina_rezgis, "atmina_cipari": atmina_cipari,
    "atmina_figuras": atmina_figuras, "citads": citads, "skaiti": skaiti,
    "atzime": atzime,
}
