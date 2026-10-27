# -*- coding: utf-8 -*-
"""Dienas izaicinājuma uzdevumi: 10 testi pa riņķi, katrā 3 uzdevumi.

Kurš tests ir šodien, nosaka datums (dienas numurs mod 10), un skaitļus
izloze ar sēklu no datuma. Tāpēc:

  * vienā dienā visiem ir vieni un tie paši uzdevumi - rezultātus var
    salīdzināt;
  * nākamreiz, kad tas pats tests atgriežas pēc 10 dienām, skaitļi ir citi;
  * rezultāta lapa (play_rezultats.py) no saites datuma uzdevumus uzbūvē
    vēlreiz, tāpēc saitē nav jāglabā pats uzdevums.

Šis modulis zina tikai uzdevumus (SRP): PU.dienas(d) -> 3 uzdevumi
{q: norādījums, e: izteiksme, opts: 4 atbildes (HTML), ok: pareizās indekss}.
Nepareizās atbildes ir tipiskas kļūdas (iekavas aizmirstas, saucēji
saskaitīti), nevis nejauši skaitļi. Ja kļūdas sakrīt ar pareizo atbildi vai
savā starpā, trūkstošās aizpilda ar tuviem skaitļiem (pildi).

Ja uzdevumus maina, jāpalielina play_rezultats VERSIJA: vecās saites tad
saka «bojāta», nevis rāda citus uzdevumus, nekā bērns risināja.
"""

