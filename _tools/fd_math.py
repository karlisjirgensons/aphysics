# -*- coding: utf-8 -*-
"""Darba lapas matemātiskā pieraksta parsētājs - JavaScript teksts.

Saturā formulas raksta ar vienu marķējumu (rules_pd.txt):

    {a|b}        vertikāla daļa - skaitītājs a virs saucēja b;
    √(a + b)     kvadrātsakne - zem vinkula paliek VISA izteiksme;
    √25, √a      kvadrātsakne bez iekavām, ja zem tās ir viens loceklis.

Šis modulis marķējumu tikai izjauc atomos; kā atomus uzzīmēt, zina lapa
(fd_paper.py) un Word rakstītājs (fd_docx.py), tāpēc parsētājs ir vienā
eksemplārā abiem (SRP + DRY).

    FD_MATH.atomi("x = {−b ± √(D)|2a}")
      -> [{text:"x = "}, {frac:[[{text:"−b ± "},{root:"D"}], [{text:"2a"}]]}]

    FD_MATH.vienkarsi(s)  - teksts bez marķējuma, platuma mērīšanai; daļa
                            aizņem savu platāko rindu.

    FD_MATH.indeksi("R(Z) = 6,4")
      -> [{text:"R"}, {sub:"Z"}, {text:" = 6,4"}]

Indeksa noteikums nav pārrakstīts JavaScriptā vēlreiz: izņēmumu saraksts un
prefiksi nāk no mathfmt.py (js() tos ieliek tekstā), tāpēc pieraksts, ko
maina vienā vietā, mainās gan prezentācijās, gan darba lapās (DRY).

Indeksus lieto fizika (P(pat), s(kopā)); matemātikā tie paši burti iekavās
nozīmē ko citu - P(sarkana) ir varbūtība, f(x) funkcija - tāpēc lapas
būvētājs pasaka, kuru pierakstu lieto: js(indeksi=True/False).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import mathfmt as MF                                      # noqa: E402

_JS = r"""
window.FD_MATH=(function(){
"use strict";

/* Daļas marķējums: {skaitītājs|saucējs}. */
var DALA=/\{([^{}|]*)\|([^{}|]*)\}/g;
var ZIME="√";                                   /* √ */
/* Cik tālu sniedzas sakne, ja aiz zīmes nav iekavas: viens skaitlis vai
   viens simbols ar kāpinātāju - √2, √25, √a, √x². */
var LOCEKLIS=/[0-9A-Za-zĀ-ſ,.²³]/;

function gals(s,i){
  /* Kur beidzas √-izteiksme, ja saknes zīme ir pozīcijā i. */
  var j=i+1,dz=0;
  if(s.charAt(j)==="("){
    for(;j<s.length;j++){
      if(s.charAt(j)==="(")dz++;
      else if(s.charAt(j)===")"&&!--dz)return j+1;
    }
    return s.length;
  }
  while(j<s.length&&LOCEKLIS.test(s.charAt(j)))j++;
  return j;
}

function bezIekavam(e){
  return (e.charAt(0)==="("&&e.charAt(e.length-1)===")")?e.slice(1,-1):e;
}

function saknes(s){
  /* Teksts -> atomi {text} un {root}; daļu marķējuma te vairs nav. */
  var out=[],last=0,i=s.indexOf(ZIME),g;
  while(i>=0){
    g=gals(s,i);
    if(i>last)out.push({text:s.slice(last,i)});
    out.push({root:bezIekavam(s.slice(i+1,g))});
    last=g;
    i=s.indexOf(ZIME,g);
  }
  if(last<s.length)out.push({text:s.slice(last)});
  return out;
}

function atomi(s){
  /* Viss marķējums vienā piegājienā: vispirms daļas, tad saknes. */
  var out=[],last=0,m;
  s=String(s==null?"":s);
  DALA.lastIndex=0;
  while((m=DALA.exec(s))!==null){
    if(m.index>last)out=out.concat(saknes(s.slice(last,m.index)));
    out.push({frac:[saknes(m[1]),saknes(m[2])]});
    last=DALA.lastIndex;
  }
  if(last<s.length)out=out.concat(saknes(s.slice(last)));
  return out;
}

function vienkarsi(s){
  /* Teksts bez marķējuma - platuma mērīšanai; daļa aizņem platāko rindu. */
  return String(s==null?"":s).replace(DALA,function(_,a,b){
    return a.length>=b.length?a:b;});
}

/* ------------------------------------------------------------- indeksi */
/* Kas ir indekss, izlemj mathfmt.py; te ir tikai tas pats noteikums
   JavaScriptā, ar tur doto izņēmumu sarakstu. */
var INDEKSI=%(ieslegts)s;
var FUNKCIJAS=%(funkcijas)s;         /* v(t), I(U) - grafiks, nevis indekss */
var PREFIKSI=%(prefiksi)s;           /* ΣE(dienā): Σ nav simbola daļa */
var BURTS=/\p{L}/u;
var SATURS=/^[\p{L}\p{N}]{1,12}$/u;
var CIPARI=/^[0-9]+$/;
var ASCII=/^[0-9A-Za-z]$/;

function iekavuIndekss(s,i){
  /* "R(Z)": aizverošās iekavas vieta vai 0, ja tur nav indeksa. */
  var pirms=s.charAt(i-1),priekspirms,aizver,saturs;
  if(s.charAt(i)!=="("||i===0||!BURTS.test(pirms))return 0;
  if(i>1){
    priekspirms=s.charAt(i-2);
    if(PREFIKSI.indexOf(priekspirms)<0&&
       (BURTS.test(priekspirms)||ASCII.test(priekspirms)))return 0;
  }
  aizver=s.indexOf(")",i+1);
  if(aizver<0)return 0;
  saturs=s.slice(i+1,aizver);
  if(!SATURS.test(saturs)||CIPARI.test(saturs))return 0;
  return FUNKCIJAS.indexOf(pirms+"("+saturs+")")>=0?0:aizver;
}

function pasvitrasIndekss(s,i){
  /* "F_y" un "F_{max}": [indeksa sākums, gabala beigas] vai null. */
  var nak=s.charAt(i+1),aizver;
  if(s.charAt(i)!=="_"||i===0||pirmsIrAtstarpe(s,i))return null;
  if(nak==="{"){
    aizver=s.indexOf("}",i+2);
    if(aizver<0||!SATURS.test(s.slice(i+2,aizver)))return null;
    return [i+2,aizver,aizver+1];
  }
  if(!ASCII.test(nak)||ASCII.test(s.charAt(i+2)))return null;
  return [i+1,i+2,i+2];
}

function pirmsIrAtstarpe(s,i){var c=s.charAt(i-1);return c===" "||c==="	";}

function indeksi(s){
  /* Teksts -> atomi {text} un {sub}. Bez indeksiem - viens {text}. */
  s=String(s==null?"":s);
  if(!INDEKSI)return [{text:s}];
  var out=[],buf="",i=0,pas,aizver;
  function izliet(){if(buf){out.push({text:buf});buf="";}}
  while(i<s.length){
    pas=pasvitrasIndekss(s,i);
    if(pas){izliet();out.push({sub:s.slice(pas[0],pas[1])});i=pas[2];continue;}
    aizver=iekavuIndekss(s,i);
    if(aizver){izliet();out.push({sub:s.slice(i+1,aizver)});i=aizver+1;continue;}
    buf+=s.charAt(i);
    i++;
  }
  izliet();
  return out.length?out:[{text:""}];
}

return {atomi:atomi,saknes:saknes,vienkarsi:vienkarsi,indeksi:indeksi};
})();
"""


def js(indeksi=False):
    """Parsētāja JavaScript; indeksi=True ieslēdz "R(Z)" pierakstu.

    Izņēmumus un prefiksus paņem no mathfmt, tāpēc saraksts ir vienā vietā.
    """
    return _JS % {
        "ieslegts": "true" if indeksi else "false",
        "funkcijas": _masivs(sorted(MF.FUNKCIJAS)),
        "prefiksi": _teksts("".join(sorted(MF._PREFIKSI))),
    }


def _teksts(s):
    return '"%s"' % s.replace("\\", "\\\\").replace('"', '\\"')


def _masivs(values):
    return "[%s]" % ",".join(_teksts(v) for v in values)
