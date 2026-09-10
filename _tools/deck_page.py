# -*- coding: utf-8 -*-
"""
Prezentācijas lapas čaula: noformējums (CSS), vadība (JS) un lapas veidne.

Šis modulis neko nezina par .pptx - tam padod gatavus slaidu HTML gabalus.
html_deck.py pārvērš slaidus HTML, šis tos ieliek lapā (SRP). Krāsas un
fonti nāk no palette.py, tāpēc te to nav (DRY).

Trīs skati, viens saturs:
    dators    - precīzs slaids cits zem cita, lapa ritinās;
    telefons  - slaidi horizontālā lentē, ko šķir ar pirkstu;
    pilnekrāns - viens slaids uz visa ekrāna, ar bultām un taustiņiem.
"""

import html

import palette

CSS = """
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{background:var(--bg);color:var(--fg);
     font-family:var(--font);
     -webkit-text-size-adjust:100%}
.top{position:sticky;top:0;z-index:20;display:flex;gap:.6rem;
     align-items:center;flex-wrap:wrap;
     padding:.6rem .9rem;background:var(--grad);color:#fff;
     box-shadow:var(--sh-md)}
.top b{font-size:1rem;font-weight:600;font-family:var(--font-h)}
.top .sub{font-size:.78rem;color:rgba(255,255,255,.82);flex:1 1 12rem}
.top button{font:inherit;font-size:.85rem;font-weight:500;border:0;
     border-radius:var(--r-pill);padding:.4rem .95rem;color:#fff;
     background:rgba(255,255,255,.18);cursor:pointer;
     transition:background .15s}
.top button:hover{background:rgba(255,255,255,.30)}
.top .cnt{font-size:.8rem;color:rgba(255,255,255,.82);
     font-variant-numeric:tabular-nums}
.top .back{font-size:.82rem;color:#fff;text-decoration:none;
     padding:.35rem .75rem;border-radius:var(--r-pill);
     background:rgba(255,255,255,.14);transition:background .15s}
.top .back:hover{background:rgba(255,255,255,.28)}

.deck{padding:.9rem;display:flex;flex-direction:column;gap:.9rem}
.slide{container-type:inline-size;background:var(--surface);
       border-radius:var(--r);overflow:hidden;box-shadow:var(--sh-md);
       position:relative}
.num{position:absolute;z-index:5;right:.6rem;top:.4rem;font-size:.7rem;
     color:var(--dim);font-variant-numeric:tabular-nums}

/* ---------- DATORA SKATS: precīzs slaids ---------- */
.stage{position:relative;width:100%;aspect-ratio:13.333/7.5;
       background:var(--surface)}
.stage i,.stage .rg{position:absolute;display:block}
/* vektoru zīmējums: bultas vienā SVG pāri slaidam */
.stage .fg{position:absolute;left:0;top:0;width:100%;height:100%;
           overflow:visible;pointer-events:none}
.fig{position:relative;container-type:inline-size;width:100%;
     margin:.6rem 0}
.fig svg{position:absolute;left:0;top:0;width:100%;height:100%}
.fig b{position:absolute;text-align:center;font-weight:600;
       line-height:1.1;transform:translateY(-.1em)}
.stage .tb{position:absolute;display:flex;flex-direction:column;
           justify-content:flex-start;overflow:visible}
.stage .tb p{margin:0;line-height:1.22}
.flow{display:none}

/* ---------- vertikāla daļa (a/b) ---------- */
.f{display:inline-flex;flex-direction:column;align-items:stretch;
   text-align:center;vertical-align:middle;margin:0 .28em;line-height:1.14}
.f .n{display:block;padding:0 .2em}
.f .d{display:block;padding:0 .2em;border-top:.075em solid currentColor}

/* ---------- kvadrātsakne: vinkuls pāri visai izteiksmei ----------
   Saknes zīme ir zīmēta (SVG), tāpēc tā izstiepjas līdz izteiksmes
   augstumam un vinkuls turpinās tieši no tās augšējā stūra. */
.rt{position:relative;display:inline-block;white-space:nowrap;
    --rw:.66em;padding-left:var(--rw);margin:0 .06em}
.rt .rk{position:absolute;left:0;top:0;bottom:0;width:var(--rw);height:auto;
        fill:currentColor}
.rt .rv{display:inline-block;border-top:.075em solid currentColor;
        padding:.16em .2em 0 .06em}

/* ---------- vektors: bultiņa virs simbola ----------
   Unikoda kombinējošā bultiņa (U+20D7) lapas fontos vai nu iztrūkst, vai
   nostājas blakus burtam, tāpēc bultiņu zīmē CSS: kāts pāri simbolam un
   trīsstūra uzgalis labajā galā. */
.vv{position:relative;display:inline-block;line-height:1}
.vv::before{content:"";position:absolute;left:-.03em;right:.13em;top:-.05em;
            border-top:.07em solid currentColor}
.vv::after{content:"";position:absolute;right:-.04em;top:-.105em;
           width:0;height:0;border-left:.2em solid currentColor;
           border-top:.1em solid transparent;
           border-bottom:.1em solid transparent}

/* ---------- TELEFONA SKATS ---------- */
@media (max-width:768px){
  /* Lapa pati nekustas - kustas tikai slaidu lente. */
  html,body{overflow:hidden;overscroll-behavior:none}
  body{display:flex;flex-direction:column;height:100vh;height:100dvh}
  .top button{font-size:.78rem;padding:.35rem .7rem}
  .top b{font-size:.95rem;flex:1 1 100%;order:2}
  .top .back{order:1}
  /* Josla telefonā ir šaura - paskaidrojums nav tā vērts, lai atņemtu
     slaidam augstumu; tas pats teksts ir uz pirmā slaida. */
  .top .sub{display:none}

  /* Slaidus šķir ar pirkstu: horizontāla lente, kas piesienas pie katra
     slaida (scroll-snap). Ritina pati pārlūkprogramma, tāpēc kustība ir
     tikpat plūstoša kā lapas ritināšana un JavaScript te nav vajadzīgs.
     Garš slaids ritinās uz leju pats savā rāmī. */
  .deck{flex:1 1 auto;min-height:0;flex-direction:row;gap:0;padding:0;
        overflow-x:auto;overflow-y:hidden;overscroll-behavior-x:contain;
        scroll-snap-type:x mandatory;scroll-behavior:smooth;
        -webkit-overflow-scrolling:touch;scrollbar-width:none}
  .deck::-webkit-scrollbar{display:none}
  .slide{flex:0 0 100%;height:100%;display:flex;flex-direction:column;
         overflow-y:auto;overscroll-behavior-y:contain;
         scroll-snap-align:start;scroll-snap-stop:always;
         border-radius:0;box-shadow:none}
  .stage{display:none}
  /* Fons aizpilda slaidu līdz apakšai arī tad, ja teksta ir maz. */
  .flow{display:block;flex:1 0 auto;padding:.85rem .8rem 1rem}
  .flow *{max-width:100%}
  /* Kārtas numuru rāda augšējā josla, uz paša slaida tas nav vajadzīgs. */
  .num{display:none}

  .flow p{margin:.28rem 0;line-height:1.36;overflow-wrap:anywhere}
  .flow .h1{font-size:clamp(1.15rem,5.6vw,1.7rem);font-weight:700;
            line-height:1.22}
  .flow .h2{font-size:clamp(1.02rem,4.7vw,1.4rem);font-weight:700;
            line-height:1.26}
  .flow .p1{font-size:clamp(.95rem,4.1vw,1.15rem)}
  .flow .p2{font-size:clamp(.88rem,3.7vw,1.05rem)}
  .flow .p3{font-size:clamp(.8rem,3.3vw,.95rem)}
  .flow .kicker p{font-size:clamp(.68rem,3vw,.8rem);letter-spacing:.06em;
                  text-transform:uppercase;color:var(--dim)}
  .flow .title p{font-size:clamp(1.15rem,5.4vw,1.6rem);font-weight:600;
                 font-family:var(--font-h);color:var(--primary)}
  .flow .badge p{font-size:clamp(.78rem,3.4vw,.95rem);font-weight:600;
                 color:var(--amber-ink)}
  .flow.dark p{color:#EEF2FF}
  .flow.dark .card{background:rgba(255,255,255,.07);
                    border-color:rgba(255,255,255,.25)}
  .flow .card{border:1px solid var(--line);border-left-width:4px;
              border-left-color:var(--violet);border-radius:.75rem;
              padding:.65rem .75rem;margin:.55rem 0;
              background:var(--surface)}
  .flow .blk{margin:.35rem 0}
  .flow .mf{font-size:clamp(1.15rem,6vw,1.75rem);font-weight:600;
            text-align:center;color:var(--primary);margin:.5rem 0}
  .flow .mf .mc{display:inline-block;margin:.15rem .5rem}
  .flow .mfcard{background:var(--surface2);border-radius:.75rem}

  .flow .mtbl{margin:.55rem 0;display:flex;flex-direction:column;gap:.5rem}
  .flow .mrow{border:1px solid var(--line);border-radius:.75rem;
              overflow:hidden}
  .flow .mcell{display:flex;gap:.6rem;align-items:baseline;
               padding:.45rem .65rem;border-top:1px solid var(--line)}
  .flow .mrow .mcell:first-child{border-top:0;background:var(--surface2);
                                 font-weight:600;color:var(--primary)}
  .flow .ml{flex:0 0 38%;font-size:clamp(.7rem,3vw,.82rem);
            color:var(--dim);text-transform:uppercase;
            letter-spacing:.06em}
  .flow .mv{flex:1 1 auto;font-size:clamp(.88rem,3.8vw,1.05rem)}
}

/* ---------- PILNEKRĀNA SKATS: viens slaids uz visa ekrāna ---------- */
/* Slaids patur 13.333:7.5 malu attiecību un ieņem tik daudz, cik ietilpst;
   pārējais paliek tumšs. Teksts mērogojas pats, jo .slide ir konteiners. */
body.fs{background:#1E1B4B;overflow:hidden}
body.fs .top{display:none}
body.fs .deck{position:fixed;inset:0;margin:0;padding:0;gap:0;
              align-items:center;justify-content:center;
              overflow:hidden;scroll-snap-type:none}
body.fs .slide{display:none;margin:0;border-radius:0;box-shadow:none;
               flex:0 0 auto;overflow:hidden;
               width:min(100vw,calc(100vh * 13.333 / 7.5));
               height:min(100vh,calc(100vw * 7.5 / 13.333))}
body.fs .slide.on{display:block}
body.fs .num{display:none}
/* pilnekrānā vienmēr rāda īsto slaidu, arī telefonā */
body.fs .stage{display:block}
body.fs .flow{display:none}

.fsui{display:none}
body.fs .fsui{display:flex;position:fixed;z-index:30;left:50%;
  bottom:calc(1rem + env(safe-area-inset-bottom));transform:translateX(-50%);
  align-items:center;gap:.35rem;padding:.3rem .45rem;color:#fff;
  border-radius:var(--r-pill);background:rgba(15,12,45,.7);
  opacity:.45;transition:opacity .2s}
body.fs .fsui:hover,body.fs .fsui:focus-within{opacity:1}
.fsui button{font:inherit;line-height:1;border:0;cursor:pointer;color:#fff;
  background:transparent;border-radius:var(--r-pill);padding:.3rem .7rem;
  transition:background .15s}
.fsui button:hover{background:rgba(255,255,255,.18)}
.fsui .nav{font-size:1.25rem;padding:.15rem .6rem}
.fsui .cnt{font-size:.8rem;min-width:4.2rem;text-align:center;
           font-variant-numeric:tabular-nums}
"""

