# -*- coding: utf-8 -*-
"""
Uzdevuma risinājuma pieraksta pārbaude - viens noteikumu īpašnieks (SRP).

Latviešu standarts prasa, lai zīme starp soļa pusēm būtu godīga:

    "="  tikai tad, ja abas puses tiešām ir vienādas;
    "≈"  tikai tad, ja kaut kur ir noapaļots.

Abas kļūdas ir vienlīdz nepareizas, tāpēc tās meklē viena un tā pati
staigāšana pa uzdevuma soļiem. Soļi nav savstarpēji neatkarīgi:

    1)  λ = 1500 : 40 000        λ kļūst zināms - precīzi 0,0375
    2)  λ = 0,0375 m             tā pati vērtība, tātad "="
    3)  λ ≈ 37,5 mm              tas pats skaitlis citā mērvienībā -
                                 te "≈" ir nepelnīts, jāraksta "="

Tāpēc modulis tur līdzi uzdevuma "atmiņu": ko katrs apzīmējums nozīmē un
vai tā vērtība jau reiz ir noapaļota (tad "≈" tālāk ir pareizi).

Rēķina aritmetika.py, mērvienības pārrēķina mervienibas.py; šeit ir tikai
lēmums par zīmi. Izdruka ir check_math.py, labošana - fix_math.py (abi
lieto šo vienu funkciju, DRY):

    import risinajums as R

    R.parbaudit(uzdevums)   -> [Piezime(veids, apraksts, rinda, labota), ...]
"""

import collections
import re
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import aritmetika as A          # noqa: E402
import mervienibas as MV        # noqa: E402

# Cik daudz drīkst atšķirties puses, ko savieno "=".
EXACT = 5e-4
# Virs šīs starpības tā vairs nav noapaļošana, bet kļūda.
GROSS = 0.05
# Cik tuvu jābūt pusēm, lai "≈" būtu nepelnīts. Robeža ir daudz stingrāka
# nekā EXACT: "precīzi vienāds" nozīmē vienādu līdz pēdējai zīmei, citādi
# par noapaļojumu nosauktu arī īstu noapaļojumu (√3,06 ≈ 1,75).
PRECIZI = 1e-9

Piezime = collections.namedtuple("Piezime", "veids apraksts rinda labota")
# Viens soļa segments: cik liels, kādā mērvienībā, vai noapaļots un vai
# vērtība nāk no agrāka soļa (tad tā ir atmiņa, nevis šī soļa apgalvojums).
Segments = collections.namedtuple("Segments", "vertiba mervieniba noapalots "
                                              "no_atminas")

# Skaitlis latviešu pierakstā: "39,4", "40 000", "1500".
_SKAITLIS = re.compile(r"\d+(?:[  ]\d{3})*(?:,\d+)?")
# Soļa numurs rindas sākumā ("3)  ") pie apzīmējuma nepieder.
_SOLIS = re.compile(r"^\s*\d+\)\s*")
# Apzīmējums, ko drīkst atcerēties: "λ", "T", "v(m)", "Δt", "T/T(Z)".
_APZIME = re.compile(r"[A-Za-zĀ-žΑ-Ωα-ωΔ∆][A-Za-zĀ-žΑ-Ωα-ω₀-₉ₓ()/²³_]{0,13}$")


def _rel(a, b):
    if a == b:
        return 0.0
    mers = max(abs(a), abs(b))
    return abs(a - b) / mers if mers else abs(a - b)


def _viens_lielums(a, b):
    """Vai abas mērvienības apzīmē vienu lielumu (tātad puses salīdzināmas)?

    Vienāds pieraksts der vienmēr; atšķirīgs - tikai tad, ja abas
    mērvienības ir pazīstamas un pārrēķināmas ("m" un "mm"). Ja vienas
    puses mērvienība nav zināma, apgalvojuma lielumu nesalīdzina.
    """
    if a.strip() == b.strip():
        return True
    return (MV.pamatot(a) is not None and MV.pamatot(b) is not None
            and MV.koeficients(a, b) is not None)


def _apzime(izteiksme):
    """Apzīmējums, ja segments ir tikai apzīmējums; citādi None."""
    t = _SOLIS.sub("", izteiksme).strip()
    return t if _APZIME.match(t) else None


class Atmina(object):
    """Ko uzdevums jau ir pateicis: apzīmējumu vērtības un noapaļojumi."""

    def __init__(self):
        self.vertibas = {}          # apzīmējums -> (vērtība, mērvienība)
        self.noapalotie = set()     # apzīmējumi, kuru vērtība ir noapaļota
        self.skaitli = set()        # noapaļoti skaitļi, kā tie uzrakstīti

    def atcereties(self, apzime, vertiba, mervieniba, noapalots):
        if apzime is None or vertiba is None:
            return
        self.vertibas[apzime] = (vertiba, mervieniba)
        if noapalots:
            self.noapalotie.add(apzime)
        else:
            self.noapalotie.discard(apzime)

    def pierakstit_skaitlus(self, izteiksme):
        """Noapaļotā soļa skaitļus atceras, lai tos pazītu nākamajā solī."""
        for m in _SKAITLIS.finditer(izteiksme):
            if "," in m.group(0) or len(m.group(0)) >= 3:
                self.skaitli.add(m.group(0))

    def satur_noapalotu(self, izteiksme):
        return any(s in izteiksme for s in self.skaitli)

    def nolasit(self, izteiksme):
        """Viena soļa segmenta vērtība - izrēķināta vai atcerēta."""
        v, u = A.value(izteiksme), A.unit(izteiksme)
        if v is not None:
            return Segments(v, u, self.satur_noapalotu(izteiksme), False)
        apzime = _apzime(izteiksme)
        if apzime in self.vertibas:
            v, u = self.vertibas[apzime]
            return Segments(v, u, apzime in self.noapalotie, True)
        return Segments(None, u, False, False)


