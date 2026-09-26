# -*- coding: utf-8 -*-
"""Bloki, kuros ar matemātiku kaut kas *notiek* uz ekrāna.

math_bloki.py ir stundas pamats, math_uzdevumi.py - uzdevumi ar atbildi; te
ir tas trešais veids, ko prasa rules_matematika.txt: skolēns izrēķina skaitli
un tad redz, kas ar to notiek (SRP).

    Kustiba - kustīgs objekts uz trases. Ieraksti skaitli, spied «Palaist»,
              un objekts aizbrauc tieši tik tālu; ja aprēķins bija pareizs,
              tas apstājas pie mērķa karodziņa.
    Simulacija - nejaušs eksperiments: simts metienu vienā pieskārienā
              un relatīvais biežums, kas tuvojas varbūtībai.
    Slidnis  - vizualizācija pa soļiem. Katrs soļa stāvoklis
              ir sagatavots jau būvējot, tāpēc lapā nav ne formulu, ne
              rēķināšanas - tikai iepriekš uzzīmēti stāvokļi (DRY).

Abi lieto to pašu spēļu dzinēju un tās pašas pogas, kas visi pārējie
uzdevumi; te ir tikai tas, ar ko šie divi atšķiras.
"""

from math_bloki import Bloks, Spele, _Kartas, _atr, esc


