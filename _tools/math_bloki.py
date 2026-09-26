# -*- coding: utf-8 -*-
"""Matemātikas stundas lapas bloki - no kā stunda ir salikta.

Viena stunda ir bloku virkne: stāsts no dzīves, galvenā doma, spēle, kurā to
izmēģina, kopsavilkums un darbiņš mājās. Katrs bloka veids ir viena klase, un
tā zina trīs lietas par sevi - savu HTML, savu CSS un savu JavaScript (SRP).
Lapa (math_lapa.py) tos tikai saliek kopā un paņem katru CSS un JS gabalu
vienu reizi, arī tad, ja tāds bloks lapā ir vairākas reizes (DRY).

Jaunu bloka veidu pievieno, uzrakstot vēl vienu klasi ar CSS, JS un html();
stundu saturs (math_<klase>_<nr>.py) par noformējumu nezina neko.
"""

import html
import json

import math_ikonas
import mathhtml


def esc(s):
    """Teksts blokā: HTML aizsegts un matemātika uzzīmēta.

    Stundas saturā daļu raksta ar to pašu marķējumu, ko darba lapās -
    {3|4} un √(a + b) (rules_pd.txt) -, tāpēc virsrakstā, teikumā un
    uzdevumā daļa izskatās vienādi (DRY). Kas nav marķēts, paliek teksts.
    """
    return mathhtml.mat(s)


def teksts(s):
    """Tikai aizsegšana - tur, kur marķējumu nedrīkst tulkot."""
    return html.escape(s, quote=False)


def _atr(vertiba):
    """Dati blokam - JSON pēdiņās, drošs HTML atribūtā."""
    return html.escape(json.dumps(vertiba, ensure_ascii=False), quote=True)



def _saraksts(punkti):
    return ('<ul class="punkti">\n%s\n</ul>'
            % "\n".join("<li>%s</li>" % esc(p) for p in punkti))



# ===================================================================== pamats
class Bloks(object):
    """Bloka pamats: virsraksts un sava vieta lapā."""

    CSS = """
.bl{background:var(--surface);border-radius:var(--r);box-shadow:var(--sh);
    padding:1.1rem 1rem 1.2rem;margin:0 0 1rem}
.bl>h2{margin:0 0 .5rem;font-family:var(--font-h);font-weight:600;
    color:var(--primary);font-size:clamp(1.05rem,4.6vw,1.3rem)}
.bl p{margin:.45rem 0;font-size:clamp(1rem,4.2vw,1.12rem)}
.bl .punkti{list-style:none;margin:.5rem 0 0;padding:0;display:grid;gap:.5rem}
.bl .punkti li{position:relative;padding:.55rem .7rem .55rem 2.2rem;
    background:var(--bg);border-radius:var(--r-sm);
    font-size:clamp(.98rem,4vw,1.08rem)}
.bl .punkti li::before{content:"";position:absolute;left:.85rem;top:1.05em;
    width:.5rem;height:.5rem;margin-top:-.25rem;border-radius:50%;
    background:var(--cyan)}
.bl .zime{display:flex;gap:.8rem;flex-wrap:wrap;justify-content:center;
    margin:.8rem 0 .2rem;color:var(--violet)}
.bl .zime .ik{font-size:2.8rem}
"""
    JS = ""

    def __init__(self, virsraksts):
        self.virsraksts = virsraksts

    def fragmenti(self):
        """[(atslēga, CSS, JS), ...] - no katras mantojuma klases pa vienam.

        Bloks, kas sevī ietver citu bloku (Pasaule), šo papildina ar ietvertā
        bloka gabaliem, tāpēc lapa saņem visu, kas tai jāuzzīmē.
        """
        out = []
        for k in reversed(type(self).__mro__):
            if "CSS" in k.__dict__ or "JS" in k.__dict__:
                out.append((k.__name__, k.__dict__.get("CSS", ""),
                            k.__dict__.get("JS", "")))
        return out

    def galva(self):
        return "<h2>%s</h2>" % esc(self.virsraksts) if self.virsraksts else ""

    def kermenis(self):
        raise NotImplementedError

    def klase(self):
        """Bloka papildu CSS klase - pēc noklusējuma nav."""
        return ""

    def html(self):
        klase = self.klase()
        return ('<section class="bl%s">\n%s\n%s\n</section>'
                % (" " + klase if klase else "", self.galva(),
                   self.kermenis()))


