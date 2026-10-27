# -*- coding: utf-8 -*-
"""Dienas izaicinājuma lapu stils - papildus site_index.CSS (galva, fons,
fonti, krāsas no palette.py). Telefons pirmais: viena kolonna, lielas
pogas; datorā tikai platāka mala."""

CSS = """
.pl{max-width:34rem;margin:1.4rem auto 0;display:grid;gap:1rem}
.pl [hidden]{display:none!important}
/* Pogas ir pogas: pieskaroties nerodas teksta kursors, iezīmējums vai
   zilais pieskāriena plankums - tikai ievades laukā var rakstīt. */
.pl button,.pl a,.pl summary,.pl-opt,.pl-e,.pl-q{user-select:none;
  -webkit-user-select:none;-webkit-tap-highlight-color:transparent;
  caret-color:transparent}
.pl{caret-color:transparent}
.pl input{caret-color:auto}
.pl button:focus:not(:focus-visible),.pl a:focus:not(:focus-visible),
.pl summary:focus:not(:focus-visible){outline:none}
.pl-kartite{background:var(--surface);border-radius:var(--r);
  box-shadow:var(--sh);padding:1.2rem 1rem}
.pl h2{margin:0 0 .4rem;color:var(--primary);font-family:var(--font-h);
  font-weight:600;font-size:clamp(1.1rem,4.6vw,1.3rem)}
.pl p{margin:.4rem 0}

.pl-poga{display:inline-flex;align-items:center;justify-content:center;
  gap:.4rem;min-height:2.9rem;padding:.6rem 1.1rem;border:0;
  border-radius:var(--r-pill);background:var(--surface2);color:var(--primary);
  font:inherit;font-weight:600;cursor:pointer;text-align:center;
  transition:transform .12s,box-shadow .15s,background .15s}
.pl-poga:hover{transform:translateY(-1px);box-shadow:var(--sh-lg)}
.pl-poga:disabled{opacity:.6;cursor:default;transform:none}
.pl-galvena{background:var(--grad);color:#fff}
.pl-liela{width:100%;min-height:3.8rem;font-family:var(--font-h);
  font-size:clamp(1.1rem,5vw,1.35rem)}
#pl-sakums,#pl-rezultats{display:grid;gap:1rem}
.pl-start{text-align:center}
.pl-meta{color:var(--dim);font-size:.9rem}

/* «Esmu vecāks» - atveras ar bultiņu */
.pl-vecaks{background:var(--surface);border-radius:var(--r);
  box-shadow:var(--sh);overflow:hidden}
.pl-vecaks summary{display:flex;align-items:center;gap:.6rem;cursor:pointer;
  list-style:none;padding:1rem;font-weight:600}
.pl-vecaks summary::-webkit-details-marker{display:none}
.pl-vecaks summary span{flex:1}
.pl-vecaks summary::after{content:"";flex:none;width:.55rem;height:.55rem;
  margin-right:.3rem;transform:rotate(45deg);transition:transform .15s;
  border-right:2px solid var(--primary);border-bottom:2px solid var(--primary)}
.pl-vecaks[open] summary::after{transform:rotate(225deg)}
.pl-iekss{padding:0 1rem 1.1rem}

/* E-pasta forma */
.pl-ievade{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.7rem}
.pl-ievade input{flex:1 1 13rem;min-width:0;min-height:2.9rem;
  padding:.55rem .9rem;border:1px solid var(--line);border-radius:var(--r-pill);
  font:inherit;font-size:16px;background:var(--bg);color:var(--fg)}
.pl-ievade input:focus{outline:2px solid var(--violet);outline-offset:1px}
.pl-ievade .pl-poga{flex:1 1 auto}
.pl-piekr{color:var(--dim);font-size:.78rem;line-height:1.45}
.pl-zina{font-weight:600}
.pl-zina.ok{color:#047857}
.pl-zina.kluda{color:#B91C1C}
.pl-sl{position:absolute;width:1px;height:1px;overflow:hidden;
  clip:rect(0 0 0 0);white-space:nowrap}

/* Spēle */
.pl-augsa{display:flex;justify-content:space-between;color:var(--dim);
  font-weight:600;font-size:.9rem}
.pl-laiks{font-variant-numeric:tabular-nums;color:var(--primary)}
.pl-laiks.maz{color:#B91C1C}
.pl-josla{height:.45rem;margin:.5rem 0 1rem;border-radius:1rem;
  background:var(--line);overflow:hidden}
.pl-josla i{display:block;height:100%;background:var(--grad);
  transition:width .2s linear}
.pl-q{color:var(--dim);text-align:center}
.pl-e{margin:.3rem 0 1.1rem;text-align:center;color:var(--fg);
  font-family:var(--font-h);font-weight:600;line-height:1.35;
  font-size:clamp(1.5rem,7.5vw,2.2rem)}
.pl-opt{display:grid;grid-template-columns:1fr 1fr;gap:.6rem}
.pl-opt button{min-height:3.6rem;padding:.5rem;border:2px solid var(--line);
  border-radius:var(--r);background:var(--surface);color:var(--fg);
  font:inherit;font-weight:600;font-size:clamp(1.05rem,4.8vw,1.25rem);
  cursor:pointer;transition:border-color .12s,background .12s}
.pl-opt button:hover:not(:disabled){border-color:var(--violet);
  background:var(--surface2)}
.pl-opt button:disabled{cursor:default}
.pl-opt button.ok{border-color:#059669;background:#D1FAE5;color:#065F46}
.pl-opt button.kluda{border-color:#DC2626;background:#FEE2E2;color:#991B1B}
.pl-fb{min-height:1.6rem;text-align:center;font-weight:600}
.pl-fb.ok{color:#047857}
.pl-fb.kluda{color:#B91C1C}
.pl-izlaist{display:block;margin:.2rem auto 0;padding:.5rem 1.2rem;border:0;
  background:none;color:var(--dim);font:inherit;font-weight:600;
  cursor:pointer;text-decoration:underline}
.pl-izlaist:disabled{visibility:hidden}

/* Stāvā daļa {3|4} */
.fr{display:inline-flex;flex-direction:column;vertical-align:middle;
  text-align:center;line-height:1.1;font-size:.85em;margin:0 .1em}
.fr>span:first-child{border-bottom:2px solid currentColor;padding:0 .15em}

/* Rezultāts */
.pl-rr{display:grid;grid-template-columns:repeat(2,1fr);gap:.5rem;
  margin:.7rem 0}
.pl-r{display:flex;flex-direction:column;align-items:center;text-align:center;
  padding:.7rem .3rem;border-radius:var(--r);background:var(--surface2)}
.pl-rn{font-size:.78rem;font-weight:600;color:var(--dim)}
.pl-r b{font-family:var(--font-h);font-size:clamp(1.3rem,6vw,1.75rem);
  color:var(--primary);line-height:1.3}
.pl-r.r2 b{color:var(--violet)}
.pl-r.r3 b{color:var(--amber-ink)}
.pl-rs{font-size:.72rem;color:var(--dim);line-height:1.3}
.pl-sk{color:var(--dim);font-size:.85rem;text-align:center}
.pl-uzd{list-style:none;margin:.8rem 0 0;padding:0;display:grid;gap:.45rem}
.pl-uzd li{display:flex;gap:.7rem;align-items:flex-start;padding:.6rem .7rem;
  border-radius:.75rem;border:1px solid var(--line)}
.pl-z{flex:none;width:1.7rem;height:1.7rem;display:grid;place-items:center;
  border-radius:50%;font-weight:700;background:var(--line);color:var(--dim)}
.pl-c .pl-z{background:#D1FAE5;color:#047857}
.pl-w .pl-z{background:#FEE2E2;color:#B91C1C}
.pl-ut{display:flex;flex-direction:column;min-width:0}
.pl-uq{font-size:.8rem;color:var(--dim)}
.pl-ue{font-weight:600}
.pl-ua{font-size:.85rem;color:var(--dim)}
.pl-dalities{display:grid;gap:.5rem;margin-top:1rem}
.pl-otras{display:grid;grid-template-columns:1fr 1fr;gap:.5rem}
.pl-wa{background:#25D366;color:#fff}
.pl-centrs{text-align:center}
"""


def css():
    return CSS
