# -*- coding: utf-8 -*-
"""Lapas valoda - latviešu vai angļu - un teksts tai valodai.

Vietne ir latviska; angliski ir tikai IQ testi (en/...), lai tos var dot
arī ārzemēs. Mīklu ģeneratori, testu plāns un lapu veidnes teikumus raksta
pāros - t("latviski", "in English") - un šis modulis izlemj, kuru ņemt
(SRP). Ģeneratori paliek tie paši, un nejaušība ar sēklu nav atkarīga no
valodas, tāpēc angļu tests ir tieši tas pats tests, tikai tulkots (DRY).

    with valoda.ar("en"):
        iq_vietne.build()          # tas pats kods, angliski

Valoda ir būvēšanas stāvoklis, nevis parametrs katrai funkcijai: citādi tā
būtu jāpadod caur desmit slāņiem, kas paši par valodu neko nezina.
"""

import contextlib

VALODAS = ("lv", "en")
_TAGAD = ["lv"]


def tagad():
    """Valoda, kurā tagad būvē: "lv" vai "en"."""
    return _TAGAD[-1]


def en():
    return tagad() == "en"


def t(lv, en_):
    """Teksts tagadējā valodā."""
    return en_ if en() else lv


@contextlib.contextmanager
def ar(valoda):
    """Uz bloka laiku būvē citā valodā."""
    if valoda not in VALODAS:
        raise ValueError("nav valodas «%s»; ir: %s"
                         % (valoda, ", ".join(VALODAS)))
    _TAGAD.append(valoda)
    try:
        yield
    finally:
        _TAGAD.pop()


def skaits(n, lv, en_):
    """«3 testi» / «3 tests»: lv - (1, daudz, 0) kā site_index.plural,
    en_ - (vienskaitlis, daudzskaitlis)."""
    if en():
        return "%d %s" % (n, en_[0] if n == 1 else en_[1])
    import site_index
    return site_index.plural(n, *lv)