# ============================================================== teksta bloki
class Sakums(Bloks):
    """Stundas sākums: viens jautājums, attēls un daži īsi fakti.

    Stundu nesāk ar rindkopām. Skolēns garu ievadu nelasa, un garā tekstā
    visvieglāk iezogas kļūda, tāpēc te teksta vietā ir attēls un daži fakti,
    katrs vienā rindā. Garumu ierobežo pati klase: ja fakts sanāk par garu
    vai to ir par daudz, stunda vienkārši neuzbūvējas.
    """

    MAX_FAKTI = 3
    FAKTA_GARUMS = 90

    CSS = """
.bl.sakums{background:linear-gradient(135deg,#EEF2FF,#F5F3FF);
    border:1px solid #DDD6FE;box-shadow:none}
.bl.sakums>h2{font-size:clamp(1.15rem,5.2vw,1.5rem);line-height:1.25}
.bl.sakums .fakti{list-style:none;margin:.7rem 0 0;padding:0;display:grid;
    gap:.45rem}
.bl.sakums .fakti li{padding:.55rem .75rem;background:#fff;
    border-radius:var(--r-sm);border:1px solid #DDD6FE;
    font-size:clamp(.95rem,3.9vw,1.05rem)}
.bl.sakums .paraksts{margin:.35rem 0 0;color:var(--dim);text-align:center;
    font-size:clamp(.85rem,3.5vw,.95rem)}
"""

    def __init__(self, virsraksts, zimejums=None, fakti=(), paraksts=None):
        Bloks.__init__(self, virsraksts)
        self.zimejums, self.paraksts = zimejums, paraksts
        self.fakti = list(fakti)
        if len(self.fakti) > self.MAX_FAKTI:
            raise AssertionError(
                "«%s»: sākumā drīkst būt līdz %d faktiem, tagad to ir %d"
                % (virsraksts, self.MAX_FAKTI, len(self.fakti)))
        for f in self.fakti:
            if len(f) > self.FAKTA_GARUMS:
                raise AssertionError(
                    "«%s»: fakts ir %d rakstzīmes, atļautas %d - «%s...»"
                    % (virsraksts, len(f), self.FAKTA_GARUMS, f[:40]))
        if not self.zimejums and not self.fakti:
            raise AssertionError("«%s»: sākumā vajag attēlu vai faktus"
                                 % virsraksts)

    def klase(self):
        return "sakums"

    def kermenis(self):
        gabali = []
        if self.zimejums:
            gabali.append(self.zimejums)
            if self.paraksts:
                gabali.append('<p class="paraksts">%s</p>'
                              % esc(self.paraksts))
        if self.fakti:
            gabali.append('<ul class="fakti">\n%s\n</ul>'
                          % "\n".join("<li>%s</li>" % esc(f)
                                      for f in self.fakti))
        return "\n".join(gabali)


class Doma(Bloks):
    """Galvenā doma vienā teikumā un soļi, kā to izdara."""

    CSS = """
.bl.doma{border-left:5px solid var(--violet)}
.bl.doma .liela{margin:.2rem 0 .6rem;font-family:var(--font-h);
    font-weight:600;color:var(--violet);line-height:1.35;
    font-size:clamp(1.12rem,5vw,1.42rem)}
.bl.doma ol{margin:.5rem 0 0;padding-left:1.4rem;display:grid;gap:.4rem}
.bl.doma ol li{font-size:clamp(.98rem,4vw,1.08rem)}
.bl.doma ol li::marker{color:var(--primary);font-weight:600}
"""

    def __init__(self, virsraksts, doma, soli=(), pieze=None):
        Bloks.__init__(self, virsraksts)
        self.doma, self.soli, self.pieze = doma, list(soli), pieze

    def klase(self):
        return "doma"

    def kermenis(self):
        gabali = ['<p class="liela">%s</p>' % esc(self.doma)]
        if self.soli:
            gabali.append("<ol>\n%s\n</ol>"
                          % "\n".join("<li>%s</li>" % esc(s)
                                      for s in self.soli))
        if self.pieze:
            gabali.append("<p>%s</p>" % esc(self.pieze))
        return "\n".join(gabali)


class Kopsavilkums(Bloks):
    """Ko es tagad protu - stundas beigās."""

    CSS = """
.bl.kopa{background:#ECFDF5;border:1px solid #A7F3D0;box-shadow:none}
.bl.kopa>h2{color:#047857}
.bl.kopa .punkti li{background:#fff}
.bl.kopa .punkti li::before{background:#047857}
"""

    def __init__(self, punkti, virsraksts="Tagad es protu"):
        Bloks.__init__(self, virsraksts)
        self.punkti = list(punkti)

    def klase(self):
        return "kopa"

    def kermenis(self):
        return _saraksts(self.punkti)


