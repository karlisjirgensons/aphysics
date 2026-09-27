# -*- coding: utf-8 -*-
"""IQ testa bloks: mīklu virkne ar punktiem, sēriju, laiku un rezultātu.

Matemātikas stundā uzdevumi ir mācīšanās daļa; IQ testā tie ir spēle, tāpēc
te ir viss, kas liek gribēt vēl vienu mīklu: punkti par pareizu atbildi no
pirmās reizes, sērija, kas «iekarst», konfeti, progresa josla un beigās
zvaigznes un personīgais rekords. Kļūda neaptur spēli - pēc tās mīklu var
atrisināt vēlreiz, un paskaidrojums «Kāpēc?» parādās vienmēr.

Bloks manto math_bloki.Spele, tāpēc pogas, ievades lauks, atbildes
salīdzināšana (MSP.tirs) un atbilžu sajaukšana (math_uzdevumi.sajauc) ir tās
pašas, kas stundās (DRY). Te ir tikai tas, ar ko IQ tests atšķiras (SRP):
kārtu veidi «izvele», «ievade» un «rezgis» un iegaumēšanas fāze, ko var
pielikt jebkuram no tiem. Kārtas saliek iq_miklas.py.

Viss tests ir viena ekrāna augstumā (skatuve): zīmējumi pielāgojas
atlikušajai vietai, un pēc atbildes paskaidrojums uzbrauc kā panelis no
apakšas, tāpēc spēlē nekad nav jāritina - ne telefonā, ne datorā, ne
pilnekrānā.

Pēc pirmās kļūdas parādās poga «Izlaist»: tā parāda pareizo atbildi un
paskaidrojumu, un spēle iet tālāk - neviens nepaliek iestrēdzis. Pareizai
atbildei pieliek laika vērtējumu pret kārtas mērķa laiku (MSP.tempo no
spēļu dzinēja, tāpēc to pašu var lietot arī stundu uzdevumos).
"""

import json

from math_bloki import Spele, _atr, esc
from math_uzdevumi import sajauc

VEIDI = ("izvele", "ievade", "rezgis")

# Spēles teikumi abās valodās; JS ņem tos, kas atbilst <html lang>. {n} u.c.
# aizpilda JS (f). Rūtiņu vārdam latviski ir trīs formas (1, daudz, 0),
# angliski divas - pēc tā JS zina, kā locīt.
TEKSTI = {
    "lv": {
        "slave": ["Pareizi!", "Lieliski!", "Tā turpināt!", "Ass prāts!",
                  "Nepārspējami!"],
        "variants": "Variants {n}", "atbilde": "Atbilde",
        "parbaudit": "Pārbaudīt", "ieraksti": "Ieraksti atbildi lodziņā.",
        "rutina": "Rūtiņa {n}", "rutinas": ["rūtiņa", "rūtiņas", "rūtiņu"],
        "atzime": "Vispirms atzīmē rūtiņas.", "trukst": "trūkst {n}",
        "lieka": "lieka {n}", "liekas": "liekas {n}",
        "vel_ne_rez": "Vēl ne: {t}. Labo un pārbaudi vēlreiz!",
        "atceros": "Atceros!", "kapec": "Kāpēc?",
        "mans": "Mans rezultāts", "talak": "Tālāk",
        "serija": " Sērija: {n}!",
        "velak": "Pareizi! Nākamo reizi sanāks ar pirmo mēģinājumu.",
        "izlaists": "Nekas! Pareizā atbilde ir iezīmēta - izlasi, kāpēc tā, "
                    "un nākamā sanāks.",
        "izlaist": "Izlaist - parādīt atbildi",
        "vel_ne": "Vēl ne - pamēģini vēlreiz vai izlaid.",
        "nr": "{i}. mīkla no {n}",
        "virsraksti": ["Treniņš dara meistaru!", "Labs sākums!",
                       "Ass prāts!", "Ģeniāli!"],
        "rezultats": "Ar pirmo mēģinājumu atrisināji {p} no {n} mīklām.",
        "labaka": "labākā sērija {n}", "atri": "ātrāk par mērķi: {a} no {n}",
        "jauns": "jauns rekords!", "rekords": "rekords {b}/{n}",
        "atkal": "Spēlēt vēlreiz",
        "tempo": ["Zibens! Divreiz ātrāk par mērķa laiku.",
                  "Super! Ātrāk par mērķa laiku.",
                  "Labs darbs! Mērķa laiks jau pavisam tuvu.",
                  "Izdevās! Ar katru reizi sanāks ātrāk."],
        "merkis": "mērķis {m} s",
    },
    "en": {
        "slave": ["Correct!", "Great!", "Keep it up!", "Sharp mind!",
                  "Unbeatable!"],
        "variants": "Option {n}", "atbilde": "Answer",
        "parbaudit": "Check", "ieraksti": "Type your answer in the box.",
        "rutina": "Cell {n}", "rutinas": ["cell", "cells"],
        "atzime": "Tap some cells first.", "trukst": "{n} missing",
        "lieka": "{n} extra", "liekas": "{n} extra",
        "vel_ne_rez": "Not yet: {t}. Fix it and check again!",
        "atceros": "Got it!", "kapec": "Why?",
        "mans": "My result", "talak": "Next",
        "serija": " Streak: {n}!",
        "velak": "Correct! Next time you'll get it on the first try.",
        "izlaists": "No problem! The right answer is marked - read why, and "
                    "you'll get the next one.",
        "izlaist": "Skip - show the answer",
        "vel_ne": "Not yet - try again or skip.",
        "nr": "Puzzle {i} of {n}",
        "virsraksti": ["Practice makes perfect!", "Good start!",
                       "Sharp mind!", "Genius!"],
        "rezultats": "You solved {p} of {n} puzzles on the first try.",
        "labaka": "best streak {n}", "atri": "faster than target: {a} of {n}",
        "jauns": "new record!", "rekords": "record {b}/{n}",
        "atkal": "Play again",
        "tempo": ["Lightning! Twice as fast as the target time.",
                  "Super! Faster than the target time.",
                  "Good job! The target time is very close.",
                  "Done! It gets faster every time."],
        "merkis": "target {m} s",
    },
}


