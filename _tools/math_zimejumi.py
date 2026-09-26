# -*- coding: utf-8 -*-
"""Stundas zīmējumi: skaitļu taisne, laika ass un Venna diagramma.

Zīmējumus zīmē pati lapa ar SVG, nevis ņem kā attēlus: tie mērogojas līdz ar
tekstu, ir vienā krāsā ar pārējo lapu un telefonā paliek asi. Stundas saturs
zīmējumu pasūta ar vārdiem - cik liela ir ass un kas uz tās jāatzīmē -, tāpēc
pašā stundas failā SVG nav (SRP).

    Zimejums("Skaitļu taisne", taisne(0, 100, 10, [(30, "30"), (75, "75")]))

Zīmējuma laukums ir platumam pielāgots (viewBox + preserveAspectRatio), tāpēc
tas pats zīmējums der gan telefonā, gan uz visa ekrāna (DRY).
"""

import math
import re

import mathfmt as MF
from math_bloki import Bloks, esc, teksts

# Zīmējuma iekšējais koordinātu tīkls. Platums ir 100 vienības, tāpēc
# procentus var rakstīt tieši; augstumu katrs zīmējums izvēlas pats.
PLATUMS = 100.0


def _svg(augstums, saturs):
    return ('<svg class="zim" viewBox="0 0 %g %g" '
            'preserveAspectRatio="xMidYMid meet" aria-hidden="true">%s</svg>'
            % (PLATUMS, augstums, saturs))


# Uzraksts zīmējumā ir SVG teksts, nevis HTML, tāpēc {3|4} marķējums tam
# neder - tur nevar ielikt <span>. Daļu te raksta ar slīpsvītru («3/4»), un
# zīmējums pats to saliek vertikāli, kā prasa latviešu standarts.
_DALA = re.compile(r"^(-?\d+)\s+(\d+)/(\d+)$|^(-?\d+)/(\d+)$")


# Burtu izmērs katrai uzraksta šķirai (math_lapa.py CSS) zīmējuma vienībās.
# Daļas mēri ir tikai šī skaitļa daļās, jo citādi svītra iznāk īsāka nekā
# cipari un jauktā skaitļa veselais uzkāpj tai virsū.
_FONTI = {"z-mazs": 3.0, "z-nr": 3.4, "z-atzime": 3.6, "z-virs": 3.8,
          "z-bits-c": 4.4, "z-ruts-c": 5.0}
_FONTS = 3.4                # tikpat, cik z-nr - noklusētā uzraksta šķira
_CIPARS = 0.58              # cipara platums burtu izmēra daļās


def _teksts(x, y, s, klase="z-nr", maks=None):
    """Uzraksts zīmējumā. maks - cik plata ir rūtiņa, kurā tas stāv: garāku
    uzrakstu saraukst, lai tas nekad neizlīstu pāri malai (sk. _ietilpina)."""
    s = str(s)
    if "{" in s and "|" in s:
        raise AssertionError(
            "zīmējuma uzrakstā «%s» nedrīkst būt {a|b} - SVG tekstā daļu "
            "raksta ar slīpsvītru («3/4»), un zīmējums to saliek pats" % s)
    m = _DALA.match(s.strip())
    if m:
        if m.group(3):
            vesels, skait, sauc = m.group(1), m.group(2), m.group(3)
        else:
            vesels, skait, sauc = None, m.group(4), m.group(5)
        return _dalas_teksts(x, y, vesels, skait, sauc, klase)
    if _DALA_TEKSTA.search(s) or MF.ROOT_SIGN in s:
        return _rinda_ar_dalu(x, y, s.strip(), klase)
    return _uzraksts(x, y, s, klase, maks)


def _ir_dala(s):
    """Vai uzraksts ir daļa - tā aizņem trīs rindas, ne vienu."""
    return bool(_DALA.match(str(s).strip()))


# Punkta indekss zīmējumā - tas pats «A_1» marķējums, ko raksta stundas
# tekstā (mathhtml), tāpēc trijstūris A_1B_1C_1 izskatās vienādi abās vietās.
_INDEKSS = re.compile(r"(?<=[^\W\d_])_(\d)")


def _uzraksts(x, y, s, klase, maks=None):
    iekss = _INDEKSS.sub(r'<tspan baseline-shift="sub" font-size="70%">'
                         r'\1</tspan>', teksts(str(s)))
    return ('<text class="%s" x="%.2f" y="%.2f" text-anchor="middle"%s>%s'
            '</text>' % (klase, x, y, _ietilpina(s.replace("_", ""), klase,
                                                 maks), iekss))


def _ietilpina(s, klase, maks):
    """Uzraksta atribūti, kas to satur rūtiņā maks vienību platumā.

    Platumu te var tikai aplēst, tāpēc garam uzrakstam burtus samazina jau
    lapā ar rezervi, un data-maks ļauj lapai pašai (JS zemāk) to pārmērīt ar
    īsto fontu - tā uzraksts ietilpst arī tad, ja aplēse kļūdījusies."""
    if not maks:
        return ""
    klase = klase.split()[0]
    fs = _FONTI.get(klase, _FONTS)
    plat = _teksta_plat(str(s), fs) * 1.08
    stils = (' style="font-size:%.2fpx"' % (fs * maks / plat)
             if plat > maks else "")
    return ' data-maks="%.2f"%s' % (maks, stils)


# Lapas gabals, kas uzrakstus pārmēra ar īsto fontu. Tas strādā pēc fontu
# ielādes vēlreiz, jo tīmekļa fonts var būt platāks par rezerves fontu.
JS = """
(function(){
  function ietilpini(){
    var t=document.querySelectorAll(".zim text[data-maks]");
    for(var i=0;i<t.length;i++){
      var maks=parseFloat(t[i].getAttribute("data-maks"));
      var gar=t[i].getComputedTextLength?t[i].getComputedTextLength():0;
      if(!gar||gar<=maks){continue;}
      var fs=parseFloat(window.getComputedStyle(t[i]).fontSize)||0;
      if(fs){t[i].style.fontSize=(fs*maks/gar*0.97)+"px";}
    }
  }
  ietilpini();
  if(document.fonts&&document.fonts.ready){
    document.fonts.ready.then(ietilpini);
  }
  window.addEventListener("load",ietilpini);
})();
"""


def _dalas_teksts(x, y, vesels, skait, sauc, klase):
    """Vertikāla daļa zīmējumā: skaitītājs virs svītras, saucējs zem tās.

    Svītra ir garāka par plašāko ciparu rindu, un jauktā skaitļa veselais
    stāv savrup no tās - tā pati forma, ko tekstā dod .f (math_lapa.py CSS).
    """
    fs = _FONTI.get(klase, _FONTS)
    cipars = _CIPARS * fs
    # Skaitītājs var būt sakne («√3/2» = √3 virs 2) - tad tā platums ir
    # saknes zīme ar vinkulu, nevis cipari.
    skait_plat = _gabala_plat(("s", skait[1:]), fs) if skait.startswith(
        MF.ROOT_SIGN) else cipars * len(skait)
    plat = max(skait_plat, cipars * len(sauc)) + 0.36 * fs
    dalas = []
    if vesels:
        vplat = cipars * len(vesels)
        starp = 0.24 * fs                     # atstarpe starp veselo un daļu
        kreisa = x - (vplat + starp + plat) / 2.0
        # Veselais stāv pret svītru - tas ir viens skaitlis, ne divi.
        dalas.append(_uzraksts(kreisa + vplat / 2.0, y + 0.35 * fs,
                               vesels, klase))
        x = kreisa + vplat + starp + plat / 2.0
    if skait.startswith(MF.ROOT_SIGN):
        dalas.append(_saknes_teksts(x - skait_plat / 2.0, y - 0.34 * fs,
                                    skait[1:], klase))
    else:
        dalas.append(_uzraksts(x, y - 0.34 * fs, skait, klase))
    dalas.append('<line class="z-dsvitra" x1="%.2f" y1="%.2f" x2="%.2f" '
                 'y2="%.2f"/>' % (x - plat / 2, y, x + plat / 2, y))
    dalas.append(_uzraksts(x, y + 0.96 * fs, sauc, klase))
    return "".join(dalas)


# Daļa uzraksta vidū: «4/8 picas», «3/4 = 180 km». Aiz slīpsvītras te
# vienmēr ir cipari, tāpēc mērvienības («m/s», «kg/m³») šim nepakļūst - tās
# ir burti. Četrciparu pāri («2024/2025») ir gadi, ne daļas.
# Skaitītājs drīkst būt arī sakne: «√2/2» ir √2 virs 2, nevis √(2/2).
_DALA_TEKSTA = re.compile(r"(?<![\d/√])(√?\d{1,3})/(\d{1,3})(?![\d/])")
# Vai tieši pirms daļas stāv veselais - «2 3/4» ir viens skaitlis.
_VESELAIS = re.compile(r"(?:^|(?<=[\s(]))(-?\d+)\s+$")

# Burtu platums burtu izmēra daļās. Mērs ir aptuvens - to lieto tikai, lai
# uzrakstu nocentrētu, un kļūda iznāk mazāka par vienu burtu.
_SAURIE = "iíjltfr.,:;'!|()[]/ "
_PLATIE = "mwMWĀ—"


def _teksta_plat(s, fs):
    plat = 0.0
    for c in s:
        if c == " ":
            plat += 0.28
        elif c in _SAURIE:
            plat += 0.31
        elif c in _PLATIE:
            plat += 0.85
        elif c.isdigit() or c.isupper():
            plat += 0.60
        else:
            plat += 0.545
    return plat * fs


def _gabali(s):
    """Uzraksts pa gabaliem: («t», teksts), («d», vesels, skaitītājs,
    saucējs) un («s», zemsaknes teksts). Veselo pievelk pie daļas, lai
    «2 3/4» paliktu viens skaitlis."""
    out = []
    for g in _dalas_gabali(s):
        out.extend(_saknes_gabali(g[1]) if g[0] == "t" else [g])
    return out


