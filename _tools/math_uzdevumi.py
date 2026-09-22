# -*- coding: utf-8 -*-
"""Uzdevumu bloki, kuros atbildi raksta vai izvēlas.

math_bloki.py ir stundas pamats - teksta bloki un spēļu dzinējs; te ir tie
uzdevumu veidi, kas der no vidusskolas puses skatoties visām klasēm, kur
atbilde jau ir skaitlis, daļa vai apgalvojums (SRP). Kārtu dzinējs, pogas un
atbildes rinda nāk no math_bloki.Spele, tāpēc te ir tikai tas, ar ko šie
uzdevumi atšķiras (DRY).

Matemātiku uzdevuma tekstā raksta ar to pašu marķējumu, ko visur citur:
{3|4} ir daļa, √(a + b) ir sakne (rules_pd.txt).
"""

import math_pavedieni
from math_bloki import Bloks, _Kartas, esc


# ======================================================== rēķina paraugs
class Paraugs(Bloks):
    """Nostrādāts piemērs: uzdevums, soļi un atbilde.

    Soļi iet pa vienam - vispirms pieraksts, tad teikums, kāpēc tā drīkst.
    Tā ir tā pati kārtība, ko pēc tam prasa no skolēna: vispirms formula un
    darbība, tad vērtības, tad atbilde.
    """

    CSS = """
.bl.paraugs{border-left:5px solid var(--cyan)}
.bl.paraugs .uzd{margin:.2rem 0 .7rem;padding:.6rem .8rem;
    background:var(--surface2);border-radius:var(--r);font-weight:500}
.bl.paraugs ol{margin:.4rem 0 0;padding:0;list-style:none;display:grid;
    gap:.7rem;counter-reset:solis}
.bl.paraugs ol li{position:relative;padding-left:2.3rem}
.bl.paraugs ol li::before{counter-increment:solis;content:counter(solis);
    position:absolute;left:0;top:.1rem;width:1.7rem;height:1.7rem;
    display:flex;align-items:center;justify-content:center;
    border-radius:50%;background:var(--cyan);color:#fff;font-weight:600;
    font-size:.85rem}
.bl.paraugs .mat{margin:0;font-size:clamp(1.05rem,4.6vw,1.25rem);
    color:var(--primary);font-weight:500}
.bl.paraugs .kap{margin:.15rem 0 0;color:var(--dim);
    font-size:clamp(.9rem,3.7vw,1rem)}
.bl.paraugs .atbilde{margin:.9rem 0 0;padding:.6rem .8rem;
    background:#ECFDF5;border:1px solid #A7F3D0;border-radius:var(--r);
    color:#047857;font-weight:600;
    font-size:clamp(1.02rem,4.4vw,1.18rem)}
"""

    def __init__(self, virsraksts, uzd, soli, atbilde=None):
        Bloks.__init__(self, virsraksts)
        self.uzd, self.soli, self.atbilde = uzd, list(soli), atbilde

    def klase(self):
        return "paraugs"

    def kermenis(self):
        gabali = ['<p class="uzd">%s</p>' % esc(self.uzd)]
        rindas = []
        for solis in self.soli:
            if isinstance(solis, (list, tuple)):
                mat, kapec = solis[0], (solis[1] if len(solis) > 1 else None)
            else:
                mat, kapec = solis, None
            iekss = '<p class="mat">%s</p>' % esc(mat)
            if kapec:
                iekss += '\n<p class="kap">%s</p>' % esc(kapec)
            rindas.append("<li>%s</li>" % iekss)
        gabali.append("<ol>\n%s\n</ol>" % "\n".join(rindas))
        if self.atbilde:
            gabali.append('<p class="atbilde">Atbilde: %s</p>'
                          % esc(self.atbilde))
        return "\n".join(gabali)


