# -*- coding: utf-8 -*-
"""«Cik labi zini bērna matemātiku» stils - tikai tas, kā nav citur.

Kartītes, pogas, «lielīšanās» galva, uzdevumu saraksts un forma ir
play_stils, jautājuma solis - aptaujas_solis (DRY); šeit ir klašu režģis
un liels rezultāta skaitlis. Telefons pirmais: 3 × 3 pogas.
"""

import aptaujas_solis
import play_stils

CSS = """
.sm-klases-v{margin:1rem 0 .5rem;font-weight:600;color:var(--dim)}
.sm-klases{display:grid;grid-template-columns:repeat(3,1fr);gap:.55rem}
.sm-klases .pl-poga{min-height:3.4rem;padding:.5rem .3rem;white-space:nowrap;
  border:2px solid var(--line);
  background:var(--surface);color:var(--primary);font-family:var(--font-h);
  font-size:clamp(1rem,4.4vw,1.15rem)}
.sm-klases .pl-poga:hover{border-color:var(--violet);background:var(--surface2)}
.sm-skaits{font-family:var(--font-h);font-weight:700;line-height:1.1;
  font-size:clamp(2rem,10vw,2.6rem);background:var(--grad);
  -webkit-background-clip:text;background-clip:text;color:transparent}
.pl-ue .fr,.pl-ua .fr{font-size:.8em}
"""


def css():
    return play_stils.css() + aptaujas_solis.css() + CSS