JS = """
(function(){
  /* Katrai daļai viens uzdevums: ekrāns (fullscreen API), stāvoklis
     (kurš slaids) un attēlošana. Taustiņi un pogas tikai sauc tos pašus
     trīs darbus - open, close, go. */
  var slides=[].slice.call(document.querySelectorAll('.slide'));
  var cnt=document.getElementById('cnt');
  var fscnt=document.getElementById('fscnt');
  var deck=document.getElementById('deck');
  var cur=0,on=false;

  /* --- ekrāns --- */
  var root=document.documentElement;
  function fsel(){return document.fullscreenElement||
                         document.webkitFullscreenElement;}
  function ask(){
    var f=root.requestFullscreen||root.webkitRequestFullscreen;
    if(f){try{var p=f.call(root);if(p&&p.catch)p.catch(function(){});}
          catch(e){}}
  }
  function drop(){
    var f=document.exitFullscreen||document.webkitExitFullscreen;
    if(fsel()&&f){try{var p=f.call(document);if(p&&p.catch)p.catch(function(){});}
                  catch(e){}}
  }

  /* --- attēlošana --- */
  function render(){
    for(var i=0;i<slides.length;i++)
      slides[i].classList.toggle('on',i===cur);
    var pos=(cur+1)+' / '+slides.length;
    fscnt.textContent=pos;
    cnt.textContent=pos;
  }

  /* --- stāvoklis --- */
  function go(i){
    cur=i<0?0:(i>=slides.length?slides.length-1:i);
    render();
  }
  function open(){
    on=true;document.body.classList.add('fs');ask();render();
  }
  function close(){
    on=false;document.body.classList.remove('fs');drop();render();reveal();
  }
  function reveal(){
    if(slides[cur])slides[cur].scrollIntoView({block:'start',inline:'start'});
  }

  /* --- kurš slaids ir redzams --- */
  /* Telefonā slaidus šķir pati lente, tāpēc kārtas numuru nolasa no
     ekrāna, nevis glabā atsevišķi - tā skaitītājs un poga "Pilnekrāns"
     vienmēr runā par to slaidu, ko cilvēks tobrīd redz. */
  function watch(){
    if(!window.IntersectionObserver)return;
    var seen=slides.map(function(){return 0;});
    var io=new IntersectionObserver(function(es){
      for(var i=0;i<es.length;i++)
        seen[slides.indexOf(es[i].target)]=es[i].intersectionRatio;
      if(on)return;
      var best=0;
      for(var j=1;j<slides.length;j++)if(seen[j]>seen[best])best=j;
      if(best!==cur)go(best);
    },{threshold:[0,.25,.5,.75,1]});
    slides.forEach(function(s){io.observe(s);});
  }

  /* --- vadība --- */
  document.getElementById('fs').addEventListener('click',open);
  document.getElementById('fsx').addEventListener('click',close);
  document.getElementById('prev').addEventListener('click',function(e){
    e.stopPropagation();go(cur-1);});
  document.getElementById('next').addEventListener('click',function(e){
    e.stopPropagation();go(cur+1);});
  deck.addEventListener('click',function(){if(on)go(cur+1);});

  document.addEventListener('keydown',function(e){
    if(!on)return;
    var k=e.key;
    if(k==='ArrowRight'||k===' '||k==='PageDown'||k==='Enter'){go(cur+1);}
    else if(k==='ArrowLeft'||k==='PageUp'||k==='Backspace'){go(cur-1);}
    else if(k==='Home'){go(0);}
    else if(k==='End'){go(slides.length-1);}
    else if(k==='Escape'){close();}
    else{return;}
    e.preventDefault();
  });
  /* Esc pilnekrānā pārtver pārlūks - tad jāsakārto pašiem. */
  function synced(){if(on&&!fsel())close();}
  document.addEventListener('fullscreenchange',synced);
  document.addEventListener('webkitfullscreenchange',synced);

  watch();
  render();
})();
"""