# ==================================================== uzdevumi ar atbildi
class Ievadi(_Kartas):
    """Ieraksti atbildi: skolēns izrēķina pats un uzraksta rezultātu.

    Atbildi salīdzina pēc būtības, nevis pēc rakstzīmēm: atstarpes neskaita,
    un punkts der komata vietā, jo uz tastatūras tas gadās pats no sevis.
    Pareizi var būt vairāki pieraksti - tos uzskaita sarakstā.

    Pēc trešā nepareizā mēģinājuma lapa parāda atbildi: mājās neviena nav,
    kas to pateiktu, un sēdēt uz vietas nav vērts.
    """

    MATEMATIKA = ("jaut", "padoms")

    CSS = """
.speles .ie-mers{margin:.35rem 0 0;color:var(--dim);font-size:.9rem}
"""

    JS = """
MSP.veidi.ievadi=function(root){
  MSP.kartas(root,function(k,c){
    /* Atbildi salīdzina bez atstarpēm, un punkts der komata vietā. */
    function tirs(s){
      return (s==null?"":""+s).toLowerCase().replace(/\\s+/g,"")
             .replace(/\\./g,",");
    }
    var derigas=[],i;
    for(i=0;i<k.atb.length;i++){derigas.push(tirs(k.atb[i]));}
    var meginajumi=0;
    var rinda=MSP.e("div","ie-rinda");
    var lauks=document.createElement("input");
    lauks.type="text";
    lauks.setAttribute("inputmode",k.tastatura||"decimal");
    lauks.setAttribute("aria-label","Atbilde");
    lauks.placeholder=k.vieta||"atbilde";
    var parbaudit=MSP.poga("galvena","Pārbaudīt");
    rinda.appendChild(lauks);rinda.appendChild(parbaudit);
    c.laukums.appendChild(rinda);
    if(k.mers){c.laukums.appendChild(MSP.e("p","ie-mers",k.mers));}
    function skatit(){
      var ir=tirs(lauks.value);
      if(!ir){c.saki("Ieraksti atbildi lodziņā.",false);return;}
      if(derigas.indexOf(ir)>=0){
        lauks.className="labi";lauks.readOnly=true;
        c.gatavs(k.labi||"Pareizi!");
        return;
      }
      meginajumi++;
      lauks.className="nepareizi";
      var teikums=k.padoms?("Vēl ne. "+k.padoms)
                          :"Vēl ne. Pārrēķini un mēģini vēlreiz.";
      if(meginajumi>=3){teikums+=" Pareizā atbilde: "+k.atbZ+".";}
      c.saki(teikums,false);
    }
    parbaudit.addEventListener("click",skatit);
    lauks.addEventListener("keydown",function(ev){
      if(ev.key==="Enter"){ev.preventDefault();skatit();}
    });
  },"Šos uzdevumus tu proti izrēķināt pats!");
};
"""

    def parbaudi_kartas(self):
        for k in self.kartas:
            if not k.get("atb"):
                raise AssertionError("«%s»: kārtai «%s» nav atbildes"
                                     % (self.virsraksts, k.get("jaut")))

    def _zimeta(self, karta):
        """Blakus atbilžu sarakstam vajag arī vienu uzzīmētu - to lapa rāda
        teikumā «Pareizā atbilde: ...»."""
        out = _Kartas._zimeta(self, karta)
        atb = karta["atb"]
        atb = list(atb) if isinstance(atb, (list, tuple)) else [atb]
        out["atb"] = atb
        out["atbZ"] = esc(atb[0])
        return out

    def veids(self):
        return "ievadi"


class Varianti(_Kartas):
    """Izvēlies pareizo: vairākas atbildes, no kurām der viena."""

    MATEMATIKA = ("jaut", "opcijas", "padoms")

    CSS = """
.speles .va-opcijas{display:grid;gap:.5rem;margin:.8rem 0 0;width:100%}
.speles .va-opcijas button{text-align:left;padding:.75rem .9rem;
    border-radius:var(--r);border:2px solid var(--line);
    font-size:clamp(.98rem,4.1vw,1.1rem);display:flex;gap:.6rem;
    align-items:baseline}
.speles .va-opcijas button .b{flex:none;color:var(--primary);font-weight:700}
.speles .va-opcijas button.labi{background:#DCFCE7;border-color:#047857}
.speles .va-opcijas button.labi .b{color:#047857}
.speles .va-opcijas button.nepareizi{background:#FEF2F2;border-color:#FCA5A5}
.speles .va-opcijas button.nepareizi .b{color:#B91C1C}
@media (min-width:600px){
  .speles .va-opcijas{grid-template-columns:1fr 1fr}
}
"""

    JS = """
MSP.veidi.varianti=function(root){
  MSP.kartas(root,function(k,c){
    var burti="ABCDEFGH";
    var saraksts=MSP.e("div","va-opcijas");
    for(var i=0;i<k.opcijas.length;i++){
      (function(i){
        var b=MSP.poga("","");
        var burts=MSP.e("span","b",burti.charAt(i)+")");
        var teksts=MSP.e("span","t","");
        teksts.innerHTML=k.opcijas[i];
        b.appendChild(burts);b.appendChild(teksts);
        b.addEventListener("click",function(){
          if(i===k.pareizi){
            b.className="labi";
            c.gatavs(k.labi||"Pareizi!");
          }else{
            b.className="nepareizi";
            c.saki(k.padoms||"Vēl ne. Pārdomā vēlreiz.",false);
          }
        });
        saraksts.appendChild(b);
      })(i);
    }
    c.vadiba.appendChild(saraksts);
  },"Šo tu tagad proti atšķirt!");
};
"""

    def parbaudi_kartas(self):
        for k in self.kartas:
            n = len(k.get("opcijas") or ())
            if n < 2:
                raise AssertionError(
                    "«%s»: kārtai «%s» vajag vismaz divas atbildes"
                    % (self.virsraksts, k.get("jaut")))
            if not 0 <= k.get("pareizi", -1) < n:
                raise AssertionError(
                    "«%s»: kārtai «%s» nav pareizās atbildes numura"
                    % (self.virsraksts, k.get("jaut")))

    def veids(self):
        return "varianti"