def _saknes_gabali(s):
    """Teksta gabals ar √: sakne ir savs gabals, jo tās zīmi un vinkulu
    zīmē mēs, nevis fonts (drawn-math-symbols) - kur sakne beidzas, zina
    mathfmt, tāpat kā tekstā (DRY)."""
    out, i = [], 0
    while True:
        j = s.find(MF.ROOT_SIGN, i)
        if j < 0:
            if s[i:]:
                out.append(("t", s[i:]))
            return out
        if s[i:j]:
            out.append(("t", s[i:j]))
        sakums, beigas = MF._root_span(s, j)
        iekss = s[sakums:beigas]
        if iekss.startswith("(") and iekss.endswith(")"):
            iekss = iekss[1:-1]
        out.append(("s", iekss))
        i = beigas


def _dalas_gabali(s):
    out, i = [], 0
    for m in _DALA_TEKSTA.finditer(s):
        pirms = s[i:m.start()]
        vesels = None
        v = _VESELAIS.search(pirms)
        if v:
            vesels = v.group(1)
            pirms = pirms[:v.start(1)]
        if pirms:
            out.append(("t", pirms))
        out.append(("d", vesels, m.group(1), m.group(2)))
        i = m.end()
    if s[i:]:
        out.append(("t", s[i:]))
    return out


def _gabalu_plat(s, fs):
    """Visa uzraksta platums - arī tad, ja tajā ir daļa."""
    return sum(_gabala_plat(g, fs) for g in _gabali(str(s)))


def _gabala_plat(g, fs):
    if g[0] == "t":
        return _teksta_plat(g[1], fs)
    if g[0] == "s":
        return (MF.root_width(_SAKNE_H) + MF.ROOT_INNER) * fs             + _teksta_plat(g[1], fs) + 0.12 * fs
    vesels, skait, sauc = g[1], g[2], g[3]
    cipars = _CIPARS * fs
    skait_plat = (_gabala_plat(("s", skait[1:]), fs)
                  if skait.startswith(MF.ROOT_SIGN) else cipars * len(skait))
    plat = max(skait_plat, cipars * len(sauc)) + 0.36 * fs
    if vesels:
        plat += cipars * len(vesels) + 0.24 * fs
    return plat


def _virs_atkape(virsraksts, klase="z-virs"):
    """Cik zemāk jāsākas zīmējumam, ja virsrakstā ir daļa.

    Daļai virs pamatlīnijas ir skaitītājs un zem tās saucējs, tāpēc virsraksts
    aizņem trīs rindas vienas vietā; bez šīs atkāpes saucējs nokristu uz paša
    zīmējuma. Pamatlīniju pabīda _virs_linija().
    """
    if not virsraksts:
        return 0.0
    fs = _FONTI.get(klase, _FONTS)
    s = str(virsraksts)
    return (1.08 * fs if _ir_dala(s) or _DALA_TEKSTA.search(s) else 0.0)


def _virs_linija(virsraksts, klase="z-virs"):
    """Cik zemāk jāstāv paša virsraksta pamatlīnijai (skaitītājs paliek
    turpat, kur būtu parasta virsraksta augšmala)."""
    fs = _FONTI.get(klase, _FONTS)
    return 0.34 * fs if _virs_atkape(virsraksts, klase) else 0.0


def _zem_pamatlinijas(s, klase="z-nr"):
    """Cik vietas uzraksts prasa zem savas pamatlīnijas.

    Daļai tur ir vesela rinda - saucējs -, tāpēc zīmējums, kura apakšā stāv
    daļa, ir attiecīgi augstāks; citādi saucējs uzkristu tekstam zem attēla.
    """
    fs = _FONTI.get(klase, _FONTS)
    s = str(s)
    return (1.15 * fs if _ir_dala(s) or _DALA_TEKSTA.search(s)
            else 0.25 * fs)


def _rinda_ar_dalu(x, y, s, klase):
    """Uzraksts, kurā daļa stāv starp vārdiem: vārdi rindā, daļa vertikāli.

    Platumu mēra pēc burtu skaita (_teksta_plat), jo SVG teksts pats savu
    platumu pasaka tikai pārlūkā; centrēšanai ar to pietiek.
    """
    fs = _FONTI.get(klase, _FONTS)
    gabali = _gabali(s)
    platumi = [_gabala_plat(g, fs) for g in gabali]
    xi = x - sum(platumi) / 2.0
    out = []
    for g, w in zip(gabali, platumi):
        if g[0] == "t":
            # xml:space, jo SVG citādi nogriež atstarpi pirms vārda -
            # un tieši tā atstarpe atdala vārdu no daļas.
            out.append('<text class="%s" x="%.2f" y="%.2f" '
                       'xml:space="preserve">%s</text>'
                       % (klase, xi, y, teksts(g[1])))
        elif g[0] == "s":
            out.append(_saknes_teksts(xi, y, g[1], klase))
        else:
            out.append(_dalas_teksts(xi + w / 2.0, y, g[1], g[2], g[3],
                                     klase))
        xi += w
    return "".join(out)


# Saknes zīmes augstums fonta izmēra daļās: no vinkula līdz zem pamatlīnijas.
_SAKNE_H = MF.ROOT_ASC + MF.ROOT_DESC


def _saknes_teksts(x, y, iekss, klase):
    """√ ar vinkulu pāri visai zemsaknes izteiksmei; x - kreisā mala.

    Zīmes kontūra ir tā pati, ko zīmē tekstā un slaidos (mathfmt.root_pts),
    tikai mērogota uz zīmējuma burtu izmēru. Zīme un vinkuls ir aizpildīti ar
    uzraksta klasi, tāpēc tie ir tādā pašā krāsā kā cipari.
    """
    fs = _FONTI.get(klase.split()[0], _FONTS)
    zw = MF.root_width(_SAKNE_H) * fs
    augsa = y - MF.ROOT_ASC * fs
    tx = x + zw + MF.ROOT_INNER * fs
    tw = _teksta_plat(iekss, fs)
    return ('<path class="%s" transform="translate(%.2f %.2f) scale(%.3f)" '
            'd="%s"/>'
            '<rect class="%s" x="%.2f" y="%.2f" width="%.2f" height="%.2f"/>'
            '<text class="%s" x="%.2f" y="%.2f" xml:space="preserve">%s</text>'
            % (klase, x, augsa, fs, MF.root_path_d(_SAKNE_H),
               klase, x + zw - MF.ROOT_T * fs / 2.0, augsa,
               tw + 0.12 * fs + MF.ROOT_INNER * fs + MF.ROOT_T * fs / 2.0,
               MF.ROOT_BAR * fs,
               klase, tx, y, teksts(iekss)))


# --------------------------------------------------------- skaitļu taisne
def taisne(sakums, beigas, solis, atzimes=(), virsraksts=None, bultas=(),
           sikas=None, intervali=()):
    """Skaitļu taisne ar iedaļām, atzīmētiem punktiem un lēcienu bultām.

    atzimes: [(vērtība, uzraksts), ...] - punkts uz ass ar uzrakstu virs tā.
    bultas: [(no, uz, uzraksts), ...] - lēciens pa taisni, uzzīmēts kā loks
    virs ass; tieši tā skaitļu taisnē izskatās «pieskaitīt» un «atņemt».
    sikas: cik sīkās daļās sadalīts katrs solis - īsas iedaļas bez
    skaitļiem. Tā daļu taisnē redz ceturtdaļas vai astotdaļas, bet zem ass
    paliek tikai veseli skaitļi, nevis 0,25 un 0,125.
    Vienību izvēlas pats zīmējums: no `sakums` līdz `beigas` vienmēr iznāk
    viss platums, tāpēc uz ass der arī lieli skaitļi.
    intervali: [(no, līdz, no_ieskaitot, līdz_ieskaitot), ...] - nevienādības
    atrisinājums, šķērssvītrots virs ass, kā to zīmē latviešu mācību
    grāmatās; None ir bezgalība (svītrojums iet līdz ass galam). Ieskaitīts
    galapunkts ir pilns, neieskaitīts - «izdurts» (tukšs aplītis).
    """
    mala = 6.0
    garums = PLATUMS - 2 * mala
    # Daļa virsrakstā aizņem trīs rindas, tāpēc ass nolaižas par tikpat.
    atkape = _virs_atkape(virsraksts)
    aug = (26.0 if not bultas else 34.0) + atkape
    y = (17.0 if not bultas else 25.0) + atkape

    def x(v):
        if beigas == sakums:
            return mala
        return mala + garums * (float(v) - sakums) / (beigas - sakums)

    dalas = ['<line class="z-ass" x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f"/>'
             % (mala - 3, y, PLATUMS - mala + 3, y)]
    dalas.append('<path class="z-ass" d="M%.2f %.2f l-2.6 -1.6 v3.2 z"/>'
                 % (PLATUMS - mala + 3.4, y))
    v = sakums
    while v <= beigas + 1e-9:
        xi = x(v)
        dalas.append('<line class="z-iedala" x1="%.2f" y1="%.2f" x2="%.2f" '
                     'y2="%.2f"/>' % (xi, y - 2.2, xi, y + 2.2))
        dalas.append(_teksts(xi, y + 7.4, _skaitlis(v)))
        if sikas and v + solis <= beigas + 1e-9:
            for k in range(1, int(sikas)):
                xs = x(v + solis * k / float(sikas))
                dalas.append('<line class="z-iedala" x1="%.2f" y1="%.2f" '
                             'x2="%.2f" y2="%.2f"/>'
                             % (xs, y - 1.3, xs, y + 1.3))
        v += solis
    for vert, uzraksts in atzimes:
        xi = x(vert)
        dalas.append('<circle class="z-punkts" cx="%.2f" cy="%.2f" r="2.2"/>'
                     % (xi, y))
        # Daļai zem svītras ir vēl viena rinda, tāpēc tā jāpaceļ augstāk -
        # citādi saucējs uzsēžas punktam uz ass.
        dalas.append(_teksts(xi, y - (7.0 if _ir_dala(uzraksts) else 6.2),
                             uzraksts, "z-atzime"))
    dalas.extend(_intervali(intervali, x, y, mala))
    dalas.extend(_lekumi(bultas, x, y))
    if virsraksts:
        dalas.append(_teksts(PLATUMS / 2, 5.0 + _virs_linija(virsraksts),
                             virsraksts, "z-virs"))
    return _svg(aug, "".join(dalas))