class Kustiba(_Kartas):
    """Kustīgs objekts: izrēķini, cik tālu tam jāaizbrauc, un palaid.

    Kārtas lauki:
        jaut    - jautājums;
        atb     - pareizais skaitlis (tas pats, kas objekta apstāšanās vieta);
        beigas  - trases skalas gals; sakums pēc noklusējuma ir 0;
        mers    - mērvienība, ko raksta pie skalas;
        iedala  - cik liels solis starp skalas iedaļām;
        merkis  - uzraksts pie mērķa karodziņa;
        objekts - kas brauc (viens vārds: «Rovers», «Kuģis», «Lifts»);
        padoms  - ko pateikt, ja objekts apstājas garām.

    Objekts aizbrauc tieši tur, kur skolēns pateica, arī tad, ja tas ir
    nepareizi - tieši tāpēc kļūdu ir *redzams*, nevis tikai pateikts.
    """

    MATEMATIKA = ("jaut", "padoms", "stasts")

    CSS = """
.speles .kust{margin:.7rem 0 0}
.speles .kust-stasts{margin:0 0 .5rem;color:var(--dim);
    font-size:clamp(.88rem,3.6vw,.98rem)}
.speles .kust-trase{position:relative;height:4.3rem;border-radius:var(--r);
    background:linear-gradient(180deg,#EEF2FF,#E0E7FF);
    border:1px solid #C7D2FE;overflow:hidden}
.speles .kust-celjs{position:absolute;left:0;right:0;bottom:1.15rem;
    height:.32rem;background:repeating-linear-gradient(90deg,
    var(--violet) 0 .55rem,transparent .55rem 1.1rem);opacity:.45}
.speles .kust-merkis{position:absolute;bottom:1.1rem;width:0;
    border-left:2px dashed var(--amber-ink);height:2.6rem}
.speles .kust-merkis b{position:absolute;left:.25rem;top:-.15rem;
    white-space:nowrap;color:var(--amber-ink);font-size:.74rem;
    font-weight:700}
.speles .kust-obj{position:absolute;bottom:1.05rem;left:0;
    transform:translateX(-50%);transition:left 1s cubic-bezier(.3,.1,.2,1);
    display:flex;flex-direction:column;align-items:center;
    color:var(--primary)}
.speles .kust-obj i{display:block;width:1.5rem;height:1.5rem;
    border-radius:50%;background:var(--primary);
    box-shadow:0 0 0 .3rem rgba(79,70,229,.18)}
.speles .kust-obj b{font-size:.72rem;font-weight:700;white-space:nowrap}
.speles .kust-skala{position:relative;height:1.5rem;margin:.2rem 0 0}
.speles .kust-skala span{position:absolute;transform:translateX(-50%);
    color:var(--dim);font-size:.72rem}
.speles .kust-mers{margin:.1rem 0 0;text-align:right;color:var(--dim);
    font-size:.78rem}
"""

    JS = """
MSP.veidi.kustiba=function(root){
  MSP.kartas(root,function(k,c){
    var sak=k.sak,beig=k.beig;
    /* Skala neaizņem visu platumu: malās paliek vieta objekta uzrakstam,
       lai tas neaizietu aiz trases malas. */
    function vieta(v){return 5+(v-sak)/(beig-sak)*90;}
    var kust=MSP.e("div","kust");
    if(k.stasts){kust.appendChild(MSP.e("div","kust-stasts")).innerHTML=
      k.stasts;}
    var trase=MSP.e("div","kust-trase");
    trase.appendChild(MSP.e("div","kust-celjs"));
    var merkis=MSP.e("div","kust-merkis");
    merkis.style.left=vieta(k.atb)+"%";
    merkis.appendChild(MSP.e("b",null,k.merkis||"mērķis"));
    trase.appendChild(merkis);
    var obj=MSP.e("div","kust-obj");
    obj.appendChild(MSP.e("i"));
    obj.appendChild(MSP.e("b",null,k.objekts||"objekts"));
    trase.appendChild(obj);
    kust.appendChild(trase);
    var skala=MSP.e("div","kust-skala"),v;
    for(v=sak;v<=beig+1e-9;v+=k.iedala){
      var s=MSP.e("span",null,MSP.cip(v));
      s.style.left=vieta(v)+"%";skala.appendChild(s);
    }
    kust.appendChild(skala);
    if(k.mers){kust.appendChild(MSP.e("p","kust-mers",k.mers));}
    c.laukums.appendChild(kust);

    var rinda=MSP.e("div","ie-rinda");
    var lauks=document.createElement("input");
    lauks.type="text";lauks.setAttribute("inputmode","decimal");
    lauks.setAttribute("aria-label","Cik tālu");
    lauks.placeholder=k.vieta||("skaitlis "+(k.mers||""));
    var palaist=MSP.poga("galvena","Palaist");
    rinda.appendChild(lauks);rinda.appendChild(palaist);
    c.laukums.appendChild(rinda);

    function braukt(){
      var t=(lauks.value||"").replace(/\\s+/g,"").replace(/,/g,".");
      var v=parseFloat(t);
      if(!t||isNaN(v)){c.saki("Ieraksti skaitli un spied «Palaist».",false);
        return;}
      var p=vieta(v);
      obj.style.left=Math.max(2,Math.min(98,p))+"%";
      if(Math.abs(v-k.atb)<1e-9){
        lauks.readOnly=true;lauks.className="labi";
        c.gatavs(k.labi||("Tieši mērķī: "+MSP.cip(k.atb)+
                 (k.mers?" "+k.mers:"")+"."));
      }else{
        lauks.className="nepareizi";
        var kur=v<k.atb?"neaizbrauca līdz mērķim":"aizbrauca garām mērķim";
        c.saki("Objekts "+kur+". "+(k.padoms||"Pārrēķini vēlreiz."),false);
      }
    }
    palaist.addEventListener("click",braukt);
    lauks.addEventListener("keydown",function(ev){
      if(ev.key==="Enter"){ev.preventDefault();braukt();}
    });
  },"Tavi aprēķini objektu aizveda tieši mērķī!");
};
"""

    def parbaudi_kartas(self):
        for k in self.kartas:
            if "atb" not in k:
                raise AssertionError("«%s»: kārtai «%s» nav atbildes"
                                     % (self.virsraksts, k.get("jaut")))
            sak = k.get("sakums", 0)
            if not sak <= k["atb"] <= k["beigas"]:
                raise AssertionError(
                    "«%s»: atbilde %s neietilpst skalā %s..%s"
                    % (self.virsraksts, k["atb"], sak, k["beigas"]))

    def _zimeta(self, karta):
        """Skalas robežas lapai padod ar īsiem vārdiem - tā JS nav jālocās."""
        out = _Kartas._zimeta(self, karta)
        out["sak"] = karta.get("sakums", 0)
        out["beig"] = karta["beigas"]
        out["iedala"] = karta.get("iedala",
                                  (out["beig"] - out["sak"]) / 10.0)
        for lauks in ("sakums", "beigas"):
            out.pop(lauks, None)
        return out

    def veids(self):
        return "kustiba"