class Pasaule(Bloks):
    """Reālās dzīves uzdevums - tas pats rēķins, tikai par īstu lietu.

    Katrā stundā ir vismaz viens šāds uzdevums; to prasa math_lapa.parbaudi,
    tāpēc noteikums der visām klasēm un tematiem vienādi.

    Pasaule pati neko nerēķina: tā apņem jebkuru uzdevuma bloku - Ievadi,
    Varianti vai 1. klases Izvele - un pieliek tam dzīves ietvaru (SRP).
    Tāpēc tas pats ietvars der gan pirmklasniekam, kas spiež attēlu, gan
    devītajai klasei, kas ieraksta atbildi, un uzdevumu loģika nav
    pārrakstīta otrreiz (DRY).

    Pavediens ir viens dzīves temats, kas iet cauri vairākām stundām
    (math_pavedieni.py) - tā stundas cita citu turpina, nevis stāv atsevišķi.
    """

    GARUMS = 130

    CSS = """
.bl.pasaule{border-left:5px solid var(--amber)}
.bl.pasaule>h2{color:var(--amber-ink)}
.bl.pasaule .pav{display:inline-block;margin:0 0 .5rem;padding:.2rem .7rem;
    border-radius:var(--r-pill);background:#FFF4D6;color:var(--amber-ink);
    font-size:.78rem;font-weight:600}
.bl.pasaule .konteksts{margin:.2rem 0 .3rem;padding:.6rem .8rem;
    background:var(--bg);border-radius:var(--r);
    font-size:clamp(.95rem,3.9vw,1.06rem)}
.bl.pasaule .kapec{margin:.7rem 0 0;color:var(--dim);
    font-size:clamp(.88rem,3.6vw,.98rem)}
"""

    def __init__(self, virsraksts, uzdevums, pavediens, konteksts=None,
                 kapec=None, zimejums=None):
        Bloks.__init__(self, virsraksts)
        self.uzdevums = uzdevums
        self.pavediens = math_pavedieni.nosaukums(pavediens)
        self.konteksts, self.kapec, self.zimejums = konteksts, kapec, zimejums
        if not isinstance(uzdevums, Bloks):
            raise AssertionError("«%s»: Pasaule apņem uzdevuma bloku"
                                 % virsraksts)
        for vards, teksts in (("konteksts", konteksts), ("kapec", kapec)):
            if teksts and len(teksts) > self.GARUMS:
                raise AssertionError(
                    "«%s»: %s ir %d rakstzīmes, atļautas %d"
                    % (virsraksts, vards, len(teksts), self.GARUMS))

    def fragmenti(self):
        """Savi gabali un ietvertā uzdevuma gabali - lapai vajag abus."""
        return Bloks.fragmenti(self) + self.uzdevums.fragmenti()

    def klase(self):
        return "pasaule"

    def kermenis(self):
        gabali = ['<p class="pav">%s</p>' % esc(self.pavediens)]
        if self.konteksts:
            gabali.append('<p class="konteksts">%s</p>' % esc(self.konteksts))
        if self.zimejums:
            gabali.append(self.zimejums)
        gabali.append(self.uzdevums.kermenis())
        if self.kapec:
            gabali.append('<p class="kapec">%s</p>' % esc(self.kapec))
        return "\n".join(gabali)
