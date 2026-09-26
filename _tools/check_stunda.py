# -*- coding: utf-8 -*-
"""Matemātikas stundu lapu pārbaude - viena komanda visai klasei.

    python check_stunda.py 5          # visas uzrakstītās 5. klases stundas
    python check_stunda.py 5 12 13    # tikai 12. un 13. stunda
    python check_stunda.py            # visas klases
    python check_stunda.py iq         # visi IQ testi (Math/IQ)
    python check_stunda.py iq 5 36    # tikai 5. un 36. IQ tests

IQ testus izspēlē vēl divos īstos ekrānos (EKRANI - telefons lentē un
klēpjdators) un katrai mīklai pirms un pēc atbildes pārbauda, vai spēle
ietilpst ekrānā: IQ spēlē nedrīkst būt jāritina.

Lapu atver īstā pārlūkā telefona platumā un pārbauda to, ko ar aci var
nepamanīt:

    * vai saturs neizplūst ārpus ekrāna (rules_lessons.txt: telefonā
      nedrīkst būt horizontāla ritināšana);
    * vai lapas JavaScript ir nostrādājis un katrs uzdevums ir uzzīmējies;
    * vai katru uzdevumu var izpildīt līdz galam - pārbaude tos izspēlē,
      kārtu pēc kārtas, un gaida, ka lapa pasaka «pareizi»;
    * vai nepareiza atbilde tiešām tiek noraidīta.

Pārlūks strādā bez loga; atbildi tas atdod kā tekstu (--dump-dom), tāpēc
rezultāts ir saraksts, nevis bilde - bildes vajag tikai tad, kad vērtē
izskatu, nevis meklē kļūdu.

Chrome telefona platumu neļauj mazāku par ~500 px, tāpēc stundu ieliek
390 px platā rāmī (sk. deck_visual_verification piezīmi).
"""

import html
import json
import os
import re
import subprocess
import sys
import tempfile
from urllib.request import pathname2url

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import iq_testi                                     # noqa: E402
import iq_vietne                                    # noqa: E402
import math_plani                                   # noqa: E402
import math_stundas                                 # noqa: E402

PLATUMS = 390            # telefona platums, kurā lapu pārbauda
AUGSTUMS = 9000          # rāmja augstums - lai neviens bloks nepaliek ārpus
# Īsti ekrāni, kuros IQ spēlei jāietilpst bez ritināšanas.
EKRANI = [("telefons", 390, 844), ("dators", 1280, 720)]
PARLUKS = os.environ.get(
    "CHROME", r"C:\Program Files\Google\Chrome\Application\chrome.exe")


def url(path):
    return "file:///" + pathname2url(os.path.abspath(path)).lstrip("/")