JS = r"""
var PU=(function(){
  var T=PT.T, X=" "+T.reiz+" ", MINUS="−";

  /* Izloze ar sēklu (mulberry32) - tā pati sēkla dod tos pašus skaitļus. */
  function rng(seed){
    return function(){
      seed=seed+0x6D2B79F5|0;
      var t=Math.imul(seed^seed>>>15,1|seed);
      t=t+Math.imul(t^t>>>7,61|t)^t;
      return ((t^t>>>14)>>>0)/4294967296;
    };
  }
  function int(r,a,b){return a+Math.floor(r()*(b-a+1));}
  function no(r,a){return a[Math.floor(r()*a.length)];}
  /* Skaitlis attēlošanai: īsta mīnusa zīme, ne defise. */
  function n(x){return x<0?MINUS+(-x):String(x);}
  function kv(x){return x+"<sup>2</sup>";}
  function vertibas(p){
    return p.map(function(v){return v[0]+" = "+n(v[1]);}).join(", ");
  }
  function f(s,v){return PT.f(s,v);}

  /* Viens uzdevums: q - norādījums, e - izteiksme, a - atbilde, w - tipiskās
     kļūdas; v - mērvienība, ko pieliek visām atbildēm. */
  function u(q,e,a,w,v){return {q:q,e:e,a:a,w:w,v:v||""};}

  var TESTI=[
    /* 0. Iekavas */
    [function(r){var k=int(r,2,5),a=int(r,2,6),b=int(r,2,6);
       return u(T.aprekini+": "+vertibas([["a",a],["b",b]]),k+"(a + b)",
         k*(a+b),[k*a+b,a+k*b,k+a+b,k*a*b]);},
     function(r){var k=int(r,2,6);
       return u(T.atver_iekavas,k+"(a + b)",k+"a + "+k+"b",
         [k+"a + b","a + "+k+"b",k+"ab",(k+1)+"a + "+(k+1)+"b"]);},
     function(r){var k=int(r,2,5),c=int(r,2,6);
       return u(T.atver_iekavas,k+"(x "+MINUS+" "+c+")",
         k+"x "+MINUS+" "+k*c,
         [k+"x "+MINUS+" "+c,k+"x + "+k*c,k+"x "+MINUS+" "+(k+c),
          "x "+MINUS+" "+k*c]);}],
    /* 1. Darbību secība */
    [function(r){var a=int(r,2,10),b=int(r,2,6),c=int(r,2,6);
       return u(T.aprekini,a+" + "+b+X+c,a+b*c,[(a+b)*c,a+b+c,a*b+c]);},
     function(r){var a=int(r,3,6),b=int(r,3,6),c=int(r,2,a),d=int(r,2,b-1);
       return u(T.aprekini,a+X+b+" "+MINUS+" "+c+X+d,a*b-c*d,
         [(a*b-c)*d,a*b-c+d,a*b+c*d]);},
     function(r){var a=int(r,2,6),b=int(r,2,6),c=int(r,2,4),d=int(r,1,5);
       return u(T.aprekini,"("+a+" + "+b+")"+X+c+" "+MINUS+" "+d,(a+b)*c-d,
         [a+b*c-d,a+b*c+d,(a+b)*c+d]);}],
    /* 2. Procenti */
    [function(r){var p=no(r,[10,25,50]),
         s={10:10,25:4,50:2}[p],nn=s*int(r,2,10),a=nn*p/100;
       return u(T.aprekini,f(T.no,{p:p,n:nn}),a,[nn-a,a+10,a*2]);},
     function(r){var p=no(r,[10,25,50]),
         s={10:10,25:4,50:2}[p],nn=s*int(r,2,10),d=nn*p/100;
       return u(T.aprekini,f(T.palielina,{p:p,n:nn}),nn+d,[nn+p,d,nn-d]);},
     function(r){var b=no(r,[20,40,50,100]),p,a;
       do{p=no(r,[10,20,25,50]);a=b*p/100;}while(a%1);
       return u(T.aprekini,f(T.cik_procenti,{a:a,b:b}),p,
         [100-p,b-a,Math.round(b/a)],"%");}],
    /* 3. Pakāpes */
    [function(r){var a=int(r,2,6),b=int(r,2,6);
       return u(T.aprekini+": "+vertibas([["a",a],["b",b]]),
         kv("a")+" + "+kv("b"),a*a+b*b,[(a+b)*(a+b),2*a+2*b,a*a+b]);},
     function(r){var a=int(r,2,5),b=int(r,2,4);
       return u(T.aprekini,kv("("+a+" + "+b+")"),(a+b)*(a+b),
         [a*a+b*b,2*(a+b),a*a+b*b+a*b]);},
     function(r){var k=int(r,3,7);
       return u(T.aprekini,"2<sup>"+k+"</sup>",Math.pow(2,k),
         [2*k,Math.pow(2,k-1),Math.pow(2,k+1)]);}],
    /* 4. Negatīvi skaitļi */
    [function(r){var a=int(r,2,10),b=a+int(r,1,10);
       return u(T.aprekini,a+" "+MINUS+" "+b,a-b,[b-a,-(a+b),a+b]);},
     function(r){var a=int(r,2,6),b=int(r,2,6);
       return u(T.aprekini,"("+MINUS+a+")"+X+b,-a*b,[a*b,-(a+b),b-a]);},
     function(r){var a=int(r,2,10),b=int(r,2,10);
       return u(T.aprekini,MINUS+a+" "+MINUS+" "+b,-(a+b),[b-a,a-b,a+b]);}],
    /* 5. Vienādojumi */
    [function(r){var x=int(r,2,9),a=int(r,2,5),b=int(r,1,10),c=a*x+b;
       return u(T.atrisini+": x = ?",a+"x + "+b+" = "+c,x,[c-b,x+a,c+b]);},
     function(r){var a=int(r,2,5),b=int(r,2,9);
       return u(T.atrisini+": x = ?","x : "+a+" = "+b,a*b,
         [a+b,a*b+a,a*b-b]);},
     function(r){var a=int(r,2,4),b=int(r,1,5),x=b+int(r,1,5),c=a*(x-b);
       return u(T.atrisini+": x = ?",a+"(x "+MINUS+" "+b+") = "+c,x,
         [c/a,c-b,x+1]);}],
    /* 6. Daļas */
    [function(r){var q=no(r,[2,3,4,5]),p=int(r,1,q-1),nn=q*int(r,2,8),
         a=nn/q*p;
       return u(T.aprekini,f(T.dala_no,{d:"{"+p+"|"+q+"}",n:nn}),a,
         [nn/q,nn-a,a+nn/q]);},
     function(r){var b=int(r,4,9),a=int(r,1,b-2),c=int(r,1,b-1-a);
       function d(p,q){return "{"+p+"|"+q+"}";}
       return u(T.aprekini,d(a,b)+" + "+d(c,b),d(a+c,b),
         [d(a+c,2*b),d(a*c,b),d(a+c+1,b),d(a+c,b+1)]);},
     function(r){var q=no(r,[2,4,5,10]),p=int(r,1,q-1);
       return u(T.procentos,"{"+p+"|"+q+"}",p*100/q,
         [p*10,100-p*100/q,p+q],"%");}],
    /* 7. Galvas rēķini */
    [function(r){var k=int(r,2,12);
       return u(T.aprekini,"25"+X+k,25*k,[25*k+25,25*k-25,20*k]);},
     function(r){var k=int(r,12,40);
       return u(T.aprekini,"11"+X+k,11*k,[11*k+10,11*k-10,11*k+11]);},
     function(r){var ab=int(r,12,29),c=int(r,2,5),
         bez=Math.floor(ab/10)*c*10+(ab%10*c)%10;
       return u(T.aprekini,ab+X+c,ab*c,[bez,ab*c+10,ab*c-c]);}],
    /* 8. Ģeometrija */
    [function(r){var a=int(r,2,10),b=int(r,2,6);
       return u(T.aprekini,f(T.laukums,{a:a,b:b}),a*b,
         [2*(a+b),a+b,a*b+a]," cm<sup>2</sup>");},
     function(r){var a=int(r,2,10),b=int(r,2,6);
       return u(T.aprekini,f(T.perimetrs,{a:a,b:b}),2*(a+b),
         [a*b,a+b,2*a+b]," cm");},
     function(r){var a=10*int(r,3,9),b=10*int(r,2,(170-a)/10);
       return u(T.aprekini,f(T.lenkis,{a:a,b:b}),180-a-b,
         [360-a-b,180-a,190-a-b],"°");}],
    /* 9. Burtu vietā skaitļi */
    [function(r){var a=int(r,2,6),b=int(r,2,6);
       return u(T.aprekini+": "+vertibas([["a",a],["b",b]]),"2a + 3b",
         2*a+3*b,[2*b+3*a,5*(a+b),2*a+3+b]);},
     function(r){var a=int(r,2,6),b=int(r,1,10);
       return u(T.aprekini+": "+vertibas([["a",a],["b",b]]),
         kv("a")+" "+MINUS+" b",a*a-b,[2*a-b,a*a+b,(a-b)*(a-b)]);},
     function(r){var b=int(r,1,5),a=b+int(r,1,5);
       return u(T.aprekini+": "+vertibas([["a",a],["b",b]]),
         kv("(a "+MINUS+" b)"),(a-b)*(a-b),
         [a*a-b*b,2*(a-b),a*a+b*b]);}]
  ];

  /* Trūkstošās kļūdas: tuvi skaitļi (tikai skaitliskai atbildei). */
  var TUVI=[1,-1,2,-2,3,-3,5,-5,10,-10];

  function opcijas(r,x){
    var w=[],ab=[x.a],i;
    for(i=0;i<x.w.length&&w.length<3;i++){
      if(ab.indexOf(x.w[i])<0){ab.push(x.w[i]);w.push(x.w[i]);}
    }
    for(i=0;w.length<3&&typeof x.a==="number";i++){
      var c=x.a+TUVI[i];
      if(ab.indexOf(c)<0){ab.push(c);w.push(c);}
    }
    var o=[x.a].concat(w);
    for(i=o.length-1;i>0;i--){
      var j=Math.floor(r()*(i+1)),t=o[i];o[i]=o[j];o[j]=t;
    }
    return {q:x.q,e:html(x.e),ok:o.indexOf(x.a),
      opts:o.map(function(v){
        return html(typeof v==="number"?n(v):v)+x.v;})};
  }

  /* {3|4} -> stāvā daļa (tā pati iezīme kā stundās). */
  function html(s){
    return String(s).replace(/\{([^|{}]+)\|([^|{}]+)\}/g,
      '<span class="fr"><span>$1</span><span>$2</span></span>');
  }

  /* "20261027" -> dienas numurs kopš 1970-01-01 (UTC, bez laika joslām). */
  function numurs(d){
    return Math.round(Date.UTC(+d.slice(0,4),+d.slice(4,6)-1,+d.slice(6,8))
                      /864e5);
  }

  function sodiena(){
    var t=new Date(),p=function(x){return (x<10?"0":"")+x;};
    return ""+t.getFullYear()+p(t.getMonth()+1)+p(t.getDate());
  }

  /* Dienas 3 uzdevumi. */
  function dienas(d){
    var nr=numurs(d),r=rng(nr*7919+13);
    return TESTI[nr%TESTI.length].map(function(g){return opcijas(r,g(r));});
  }

  return {dienas:dienas,sodiena:sodiena,html:html,TESTI:TESTI};
})();
"""


def js():
    return JS
