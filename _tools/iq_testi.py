# -*- coding: utf-8 -*-
"""IQ sadaļas plāns: kategorijas, grūtības pakāpes un testi.

IQ ir kā atsevišķa klase matemātikas sadaļā (Math/IQ), tikai bez mācību
kalendāra un bez teorijas: katrs tests ir 10 (lielie - 15) mīklu virkne, kas
sākas uzreiz. Kategorija ir kā temats, grūtības pakāpe - kā mikrotemats, un
tests - kā stunda, tāpēc tematu lapu, failu ceļus un saites uz kaimiņiem
uzbūvē tie paši moduļi, kas klasēm (math_vietne.py, math_stundas.py) - te ir
tikai saturs (SRP, DRY).

Testu raksta ar vienu rindu:

    T("Kāpnes uz augšu", 1, [("virkne", 10, {"likums": "plus"})])

- nosaukums, līmenis (1 - no 1. klases, 2 - no 4., 3 - no 7.) un sastāvs:
kuru ģeneratoru (iq_miklas.GENERATORI) cik reižu izsaukt. Mīklas sajauc
pamīšus, lai tests nav viena veida garš saraksts.
"""

import random

import iq_miklas
from math_plani import B, Stunda

NOSAUKUMS = "IQ"
KODS = "IQ"
MIKLAS_TESTA = 10


class Tests(Stunda):
    """Viens IQ tests - plānā tas ir tas pats, kas stunda."""

    def __init__(self, tema, limenis, sastavs):
        Stunda.__init__(self, tema, iq_miklas.LIMENI[limenis])
        self.limenis, self.sastavs = limenis, list(sastavs)

    def seciba(self):
        """[(ģenerators, parametri), ...] - veidi pamīšus, nevis blokos."""
        rindas = [[(g, p[0] if p else {})] * n
                  for g, n, *p in self.sastavs]
        out = []
        while any(rindas):
            for r in rindas:
                if r:
                    out.append(r.pop())
        return out

    def kartas(self):
        """Testa mīklas; nejaušība ar sēklu - katrs būvējums ir vienāds.

        Vienādas mīklas vienā testā neatkārtojas: ja ģenerators iedod tādu
        pašu, to izsauc vēlreiz ar citu sēklu.
        """
        out, redzetas, mikla = [], set(), 0
        for i, (vards, param) in enumerate(self.seciba()):
            gen = iq_miklas.GENERATORI[vards]
            for meg in range(20):
                rng = random.Random("iq-%d-%d-%d" % (self.nr, i, meg))
                p = dict(param)
                lim = p.pop("lim", self.limenis)
                if vards == "mikla":
                    p["nr"] = self.nr * 3 + mikla + meg
                karta = gen(rng, lim, **p)
                seja = (karta["jaut"], karta.get("zim"), karta.get("radit"),
                        str(karta.get("atb")), str(karta.get("opcijas")))
                if seja not in redzetas:
                    break
            redzetas.add(seja)
            karta.setdefault("merkis",
                             iq_miklas.MERKA_LAIKS[vards][lim - 1])
            if vards == "mikla":
                mikla += 1
            out.append(karta)
        return out


class Kategorija(object):
    """Mīklu veids - IQ klasē tas ir temats."""

    def __init__(self, kods, nosaukums, apraksts, bloki):
        self.kods, self.nosaukums, self.apraksts = kods, nosaukums, apraksts
        self.bloki = bloki
        for b in bloki:
            for s in b.stundas:
                s.temats = self

    @property
    def stundas(self):
        return [s for b in self.bloki for s in b.stundas]

    def __len__(self):
        return len(self.stundas)


class Kurss(object):
    """IQ «klase»: kategorijas un testu numuri pēc kārtas."""

    def __init__(self, temati):
        self.nosaukums, self.kods = NOSAUKUMS, KODS
        self.temati = temati
        self.noslegums = []
        for i, s in enumerate(self.visas):
            s.nr = i + 1

    @property
    def visas(self):
        return [s for t in self.temati for s in t.stundas]

    @property
    def stundu_skaits(self):
        return len(self.visas)


def T(tema, limenis, sastavs):
    return Tests(tema, limenis, sastavs)


def V(likums, n):
    """Skaitļu virkne ar noteiktu likumu."""
    return ("virkne", n, {"likums": likums})