class Slidnis(Spele):
    """Vizualizācija pa soļiem: spied nākamo soli un skaties, kas mainās.

    Katrs rādītāja stāvoklis ir sagatavots jau būvējot - teksts, josla un, ja
    vajag, zīmējums. Lapa neko nerēķina, tāpēc te nevar iezagties kļūda, un
    tas pats bloks der gan procentiem, gan tilpumam, gan punktam plaknē.

    Soļa lauki: v (soļa uzraksts), teksts, josla (0-100), zim (SVG).
    """

    CSS = """
.speles .sl{margin:.7rem 0 0;padding:.9rem;border-radius:var(--r);
    background:var(--surface2)}
.speles .sl-zim{margin:0 0 .4rem}
.speles .sl-v{margin:0;text-align:center;font-family:var(--font-h);
    font-weight:600;color:var(--violet);line-height:1.2;
    font-size:clamp(1.3rem,6vw,1.7rem)}
.speles .sl-teksts{margin:.35rem 0 0;text-align:center;color:var(--fg);
    font-size:clamp(1rem,4.2vw,1.12rem)}
.speles .sl-josla{height:1.1rem;margin:.6rem 0 .2rem;border-radius:var(--r-sm);
    background:var(--surface);border:1px solid var(--line);overflow:hidden}
.speles .sl-josla i{display:block;height:100%;width:0;background:var(--violet);
    transition:width .25s}
/* Rādītāju stumj ar pogām, nevis velk: velkot pirmais gabaliņš neko
   nemainīja, un bija jāuzmin, ka vispār drīkst vilkt. Viens pieskāriens -
   viens solis, un visi soļi ir redzami uzreiz. */
.speles .sl-vad{display:flex;align-items:center;gap:.4rem;margin:.75rem 0 0}
.speles .sl-vad button{min-height:2.8rem;padding:0 .4rem;
    border:1px solid var(--line);border-radius:var(--r-sm);
    background:var(--surface);color:var(--primary);font:inherit;
    font-weight:700;line-height:1;cursor:pointer;
    transition:background .15s,border-color .15s,color .15s}
.speles .sl-vad button:not(:disabled):hover{border-color:var(--violet)}
.speles .sl-vad button:disabled{opacity:.35;cursor:default}
.speles .sl-lec{flex:0 0 auto;width:2.8rem;font-size:1.5rem}
.speles .sl-soli{flex:1 1 auto;display:flex;flex-wrap:wrap;gap:.35rem;
    justify-content:center}
.speles .sl-soli button{flex:0 1 2.8rem;min-width:2.4rem;font-size:1rem;
    color:var(--dim)}
.speles .sl-soli button[aria-current="true"]{background:var(--violet);
    border-color:var(--violet);color:#fff}
.speles .sl-kur{margin:.45rem 0 0;text-align:center;color:var(--dim);
    font-size:.82rem}
/* Telefonā visiem soļiem jāsatilpst vienā rindā: tikai tad uzreiz redz,
   cik soļu ir pavisam un kurš no tiem ir priekšā. */
@media (max-width:480px){
  .speles .sl-vad{gap:.3rem}
  .speles .sl-lec{width:2.4rem}
  .speles .sl-soli{gap:.3rem}
  .speles .sl-soli button{flex:1 1 1.9rem;min-width:1.9rem}
}
"""

    JS = """
MSP.veidi.slidnis=function(root){
  var soli=MSP.dati(root,"data-soli")||[];
  if(!soli.length){return;}
  var sl=MSP.e("div","sl");
  var zim=MSP.e("div","sl-zim"),v=MSP.e("p","sl-v"),t=MSP.e("p","sl-teksts");
  var josla=MSP.e("div","sl-josla"),pild=MSP.e("i");
  josla.appendChild(pild);
  var vad=MSP.e("div","sl-vad"),numuri=MSP.e("div","sl-soli");
  var kur=MSP.e("p","sl-kur");
  var atpakal=MSP.poga("sl-lec","‹"),talak=MSP.poga("sl-lec","›");
  atpakal.setAttribute("aria-label","Iepriekšējais solis");
  talak.setAttribute("aria-label","Nākamais solis");
  var pogas=[],n=0,i;
  for(i=0;i<soli.length;i++){
    pogas.push(numurs(i));
    numuri.appendChild(pogas[i]);
  }
  function numurs(k){
    var b=MSP.poga(null,""+(k+1));
    b.setAttribute("aria-label",(k+1)+". solis");
    b.addEventListener("click",function(){ej(k);});
    return b;
  }
  atpakal.addEventListener("click",function(){ej(n-1);});
  talak.addEventListener("click",function(){ej(n+1);});
  /* Bultiņas uz tastatūras dara to pašu, ko pogas - tas, ko no slīdņa
     gaidīja tie, kas lapu lasa bez peles. */
  vad.addEventListener("keydown",function(ev){
    if(ev.key==="ArrowRight"||ev.key==="ArrowDown"){ev.preventDefault();
      ej(n+1);}
    if(ev.key==="ArrowLeft"||ev.key==="ArrowUp"){ev.preventDefault();ej(n-1);}
  });
  vad.appendChild(atpakal);vad.appendChild(numuri);vad.appendChild(talak);
  sl.appendChild(zim);sl.appendChild(v);sl.appendChild(t);
  sl.appendChild(josla);sl.appendChild(vad);sl.appendChild(kur);
  root.appendChild(sl);
  function ej(jauns){
    n=Math.max(0,Math.min(soli.length-1,jauns));
    radi();
  }
  function radi(){
    var k=soli[n]||soli[0],j;
    zim.innerHTML=k.zim||"";
    zim.style.display=k.zim?"":"none";
    v.innerHTML=k.v||"";
    t.innerHTML=k.teksts||"";
    josla.style.display=(k.josla==null)?"none":"";
    pild.style.width=(k.josla||0)+"%";
    for(j=0;j<pogas.length;j++){
      pogas[j].setAttribute("aria-current",j===n?"true":"false");
    }
    atpakal.disabled=(n===0);
    talak.disabled=(n===soli.length-1);
    kur.textContent=(n+1)+". solis no "+soli.length;
    /* Ja tikko nospiestā poga kļuva pelēka, fokuss nepazūd. */
    if(document.activeElement&&document.activeElement.disabled){
      pogas[n].focus();
    }
  }
  radi();
};
"""

    def __init__(self, virsraksts, soli, ievads=None):
        Spele.__init__(self, virsraksts, ievads)
        self.soli = list(soli)
        if len(self.soli) < 2:
            raise AssertionError("«%s»: slīdnim vajag vismaz divus soļus"
                                 % virsraksts)

    def veids(self):
        return "slidnis"

    def atributi(self):
        return {"data-soli": _atr([self._zimets(s) for s in self.soli])}

    @staticmethod
    def _zimets(solis):
        """Teksts un rādītāja uzraksts iet caur to pašu matemātikas zīmētāju,
        ko visi pārējie bloki, tāpēc {3|4} arī te ir īsta daļa."""
        out = dict(solis)
        for lauks in ("v", "teksts"):
            if lauks in out:
                out[lauks] = esc(out[lauks])
        return out