class Majas(Bloks):
    """Darbiņš ar īstām lietām ārpus stundas."""

    CSS = """
.bl.majas{background:#FFFBEB;border:1px solid #FDE68A;box-shadow:none}
.bl.majas>h2{color:var(--amber-ink)}
.bl.majas .punkti li{background:#fff}
.bl.majas .punkti li::before{background:var(--amber)}
"""

    def __init__(self, punkti, virsraksts="Pamēģini mājās", ievads=None):
        Bloks.__init__(self, virsraksts)
        self.punkti, self.ievads = list(punkti), ievads

    def klase(self):
        return "majas"

    def kermenis(self):
        sakums = "<p>%s</p>\n" % esc(self.ievads) if self.ievads else ""
        return sakums + _saraksts(self.punkti)


# ==================================================================== spēles
class Spele(Bloks):
    """Visu spēļu kopīgā daļa: laukums, vadības pogas un atbildes rinda.

    JavaScript te ir mazs dzinējs - tas zina, kā rādīt kārtas citu pēc citas
    un kā pateikt, vai sanāca. Katrs spēles veids pieliek tikai savu
    zīmēšanu, tāpēc pogas, atbildes un vārdu locīšana ir vienā vietā (DRY).
    """

    CSS = """
.speles{margin:.7rem 0 0}
.speles .virsa{display:flex;align-items:baseline;gap:.6rem;flex-wrap:wrap;
    padding:.6rem .8rem;border-radius:var(--r);background:var(--surface2)}
.speles .kart{flex:none;padding:.15rem .6rem;border-radius:var(--r-pill);
    background:var(--surface);color:var(--primary);font-weight:600;
    font-size:.82rem}
.speles .jaut{flex:1 1 12rem;margin:0;color:var(--primary);font-weight:600;
    font-size:clamp(1rem,4.3vw,1.15rem)}
.speles .laukums{margin:.7rem 0}
.speles .kzim{margin:0 0 .6rem}
/* Atbildes rinda ar lodziņu - to lieto gan Ievadi, gan Kustiba, tāpēc tā ir
   dzinējā, nevis vienā uzdevuma veidā (DRY). */
.speles .ie-rinda{display:flex;gap:.5rem;flex-wrap:wrap;align-items:center;
    margin:.8rem 0 0}
.speles .ie-rinda input{flex:1 1 8rem;min-width:7rem;font:inherit;
    padding:.7rem .9rem;min-height:2.9rem;border-radius:var(--r);
    border:2px solid var(--line);background:var(--surface);color:var(--fg);
    font-size:clamp(1rem,4.3vw,1.15rem)}
.speles .ie-rinda input:focus{outline:0;border-color:var(--violet)}
.speles .ie-rinda input.labi{border-color:#047857;background:#DCFCE7}
.speles .ie-rinda input.nepareizi{border-color:#FCA5A5;background:#FEF2F2}
.speles .vadiba{display:flex;gap:.5rem;flex-wrap:wrap;margin:.6rem 0 0}
.speles .atb{margin:.6rem 0 0;min-height:1.5rem;font-weight:600;
    font-size:clamp(.98rem,4vw,1.08rem)}
.speles .atb.labi{color:#047857}
.speles .atb.vel{color:var(--amber-ink)}
.speles .gals{margin:.2rem 0;color:#047857;font-weight:600}

.speles button{font:inherit;cursor:pointer;border-radius:var(--r-pill);
    border:1px solid var(--line);background:var(--surface);color:var(--fg);
    padding:.7rem 1.1rem;min-height:2.9rem;font-weight:500;
    font-size:clamp(.95rem,4vw,1.05rem);transition:background .15s}
.speles button:hover{background:var(--surface2)}
.speles button:disabled{opacity:.4;cursor:default}
.speles button:disabled:hover{background:var(--surface)}
.speles button.galvena,.speles button.talak{background:var(--primary);
    border-color:var(--primary);color:#fff}
.speles button.galvena:hover,.speles button.talak:hover{
    background:var(--violet);border-color:var(--violet)}

.speles .mantas{display:flex;flex-wrap:wrap;gap:.5rem;justify-content:center}
.speles .manta{position:relative;display:inline-flex;align-items:center;
    justify-content:center;width:4rem;height:4rem;padding:0;
    border-radius:var(--r);border:2px solid var(--line);
    background:var(--surface);color:var(--primary)}
.speles .manta .ik{font-size:2.4rem}
.speles .manta.ok{background:#DCFCE7;border-color:#047857;color:#047857}
.speles .manta .nr{position:absolute;right:.15rem;top:.05rem;
    font-style:normal;font-weight:700;font-size:.85rem;color:#047857}
.speles .manta.klusi{cursor:default}

/* Laika vērtējums (MSP.tempo): cik ātri atrisināts pret mērķa laiku. */
.speles .tempo{margin:.6rem 0 0;padding:.6rem .8rem .5rem;
    border-radius:var(--r);background:var(--surface2);animation:tempo-in .35s}
.speles .tempo-r{display:flex;align-items:baseline;gap:.55rem;flex-wrap:wrap}
.speles .tempo-r b{font-family:var(--font-h);font-weight:600;
    font-size:clamp(1.25rem,5.5vw,1.5rem);color:var(--primary)}
.speles .tempo-r span{font-weight:600;font-size:clamp(.92rem,3.8vw,1.02rem)}
.speles .tempo-j{position:relative;height:.5rem;margin:.45rem 0 1.1rem;
    border-radius:1rem;background:#fff}
.speles .tempo-j i{position:absolute;left:0;top:0;bottom:0;border-radius:1rem;
    background:var(--violet);animation:tempo-aug .8s ease-out}
.speles .tempo-j em{position:absolute;left:50%;top:-.25rem;bottom:-.25rem;
    width:2px;background:var(--fg)}
.speles .tempo-j small{position:absolute;left:50%;top:.75rem;
    transform:translateX(-50%);white-space:nowrap;color:var(--dim);
    font-size:.75rem}
.speles .tempo.zibens{background:linear-gradient(135deg,#EDE9FE,#CFFAFE)}
.speles .tempo.zibens .tempo-r span{color:var(--violet)}
.speles .tempo.atri{background:#DCFCE7}
.speles .tempo.atri .tempo-r span{color:#047857}
.speles .tempo.atri .tempo-j i{background:#10B981}
.speles .tempo.labi{background:#E0F2FE}
.speles .tempo.labi .tempo-r span{color:#0369A1}
.speles .tempo.labi .tempo-j i{background:#0EA5E9}
.speles .tempo.treni{background:#FEF3C7}
.speles .tempo.treni .tempo-r span{color:var(--amber-ink)}
.speles .tempo.treni .tempo-j i{background:var(--amber)}
@keyframes tempo-aug{from{width:0}}
@keyframes tempo-in{from{opacity:0;transform:translateY(6px)}}
@media (prefers-reduced-motion:reduce){
  .speles .tempo,.speles .tempo-j i{animation:none}
}
"""

    JS = """
window.MSP=(function(){
  var IK=window.MATH_IKONAS||{},FORMAS=window.MATH_VARDI||{};
  var VARDI=["nulle","viens","divi","trīs","četri","pieci","seši",
             "septiņi","astoņi","deviņi","desmit"];
  function e(t,c,x){var n=document.createElement(t);
    if(c){n.className=c;}if(x!=null){n.textContent=x;}return n;}
  function poga(c,x){var b=e("button",c,x);b.type="button";return b;}
  function ikona(v){var s=e("span","ik");s.innerHTML=IK[v]||"";return s;}
  function formas(k){return k.vardi||FORMAS[k.ikona]||null;}
  /* Latviski skaits maina vārdu: 1 logs, 2 logi, 0 logu. */
  function skaitlis(n,v){
    if(!v){return ""+n;}
    if(n===0){return n+" "+v[2];}
    if(n%10===1&&n%100!==11){return n+" "+v[0];}
    return n+" "+v[1];
  }
  function vards(n){return VARDI[n]||(""+n);}
  /* Latviski decimāldaļu atdala komats, arī tad, kad skaitli raksta JS. */
  function cip(n){
    var t=Math.round(n*1e6)/1e6;
    return (""+t).replace(".",",");
  }
  /* Atbildi salīdzina bez atstarpēm, punkts der komata vietā, un
     tastatūras «-» ir tas pats mīnuss, ko grāmatā raksta «−». Pakāpe
     a⁵, a^5 un a^{5} ir viena un tā pati atbilde - telefonā augšraksta
     nav, tāpēc katrs to raksta, kā prot. Visi uzdevumi, kur atbildi
     raksta, salīdzina ar šo pašu funkciju. */
  function tirs(s){
    return (s==null?"":""+s).toLowerCase().replace(/\\s+/g,"")
           .replace(/\\./g,",").replace(/\\u2212/g,"-")
           .replace(/\\^\\{([^{}]*)\\}/g,"^$1").replace(/[⁰¹²³⁴⁵⁶⁷⁸⁹⁻]+/g,
             function(p){return "^"+p.replace(/./g,function(c){
               return "0123456789-".charAt("⁰¹²³⁴⁵⁶⁷⁸⁹⁻".indexOf(c));});});
  }
  /* Laika vērtējums: sekundes pret uzdevuma mērķa laiku. Mērķis ir
     aptuvens laiks, kurā šāda veida uzdevumu atrisina, tāpēc teikums
     uzslavē ātru darbu un lēnāku mudina trenēties, nevis bāra. Joslā mērķis
     stāv pa vidu - pa kreisi no tā ir ātrāk. Atgriež {el, limenis}:
     0 - zibens (≤ puse mērķa), 1 - ātrāk, 2 - līdz divreiz, 3 - lēnāk. */
  var TEMPO=[["zibens","Zibens! Divreiz ātrāk par mērķa laiku."],
             ["atri","Super! Ātrāk par mērķa laiku."],
             ["labi","Labs darbs! Mērķa laiks jau pavisam tuvu."],
             ["treni","Izdevās! Ar katru reizi sanāks ātrāk."]];
  function tempo(sek,merkis){
    var r=sek/merkis,lim=r<=0.5?0:r<=1?1:r<=2?2:3,T=TEMPO[lim];
    var el=e("div","tempo "+T[0]),rinda=e("div","tempo-r"),
        j=e("div","tempo-j"),f=e("i");
    rinda.appendChild(e("b","",Math.max(1,Math.round(sek))+" s"));
    rinda.appendChild(e("span","",T[1]));
    f.style.width=Math.min(100,r*50)+"%";
    j.appendChild(f);j.appendChild(e("em"));
    j.appendChild(e("small","","mērķis "+merkis+" s"));
    el.appendChild(rinda);el.appendChild(j);
    return {el:el,limenis:lim};
  }
  function dati(el,k){try{return JSON.parse(el.getAttribute(k));}
    catch(x){return null;}}
  function manta(k,klikskis){
    var b=klikskis?poga("manta"):e("span","manta klusi");
    b.appendChild(ikona(k.ikona));
    if(klikskis){
      var nr=e("i","nr","");
      b.appendChild(nr);
      b.addEventListener("click",function(){klikskis(b,nr);});
    }
    return b;
  }
  function mantas(k,klikskis){
    var g=e("div","mantas"),i;
    for(i=0;i<k.skaits;i++){g.appendChild(manta(k,klikskis));}
    return g;
  }
  /* Kārtu dzinējs: viena kārta uz ekrāna, tad nākamā. Obligātās kārtas ir
     pirmās «data-pamats»; pārējās izsniedz pa divām, kad lūdz vēl. */
  function kartas(root,zime,gala){
    var visas=dati(root,"data-kartas")||[],i=0;
    var pamats=parseInt(root.getAttribute("data-pamats")||"0",10)||
               visas.length;
    var redz=Math.min(pamats,visas.length);
    var virsa=e("div","virsa"),kart=e("span","kart"),jaut=e("p","jaut");
    var laukums=e("div","laukums"),vadiba=e("div","vadiba"),atb=e("p","atb");
    virsa.appendChild(kart);virsa.appendChild(jaut);
    root.appendChild(virsa);root.appendChild(laukums);
    root.appendChild(vadiba);root.appendChild(atb);
    var talak=poga("talak","Nākamais");
    talak.addEventListener("click",function(){i++;radi();});
    var vel=poga("talak","Vēl divi uzdevumi");
    vel.addEventListener("click",function(){
      redz=Math.min(redz+2,visas.length);i++;radi();
    });
    function saki(teksts,labi){
      /* Atbildē mēdz būt daļa, tāpēc te liek gatavu HTML, nevis tekstu. */
      atb.innerHTML=teksts;atb.className="atb "+(labi?"labi":"vel");
    }
    function gatavs(teksts){
      /* Kad kārta atrisināta, atbilde nāk pirms pogas - vispirms izlasa,
         ko izdarīja, tikai tad iet tālāk. */
      saki(teksts,true);root.insertBefore(atb,vadiba);vadiba.innerHTML="";
      if(i+1<redz){vadiba.appendChild(talak);return;}
      vadiba.appendChild(e("p","gals",gala||"Viss izdarīts!"));
      if(redz<visas.length){vadiba.appendChild(vel);}
    }
    function radi(){
      var k=visas[i];
      kart.textContent=(i+1)+". no "+redz;
      jaut.innerHTML=k.jaut||"";
      laukums.innerHTML="";vadiba.innerHTML="";
      root.appendChild(atb);atb.textContent="";atb.className="atb";
      if(k.zim){
        var z=e("div","kzim");z.innerHTML=k.zim;laukums.appendChild(z);
      }
      zime(k,{laukums:laukums,vadiba:vadiba,gatavs:gatavs,saki:saki});
    }
    if(visas.length){radi();}
  }
  var veidi={};
  function sakt(){
    var els=document.querySelectorAll("[data-veids]"),i,f;
    for(i=0;i<els.length;i++){
      f=veidi[els[i].getAttribute("data-veids")];
      if(f){f(els[i]);}
    }
  }
  if(document.readyState==="loading"){
    document.addEventListener("DOMContentLoaded",sakt);
  }else{setTimeout(sakt,0);}
  return {e:e,poga:poga,ikona:ikona,formas:formas,skaitlis:skaitlis,
          vards:vards,cip:cip,tirs:tirs,tempo:tempo,dati:dati,manta:manta,mantas:mantas,
          kartas:kartas,veidi:veidi};
})();
"""

    def __init__(self, virsraksts, ievads=None):
        Bloks.__init__(self, virsraksts)
        self.ievads = ievads

    def veids(self):
        raise NotImplementedError

    def atributi(self):
        return {}

    def kermenis(self):
        atr = "".join(' %s="%s"' % (k, v)
                      for k, v in sorted(self.atributi().items()))
        sakums = "<p>%s</p>\n" % esc(self.ievads) if self.ievads else ""
        return ('%s<div class="speles" data-veids="%s"%s></div>'
                % (sakums, self.veids(), atr))