def _intervali(intervali, x, y, mala):
    """Šķērssvītrojums virs ass un galapunkti uz tās - katram intervālam.

    Otrais intervāls (nevienādību sistēmā) ir svītrots uz otru pusi un
    augstāk, tāpēc abu kopīgā daļa - šķēlums - ir redzama kā krustojums.
    """
    out = []
    for i, (no_, lidz, no_iekl, lidz_iekl) in enumerate(intervali):
        x1 = x(no_) if no_ is not None else mala - 3
        x2 = x(lidz) if lidz is not None else PLATUMS - mala + 3
        augsa = 3.2 + 2.6 * i
        virz = 1.0 if i % 2 == 0 else -1.0
        xs = x1
        while xs < x2 - 0.2:
            gals = min(xs + 1.7, x2)
            out.append('<line class="z-svitr" x1="%.2f" y1="%.2f" x2="%.2f" '
                       'y2="%.2f"/>'
                       % (gals if virz > 0 else xs, y - augsa,
                          xs if virz > 0 else gals, y - 0.4))
            xs += 1.7
        out.append('<line class="z-svitr" x1="%.2f" y1="%.2f" x2="%.2f" '
                   'y2="%.2f"/>' % (x1, y - augsa, x2, y - augsa))
        for v, ieskaitits in ((no_, no_iekl), (lidz, lidz_iekl)):
            if v is None:
                continue
            out.append('<circle class="%s" cx="%.2f" cy="%.2f" r="1.6"/>'
                       % ("z-punkts" if ieskaitits else "z-tukss", x(v), y))
    return out


def _lekumi(bultas, x, y):
    """Lēciena loks virs ass: no viena skaitļa uz otru, ar uzrakstu virsū."""
    out = []
    for no_, uz, uzraksts in bultas:
        x1, x2 = x(no_), x(uz)
        # Loka augstums aug līdz ar lēciena garumu, lai divi lēcieni vienā
        # zīmējumā neuzliktos viens uz otra.
        h = min(12.0, 4.0 + abs(x2 - x1) * 0.28)
        out.append('<path class="z-bulta" d="M%.2f %.2f Q%.2f %.2f %.2f %.2f"/>'
                   % (x1, y - 2.6, (x1 + x2) / 2, y - 2.6 - h * 2, x2,
                      y - 2.6))
        zime = 1.0 if x2 >= x1 else -1.0
        out.append('<path class="z-bultgals" d="M%.2f %.2f l%.2f -1.9 '
                   'l%.2f 3.8 z"'
                   '/>' % (x2, y - 2.4, -2.8 * zime, 0.0))
        out.append(_teksts((x1 + x2) / 2, y - 3.4 - h, uzraksts, "z-atzime"))
    return out


def _skaitlis(v):
    """Skaitlis uz ass: mīnuss ir «−», nevis defise (latviešu standarts)."""
    return _skaitlis_bez_zimes(v).replace("-", "−")


def _skaitlis_bez_zimes(v):
    """Veselu skaitli raksta bez komata; tūkstošus atdala ar atstarpi."""
    if abs(v - round(v)) < 1e-9:
        teksts = "%d" % int(round(v))
        if len(teksts) > 4:
            gabali = []
            while len(teksts) > 3:
                gabali.insert(0, teksts[-3:])
                teksts = teksts[:-3]
            gabali.insert(0, teksts)
            return " ".join(gabali)
        return teksts
    return ("%g" % v).replace(".", ",")


def laika_ass(atzimes, sakums=None, beigas=None, solis=None):
    """Laika ass: tie paši noteikumi, kas skaitļu taisnei, tikai gadi.

    Bez atsevišķa koda - laika ass ir skaitļu taisne, kurai vienība ir gads
    (DRY). Robežas un iedaļu soli var izvēlēties pats.
    """
    gadi = [g for g, _ in atzimes]
    sak = sakums if sakums is not None else min(gadi)
    beig = beigas if beigas is not None else max(gadi)
    sol = solis or max(1, int(round((beig - sak) / 5.0)))
    return taisne(sak, beig, sol, atzimes)


# ------------------------------------------------------- stabiņu attēls
def kolonnas(dati, mervieniba=""):
    """Stabiņi salīdzināšanai: [(uzraksts, vērtība), ...].

    Stabiņu augstums ir attiecība pret lielāko vērtību, tāpēc vienā attēlā
    var salikt gan 8, gan 8 000 000 - skolēns uzreiz redz, cik reižu viens
    ir lielāks par otru. Skaitli raksta virs stabiņa, nosaukumu - zem tā.
    """
    dati = list(dati)
    aug = 56.0
    pamats = 42.0
    lielaka = max(v for _, v in dati) or 1
    platums = (PLATUMS - 8.0) / len(dati)
    stabs = platums * 0.56
    dalas = ['<line class="z-ass" x1="4" y1="%.1f" x2="%.1f" y2="%.1f"/>'
             % (pamats, PLATUMS - 4, pamats)]
    for i, (uzraksts, vertiba) in enumerate(dati):
        x = 4.0 + platums * i + (platums - stabs) / 2.0
        h = 30.0 * float(vertiba) / lielaka
        dalas.append('<rect class="z-stabs" x="%.2f" y="%.2f" width="%.2f" '
                     'height="%.2f" rx="1"/>'
                     % (x, pamats - h, stabs, max(h, 0.6)))
        dalas.append(_teksts(x + stabs / 2, pamats - h - 2.0,
                             _skaitlis(vertiba) + mervieniba, "z-atzime",
                             maks=platums - 1.0))
        dalas.append(_teksts(x + stabs / 2, pamats + 6.0, uzraksts,
                             maks=platums - 1.0))
    return _svg(aug, "".join(dalas))


def sektori(dati, procenti=True):
    """Sektoru diagramma: [(uzraksts, vērtība), ...] - daļas no veseluma.

    Sektora leņķis ir vērtības daļa no summas, tāpēc tos pašus datus var
    dot gan kā skaitu, gan kā procentus. Uzrakstus liek leģendā blakus, nevis
    sektoros: telefonā šaurā sektorā vārds neietilpst. procenti=True leģendā
    raksta daļu procentos (noapaļotu), False - pašu vērtību.
    """
    dati = list(dati)
    kopa = float(sum(v for _, v in dati)) or 1.0
    R, cx = 21.0, 25.0
    rinda = 7.0
    aug = max(2 * R + 6.0, rinda * len(dati) + 6.0)
    cy = aug / 2.0
    dalas = []
    sak = 90.0                       # pirmais sektors sākas augšā
    y = cy - rinda * (len(dati) - 1) / 2.0
    for i, (uzraksts, vertiba) in enumerate(dati):
        gradi = 360.0 * vertiba / kopa
        klase = "z-sekt s%d" % (i % 6)
        if gradi >= 359.99:
            dalas.append('<circle class="%s" cx="%.2f" cy="%.2f" r="%.2f"/>'
                         % (klase, cx, cy, R))
        elif gradi > 0:
            a1, a2 = math.radians(sak), math.radians(sak - gradi)
            dalas.append(
                '<path class="%s" d="M%.2f %.2f L%.2f %.2f A%.2f %.2f 0 %d 1 '
                '%.2f %.2f Z"/>'
                % (klase, cx, cy, cx + R * math.cos(a1), cy - R * math.sin(a1),
                   R, R, 1 if gradi > 180 else 0,
                   cx + R * math.cos(a2), cy - R * math.sin(a2)))
        sak -= gradi
        dalas.append('<rect class="%s" x="52" y="%.2f" width="4" height="4" '
                     'rx=".6"/>' % (klase, y - 2.0))
        vert = (_skaitlis(round(100.0 * vertiba / kopa)) + " %" if procenti
                else _skaitlis(vertiba))
        dalas.append(_teksts(77.5, y + 1.2, "%s - %s" % (uzraksts, vert),
                             maks=42.0))
        y += rinda
    return _svg(aug, "".join(dalas))


# --------------------------------------------------------- bitu slēdži
def biti(virkne, vertibas=True):
    """Binārā skaitļa slēdži: ieslēgts kvadrāts ir 1, izslēgts - 0.

    virkne: teksts no nullēm un vieniniekiem, piemēram "1011". Zem katra
    slēdža raksta tā vietas vērtību (8, 4, 2, 1), tāpēc attēls pats
    izstāsta, kāpēc sanāk tieši tas skaitlis.
    """
    virkne = "".join(c for c in virkne if c in "01")
    n = len(virkne) or 1
    aug = 34.0
    platums = min(14.0, (PLATUMS - 10.0) / n)
    mala = platums * 0.72
    sakums = (PLATUMS - platums * n) / 2.0
    y = 8.0
    dalas = []
    for i, c in enumerate(virkne):
        x = sakums + platums * i + (platums - mala) / 2.0
        dalas.append('<rect class="z-bits%s" x="%.2f" y="%.2f" width="%.2f" '
                     'height="%.2f" rx="1.5"/>'
                     % (" on" if c == "1" else "", x, y, mala, mala))
        dalas.append(_teksts(x + mala / 2, y + mala * 0.68, c,
                             "z-bits-c" + (" on" if c == "1" else "")))
        if vertibas:
            dalas.append(_teksts(x + mala / 2, y + mala + 5.6,
                                 str(2 ** (n - 1 - i))))
    if vertibas:
        kopa = sum(2 ** (n - 1 - i) for i, c in enumerate(virkne) if c == "1")
        dalas.append(_teksts(PLATUMS / 2, aug - 1.2,
                             "kopā %d" % kopa, "z-virs"))
    return _svg(aug, "".join(dalas))