class IQTests(Spele):
    """Viens IQ tests - visas tā mīklas vienā blokā."""

    MATEMATIKA = ("jaut", "skaidro")

    CSS = """
/* ---- Skatuve: visa spēle ir tieši viena ekrāna augstumā ----
   Bloks nekad nav garāks par ekrānu, tāpēc tajā nav jāritina: augstums ir
   --iq-h, un zīmējums aizņem to, kas paliek pāri virsrakstam un atbildēm.
   Zīmējumu izmērus rēķina no konteinera (cqw/cqh), nevis no ekrāna, tāpēc
   viens un tas pats CSS der telefonam, datoram un pilnekrānam. */
:root{--iq-h:min(calc(100svh - 5.5rem),52rem)}
body.pilns{--iq-h:calc(100svh - 5.8rem);--gals:"Tests galā"}
body{--gals:"Tests galā"}
html[lang="en"] body{--gals:"Test complete"}
body.pilns .bl.iq{padding-top:1rem;padding-bottom:4.8rem;
    justify-content:flex-start}
.bl.iq{position:relative;overflow:hidden;padding-top:.9rem}
.speles[data-veids="iq"]{height:var(--iq-lapa,var(--iq-h));margin:0;
    display:flex;flex-direction:column;container-type:size}
body.pilns .speles[data-veids="iq"]{height:var(--iq-h)}
/* Garajā lapā galva ir šaura, lai spēle ietilptu zem tās tajā pašā
   ekrānā; cik vietas palika, izmēra JS (--iq-lapa). */
body:not(.pilns) .lapa:has(.bl.iq) header.galva{margin-bottom:.8rem;
    padding:.8rem 1.1rem .9rem}
body:not(.pilns) .lapa:has(.bl.iq) header.galva h1{
    font-size:clamp(1.2rem,5vw,1.55rem)}
body:not(.pilns) .lapa:has(.bl.iq) header.galva .merkis{margin-top:.15rem;
    font-size:.9rem}

.iq-hud{flex:none;display:flex;flex-direction:column;gap:.45rem;
    margin:0 0 .6rem}
.iq-prog{display:flex;gap:3px}
.iq-prog span{flex:1;height:.5rem;border-radius:1rem;background:var(--line);
    transition:background .3s}
.iq-prog span.tagad{background:#C4B5FD;animation:iq-puls 1.2s infinite}
.iq-prog span.ja{background:#10B981}
.iq-prog span.velak{background:var(--amber)}
.iq-prog span.izlaists{background:#F87171}
.iq-stat{display:flex;gap:.45rem;flex-wrap:wrap}
.iq-pill{display:inline-flex;align-items:center;gap:.3rem;
    padding:.2rem .7rem;border-radius:var(--r-pill);background:var(--bg);
    font-weight:600;font-size:.9rem;color:var(--fg)}
.iq-pill svg{width:1.05rem;height:1.05rem;fill:currentColor}
.iq-pill.zv{color:#B45309;background:#FEF3C7}
.iq-pill.ug{color:var(--dim)}
.iq-pill.ug.karsts{color:#DC2626;background:#FEE2E2;
    animation:iq-hop .5s}
.iq-pill.lk{margin-left:auto;color:var(--dim);font-variant-numeric:tabular-nums}
.iq-pill.hop{animation:iq-hop .5s}

.iq-kart{flex:1 1 0;min-height:0;display:flex;flex-direction:column;
    position:relative}
.iq-kart.iq-in{animation:iq-in .35s ease-out}
.iq-nr{flex:none;margin:0;color:var(--violet);font-weight:600;
    font-size:.78rem;text-transform:uppercase;letter-spacing:.06em}
.iq-jaut{flex:none;margin:.15rem 0 .5rem;color:var(--primary);
    font-family:var(--font-h);font-weight:600;line-height:1.28;
    font-size:clamp(1.02rem,4.6vw,1.3rem)}
/* Vieta starp jautājumu un pogām: tās izmērs ir atskaites punkts visam,
   kas tajā zīmēts. */
.iq-vieta{flex:1 1 0;min-height:0;container-type:size}
.iq-lauks{height:100%;display:flex;flex-direction:column;gap:.5rem}
.iq-lauks.krata{animation:iq-krata .4s}
.iq-zim{flex:1 1 0;min-height:0;container-type:size;display:flex;
    flex-direction:column;align-items:center;justify-content:center;
    gap:.3rem}
.iq-zim:empty{display:none}
.iq-zim>svg.iq-f,.iq-atcer>svg.iq-f{flex:1 1 0;min-height:0;width:100%;
    height:100%}

/* Figūras un to režģi. Režģis ir tik liels, cik ļauj gan platums, gan
   augstums: --n kolonnas, --rindas rindas. */
svg.iq-f{display:block;width:100%;height:auto}
svg.iq-s{display:inline-block;width:1.7em;height:1.7em;vertical-align:middle}
.iq-mat,.iq-rez,.iq-tab{display:grid;grid-template-columns:repeat(var(--n),1fr);
    width:min(100cqw,calc(100cqh * var(--n) / var(--rindas,var(--n))));
    margin:0 auto}
.iq-mat{gap:.4rem;padding:.4rem;border-radius:var(--r);
    background:var(--surface2)}
.iq-mat>div{aspect-ratio:1;display:flex;align-items:center;min-width:0;
    justify-content:center;background:#fff;border-radius:.6rem;
    border:1px solid #DDD6FE;padding:8%}
.iq-q{color:var(--violet);font-family:var(--font-h);font-weight:700;
    font-size:1.6rem;border:2px dashed var(--violet)!important;
    background:#F5F3FF!important;animation:iq-puls 1.4s infinite}
.iq-flizes{display:flex;flex-wrap:wrap;gap:.45rem;justify-content:center}
.iq-flizes span{min-width:3.1rem;padding:.5rem .6rem;text-align:center;
    border-radius:.7rem;background:var(--surface2);border:1px solid #DDD6FE;
    color:var(--primary);font-family:var(--font-h);font-weight:600;
    font-size:clamp(1.1rem,5vw,1.4rem)}
.iq-tab{gap:.35rem;max-width:15rem}
.iq-tab span,.iq-pir span{display:flex;align-items:center;
    justify-content:center;aspect-ratio:1;border-radius:.6rem;
    background:var(--surface2);border:1px solid #DDD6FE;color:var(--primary);
    font-family:var(--font-h);font-weight:600;
    font-size:clamp(1.05rem,5vw,1.35rem)}
.iq-pir{display:flex;flex-direction:column;align-items:center;gap:.3rem}
.iq-pir div{display:flex;gap:.3rem}
.iq-pir span{width:clamp(2.8rem,15vw,3.6rem);aspect-ratio:auto;
    height:min(2.6rem,calc((100cqh - 1rem) / 4))}
.iq-vienadojumi{display:grid;gap:.4rem;justify-content:center;
    font-size:min(1.45rem,calc(100cqh / 7.5))}
.iq-vien{display:flex;align-items:center;gap:.4rem;flex-wrap:wrap;
    font-family:var(--font-h);font-weight:600;color:var(--primary)}
.iq-sv{fill:none;stroke:var(--fg);stroke-width:2;stroke-linecap:round}
.iq-svc{fill:var(--fg)}
.iq-svq{font-family:var(--font-h);font-weight:700;font-size:22px;
    fill:var(--violet)}
.iq-viena{flex:1 1 0;min-height:0;width:100%}
.iq-viena svg.iq-f{height:100%}
.iq-spogulis{display:grid;grid-template-columns:1fr auto 1fr;gap:.6rem;
    align-items:center;width:min(100cqw,calc(100cqh * 2.1));margin:0 auto}
.iq-sp-l{width:4px;align-self:stretch;border-radius:2px;
    background:repeating-linear-gradient(180deg,#0EA5E9 0 8px,
    transparent 8px 13px)}
.iq-spogulis .iq-q{aspect-ratio:1;display:flex;align-items:center;
    justify-content:center;border-radius:.6rem}
.iq-cipari{display:flex;gap:.35rem;justify-content:center;flex-wrap:wrap}
.iq-cipari span{width:2.6rem;padding:.4rem 0;text-align:center;
    border-radius:.6rem;background:var(--grad);color:#fff;
    font-family:var(--font-h);font-weight:600;font-size:1.6rem}
.iq-rez{gap:.35rem;max-width:26rem}
.iq-rez>span,.iq-rez>button{aspect-ratio:1;display:flex;align-items:center;
    justify-content:center;padding:10%;border-radius:.55rem;min-width:0;
    background:var(--surface2);border:2px solid #DDD6FE;min-height:0}
.iq-rez>span.on{background:var(--violet);border-color:var(--violet)}
.speles .iq-rez>button{min-height:0;padding:10%;border-radius:.55rem}
.speles .iq-rez>button.sel{background:#DDD6FE;border-color:var(--violet);
    box-shadow:inset 0 0 0 3px var(--violet)}
.iq-rez.tukss>button.sel{background:var(--violet)}
.speles .iq-rez>button.rada{border-color:#10B981;
    box-shadow:inset 0 0 0 3px #10B981;background:#DCFCE7}
.speles .ie-rinda{flex:none;margin:0}
.speles .ie-rinda input.rada{border-color:#10B981;background:#ECFDF5}

/* Atbilžu varianti. Ar figūrām tie ir kvadrāti, un to rinda aizņem ne
   vairāk kā --dala no vietas (bez zīmējuma - visu vietu). */
.iq-opc{flex:none;display:grid;grid-template-columns:repeat(var(--kol),1fr);
    gap:.5rem}
.iq-opc.fig{--dala:44cqh;grid-template-rows:repeat(var(--rindas),1fr);
    height:min(var(--dala),calc(var(--rindas) * 100cqw / var(--kol)));
    width:min(100%,calc(var(--dala) * var(--kol) / var(--rindas)));
    margin:0 auto}
.iq-lauks.bez-zim{justify-content:center}
.iq-lauks.bez-zim .iq-opc.fig{--dala:100cqh}
.speles .iq-o{padding:.5rem;min-height:3.2rem;border-radius:.8rem;
    border:2px solid var(--line);background:#fff;display:flex;min-width:0;
    align-items:center;justify-content:center;
    transition:transform .12s,border-color .15s,background .15s}
.speles .iq-opc.fig .iq-o{min-height:0;height:100%;padding:8%}
.speles .iq-o:hover{border-color:var(--violet);background:#fff;
    transform:translateY(-2px)}
.speles .iq-o svg.iq-f{width:100%;height:100%}
.speles .iq-o svg.iq-s{width:2.6rem;height:2.6rem;max-width:100%;
    max-height:100%}
.iq-t{font-weight:600;font-size:clamp(1rem,4.3vw,1.15rem);color:var(--fg)}
.speles .iq-o.ja{border-color:#10B981;background:#DCFCE7;
    animation:iq-pop .45s;box-shadow:0 0 0 4px rgba(16,185,129,.25)}
.speles .iq-o.ne{border-color:#FCA5A5;background:#FEF2F2;opacity:.55}
.speles .iq-o:disabled:hover{background:#FEF2F2}
.speles .iq-o.rada{border-style:dashed}
.iq-opc.sikas{gap:.3rem}
.speles .iq-opc.sikas .iq-o{padding:10%}

.iq-zin{flex:none;margin:.45rem 0 0;font-weight:600}
.iq-zin:empty{display:none}
.iq-zin.labi{color:#047857}
.iq-zin.vel{color:var(--amber-ink)}
.iq-vad{flex:none;display:flex;gap:.5rem;flex-wrap:wrap;margin:.5rem 0 0}
.iq-vad:empty{display:none}
.speles .iq-vad button{flex:1 1 10rem}
.speles .iq-vad button.iq-izlaist{flex:0 1 auto;background:#fff;
    border:2px solid var(--amber);color:var(--amber-ink);font-weight:600}
.speles .iq-vad button.iq-izlaist:hover{background:#FFFBEB}

/* Pēc atbildes: panelis uzbrauc no apakšas pāri variantiem, nevis
   pagarina karti - zīmējums paliek redzams, un ritināt nekas nav jā. */
.iq-panelis{position:absolute;left:0;right:0;bottom:0;z-index:4;
    max-height:100%;overflow-y:auto;padding:.8rem .9rem .9rem;
    border-radius:1.1rem 1.1rem .8rem .8rem;background:#fff;
    border-top:4px solid #10B981;box-shadow:0 -8px 24px rgba(15,12,45,.14);
    animation:iq-uz .3s ease-out}
.iq-panelis.vel{border-top-color:var(--amber)}
.iq-panelis .iq-zin{margin:0;font-size:clamp(1.02rem,4.4vw,1.15rem)}
.iq-panelis .tempo{margin-top:.45rem}
.iq-skaidro{margin:.45rem 0 0;padding:.55rem .8rem;border-radius:var(--r);
    background:#ECFDF5;border:1px solid #A7F3D0;
    font-size:clamp(.92rem,3.8vw,1.02rem)}
.iq-skaidro b{color:#047857}

.iq-atcer{flex:1 1 0;min-height:0;container-type:size;display:flex;
    flex-direction:column;align-items:center;justify-content:center;
    padding:.5rem;border-radius:var(--r);background:#FFFBEB;
    border:1px solid #FDE68A}
.iq-laiks{flex:none;height:.4rem;border-radius:1rem;background:#FDE68A;
    overflow:hidden}
.iq-laiks i{display:block;height:100%;background:var(--amber);
    animation:iq-laiks linear forwards}

/* Rezultāts - arī tas ietilpst skatuvē. */
.iq-beigas{text-align:center;justify-content:center}
.iq-beigas p{margin:.3rem 0}
.iq-rinkis{position:relative;width:min(9.5rem,30cqh);margin:0 auto .3rem}
.iq-rinkis svg{display:block;width:100%;transform:rotate(-90deg)}
.iq-rinkis circle{fill:none;stroke-width:10}
.iq-rinkis .fons{stroke:var(--surface2)}
.iq-rinkis .vert{stroke:url(#iq-grad);stroke-linecap:round;
    transition:stroke-dashoffset 1.2s cubic-bezier(.3,.1,.2,1)}
.iq-rinkis b{position:absolute;inset:0;display:flex;align-items:center;
    justify-content:center;font-family:var(--font-h);font-weight:600;
    color:var(--primary);font-size:min(2rem,7cqh)}
.iq-zvaigznes{display:flex;justify-content:center;gap:.4rem}
.iq-zvaigznes svg{width:min(2.6rem,8cqh);height:min(2.6rem,8cqh);
    fill:var(--line)}
.iq-zvaigznes svg.on{fill:#F59E0B;animation:iq-pop .5s both}
.iq-beigas h3{margin:.4rem 0 .1rem;font-family:var(--font-h);
    color:var(--primary);font-size:clamp(1.3rem,6vw,1.7rem)}
.iq-beigas .iq-stat{justify-content:center;margin:.4rem 0 0}
.iq-beigas .iq-pill.lk{margin-left:0}

.iq-konf{position:absolute;left:50%;top:38%;width:0;height:0;
    pointer-events:none;z-index:5}
.iq-konf i{position:absolute;width:.55rem;height:.8rem;border-radius:2px;
    animation:iq-konf 1.3s cubic-bezier(.2,.6,.4,1) forwards}

/* Ienākšanas kustības nekad neiziet ārpus savas vietas (mērogs uz iekšu,
   atklāšana no apakšas), citādi skatuvē uz mirkli rastos ritjosla. */
@keyframes iq-in{from{opacity:0;transform:scale(.97)}
    to{opacity:1;transform:none}}
@keyframes iq-uz{from{opacity:.4;clip-path:inset(100% 0 0 0)}
    to{opacity:1;clip-path:inset(0 0 0 0)}}
@keyframes iq-pop{0%{transform:scale(.6)}60%{transform:scale(1.12)}
    100%{transform:scale(1)}}
@keyframes iq-hop{0%,100%{transform:none}40%{transform:scale(1.25)}}
@keyframes iq-krata{0%,100%{transform:none}20%{transform:translateX(-7px)}
    40%{transform:translateX(7px)}60%{transform:translateX(-4px)}
    80%{transform:translateX(4px)}}
@keyframes iq-puls{0%,100%{opacity:1}50%{opacity:.55}}
@keyframes iq-laiks{from{width:100%}to{width:0}}
@keyframes iq-konf{0%{transform:translate(0,0) rotate(0);opacity:1}
    100%{transform:translate(var(--x),var(--y)) rotate(var(--r));opacity:0}}
@media (prefers-reduced-motion:reduce){
  .iq-kart.iq-in,.iq-q,.iq-prog span.tagad,.iq-lauks.krata,.iq-o.ja,
  .iq-zvaigznes svg.on,.iq-panelis{animation:none}
}
"""

    JS = """
MSP.veidi.iq=function(root){
  var e=MSP.e,poga=MSP.poga,visas=MSP.dati(root,"data-kartas")||[];
  var id=root.getAttribute("data-id")||location.pathname;
  var IK={
    zv:'<svg viewBox="0 0 24 24"><path d="M12 2l2.9 6.6 7.1.7-5.4 4.8 1.6 7'+
       '-6.2-3.7-6.2 3.7 1.6-7L2 9.3l7.1-.7z"/></svg>',
    ug:'<svg viewBox="0 0 24 24"><path d="M12 2c.8 4 6 6.2 6 12a6 6 0 0 1-12'+
       ' 0c0-3 1.7-5 3-6.8.2 2 1 3.1 2.2 3.4C11 8 10.4 5 12 2z"/></svg>',
    lk:'<svg viewBox="0 0 24 24"><path d="M9 1h6v2H9zM12 4a9 9 0 1 0 0 18'+
       'A9 9 0 0 0 12 4zm1 9.4V8h-2v6.2l4 2.4 1-1.7z"/></svg>'
  };
  var KRASAS=["#7C3AED","#F59E0B","#0EA5E9","#10B981","#EC4899","#4F46E5"];
  var VALODA=document.documentElement.lang==="en"?"en":"lv";
  var T=/*TEKSTI*/[VALODA];
  var st,taimeris;
  /* T teikumā «{n}» vietā liek o.n. */
  function f(s,o){return s.replace(/\\{(\\w+)\\}/g,function(_,k){return o[k];});}
  /* «2 rūtiņas» / «2 squares» - latviski trīs formas, angliski divas. */
  function rutinas(n){var v=T.rutinas;
    return v.length>2?MSP.skaitlis(n,v):n+" "+v[n===1?0:1];}
  /* Google Analytics notikums (analytics.py): tests sākts / pabeigts. Lokāli
     gtag nav - tad nekas nenotiek. */
  function zinot(vards,dati){
    if(!window.gtag){return;}
    dati.test_id=id;dati.test_lang=VALODA;
    try{window.gtag("event",vards,dati);}catch(x){}
  }
  var hud=e("div","iq-hud"),prog=e("div","iq-prog"),stat=e("div","iq-stat");
  var pZv=e("span","iq-pill zv"),pUg=e("span","iq-pill ug"),
      pLk=e("span","iq-pill lk"),kart=e("div","iq-kart");
  stat.appendChild(pZv);stat.appendChild(pUg);stat.appendChild(pLk);
  hud.appendChild(prog);hud.appendChild(stat);
  root.appendChild(hud);root.appendChild(kart);

  function pill(el,ik,t){el.innerHTML=IK[ik]+"<b></b>";
    el.lastChild.textContent=t;}
  function hop(el){el.classList.remove("hop");void el.offsetWidth;
    el.classList.add("hop");}
  function laiks(ms){var s=Math.floor(ms/1000);
    return Math.floor(s/60)+":"+("0"+s%60).slice(-2);}
  function atjauno(){
    pill(pZv,"zv",st.punkti);pill(pUg,"ug",st.serija);
    pill(pLk,"lk",laiks(Date.now()-st.sak));
    pUg.className="iq-pill ug"+(st.serija>=3?" karsts":"");
  }
  function josla(){
    prog.innerHTML="";
    for(var i=0;i<visas.length;i++){
      prog.appendChild(e("span",i<st.rez.length?st.rez[i]:
                                (i===st.i&&!st.beigas?"tagad":"")));
    }
  }
  function saki(c,t,labi){c.zin.innerHTML=t;
    c.zin.className="iq-zin "+(labi?"labi":"vel");}
  function redzams(){
    /* Jauna mīkla sākas tur, kur ir tās jautājums, nevis kaut kur lejā -
       gan garajā lapā, gan lentē, kur ritina pats bloks. */
    var r=root.getBoundingClientRect();
    if(r.top<0&&root.scrollIntoView){root.scrollIntoView({block:"start"});}
  }
  function konfeti(cik){
    if(window.matchMedia&&
       matchMedia("(prefers-reduced-motion: reduce)").matches){return;}
    var box=e("div","iq-konf");
    for(var i=0;i<cik;i++){
      var s=e("i");s.style.background=KRASAS[i%KRASAS.length];
      s.style.setProperty("--x",(Math.random()*320-160)+"px");
      s.style.setProperty("--y",(Math.random()*260-150)+"px");
      s.style.setProperty("--r",(Math.random()*720-360)+"deg");
      s.style.animationDelay=(Math.random()*.15)+"s";
      box.appendChild(s);
    }
    root.appendChild(box);
    setTimeout(function(){if(box.parentNode){root.removeChild(box);}},1700);
  }

  /* ---- kārtas veidi: katrs zīmē savu atbildes vietu ---- */
  function zim(k){var z=e("div","iq-zim");if(k.zim){z.innerHTML=k.zim;}
    return z;}
  var VEIDI={
    izvele:function(c){
      var k=c.k,kol=k.kol||2,pogas=[];
      var fig=k.opcijas.some(function(h){return h.indexOf("<svg")>=0;});
      var g=e("div","iq-opc"+(fig?" fig":"")+(k.sikas?" sikas":""));
      g.style.setProperty("--kol",kol);
      g.style.setProperty("--rindas",Math.ceil(k.opcijas.length/kol));
      if(!k.zim){c.lauks.classList.add("bez-zim");}
      c.lauks.appendChild(zim(k));
      c.rada=function(){pogas[k.pareizi].classList.add("ja","rada");};
      k.opcijas.forEach(function(h,i){
        var b=poga("iq-o","");b.innerHTML=h;
        b.setAttribute("aria-label",f(T.variants,{n:i+1}));
        b.addEventListener("click",function(){
          if(st.gatavs){return;}
          if(i===k.pareizi){b.classList.add("ja");c.labi();}
          else{b.classList.add("ne");b.disabled=true;c.ne();}
        });
        pogas.push(b);g.appendChild(b);
      });
      c.lauks.appendChild(g);
    },
    ievade:function(c){
      var k=c.k,derigas=k.atb.map(MSP.tirs);
      c.lauks.appendChild(zim(k));
      var rinda=e("div","ie-rinda"),inp=document.createElement("input");
      inp.type="text";inp.autocomplete="off";
      inp.setAttribute("inputmode",k.tastatura||"decimal");
      inp.setAttribute("aria-label",T.atbilde);
      inp.placeholder=k.vieta||"?";
      var b=poga("galvena",T.parbaudit);
      rinda.appendChild(inp);rinda.appendChild(b);c.lauks.appendChild(rinda);
      c.rada=function(){inp.value=k.atb[0].replace(/<[^>]*>/g,"");
        inp.className="rada";inp.readOnly=true;b.disabled=true;};
      function skatit(){
        if(st.gatavs){return;}
        var ir=MSP.tirs(inp.value);
        if(!ir){saki(c,T.ieraksti,false);return;}
        if(derigas.indexOf(ir)>=0){
          inp.className="labi";inp.readOnly=true;b.disabled=true;c.labi();
          return;
        }
        inp.className="nepareizi";c.ne();
      }
      b.addEventListener("click",skatit);
      inp.addEventListener("keydown",function(ev){
        if(ev.key==="Enter"){ev.preventDefault();skatit();}
      });
    },
    rezgis:function(c){
      var k=c.k,cik=k.saturs?k.saturs.length:k.n*k.n,izv={},pogas=[];
      var g=e("div","iq-rez"+(k.saturs?"":" tukss"));
      g.style.setProperty("--n",k.n);
      g.style.setProperty("--rindas",Math.ceil(cik/k.n));
      c.lauks.classList.add("bez-zim");
      for(var i=0;i<cik;i++){(function(i){
        var b=poga("","");
        if(k.saturs){b.innerHTML=k.saturs[i];}
        b.setAttribute("aria-label",f(T.rutina,{n:i+1}));
        b.addEventListener("click",function(){
          if(st.gatavs){return;}
          izv[i]=!izv[i];b.classList.toggle("sel",!!izv[i]);
        });
        pogas.push(b);g.appendChild(b);
      })(i);}
      c.lauks.appendChild(g);
      c.rada=function(){
        for(var j=0;j<k.atb.length;j++){pogas[k.atb[j]].classList.add("rada");}
      };
      var parb=poga("galvena iq-parb",T.parbaudit);c.vad.appendChild(parb);
      parb.addEventListener("click",function(){
        if(st.gatavs){return;}
        var trukst=0,lieki=0,ir=0,j;
        for(j=0;j<cik;j++){
          var der=k.atb.indexOf(j)>=0;
          if(izv[j]){ir++;}
          if(der&&!izv[j]){trukst++;}
          if(!der&&izv[j]){lieki++;}
        }
        if(!ir){saki(c,T.atzime,false);return;}
        if(!trukst&&!lieki){c.labi();return;}
        var t=[];
        if(trukst){t.push(f(T.trukst,{n:rutinas(trukst)}));}
        if(lieki){t.push(f(lieki>1?T.liekas:T.lieka,{n:rutinas(lieki)}));}
        c.ne(f(T.vel_ne_rez,{t:t.join(", ")}));
      });
    }
  };

  /* Iegaumēšana: vispirms parāda, tad paslēpj un tikai tad jautā. */
  function atcereties(c,tad){
    var box=e("div","iq-atcer"),lj=e("div","iq-laiks"),li=e("i");
    lj.appendChild(li);li.style.animationDuration=c.k.laiks+"ms";
    box.innerHTML=c.k.radit;
    var b=poga("iq-atceros galvena",T.atceros);
    c.lauks.appendChild(lj);c.lauks.appendChild(box);c.vad.appendChild(b);
    var t=setTimeout(beigt,c.k.laiks),bija=false;
    function beigt(){
      if(bija){return;}bija=true;clearTimeout(t);
      c.lauks.innerHTML="";c.vad.innerHTML="";tad();
    }
    b.addEventListener("click",beigt);
  }

  /* Mīklas beigas - kopīgas pareizai atbildei un izlaistai: ieraksts
     progresa joslā, teikums, (laika vērtējums), paskaidrojums un «Tālāk». */
  function noslegt(c,rez,teikums,labi,vel){
    st.gatavs=true;st.rez.push(rez);
    atjauno();josla();
    c.zin.innerHTML="";c.zin.className="iq-zin";c.vad.innerHTML="";
    var p=e("div","iq-panelis"+(labi?"":" vel")),z=e("p","");
    saki({zin:z},teikums,labi);p.appendChild(z);
    if(vel){p.appendChild(vel);}
    if(c.k.skaidro){
      var s=e("div","iq-skaidro");
      s.innerHTML="<b>"+T.kapec+"</b> "+c.k.skaidro;
      p.appendChild(s);
    }
    var vad=e("div","iq-vad");p.appendChild(vad);c.kart.appendChild(p);
    var pedeja=st.i+1>=visas.length;
    var t=poga("iq-talak galvena",pedeja?T.mans:T.talak);
    t.addEventListener("click",function(){
      if(pedeja){beigas();}else{st.i++;radi();redzams();}
    });
    vad.appendChild(t);
  }
  function atrisinats(c){
    if(st.gatavs){return;}
    var pirma=!st.kluda,sek=(Date.now()-c.t0)/1000;
    var tp=c.k.merkis?MSP.tempo(sek,c.k.merkis,T):null;
    if(pirma){
      st.punkti++;st.serija++;st.labaka=Math.max(st.labaka,st.serija);
      if(tp&&tp.limenis<=1){st.atri++;}
      konfeti(st.serija>=3||(tp&&tp.limenis===0)?30:14);
    }
    hop(pirma?pZv:pUg);
    noslegt(c,pirma?"ja":"velak",
            pirma?(T.slave[Math.min(st.serija,T.slave.length)-1]+
                   (st.serija>=3?f(T.serija,{n:st.serija}):""))
                 :T.velak,
            true,tp&&tp.el);
  }
  function izlaist(c){
    if(st.gatavs){return;}
    st.serija=0;
    if(c.rada){c.rada();}
    noslegt(c,"izlaists",T.izlaists,false);
  }
  function kluda(c,teksts){
    if(!st.kluda){st.kluda=true;st.serija=0;atjauno();}
    if(!c.izl){
      /* Kad neiet, ir skaidra izeja: parādīt atbildi un iet tālāk. */
      c.izl=poga("iq-izlaist",T.izlaist);
      c.izl.addEventListener("click",function(){izlaist(c);});
      c.vad.appendChild(c.izl);
    }
    saki(c,teksts||T.vel_ne,false);
    c.lauks.classList.remove("krata");void c.lauks.offsetWidth;
    c.lauks.classList.add("krata");
  }

  function radi(){
    var k=visas[st.i];
    st.kluda=false;st.gatavs=false;
    josla();atjauno();
    kart.innerHTML="";kart.className="iq-kart";void kart.offsetWidth;
    kart.className="iq-kart iq-in";
    var jaut=e("p","iq-jaut");jaut.innerHTML=k.jaut;
    var c={k:k,kart:kart,lauks:e("div","iq-lauks"),zin:e("p","iq-zin"),
           vad:e("div","iq-vad")};
    c.labi=function(){atrisinats(c);};
    c.ne=function(t){kluda(c,t);};
    kart.appendChild(e("p","iq-nr",f(T.nr,{i:st.i+1,n:visas.length})));
    var vieta=e("div","iq-vieta");vieta.appendChild(c.lauks);
    kart.appendChild(jaut);kart.appendChild(vieta);
    kart.appendChild(c.zin);kart.appendChild(c.vad);
    /* Laiku skaita no brīža, kad var atbildēt - iegaumēšana neskaitās. */
    function jautat(){c.t0=Date.now();VEIDI[k.veids](c);}
    if(k.radit){atcereties(c,jautat);}else{jautat();}
  }

  function beigas(){
    clearInterval(taimeris);
    st.beigas=true;josla();
    var n=visas.length,p=st.punkti,d=p/n;
    var zv=d>=0.9?3:d>=0.7?2:d>=0.4?1:0;
    var bija=-1;
    try{
      bija=parseInt(localStorage.getItem("iq:"+id)||"-1",10);
      if(p>bija){localStorage.setItem("iq:"+id,""+p);}
    }catch(x){}
    kart.innerHTML="";kart.className="iq-kart iq-in iq-beigas";
    var L=2*Math.PI*52;
    var r=e("div","iq-rinkis");
    r.innerHTML='<svg viewBox="0 0 120 120"><defs><linearGradient '+
      'id="iq-grad"><stop offset="0" stop-color="#4F46E5"/><stop '+
      'offset="1" stop-color="#06B6D4"/></linearGradient></defs>'+
      '<circle class="fons" cx="60" cy="60" r="52"/><circle class="vert" '+
      'cx="60" cy="60" r="52" stroke-dasharray="'+L+'" '+
      'stroke-dashoffset="'+L+'"/></svg><b></b>';
    r.lastChild.textContent=p+"/"+n;
    kart.appendChild(r);
    setTimeout(function(){r.querySelector(".vert")
      .setAttribute("stroke-dashoffset",""+L*(1-d));},60);
    var zvs=e("div","iq-zvaigznes");
    for(var i=0;i<3;i++){
      var s=e("span");s.innerHTML=IK.zv;
      if(i<zv){s.firstChild.setAttribute("class","on");
        s.firstChild.style.animationDelay=(0.5+i*0.25)+"s";}
      zvs.appendChild(s);
    }
    kart.appendChild(zvs);
    kart.appendChild(e("h3","",T.virsraksti[zv]));
    kart.appendChild(e("p","",f(T.rezultats,{p:p,n:n})));
    var ch=e("div","iq-stat"),a=e("span","iq-pill lk"),
        b=e("span","iq-pill ug"),c=e("span","iq-pill zv");
    pill(a,"lk",laiks(Date.now()-st.sak));
    pill(b,"ug",f(T.labaka,{n:st.labaka}));
    ch.appendChild(a);ch.appendChild(b);
    var d_=e("span","iq-pill lk");
    pill(d_,"lk",f(T.atri,{a:st.atri,n:n}));
    ch.appendChild(d_);
    if(bija>=0){
      pill(c,"zv",p>bija?T.jauns:f(T.rekords,{b:bija,n:n}));
      ch.appendChild(c);
    }
    kart.appendChild(ch);
    var vad=e("div","iq-vad"),no=poga("galvena iq-atkal",T.atkal);
    no.addEventListener("click",function(){sakt();redzams();});
    vad.appendChild(no);kart.appendChild(vad);
    if(zv>=2){setTimeout(function(){konfeti(60);},400);}
    zinot("iq_finish",{score:p,total:n,stars:zv,best_streak:st.labaka,
                       seconds:Math.round((Date.now()-st.sak)/1000)});
  }

  /* Garajā lapā spēle aizņem tieši to, kas ekrānā palicis zem galvas.
     Ja tas ir par maz (ļoti zems ekrāns), paliek CSS augstums - viss ekrāns,
     un lapu vienreiz pabīda līdz spēlei. Lentē augstumu dod CSS. */
  var MIN_H=440;
  function izmers(){
    if(document.body.classList.contains("pilns")){return;}
    var bl=root.closest(".bl")||root;
    var apaksa=parseFloat(getComputedStyle(bl).paddingBottom)||0;
    var h=window.innerHeight-(root.getBoundingClientRect().top+
          window.pageYOffset)-apaksa-8;
    if(h>=MIN_H){root.style.setProperty("--iq-lapa",Math.floor(h)+"px");}
    else{root.style.removeProperty("--iq-lapa");}
  }
  izmers();
  window.addEventListener("resize",izmers);
  if(window.MutationObserver){
    new MutationObserver(izmers).observe(document.body,
      {attributes:true,attributeFilter:["class"]});
  }

  function sakt(){
    st={i:0,punkti:0,serija:0,labaka:0,atri:0,sak:Date.now(),rez:[]};
    zinot("iq_start",{total:visas.length});
    clearInterval(taimeris);
    taimeris=setInterval(function(){pill(pLk,"lk",
      laiks(Date.now()-st.sak));},1000);
    radi();
  }
  if(visas.length){sakt();}
};
"""

    def __init__(self, kartas, id_):
        Spele.__init__(self, None)
        self.id = id_
        self.kartas = [self._zimeta(k) for k in kartas]

    def _zimeta(self, karta):
        """Kārta lapai: teksts uzzīmēts, izvēles varianti sajaukti."""
        if karta["veids"] not in VEIDI:
            raise AssertionError("nezināms mīklas veids «%s»"
                                 % karta["veids"])
        out = dict(karta)
        for lauks in self.MATEMATIKA:
            if lauks in out:
                out[lauks] = esc(out[lauks])
        if karta["veids"] == "izvele":
            sajauc(out, karta)
        return out

    JS = JS.replace("/*TEKSTI*/", json.dumps(TEKSTI, ensure_ascii=False))

    def klase(self):
        return "iq"

    def veids(self):
        return "iq"

    def atributi(self):
        return {"data-kartas": _atr(self.kartas), "data-id": self.id}


def parbaudi(saturs):
    """IQ testa lapā ir tikai IQ bloki - bez ievada un teorijas."""
    for b in saturs.SATURS:
        if not isinstance(b, IQTests):
            raise AssertionError("IQ testā «%s» ir %s - tur drīkst būt tikai "
                                 "IQTests" % (saturs.TEMA,
                                              b.__class__.__name__))
