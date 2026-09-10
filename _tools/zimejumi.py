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