# --------------------------------------------------------- skaitļu režģis
def restis(rindas, virsraksts=None):
    """Skaitļu režģis: maģiskais kvadrāts, skaitļu tabula, sakārtojums.

    rindas: [[8, 1, 6], [3, None, 7], ...] - None ir tukša rūtiņa, kuru
    skolēns aizpilda pats; tā zīmēta ar punktētu malu un jautājuma zīmi,
    tāpēc uzdevumu var izlasīt no attēla, nevis no teksta. Rūtiņā drīkst būt
    arī īss teksts, tāpēc tas pats režģis der joslai, kas sadalīta daļās.

    Rūtiņas malu izvēlas pats zīmējums, tāpēc der gan 3x3, gan 4x4 režģis.
    """
    rindas = [list(r) for r in rindas]
    n = max(len(r) for r in rindas)
    m = len(rindas)
    vieta = PLATUMS - 8.0
    mala = min(18.0, vieta / n)
    # Kolonna ir tik plata, lai tās garākais uzraksts ietilpst; ja visas kopā
    # neietilpst zīmējumā, tās saraujas vienādi, un uzrakstus samazina
    # _teksts(maks=...).
    fs = _FONTI["z-ruts-c"]
    kol = [max([mala] + [_gabalu_plat(_rutas_teksts(r[j]), fs) * 1.1 + 5.0
                         for r in rindas if j < len(r)])
           for j in range(n)]
    if sum(kol) > vieta:
        kol = [k * vieta / sum(kol) for k in kol]
    x0 = (PLATUMS - sum(kol)) / 2.0
    y0 = 7.0 + _virs_atkape(virsraksts) if virsraksts else 2.0
    aug = y0 + mala * m + 2.0
    dalas = []
    if virsraksts:
        dalas.append(_teksts(PLATUMS / 2, 4.6 + _virs_linija(virsraksts),
                             virsraksts, "z-virs"))
    for i, rinda in enumerate(rindas):
        for j in range(n):
            vert = rinda[j] if j < len(rinda) else None
            tuksa = "" if vert is not None else " tuksa"
            x, y = x0 + sum(kol[:j]), y0 + mala * i
            dalas.append('<rect class="z-ruts%s" x="%.2f" y="%.2f" '
                         'width="%.2f" height="%.2f" rx="1.5"/>'
                         % (tuksa, x, y, kol[j], mala))
            dalas.append(_teksts(x + kol[j] / 2, y + mala * 0.63,
                                 _rutas_teksts(vert), "z-ruts-c" + tuksa,
                                 maks=kol[j] - 3.0))
    return _svg(aug, "".join(dalas))


def _rutas_teksts(vert):
    """Rūtiņas uzraksts: tukšai - jautājuma zīme, skaitlim - skaitlis."""
    if vert is None:
        return "?"
    return vert if isinstance(vert, str) else _skaitlis(vert)


# ------------------------------------------------------ Venna diagramma
def venna(kreisais, labais, kopigie, nosaukumi):
    """Divas pārklājošās kopas: kas ir tikai vienā, otrā un abās.

    nosaukumi: (kreisās kopas nosaukums, labās kopas nosaukums).
    Skaitļus raksta pa rindām, lai tie ietilpst aplī arī telefonā.
    """
    aug = 62.0
    # Apļu centri ir tuvāk nekā puse rādiusa, lai kopīgā daļa būtu pietiekami
    # plata diviem cipariem - citādi skaitļi tajā neietilpst.
    r = 22.0
    cx1, cx2, cy = 36.0, 64.0, 34.0
    dalas = [
        '<circle class="z-kopa" cx="%.1f" cy="%.1f" r="%.1f"/>' % (cx1, cy, r),
        '<circle class="z-kopa" cx="%.1f" cy="%.1f" r="%.1f"/>' % (cx2, cy, r),
        _teksts(cx1 - 6, 8.0, nosaukumi[0], "z-virs"),
        _teksts(cx2 + 6, 8.0, nosaukumi[1], "z-virs"),
    ]
    # Kopīgajā daļā vietas ir maz, tāpēc tur raksta pa vienam skaitlim rindā.
    for x, saraksts, katra in ((cx1 - 11, kreisais, 2), (50.0, kopigie, 1),
                               (cx2 + 11, labais, 2)):
        rindas = _rindas(saraksts, katra)
        # Rindu kaudzi centrē pret apļa viduslīniju: pirmā rinda ceļas tik
        # augstu, cik puse no visas kaudzes augstuma.
        atstarpe = 5.2
        y0 = cy - atstarpe * (len(rindas) - 1) / 2.0 + 1.6
        for i, rinda in enumerate(rindas):
            dalas.append(_teksts(x, y0 + i * atstarpe, rinda))
    return _svg(aug, "".join(dalas))


def _rindas(saraksts, katra=2):
    """Skaitļus sadala pa rindām, lai tie ietilptu aplī."""
    gabali = [str(x) for x in saraksts]
    return [", ".join(gabali[i:i + katra])
            for i in range(0, len(gabali), katra)] or [""]


# ------------------------------------------------------- koordinātu plakne
def plakne(lauzta=None, punkti=(), no_x=-5, lidz_x=5, no_y=-5, lidz_y=5,
           solis=1, virsraksts=None, aizpildi=False, x_nos="x", y_nos="y",
           grafiki=(), solis_y=None):
    """Koordinātu plakne: režģis, abas asis un uz tām atzīmēti punkti.

    punkti: [(x, y, uzraksts), ...]; lauzta: [(x, y), ...] - punkti,
    savienoti ar līniju. `aizpildi` noslēdz lauzto līniju un iekrāso figūru,
    tāpēc tā pati funkcija der gan temperatūras grafikam, gan daudzstūrim
    plaknē (DRY).
    grafiki: [(k, b, uzraksts), ...] - taisne y = kx + b, nogriezta pie
    plaknes malām; vai [([(x, y), ...], uzraksts), ...] - līkne pa punktiem.
    Katram grafikam sava krāsa, tāpēc divus tarifus var salīdzināt vienā
    zīmējumā.
    solis_y: iedaļa uz y ass, ja tā atšķiras no x ass iedaļas (kilogrami
    pret eiro, stundas pret kilometriem). Rūtiņa paliek kvadrātiska, tikai
    uz y ass tā nozīmē citu skaitli - tieši tā vienības izvēlas burtnīcā.
    """
    solis_y = solis_y or solis
    mala = 8.0
    n_x = float(lidz_x - no_x)
    ruts = (PLATUMS - 2 * mala) / n_x
    ruts_y = ruts * solis / float(solis_y)
    # Virs plaknes paliek vieta y ass nosaukumam - citādi tas uzkāpj
    # zīmējuma augšmalai un bloka virsrakstam.
    y0 = 6.0 + _virs_atkape(virsraksts) if virsraksts else 5.0
    aug = y0 + ruts_y * (lidz_y - no_y) + 4.0

    def X(v):
        return mala + (float(v) - no_x) * ruts

    def Y(v):
        return y0 + (lidz_y - float(v)) * ruts_y

    dalas = []
    if virsraksts:
        dalas.append(_teksts(PLATUMS / 2, 4.4 + _virs_linija(virsraksts),
                             virsraksts, "z-virs"))
    v = no_x
    while v <= lidz_x + 1e-9:
        dalas.append('<line class="z-resti" x1="%.2f" y1="%.2f" x2="%.2f" '
                     'y2="%.2f"/>' % (X(v), Y(no_y), X(v), Y(lidz_y)))
        v += solis
    v = no_y
    while v <= lidz_y + 1e-9:
        dalas.append('<line class="z-resti" x1="%.2f" y1="%.2f" x2="%.2f" '
                     'y2="%.2f"/>' % (X(no_x), Y(v), X(lidz_x), Y(v)))
        v += solis_y
    # Ass iet caur nulli; ja nulle nav redzamajā daļā (augums 145-190 cm),
    # ass stāv plaknes malā - tā skaitļi pie tās vienmēr ir redzami.
    ass_y = 0 if no_y <= 0 <= lidz_y else no_y
    ass_x = 0 if no_x <= 0 <= lidz_x else no_x
    dalas.append('<line class="z-ass" x1="%.2f" y1="%.2f" x2="%.2f" '
                 'y2="%.2f"/>' % (X(no_x), Y(ass_y), X(lidz_x) + 2.5, Y(ass_y)))
    dalas.append(_teksts(X(lidz_x) + 1.6, Y(ass_y) - 2.2, x_nos, "z-virs"))
    dalas.append('<line class="z-ass" x1="%.2f" y1="%.2f" x2="%.2f" '
                 'y2="%.2f"/>' % (X(ass_x), Y(no_y), X(ass_x), Y(lidz_y) - 2.5))
    dalas.append(_teksts(X(ass_x) + 3.6, Y(lidz_y) - 2.8, y_nos, "z-virs"))
    dalas.extend(_plaknes_skaitli(no_x, lidz_x, no_y, lidz_y, solis, X, Y,
                                  solis_y))
    if lauzta:
        celi = " ".join("%.2f,%.2f" % (X(x), Y(y)) for x, y in lauzta)
        birka = "polygon" if aizpildi else "polyline"
        dalas.append('<%s class="%s" points="%s"/>'
                     % (birka, "z-figura" if aizpildi else "z-lin", celi))
        for x, y in lauzta:
            dalas.append('<circle class="z-punkts" cx="%.2f" cy="%.2f" '
                         'r="1.5"/>' % (X(x), Y(y)))
    for i, g in enumerate(grafiki):
        dalas.extend(_grafiks(g, i, X, Y, (no_x, lidz_x, no_y, lidz_y)))
    for p in punkti:
        x, y = p[0], p[1]
        dalas.append('<circle class="z-punkts" cx="%.2f" cy="%.2f" r="2"/>'
                     % (X(x), Y(y)))
        if len(p) > 2 and p[2]:
            dalas.append(_teksts(X(x), Y(y) - 3.4, p[2], "z-atzime"))
    return _svg(aug, "".join(dalas))