class Petijums(Bloks):
    """Pētījuma solis: ko izmēģināt ar rokām un ko pierakstīt.

    Programma prasa praktisko daļu (mērīšanu, modelēšanu, datu vākšanu), un
    tā nav uzdevums ar atbildi - tāpēc tam ir savs bloks, nevis vēl viens
    uzdevumu veids.
    """

    CSS = """
.bl.petijums{background:#F0F9FF;border:1px solid #BAE6FD;box-shadow:none}
.bl.petijums>h2{color:#0369A1}
.bl.petijums .vajag{margin:.2rem 0 .6rem;color:var(--dim);
    font-size:clamp(.88rem,3.6vw,.98rem)}
.bl.petijums ol{margin:.4rem 0 0;padding-left:1.4rem;display:grid;gap:.4rem}
.bl.petijums ol li{font-size:clamp(.98rem,4vw,1.08rem)}
.bl.petijums ol li::marker{color:#0369A1;font-weight:600}
.bl.petijums .secinajums{margin:.8rem 0 0;padding:.6rem .8rem;
    background:#fff;border-radius:var(--r);border:1px dashed #7DD3FC;
    font-size:clamp(.95rem,3.9vw,1.05rem)}
"""

    def __init__(self, virsraksts, soli, vajag=None, secinajums=None):
        Bloks.__init__(self, virsraksts)
        self.soli, self.vajag = list(soli), vajag
        self.secinajums = secinajums

    def klase(self):
        return "petijums"

    def kermenis(self):
        gabali = []
        if self.vajag:
            gabali.append('<p class="vajag">Vajadzēs: %s</p>' % esc(self.vajag))
        gabali.append("<ol>\n%s\n</ol>"
                      % "\n".join("<li>%s</li>" % esc(s) for s in self.soli))
        if self.secinajums:
            gabali.append('<p class="secinajums">%s</p>' % esc(self.secinajums))
        return "\n".join(gabali)