L1, L2, L3 = ("Iesildīšanās · no 1. klases", "Uzkāpiens · no 4. klases",
              "Virsotne · no 7. klases")

KATEGORIJAS = [
    Kategorija("1.", "Skaitļu virknes",
               "Atrodi likumu, pēc kura aug skaitļi, un uzmini nākamo.", [
                   B(L1, [
                       T("Kāpnes uz augšu", 1, [V("plus", 10)]),
                       T("Kāpnes uz leju", 1, [V("minus", 5), V("plus", 5)]),
                       T("Dubultā!", 1, [V("divreiz", 4), V("plus", 3),
                                         V("minus", 3)]),
                   ]),
                   B(L2, [
                       T("Soļi, kas aug", 2, [V("augosi", 4), V("mainigi", 3),
                                              V("negativi", 3)]),
                       T("Divas virknes vienā", 2, [V("divas", 5),
                                                    V("puse", 3),
                                                    V("trisreiz", 2)]),
                       T("Kvadrāti un reizinājumi", 2, [
                           V("kvadrati", 4), V("trisreiz", 3),
                           V("augosi", 3)]),
                   ]),
                   B(L3, [
                       T("Fibonači noslēpums", 3, [V("fibonaci", 4),
                                                   V("trijstura", 3),
                                                   V("dubultsoli", 3)]),
                       T("Pirmskaitļi un kubi", 3, [V("pirmskaitli", 4),
                                                    V("kubi", 3),
                                                    V("reizpluss", 3)]),
                       T("Virkņu meistars", 3, [("virkne", 10)]),
                   ]),
               ]),
    Kategorija("2.", "Figūru matricas",
               "Kas iet tukšajā rūtiņā? Atrodi likumu rindās un kolonnās.", [
                   B(L1, [
                       T("Kas iztrūkst?", 1, [("matrica", 10, {"n": 2})]),
                       T("Viena pazīme mainās", 1, [("matrica", 10,
                                                     {"n": 3})]),
                       T("Rindas un kolonnas", 1, [
                           ("matrica", 5, {"n": 2}),
                           ("matrica", 5, {"n": 3, "lim": 2})]),
                   ]),
                   B(L2, [
                       T("Divi likumi vienlaikus", 2, [("matrica", 10,
                                                        {"n": 3})]),
                       T("Bultas griežas", 2, [("matrica", 10,
                                                {"n": 3, "bulta": True})]),
                       T("Rūtiņu detektīvs", 2, [("matrica", 10)]),
                   ]),
                   B(L3, [
                       T("Trīs likumi", 3, [("matrica", 10, {"n": 3})]),
                       T("Griežas un mainās", 3, [("matrica", 10,
                                                   {"n": 3, "bulta": True})]),
                       T("Matricu meistars", 3, [("matrica", 10)]),
                   ]),
               ]),
    Kategorija("3.", "Lieks ārā",
               "Viens no tiem neiederas. Kurš un kāpēc?", [
                   B(L1, [
                       T("Kurš neiederas?", 1, [("lieks", 10,
                                                 {"ko": "figuras"})]),
                       T("Pāra un nepāra", 1, [("lieks", 6,
                                                {"ko": "skaitli"}),
                                               ("lieks", 4,
                                                {"ko": "figuras"})]),
                       T("Ātrā acs", 1, [("citads", 6),
                                         ("lieks", 4, {"ko": "figuras"})]),
                   ]),
                   B(L2, [
                       T("Skaiti un salīdzini", 2, [("lieks", 10,
                                                     {"ko": "figuras"})]),
                       T("Dalāmības detektīvs", 2, [("lieks", 7,
                                                     {"ko": "skaitli"}),
                                                    ("lieks", 3,
                                                     {"ko": "figuras"})]),
                       T("Bultu labirints", 2, [("citads", 6),
                                                ("lieks", 4,
                                                 {"ko": "figuras"})]),
                   ]),
                   B(L3, [
                       T("Spoguļa slazds", 3, [("lieks", 6,
                                                {"ko": "figuras"}),
                                               ("citads", 4)]),
                       T("Pirmskaitļi un kvadrāti", 3, [("lieks", 10,
                                                         {"ko": "skaitli"})]),
                       T("Liekā meistars", 3, [("lieks", 10)]),
                   ]),
               ]),
    Kategorija("4.", "Telpiskā domāšana",
               "Pagriez, apgriez, saloki un saskaiti - tikai prātā.", [
                   B(L1, [
                       T("Pagriez figūru", 1, [("rotacija", 10)]),
                       T("Spogulītis", 1, [("spogulis", 10)]),
                       T("Kubu tornis", 1, [("kubi", 10)]),
                   ]),
                   B(L2, [
                       T("Pagriez vai apgriez?", 2, [("rotacija", 5),
                                                     ("spogulis", 5)]),
                       T("Kubu pilsēta", 2, [("kubi", 10)]),
                       T("Saloki kubu", 2, [("tikls", 5, {"lim": 1}),
                                            ("tikls", 5)]),
                   ]),
                   B(L3, [
                       T("Sešu rūtiņu galvasgrieziens", 3, [
                           ("rotacija", 5), ("spogulis", 5)]),
                       T("Lielais kubs", 3, [("kubi", 10)]),
                       T("Kuba tīklu meistars", 3, [("tikls", 10)]),
                   ]),
               ]),
    Kategorija("5.", "Loģika un svari",
               "Figūras slēpj skaitļus, svari nemelo, un katrai mīklai ir "
               "atbilde.", [
                   B(L1, [
                       T("Figūru šifrs", 1, [("simboli", 10)]),
                       T("Svaru mīklas", 1, [("svari", 10)]),
                       T("Skaitļu piramīda", 1, [("piramida", 6),
                                                 ("mikla", 4)]),
                   ]),
                   B(L2, [
                       T("Trīs figūru šifrs", 2, [("simboli", 10)]),
                       T("Svaru ķēde", 2, [("svari", 10)]),
                       T("Viltīgās mīklas", 2, [("mikla", 6),
                                                ("piramida", 4)]),
                   ]),
                   B(L3, [
                       T("Darbību secības šifrs", 3, [("simboli", 10)]),
                       T("Maģiskais kvadrāts", 3, [("magiskais", 6),
                                                   ("svari", 4)]),
                       T("Mīklas ar āķi", 3, [("mikla", 6),
                                              ("piramida", 4)]),
                   ]),
               ]),
    Kategorija("6.", "Atmiņa un uzmanība",
               "Iegaumē, pamani un saskaiti - ātri un precīzi.", [
                   B(L1, [
                       T("Spīdošās rūtiņas", 1, [("atmina_rezgis", 10)]),
                       T("Ko tu redzēji?", 1, [("atmina_cipari", 5),
                                               ("atmina_figuras", 5)]),
                       T("Asā acs", 1, [("skaiti", 5), ("atzime", 5)]),
                   ]),
                   B(L2, [
                       T("Rūtiņu labirints", 2, [("atmina_rezgis", 10)]),
                       T("Figūru rinda", 2, [("atmina_figuras", 5),
                                             ("atmina_cipari", 5)]),
                       T("Detektīva acs", 2, [("atzime", 5), ("skaiti", 5)]),
                   ]),
                   B(L3, [
                       T("Atmiņas čempions", 3, [("atmina_rezgis", 10)]),
                       T("Ciparu virtuozs", 3, [("atmina_cipari", 6),
                                                ("atmina_figuras", 4)]),
                       T("Uzmanības meistars", 3, [("atzime", 5),
                                                   ("skaiti", 5)]),
                   ]),
               ]),
]

# Lielie testi: no katras kategorijas pa mīklai vai divām - 15 kopā.
_JAUKTS = [("virkne", 2), ("matrica", 2), ("lieks", 2), ("rotacija", 1),
           ("kubi", 1), ("tikls", 1), ("simboli", 1), ("svari", 1),
           ("mikla", 2), ("atmina_rezgis", 1), ("atzime", 1)]

KATEGORIJAS.append(Kategorija(
    "7.", "Lielie IQ testi",
    "15 dažādas mīklas pēc kārtas - pārbaudi sevi visās jomās.", [
        B("Viss kopā · trīs līmeņi", [
            T("IQ tests: sākums", 1, _JAUKTS),
            T("IQ tests: izaicinājums", 2, _JAUKTS),
            T("IQ tests: ģēnijs", 3, _JAUKTS),
        ]),
    ]))

_KURSS = []


def kurss():
    """IQ «klase» - vienreiz uzbūvēta, tad ņemta no atmiņas."""
    if not _KURSS:
        _KURSS.append(Kurss(KATEGORIJAS))
    return _KURSS[0]