def taisnes_gali(k, b, robezas):
    """Taisnes y = kx + b redzamā daļa plaknē: divi gali vai None."""
    no_x, lidz_x, no_y, lidz_y = robezas
    if abs(k) < 1e-12:
        return [(no_x, b), (lidz_x, b)] if no_y <= b <= lidz_y else None
    xs = sorted([no_x, lidz_x, (no_y - b) / float(k), (lidz_y - b) / float(k)])
    x1, x2 = max(no_x, xs[1]), min(lidz_x, xs[2])
    if x2 - x1 < 1e-9:
        return None
    return [(x1, k * x1 + b), (x2, k * x2 + b)]


def likne(f, no_x, lidz_x, no_y, lidz_y, n=80):
    """Funkcijas y = f(x) redzamā daļa kā punktu saraksts grafikam plaknē.

    9. klasē parabolu zīmē daudzās stundās; lai katrā nav jāraksta savs
    punktu cikls, likni aprēķina te (DRY). Kur grafiks iziet ārpus plaknes
    augšā vai apakšā, punktu nogriež tieši uz malas, tāpēc zari nekad
    neizlīst ārā no režģa:

        plakne(grafiki=[(likne(lambda x: x * x - 4, -4, 4, -5, 6), "")])
    """
    def iekss(y):
        return no_y <= y <= lidz_y

    def mala(x1, y1, x2, y2):
        yb = lidz_y if max(y1, y2) > lidz_y else no_y
        return (x1 + (x2 - x1) * (yb - y1) / (y2 - y1), yb)

    xs = [no_x + (lidz_x - no_x) * i / float(n) for i in range(n + 1)]
    ys = [f(x) for x in xs]
    out = []
    for i, (x, y) in enumerate(zip(xs, ys)):
        if i and iekss(y) != iekss(ys[i - 1]):
            out.append(mala(xs[i - 1], ys[i - 1], x, y))
        if iekss(y):
            out.append((x, y))
    return out


def _skaitlis_teksta(v):
    """1.5 -> «1,5», −2.0 -> «−2» - koeficients funkcijas pierakstā."""
    return ("%g" % v).replace(".", ",").replace("-", "−")


def funkcijas_teksts(a, b, c):
    """«y = x² − 4x + 3» no koeficientiem - bez «1x» un «+ −»."""
    out = []
    for koef, burts in ((a, "x²"), (b, "x"), (c, "")):
        if not koef:
            continue
        zime = "−" if koef < 0 else "+"
        k = abs(koef)
        teksts = (_skaitlis_teksta(k) if (k != 1 or not burts) else "") + burts
        out.append((zime, teksts))
    if not out:
        return "y = 0"
    pirmais = ("−" if out[0][0] == "−" else "") + out[0][1]
    return "y = " + " ".join([pirmais] + ["%s %s" % z for z in out[1:]])


def parabola(a, b, c, no_x=-5, lidz_x=5, no_y=-5, lidz_y=5, punkti=(),
             uzraksts=True, solis_y=None, citi=(), asis=("x", "y"),
             solis=1):
    """Kvadrātfunkcijas y = ax^2 + bx + c grafiks koordinātu plaknē.

    9.5. temata stundās parabola ir gandrīz katrā zīmējumā; te tā ir viena
    rinda (DRY). uzraksts=True - pie grafika raksta tā formulu; citi -
    papildu grafiki plaknē (taisne (k, b, uzraksts) vai līkne); asis - asu
    nosaukumi, piemēram, ("t", "h") kustības uzdevumā.
    """
    teksts = funkcijas_teksts(a, b, c) if uzraksts is True else (uzraksts
                                                                  or "")
    # Augsta un šaura plakne telefonā ir sīka; tad y asij ņem soli 2 un
    # robežas noapaļo līdz pāra skaitļiem, lai iedaļas būtu 0, 2, 4, ...
    if solis_y is None and (lidz_y - no_y) > 1.3 * (lidz_x - no_x) / solis:
        solis_y = 2
        no_y, lidz_y = 2 * math.floor(no_y / 2.0), 2 * math.ceil(lidz_y / 2.0)
    liknes = likne(lambda x: a * x * x + b * x + c, no_x, lidz_x, no_y,
                   lidz_y)
    return plakne(grafiki=[(liknes, teksts)] + list(citi), punkti=punkti,
                  no_x=no_x, lidz_x=lidz_x, no_y=no_y, lidz_y=lidz_y,
                  solis=solis, solis_y=solis_y, x_nos=asis[0],
                  y_nos=asis[1])


def _grafiks(g, i, X, Y, robezas):
    """Viens grafiks plaknē: līnija un uzraksts pie tās labā gala."""
    if isinstance(g[0], (list, tuple)):
        celi, uzraksts = [(float(x), float(y)) for x, y in g[0]], g[1]
    else:
        celi, uzraksts = taisnes_gali(g[0], g[1], robezas), g[2]
    if not celi:
        return []
    klase = "" if i % 2 == 0 else " otra"
    out = ['<polyline class="z-graf%s" points="%s"/>'
           % (klase, " ".join("%.2f,%.2f" % (X(x), Y(y)) for x, y in celi))]
    if uzraksts and len(celi) > 1:
        # Katram grafikam uzraksts citā vietā gar līniju (pirmajam tuvu labajam
        # galam, otrajam - pie vidus), tāpēc divi uzraksti neuzkrīt viens
        # otram; ar baltu apmali tas paliek lasāms arī pāri režģim.
        (x1, y1), (x2, y2) = celi[0], celi[-1]
        t = 0.82 if i % 2 == 0 else 0.42
        px = X(x1 + (x2 - x1) * t)
        py = Y(y1 + (y2 - y1) * t)
        px = min(max(px, X(robezas[0]) + 9.0), X(robezas[1]) - 9.0)
        out.append(_teksts(px - 5.0, py - 2.2, uzraksts,
                           "z-atzime z-uz" + klase))
    return out


def _plaknes_skaitli(no_x, lidz_x, no_y, lidz_y, solis, X, Y, solis_y=None):
    """Iedaļu skaitļi pie abām asīm - blakus asij, nevis pāri režģim."""
    out = []
    ir_x = no_y <= 0 <= lidz_y
    ir_y = no_x <= 0 <= lidz_x
    ass_y = 0 if ir_x else no_y          # kur stāv asis (sk. plakne)
    ass_x = 0 if ir_y else no_x
    v = no_x
    while v <= lidz_x + 1e-9:
        # Nulli pie krustpunkta raksta vienu reizi - zemāk.
        if abs(v) > 1e-9 or not ir_y:
            out.append(_teksts(X(v), Y(ass_y) + 4.8, _skaitlis(v)))
        v += solis
    v = no_y
    while v <= lidz_y + 1e-9:
        if abs(v) > 1e-9 or not ir_x:
            out.append('<text class="z-nr" x="%.2f" y="%.2f" '
                       'text-anchor="end">%s</text>'
                       % (X(ass_x) - 1.4, Y(v) + 1.3,
                          teksts(_skaitlis(v))))
        v += solis_y or solis
    if ir_x and ir_y:
        out.append('<text class="z-nr" x="%.2f" y="%.2f" '
                   'text-anchor="end">0</text>' % (X(0) - 1.4, Y(0) + 4.8))
    return out


# ---------------------------------------------------------- laukuma modelis
def kvadrats(kol, rind, a=0, b=0, virsraksts=None, paraksts=None):
    """Vienības kvadrāts, sadalīts rūtiņās; iekrāsotas a kolonnas un b rindas.

    Ar to redz, kāpēc {2|3} · {3|4} ir mazāks par abiem reizinātājiem, un tas
    pats režģis 10 x 10 parāda 0,4 · 0,7 (DRY).
    """
    y0 = 6.0 + _virs_atkape(virsraksts) if virsraksts else 1.5
    mala = 58.0
    x0 = (PLATUMS - mala) / 2.0
    sk, sr = mala / float(kol), mala / float(rind)
    dalas = []
    if virsraksts:
        dalas.append(_teksts(PLATUMS / 2, 4.4 + _virs_linija(virsraksts),
                             virsraksts, "z-virs"))
    if a and b:
        dalas.append('<rect class="z-lauks" x="%.2f" y="%.2f" width="%.2f" '
                     'height="%.2f"/>' % (x0, y0, sk * a, sr * b))
    for i in range(kol + 1):
        dalas.append('<line class="z-resti" x1="%.2f" y1="%.2f" x2="%.2f" '
                     'y2="%.2f"/>' % (x0 + sk * i, y0, x0 + sk * i, y0 + mala))
    for j in range(rind + 1):
        dalas.append('<line class="z-resti" x1="%.2f" y1="%.2f" x2="%.2f" '
                     'y2="%.2f"/>' % (x0, y0 + sr * j, x0 + mala, y0 + sr * j))
    dalas.append('<rect class="z-rame" x="%.2f" y="%.2f" width="%.2f" '
                 'height="%.2f"/>' % (x0, y0, mala, mala))
    aug = y0 + mala + 2.0
    if paraksts:
        dalas.append(_teksts(PLATUMS / 2, y0 + mala + 5.6, paraksts, "z-virs"))
        aug = y0 + mala + 6.1 + _zem_pamatlinijas(paraksts, "z-virs")
    return _svg(aug, "".join(dalas))


