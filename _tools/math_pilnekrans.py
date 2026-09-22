# -*- coding: utf-8 -*-
"""Stundas pilnekrāna skats: viena daļa uz visa ekrāna, šķirstāma ar pirkstu.

Uz datora un planšetes stundu var rādīt kā prezentāciju - virsraksts un katrs
bloks pa vienam uz visa ekrāna. Šķir ar pirkstu (lente pati piesienas pie
malas), ar bultiņām, ar pogām lejā vai ar atstarpi; Esc iziet ārā.

Pogas un joslu uzbūvē pats JavaScript, tāpēc lapas veidnē (math_lapa.py) par
šo skatu nav nevienas rindas (SRP), un vadība ir tā pati, kas prezentācijām
(deck_page.py): «Pilnekrāns», ‹ › un Esc.

Telefonā šis ir noklusētais skats: stunda atveras kā šķirstāma lente, jo uz
maza ekrāna gara ritināma lapa pazaudē, kur beidzas viens bloks un sākas
nākamais. Ar pogu «Visa lapa» var pāriet uz garo lapu, un izvēle paliek
atmiņā (localStorage), tāpēc nākamā stunda atveras tā, kā students grib.

Pilnekrāna režīmu (fullscreen API) telefonā neprasa: pārlūks to atļauj tikai
pēc pieskāriena, un lentes skatam tas nav vajadzīgs - to dod pati CSS.
"""

# Lente ir pati .lapa; .saturs kļūst par display:contents, tāpēc bloki nonāk
# tieši lentē un otra ietvara nav vajadzīga (DRY - viens un tas pats HTML
# kalpo abiem skatiem).
CSS = """
.pilnpoga{display:none;flex:none;font:inherit;font-size:.82rem;
    font-weight:500;cursor:pointer;border:0;border-radius:var(--r-pill);
    padding:.35rem .9rem;color:#fff;background:rgba(255,255,255,.16);
    transition:background .15s}
.pilnpoga:hover{background:rgba(255,255,255,.3)}
.pilnpoga{display:inline-block}

body.pilns{overflow:hidden;background:#1E1B4B}
body.pilns .augsa{display:none}
body.pilns .skolotajam,body.pilns nav.talak{display:none}
body.pilns .lapa{max-width:none;height:100vh;height:100svh;margin:0;padding:0;
    display:flex;overflow-x:auto;overflow-y:hidden;
    scroll-snap-type:x mandatory;scroll-behavior:smooth;
    -webkit-overflow-scrolling:touch;scrollbar-width:none}
body.pilns .lapa::-webkit-scrollbar{display:none}
body.pilns .saturs{display:contents}
body.pilns header.galva,body.pilns .bl{flex:0 0 100%;height:100vh;
    height:100svh;
    overflow-y:auto;
    scroll-snap-align:start;margin:0;border-radius:0;box-shadow:none;
    border:0;background:var(--surface);
    display:flex;flex-direction:column;justify-content:center;
    justify-content:safe center;
    padding:3rem max(1.2rem,calc((100vw - 46rem)/2)) 5rem}
body.pilns header.galva{background:var(--grad)}
body.pilns .bl.stasts{background:linear-gradient(135deg,#EEF2FF,#F5F3FF)}
body.pilns .bl.kopa{background:#ECFDF5}
body.pilns .bl.majas{background:#FFFBEB}
/* Uz visa ekrāna kreisā mala būtu tālu no teksta, tāpēc galveno domu
   iezīmē fons, nevis svītra. */
body.pilns .bl.doma{background:var(--surface2)}
body.pilns .bl>h2{font-size:clamp(1.3rem,3.2vw,1.9rem)}
body.pilns header.galva h1{font-size:clamp(1.8rem,4.6vw,2.8rem)}

.pilnjosla{display:none}
body.pilns .pilnjosla{display:flex;position:fixed;z-index:30;left:50%;
    bottom:calc(1rem + env(safe-area-inset-bottom));transform:translateX(-50%);
    align-items:center;gap:.35rem;padding:.3rem .45rem;color:#fff;
    border-radius:var(--r-pill);background:rgba(15,12,45,.78);
    opacity:.55;transition:opacity .2s}
body.pilns .pilnjosla:hover,body.pilns .pilnjosla:focus-within{opacity:1}
.pilnjosla button{font:inherit;line-height:1;border:0;cursor:pointer;
    color:#fff;background:transparent;border-radius:var(--r-pill);
    padding:.3rem .7rem;white-space:nowrap;transition:background .15s}
.pilnjosla button:hover{background:rgba(255,255,255,.18)}
.pilnjosla .nav{font-size:1.3rem;padding:.15rem .65rem}
.pilnjosla .cnt{font-size:.8rem;min-width:4.2rem;text-align:center;
    font-variant-numeric:tabular-nums}

/* Cik tālu stunda aizgājusi - plāna svītra augšmalā. Uz telefona tā ir
   vienīgā zīme, ka aiz malas vēl kaut kas ir, tāpēc tā ir vienmēr redzama. */
.pilnprog{display:none}
body.pilns .pilnprog{display:block;position:fixed;z-index:31;left:0;top:0;
    height:.2rem;width:0;background:var(--violet);transition:width .2s}

/* Pirmajā reizē pasaka, ko ar lenti darīt; pēc pāris sekundēm pazūd pati. */
.pilnmajiens{display:none}
body.pilns .pilnmajiens{display:block;position:fixed;z-index:30;left:50%;
    bottom:calc(4.4rem + env(safe-area-inset-bottom));
    transform:translateX(-50%);padding:.4rem .95rem;white-space:nowrap;
    border-radius:var(--r-pill);background:rgba(15,12,45,.8);color:#fff;
    font-size:.82rem;animation:pilnzud 4.5s forwards}
@keyframes pilnzud{0%,55%{opacity:.95}100%{opacity:0;visibility:hidden}}

/* Telefonā lente ir noklusētais skats, tāpēc vadība nav pieklusināta un
   pogas ir tik lielas, cik prasa īkšķis. */
@media (max-width:767px){
  body.pilns .pilnjosla{opacity:1;gap:.1rem;padding:.25rem .4rem;
      bottom:calc(.6rem + env(safe-area-inset-bottom))}
  body.pilns .pilnjosla .nav{font-size:1.6rem;padding:.4rem 1.2rem}
  body.pilns .pilnjosla button{padding:.5rem .85rem}
  body.pilns .pilnjosla .cnt{min-width:3.6rem}
  body.pilns header.galva,body.pilns .bl{padding:2rem 1.1rem 5rem}
}
"""

