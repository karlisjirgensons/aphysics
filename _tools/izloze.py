# -*- coding: utf-8 -*-
"""Varianta izloze pārlūkā - JavaScript teksts.

Darbu variantu izlozē lapa pati, bez servera. Šeit ir tikai izloze (SRP);
ko ar izlozēto darīt, zina fd_page.py (viens variants) un mat_page.py (trīs
varianti vienā reizē), un abi lasa šo pašu moduli (DRY).

Izloze ir atkārtojama: no četru zīmju koda nāk sēkla, no sēklas - visi
gadījuma skaitļi. Tāpēc ar to pašu kodu vienmēr sanāk tas pats darbs, un
skolotājs var izdrukāt tieši to, ko redzēja ekrānā, vai pateikt kodu kolēģim.

    IZLOZE.kods(n)                 - jauns n zīmju kods (pēc noklusējuma 4)
    IZLOZE.lozes(IZLOZE.seja(k))   - gadījuma skaitļu avots no koda
    IZLOZE.jauc(saraksts, rnd)     - sajauc sarakstu uz vietas
    IZLOZE.indeksi(n)              - [0, 1, ... n-1]
    IZLOZE.merki(n, rnd)           - kur katrā jautājumā likt pareizo atbildi
    IZLOZE.sagatavo(jaut, merkis, rnd) - jautājums ar pārkārtotām atbildēm
"""

JS = r"""
window.IZLOZE=(function(){
"use strict";
/* Kodā nav līdzīgo zīmju (0/O, 1/I), lai to var nolasīt un pateikt balsī. */
var ZIMES="ABCDEFGHJKLMNPQRSTUVWXYZ23456789";

function kods(garums){
  var n=garums||4,out="",i,a=new Uint32Array(n);
  if(window.crypto&&window.crypto.getRandomValues)
    window.crypto.getRandomValues(a);
  else for(i=0;i<n;i++)a[i]=Math.floor(Math.random()*4294967296);
  for(i=0;i<n;i++)out+=ZIMES[a[i]%ZIMES.length];
  return out;
}
function seja(s){
  var h=2166136261,i;
  for(i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619);}
  return h>>>0;
}
function lozes(seed){
  return function(){
    seed=seed+0x6D2B79F5|0;
    var t=Math.imul(seed^seed>>>15,1|seed);
    t=t+Math.imul(t^t>>>7,61|t)^t;
    return ((t^t>>>14)>>>0)/4294967296;
  };
}
function jauc(masivs,rnd){
  var i,j,t;
  for(i=masivs.length-1;i>0;i--){
    j=Math.floor(rnd()*(i+1));t=masivs[i];masivs[i]=masivs[j];masivs[j]=t;
  }
  return masivs;
}
function indeksi(n){
  var out=[],i;
  for(i=0;i<n;i++)out.push(i);
  return out;
}
function merki(n,rnd){
  /* Pareizajām atbildēm jāsadalās pa A-D vienmērīgi, lai atbilžu tabulā
     nesanāk virkne ar vienu burtu. */
  var out=[],i;
  for(i=0;i<n;i++)out.push(i%4);
  return jauc(out,rnd);
}
function sagatavo(jaut,merkis,rnd){
  var varianti=jaut[1].slice(),pareizais=jaut[2];
  var pari=varianti.map(function(v,i){return {v:v,ok:i===pareizais};});
  jauc(pari,rnd);
  var tag=pari.map(function(p){return p.ok;}).indexOf(true);
  var t=pari[tag];pari[tag]=pari[merkis];pari[merkis]=t;
  return {teksts:jaut[0],varianti:pari.map(function(p){return p.v;}),
          pareizais:merkis};
}

return {kods:kods,seja:seja,lozes:lozes,jauc:jauc,indeksi:indeksi,
        merki:merki,sagatavo:sagatavo};
})();
"""
