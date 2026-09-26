# -*- coding: utf-8 -*-
"""1.-2. klases zīmējumi: priekšmeti rindās, pulkstenis, nauda, desmitnieka
rāmis, skaitļa mājiņa, desmiti un vieni, simta kvadrāts, rūtiņu laukums ar
ceļu un lineāls.

Pirmklasnieks skaitli vispirms redz kā lietas, tikai tad kā ciparu, tāpēc
šie zīmējumi rāda skaitu, nevis formulu. Tie lieto to pašu zīmēšanas pamatu,
ko math_zimejumi.py (_svg, _teksts, PLATUMS), un tos pašus priekšmetu
attēlus, ko spēles (math_ikonas.py) - tā ābols zīmējumā un spēlē izskatās
vienādi (DRY). Šis modulis zina tikai, kā zīmēt (SRP).

    Sakums("Cik ābolu?", zimejums=bildes([("abols", 5)]))
"""

import math

import math_ikonas
from math_zimejumi import PLATUMS, _svg, _teksts, _virs_atkape, _virs_linija


def _virsraksts(virsraksts):
    """(zīmējuma daļas, y, no kura sākas saturs) - virsraksts augšā."""
    if not virsraksts:
        return [], 2.0
    return ([_teksts(PLATUMS / 2, 4.6 + _virs_linija(virsraksts),
                     virsraksts, "z-virs")],
            7.0 + _virs_atkape(virsraksts))


def _ikona(vards, x, y, izmers):
    """Priekšmeta attēls izmers × izmers vienību kvadrātā ar kreiso augšējo
    stūri (x; y). Vārds ar zvaigznīti («aplis*») ir otrā krāsā - tā redz
    divpusējas ripiņas un rakstu, kas atkārtojas."""
    otra = vards.endswith("*")
    vards = vards.rstrip("*")
    forma = math_ikonas.svg(vards)
    iekss = forma[forma.index(">") + 1:forma.rindex("</svg>")]
    return ('<g class="z-ik%s" transform="translate(%.2f %.2f) scale(%.4f)">'
            '%s</g>' % (" otra" if otra else "", x, y, izmers / 64.0, iekss))


def _izvers(rinda):
    """Rinda var saturēt ("abols", 5) - tas ir pieci āboli pēc kārtas."""
    out = []
    for v in rinda:
        if isinstance(v, tuple):
            out.extend([v[0]] * v[1])
        else:
            out.append(v)
    return out


def bildes(rindas, virsraksts=None, uzraksti=None):
    """Priekšmeti rindās - skaitīšanai, salīdzināšanai un virknēm.

    rindas: [["abols", "abols", None], [("bumba", 4)], ...] - katra rinda ir
    saraksts; ("abols", 5) ir pieci āboli, None - tukša vieta ar «?» (virknē
    jāuzmin nākamais), "" - tukša vieta bez zīmes. «aplis*» - otrā krāsā.
    uzraksti: katras rindas nosaukums kreisajā pusē (piem. «pie loga»).
    Visās rindās attēli ir vienā lielumā un stāv viens zem otra, tāpēc divas
    rindas var salīdzināt pa pāriem - to jau redz, nevis skaita.
    """
    rindas = [_izvers(r) for r in rindas]
    n = max(len(r) for r in rindas)
    kreisa = 16.0 if uzraksti else 0.0
    solis = min(14.0, (PLATUMS - 4.0 - kreisa) / n)
    izmers = solis * 0.84
    dalas, y0 = _virsraksts(virsraksts)
    x0 = (PLATUMS - kreisa - solis * n) / 2.0 + kreisa
    for i, rinda in enumerate(rindas):
        y = y0 + i * solis
        if uzraksti:
            dalas.append(_teksts(kreisa / 2 + 1.0, y + solis * 0.58,
                                 uzraksti[i], "z-nr", maks=kreisa))
        for j, v in enumerate(rinda):
            x = x0 + j * solis + (solis - izmers) / 2.0
            if v is None:
                dalas.append('<rect class="z-ruts tuksa" x="%.2f" y="%.2f" '
                             'width="%.2f" height="%.2f" rx="1.5"/>'
                             % (x, y + (solis - izmers) / 2, izmers, izmers))
                dalas.append(_teksts(x + izmers / 2, y + solis * 0.64, "?",
                                     "z-ruts-c tuksa"))
            elif v:
                dalas.append(_ikona(v, x, y + (solis - izmers) / 2, izmers))
    return _svg(y0 + len(rindas) * solis + 2.0, "".join(dalas))