class _Kartas(Spele):
    """Spēle, kas sastāv no vairākām vienādi uzbūvētām kārtām.

    «pamats» pasaka, cik kārtas izdara visi; pārējās lapa piedāvā pa divām,
    kad skolēns spiež «Vēl divi uzdevumi». Tā ātrākajam ir ko darīt, bet
    stundas garums nemainās.

    Kuros kārtas laukos ir matemātika, pasaka MATEMATIKA: tos uzzīmē jau
    būvējot, tāpēc lapai nav jāzina marķējums un {3|4} nekad neparādās
    ekrānā kā teksts.
    """

    MATEMATIKA = ("jaut",)

    def __init__(self, virsraksts, kartas, pamats=None, ievads=None):
        Spele.__init__(self, virsraksts, ievads)
        self.kartas = list(kartas)
        self.pamats = pamats or len(self.kartas)
        self.parbaudi_kartas()
        if not 0 < self.pamats <= len(self.kartas):
            raise AssertionError("«%s»: pamatā %d kārtas no %d"
                                 % (virsraksts, self.pamats,
                                    len(self.kartas)))
        if (len(self.kartas) - self.pamats) % 2:
            raise AssertionError(
                "«%s»: papildu kārtas jādod pa pāriem, tagad to ir %d"
                % (virsraksts, len(self.kartas) - self.pamats))

    def parbaudi_kartas(self):
        """Ko katrai kārtai vajag - pasaka pats spēles veids."""

    def _zimeta(self, karta):
        """Kārta ar uzzīmētu matemātiku - to saņem lapa."""
        out = dict(karta)
        for lauks in self.MATEMATIKA:
            if lauks not in out:
                continue
            if isinstance(out[lauks], (list, tuple)):
                out[lauks] = [esc(x) for x in out[lauks]]
            else:
                out[lauks] = esc(out[lauks])
        return out

    def atributi(self):
        atr = {"data-kartas": _atr([self._zimeta(k) for k in self.kartas])}
        if self.pamats < len(self.kartas):
            atr["data-pamats"] = str(self.pamats)
        return atr


