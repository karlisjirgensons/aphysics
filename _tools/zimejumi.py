# -*- coding: utf-8 -*-
"""
Vektoru zīmējumi stundu slaidos.

Zīmējumu apraksta deklaratīvi - vienā vietā pateikts, kas jāuzzīmē, nevis
kur uz slaida tas nonāk (SRP). Izmērus dod paša zīmējuma vienībās; šis
modulis tos vienādi mērogo abās asīs, lai leņķi un proporcijas (piem.,
taisnleņķa trijstūris 3-4-5) paliktu pareizas.

    SPEC = dict(w=20, h=6, items=[
        ("v", x1, y1, x2, y2, BLUE),        # vektors ar bultu
        ("s", x1, y1, x2, y2, LINEGREY),    # palīglīnija bez bultas
        ("b", x1, y1, x2, y2, GREY),        # kaste (ķermenis)
        ("t", x, y, "a⃗", BLUE, 15),         # apzīmējums
    ])

    zimejums(slide, x, y, w, h, SPEC)

Koordinātas: x pa labi, y uz leju (tāpat kā slaidā).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import gen_dabaszinibas_1_1 as S              # noqa: E402
from gen_dabaszinibas_1_1 import (            # noqa: E402
    BLUE, GREEN, RED, GREY, LINEGREY, NAVY, GOLD, DARK, PP_ALIGN,
    MSO_ANCHOR, arrow, segment, put, uid)     # noqa: F401

LBL_PAD = 0.16            # apzīmējuma kastes elpa collās
LBL_H = 0.34


def zimejums(slide, x, y, w, h, spec, name=None):
    """Uzzīmē zīmējumu dotajā laukumā, saglabājot proporcijas."""
    fid = name or uid("FIG")
    k = min(w / float(spec["w"]), h / float(spec["h"]))
    ox = x + (w - spec["w"] * k) / 2.0
    oy = y + (h - spec["h"] * k) / 2.0

    def px(a):
        return ox + a * k

    def py(b):
        return oy + b * k

    for it in spec["items"]:
        kind = it[0]
        if kind in ("v", "s"):
            _, x1, y1, x2, y2, color = it[:6]
            lw = it[6] if len(it) > 6 else (S.ARROW_LW if kind == "v"
                                            else 0.014)
            f = arrow if kind == "v" else segment
            f(slide, px(x1), py(y1), px(x2), py(y2), color, lw, name=fid)
        elif kind == "b":
            # Kaste ir četras palīglīnijas, nevis atsevišķa forma - tā
            # HTML zīmētājs to atkārto bez jauna gabala (DRY).
            _, x1, y1, x2, y2, color = it[:6]
            lw = it[6] if len(it) > 6 else 0.022
            malas = ((x1, y1, x2, y1), (x2, y1, x2, y2),
                     (x2, y2, x1, y2), (x1, y2, x1, y1))
            for a, b, c, d in malas:
                segment(slide, px(a), py(b), px(c), py(d), color, lw,
                        name=fid)
        elif kind == "t":
            _, tx, ty, text, color = it[:5]
            size = it[5] if len(it) > 5 else 14
            # kaste tikai tik plata, cik teksts - citādi tukšās malas
            # pārklātos ar kaimiņu apzīmējumiem
            lw_ = (it[6] if len(it) > 6
                   else S.MF.text_w(text, size, bold=True) / 72.0 + LBL_PAD)
            tf = put(slide, px(tx) - lw_ / 2.0, py(ty) - LBL_H / 2.0,
                     lw_, LBL_H,
                     [{"t": text, "size": size, "bold": True,
                       "color": color, "align": PP_ALIGN.CENTER}],
                     anchor=MSO_ANCHOR.MIDDLE, autofit=False,
                     name=fid + "|LBL")
            tf.word_wrap = False        # apzīmējums vienmēr vienā rindā
    return fid


# ------------------------------------------------------- spēki uz ķermeņa
# Latviešu standartā spēka bultu zīmē no ķermeņa centra (spēks pielikts
# masas centrā). Ģeometriju rēķina šī viena funkcija, nevis katrs zīmējums
# atsevišķi (DRY), tāpēc visos slaidos bultas sākas vienādi - kastes vidū.

LBL_GAP = 0.55            # apzīmējuma attālums no bultas (zīm. vienībās)


def bulta(dx, dy, krasa, lbl="", puse=1, nobide=0.0, vieta=0.5, izmers=15,
          atstatums=None):
    """Viena spēka bulta no kastes centra.

    dx, dy     - bultas projekcijas; garums ir spēka modulis mērogā
    puse       - +1 / -1: kurā pusē no bultas likt apzīmējumu
    nobide     - bultas paralēlā nobīde; vajadzīga tikai vienā virzienā
                 vērstām bultām, lai tās nesakristu
    vieta      - apzīmējuma vieta gar bultu (0 - sākums, 1 - gals)
    atstatums  - apzīmējuma attālums no bultas; garam apzīmējumam
                 ("F⃗₂ = 30 N") vajag vairāk vietas nekā īsam ("F⃗₂")
    """
    return dict(dx=dx, dy=dy, krasa=krasa, lbl=lbl, puse=puse,
                nobide=nobide, vieta=vieta, izmers=izmers,
                atstatums=atstatums)


def _perp(dx, dy):
    """Vienības vektors, kas perpendikulārs (dx, dy)."""
    n = (dx * dx + dy * dy) ** 0.5 or 1.0
    return -dy / n, dx / n


def spekukaste(cx, cy, w, h, bultas, kaste=GREY, gap=LBL_GAP):
    """Kaste ar spēku bultām, kas visas sākas kastes centrā (cx, cy).

    Atgriež items sarakstu, ko ieliek zīmējuma specifikācijā.
    """
    items = [("b", cx - w / 2.0, cy - h / 2.0,
              cx + w / 2.0, cy + h / 2.0, kaste)]
    for b in bultas:
        ux, uy = _perp(b["dx"], b["dy"])
        x1 = cx + ux * b["nobide"]
        y1 = cy + uy * b["nobide"]
        x2, y2 = x1 + b["dx"], y1 + b["dy"]
        items.append(("v", x1, y1, x2, y2, b["krasa"]))
        if b["lbl"]:
            t, a = b["vieta"], b["atstatums"] or gap
            items.append(("t", x1 + (x2 - x1) * t + ux * a * b["puse"],
                          y1 + (y2 - y1) * t + uy * a * b["puse"],
                          b["lbl"], b["krasa"], b["izmers"]))
    return items