class Simulacija(Spele):
    """Nejaušs eksperiments: met kauliņu vai monētu daudz reižu un vēro.

    Varbūtību 7. klasē vispirms iegūst ar eksperimentu: relatīvais biežums
    ar katru metienu svārstās mazāk un tuvojas teorētiskajai varbūtībai.
    Ar rokām simts metienu stundā nepaspēj, tāpēc tos izdara lapa - skolēns
    redz gan katra iznākuma skaitu, gan notikuma biežumu.

    iznakumi  - iznākumu nosaukumi («1» ... «6», «ģerbonis», «cipars»);
    svari     - cik «vietu» katram iznākumam (ruletei ar nevienādiem
                sektoriem), pēc noklusējuma visiem vienādi;
    notikums  - to iznākumu numuri (no 0), kuros notikums notiek;
    nosaukums - notikuma vārdi («uzkrīt sešinieks»);
    teorija   - teorētiskā varbūtība marķējumā, piemēram, «{1|6} ≈ 0,17»;
                to rāda tikai pēc 50 metieniem, kad ir ar ko salīdzināt.
    """

    CSS = """
.speles .sim-pogas{display:flex;flex-wrap:wrap;gap:.5rem;margin:.2rem 0 .7rem}
.speles .sim-pedejais{margin:0 0 .6rem;text-align:center;color:var(--dim)}
.speles .sim-pedejais b{display:inline-block;min-width:2.6rem;
    margin-left:.4rem;padding:.2rem .6rem;border-radius:var(--r-sm);
    background:var(--violet);color:#fff;font-family:var(--font-h);
    font-size:1.2rem}
.speles .sim-rinda{display:grid;gap:.5rem;align-items:center;margin:.25rem 0;
    grid-template-columns:minmax(3.2rem,auto) 1fr 2.6rem}
.speles .sim-rinda .n{font-weight:600;color:var(--primary);
    overflow-wrap:anywhere}
.speles .sim-rinda .s{height:1rem;border-radius:var(--r-sm);
    background:var(--surface2);overflow:hidden}
.speles .sim-rinda .s i{display:block;height:100%;width:0;
    background:var(--violet);transition:width .2s}
.speles .sim-rinda.ir .s i{background:var(--amber)}
.speles .sim-rinda .c{text-align:right;font-variant-numeric:tabular-nums}
.speles .sim-kopa{margin:.8rem 0 0;padding:.6rem .8rem;border-radius:var(--r);
    background:var(--bg);font-size:clamp(.98rem,4vw,1.08rem)}
.speles .sim-teorija{margin:.4rem 0 0;color:var(--dim)}
"""

    JS = """
MSP.veidi.simulacija=function(root){
  var d=MSP.dati(root,"data-sim")||{};
  var iz=d.iznakumi||[],svari=d.svari||[],ir={},kopa=0,i;
  for(i=0;i<(d.notikums||[]).length;i++){ir[d.notikums[i]]=1;}
  for(i=0;i<svari.length;i++){kopa+=svari[i];}
  var skaits=[],n=0,m=0,pedejais=null,joslas=[],cipari=[];
  var pogas=MSP.e("div","sim-pogas"),ped=MSP.e("p","sim-pedejais");
  var rindas=MSP.e("div","sim-rindas"),kopsav=MSP.e("p","sim-kopa");
  var teorija=MSP.e("p","sim-teorija");
  for(i=0;i<iz.length;i++){
    skaits.push(0);
    var r=MSP.e("div","sim-rinda"+(ir[i]?" ir":""));
    var s=MSP.e("span","s"),j=MSP.e("i"),c=MSP.e("span","c","0");
    s.appendChild(j);
    r.appendChild(MSP.e("span","n",iz[i]));r.appendChild(s);r.appendChild(c);
    joslas.push(j);cipari.push(c);rindas.appendChild(r);
  }
  /* Viens metiens: nejaušs skaitlis nokrīt kāda iznākuma «vietās». */
  function viens(){
    var x=Math.random()*kopa,k=0;
    while(k<svari.length-1&&x>=svari[k]){x-=svari[k];k++;}
    skaits[k]++;n++;if(ir[k]){m++;}pedejais=k;
  }
  function radi(){
    var liel=1,k;
    for(k=0;k<skaits.length;k++){liel=Math.max(liel,skaits[k]);}
    for(k=0;k<skaits.length;k++){
      joslas[k].style.width=(100*skaits[k]/liel)+"%";
      cipari[k].textContent=skaits[k];
    }
    ped.textContent=pedejais===null?"Vēl nav mests.":"Pēdējais iznākums:";
    if(pedejais!==null){ped.appendChild(MSP.e("b","",iz[pedejais]));}
    kopsav.textContent=n?("Notikums «"+d.nosaukums+"»: "+m+" reizes no "+n+
      ". Relatīvais biežums "+m+" : "+n+" ≈ "+MSP.cip(Math.round(m/n*100)/100))
      :"Spied pogu un skaties, kā mainās biežums.";
    teorija.innerHTML=(n>=50&&d.teorija)?
      ("Teorētiskā varbūtība: "+d.teorija):"";
  }
  function metiens(reizes,uzraksts){
    var b=MSP.poga(reizes===100?"galvena":"",uzraksts);
    b.setAttribute("data-reizes",""+reizes);
    b.addEventListener("click",function(){
      for(var q=0;q<reizes;q++){viens();}
      radi();
    });
    pogas.appendChild(b);
  }
  metiens(1,"1 reizi");metiens(10,"10 reizes");metiens(100,"100 reizes");
  var no=MSP.poga("","No sākuma");
  no.addEventListener("click",function(){
    for(var k=0;k<skaits.length;k++){skaits[k]=0;}
    n=0;m=0;pedejais=null;radi();
  });
  pogas.appendChild(no);
  root.appendChild(pogas);root.appendChild(ped);root.appendChild(rindas);
  root.appendChild(kopsav);root.appendChild(teorija);
  radi();
};
"""

    def __init__(self, virsraksts, iznakumi, notikums, nosaukums,
                 teorija=None, svari=None, ievads=None):
        Spele.__init__(self, virsraksts, ievads)
        self.iznakumi = [str(x) for x in iznakumi]
        self.svari = list(svari or [1] * len(self.iznakumi))
        self.notikums, self.nosaukums = list(notikums), nosaukums
        self.teorija = teorija
        if len(self.svari) != len(self.iznakumi):
            raise AssertionError("«%s»: svaru un iznākumu skaits nesakrīt"
                                 % virsraksts)
        if not all(0 <= i < len(self.iznakumi) for i in self.notikums):
            raise AssertionError("«%s»: notikumā ir neesošs iznākums"
                                 % virsraksts)

    def veids(self):
        return "simulacija"

    def atributi(self):
        return {"data-sim": _atr({
            "iznakumi": self.iznakumi, "svari": self.svari,
            "notikums": self.notikums, "nosaukums": self.nosaukums,
            "teorija": esc(self.teorija) if self.teorija else ""})}