class _Mantas(_Kartas):
    """Kārtas, kurās skaita zīmētus priekšmetus (1.-2. klase)."""

    def parbaudi_kartas(self):
        for k in self.kartas:
            math_ikonas.svg(k["ikona"])        # nepareizs vārds - uzreiz kļūda


class Skaiti(_Mantas):
    """Pieskaries katrai lietai pēc kārtas - skaitītājs rāda, cik jau ir."""

    CSS = """
.speles .skaititajs{display:flex;align-items:baseline;gap:.6rem;
    justify-content:center;margin:0 0 .7rem}
.speles .skaititajs .c{font-family:var(--font-h);font-weight:600;
    color:var(--primary);line-height:1;font-size:clamp(2.6rem,14vw,3.6rem)}
.speles .skaititajs .v{color:var(--dim);font-size:clamp(1rem,4.4vw,1.2rem)}
"""

    JS = """
MSP.veidi.skaiti=function(root){
  MSP.kartas(root,function(k,c){
    var n=0;
    var sk=MSP.e("div","skaititajs"),cip=MSP.e("b","c","0"),
        vrd=MSP.e("span","v","sāc skaitīt");
    sk.appendChild(cip);sk.appendChild(vrd);
    c.laukums.appendChild(sk);
    c.laukums.appendChild(MSP.mantas(k,function(b,nr){
      if(b.className.indexOf("ok")>=0){
        c.saki("Šo jau saskaitīji. Katru skaita tikai vienu reizi!",false);
        return;
      }
      b.className="manta ok";n++;
      cip.textContent=n;vrd.textContent=MSP.vards(n);nr.textContent=n;
      if(n===k.skaits){
        c.gatavs("Pēdējais skaitlis ir "+n+". Kopā ir "
                 +MSP.skaitlis(n,MSP.formas(k))+".");
      }
    }));
  },"Tu proti saskaitīt un pateikt, cik ir kopā!");
};
"""

    def veids(self):
        return "skaiti"