# -------------------------------------------------------------- daļas josla
def dala(n, k, uzraksts=None, virsraksts=None):
    """Josla no n vienādām daļām, no kurām k ir iekrāsotas.

    Tā pati josla rāda gan daļu ({3|8}), gan procentus (n = 10, k = 3), gan
    atlaidi - mainās tikai uzraksts.
    """
    y0 = 6.0 + _virs_atkape(virsraksts) if virsraksts else 2.0
    h = 13.0
    mala = 6.0
    platums = (PLATUMS - 2 * mala) / float(n)
    dalas = []
    if virsraksts:
        dalas.append(_teksts(PLATUMS / 2, 4.4 + _virs_linija(virsraksts),
                             virsraksts, "z-virs"))
    for i in range(n):
        x = mala + platums * i
        dalas.append('<rect class="z-%s" x="%.2f" y="%.2f" width="%.2f" '
                     'height="%.2f"/>'
                     % ("lauks" if i < k else "ruts", x, y0, platums, h))
    dalas.append('<rect class="z-rame" x="%.2f" y="%.2f" width="%.2f" '
                 'height="%.2f"/>' % (mala, y0, PLATUMS - 2 * mala, h))
    aug = y0 + h + 2.0
    if uzraksts:
        dalas.append(_teksts(PLATUMS / 2, y0 + h + 5.6, uzraksts, "z-virs"))
        aug = y0 + h + 6.1 + _zem_pamatlinijas(uzraksts, "z-virs")
    return _svg(aug, "".join(dalas))


# --------------------------------------------------------- telpiski ķermeņi
def kermenis(veids, uzraksti=(), virsraksts=None):
    """Telpiska ķermeņa skice: redzamās šķautnes veselas, slēptās - punktētas.

    veids: kubs, kvadrs, prizma, cilindrs, konuss, piramida, lode.
    uzraksti: [(x, y, teksts), ...] zīmējuma koordinātās - izmēru atzīmes.
    """
    if veids not in _KERMENI:
        raise KeyError("nav ķermeņa «%s»; ir: %s"
                       % (veids, ", ".join(sorted(_KERMENI))))
    y0 = 6.0 + _virs_atkape(virsraksts) if virsraksts else 0.0
    dalas = []
    if virsraksts:
        dalas.append(_teksts(PLATUMS / 2, 4.4 + _virs_linija(virsraksts),
                             virsraksts, "z-virs"))
    dalas.append('<g transform="translate(0 %.1f)">%s</g>'
                 % (y0, _KERMENI[veids]()))
    for x, y, t in uzraksti:
        dalas.append(_teksts(x, y + y0, t, "z-atzime"))
    return _svg(y0 + 56.0, "".join(dalas))


def _skautne(d, slepta=False):
    return '<path class="z-kerm%s" d="%s"/>' % (" slepts" if slepta else "", d)


def _kvadrs_sk(w, h, dz):
    """Kvadrs ar priekšējo skaldni w x h un dziļumu dz; kubs ir tas pats.

    Redzamās ir trīs skaldnes - priekšējā, augšējā un labā -, bet trīs
    šķautnes, kas satiekas aizmugurējā apakšējā stūrī, paliek punktētas.
    """
    x0, y0 = (PLATUMS - w - dz) / 2.0, 10.0
    # Priekšējās skaldnes stūri un tie paši stūri, nobīdīti par dziļumu.
    ax, ay = x0, y0 + dz
    bx = x0 + w
    return "".join([
        _skautne("M%.1f %.1f h%.1f v%.1f h-%.1f z" % (ax, ay, w, h, w)),
        _skautne("M%.1f %.1f l%.1f -%.1f h%.1f l-%.1f %.1f"
                 % (ax, ay, dz, dz, w, dz, dz)),
        _skautne("M%.1f %.1f l%.1f -%.1f v%.1f l-%.1f %.1f"
                 % (bx, ay, dz, dz, h, dz, dz)),
        _skautne("M%.1f %.1f v%.1f h%.1f"
                 % (ax + dz, y0, h, w), True),
        _skautne("M%.1f %.1f l-%.1f %.1f"
                 % (ax + dz, y0 + h, dz, dz), True),
    ])


def _kubs():
    return _kvadrs_sk(32.0, 32.0, 12.0)


def _kvadrs():
    return _kvadrs_sk(44.0, 24.0, 12.0)


def _prizma():
    """Trijstūra prizma: priekšā trijstūris, dziļums uz augšu pa labi.

    Aizmugurējā kreisā apakšējā virsotne projicējas priekšējā trijstūra
    iekšpusē, tāpēc visas trīs tās šķautnes ir punktētas; labā sānu skaldne
    ir redzama, tātad aizmugurējā labā šķautne - vesela.
    """
    x0, y0, w, h, dz = 28.0, 12.0, 34.0, 30.0, 11.0
    dx, dy = x0 + dz, y0 + h - dz          # aizmugurējā kreisā apakšējā
    return "".join([
        _skautne("M%.1f %.1f l%.1f -%.1f l%.1f %.1f z"
                 % (x0, y0 + h, w / 2, h, w / 2, h)),
        _skautne("M%.1f %.1f l%.1f -%.1f" % (x0 + w, y0 + h, dz, dz)),
        _skautne("M%.1f %.1f l%.1f -%.1f l%.1f %.1f"
                 % (x0 + w / 2, y0, dz, dz, w / 2, h)),
        _skautne("M%.1f %.1f l%.1f %.1f" % (x0, y0 + h, dz, -dz), True),
        _skautne("M%.1f %.1f l%.1f -%.1f" % (dx, dy, w / 2, h), True),
        _skautne("M%.1f %.1f h%.1f" % (dx, dy, w), True),
    ])


def _cilindrs():
    cx, top, h, rx, ry = PLATUMS / 2, 12.0, 30.0, 18.0, 5.5
    return "".join([
        '<ellipse class="z-kerm" cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f"/>'
        % (cx, top, rx, ry),
        _skautne("M%.1f %.1f v%.1f" % (cx - rx, top, h)),
        _skautne("M%.1f %.1f v%.1f" % (cx + rx, top, h)),
        _skautne("M%.1f %.1f a%.1f %.1f 0 0 0 %.1f 0"
                 % (cx - rx, top + h, rx, ry, 2 * rx)),
        _skautne("M%.1f %.1f a%.1f %.1f 0 0 1 %.1f 0"
                 % (cx - rx, top + h, rx, ry, 2 * rx), True),
    ])


def _konuss():
    cx, top, h, rx, ry = PLATUMS / 2, 10.0, 34.0, 17.0, 5.0
    return "".join([
        _skautne("M%.1f %.1f L%.1f %.1f" % (cx, top, cx - rx, top + h)),
        _skautne("M%.1f %.1f L%.1f %.1f" % (cx, top, cx + rx, top + h)),
        _skautne("M%.1f %.1f a%.1f %.1f 0 0 0 %.1f 0"
                 % (cx - rx, top + h, rx, ry, 2 * rx)),
        _skautne("M%.1f %.1f a%.1f %.1f 0 0 1 %.1f 0"
                 % (cx - rx, top + h, rx, ry, 2 * rx), True),
    ])


def _piramida():
    cx, top, h, w, dz = PLATUMS / 2, 10.0, 34.0, 32.0, 11.0
    x0 = cx - w / 2 - dz / 2
    return "".join([
        _skautne("M%.1f %.1f h%.1f l%.1f -%.1f h-%.1f z"
                 % (x0, top + h, w, dz, dz, w)),
        _skautne("M%.1f %.1f L%.1f %.1f" % (cx, top, x0, top + h)),
        _skautne("M%.1f %.1f L%.1f %.1f" % (cx, top, x0 + w, top + h)),
        _skautne("M%.1f %.1f L%.1f %.1f"
                 % (cx, top, x0 + w + dz, top + h - dz)),
        _skautne("M%.1f %.1f L%.1f %.1f"
                 % (cx, top, x0 + dz, top + h - dz), True),
    ])


def _lode():
    cx, cy, r = PLATUMS / 2, 28.0, 19.0
    return ('<circle class="z-kerm" cx="%.1f" cy="%.1f" r="%.1f"/>'
            '<ellipse class="z-kerm slepts" cx="%.1f" cy="%.1f" rx="%.1f" '
            'ry="%.1f"/>' % (cx, cy, r, cx, cy, r, r * 0.3))


_KERMENI = {"kubs": _kubs, "kvadrs": _kvadrs, "prizma": _prizma,
            "cilindrs": _cilindrs, "konuss": _konuss,
            "piramida": _piramida, "lode": _lode}


# ----------------------------------------------------------------- izklājums
def izklajums(a, b, c, uzraksti=True):
    """Kvadra izklājums krusta formā: kuras skaldnes sanāk vienādas.

    a - platums, b - augstums, c - dziļums; skaitļi ir proporcijas, tāpēc
    tas pats zīmējums der jebkurai kastei.
    """
    liel = float(max(a, b, c))
    v = min(17.0, (PLATUMS - 12.0) * liel / (2.0 * (a + c)))
    A, B, C = a / liel * v, b / liel * v, c / liel * v
    x0 = (PLATUMS - 2 * (A + C)) / 2.0
    y0 = 2.0
    lauki = [(x0 + C, y0, A, C, "augša"),
             (x0, y0 + C, C, B, "sāns"),
             (x0 + C, y0 + C, A, B, "priekša"),
             (x0 + C + A, y0 + C, C, B, "sāns"),
             (x0 + 2 * C + A, y0 + C, A, B, "aizmugure"),
             (x0 + C, y0 + C + B, A, C, "apakša")]
    dalas = []
    for x, y, w, h, nos in lauki:
        dalas.append('<rect class="z-ruts" x="%.2f" y="%.2f" width="%.2f" '
                     'height="%.2f"/>' % (x, y, w, h))
        if uzraksti:
            dalas.append(_teksts(x + w / 2, y + h / 2 + 1.3, nos, "z-mazs",
                                 maks=w - 1.0))
    return _svg(y0 + 2 * C + B + 2.0, "".join(dalas))