def pulkstenis(stundas, minutes=0, virsraksts=None):
    """Analogais pulkstenis: ciparnīca ar 12 cipariem un diviem rādītājiem.

    Stundu rādītājs starp cipariem stāv tieši tur, kur īstajā pulkstenī -
    pusseptiņos tas ir pusceļā starp 6 un 7, tāpēc attēls māca to pašu, ko
    sienas pulkstenis.
    """
    dalas, y0 = _virsraksts(virsraksts)
    r = 22.0
    cx, cy = PLATUMS / 2, y0 + r + 1.0
    dalas.append('<circle class="z-ciparnica" cx="%.2f" cy="%.2f" r="%.2f"/>'
                 % (cx, cy, r))
    for i in range(60):
        a = math.radians(i * 6 - 90)
        garums = 2.6 if i % 5 == 0 else 1.1
        dalas.append('<line class="z-iedala" x1="%.2f" y1="%.2f" x2="%.2f" '
                     'y2="%.2f"/>'
                     % (cx + (r - garums) * math.cos(a),
                        cy + (r - garums) * math.sin(a),
                        cx + r * math.cos(a), cy + r * math.sin(a)))
    for c in range(1, 13):
        a = math.radians(c * 30 - 90)
        dalas.append(_teksts(cx + (r - 6.0) * math.cos(a),
                             cy + (r - 6.0) * math.sin(a) + 1.4, str(c),
                             "z-cipars"))
    for garums, grads, klase in (
            (r * 0.52, ((stundas % 12) + minutes / 60.0) * 30, "z-rad"),
            (r * 0.8, minutes * 6, "z-rad min")):
        a = math.radians(grads - 90)
        dalas.append('<line class="%s" x1="%.2f" y1="%.2f" x2="%.2f" '
                     'y2="%.2f"/>' % (klase, cx, cy, cx + garums * math.cos(a),
                                      cy + garums * math.sin(a)))
    dalas.append('<circle class="z-punkts" cx="%.2f" cy="%.2f" r="1.2"/>'
                 % (cx, cy))
    return _svg(cy + r + 2.0, "".join(dalas))


def _naudas_vertiba(s):
    """«50 c» -> 50, «2 €» -> 200 (centos) - lai monētas lielums atbilst."""
    skaitlis, zime = s.split()
    return int(skaitlis) * (100 if zime == "€" else 1)


def monetas(vertibas, virsraksts=None):
    """Nauda rindā: monētas - apļi, banknotes (no 5 €) - taisnstūri.

    vertibas: ["1 €", "50 c", "20 c", ...]. Lielāka monēta ir lielāka arī
    attēlā, bet uzraksts vienmēr ir tajā - skolēns mācās lasīt vērtību, nevis
    minēt pēc izmēra.
    """
    dalas, y0 = _virsraksts(virsraksts)
    platumi = []
    for v in vertibas:
        c = _naudas_vertiba(v)
        platumi.append(22.0 if c >= 500 else 11.0 + 5.0 * min(c, 200) / 200.0)
    atstarpe = 2.0
    kopa = sum(platumi) + atstarpe * (len(platumi) - 1)
    merogs = min(1.0, (PLATUMS - 4.0) / kopa)
    x = (PLATUMS - kopa * merogs) / 2.0
    aug = 16.0 * merogs
    for v, p in zip(vertibas, platumi):
        p *= merogs
        cy = y0 + aug / 2
        if _naudas_vertiba(v) >= 500:
            dalas.append('<rect class="z-nauda banknote" x="%.2f" y="%.2f" '
                         'width="%.2f" height="%.2f" rx="1.2"/>'
                         % (x, cy - p * 0.3, p, p * 0.6))
        else:
            dalas.append('<circle class="z-nauda" cx="%.2f" cy="%.2f" '
                         'r="%.2f"/>' % (x + p / 2, cy, p / 2))
        dalas.append(_teksts(x + p / 2, cy + 1.3, v, "z-nr", maks=p - 1.0))
        x += p + atstarpe * merogs
    return _svg(y0 + aug + 2.0, "".join(dalas))