class Modelis(_Mantas):
    """Noliec tik pat ripiņu, cik ir lietu - skaitlis kļūst par modeli."""

    CSS = """
.speles .paplate{display:flex;flex-wrap:wrap;gap:.45rem;
    justify-content:center;min-height:4rem;align-items:center;
    margin:.7rem 0 0;padding:.7rem;border:2px dashed var(--violet);
    border-radius:var(--r) var(--r) 0 0;border-bottom:0;
    background:var(--surface2);color:var(--violet)}
.speles .paplate .ik{font-size:2rem}
.speles .paplate .tukss{color:var(--violet);font-size:.95rem;font-weight:500}
/* Pogas «Noliec ripiņu» vieta ir pie pašas paplātes, nevis lapas lejā:
   bērnam jāredz, kur ripiņa parādīsies, kad viņš spiedīs. */
.speles .liekam{display:flex;gap:.5rem;justify-content:center;
    flex-wrap:wrap;margin:0 0 .3rem;padding:.6rem;
    border:2px dashed var(--violet);border-top:0;
    border-radius:0 0 var(--r) var(--r);background:var(--surface2)}
.speles button.liek{background:var(--violet);border-color:var(--violet);
    color:#fff;font-weight:600}
.speles button.liek:hover{background:var(--primary);
    border-color:var(--primary)}
.speles .cik{margin:.2rem 0 0;text-align:center;color:var(--dim);
    font-size:.95rem}
"""

    JS = """
MSP.veidi.modelis=function(root){
  MSP.kartas(root,function(k,c){
    var n=0,ripa=MSP.formas({ikona:"ripina"});
    c.laukums.appendChild(MSP.mantas(k,null));
    /* Paplāte un abas pogas ir viens rāmis: poga stāv tieši zem vietas,
       kur ripiņa parādīsies. */
    var paplate=MSP.e("div","paplate"),liekam=MSP.e("div","liekam"),
        cik=MSP.e("p","cik","");
    var liek=MSP.poga("liek","+ Noliec ripiņu"),
        nonem=MSP.poga("","− Noņem ripiņu"),
        parbaudit=MSP.poga("galvena","Pārbaudīt");
    liekam.appendChild(liek);liekam.appendChild(nonem);
    c.laukums.appendChild(paplate);c.laukums.appendChild(liekam);
    c.laukums.appendChild(cik);
    function zimet(){
      paplate.innerHTML="";
      if(n===0){
        paplate.appendChild(MSP.e("span","tukss",
          "Spied «Noliec ripiņu» - ripiņa nāks šeit"));
      }
      for(var i=0;i<n;i++){paplate.appendChild(MSP.ikona("ripina"));}
      cik.textContent="Paplātē: "+MSP.skaitlis(n,ripa);
      nonem.disabled=n===0;
    }
    /* Arī pati paplāte pieņem pieskārienu - bērnam tā ir tā pati kustība. */
    paplate.addEventListener("click",function(){if(n<12){n++;zimet();}});
    liek.addEventListener("click",function(){if(n<12){n++;zimet();}});
    nonem.addEventListener("click",function(){if(n>0){n--;zimet();}});
    parbaudit.addEventListener("click",function(){
      if(n===k.skaits){
        c.gatavs("Tieši tik pat: "+MSP.skaitlis(k.skaits,MSP.formas(k))
                 +" un "+MSP.skaitlis(n,ripa)+".");
      }else if(n<k.skaits){
        c.saki("Ripiņu ir par maz. Spied «Noliec ripiņu» vēl vienu reizi!",
               false);
      }else{
        c.saki("Ripiņu ir par daudz. Noņem vienu!",false);
      }
    });
    c.vadiba.appendChild(parbaudit);
    zimet();
  },"Tu proti parādīt skaitli ar ripiņām!");
};
"""

    def veids(self):
        return "modelis"