PAGE = """<!DOCTYPE html>
<html lang="lv">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>%(title)s</title>
%(fonts)s<style>%(root)s%(css)s</style>
</head>
<body>
<div class="top">
  <a class="back" href="../index.html">&#8592; Uz t&#275;m&#257;m</a>
  <b>%(title)s</b>
  <span class="sub">%(kicker)s</span>
  <span class="cnt" id="cnt"></span>
  <button id="fs" type="button">Pilnekr&#257;ns</button>
</div>
<div class="deck" id="deck">
%(slides)s
</div>
<div class="fsui" id="fsui">
  <button class="nav" id="prev" type="button" aria-label="Iepriek&#353;&#275;jais">&#8249;</button>
  <span class="cnt" id="fscnt"></span>
  <button class="nav" id="next" type="button" aria-label="N&#257;kamais">&#8250;</button>
  <button id="fsx" type="button">Esc</button>
</div>
<script>%(js)s</script>
</body>
</html>
"""


def page(title, kicker, slides):
    """Gatava prezentācijas lapa no slaidu HTML gabaliem.

    Virsrakstu un paskaidrojumu aizsedz šeit, lai izsaucējam par to nav
    jādomā."""
    return PAGE % {"title": html.escape(title),
                   "kicker": html.escape(kicker),
                   "slides": "\n".join(slides),
                   "css": CSS, "js": JS,
                   "root": palette.root_css(), "fonts": palette.FONT_LINK}