def ramis(n, ramji=1, otra=0, virsraksts=None):
    """Desmitnieka rāmis: 2 rindas pa 5 rūtiņām, n no tām ar ripiņu.

    Ripiņas liek kā klasē - vispirms augšējā rinda no kreisās, tad apakšējā,
    tāpēc 7 izskatās kā «pilna rinda un vēl 2» un tukšās rūtiņas uzreiz
    pasaka, cik pietrūkst līdz 10. ramji=2 - divi rāmji blakus (skaitļi līdz
    20); otra - cik pēdējo ripiņu ir otrā krāsā (8 + 5: astoņas un piecas).
    """
    dalas, y0 = _virsraksts(virsraksts)
    atstarpe = 6.0
    mala = min(9.0, (PLATUMS - 4.0 - atstarpe * (ramji - 1)) / (5 * ramji))
    kopa = mala * 5 * ramji + atstarpe * (ramji - 1)
    x0 = (PLATUMS - kopa) / 2.0
    for k in range(ramji):
        for i in range(10):
            rinda, kol = divmod(i, 5)
            x = x0 + k * (mala * 5 + atstarpe) + kol * mala
            y = y0 + rinda * mala
            dalas.append('<rect class="z-ruts" x="%.2f" y="%.2f" width="%.2f" '
                         'height="%.2f"/>' % (x, y, mala, mala))
            nr = k * 10 + i
            if nr < n:
                klase = "z-ripa otra" if nr >= n - otra else "z-ripa"
                dalas.append('<circle class="%s" cx="%.2f" cy="%.2f" '
                             'r="%.2f"/>'
                             % (klase, x + mala / 2, y + mala / 2, mala * 0.36))
    return _svg(y0 + 2 * mala + 2.0, "".join(dalas))


def majina(skaitlis, stavi, virsraksts=None):
    """Skaitļa mājiņa: jumtā skaitlis, katrā stāvā divas daļas, kas kopā to
    dod. None - tukša rūtiņa ar «?», ko skolēns aizpilda.

        majina(5, [(1, 4), (2, None), (None, 2)])
    """
    dalas, y0 = _virsraksts(virsraksts)
    mala = 12.0
    x0 = PLATUMS / 2 - mala
    jumts = 11.0
    dalas.append('<path class="z-figura" d="M%.2f %.2fL%.2f %.2fL%.2f %.2fz"/>'
                 % (x0 - 3, y0 + jumts, PLATUMS / 2, y0, x0 + 2 * mala + 3,
                    y0 + jumts))
    dalas.append(_teksts(PLATUMS / 2, y0 + jumts - 2.2,
                         "?" if skaitlis is None else str(skaitlis),
                         "z-ruts-c" + (" tuksa" if skaitlis is None else "")))
    for i, stavs in enumerate(stavi):
        for j, v in enumerate(stavs):
            x, y = x0 + j * mala, y0 + jumts + i * mala
            tuksa = " tuksa" if v is None else ""
            dalas.append('<rect class="z-ruts%s" x="%.2f" y="%.2f" '
                         'width="%.2f" height="%.2f"/>'
                         % (tuksa, x, y, mala, mala))
            dalas.append(_teksts(x + mala / 2, y + mala * 0.66,
                                 "?" if v is None else str(v),
                                 "z-ruts-c" + tuksa))
    return _svg(y0 + jumts + len(stavi) * mala + 2.0, "".join(dalas))


