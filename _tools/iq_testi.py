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
import valoda
from math_plani import B, Stunda
from valoda import t

NOSAUKUMS = "IQ"
KODS = "IQ"
MIKLAS_TESTA = 10


class Tests(Stunda):
    """Viens IQ tests - plānā tas ir tas pats, kas stunda."""

    def __init__(self, tema, limenis, sastavs):
        Stunda.__init__(self, tema, iq_miklas.limenis(limenis))
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
        return [s for k in self.temati for s in k.stundas]

    @property
    def stundu_skaits(self):
        return len(self.visas)


def T(tema, limenis, sastavs):
    """Tests; tema - (latviski, angliski)."""
    return Tests(t(*tema), limenis, sastavs)


def V(likums, n):
    """Skaitļu virkne ar noteiktu likumu."""
    return ("virkne", n, {"likums": likums})


def K(kods, nosaukums, apraksts, bloki):
    """Kategorija; nosaukums un apraksts - (latviski, angliski)."""
    return Kategorija(kods, t(*nosaukums), t(*apraksts), bloki)


def L(n, testi):
    """Grūtības pakāpes bloks: 1 - no 1. klases, 2 - no 4., 3 - no 7."""
    return B(t(*{1: ("Iesildīšanās · no 1. klases", "Warm-up · age 7+"),
                 2: ("Uzkāpiens · no 4. klases", "Climb · age 10+"),
                 3: ("Virsotne · no 7. klases", "Summit · age 13+")}[n]),
             testi)


# Lielie testi: no katras kategorijas pa mīklai vai divām - 15 kopā.
_JAUKTS = [("virkne", 2), ("matrica", 2), ("lieks", 2), ("rotacija", 1),
           ("kubi", 1), ("tikls", 1), ("simboli", 1), ("svari", 1),
           ("mikla", 2), ("atmina_rezgis", 1), ("atzime", 1)]