JS = """
(function(){
  /* Katrai daļai viens uzdevums: ekrāns (fullscreen API), stāvoklis (kura
     daļa ir priekšā) un attēlošana. Pogas un taustiņi sauc tos pašus
     darbus - atver, aizver, ej. */
  var lapa=document.querySelector(".lapa");
  var dalas=[].slice.call(
    document.querySelectorAll("header.galva,.saturs>.bl"));
  if(!lapa||dalas.length<2){return;}
  var cur=0,on=false;

  function e(tag,cls,txt){var n=document.createElement(tag);
    if(cls){n.className=cls;}if(txt!=null){n.textContent=txt;}return n;}
  function poga(cls,txt,zime){var b=e("button",cls,txt);b.type="button";
    b.addEventListener("click",zime);return b;}

  /* Telefons ir citāds tikai divās lietās: lente tur atveras pati, un
     pilnekrāna režīmu no pārlūka neprasa (to atļauj tikai pēc pieskāriena
     - un lentei tas nav vajadzīgs). */
  var telefons=!!(window.matchMedia&&
                  window.matchMedia("(max-width:767px)").matches);
  function atceras(k,v){try{localStorage.setItem(k,v);}catch(x){}}
  function atminas(k){try{return localStorage.getItem(k);}
    catch(x){return null;}}
  var SKATS="math-lente",MAJIENS="math-lente-majiens";

  /* --- josla lejā un poga augšā --- */
  var skaits=e("span","cnt","");
  var progress=e("div","pilnprog");
  document.body.appendChild(progress);
  var josla=e("div","pilnjosla");
  josla.appendChild(poga("nav","‹",function(){ej(cur-1);}));
  josla.appendChild(skaits);
  josla.appendChild(poga("nav","›",function(){ej(cur+1);}));
  josla.appendChild(poga("",telefons?"Visa lapa":"Esc",aizvert));
  document.body.appendChild(josla);

  var augsa=document.querySelector(".augsa");
  var pilnpoga=poga("pilnpoga",telefons?"Šķirstīt":"Pilnekrāns",function(){
    atvert(!telefons);
  });
  if(augsa){augsa.appendChild(pilnpoga);}

  /* --- ekrāns --- */
  var sakne=document.documentElement;
  function ekrana(){return document.fullscreenElement||
                           document.webkitFullscreenElement;}
  function prasit(){
    var f=sakne.requestFullscreen||sakne.webkitRequestFullscreen;
    if(f){try{var p=f.call(sakne);if(p&&p["catch"]){p["catch"](
      function(){});}}catch(x){}}
  }
  function atlaist(){
    var f=document.exitFullscreen||document.webkitExitFullscreen;
    if(ekrana()&&f){try{var p=f.call(document);
      if(p&&p["catch"]){p["catch"](function(){});}}catch(x){}}
  }

  /* --- stāvoklis --- */
  function zimet(){
    skaits.textContent=(cur+1)+" / "+dalas.length;
    progress.style.width=((cur+1)/dalas.length*100)+"%";
  }
  function ej(i){
    cur=i<0?0:(i>=dalas.length?dalas.length-1:i);
    lapa.scrollTo({left:cur*lapa.clientWidth,behavior:"smooth"});
    zimet();
  }
  function atvert(arEkranu){
    on=true;document.body.classList.add("pilns");
    if(arEkranu){prasit();}
    if(telefons){atceras(SKATS,"1");}
    /* Lente rodas tikai tagad, tāpēc vieta jāieņem pēc pārzīmēšanas. */
    setTimeout(function(){lapa.scrollLeft=cur*lapa.clientWidth;zimet();},0);
  }
  function aizvert(){
    on=false;document.body.classList.remove("pilns");atlaist();
    if(telefons){atceras(SKATS,"0");}
    if(dalas[cur]){dalas[cur].scrollIntoView({block:"start"});}
  }

  /* Telefonā lente ir noklusējums - bet tikai tik ilgi, kamēr students nav
     izvēlējies garo lapu. */
  if(telefons&&atminas(SKATS)!=="0"){
    atvert(false);
    if(atminas(MAJIENS)!=="1"){
      document.body.appendChild(e("div","pilnmajiens",
                                  "Velc uz sāniem →"));
      atceras(MAJIENS,"1");
    }
  }

  /* Pagriežot telefonu, lentes solis kļūst cits, tāpēc tā pati daļa
     jāpabīda no jauna zem malas. */
  window.addEventListener("resize",function(){
    if(on&&lapa.clientWidth){lapa.scrollLeft=cur*lapa.clientWidth;}
  });

  /* Ar pirkstu šķirot, kārtas numuru nolasa no lentes, nevis glabā
     atsevišķi - tā skaitītājs vienmēr runā par to, ko cilvēks redz.
     Nolasa tikai tad, kad lente apstājusies: citādi ar pogu sāktais
     slīdiens pa ceļam pārrakstītu tikko izvēlēto numuru. */
  var miers=null;
  lapa.addEventListener("scroll",function(){
    if(!on||!lapa.clientWidth){return;}
    if(miers){clearTimeout(miers);}
    miers=setTimeout(function(){
      var i=Math.round(lapa.scrollLeft/lapa.clientWidth);
      if(i!==cur&&i>=0&&i<dalas.length){cur=i;zimet();}
    },140);
  });

  /* Kamēr cilvēks raksta atbildi, taustiņi pieder laukam, nevis lentei:
     jauktā daļskaitlī «3 2/5» atstarpe ir daļa no atbildes. */
  function raksta(el){
    if(!el){return false;}
    if(el.isContentEditable){return true;}
    var t=(el.tagName||"").toUpperCase();
    return t==="INPUT"||t==="TEXTAREA"||t==="SELECT";
  }
  document.addEventListener("keydown",function(ev){
    if(!on||raksta(ev.target)){return;}
    var k=ev.key;
    if(k==="ArrowRight"||k===" "||k==="PageDown"){ej(cur+1);}
    else if(k==="ArrowLeft"||k==="PageUp"){ej(cur-1);}
    else if(k==="Home"){ej(0);}
    else if(k==="End"){ej(dalas.length-1);}
    else if(k==="Escape"){aizvert();}
    else{return;}
    ev.preventDefault();
  });
  /* Esc pilnekrānā pārtver pārlūks - tad jāsakārto pašiem. */
  function saskanot(){if(on&&!ekrana()){aizvert();}}
  document.addEventListener("fullscreenchange",saskanot);
  document.addEventListener("webkitfullscreenchange",saskanot);

  zimet();
})();
"""