def _lemums(zime, kreisa, laba, noapalots):
    """Vai zīme starp divām soļa pusēm ir pelnīta?

    Atgriež (zīme, piezīme, vai_rezultāts_noapaļots). Vienīgā vieta, kur
    "=" un "≈" izvēli izšķir - to pašu lēmumu lieto gan check_math.py
    izdrukai, gan fix_math.py labojumam (DRY).
    """
    k = (MV.koeficients(laba.mervieniba, kreisa.mervieniba)
         if kreisa.vertiba is not None and laba.vertiba is not None else None)
    if k is None:
        # Salīdzināt neizdevās (viena puse ir apzīmējums vai mērvienības nav
        # pārrēķināmas). Ja autors pats ir uzrakstījis "≈", vērtība ir
        # noapaļota, un tālāk uzdevumā to par precīzu neuzskata.
        return zime, None, laba.noapalots or "≈" in zime

    d = _rel(kreisa.vertiba, laba.vertiba * k)
    aiz = laba.vertiba * k
    if d > GROSS:
        # Rupju kļūdu meklē tikai tur, kur abas puses ir šī paša soļa
        # apgalvojums par vienu lielumu. Ja kreisā puse nāk no atmiņas,
        # apzīmējums visdrīzāk vienkārši lietots otrreiz ("x" mazākajai un
        # lielākajai slodzei), nevis kļūdains.
        if _viens_lielums(kreisa.mervieniba, laba.mervieniba)                 and not kreisa.no_atminas:
            return zime, ("KĻŪDA", "%.6g %s %.6g" % (kreisa.vertiba,
                                                     zime.strip(), aiz)), True
        return zime, None, True
    if d > EXACT:
        if "=" in zime:
            return zime.replace("=", "≈"), ("=→≈", "%.6g ≠ %.6g"
                                            % (kreisa.vertiba, aiz)), True
        return zime, None, True
    if d > PRECIZI:
        return zime, None, True          # noapaļots, bet zīme jau ir "≈"
    if "≈" in zime and not (noapalots or laba.noapalots):
        return zime.replace("≈", "="), ("≈→=", "precīzi vienādi"), False
    return zime, None, laba.noapalots


def _apgalvojums(atmina, teksts):
    """Viens apgalvojums: (labotais teksts, [(veids, apraksts), ...]).

    Iet pa "=" / "≈" zīmēm no kreisās uz labo, katrai prasa _lemums()
    spriedumu un pa ceļam uzkrāj, vai ķēdē jau kaut kas ir noapaļots.
    """
    gab = A.split_keep(teksts)
    if len(gab) < 3:
        return teksts, []

    piez = []
    kreisa = atmina.nolasit(gab[0])
    noapalots, kreisais = kreisa.noapalots, _SOLIS.sub("", gab[0]).strip()
    # Ko no šī apgalvojuma ir vērts atcerēties: precīzāko vērtību, t.i. to,
    # kas pierakstīta pirms pirmās noapaļošanas. Citādi "v = 24 m/s =
    # 86 km/h" liktu atcerēties noapaļotās 86 km/h, un vēlāk precīzais
    # "v = 24 m/s" izskatītos pēc noapaļojuma.
    labakais = None
    for i in range(1, len(gab) - 1, 2):
        labais, veca_zime = gab[i + 1], gab[i]
        laba = atmina.nolasit(labais)
        gab[i], piezime, cur_noap = _lemums(gab[i], kreisa, laba, noapalots)
        if piezime:
            # Piezīmē rāda to, kas avotā ir uzrakstīts, nevis labojumu.
            piez.append((piezime[0], "%s %s %s  (%s)"
                         % (kreisais, veca_zime.strip(), labais.strip(),
                            piezime[1])))
        if laba.vertiba is None:
            continue
        if cur_noap:
            atmina.pierakstit_skaitlus(labais)
        kreisa = laba._replace(noapalots=cur_noap)
        noapalots = noapalots or cur_noap
        kreisais = labais.strip()
        if not noapalots:
            labakais = (laba.vertiba, laba.mervieniba)

    # Ko šis apgalvojums iemācīja par kreisās puses apzīmējumu.
    if labakais is not None:
        atmina.atcereties(_apzime(gab[0]), labakais[0], labakais[1], False)
    else:
        atmina.atcereties(_apzime(gab[0]), kreisa.vertiba, kreisa.mervieniba,
                          noapalots)
    return "".join(gab), piez


def labot_rindu(atmina, rinda):
    """(labotā rinda, [(veids, apraksts), ...]) - viena soļa rinda."""
    gab = A.split_keep(rinda, A.STATEMENT)
    piez = []
    for i in range(0, len(gab), 2):
        gab[i], p = _apgalvojums(atmina, gab[i])
        piez.extend(p)
    return "".join(gab), piez


def rindas(u):
    """Uzdevuma rindas, kurās zīme ir jāpārbauda."""
    return list(u["aprekins"]) + [u["atbilde"]]


def parbaudit(u):
    """Visa uzdevuma piezīmes; «labota» ir rinda ar izlabotām zīmēm."""
    atmina, out = Atmina(), []
    for rinda in rindas(u):
        labota, piez = labot_rindu(atmina, rinda)
        for veids, apraksts in piez:
            out.append(Piezime(veids, apraksts, rinda, labota))
    return out
