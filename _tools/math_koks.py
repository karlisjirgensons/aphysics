# -*- coding: utf-8 -*-
"""Iespēju koks: pilnās pārlases zīmējums.

Kombinatorikā visbiežākā kļūda ir izlaists gadījums. Koks to padara
redzamu: katrs zars ir viena izvēle, katra lapa (zara gals) ir viens
iznākums, un iznākumu skaits ir lapu skaits - tieši tas, ko prasa
reizināšanas likums. Stundas saturs pasaka tikai izvēles katrā solī:

    koks([["A", "B"], ["1", "2", "3"]])        # 2 · 3 = 6 lapas

Koks aug no kreisās uz labo, lapas stāv cita zem citas; tā telefonā arī
divpadsmit iznākumi ietilpst platumā (SRP - šis modulis tikai zīmē).
"""

from math_zimejumi import PLATUMS, _FONTI, _gabalu_plat, _svg, _teksts

RINDA = 5.8             # attālums starp divām lapām
MAKS_LAPAS = 16         # vairāk lapu vairs nav pārskatāms - tad jāspriež
ZARS = 7.0              # zara līnijas mazākais garums starp kolonnām
ATSTARPE = 0.8          # starp zara galu un uzrakstu
KLASE = "z-virs"           # izvēles; iznākumi - z-atzime, tikpat plati


def koks(limeni, iznakumi=True, atdalitajs="", sakne="sākums"):
    """Pilns iespēju koks.

    limeni: [[izvēles 1. solī], [izvēles 2. solī], ...] - katrā zarā vienas
    un tās pašas. iznakumi=True labajā pusē uzraksta katru iznākumu
    (izvēles pēc kārtas, savienotas ar atdalitajs).

    Katras kolonnas platums ir tās garākā uzraksta platums, un zars iet no
    viena uzraksta labās malas līdz nākamā kreisajai - tā garāki vārdi
    («balts», «džinsi») neuzkrīt līnijām. Ja viss neietilpst platumā,
    burtus samazina visiem vienādi.
    """
    lapas = 1
    for l in limeni:
        lapas *= len(l)
    if lapas > MAKS_LAPAS:
        raise AssertionError("kokā %d lapas - vairāk par %d nav pārskatāmi"
                             % (lapas, MAKS_LAPAS))
    fs = _FONTI[KLASE]
    kolonnas = [[""]] + [list(l) for l in limeni]
    if iznakumi:
        cels = [""]
        for l in limeni:
            cels = [c + (atdalitajs if c else "") + x for c in cels for x in l]
        kolonnas.append(cels)
    platumi = [max(_gabalu_plat(x, fs) for x in k) + 1.0 for k in kolonnas]
    platumi[0] = 2.5
    vajag = sum(platumi) + ZARS * (len(limeni)) + (4.0 if iznakumi else 0)
    merogs = min(1.0, (PLATUMS - 4.0) / vajag)
    platumi = [w * merogs for w in platumi]
    # Ja vietas pietiek, zari kļūst garāki un koks aizņem visu platumu.
    zars = ZARS * merogs + max(0.0, (PLATUMS - 4.0 - vajag)
                               / max(len(limeni), 1))
    # Kolonnu centri no kreisās malas.
    x, centri = 2.0, []
    for i, w in enumerate(platumi):
        centri.append(x + w / 2.0)
        x += w + (zars if i < len(limeni) else 4.0 * merogs)
    aug = lapas * RINDA + 6.0
    stils = (' style="font-size:%.2fpx"' % (fs * merogs)) if merogs < 1 else ""
    dalas = []

    def uzraksts(x, y, t, klase):
        teksts = _teksts(x, y + 1.2, t, klase)
        return teksts.replace("<text ", "<text%s " % stils, 1)

    def zars_(limenis, no, lidz, y_vec):
        if limenis == len(limeni):
            return
        izveles = limeni[limenis]
        katrai = (lidz - no) / float(len(izveles))
        for j, izv in enumerate(izveles):
            a = no + katrai * j
            y = 3.0 + (a + katrai / 2.0) * RINDA
            k = limenis + 1
            dalas.append('<line class="z-lin" x1="%.2f" y1="%.2f" x2="%.2f" '
                         'y2="%.2f"/>'
                         % (centri[k - 1] + platumi[k - 1] / 2.0 + ATSTARPE,
                            y_vec, centri[k] - platumi[k] / 2.0 - ATSTARPE,
                            y))
            dalas.append(uzraksts(centri[k], y, izv, KLASE))
            zars_(k, a, a + katrai, y)

    y_sakne = 3.0 + lapas * RINDA / 2.0
    dalas.append('<circle class="z-punkts" cx="%.2f" cy="%.2f" r="1.2"/>'
                 % (centri[0], y_sakne))
    if sakne:
        dalas.append(_teksts(centri[0] + 1.0, y_sakne - 3.0, sakne, "z-mazs"))
    zars_(0, 0, lapas, y_sakne)
    if iznakumi:
        for i, c in enumerate(kolonnas[-1]):
            dalas.append(uzraksts(centri[-1], 3.0 + (i + 0.5) * RINDA, c,
                                  "z-atzime"))
    return _svg(aug, "".join(dalas))
