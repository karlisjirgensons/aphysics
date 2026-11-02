# -*- coding: utf-8 -*-
"""Vecāku aptaujas stils - tikai tas, kā nav dienas izaicinājumā.

Kartītes, pogas, progresa josla, «lielīšanās» galva un e-pasta forma ir
play_stils, jautājuma solis - aptaujas_solis (DRY); šeit ir tikai
salīdzinājuma joslas un ieradumu saraksts. Telefons pirmais.
"""

import aptaujas_solis
import play_stils

CSS = """
.vk-salid{display:grid;gap:.55rem;margin:.9rem 0 .4rem}
.vk-rinda{display:grid;grid-template-columns:7.5rem 1fr auto;gap:.6rem;
  align-items:center;font-size:.9rem;font-weight:600}
.vk-j{height:.8rem;border-radius:1rem;background:var(--line);overflow:hidden}
.vk-j i{display:block;height:100%;background:var(--grad);
  transition:width .6s ease-out}
.vk-rinda.tip{color:var(--dim)}
.vk-rinda.tip .vk-j i{background:var(--dim);opacity:.45}
.vk-rinda b{font-variant-numeric:tabular-nums;color:var(--primary)}
.vk-rinda.tip b{color:var(--dim)}

.vk-ier{list-style:none;margin:.9rem 0 0;padding:0;display:grid;gap:.45rem}
.vk-ier li{display:flex;gap:.7rem;align-items:flex-start;padding:.6rem .7rem;
  border-radius:.75rem;border:1px solid var(--line)}
.vk-z{flex:none;width:1.7rem;height:1.7rem;display:grid;place-items:center;
  border-radius:50%;font-weight:700;background:var(--line);color:var(--dim)}
.vk-labi .vk-z{background:#D1FAE5;color:#047857}
.vk-it{display:flex;flex-direction:column;min-width:0;font-size:.9rem}
.vk-it b{font-size:1rem}
.vk-dim{color:var(--dim);font-size:.82rem}
.vk-avoti{color:var(--dim);font-size:.75rem;line-height:1.45;margin:0 .3rem}
"""


def css():
    return play_stils.css() + aptaujas_solis.css() + CSS