# Pārbaudes skripts strādā stundas lapā - katram uzdevuma veidam savs
# izspēlētājs. Jaunam bloka veidam pieraksta vienu funkciju (SRP).
AUDITS = """
function audits(doc){
  var zin={plats:null,speles:[],kludas:[]};
  var de=doc.documentElement;
  if(de.scrollWidth>de.clientWidth+1){
    var vainigs="";
    var visi=doc.querySelectorAll("*");
    for(var i=0;i<visi.length;i++){
      var r=visi[i].getBoundingClientRect();
      if(r.right>de.clientWidth+1){
        vainigs=visi[i].tagName+"."+(visi[i].className||"");break;
      }
    }
    zin.plats="satura platums "+de.scrollWidth+" > "+de.clientWidth+
              (vainigs?" ("+vainigs+")":"");
  }
  /* Teksts rūtiņā: zīmējuma uzraksts nedrīkst būt platāks par savu rūtiņu,
     un HTML lodziņa saturs - par pašu lodziņu. */
  var zt=doc.querySelectorAll(".zim text[data-maks]");
  for(var z=0;z<zt.length;z++){
    var gar=zt[z].getComputedTextLength();
    if(gar>parseFloat(zt[z].getAttribute("data-maks"))+0.2){
      zin.kludas.push("zīmējuma uzraksts «"+zt[z].textContent+
                      "» neietilpst rūtiņā");
    }
  }
  var lodz=doc.querySelectorAll(".bl *");
  for(var l=0;l<lodz.length;l++){
    var el=lodz[l];
    if(el.closest("svg")||!el.clientWidth){continue;}
    if(el.scrollWidth>el.clientWidth+2){
      zin.kludas.push("teksts neietilpst lodziņā "+el.tagName.toLowerCase()+
                      "."+String(el.className).split(" ")[0]+" («"+
                      (el.textContent||"").trim().slice(0,30)+"»)");
      break;
    }
  }
  if(!doc.defaultView.MSP&&doc.querySelector("[data-veids]")){
    zin.kludas.push("MSP dzinējs nav ielādējies");
  }
  /* Marķējums pieder pirmkodam; ja tas nonācis ekrānā, tas nav pārvērsts. */
  var redzams=doc.body.innerText||"";
  if(/\\{[^{}\\n]*\\|[^{}\\n]*\\}/.test(redzams)){
    zin.kludas.push("ekrānā redzams daļas marķējums {a|b}");
  }
  if(/\\^[{0-9A-Za-z\\u2212-]/.test(redzams)){
    zin.kludas.push("ekrānā redzams kāpinātāja marķējums a^n");
  }
  /* Indeksa marķējums: a_{10} un aₙ ir pareizi, bet «a_10» paliek teksts.
     Zīmējumu uzraksti (SVG) innerText neietilpst - tos pārbauda atsevišķi. */
  var zim="";
  var teksti=doc.querySelectorAll("svg text");
  for(var t=0;t<teksti.length;t++){zim+=" "+teksti[t].textContent;}
  if(/[A-Za-z\\u0370-\\u03ff]_[{0-9A-Za-z]/.test(redzams+zim)){
    zin.kludas.push("ekrānā redzams indeksa marķējums a_n");
  }
  if(/\\^[{0-9A-Za-z\\u2212-]/.test(zim)){
    zin.kludas.push("zīmējumā redzams kāpinātāja marķējums a^n");
  }
  if(/<\\/?[a-zA-Z]+ ?\\/?>/.test(redzams)){
    zin.kludas.push("ekrānā redzama HTML birka - saturā lieto *izcēlumu*");
  }

  function teksts(el,sel){var x=el.querySelector(sel);
    return x?x.textContent:"";}
  function pogas(el,sel){
    return Array.prototype.slice.call(el.querySelectorAll(sel));}

  /* Izspēlē visas kārtas, arī papildu pāri, ko dod «Vēl divi uzdevumi». */
  function kartas(el,atrisini){
    for(var i=0;i<40;i++){
      var kart=teksts(el,".kart");
      var kluda=atrisini(el);
      if(kluda){return kart+": "+kluda;}
      if(!el.querySelector(".atb.labi")){
        return kart+": atbilde netika pieņemta";
      }
      var talak=el.querySelector(".vadiba button.talak");
      if(!talak){return null;}
      talak.click();
    }
    return "kārtas nebeidzas";
  }

  var draiveri={
    josla:function(el){
      var p=pogas(el,".josla button");
      if(p.length<2){return "nav skaitļu joslas";}
      p[p.length-1].click();
      return el.querySelector(".atb.labi")?null:"josla neatbild";
    },
    skaiti:function(el){
      return kartas(el,function(e){
        var m=pogas(e,".mantas button");
        if(!m.length){return "nav priekšmetu";}
        for(var i=0;i<m.length;i++){m[i].click();}
        return null;
      });
    },
    modelis:function(el){
      return kartas(el,function(e){
        var cik=e.querySelectorAll(".mantas .manta").length;
        var liek=e.querySelector(".liekam button.liek");
        var parb=e.querySelector(".vadiba button.galvena");
        if(!cik||!liek||!parb){return "nav paplātes vai pogas";}
        liek.click();
        parb.click();
        if(cik>1&&!e.querySelector(".atb.vel")){
          return "par mazu ripiņu skaitu netiek brīdināts";
        }
        for(var i=1;i<cik;i++){liek.click();}
        parb.click();
        return null;
      });
    },
    ievadi:function(el){
      var dati=JSON.parse(el.getAttribute("data-kartas"));
      var n=0;
      return kartas(el,function(e){
        var lauks=e.querySelector(".ie-rinda input");
        var poga=e.querySelector(".ie-rinda button");
        if(!lauks||!poga){return "nav ievades lauka";}
        /* Vispirms apzināti greiza atbilde - vai to noraida. */
        lauks.value="—";
        poga.click();
        if(!e.querySelector(".atb.vel")){
          return "nepareiza atbilde netiek noraidīta";
        }
        lauks.value=dati[n].atb[0];
        n++;
        poga.click();
        return null;
      });
    },
    varianti:function(el){
      return kartas(el,function(e){
        var o=pogas(e,".va-opcijas button");
        if(o.length<2){return "nav atbilžu";}
        for(var i=0;i<o.length;i++){
          o[i].click();
          if(e.querySelector(".atb.labi")){return null;}
          if(!e.querySelector(".atb.vel")){
            return "nepareiza atbilde netiek noraidīta";
          }
        }
        return "neviena atbilde nav pareiza";
      });
    },
    kustiba:function(el){
      var dati=JSON.parse(el.getAttribute("data-kartas"));
      var n=0;
      return kartas(el,function(e){
        var lauks=e.querySelector(".ie-rinda input");
        var poga=e.querySelector(".ie-rinda button");
        if(!lauks||!poga){return "nav ievades lauka";}
        if(!e.querySelector(".kust-merkis")){return "nav mērķa uz trases";}
        lauks.value="—";
        poga.click();
        if(!e.querySelector(".atb.vel")){
          return "nepareiza atbilde netiek noraidīta";
        }
        lauks.value=(""+dati[n].atb).replace(".",",");
        n++;
        poga.click();
        return null;
      });
    },
    slidnis:function(el){
      var soli=pogas(el,".sl-soli button");
      var t=el.querySelector(".sl-teksts");
      if(soli.length<2){return "nav soļu pogu";}
      if(!t||!t.textContent.trim()){return "slīdnis neko nerāda";}
      /* Izspēlē visus soļus. Divi soļi drīkst rādīt vienu un to pašu
         (|−5| un |5| ir 5), bet visi pēc kārtas - ne: tad poga nav
         pieslēgta. Skatās gan rādītāja uzrakstu, gan tekstu. */
      var v=el.querySelector(".sl-v"),redzets={},cik=0,i;
      for(i=0;i<soli.length;i++){
        soli[i].click();
        if(soli[i].getAttribute("aria-current")!=="true"){
          return "solis " + (i+1) + " neatzīmējas";
        }
        var seja=(v?v.textContent:"")+"|"+t.textContent;
        if(!redzets[seja]){redzets[seja]=1;cik++;}
      }
      if(cik<2){return "soļa pogas neko nemaina";}
      return null;
    },
    simulacija:function(el){
      var p=el.querySelector(".sim-pogas button[data-reizes='100']");
      if(!p){return "nav metienu pogas";}
      p.click();
      if(teksts(el,".sim-kopa").indexOf("no 100")<0){
        return "pēc 100 metieniem skaits nav 100";
      }
      var c=pogas(el,".sim-rinda .c"),summa=0;
      for(var i=0;i<c.length;i++){summa+=parseInt(c[i].textContent,10);}
      return summa===100?null:"iznākumu skaitu summa nav 100";
    },
    /* Vai IQ spēle ietilpst: bloks nav jāritina, un nekas neiziet ārpus
       savas vietas (skatuves, zīmējuma laukuma vai paneļa). Īstā ekrānā
       to mēra tikai tad, kad rāmis nav mākslīgi augsts. */
    ietilpst:function(el){
      if(doc.defaultView.innerHeight>3000){return null;}
      var bl=el.closest(".bl"),kl=[];
      function ara(x,sk){
        if(x&&x.scrollHeight>x.clientHeight+2){kl.push(sk+" jāritina ("+
          x.scrollHeight+" > "+x.clientHeight+")");}}
      ara(bl,"bloks");ara(el,"spēle");
      ara(el.querySelector(".iq-kart"),"kārts");
      ara(el.querySelector(".iq-panelis"),"panelis");
      var v=el.querySelector(".iq-vieta");
      if(v){
        var r=v.getBoundingClientRect(),d=v.querySelectorAll("*");
        for(var i=0;i<d.length;i++){
          if(d[i].closest("svg")&&d[i].tagName.toLowerCase()!=="svg"){
            continue;}
          var q=d[i].getBoundingClientRect();
          if(!q.height){continue;}
          if(q.bottom>r.bottom+2||q.right>r.right+2){
            kl.push("iziet ārpus vietas: "+d[i].tagName.toLowerCase()+"."+
                    String(d[i].getAttribute("class")||"").split(" ")[0]);
            break;
          }
        }
      }
      if(doc.documentElement.scrollWidth>doc.documentElement.clientWidth+1){
        kl.push("lapa platāka par ekrānu");}
      /* Garajā lapā visa spēle redzama jau pirmajā ekrānā. */
      var w=doc.defaultView;
      if(!doc.body.classList.contains("pilns")&&
         el.getBoundingClientRect().bottom+w.pageYOffset>w.innerHeight+2){
        kl.push("spēle nav redzama visa bez lapas ritināšanas");}
      return kl.length?kl.join("; "):null;
    },
    /* IQ tests: katrai mīklai vispirms greiza atbilde (vai to noraida un
       piedāvā «Izlaist»), tad pareizā ar laika vērtējumu. Pirmo mīklu
       izlaiž - arī tam ceļam jānoved līdz «Tālāk». Beigās jābūt rezultāta
       ekrānam ar «Spēlēt vēlreiz». */
    iq:function(el){
      var dati=JSON.parse(el.getAttribute("data-kartas"));
      var vieta;
      for(var n=0;n<dati.length;n++){
        var k=dati[n],nr=(n+1)+". mīkla: ";
        if((vieta=draiveri.ietilpst(el))){return nr+vieta;}
        var atc=el.querySelector("button.iq-atceros");
        if(k.radit){
          if(!atc){return nr+"nav iegaumēšanas pogas";}
          atc.click();
        }
        if(k.veids==="izvele"){
          var o=pogas(el,".iq-opc button");
          if(o.length<2){return nr+"nav variantu";}
          o[(k.pareizi+1)%o.length].click();
          if(!el.querySelector(".iq-zin.vel")){
            return nr+"nepareiza atbilde netiek noraidīta";}
        }else if(k.veids==="ievade"){
          var lauks=el.querySelector(".ie-rinda input");
          var poga=el.querySelector(".ie-rinda button");
          if(!lauks||!poga){return nr+"nav ievades lauka";}
          lauks.value="—";poga.click();
          if(!el.querySelector(".iq-zin.vel")){
            return nr+"nepareiza atbilde netiek noraidīta";}
        }else{
          var r=pogas(el,".iq-rez button"),parb=el.querySelector(".iq-parb");
          if(!r.length||!parb){return nr+"nav rūtiņu";}
          var cita=0;while(k.atb.indexOf(cita)>=0){cita++;}
          r[cita].click();parb.click();
          if(!el.querySelector(".iq-zin.vel")){
            return nr+"nepareiza atzīme netiek noraidīta";}
        }
        var izl=el.querySelector("button.iq-izlaist");
        if(!izl){return nr+"pēc kļūdas nav pogas «Izlaist»";}
        if(n===0){
          izl.click();
          if(!el.querySelector(".iq-prog span.izlaists")){
            return nr+"izlaistā mīkla nav atzīmēta joslā";}
        }else{
          if(k.veids==="izvele"){o[k.pareizi].click();}
          else if(k.veids==="ievade"){lauks.value=k.atb[0];poga.click();}
          else{
            r[cita].click();
            for(var j=0;j<k.atb.length;j++){r[k.atb[j]].click();}
            parb.click();
          }
          if(!el.querySelector(".iq-zin.labi")){
            return nr+"pareizā atbilde netika pieņemta";}
          if(!el.querySelector(".tempo .tempo-r b")){
            return nr+"nav laika vērtējuma";}
        }
        if(k.skaidro&&!teksts(el,".iq-skaidro").trim()){
          return nr+"nav paskaidrojuma";}
        if((vieta=draiveri.ietilpst(el))){return nr+"pēc atbildes "+vieta;}
        var t=el.querySelector("button.iq-talak");
        if(!t){return nr+"nav pogas «Tālāk»";}
        t.click();
      }
      if(!el.querySelector(".iq-beigas button.iq-atkal")){
        return "nav rezultāta ekrāna";}
      if((vieta=draiveri.ietilpst(el))){return "rezultāts: "+vieta;}
      return null;
    },
    izvele:function(el){
      return kartas(el,function(e){
        var c=pogas(e,".cipari button");
        if(!c.length){return "nav ciparu";}
        var pareizi=0;
        for(var i=0;i<c.length;i++){
          c[i].click();
          if(e.querySelector(".atb.labi")){pareizi++;break;}
          if(!e.querySelector(".atb.vel")){
            return "nepareiza atbilde netiek noraidīta";
          }
        }
        return pareizi?null:"neviena atbilde nav pareiza";
      });
    }
  };

  var els=doc.querySelectorAll("[data-veids]");
  for(var i=0;i<els.length;i++){
    var v=els[i].getAttribute("data-veids");
    var rez={veids:v,kluda:null};
    if(!els[i].childElementCount){
      rez.kluda="nav uzzīmējies";
    }else if(draiveri[v]){
      try{rez.kluda=draiveri[v](els[i]);}
      catch(x){rez.kluda="kļūda izspēlējot: "+x.message;}
    }
    zin.speles.push(rez);
  }
  return zin;
}
"""