# --------------------------------------------------------------- gradi
def lenkis(stari, loki=(), virsraksts=None, r=34.0):
    """Leņķis: stari ar kopīgu virsotni un loki, kas apzīmē leņķus.

    stari: [(grādi, uzraksts), ...] - grādus skaita pretēji pulksteņa
    rādītājam no labās horizontāles, tāpēc izstiepts gradi ir 0 un 180.
    loki: [(no, līdz, uzraksts), ...] - loks starp diviem stariem; tieši tur
    raksta leņķa lielumu. Tas pats zīmējums der gan vienam leņķim, gan
    izstieptam leņķim, ko sadala trešais stars (DRY).
    """
    stari = [(float(g), u) for g, u in stari]
    loki = [(float(a), float(b), u) for a, b, u in loki]
    visi = [g for g, _ in stari] + [a for a, _, _ in loki]         + [b for _, b, _ in loki]
    # Ja neviens stars neiet uz leju, zīmējumam pietiek ar augšējo pusi.
    apaksa = any(math.sin(math.radians(g)) < -1e-9 for g in visi)
    y0 = 6.0 + _virs_atkape(virsraksts) if virsraksts else 2.0
    yv = y0 + r + 7.0
    aug = yv + (r + 8.0 if apaksa else 6.0)

    def p(grads, rad):
        a = math.radians(grads)
        return (PLATUMS / 2 + rad * math.cos(a), yv - rad * math.sin(a))

    dalas = []
    if virsraksts:
        dalas.append(_teksts(PLATUMS / 2, 4.4 + _virs_linija(virsraksts),
                             virsraksts, "z-virs"))
    for grads, uzraksts in stari:
        x, y = p(grads, r)
        dalas.append('<line class="z-ass" x1="%.2f" y1="%.2f" x2="%.2f" '
                     'y2="%.2f"/>' % (PLATUMS / 2, yv, x, y))
        if uzraksts:
            tx, ty = p(grads, r + 5.0)
            dalas.append(_teksts(tx, ty + 1.2, uzraksts, "z-atzime"))
    for i, (a, b, uzraksts) in enumerate(loki):
        rl = 10.0 + 5.0 * i
        x1, y1 = p(a, rl)
        x2, y2 = p(b, rl)
        liels = 1 if abs(b - a) > 180 else 0
        dalas.append('<path class="z-lin" d="M%.2f %.2f A%.2f %.2f 0 %d 0 '
                     '%.2f %.2f"/>' % (x1, y1, rl, rl, liels, x2, y2))
        if uzraksts:
            tx, ty = p((a + b) / 2.0, rl + 5.0)
            dalas.append(_teksts(tx, ty + 1.2, uzraksts, "z-atzime"))
    dalas.append('<circle class="z-punkts" cx="%.2f" cy="%.2f" r="1.2"/>'
                 % (PLATUMS / 2, yv))
    return _svg(aug, "".join(dalas))


# ---------------------------------------------------------- riņķa līnija
def rinkis(radiuss=None, diametrs=None, sektors=None, virsraksts=None,
           paraksts=None):
    """Riņķa līnija ar centru; pēc izvēles rādiuss, diametrs un sektors.

    radiuss un diametrs ir uzraksti (piemēram, «r = 3 cm»), nevis skaitļi -
    zīmējuma lielums ir vienmēr viens un tas pats, jo tas rāda sakarību,
    nevis mērogu. sektors ir grādu skaits, ko iekrāso no labās horizontāles.
    """
    R = 28.0
    y0 = 6.0 + _virs_atkape(virsraksts) if virsraksts else 2.0
    yc = y0 + R + 2.0
    aug = (yc + R + 6.9 + _zem_pamatlinijas(paraksts, "z-virs")
           if paraksts else yc + R + 4.0)
    cx = PLATUMS / 2

    def p(grads, rad=R):
        a = math.radians(grads)
        return (cx + rad * math.cos(a), yc - rad * math.sin(a))

    dalas = []
    if virsraksts:
        dalas.append(_teksts(cx, 4.4 + _virs_linija(virsraksts),
                             virsraksts, "z-virs"))
    if sektors:
        x1, y1 = p(0)
        x2, y2 = p(sektors)
        liels = 1 if float(sektors) > 180 else 0
        dalas.append('<path class="z-kopa" d="M%.2f %.2f L%.2f %.2f '
                     'A%.2f %.2f 0 %d 0 %.2f %.2f Z"/>'
                     % (cx, yc, x1, y1, R, R, liels, x2, y2))
    dalas.append('<circle class="z-lin" cx="%.2f" cy="%.2f" r="%.2f"/>'
                 % (cx, yc, R))
    dalas.append('<circle class="z-punkts" cx="%.2f" cy="%.2f" r="1.2"/>'
                 % (cx, yc))
    if diametrs:
        x1, y1 = p(180)
        x2, y2 = p(0)
        dalas.append('<line class="z-ass" x1="%.2f" y1="%.2f" x2="%.2f" '
                     'y2="%.2f"/>' % (x1, y1, x2, y2))
        dalas.append(_teksts(cx + 13.0, yc + 5.2, diametrs, "z-atzime"))
    if radiuss:
        x2, y2 = p(55)
        dalas.append('<line class="z-ass" x1="%.2f" y1="%.2f" x2="%.2f" '
                     'y2="%.2f"/>' % (cx, yc, x2, y2))
        # Uzrakstu noliek blakus rādiusam, nevis uz tā: nobīde ir 90 grādu
        # leņķī pret pašu nogriezni, tāpēc tas nekad nekrīt virsū līnijai.
        tx, ty = p(55, R * 0.5)
        a = math.radians(55 - 90)
        dalas.append(_teksts(tx + 6.5 * math.cos(a), ty - 6.5 * math.sin(a),
                             radiuss, "z-atzime"))
    if paraksts:
        dalas.append(_teksts(cx, yc + R + 6.4, paraksts, "z-virs"))
    return _svg(aug, "".join(dalas))


def gredzens(ara="R", ieksa="r", virsraksts=None):
    """Riņķa gredzens: iekrāsota tikai josla starp divām riņķa līnijām.

    Abi rādiusi iet no centra dažādos virzienos, tāpēc to uzraksti nekad
    nesaduras - laukums ir lielā riņķa laukums bez mazā.
    """
    R, r = 28.0, 15.0
    y0 = 6.0 + _virs_atkape(virsraksts) if virsraksts else 2.0
    cx, yc = PLATUMS / 2, y0 + R + 2.0
    dalas = []
    if virsraksts:
        dalas.append(_teksts(cx, 4.4 + _virs_linija(virsraksts),
                             virsraksts, "z-virs"))
    dalas.append('<path class="z-figura" fill-rule="evenodd" d="'
                 'M%.2f %.2f a%.2f %.2f 0 1 0 %.2f 0 a%.2f %.2f 0 1 0 -%.2f 0 '
                 'M%.2f %.2f a%.2f %.2f 0 1 0 %.2f 0 a%.2f %.2f 0 1 0 -%.2f 0"/>'
                 % (cx - R, yc, R, R, 2 * R, R, R, 2 * R,
                    cx - r, yc, r, r, 2 * r, r, r, 2 * r))
    dalas.append('<circle class="z-punkts" cx="%.2f" cy="%.2f" r="1.2"/>'
                 % (cx, yc))
    # Lielā rādiusa uzraksts stāv joslā starp abām līnijām, mazā - mazajā
    # riņķī, tāpēc neviens neuzkrīt otrai riņķa līnijai.
    for rad, grads, uzr, kur in ((R, 40, ara, (R + r) / 2.0),
                                 (r, 200, ieksa, r * 0.55)):
        a = math.radians(grads)
        x2, y2 = cx + rad * math.cos(a), yc - rad * math.sin(a)
        dalas.append('<line class="z-ass" x1="%.2f" y1="%.2f" x2="%.2f" '
                     'y2="%.2f"/>' % (cx, yc, x2, y2))
        if uzr:
            b = math.radians(grads + 90)
            tx = cx + kur * math.cos(a) + 4.5 * math.cos(b)
            ty = yc - kur * math.sin(a) - 4.5 * math.sin(b) + 1.2
            dalas.append(_teksts(tx, ty, uzr, "z-atzime z-uz"))
    return _svg(yc + R + 3.0, "".join(dalas))