def kategorijas():
    """Viss IQ plāns tagadējā valodā (valoda.py)."""
    return [
        K("1.", ("Skaitļu virknes", "Number sequences"),
          ("Atrodi likumu, pēc kura aug skaitļi, un uzmini nākamo.",
           "Find the rule that makes the numbers grow, and guess the next "
           "one."), [
              L(1, [T(("Kāpnes uz augšu", "Stairs up"), 1, [V("plus", 10)]),
                    T(("Kāpnes uz leju", "Stairs down"), 1,
                      [V("minus", 5), V("plus", 5)]),
                    T(("Dubultā!", "Double it!"), 1,
                      [V("divreiz", 4), V("plus", 3), V("minus", 3)])]),
              L(2, [T(("Soļi, kas aug", "Growing steps"), 2,
                      [V("augosi", 4), V("mainigi", 3), V("negativi", 3)]),
                    T(("Divas virknes vienā", "Two sequences in one"), 2,
                      [V("divas", 5), V("puse", 3), V("trisreiz", 2)]),
                    T(("Kvadrāti un reizinājumi", "Squares and products"), 2,
                      [V("kvadrati", 4), V("trisreiz", 3), V("augosi", 3)])]),
              L(3, [T(("Fibonači noslēpums", "Fibonacci's secret"), 3,
                      [V("fibonaci", 4), V("trijstura", 3),
                       V("dubultsoli", 3)]),
                    T(("Pirmskaitļi un kubi", "Primes and cubes"), 3,
                      [V("pirmskaitli", 4), V("kubi", 3), V("reizpluss", 3)]),
                    T(("Virkņu meistars", "Sequence master"), 3,
                      [("virkne", 10)])]),
          ]),
        K("2.", ("Figūru matricas", "Shape matrices"),
          ("Kas iet tukšajā rūtiņā? Atrodi likumu rindās un kolonnās.",
           "What goes in the empty cell? Find the rule in the rows and "
           "columns."), [
              L(1, [T(("Kas iztrūkst?", "What's missing?"), 1,
                      [("matrica", 10, {"n": 2})]),
                    T(("Viena pazīme mainās", "One feature changes"), 1,
                      [("matrica", 10, {"n": 3})]),
                    T(("Rindas un kolonnas", "Rows and columns"), 1,
                      [("matrica", 5, {"n": 2}),
                       ("matrica", 5, {"n": 3, "lim": 2})])]),
              L(2, [T(("Divi likumi vienlaikus", "Two rules at once"), 2,
                      [("matrica", 10, {"n": 3})]),
                    T(("Bultas griežas", "Arrows turn"), 2,
                      [("matrica", 10, {"n": 3, "bulta": True})]),
                    T(("Rūtiņu detektīvs", "Grid detective"), 2,
                      [("matrica", 10)])]),
              L(3, [T(("Trīs likumi", "Three rules"), 3,
                      [("matrica", 10, {"n": 3})]),
                    T(("Griežas un mainās", "Turning and changing"), 3,
                      [("matrica", 10, {"n": 3, "bulta": True})]),
                    T(("Matricu meistars", "Matrix master"), 3,
                      [("matrica", 10)])]),
          ]),
        K("3.", ("Lieks ārā", "Odd one out"),
          ("Viens no tiem neiederas. Kurš un kāpēc?",
           "One of them doesn't belong. Which one, and why?"), [
              L(1, [T(("Kurš neiederas?", "Which one doesn't fit?"), 1,
                      [("lieks", 10, {"ko": "figuras"})]),
                    T(("Pāra un nepāra", "Odd and even"), 1,
                      [("lieks", 6, {"ko": "skaitli"}),
                       ("lieks", 4, {"ko": "figuras"})]),
                    T(("Ātrā acs", "Quick eye"), 1,
                      [("citads", 6), ("lieks", 4, {"ko": "figuras"})])]),
              L(2, [T(("Skaiti un salīdzini", "Count and compare"), 2,
                      [("lieks", 10, {"ko": "figuras"})]),
                    T(("Dalāmības detektīvs", "Divisibility detective"), 2,
                      [("lieks", 7, {"ko": "skaitli"}),
                       ("lieks", 3, {"ko": "figuras"})]),
                    T(("Bultu labirints", "Arrow maze"), 2,
                      [("citads", 6), ("lieks", 4, {"ko": "figuras"})])]),
              L(3, [T(("Spoguļa slazds", "Mirror trap"), 3,
                      [("lieks", 6, {"ko": "figuras"}), ("citads", 4)]),
                    T(("Pirmskaitļi un kvadrāti", "Primes and squares"), 3,
                      [("lieks", 10, {"ko": "skaitli"})]),
                    T(("Liekā meistars", "Odd-one-out master"), 3,
                      [("lieks", 10)])]),
          ]),
        K("4.", ("Telpiskā domāšana", "Spatial thinking"),
          ("Pagriez, apgriez, saloki un saskaiti - tikai prātā.",
           "Turn, flip, fold and count - all in your head."), [
              L(1, [T(("Pagriez figūru", "Turn the shape"), 1,
                      [("rotacija", 10)]),
                    T(("Spogulītis", "Little mirror"), 1, [("spogulis", 10)]),
                    T(("Kubu tornis", "Cube tower"), 1, [("kubi", 10)])]),
              L(2, [T(("Pagriez vai apgriez?", "Turn or flip?"), 2,
                      [("rotacija", 5), ("spogulis", 5)]),
                    T(("Kubu pilsēta", "Cube city"), 2, [("kubi", 10)]),
                    T(("Saloki kubu", "Fold a cube"), 2,
                      [("tikls", 5, {"lim": 1}), ("tikls", 5)])]),
              L(3, [T(("Sešu rūtiņu galvasgrieziens",
                       "Six-square brain teaser"), 3,
                      [("rotacija", 5), ("spogulis", 5)]),
                    T(("Lielais kubs", "The big cube"), 3, [("kubi", 10)]),
                    T(("Kuba tīklu meistars", "Cube net master"), 3,
                      [("tikls", 10)])]),
          ]),
        K("5.", ("Loģika un svari", "Logic and scales"),
          ("Figūras slēpj skaitļus, svari nemelo, un katrai mīklai ir "
           "atbilde.",
           "Shapes hide numbers, scales never lie, and every riddle has an "
           "answer."), [
              L(1, [T(("Figūru šifrs", "Shape code"), 1, [("simboli", 10)]),
                    T(("Svaru mīklas", "Scale puzzles"), 1, [("svari", 10)]),
                    T(("Skaitļu piramīda", "Number pyramid"), 1,
                      [("piramida", 6), ("mikla", 4)])]),
              L(2, [T(("Trīs figūru šifrs", "Three-shape code"), 2,
                      [("simboli", 10)]),
                    T(("Svaru ķēde", "Chain of scales"), 2, [("svari", 10)]),
                    T(("Viltīgās mīklas", "Tricky riddles"), 2,
                      [("mikla", 6), ("piramida", 4)])]),
              L(3, [T(("Darbību secības šifrs", "Order-of-operations code"),
                      3, [("simboli", 10)]),
                    T(("Maģiskais kvadrāts", "Magic square"), 3,
                      [("magiskais", 6), ("svari", 4)]),
                    T(("Mīklas ar āķi", "Riddles with a catch"), 3,
                      [("mikla", 6), ("piramida", 4)])]),
          ]),
        K("6.", ("Atmiņa un uzmanība", "Memory and attention"),
          ("Iegaumē, pamani un saskaiti - ātri un precīzi.",
           "Remember, notice and count - quickly and precisely."), [
              L(1, [T(("Spīdošās rūtiņas", "Glowing squares"), 1,
                      [("atmina_rezgis", 10)]),
                    T(("Ko tu redzēji?", "What did you see?"), 1,
                      [("atmina_cipari", 5), ("atmina_figuras", 5)]),
                    T(("Asā acs", "Sharp eye"), 1,
                      [("skaiti", 5), ("atzime", 5)])]),
              L(2, [T(("Rūtiņu labirints", "Square maze"), 2,
                      [("atmina_rezgis", 10)]),
                    T(("Figūru rinda", "Row of shapes"), 2,
                      [("atmina_figuras", 5), ("atmina_cipari", 5)]),
                    T(("Detektīva acs", "Detective's eye"), 2,
                      [("atzime", 5), ("skaiti", 5)])]),
              L(3, [T(("Atmiņas čempions", "Memory champion"), 3,
                      [("atmina_rezgis", 10)]),
                    T(("Ciparu virtuozs", "Digit virtuoso"), 3,
                      [("atmina_cipari", 6), ("atmina_figuras", 4)]),
                    T(("Uzmanības meistars", "Attention master"), 3,
                      [("atzime", 5), ("skaiti", 5)])]),
          ]),
        K("7.", ("Lielie IQ testi", "Big IQ tests"),
          ("15 dažādas mīklas pēc kārtas - pārbaudi sevi visās jomās.",
           "15 different puzzles in a row - test yourself in every area."), [
              B(t("Viss kopā · trīs līmeņi",
                  "Everything together · three levels"), [
                  T(("IQ tests: sākums", "IQ test: start"), 1, _JAUKTS),
                  T(("IQ tests: izaicinājums", "IQ test: challenge"), 2,
                    _JAUKTS),
                  T(("IQ tests: ģēnijs", "IQ test: genius"), 3, _JAUKTS),
              ]),
          ]),
    ]


_KURSI = {}


def kurss():
    """IQ «klase» tagadējā valodā - katrai valodai uzbūvēta vienreiz."""
    v = valoda.tagad()
    if v not in _KURSI:
        _KURSI[v] = Kurss(kategorijas())
    return _KURSI[v]
