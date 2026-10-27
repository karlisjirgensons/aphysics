# -*- coding: utf-8 -*-
"""Rezultāta «lielīšanās»: virsraksts, ar kuru gribas palielīties vecākiem.

Labam rezultātam (2 vai 3 pareizi) ir liela ikona, skaļš virsraksts, ātruma
uzslava un konfeti, un tas pats virsraksts ieiet WhatsApp ziņā. Vājākam
rezultātam - mierīgs uzmundrinājums bez konfeti: lielīties nav ar ko, bet
bēdāties arī nevajag.

Šis modulis zina tikai līmeņus un svinēšanu (SRP); karti zīmē PR.karte,
ziņu raksta PD.pogas - abi ņem līmeni no šejienes (DRY).
"""

import json

# Pareizo skaits -> (ikona, teksta atslēga play_teksti.py).
LIMENI = {3: ("\U0001F3C6", "slava_3"), 2: ("\U0001F525", "slava_2"),
          1: ("\U0001F44D", "slava_1"), 0: ("\U0001F4AA", "slava_0")}

# No cik pareizajiem rezultāts ir «lielīšanās» vērts.
LABS = 2

JS = r"""
var PSL=(function(){
  var T=PT.T, LIMENI=%(limeni)s, LABS=%(labs)d;

  /* Rādītāji (PR.raditaji) -> {ikona, virsraksts, atrums, labs} */
  function limenis(m){
    var l=LIMENI[m.c],labs=m.c>=LABS;
    return {ikona:l[0],virsraksts:T[l[1]],labs:labs,
      atrums:!labs||m.atrums===null?"":
        m.atrums>=100?T.slava_atri:m.atrums>=60?T.slava_veikli:""};
  }

  function html(l){
    return '<div class="pl-slava'+(l.labs?' labs':'')+'">'+
      '<span class="pl-ikona">'+l.ikona+'</span>'+
      '<b>'+l.virsraksts+'</b>'+
      (l.atrums?'<span class="pl-atri">'+l.atrums+'</span>':'')+'</div>';
  }

  /* Konfeti pār visu ekrānu uz pāris sekundēm. */
  function konfeti(){
    if(window.matchMedia&&
       matchMedia("(prefers-reduced-motion: reduce)").matches){return;}
    var k=document.createElement("div"),
        krasas=["#4F46E5","#7C3AED","#06B6D4","#F59E0B","#10B981"];
    k.className="pl-konfeti";
    for(var i=0;i<60;i++){
      var s=document.createElement("i");
      s.style.left=Math.random()*100+"%%";
      s.style.background=krasas[i%%krasas.length];
      s.style.animationDelay=Math.random()*.6+"s";
      s.style.animationDuration=1.8+Math.random()*1.4+"s";
      s.style.transform="rotate("+Math.random()*360+"deg)";
      k.appendChild(s);
    }
    document.body.appendChild(k);
    setTimeout(function(){k.remove();},4000);
  }

  return {limenis:limenis,html:html,konfeti:konfeti};
})();
"""


def js():
    return JS % {"limeni": json.dumps({str(k): v for k, v in LIMENI.items()},
                                      ensure_ascii=False),
                 "labs": LABS}
