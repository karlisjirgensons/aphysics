# -*- coding: utf-8 -*-
"""No vienas veidnes - daudz līdzvērtīgu jautājumu un uzdevumu variantu.

Lapa no katras grupas izlozē vienu jautājumu un no katra uzdevuma vienu
variantu. Ja grupā ir tikai trīs jautājumi, tie ātri sāk atkārtoties, un
skolēniem šķiet, ka darbu ir tikai daži. Lai tā nebūtu, vienā grupā vajag
daudz līdzvērtīgu jautājumu (MERKIS).

Ar roku tos rakstīt nozīmētu vienu un to pašu teikumu pārrakstīt 15 reizes,
tāpēc te ir veidne: viena funkcija, kas no skaitļiem uztaisa jautājumu, un
skaitļu saraksts (DRY). Šis modulis neko nezina par lapu un neko nezīmē - tas
tikai pavairo saturu (SRP); saturu pārbauda mat_common.py.

    V.kopa(veidne, dati)             - jautājumu grupa no veidnes
    V.izvele(pareiza, *maldi)        - četri atbilžu varianti, pareizais pirmais
    V.sk(x)                          - skaitlis latviski (komats, ne punkts)
    V.iek(x)                         - negatīvs skaitlis iekavās: (−3)
    V.dalu(a, b)                     - nesaīsināma daļa {a|b} (vai vesels)
    V.parveide(virs, veidne, dati)   - «ieraksti trūkstošo» uzdevuma varianti
    V.aprekins(virs, veidne, dati)   - situāciju uzdevuma varianti
    V.jautajumi(virs, veidne, dati)  - uzdevuma varianti ar jautājumiem
"""

MERKIS = 15          # cik jautājumu grupā ir «daudz» - uz to tiecas saturs

NOTE = "Ieraksti atbildi! Par katru pareizu atbildi — 1 punkts."
VIETA_APREKINS = 5.6
VIETA_JAUTAJUMI = 4.6


# ------------------------------------------------------------- skaitļi
def sk(x):
    """Skaitlis latviešu pierakstā: komats, nevis punkts; tūkstoši ar atstarpi.

    Lielus skaitļus latviešu standartā šķiro pa trim cipariem (300 000), un
    tā tie ir salasāmi arī uz darba lapas.
    """
    if isinstance(x, float):
        teksts = ("%.4f" % x).rstrip("0").rstrip(".")
    else:
        teksts = str(x)
    zime, teksts = ("−", teksts[1:]) if teksts.startswith("-") else ("",
                                                                    teksts)
    veselie, _, dalas = teksts.partition(".")
    if len(veselie) > 4:
        veselie = _tukstosi(veselie)
    return zime + veselie + ("," + dalas if dalas else "")


def _tukstosi(cipari):
    """«1234567» -> «1 234 567» - trīs ciparu grupas ar atstarpi."""
    out = []
    while len(cipari) > 3:
        out.insert(0, cipari[-3:])
        cipari = cipari[:-3]
    out.insert(0, cipari)
    return " ".join(out)


def iek(x):
    """Negatīvu skaitli izteiksmē raksta iekavās:  (−3) · 5."""
    return "(%s)" % sk(x) if x < 0 else sk(x)


def dalu(a, b):
    """Daļa {a|b} nesaīsināmā veidā - tā, kā to raksta atbildē.

    Vesels rezultāts paliek vesels skaitlis, nevis daļa ar saucēju 1.
    """
    d = _lkd(abs(a), abs(b))
    a, b = a // d, b // d
    if b < 0:
        a, b = -a, -b
    return sk(a) if b == 1 else "{%s|%s}" % (sk(a), sk(b))


def _lkd(a, b):
    """Lielākais kopīgais dalītājs - bez ārējiem moduļiem, kā pārējais kods."""
    while b:
        a, b = b, a % b
    return a or 1


# ---------------------------------------------------------- jautājumi
def izvele(pareiza, *maldi):
    """Četri atbilžu varianti: pareizais pirmais, tad tipiskās kļūdas.

    Atbildes uz lapas tāpat tiek sajauktas, tāpēc te svarīga ir tikai to
    kopa; atkārtošanās ir satura kļūda, un to pamana jau būvējot.
    """
    out = []
    for a in (pareiza,) + maldi:
        teksts = a if isinstance(a, str) else sk(a)
        if teksts not in out:
            out.append(teksts)
    assert len(out) >= 4, "atbilžu varianti atkārtojas: %s" % (out,)
    return out[:4]


def kopa(veidne, dati):
    """Veidne un parametru saraksts -> līdzvērtīgu jautājumu saraksts.

    Katrs `dati` elements ir veidnes argumenti: vairāki - kortežā, viens -
    pats par sevi.
    """
    return [veidne(*d) if isinstance(d, tuple) else veidne(d) for d in dati]


# ------------------------------------------------------------ uzdevumi
def parveide(virs, veidne, dati, note=NOTE):
    """«Ieraksti trūkstošo» varianti: veidne atgriež rindu sarakstu."""
    return [{"tips": "parveide", "virs": virs, "note": note,
             "rindas": veidne(*d) if isinstance(d, tuple) else veidne(d)}
            for d in dati]


def aprekins(virs, veidne, dati, vieta=VIETA_APREKINS):
    """Situāciju uzdevuma varianti: veidne atgriež tekstu un kritērijus."""
    return [dict({"tips": "aprekins", "virs": virs, "vieta": vieta},
                 **(veidne(*d) if isinstance(d, tuple) else veidne(d)))
            for d in dati]


def jautajumi(virs, veidne, dati, vieta=VIETA_JAUTAJUMI):
    """Uzdevuma varianti ar jautājumiem: veidne atgriež ievadu un jautājumus."""
    return [dict({"tips": "jautajumi", "virs": virs, "vieta": vieta},
                 **(veidne(*d) if isinstance(d, tuple) else veidne(d)))
            for d in dati]