def rinka_sektori(n, virsraksts=None):
    """Riņķis, sagriezts n sektoros, un tie paši sektori salikti joslā.

    Puse sektoru stāv ar loku uz leju, puse - ar loku uz augšu, tāpēc josla
    ir gandrīz taisnstūris: garums - puse riņķa līnijas (πr), augstums - r.
    Jo vairāk sektoru, jo taisnākas malas; tā redz, no kurienes rodas πr^2.
    """
    n = int(n) // 2 * 2
    R = 15.0
    y0 = 6.0 + _virs_atkape(virsraksts) if virsraksts else 2.0
    teta = 2 * math.pi / n
    dalas = []
    if virsraksts:
        dalas.append(_teksts(PLATUMS / 2, 4.4 + _virs_linija(virsraksts),
                             virsraksts, "z-virs"))
    # Riņķis kreisajā pusē: augšējā puse vienā krāsā, apakšējā - otrā.
    cx, cy = 20.0, y0 + R + 2.0
    for k in range(n):
        a1, a2 = k * teta, (k + 1) * teta
        x1, y1 = cx + R * math.cos(a1), cy - R * math.sin(a1)
        x2, y2 = cx + R * math.cos(a2), cy - R * math.sin(a2)
        dalas.append('<path class="z-figura%s" d="M%.2f %.2f L%.2f %.2f '
                     'A%.2f %.2f 0 0 0 %.2f %.2f Z"/>'
                     % ("" if k < n // 2 else " otra", cx, cy, x1, y1,
                        R, R, x2, y2))
    # Josla: hordas garums w, sektora augstums h.
    w = 2 * R * math.sin(teta / 2)
    h = R * math.cos(teta / 2)
    x0 = 44.0
    augsa = cy - h / 2
    for i in range(n // 2):
        ax = x0 + (i + 0.5) * w
        dalas.append('<path class="z-figura otra" d="M%.2f %.2f L%.2f %.2f '
                     'A%.2f %.2f 0 0 0 %.2f %.2f Z"/>'
                     % (ax, augsa, ax - w / 2, augsa + h, R, R,
                        ax + w / 2, augsa + h))
        bx = x0 + (i + 1) * w
        dalas.append('<path class="z-figura" d="M%.2f %.2f L%.2f %.2f '
                     'A%.2f %.2f 0 0 1 %.2f %.2f Z"/>'
                     % (bx, augsa + h, bx - w / 2, augsa, R, R,
                        bx + w / 2, augsa))
    garums = (n // 2 + 0.5) * w
    dalas.append(_teksts(x0 + garums / 2, augsa + h + 6.5, "≈ πr",
                         "z-atzime"))
    dalas.append(_teksts(x0 - 3.2, cy + 1.2, "r", "z-atzime"))
    return _svg(max(cy + R + 2.0, augsa + h + 8.0), "".join(dalas))


def cilindra_izklajums(r="r", h="h", garums="2πr"):
    """Cilindra virsmas izklājums: taisnstūris un divi riņķi pie tā malām.

    Taisnstūra garums ir tieši pamata riņķa līnijas garums (2πr), tāpēc tas
    zīmēts proporcionāli - redz, ka sānu virsma «aptin» pamatu tieši vienreiz.
    """
    rz = 7.5
    plat, aug = 2 * math.pi * rz, 24.0
    x0, y0 = (PLATUMS - plat) / 2.0, 2.0
    cx = x0 + rz + 4.0
    augsa = y0 + 2 * rz
    dalas = [
        '<circle class="z-figura otra" cx="%.2f" cy="%.2f" r="%.2f"/>'
        % (cx, y0 + rz, rz),
        '<rect class="z-figura" x="%.2f" y="%.2f" width="%.2f" '
        'height="%.2f"/>' % (x0, augsa, plat, aug),
        '<circle class="z-figura otra" cx="%.2f" cy="%.2f" r="%.2f"/>'
        % (cx, augsa + aug + rz, rz),
        '<line class="z-ass" x1="%.2f" y1="%.2f" x2="%.2f" y2="%.2f"/>'
        % (cx, y0 + rz, cx + rz, y0 + rz),
    ]
    dalas.append(_teksts(cx + rz / 2, y0 + rz - 1.4, r, "z-mazs"))
    dalas.append(_teksts(x0 + plat * 0.62, augsa + aug / 2 + 1.3, garums,
                         "z-atzime"))
    dalas.append(_teksts(x0 + plat + 4.0, augsa + aug / 2 + 1.3, h,
                         "z-atzime"))
    return _svg(augsa + aug + 2 * rz + 2.0, "".join(dalas))


# ------------------------------------------------------- figūra rūtiņās
def _rutinu_lapa(kol, rin, virsraksts=None):
    """Rūtiņu lapas fons: [(daļas)], X(x), Y(y) un zīmējuma augstums.

    Koordinātes ir rūtiņās, sākums kreisajā apakšā. To pašu lapu lieto
    figura (slēgts daudzstūris) un linijas (atsevišķi nogriežņi un stari),
    tāpēc rūtiņu izmērs un atkāpes abiem ir vienādas (DRY).
    """
    mala = min(9.0, (PLATUMS - 10.0) / max(kol, 1))
    x0 = (PLATUMS - mala * kol) / 2.0
    y0 = 6.0 + _virs_atkape(virsraksts) if virsraksts else 2.0
    aug = y0 + mala * rin + 4.0

    def X(x):
        return x0 + mala * x

    def Y(y):
        return y0 + mala * (rin - y)

    dalas = []
    if virsraksts:
        dalas.append(_teksts(PLATUMS / 2, 4.4 + _virs_linija(virsraksts),
                             virsraksts, "z-virs"))
    for i in range(kol + 1):
        dalas.append('<line class="z-iedala" x1="%.2f" y1="%.2f" x2="%.2f" '
                     'y2="%.2f"/>' % (X(i), Y(0), X(i), Y(rin)))
    for j in range(rin + 1):
        dalas.append('<line class="z-iedala" x1="%.2f" y1="%.2f" x2="%.2f" '
                     'y2="%.2f"/>' % (X(0), Y(j), X(kol), Y(j)))
    return dalas, X, Y, aug


def figura(virsotnes, uzraksti=(), virsraksts=None, platums=None,
           augstums=None, aizpildi=True):
    """Daudzstūris rūtiņu lapā: virsotnes dotas rūtiņās, sākums kreisajā apakšā.

    virsotnes: [(x, y), ...] - lauztās līnijas punkti rūtiņu koordinātēs;
    līnija tiek noslēgta. uzraksti: [(x, y, teksts), ...] tajās pašās
    koordinātēs - malu garumi vai virsotņu burti. Rūtiņu lapa te ir fons,
    nevis koordinātu plakne: asu un skaitļu nav, tāpēc tas pats zīmējums der
    arī pirms koordinātu plaknes apgūšanas.
    """
    virsotnes = [(float(x), float(y)) for x, y in virsotnes]
    kol = int(platums or max(x for x, _ in virsotnes) + 1)
    rin = int(augstums or max(y for _, y in virsotnes) + 1)
    dalas, X, Y, aug = _rutinu_lapa(kol, rin, virsraksts)
    celi = " ".join("%s%.2f %.2f" % ("M" if i == 0 else "L", X(x), Y(y))
                    for i, (x, y) in enumerate(virsotnes))
    if aizpildi:
        dalas.append('<path class="z-kopa" d="%s Z"/>' % celi)
    else:
        dalas.append('<path class="z-lin" d="%s Z"/>' % celi)
    for x, y in virsotnes:
        dalas.append('<circle class="z-punkts" cx="%.2f" cy="%.2f" r="0.9"/>'
                     % (X(x), Y(y)))
    for x, y, t in uzraksti:
        dalas.append(_teksts(X(x), Y(y), t, "z-atzime"))
    return _svg(aug, "".join(dalas))


def linijas(nogriezni, uzraksti=(), punkti=(), virsraksts=None, platums=12,
            augstums=6):
    """Atsevišķas līnijas rūtiņu lapā: paralēlas, perpendikulāras, stari.

    nogriezni: [(x1, y1, x2, y2), ...] rūtiņu koordinātēs; ja nogrieznim ir
    piektais elements "stars", tā otrajā galā ir bultiņa - tā izskatās stars
    vai taisne, kas turpinās. punkti: [(x, y), ...] - iezīmēti punkti
    (virsotnes, krustpunkti). figura zīmē vienu slēgtu līniju, tāpēc divas
    sliedes vai leņķa malas ar to nevar uzzīmēt - te katra līnija ir sava.
    """
    dalas, X, Y, aug = _rutinu_lapa(int(platums), int(augstums), virsraksts)
    for n in nogriezni:
        x1, y1, x2, y2 = [float(v) for v in n[:4]]
        dalas.append('<line class="z-lin" x1="%.2f" y1="%.2f" x2="%.2f" '
                     'y2="%.2f"/>' % (X(x1), Y(y1), X(x2), Y(y2)))
        if len(n) > 4 and n[4] == "stars":
            a = math.atan2(Y(y2) - Y(y1), X(x2) - X(x1))
            gals = [(X(x2) - 2.6 * math.cos(a + d),
                     Y(y2) - 2.6 * math.sin(a + d)) for d in (0.45, -0.45)]
            dalas.append('<path class="z-bultgals" d="M%.2f %.2f L%.2f %.2f '
                         'L%.2f %.2f Z"/>' % (X(x2), Y(y2), gals[0][0],
                                              gals[0][1], gals[1][0],
                                              gals[1][1]))
    for x, y in punkti:
        dalas.append('<circle class="z-punkts" cx="%.2f" cy="%.2f" r="0.9"/>'
                     % (X(x), Y(y)))
    for x, y, t in uzraksti:
        dalas.append(_teksts(X(x), Y(y), t, "z-atzime"))
    return _svg(aug, "".join(dalas))


# ----------------------------------------------------------------- bloks
class Zimejums(Bloks):
    """Zīmējums ar virsrakstu un paskaidrojumu zem tā."""

    CSS = """
.bl.zimejums .ramis{margin:.6rem 0 .2rem}
.bl.zimejums .paskaidro{margin:.3rem 0 0;color:var(--dim);
    font-size:clamp(.88rem,3.6vw,.98rem)}
"""

    def __init__(self, virsraksts, svg, paskaidro=None, ievads=None):
        Bloks.__init__(self, virsraksts)
        self.svg, self.paskaidro, self.ievads = svg, paskaidro, ievads

    def klase(self):
        return "zimejums"

    def kermenis(self):
        gabali = []
        if self.ievads:
            gabali.append("<p>%s</p>" % esc(self.ievads))
        gabali.append('<div class="ramis">%s</div>' % self.svg)
        if self.paskaidro:
            gabali.append('<p class="paskaidro">%s</p>' % esc(self.paskaidro))
        return "\n".join(gabali)