RAMIS = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>parbaude</title></head>
<body style="margin:0">
<iframe id="r" width="%(w)d" height="%(h)d" style="border:0"></iframe>
<pre id="zinojums">GAIDA</pre>
<script>
%(audits)s
var lapas=%(lapas)s, rez=[], i=0;
var r=document.getElementById("r");
r.addEventListener("load",function(){
  var z;
  try{z=audits(r.contentDocument);}
  catch(x){z={plats:null,speles:[],kludas:["nepiekļūst lapai: "+x.message]};}
  z.stunda=lapas[i].nr;
  z.nos=lapas[i].nos;
  rez.push(z);
  i++;
  if(i<lapas.length){r.src=lapas[i].url;}
  else{document.getElementById("zinojums").textContent=
        "ZINOJUMS"+JSON.stringify(rez)+"BEIGAS";}
});
if(lapas.length){r.src=lapas[0].url;}
else{document.getElementById("zinojums").textContent="ZINOJUMS[]BEIGAS";}
</script>
</body></html>
"""

_ZINO = re.compile(r"ZINOJUMS(\[.*?\])BEIGAS", re.S)


def lapas(klase, gatavas, numuri=None):
    """[{nr, nos, url}, ...] - uzbūvētās lapas, ko atvērt pārlūkā."""
    ja = sorted(n for n in gatavas if not numuri or n in numuri)
    return [{"nr": n, "nos": gatavas[n].tema,
             "url": url(os.path.join(math_stundas.mape(klase),
                                     math_stundas.cels(klase, gatavas[n])))}
            for n in ja]


def parbaudi(klases_nr, numuri=None):
    """Uzbūvē stundas, atver tās pārlūkā un atgriež ziņojumu sarakstu."""
    klase = math_plani.klase(klases_nr)
    math_stundas.build_klase(klase)
    return parbaudi_lapas(lapas(klase, math_stundas.saturi(klase), numuri))


def parbaudi_iq(numuri=None):
    """Tas pats IQ testiem: uzbūvē un izspēlē katru testu - vispirms garā
    rāmī (kā stundas), tad katrā īstajā ekrānā, kur mēra, vai ietilpst."""
    iq_vietne.build()
    kurss = iq_testi.kurss()
    visas = lapas(kurss, {t.nr: t for t in kurss.visas}, numuri)
    out = parbaudi_lapas(visas)
    for nos, w, h in EKRANI:
        for z in parbaudi_lapas(visas, w, h):
            for s in z.get("speles") or []:
                if s.get("kluda"):
                    s["kluda"] = "%s %dx%d: %s" % (nos, w, h, s["kluda"])
            out.append(z)
    return out


def parbaudi_lapas(lapas, platums=PLATUMS, augstums=AUGSTUMS):
    """Atver lapas pārlūkā pēc kārtas un atgriež ziņojumu sarakstu."""
    if not lapas:
        return []

    mape = tempfile.mkdtemp(prefix="stundas_")
    cels = os.path.join(mape, "parbaude.html")
    with open(cels, "w", encoding="utf-8") as f:
        f.write(RAMIS % {"w": platums, "h": augstums, "audits": AUDITS,
                         "lapas": json.dumps(lapas, ensure_ascii=False)})
    # Budžets aug līdz ar stundu skaitu - katra lapa jāielādē un jāizspēlē.
    budzets = 4000 + 1500 * len(lapas)
    out = subprocess.run(
        [PARLUKS, "--headless=new", "--disable-gpu",
         "--allow-file-access-from-files", "--hide-scrollbars",
         "--window-size=%d,%d" % (platums + 140, min(augstums, 900) + 80),
         "--virtual-time-budget=%d" % budzets, "--dump-dom", url(cels)],
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    m = _ZINO.search(out.stdout or "")
    if not m:
        raise SystemExit("Pārlūks neatbildēja. %s"
                         % (out.stderr or "")[:400])
    # --dump-dom atdod HTML, tāpēc «>» tekstā ir &gt;.
    return json.loads(html.unescape(m.group(1)))


def rinda(z):
    """Viena stundas rinda: vai nu «labi», vai visas atrastās vainas."""
    vainas = list(z.get("kludas") or [])
    if z.get("plats"):
        vainas.append(z["plats"])
    for s in z.get("speles") or []:
        if s.get("kluda"):
            vainas.append("%s: %s" % (s["veids"], s["kluda"]))
    return vainas


def main(argv):
    skaitli = [int(a) for a in argv if a.isdigit()]
    if "iq" in [a.lower() for a in argv]:
        klases, numuri = ["IQ"], skaitli or None
    else:
        klases = ([skaitli[0]] if skaitli
                  else range(1, math_plani.KLASU_SKAITS + 1))
        numuri = skaitli[1:] or None
    slikti = 0
    for nr in klases:
        try:
            zinojumi = (parbaudi_iq(numuri) if nr == "IQ"
                        else parbaudi(nr, numuri))
        except ImportError:
            continue
        for z in zinojumi:
            vainas = rinda(z)
            speles = len(z.get("speles") or [])
            if vainas:
                slikti += 1
                print("VAINA  %s.kl %3d. %s" % (nr, z["stunda"], z["nos"]))
                for v in vainas:
                    print("       - %s" % v)
            else:
                print("labi   %s.kl %3d. %-44s %d uzdevumi"
                      % (nr, z["stunda"], z["nos"][:44], speles))
    print("-" * 60)
    print("Vainas: %d" % slikti if slikti else "Viss kārtībā.")
    return 1 if slikti else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv[1:]))