class Izvele(_Mantas):
    """Cik ir? - saskaita pats un izvēlas pareizo skaitli."""

    CSS = """
.speles .cipari{display:grid;gap:.45rem;width:100%;
    grid-template-columns:repeat(5,1fr)}
.speles .cipars{padding:.6rem .2rem;min-height:3.1rem;
    font-family:var(--font-h);font-weight:600;
    font-size:clamp(1.15rem,5.5vw,1.4rem);color:var(--primary)}
.speles .cipars.labi{background:#DCFCE7;border-color:#047857;color:#047857}
.speles .cipars.nepareizi{background:#FEF2F2;border-color:#FCA5A5;
    color:#B91C1C}
@media (min-width:600px){
  .speles .cipari{grid-template-columns:repeat(10,1fr)}
}
"""

    JS = """
MSP.veidi.izvele=function(root){
  var lidz=parseInt(root.getAttribute("data-lidz")||"10",10);
  MSP.kartas(root,function(k,c){
    c.laukums.appendChild(MSP.mantas(k,null));
    var cipari=MSP.e("div","cipari");
    for(var i=1;i<=lidz;i++){
      (function(i){
        var b=MSP.poga("cipars",""+i);
        b.addEventListener("click",function(){
          if(i===k.skaits){
            b.className="cipars labi";
            c.gatavs("Pareizi! Ir "+MSP.skaitlis(k.skaits,MSP.formas(k))+".");
          }else{
            b.className="cipars nepareizi";
            c.saki("Vēl ne. Rādi ar pirkstu un skaiti skaļi!",false);
          }
        });
        cipari.appendChild(b);
      })(i);
    }
    c.vadiba.appendChild(cipari);
  },"Tu proti pateikt, cik ir!");
};
"""

    def __init__(self, virsraksts, kartas, pamats=None, lidz=10,
                 ievads=None):
        _Mantas.__init__(self, virsraksts, kartas, pamats, ievads)
        self.lidz = lidz

    def veids(self):
        return "izvele"

    def atributi(self):
        atr = _Mantas.atributi(self)
        atr["data-lidz"] = str(self.lidz)
        return atr


