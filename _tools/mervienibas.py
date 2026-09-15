# -*- coding: utf-8 -*-
"""
Mērvienību salīdzināšana - viens īpašnieks (SRP).

Aprēķinu pārbaudei (risinajums.py) vajag atbildēt uz vienu jautājumu: vai
"0,0375 m" un "37,5 mm" ir viens un tas pats skaitlis? Tā ir mērvienību,
nevis aritmētikas atbildība, tāpēc tā dzīvo atsevišķi no aritmetika.py.

    >>> koeficients("mm", "m")
    0.001
    >>> koeficients("km/s", "m/s")
    1000.0
    >>> koeficients("m", "s") is None
    True

Mērvienību lasa pa daļām: priedēklis + pamatvienība + pakāpe, saliktas ar
"·" un vienu "/" ("Ω·mm²/m", "J/(kg·K)", "m/s²"). Nezināmu pieraksta daļu
neuzmin - tad atbilde ir None, un pārbaudītājs tādu soli izlaiž (labāk neko
nepateikt nekā pateikt nepareizi).
"""

import re

# Pamatvienības, kurām drīkst likt SI priedēkli ("k" + "Hz" = "kHz").
PAMATI = {
    "m", "s", "g", "Hz", "N", "Pa", "J", "W", "V", "A", "C", "Ω", "F",
    "T", "Wb", "H", "eV", "K", "mol", "lm", "lx", "Bq", "Sv", "Gy",
}

# Priedēkļi; garākos pārbauda pirmos ("da" pirms "d").
PRIEDEKLI = {
    "da": 1e1, "h": 1e2, "k": 1e3, "M": 1e6, "G": 1e9, "T": 1e12,
    "d": 1e-1, "c": 1e-2, "m": 1e-3, "µ": 1e-6, "μ": 1e-6, "n": 1e-9,
    "p": 1e-12,
}

# Mērvienības, kas nav priedēklis + pamats: (reizinātājs, {pamats: pakāpe}).
SEVISKAS = {
    "min": (60.0, {"s": 1}),
    "h": (3600.0, {"s": 1}),
    "st": (3600.0, {"s": 1}),
    "t": (1e6, {"g": 1}),
    "l": (1e-3, {"m": 3}),
    "L": (1e-3, {"m": 3}),
}

_PAKAPES = {"²": 2, "³": 3}
_TOKENS = re.compile(r"^([A-Za-zĀ-žµμΩ]+)([²³]?)$")


def _reizinatajs(tok):
    """Viena reizinātāja (reizinātājs, {pamats: pakāpe}) vai None."""
    m = _TOKENS.match(tok.strip())
    if not m:
        return None
    vards, pakape = m.group(1), _PAKAPES.get(m.group(2), 1)
    pamats = SEVISKAS.get(vards)
    if pamats is None and vards in PAMATI:
        pamats = (1.0, {vards: 1})
    if pamats is None:
        for p in sorted(PRIEDEKLI, key=len, reverse=True):
            if vards.startswith(p):
                atlikums = vards[len(p):]
                if atlikums in PAMATI:
                    pamats = (PRIEDEKLI[p], {atlikums: 1})
                elif atlikums in SEVISKAS:
                    k, d = SEVISKAS[atlikums]
                    pamats = (PRIEDEKLI[p] * k, d)
                if pamats is not None:
                    break
    if pamats is None:
        return None
    k, dim = pamats
    return k ** pakape, {b: e * pakape for b, e in dim.items()}


def _puse(teksts, zime, kopa, dim):
    """Saskaita vienu "/" pusi reizinātāju kopā (skaitītājs vai saucējs)."""
    for tok in teksts.split("·"):
        if not tok.strip():
            continue
        r = _reizinatajs(tok)
        if r is None:
            return None
        k, d = r
        kopa[0] *= k ** zime
        for b, e in d.items():
            dim[b] = dim.get(b, 0) + e * zime
    return kopa


def pamatot(u):
    """(reizinātājs, dimensija) vai None, ja mērvienība nav pazīstama.

    Dimensija ir sakārtots pamatvienību un pakāpju saraksts - divas
    mērvienības ir savstarpēji pārrēķināmas tieši tad, ja tā sakrīt.
    """
    u = (u or "").strip().replace("(", "").replace(")", "")
    if not u:
        return None
    skaititajs, _, saucejs = u.partition("/")
    kopa, dim = [1.0], {}
    if _puse(skaititajs, 1, kopa, dim) is None:
        return None
    if saucejs and _puse(saucejs, -1, kopa, dim) is None:
        return None
    return kopa[0], tuple(sorted((b, e) for b, e in dim.items() if e))


def koeficients(no, uz):
    """Ar ko jāreizina vērtība mērvienībā «no», lai iegūtu «uz».

    1.0, ja mērvienība ir tā pati vai kādas nav vispār (skaitlis bez
    mērvienības ir salīdzināms ar jebkuru - tā slaidos raksta starpsoļus);
    None, ja mērvienības nav savstarpēji pārrēķināmas.
    """
    no, uz = (no or "").strip(), (uz or "").strip()
    if no == uz or not no or not uz:
        return 1.0
    a, b = pamatot(no), pamatot(uz)
    if a is None or b is None or a[1] != b[1]:
        return None
    return a[0] / b[0]