def desmiti(d, v, virsraksts=None):
    """Desmiti un vieni: d stienīši pa 10 kubiņiem un v atsevišķi kubiņi.

    Stienis ir sadalīts desmit kubiņos, tāpēc redz, ka «viens desmits» ir
    tieši desmit vieni - tā pati lieta, tikai sasaistīta kopā.
    """
    dalas, y0 = _virsraksts(virsraksts)
    kubs = 4.0
    atst = 2.2
    kopa = (d * (kubs + atst) + (atst * 2 if d and v else 0)
            + min(v, 10) * (kubs + 1))
    x = (PLATUMS - kopa) / 2.0
    for _ in range(d):
        for i in range(10):
            dalas.append('<rect class="z-kubs" x="%.2f" y="%.2f" width="%.2f" '
                         'height="%.2f"/>' % (x, y0 + i * kubs, kubs, kubs))
        x += kubs + atst
    if d and v:
        x += atst * 2
    # Vairāk nekā 10 vienu (38 + 25 = 5 desmiti un 13 vieni) liek otrā
    # rindā virs pirmās - tieši tā izskatās brīdis pirms jaunā desmita.
    for i in range(v):
        rinda, kol = divmod(i, 10)
        dalas.append('<rect class="z-kubs viens" x="%.2f" y="%.2f" '
                     'width="%.2f" height="%.2f"/>'
                     % (x + kol * (kubs + 1), y0 + (9 - rinda * 1.25) * kubs,
                        kubs, kubs))
    return _svg(y0 + 10 * kubs + 2.0, "".join(dalas))


def simta_kvadrats(no=1, lidz=100, slept=(), izcelt=(), virsraksts=None):
    """Simta kvadrāts (vai tā rindas): skaitļi pa 10 rindā.

    no, lidz - kuras rindas rādīt (no 1 līdz 100 - viss kvadrāts; no 41 līdz
    60 - divas rindas). slept - skaitļi, kuru vietā ir «?»; izcelt - skaitļi
    iekrāsotā rūtiņā (skaitīšana pa 5, kaimiņi, starp).
    """
    dalas, y0 = _virsraksts(virsraksts)
    mala = 9.4
    x0 = (PLATUMS - 10 * mala) / 2.0
    pirma = (no - 1) // 10 * 10 + 1
    rindas = (lidz - pirma) // 10 + 1
    for s in range(pirma, pirma + rindas * 10):
        i, j = divmod(s - pirma, 10)
        x, y = x0 + j * mala, y0 + i * mala
        if s < no or s > lidz:
            continue
        slepts = s in slept
        klase = ("z-ruts tuksa" if slepts
                 else "z-ruts on" if s in izcelt else "z-ruts")
        dalas.append('<rect class="%s" x="%.2f" y="%.2f" width="%.2f" '
                     'height="%.2f"/>' % (klase, x, y, mala, mala))
        dalas.append(_teksts(x + mala / 2, y + mala * 0.64,
                             "?" if slepts else str(s),
                             "z-simts" + (" tuksa" if slepts else "")))
    return _svg(y0 + rindas * mala + 2.0, "".join(dalas))


_VIRZIENI = {"→": (1, 0), "←": (-1, 0), "↑": (0, -1), "↓": (0, 1)}


def celjs(kol, rind, sakums, merkis=None, soli="", skersli=(),
          virsraksts=None, zime="abols"):
    """Rūtiņu laukums: sākums (ripiņa), mērķis (attēls), šķēršļi un ceļš.

    sakums, merkis, skersli - rūtiņas (kolonna; rinda), skaitot no kreisā
    augšējā stūra no 0. soli - bultiņu virkne «→→↑↑»; ceļu zīmē ar līniju no
    sākuma, un katrs solis ir viena rūtiņa, tāpēc ceļa garumu var saskaitīt
    pa rūtiņām. zime - mērķa attēls (math_ikonas.py).
    """
    dalas, y0 = _virsraksts(virsraksts)
    mala = min(11.0, (PLATUMS - 4.0) / kol)
    x0 = (PLATUMS - kol * mala) / 2.0

    def centrs(k, r):
        return x0 + (k + 0.5) * mala, y0 + (r + 0.5) * mala

    for r in range(rind):
        for k in range(kol):
            klase = "z-ruts siena" if (k, r) in skersli else "z-ruts"
            dalas.append('<rect class="%s" x="%.2f" y="%.2f" width="%.2f" '
                         'height="%.2f"/>'
                         % (klase, x0 + k * mala, y0 + r * mala, mala, mala))
    if merkis is not None:
        dalas.append(_ikona(zime, x0 + (merkis[0] + 0.12) * mala,
                            y0 + (merkis[1] + 0.12) * mala, mala * 0.76))
    if soli:
        k, r = sakums
        punkti = [centrs(k, r)]
        for s in soli:
            dk, dr = _VIRZIENI[s]
            k, r = k + dk, r + dr
            punkti.append(centrs(k, r))
        dalas.append('<polyline class="z-cels" points="%s"/>'
                     % " ".join("%.2f,%.2f" % p for p in punkti))
    cx, cy = centrs(*sakums)
    dalas.append('<circle class="z-ripa" cx="%.2f" cy="%.2f" r="%.2f"/>'
                 % (cx, cy, mala * 0.3))
    return _svg(y0 + rind * mala + 2.0, "".join(dalas))