class Josla(Spele):
    """Skaitļu josla: pieskaries skaitlim un redzi, cik daudz tas ir."""

    CSS = """
.speles .josla{display:grid;gap:.4rem;grid-template-columns:repeat(6,1fr)}
.speles .js{padding:.55rem .2rem;min-height:2.9rem;font-family:var(--font-h);
    font-weight:600;font-size:clamp(1.05rem,5vw,1.3rem);color:var(--primary)}
.speles .js.izvelets{background:var(--primary);border-color:var(--primary);
    color:#fff}
@media (min-width:600px){
  .speles .josla{grid-template-columns:repeat(11,1fr)}
}
"""

    JS = """
MSP.veidi.josla=function(root){
  var lidz=parseInt(root.getAttribute("data-lidz")||"10",10);
  var josla=MSP.e("div","josla"),paplate=MSP.e("div","paplate"),
      atb=MSP.e("p","atb"),pogas=[],i;
  function radi(n){
    for(var j=0;j<pogas.length;j++){pogas[j].className="js";}
    pogas[n].className="js izvelets";
    paplate.innerHTML="";
    if(n===0){
      paplate.appendChild(MSP.e("span","tukss","Nulle – nevienas ripiņas"));
    }
    for(var q=0;q<n;q++){paplate.appendChild(MSP.ikona("ripina"));}
    atb.textContent=n+" – "+MSP.vards(n);
    atb.className="atb labi";
  }
  for(i=0;i<=lidz;i++){
    (function(i){
      var b=MSP.poga("js",""+i);
      b.addEventListener("click",function(){radi(i);});
      pogas.push(b);josla.appendChild(b);
    })(i);
  }
  root.appendChild(josla);root.appendChild(paplate);root.appendChild(atb);
  radi(0);
};
"""

    def __init__(self, virsraksts, lidz=10, ievads=None):
        Spele.__init__(self, virsraksts, ievads)
        self.lidz = lidz

    def veids(self):
        return "josla"

    def atributi(self):
        return {"data-lidz": str(self.lidz)}