def lineals(garums, objekti=(), virsraksts=None, mm=False):
    """Lineāls centimetros ar izmērāmajiem nogriežņiem virs tā.

    objekti: [(no, līdz, uzraksts), ...] centimetros - josla virs lineāla.
    Nogrieznis, kas nesākas pie 0, māca to pašu, ko salauzts lineāls: garums
    ir starpība, nevis skaitlis pie gala. mm=True - katrs centimetrs sadalīts
    10 milimetros (2. klase), un no, lidz drīkst būt 6.5 (6 cm 5 mm); pusē
    centimetra iedaļa ir garāka, kā īstam lineālam.
    """
    dalas, y0 = _virsraksts(virsraksts)
    mala = 4.0
    cm = (PLATUMS - 2 * mala) / garums
    y = y0 + 7.0 * max(len(objekti), 1)
    for i, (no, lidz, uzraksts) in enumerate(objekti):
        yo = y0 + 7.0 * i + 1.5
        dalas.append('<rect class="z-lauks" x="%.2f" y="%.2f" width="%.2f" '
                     'height="3.2" rx="1"/>'
                     % (mala + no * cm, yo, (lidz - no) * cm))
        if uzraksts:
            dalas.append(_teksts(mala + (no + lidz) / 2.0 * cm, yo - 0.6,
                                 uzraksts, "z-mazs"))
    dalas.append('<rect class="z-lineals" x="%.2f" y="%.2f" width="%.2f" '
                 'height="11" rx="1"/>' % (mala - 2, y, garums * cm + 4))
    sikas = 10 if mm else 2
    for i in range(garums * sikas + 1):
        x = mala + i * cm / sikas
        if i % sikas == 0:
            gar = 3.4
        elif sikas == 10 and i % 5 == 0:
            gar = 2.6
        else:
            gar = 2.0 if sikas == 2 else 1.4
        dalas.append('<line class="z-iedala" x1="%.2f" y1="%.2f" x2="%.2f" '
                     'y2="%.2f"/>' % (x, y, x, y + gar))
        if i % sikas == 0:
            dalas.append(_teksts(x, y + 6.8, str(i // sikas), "z-mazs"))
    dalas.append(_teksts(mala + garums * cm - 2.0, y + 10.0, "cm",
                         "z-mazs"))
    return _svg(y + 13.0, "".join(dalas))


# Punktu vietas kauliņa skaldnē (0..1), kā īstam metamajam kauliņam.
_KAULINS = {
    1: [(.5, .5)],
    2: [(.25, .25), (.75, .75)],
    3: [(.25, .25), (.5, .5), (.75, .75)],
    4: [(.25, .25), (.75, .25), (.25, .75), (.75, .75)],
    5: [(.25, .25), (.75, .25), (.5, .5), (.25, .75), (.75, .75)],
    6: [(.25, .22), (.75, .22), (.25, .5), (.75, .5), (.25, .78),
        (.75, .78)],
}


def kaulini(skaitli, virsraksts=None):
    """Metamo kauliņu skaldnes rindā: [3, 5] - trīs un pieci punkti.

    Kauliņa rakstu acs pazīst uzreiz, neskaitot - tieši to 3. stundā mācās:
    pieci ir «četri stūri un vidus».
    """
    dalas, y0 = _virsraksts(virsraksts)
    n = len(skaitli)
    mala = min(20.0, (PLATUMS - 4.0 - 4.0 * (n - 1)) / n)
    x = (PLATUMS - n * mala - 4.0 * (n - 1)) / 2.0
    for s in skaitli:
        dalas.append('<rect class="z-ruts" x="%.2f" y="%.2f" width="%.2f" '
                     'height="%.2f" rx="%.2f"/>'
                     % (x, y0, mala, mala, mala * 0.18))
        for px, py in _KAULINS[s]:
            dalas.append('<circle class="z-ripa" cx="%.2f" cy="%.2f" '
                         'r="%.2f"/>'
                         % (x + px * mala, y0 + py * mala, mala * 0.09))
        x += mala + 4.0
    return _svg(y0 + mala + 2.0, "".join(dalas))


def vienibas(n, virsraksts=None):
    """Viens un tas pats garums, izmērīts ar n vienībām: vienāda platuma
    josla, sadalīta n numurētās rūtiņās.

    Josla vienmēr ir visā platumā, tāpēc 3 plaukstas un 12 dzēšgumijas
    izskatās kā tas pats galds - mainās tikai, cik reižu vienība ietilpst.
    """
    dalas, y0 = _virsraksts(virsraksts)
    platums = PLATUMS - 8.0
    solis = platums / n
    for i in range(n):
        x = 4.0 + i * solis
        dalas.append('<rect class="z-ruts" x="%.2f" y="%.2f" width="%.2f" '
                     'height="9" rx="1"/>' % (x, y0, solis))
        dalas.append(_teksts(x + solis / 2, y0 + 6.0, str(i + 1), "z-simts",
                             maks=solis - 0.6))
    return _svg(y0 + 11.0, "".join(dalas))


def sloksnes(rindas, starpiba=True, virsraksts=None):
    """Salīdzināšanas sloksnes: katra rinda - josla no vienādām rūtiņām.

    rindas: [(uzraksts, skaits), ...] vai (uzraksts, skaits, beigu_teksts) -
    beigu teksts stāv aiz joslas («?», «8»). Visas joslas sākas vienā vietā,
    tāpēc garāko var salīdzināt ar īsāko rūtiņu pa rūtiņai; starpiba=True
    izceļ rūtiņas, par kurām josla ir garāka nekā īsākā, - tieši to «par cik
    vairāk» 1.6. tematā prasa atrast.
    """
    dalas, y0 = _virsraksts(virsraksts)
    kreisa = 14.0
    labais = 7.0
    lielakais = max(r[1] for r in rindas)
    mazakais = min(r[1] for r in rindas)
    mala = min(7.0, (PLATUMS - 4.0 - kreisa - labais) / lielakais)
    x0 = 2.0 + kreisa
    for i, r in enumerate(rindas):
        uzraksts, n = r[0], r[1]
        beigas = r[2] if len(r) > 2 else str(n)
        y = y0 + i * (mala + 3.0)
        dalas.append(_teksts(kreisa / 2 + 1.0, y + mala * 0.68, uzraksts,
                             "z-nr", maks=kreisa))
        for j in range(n):
            klase = ("z-ruts dz" if starpiba and j >= mazakais
                     else "z-ruts")
            dalas.append('<rect class="%s" x="%.2f" y="%.2f" width="%.2f" '
                         'height="%.2f"/>'
                         % (klase, x0 + j * mala, y, mala, mala))
        dalas.append(_teksts(x0 + n * mala + labais / 2, y + mala * 0.7,
                             beigas, "z-atzime"))
    return _svg(y0 + len(rindas) * (mala + 3.0), "".join(dalas))


def kubi(pozicijas, virsraksts=None, aug=42.0):
    """Būve no vienādiem kubiem slīpā skatā: priekša, augša un labais sāns.

    pozicijas: [(x, y, z), ...] - x pa labi, y uz aizmuguri, z uz augšu,
    veseli skaitļi. Kubus zīmē no tālākā uz tuvāko (lielāks y vispirms,
    tad no kreisās, tad no apakšas), tāpēc aizsegtās skaldnes pārklāj
    priekšējie kubi - tā izskatās īsta klucīšu būve, ko var saskaitīt.
    """
    dalas, y0 = _virsraksts(virsraksts)
    dz = 0.5

    def p(x, y, z):
        return (x + y * dz, -z - y * dz)

    skaldnes = []
    for x, y, z in sorted(pozicijas, key=lambda k: (-k[1], k[0], k[2])):
        skaldnes.append(("z-kf", [p(x, y, z), p(x + 1, y, z),
                                  p(x + 1, y, z + 1), p(x, y, z + 1)]))
        skaldnes.append(("z-kt", [p(x, y, z + 1), p(x + 1, y, z + 1),
                                  p(x + 1, y + 1, z + 1), p(x, y + 1, z + 1)]))
        skaldnes.append(("z-ks", [p(x + 1, y, z), p(x + 1, y + 1, z),
                                  p(x + 1, y + 1, z + 1), p(x + 1, y, z + 1)]))
    visi = [q for _, pp in skaldnes for q in pp]
    xmin, xmax = min(q[0] for q in visi), max(q[0] for q in visi)
    ymin, ymax = min(q[1] for q in visi), max(q[1] for q in visi)
    merogs = min((PLATUMS - 8.0) / (xmax - xmin), aug / (ymax - ymin))
    x0 = (PLATUMS - (xmax - xmin) * merogs) / 2.0
    for klase, pp in skaldnes:
        dalas.append('<polygon class="%s" points="%s"/>' % (klase, " ".join(
            "%.2f,%.2f" % (x0 + (q[0] - xmin) * merogs,
                           y0 + (q[1] - ymin) * merogs) for q in pp)))
    return _svg(y0 + (ymax - ymin) * merogs + 2.0, "".join(dalas))


def stabins(a, b, zime="+", rezultats=True, virs=None, virsraksts=None):
    """Saskaitīšana vai atņemšana stabiņā: cipari rūtiņās, vieni zem
    vieniem, desmiti zem desmitiem, zem svītras - rezultāts.

    rezultats=False - rezultāta vietā tukšas rūtiņas ar «?», ko skolēns
    izrēķina pats. virs - mazs cipars virs desmitu kolonnas: saskaitot tas
    ir pārnestais desmits («1»), atņemot - sadalītais desmits («10»). Kas
    ir rezultāts, izrēķina pats zīmējums, tāpēc atbilde vienmēr sakrīt ar
    uzdevumu (DRY).
    """
    c = a + b if zime == "+" else a - b
    rindas = [str(a), str(b), str(c)]
    n = max(len(r) for r in rindas)
    mala = 9.0
    dalas, y0 = _virsraksts(virsraksts)
    if virs:
        y0 += 4.0
    x0 = (PLATUMS - mala * (n + 1)) / 2.0 + mala

    def cipari(s, y, tukss=False):
        for i, cip in enumerate(s.rjust(n)):
            if cip == " ":
                continue
            x = x0 + i * mala
            klase = "z-ruts tuksa" if tukss else "z-ruts"
            dalas.append('<rect class="%s" x="%.2f" y="%.2f" width="%.2f" '
                         'height="%.2f" rx="1"/>' % (klase, x, y, mala, mala))
            dalas.append(_teksts(x + mala / 2, y + mala * 0.68,
                                 "?" if tukss else cip,
                                 "z-ruts-c" + (" tuksa" if tukss else "")))

    if virs:
        dalas.append(_teksts(x0 + (n - 2) * mala + mala / 2, y0 - 1.2,
                             virs, "z-atzime"))
    cipari(rindas[0], y0)
    dalas.append(_teksts(x0 - mala / 2, y0 + mala * 1.68,
                         "+" if zime == "+" else "−", "z-ruts-c"))
    cipari(rindas[1], y0 + mala)
    ys = y0 + 2 * mala + 1.2
    dalas.append('<line class="z-ass" x1="%.2f" y1="%.2f" x2="%.2f" '
                 'y2="%.2f"/>' % (x0 - mala, ys, x0 + n * mala, ys))
    cipari(rindas[2], ys + 1.2, tukss=not rezultats)
    return _svg(ys + 1.2 + mala + 2.0, "".join(dalas))


def algoritms(soli, virsraksts=None):
    """Algoritma shēma: soļi kastītēs no augšas uz leju, starp tiem bultas.

    soli: ["Paņem skaitli", ("Vai ir lielāks nekā 50?", "atņem 10",
    "pieskaiti 10"), "Pieraksti rezultātu"]. Teksts ir parasts solis;
    trijnieks (jautājums, ja jā, ja nē) ir nosacījums - rombveida kaste un
    zem tās divi zari, kas pēc tam atkal saiet kopā. Tā pati shēma der gan
    lineāram, gan sazarotam algoritmam (DRY).
    """
    dalas, y = _virsraksts(virsraksts)
    plat, aug, bulta = 76.0, 9.0, 5.0
    x0 = (PLATUMS - plat) / 2.0
    cx = PLATUMS / 2.0

    def kaste(x, y, w, teksts, klase="z-ruts"):
        dalas.append('<rect class="%s" x="%.2f" y="%.2f" width="%.2f" '
                     'height="%.2f" rx="2"/>' % (klase, x, y, w, aug))
        dalas.append(_teksts(x + w / 2, y + aug * 0.64, teksts, "z-nr",
                             maks=w - 3.0))

    def lejup(x, y1, y2):
        dalas.append('<line class="z-ass" x1="%.2f" y1="%.2f" x2="%.2f" '
                     'y2="%.2f"/>' % (x, y1, x, y2 - 1.2))
        dalas.append('<path class="z-ass" d="M%.2f %.2f l-1.4 -2.2 h2.8 z"/>'
                     % (x, y2))

    for i, s in enumerate(soli):
        if i:
            lejup(cx, y, y + bulta)
            y += bulta
        if isinstance(s, tuple):
            jaut, ja, ne = s
            dalas.append('<path class="z-ruts tuksa" d="M%.2f %.2f L%.2f %.2f '
                         'L%.2f %.2f L%.2f %.2f L%.2f %.2f L%.2f %.2f Z"/>'
                         % (x0, y + aug / 2, x0 + 5, y, x0 + plat - 5, y,
                            x0 + plat, y + aug / 2, x0 + plat - 5, y + aug,
                            x0 + 5, y + aug))
            dalas.append(_teksts(cx, y + aug * 0.64, jaut, "z-nr",
                                 maks=plat - 10.0))
            w = plat / 2 - 2.0
            xl, xr = x0, x0 + plat / 2 + 2.0
            for xz, zars, teksts in ((xl, "jā", ja), (xr, "nē", ne)):
                lejup(xz + w / 2, y + aug, y + aug + bulta + 1.0)
                dalas.append(_teksts(xz + w / 2 + 4.0, y + aug + 3.4, zars,
                                     "z-mazs"))
                kaste(xz, y + aug + bulta + 1.0, w, teksts)
            y += 2 * aug + bulta + 1.0
            ys = y + 2.5
            for xz in (xl, xr):
                dalas.append('<line class="z-ass" x1="%.2f" y1="%.2f" '
                             'x2="%.2f" y2="%.2f"/>'
                             % (xz + w / 2, y, xz + w / 2, ys))
            dalas.append('<line class="z-ass" x1="%.2f" y1="%.2f" x2="%.2f" '
                         'y2="%.2f"/>' % (xl + w / 2, ys, xr + w / 2, ys))
            y = ys
        else:
            kaste(x0, y, plat, s)
            y += aug
    return _svg(y + 2.0, "".join(dalas))


def rutinas(kol, rind, a=None, b=None, virsraksts=None):
    """Taisnstūris no kol x rind vienādām kvadrātveida rūtiņām; a kolonnas
    un b rindas no kreisā augšējā stūra iekrāsotas.

    Rūtiņa vienmēr ir kvadrāts (atšķirībā no math_zimejumi.kvadrats, kas
    visu režģi ievelk vienā kvadrātā), tāpēc 5 x 3 izskatās kā īsta flīžu
    grīda vai šokolāde, un to pašu attēlu lieto gan laukumam rūtiņās, gan
    reizinājumam «3 rindas pa 5».
    """
    a = kol if a is None else a
    b = rind if b is None else b
    dalas, y0 = _virsraksts(virsraksts)
    mala = min(9.0, (PLATUMS - 8.0) / kol, 60.0 / rind)
    x0 = (PLATUMS - mala * kol) / 2.0
    for r in range(rind):
        for k in range(kol):
            klase = "z-lauks" if k < a and r < b else "z-ruts"
            dalas.append('<rect class="%s" x="%.2f" y="%.2f" width="%.2f" '
                         'height="%.2f"/>'
                         % (klase, x0 + k * mala, y0 + r * mala, mala, mala))
    dalas.append('<rect class="z-rame" x="%.2f" y="%.2f" width="%.2f" '
                 'height="%.2f"/>' % (x0, y0, mala * kol, mala * rind))
    return _svg(y0 + mala * rind + 2.0, "".join(dalas))
